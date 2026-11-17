# Topology Optimization Utilizing VAE Latent Vector

**VAE 잠재 벡터를 활용한 위상최적화**

A research archive of a **2024 KAIST undergraduate project** by **Jaeuk Kim**,
Department of Mechanical Engineering. Advisor: **Ikjin Lee**. Teaching assistant:
**Jihwan Park**.

The project explored whether previously optimized structures could help predict
new designs without repeating the full optimization process. A variational
autoencoder (VAE) compresses structural designs into short numerical vectors;
nearest-neighbor interpolation combines these representations for a new set of
loading and material conditions.

This repository brings the original code and saved results together with readable
summaries of the project's reports and research notes. It preserves the completed
study and its earlier experiments. **The code is historical reference material;
execution and scientific results have not been revalidated during archiving.**

## Start here

1. Read the [final-study summary](research/final-study.md) for the problem,
   method, settings, and reported findings.
2. Read the [project history](docs/PROJECT_HISTORY.md) to understand the shift
   from reinforcement-learning prototypes to the final interpolation study.
3. Use the [file guide](docs/FILE_GUIDE.md) to connect the explanations to
   notebooks, datasets, models, and results.
4. Browse the [main notebook](notebooks/final_interpolation/topo_VAE_interpolation.ipynb)
   and its preserved outputs for the implementation record.

## The idea

**Topology optimization** finds a distribution of material that performs well
under specified loads and supports. Here, a numerical method called **SIMP**
generated examples on a 64×32 grid. The final study varied load position, load
direction, and material volume fraction.

```text
10,000 SIMP designs → train VAE → map problem conditions to 16-number latent vectors
                                              ↓
New problem conditions → find similar conditions → average their latent vectors
                                              ↓
                                   decode a predicted design
                                              ↓
                             compare its compliance with SIMP
```

**Compliance** measures structural flexibility under a load. Lower compliance
means a stiffer structure when other constraints are equal. The report compares
predicted and reference compliance for 2,500 target cases and nearest-neighbor
counts of 1, 3, 5, and 10. It reports many ratios near one and more severe outliers
as more latent vectors are averaged. These are the original study's observations;
the [summary](research/final-study.md#reported-findings) retains their context.

![Saved examples from the base-design dataset](<results/interpolation/sample_a(example).png>)

*An original example figure, retained from the research snapshot.*

## Archive layout

| Directory | Contents |
| --- | --- |
| [research/](research/README.md) | Markdown summaries of the final report, abstract, and development notes; source catalogue |
| [docs/](docs/README.md) | History, file guide, archive limitations, and original-to-current path manifest |
| [code/](code/README.md) | Original Python solver, VAE, compliance, plotting, and prototype scripts |
| [notebooks/](notebooks/README.md) | Final interpolation study, earlier VAE experiments, and RL prototypes |
| [data/](data/README.md) | SIMP datasets, VAE inputs, sampled designs, and serialized mappings |
| [models/](models/README.md) | Four original model checkpoints |
| [results/](results/README.md) | Saved figures, reconstructed densities, and comparison outputs |
| [references/](references/README.md) | Existing reference code, demo material, and MNIST example data |

## Preservation and use

The original snapshot is preserved on **`original_backup`** at commit
`b5fabb8e869eb6bb61dc3c2cb2fb9c6843e5e6a7`. This **`main`** branch organizes it for
reading. Code, retained notebooks (including outputs), datasets, and model files
are unchanged in content; their locations have changed. Exact duplicate snapshots
are consolidated, with every original path accounted for in the
[path manifest](docs/path-manifest.tsv).

The original environment was not locked. Notebook cells contain historical
imports, CUDA assumptions, and paths relative to the old layout; some overwrite
saved outputs. **This layout is for browsing, not a ready-to-run package.**
See the [archive notes](docs/ARCHIVE_NOTES.md) for the preservation policy and
path conventions. No GPU, model training, inference, solver runs, or functional
tests were used to validate this archive.
