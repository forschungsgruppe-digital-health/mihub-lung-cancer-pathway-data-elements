# Mitwirken am MiHUB-Patientenpfad-Datenelement-Repository

Vielen Dank für Ihr Interesse, das Datenelement-Repository mit Ihrer klinischen oder methodischen Expertise zu erweitern.

## Zwei Spuren

Es gibt **zwei abgestimmte Beitrags-Spuren** — wählen Sie die zu Ihrer Rolle passende:

### 🩺 Klinik-Spur (niederschwellig, ohne Git/YAML)

Sie kennen die klinische Domäne, wollen aber nicht mit YAML/Git arbeiten:

→ Nutzen Sie das Web-Formular **„📋 Neues Datenelement vorschlagen"** unter [Issues → New Issue](../../issues/new/choose).
Das MI-Team übernimmt die technische Umsetzung und bittet Sie am Ende, den Pull Request inhaltlich zu bestätigen.

### 🛠 MI-Spur (vollständig, YAML + Git + PR)

Sie sind Medizininformatiker:in oder hinreichend technisch:

→ Folgen Sie der ausführlichen Anleitung in [`docs/howto-add-element.md`](docs/howto-add-element.md).

## Allgemeine Regeln

- Pro Pull Request möglichst **ein** Datenelement (atomare Reviews).
- Jedes Element braucht **mindestens eine Leitlinien-/Quellen-Referenz** (`evidence.guideline_references`).
- Alle Pflichtfelder (CSV mit `*` markiert) müssen befüllt sein, bevor der PR gemergt wird.
- Statuswechsel (`AuthorDraft → CommitteeDraft → ApprovedForProductionUse`) erfolgen je Element einzeln.
- Versions-Bumps folgen SemVer (siehe `docs/howto-add-element.md` §C).

## Verhaltenskodex

Beiträge erfolgen unter Lizenz **CC-BY-4.0** (Inhalte) bzw. **Apache-2.0** (Skripte). Sensible klinische Sachverhalte (z. B. Todeswunsch, Sterbephase, Suizidalität) werden mit besonderer Sorgfalt diskutiert; Reviewer:innen behandeln solche Issues vertraulich, wenn nicht anders vereinbart.

## Bei Fragen

→ Issue „❓ Frage" oder Direktkontakt MI-Lead via CODEOWNERS.
