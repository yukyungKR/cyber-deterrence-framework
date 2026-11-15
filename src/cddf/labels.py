"""Objective labels of a EuRepoC incident, assigned by rule from the fields `incident_type` and `mitre_impact`.

The two fields are read as `;`-separated values; repeated values and missing markers are ignored. The labels are
the union of the labels of all values. `Hijacking with Misuse` is a means, not an effect, and gives no label.
An incident with no label is `label_absent` (EuRepoC records no effect) and is not graded.
"""
from __future__ import annotations

import csv
from pathlib import Path

EXFILTRATION, MANIPULATION, DISRUPTION, DORMANCY = ("exfiltration", "manipulation_disclosure",
                                                     "disruption_destruction", "dormancy")

INCIDENT_TYPE_MAP = {
    "Data theft": {EXFILTRATION},
    "Data theft & Doxing": {EXFILTRATION, MANIPULATION},
    "Disruption": {DISRUPTION},
    "Ransomware": {DISRUPTION},
    "Hijacking without Misuse": {DORMANCY},
}
MITRE_IMPACT_MAP = {
    "Data Exfiltration": {EXFILTRATION},
    "Defacement": {MANIPULATION},
    "Data Manipulation": {MANIPULATION},
    "Network Denial of Service": {DISRUPTION},
    "Data Encrypted for Impact": {DISRUPTION},
    "Endpoint Denial of Service": {DISRUPTION},
    "Data Destruction": {DISRUPTION},
    "Disk Wipe": {DISRUPTION},
    "Service Stop": {DISRUPTION},
    "System Shutdown/Reboot": {DISRUPTION},
    "Account Access Removal": {DISRUPTION},
    "Firmware Corruption": {DISRUPTION},
    "Resource Hijacking": {EXFILTRATION},
}
HIJACKING_WITH_MISUSE = "Hijacking with Misuse"
MISSING = {"Not available", "Not applicable", "Unknown", ""}


def _atoms(raw: str) -> list[str]:
    out, seen = [], set()
    for a in (raw or "").split(";"):
        a = a.strip()
        if a and a not in MISSING and a not in seen:
            seen.add(a)
            out.append(a)
    return out


def labels_of(incident_type: str, mitre_impact: str) -> set[str]:
    """All labels, including dormancy. The three objective types estimated in Phase 2 exclude dormancy."""
    labels: set[str] = set()
    for a in _atoms(incident_type):
        if a != HIJACKING_WITH_MISUSE:
            labels |= INCIDENT_TYPE_MAP.get(a, set())
    for a in _atoms(mitre_impact):
        labels |= MITRE_IMPACT_MAP.get(a, set())
    return labels


def eurepoc_labels(csv_path: Path | str, incident_ids) -> dict[str, set[str]]:
    """Labels of the given incidents from the EuRepoC Global Dataset CSV (one row per incident and receiver)."""
    wanted = {str(i) for i in incident_ids}
    out: dict[str, set[str]] = {}
    with open(csv_path, encoding="utf-8", errors="replace", newline="") as f:
        for row in csv.DictReader(f):
            low = {(k or "").strip().lower(): (v or "").strip() for k, v in row.items()}
            iid = low.get("incident_id")
            if iid in wanted:   # the last row of an incident is kept, as in the original reader
                out[iid] = labels_of(low.get("incident_type", ""), low.get("mitre_impact", ""))
    missing = wanted - set(out)
    if missing:
        raise KeyError(f"incidents not found in {csv_path}: {sorted(missing)[:5]}")
    return out
