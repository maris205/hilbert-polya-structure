# R9: Frobenius-twisted Hilbert--90 transfers

2026-09-10 UTC. One bounded proof-mechanism test.

## 1. Unchanged question and initial status

For every prime $p$, every integer $d\ge2$, every
$c\in k=\overline{\mathbf F}_p$, and every
$g\in k(x)^\times$, set $f(x)=x^d+c$ and
$\delta h=h\circ f/h$. Condition (CP) means that all but finitely
many ordinary primitive native $f$-cycles avoid the zeros and poles
of $g$ and have product $\prod_{a\in O}g(a)=1$.

The full MS6 existence question is whether (CP) implies that
$[g]\in k(x)^\times/\delta k(x)^\times$ is torsion. The accepted
R6 saturation theorem then gives a rational transfer for $g^{p^e}$
for some fixed $e\ge0$. Neither all primes nor any degrees or
constants are removed. This report initially classifies that missing
existence implication as **NOT CURRENTLY JUSTIFIED**.

**Final outcome: NOT CURRENTLY JUSTIFIED for full MS6.** The actual
incidence/norm identity, finite interpolation, and bounded-degree
identity test are proved below for all the parameters. The stronger
uniform rational-degree assertion without saturation is false, with
an explicit linear lower bound on every interpolant. The correctly
saturated uniform bound (UB) remains unproved. This is a bounded
route diagnosis with reusable exact interfaces, not an MS6 no-go.

## 2. Single mechanism and corrected decisive lemma, frozen first

Choose a finite field $\mathbf F_Q$ containing the coefficients of
$f,g$, and consider $q=Q^r>d$. The actual incidence is

$$S_q=\{a\in k:f(a)=a^q\}.$$

Only on this set does one native step coincide with the $q$-power
Frobenius. The proposal is to turn its finite-field Hilbert--90
transfers into one bounded-complexity rational or finite algebraic
transfer. Interpolation degree is not assumed bounded.

**Frozen repaired bridge.** If (CP) holds, do there exist a fixed
integer $e\ge0$, a fixed integer $B\ge0$, a finite field
$\mathbf F_Q$ as above, and a fixed finite forward-$f$-stable set
$T\subset k$, containing all finite zeros and poles of $g$ and every
exceptional affine cycle, such that for arbitrarily large $q=Q^r>d$ there
is a rational function $h_q\in\mathbf F_q(x)^\times$ of degree
at most $B$, regular and nonzero on $S_q\setminus T$, satisfying

$$h_q(f(a))=g(a)^{p^e}h_q(a)
\qquad(a\in S_q\setminus T)? \tag{UB}
$$

The exponent, degree bound, base field, and discarded set are fixed
before $q$ varies. The exponent must be permitted from the outset:
R6 already owns the counterexample $f=x^{p+1},g=x$ to an unsaturated
rational conclusion. This report will not relabel that example as new.
Its specific new diagnostic is the degree growth of every rational
transfer on the actual Frobenius incidence, even though (CP) holds.

An affirmative proof of (UB), or a construction of a single finite
stable algebraic difference extension instead, would settle the selected
bridge. Proving finite interpolation for each $q$ does not settle it.
An obstruction to the stronger version with $e=0$ does not refute MS6.

## 3. Proof obligations and execution boundary

1. Prove the exact native/Frobenius orbit and finite-field norm identities
   on $S_q$, keeping the finite exceptional set explicit.
2. Handle the reduced incidence for all inseparable degrees, including
   its exceptional multiple root when $c=0$.
3. Construct the actual Hilbert--90 interpolation and state its genuine
   degree bound, then prove why a uniform bound in (UB) would suffice.
4. Check the R6-owned $f=x^{p+1},g=x$ control on these incidences,
   including nonzero rational denominators and exact degree growth.
5. Attempt only the fixed-exponent boundedness/finite-algebraicity bridge;
   if it does not follow, retain that exact gap without an admission.

Only this new report is writable. R8 and all earlier author/review files
remain frozen. At most two relevant primary-source query batches are
allocated. No mathematical execution, parameter census, nested agent,
external model/API, GPU, PDF, Git, or shared/old-file edit is allocated.
This does not duplicate A1's arbitrary quadratic cyclic-coefficient
operator task or reopen a general invariant-hypersurface search.

## 4. Actual input subtraction

The complete Section 1 of the R6
[M6 scout](../../continuation_round6/x2_independent_replacement/REPORT.md)
and Sections 1--3 of the R6
[saturation proof](../../continuation_round6/a2_multiplicative_saturation/REPORT.md)
were read again. The former already owns the all-prime family
$f=x^{p+1},g=x$, its full ordinary-cycle calculation, and its failure
of an unsaturated rational transfer. The latter proves that, under
(CP), torsion, a finite stable algebraic transfer, and a $p$-power
rational transfer are equivalent; it does not prove their existence.

The complete R6
[source audit](../../continuation_round6/x2_multiplicative_saturation_sources/REPORT.md)
and the complete R7
[finite-divisor report](../../continuation_round7/a2_multiplicative_existence/REPORT.md)
were also read. The latter's finite torsion criterion and full pure-
Frobenius subtype remain proved inputs. Neither sibling Hilbert--90
nor the existence of a formal difference-field solution was an accepted
bridge to full MS6. No earlier claim is reopened or relabelled here.

The R8 critical-atom report remains byte-frozen. The coordinator and
E5 have separately reported its completed full review; this R9 task
does not edit it, count an admission, or use its one-atom conclusion
to infer a factorwise condition for a product of atoms.

## 5. The actual incidence, all degrees, and all finite exceptions

Write

$$d=\eta s,\qquad \eta=p^{v_p(d)},\qquad p\nmid s.$$

Choose $\mathbf F_Q$ containing the coefficients of $f,g$ and the
coordinates of a finite forward-$f$-stable set $T$ containing the
finite zeros/poles of $g$ and all the exceptional affine cycles.
Such a set exists under (CP): first take the finitely many listed
points and then their forward orbits. A finite field containing
these points and $c$ is preserved by $f$, so those forward orbits
remain finite. If cycles are formulated on $\mathbf P^1$, infinity
is a single additional fixed cycle and may be omitted throughout.

For $q=Q^r>d$, define $S_q$ as in Section 2 and $G_q=S_q\setminus T$.
The polynomial defining the incidence factors as

$$X^q-X^d-c=
 \left(X^{q/\eta}-X^s-c^{1/\eta}\right)^\eta. \tag{5.1}$$

The unique $\eta$th root of $c$ belongs to $\mathbf F_q$.
The inequality $q>d$ implies that $q/\eta$ is a positive power
of $p$ and exceeds $s$. Thus the derivative of the parenthesized
polynomial is $-sX^{s-1}$. If $c\ne0$, it has no multiple roots.
If $c=0$, it is

$$X^s\left(X^{q/\eta-s}-1\right),$$

where $q/\eta-s$ is prime to $p$; its nonzero roots are simple
and zero has multiplicity $s$. Consequently the number of distinct
geometric roots is exactly

$$|S_q|=
 \begin{cases}
 q/\eta,&c\ne0,\\
 q/\eta-s+1,&c=0.
 \end{cases} \tag{5.2}$$

In particular $|G_q|\ge q/\eta-s+1-|T|\longrightarrow\infty$.
The raw degree $q$ is not used as a count of ordinary sample points
when the incidence is nonreduced.

For every $a\in S_q$, the commutation of $f$ with $q$-Frobenius gives

$$f^{\circ j}(a)=a^{q^j}\qquad(j\ge0). \tag{5.3}$$

The Frobenius orbit is finite, so $a$ is genuinely periodic under $f$.
Its least native period is exactly

$$n=[\mathbf F_q(a):\mathbf F_q]. \tag{5.4}$$

Indeed both sides are the least positive integer with
$a^{q^n}=a$, by (5.3). The set $S_q$ is permuted by $f$. Since
$T\cap S_q$ is finite and forward stable under that permutation,
it is a union of full cycles. Therefore $G_q$ is also a union of
full ordinary native cycles. All these cycles are good under (CP).

The removal of finite exceptions is particularly explicit after the
chosen base-field enlargement. Every point of $T$ is fixed by
$q$-Frobenius. Such a point belongs to $S_q$ only if it is fixed
by $f$. Nonfixed exceptional cycles do not occur in this incidence
at all; the remaining fixed exceptions are discarded by $T$.

## 6. What Hilbert--90 really constructs

Let $O\subset G_q$ be one cycle, of least native period $n$, and
choose $a\in O$. Since $g\in\mathbf F_q(x)$, (5.3)--(5.4) imply

$$N_{\mathbf F_{q^n}/\mathbf F_q}(g(a))
 =\prod_{j=0}^{n-1}g(a)^{q^j}
 =\prod_{j=0}^{n-1}g(f^{\circ j}(a))=1. \tag{6.1}$$

This is an actual finite-field norm over precisely the native period,
including periods divisible by $p$. There is no replacement of the
native clock away from $S_q$.

For completeness, in the cyclic group $\mathbf F_{q^n}^{\times}$,
the image of $b\mapsto b^{q-1}$ and the kernel of the norm both
have order $(q^n-1)/(q-1)$, and the image lies in the kernel. Thus
there is $b\in\mathbf F_{q^n}^{\times}$ with

$$b^q=g(a)b. \tag{6.2}$$

This is the finite-field Hilbert--90 assertion used here. Assign to
$f^{\circ j}(a)=a^{q^j}$ the value $b^{q^j}$. The assignment is
consistent when the orbit closes because $b^{q^n}=b$. Carry this
out separately on each cycle in $G_q$.

Let $v_q(a)$ denote the assigned values. They are nonzero and satisfy

$$v_q(a^q)=v_q(a)^q=g(a)v_q(a).$$

Let $s_q=|G_q|$. For $s_q>0$, interpolation at its distinct points
gives a unique polynomial $H_q\in k[x]$ of degree less than $s_q$
with $H_q(a)=v_q(a)$. This polynomial is actually in $\mathbf F_q[x]$:
Frobenius-conjugating its coefficients gives a polynomial with the
same values at the permuted points $a^q$, hence the same polynomial
by uniqueness. It is nonzero, is nonzero at every point of $G_q$,
and satisfies

$$H_q(f(a))=g(a)H_q(a)\quad(a\in G_q),\qquad
\deg H_q<s_q. \tag{6.3}$$

For any fixed $e\ge0$ the same proof applied to $g^{p^e}$ gives
an interpolant of degree less than $s_q$. It supplies **no improvement**
to this degree bound. Since $s_q$ grows with $q$, (6.3) does not prove
(UB), even when all the coefficients are in the original finite field.

One can express the conclusion in the finite reduced algebra

$$A_q=\mathbf F_q[x]/\Bigl(\prod_{a\in G_q}(x-a)\Bigr).$$

This is a product of the finite fields attached to the distinct
Frobenius cycles. The class of $H_q$ is a unit and solves the local
equation there. However, $A_q$ is **not** a finite extension of
$k(x)$ or even of $\mathbf F_q(x)$: the map from $\mathbf F_q[x]$
has a nonzero polynomial kernel and cannot extend to its fraction
field. R6's minimal-polynomial descent for a finite function-field
extension therefore does not apply to this object.

## 7. A uniform degree bound would suffice, with no compactness shortcut

Write $g=A/B$ with coprime polynomials and set
$H(g)=\max(\deg A,\deg B)$. For a rational function its degree
means this height of a coprime presentation; a nonzero constant has
degree zero. Suppose (UB) holds, put $P=p^e$, and choose one of its
functions $h_q=U/V$, with coprime polynomials of degree at most $B_0$,
where $B_0$ is the fixed bound called $B$ in (UB).

To avoid confusing the bound with the denominator of $g$, form

$$J_q(x)=B(x)^P U(f(x))V(x)
              -A(x)^P U(x)V(f(x)). \tag{7.1}$$

Every point of $G_q$ is a zero of this polynomial. All denominators
used in this assertion are nonzero: $g$ is defined and nonzero there,
and $h_q$ is regular and nonzero at both the point and its image,
because $G_q$ is a union of cycles. Its degree satisfies

$$\deg J_q\le P H(g)+(d+1)B_0 \tag{7.2}$$

unless it is the zero polynomial. By (5.2), for a sufficiently large
one of the allowed $q$, the number of distinct zeros exceeds this
fixed bound. Hence $J_q=0$, and that single $h_q$ gives the global
rational identity

$$g^{p^e}=h_q\circ f/h_q. \tag{7.3}$$

The coefficients of $h_q$ need not stabilize across different $q$.
Root counting at one sufficiently large incidence already proves
the identity, so no unjustified compactness or repetition claim is
being used.

Conversely, if (7.3) holds for a rational $h$, enlarge the base field
to contain its coefficients, and enlarge $T$ by the finite forward
orbits of its finite zeros and poles. On the remaining incidence,
the same $h_q=h$ works for every $q=Q^r>d$, with fixed bound
$B_0=H(h)$. Thus, under the frozen conventions, (UB) is equivalent
to the desired $p$-power rational conclusion. Allowing an arbitrary
fixed positive integer power instead would give torsion by the same
root count, and R6 would then supply the $p$-power saturation.

This equivalence isolates the missing step; it does not derive (UB)
from the degree-$s_q-1$ interpolation in Section 6.

## 8. Exact degree-growth control from the R6-owned M6 example

For this section let $p$ be any prime and take the already owned
family $f=x^{p+1}$, $g=x$. A nonzero native cycle of least period
$n$ has product whose $p$th power is $a^{(p+1)^n-1}=1$, so its
product is $1$. Every admissible ordinary cycle is good. A rational
identity $\delta h=x$ would give
$p\operatorname{ord}_0(h)=1$ in the integers, which is impossible.
On the other hand $\delta x=x^p=g^p$. These facts are imported
from R6, not a new counterexample.

What follows is their exact new interface with the present incidence.
For $q=p^r>p+1$ put $m_q=q-p-1$, which is prime to $p$. Then

$$X^q-X^{p+1}=X^{p+1}(X^{m_q}-1),$$

so the admissible nonzero incidence consists of the $m_q$ distinct
roots $\mu_{m_q}(k)$. There is an explicit Hilbert--90 interpolant

$$h_q(x)=x^{q/p-1},\qquad
\frac{h_q(f(a))}{h_q(a)}
 =a^{q-p}=a\quad(a\in\mu_{m_q}). \tag{8.1}$$

It is regular and nonzero at every asserted sample point and has
degree $q/p-1$, which grows with $q$.

The growth is not an artefact of that choice. Let $T_0$ be any
fixed finite discarded set, $C=|T_0|$, and let $h=U/V$ be any
rational function of degree $b$, regular and nonzero at all asserted
sample points and their images, satisfying $\delta h(a)=a$ for
every $a\in\mu_{m_q}\setminus T_0$. In a coprime presentation
$\deg U,\deg V\le b$, the polynomial

$$J_h=U(x^{p+1})V(x)-xU(x)V(x^{p+1})$$

is nonzero: otherwise it would give the globally impossible
$\delta h=x$. It has degree at most $(p+2)b+1$ and has at least
$m_q-C$ distinct zeros. Thus

$$b\ge\frac{q-p-2-C}{p+2}. \tag{8.2}$$

In particular every family of valid original-$g$ rational transfers
has unbounded degree, even after an arbitrary fixed finite deletion.
This refutes the stronger $e=0$ version of (UB), including rational
denominators; it does not refute the correctly saturated bridge.

Indeed the single function $h=x$ works for $g^p$ with degree $1$.
The algebraic interface is also exact. Adjoin $Y$ with $Y^p=x$;
in the degree-$p$ purely inseparable extension $k(Y)/k(x)$, extend
$\sigma(a)=a\circ f$ by $\widetilde\sigma(Y)=Y^{p+1}=xY$.
Then $\widetilde\sigma(Y)=gY$. On the finite incidence, (8.1)
satisfies $h_q(a)^p=a^{q-p}=a$, so all its graph points lie on the
same curve $Y^p=X$. Unbounded rational interpolation degree can
therefore coexist with a fixed-degree finite algebraic transfer.

## 9. Two further exact boundaries of the same incidence mechanism

### 9.1. These incidences do not cover all ordinary native cycles

In characteristic $3$ let $f=x^2$. For every integer $t\ge1$, a
primitive $13^t$th root $a$ lies on a native cycle, since squaring
permutes that finite root-of-unity group. Its points never lie on
any first-step Frobenius incidence, for any $q=3^r$: equality
$a^2=a^{3^r}$ would imply $3^r\equiv2\pmod{13}$, whereas the
powers of $3$ modulo $13$ are $1,3,9$. Cycles arising from different
$t$ are distinct because squaring preserves their exact root order.
Thus infinitely many native cycles are absent from the union of
these incidences, even if the finite coefficient field is enlarged.

This does not refute (UB), whose hypothesis is full (CP), and does
not exhibit a rational observable passing every incidence norm test
while failing (CP). It only rules out treating the actual incidence
as a pointwise exhaustion of all native cycles or replacing (CP)
by such an exhaustion without another proof.

### 9.2. A general difference-field solution is too weak

For any $g\in k(x)^\times$, even without (CP), the transcendental
extension $k(x)(Y)$ has an injective $k$-endomorphism extending
$\sigma$ by $Y\mapsto gY$. Injectivity follows because a nonzero
polynomial in the transcendental $Y$ retains at least one nonzero
coefficient after the substitution. It has the formal solution
$\widetilde\sigma(Y)=gY$ but has infinite algebraic degree over
$k(x)$. A finitely generated difference-field object is not thereby
the finite algebraic extension required by R6.

Neither this construction nor the finite algebras $A_q$ supplies
one finite stable algebraic transfer. The missing datum is a single
finite algebraic extension carrying a forward-stable lift and a
nonzero transfer, or, under (CP), the equivalent uniform bound (UB).
A polynomial relation without that stable lift is not sufficient.

## 10. Bounded source check and exact applicability

The research-lit skill was used for a narrow applicability check,
not a new broad literature review. No exposed Zotero/Obsidian tool
was found. The local relevant-filename check produced only unrelated
symbolic-stream files, which were not read; no relevant local paper
was imported. No callable arXiv-fetch script was found, so the
arXiv-domain search fallback was used. No PDF was downloaded.

Exactly two query batches were used: first the Frobenius-incidence,
finite-field Hilbert--90, periodic-norm and rational-transfer interface;
second the exact original paper behind a Frobenius-difference survey
hit. The cap is exhausted; there is no third query batch.

| Actually accessed item | Relevant passage and exact subtraction |
| --- | --- |
| Chieh-Yu Chang, *Frobenius Difference Equations and Difference Galois Groups*, author survey dated 19 April 2015, [author PDF](https://www.math.nthu.edu.tw/~cychang/FBDGalois-Rev.pdf) | Introduction, Sections 2.1--2.3, and their displayed theorem statements were read. This was a routing source, not an imported original theorem; its Frobenius action twists coefficients while leaving the series variable fixed. Two later navigation attempts failed, and no missing text is claimed read. |
| Matthew A. Papanikolas, *Tannakian duality for Anderson--Drinfeld motives and algebraic independence of Carlitz logarithms*, [arXiv:math/0506078v2, 29 June 2007](https://arxiv.org/pdf/math/0506078v2) | Actually read: Sections 1.1--1.3, the complete twisting definition in 2.2.5, Theorem 4.3.1 with its proof, and Proposition 4.3.3 with its proof. Here the variable is fixed and coefficient Frobenius is an automorphism. The construction starts with an appropriate rigid analytic trivialization; it measures transcendence degree, not its vanishing from native cycle products. No (UB) or finite-algebraicity implication is imported. |

The original source's clock and starting object differ from this
task's substitution $x\mapsto x^d+c$. These specific results do not
justify the desired bridge. This bounded check does not establish
that no applicable theorem exists elsewhere or claim novelty for
the elementary finite-field calculations above.

## 11. Final gap and bounded handoff

The proved interface is

$$\text{full (CP)}
\Longrightarrow\text{actual norm-one data on every good }S_q
\Longrightarrow\text{finite interpolants of degree }<|G_q|.$$

The required additional implication remains exactly (UB): some fixed
$p^e$ must admit a degree bound independent of $q$, or a single
finite stable algebraic transfer must be constructed by equivalent
means. The first implication above handles every finite exception,
ordinary period and inseparable degree; none of those repairs produces
the missing complexity bound.

The old M6 family now has an explicit linear lower bound on all
unsaturated rational incidence transfers, while its fixed purely
inseparable algebraic transfer survives. Thus it diagnoses an
overstrong shortcut, not the full saturated claim. No example here
satisfies (CP) while excluding every $p$-power transfer, and no proof
of the full existence implication has been obtained.

The proof-writer skill requires retaining **NOT CURRENTLY JUSTIFIED**
for that implication; the research-lit skill influenced the exact
source/clock subtraction. This task stops at its frozen mechanism
and exhausted source cap. It has no mathematical execution, new agent,
external model/API, GPU, Git operation, PDF/manuscript, or old/shared
edit. General MS6 remains open; there is no fifth-contract admission.
