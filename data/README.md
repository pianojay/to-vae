# Saved research data

| Group | Contents |
| --- | --- |
| [interpolation/sample_a](interpolation/sample_a/) | 10,000 base density CSVs |
| [interpolation/sample_b_beta_0.5](interpolation/sample_b_beta_0.5/) | 2,557 saved target density CSVs |
| [interpolation/sample_b](interpolation/sample_b/) | 30 earlier target density CSVs |
| [interpolation/mappings](interpolation/mappings/) | Three original pickle snapshots associating conditions, paths, and latent values |
| [simp](simp/) | Earlier datasets at five mesh sizes: 32×16, 32×32, 64×32, 96×32, 128×32 |
| [sweeps](sweeps/) | Four simply supported beam sweeps labeled by volume fraction |
| [earlier_vae](earlier_vae/) | Six original `vae_input_*` dataset combinations |

Density matrices use `(nelx, nely)` array shape and are transposed for visualization.
The report describes 2,500 target cases; all 2,557 saved target CSVs are preserved
without inferring which belong to that evaluation. Reconstructions, comparison
matrices, and figures are under [results](../results/README.md).

Pickles were retained without loading them. Embedded file paths, tensor devices,
and Python-object representations remain historical; use the
[path manifest](../docs/path-manifest.tsv) to resolve original relative paths.
File counts describe the archive, not a recovered training/evaluation split.
