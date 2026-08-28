# Source and ownership audit

## Primary references

| Key | Verified bibliographic record | What is imported | What C209 does not claim |
|---|---|---|---|
| `kreweras_1972` | G. Kreweras, *Sur les partitions non croisees d'un cycle*, Discrete Mathematics 1 (1972), 333-350, DOI `10.1016/0012-365X(72)90041-6` | ordinary NC(n), complement construction, Catalan/Narayana background | priority beyond the cited source |
| `reiner_stanton_white_2004` | V. Reiner, D. Stanton, D. White, *The cyclic sieving phenomenon*, JCTA 108 (2004), 17-50, DOI `10.1016/j.jcta.2004.04.009` | type-A rotation q-Catalan CSP and root-of-unity calculation | ownership of CSP or a new q-analogue |
| `bessis_reiner_2011` | D. Bessis, V. Reiner, *Cyclic sieving of noncrossing partitions for complex reflection groups*, Annals of Combinatorics 15(2) (2011), 197-222, DOI `10.1007/s00026-011-0090-9`, arXiv `math/0701792` | records the order-2n m=1 Kreweras-complement CSP and credits Dennis White's direct verification | treating the reported verification as C209 priority |

The arXiv identifier is retained as a preprint locator; the year and volume in
the release ledger are the formal 2011 publication.  The package's odd-power
fixed row is therefore labelled source-derived rather than newly proved.

## Convention audit

The scripts use vertices 0,...,n-1, c(i)=i+1, and
K(pi)=cycles(p_pi^{-1} c).  A direct NC(n) enumerator checks K^2=rho_{-1}.
Papers using c^{-1} report the inverse rotation; that is a conjugate
convention, not a disagreement in fixed counts.

## Deduplication against HCS-C187

C187 is the rectangular standard-Young-tableau promotion CSP (state set
SYT(b^a), q-hook polynomial, promotion/evacuation).  C209 is the geometric
set-partition complement (state set NC(n), K^2 polygon rotation, order-2n
complement action).  There is no parameter map from (a,b) to n, no shared
action, and no inherited theorem.  Generic Mobius and finite determinant
identities are bookkeeping tools only.

## Claim firewall

No target prime or zero table, local arithmetic datum, Euler factor, root
number, automorphy assertion, target divisor, functional equation, or
Hilbert-Polya operator enters the evidence.  The finite Koopman matrix is
source-native and is not promoted to a target operator.
