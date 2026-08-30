# HCS-C243 — Bose–Josephson dimer phase portrait

This package freezes the Bloch-sphere Hamiltonian
\[
H(z,\phi)=\frac{\Lambda z^2}{2}-\sqrt{1-z^2}\cos\phi,\qquad \Lambda\ge0,
\]
with \(\dot z=-\sqrt{1-z^2}\sin\phi\) and
\(\dot\phi=\Lambda z+z\cos\phi/\sqrt{1-z^2}\).  The Bloch vector
\((x,y,z)=(\sqrt{1-z^2}\cos\phi,\sqrt{1-z^2}\sin\phi,z)\) removes the
coordinate singularity at \(z=\pm1\).

The theorem atlas covers \((0,0)\), \((0,\pi)\), the
\(\Lambda>1\) symmetry-broken points
\(z=\pm\sqrt{1-\Lambda^{-2}},\phi=\pi\), the \(\Lambda=1\) pitchfork,
and the \(\Lambda=0,2\) boundaries.  Eliminating \(\phi\) gives
\[
\dot z^2=-\frac{\Lambda^2}{4}z^4+(\Lambda H-1)z^2+1-H^2,
\]
with exact roots, complete-elliptic-\(K\) periods on crossing and
self-trapped components, the \(H=1\) sech homoclinic, and the strict
component-level self-trapping/reverse criterion.

The release has 28 physical files (27 payload files plus the self-excluded
manifest), baseline `489506cf92bfed721f94f22dd0444a60427f90a5`, epoch
`1788048000`, and scope `NO_BAD_EULER_OR_ROOT_NUMBER`.  It is a source-local
analytic phase-portrait result: A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL and
A4_NATURAL_QUANTIZATION; Route B is disabled.  No arithmetic or target
determinant claim is made, and `NEW` is workspace-local only.

Audit commands:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c243_dimer_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c243_dimer_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c243_dimer_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c243_dimer_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c243_dimer_mutation.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c243_release_manifest.py
```
