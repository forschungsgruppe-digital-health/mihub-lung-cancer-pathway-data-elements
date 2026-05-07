# AI Usage Disclosure

> **Vorlage gemäß:**
> - EU AI Act, Art. 50 (Verordnung (EU) 2024/1689)
> - EU Code of Practice on Transparency of AI-Generated Content (Draft, 2026)
> - COPE: Authorship and AI Tools (2024)
> - ICMJE Recommendations
> - Linux Kernel AI Policy (2025)
> - Red Hat OSS AI Policy (2025)
>
> Pflichtfelder gemäß Art. 50 EU AI Act sind mit `[EU AI Act §]` markiert.
> COPE-relevante Felder (für zugehörige Publikationen) mit `[COPE]`.
> Empfohlene Felder (Community Standard) mit `[CS]`.

> ℹ️ **Pflege-Hinweis:** Diese Datei ist die zentrale, repository-weite KI-Nutzungs-Disklosure
> und verweist auf das fortlaufende [`docs/audit-log.md`](docs/audit-log.md) als operative
> Evidenz menschlicher Aufsicht (siehe §4 + §10). Aktualisierung erfolgt durch den
> [`ai-usage-curator`](.claude/agents/ai-usage-curator.md)-Sub-Agenten bei werkzeug-/governance-bezogenen
> Trigger-Ereignissen — siehe [`AGENTS.md`](AGENTS.md). Bei wesentlichen Änderungen ist die
> Datei zeitnah zu aktualisieren (siehe Changelog §9).

## 1. Überblick

> **Zweck dieser Datei:** Sie dokumentiert Art, Umfang und Verantwortlichkeit der KI-Nutzung
> in diesem Repository. Sie richtet sich an Beitragende, Reviewer und Dritte, die die
> Entstehung von Artefakten nachvollziehen möchten. Die Struktur folgt den Transparenzpflichten
> des EU AI Act (Art. 50, Verordnung (EU) 2024/1689) sowie einschlägigen Community-Standards.
> Die Datei ist bei wesentlichen Änderungen im KI-Einsatz zu aktualisieren.

**Verantwortliche Person (Human Oversight):** Marcel Susky, Forschungsgruppe Digital Health (FGDH), Technische Universität Dresden — `marcel.susky@tu-dresden.de`
**Letzte Aktualisierung:** 2026-05-06
**Geltungsbereich:** Repository `data-elements/` — Erhebung, Strukturierung und Pflege der klinischen Datenelemente entlang der Lungenkrebs-Patient Journey im Rahmen von MiHUB (AP6/AP7/AP8 in Bezug auf AP3). Alle Branches.

---

## 2. Nutzungsübersicht [EU AI Act §50 Abs. 2 | CS]

> **Normative Grundlage:** Art. 50 Abs. 2 EU AI Act verlangt, dass KI-generierte Outputs
> maschinenlesbar markiert und als künstlich erzeugt erkennbar sind. Diese Tabelle dient
> der strukturierten, menschenlesbaren Entsprechung. Die maschinenlesbare Markierung
> erfolgt zusätzlich via Commit-Trailer (Abschnitt 5) und/oder Datei-Metadaten.

| Artefakttyp | KI-Einsatz | Werkzeug / Modell | Scope | Menschliche Überprüfung |
|---|---|---|---|---|
| **YAML-Datenelemente** (`elements/<phase>/*.yaml`) | Generated | Anthropic Claude (Sonnet 4.5 / Sonnet 4.6 / Opus 4.7) | Vollständige initiale Erstellung auf Basis bereitgestellter klinischer Leitlinien, Onkopedia-Stände und Fachpublikationen | Stichprobenartige Quellen-Verifikation gegen Primärbelege (siehe `docs/audit-log.md`); **klinisches Review durch Domänenexpert:innen ausstehend** (publication_status: AuthorDraft) |
| **JSON-Schema** (`schemas/data-element.schema.json`) | Assisted | Anthropic Claude (Sonnet 4.5) | Schema-Design auf Basis ISO 13972/13606-Mustern; iterative Verfeinerung | Vollständig durch Repository-Maintainer geprüft; CI-validiert |
| **Markdown-Dokumentation** (README, AGENTS, CONTRIBUTING, methodology, howto, GLOSSARY u. a.) | Assisted | Anthropic Claude (Sonnet 4.5 / 4.6 / Opus 4.7) | Strukturierung, Formulierung, Synthese aus Antrag/Leitlinien/Standards | Inhaltlich durch Repository-Maintainer geprüft und freigegeben |
| **Sub-Agent-Spezifikationen** (`.claude/agents/*.md`, `AGENTS.md`) | Assisted | Anthropic Claude (Sonnet 4.5 / Opus 4.7) | Entwurf der System-Prompts; Workflow-Regeln; Separation-of-Concerns-Architektur | Durch Repository-Maintainer entworfen und auf Konsultations-Pflicht zugeschnitten |
| **Python-Skripte** (`scripts/*.py`) | Assisted | Anthropic Claude (Sonnet 4.5 / 4.6) | Validierung, Aggregation, FHIR-Logical-Model-Generierung | Manuell ausgeführt und ergebnis-geprüft |
| **Glossar** (`GLOSSARY.md`) | Assisted | Anthropic Claude (Opus 4.7) | Sammlung, Strukturierung, Quellen-Verifikation | Web-stichprobenartige Quellen-Validierung (Primärpublikationen, Score-Cut-offs); §18 markiert Verifikations-Status explizit |
| **Generierte Sichten** (`catalog/data-dictionary.csv`, `.md`; `derived/fhir-logical-model/*.fsh`; `docs/phases-overview.md`) | Generated (deterministisch) | Eigene Python-Skripte (kein direkter KI-Aufruf zur Laufzeit) | Vollständig autogeneriert aus den YAML-Quellen; jeder Lauf ist reproduzierbar | Schema-Validierung vor Generierung; Diff-Review durch Maintainer |
| **Issue- und PR-Templates** (`.github/`) | Assisted | Anthropic Claude (Sonnet 4.5) | Strukturentwurf | Durch Maintainer angepasst |
| **Testdaten / Beispieldaten** | None | — | Keine separaten Testdaten vorhanden — die YAML-Datenelemente selbst sind das Datenmaterial | n/a |

**Legende Scope:**
- `Generated` — Inhalt vollständig oder überwiegend durch KI erzeugt
- `Assisted` — KI unterstützt, Mensch entwirft und prüft substanziell
- `Reviewed` — KI zur Überprüfung/Qualitätssicherung menschlicher Inhalte genutzt
- `None` — Kein KI-Einsatz

---

## 3. Eingesetzte Werkzeuge [COPE]

> **Normative Grundlage:** COPE und ICMJE verlangen die vollständige Angabe der genutzten
> Werkzeuge inklusive Version/Modell, da sich Outputs je Modellversion unterscheiden können.
> Die Versionsangabe ist zugleich Voraussetzung für Reproduzierbarkeit in Forschungskontexten
> und erleichtert die nachträgliche Bewertung von Qualität und Zuverlässigkeit der erzeugten
> Inhalte.

| Werkzeug | Anbieter | Modell / Version | Einsatzzeitraum | Zweck |
|---|---|---|---|---|
| **Claude (via Cowork mode, Claude Desktop)** | Anthropic | `claude-sonnet-4-5` (`claude-sonnet-4-5-20251001`) | 2026-04 – 2026-05 (Erstbefüllung, Sub-Agenten, Skripte, Initial-Doku) | Recherche, Strukturierung, YAML-Erstellung, Skript-Entwicklung |
| **Claude (via Cowork mode, Claude Desktop)** | Anthropic | `claude-sonnet-4-6` | 2026-05 (Patches, README-Neufassung) | Doku-Anpassung, Antrags-Auswertung |
| **Claude (via Cowork mode, Claude Desktop)** | Anthropic | `claude-opus-4-7` | 2026-05 (Glossar-Verifikation, AI_USAGE-Befüllung, Curator-Sub-Agent) | Quellen-Verifikation, Compliance-Dokumentation, Sub-Agent-Architektur |
| **Repo-eigene Sub-Agenten** (`.claude/agents/`) | basierend auf Claude | `data-element-analyzer`, `data-element-validator`, `ai-usage-curator` — siehe [`AGENTS.md`](AGENTS.md) | 2026-05 – laufend | Datenelementweise Analyse + Validation + KI-Nutzungs-Pflege |

> **Hinweis zur Modellversionierung:** Die hier aufgeführten Modellkennungen entsprechen
> den zum Nutzungszeitpunkt verfügbaren Cowork-Mode-Modellen. Da Modelle ohne Versionsangabe
> vom Anbieter aktualisiert werden können, wird die jeweils im jeweiligen Lauf eingesetzte
> Version dokumentiert.

> **Nicht eingesetzt (bewusst dokumentiert):** GitHub Copilot, OpenAI ChatGPT, Google
> Gemini sowie andere KI-Codierhilfen wurden im bisherigen Projektverlauf **nicht**
> verwendet.

---

## 4. Menschliche Aufsicht und redaktionelle Verantwortung [EU AI Act §50 Abs. 2 | COPE]

> **Normative Grundlage:** Art. 50 Abs. 2 EU AI Act sieht eine Ausnahme von der
> Markierungspflicht vor, wenn KI-generierte Inhalte einen echten menschlichen
> Überprüfungsprozess durchlaufen haben und eine natürliche Person die redaktionelle
> Verantwortung übernimmt. Dieser Abschnitt dokumentiert diesen Prozess explizit und
> begründet damit den Anspruch auf die Ausnahmeregelung. Der EU Code of Practice (Draft 2026)
> konkretisiert, dass hierfür ein nachweisbarer dokumentierter Redaktionsworkflow mit
> identifizierbaren Verantwortlichen erforderlich ist — eine bloße Behauptung der Überprüfung
> reicht nicht aus.

Alle in diesem Repository enthaltenen KI-assistierten Artefakte wurden vor Aufnahme
in den Haupt-Branch durch mindestens eine menschliche Person inhaltlich geprüft.
Die redaktionelle Verantwortung liegt bei:

- **Primär verantwortlich:** Marcel Susky (Repository-Maintainer, Forschungsgruppe Digital Health, TU Dresden) — `marcel.susky@tu-dresden.de`
- **Sekundär verantwortlich (Institution):** Forschungsgruppe Digital Health (FGDH), TU Dresden — `digital-health@tu-dresden.de`
- **Klinisches Review (ausstehend, vor produktiver Nutzung):** Klinische Reviewer:innen werden über die in `.github/CODEOWNERS` hinterlegten Rollen pro Phase markiert (siehe `CONTRIBUTING.md` und `docs/howto-add-element.md` §A3).

### Prüfprozess

Der Prüfprozess ist mehrschichtig im Repository operationalisiert:

1. **KI-generierter Entwurf** wird in einer Sitzung mit dem im Cowork-Mode aktiven Claude-Modell erstellt und in der Arbeitskopie abgelegt.
2. **Sub-Agent-Disziplin** (siehe [`AGENTS.md`](AGENTS.md)): Eigenständige Änderungen am Datenbestand sind ausgeschlossen — vor jeder Änderung an Schema, YAML, CodeSystems/ValueSets oder Dokumentation ist die explizite Zustimmung der Nutzer:in einzuholen, **datenelementweise** bei inhaltlichen Änderungen.
3. **Schema-Validierung**: `python scripts/validate.py` muss grün laufen, bevor YAML-Änderungen aufgenommen werden (CI-erzwungen).
4. **Audit-Eintrag**: Jede ausgeführte Aktion wird in [`docs/audit-log.md`](docs/audit-log.md) dokumentiert (Element-ID, Änderungstyp, Quelle, Begründung, Datum). Diese Datei ist die operative Evidenz menschlicher Aufsicht (siehe §10).
5. **Iterations-Log**: [`docs/methodology.md`](docs/methodology.md) §7 protokolliert die übergeordneten Entwicklungs-Iterationen.
6. **Glossar-Pflege**: Neu auftretende Akronyme/Skalen/Codes werden in [`GLOSSARY.md`](GLOSSARY.md) aufgenommen (siehe Analyzer-Agent-Workflow Schritt 8).
7. **Doku-Konsistenz**: Vor Beendigung jeder Aufgabe prüfen die Sub-Agenten, ob `README.md`, `docs/methodology.md`, `docs/phases-overview.md` und `docs/audit-log.md` mit dem Ergebnis konsistent sind.
8. **Pull-Request-Template** ([`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md): klinisch/methodische Begründung, LL-Referenz, klinische:r Reviewer:in. _Empfohlene Erweiterung (offen):_ explizites Feld zur KI-Nutzungs-Disklosure auf PR-Ebene (siehe §11 Offene Punkte).
9. **Zwei Beitrags-Spuren** (siehe [`CONTRIBUTING.md`](CONTRIBUTING.md)):
   - **Klinik-Spur** (niederschwellig): Web-Formular auf GitHub Issues — die KI unterstützt das MI-Team bei der Konvertierung in YAML, die klinische Person reviewt den fertigen PR-Diff.
   - **MI-Spur** (vollständig): YAML + Git + PR; Maintainer prüft KI-assistierte Änderungen vor Merge.

---

## 5. Maschinenlesbare Kennzeichnung [EU AI Act §50 Abs. 2]

> **Normative Grundlage:** Art. 50 Abs. 2 EU AI Act verlangt, dass KI-generierte Inhalte
> in einem maschinenlesbaren Format markiert und als künstlich erzeugt detektierbar sind.
> Der EU Code of Practice (Draft 2026) empfiehlt eine Multi-Layer-Strategie bestehend aus
> digital signierten Metadaten, unsichtbarem Wasserzeichen und optionalem Fingerprinting.
> Für Quellcode-Repositories ist die Commit-Trailer-Konvention (Linux Kernel, Red Hat, 2025)
> derzeit die etablierteste maschinenlesbare Methode. Der Code of Practice erarbeitet noch
> spezifische Guidance für Software-Code; diese Datei dient als ergänzende menschenlesbare
> Dokumentationsschicht.

### 5.1 Commit-Trailer-Konvention

> ⚠️ **Aktueller Stand (2026-05-06):** Die Commit-Historie verwendet die `Assisted-by:`-Trailer
> derzeit **noch nicht durchgehend**. Die folgende Konvention wird als Empfehlung etabliert
> und ab dem Datum der nächsten Aktualisierung systematisch angewandt; rückwirkende
> Annotation der bisherigen Commits über die `git notes`-Funktion ist als Option offen
> (siehe §11 Offene Punkte).

Commits, die KI-assistierte Änderungen enthalten, verwenden folgende Trailer
(kompatibel mit der Linux-Kernel-Konvention, etabliert 2025):

```
Assisted-by: Claude (Anthropic, claude-sonnet-4-6) <https://claude.ai>
```

**Filterung:** KI-assistierte Commits können gefunden werden mit:

```bash
git log --grep="Assisted-by:"
```

### 5.2 Dateiebene

Für Nicht-Code-Artefakte (z. B. Markdown, XML, JSON, SVG) wird KI-Nutzung
im Datei-Header dokumentiert, sofern das Dateiformat es erlaubt:

```markdown
<!-- AI-Assisted: Claude (Anthropic), claude-sonnet-4-6, 2026-05-06 -->
```

> **Aktueller Stand:** Auf Datei-Ebene wird die KI-Nutzung in den YAML-Datenelementen
> indirekt über `iso13972_metadata.publication_status: AuthorDraft` und
> `provenance.created_by` markiert. Eine zusätzliche, für Nicht-YAML-Dateien einheitliche
> Header-Konvention ist in §11 als Verbesserungspunkt aufgeführt.

### 5.3 Repository-Topic

> **Empfohlener Stand:** Das Repository soll das GitHub-Topic `ai-assisted` zur Auffindbarkeit
> und Signalisierung auf Repository-Ebene verwenden. Die Setzung des Topics ist Teil der
> Veröffentlichungs-Checkliste auf der Forschungsgruppe-GitHub-Organisation.

---

## 6. Nicht-Nutzung / Ausschlüsse [CS]

> **Hinweis:** Dieser Abschnitt dient der positiven Abgrenzung: Er dokumentiert explizit,
> welche Artefakte oder Inhaltsbereiche bewusst ohne KI-Werkzeuge erstellt wurden. Dies
> stärkt die Glaubwürdigkeit der Gesamtdokumentation und ist insbesondere für
> qualitätskritische oder haftungsrelevante Inhalte relevant.

Folgende Bereiche unterliegen **bewusst nicht** dem KI-Workflow (entspricht Scope `None`):

- **Klinische Endfreigabe vor produktiver Nutzung** — Übergang von `AuthorDraft` zu `CommitteeDraft` und schließlich `ApprovedForProductionUse` erfolgt ausschließlich durch klinische und medizininformatische Reviewer:innen. KI darf den Status nicht autonom heben.
- **Rechtsverbindliche Konformitätsprüfungen** — die Beurteilung, ob ein Element die Anforderungen von §65c SGB V (oBDS-Krebsregistermeldung), KDL-Pflicht (seit 01.01.2024), MDR/IVDR oder GDPR/DSGVO erfüllt, liegt außerhalb der KI-Verantwortung.
- **Terminologie-Server-Validierung** — die Korrektheit konkreter SNOMED-CT-/LOINC-/ICD-Codes wurde **plausibilitätsgestützt** durch KI vorgeschlagen, aber **nicht** gegen Snowstorm/IHTSDO-/LOINC-FHIR-/IARC-Server endgültig verifiziert. Dies bleibt klinischem Review überlassen (siehe `GLOSSARY.md` §18).
- **Festlegung des Repository-Förderkennzeichens und der Konsortial-Verantwortlichkeiten** — diese folgen dem MiHUB-Antrag und werden vom Konsortium freigegeben, nicht von der KI.
- **Personenbezogene oder vertrauliche Daten** — keinerlei Eingabe in KI-Werkzeuge.

---

## 7. Einschränkungen und Hinweise [COPE | CS]

> **Normative Grundlage:** COPE verlangt, dass Autoren vollständige Verantwortung für alle
> publizierten Inhalte übernehmen — einschließlich KI-generierter Anteile. KI-Werkzeuge
> können weder Verantwortung tragen noch als Autoren gelistet werden (COPE, ICMJE, WAME,
> übereinstimmend). Dieser Abschnitt macht die Risikowahrnehmung und die ergriffenen
> Gegenmaßnahmen explizit und dient damit der Dokumentation angemessener Sorgfalt.

- KI-Werkzeuge können **halluzinieren** — alle fachlichen Aussagen (klinische Definitionen, Empfehlungsgrade, Score-Cut-offs, Code-Bindings) wurden gegen die in `evidence.guideline_references[]` zitierten Primärquellen gegengelesen. Stichprobenartige Verifikation ist in `docs/audit-log.md` dokumentiert; eine **vollständige Wort-für-Wort-Verifikation** ist Teil des klinischen Reviews der nächsten Iteration.
- KI-Werkzeuge können **veraltete Informationen** enthalten — inhaltliche Referenzen wurden gegen die jeweils zum Stichtag aktuelle Leitlinien-/Onkopedia-Fassung geprüft (Versionspin in `evidence.guideline_references[].version`).
- KI-Werkzeuge können **Bias** aufweisen — die Quellen-Reihenfolge (national vor international, Leitlinie vor Sekundärliteratur) und die Konsultations-Pflicht der Sub-Agenten reduzieren das Risiko unbeobachteter Schief-Gewichtung.
- Die KI-generierten Inhalte ersetzen **keine** klinische Expertise, **keine** Terminologie-Server-Validierung und **keine** rechtsverbindliche Konformitätsprüfung. Gesetzliche Pflichten (z. B. oBDS-Krebsregistermeldung gem. §65c SGB V, KDL-Pflicht seit 01.01.2024) bleiben in der Verantwortung der einsetzenden Organisation.
- Die Nutzung kommerzieller KI-Dienste (Anthropic Claude über Cowork-Mode) unterliegt den Nutzungsbedingungen von Anthropic. Keine vertraulichen oder personenbezogenen Daten wurden eingegeben.
- Diese Datei gibt den Stand zum Zeitpunkt der letzten Aktualisierung wieder. Bei wesentlichen Änderungen im KI-Einsatz wird sie aktualisiert.

---

## 8. Rechtliche Grundlagen und Standards [EU AI Act]

> **Hinweis:** Dieser Abschnitt verzeichnet die normativen Quellen, auf die sich diese
> Datei stützt. Er ermöglicht es Dritten, die Ableitung der Dokumentationspflichten
> nachzuvollziehen, und erleichtert die Anpassung der Vorlage bei Änderungen der
> Rechtslage — insbesondere im Hinblick auf die finalen Guidelines der EU-Kommission
> zu Art. 50 (angekündigt für Q2 2026; Veröffentlichungsstatus bei Nutzung dieser
> Vorlage bitte eigenständig prüfen).

| Quelle | Relevanz |
|---|---|
| [EU AI Act, Art. 50 (Verordnung (EU) 2024/1689)](https://artificialintelligenceact.eu/article/50/) | Transparenzpflichten für KI-generierte Inhalte (bindend ab 02.08.2026) |
| [EU Code of Practice on Transparency of AI-Generated Content (Draft 2026)](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content) | Technische Umsetzungshinweise zu Art. 50 Abs. 2 & 4 |
| [COPE: Authorship and AI Tools (2024)](https://publicationethics.org/guidance/cope-position/authorship-and-ai-tools) | Offenlegungspflichten in Forschungspublikationen |
| [ICMJE Recommendations (2026)](https://www.icmje.org/recommendations/) | Autorschaft und Beitragsdokumentation |
| [Linux Kernel AI Policy (2025)](https://docs.kernel.org/process/coding-assistants.html) | `Assisted-by:`-Commit-Trailer-Konvention |
| [Red Hat OSS AI Policy (2025)](https://www.redhat.com/en/blog/ai-assisted-development-and-open-source-navigating-legal-issues) | Disclosure-Empfehlungen für Open Source |

---

## 9. Changelog [CS]

> **Hinweis:** Die Versionierung dieser Datei ist selbst Teil der Transparenzpflicht.
> Wesentliche Änderungen im KI-Einsatz — neue Werkzeuge, geänderter Scope, neue
> Verantwortlichkeiten — sollen zeitnah eingetragen werden, um die Nachvollziehbarkeit
> über den Projektverlauf sicherzustellen.

| Datum | Änderung | Bearbeitet von |
|---|---|---|
| 2026-05-06 | Erstmalige inhaltliche Befüllung der Vorlage; vollständige Subsumierung des bisherigen `DISCLAIMER.md` (Datei entfernt); README-Badge auf `AI_USAGE.md` umgelinkt; `ai-usage-curator`-Sub-Agent etabliert | Marcel Susky (Repository-Maintainer) |

---

## 10. Verhältnis zu `docs/audit-log.md`

`docs/audit-log.md` dokumentiert **inhaltliche Quellen-Verifikation pro Datenelement** sowie das **Iterations-Protokoll der ausgeführten Pflege-Aktionen** (Belegtext-Zitate, Korrektur-Iterationen, Validator-/Analyzer-/Curator-Lauf-Ergebnisse). Es erfüllt damit eine **andere Funktion** als die hier vorliegende KI-Nutzungs-Disklosure und bleibt parallel geführt:

| Aspekt | `AI_USAGE.md` | `docs/audit-log.md` |
|---|---|---|
| Ebene | Repository-weit, Werkzeug- und Verantwortungs-Doku | Element-/Iterations-spezifisch, Inhalts- und Prozess-Audit |
| Adressat | Beitragende, Reviewer, Aufsichtsbehörden, Öffentlichkeit | Reviewer:innen, Maintainer:innen — operative Arbeitsebene |
| Aktualisierungsanlass | Werkzeug-/Scope-/Verantwortungs-Änderung | Jede inhaltliche Änderung an einem Datenelement / jeder Sub-Agenten-Lauf |
| Zuständiger Sub-Agent | `ai-usage-curator` | `data-element-analyzer`, `data-element-validator`, `ai-usage-curator` (jeweils für ihre Lauf-Spuren) |
| EU-AI-Act-Bezug | direkt (Art. 50 Abs. 2) | indirekt (operativer Nachweis menschlicher Aufsicht gemäß §4) |

---

## 11. Offene Punkte (Verbesserungs- / Umsetzungs-Backlog)

Die folgenden Punkte sind **noch nicht umgesetzt** und werden im Laufe der weiteren Repository-Pflege adressiert:

| # | Maßnahme | Begründung | Priorität |
|---|---|---|---|
| 1 | `.github/PULL_REQUEST_TEMPLATE.md` um KI-Disclosure-Feld erweitern (z. B. Checkbox „KI-assistiert (Werkzeug/Modell): _____") | Macht KI-Anteil pro PR sichtbar; harmonisiert mit Commit-Trailer | hoch |
| 2 | `Assisted-by:`-Commit-Trailer-Konvention in CONTRIBUTING.md aufnehmen und ab Datum X verbindlich | Maschinenlesbare Markierung gemäß Linux-Kernel-Konvention | hoch |
| 3 | GitHub-Repository-Topic `ai-assisted` setzen (Veröffentlichungs-Checkliste FGDH) | Erkennbarkeit auf Repo-Ebene | mittel |
| 4 | Datei-Header-Konvention `<!-- AI-Assisted: ... -->` für Markdown-Dateien außerhalb der YAMLs definieren | Einheitliche Datei-Ebene-Markierung | mittel |
| 5 | Rückwirkende `git notes`-Annotation für bisherige Commits prüfen | Vollständige historische Disclosure | niedrig |
| 6 | Klinisches Review-Board konstituieren und in CODEOWNERS pflegen | Voraussetzung für Statuswechsel `AuthorDraft → CommitteeDraft → ApprovedForProductionUse` | hoch (außerhalb KI-Disclosure, hier nur erwähnt, da §6 darauf verweist) |
| 7 | Bei finaler Veröffentlichung der EU-Kommissions-Guidance zu Art. 50 (angekündigt Q2 2026): Datei gegen die Guidance gegenprüfen | Compliance-Fortschreibung | laufend |

---

*Diese Datei ist Teil der Community-Health-Dokumentation dieses Repositories.*
*Für Fragen zur KI-Nutzung: `marcel.susky@tu-dresden.de` oder `digital-health@tu-dresden.de`*
