# R7 A1: one balanced quadratic divisor atom

2026-09-10 UTC. A bounded adversarial discriminator inside unchanged MS6,
not a separate research contract or paper.

## Frozen exact sublemma and failure boundary

For every odd prime $p$, put $k=\overline{\mathbb F}_p$. For every
$c\in k$ and every $a\in k^\times$, set

$$f(x)=x^2+c,\qquad g_a(x)=\frac{x-a}{x+a}.$$

The native clock is one application of $f$. A good ordinary primitive
cycle $O$ avoids $\{a,-a\}$ and satisfies

$$\prod_{x\in O}g_a(x)=1.$$

The chosen exact sublemma to test is:

> For every stated $p,c,a$, there are infinitely many distinct ordinary
> primitive cycles, disjoint from $\{a,-a\}$, on which the displayed
> product is not $1$.

If this sublemma is false, a complete discriminator must exhibit stated
parameters for which all but finitely many primitive cycles are good.
Finding only finitely many bad cycles does not refute that cofinite
condition (CP). Finding a nonzero balanced divisor alone also does not
establish a (CP) counterexample.

No parameter is removed from the chosen atom family. There is no
enlargement to several atoms, other degrees, an additive kernel, or a
formal logarithm.

## Status and input subtraction

**NOT CURRENTLY JUSTIFIED for the full frozen sublemma.** The bounded
test proves the following exact reduction, without silently changing
the original all-parameter question:

> If $g_a$ satisfies (CP), then $c=-1$ and $a\in\{1,-1\}$.
> Consequently every other parameter in the frozen family has
> infinitely many bad ordinary primitive cycles.

The residual family $f=x^2-1$, $a=\pm1$, for every odd $p$, is not
settled here: neither (CP) nor infinitely many bad cycles is proved
for it. Thus no MS6 counterexample or full-family closure is asserted.

The accepted 441-line
[R6 saturation proof](../../continuation_round6/a2_multiplicative_saturation/REPORT.md)
was read completely. It supplies saturation conditional on an existing
integer-power transfer, not the existence implication needed here.
The [R7 finite-divisor mechanism](../a2_multiplicative_existence/REPORT.md)
was read at its initial frozen version; its (CP)-to-residual-zero arrow
is not assumed.

Only this report is writable. No mathematical program, nested agent,
external model/API, Git, old/shared-file, manuscript or PDF action is
allocated. At most two bounded primary-source query batches are allowed.

## Plan and dependency map

1. Prove directly that the atom has no nonzero integer-power rational
   transfer, using $f_*\operatorname{div}(g_a)=0$.
2. Test whether the cofinite product condition nevertheless can hold,
   retaining ordinary primitive periods and exceptional cycles exactly.
3. Give either a full all-parameter infinite-bad-cycle proof, an actual
   (CP) counterexample with non-torsion certified, or the precise gap.

## Hand proof

Write $F_n(X)=f^{\circ n}(X)-X$ for $n\ge1$. A product over roots
of $F_n$ below includes their polynomial multiplicities. The primitive
cycle products in (CP) continue to use each distinct cycle point once.
The next lemma justifies the passage between those two conventions.

### 1. Multiplicities on a cycle and under large prime repetitions

**Lemma 1.** The multiplicity in $F_n$ is constant along every
ordinary cycle whose least period divides $n$. Fix $N\ge1$ and a
finite collection of points fixed by $f^{\circ N}$. For all sufficiently
large prime integers $\ell\ne p$, their multiplicities in $F_{N\ell}$
equal their multiplicities in $F_N$.

**Proof.** If a periodic cycle contains a critical point, its return
multiplier is zero. At each point of that cycle the derivative of
$F_n$ is then $-1$, so every root is simple. Otherwise all derivatives
of $f$ along the cycle are nonzero. Each step of $f$ is an invertible
formal coordinate change at the corresponding cycle points. The
identity $f^{\circ n}\circ f=f\circ f^{\circ n}$ formally conjugates
their return germs. The order of a germ minus the identity is preserved
under such conjugacy, proving constancy of the multiplicity.

For the second assertion, let $G$ be the local germ of $f^{\circ N}$
at one of the finitely many points, and let $\theta=G'(0)$. If
$\theta=0$, both multiplicities are one. If $\theta\ne0,1$, it has
finite order $t$ in $k^\times$. For a prime $\ell>t$, one has
$\theta^\ell\ne1$, so both multiplicities are again one. If
$\theta=1$, the polynomial iterate is not the identity because it
has degree $2^N>1$. Therefore, for some $m\ge2$ and $u\ne0$,

$$G(z)=z+uz^m+O(z^{m+1}).$$

Composition gives

$$G^{\circ\ell}(z)=z+\ell u z^m+O(z^{m+1}). \tag{1}$$

For $\ell\ne p$ the multiplicity is $m$ in both iterates. Taking
the maximum of the finitely many required bounds proves the lemma.
No uniform assertion over all periodic points is made. $\square$

### 2. The atom is non-torsion for every frozen parameter

Let $D=\operatorname{div}(g_a)=[a]-[-a]$. Since $a\ne0$ and $p$
is odd, $D\ne0$. For geometric points let $f_*[x]=[f(x)]$. Then

$$f_*D=[a^2+c]-[a^2+c]=0. \tag{2}$$

Suppose that $g_a^m=h\circ f/h$ for an integer $m\ge1$ and a
rational function $h\in k(x)^\times$. With $E=\operatorname{div}(h)$,
taking divisors and then pushforward gives

$$mD=f^*E-E,\qquad 0=2E-f_*E. \tag{3}$$

Here $f_*f^*E=2E$, including ramified fibers, because $f$ has degree
two and the residue fields of geometric points are $k$. For a finite
real divisor $B=\sum b_x[x]$ define
$\|B\|_1=\sum|b_x|$. Merging coefficients under pushforward cannot
increase this norm, so $\|f_*B\|_1\le\|B\|_1$. Equation (3) implies
$2\|E\|_1\le\|E\|_1$, hence $E=0$. Its first equality then forces
$mD=0$ in the torsion-free divisor group, contradicting $D\ne0$.

Thus every $g_a$ in the frozen family has infinite order modulo
rational multiplicative coboundaries. This proof also excludes every
$p$-power transfer. It does not imply (CP).

### 3. An elementary prime-residue observation

**Lemma 2.** If a positive integer $t$ divides $\ell-1$ for every
sufficiently large prime integer $\ell$, then $t\le2$. In particular,
for every odd prime $p$ there are arbitrarily large primes $\ell$
with $\ell\not\equiv1\pmod p$.

**Proof.** Suppose $t>2$, and choose a bound $B$ beyond which all
primes are assumed congruent to one modulo $t$. Let $Q$ be the product
of all primes at most $B$ that do not divide $t$, taking an empty
product to be one. The integer $tQ-1>1$ has no prime divisor at most
$B$: primes dividing $t$ or $Q$ both give residue $-1$. All its prime
factors are therefore congruent to one modulo $t$. This forces
$tQ-1\equiv1\pmod t$, whereas $tQ-1\equiv-1\pmod t$. Hence
$t\mid2$, a contradiction. This uses no Dirichlet theorem. $\square$

### 4. (CP) forces a signed atom point onto a cycle of length at most two

Assume (CP). If one of $a,-a$ is fixed, the asserted conclusion of
this step already holds. Otherwise neither point is fixed. Since
$a,c\in\overline{\mathbb F}_p$, their coordinates and coefficients
lie in some finite field stable under $f$, so each has finite forward
orbit. Choose prime integers $\ell$ larger than the periods of every
exceptional cycle in (CP), larger than any period of $a$ or $-a$
when those points are periodic, and large enough for Lemma 1 with
$N=1$. Also require $\ell\ne p$.

Then neither $a$ nor $-a$ is a root of $F_\ell$. Every root is
either fixed or has exact period $\ell$. All the latter cycles are
good by (CP); by Lemma 1 each such cycle contributes its ordinary
product raised to one common positive integer multiplicity, still
one. The fixed-point multiplicities equal those in $F_1$. Thus

$$\prod_{F_\ell(\alpha)=0}g_a(\alpha)
=\prod_{F_1(\alpha)=0}g_a(\alpha). \tag{4}$$

For every $n\ge1$, $f^{\circ n}$ is even, and $F_n$ is monic.
Consequently, whenever the displayed values are nonzero,

$$\prod_{F_n(\alpha)=0}g_a(\alpha)
=\frac{F_n(a)}{F_n(-a)}
=\frac{f^{\circ n}(a)-a}{f^{\circ n}(a)+a}. \tag{5}$$

The signs from the two monic root products cancel. All denominators
and numerators in (4)–(5) are nonzero under the present assumptions.
Set $b=f(a)$. Substituting (5) in (4) and cross-multiplying yields

$$2a\bigl(f^{\circ\ell}(a)-b\bigr)=0.$$

Since $2a\ne0$, this proves

$$f^{\circ\ell}(a)=f(a)=b
\quad\text{for every sufficiently large prime }\ell. \tag{6}$$

In particular $b$ is periodic. If its least period is $t$, equation
(6) gives $t\mid\ell-1$ for every sufficiently large prime $\ell$.
Lemma 2 implies $t\le2$. Let $u$ be the predecessor of $b$ in this
periodic cycle. Then $f(u)=b=f(a)$, so $u^2=a^2$, and $u=a$ or
$u=-a$. Hence one of $a,-a$ belongs to a cycle of least period at
most two. The all-large-prime quantifier is essential here; selecting
one congruence progression would not prove the same period bound.

The aggregate mechanism in this step was also suggested independently
by the coordinator. The proof above checks its multiplicities and
strengthens the prime selection without invoking a progression theorem.

### 5. A noncritical support cycle contradicts (CP)

This step in fact applies whenever one of $a,-a$ is periodic with
nonzero return multiplier, regardless of its least period. Replacing
$a$ by $-a$ replaces $g_a$ by its reciprocal and preserves both (CP)
and the set of bad cycles. Thus assume $a$ is periodic, with cycle
$O_a$, least period $r$, and multiplier
$\lambda=(f^{\circ r})'(a)\ne0$.

The point $-a$ is not periodic. Indeed, the restriction of any map
to its set of periodic points is injective: a periodic image has a
unique periodic predecessor in its own cycle. If both signed points
were periodic, $f(a)=f(-a)$ would force $a=-a$, contrary to $2a\ne0$.

Let $t$ be the finite order of $\lambda\in k^\times$, and put
$N=rt$. The germ of $f^{\circ N}$ at $a$ has the form

$$f^{\circ N}(a+z)=a+z+u z^m+O(z^{m+1}),
\qquad m\ge2,\quad u\ne0. \tag{7}$$

Such a finite $m$ exists since a polynomial of degree $2^N>1$
cannot be the identity germ. For every prime $\ell\ne p$,
equation (1) gives

$$F_{N\ell}(a+z)=\ell u z^m+O(z^{m+1}). \tag{8}$$

Choose $\ell$ larger than the periods of all exceptional cycles
in (CP), and large enough for Lemma 1 applied to all the finitely
many roots of $F_N$. An exceptional cycle of period $s$ can occur
in $\operatorname{Fix}(f^{\circ N\ell})$ only if $s\mid N\ell$.
Because $\ell>s$ is prime, this is equivalent to $s\mid N$.
Thus no additional exceptional cycle occurs at time $N\ell$.
All old fixed-point multiplicities are unchanged by Lemma 1.

For $n=N$ or $n=N\ell$, let

$$J_n:=\prod_{\substack{F_n(\alpha)=0\\\alpha\ne a}}
g_a(\alpha), \tag{9}$$

again with multiplicities. These products are finite and nonzero:
the only periodic zero of $g_a$ is $a$, which is removed, and its
pole $-a$ is not periodic. Separate the other points of $O_a$ in
(9), together with the finitely many exceptional cycles. Their
factors and multiplicities are unchanged. Every other complete cycle
contributes one by (CP) and Lemma 1. Therefore

$$J_{N\ell}=J_N. \tag{10}$$

On the other hand, factor $F_n(X)=(X-a)^m H_n(X)$. Let $u_n$ be
the coefficient of $(X-a)^m$ in $F_n$, so $H_n(a)=u_n$. Because
$f^{\circ n}(a)=a$ and $f^{\circ n}$ is even,
$F_n(-a)=2a$. Hence

$$H_n(-a)=\frac{2a}{(-2a)^m},\qquad
J_n=\frac{H_n(a)}{H_n(-a)}
=(-1)^m(2a)^{m-1}u_n. \tag{11}$$

Equations (7)–(8) say $u_N=u$ and $u_{N\ell}=\ell u$. Thus
(11) gives $J_{N\ell}=\ell J_N$. Since $J_N\ne0$, equation (10)
would force $\ell=1$ in $k$ for every sufficiently large prime
$\ell\ne p$. Lemma 2 with $t=p>2$ contradicts this. Therefore
(CP) is impossible when the signed support cycle is noncritical.

The coordinator independently supplied the same local-leading-term
mechanism. This proof uses large primes to keep the entire fixed
finite exceptional set unchanged; it does not assert anything about
multiplicity growth at all new cycles.

### 6. Complete parameter reduction and its exact residual

Under (CP), Step 4 supplies a signed support point on a cycle of
least period one or two. Step 5 requires its return multiplier to be
zero. For $f'=2x$ in odd characteristic this means that its cycle
contains $0$.

A critical fixed cycle would consist of $0$, whereas the signed
support point is nonzero. Thus the cycle has least period two.
Writing it as $0\mapsto c\mapsto0$ gives $c\ne0$ and

$$c^2+c=0,$$

so $c=-1$. Its unique nonzero point is $-1$, and therefore
$a\in\{1,-1\}$. This proves the parameter reduction stated in
the status section.

For every parameter outside that residual, if there were only
finitely many bad cycles disjoint from the atom support, (CP) would
hold: at most two other cycles can meet the two support points.
The reduction gives a contradiction. Hence the conclusion there is
genuinely infinitely many distinct bad primitive cycles, not merely
one bad finite sample.

## The remaining critical two-cycle test

For $f=x^2-1$ and $a=1$, let $O$ be any primitive cycle avoiding
$\{0,1,-1\}$, and set

$$A_O=\prod_{x\in O}x,\qquad
B_O=\prod_{x\in O}(x+1),\qquad
C_O=\prod_{x\in O}(x-1).$$

The identities $f(x)+1=x^2$ and $f(x)=(x-1)(x+1)$, followed by
permutation of the cycle under $f$, give

$$B_O=A_O^2,\qquad B_OC_O=A_O,
\qquad \prod_{x\in O}g_1(x)=A_O^{-3}. \tag{12}$$

The same criterion holds for $a=-1$, by inversion. These identities
were also supplied by the coordinator and are checked here directly.
Thus the exact residual obligation is whether, for every odd $p$,
infinitely many such cycles satisfy $A_O^3\ne1$, or whether some
odd $p$ supplies a genuine cofinite counterexample.

Condition (CP) in this residual would force, on all but finitely
many cycles of length $n$, the nonzero multiplier
$\lambda_O=2^n A_O$ to satisfy

$$\lambda_O^{3(p-1)}=1. \tag{13}$$

In characteristic three, (12) would even give $A_O=1$ on all such
cycles. These are necessary restrictions, not established rigidity
theorems. Every multiplier merely being a root of unity is automatic
over $\overline{\mathbb F}_p$ and would supply no such bound.

At the critical two-cycle the return multiplier is zero, so the germ
of a return minus the identity has linear coefficient $-1$ for every
positive repetition. In particular the varying coefficient in (8)
is absent. This is the exact failure of Step 5, not a counterexample
to the full sublemma. Neither finitely many explicit bad cycles nor
their merged resultant products settle the remaining cofinite question.

## Source and execution audit

The proof-writer skill was used to freeze the unchanged all-parameter
sublemma and to separate the proved parameter reduction from the
remaining case. The repository batch skill keeps this as an auxiliary
discriminator inside MS6; it does not create a fifth contract.

Two bounded primary-search batches were used through research-lit.
The first used multiplicative periodic-cocycle/finite-characteristic
terms, with an arXiv-domain fallback. No Zotero/Obsidian interface was
available; relevant filename checks in the local paper-library and
expected arXiv-script locations found no applicable file. The first
batch returned classical hyperbolic Livšic papers and unrelated hits;
none supplied or was imported as an algebraic existence theorem here.

The second batch tested whether a uniform finite multiplier set for
a single positive-characteristic map is covered by a verified
rigidity theorem. Alon Levy's
[*The McMullen Map in Positive Characteristic*, arXiv:1304.2834v2](https://arxiv.org/html/1304.2834v2)
was read at its exact Theorem 1.1, Example 1.4, Theorems 1.10 and
1.12, Corollary 1.14 and surrounding scope discussion. Those statements
concern multiplier-spectrum maps and isospectral families, not the
needed bounded-multiplier classification of this single map.
In particular Theorem 1.12 excludes spectra entirely over
$\overline{\mathbb F}_p$, so it cannot be applied to (13).
No rigidity consequence for the residual is claimed. The author's PDF
fetch timed out; the primary arXiv HTML supplied the actual checked
statements. No source theorem is needed for Steps 1–6.

The actual R7 A2 characteristic-five infinite-bad control and its
characteristic-three aggregate-information-loss example were read in
its report. They are already owned inputs, not new results here, and
neither treats the surviving critical-two-cycle family.

No mathematical program, parameter census, new/nested agent, external
model/API upload, Git operation, old/shared-file change, manuscript or
PDF action was performed. The two source-query batches are exhausted.

## Frozen disposition

The atom is non-torsion for every frozen parameter. Infinitely many
bad native cycles are proved for every parameter except
$f=x^2-1$, $a=\pm1$. For that remaining family no (CP) witness and
no infinite-bad-cycle proof was obtained in this bounded test.
The full frozen sublemma and MS6 existence implication therefore
remain **NOT CURRENTLY JUSTIFIED**. This report freezes that exact
gap without expanding the atom family, degree, or mechanism.
