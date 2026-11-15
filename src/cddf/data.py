"""Loading of the derived data tables in ``data/``."""
from __future__ import annotations

import csv
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path

DEFAULT_DATA_DIR = Path(__file__).resolve().parents[2] / "data"

#: Objective types estimated in Phase 2 (column suffixes of incidents.csv).
OBJECTIVES = ("exfiltration", "manipulation_disclosure", "disruption_destruction")


def _split(value: str) -> tuple[str, ...]:
    return tuple(v for v in (value or "").split(";") if v)


def _rows(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


@dataclass(frozen=True)
class Incident:
    eurepoc_id: str
    split: str
    name: str
    actor: str
    reports: tuple[str, ...]
    techniques: frozenset
    sector: str
    sector_sub: str
    assets: tuple[str, ...]
    objectives: frozenset
    dormancy: bool
    start_date: str


@dataclass(frozen=True)
class Eligibility:
    n_reports_dated: int
    n_reports_undated: int
    earliest_report_date: str | None
    start_date: str | None


class Data:
    """All tables used by the framework, read once from ``data_dir``."""

    def __init__(self, data_dir: Path | str | None = None):
        self.dir = Path(data_dir) if data_dir else DEFAULT_DATA_DIR
        if not (self.dir / "incidents.csv").exists():
            raise FileNotFoundError(f"incidents.csv not found in {self.dir}")

    # -- incident dataset -------------------------------------------------------
    @cached_property
    def incidents(self) -> list[Incident]:
        out = []
        for r in _rows(self.dir / "incidents.csv"):
            out.append(Incident(
                eurepoc_id=r["eurepoc_id"], split=r["split"], name=r["incident_name"], actor=r["actor"],
                reports=_split(r["orkl_report_ids"]), techniques=frozenset(_split(r["techniques"])),
                sector=r["sector"], sector_sub=r["sector_sub"], assets=_split(r["victim_assets"]),
                objectives=frozenset(o for o in OBJECTIVES if r[f"label_{o}"] == "1"),
                dormancy=r["label_dormancy"] == "1", start_date=r["start_date"]))
        return out

    def training_incidents(self) -> list[Incident]:
        return [i for i in self.incidents if i.split == "train"]

    @cached_property
    def eligibility(self) -> dict[str, Eligibility]:
        return {r["eurepoc_id"]: Eligibility(int(r["n_reports_dated"]), int(r["n_reports_undated"]),
                                             r["earliest_report_date"] or None, r["start_date"] or None)
                for r in _rows(self.dir / "precedent_eligibility.csv")}

    @cached_property
    def responses(self) -> dict[str, dict]:
        return {r["eurepoc_id"]: r for r in _rows(self.dir / "eurepoc_responses.csv")}

    @cached_property
    def response_columns(self) -> list[str]:
        with (self.dir / "eurepoc_responses.csv").open(encoding="utf-8", newline="") as f:
            header = next(csv.reader(f))
        return [h for h in header if h.startswith(("political_response", "legal_response"))]

    # -- vocabularies and legal tables ------------------------------------------------
    @cached_property
    def sector_of_sub(self) -> dict[str, str]:
        return {r["sector_sub"]: r["sector"] for r in _rows(self.dir / "sectors.csv")}

    @cached_property
    def essential_subsectors(self) -> frozenset:
        return frozenset(r["sector_sub"] for r in _rows(self.dir / "sectors.csv") if r["essential_interest"] == "1")

    @cached_property
    def measures(self) -> list[dict]:
        out = []
        for r in _rows(self.dir / "measures.csv"):
            r = dict(r)
            r["measure_id"] = int(r["measure_id"])
            r["required_grade"] = int(r["required_grade"]) if r["required_grade"] else None
            out.append(r)
        return out

    @cached_property
    def state_positions(self) -> dict[str, dict]:
        return {r["state"]: r for r in _rows(self.dir / "state_positions.csv")}

    # -- D3FEND --------------------------------------------------------------------------
    @cached_property
    def d3fend_attack_ids(self) -> frozenset:
        return frozenset(r["attack_id"] for r in _rows(self.dir / "d3fend" / "attack_ids.csv"))

    @cached_property
    def d3fend_artifacts(self) -> dict[str, list[dict]]:
        out: dict[str, list[dict]] = {}
        for r in _rows(self.dir / "d3fend" / "attack_artifacts.csv"):
            out.setdefault(r["attack_id"], []).append(r)
        return out

    @cached_property
    def d3fend_defences(self) -> dict[str, list[dict]]:
        out: dict[str, list[dict]] = {}
        for r in _rows(self.dir / "d3fend" / "artifact_defences.csv"):
            out.setdefault(r["artifact"], []).append(r)
        return out
