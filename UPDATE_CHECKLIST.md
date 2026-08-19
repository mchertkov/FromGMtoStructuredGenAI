# Update checklist

Use this checklist for course/book snapshots during Fall 2026.

## Routine update

1. Replace `book/FromGMtoStructuredGenAI_draft.pdf` with the newly compiled manuscript.
2. Add or revise notebooks in the appropriate `notebooks/chXX/` directory.
3. Run changed notebooks from a clean kernel.
4. Run:

   ```bash
   python scripts/validate_notebooks.py
   ```

5. Confirm that no machine-specific absolute paths or private data were added.
6. Update `NOTEBOOKS.md` if notebooks were added/removed.
7. Add a dated entry to `CHANGELOG.md`.
8. Update `version` and `date-released` in `CITATION.cff` for a substantial snapshot.
9. Commit with a descriptive message.

## Stable class/review snapshot

For a version you expect students or reviewers to cite:

1. complete the routine update above;
2. create a date-based tag, e.g. `2026.09.21`;
3. create a GitHub Release from the tag;
4. summarize major manuscript/notebook changes in the release notes.

This keeps the filename used by the course stable while preserving reproducible historical snapshots through Git tags/releases.
