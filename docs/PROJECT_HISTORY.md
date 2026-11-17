# Project history

This archive brings together several stages of a project undertaken through the
**2024 Summer/Fall KAIST Undergraduate Research Program (URP)**.
The changing methods explain the mixture of datasets, VAE notebooks, PPO
prototypes, and interpolation experiments.

## Original direction: reinforcement learning in latent space

The proposal was titled **Reinforcement Learning based Topology Optimization
utilizing VAE Latent Vectors**. Its idea was to compress a design with a VAE,
let a reinforcement-learning agent modify the latent vector, decode it, and
use structural compliance to evaluate the change.

Early work generated SIMP designs for several support/load configurations and
mesh sizes. VAE experiments then investigated reconstruction and small latent
spaces, including two-dimensional examples that could be explored visually.
The [earlier VAE notebooks](../notebooks/earlier_vae/) and saved
[input](../data/earlier_vae/) / [output](../results/earlier_vae/) folders belong
to this phase.

Week-five notes describe an actor–critic/PPO prototype for a Michell truss. They
record that the agent and environment had been implemented but were not fully
integrated with the pretrained VAE. The [RL notebooks](../notebooks/rl_prototypes/)
and [demo sketch](../code/demo.txt) document this direction, rather than the
final method. Sources: [proposal](../research/SOURCES.md#s05),
[week three](../research/SOURCES.md#s13), [week four](../research/SOURCES.md#s14),
and [week five](../research/SOURCES.md#s15).

In a [retrospective account given during archiving](../research/READING_INFLUENCES.md#researcher-recollection-why-the-rl-direction-was-dropped),
the researcher explained that he dropped the RL direction because his understanding
of reinforcement learning at the time was not yet sufficient to carry it through.
This personal explanation complements the weekly record of an incomplete prototype.

## Later direction: interpolate between known designs

Later research notes discuss using existing optimized designs to estimate a
solution for new conditions. Candidate methods included splines, Gaussian
processes, and nearest neighbors. The [September notebook](../notebooks/earlier_vae/topo_VAE_0925.ipynb)
and [Gaussian-process example](../code/gp_demo.py) reflect this exploratory work.

The final report, **Topology Optimization Utilizing VAE Latent Vector**, focuses
on a VAE + k-NN workflow. It uses a 64×32 simply supported beam with varying load
location, angle, and volume fraction. Neighbors are found in problem-condition
space; their latent vectors are averaged and decoded.

The [final notebook](../notebooks/final_interpolation/topo_VAE_interpolation.ipynb)
connects base designs, a 16-dimensional VAE, target samples, and compliance
comparisons. Earlier work remains alongside it as development history.
Sources: [later notes](../research/SOURCES.md#s07) and
[submitted final report](../research/SOURCES.md#s16).

## Final study and archive

The report describes 10,000 base designs and 2,500 target cases, comparing
nearest-neighbor counts of 1, 3, 5, and 10. It reports many compliance ratios near
one and worsening extreme errors with larger neighbor counts. The discussion
considers reconstruction blur, possible overfitting, and nonlinear latent-space
structure as explanations, rather than established diagnoses.

The [workshop abstract](../research/abstract-summary.md) presents the same final
method. The [final-report summary](../research/final-study.md) explains its
settings and findings in more detail.

The original repository's last commit is dated December 27, 2024. The archive
organization and summaries were added in November 2026. The researcher confirmed
participation in the **2024 Summer/Fall** program; that identification is used
throughout the archive.
