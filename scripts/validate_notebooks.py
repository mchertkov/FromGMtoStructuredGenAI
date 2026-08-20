#!/usr/bin/env python3
"""Fast structural validation of all Jupyter notebooks in the repository."""
from pathlib import Path
import sys
import nbformat

ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "notebooks").glob("ch*/*.ipynb"))
errors = []
for path in paths:
    try:
        nb = nbformat.read(path, as_version=4)
        nbformat.validator.validate(nb)
    except Exception as exc:
        errors.append((path, exc))

if errors:
    for path, exc in errors:
        print(f"FAIL {path.relative_to(ROOT)}: {exc}")
    sys.exit(1)
print(f"Validated {len(paths)} notebooks.")
