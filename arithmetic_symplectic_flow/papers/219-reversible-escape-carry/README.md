# 219 — Endogenous escape-carry screen

**Candidate:** `ASFS-SCOUT-20260918-REC01`  
**Status:** `PRE-P0 STOP — INTEGER UPDATE AND NONFIXED ESCAPE ARE PRESENT, BUT THE RESET IS NONINVERTIBLE AND THE PRIME CLOCK IS SQRT-SCALE.`

This bounded screen follows 218 with a genuinely changing integer register and
an unbounded escape counter. A divisor hit changes `n`, rather than entering a
fixed state `E_n`; the counter `k` records the escape. The exact rule is still
many-to-one at the scan reset, and a prime component has a unit-step period
controlled by the first `d` with `d^2>n`, not an endogenous `log n` roof. The
screen therefore stops before P0 geometry. It is a negative control for the
claim that adding a moving escape register alone repairs the return problem.

- [Frozen rule and ownership boundaries](candidate-card.md)
- [Bounded mathematical screen](paper.md)
- [Claim ledger](claim-ledger.md)
- [Evidence and reproducibility](evidence/README.md)

Classical A0/A1/A2 are `UNASSIGNED`; formal Route coordinates are `NOT
EVALUATED`; Route B is `NOT INVOKED`. Portfolio position: **stop/fork**.
