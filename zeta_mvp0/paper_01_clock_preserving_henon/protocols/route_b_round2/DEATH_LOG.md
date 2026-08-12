# Route B Round 2 Death Log

**Date opened:** 2026-08-06

This log records mechanism-level failures.  A dead route is not revived by a
larger numerical cutoff unless the failed assumption itself changes.

## Inherited deaths

| ID | Route | Status | Decisive reason |
|---|---|---|---|
| D001 | global \(a=1.02\) cycle-zeta/operator identification | DEAD AS GLOBAL ROUTE | mixed phase, an elliptic orbit, and unstable formal Fredholm comparison |
| D002 | finite spectral prefix \(\Rightarrow\) divisor | DEAD | exact hidden-shell counterexamples preserve finite prefixes while changing later zeros |
| D003 | fixed rank/mass/cap \(\Rightarrow\) first alias | DEAD | equal-rank/equal-mass countermodels give different aliases |
| D004 | scalar parity/cubic phase completion | STOP_SCOPED | actual orbit atom doubles the compensation burden and the signed replacement is undetermined |
| D005 | arbitrary Hermitization of a transfer operator | DEAD FOR DETERMINANT CLAIM | singular values of the Hermitization do not preserve \(\det(I-\mathcal L_s)\) |
| D006 | Koopman unitarity alone | DEAD FOR Q/W | typical spectrum is continuous and there is no compact-resolvent RvM sequence |
| D007 | Cuntz--Krieger spectral triple alone | DEAD FOR NOVELTY/W | known construction; its spectral dimension/word clock is not the RvM law |
| D008 | adelic/finite-field product called “prime-free” | DEAD AS WORDING | a product over finite places explicitly ranges over prime ideals |
| D009 | direct zero comparison before P | FORBIDDEN | violates the frozen gate order and permits arithmetic leakage |
| D010 | R108-C0 attempt 2 under unchanged protocol | CLOSED | attempt 1 failed the frozen all-mode residual guard; branch terminalized |

## Active fatal tests

| Pilot | Candidate | Pass condition | Death condition | Status |
|---|---|---|---|---|
| R300 | relative heat-trace activity | nonzero exact Hénon coefficient plus a defensible uniform remainder route | coefficient cancels, depends on zero data, or remainder is of the same order with no sign control | `PARTIAL_PASS`: coefficient independently confirmed; remainder proof open |
| R301 | local homoclinic/horsehoe precheck | stable numerical transverse intersection at \(a=51/50\), separated from tangency and reproducible independently | only tangency-scale/mesh artifacts or no robust intersection | PLANNED |
| R302 | symbolic self-adjoint clock audit | explicit fixed domain, compact resolvent, RvM two-term law, and non-cosmetic Hénon dependence | log-periodic order-\(T\) oscillation, infinite zero multiplicity, or engineered direct-sum clock | PAPER-ONLY UNTIL R300/R301 |

## Claim rule

Passing R300 would upgrade only S.  Passing R301 would establish numerical
support for a later local-horseshoe proof and a generalized-prime \(P^*\)
module.  Neither outcome passes the rational-prime P gate or authorizes Z.
