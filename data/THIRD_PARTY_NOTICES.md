# Third-party notices for the data in this folder

The files in `data/` are derived data. They contain no text of the CTI reports.

## European Repository of Cyber Incidents (EuRepoC)

`incidents.csv` (incident names, start dates, victim sectors and objective labels derived from EuRepoC fields) and
`eurepoc_responses.csv` (the political and legal response columns of the training incidents) are derived from the
EuRepoC Global Dataset v1.3, DOI 10.5281/zenodo.14965395, licensed under the Creative Commons
Attribution-NonCommercial 4.0 International licence (CC BY-NC 4.0). The values were transformed as described in
`README.md` (sector mapping, objective labels, date format). EuRepoC does not endorse this work.

## ORKL

`incidents.csv` lists the identifiers of the ORKL reports linked to each incident, and the technique sets extracted
from those reports. `precedent_eligibility.csv` holds the earliest publication date found for the linked reports.
No report text is included. The reports themselves are available from ORKL (https://orkl.eu).

## MITRE ATT&CK

Technique identifiers in `incidents.csv`, in the evidence records and in `d3fend/` are MITRE ATT&CK identifiers.
© The MITRE Corporation. This work is reproduced and distributed with the permission of The MITRE Corporation.
ATT&CK® is a registered trademark of The MITRE Corporation. See https://attack.mitre.org/resources/legal-and-branding/terms-of-use/.

## MITRE D3FEND

The tables in `d3fend/` (relations from ATT&CK techniques to digital artefacts and from artefacts to defensive
techniques and tactics, with their labels and identifiers) are derived from the MITRE D3FEND ontology, version
1.6.0, which states the MIT licence. © The MITRE Corporation. D3FEND™ is a trademark of The MITRE Corporation.
See https://d3fend.mitre.org.

The victim-asset identifiers in `incidents.csv` are D3FEND class identifiers (`d3f:...`) and MITRE ATT&CK for ICS
asset identifiers (`A0001` ...).
