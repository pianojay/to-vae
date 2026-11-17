# File guide

Paths below describe this organized archive. Historical names within experiment
groups are preserved. Use the [path manifest](path-manifest.tsv) when an original
notebook, report, or serialized object refers to a path from the old layout.

## Final interpolation study

| Material | Current location | Role |
| --- | --- | --- |
| Main notebook | [Final interpolation](../notebooks/final_interpolation/topo_VAE_interpolation.ipynb) | Sampling, β-VAE, interpolation, and compliance evaluation |
| Base designs | [sample_a](../data/interpolation/sample_a/) | 10,000 CSV design files |
| Target designs | [sample_b_beta_0.5](../data/interpolation/sample_b_beta_0.5/) | 2,557 saved root-level CSVs; not a claim that all belong to the reported 2,500-case evaluation |
| Earlier target samples | [sample_b](../data/interpolation/sample_b/) | 30 saved root-level CSVs |
| Sample dictionaries | [Mappings](../data/interpolation/mappings/) | Three `.pkl` snapshots, including base and target latent mappings |
| Checkpoints | [Models](../models/README.md) | Snapshots labeled by latent dimension or experiment |
| Reconstructions and comparisons | [Interpolation results](../results/interpolation/) | Original/reconstructed matrices, figures, and k-NN comparison grids |
| Report and context | [Research summaries](../research/README.md) | Human-readable explanation of the project and reported findings |

The notebook connects `(load location, load angle, volume fraction)` to designs
and latent vectors. Data filenames often come from hashes of those condition
tuples; the serialized dictionaries supply the historical associations. The
pickle contents were not loaded or rewritten during archiving.

## Shared code

All original top-level scripts now live together in [code/](../code/README.md).

| File | Purpose |
| --- | --- |
| [topopt_cholmod.py](../code/topopt_cholmod.py) | SIMP solver with CHOLMOD finite-element solves |
| [bc_options.py](../code/bc_options.py) | Supports, boundary conditions, load vectors |
| [VAE.py](../code/VAE.py) | Fully connected VAE definition |
| [FEA_Comp.py](../code/FEA_Comp.py) | Notebook compliance evaluator (`fea_c`) |
| [csv2fig.py](../code/csv2fig.py) | Grid visualization of density CSVs |
| [main.py](../code/main.py) | Earlier parameter sweep, distinct from the final notebook's random sampler |
| [FEA_compliance.py](../code/FEA_compliance.py) | Earlier compliance/OC-update experiment |
| [demo.py](../code/demo.py), [demo.txt](../code/demo.txt) | Conceptual VAE/agent/compliance loop |
| [gp_demo.py](../code/gp_demo.py) | Standalone Gaussian-process example |

These are historical sources. The organizer did not repair their interfaces or
adapt them to the new filesystem layout.

## Earlier experiments

| Material | Current location |
| --- | --- |
| VAE reconstruction / latent exploration and September interpolation | [Earlier VAE notebooks](../notebooks/earlier_vae/) |
| PPO and actor–critic prototypes | [RL notebooks](../notebooks/rl_prototypes/) |
| Mesh-resolution SIMP datasets | [SIMP data](../data/simp/) and [figures](../results/simp/) |
| Simply supported beam load-angle / volume sweeps | [Sweep data](../data/sweeps/) and [figures](../results/sweeps/) |
| Earlier VAE inputs and outputs for six dataset combinations | [Inputs](../data/earlier_vae/) and [outputs](../results/earlier_vae/) |
| Reference examples, original baseline solver, demos, and MNIST data | [References](../references/README.md) |

Structural labels include `Simple` (simply supported beam), `Bridge`, `Cantil`
(cantilever), `MBB`, and `MTruss` (Michell/Prager truss). In generated folder names,
`64x32` denotes the grid dimensions; the final side index uses `0=right`, `1=top`,
`2=left`, `3=bottom`. A prefix such as `0.4_` labels volume fraction in the sweeps.

## Data conventions

- Density CSVs use shape `(nelx, nely)` and are transposed for display. Values near
  zero represent void; values near one represent solid material.
- Sweep filenames such as `1154_6_8.csv` encode a load-node index, angle index,
  and number of angle samples. The final-study sampler uses hashed condition
  tuples instead.
- `beta` identifies the weight on VAE latent-distribution regularization;
  `knn` identifies nearest-neighbor interpolation.
- Checkpoint and folder names are historical labels, not complete run provenance.
  The [model guide](../models/README.md) distinguishes the saved snapshots.
