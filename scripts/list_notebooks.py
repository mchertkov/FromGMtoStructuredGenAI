#!/usr/bin/env python3
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "notebooks").glob("ch*/*.ipynb"))
counts = Counter(p.parent.name for p in paths)
print(f"Total notebooks: {len(paths)}")
for chapter in sorted(counts):
    print(f"{chapter}: {counts[chapter]}")
    for p in paths:
        if p.parent.name == chapter:
            print(f"  - {p.name}")
