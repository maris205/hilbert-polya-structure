# D2: Frobenius ownership of native Fricke cycles

## Frozen question and decisive boundary

Frozen before the full proof and any mathematical execution, 2026-09-09 UTC.
The exploratory quadratic-Hénon period-one witness is not retained as a
second question. The retained concrete family is the ordered Fricke return
on the Cayley member, for every odd prime power $q$:

$$
X:x^2+y^2+z^2-xyz=4,\qquad T=s_zs_ys_x,
$$

where $s_x(x,y,z)=(yz-x,y,z)$ and the other two maps exchange their
respective coordinates by the Vieta rule. Composition is rightmost first.
One whole $T$ is the native tick. Arithmetic Frobenius is
$\Phi_q(x,y,z)=(x^q,y^q,z^q)$; its extension exponent $r$ is separate
from the native iterate $n$ and from varying the rational characteristic
prime $p$. All geometric points and cycles below are ordinary/reduced.

**Single question.** Can one finite extension $\mathbb F_{q^r}$ make
arithmetic Frobenius compatible with *every* geometric primitive native
cycle without merging primitive owners? The weakest required compatibility
is $\Phi_q^r(O)=O$ for each primitive $T$-cycle $O$; only then can
Frobenius act as a rotation $T^{a(O)}$ on that cycle. A one-to-one ownership
by arithmetic closed points additionally requires that rotation to be
transitive. Equivariant relabelling may not merge distinct $T$-cycles or
replace $T$ by Frobenius as the clock.

Success requires a proof with the quantifiers $\exists r\ \forall O$,
actual descent/equivariance, and the primitive transitivity check. A
decisive counterexample is an explicit smooth primitive-cycle family for
which the Frobenius packet degree is unbounded, despite a common native
map and characteristic. A fixed-period Hasse–Weil determinant or mixed
Hénon count does not answer this question.

## Source subtraction fixed at entry

- C12 already proves fixed-native-period finite Frobenius rationality,
  nilpotent blindness, and loss of joint-action information in rectangular
  counts. Its derivation package and README were read; no such result is
  claimed anew.
- C401 already owns the generalized-Hénon mixed fixed-point count, as
  recorded in `continuation_c414_c418_round2/frobenius_clocks/SCOUT_REPORT.md`.
- PC424-L and round-four positive-characteristic proofs concern polynomial
  transfer regularity and the exact characteristic-$p$ local-length trace
  blindness. Neither descent from ordinary cycle sums nor jet recovery is
  supplied by this D2 question.
- The Cayley torus quotient and Markoff monomial action are classical.
  Cerbu–Gunther–Magee–Peilen, §3.3/Lemma 3.3 of the served arXiv v2,
  and Cantat–Loray, §2.1, are the closest primary-source checks. The
  initial §2.3 locator belonged to another version; the actual read
  locator is §3.3. Their native finite-field theory is subtracted.
- C425 owns the all-integer-coefficient, all-integer-point ordered Fricke
  classification. The present geometric finite-field domain is different,
  but using the same word does not by itself create a new paper.

## Bounded analytic test

Use the canonical torus quotient
$\pi(u,v)=(u+u^{-1},v+v^{-1},uv+(uv)^{-1})$ and derive the exact lift
$M$ of $T$. On $P_N=\pi(\zeta_N,1)$, for odd $N$ prime to $p$,
test whether $\Phi_q^r(P_N)=T^s(P_N)$ forces a scalar matrix congruence
and a determinant obstruction. Retain all quotient signs and least-period
conditions. This is a hand-proof test; no new or old mathematical program,
build, PDF, formal evaluation, external model upload or Git write is used.

## Outcome

**The positive bridge is refuted by a uniform infinite-family mechanism.**
The full hand proof is [Theorem D2](PROOF_PACKAGE.md). No mathematical
execution was required. This is source-level clock separation, not target
arithmetic progress or an automatic new-paper admission.

The native lift is
$M=\left(\begin{smallmatrix}-1&-2\\-2&-3\end{smallmatrix}\right)$.
For every odd $N\ge3$ prime to $p$, let
$P_N=\pi(\zeta_N,1)$ and let $O_N$ be its native primitive cycle.
All these cycles are smooth, despite the surface's four nodes. Their
least native periods satisfy

$$
n_N=\min\{n\ge1:M^n\equiv\pm I\pmod N\}>2.
$$

Since $v=(1,0)^t$ and $Mv$ form a basis modulo odd $N$, the exact bridge is

$$
\Phi_q^r(P_N)=T^s(P_N)
\iff M^s\equiv\pm q^rI\pmod N.
$$

Taking determinants forces $q^{2r}\equiv(-1)^s\pmod N$. This yields
two distinct obstructions, not a conflation of the clocks:

1. **Uniform descent fails.** The minimal degree $f_N$ over which the
   *cycle* becomes stable satisfies
   $f_N\ge\log(N+1)/(4\log q)$. For any proposed common extension
   exponent $r$, every admissible $N>q^{4r}-1$ provides a counterexample.
2. **Primitive ownership fails even after individual descent.** If
   $\Phi_q^r$ stabilizes $O_N$, it has order at most two on that cycle.
   Since $n_N>2$, it cannot act transitively. No extension, even
   selected separately for that cycle, makes it a single closed point.

The packet bookkeeping is explicit. If
$\Phi_q^{f_N}P_N=T^{s_N}P_N$, then
$a_N=f_Nn_N/\gcd(n_N,s_N)$ is the point's arithmetic degree.
There are $f_N$ distinct native cycles and $\gcd(n_N,s_N)$ arithmetic
closed points in the packet. Here $s_N$ is zero or the half-turn, so
$a_N$ is $f_N$ or $2f_N$. These are proved ordinary finite-set
statements, not scheme lengths, trace eigenvalues, or assigned weights.

## Positive control from the existing Fricke line package

The coordinator/X1 supplied this candidate interface; D2 checked it
directly against C425's [affine return](../../../research_c424_c428/papers/C425_fricke_return/sections/05_line_exhaustion.tex)
and [quadratic invariant](../../../research_c424_c428/papers/C425_fricke_return/sections/07_level_counts.tex)
proof passages. The links are repository-relative source pointers;
the source files were not modified.

Suppose a retained reflection cycle supplies an injective affine line
$P(t)$ defined over $\mathbb F_q$, an actual native iterate $j$, and
polynomial identities

$$
T^jP(t)=P(-t+\beta),\qquad K(P(t))=t^2-bt+c.
$$

These hypotheses require the line identity to survive reduction; they
do not follow merely from a finite-field cycle census. Invariance of
$K$ gives $Q(-t+\beta)=Q(t)$, with $Q=t^2-bt+c$. Comparing the
linear coefficients gives $2\beta=2b$, hence $\beta=b$ for odd $q$.
On a nonsplit quadratic level $Q(t)=D$, arithmetic Frobenius swaps
the two roots and therefore satisfies

$$
\Phi_qP(t)=P(b-t)=T^jP(t).
$$

If the point has native least period $h$, its distinct conjugate gives
$h\nmid j$ while $h\mid2j$; consequently $h$ is even and
$j\equiv h/2\pmod h$. This is a genuine, derived native half-turn,
but is transitive on the whole cycle only when $h=2$.

The control is non-vacuous: with $A=B=C=0$, the line $P(t)=(t,0,0)$
satisfies $T(P(t))=P(-t)$ and $K(P(t))=t^2$. Every nonsquare
$D\in\mathbb F_q^\times$ supplies one exact native two-cycle which
is one arithmetic degree-two closed point. These are different levels
from Cayley $D=4$, and they do not invalidate Theorem D2. They also
show why the conclusion must not be advertised as a no-go for every
Fricke arithmetic/dynamical compatibility. No second contract is counted.

## Primary-source check and actual access

Only bounded primary-source browsing was used; root `papers/` belongs
to another stream. Relevant local theorem/source text was read instead
of reopening PDFs. No local PDF read/preflight, bibliographic resolver,
external model, or worldwide-novelty certification is claimed.

| Source | Actual inspected scope | Ownership and applicability |
| --- | --- | --- |
| Cerbu, Gunther, Magee, Peilen, *The cycle structure of a Markoff automorphism over finite fields*, J. Number Theory 211 (2020), 1–27; [arXiv paper](https://arxiv.org/pdf/1610.07077) | Served v2 title/introduction/Theorem 1.5; §3.2 setup, §3.3 torus presentation and Lemma 3.3 with its proof; adjacent Proposition 3.5 statement. HTML fetch failed; PDF extraction succeeded. | Owns the integral monomial/trace-coordinate method and equivariance, and a native long-cycle lower bound as the characteristic prime varies. The determinant obstruction here instead fixes $q$ and varies geometric torsion order. That distinction is not a claim of global priority. |
| Cantat, Loray, *Holomorphic dynamics, Painlevé VI equation and character varieties*, [author preprint](https://arxiv.org/pdf/0711.1579) | §2.1 quotient formula, inversion involution, node discussion, and adjoining monomial action. | Classical quotient is fully subtracted. Its equation has $+xyz$; negating all three trace coordinates converts to our $-xyz$ convention. The finite-field identity is proved directly rather than inferred from a complex-analytic theorem. |
| Robin Zhang, *A Galois–dynamics correspondence for unicritical polynomials*, Arnold Math. J. 7 (2021), 467–481; [v5](https://arxiv.org/pdf/1610.00807) | Official abstract/metadata and introductory Definition 1.1 with the opening counterexample discussion. | Galois/native compatibility is an established question, and a nontrivial Galois element acting by an iterate is weaker than the transitive primitive ownership tested here. No unicritical or irreducibility theorem is transferred to Fricke surfaces. |

The relevant C424–C428 `EVALUATION_SCOPE.md` and
`EVALUATION_REFERENCE_ROUTING.md` were also read. They explicitly retain
the missing all-rational-prime owner/time/weight map, target
`NOT_TESTABLE` metrics, and incomplete controls. D2 does not perform a
new formal evaluation, reread the six historical PDFs, or inherit a
target verdict from finite-field arithmetic.

## Reusable interfaces and remaining boundaries

**To C4/D1 and future torus-factor proposals.** The transferable input
is a rank-two monomial lift $A\in\mathrm{GL}_2(\mathbb Z)$, a
simultaneous-inversion quotient, and a torsion vector $v$ for which
$\det[v,Av]$ is invertible modulo $N$. A pointwise Frobenius/native
relation then forces $A^s=\pm q^rI$ and
$q^{2r}=\det(A)^s$. The cyclic-vector condition must be checked; it
does not hold for every torsion vector or arbitrary Fricke parameter.

**To X1/X2.** An equivariant bijective recoding preserving both actions
and primitive cycles cannot change packet degrees or rotation orders.
Base extension is already covered. A semiconjugacy merging cycles or
changing the descent datum with a native-time twist is not covered and
cannot inherit this no-go without a new argument.

**To PC424-L/A1/A2.** No polynomial transfer, ordinary-cycle-to-cover
construction, wild multiplicity bound, or Frobenius trace repair is
proved here. The earlier all-degree polynomial-coboundary question
remains separate and unresolved by D2.

The frozen bridge itself has no remaining proof lemma. Remaining
research would need a materially different arithmetic carrier or a
proved mechanism selecting an appropriate subset while preserving its
intended owners; it is not licensed to identify $r$ with native time
or $N$ with rational-prime labels. The reflection control identifies
one restricted compatibility that survives, not the missing full bridge.

## Disposition and verification

Recommended disposition: **complete auxiliary obstruction / not automatic
paper admission**. The all-$q$, all-admissible-$N$ argument is stronger
than an isolated counterexample, but its mechanism is an elementary
consequence of a classical torus linearization. Independent paper-level
substance is for the coordinator and nonauthor source review to decide.

The proof-writer skill enforced a literal theorem/quantifier boundary and
a complete proof supplement; research-lit and the batch workflow caused
the local-source subtraction and primary-source applicability checks.
The broad idea-creator pilot/MCP examples were not used to enlarge the
single-question hand-proof contract. Actual mathematical executions: **0**.
No code, build, PDF, old certification, formal evaluator, config, shared
index, Git object, or earlier batch was written. The coordinator has
been sent the exact interface and the ready proof for nonauthor review;
no review outcome is asserted here.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains in force. Rational characteristic
primes, extension degrees, torsion orders, and native periods stay
distinct; no target coefficients, Euler factors, root numbers,
automorphy, zero/divisor map, or Hilbert–Pólya realization follows.
