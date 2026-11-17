# How the reading shaped the research

This record connects reading to decisions documented in the research notes.
A paper's presence in the collection or final bibliography does not by itself
show that it caused a decision. The links below distinguish documented uses,
comparisons, and questions the available records do not answer.

## Documented connections

### Combining design compression with reinforcement learning

The July 9 direction slides place two ideas together:

- Brown et al.'s *Deep Reinforcement Learning for Engineering Design through
  Topology Optimization of Elementally Discretized Design Domains*: the notes
  describe an agent removing material and using compliance as feedback, along
  with difficulty scaling a grid-based representation.
- Guo et al.'s *An Indirect Design Representation for Topology Optimization Using
  Variational Autoencoder and Style Transfer*: the notes describe compressing
  topology while preserving useful information.

The slides explicitly combine these into a proposal to use VAE dimension
reduction for RL-based topology optimization. This supports a concrete influence:
**the proposed agent would operate on a compressed design rather than directly
on all grid elements**. It does not establish that either paper supplied the
specific PPO algorithm or the eventual network architecture.

Evidence: [July direction slides, numbered slides 1–3](SOURCES.md#s03).
The [week-five notes](SOURCES.md#s15) also name the 2022 RL paper as a prototype
reference, but do not establish line-by-line code derivation.

### World Models as a contemporary VAE-and-control reference

The 2024 research-direction slide deck explicitly lists **World Models (2018)**,
attributed there to David Ha et al., under a section on VAE × RL in AI. The slide
summarizes three components: V for vision/compression using a VAE, M for RNN-based
memory, and C for control. Its introductory point is to compress the situation
with a VAE so an RL agent can make decisions more efficiently.

This records World Models as a **conceptual reference for combining learned
representations with control during the original research**, beyond its presence
in the saved PDF collection. It does not establish adoption of the paper's RNN
memory component in the topology prototype. The same slide also discusses DARLA
and variational state encoding as related representation-learning/RL work.

Evidence: [research-direction slides, section “VAE x RL”, numbered slide 19](SOURCES.md#s03).
The saved PDF is recorded in the [paper inventory](../references/paper-inventory.tsv)
as `misc/no(no)/VAE + RL (any)/Pure/World Models.pdf` inside `Desktop.zip`.

### Implementing the VAE and questioning its generality

Week-four notes explicitly identify the 2018 *An Indirect…* paper as a reference
for compressing topology with a VAE, then describe the implemented model and
reconstruction experiments. This connects Guo et al.'s representation idea to
**the early VAE experiments**, beyond its appearance in the bibliography.

Those notes also compare the limited range of the early model to a restricted
loading example in *Robust Topology Optimization Using Variational Autoencoders*.
The recorded takeaway is that broader generalization would require more varied
data. The earlier July slides also list that paper as an example of low-dimensional
latent optimization with a compliance surrogate. The evidence supports a
**comparison and motivation concerning generalization**, not adoption of its
complete optimization procedure.

Evidence: [week-four notes, opening and evaluation/future-plan sections](SOURCES.md#s14)
and [July slides, numbered slide 5](SOURCES.md#s03).

### Thinking about evaluation and problem families

Week-three notes discuss *Neural Reparameterization Improves Structural
Optimization* and its collection of test problems while considering which
boundary conditions to study. Nearby notes narrow the initial problem family
to beams on rectangular domains. This documents **benchmark/problem-selection
context**, but does not prove that the paper alone caused that restriction.

The July slides' 2022 review discussion emphasizes physical performance,
generalization, and legitimacy of a solver. This records the evaluation concerns
being considered; it does not show that all proposed checks were implemented.

Evidence: [week-three notes, boundary-condition discussion](SOURCES.md#s13)
and [July slides, numbered slide 8](SOURCES.md#s03).

### Moving toward interpolation between existing designs

Later editable notes begin with a discussion with the teaching assistant and a
reflection after a seminar. They contrast prior low-dimensional optimization
and “latent crossover” with the project's emerging aim: use existing optimized
designs to find a design for different conditions. This supports **a recorded
reframing through discussion and comparison with prior work**. The notes do not
identify a precise date or one paper as the cause of ending the RL direction.

The same notes compare candidate interpolators and describe scaled, weighted
k-NN as appealing because it is inexpensive compared with alternatives. The
final report likewise motivates k-NN by local consistency and computational
cost. Thus, **the recorded reason for choosing k-NN is available**, even though
an originating paper for that choice is not established.

Evidence: [later editable notes, opening discussion and interpolation sections](SOURCES.md#s07)
and [final report, section 4.2](SOURCES.md#s16).

## Researcher recollection: why the RL direction was dropped

In November 2026, while organizing this archive, the researcher explained that
his understanding of reinforcement learning in 2024 was not yet sufficient to
carry the proposed RL approach through. This was the reason he dropped that
direction. He continues to find the idea interesting. World Models also appears explicitly
in the original direction slides, as documented above.

This account supplies the personal reason for the change of direction. It is
retrospective testimony from the researcher, separate from the contemporaneous
weekly notes, which document the incomplete prototype. It does not establish a
precise date for the decision or an experimental assessment of the approach's
feasibility.

## Recorded reading with thinner decision evidence

The final report cites foundational VAE, β-VAE, SIMP, and topology-optimization
literature. The saved collection also contains broader RL, representation-learning,
and multifidelity papers. These are recorded as reading/background in the
[bibliography](../references/BIBLIOGRAPHY.md). Without a note connecting a paper
to a particular choice, this archive does not assign it a causal role.

For example, the final study's 16-dimensional latent space and β-labeled model
snapshots document settings, but do not explain why those values were selected.
A β-VAE citation alone cannot supply that missing explanation.

## Focused questions for the physical records

These are gaps in the historical account, not proposed research work:

| Question | What is already recorded | What a physical note or recollection could add |
| --- | --- | --- |
| When was the move away from RL made? | The researcher has clarified the reason: his understanding of RL was not yet sufficient to carry the approach through | A dated note locating the decision in the project timeline |
| Which readings most directly changed the later method? | Discussion of latent crossover, latent optimization, GP/BO, and alternative interpolators | Paper-specific annotations distinguishing an adopted idea from a comparison or rejected idea |
| Why choose latent dimension 16 and the β settings? | Final settings and named model snapshots | The original tradeoff, trial comparison, or recommendation behind those choices |
| What supplied implementation details? | Named conceptual references and preserved solver credits | Which tutorials, repositories, or paper algorithms supplied specific model/PPO details |

When additional material is available, record **the source, its date if known,
the idea taken from it, the resulting decision, and the affected experiment**.
Keep later researcher recollection labeled separately from contemporaneous
notes. Unanswered questions should remain unanswered rather than being filled
from what the final code happens to contain.
