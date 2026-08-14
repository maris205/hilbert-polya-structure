# Implementation Notes — Paper 33

The core module contains only source construction and quotient arithmetic.  It
does not classify primes, read target zeros, or use accepted support.  The
post-census `classify` helper in `generate_results.py` is used only to label
already-computed rows.

Sparse ranks are computed over `F_1000003`, a prime avoiding characteristics
2 and 3.  This validates finite certificates; the theorems are proved over
`Q`.

The double-run certificate uses temporary directories and compares each
primary payload against the frozen authority payload.
