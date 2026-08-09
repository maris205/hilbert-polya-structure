# Source and novelty audit

## Audit verdict

The fixed-word sequence \(\{\Delta_{w,r}\}_{r\geq 1}\) is a classical
cyclic-resultant sequence of a packet multiplier polynomial.  Consequently,
the definition of \(\Delta_{w,r}\), its computation by a full fixed-point
packet, the divisibility for \(r\mid s\), and recurrence or reconstruction
properties for a fixed word are **baselines, not novelty claims**.

The only presently viable novelty target is narrower: an exact, all-period
relation between multiplier polynomials (or cyclic resultants) attached to
different chronological Hénon words that is not reproduced by matched
reciprocal-polynomial or reversible-map controls.  A finite pair of
prime-separation certificates does not meet that target.

## Hénon multiplier rigidity: scope of the 2026 source

Cantat and Dujardin's **2026 preprint** states that, for a given degree, a
complex Hénon map is determined up to finitely many choices by its multiplier
spectrum (indeed, by the unstable multipliers of saddle periodic points).  For
compositions, the statement assumes fixed multi-degree and multi-Jacobian.

- S. Cantat and R. Dujardin, *Multiplier rigidity for complex Hénon maps*,
  preprint submitted 10 March 2026,
  [arXiv:2603.09445](https://arxiv.org/abs/2603.09445).

This is a complex-analytic rigidity statement.  Its abstract does **not**
state arithmetic rigidity, reduction-mod-prime results, Fitting/different
ideal identities, cyclic-resultant divisibility, Zsigmondy theorems, or
relations among chronology-indexed word families.  It supports the choice of
multiplier data as a natural observable, but it cannot supply the arithmetic
claim sought here.

## Exact cyclic-resultant baseline

Let \(K=\operatorname{Frac}(R)\), and work first on the finite generic
fixed-point algebra \(A_{w,K}\).  Define the packet multiplier polynomial

\[
P_w(T)
  :=\operatorname{Norm}_{A_{w,K}/K}\!\bigl(\det(TI-M_w)\bigr).
\]

Geometrically, its roots are all eigenvalues of the tangent return matrices
at the fixed-point packet, with scheme multiplicity.  Since every tangent
matrix is \(2\times2\), \(P_w\) has even degree.  Directly from the definition
of the resultant,

\[
\boxed{
\Delta_{w,r}
 =\operatorname{Norm}_{A_{w,K}/K}\!\bigl(\det(I-M_w^r)\bigr)
 =\operatorname{Res}_T\!\left(P_w(T),T^r-1\right).
}
\]

With the displayed monic-polynomial convention the possible rootwise sign is
\((-1)^{\deg P_w}=1\), so the identity is exact.  Its integral interpretation
still requires a canonical finite-flat model or a fixed canonical
presentation over \(R\).

The right-hand side is the \(r\)-th cyclic resultant of \(P_w\).  Hillar
classifies polynomials with the same nonzero cyclic resultants and proves
rigidity for reciprocal polynomials.  Hillar--Levine prove finite-determination
bounds and polynomial recurrences for cyclic-resultant sequences.

- C. J. Hillar, *Cyclic Resultants*, J. Symbolic Comput. 39 (2005),
  [arXiv:math/0401220](https://arxiv.org/abs/math/0401220).
- C. J. Hillar and L. Levine, *Polynomial recurrences and cyclic resultants*,
  [arXiv:math/0411414](https://arxiv.org/abs/math/0411414).

In particular, if \(r\mid s\), the factorization
\(T^r-1\mid T^s-1\) gives the corresponding fixed-word divisibility whenever
the cyclic resultants are integral.  This automatic divisibility, as well as
any recurrence or recovery of \(P_w\) from its own \(r\)-sequence, cannot be
promoted as a Hénon-specific discovery.  Strong-gcd identities are not being
asserted by this observation and must not be conflated with the automatic
divisibility.

## Direct dynatomic, multiplier, and discriminant precedents

Several sources are closer to the construction than a generic
primitive-divisor analogy:

- B. Hutz constructs effective dynatomic cycles, degrees, and formal-period
  multiplicities for morphisms of projective varieties.
  [arXiv:0801.3643](https://arxiv.org/abs/0801.3643)
- B. Hutz relates primitive period over a discrete valuation ring to reduced
  period, the order of the induced action on the cotangent space, and the
  residue characteristic.  This is a direct control for interpreting
  multiplier orders modulo a prime.
  [arXiv:0801.3645](https://arxiv.org/abs/0801.3645)
- B. Hutz constructs conjugacy-invariant functions from the complete
  multiplier matrices of periodic points in dimension greater than one and
  gives a zero-dimensional elimination/Gröbner method for computing the
  product of their characteristic polynomials without solving for individual
  points.
  [arXiv:1908.03184](https://arxiv.org/abs/1908.03184)
- P. Morton and F. Vivaldi express polynomial-map bifurcation/discriminant
  data algebraically in terms of periodic-orbit and multiplier polynomials,
  including an integral-domain formulation: *Bifurcations and discriminants
  for polynomial maps*, Nonlinearity 8 (1995), 571--584,
  [doi:10.1088/0951-7715/8/4/006](https://doi.org/10.1088/0951-7715/8/4/006).
- Y. Murakami, K. Sano, and K. Takehira prove arithmetic integrality results
  for multiplier polynomials and study parabolic parameters in polynomial
  families.
  [arXiv:2403.17315](https://arxiv.org/abs/2403.17315)
- P. Morton and J. H. Silverman develop periodic-point multiplicity and
  dynamical-unit foundations: *Periodic points, multiplicities, and
  dynamical units*, J. Reine Angew. Math. 461 (1995), 81--122,
  [doi:10.1515/crll.1995.461.81](https://doi.org/10.1515/crll.1995.461.81).
- J. R. Doyle, P. Fili, and T. Hyde develop universal
  dynatomic/necklace relations and dynamical units.
  [arXiv:2108.09333](https://arxiv.org/abs/2108.09333)
- J. Doyle, H. Krieger, A. Obus, R. Pries, S. Rubinstein-Salzedo, and L. West
  study bad reduction and ramification discriminants of one-dimensional
  dynatomic curves.
  [arXiv:1703.04172](https://arxiv.org/abs/1703.04172)

Hutz's projective-space theorems concern endomorphisms, whereas a Hénon map
extends birationally; the cited results therefore do not automatically prove
the Hénon statements.  They are nevertheless direct definitional and
computational prior art.  Likewise, the one-dimensional discriminant results
do not settle a chronology-preserving two-dimensional cross-word theorem,
but they rule out presenting multiplier-polynomial elimination or
nontransversality primes alone as new.

## Additional arithmetic-dynamical controls

- S. Kawaguchi proves the canonical-height framework for regular polynomial
  automorphisms; periodic points have canonical height zero.
  [arXiv:math/0405007](https://arxiv.org/abs/math/0405007)
- P. Ingram studies Hénon canonical heights and specialization.
  [arXiv:1111.3609](https://arxiv.org/abs/1111.3609)
- L.-C. Hsia and S. Kawaguchi develop adelic Hénon-family heights.
  [arXiv:1810.03841](https://arxiv.org/abs/1810.03841)
- P. Ingram and J. Silverman develop primitive divisors in arithmetic
  dynamics.
  [arXiv:0707.2505](https://arxiv.org/abs/0707.2505)

The height literature blocks a tempting but empty alternative: the canonical
height of a periodic point cannot serve as a nonzero orbit roof.  The
primitive-divisor literature is relevant only after a canonical single-index
sequence, or a cutoff-independent partial order, has been fixed.

## Targeted prior-art search and residual novelty

The 2026-08-09 targeted primary-source search used the combinations

- Hénon + multiplier spectrum;
- Hénon + fixed point scheme + ramification;
- Hénon + dynatomic discriminant;
- polynomial automorphism + primitive divisor;
- multiplier polynomial + resultant;
- cyclic resultant + recurrence/rigidity;
- dynatomic + discriminant/reduction.

No source was located that states the exact desired theorem: a
chronology-preserving relation among \(P_w\) or \(\Delta_{w,r}\) for distinct
Hénon composition words.  This absence is not by itself a novelty result.
The search did locate the direct classical baselines above, so the novelty
claim is **provisional and strictly cross-word/cross-period**.

The admissible delta, if one exists, is therefore:

> a Hénon-specific, chronology-preserving, all-period relation between
> distinct word packets, remaining after the dynatomic,
> multiplier-invariant, and cyclic-resultant baselines are subtracted and
> after matched reciprocal-polynomial and reversible-map nulls fail.

If no explicit falsifiable relation of this kind can be stated before opening
the extended ledger, the candidate is a no-go rather than an invitation to
search post hoc correlations.

## Distinction from repository work

- C03/C12A used finite-set Frobenius permutations at fixed period; C23 uses
  tangent nontransversality and varies \(n,r\).
- C12B/C19--C21 used selected characters or fixed-period covers; C23 takes
  the full canonical packet norm and selects no Galois root.
- C22G cancelled \(\det(I-M)\) analytically; C23 treats its arithmetic
  nonunit ideal as the observable.
- The first-gate prime scan is not a fitted prime table: all degree-good
  primes through the frozen bound are emitted, including null rows.

These distinctions explain the repository role of the computation; they do
not override the external cyclic-resultant and multiplier-polynomial
baselines.  The two explicit separating primes are finite arithmetic
chronology certificates, not a new Euler product, a Zsigmondy theorem, or a
standalone conceptual novelty claim.
