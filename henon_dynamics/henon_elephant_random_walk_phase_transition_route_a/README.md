# HCS-C316 — Elephant random walk phase transition

This package gives one theorem-scale treatment of the full-memory elephant random walk over the full square `(p,q) in [0,1]^2`. It joins the exact transition kernel and all-time first two moments to the diffusive, critical, and superdiffusive limits, while splitting the singular martingale endpoint `p=0` and the deterministic/two-point endpoint `p=1`.

The machine evidence contains 35 parameter cases through time 14, an independent history enumerator, 453 martingale cells, and nine superdiffusive moment ledgers. These finite computations are regression witnesses only; the asymptotic theorems are analytic and source-attributed.

Run `python3 code/c316_release_manifest.py` to verify the closed release. The Route-A result is `ROUTE_A_REJECTED`; the firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.
