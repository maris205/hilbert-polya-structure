# Source audit

The sole data authority is frozen C88:

- evidence `4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b`;
- prefreeze manifest `aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5`.

The producer and independent checker verify both hashes, canonical JSON, `PREFREEZE_G3_PASS`, and `NO_BAD_EULER_OR_ROOT_NUMBER` before decoding bitsets.  No external source or stochastic sample is used.
