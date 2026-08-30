# HCS-C248 — Rudin–Shapiro diffraction cocycle (Route A)

This package is a self-contained, exact receipt for the classical four-letter
Rudin–Shapiro substitution

\[
 a\mapsto ab,\quad b\mapsto ac,\quad c\mapsto db,\quad d\mapsto dc,
 \qquad a,b\mapsto +1, c,d\mapsto -1 .
\]

The main advance is theorem-scale and source-local: the primitive substitution
has uniform letter frequencies; its binary factor is represented by the
dyadic Hadamard cocycle
\(P_{k+1}=P_k+z^{2^k}Q_k\),
\(Q_{k+1}=P_k-z^{2^k}Q_k\); the exact energy identity gives the square-root
unit-circle bound; and a four-component Laurent correlation recursion yields
the declared symmetric Cesàro/van Hove autocorrelation \(\delta_0\) and hence
Lebesgue diffraction.

Finite dyadic blocks are receipts, not periodic orbits.  The substitution hull
is aperiodic, so there is no primitive shift-periodic orbit ledger.  Diffraction
is explicitly separated from the full dynamical spectrum.

The locked Route-A tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, with
`ROUTE_A_REJECTED` and Route B disabled.  The scope firewall is literal
`NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic data are used.

Reproduce from this directory:

```text
python3 -B code/c248_rs_producer.py
python3 -B code/c248_rs_checker.py
python3 -B code/c248_rs_sympy_crosscheck.py
python3 -B code/c248_rs_replay.py
python3 -B code/c248_rs_mutation.py
python3 -B code/c248_release_manifest.py
```

`paper/main.pdf` is the final paper.  The three PDFs in `paper/` document the
original, first-revision, and second-revision content; the final PDF is byte
equal to the second revision under the fixed build epoch.
