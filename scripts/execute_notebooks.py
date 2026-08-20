#!/usr/bin/env python3
"""Execute one chapter or all repository notebooks in place."""
from pathlib import Path
import argparse
import sys
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

ROOT = Path(__file__).resolve().parents[1]
NBROOT = ROOT / "notebooks"

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--chapter", help="chapter directory, e.g. ch06")
group.add_argument("--all", action="store_true", help="execute every notebook")
parser.add_argument("--timeout", type=int, default=300, help="per-cell timeout in seconds")
args = parser.parse_args()

if args.all:
    paths = sorted(NBROOT.glob("ch*/*.ipynb"))
else:
    chapter = NBROOT / args.chapter
    if not chapter.is_dir():
        sys.exit(f"No such chapter directory: {chapter}")
    paths = sorted(chapter.glob("*.ipynb"))

failures = []
for path in paths:
    print(f"Executing {path.relative_to(ROOT)}")
    try:
        nb = nbformat.read(path, as_version=4)
        ep = ExecutePreprocessor(timeout=args.timeout, kernel_name="python3")
        ep.preprocess(nb, {"metadata": {"path": str(path.parent)}})
        nbformat.write(nb, path)
    except Exception as exc:
        print(f"  FAILED: {exc}")
        failures.append((path, exc))

if failures:
    print(f"\n{len(failures)} notebook(s) failed:")
    for path, exc in failures:
        print(f"- {path.relative_to(ROOT)}: {exc}")
    sys.exit(1)
print(f"Executed {len(paths)} notebook(s) successfully.")
