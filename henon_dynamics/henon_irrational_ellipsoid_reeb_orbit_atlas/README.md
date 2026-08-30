# HCS-C242 — Irrational ellipsoid Reeb-orbit atlas

This package freezes the standard contact form on
\(E(a,b)=\{\pi|z_1|^2/a+\pi|z_2|^2/b\le1\}\).  For irrational \(a/b\),
the Reeb flow has exactly the two simple coordinate circles
\(\gamma_1=\{z_2=0\}\) and \(\gamma_2=\{z_1=0\}\).  Their iterates have
\(A=T=ka\) and \(A=T=kb\), transverse multipliers
\(e^{\pm2\pi i k a/b}\), \(e^{\pm2\pi i k b/a}\), and, in the coordinate
the coordinate complex-line trivialization used by Hutchings, Conley--Zehnder indices
\(2\lfloor ka/b\rfloor+1\) and \(2\lfloor kb/a\rfloor+1\).

The receipt uses \(a/b=\sqrt2\) and its reciprocal as exact irrational
sentinels. Every floor is certified by integer-square inequalities; decimal
trigonometric values are display-only. Three coprime rational controls make
the Morse--Bott boundary explicit: at \(a/b=p/q\), the common period
\(qa=pb\) carries the full boundary family, and no nondegenerate CZ index is
assigned before perturbation.

The release has 28 physical files (27 payload files plus the self-excluded
manifest), fixed epoch `1788048000`, source baseline
`489506cf92bfed721f94f22dd0444a60427f90a5`, and scope
`NO_BAD_EULER_OR_ROOT_NUMBER`. It is a source-local analytic A1 result;
A0/A2/A3 fail and no arithmetic, target determinant, or Hilbert--Pólya claim
is made. `NEW` means workspace-local only.

Run the audit from this directory:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c242_reeb_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c242_reeb_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c242_reeb_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c242_reeb_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c242_reeb_mutation.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c242_release_manifest.py
```

The strict Route-A tuple is
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` and Route B is
disabled.
