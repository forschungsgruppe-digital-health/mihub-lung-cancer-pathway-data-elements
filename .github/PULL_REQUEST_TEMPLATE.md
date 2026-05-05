# Datenelement-Änderung

## Betroffene Element-IDs

- `mihub.lung.<phase>.<element>.v<x>.<y>`

## Art der Änderung

- [ ] Neues Element
- [ ] Inhaltliche Anpassung (Definition, ValueSet, Codings, FHIR-Mapping)
- [ ] Statuswechsel (`publication_status`)
- [ ] Versions-Bump (`version_number`)
- [ ] Sonstiges (Doku, Tooling): __

## Klinische / methodische Begründung

<!-- Quelle (S3-LL, Onkopedia, OCP, AG LONKO ...), Kapitel/Empfehlung/Tabelle, Evidenzgrad -->

## Checkliste

- [ ] `python scripts/validate.py` lokal grün
- [ ] `python scripts/build-catalog.py` ausgeführt; CSV committed
- [ ] LL-Referenz in `evidence.guideline_references[]` mit Section + Empfehlungsgrad/Evidenzlevel
- [ ] `iso13972_metadata.version_number` ggf. erhöht (SemVer)
- [ ] Klinische:r Reviewer:in markiert (CODEOWNERS)
- [ ] Bei Statuswechsel: `next_revision_date` gesetzt
- [ ] Bei sensitiven Inhalten (z. B. Todeswunsch, Sterbephase): Hinweis in `issues[]`
