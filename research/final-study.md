# Final study: topology prediction through latent interpolation

**Topology Optimization Utilizing VAE Latent Vector**

**VAE 잠재 벡터를 활용한 위상최적화**

Jaeuk Kim, Department of Mechanical Engineering, KAIST. Advisor: Ikjin Lee.
Teaching assistant: Jihwan Park. This summary draws primarily on the
[submitted final report](SOURCES.md#s16), its [editable draft](SOURCES.md#s06),
and the [workshop abstract](SOURCES.md#s01). The draft is dated December 27, 2024.

## Research question

Can optimized structures already computed for one set of conditions help predict
a useful design for a new set of conditions, without repeating the full numerical
optimization? The study combines compression of structural designs with local
interpolation between examples.

**Topology optimization** distributes material within a domain to meet a
mechanical objective. In this project, the reference designs minimize compliance
using SIMP (Solid Isotropic Material with Penalization). A **VAE** learns a short
numerical representation, or latent vector, for each density image.

The original proposal used reinforcement learning to modify latent vectors.
The final report instead studies k-NN interpolation. See the
[development notes](development-notes.md) for that progression.

## Problem and settings

| Item | Setting described by the report |
| --- | --- |
| Design domain | 64×32 element grid |
| Supports | Simply supported beam: pin at the bottom-left, vertical support at the bottom-right allowing horizontal motion |
| Varied conditions | Load location `l`, load angle `theta`, volume fraction `v` |
| Location index | Integer 0–63, mapped in the sampler to node `65 + 33*l` |
| Angle | A full turn, sampled from 0 to 2π radians |
| Volume fraction | 0.2–0.8 |
| SIMP parameters | Penalization 3, filter radius 2, `ft=1` |
| Base / target dataset sizes | 10,000 / 2,500 designs, as reported |
| VAE | Fully connected, 16-dimensional latent space |
| Layer widths | 2048 → 512 → 256 → 16 → 256 → 512 → 2048 |
| Training | Adam, 1,000 epochs, binary cross-entropy plus β-weighted KL divergence |
| Neighbor counts compared | 1, 3, 5, 10 |

The report calls `ft` a threshold factor; in the preserved solver `ft=1` selects
density filtering. The VAE implementation uses separate mean/log-variance heads,
ReLU hidden activations, and a sigmoid decoder output. Model snapshots include
a β=0.5 label, but filenames do not identify every setting of every saved run.

## Procedure

1. **Create reference designs.** Sample problem conditions and use SIMP to obtain
   the base designs. The base-design dictionary associates each condition tuple
   with a design file.
2. **Learn the representation.** Train the VAE on the density images. Encode the
   base designs and associate their conditions with latent vectors.
3. **Find comparable problems.** Normalize load position, angle, and volume
   fraction to comparable ranges. For a target condition, find its nearest
   neighbors in this normalized **condition space**, not in latent space.
4. **Interpolate and decode.** Weight the neighbors' latent vectors by inverse
   distance, using `1 / (distance + 1e-8)` and normalizing the weights. Decode
   their weighted average into a predicted density matrix. At `k=1`, this retrieves
   one neighbor's code rather than averaging several codes.
5. **Compare mechanical behavior.** Evaluate the predicted and reference designs
   under the same target load/support conditions. The report uses the ratio
   `predicted compliance / reference compliance`.

The [final notebook](../notebooks/final_interpolation/topo_VAE_interpolation.ipynb)
contains the sampling, training, interpolation, and comparison record.
[Base data](../data/interpolation/sample_a/), [target data](../data/interpolation/sample_b_beta_0.5/),
[mappings](../data/interpolation/mappings/), [checkpoints](../models/README.md), and
[saved outputs](../results/interpolation/) are retained separately by role.

## Reported findings

The report describes many predicted designs with compliance ratios near one.
Its comparisons of `k=1, 3, 5, 10` show more severe high-compliance outliers with
larger neighbor counts; averaging more latent vectors did not provide a clear
advantage in this experiment. The discussion offers possible explanations:
latent-space nonlinearity, possible VAE overfitting, and blurred reconstructions.
These are the report's interpretations, not separately established causes.

The result table and surrounding prose use overlapping ratio-column labels and
ambiguous “solutions” counts. This archive therefore does not turn those counts
into an accuracy percentage or solver-success rate. Likewise, a ratio below one
is not treated as proof of a better constrained optimum: equal material-volume
constraints on the decoded and reference designs were not established by this
archival review. The reported run timings are not presented as a verified speedup.

The conclusions are best read as observations from the original exploratory
study. No numerical results were recomputed when this archive was organized.

## Relationship to the saved files

The base folder contains 10,000 root-level CSVs, matching the stated base-data
size. The β=0.5 target folder contains 2,557 root-level CSVs, while the report
states 2,500 evaluated cases. The folder is retained in full; file count alone
is not used to infer the membership of the reported evaluation.

Saved k-NN result folders contain figures and example original/reconstructed
matrices. They are supporting artifacts, not a newly reconstructed table of all
case-level metrics. Checkpoint and pickle contents were not loaded during
archiving. Original notebook cells and outputs remain unchanged, including
intermediate cells and historical path references.
