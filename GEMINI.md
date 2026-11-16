# GEOMETOR • `pascal`

the French mathematician and philosopher whose 1640 broadside Essay pour les Coniques unveiled the Mystic Hexagram theorem for any conic section

---

## 1. Repository Identity & Archetype

- **Organization**: `geometor` (`GEOMETOR`)
- **Package**: `geometor.pascal` (`src/geometor/pascal/`)
- **Archetype**: `codex`
- **Work**: *Essay pour les Coniques* — Blaise Pascal

---

## 2. Architectural & Editorial Mandates

1. **Python 3.13 & Exact Symbolic Standards**:
   - Every Python module begins with a module docstring followed immediately by `from __future__ import annotations`, built-in generic types (`list`, `dict`, `tuple`, `X | Y`), Google-style docstrings, and an explicit `__all__`.
   - Zero `float` or `sympy.Float` approximations in symbolic geometry constructions.
2. **Digital Scriptorium Codex Discipline (`codex`)**:
   - **Multimodal Scan Vision Over OCR**: Always inspect 300 DPI archival page scans directly via `view_file`; never rely on `pdftotext`, `pypdf`, or embedded OCR text layers for transcription, formulas, or geometric labels.
   - **Strict Content / Code Separation**: Keep `docsrc/essay_coniques_1640/` (`:layout: book`) dedicated to faithful source transcription, translations, scholarly apparatus, and calibrated `.euclid-graphic` SVGs—never embed executable `py_file` scripts inside historical treatise tracks.
   - **Git Hygiene**: Never commit `.pdf` files or raw raster scan directories (`resources/**/scans/*.png`) to git.

---

## 3. Verification Commands (Offline Sandbox Safe)

```bash
uv run --no-sync pytest
ruff check src tests demos
publish build
```
