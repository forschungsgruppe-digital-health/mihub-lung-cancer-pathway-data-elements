# GitHub-Workflow für die Pflege der MiHUB-Datenelemente

## 1 Repository-Setup

- **Default-Branch** `main` mit Branch-Protection (mindestens 1 Review, CI grün, lineare History).
- **CODEOWNERS** je Phase (klinisch-fachliche Reviewer:innen):
  ```
  /elements/follow-up/      @<lead-onko>
  /elements/surveillance/   @<lead-onko>
  /elements/palliative/     @<lead-pall>
  /schemas/                 @<lead-mi>
  ```
- **Issue-Templates** mit Pflichtfeldern: betroffene Element-ID(s), Quellen-LL-Referenz, Begründung.
- **PR-Template**: Checkliste (Schema valid, CSV neu generiert, LL-Referenz angegeben, Klinik-Reviewer markiert).

## 2 Branching-/Commit-Konvention

- Feature-Branches: `feat/<phase>/<element-id>`, z. B. `feat/palliative/dyspneaIntensity`.
- Conventional Commits: `feat(palliative): add dyspneaIntensity (NRS, S3-PalliativLL Empf. 9.1)`.
- Pro PR ein **kohärentes thematisches Set** (z. B. „alle Bildgebungselemente Nachsorge“) — atomare Element-PRs sind besser, aber gruppierte PRs für initiale Bulk-Erfassung akzeptabel.

## 3 CI-Pipeline (GitHub Actions)

Schritte:

1. **Schema-Validierung**: `python scripts/validate.py elements/**/*.yaml`
2. **ID-Eindeutigkeit**: `python scripts/check-ids.py`
3. **Catalog-Build**: `python scripts/build-catalog.py` → `catalog/data-dictionary.csv` (committed via PR-Bot oder als Pflicht-Schritt im PR).
4. **Markdown-Lint** für `docs/*.md`.
5. **Optional**: Pages-Deploy einer statischen Website (mkdocs/Material) als Browse-Oberfläche.

## 4 Releases

- SemVer-Tags je Reife-Iteration: `v0.x.y` (Author/Committee Draft), `v1.0.0` (erste freigegebene Fassung), Folgeversionen für additive Phasen-Erweiterungen.
- **Zenodo-Hook**: jedes Tag erzeugt eine zitierbare DOI.
- `iso13972_metadata.publication_status` der einzelnen Elemente synchronisiert mit Release-Stage:
  - `AuthorDraft` (offene Bearbeitung)
  - `CommitteeDraft` (Konsultation)
  - `ApprovedForTesting` (Pilotierung)
  - `ApprovedForProductionUse` (Produktivnutzung)

## 5 Pflege-Lebenszyklus pro Element

```
AuthorDraft  ──►  CommitteeDraft  ──►  ApprovedForTesting  ──►  ApprovedForProductionUse
                                                              │
                                                              ▼
                                                         Superseded ◄── neue Version
                                                         Withdrawn / Rejected
```

Statuswechsel **immer** als Diff im YAML (`publication_status`, `next_revision_date`, `superseded_by`/`supersedes` über `related_elements`).

## 6 Mehrsprachigkeit & Lokalisation

- Inhalte in Deutsch (`label_de`, `definition_de`, `instruction_de`).
- Englisch optional (`label_en`).
- Sprache(n) explizit in `iso13972_metadata.language` (ISO 639).

## 7 Externe Anbindung

- **FHIR Implementation Guide-Generierung**: Aus den YAMLs werden in einer nachgelagerten Iteration StructureDefinitions / ValueSets erzeugt (`fhir-mii-kds`, `mcode`, `kbv-mio`).
- **oBDS-Mapping**: Strukturierte Tumorhistorie wird in den oBDS-Pflichtmeldungspfad gekoppelt (`obds`).
- **gematik ePA / KBV MIO**: Übergaben Onko ↔ Hausarzt nutzen die `kbv-mio`- bzw. `gematik-epa-fhir`-Mappings.
- **Versorgungsforschung**: SNOMED-CT-Implicit-ValueSets, OMOP-CDM-Brücke (mCODE↔OMOP) und FDPG-Anbindung folgen schrittweise.
