# Veröffentlichungs-Checkliste (privat → öffentlich)

Dieses Repository ist derzeit **privat**. Vor dem Umschalten auf **öffentlich** sind die
folgenden Punkte zu erfüllen. Reihenfolge ist Empfehlung; **fett** = Blocker.

## 1. Recht & Datenschutz (Blocker)

- [ ] **`DISCLAIMER.md` durch TU-Dresden-Justiziariat + DPO freigegeben.** Datei ist aktuell
      als **DRAFT** gekennzeichnet (Zweckbestimmung, „kein Medizinprodukt"/MDR, Haftung). Erst
      nach Sign-off den DRAFT-Banner entfernen.
- [ ] **Keine personenbezogenen / realen Patientendaten** im Repo oder in der Historie
      (`git log -p | grep -i …`). Die Datenelemente sind abstrakte Definitionen — das ist konform.
- [ ] Keine Secrets/Tokens in Historie (`git log`, ggf. gitleaks).
- [ ] BMFTR/BMBF-vertrauliche Antragsdetails nicht enthalten.

## 2. Lizenzierung

- [ ] `LICENSE` (CC BY 4.0, Inhalte) vorhanden → GitHub erkennt die Lizenz (Repo-Sidebar).
- [ ] `LICENSE-APACHE-2.0.txt` (Skripte) vorhanden; Skripte tragen `SPDX-License-Identifier: Apache-2.0`.
- [ ] README-Abschnitt „Lizenz" beschreibt den Split (Inhalte CC BY 4.0 / Skripte Apache 2.0).

## 3. Zitierbarkeit

- [ ] `CITATION.cff` vorhanden und valide (`cffconvert --validate`); Autor:innen/ORCIDs korrekt.
- [ ] **Zenodo aktiviert** und erste Release archiviert; **Concept-DOI** in `CITATION.cff`
      (`doi:`) und als README-Badge eingetragen (analog Pathway-Repo).

## 4. Community-Health & Discovery

- [ ] `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `.github/ISSUE_TEMPLATE/`, `PULL_REQUEST_TEMPLATE.md` vorhanden.
- [ ] `README.md`: alle `<repo-name>`-Platzhalter durch `mihub-lung-cancer-pathway-data-elements`
      ersetzt; Disclaimer-/Lizenz-/Zitier-Verweise auflösbar.
- [ ] Repo-Beschreibung + **Topics** gesetzt (`ai-assisted`, `fhir`, `oncology`, `lung-cancer`,
      `clinical-information-model`, `iso-13972`, `mihub`).
- [ ] `AI_USAGE.md` aktuell (EU AI Act Art. 50): eingesetzte Modelle, neue Skills/Skripte erfasst.

## 5. Governance & CI

- [ ] **Branches:** `main` = Release, `dev` = Integration; Default-Branch bleibt `main`.
- [ ] Branch-Protection auf `main` (PRs erforderlich, CI grün) — soweit gewünscht.
- [ ] `.github/CODEOWNERS`-Teams existieren in der Organisation (`@mihub-ap8/*`).
- [ ] CI grün: `validate.yml` (Schema + Catalog-Drift), `skill-lint.yml`, `duplicate-check.yml`.

## 6. Inhaltlicher Reifegrad (Hinweis, kein Blocker)

- [ ] Datenelemente bleiben `AuthorDraft` bis zum klinischen Review — im README/DISCLAIMER klar
      kommuniziert. Eine Veröffentlichung als **Entwurf** ist zulässig und transparent gekennzeichnet.

## 7. Release-Automatisierung (release-please) — einrichten

Analog zum Schwester-Repo [`mihub-lung-cancer-pathway`](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway)
einrichten, damit Releases + der Zenodo-DOI (siehe §3) reproduzierbar aus Conventional Commits
entstehen (`feat`/`fix`/… → automatische Version + Changelog + Tag):

- [ ] `release-please-config.json` + `.release-please-manifest.json` anlegen (Release-Type `simple`;
      `version.txt`, `CITATION.cff` (`version`/`date-released`) und den README-Versions-/DOI-Badge als
      `extra-files` mitpflegen lassen).
- [ ] Workflow `.github/workflows/release-please.yml` (googleapis/release-please-action): Release-PRs
      gegen **`main`** (Release-Branch); Entwicklung läuft auf `dev`. ⚠ GitHub-hosted Actions sind
      org-seitig geblockt → denselben Runner wie die übrige CI verwenden (ggf. self-hosted, vgl.
      `validate.yml`/`skill-lint.yml`).
- [ ] SemVer an die Element-Reife koppeln: `v0.x` (AuthorDraft/CommitteeDraft) → `v1.0`
      (ApprovedForProductionUse); vgl. `docs/github-workflow.md` §4.
- [ ] RCs/konkrete Versionen über einen **`Release-As:`-COMMIT-FOOTER** schneiden — **nicht**
      `release-as` in der Config pinnen (sticky Pin → Duplicate-Tag-Loop; Lehre aus dem Pathway-Repo).
- [ ] Zenodo-GitHub-Integration aktivieren, sodass jedes von release-please erzeugte Tag archiviert
      wird → resultierenden **Concept-DOI** in `CITATION.cff` und README-Badge eintragen (schließt §3).

---

Nach Abschluss: Repo-Sichtbarkeit umstellen (Settings → Danger Zone → Change visibility) bzw.
`gh repo edit forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements --visibility public`.
