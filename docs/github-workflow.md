# GitHub-Workflow für die Pflege der MiHUB-Datenelemente

## 1 Repository-Setup

- **Branches:** `main` (Default + **Release**-Branch, Branch-Protection: mind. 1 Review, CI grün,
  lineare History) und `dev` (**Integrations-/Review**-Branch). Beiträge per Pull Request gegen
  **`dev`**; Freigabe in eine Release erfolgt via PR `dev` → `main`. Nicht direkt auf `main` pushen.
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

- Feature-Branches: `feat/<phase>/<element-id>`, z. B. `feat/palliative/dyspneaIntensity`; **PR gegen `dev`**.
- Conventional Commits: `feat(palliative): add dyspneaIntensity (NRS, S3-PalliativLL Empf. 9.1)`.
- Pro PR ein **kohärentes thematisches Set** (z. B. „alle Bildgebungselemente Nachsorge“) — atomare Element-PRs sind besser, aber gruppierte PRs für initiale Bulk-Erfassung akzeptabel.
- **Drei Beitrags-Wege** (Issue · Excel · YAML) — siehe [`../CONTRIBUTING.md`](../CONTRIBUTING.md); neue Kandidaten vor Aufnahme auf Dubletten prüfen (`scripts/check-duplicates.py`).

## 3 CI-Pipeline (GitHub Actions)

Aktive Workflows (`.github/workflows/`):

1. **`validate.yml`** — Schema-Validierung (`python scripts/validate.py`) **und** Catalog-Drift-Check
   (`build-catalog.py`; bricht ab, wenn `catalog/data-dictionary.csv` nicht aktuell committed ist).
2. **`skill-lint.yml`** — prüft die Agent Skills + Sub-Agenten + Symlinks + Copilot-Brücke
   (`python3 .github/scripts/validate-agent-skills.py`).
3. **`duplicate-check.yml`** — kommentiert bei neuen „data-element"-Issues mögliche Dubletten
   (`scripts/check-duplicates.py --from-issue-file`).
4. **`citation-validate.yml`** — validiert `CITATION.cff` gegen das CFF-Schema (blockierend; ein
   ungültiges CFF bricht den Zenodo-Publish still ab).
5. **`link-check.yml`** — lychee-Prüfung der Markdown-Links (intern + Attributions-/Förder-URLs;
   non-blocking, wöchentlich + bei PRs).
6. **Optional/geplant**: Markdown-Lint für `docs/*.md`; Pages-Deploy (mkdocs/Material) als Browse-Oberfläche.

> Runner: alle Workflows nutzen `ubuntu-latest`. Solange das Repo privat ist, ist GitHub-hosted
> org-weit geblockt — siehe [`../RUNNERS.md`](../RUNNERS.md) (self-hosted-Fallback; beim
> Public-Schalten auf `ubuntu-latest` zurück).

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
