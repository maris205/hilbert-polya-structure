# HCS-C238 — Coulomb dry-friction oscillator

This package freezes one autonomous nonsmooth mechanical system:

\[
 \dot x=v,\qquad \dot v=-\omega^2x-c\,\xi,
 \qquad \xi\in\operatorname{Sign}(v),\quad
 \omega>0, c\ge0,
\]
where `Sign(0)=[-1,1]`.  The selection law is part of the model: at rest,
stick exactly when \(|x|\le a_f:=c/\omega^2\), and release uniquely inward
outside that interval.

The theorem closes global forward well-posedness under this maximal-monotone/viability
choice, \(E'=-c|v|\) on slip, the exact positive-rest half-cycle map
\(x_1=2a_f-A\), the integer capture count
\(\lceil(A-a_f)/(2a_f)\rceil\), general nonzero-velocity first-turn phases,
and the separate conservative \(c=0\) harmonic face.  A general first segment
with \(v_0\ne0\) is a partial slip arc; the ledger calls subsequent complete
segments `remaining_half_cycles` and records the total number of moving arcs
as `moving_arc_count`.

The release has 28 physical files (27 payload files plus the self-excluded
manifest), fixed epoch `1787875200`, and scope literal
`NO_BAD_EULER_OR_ROOT_NUMBER`.  It makes no arithmetic, target determinant,
Euler-factor, root-number, automorphy, or Hilbert–Pólya claim.  “NEW” in the
surrounding registry is workspace-local only, not a literature-priority claim.

Run the audit from this directory with:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c238_friction_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c238_friction_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c238_friction_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c238_friction_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c238_friction_mutation.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c238_release_manifest.py
```

The strict Route-A tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` and Route B is disabled.
