# Disclaimer — KI-gestützte Erstellung

Dieses Repository wurde **mit KI-Unterstützung** (Anthropic Claude und/oder OpenAI-Modellen) erstellt und gepflegt. Alle Inhalte — insbesondere Datenelemente, Codings, Quellenangaben und Mappings — sind **als Author Draft zu betrachten** und vor produktiver Nutzung durch klinische und medizininformatische Reviewer:innen zu validieren.

## Konkret KI-unterstützte Aufgaben

- Sichtung von Standards & Referenzarchitekturen (ISO 13972 / 13606 / 23903, HL7 HSRA)
- Auswertung klinischer Leitlinien (S3-LL Lungenkarzinom, Palliativmedizin, Tabakentwöhnung, Onkopedia, OCP)
- Erhebung & Strukturierung von Datenelementen entlang des onkologischen Patientenpfads
- Vorschlag von Beispiel-Codings (SNOMED CT, LOINC, ICD-10-GM, OPS, ATC, KDL)
- Mapping auf nationale und internationale Implementation Guides (oBDS, MII KDS, KBV MIO, gematik ePA, mCODE, OMOP CDM u. a.)
- Schema-Validierung, CSV-Aggregation, FHIR-Logical-Model-Generierung (on-demand)
- Konsistenz-/Mehrwert-Audit der Repository-Dokumentation

## Verbindlichkeit

Die KI-generierten Inhalte ersetzen **keine** klinische Expertise, **keine** Terminologie-Server-Validierung und **keine** rechtsverbindliche Konformitätsprüfung. Gesetzliche Pflichten (z. B. oBDS-Krebsregistermeldung gem. §65c SGB V, KDL-Pflicht seit 01.01.2024) bleiben in der Verantwortung der einsetzenden Organisation.

## Reproduzierbarkeit

Der Erstellungsprozess ist im Iterations-Log (`docs/methodology.md` §7) und im Audit-Trail (`docs/verification-log.md`) dokumentiert. Aktualisierung der Inhalte erfolgt über die in `AGENTS.md` beschriebenen, konsens-basierten Sub-Agenten — eigenständige Änderungen sind ausgeschlossen.
