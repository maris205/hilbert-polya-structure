# LG4 Round 2 — finite-ring invariant separators and their degree cost

2026-09-09 UTC. B1 author. Exclusive new-file scope:
`continuation_round2/b1_global_orbit_separation/`.

## Original claim, unchanged

For every integral polynomial automorphism $F$ of $\mathbb A^2$, whose inverse
also has integral polynomial coordinates, and every $P,Q\in\mathbb Z^2$,
determine whether
$$
Q\in\{F^nP:n\in\mathbb Z\}
\quad\Longleftrightarrow\quad
\forall m\ge2\;\exists n_m\in\mathbb Z:
F^{n_m}P\equiv Q\pmod m.                       \tag{LG4}
$$
All integer times, all prime powers, and mixed moduli remain in scope. This
round does not replace the original claim with a periodic-target or one-prime
problem. The original proof status is `NOT CURRENTLY JUSTIFIED`.

The accepted first-pass virtual-centralizer theorem, local interpolation,
finite-place Green-function failure, and equivalent bounded-height condition
are read-only inputs and are not repeated as new progress.

## Primary-source triage before freezing the new target

Read the current Hénon instructions, `CONTINUOUS_RUN.md`,
`FIRST_PASS_DECISION.md`, and the complete 328-line
[E7 final audit](../../reviews/e7_congruence/REVIEW.md). The local theorem and
source records establish the previous scope and what has already been
accepted. This is a continuation of that gap, not a new claim that the old
results need rechecking.

Eight targeted searches covered Hénon local-global orbit incidence,
wandering-point dynamical Hasse principles, reduction of orbit intersections,
the dynamical support problem, and two-sided orbit separation. They retrieved
the primary author-hosted AKNTVV article but no applicable general Hénon
separation theorem. Its relevant target hypotheses remain invariant or
preperiodic; its predecessor obstruction remains forward-time. This bounded
search does not certify that LG4 is a publicly recognized open problem.

## Frozen missing mechanism and decisive test

A finite quotient can separate two orbits by a function constant along the
finite $F$-cycles. The new question is whether such separating functions can
be realized by polynomial formulas of bounded degree while the modulus is
allowed to grow arbitrarily.

Fix $D\ge1$. At each modulus $m$, allow every polynomial
$h\in(\mathbb Z/m\mathbb Z)[x,y]$ of total degree at most $D$ that satisfies
$$
h(F(z))=h(z)\quad\text{for all }z\in(\mathbb Z/m\mathbb Z)^2.  \tag{INV}
$$
This is pointwise function invariance, weaker than polynomial-identity
invariance. The coefficients may vary independently with $m$, and any number
of such invariant observables is permitted.

**Exact target (BDQ).** For each $F$ with
$\mathbb Q[x,y]^F=\mathbb Q$ and each $D$, construct one effectively specified
positive integer $\Delta(F,D)$ such that
$$
P\equiv Q\pmod{\Delta(F,D)}
\Longrightarrow
\bigl[h(P)=h(Q)\pmod m\text{ for every }m\ge2
\text{ and every degree-}\le D\text{ function satisfying (INV)}\bigr].
$$
If proved, this defeats a bounded-degree algebraic invariant-separator route
and supplies an exact all-modulus complexity boundary. It is not a
counterexample to LG4, because unbounded-degree functions and arbitrary
finite quotient data remain allowed.

**Decisive proof/check.** Form the integer matrix of evaluations of
$b\circ F-b$ for the nonconstant monomials $b$ of degree at most $D$ on a
fixed finite interpolation grid. The key check is full column rank over
$\mathbb Q$ under the displayed no-invariant hypothesis. An adjugate
identity must then retain all modulus factors, including nonunits and mixed
moduli; replacing a congruence by division by its determinant is forbidden.

No mathematical program was proposed or run. The finite matrix is an
explicit symbolic definition with an all-input proof, not a computed census.

## Final round-2 result

The complete argument is in [PROOF_PACKAGE.md](PROOF_PACKAGE.md). All three
results below are source-subtracted auxiliary results, pending nonauthor
review. They do not close LG4 and do not constitute a new paper admission.

### 1. BDQ is proved, including function invariants at bad and mixed moduli

Put $d=\max(\deg F_1,\deg F_2)$, $L=dD$, and enumerate the nonconstant
monomials $b_1,\ldots,b_N$ of total degree at most $D$. The exact row set is
$G=\{0,\ldots,L\}^2$, and
$$
M_{z,j}=b_j(F(z))-b_j(z).
$$
The no-invariant assumption gives full column rank over $\mathbb Q$.
Define $\Delta(F,D)$ to be the absolute determinant of the first nonzero
maximal square row minor in the specified order. Integer-valued Newton
expansion proves that the grid checks pointwise invariance over every
residue ring, including rings with zero divisors. The adjugate identity
then gives $\Delta a_j=0\pmod m$ for every nonconstant coefficient, without
inverting $\Delta$. This proves BDQ at every modulus.

For $F_0(x,y)=(y,y^3-x)$ the package also verifies the no-invariant
hypothesis without relying on an unverified citation. The explicit pair
$$
P=(1,2),\qquad Q_D=(1+10\Delta(F_0,D),2)
$$
consists of nonperiodic points on distinct two-sided integer orbits, yet
passes all degree-at-most-$D$ invariant polynomial tests at every modulus.
The pair depends on $D$; it is not an LG4 false positive.

### 2. Unrestricted polynomial invariants have an exact prime-power scope

For every integral polynomial automorphism and every integer pair, the
package proves
$$
\begin{split}
&\text{equality under all invariant polynomial functions at all moduli}\\
&\qquad\Longleftrightarrow
\text{same finite orbit modulo every separate prime power}.
\end{split}
$$
If a cycle separates the points modulo $q=p^r$, denominator-cleared
integer-valued interpolation constructs an ordinary polynomial separator
of degree at most $2(q-1)$, invariant modulo
$$
p^{\,2v_p((q-1)!)+1}.
$$
The increase of the modulus is essential to the construction as stated.
The converse is CRT on polynomial values. This reduction identifies what
unbounded degree can recover, but supplies neither a prime-power
separation theorem for integer off-orbit points nor a global height bound.

### 3. Scalar polynomial values do not directly encode mixed time phases

For $F(x,y)=(y,x+6y^2)$, $P=(0,1)$ and $Q=(4,3)$, the modulo-$6$ orbit
of $P$ excludes $Q$. The local hitting times are even modulo $2$ and odd
modulo $3$. Every invariant polynomial function modulo $6$ nevertheless
has equal values at the two points. This is an exact single-modulus
control. The pair is separated modulo $4$, so it does not pass the
all-level prime-power test.

In general, local hitting-time cosets $a_q+t_q\mathbb Z$ can be glued
across prime-power factors of a mixed modulus precisely when
$a_{q_i}\equiv a_{q_j}\pmod{\gcd(t_{q_i},t_{q_j})}$ for every pair. The
unrestricted polynomial-value test asserts separate prime-power hits,
not these compatibility congruences. No counterexample or proof is given
here for the possibility that the all-level conditions might force them
through additional dynamics.

## Source audit and ownership

The targeted local-global search accessed the primary author copy of
Amerik–Kurlberg–Nguyen–Towsley–Viray–Voloch,
[“Evidence for the Dynamical Brauer–Manin Criterion”](https://www.imo.universite-paris-saclay.fr/~ekaterina.amerik/articles/DBM.pdf),
*Experimental Mathematics* **25** (2016), 54–65. The actual passages
checked were Theorems 4.2–4.4 (printed page 60) and Proposition 4.9 with
its proof (printed page 63). Their invariant/preperiodic target
hypotheses and the forward-time obstruction do not supply arbitrary
nonperiodic Hénon two-sided orbit separation. No novelty or public-open-
problem conclusion is inferred from failure to find such a theorem.

The unrestricted interpolation investigation then identified an explicit
source collision: Schauz's
[author preprint](https://arxiv.org/pdf/1212.5522), Corollary 3.7,
Theorem 3.8, and Theorems 3.14–3.17. Exact bibliographic attribution,
the ordinary-polynomial/polyfract distinction, and the subtraction are
recorded in the proof package. The general interpolation and primary
decomposition are owned by existing work. The dynamical specialization
and explicit clearing-factor bound are not offered as a paper.

Actual read-only work comprised targeted web searches, primary-source
passage inspection, local context reads, and symbolic hand proofs.
Search coverage is bounded; no exhaustive literature audit is claimed.
No external research upload, mathematical execution, manuscript, PDF,
formal evaluation, Git operation, first-pass modification, or shared
index edit was performed by this lane.

## Reusable interface and remaining task

Input: $F\in\operatorname{Aut}_{\mathbb Z}(\mathbb A^2)$ and a separated
cycle modulo a specified $p^r$. Output: an explicitly defined ordinary
integer polynomial invariant separator at the prime-power modulus and
degree bound above. With the additional no-invariant assumption and a
fixed degree, BDQ instead gives an explicit congruence class on which all
such bounded-degree tests agree across every modulus.

To separate every off-orbit integer point using these scalar polynomial
invariants, the missing arithmetic input is the stronger assertion that
some **prime-power** modulus always separates it. That assertion is not
proved. To preserve the original, possibly mixed-modulus LG4 task without
this stronger demand, a new mechanism must retain actual finite cycle
labels or the complete compatible hitting-time cosets. Merely invoking
unbounded-degree polynomial interpolation does not close that gap.

Recommended bounded nonauthor audit: the whole proof package, focusing on
grid sufficiency over all residue rings, the integer minor argument,
the no-invariant Hénon proof, denominator clearing at $p^{s+1}$, and the
all-modulus/all-prime-power/mixed-phase quantifier distinctions.

Final author disposition: **auxiliary result ready for internal review;
LG4 remains `NOT CURRENTLY JUSTIFIED`; paper count contribution 0.**
