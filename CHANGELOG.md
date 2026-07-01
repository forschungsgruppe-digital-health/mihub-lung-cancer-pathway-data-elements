# Changelog

All notable changes to this repository are documented here. Versions follow SemVer; this is a
**prerelease (release candidate)**. Detailed per-element provenance lives in
[`docs/audit-log.md`](docs/audit-log.md).

## [0.1.0-rc.2](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements/compare/v0.1.0-rc.1...v0.1.0-rc.2) (2026-07-01)


### Documentation & governance

* **citation:** add co-authors Gräfe, Voigt, Klein (ORCIDs) ([e34c23c](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements/commit/e34c23cda999965d08eca33f0f19efb6d0cbc0d2))
* **citation:** add co-authors Gräfe, Voigt, Klein (with ORCIDs) ([651f8c9](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements/commit/651f8c91f66b6971af0447f983784dc15d72701e))


### Tooling & maintenance

* release 0.1.0-rc.2 ([d10813a](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements/commit/d10813a2238ff8b71d9121301ddc7cdbef4a73e4))

## [0.1.0-rc.1] - 2026-06-30

First **release candidate** of the lung-cancer data-element catalog — a content-side supplement to
the BPMN pathway repo `mihub-lung-cancer-pathway` (AP3). **Author Draft — not clinically validated;
[`DISCLAIMER.md`](DISCLAIMER.md) is pending TU Dresden legal/DPO sign-off.** Published for citation
and review, not for clinical use.

### Data elements & schema
- 51 data elements across **follow-up (18), surveillance (15), palliative (18)**.
- ISO 13972:2022 / ISO 13606-2 JSON schema, incl. `care_process.data_flows[]` (system · role · usage).
- Generated data dictionary (`catalog/data-dictionary.csv` + `.md`, 24 columns) and phase overview.

### Tooling (reproduce extraction & use)
- `scripts/validate.py`, `scripts/build-catalog.py`, `scripts/build-fhir-logical-models.py`.
- Excel elicitation workbook + importer (`scripts/build-/import-elicitation-workbook.py`,
  `templates/datenelement-erhebung.xlsx`) with terminology dropdowns + ignored example row.
- Duplicate/similarity checker (`scripts/check-duplicates.py`).

### Documentation & governance
- README, methodology, how-to, glossary; CONTRIBUTING (three contribution paths).
- LICENSE (CC BY 4.0, content) + Apache-2.0 (scripts); DISCLAIMER (DRAFT); CITATION; CODE_OF_CONDUCT;
  AI_USAGE (EU AI Act Art. 50 transparency).
- Vendor-neutral Agent Skills (`skills/`); CI (schema/catalog/skill-lint/citation/link-check).

[0.1.0-rc.1]: https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements/releases/tag/v0.1.0-rc.1
