# Exact control results

The deterministic verifier uses modular Gaussian elimination for determinants
and a separate literal signed-minor construction for adjugates.

Registered exhaustive lanes:

- `M_3(F_2)` — 512 matrices;
- `M_3(F_3)` — 19,683 matrices;
- `M_4(F_2)` — 65,536 matrices.

It checks literal/closed double adjugation, singular collapse, six fixed
counts, and six image sets.  Four determinant-representative lanes check
twelve periods, the full iterate normal form, and the named anomalies.
Five independent scalar-line lanes check the exact image staircase and first
stabilization at `t_*=0,1,2,4,1` for
`(q,d)=(5,4),(7,3),(17,3),(257,3),(19,4)`.  The canonical output is
`code/verification_output.txt`.

Fresh cross-hostile-A result: **PASS, 141,190 exact assertions**.

The control is a finite falsifier; the paper's field-uniform statements are
proved analytically.
