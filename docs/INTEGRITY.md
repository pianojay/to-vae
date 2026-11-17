# Archive integrity record

Organization date: **2026-11-17**. Original snapshot:
`b5fabb8e869eb6bb61dc3c2cb2fb9c6843e5e6a7` on `original_backup`.

The checks for this reorganization concern preservation and navigation only.
They do not execute or validate the research implementation.

| Check | Result |
| --- | --- |
| Original branch and checkout | Original commit retained; checkout clean on `original_backup` |
| Original tracked paths accounted for | 24,674 / 24,674 |
| Original contents preserved at relocated destinations | 24,163 files, with original size and SHA-256 verified |
| Consolidated duplicate paths | 505, each matched to a byte-identical surviving file |
| Generated caches omitted | Five `.pyc` files |
| Original documentation replaced | One one-byte README |
| Notebook preservation | Seven retained notebooks parse as notebook JSON and match their original hashes, including outputs |
| Navigation | Local Markdown file, directory, image, and heading links resolve |
| Git whitespace check | No whitespace errors in added archive documentation |
| Research execution | None: no imports, environment installation, GPU checks, model loading, training, inference, solver runs, or functional tests |

All preserved artifacts were checked against the untouched original checkout.
The [manifest](path-manifest.tsv) records the original Git blob, SHA-256, byte
count, current path, and disposition for each original file. The
[inventory](archive-inventory.json) records aggregate counts. Document summaries
have source identifiers and original-document hashes in the
[source catalogue](../research/SOURCES.md).

These checks establish content preservation and navigability, not numerical
correctness or reproducibility. Original source and notebook content remains
unchanged; historical runtime issues and paths are described in the
[archive notes](ARCHIVE_NOTES.md).
