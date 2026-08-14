# Proof Sketch and Dependency Ledger

**Candidate:** `additive_finite_arithmetic_capacity_v2`  
**Role:** compact map of the complete proof in `PROOF_PACKAGE.md`

## Main theorem

Fix a finite-dimensional $\mathbb Q$-space $V\subset\mathbb R$ and a finite
set $S_{\mathbb Q}$ of rational primes.  If every distinct realized prime has
a certificate

$$
\log p=v_p+\log q_p+\alpha_p,
$$

with $v_p\in V$, $q_p>0$ algebraic, $q_p^2$ an
$S_{\mathbb Q}$-unit, and $\alpha_p$ real algebraic, then

$$
\#\mathcal P_{\rm hit}
\le \dim_{\mathbb Q}V+|S_{\mathbb Q}|.
$$

All data are fixed independently of the target.  The logarithm is real and
all equalities are exact.

## Proof spine

1. Remove the at most $|S_{\mathbb Q}|$ hit primes already in the bad
   support and choose one certificate for every remaining distinct prime.
2. A rational relation among the corresponding $v_p$ terms can be cleared to
   an integer relation $\sum m_pv_p=0$.
3. Substitution gives $\log R=\beta$, where

   $$
   R=\frac{\prod p^{m_p}}{\prod q_p^{m_p}}>0
   $$

   is algebraic and $\beta=\sum m_p\alpha_p$ is real algebraic.
4. Hermite--Lindemann forces $\beta=0$, since otherwise
   $R=e^\beta$ would be transcendental.  Hence $R=1$.
5. Square the equality:

   $$
   \prod p^{2m_p}=\prod(q_p^2)^{m_p}.
   $$

6. Put the finitely many factors in one number field.  Unit status away from
   $S_{\mathbb Q}$ survives finite extension and negative powers.
7. At a place above one distinct outside prime $p$, every right-hand factor
   has valuation zero and every other rational prime has valuation zero.  The
   remaining valuation is $2m_pv_w(p)$, hence $m_p=0$.
8. The selected $v_p$ terms are rationally independent, so at most
   $\dim_{\mathbb Q}V$ outside primes can occur.

No finiteness assumption on the hit set is used: any finite subset of size
$\dim V+1$ would already contradict Step 8.

## Closure ledger

- L terms: fixed finite memory is absorbed by a higher-block finite graph;
  rational combinations stay in the common $V$.
- M terms: rational sums $\sum c_j\log q_j$ become $\log q$ after adjoining
  positive algebraic roots.  If each $q_j^2$ is an $S_{\mathbb Q}$-unit,
  then $q^2$ is too.  Negative powers use inverses.
- A terms: finite algebraic sums and allowed algebraic real-valued transforms
  remain algebraic.
- Excluded: algebraic irrational coefficients on multiplier logs, nonlinear
  mixing, target-indexed lookup, log-after-action, complex logarithm branches,
  and approximate equality.

## Class-M dependency detail

1. Expand a composed Hénon orbit into its cyclic scalar recurrence.
2. Homogenize each recurrence equation to its own polynomial degree.
3. Monicity removes all points at infinity.
4. A projective variety contained in an affine chart is projective and
   affine, hence zero-dimensional; periodic coordinates are algebraic.
5. The nonarchimedean maximum argument proves integrality outside the bad
   places.
6. Monodromy and its inverse are integral, so eigenvalues are units.
7. Pass to a normal extension and saturate all places over
   $S_{\mathbb Q}$ before applying complex conjugation.
8. Use only $q^2=\lambda\overline\lambda$, never
   $\overline\lambda=\lambda^{-1}$.

## Class-A dependency detail

Algebraic endpoint or gauge shifts preserve algebraicity whether or not they
cancel.  Endpoint compatibility is needed for canonical gauge invariance,
not for the capacity theorem.  A constant $G=\log2$ on the identity map of
$\mathbb A^2$ is the positive-dimensional forbidden control.

## Corollaries and scope

The selector/union theorem is obtained by setting two of $(v,\log q,\alpha)$
to zero.  The escape map is only the contraposition of the certificate
assumptions.  It is not a universal no-go theorem, complete trichotomy, or a
sufficiency claim, and it has no Riemann-zero or Route-B consequence.
