# Computational notebooks

The notebooks are organized by book chapter. The current snapshot contains **56 notebooks** in 15 chapter directories.

For a complete chapter-by-chapter inventory, see [`../NOTEBOOKS.md`](../NOTEBOOKS.md).

## Current directories

- `ch02/` — representations, partition functions, conditional independence, Ising/Gaussian/dynamic graphical models.
- `ch03/` — exact elimination, treewidth, sum-product on trees, junction trees.
- `ch04/` — MAP/temperature, variational identities, exact conditional generation, exponential-family learning.
- `ch05/` — gauges, reparametrizations, Möbius/region structure, tree transformations.
- `ch06/` — mean field, Bethe/BP, TRW, Kikuchi/GBP, zero-temperature/MAP-LP.
- `ch07/` — mini-buckets, Hölder bounds, low-rank renormalization.
- `ch08/` — stationarity/mixing, Gibbs/Metropolis, coupling from the past, AIS.
- `ch09/` — loop corrections, generalized loops, cluster cumulants, tensor gauge invariance.
- `ch10/` — Chow–Liu, local estimators, hidden variables/EM/CD.
- `ch11/` — scientific/engineering/information-processing applications and approximation stress tests.
- `ch12/` — structured MAP: submodularity, TUM/network flow, tightening relaxations.
- `ch13/` — permanent/Bethe, Gaussian BP, planar Ising, hierarchical control.
- `ch14/` — order MCMC, continuous DAG learning, graphical lasso.
- `ch15/` — neural BP warm starts and learned BP residuals.
- `ch17/` — exactly solvable PoE/PoIE/PoPE Gaussian composition laboratory.

## Running notebooks

Run Jupyter from the repository root:

```bash
jupyter lab
```

or execute a complete chapter from the command line:

```bash
python scripts/execute_notebooks.py --chapter ch09
```

All generated figures are stored chapter-locally in `figs/` as PDF and/or PNG files.

## Design rule for approximate methods

Whenever feasible, a notebook involving approximation or learning should not stop at a successful example. It should expose a controllable parameter that moves the example through an easy regime, a crossover, and a failure/loss-of-guarantee regime, and compare against an exact or certified reference when one is available.
