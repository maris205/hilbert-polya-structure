# Source audit

Authority hashes are embedded in producer and checker:

- C88 evidence: `4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b`;
- C88 prefreeze manifest: `aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5`;
- C89 evidence: `86a589505280721590674235626ddc21e37d57c891c726c7e6fbba98b2bd3af9`.

Both source receipts are canonical JSON, `PREFREEZE_G3_PASS`, and carry the `NO_BAD_EULER_OR_ROOT_NUMBER` firewall.  C99 reconstructs from C88 bitsets rather than trusting C88 coefficient rows.
