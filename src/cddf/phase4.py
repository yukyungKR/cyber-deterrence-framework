"""Phase 4: reference to the public responses recorded for the precedents selected in Phase 2."""
from __future__ import annotations

from .data import Data

RESPONSE_TYPES = {"political": "number_political_responses", "legal": "number_legal_responses"}
MISSING = {"not available", "na"}


def is_missing(value: str) -> bool:
    """EuRepoC missing-value markers, also when repeated with ';' separators."""
    parts = {p.strip().lower() for p in (value or "").split(";")} - {""}
    return not parts or parts <= MISSING


def _count(raw: str) -> int | None:
    raw = (raw or "").strip()
    return int(raw) if raw.isdigit() else None


def run(neighbours: list[dict], data: Data) -> dict:
    cols = data.response_columns
    out = []
    for n in neighbours:
        row = data.responses.get(n["eurepoc_id"])
        if row is None:
            out.append({"eurepoc_id": n["eurepoc_id"], "found": False, "no_record_found": True})
            continue
        entry = {"eurepoc_id": n["eurepoc_id"], "incident_name": n["incident_name"], "found": True,
                 "initiator_name": row["initiator_name"], "receiver_country": row["receiver_country"]}
        has = {}
        for typ, ccol in RESPONSE_TYPES.items():
            count = _count(row[ccol])
            fields = {c[len(f"{typ}_response_"):]: (None if is_missing(row[c]) else row[c])
                      for c in cols if c.startswith(f"{typ}_response_")}
            # the count column decides; a non-integer count falls back to the presence of recorded values
            has[typ] = count > 0 if count is not None else any(v is not None for v in fields.values())
            entry[typ] = {"count": count, "count_raw": row[ccol], "has_response": has[typ],
                          "record": fields if has[typ] else None}
        entry["no_record_found"] = not any(has.values())
        out.append(entry)
    k = len(out)
    with_pol = sum(1 for e in out if e.get("political", {}).get("has_response"))
    with_leg = sum(1 for e in out if e.get("legal", {}).get("has_response"))
    with_any = sum(1 for e in out if not e["no_record_found"])
    return {"source": "EuRepoC Global Dataset v1.3, political and legal response columns",
            "neighbours": out,
            "proportions": {"political": {"n": with_pol, "of": k, "share": with_pol / k},
                            "legal": {"n": with_leg, "of": k, "share": with_leg / k},
                            "any": {"n": with_any, "of": k, "share": with_any / k}}}
