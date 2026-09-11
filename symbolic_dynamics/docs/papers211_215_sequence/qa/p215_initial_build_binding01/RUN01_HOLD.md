# P215 run01 artifact HOLD

2026-09-11 UTC. The single granted build completed successfully: controller
and all 14 supervised commands exited zero, every captured stderr is empty,
the final PDF has six pages and 200910 bytes, and all six pages were actually
viewed without a visual finding. The log diagnostic extractor emitted only
the informational line that file:line:error style messages are enabled.

Artifact acceptance is nevertheless held. The final FLS contains 67 unique
absolute INPUT paths. Four actually consumed AMS extra TFM files are not in
the prebound 223-row runtime manifest:

- cmbsy6.tfm
- cmbsy8.tfm
- cmmib6.tfm
- cmmib8.tfm

The four current files exist and have now been identified exactly, but they
are not added retrospectively to run01's binding. This run and its one-use
grant remain consumed and preserved. A distinct current02 source/binding and
new run02 output path must include all four resources before a new grant.
No cleanup, retry, PDF adoption, artifact acceptance or Round0 occurred.
