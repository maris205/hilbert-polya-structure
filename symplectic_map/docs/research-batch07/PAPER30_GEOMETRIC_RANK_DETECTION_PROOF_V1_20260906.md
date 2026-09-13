# Paper30 geometric detection: a multiplication-rank route

Date: 2026-09-06. Status: NEW_AUTHOR_PROOF_PACKAGE, NOT_INDEPENDENTLY_ACCEPTED.
This is a new proof addressing the actual main gap of the earlier
[geometric probe](PAPER30_GEOMETRIC_TEST_PROBE_20260906.md). That frozen
probe and its [checked erratum](PAPER30_GEOMETRIC_TEST_ERRATUM_20260906.md)
remain unchanged. Its earlier OPEN assessment records the state before
this argument; the present claimed closure still requires independent
proof checking, targeted novelty work and candidate evaluation.
The quantum and wild-cover packages are not included in this proof.

## 1. Exact claims, assumptions and notation

Fix complex polynomials $p_i$ of degrees $d_i\ge2$ with nonzero leading
coefficients, indexed periodically with period $k\ge1$. Use the same
actual orbit-coordinate convention as Paper29:
$$
X_0=x,\quad X_{-1}=y,\quad
X_{i+1}+X_{i-1}=p_i(X_i),\quad \sigma X_i=X_{i+k}.
$$
The induced polynomial symplectic automorphism is denoted $F$, with
$\sigma=F^*$ and dynamical degree $\delta=\prod_{i=0}^{k-1}d_i>1$.
Write $A=\mathbb C[x,y]$, $S_ng=\sum_{j=0}^{n-1}\sigma^jg$, $N=kn$,
and $A_N$ for the complete fixed-scheme ring of $F^n$.

Use the accepted standard orbit basis $M_e=\prod_iX_i^{e_i}$, where
$0\le e_i<d_i$ and only finitely many $e_i$ are nonzero. The diameter
$L(g)$ is the largest support diameter of an individual nonconstant word
in $g$'s normal form, with maximum zero if there is none. For $L\ge0$ put
$$
V_L=\max_{a\in\{0,\ldots,k-1\}}\prod_{j=0}^{L}d_{a+j},
\qquad \kappa_L=V_L^{-1}>0.                              \tag{1}
$$
Let $s_n(F)$ be the number of saddle **points** of least period exactly
$n$, and $r_n(F)$ the number of all distinct geometric points fixed by
$F^n$. All cardinalities are unweighted point counts, not orbit counts.

For a degree bound $D\ge0$, let $L_D$ be any known integer satisfying
$L(g)\le L_D$ for all $\deg g\le D$, and set $\kappa_D=\kappa_{L_D}$.
Such an $L_D$ is finite and explicit from Paper29's degree-to-diameter
bound. Equivalently, take the maximum diameter among the finitely many
standard words of ordinary coordinate degree at most $D$, including zero
as the empty maximum. The accepted triangular basis makes this an actual
bound for every degree-at-most-$D$ polynomial, not an assumed support bound.

**G1: finite rank/defect certificate — PROVABLE AS STATED.** If
$N\ge3$, $N>2L(g)$ and $g\notin(\sigma-1)A$, then multiplication by
$f=[S_ng]\in A_N$ has rank at least
$$
\operatorname{rank}(m_f)\ge\kappa_{L(g)}\delta^n.        \tag{2}
$$
The number of geometric zeros of $S_ng$ in $\operatorname{Fix}(F^n)$
is at most $(1-\kappa_{L(g)})\delta^n$. In particular,
$$
r_n(F)>(1-\kappa_D)\delta^n                             \tag{3}
$$
certifies that complete geometric point testing at this period detects
all polynomial coboundaries of degree at most $D$ exactly, provided
$kn\ge3$ and $kn>2L_D$.

**G2: eventual geometric and saddle detection — PROVABLE AS STATED.**
For each fixed $F,D$ there is $n_0(F,D)$ such that for **every integer**
$n\ge n_0(F,D)$ and every $g\in A$ of degree at most $D$,
$$
S_ng(z)=0\quad\text{for every saddle point of least period }n
\quad\Longleftrightarrow\quad g\in(\sigma-1)A.          \tag{4}
$$
The same equivalence holds if one tests all geometric points fixed by
$F^n$. In fact every non-coboundary in this degree range has nonzero
$S_ng$ on at least $(\kappa_D/2)\delta^n$ such saddle points for all
sufficiently large $n$, uniformly over these $g$.

**G3: an exact adaptive algebraic certificate — PROVABLE AS STATED.**
For coefficients in a given number field, exact finite linear algebra
on the cyclic scheme rings gives a terminating search for one period
satisfying (3), and a geometric-values-only trace-pairing test at that
period. This is an adaptive terminating algorithm, not an explicit a priori
bound on $n_0$, a degree-only bound, or a polynomial-time complexity claim.

## 2. Strategy, dependencies and the critical change of argument

The previous Loewy route sought a bound on the worst local degeneration.
No such bound is used here. Instead, a nonzero short-word orbit sum forces
a fixed positive fraction of the entire algebra into its multiplication
image. Vanishing at geometric points would force too large a defect in
the distinct-point count.

Dependencies, separated from the new combination, are:

1. **Paper29, accepted:** infinite standard words and their orbit-sum
   obstructions; the full cyclic standard basis of size $\delta^n$;
   no alias for $N>2L$; ordinary-degree control of $L_D$.
2. **Elementary leading-monomial/footprint argument:** the rank lower bound
   for multiplication in a zero-dimensional ring, proved in §3. This is
   a standard type of algebraic bound; its general principle is not claimed
   new. The dedicated primary-source check will locate the closest prior.
3. **Bedford–Lyubich–Smillie, existing theorem:** for every fixed complex
   polynomial automorphism with dynamical degree $\delta>1$,
   $s_n(F)/\delta^n\to1$ as $n\to\infty$ through all integers.
4. **Finite Artin-algebra trace pairing:** its rank counts distinct
   geometric points in characteristic zero, proved directly in §6.

G1 combines 1 and 2. G2 combines G1 with 3, not with a uniform Loewy bound.
G3 combines G1, the asymptotic termination supplied by 3, and 4.
The general standard tools are stated explicitly to permit novelty and
substantive-capacity deductions rather than counting them as new theories.

## 3. Multiplication rank in a monic staircase ring

Let $B=K[z_0,\ldots,z_{N-1}]/I$ over a field, where for a degree-compatible
monomial order the initial ideal is $(z_0^{d_0},\ldots,z_{N-1}^{d_{N-1}})$.
Its standard monomials have exponents $0\le u_i<d_i$.
Let $0\ne f\in B$ have normal-form leading monomial $z^e$.

**Lemma.** One has
$$
\operatorname{rank}_K(m_f)\ge\prod_{i=0}^{N-1}(d_i-e_i).\tag{5}
$$

**Proof.** For each exponent vector $u$ with $0\le u_i<d_i-e_i$, consider
$fz^u$. The monomial $z^{e+u}$ is standard. Before reduction it is the
leading monomial of the product, with nonzero coefficient, because a
monomial order is preserved by multiplication. Every other monomial in
the product is smaller, and every step of Gröbner reduction replaces a
monomial by smaller monomials. Reduction therefore cannot remove or
cancel $z^{e+u}$ or produce a larger term. Its normal form still has
leading monomial $z^{e+u}$.

These leading monomials are different for different $u$. In a nonzero
linear combination of these normal forms, choose the largest leading
monomial among terms with nonzero coefficients. No smaller-leading normal
form contains that monomial, so it cannot cancel. The images are linearly
independent. Their number is the right-hand side of (5).

For the cyclic ring $A_N$, $N\ge3$, the relations are
$p_i(z_i)-z_{i-1}-z_{i+1}$. Divide each by its nonzero leading coefficient.
In graded lexicographic order its leading monomial is $z_i^{d_i}$.
These leading monomials are pairwise relatively prime, so the relations
form a Gröbner basis; alternatively this is the already accepted cyclic
standard-basis statement. All nonleading replacements strictly lower
formal $z$ total degree. Nonreducedness of the quotient changes none of
these facts. This paragraph does not assume that the leading coefficients
were originally one.

## 4. Apply the rank bound to a periodic orbit sum

Suppose $g\notin(\sigma-1)A$, $N\ge3$, $N>2L(g)$. Combine its coefficients
on each infinite macro-word orbit. Paper29's exact cyclic no-alias result
gives the nonzero normal form
$$
f=[S_ng]=nc_0[1]+\sum_O c_O\sum_{j=0}^{n-1}W_N(\sigma^jM_O),\tag{6}
$$
with disjoint nonconstant cyclic basis supports and $c_O$ the infinite
orbit coefficient sums. Every nonconstant monomial occurring on the right
is a wrapped short word of individual diameter at most $L(g)$.

If the leading monomial of $f$ is constant, then $f$ is a nonzero constant
and its multiplication rank is $\delta^n$, which implies (2).
Otherwise let its exponents be $e_i$, with support $J$ contained in a
cyclic interval of length at most $L(g)+1$. Using (5),
$$
\operatorname{rank}(m_f)
\ge\delta^n\prod_{i\in J}\left(1-\frac{e_i}{d_i}\right)
\ge\frac{\delta^n}{\prod_{i\in J}d_i}
\ge\frac{\delta^n}{V_{L(g)}}.                          \tag{7}
$$
For the last inequality, include any unoccupied sites of that interval;
all degrees are at least two. The cyclic interval may cross the chosen
index zero. Since $k\mid N$, the phase product is one of the products in
(1). There is no dependence on which monomial becomes largest at this $n$.
Thus (2) holds with a constant independent of $n$ and of the coefficients
of $g$. For $\deg g\le D$, $V_{L(g)}\le V_{L_D}$, so the same lower bound
$\kappa_D\delta^n$ holds uniformly.

Now decompose $A_N=\prod_z B_z$ over its geometric points. If $f(z)=0$,
then $f$ lies in the maximal ideal of the local Artin algebra $B_z$;
multiplication by $f$ is nilpotent and hence has kernel dimension at least
one on that nonzero vector space. Distinct local factors contribute
independent kernel vectors. Consequently
$$
\#\{z\in\operatorname{Fix}(F^n):S_ng(z)=0\}
\le\dim\ker(m_f)
=\delta^n-\operatorname{rank}(m_f)
\le(1-\kappa_{L(g)})\delta^n.                          \tag{8}
$$
This proves G1, including (3). Equivalently, a false geometric positive
would force the total distinct-point defect
$\delta^n-r_n(F)$ to be at least $\kappa_D\delta^n$.
No maximum local Loewy length has been estimated.

## 5. Close the fixed-map geometric theorem with the saddle count

The one external dynamical input is Bedford–Lyubich–Smillie,
*Distribution of Periodic Points of Polynomial Diffeomorphisms of
$\mathbb C^2$*, Invent. Math. 114 (1993), 277–288, §1 Corollary 1.
Root has read the definitions, Theorem 1 and Corollary 1 in the first two
pages of the [original author version](https://arxiv.org/pdf/math/9301220v1).
They define $\mathrm{SPer}_n$ as the set of saddle points of least period
exactly $n$ and prove
$$
\lim_{n\to\infty}\delta^{-n}\#\mathrm{SPer}_n=1.       \tag{9}
$$
The map is fixed, the limit is over all positive integers, and there is
no global hyperbolicity or dissipativity assumption. This is a prior
theorem, not a newly proved count. Each such saddle is simple in the fixed
scheme because neither eigenvalue of its return derivative is one.

Fix $F,D$. By (9), there exists $n_1(F,D)$ such that for every $n\ge n_1$,
$$
s_n(F)>(1-\kappa_D/2)\delta^n.                        \tag{10}
$$
Increase $n_1$ so that also $kn\ge3$ and $kn>2L_D$, and call the result
$n_0(F,D)$. If $g$ in the specified degree range is not a coboundary,
(8) bounds all its zero-valued geometric periodic points. In particular,
among the saddle points of least period $n$, the number with nonzero
orbit sum is at least
$$
s_n(F)-(1-\kappa_D)\delta^n
> (\kappa_D/2)\delta^n.                                \tag{11}
$$
This proves the forward detection implication and the uniform positive
density assertion. A coboundary telescopes to zero on every periodic
point, proving the converse. Since the saddle set is contained in the
complete geometric fixed set, its version of the equivalence follows too.
The choice of $n_0$ depends on $F,D$ but not on the particular $g$.

It follows that testing all geometric periodic orbits, or just all saddle
periodic orbits, detects polynomial coboundaries without a degree bound:
any given polynomial has some finite degree to which the theorem applies.
This does not assert one uniform period for polynomials of unbounded degree.

A useful finite-data version of the same proof is that any set of more
than $(1-\kappa_D)\delta^n$ distinct geometric fixed points is a detecting
set under the short-word period condition. This permits discarding a fixed
fraction of the eventual saddle data. It is a consequence of (8), not a
separately claimed coding or statistical theory.

## 6. Trace pairing: a computable distinct-point certificate

For any finite-dimensional commutative algebra $B$ over $\mathbb C$, let
$$
\Gamma_B(a,b)=\operatorname{Tr}_B(m_{ab}).
$$
Write its local Artin decomposition $B=\prod_z B_z$ and
$\ell_z=\dim B_z$. In a local factor, multiplication by $u$ is the sum of
$u(z)$ times the identity and a nilpotent operator. Its trace is
$\ell_z u(z)$. Hence
$$
\Gamma_B(a,b)=\sum_z\ell_z a(z)b(z).                    \tag{12}
$$
The radical of this bilinear pairing is exactly the nilradical of $B$:
nilpotent elements have every value zero, while a nonzero value is detected
by the idempotent supported on that one local factor. Characteristic zero
ensures $\ell_z\ne0$. Thus
$$
\operatorname{rank}\Gamma_B=\#\operatorname{Spec}(B)(\mathbb C),
\qquad \Gamma_B(f,-)=0\ \Longleftrightarrow\ f(z)=0\ \forall z.\tag{13}
$$
These are elementary standard trace-form facts. They are not assertions
that a single trace $\operatorname{Tr}(m_f)$ separates points or nilpotents.

Apply (13) to $B=A_N$ in its known standard basis. Condition (3) can be
checked exactly as
$$
\operatorname{rank}\Gamma_{A_N}>(1-\kappa_D)\delta^n.  \tag{14}
$$
Once (14) and the short-word conditions hold, the vector of pairings
$\Gamma_{A_N}([S_ng],b)$ for all standard basis elements $b$ vanishes
exactly when $g$ is a coboundary. By (12) these are weighted geometric
value moments; they annihilate nilpotent directions, unlike testing
$[S_ng]=0$ in the full scheme ring before this new certification.

For polynomials over an explicitly given number field $K$, all cyclic
relations, multiplication matrices and entries of $\Gamma$ are exactly
computable in $K$. Their rank is unchanged after extension to $\mathbb C$.
The following procedure therefore terminates:

1. Compute a valid $L_D$ and rational $\kappa_D$ from the fixed degrees
   and the accepted orbit-word degree formulas.
2. Enumerate integer periods with $kn\ge3$ and $kn>2L_D$.
3. Form the cyclic standard ring and its trace-pairing matrix by exact
   polynomial reduction. Stop at the first period satisfying (14).

Termination follows because $r_n\ge s_n$ and (9) eventually guarantees
(14). After termination, the complete pairing vector provides the stated
test for every input $g$ of degree at most $D$; the period search depends
only on $F,D$, not on that input. This proves G3. No numerical separation
of nearly colliding roots or empirical stopping threshold is used.

## 7. Boundaries, compatibility and independent checks still required

This proof does not change the earlier finite-period counterexample or
the across-maps resonance family. It allows all individual collisions;
what becomes small for a fixed map is the **total distinct-point defect**
relative to $\delta^n$, by an existing global theorem. Arbitrarily large
Loewy length somewhere is not the same as a positive fraction of the full
periodic algebra. The earlier separated-block power lemma remains a
different, valid quantitative obstruction; G2 does not assume its missing
Loewy bound has been proved.

No uniformity in a parameter family is inferred from (9). The author
has not proved a numerical convergence rate, a priori period bound,
degree-only threshold or optimal sampling/algorithmic complexity. G3's
terminating exact search is a distinct effective statement, not a claim
to any of those stronger bounds. The $N=1,2$ rings are not needed for G1–G3;
they remain outside the displayed short-word hypothesis $N\ge3$.

The next independent mathematical check must test the leading-monomial
rank argument, the cyclic phase product, the uniform-over-$g$ quantifiers,
the defect versus Loewy distinction, and the trace-form termination claim.
The parallel one-source saddle-count check confirms the external theorem's
exact hypotheses; its final report must still be read. A targeted novelty
comparison must deduct the general footprint bound, BLS count, trace-form
facts and Paper29's no-alias theorem, and check whether this combination
or a stronger polynomial geometric Livšic theorem is already available.

Until those steps and fresh candidate evaluation are complete, this is an
author proof package only. No manuscript, lock, build, PDF or Paper30
acceptance is implied. Batch07 remains 3/5; all accepted papers are untouched.
Route applicability is NOT_APPLICABLE, with local research effects only.
