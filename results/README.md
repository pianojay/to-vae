# Saved results and figures

| Group | Contents |
| --- | --- |
| [interpolation](interpolation/) | Base-design examples, VAE reconstructions, target examples, and k-NN comparison outputs |
| [simp](simp/) | Grouped figures for the earlier mesh-resolution datasets |
| [sweeps](sweeps/) | Figures for the four volume-fraction sweeps |
| [earlier_vae](earlier_vae/) | Original `vae_output_*` reconstructions, latent-space samples, and figures |

## Examples from the final study

- [Base-design example grid](<interpolation/sample_a(example).png>).
- [Base VAE reconstructions, β=0.5](interpolation/sample_a/reconstructed_beta_0_5.png).
- Saved comparison figures for [k=1](interpolation/sample_b_beta_0.5/knn_1/),
  [k=3](interpolation/sample_b_beta_0.5/knn_3/),
  [k=5](interpolation/sample_b_beta_0.5/knn_5/), and
  [k=10](interpolation/sample_b_beta_0.5/knn_10/).

Within the comparison groups, `sample_b_order` records reference densities and
`sample_b_rest` records decoded densities. `output.png` contains a saved evaluation
plot. The [final-report summary](../research/final-study.md#reported-findings)
provides the original interpretation and qualifications.

CSV reconstructions are results rather than source training inputs, so they are
kept here alongside their figures. Figures were not regenerated and matrices were
not recomputed during organization. Original names, including some legacy `.png`
filenames with no descriptive stem, remain in place within their groups.
