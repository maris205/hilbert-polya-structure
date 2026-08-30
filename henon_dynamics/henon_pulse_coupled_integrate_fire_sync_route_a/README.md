# HCS-C245 — Pulse-coupled integrate-and-fire event atlas

This package freezes an all-to-all network of (N) identical oscillators,
(dotphi_i=1), with the strictly concave rise

\[
 U_a(\phi)=\frac{1-e^{-a\phi}}{1-e^{-a}},\qquad 0\leq\phi<1,
\]

and excitatory pulse size (epsilon).  Writing (r=e^{-a}) and
(u_i=e^{-aphi_i}) turns a free flight into the exact common rescaling
(u_i\mapsto r u_i/\min_j u_j).  A pulse subtracts
(c=(1-r)\epsilon) and clips at the threshold (r); newly recruited
oscillators emit further pulses until the same-time avalanche closes.

The producer and an independent checker use only `Fraction` arithmetic for
(r\in\{1/2,2/3,3/4\}), (epsilon\in\{1/5,1/4,1/3\}), (N=2,ldots,8),
seven rational initial seeds, and twelve event steps.  The receipt has 441
event rows, 63 synchronized rows, and 441 partition-coarsening rows.  It
proves common-coordinate clusters cannot split, the all-equal cluster is
absorbing, and its event word ([N]) is primitive of period one.  This is a
finite event receipt, not a claim of an exhaustive continuous-state cell
census.  Mirollo--Strogatz almost-everywhere synchrony is cited separately
under its hypotheses.

The strict scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; event words are source-local
labels and no target determinant, arithmetic clock, Euler factor, root datum,
automorphy, or Hilbert--Pólya operator is claimed.  Route B is disabled and
the tuple is `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.
“NEW” means workspace-local only.

The release contract contains 28 physical files: 27 payload files plus the
self-excluded manifest.  It is locked to source/code baseline
`5f357e2d2b78604f6c286bfbd05da922e1d6791f`, evaluator SHA
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`, date
`2026-08-30`, and fixed epoch `1788048000`.

Run the audit from this directory:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c245_pulse_if_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c245_pulse_if_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c245_pulse_if_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c245_pulse_if_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c245_pulse_if_mutation.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c245_release_manifest.py
```
