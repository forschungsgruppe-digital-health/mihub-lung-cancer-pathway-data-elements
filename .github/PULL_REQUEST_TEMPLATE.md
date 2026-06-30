# Datenelement-Änderung

> Ziel-Branch: **`dev`** (nicht `main`). `main` ist die Release-Branch.

## Beitrags-Weg

- [ ] 🟢 GitHub-Issue-Formular (Klinik-Spur) — Issue-Referenz: #
- [ ] 🟡 Excel-Vorlage (Klinik-Spur) — importiert via `import-elicitation-workbook.py`
- [ ] 🔵 YAML direkt (MI-Spur)

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
- [ ] `python scripts/check-duplicates.py` ausgeführt — keine ungelöste DUBLETTE/NAH-DUBLETTE
- [ ] LL-Referenz in `evidence.guideline_references[]` mit Section + Empfehlungsgrad/Evidenzlevel
- [ ] Datennutzung erfasst, sofern bekannt (`care_process.data_flows[]` — WO/WER/WIE)
- [ ] `iso13972_metadata.version_number` ggf. erhöht (SemVer)
- [ ] Klinische:r Reviewer:in markiert (CODEOWNERS)
- [ ] Bei Statuswechsel: `next_revision_date` gesetzt
- [ ] Bei sensitiven Inhalten (z. B. Todeswunsch, Sterbephase): Hinweis in `issues[]`

## KI-Nutzung (EU AI Act Art. 50 — siehe [`AI_USAGE.md`](../AI_USAGE.md))

- [ ] Diese Änderung ist KI-assistiert. Werkzeug/Modell: ______________ (sonst leer lassen)
