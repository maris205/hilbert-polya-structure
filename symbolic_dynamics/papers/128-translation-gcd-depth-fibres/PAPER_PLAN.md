# Paper plan: all-depth translation--GCD fibres

## Frozen scope

This is an old-reserve re-entry, internally numbered P128.  The literal map,
its window iterate, its order-`p` clock, its fixed ring, its fixed counts, and
all previously enumerated depth profiles are not new outputs.  Garefalakis's
and Reis's translation-fixed irreducible results, including Reis's displayed
formula for `b_(pm)`, are also fully zero credit.

The paper has exactly two residual theorem packages.

1. **All-depth formal orbit Euler product.**  Translation-orbit exponent vectors are
   normalized by their minimum.  Their stabilization depth is the longest
   positive cyclic run.  A finite run automaton gives `R_(p,t)`, and the
   owned irreducible-orbit counts assemble these factors into the exact OGF
   `H_(q,p,t)` for every degree and every depth threshold.
2. **Every terminal target fibre.**  The terminal map `Q=T^(p-1)` gives a
   unique graded set decomposition into an invariant core and a residual in
   the **unit fibre** `Q^(-1)(1)`.  This yields its OGF and the exact-degree
   and degree-capped fibre over each invariant target.

No claim of novelty or priority is made for the literal system or for any
zero-credit ingredient.  External release remains `HOLD_EXTERNAL`.

## Proof architecture

1. Factor a monic polynomial into irreducible translation orbits.
2. On a nonfixed orbit, prove the cyclic sliding-minimum formula by induction.
3. Subtract the minimum exponent and identify depth with the longest positive
   cyclic run.
4. Prove that `trace(M_t(u)^p)` counts exactly the normalized exponent vectors;
   the all-positive support is excluded because a normalized vector has a
   zero.
5. Multiply the local series over nonfixed irreducible orbits and attach one
   invariant-core factor `1/(1-qz^p)`.
6. Prove the terminal-core split from orbit exponents.  Use only the restricted
   identity `Q(hr)=hQ(r)` for invariant `h`; never assert that `Q` is
   multiplicative.
7. Divide the all-monic OGF by the invariant-core OGF to obtain the unit-fibre
   OGF, then translate it to each exact and capped target fibre.

## Claim/evidence contract

| claim | proof object | mechanical stress | credit status |
|---|---|---|---|
| all-depth OGF `H_(q,p,t)` | Theorem 3.2 | F4/F8/F9 literal dynamics plus a literal truncated-matrix trace checked against direct residual-vector enumeration | residual lead claim |
| exact depth layers | Corollary 3.3 | every enumerated degree/depth CDF | immediate residual corollary |
| graded invariant/residual split | Proposition 4.1 | quotient reconstruction for every state | residual support |
| unit-fibre coefficients | Theorem 4.2 | exact degree cells in three extension fields | residual second claim |
| every target exact/capped fibre | Theorem 4.2 | exhaustive target-by-degree and bounded sums | residual second claim |
| `b_(pm)` and `a_d` | Garefalakis/Reis | irreducible orbit census | **zero credit input** |
| window/clock/fixed/depth setup | old scout and P110 order-dual mechanism | literal iteration checks only | **zero credit setup** |

## Required firewalls

- **Owner firewall:** Garefalakis and Reis own the fixed-irreducible
  classification/count; Reis Theorem 2(c) is algebraically identical to the
  displayed `b_(pm)` formula.
- **P110 firewall:** the generic meet iterate, invariant endpoint, finite
  clock, and recurrent/fixed statement are order-dual to P110's cyclic
  shift--join dynamics and receive zero credit.  The residual here is the
  polynomial-specific orbit-exponent census and target-refined graded fibres.
- **Terminology firewall:** `Q^(-1)(1)` is the **unit fibre**, never an
  algebraic kernel.  The counterexample `Q(x)=Q((x^p-x)/x)=1` but
  `Q(x^p-x)=x^p-x` is printed.
- **Verification firewall:** extension fields are finite falsifiers.  They do
  not prove the all-parameter theorems or establish ownership/novelty.

## Deliverables and rounds

All listed paper-local rounds and deliverables are complete.

- anonymous `amsart` manuscript and primary-source bibliography;
- paper-local independent extension-field verifier and canonical transcript;
- four-stage isolated build and frozen `main_round0_original.pdf`;
- independent hostile Review A, repair pass, and `main_round1.pdf`;
- independent hostile Review B, repair pass if needed, and `main_round2.pdf`;
- final QA, exact hashes, and `SHA256SUMS`.

## Release state

Both independent reviews and final QA passed, so the frozen package is
`GO_INTERNAL`.
Posting, submission, priority language, and external novelty claims remain
`HOLD_EXTERNAL` pending specialist owner review and explicit authorization.
