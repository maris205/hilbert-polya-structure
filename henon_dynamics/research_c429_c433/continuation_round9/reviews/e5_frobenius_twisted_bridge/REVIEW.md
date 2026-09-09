# R9 full nonauthor review: Frobenius-twisted transfers

2026-09-10 UTC. Reviewer: E5. Current-team internal mathematical review.
This is not a new theorem admission, external peer review, or MS6 closure.

## 1. Reviewed version, original question, and verdict

The whole actual author proof was read, not only its summary:

- `continuation_round9/a2_frobenius_twisted_bridge/REPORT.md`;
- 421 lines;
- SHA256: `feb532fd56b8180b52bf45991bff1c8edebbabdef743317619ac53fe0b475052`.

The original question retains every prime $p$, integer $d\ge2$,
$c\in k=\overline{\mathbf F}_p$, and $g\in k(x)^\times$.
With $f=x^d+c$ and $\delta h=h\circ f/h$, (CP) asserts goodness
of all but finitely many ordinary primitive native cycles, with the
finite zero/pole exceptions retained. The unresolved implication is
that (CP) makes $[g]\in k(x)^\times/\delta k(x)^\times$ torsion.
The accepted R6 saturation theorem would then supply
$g^{p^e}=\delta h$ for some fixed $e$ and rational $h$.

**Auxiliary verdict: PROVABLE AS STATED.** The reduced-incidence
counts, exact orbit/norm identities, finite interpolation, uniform-bound
equivalence, rational interpolation lower bound, fixed algebraic curve,
omitted-cycle example, and transcendental-solution caution all pass.
There are **zero unresolved mathematical or source-applicability
must-fixes** in the frozen author report. No author repair was requested.

**Original MS6 and the proposed (CP)-to-(UB) implication:
NOT CURRENTLY JUSTIFIED.** The report correctly leaves both open.
The unsaturated bound is refuted; the correctly saturated bound is
neither proved nor refuted here. No fifth contract or general no-go is
inferred from this auxiliary result.

## 2. Assumptions, quantifier order, and dependency map

For a fixed input $(p,d,c,g)$ satisfying (CP), the proposed (UB)
requires one exponent $e\ge0$, one rational-degree bound $B_0$,
one finite coefficient field $\mathbf F_Q$, and one finite forward-
$f$-stable discarded set $T$, all fixed before the unbounded choices
$q=Q^r>d$. These choices may depend on the fixed input. The report
does not assert a single exponent or bound uniform over all inputs.

For arbitrarily large such $q$, (UB) asks for
$h_q\in\mathbf F_q(x)^\times$ of rational degree at most $B_0$,
regular and nonzero on $G_q=S_q\setminus T$, with

$$S_q=\{a:f(a)=a^q\},\qquad
h_q(f(a))=g(a)^{p^e}h_q(a)\quad(a\in G_q).$$

Rational degree means the maximum degree of a coprime numerator and
denominator; nonzero constants have degree zero.

The dependency chain checked here is:

1. Finite coefficient/exception data give a fixed finite $T$ and field.
2. Reduced root counting proves $|G_q|\to\infty$ in every degree.
3. On this actual incidence, native cycles are Frobenius cycles.
4. (CP) gives finite-field norm one, hence nonzero finite interpolants.
5. A fixed exponent and degree bound allow a polynomial identity test.
6. The old R6 example tests the unsaturated bound, not the saturated one.

Step 4 does not imply the hypothesis of Step 5. The report explicitly
retains that missing implication instead of substituting a weaker
question about a separate interpolant at each $q$.

## 3. Finite exceptions and the reduced incidence in every degree

The construction of $T$ is valid over $\overline{\mathbf F}_p$.
The finite zeros and poles of $g$, and all points in the finitely many
exceptional affine cycles from (CP), lie in one finite field together
with the coefficients of $f,g$. That finite field is preserved by $f$.
Their forward orbits therefore have finite union. Taking that union
gives a finite forward-stable $T$; a coefficient field can be chosen
to contain every point of $T$ as well. No finiteness of backward
orbits is required. Infinity, if included in the convention, is one
additional fixed cycle and does not affect the affine argument.

Write $d=\eta s$, where $\eta=p^{v_p(d)}$ and $p\nmid s$.
For $q=Q^r>d$, both $q$ and $\eta$ are powers of $p$, and
$q>d\ge\eta$ forces $q/\eta$ to be a positive power of $p$.
In particular it is an integer divisible by $p$, and $q/\eta>s$.
Perfectness of $\mathbf F_q$ supplies $c^{1/\eta}\in\mathbf F_q$.
Thus

$$X^q-X^d-c=
\left(X^{q/\eta}-X^s-c^{1/\eta}\right)^\eta.$$

The derivative of the inner polynomial is $-sX^{s-1}$.
For $c\ne0$, its only possible multiple root, zero, is not a root;
when $s=1$, the derivative is already a nonzero constant. Hence
there are exactly $q/\eta$ distinct roots in that case.

For $c=0$, the inner polynomial is

$$X^s(X^{q/\eta-s}-1).$$

The integer $q/\eta-s$ is positive and prime to $p$. Its nonzero
roots are simple; zero has inner multiplicity $s$. The distinct count
is therefore $q/\eta-s+1$. In the original polynomial the nonzero
roots have multiplicity $\eta$ and zero has multiplicity $\eta s=d$.
Those multiplicities are not counted as additional sample points.

Consequently the exact counts and the lower bound are

$$|S_q|=\begin{cases}q/\eta,&c\ne0,\\q/\eta-s+1,&c=0,
\end{cases}\qquad
|G_q|\ge q/\eta-s+1-|T|\longrightarrow\infty.$$

This includes $p=2$, separable degrees $\eta=1$, and pure
Frobenius degrees $s=1$. In the last case both formulas give
$q/\eta$. No use of the raw degree $q$ as an ordinary point count
survives in the proof. Empty small incidences cause no problem:
the interpolation is stated for nonempty $G_q$, and all sufficiently
large $q$ have nonempty $G_q$ by this lower bound.

## 4. Exact native/Frobenius periods and the norm identity

Because the coefficients of $f$ lie in $\mathbf F_q$,
$f(a^q)=f(a)^q$. If $a\in S_q$, induction gives

$$f^{\circ j}(a)=a^{q^j}\quad(j\ge0).$$

Every element of $k$ lies in a finite extension of $\mathbf F_q$.
The least positive $n$ with $a^{q^n}=a$ is therefore both its
native least period and $[\mathbf F_q(a):\mathbf F_q]$.
This is an equality on $S_q$, not on arbitrary periodic points.

The set $S_q$ is stable under Frobenius, and the latter is a
permutation of this finite set. Its restriction equals $f$, so $f$
also permutes $S_q$. A finite forward-stable subset of a permutation
set is a union of whole cycles; hence $T\cap S_q$ and its complement
$G_q$ are unions of full native cycles. Every retained cycle is good
under (CP) and avoids every finite zero or pole of $g$.

After choosing the base field to contain all coordinates in $T$, any
point $a\in T$ satisfies $a^q=a$. If it also lies in $S_q$, then
$f(a)=a$. Thus the observation that nonfixed exceptional cycles do
not occur in these incidences is correct. Fixed exceptions are removed.

For an $n$-cycle in $G_q$, the chosen point has
$\mathbf F_q(a)=\mathbf F_{q^n}$. Coefficient invariance of $g$ gives

$$N_{\mathbf F_{q^n}/\mathbf F_q}(g(a))
=\prod_{j=0}^{n-1}g(a)^{q^j}
=\prod_{j=0}^{n-1}g(f^{\circ j}(a))=1.$$

This uses exactly $n$ distinct orbit points. It works when $p\mid n$:
there is no averaging by $n$, replacement by a prime-to-$p$ period,
or scheme-multiplicity weight.

## 5. Finite Hilbert--90 and descent of the interpolating polynomial

In the cyclic group $\mathbf F_{q^n}^\times$, the map
$b\mapsto b^{q-1}$ has image of size $(q^n-1)/(q-1)$.
The norm kernel has the same size and contains that image. Thus
norm one gives a nonzero $b\in\mathbf F_{q^n}$ such that
$b^q=g(a)b$. This elementary group argument proves the exact
Hilbert--90 fact needed here, including $n=1$ and $p\mid n$.

Assign $b^{q^j}$ to the point $a^{q^j}=f^{\circ j}(a)$ of the cycle.
The values are consistent at closure since $b^{q^n}=b$. At phase
$j$ the relation follows by applying $q^j$-Frobenius to
$b^q=g(a)b$. Carrying this out on each disjoint cycle gives nonzero
values $v_q$ with

$$v_q(a^q)=v_q(a)^q=g(a)v_q(a).$$

For $s_q=|G_q|>0$, ordinary interpolation at distinct points gives
one polynomial $H_q\in k[x]$ of degree less than $s_q$ with these
values. It is nonzero and has no zero on $G_q$.
To check coefficient descent explicitly, let $H_q^{[q]}$ be obtained
by raising its coefficients to the $q$th power. At each $a\in G_q$,

$$H_q^{[q]}(a^q)=H_q(a)^q=v_q(a)^q=v_q(a^q)=H_q(a^q).$$

Both polynomials have degree below $s_q$, and the points $a^q$
permute $G_q$. Uniqueness therefore gives $H_q^{[q]}=H_q$, so
$H_q\in\mathbf F_q[x]$. Since $f$ preserves $G_q$, it satisfies
$H_q(f(a))=g(a)H_q(a)$ throughout the asserted domain.

For each fixed $e$, replacing $g$ by $g^{p^e}$ preserves the good
products and repeats this construction with the same bound
$\deg H_q<s_q$. It does not turn that bound into one independent
of $q$.

The polynomial $\prod_{a\in G_q}(x-a)$ is squarefree and lies in
$\mathbf F_q[x]$. Its quotient algebra $A_q$ is a product of finite
fields, one per Frobenius orbit, and the class of $H_q$ is a unit.
This is a valid finite reduced algebraic solution, but not a finite
extension of the rational function field. The quotient map kills a
nonzero polynomial, which would have to become invertible in
$\mathbf F_q(x)$. It cannot extend to a unital map from that field.
Base change to $k$ does not remove this obstruction.

## 6. Uniform degree if and only if a global saturated identity

Let $g=A/B$ be a coprime polynomial presentation, and put
$H(g)=\max(\deg A,\deg B)$. For fixed $P=p^e$ and a (UB)
function $h_q=U/V$ with coprime numerator and denominator of degree
at most $B_0$, form

$$J_q=B^P U(f)V-A^P U V(f).$$

At a point of $G_q$, both $g$ and $h_q$ are regular and nonzero.
The same is true of $h_q$ at its image because that image is still
in $G_q$. In coprime presentations these assertions make all relevant
numerators and denominators nonzero at those points. Thus the
pointwise relation really implies $J_q(a)=0$ without an evaluation
at a cancelled transfer zero or pole.

If $J_q$ is not zero, its degree is at most

$$P H(g)+(d+1)B_0.$$

The quantities on this line are fixed as $q$ varies. For a sufficiently
large one of the arbitrarily large permitted $q$, the distinct-root
bound for $G_q$ exceeds this number. Hence $J_q$ is zero, and the
single corresponding rational function satisfies
$g^{p^e}=h_q\circ f/h_q$ in $k(x)$.
No stabilization of coefficients, repeated choice of $h_q$, compactness,
or limiting rational function is necessary.

Conversely, given $g^{p^e}=\delta h$, the elementary telescoping
argument gives (CP) after omitting the finitely many cycles meeting
the supports of $g$ or $h$. Choose a finite field containing all
coefficients and the finitely many support points, and include their
finite forward orbits and the exceptional cycles in $T$.
These are choices made once. Then $h_q=h$ belongs to
$\mathbf F_q(x)$ and is regular and nonzero on $G_q$ for every
$q=Q^r>d$, with fixed degree $H(h)$.

This proves the stated equivalence under the frozen conventions.
Allowing a fixed arbitrary positive integer exponent in place of
$p^e$ would give torsion by the same argument; under (CP), the
accepted R6 saturation theorem then removes its prime-to-$p$ part.
Allowing the exponent, bound, or deleted set to grow with $q$ is
not the assertion proved here and would invalidate this degree test.

## 7. Old R6 example and the new denominator-inclusive lower bound

For every prime $p$, the example $f=x^{p+1}$, $g=x$ is already
proved in R6. If $a\ne0$ has native period $n$, its cycle product
has $p$th power $a^{(p+1)^n-1}=1$, and so the product is $1$.
Only the zero cycle is an affine support exception. A rational
identity $\delta h=x$ would force
$p\operatorname{ord}_0h=1$ in the integers, impossible. But
$\delta x=x^p$. These observations are correctly subtracted as old
inputs, not offered as a new MS6 counterexample.

For $q=p^r>p+1$, let $m_q=q-p-1$. This positive integer is prime
to $p$, and the nonzero incidence is exactly the distinct set
$\mu_{m_q}(k)$. The stated function

$$h_q=x^{q/p-1}$$

is regular and nonzero there, and its transfer ratio on that set is
$a^{q-p}=a^{m_q+1}=a$. The function has the asserted degree
$q/p-1$. This explicit representative need not be the unique
degree-below-$|G_q|$ interpolant from Section 5; for example the
small case $p=2,q=4$ has just one nonzero sample point. No such
minimal-degree claim is made in the author report.

Now let $T_0$ be any fixed finite deleted set and $C=|T_0|$.
For any rational $h=U/V$ of degree $b$, regular and nonzero at
the retained points and their images, the local transfer equation
implies that

$$J_h=U(x^{p+1})V(x)-xU(x)V(x^{p+1})$$

vanishes at at least $m_q-C$ distinct points. The polynomial $J_h$
is nonzero, because its vanishing identically would give the globally
impossible unsaturated identity. Its degree is at most $(p+2)b+1$.
Consequently

$$b\ge\frac{q-p-2-C}{p+2}.$$

The argument allows arbitrary coefficients in $k$ and rational
denominators, not just polynomial or monomial candidates. It applies
to every valid family after any fixed finite deletion; a negative or
zero lower bound at small $q$ does not affect the unbounded conclusion.
Every sequence $q=Q^r$ from a larger finite coefficient field is a
subsequence of the powers of $p$, so a field enlargement cannot
evade it. Thus the stronger (CP)-to-(UB) assertion with $e=0$ is
indeed false. The result is a degree-growth diagnosis, not an optimal
interpolation-degree formula.

## 8. Saturation and the fixed purely inseparable curve

For the same example, the one rational function $h=x$ works for
$g^p$, with degree one, so the correctly saturated (UB) survives.
The stated algebraic extension is also valid. Adjoin $Y$ with
$Y^p=x$. The element $x$ is not a $p$th power in $k(x)$, as seen
from its order one at zero. Thus $k(Y)/k(x)$ is purely inseparable
of degree $p$.

The substitution $Y\mapsto Y^{p+1}$ defines an injective
$k$-endomorphism of $k(Y)$. On $x=Y^p$ it induces
$x\mapsto x^{p+1}$, so it extends the required native substitution.
Moreover $Y^{p+1}=xY=gY$, giving a genuine finite forward-stable
algebraic transfer, not merely a polynomial relation.

At every nonzero incidence point,

$$h_q(a)^p=a^{q-p}=a.$$

Hence the sampled graph points of every displayed $h_q$ lie on the
single curve $Y^p=X$. This statement concerns sampled graph points,
not a rational-function identity $h_q(x)^p=x$. The explicit stable
lift proves that the fixed curve actually supplies an algebraic
transfer in this example. Unbounded unsaturated rational interpolation
degree therefore does not exclude bounded algebraic degree.

## 9. Omitted cycles and the general transcendental construction

For $p=3$ and $f=x^2$, a primitive $13^t$th root exists for every
$t\ge1$. Squaring preserves its exact order and permutes the finite
group, so the point lies on a native periodic cycle. The same holds
at every phase of that cycle.
If any phase belonged to an incidence for $q=3^r$, its exact order
would imply $3^r\equiv2\pmod{13}$. But the powers of $3$ modulo
$13$ cycle through $1,3,9$, none equal to $2$. No phase is on any
such incidence. Different $t$ give disjoint cycles because the exact
root order is preserved. This proves the asserted infinite omission,
including after any finite coefficient-field enlargement.

This example has no specified rational observable satisfying all
incidence tests. It is therefore not a counterexample to (CP), MS6,
or the implication from incidence norm tests to (CP). It only refutes
pointwise exhaustion of native cycles by these first-step incidences.
Infinite omission does not invalidate the uniform-degree identity
test, which needs only an unbounded number of distinct sample points.

For arbitrary $g\ne0$, adjoining a transcendental $Y$ and setting
$\widetilde\sigma(Y)=gY$ also gives a valid injective extension of
$\sigma$ to $k(x)(Y)$. A nonzero polynomial
$\sum_i a_iY^i$ maps to $\sum_i\sigma(a_i)g^iY^i$, which is
nonzero because substitution on $k(x)$ is injective and distinct
powers of $Y$ cannot cancel. Thus denominators remain nonzero and
the map extends to the fraction field.

This construction works with or without (CP), but the extension is
transcendental, not finite algebraic. An injective endomorphism is
enough for the forward-stable convention here; no surjectivity is
claimed. The construction and the finite quotient algebras from
Section 5 leave the R6 finite-function-field hypothesis unsupplied.

## 10. Primary-source applicability and accepted-input ownership

I directly read [Papanikolas, arXiv:math/0506078v2 (2007)](https://arxiv.org/pdf/math/0506078v2):
the introduction through the relevant methods discussion, the complete
twisting definition in Section 2.2.5, the setup in Section 4.1 and the
opening construction in 4.2.1, and Theorem 4.3.1 and Proposition 4.3.3
with their complete displayed proofs.

The concrete twist fixes $t$ and applies inverse coefficient Frobenius.
The abstract framework is broader, but requires an automorphism,
a separable ambient extension, and an existing fundamental solution
matrix. Theorem 4.3.1 relates group dimension to transcendence degree
under its relative-algebraic-closure hypothesis. Proposition 4.3.3
establishes relative algebraic closure in its specified analytic setting;
it does not establish algebraicity of the solution field. These results
do not derive a zero transcendence degree from native cycle products.
See the [original definitions and results](https://arxiv.org/pdf/math/0506078v2).

Our substitution fixes $k$ and sends $x$ to $x^d+c$; for $d>1$ it
is not surjective on $k(x)$. A preimage of $x$ would require a rational
$u$ with $u\circ f=x$, contradicting $d\deg u=1$. No compatible
reduction to the source hypotheses is supplied. Thus the author's
limited non-applicability conclusion is justified.

The Chang survey is an author-reported routing source, not an imported
theorem; I did not independently reread that survey. This review does
not certify every step of the cited paper or assert that no applicable
result exists elsewhere. Its primary check is confined to the precise
operator and hypothesis boundary above.

For accepted local ownership, I reread the full R6 M6 Section 1,
R6 saturation Sections 1--3, and the complete R6 saturation-source
audit. They confirm the old example, the conditional finite-extension
equivalence, and the distinction between existence and saturation.
The accepted R7 finite-divisor/pure-Frobenius results remain inputs,
not new R9 discoveries or reasons to reopen their full proofs.
The accepted R8 single-atom theorem is not used to infer a factorwise
condition for a product of atoms.

## 11. Corrections, open risks, and final handoff

No mathematical, quantifier, denominator, multiplicity, or source-scope
repair was required in the reviewed 421-line version. In particular,
the proof covers all primes, all unicritical degrees, $c=0$, pure
inseparability, periods divisible by $p$, rational denominators,
and every fixed finite deletion permitted in the stated lower bound.

The remaining obligation is exactly

$$(CP)\Longrightarrow\text{one fixed }e\text{ and a bound }B_0
\text{ independent of }q,$$

or, equivalently under the accepted saturation result, construction
of one finite algebraic extension with a forward-stable lift and a
nonzero transfer. Neither finite Hilbert--90 interpolation nor a
generic transcendental difference-field solution supplies this step.
The unsaturated example does not rule out every $p$-power transfer.

The proof-writer and research-review disciplines determined the split
verdict: the auxiliary claims pass, while full MS6 and (UB) stay
unjustified. The research-lit check retained the actual source's
operator and starting hypotheses. The repository workflow uses this
current-team internal review, not an external model call.

Only this allocated new review file was written. No mathematical
program, old checker, parameter census, nested agent, external model/API,
GPU job, Git operation, manuscript/PDF, or author/old/shared-file edit
was performed. Source access used direct primary-page opens and
within-document navigation; no new search-query batch or local PDF
download was performed. No relevant local paper or exposed
Zotero/Obsidian tool was found. File hashes establish provenance,
not mathematical verification.

Final verdict: **PROVABLE AS STATED for the auxiliary results;
NOT CURRENTLY JUSTIFIED for full MS6 and the missing (CP)-to-(UB)
implication. Zero unresolved mathematical/source-applicability
must-fixes in the frozen report. No admission is made.**
