# Effective cyclotomic periodic-point exhaustion by torsion descent

Date: 2026-09-08. AF5-C, original fifth-pass full contract, sixth-pass
closing attempt. Coordinator-authored global argument; no mathematical
program has been executed. This is not a manuscript or an admission.

## 1. Claim and current status

For every input integer $c$, give an explicit terminating exact procedure
that outputs the set

$$S_c=\operatorname{Per}(F_c,\mathbb A^2(\mathbb Q^{\rm cyc})),
\qquad F_c(x,y)=(y,y^2+c-x),$$

and the least positive native period of every point. Here
$\mathbb Q^{\rm cyc}=\mathbb Q(\mu_\infty)$ in a fixed algebraic closure
of $\mathbb Q$. Coordinates equal to zero and all integer parameters are
included. No a priori period, field-degree, or conductor cutoff is imposed.
The output is an exact finite algebraic list, not a numerical approximation.

**Original-claim proof status: PROVABLE AS STATED**, with the external
finite-set theorem (F) explicitly retained. The coordinator has now read
the complete effective lemmas (E) and (T), including their proofs, and the
previously provisional dependencies are supplied below. There is no
unspecified Loxton constant or qualitative torsion-closure oracle.
Non-author review and the independent-increment admission judgment are
separate gates; a complete effective corollary is not automatically a paper.

## 2. Assumptions, classical inputs, and dependencies

Throughout, varieties are reduced algebraic sets over $\overline{\mathbb Q}$,
not schemes. The torus $\mathbb G_m^d$ has torsion subgroup
$\mu_\infty^d$. A connected torsion coset is $\tau H$, where
$H\subseteq\mathbb G_m^d$ is a connected algebraic subtorus and
$\tau\in\mu_\infty^d$.

The following two statements are supplied in effective form.

**(E), effective length.** For positive integers $H$, put

$$L(H)=H\left(\prod_{p\le4H,\ p\ {\rm prime}}(p-1)\right)(2H)^{2H}.$$

Every cyclotomic algebraic
integer $\alpha$ with house at most $\sqrt H$ is a sum of at most $L(H)$
roots of unity. The zero sum may be empty. The lemma need not construct a
representation from $\alpha$; only the computable uniform length is used.
The full trace/ambient-index descent proof is
[EFFECTIVE_LENGTH_LEMMA.md](../cyclotomic_sources/EFFECTIVE_LENGTH_LEMMA.md).

**(T), exact torsion kernel.** Given finitely many Laurent equations with
explicit cyclotomic coefficients, an algorithm produces finitely many
connected torsion cosets whose union is exactly the Zariski closure of all
torsion solutions. Each coset is represented effectively by a torsion
basepoint and a saturated character lattice, or by equivalent exact
binomial/monomial data. Intersections, coordinate projections, torsion
basepoints, and equality of finite unions are computable. Projection
satisfies the exact torsion lifting identity in Step 4 below. The full
rational-Mann/Smith-normal-form algorithm and proof are in
[the torsion kernel](../torsion_kernel/PROOF_PACKAGE.md), Steps 1–8.
The claim is classical; an existing different explicit algorithm is
Kedlaya–Kolpakov–Poonen–Rubinstein,
[Algorithm 7.5 and Theorem 7.6](https://math.mit.edu/~poonen/papers/space_vectors.pdf),
which also uses Noetherianity to prove termination. Neither effective
torsion closure nor Noetherian termination is claimed as a new ingredient.

**(F), inherited finite-set theorem.** For every integer $c$, the set $S_c$
is finite. This is Theorem 4.3 of
[the fifth-pass proof](../../continuation_round5/arithmetic_frontier/PROOF_PACKAGE.md),
deduced there from Ji–Xie–Zhang, *Cyclotomic integral points for affine
dynamics*, [arXiv:2511.13443v2, Theorem 1.8](https://arxiv.org/html/2511.13443v2),
and the classical absence of periodic affine curves for plane Hénon maps.
The inspected v2 is dated 20 January 2026 and is a preprint. It is an
external theorem dependency, not a new result of this package. Its
Hénon-type hypothesis applies to $F_c$: the map and polynomial inverse have
distinct projective indeterminacy points, and degree two.

The inherited Lemma 4.1 proves that every algebraic periodic coordinate is
integral and has house at most

$$B(c)=1+\sqrt{1+|c|}.$$

Neither inherited fact is reproved or counted as a new contract. The other
inputs are the Hilbert basis theorem (a fixed affine torus is Noetherian),
elementary integer Smith normal form, and elementary exact arithmetic in
finite cyclotomic fields. The finiteness argument for a fixed number field
is supplied below rather than hidden in an inappropriate unbounded-degree
use of Northcott.

Dependency map: (E) and the inherited house bound give a fixed torus that
represents every required orbit; (T) gives computable exact successor
pruning; Noetherianity gives termination; the fixed-field argument identifies
the surviving torsion images as precisely periodic; (F) makes each surviving
connected coset have constant image, giving a finite output list.

## 3. Fixed-length encoding, including zero

Compute the positive integer

$$H=2|c|+4,\qquad N=L(H),\qquad M=N+2.$$

We may replace $L$ by $\max(1,L)$, so $M\ge3$.
Writing $q=|c|$, we have
$B(c)^2=q+2+2\sqrt{1+q}\le2q+4=H$, because
$(q+2)^2-4(q+1)=q^2\ge0$. Thus every periodic coordinate is a sum of
$\ell\le N$ roots of unity. It can be expressed as a sum of exactly $M$
roots: the gap $M-\ell\ge2$ can be written $2a+3b$ with nonnegative
integers $a,b$ (use $b=0$ for an even gap and $b=1$ for an odd gap).
Append $a$ copies of $1+(-1)=0$ and $b$ copies of
$1+\omega+\omega^2=0$, with $\omega$ a primitive cube root of unity.
This also encodes zero starting with the empty sum; no torus coordinate is
set equal to zero.

Set $T=\mathbb G_m^{2M}$ and define the morphism

$$\phi:T\longrightarrow\mathbb A^2,\qquad
\phi(u)=\left(\sum_{i=1}^{M}u_i,\sum_{i=M+1}^{2M}u_i\right).$$

Every $P\in S_c$ has a torsion representative, as does every iterate of
$P$. Conversely, every coordinate of $\phi(u)$ for $u\in T_{\rm tor}$
is a cyclotomic algebraic integer of house at most $M$. Indeed, any
embedding of its coordinate field into $\mathbb C$ extends to an embedding
of a finite cyclotomic field containing all the $u_i$, and sends those
roots of unity to roots of unity. The triangle inequality then gives $M$.
This converse bound holds for all torsion representatives, regardless of
their conductors or the degree of their fields.

## 4. Exact successor operation on finite torsion-coset unions

For a closed Laurent algebraic set $W\subseteq\mathbb G_m^d$ define

$$\operatorname{TC}(W)=\overline{W\cap\mu_\infty^d}^{\rm Zar}.$$

It is important that $W$ is closed. Consequently

$$\operatorname{TC}(W)\subseteq W,\qquad
\operatorname{TC}(W)\cap\mu_\infty^d=W\cap\mu_\infty^d.\tag{4.1}$$

The first inclusion follows because the closure of a subset of a closed
set remains inside it. One inclusion in the equality follows from this;
the other follows because every torsion solution belongs to its own
closure. Statement (T) computes this closed set as a finite union of
connected torsion cosets, not as a closure oracle with no implementation.

For a finite union $V\subseteq T$ of connected torsion cosets, form

$$W(V)=\{(u,v)\in V\times V:F_c(\phi(u))=\phi(v)\}\subseteq T\times T,$$

and put

$$\mathcal P(V)=\pi_1\operatorname{TC}(W(V)).\tag{4.2}$$

All equations are Laurent equations over an explicitly known finite
cyclotomic field. A finite union can be handled by considering every pair
of component cosets and taking the union of the resulting torsion closures;
closure commutes with finite unions. Thus one never needs to input a
logical existential formula to an unprovided oracle.

For a connected torsion coset $C\subseteq T\times T$, its coordinate
projection $\pi_1(C)$ is a connected torsion coset and is closed. Moreover,

$$\pi_1(C\cap(T\times T)_{\rm tor})
=\pi_1(C)\cap T_{\rm tor}.\tag{4.3}$$

Here is why torsion lifting is stronger than merely closed projection.
Write $C=\tau H$ and choose an isomorphism
$\psi:\mathbb G_m^r\to H$ with integer monomial coordinates. The
homomorphism $\pi_1\psi$ is specified by an integer matrix. To lift a
torsion point of $\pi_1(C)$, divide by $\pi_1(\tau)$ and solve this
monomial system. Smith normal form gives equations $z_i^{d_i}=\eta_i$
with $\eta_i$ roots of unity and redundant equations already satisfied by
membership in the image. Choose roots of unity solving each nonzero-power
equation and set free parameters to $1$. The resulting lift is torsion.
The reverse inclusion follows because monomial maps preserve torsion.
For $r=0$ the statement is the assertion about the single point $\tau$.

It follows from (4.1), (4.3), and finiteness of the coset union that

$$\mathcal P(V)\cap T_{\rm tor}
=\{u\in V\cap T_{\rm tor}:\exists v\in V\cap T_{\rm tor},
\ F_c(\phi(u))=\phi(v)\}.\tag{4.4}$$

Also $\mathcal P(V)\subseteq V$ as closed algebraic sets: by (4.1) the
projected set is the projection of a subset of $W(V)\subseteq V\times V$.
Thus neither torsion closure nor projection introduces a false torsion
successor. The output is again a closed finite union of torsion cosets.

**Fixed-correspondence reduction, supplied during non-author review.**
One does not need to recompute a torsion closure on every iteration. Form
once the known closed relation

$$R=\{(u,v)\in T^2:F_c(\phi(u))=\phi(v)\},\qquad
\Gamma=\operatorname{TC}(R).$$

For any finite torsion-coset union $V$, the intersection
$A=\Gamma\cap(V\times V)$ is a finite torsion-coset union by (T),
is contained in $W(V)$, and has exactly $W(V)$'s torsion points by
(4.1). Torsion is dense in every component of $A$, so

$$\operatorname{TC}(W(V))=\Gamma\cap(V\times V),\qquad
\mathcal P(V)=\pi_1\bigl(\Gamma\cap(V\times V)\bigr).\tag{4.5}$$

Use (4.5) for the implementation below. It is exactly equivalent to the
frozen successor operation, not a weakened question. The simplification
also removes repeated torsion-closure computation as a proposed increment.

## 5. Descent and an effective stopping test

Start with $V_0=T$ and compute recursively $V_{j+1}=\mathcal P(V_j)$.
By Step 4 this is a descending chain of closed subsets of the *fixed*
torus $T$:

$$T=V_0\supseteq V_1\supseteq V_2\supseteq\cdots.$$

The coordinate ring $\overline{\mathbb Q}[u_1^{\pm1},\ldots,u_{2M}^{\pm1}]$
is Noetherian, being a localization of a polynomial ring over a field.
Its ideals of vanishing functions on these sets form an ascending chain,
so for some finite $j$ the closed sets satisfy $V_{j+1}=V_j$.
Changing the finite cyclotomic coefficient field in intermediate steps
does not change the ambient torus over $\overline{\mathbb Q}$ or this
Noetherian argument. We are not applying Noetherianity to arbitrary
constructible sets or to a chain in growing dimension.

Equality is an exact effective test. To make its use transparent, reduce
the two lists to connected cosets. A connected coset $C$ is contained in
a finite union $\bigcup D_i$ if and only if it is contained in one $D_i$:
the intersections $C\cap D_i$ are closed in the irreducible variety $C$,
and irreducibility excludes a cover by finitely many proper closed sets.
Coset containment is decided by the character equations of $D_i$:
substitution of a monomial parametrization of $C$ makes each equation
identically true exactly when its parameter exponent is zero and its
torsion constant is the required root of unity. Test containment in both
directions for the two finite lists. Empty lists and point cosets are
included. All roots of unity can be compared in a common finite cyclotomic
field using exact polynomial arithmetic.

Stop at the first equality and denote that set by $V_*$.
This is a computable procedure with a proof that it halts. No explicit
upper bound on the number of iterations, practical complexity estimate,
or claim that the iteration has been executed is made. Equal successive
sets are a fixed point because $\mathcal P$ is a deterministic operation
on algebraic sets.

## 6. Identification of the surviving torsion images

We prove the exact equality

$$\phi(V_*\cap T_{\rm tor})=S_c.\tag{6.1}$$

First fix $P\in S_c$. We show by induction on $j$ that *every* torsion
representative of *every* point of its finite orbit belongs to $V_j$.
For $j=0$ this is the definition of $T$. At the inductive step let $u$
represent an orbit point $Q$. The next orbit point $F_c(Q)$ has a torsion
representative $v$ by Step 3. Both $u$ and $v$ lie in $V_j$ by the
induction hypothesis. Identity (4.4) puts $u$ in $V_{j+1}$. Thus at
stabilization $P$ has a representative in $V_*$.

For the reverse inclusion let $u_0\in V_*\cap T_{\rm tor}$ and
$P=\phi(u_0)$. Since $\mathcal P(V_*)=V_*$, (4.4) supplies a torsion
successor in $V_*$ to every such representative. Repeatedly applying this
fact shows for every $n\ge0$ that $F_c^n(P)$ has a torsion representative
in $V_*$. Only existence for each finite $n$ is needed; no computable
choice of an infinite sequence is an extra hypothesis. Step 3 shows that
both coordinates of all these iterates are algebraic integers of house
at most $M$.

Now set $K=\mathbb Q(P_x,P_y)$ and $d=[K:\mathbb Q]$. This is one fixed
finite number field. Because $F_c$ has rational coefficients, every
forward iterate belongs to $K^2$, even though different torsion
representatives might live in arbitrarily large cyclotomic fields.

There are only finitely many algebraic integers in $K$ with house at most
$M$. Indeed, their monic minimal polynomials have degree $e\le d$ and
integer coefficients. The coefficient of degree $e-k$ is an elementary
symmetric sum of $e$ roots of modulus at most $M$, so its absolute value is
at most $\binom{e}{k}M^k$. For each $e\le d$ this leaves finitely many
integer coefficient tuples and hence finitely many roots. It follows that
the forward orbit of $P$ is finite. There exist $0\le i<j$ with
$F_c^i(P)=F_c^j(P)$. The polynomial inverse

$$F_c^{-1}(x,y)=(x^2+c-y,x)$$

allows cancellation of $F_c^i$, giving $P=F_c^{j-i}(P)$. Hence $P$ is
periodic, not merely preperiodic, and (6.1) follows.

This argument uses fixed-field bounded degree only after the deterministic
orbit starts from $P$. It does not incorrectly assert that bounded house
alone makes all cyclotomic integers finite.

## 7. Extraction of all points and least periods

Statement (T) gives $V_*$ as a finite union of connected torsion cosets
$C_1,\ldots,C_s$, with an explicit torsion basepoint $\tau_i\in C_i$.
Torsion points are Zariski-dense in each $C_i$. For completeness, density
on $\mathbb G_m^r$ follows by induction on $r$: a Laurent polynomial
vanishing on all torsion tuples, viewed as a polynomial in its last
variable after clearing powers, has infinitely many last-variable roots
for every fixed torsion tuple of the first $r-1$ variables. All coefficient
Laurent polynomials therefore vanish on those tuples; induction makes
them zero. Monomial isomorphisms and torsion translations preserve this
density. Dimension zero is immediate.

By (6.1), $\phi(C_i\cap T_{\rm tor})\subseteq S_c$. Input (F) makes
$S_c$ a finite closed set in $\mathbb A^2$. The preimage
$\phi^{-1}(S_c)\cap C_i$ is closed and contains a dense subset of $C_i$,
so $\phi(C_i)\subseteq S_c$. Since $C_i$ is irreducible, its image cannot
contain two distinct points of a finite set: preimages of individual
points would otherwise cover it by finitely many proper closed sets.
Thus $\phi$ is constant on $C_i$ and equals $P_i=\phi(\tau_i)$ there.
Equation (6.1) now gives

$$S_c=\{P_i:1\le i\le s\}.$$

Evaluate these sums exactly in a finite cyclotomic field containing the
basepoints and remove duplicates. As an optional internal certificate,
substitute each monomial parametrization into $\phi$ and collect Laurent
monomials: all nonconstant coefficients must vanish, and the constant
term is $P_i$. This identity test is effective; its success follows from
the proof and is not being substituted for the finite-set theorem.

For each distinct point $P_i$, iterate $F_c$ in its finite coefficient
field until its first return to $P_i$. Step 6 proves that the return
occurs. The first positive return is its least native period by
definition. Alternatively, the exact list is closed under $F_c$ and the
map is injective, so compute its permutation on the list and read the
cycle lengths; this simultaneously obtains all periods with a finite
number of comparisons. No iterate quotient or altered time clock is used.
The empty-union case returns an empty list; the algorithm does not rely
on a presupposed nonempty periodic set. Zero coordinate sums are retained.

## 8. Explicit algorithm with supplied (E) and (T)

Input: an integer $c$.

1. Compute $H=2|c|+4$, $N=L(H)$, $M=N+2$, $T$ and $\phi$.
2. Apply (T) once to the two graph equations
   $F_c(\phi(u))=\phi(v)$ on $T^2$, obtaining the fixed finite
   torsion-coset union $\Gamma$. Set the list for $V$ to the single coset $T$.
3. Intersect every coset of $\Gamma$ with every ordered pair of cosets
   in $V$, using binomial equations and Smith normal form. Project all
   resulting connected torsion cosets to the first coordinate block.
   Take their union to obtain a new coset list $V'$.
4. Decide whether $V'=V$ by exact connected-coset containment tests. If
   unequal, replace $V$ by $V'$ and return to step 3. If equal, proceed.
5. Compute one torsion basepoint of each coset, evaluate $\phi$, and
   deduplicate. Optionally verify the Laurent constancy identities.
6. Compute the permutation of this exact finite point list induced by
   $F_c$, and output the points with their permutation-cycle lengths.

Each step is finite, step 4 eventually detects equality, and the output
has exactly the required meaning by Steps 6 and 7. With the complete (E)
and (T) proofs linked above, the original all-$c$ contract is proved without
weakening its domain or its output. The mathematical result remains
dependent on external input (F). $\square$

## 9. Ownership boundary and open risks

The Loxton-style representation, rational Mann torsion relations, torus
cosets, and cyclotomic non-density are classical/external inputs. JXZ v2
already builds torus lifts and torsion correspondences from the unknown
invariant point set (especially §1.4 and §3). More strongly, §3 Step 3
explicitly iterates images under a fixed torsion correspondence in a
decreasing torsion-coset sequence and applies Noetherianity to stabilize it.
Thus neither torsion-correspondence descent nor its stabilization can be
claimed as an added mechanism. KKPR already supplies an explicit general
torsion-closure algorithm, with termination and an implementation report.

The precise residual is the effective combination starting from the
known whole torus, preserving all torsion representatives without dropping
exceptional periodic points, and using a fixed-point equality test plus
fixed-number-field bounded-house finiteness and finite point extraction
to return the complete list. Equation (4.5) further reduces this to fixed-correspondence predecessor
pruning. Whether this natural effective-corollary synthesis has enough
independent substance for a paper remains an admission question; correct
completion of the original effective question does not settle that question.

Pending at this revision: final non-author review of the combined theorem
and closest-source/increment adjudication. The first draft's unprovided
(E)/(T) risks have been closed by the actual complete proof artifacts, not
by assuming those risks away. No running
implementation, numerical examples, runtime estimate, new paper, formal
evaluation, A2 promotion, target Euler factors, or root-number identification
is asserted. `NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.
