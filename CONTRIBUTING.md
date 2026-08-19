# Contributing

Contributions are welcome. This is a living research/teaching repository, so the most valuable contributions are those that improve mathematical correctness, reproducibility, and the connection between structure and modern generative modeling.

## Good contribution types

1. **Book correction** — a mathematical error, missing condition, notation conflict, unclear argument, or useful counterexample.
2. **Notebook bug** — code that fails, gives a wrong result, depends on an undocumented environment detail, or is not reproducible.
3. **Stress test** — an extension that identifies a crossover/failure regime of an approximation or learned method.
4. **Verification** — an exact calculation, certificate, alternative implementation, or independent reproduction.
5. **Exercise / Problem / Challenge** — a pedagogically useful addition with a checked solution or a clearly stated open status.
6. **New structured-GenAI connection** — a mathematically explicit connection that identifies the object being approximated/neuralized and what structure is retained.

## Before opening a pull request

- Run the notebook you changed from a clean kernel.
- Keep random seeds fixed when reproducibility matters.
- Save generated figures into that chapter's `figs/` directory.
- Do not commit machine-specific absolute paths, credentials, private data, or large raw datasets.
- If changing a mathematical claim, explain the reason and provide a reference, derivation, counterexample, or reproducible check.
- Prefer a small focused pull request over a broad unrelated rewrite.

## Notebook conventions

- Use chapter-prefixed names such as `ch09_04_...ipynb`.
- A notebook should state what mathematical point it demonstrates.
- For approximate/learned methods, include a success regime and, whenever feasible, a controlled failure/crossover regime.
- Distinguish exact/certified quantities from heuristics or empirical diagnostics.
- Generated figures should have informative axis labels and captions/titles that can stand alone.

## MATH 577 students

Graded course work is submitted through the course system, not through public GitHub. The instructor may anonymously share screened submissions within the class for challenges/peer review. A student's work is moved into this public repository only with the student's knowledge and permission; attribution is provided when desired.

Public GitHub activity is not itself a grading requirement.

## Issues vs pull requests

- Use an **Issue** when reporting a problem, asking a mathematical question, or proposing a new direction.
- Use a **Pull Request** when you have a concrete correction or reproducible improvement ready to merge.
