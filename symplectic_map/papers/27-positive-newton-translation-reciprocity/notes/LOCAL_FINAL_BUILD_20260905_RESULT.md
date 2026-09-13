# Final local execution: preserved comparator failure

Builder status: FAIL_PRESERVED_NO_RETRY

Session 71027 ran LOCAL_FINAL_BUILD_20260905.py once and exited 1. Both r0 and r1 completed the exact four publication passes, and both emitted OUTPUT_CHECKS_PASS. The final comparison then stopped at CROSS_MANIFEST:R009. The frozen script, all sources, both roots, receipts, snapshots, acceptance records and `failure.json` remain unchanged. No fourth compilation attempt is planned or permitted by this bounded compile-fix workflow.

Both PDFs are 336871 bytes, SHA256 `ab195a2b49012e9b4b320ddbabffd9666c076b37b09a8b9dc20c400dd266a5b4`. Both acceptance records have SHA256 `8022e67263546aed1447119f16d80351080750a38e5862f82590b88efacff69f`. Each records 27 proof pages, References starting page 28, 29 total pages, zero overfull, 18 explicitly retained underfull warnings, the required text/bibliography/boundary census, embedded fonts and compliant PDF metadata/security. These bytes are identical to the separately content-reviewed and visually inspected layout diagnostic PDF.

The failed condition compares physical directory `st_size` values across roots. The actual values are:

| Manifest | r0 root st_size | r1 root st_size | Each of five empty caches, r0/r1 |
| --- | ---: | ---: | --- |
| R009 | 188 | 152 | 10 / 6 |
| R024 | 268 | 216 | 10 / 6 |
| R033 | 308 | 248 | 10 / 6 |
| R044 | 308 | 248 | 10 / 6 |
| R054 | 308 | 248 | 10 / 6 |

The main agent's read-only comparison of all five manifest pairs found equality after only (a) the already-declared recorder-prefix/hash projection and (b) excluding the size field on entries explicitly typed `dir`. No regular-file size, bytes, line count, mode, link count or hash was excluded. Directory names, types, modes, link counts and membership requirements were retained. This is a diagnostic finding, not a rewrite of the failed original comparison; it requires fresh independent final-artifact audit.

Regular-file byte identity is the reproducibility property at issue. POSIX defines `st_size` as byte size for regular files; it does not define directory `st_size` as a canonical encoding of logical entries. Treating identical logical directories as unequal solely on that field is therefore an inappropriate artifact-content predicate; this conclusion is an inference applied to the observed manifests, not a claim that the original contract already omitted the field. See [POSIX sys/stat.h](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/sys_stat.h.html).

The next action is read-only independent technical audit of the proposed directory-content correction, documented separately in LOCAL_DELIVERY_LOCK_20260905.md. On rereading the complete user-confirmed recovery proposal, the main agent identified that it explicitly retained only root-prefix normalization. The directory-field exclusion is thus a proposed new comparison boundary, not already authorized: local acceptance additionally requires one narrow user confirmation. The audit is not another build, root reuse, failure reclassification, silent normalization of files or externally effective release. If it finds any other discrepancy or incomplete scientific/output lineage, local delivery must also remain pending for that reason.
