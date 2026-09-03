# HCS-C322 — Kac master-equation spectral gap

This package fixes the uniform-angle Kac walk on `S^{N-1}(sqrt(N))` and the positive generator

`L_N=N(I-Q_N)`.

It proves the exact gap `Delta_N=(N+2)/[2(N-1)]`, the quartic slow mode, its uniqueness for `N>=3`, and sharp `L2` semigroup decay.  The lower bound is reproduced through the Carlen–Carvalho–Loss conditional-expectation induction, including the `P=TT*/N` nonzero-spectrum transfer and complete trivial/standard index-branch analysis: it is not inferred from finite polynomial matrices or merely quoted.

Exact rational polynomial evidence audits sphere moments, the one-coordinate correlation spectrum, finite Gram/Dirichlet forms, the quartic eigenpair, and the telescoping induction.  Run `python3 code/c322_release_manifest.py` after all release artifacts exist.  The Route-A result is `ROUTE_A_REJECTED`, with `A4_FORMAL_HINT`; Route B remains locked under `NO_BAD_EULER_OR_ROOT_NUMBER`.
