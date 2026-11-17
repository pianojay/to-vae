# Notebooks by research stage

| Notebook | Role |
| --- | --- |
| [Final interpolation study](final_interpolation/topo_VAE_interpolation.ipynb) | Main record of sampling, β-VAE, condition-space k-NN interpolation, and compliance comparison |
| [Earlier VAE](earlier_vae/topo_VAE.ipynb) | Reconstruction and latent-space exploration |
| [September experiments](earlier_vae/topo_VAE_0925.ipynb) | Earlier interpolation experiments, including splines |
| [Early PPO](rl_prototypes/latent_ppo.ipynb) | Initial latent-space reinforcement-learning prototype |
| [Later PPO prototype](rl_prototypes/latent_ppo_.ipynb) | Later actor–critic/environment work; not the final interpolation method |

The original `latent_ppo(deprecated).ipynb` was identical to the retained early
PPO notebook and is accounted for in the [path manifest](../docs/path-manifest.tsv).
Two reference notebooks remain with the [reference code](../references/code/).

All retained notebook files, including saved outputs and execution counters, are
unchanged. Their imports, intermediate cells, CUDA assumptions, and relative
paths reflect the old layout. Browse them as research records; this archive does
not provide a restart-and-run-all workflow. For context, read the
[project history](../docs/PROJECT_HISTORY.md).
