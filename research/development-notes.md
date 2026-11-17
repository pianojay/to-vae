# Development notes: from RL proposal to interpolation study

This summary connects the proposal, weekly notes, and later research notes to
the material in the repository. It describes the work as recorded at each stage;
ideas listed as plans in old notes are not assumed to have been completed.
[Reading influences](READING_INFLUENCES.md) separates documented connections
between papers and decisions from citations whose influence is not established.

## Proposal and early direction

The proposal's title was **Reinforcement Learning based Topology Optimization
utilizing VAE Latent Vectors**. The goal was to reduce a high-dimensional design
to a small latent vector, then train an agent to change that vector. A finite-element
compliance calculation would provide feedback on the decoded design.

The early direction notes contrast element-by-element design changes with
learning to explore a compressed representation. They also discuss generalization
across loads, supports, and domain dimensions as research concerns.
Sources: [proposal](SOURCES.md#s05), [July direction notes](SOURCES.md#s03),
and [midterm record](SOURCES.md#s04).

## Dataset generation

Week-three notes describe the Python SIMP generator and boundary-condition
classes, including simply supported beams, bridges, cantilevers, MBB beams,
Michell beams, and Michell/Prager trusses. Design densities were saved as CSVs
and grouped figures were used for visual inspection.

The notes describe multiple rectangular grid sizes and initial settings such as
volume fraction 0.4, filter radius 2, and penalization 3. They record that finite-element
data generation was kept on the CPU after experiments with GPU transfers.
The [SIMP data](../data/simp/), [figures](../results/simp/),
[solver](../code/topopt_cholmod.py), and [boundary conditions](../code/bc_options.py)
preserve this work. Source: [week three](SOURCES.md#s13).

## VAE reconstruction and exploration

Week-four notes describe a fully connected VAE with a two-dimensional latent
space, trained for 200 epochs with batch size 32. Six input combinations were
explored: simple beam, bridge, simple+bridge, cantilever, Michell truss, and
cantilever+Michell truss. The notes describe successful visual reconstruction of
training examples along with blur in thin features.

The [earlier notebooks](../notebooks/earlier_vae/),
[input datasets](../data/earlier_vae/), and
[reconstruction outputs](../results/earlier_vae/) show these experiments. These
early settings differ from the final study's 16-dimensional VAE.
Source: [week four](SOURCES.md#s14).

## RL prototype

Week-five notes describe an actor–critic/PPO design. The actor changes a latent
vector, while the critic estimates reward. The notes use a 64×32 Michell truss,
a two-dimensional latent space, and compliance before/after a latent change as
an illustrative comparison.

They explicitly record that the RL agent/environment and the pretrained VAE had
not been completed as one integrated workflow. The archive therefore labels the
[RL notebooks](../notebooks/rl_prototypes/) and
[demo sketch](../code/demo.txt) as prototypes, not the final method.
Source: [week five](SOURCES.md#s15).

The researcher later clarified that he dropped the RL approach because his
understanding of RL at the time was not yet sufficient to realize it. This is
recorded separately as a [retrospective account](READING_INFLUENCES.md#researcher-recollection-why-the-rl-direction-was-dropped),
rather than attributed to the original weekly notes.

## Transition toward interpolation

Later editable notes discuss using existing optimal designs to estimate an
optimum for different conditions. They narrow the problem to a 64×32 simply
supported beam and three variables: load location, angle, and volume fraction.

Candidate interpolation techniques include RBFs, Gaussian processes, splines,
neural approximations, and k-NN. The notes describe a dictionary mapping each
condition tuple to its sample path and latent vector. They also outline the
10,000-base / 2,500-target workflow ultimately described by the final report.

The [September interpolation notebook](../notebooks/earlier_vae/topo_VAE_0925.ipynb)
and [GP example](../code/gp_demo.py) are retained as exploration. The
[final notebook](../notebooks/final_interpolation/topo_VAE_interpolation.ipynb)
and [final-study summary](final-study.md) describe the later k-NN method.
Sources: [later notes](SOURCES.md#s07), [method draft](SOURCES.md#s09), and
[final report](SOURCES.md#s16).
