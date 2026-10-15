#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Prüft die Zitate (`evidence.guideline_references[].quote`) der Datenelemente gegen Textfassungen der Quellen.

Die Quellen selbst liegen nicht im Repo (Urheberrecht). Wer prüfen will, erzeugt Textfassungen der Quell-PDFs
(z. B. `pdftotext -layout S3_LL_Lungenkarzinom_Langversion_5.1.pdf s3-lunge.txt`) und übergibt eine Zuordnung
Quelle → Textdatei als JSON. Schlüssel ist der `source`-Wert; für `andere` ein Teilstring der `version`
(z. B. "Klein", "Psychoonkologie"). Mehrere Dateien je Quelle sind möglich (Liste).

  python scripts/verify-quotes.py --sources quellen-texte.json
  python scripts/verify-quotes.py --sources quellen-texte.json --json bericht.json elements/follow-up/

Beispiel quellen-texte.json:
  {"S3-LL Lungenkarzinom": "texte/s3-lunge-5.1.txt",
   "AG LONKO / Survivorship": ["texte/ag-lonko-daten.txt", "texte/ag-lonko-versorgungsmodelle.txt"],
   "andere:Klein": "texte/klein-2026.txt"}

Ein Zitat gilt als gefunden, wenn jedes durch „…“ getrennte Teilstück (ab 12 Zeichen; bei kurzen Zitaten ab 3 Zeichen) nach Normalisierung
(Leerraum zusammengefasst, Silbentrennung am Zeilenende entfernt, typografische Anführungszeichen/Striche
vereinheitlicht) wörtlich in der Textfassung vorkommt — oder als Wortfolge in derselben Reihenfolge mit höchstens
8 eingeschobenen Tokens (Spalten- und Kopfzeilentext aus dem PDF-Layout, z. B. Empfehlungsgrad neben dem Empfehlungstext). Zitate aus Expert:innen-Erhebungen werden gegen den
Mappen-Auszug `docs/reviews/2026-10-13-erhebungen.md` geprüft, wenn dieser als Quelle angegeben ist.

Nur Standardbibliothek + PyYAML; keine Schreibzugriffe auf `elements/`. Exit-Code 1 bei nicht gefundenen Zitaten.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TRANS = str.maketrans({"„": '"', "“": '"', "”": '"', "‚": "'", "‘": "'", "’": "'", "–": "-", "—": "-", "­": "", " ": " "})


def norm(text: str) -> str:
    t = text.translate(TRANS)
    t = re.sub(r"(\w)-[ \t]*\n\s*([a-zäöüß])", r"\1\2", t)   # Silbentrennung am Zeilenende
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def loose(text: str, compound: bool = False) -> str:
    """Zusätzlich ohne Bindestrich-Leerzeichen-Folgen ("wer- den") und ohne Leerraum vor Satzzeichen.

    compound=True behält den Bindestrich vor Großbuchstaben/Ziffern (Komposita über den Zeilenumbruch,
    z. B. „Niedrigdosis- CT“ → „Niedrigdosis-CT“); geprüft wird zusätzlich zur Grundform.
    """
    t = norm(text)
    if compound:
        t = re.sub(r"(\w)- ([A-ZÄÖÜ0-9])", r"\1-\2", t)
    t = re.sub(r"(\w)- (\w)", r"\1\2", t)
    return re.sub(r" ([,.;:)])", r"\1", t)


PUNCT = ",.;:()[]„“\"'!?*"
GAP = 8  # max. eingeschobene Tokens (Spalten-/Kopfzeilentext aus dem PDF-Layout)


def tokens_index(raw: str):
    """Tokenfolge der Textfassung + je Position die zulässigen Wortformen (Silbentrennung zusammengeführt)."""
    toks = [w.strip(PUNCT) for w in re.sub(r"\s+", " ", raw.translate(TRANS)).split(" ")]
    forms, index = [], {}
    for i, w in enumerate(toks):
        f = {w: i}
        if w.endswith("-") and len(w) > 1:
            for j in range(i + 1, min(i + 5, len(toks))):
                if toks[j][:1].islower():
                    f[w[:-1] + toks[j]] = j
                    break
                if toks[j][:1].isupper() or toks[j][:1].isdigit():
                    f.setdefault(w + toks[j], j)    # Kompositum mit Bindestrich, z. B. „Niedrigdosis-CT“
        forms.append(f)
        for v in f:
            index.setdefault(v, []).append(i)
    return forms, index


def gap_match(fragment: str, forms, index) -> bool:
    qt = [w.strip(PUNCT) for w in norm(fragment).split(" ") if w.strip(PUNCT)]
    if not qt:
        return False
    for start in index.get(qt[0], []):
        pos = forms[start][qt[0]]
        ok = True
        for w in qt[1:]:
            nxt = next((forms[k][w] for k in range(pos + 1, min(pos + 2 + GAP, len(forms))) if w in forms[k]), None)
            if nxt is None:
                ok = False
                break
            pos = nxt
        if ok:
            return True
    return False


def fragments(quote: str) -> list[str]:
    parts = [p.strip(" \"'") for p in re.split(r"…|\.\.\.|\[…\]", quote)]
    long = [p for p in parts if len(p) >= 12]
    return long or [p for p in parts if len(p) >= 3]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sources", required=True, help="JSON: source → Textdatei(en)")
    ap.add_argument("--json", help="Bericht als JSON speichern")
    ap.add_argument("paths", nargs="*", help="YAML-Dateien oder Ordner (Default: elements/)")
    a = ap.parse_args()
    mapping = json.loads(Path(a.sources).read_text(encoding="utf-8"))
    base = Path(a.sources).resolve().parent
    texts: dict[str, tuple[str, str]] = {}
    for key, val in mapping.items():
        files = val if isinstance(val, list) else [val]
        raw = "\n".join((base / f).read_text(encoding="utf-8", errors="replace") if not Path(f).is_absolute() else Path(f).read_text(encoding="utf-8", errors="replace") for f in files)
        texts[key] = (norm(raw), loose(raw), loose(raw, True), *tokens_index(raw))
    files = []
    for p in a.paths or [str(ROOT / "elements")]:
        pp = Path(p)
        files += sorted(pp.rglob("*.yaml")) if pp.is_dir() else [pp]
    rows, missing = [], 0
    for f in files:
        doc = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        for i, r in enumerate(((doc.get("evidence") or {}).get("guideline_references")) or []):
            q = r.get("quote")
            if not q:
                rows.append({"element": doc.get("name"), "index": i, "source": r.get("source"), "status": "OHNE-ZITAT"})
                continue
            key = r.get("source")
            if key == "andere":
                key = next((k for k in texts if k.startswith("andere:") and k.split(":", 1)[1] in str(r.get("version", ""))), None)
            if key not in texts:
                rows.append({"element": doc.get("name"), "index": i, "source": r.get("source"), "status": "KEINE-TEXTFASSUNG"})
                continue
            strict, lax, lax_c, forms, index = texts[key]
            ok = bool(fragments(q)) and all(norm(fr) in strict or loose(fr) in lax or loose(fr, True) in lax_c or gap_match(fr, forms, index) for fr in fragments(q))
            status = "GEFUNDEN" if ok else "NICHT-GEFUNDEN"
            missing += not ok
            rows.append({"element": doc.get("name"), "index": i, "source": r.get("source"), "status": status, "quote": q[:120]})
    counts: dict[str, int] = {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
        if r["status"] == "NICHT-GEFUNDEN":
            print(f"NICHT-GEFUNDEN  {r['element']:<34} [{r['index']}] {r['source']}: {r['quote']}")
    print("Zusammenfassung: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    if a.json:
        Path(a.json).write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
