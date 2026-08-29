# HCS-C226: one-phase Stefan Neumann similarity

This release freezes the dimensionless moving-front problem

    u_t=u_xx,  0<x<s(t),  u(0,t)=1,  u(s(t),t)=0,
    beta*s'(t)=-u_x(s(t)^-,t),  s(0)=0,  beta=Ste^{-1}>0.

The paper proves the unique Neumann root
`sqrt(pi)*lambda*exp(lambda^2)*erf(lambda)=Ste`, gives a five-term
small-Stefan inverse series and a two-sided large-Stefan Lambert-W bound, and
closes the exact wall/interface flux and sensible-plus-latent energy ledger.
Zero superheat, zero diffusivity (dimensional thermal diffusivity kappa=0),
and zero latent heat are explicit singular boundaries; L=0 is not called a
finite-interface solution. Citation metadata are locked to Gupta's single-
author 2003 monograph and Rubinstein's 1982 two-phase stability article.

Reproduce from this directory:

    python3 code/c226_stefan_producer.py
    python3 code/c226_stefan_checker.py
    python3 code/c226_stefan_sympy_crosscheck.py
    python3 code/c226_stefan_replay.py
    python3 code/c226_stefan_mutation.py
    python3 code/c226_release_manifest.py

The three LuaLaTeX revision PDFs are built at the fixed epoch in
`paper/COMPILE_REPORT.md`; `paper/main.pdf` is byte-identical to round 2.
Route A is intentionally rejected with
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`. The source heat clock is
not target continuation/divisor/counting law, so it is not an A3 analytic
match. No target arithmetic, Euler factors, root numbers, automorphy, or
Hilbert--Pólya operator is claimed.
