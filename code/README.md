# Original Python sources

The original top-level scripts are retained here without content changes.

- [topopt_cholmod.py](topopt_cholmod.py): SIMP/optimality-criteria solver and CSV output.
- [bc_options.py](bc_options.py): boundary-condition classes and load helpers.
- [VAE.py](VAE.py): shared fully connected VAE model.
- [FEA_Comp.py](FEA_Comp.py): compliance evaluation used by the notebooks.
- [csv2fig.py](csv2fig.py): saved-density plotting helper.
- [main.py](main.py): earlier parameter-sweep driver.
- [FEA_compliance.py](FEA_compliance.py): earlier experiment with an OC update.
- [demo.py](demo.py) and [demo.txt](demo.txt): conceptual RL loop with placeholders.
- [gp_demo.py](gp_demo.py): standalone Gaussian-process illustration.

The solver headers credit Niels Aage and Villads Egede Johansen (2013, updated
2016). Existing attribution is preserved. Reference baselines are under
[references/code](../references/code/).

These files are historical implementation, not runnable entrypoints promised by
this archive. Original interfaces and relative paths were not repaired. See the
[archive notes](../docs/ARCHIVE_NOTES.md#historical-paths-and-execution).
