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
- [ ] CI grün: `validate.yml` (Schema + Catalog-Drift), `skill-lint.yml`, `duplicate-check.yml`,
      `citation-validate.yml`, `link-check.yml`.
- [ ] **CI-Runner geklärt** ([`RUNNERS.md`](../RUNNERS.md)): solange privat ist GitHub-hosted org-weit
      geblockt → self-hosted Runner *oder* lokal verifizieren; **beim Public-Schalten auf
      `ubuntu-latest` (kostenlos + sandboxed) zurück** und self-hosted Runner entfernen.

## 6. Inhaltlicher Reifegrad (Hinweis, kein Blocker)

- [ ] Datenelemente bleiben `AuthorDraft` bis zum klinischen Review — im README/DISCLAIMER klar
      kommuniziert. Eine Veröffentlichung als **Entwurf** ist zulässig und transparent gekennzeichnet.

## 7. Release-Automatisierung (release-please) — eingerichtet ✅ (offen: Zenodo)

Mirror des Schwester-Repos [`mihub-lung-cancer-pathway`](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway):
Releases entstehen reproduzierbar aus Conventional Commits (`feat`/`fix`/… → Version + CHANGELOG + Tag).

- [x] `release-please-config.json` + `.release-please-manifest.json` + `version.txt` (Release-Type
      `simple`, `prerelease: true`, `bump-minor-pre-major`). *Hinweis:* `version.txt` ist die
      Versionsquelle; `CITATION.cff` (`version`/`date-released`) + README-DOI-Badge werden vorerst
      **manuell in der Release-PR** mitgepflegt (kein `extra-files`-Automatismus, analog Pathway-Repo).
- [x] Workflow `.github/workflows/release-please.yml` (googleapis/release-please-action; Release-PRs
      gegen **`main`**, Entwicklung auf `dev`). ⚠ `ubuntu-latest` ist im privaten Zustand geblockt
      (siehe [`../RUNNERS.md`](../RUNNERS.md)); greift erst, wenn Commits `main` erreichen (dev→main).
- [x] SemVer an die Element-Reife gekoppelt: `v0.x` (AuthorDraft/CommitteeDraft) → `v1.0`
      (ApprovedForProductionUse); siehe `docs/github-workflow.md` §4.
- [x] Konvention dokumentiert: RCs/konkrete Versionen über einen **`Release-As:`-COMMIT-FOOTER** auf
      `main` — **nicht** `release-as` in der Config pinnen (sticky Pin → Duplicate-Tag-Loop).
- [ ] **Zenodo-GitHub-Integration aktivieren** (offen): jedes erzeugte Tag archivieren →
      resultierenden **Concept-DOI** in `CITATION.cff` und README-Badge eintragen (schließt §3).

---

Nach Abschluss: Repo-Sichtbarkeit umstellen (Settings → Danger Zone → Change visibility) bzw.
`gh repo edit forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements --visibility public`.
