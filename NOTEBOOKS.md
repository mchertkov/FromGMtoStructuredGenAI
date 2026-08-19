# Notebook inventory

The computational material is organized by book chapter. The current snapshot contains **56 notebooks**. Notebooks in the classical core are comparatively mature; the neuralization and structured-generative-AI notebook suite is actively expanding during Fall 2026.

| Directory | Book chapter / theme | Notebooks |
|---|---|---:|
| [`ch02/`](notebooks/ch02/) | Graphical Models: Representations, Partition Functions, and First Examples | 6 |
| [`ch03/`](notebooks/ch03/) | Exact Elimination, Dynamic Programming, and Message Passing | 3 |
| [`ch04/`](notebooks/ch04/) | Other Inference, Optimization and Learning Challenges | 4 |
| [`ch05/`](notebooks/ch05/) | Transformations of Graphical Models | 4 |
| [`ch06/`](notebooks/ch06/) | Variational Inference: Free Energies, Bounds, and Message Passing | 5 |
| [`ch07/`](notebooks/ch07/) | Approximate Elimination: Mini-Buckets, Gauges, and Renormalization | 3 |
| [`ch08/`](notebooks/ch08/) | Markov Chain Monte Carlo: Invariance, Mixing, and Exact Sampling | 4 |
| [`ch09/`](notebooks/ch09/) | Loop Calculus: Exact Corrections Beyond Belief Propagation | 4 |
| [`ch10/`](notebooks/ch10/) | Graphical Model Learning | 3 |
| [`ch11/`](notebooks/ch11/) | Applications: Structure as the Common Language | 7 |
| [`ch12/`](notebooks/ch12/) | Maximum A-Posteriori Problems | 3 |
| [`ch13/`](notebooks/ch13/) | Soft Inference Problems | 4 |
| [`ch14/`](notebooks/ch14/) | Advanced Structure Learning: Orders, DAGs, and Sparse Graphical Models | 3 |
| [`ch15/`](notebooks/ch15/) | Neuralizing Graphical Models: Learned Factors, Messages, Operators, and Corrections | 2 |
| [`ch17/`](notebooks/ch17/) | Structured Generative Processes: From Static Factors to Space-Time Graphs | 1 |

## Detailed list

### ch02: Graphical Models: Representations, Partition Functions, and First Examples

- [`ch02_01_factorization_and_enumeration.ipynb`](notebooks/ch02/ch02_01_factorization_and_enumeration.ipynb) — factorization and enumeration.
- [`ch02_02_factor_graph_to_normal_factor_graph.ipynb`](notebooks/ch02/ch02_02_factor_graph_to_normal_factor_graph.ipynb) — factor graph to normal factor graph.
- [`ch02_03_conditional_independence.ipynb`](notebooks/ch02/ch02_03_conditional_independence.ipynb) — conditional independence.
- [`ch02_04_ising_chain_and_triangle.ipynb`](notebooks/ch02/ch02_04_ising_chain_and_triangle.ipynb) — ising chain and triangle.
- [`ch02_05_gaussian_graphical_model.ipynb`](notebooks/ch02/ch02_05_gaussian_graphical_model.ipynb) — gaussian graphical model.
- [`ch02_06_dynamic_graphical_model.ipynb`](notebooks/ch02/ch02_06_dynamic_graphical_model.ipynb) — dynamic graphical model.

### ch03: Exact Elimination, Dynamic Programming, and Message Passing

- [`ch03_01_elimination_order_and_treewidth.ipynb`](notebooks/ch03/ch03_01_elimination_order_and_treewidth.ipynb) — elimination order and treewidth.
- [`ch03_02_sum_product_on_trees.ipynb`](notebooks/ch03/ch03_02_sum_product_on_trees.ipynb) — sum product on trees.
- [`ch03_03_junction_tree.ipynb`](notebooks/ch03/ch03_03_junction_tree.ipynb) — junction tree.

### ch04: Other Inference, Optimization and Learning Challenges

- [`ch04_01_map_temperature_and_conditioning.ipynb`](notebooks/ch04/ch04_01_map_temperature_and_conditioning.ipynb) — map temperature and conditioning.
- [`ch04_02_gibbs_variational_principle.ipynb`](notebooks/ch04/ch04_02_gibbs_variational_principle.ipynb) — gibbs variational principle.
- [`ch04_03_exact_decimation_sampling.ipynb`](notebooks/ch04/ch04_03_exact_decimation_sampling.ipynb) — exact decimation sampling.
- [`ch04_04_exponential_family_learning.ipynb`](notebooks/ch04/ch04_04_exponential_family_learning.ipynb) — exponential family learning.

### ch05: Transformations of Graphical Models

- [`ch05_01_gauge_invariance.ipynb`](notebooks/ch05/ch05_01_gauge_invariance.ipynb) — gauge invariance.
- [`ch05_02_reparametrization_and_bp.ipynb`](notebooks/ch05/ch05_02_reparametrization_and_bp.ipynb) — reparametrization and bp.
- [`ch05_03_hypergraph_mobius.ipynb`](notebooks/ch05/ch05_03_hypergraph_mobius.ipynb) — hypergraph mobius.
- [`ch05_04_tree_transformations.ipynb`](notebooks/ch05/ch05_04_tree_transformations.ipynb) — tree transformations.

### ch06: Variational Inference: Free Energies, Bounds, and Message Passing

- [`ch06_01_mean_field_variational_inference.ipynb`](notebooks/ch06/ch06_01_mean_field_variational_inference.ipynb) — mean field variational inference.
- [`ch06_02_bethe_and_loopy_bp.ipynb`](notebooks/ch06/ch06_02_bethe_and_loopy_bp.ipynb) — bethe and loopy bp.
- [`ch06_03_tree_reweighted_bounds.ipynb`](notebooks/ch06/ch06_03_tree_reweighted_bounds.ipynb) — tree reweighted bounds.
- [`ch06_04_kikuchi_and_gbp.ipynb`](notebooks/ch06/ch06_04_kikuchi_and_gbp.ipynb) — kikuchi and gbp.
- [`ch06_05_zero_temperature_and_map_lp.ipynb`](notebooks/ch06/ch06_05_zero_temperature_and_map_lp.ipynb) — zero temperature and map lp.

### ch07: Approximate Elimination: Mini-Buckets, Gauges, and Renormalization

- [`ch07_01_bucket_elimination_and_minibuckets.ipynb`](notebooks/ch07/ch07_01_bucket_elimination_and_minibuckets.ipynb) — bucket elimination and minibuckets.
- [`ch07_02_holder_weights.ipynb`](notebooks/ch07/ch07_02_holder_weights.ipynb) — holder weights.
- [`ch07_03_low_rank_renormalization.ipynb`](notebooks/ch07/ch07_03_low_rank_renormalization.ipynb) — low rank renormalization.

### ch08: Markov Chain Monte Carlo: Invariance, Mixing, and Exact Sampling

- [`ch08_01_stationarity_and_mixing.ipynb`](notebooks/ch08/ch08_01_stationarity_and_mixing.ipynb) — stationarity and mixing.
- [`ch08_02_gibbs_and_metropolis.ipynb`](notebooks/ch08/ch08_02_gibbs_and_metropolis.ipynb) — gibbs and metropolis.
- [`ch08_03_coupling_from_the_past.ipynb`](notebooks/ch08/ch08_03_coupling_from_the_past.ipynb) — coupling from the past.
- [`ch08_04_annealed_importance_sampling.ipynb`](notebooks/ch08/ch08_04_annealed_importance_sampling.ipynb) — annealed importance sampling.

### ch09: Loop Calculus: Exact Corrections Beyond Belief Propagation

- [`ch09_01_single_cycle_loop_correction.ipynb`](notebooks/ch09/ch09_01_single_cycle_loop_correction.ipynb) — single cycle loop correction.
- [`ch09_02_generalized_loop_enumeration.ipynb`](notebooks/ch09/ch09_02_generalized_loop_enumeration.ipynb) — generalized loop enumeration.
- [`ch09_03_cluster_cumulants.ipynb`](notebooks/ch09/ch09_03_cluster_cumulants.ipynb) — cluster cumulants.
- [`ch09_04_tensor_gauge_beyond_positivity.ipynb`](notebooks/ch09/ch09_04_tensor_gauge_beyond_positivity.ipynb) — tensor gauge beyond positivity.

### ch10: Graphical Model Learning

- [`ch10_01_chow_liu_structure_learning.ipynb`](notebooks/ch10/ch10_01_chow_liu_structure_learning.ipynb) — chow liu structure learning.
- [`ch10_02_local_learning_estimators.ipynb`](notebooks/ch10/ch10_02_local_learning_estimators.ipynb) — local learning estimators.
- [`ch10_03_hidden_variables_em_and_cd.ipynb`](notebooks/ch10/ch10_03_hidden_variables_em_and_cd.ipynb) — hidden variables em and cd.

### ch11: Applications: Structure as the Common Language

- [`ch11_01_particle_tracking_matching.ipynb`](notebooks/ch11/ch11_01_particle_tracking_matching.ipynb) — particle tracking matching.
- [`ch11_02_ldpc_decoding.ipynb`](notebooks/ch11/ch11_02_ldpc_decoding.ipynb) — ldpc decoding.
- [`ch11_03_ksat_factor_graph.ipynb`](notebooks/ch11/ch11_03_ksat_factor_graph.ipynb) — ksat factor graph.
- [`ch11_04_robot_path_factor_graph.ipynb`](notebooks/ch11/ch11_04_robot_path_factor_graph.ipynb) — robot path factor graph.
- [`ch11_05_infrastructure_gaussian.ipynb`](notebooks/ch11/ch11_05_infrastructure_gaussian.ipynb) — infrastructure gaussian.
- [`ch11_06_independent_cascade.ipynb`](notebooks/ch11/ch11_06_independent_cascade.ipynb) — independent cascade.
- [`ch11_07_crf_sequence.ipynb`](notebooks/ch11/ch11_07_crf_sequence.ipynb) — crf sequence.

### ch12: Maximum A-Posteriori Problems

- [`ch12_01_submodularity_and_map_lp.ipynb`](notebooks/ch12/ch12_01_submodularity_and_map_lp.ipynb) — submodularity and map lp.
- [`ch12_02_tum_network_flow.ipynb`](notebooks/ch12/ch12_02_tum_network_flow.ipynb) — tum network flow.
- [`ch12_03_tightening_map_lp.ipynb`](notebooks/ch12/ch12_03_tightening_map_lp.ipynb) — tightening map lp.

### ch13: Soft Inference Problems

- [`ch13_01_permanent_and_bethe.ipynb`](notebooks/ch13/ch13_01_permanent_and_bethe.ipynb) — permanent and bethe.
- [`ch13_02_gaussian_bp_and_walk_summability.ipynb`](notebooks/ch13/ch13_02_gaussian_bp_and_walk_summability.ipynb) — gaussian bp and walk summability.
- [`ch13_03_planar_zero_field_ising.ipynb`](notebooks/ch13/ch13_03_planar_zero_field_ising.ipynb) — planar zero field ising.
- [`ch13_04_two_level_ising_control.ipynb`](notebooks/ch13/ch13_04_two_level_ising_control.ipynb) — two level ising control.

### ch14: Advanced Structure Learning: Orders, DAGs, and Sparse Graphical Models

- [`ch14_01_order_mcmc_bayesian_networks.ipynb`](notebooks/ch14/ch14_01_order_mcmc_bayesian_networks.ipynb) — order mcmc bayesian networks.
- [`ch14_02_continuous_dag_notears.ipynb`](notebooks/ch14/ch14_02_continuous_dag_notears.ipynb) — continuous dag notears.
- [`ch14_03_graphical_lasso_sparse_precision.ipynb`](notebooks/ch14/ch14_03_graphical_lasso_sparse_precision.ipynb) — graphical lasso sparse precision.

### ch15: Neuralizing Graphical Models: Learned Factors, Messages, Operators, and Corrections

- [`ch15_01_bp_warm_start.ipynb`](notebooks/ch15/ch15_01_bp_warm_start.ipynb) — bp warm start.
- [`ch15_02_learned_bp_residual.ipynb`](notebooks/ch15/ch15_02_learned_bp_residual.ipynb) — learned bp residual.

### ch17: Structured Generative Processes: From Static Factors to Space-Time Graphs

- [`ch17_01_three_compositions_gaussian.ipynb`](notebooks/ch17/ch17_01_three_compositions_gaussian.ipynb) — three compositions gaussian.

## Chapters without companion notebooks yet

The current public snapshot does not yet contain dedicated notebooks for Chapter 16 (hidden variables / variational learning / amortized inference) or Chapters 18–21 (structured diffusion, bridges/Feynman–Kac generation, structured autoregressive/discrete generation, and synthesis). These are priority areas for Fall 2026 development.

## Reproducibility convention

Each notebook is intended to be self-contained or chapter-local, with figures written to `figs/`. Exact/certified reference calculations should be clearly distinguished from approximate or learned quantities. For approximate/learned methods, new examples should include a controlled success/crossover/failure analysis whenever feasible.
