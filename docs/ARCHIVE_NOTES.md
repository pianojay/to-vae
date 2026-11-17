# Archive notes

## Purpose and preservation

This branch consolidates and explains a completed research project. No research
extension or functional restoration is part of the archive work.

The unchanged original snapshot is on `original_backup`, commit
`b5fabb8e869eb6bb61dc3c2cb2fb9c6843e5e6a7`. On `main`, the original scripts,
retained notebooks and their outputs, datasets, model checkpoints, and supporting
files are preserved byte-for-byte at new locations. The original empty README
is replaced by the archive introduction. External research context is summarized
in Markdown; original report PDFs, editable files, submission forms, and
administrative paperwork are not imported.

Every one of the original **24,674 tracked paths** is recorded in the
[path manifest](path-manifest.tsv). It contains these dispositions:

| Disposition | Count | Meaning |
| --- | ---: | --- |
| `relocated` | 24,163 | Original content preserved at a new path |
| `consolidated_duplicate` | 505 | Identical snapshot retained at the recorded canonical path |
| `omitted_generated_cache` | 5 | Compiled Python `.pyc` files; source remains |
| `replaced_documentation` | 1 | The original one-byte README replaced by this archive's introduction |

## Duplicate snapshots

- The 504 files in original `Simple_64x32_3/` were identical to the corresponding
  files in `0.4_Simple_64x32_3/`. The latter is canonical; CSVs are under
  [sweep data](../data/sweeps/0.4_Simple_64x32_3/) and its figure is under
  [sweep results](../results/sweeps/0.4_Simple_64x32_3/).
- Original `latent_ppo(deprecated).ipynb` was identical to
  [latent_ppo.ipynb](../notebooks/rl_prototypes/latent_ppo.ipynb).

Other repeated values within scientific datasets are retained: different paths
can encode different experimental conditions. The reference MNIST directory
layout is also preserved, including repeated downloads. No Git history was
rewritten; all original files remain available on `original_backup`.

## Historical paths and execution

The new directory layout is intended for reading. Imports and relative paths
inside original scripts and notebooks still describe the old layout. Serialized
sample dictionaries may contain original sample paths or saved tensor objects;
they were not unpickled, rewritten, or used for inference.

To resolve an old relative path, find its `original_path` in the manifest and
read `current_path`. A consolidated duplicate points to the same destination as
its surviving original. Blank destinations identify omitted generated caches.
`original_blob` identifies the original Git content; SHA-256 and byte count
allow content comparisons without executing code. For the replaced README,
those fields describe the original README, not the new one.

The original environment was not locked. Source imports include NumPy, SciPy,
pandas, Matplotlib, tqdm, CVXOPT/CHOLMOD, PyTorch, and experiment-specific libraries
such as torchvision, scikit-learn, GPy, and torchrl. This is historical context,
not a verified dependency specification or installation procedure.

The notebooks include CUDA-specific calls, obsolete interfaces, incomplete
prototype cells, and output paths that overwrite saved artifacts. The earlier
batch driver and plotting utilities also retain their original interface issues.
Do not interpret their preservation as a claim that they run unchanged.

## How to read the findings

The summaries distinguish original observations from archival explanations.
Reported ratios below one are not presented as proof of a better constrained
optimum, and the old timing figures are not presented as a verified speedup.
Ambiguous result-table labels are retained as a qualification in the
[final-study summary](../research/final-study.md#reported-findings), without
turning them into a new research task.

## Checks performed

Only content hashes, file accounting, notebook JSON readability, documentation
links, and branch identities were checked. No source imports, GPU checks,
checkpoint loading, training, inference, finite-element solves, or functional
tests were performed for the archive. See the [integrity record](INTEGRITY.md).

Earlier exploratory code fixes and tests were exported outside this worktree
and are not included on `main`.
