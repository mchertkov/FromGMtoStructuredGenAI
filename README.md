# From Graphical Models to Structured Generative AI

**Inference, Learning, Optimization, Sampling, and Scientific Applications**  
Michael (Misha) Chertkov, University of Arizona

This repository accompanies the living manuscript **_From Graphical Models to Structured Generative AI_** and its computational notebooks. It is being developed in parallel with **MATH 577 — From Graphical Models to Generative AI: Mathematical Foundations, Algorithms, and Modern Applications** at the University of Arizona in Fall 2026.

The organizing theme is **structure-first high-dimensional probability**: begin with explicit probabilistic, graphical, algebraic, dynamical, or scientific structure; identify the computational object; approximate only what must be approximated; and retain correction/verification mechanisms whenever possible.

## Current snapshot

- **Working manuscript:** August 2026, approximately 258 pages.
- **Computational notebooks:** 56 Jupyter notebooks, organized by book chapter.
- **Course use:** the manuscript and notebooks will be updated during Fall 2026 as material is tested in MATH 577.
- **Status:** active working draft. Corrections, counterexamples, stress tests, and reproducibility improvements are especially welcome.

[Read the current manuscript](book/FromGMtoStructuredGenAI_draft.pdf)

## Book architecture

The book develops three recurring mathematical spines:

1. **Structured probability and graphical-model computation:** factorization, exact elimination, belief propagation, variational approximations, MCMC, learning, gauges, loop calculus, and special tractable structure.
2. **Stochastic/generative dynamics:** transport, diffusion, bridges, control, Feynman–Kac representations, autoregressive and discrete generation.
3. **Reference–correction principle:** choose a structured tractable reference and represent the exact target through an explicit correction; then optimize or learn the reference/correction rather than discarding structure.

The later parts pursue two complementary directions:

- **Graphical Models → Neuralization:** learned factors, messages, operators, latent-variable/amortized inference, and learned corrections.
- **Generative AI → Structuralization:** space–time graphical models, structured scores and diffusion, bridges/path-space composition, discrete/autoregressive generation, and scientific constraints.

## Repository layout

```text
FromGMtoStructuredGenAI/
├── book/                  # current compiled working manuscript
├── notebooks/             # chapter-organized computational laboratories
├── course/Fall2026/       # MATH 577 syllabus and course-facing material
├── scripts/               # validation/execution utilities
├── .github/               # issue, pull-request, and CI templates
├── README.md
├── NOTEBOOKS.md
├── ROADMAP.md
├── CONTRIBUTING.md
├── CITATION.cff
├── requirements.txt
├── environment.yml
└── LICENSE
```

## Computational philosophy

Examples are not intended only to demonstrate success. When a method is approximate or learned, we try to push it through

\[
\text{easy/controlled regime}
\;\longrightarrow\;
\text{crossover}
\;\longrightarrow\;
\text{failure or loss of guarantee},
\]

and to compare external error against an exact/certified reference whenever possible. A useful computational example should answer both **when the approximation works** and **how we can tell that it has stopped working**.

See [NOTEBOOKS.md](NOTEBOOKS.md) for the current notebook inventory.

## Quick start

### Conda / Mamba

```bash
conda env create -f environment.yml
conda activate fromgm-structured-genai
jupyter lab
```

### pip

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\\Scripts\\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```

The notebooks are designed to be run from their own chapter directory or from the repository root. Generated figures are written to the chapter-local `figs/` directory.

To validate notebook files without executing them:

```bash
python scripts/validate_notebooks.py
```

To execute one chapter:

```bash
python scripts/execute_notebooks.py --chapter ch06
```

To execute all notebooks:

```bash
python scripts/execute_notebooks.py --all
```

## Fall 2026 course

The repository is a computational companion to:

**MATH 577 — From Graphical Models to Generative AI: Mathematical Foundations, Algorithms, and Modern Applications**  
University of Arizona, Fall 2026  
Monday/Wednesday, 11:00 AM–12:15 PM, Mathematics 514.

The course uses the book as a living text. Students may propose corrections, alternative derivations, notebook improvements, new exercises/problems/challenges, counterexamples, and approximation stress tests. Course submissions are screened by the instructor before any public contribution is added to GitHub; graded anonymous D2L submissions remain separate from this public repository unless the student explicitly agrees to public attribution/release.

See [course/Fall2026/](course/Fall2026/).

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md). Particularly useful contributions include:

- mathematical corrections or counterexamples;
- reproducible notebook fixes;
- examples that expose a failure regime of an approximation;
- exact/certified reference calculations;
- new exercises, problems, or research challenges;
- improved cross-links between classical graphical models and structured generative AI.

## Citation

Citation metadata is provided in [CITATION.cff](CITATION.cff). Because this is a living manuscript, please include the date or release tag of the version you used.

## License

Repository code, Jupyter notebooks, and repository documentation are released under the **MIT License**; see [LICENSE](LICENSE) and [LICENSE_SCOPE.md](LICENSE_SCOPE.md).

The working book manuscript PDF is distributed here as a pre-publication educational/review draft and is **not** placed under the MIT software license pending final publication arrangements. See [book/MANUSCRIPT_NOTICE.md](book/MANUSCRIPT_NOTICE.md).

## Contact

Michael (Misha) Chertkov  
Program in Applied Mathematics and Department of Mathematics  
University of Arizona  
`chertkov@arizona.edu`
