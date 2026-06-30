<!--
DRAFT — pending review and sign-off by the TU Dresden Justiziariat (legal office)
and the Data Protection Officer (DPO). This document is NOT legal advice and the
wording below is a starting point for that review, not a final legal text.
-->

# Disclaimer / Haftungsausschluss

> **Status: DRAFT — awaiting legal & DPO sign-off (TU Dresden).**
> The intended-use and liability wording below has not yet been reviewed by the
> TU Dresden legal office. It is provided so reviewers have a concrete basis to work
> from. It is **not legal advice**.

This disclaimer supplements — and does not replace — Section 5 (Disclaimer of
Warranties and Limitation of Liability) of the [CC BY 4.0 licence](LICENSE) under
which the **content** of this repository is published. The Python scripts under
`scripts/` are published under the [Apache License 2.0](LICENSE-APACHE-2.0.txt).

---

## English

### 1. Intended use

The data elements in this repository (YAML definitions, generated catalogs, the JSON
schema, glossary, and documentation) are a **research, education, and
interoperability-reference artifact** produced in the MiHUB project (TU Dresden /
Forschungsgruppe Digital Health). They are intended for purposes such as: documenting and
discussing which clinical data are captured, exchanged, and re-used along the lung-cancer
patient pathway, teaching, and serving as input to downstream technical work (e.g. FHIR
profile / terminology specification, FHIR logical models, synthetic-data generation, and
mapping to national/international implementation guides).

### 2. Not for clinical use

These data elements are an **author draft** (`publication_status: AuthorDraft`), are **not
clinically validated**, and the suggested codes (SNOMED CT, LOINC, ICD-10-GM, OPS, KDL …)
have **not** been fully verified against terminology servers. They are **not** intended for
use in direct patient care or for clinical decision-making, are **not medical advice**, are
**not a substitute** for professional medical judgment, diagnosis, or treatment, and do
**not** establish or represent a standard of care or a binding documentation obligation.
They must **not** be used to make or support decisions about an individual patient without
independent clinical validation and a regulatory assessment by the using party.

### 3. Not a medical device

The authors assign these data elements **no medical intended purpose** within the meaning of
Art. 2(1) of Regulation (EU) 2017/745 (Medical Device Regulation, MDR). They are a static,
non-executable specification (a clinical information model / data dictionary) that does not by
itself drive, control, or influence a medical device, and they are **not** provided or
CE-marked as a medical device. Any party that repurposes them in a way that gives them a
medical intended purpose assumes the corresponding regulatory responsibility.

### 4. No legal / regulatory conformity claim

Inclusion of a mapping target (e.g. oBDS, MII-KDS, KBV-MIO, gematik IGs, mCODE) does **not**
assert conformity with that standard or with any statutory obligation. The assessment of
whether an element satisfies, e.g., the cancer-registry reporting duty under § 65c SGB V, the
KDL obligation, the MDR/IVDR, or the GDPR remains with the using organisation.

### 5. No warranty

The data elements are provided **"as is" and "as available"**, without warranties of any kind
(including accuracy, completeness, currency, or fitness for a particular purpose), as set out
in Section 5 of the [CC BY 4.0 licence](LICENSE).

### 6. Limitation of liability

To the extent permitted by applicable law, the authors and their institution accept no
liability for any loss or damage arising from the use of these data elements. **Mandatory
statutory liability remains unaffected** — in particular, liability for injury to life, body,
or health, and for intent or gross negligence, cannot be and is not excluded (cf. § 309 No. 7
BGB, to the extent this disclaimer is treated as standard terms).

### 7. Currency

The data elements reflect the authors' best understanding at the time of publication, based on
the guideline and Onkopedia versions cited per element. Clinical guidelines, terminologies, and
implementation guides evolve; the content may not reflect the most recent guidance.

### 8. Third-party content and attribution

This work reuses and builds on third-party material under their respective terms (see the
"Vorarbeiten und Grundlagen" and "Lizenz" sections of [`README.md`](README.md), incl. the INA
Journey Onkologie and CraNE Joint Action WP6 attributions). The CC BY 4.0 licence grants **no**
trademark or endorsement rights; the names and logos of TU Dresden, BMFTR, MiHUB, and other
parties may not be used to imply endorsement without separate permission.

---

## Deutsch

### 1. Zweckbestimmung

Die Datenelemente in diesem Repository (YAML-Definitionen, generierte Kataloge, das
JSON-Schema, Glossar und Dokumentation) sind ein **Forschungs-, Lehr- und
Interoperabilitäts-Referenzartefakt** aus dem Projekt MiHUB (TU Dresden / Forschungsgruppe
Digital Health). Sie sind etwa zur Dokumentation und Diskussion der Frage bestimmt, *welche*
klinischen Daten entlang des Lungenkrebs-Patientenpfads erhoben, ausgetauscht und sekundär
genutzt werden, zur Lehre und als Grundlage für nachgelagerte technische Arbeiten (z. B.
FHIR-Profil-/Terminologie-Spezifikation, FHIR-Logical-Models, Generierung synthetischer Daten,
Mapping auf nationale/internationale Implementation Guides).

### 2. Kein Einsatz in der Versorgung

Die Datenelemente sind ein **Author Draft** (`publication_status: AuthorDraft`), **nicht
klinisch validiert**, und die vorgeschlagenen Codes (SNOMED CT, LOINC, ICD-10-GM, OPS, KDL …)
sind **nicht** vollständig gegen Terminologie-Server verifiziert. Sie sind **nicht** für den
Einsatz in der unmittelbaren Patient:innenversorgung oder zur klinischen Entscheidungsfindung
bestimmt, stellen **keine medizinische Beratung** dar, ersetzen **nicht** das ärztliche Urteil,
Diagnose oder Behandlung und begründen **keinen** Versorgungs-/Sorgfaltsstandard und **keine**
verbindliche Dokumentationspflicht. Sie dürfen **nicht** zur Entscheidung über einzelne
Patient:innen herangezogen werden, ohne dass die nutzende Stelle eine eigenständige klinische
Validierung und regulatorische Bewertung vornimmt.

### 3. Kein Medizinprodukt

Die Autor:innen weisen den Datenelementen **keine medizinische Zweckbestimmung** im Sinne des
Art. 2 Nr. 1 der Verordnung (EU) 2017/745 (Medizinprodukteverordnung, MDR) zu. Es handelt sich
um eine statische, nicht ausführbare Spezifikation (klinisches Informationsmodell /
Data Dictionary), die für sich genommen kein Medizinprodukt steuert, kontrolliert oder
beeinflusst; sie wird **nicht** als Medizinprodukt bereitgestellt oder CE-gekennzeichnet. Wer
die Datenelemente so weiterverwendet, dass ihnen eine medizinische Zweckbestimmung zukommt,
übernimmt die entsprechende regulatorische Verantwortung.

### 4. Keine rechtlich-regulatorische Konformitätszusage

Die Angabe eines Mapping-Ziels (z. B. oBDS, MII-KDS, KBV-MIO, gematik-IGs, mCODE) behauptet
**keine** Konformität mit diesem Standard oder mit einer gesetzlichen Pflicht. Die Beurteilung,
ob ein Element z. B. die Krebsregister-Meldepflicht nach § 65c SGB V, die KDL-Pflicht, die
MDR/IVDR oder die DSGVO erfüllt, bleibt bei der einsetzenden Organisation.

### 5. Keine Gewährleistung

Die Datenelemente werden **„wie besehen" und „wie verfügbar"** ohne jegliche Gewährleistung
(insbesondere Richtigkeit, Vollständigkeit, Aktualität, Eignung für einen bestimmten Zweck)
bereitgestellt, entsprechend Abschnitt 5 der [CC-BY-4.0-Lizenz](LICENSE).

### 6. Haftungsbeschränkung

Soweit gesetzlich zulässig, übernehmen die Autor:innen und ihre Einrichtung keine Haftung für
Schäden aus der Nutzung der Datenelemente. **Die zwingende gesetzliche Haftung bleibt
unberührt** — insbesondere die Haftung für die Verletzung von Leben, Körper oder Gesundheit
sowie für Vorsatz und grobe Fahrlässigkeit ist und wird nicht ausgeschlossen (vgl. § 309 Nr. 7
BGB, soweit dieser Haftungsausschluss als Allgemeine Geschäftsbedingung zu behandeln ist).

### 7. Aktualität

Die Datenelemente geben den besten Kenntnisstand der Autor:innen zum Zeitpunkt der
Veröffentlichung wieder, basierend auf den je Element zitierten Leitlinien-/Onkopedia-Versionen.
Leitlinien, Terminologien und Implementation Guides entwickeln sich weiter; die Inhalte bilden
möglicherweise nicht den aktuellsten Stand ab.

### 8. Drittinhalte und Namensnennung

Diese Arbeit nutzt und baut auf Materialien Dritter zu deren jeweiligen Bedingungen auf (siehe
Abschnitte „Vorarbeiten und Grundlagen" und „Lizenz" in [`README.md`](README.md), inkl. der
Attributionen zu INA Journey Onkologie und CraNE Joint Action WP6). Die CC-BY-4.0-Lizenz
gewährt **keine** Marken- oder Empfehlungsrechte; Namen und Logos der TU Dresden, des BMFTR,
von MiHUB und weiterer Beteiligter dürfen ohne gesonderte Erlaubnis nicht zur Andeutung einer
Befürwortung verwendet werden.
