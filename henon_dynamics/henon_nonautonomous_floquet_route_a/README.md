# C110 — Period-2 Non-autonomous Hénon Floquet Pilot

This package is a Route-A exploratory paper package for a periodically forced
quadratic Hénon cocycle.  The frozen maps are

\[
 F_t(x,y)=(x^2+\alpha_t x+\beta_t-y,x),\qquad
 (\alpha_0,\beta_0)=(0,0),\quad (\alpha_1,\beta_1)=(1,1/3),
\]

with forcing clock `t mod 2`.  At the frozen samples `xi=-1,+1`, the exact
Jacobian templates are `[-2,2]` at phase 0 and `[-1,3]` at phase 1.  A block
symbol is the pair `(s0,s1)`, and its chronological Floquet product is
`B_1,s1 B_0,s0`.  A frozen four-state adjacency makes chronological, reversed,
and same-phase controls distinguishable.

The certified object is intentionally finite: admissible primitive block words
through period six and three 8-by-8 matrix-valued transfer prefixes.  It is a
symbolic/modeling pilot, not a geometric Markov partition, a complete Hénon
periodic-orbit enumeration, or a Fredholm determinant.  The package makes no
arithmetic, Euler-factor, root-number, automorphy, or Hilbert–Pólya claim;
`NO_BAD_EULER_OR_ROOT_NUMBER` is enforced in the evidence and manifests.

## Reproduce

From this directory run:

```bash
python3 code/c110_nonautonomous_producer.py
python3 code/c110_nonautonomous_checker.py
python3 code/c110_sympy_crosscheck.py
python3 code/c110_replay.py
python3 code/c110_mutation.py
python3 code/c110_release_manifest.py
```

The exact evidence is `results/c110_nonautonomous_evidence.json`; the paper is
`paper/main.tex` and the compiled artifact is `paper/main.pdf`.

## Route-A boundary

The frozen ledger is assessed as `A1_WEAK` (non-autonomous symbolic pilot only),
`A2_CERTIFIED_PREFIX` (discrete Floquet transfer prefix only),
`A3_NOT_ADDRESSED`, and `A4_FAIL`.  In particular, the chronological product
is certified algebraically, while geometric coding and a source-native
function-space operator remain open.
