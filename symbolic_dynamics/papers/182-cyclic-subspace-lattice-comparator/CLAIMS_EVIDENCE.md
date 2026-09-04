# P182 claims–evidence ledger

**State:** `ROUND2_DUAL_REVIEW_FREEZE`; two process-separated hostile reviews
closed with zero findings.  
**Lifecycle:** `OWNER_AMBER / HOLD_EXTERNAL`.

| ID | Frozen claim | Proof location | Exact falsification control | Status |
|---|---|---|---|---|
| C1 | `T^4=T^2` on every lattice | `main.tex`, universal dynamics; Proof Package Lemma 1 | every source in 15 boxes | proved + checked |
| C2 | image is exactly `(C,M,J)` with `M<=J` | main theorem (i); Proof Package Lemma 2 | complete image equality per box | proved + checked |
| C3 | recurrent iff `B<=A,C`; fixed iff also `A=C`; all other recurrent states form 2-cycles | main theorem (ii); Proof Package Lemma 2 | direct cycle decomposition | proved + checked |
| C4 | fixed, strict-cycle, image, and all depth counts equal the displayed Gaussian sums | main theorem (iii–iv); Proof Package Lemmas 3–4 | all formula values per box | proved + checked |
| C5 | every target fibre is zero or `kappa_dim(J/M)` | main theorem (v); Proof Package Lemma 5 | every one of all carrier targets | proved + checked |
| C6 | complete fibre histogram and sharp max/min-positive targets | main theorem (vi); Proof Package Lemmas 5–6 | full incoming histogram | proved + checked |
| C7 | finite exact transcript is deterministic | paper-local verifier and canonical transcript | two-process byte comparison | mechanically checked |
| C8 | no exact external owner was found | bounded source log only | no computational implication | **not claimed**; owner remains amber |

## Frozen computational receipt

```text
boxes=15
transitions=328700
exact_assertions=1667850
transition_digest=b2bee01438caf59c10cf29da0a7bf11fcba1aeee2629eb2d86fadb1051a2ebb7
status=PASS
external_status=HOLD_EXTERNAL
```

The verifier is not cited as proof of C1–C6.  It is a finite, independent
attempt to falsify formulas whose proofs are symbolic.

## Zero-credit ledger

No contribution credit is assigned to lattice axioms, subspace lattices,
Gaussian coefficients, Galois-number counts, standard complement counts,
Hibi meet/join sorting, pop-operator dynamics, or generic functional-graph
bookkeeping.  The retained conjunction is the literal three-register update,
its universal depth-two/period-two theorem, and the target-local quotient-
complement atlas.
