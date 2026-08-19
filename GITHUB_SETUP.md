# One-time GitHub setup

Suggested repository name:

`FromGMtoStructuredGenAI`

Suggested short description:

> Living book and computational notebooks connecting graphical models, inference, learning, optimization, sampling, and structured generative AI.

Suggested topics:

`graphical-models`, `belief-propagation`, `variational-inference`, `monte-carlo`, `loop-calculus`, `generative-ai`, `diffusion-models`, `scientific-machine-learning`, `jupyter-notebook`, `course-materials`

## Option A: create an empty repository on GitHub, then push

Create a new **empty** repository named `FromGMtoStructuredGenAI` (do not ask GitHub to add another README/license, because they are already present here). Then, from this directory:

```bash
git init
git branch -M main
git add .
git commit -m "Initial public book and course snapshot (2026-08-19)"
git remote add origin git@github.com:mchertkov/FromGMtoStructuredGenAI.git
git push -u origin main
```

Use an HTTPS remote instead if that is your normal GitHub setup.

## Option B: GitHub CLI

If `gh` is installed and authenticated:

```bash
git init
git branch -M main
git add .
git commit -m "Initial public book and course snapshot (2026-08-19)"
gh repo create mchertkov/FromGMtoStructuredGenAI --public --source=. --remote=origin --push
```

## Recommended repository settings

- Enable **Issues** for book corrections, notebook bugs, and proposed extensions.
- Pull Requests can be used for concrete corrections and reproducible notebook improvements.
- GitHub Discussions are optional; course grading/anonymous peer challenges should remain in D2L rather than GitHub.
- Create a dated GitHub Release/tag for stable snapshots used in class.

No Git LFS is currently required: the present manuscript and notebook files are well below GitHub's per-file size limit.
