# HCS-C220 — open TASEP matrix-Ansatz phase route

This package freezes the continuous-time open totally asymmetric exclusion
process with unit bulk hopping.  It supplies one complete source theorem:

Source/code lock: `86c7bb8a39cdd1b8e941e45833b068170ca06287`.

- exact \(2^L\)-state generator and irreducible interior stationary law;
- DEHP matrix-product weights \(DE=D+E\);
- closed finite normalization \(Z_L\), including the \(\alpha=\beta\) limit;
- uniform current \(J_L=Z_{L-1}/Z_L\);
- LD, HD, maximal-current, coexistence, the two critical faces, and their
  multicritical corner \(\alpha=\beta=1/2\);
- \(\alpha=0\), \(\beta=0\), \(\alpha=\beta=0\), \(L=0\), and \(L=1\) boundaries.

On \(\alpha=\beta=0\), there are \(L+1\) absorbing extreme points; their
normalized stationary simplex has affine dimension \(L\).
The coexistence row means only the positive-rate line
\(0<\alpha=\beta<1/2\); its endpoint \((0,0)\) is covered by the zero-rate
boundary theorem.

The finite ledger uses 200 positive-rate rows and 40 boundary rows through
\(L=8\).  The checker rebuilds all rows independently and computes exact
SymPy nullspaces through \(L=4\).  SymPy, replay, and repaired/stale-hash
mutation controls are included.

## Reproduce

    python3 -B code/c220_tasep_producer.py
    python3 -B code/c220_tasep_checker.py
    python3 -B code/c220_tasep_sympy_crosscheck.py
    python3 -B code/c220_tasep_replay.py
    python3 -B code/c220_tasep_mutation.py
    python3 -B code/c220_release_manifest.py

The paper is paper/main.pdf; the release manifest is
C220_RELEASE_MANIFEST.json.  Build PDFs with LuaLaTeX and
SOURCE_DATE_EPOCH=1787875200.

Strict Route-A tuple:
(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT).
The package is ROUTE_A_REJECTED, route_b_invocation_allowed=false, and
uses NO_BAD_EULER_OR_ROOT_NUMBER.
