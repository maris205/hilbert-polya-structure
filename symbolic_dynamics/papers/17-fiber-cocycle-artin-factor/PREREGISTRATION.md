# PREREGISTRATION — SD-C19

**Freeze date:** 2026-08-14
**Candidate:** intrinsic \(C_2\) degree-parity extension of the signed
tensor-subset shift
**Forbidden data:** all Riemann-zero tables and target-derived tuning

## Frozen questions

1. Does a genuine commuting finite fiber give a lawful same-object Artin
   factor after atom relabeling fails?
2. Can a nontrivial character move recurrently while both character
   determinants remain atom-local at \(z=1\)?
3. Under functorial one-letter hypotheses, is any noncyclic clean alternative
   possible?
4. Does exact character factorization repair the primitive prime/prime-power
   ledger or distinguish arithmetic inventories from controls?

## Frozen claims

### C1 — same-object finite-fiber factorization

For \(\alpha(S)=|S|\bmod2\),

\[
D_+=\prod_p(1-x_p),\qquad
D_-=\prod_p(1+x_p),\qquad
D_{\rm reg}=D_+D_-=\prod_p(1-x_p^2).
\]

The deck action commutes with the weighted shift; \(D_{\rm reg}\) is the whole
extension, and \(D_\pm\) are its isotypic blocks.

### C2 — one-letter naturality rigidity

An inclusion-compatible, relabeling-natural one-letter cocycle satisfying the
operator-coherent atom-local identity in a faithful representation obeys
\(\alpha(S)=a^{|S|}\).  Its image is cyclic; transitivity on the whole finite
fiber forces the group to be cyclic.

### C3 — primitive lift obstruction

A primitive base necklace with total degree \(c\) closes after
\(m/\gcd(m,c)\) traversals and has \(\gcd(m,c)\) primitive lifted cycles.
Prime singleton clocks are multiplied by \(m\), while mixed immediate closures
remain.

### C4 — exact nonselectivity

All determinant identities hold over a free commutative polynomial ring.
Prime, shuffled-prime, composite, and random-rational inventories therefore
have identical identity pass rates and zero pass-rate margin.

## Frozen anti-claims

- No claim that the dynamical Artin mechanism itself is new.
- No claim that atom-local factors remove mixed coefficients or mixed cycles.
- No promotion of an isotypic divisor to the whole-extension divisor.
- No theorem about transition-dependent or higher-memory cocycles.
- No off-shell \(z\ne1\) atom-local Euler product.
- No new Fredholm continuation, Gamma factor, functional equation, Weil
  compression, self-adjoint operator, or RH conclusion.

## Frozen exact evidence grid

| Block | Cutoff / count | Success criterion |
|---|---:|---|
| Formal \(C_2\) determinants | \(n=1,\ldots,10\) | zero coefficient mismatches |
| Trace repetitions | 300 rows | every coefficient exact |
| \(C_m\) character certificates | 350 rows | zero coefficient/phase mismatches |
| Regular local determinants | \(m=2,\ldots,8\) | \(\det(I-xL_a)=1-x^m\) |
| Naturality tables | 72,079 in 35 cells | exactly one operator-clean power table per cell |
| Primitive/lift census | 350 rows | separate base, closure, and lifted counts |
| Inventory controls | 64 runs | all identities exact; pass-rate margin zero |
| Unit tests | 14 | all pass |

The exact prototype uses integer, rational, sparse-polynomial, and exact SymPy
matrix arithmetic.  It contains no floating root fitting and no target-zero
data.

## GO/STOP gates

```text
GO_GENUINE_COMMUTING_FIBER
GO_SAME_OBJECT_ARTIN_FACTORIZATION
GO_TRIVIAL_EULER_FACTOR
GO_NONTRIVIAL_RECURRENT_CHARACTER
GO_ATOM_LOCAL_CHARACTER_FACTORS_AT_Z_EQ_1

STOP_FUNCTORIAL_NONABELIAN
STOP_PRIMITIVE_LIFT
STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH
STOP_SCOPED
```

## Frozen route tuple

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_WEAK,
 A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

`A3_PARTIAL_ANALYTIC_STRUCTURE` records only the same-object Artin block
decomposition and honest-domain holomorphic structure.  It receives no credit
from imported meromorphic continuation.
