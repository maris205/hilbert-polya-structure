# PAPER PLAN

## Title

**Primitive-Cycle No-Lift for the Tensor Bar Code: Koszul, Power, and
Equivariant Obstructions**

## One-sentence contribution

The tensor-atom subset shift has the exact Koszul-shaped determinant
\(\prod_p(1-p^{-s})\), but this scalar cancellation cannot be lifted to a
natural primitive-cycle or homological atom selector because cancellation
crosses temporal power layers, fails \(S_3\)-equivariance, and changes under
the scalar-to-supertrace substitution.

## Paper type and claim boundary

Theory plus exact finite certification.  The inclusion--exclusion determinant,
bar-to-Koszul background, HKR/Harrison decomposition, and necklace formulas
are classical.  The paper's narrow contribution is the source-locked no-lift
audit for SD-C17 and its explicit low-degree obstruction package.  It makes no
priority claim beyond that bounded statement and no RH claim.

## Claims--evidence matrix

| Claim | Evidence | Status | Location |
|---|---|---|---|
| The subset shift has a genuine analytic scalar determinant | formal inclusion--exclusion and countable absolute convergence | proved | Sections 3, A |
| Scalar cancellation is not primitive-level cancellation | exact \(pq\) and \(p^2q^2\) primitive/power ledger | proved | Section 4 |
| No atom-permutation-natural sign involution exists | \(S_3\) orbit and fixed-character certificate at \(pqr\) | proved | Section 5 |
| Bar/Koszul homology does not leave atoms alone | \(\operatorname{Tor}^{R_A}(\Bbbk,\Bbbk)=\Lambda V\) | classical theorem, specialized | Section 6 |
| Chain parity cannot replace scalar sign | \((-w)^r\) versus \(-w^r\), plus acyclic supertrace lemma | proved | Section 6 |
| The determinant has no arithmetic selectivity | arbitrary-variable theorem and 112 exact controls | proved / certified | Section 7 |

## Structure

1. Introduction and exact route status.
2. Literature boundary and algebraic preliminaries.
3. Frozen Koszul subset shift and determinant.
4. Primitive/power obstruction at \(p^2q^2\).
5. Equivariant obstruction at \(pqr\).
6. Homological, cyclic, and supertrace no-lift.
7. Exact audit, universality controls, and Route-A evaluation.
8. Conclusion and next in-family obligation.
9. Appendix with full proofs and scope ledger.

## Figure plan

One pure-TikZ figure shows the only valid implication chain:

```text
tensor bar inventory -> squarefree subset scalar shift -> exact determinant
                                           |-> power-layer obstruction
                                           |-> S3-character obstruction
                                           |-> chain-parity obstruction
```

It visually separates the valid determinant identity from the invalid
primitive/homological promotion.  No data plot is necessary because the key
certificates are exact and fit in tables.

## Citation plan

- Symbolic determinant: Bowen--Lanford.
- Koszul/bar and algebraic discrete Morse: Priddy; Sköldberg;
  Jöllenbeck--Welker; Freij.
- Hochschild/Harrison/AQ: Hochschild--Kostant--Rosenberg; Barr; Quillen;
  Gerstenhaber--Schack; Loday.
- Necklaces and cyclic enumeration: Metropolis--Rota.

All bibliography records are verified against DOI/publisher metadata where a
DOI exists.  No review loop is run because the user explicitly requested
direct exploratory publication.
