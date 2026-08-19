# C77 experiment plan

## Source binding

Read the C76 evidence and prefreeze manifest, together with the C75 named
coordinate/subgroup source, as raw bytes before deriving any polynomial.  The
locked C76 SHA-256 values are

```text
C76 evidence: 42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94
C76 manifest:  55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5
```

Recover the sixteen coordinates and actual subgroup point sets from the C75
source, then bind the C76 closure-index convention and support totals.  Do not
infer a different abstract group or reorder the subgroup lattice.

## Exact computation

1. For each label `i`, form its cyclic subgroup `C_i` in `Q` and compute
   `n_H = |{i:C_i <= H}|` for every subgroup row.
2. Build the incidence relation `K <= H` and its integer Möbius function,
   using `mu(H,H)=1` and `sum_{K<=H} mu(K,H)=0` for `K<H`.
3. Form `P_{<=H}(q)=q^(16-n_H)` and
   `P_{=H}(q)=sum_{K<=H}mu(K,H)q^(16-n_K)`.
4. Recompute `Phi(A)` for every 16-bit support and collect exact counts by
   subgroup and support cardinality.  Expand the direct Bernoulli polynomial
   in the same variable `q`.
5. Compare integer coefficient vectors for every subgroup.  Check that all
   twenty exact rows sum to one and that the top row factors as the C73
   reliability polynomial.

## Independent gates

The independent checker must reimplement subgroup containment, Möbius
inversion, and direct support enumeration without importing producer state. A
separate symbolic/numeric cross-check verifies the incidence matrix and top
factorization.  A clean replay runs the checker in a fresh interpreter, while
the hostile audit mutates semantic fields (authority hashes, `n_H`, Möbius
entries, coefficients, and top polynomial) and requires rejection.

The paper is compiled twice in isolated directories with
`SOURCE_DATE_EPOCH=0` and `FORCE_SOURCE_DATE=1`; PDFs must be byte-identical.

## Claims firewall

The output is a finite named-subgroup reliability atlas.  It is not a full
Burnside-ring/table-of-marks computation and has no arithmetic/local,
Euler-factor, root-number, automorphy, or Hilbert--Polya interpretation.
