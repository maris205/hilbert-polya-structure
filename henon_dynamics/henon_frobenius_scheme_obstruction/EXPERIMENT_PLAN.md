# HCS-C12A exact-certificate plan

Date frozen: 2026-08-06  
Status: **FROZEN v2 after a structural-review amendment**

## Amendment history

Version 1 used one five-cycle with the two arithmetic actions \(F=H\) and
\(F=H^2\).  Referee review found that this control did not commute with the
rational reversor \(R\), so it was not admissible in the reversible Hénon
category.  Version 2 replaces it with the chiral doublet in M2 below.  This
was a symmetry correction, made without looking for a target match and without
changing the frozen parameter/prime grid or any kill criterion.  All v2
artifacts are regenerated from scratch; \`AMENDMENT_LOG.md\` records the audit
trail.

## Claim under test

The registered claim was that, at fixed chronological period \(n\), the
Frobenius sequence \(r\mapsto N_{a,p}(r,n)\) might exhibit a distinguished
finite trace decomposition and local rationality.  WP0 predicts instead that
these properties are universal finite-permutation facts and therefore fail the
novelty/control gate.

The experiment is a theorem regression certificate.  It is not a search over
parameters and it does not fit any target spectrum.

## Milestones

### M0: symbolic sanity

1. Construct \(H_a^n\) exactly.
2. Recover the cyclic ideals for \(n=1,2\) and verify exact equality with the
   iterate fixed ideals.
3. Verify
   \[
   D_{a,1}=-4(a+1),\qquad
   D_{a,2}=2^8(a+1)(a-3)^3.
   \]
4. Verify the generic characteristic-zero splitting over \(\mathbb Q(A)\)
   \[
   X_{a,2}\simeq X_{a,1}\sqcup P_{a,2}.
   \]
   The certificate must record that the branches collide at \(A=3\).

Kill condition: any exact symbolic identity fails.

### M1: good/nonreduced/degree-drop firewall

Freeze

\[
a=6,\quad p\in\{5,11,7,3\},\quad 1\le r\le4.
\]

- \(p=5,11\): étale-good cells for \(n=1,2\);
- \(p=7\): degree-good but ramified/nonreduced control;
- \(p=3\): direct reduction of the uninverted original family, used as a
  coefficient degree-drop control including \(n=4\).  It is not a fiber of
  the finite-flat family over \(\mathbb Z[A,A^{-1}]\).

The producer uses exact quadratic/Legendre formulas.  The checker uses an
independent finite-field implementation and direct solution enumeration.
Ordinary support counts, nonstandard multiplicity-weighted counts, scheme
length, singular-support count, and prime status are separate fields.

Frozen irreducible-polynomial ledger uses coefficient order
\((c_0,c_1,\ldots,c_{r-1})\) for
\(t^r+\sum_i c_it^i\):

| \(p\) | \(r=2\) | \(r=3\) | \(r=4\) |
|---:|---|---|---|
| 3 | \(t^2+1\) | \(t^3+2t^2+1\) | \(t^4+t^3+t^2+1\) |
| 5 | \(t^2+t+1\) | \(t^3+t^2+1\) | \(t^4+t^3+t^2+1\) |
| 7 | \(t^2+1\) | \(t^3+t^2+1\) | \(t^4+t^3+1\) |
| 11 | \(t^2+1\) | \(t^3+4t^2+1\) | \(t^4+4t^3+1\) |

The checker must verify irreducibility rather than trust the ledger.

### M2: information-loss control

Throughout M2, \(F\) denotes arithmetic Frobenius \(x\mapsto x^p\).  Replacing
it by geometric Frobenius inverts \(F\); ordinary counts are unchanged, but
the sign of the second joint index must then be adjusted.

Use two five-cycles indexed by \((\varepsilon,i)\in\{\pm1\}\times\mathbb Z/5\)
with

\[
H(\varepsilon,i)=(\varepsilon,i+1),\qquad
R(\varepsilon,i)=(-\varepsilon,-i).
\]

Then \(RHR=H^{-1}\).  Compare the two matched arithmetic actions

\[
F_c(\varepsilon,i)=(\varepsilon,i+\varepsilon c),\qquad c\in\{1,2\}.
\]

Both \(F_c\) commute with \(H\) and \(R\).  Their ordinary sequences

\[
N_i(r)=\operatorname{Tr}(F_i^r)
\]

must agree for \(1\le r\le10\), while

\[
T_i(r,s)=\operatorname{Tr}(F_i^rH^{-s})
\]

must distinguish them.  This certifies that rectangular \(N(r,n)\) data do
not preserve the relative Frobenius/Hénon phase.

### M3: period-five collision certificate

1. Restrict \(\operatorname{Fix}(H_a^5)\) to the reversor line \(q=p\).
2. Remove the fixed-point factor and recover the generic sextic \(G_a(q)\).
3. At \(a=6\), verify its discriminant and factor degrees at the unramified
   primes \(37,5,157\):
   \[
   [6],\qquad[5,1],\qquad[2,1,1,1,1].
   \]
   These types certify transitivity, a 5-cycle, and a transposition; the
   resulting primitive subgroup is \(S_6\).
4. Under \(x=6q\), compare the sextic coefficient vector to the published
   Brison--Gallas period-five polynomial.  Equality is a literature collision,
   not a novelty success.

### M4: decision

The registered C12A route is `NO_GO` if the finite-permutation theorem and
matched controls explain every fixed-\(n\) trace factor.  C12B is not promoted
from the period-five calculation if the exact arithmetic object collides with
prior work.  A later candidate may study generic parameter curves or new
higher-period dihedral-centralizer quotients only after a fresh source lock.

## Reproducibility and firewall

- exact integer/rational arithmetic only;
- no floating-point root fitting;
- no Riemann zeros, prime gaps, or target divisors;
- producer and checker share only the frozen JSON schema and constants;
- all outputs are JSON/CSV;
- rational samples are regression checks, never substitutes for proofs.

Estimated compute: below one CPU-minute; zero GPU-hours.
