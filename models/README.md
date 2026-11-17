# Saved model checkpoints

| File | Historical label / context |
| --- | --- |
| [vae_16.pth](vae_16.pth) | 16-dimensional VAE experiment |
| [vae_16_beta_0_5.pth](vae_16_beta_0_5.pth) | 16-dimensional β=0.5 experiment referenced by the final notebook |
| [vae_4.pth](vae_4.pth) | Four-dimensional VAE experiment |
| [vae_model_mtruss.pt](vae_model_mtruss.pt) | Michell-truss VAE referenced by earlier reconstruction and RL notebooks |

These labels come from filenames and notebook references. They do not establish
complete training provenance or guarantee the exact final-report run.

The notebooks use both whole-model serialization and state-dictionary patterns.
The original model definition is [code/VAE.py](../code/VAE.py). Checkpoint bytes
are unchanged; they were not loaded, converted, or tested during archiving.
