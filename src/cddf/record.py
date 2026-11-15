"""Evidence record: loading and validation.

The evidence record is the output of Phase 1. Its keys are those of the coding form; the fields read by
Phases 2 to 4 are validated here and the run stops with a message naming the field when one is invalid.
"""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

from .data import Data

TECHNIQUE_RE = re.compile(r"^T\d{4}(\.\d{3})?$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

TOP_SECTORS = ("government_defense", "critical_infrastructure", "finance_commerce", "ict", "private_other")
INDETERMINATE = "indeterminate"
#: effect values per type: observed, not observed, indeterminate
EFFECT_VALUES = ("post", "pre", "indeterminate")
#: intrusion state: not established, ongoing, terminated, indeterminate
INTRUSION_VALUES = ("none", "persisting", "terminated", "indeterminate")
#: armed-conflict nexus
NEXUS_VALUES = ("established", "ambiguous", "none")
#: intrusion depth: external systems, enterprise IT, mission-critical systems, operational technology
DEPTH_VALUES = ("external", "office", "core", "ot", "indeterminate")
TARGET_SPECIFICITY_VALUES = ("specific_victim", "capability_only", "compromised_infrastructure")
GRADES = (1, 2, 3, 4, 5)
#: effect types in the order of the coding form ("1", "2", "3")
EFFECT_TYPES = {"1": "exfiltration", "2": "manipulation_disclosure", "3": "disruption_destruction"}


class RecordError(ValueError):
    """The evidence record does not satisfy the record format."""


def _fail(key: str, why: str) -> None:
    raise RecordError(f"evidence record, field `{key}`: {why}")


def split_values(value) -> tuple[str, ...]:
    """A list of values, or a string with `+`, `;` or `,` separators, as a tuple of stripped values."""
    if value is None:
        return ()
    if isinstance(value, str):
        parts = re.split(r"[+;,]", value)
    else:
        parts = [p for item in value for p in split_values(item)]
    return tuple(p.strip() for p in parts if p and p.strip())


def _grade(rec: dict, key: str) -> int:
    obj = rec.get(key)
    if not isinstance(obj, dict):
        _fail(key, "must be an object with a `grade`")
    g = obj.get("grade")
    if isinstance(g, bool) or g not in GRADES:
        _fail(f"{key}.grade", f"must be an integer from 1 to 5 (found {g!r})")
    return g


def _iso_date(value, key: str) -> str:
    if not isinstance(value, str) or not DATE_RE.match(value.strip()):
        _fail(key, f"must be a date YYYY-MM-DD (found {value!r})")
    try:
        date.fromisoformat(value.strip())
    except ValueError:
        _fail(key, f"is not a calendar date ({value!r})")
    return value.strip()


def validate(rec: dict, data: Data) -> None:
    """Check every field the framework reads. Raises :class:`RecordError`."""
    for key in ("case_id", "name"):
        if not isinstance(rec.get(key), str) or not rec[key].strip():
            _fail(key, "must be a non-empty string")
    techs = rec.get("techniques")
    if not isinstance(techs, list) or not techs:
        _fail("techniques", "must be a non-empty list of ATT&CK technique identifiers")
    bad = [t for t in techs if not (isinstance(t, str) and TECHNIQUE_RE.match(t.strip()))]
    if bad:
        _fail("techniques", f"values not of the form T#### or T####.###: {bad}")

    tops = split_values(rec.get("victim_sector"))
    if not tops:
        _fail("victim_sector", "must not be empty")
    out = [v for v in tops if v not in TOP_SECTORS and v != INDETERMINATE]
    if out:
        _fail("victim_sector", f"values outside {TOP_SECTORS} and `indeterminate`: {out}")
    subs = split_values(rec.get("victim_sector_sub"))
    if not subs:
        _fail("victim_sector_sub", "must not be empty")
    out = [v for v in subs if v not in data.sector_of_sub and v != INDETERMINATE]
    if out:
        _fail("victim_sector_sub", f"values outside the 18 sectors and `indeterminate`: {out}")
    mapped = data.sector_of_sub.get(subs[0], INDETERMINATE)
    if mapped != tops[0]:
        _fail("victim_sector / victim_sector_sub",
              f"the first sub-sector {subs[0]!r} belongs to {mapped!r}, but the first sector is {tops[0]!r}")

    _grade(rec, "c_id")
    _grade(rec, "c_st")
    ref = rec["c_st"].get("reference_date")
    if ref not in (None, "") and ref != "none_stated":
        _iso_date(ref, "c_st.reference_date")

    eff = rec.get("effect_realized")
    if not isinstance(eff, dict) or eff.get("value") not in EFFECT_VALUES:
        _fail("effect_realized.value", f"must be one of {EFFECT_VALUES}")
    by_type = eff.get("by_type")
    if not isinstance(by_type, dict):
        _fail("effect_realized.by_type", "must be an object with keys \"1\", \"2\", \"3\"")
    for y in EFFECT_TYPES:
        if by_type.get(y) not in EFFECT_VALUES:
            _fail(f"effect_realized.by_type[\"{y}\"]", f"must be one of {EFFECT_VALUES} (found {by_type.get(y)!r})")
    observed = [y for y in EFFECT_TYPES if by_type[y] == "post"]
    if (eff["value"] == "post") != bool(observed):
        _fail("effect_realized", "the overall value must be `post` exactly when at least one type is `post`")

    intr = rec.get("intrusion_state")
    if not isinstance(intr, dict) or intr.get("value") not in INTRUSION_VALUES:
        _fail("intrusion_state.value", f"must be one of {INTRUSION_VALUES}")
    if rec.get("conflict_nexus") not in NEXUS_VALUES:
        _fail("conflict_nexus", f"must be one of {NEXUS_VALUES}")
    depth = rec.get("access_depth")
    if not isinstance(depth, dict) or depth.get("draft") not in DEPTH_VALUES:
        _fail("access_depth.draft", f"must be one of {DEPTH_VALUES}")
    ts = rec.get("target_specificity")
    if ts is not None and ts not in TARGET_SPECIFICITY_VALUES:
        _fail("target_specificity", f"must be one of {TARGET_SPECIFICITY_VALUES}")
    if ts == "compromised_infrastructure":
        _fail("target_specificity", "an incident whose target is compromised infrastructure has no victim to assess")
    _iso_date(rec.get("identified_date"), "identified_date")
    ex = rec.get("excluded_report_ids", [])
    if not isinstance(ex, list) or not all(isinstance(x, str) for x in ex):
        _fail("excluded_report_ids", "must be a list of ORKL report identifiers")
    assets = rec.get("victim_assets", [])
    if not isinstance(assets, list) or not all(isinstance(a, dict) and a.get("value") for a in assets):
        _fail("victim_assets", "must be a list of objects with a `value`")


def load(path: Path | str, data: Data) -> dict:
    """Read an evidence record (a JSON object, or a JSON-lines file with one record) and validate it."""
    text = Path(path).read_text(encoding="utf-8").strip()
    try:
        rec = json.loads(text)
    except json.JSONDecodeError:
        lines = [ln for ln in text.splitlines() if ln.strip()]
        if len(lines) != 1:
            raise RecordError(f"{path}: expected one JSON object") from None
        rec = json.loads(lines[0])
    if not isinstance(rec, dict):
        raise RecordError(f"{path}: expected one JSON object")
    validate(rec, data)
    return rec


def techniques(rec: dict) -> frozenset:
    return frozenset(t.strip() for t in rec["techniques"])


def sectors(rec: dict) -> tuple[str, str]:
    """First recorded sector and sub-sector (the main target)."""
    return split_values(rec["victim_sector"])[0], split_values(rec["victim_sector_sub"])[0]


def effect(rec: dict, objective: str) -> str:
    key = {v: k for k, v in EFFECT_TYPES.items()}[objective]
    return rec["effect_realized"]["by_type"][key]


def is_essential(rec: dict, data: Data) -> bool:
    """Victim sector is one of the essential-interest sectors (any recorded sub-sector counts)."""
    if rec.get("target_specificity") in ("capability_only", "compromised_infrastructure"):
        return False
    subs = [s for s in split_values(rec["victim_sector_sub"]) if s != INDETERMINATE]
    return any(s in data.essential_subsectors for s in subs)
