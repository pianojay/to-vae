# Reference papers and reading record

The research records contain both a final-report bibliography and saved digital
papers. This page makes those references discoverable alongside the code archive.
The [paper inventory](paper-inventory.tsv) identifies saved PDFs, their original
ZIP locations, sizes, hashes, and byte-identical copies. The PDFs themselves
remain in the owner's external collection; this repository records their context
and availability.

## Final-report references

Titles and years below follow the [submitted final report](../research/SOURCES.md#s16).
This is the historical reading record, rather than a newly standardized bibliography.
“Found” means a corresponding title was located in the digital collection; it
does not establish which particular PDF version was cited.

| Reference | Role in the study | Digital copy located |
| --- | --- | --- |
| Bendsøe and Sigmund, *Topology Optimization: Theory, Methods and Applications* (2003) | Structural/topology-optimization background | Found in `Desktop.zip`, under `misc/` |
| Woldseth et al., *On the Use of Artificial Neural Networks in Topology Optimisation* (2022) | Context and evaluation of neural methods for topology optimization | Found under `Review & Educational/` |
| Guo et al., *An Indirect Design Representation for Topology Optimization Using Variational Autoencoder and Style Transfer* (2018) | VAE compression as a representation for structural designs | Two similarly titled files under `VAE/` |
| Gladstone et al., *Robust Topology Optimization Using Variational Autoencoders* (2021) | Related latent-space structural optimization | Found under `VAE/` |
| *Latent Crossover for Data-Driven Multifidelity Topology Design* (2024) | Related use of latent representations in design search | Found under `VAE/` |
| Andreassen et al., *Efficient Topology Optimization in MATLAB Using 88 Lines of Code* (2011) | SIMP implementation background | Found under `Review & Educational/`, with an identical copy under `HomeDesktop/` |
| *Auto-Encoding Variational Bayes* (2013) | VAE foundation | No corresponding titled PDF located in this search |
| *beta-VAE: Learning Basic Visual Concepts with a Constrained Variational Framework* (2017) | β-weighted latent regularization | No corresponding titled PDF located in this search |

The last two entries are recorded references even though matching standalone
PDFs were not found. Their absence from the inventory does not mean they were
never read or that no copy exists elsewhere.

## Earlier research directions

The saved collection also documents the project's broader exploration:

- **Solver and implementation references:** *A 99 Line Topology Optimization Code
  Written in Matlab*; *A 55-Line Code for Large-Scale Parallel Topology Optimization
  in 2D and 3D*; *Open-Source Codes of Topology Optimization: A Summary for Beginners
  to Start Their Research*; *Neural Reparameterization Improves Structural Optimization*.
- **Reinforcement learning for topology design:** *Deep Reinforcement Learning for
  Engineering Design through Topology Optimization of Elementally Discretized Design
  Domains*; *Generative Design by Using Exploration Approaches of Reinforcement
  Learning in Density-Based Structural Topology Optimization*; *On the Quest to
  Achieve Fast Generalizable Topology Optimization with Reinforcement Learning*;
  *Generative Design by Reinforcement Learning: Enhancing the Diversity of Topology
  Optimization Designs*.
- **Representation learning and RL:** *World Models*, *DARLA: Improving Zero-Shot
  Transfer in Reinforcement Learning*, latent-dynamics and state-abstraction papers,
  and other exploratory reading preserved under the original `misc/` paths.
- **Later surrogate-model exploration:** *Characterising Harmful Data Sources When
  Constructing Multi-Fidelity Surrogate Models* and *Multi-Fidelity Cost-Aware
  Bayesian Optimization*, saved under `Other 추천/` and also as publisher-named
  files in the URP folder.

These are supporting reading, not claims that every paper's method was implemented
or used in the final study. The [development notes](../research/development-notes.md)
explain the transition from RL to interpolation.

## Where the digital material was found

The original collection is `/mnt/DD/24-2 Bellis/URP/`, chiefly `Desktop.zip`.
Within that ZIP, the relevant groups include `VAE/`, `Review & Educational/`,
`misc/`, `HomeDesktop/`, and `Other 추천/`. These are provenance labels, not
required filesystem dependencies for reading this archive.

The inventory was assembled from PDF filenames and file hashes. It does not claim
full bibliographic verification or a complete inventory of a physical paper stash.
