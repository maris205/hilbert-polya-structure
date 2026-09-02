# P152 paper plan — local triad dynamics on triangular books

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`  
**Contract:** `BTB_FREEZE_CONTRACT.md`; no claim may exceed that ceiling.

## One-sentence object

Run the established `p=1/3` local triad update on the triangular book
`B(3,r)=K_{1,1,r}`, count only active imbalanced-triad update epochs, and mark
the number of common-spine flips before absorption.

## Residual theorem package

1. Reduce the full signed-edge chain to the imbalance count
   `k -> k-1` with probability `2/3` and `k -> r-k` with probability `1/3`.
2. Solve the joint transform `F_k(z,u)=E_k[z^T u^J]` by eliminating the
   reflected index and obtaining a second-kind Chebyshev recurrence.
3. Derive the quadratic mean `k(r+2-k)/2` and its sharp integer extrema.
4. Derive the affine spine-parity law, characterize the exact feasible image
   of `(mean, parity)`, and recover `(r,k)`; retain explicit failures of either
   statistic alone.
5. Give a pre-generated private-edge block certificate for almost-sure
   absorption and an exponential tail.

The paper leads with items 2--4.  The stochastic rule, social-balance
interpretation, XOR/triadic dual, signed-book carrier, static count classes,
generic finite-chain recurrences, and generic absorption methodology receive
zero contribution credit.

## Section architecture

- **Section 1:** literal process, active-clock convention, primary-source
  subtraction, and the full theorem.
- **Section 2:** strong lumping and the private-block absorption certificate.
- **Section 3:** reflected Bellman equation, Chebyshev elimination, complete
  joint transform, and `r=1`, `r=2`, `z=0`, and coincident-arrow boundaries.
- **Section 4:** mean, sharp extrema, spine parity, exact inverse, feasibility,
  and one-statistic counterexamples.
- **Section 5:** exact-arithmetic falsification, collision controls,
  limitations, and declarations.

## Proof dependency

```text
signed physical-edge update on B(3,r)
    -> imbalance bits
    -> private clear / spine complement
    -> strong count quotient
       -> marked Bellman -> reflection elimination -> Chebyshev transform
       -> mean Bellman -> constant second difference -> extrema
       -> parity Bellman -> affine law -> exact two-statistic inverse
       -> private-choice blocks -> absorption and exponential tail
```

## Mandatory visible boundaries

- `r=1`: `F_1=z(2+u)/3` and the sole mean equals one.
- `r=2`: spine reflection is a self-loop at count one;
  `F_1=2z/(3-zu)` only after cancellation of the raw `(3+zu)` factor.
- `z=0`: use the Bellman boundary, not the undefined expression for `xi`.
- `k-1=r-k`: add the private and spine masses at the coincident target.
- `q=1/2`: valid central inverse case for even `r`.
- Arbitrary candidate data must satisfy `m>0` and `0<q<1` before the square
  root in the inverse criterion is formed.
- The inverse is exact-only; no noisy stability or full sign-state recovery.
- The active update-epoch clock differs from the AKR 2005 all-triad clock.
- Friendship/windmill graphs share a vertex, not an edge, and have `T=K`.

## Evidence plan

- Symbolic proofs in `main.tex` and the expanded derivation in
  `PROOF_PACKAGE.md` carry the theorem.
- `verify_p152.py` independently solves finite rational Bellman systems,
  enumerates literal bit states, compares the inverse iff with an independently
  bounded exact image grid, checks both scalar collisions, and propagates exact
  private-block/tail probabilities as counterexample pressure.
- `verification_output.txt` is the frozen deterministic transcript.
- `SOURCE_VERIFICATION.md` records only primary or author-hosted sources and
  explicitly treats a bounded non-hit as neither novelty nor priority.

Review A found 0 Critical / 0 Major / 2 Minor artifact defects; Round 1 closed
both through expanded exact pressure and complete manifest coverage.  Review
B found 0 Critical / 0 Major / 1 Minor candidate-domain defect; Round 2 closes
it by ordering the positivity/domain gate before the square root.  All
dispositions are recorded in `IMPROVEMENT_LOG.md`, surviving severity is
0 / 0 / 0, and all external action remains prohibited.
