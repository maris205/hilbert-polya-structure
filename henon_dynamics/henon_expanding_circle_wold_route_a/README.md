# HCS-C177: expanding-circle Wold and mixing obstruction

This package proves a single all-parameter theorem for every integer expanding circle endomorphism
\(T_b(x)=bx\pmod 1\), \(b\ge2\). It joins exact periodic coordinates and primitive cycles to the Haar--Koopman Wold decomposition, the Perron adjoint, and a sharp homogeneous-Sobolev correlation bound.

The explicit progress is the simultaneous identity

\[
\#\operatorname{Fix}(T_b^n)=b^n-1,
\qquad \zeta_{AM,b}(z)=\frac{1-z}{1-bz},
\qquad U_b\simeq 1\oplus S^{(\aleph_0)},
\]

together with the sharp factor \(b^{-ns}\) for mean-zero \(\dot H^s\)-against-\(L^2\) correlations. Prime and composite degrees obey the same degree-only theorem, which is the decisive Route-A obstruction.

Run:

```bash
python code/c177_expanding_circle_producer.py
python code/c177_expanding_circle_checker.py
python code/c177_sympy_crosscheck.py
python code/c177_replay.py
python code/c177_mutation.py
python code/c177_release_manifest.py
```

The manuscript is `paper/main.pdf`. The verdict is `(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`, overall `ROUTE_A_REJECTED`; Route B remains false.
