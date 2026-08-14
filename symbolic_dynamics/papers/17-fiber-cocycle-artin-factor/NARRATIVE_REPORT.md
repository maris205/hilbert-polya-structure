# NARRATIVE REPORT — SD-C19

## One-sentence contribution

The signed tensor-subset shift admits a genuine intrinsic parity cover whose
Artin character determinants are exactly atom-local, while the same
functoriality that makes them clean forces a uniform cyclic degree cocycle and
therefore leaves the primitive arithmetic ledger and all control inventories
unresolved.

## Problem inherited from Paper 16

Permuting prime labels looks like symmetry before weights are specialized, but
it ceases to commute with the arithmetic transfer once the distinct roofs
\(x_p=p^{-s}\) are frozen.  The next admissible move is not another relabeling.
It is a separate fiber whose deck transformations never touch the atom
inventory.

The smallest such fiber is \(C_2\).  Subset cardinality already supplies an
intrinsic label, so the cocycle \(\alpha(S)=|S|\bmod2\) requires no prime table
and no target data.  Singleton edges switch the fiber.  Even subset edges
provide loops, making every restriction with at least two atoms mixing.

## Positive result

The regular transfer on \(\mathbb C[C_2]\) decomposes into the trivial and sign
characters.  Inclusion–exclusion then gives

\[
D_+=\prod_p(1-x_p),\qquad
D_-=\prod_p(1+x_p),\qquad
D_{\rm reg}=D_+D_-=\prod_p(1-x_p^2).
\]

At the arithmetic specialization these become

\[
\zeta(s)^{-1},\qquad \frac{\zeta(s)}{\zeta(2s)},\qquad
\zeta(2s)^{-1}.
\]

The result repairs the same-object defect: both character factors are blocks
of one commuting regular transfer.  Only their product is the determinant of
the whole extension.  The sign block is not a gauge artifact because the
singleton fixed point has nonidentity periodic product.

## Rigidity result

The clean factor is not one example among a large natural nonabelian family.
Relabeling naturality makes a one-letter cocycle depend only on subset size,
\(\alpha(S)=g_{|S|}\).  If the atom-local identity is required as a matrix
polynomial in a faithful representation, coefficient comparison gives
\(g_k=g_1^k\).  The image is cyclic; transitivity on the whole group forces the
group itself to be cyclic.

The quantifiers matter.  The theorem does not cover a transition label
\(\alpha(S,T)\), nor does it replace matrix equality by one determinant
identity in a selected higher-dimensional representation.

## Why the positive result stops

Character factorization is not an orbitwise bijection.  A primitive base
necklace with total degree \(c\) closes in a \(C_m\) cover only after
\(m/\gcd(m,c)\) traversals and has \(\gcd(m,c)\) primitive lifted cycles.
Singleton primes therefore have multiplied clocks, while the mixed edge
\(\{p,q\}\) closes immediately in the primary \(C_2\) cover.

The phrase “no mixed local factor” is consequently narrow: local Euler factors
are atom-indexed.  Mixed monomials in coefficient expansions and mixed
primitive lifted cycles remain.

The second stop is selectivity.  The determinant identities hold in a free
commutative polynomial ring.  Every substitution preserves them.  The exact
prototype found all four identities in all 64 prime, shuffled-prime,
composite, and random-rational runs, so the identity pass-rate margin is zero.

## Evidence

| Question | Exact evidence | Outcome |
|---|---:|---|
| Same-object signs and blocks | \(n=1,\ldots,10\), zero mismatches | pass |
| Repetition ledger | 300/300 coefficients | pass |
| \(C_m\) character phases | 350/350 rows | pass |
| Natural one-letter tables | 72,079 tables, 35 cells | one power table per cell |
| Mixed immediate \(C_2\) closures | 40/40 nontrivial census rows | primitive obstruction |
| Inventory controls | 64/64 identity passes | zero selectivity margin |
| Unit tests | 14/14 | pass |

These are exact finite certificates supporting theorem statements already
proved algebraically.  They are not a zero fit, training run, or statistical
claim.

## Route decision

The arithmetic source and honest-domain determinant earn analytic A0 and A2,
but the primitive mismatch leaves A1 weak.  A3 receives only partial credit for
the same-object Artin structure in the honest domain; no imported continuation,
completed functional equation, counting law, or Weil compression is credited.
There is no natural operator lift.

The frozen tuple is

\[
(\mathrm{A0\_ANALYTIC\_ARITHMETIC\_ORIGIN},
\mathrm{A1\_WEAK},
\mathrm{A2\_ANALYTIC\_DETERMINANT},
\mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},
\mathrm{A4\_FAIL}).
\]

The overall decision is ROUTE_A_REJECTED, STOP_SCOPED / PROVES_TOO_MUCH, and
ROUTE_B_LOCKED.

## Next symbolic obligation

The one-letter branch is closed.  The next admissible object is a
transition-dependent cocycle derived from subset incidence or refinement
grammar.  Its first test must combine noncommuting merge-order holonomy with
the \(p^2q^2\) temporal-power ledger.  Geometry or a self-adjoint carrier is not
developed here and remains a ROUND2_CLUE.
