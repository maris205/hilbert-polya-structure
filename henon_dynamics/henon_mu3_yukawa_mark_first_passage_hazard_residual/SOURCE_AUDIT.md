# Source audit

C94 reads exactly two frozen files from C88:

- `results/c88_subgroup_first_passage_atlas_evidence.json`, SHA-256
  `4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b`;
- `C88_PREFREEZE_MANIFEST.json`, SHA-256
  `aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5`.

The producer and independent checker bind both digests, require canonical JSON,
and verify C88's `PREFREEZE_G3_PASS` status and scope firewall.  Counts are
reconstructed from the C88 complete hit bitsets by pivotal-edge enumeration;
no simulation, fitted parameter, or downstream paper is an input.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
