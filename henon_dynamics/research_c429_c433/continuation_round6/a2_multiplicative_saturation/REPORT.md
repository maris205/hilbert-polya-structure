# MS6: cofinite multiplicative periodic data and p-saturated transfer

2026-09-10 UTC. One bounded theory-feasibility task, not a paper admission.

## Frozen repaired question

For every prime $p$, let $k=\overline{\mathbf F}_p$. For every
integer $d\ge2$, every $c\in k$, and every $g\in k(x)^\times$,
put $f(x)=x^d+c$. Are the following conditions equivalent?

1. Except for finitely many ordinary primitive $f$-cycles, every cycle
   avoids the zeros and poles of $g$ and satisfies
   $\prod_{a\in O}g(a)=1$.
2. There exist an integer $e\ge0$ and $h\in k(x)^\times$ such that

   $$g^{p^e}=h\circ f/h.$$

The clock is one application of $f$. Cofiniteness is in the set of
ordinary primitive cycles, not in one finite field and not in only
prime-to-$p$ periods. The support of a nonzero rational function is
finite, so only finitely many cycles meet its finite zeros or poles.
Zero and pole cancellations do not justify evaluating a transfer ratio
at a point where the transfer itself is zero or has a pole.

This is the separately specified repaired problem MS6. It is not an
assertion that the already refuted M6 question has changed truth value.

## Initial proof status and discriminator

**NOT CURRENTLY JUSTIFIED.** This is the pre-assessment status of the
reverse implication. The first test is an exact elementary counterexample,
including divisor orders at totally ramified fixed points and constant
factors. A complete counterexample must satisfy the cofinite product
condition and exclude every $p$-power rational transfer, not merely an
unsaturated rational transfer. Otherwise the next obligation is an actual
finite or purely inseparable transfer construction, not a formal logarithm.

## Actual inputs and execution boundary

The full Section 1 of
[X2's M6 report](../x2_independent_replacement/REPORT.md) was read.
It already proves the original M6 counterexample $f=x^{p+1},g=x$,
whose obstruction is removed by $g^p=f(x)/x$. Its separate example
$p=5,f=x^2,h=x-1,g=x+1$ shows why cancelled transfer zeros invalidate
unqualified pointwise telescoping. Both facts are subtracted as inputs,
not claimed as new MS6 results. The additive polynomial PC424-L theorem
does not itself construct a rational multiplicative transfer.

The proof-writer skill governs the exact statement and honest status.
Only this new report is writable. There is no mathematical program,
parameter census, new/nested agent, external model/API, Git operation,
manuscript/PDF, or old/shared-file edit allocation. A separate bounded
source/substantiality review belongs to X2 and the coordinator.

## 1. Outcome: a proved saturation reduction, not existence

Write $K=k(x)$, $\sigma a=a\circ f$, and

$$\delta a=\sigma a/a,\qquad
\mathcal C_f=K^\times/\delta K^\times.$$

Call condition 1 of the frozen question **(CP)**. The full reverse
implication remains **NOT CURRENTLY JUSTIFIED**: no complete MS6
counterexample was found, and (CP) has not been shown to construct a
finite algebraic transfer or even to make $[g]\in\mathcal C_f$ torsion.

The following auxiliary theorem is proved below for the full frozen
parameter range. Its additional torsion premise is essential to its
present proof and is not a consequence established here.

**Theorem 1 (saturation after existence).** Suppose $g$ satisfies (CP).
If, for some integer $m\ge1$ and $a\in K^\times$,

$$g^m=\delta a,$$

then there is $b\in K^\times$ with

$$g^{p^{v_p(m)}}=\delta b. \tag{1.1}$$

Consequently, under (CP), these three additional properties are
equivalent:

1. $[g]\in\mathcal C_f$ has finite order;
2. there is a finite extension $L/K$, a $k$-embedding
   $\widetilde\sigma:L\hookrightarrow L$ restricting to $\sigma$,
   and $H\in L^\times$ with $\widetilde\sigma H=gH$;
3. there is a $p$-power rational transfer as in MS6 condition 2.

In property 2, the extension need not be separable, Galois, or of
degree prime to $p$. If property 3 holds, the extension in property 2
can be chosen purely inseparable. These equivalences isolate the
missing existence statement; they do not prove it.

## 2. The easy implication and the elementary discriminators

### 2.1 A p-power rational transfer gives (CP)

Assume $g^{p^e}=\delta h$. Omit the finitely many primitive cycles
meeting zeros or poles of $g$ or $h$. On every remaining cycle $O$,
ordinary telescoping is valid and gives

$$\left(\prod_{a\in O}g(a)\right)^{p^e}=1.$$

In characteristic $p$, $Z^{p^e}-1=(Z-1)^{p^e}$, so this product is 1.
This proves condition 2 $\Rightarrow$ condition 1, including $e=0$.
No evaluation at a cancelled zero of $h$ is used.

### 2.2 Why the old counterexample does not refute MS6

For $f=x^{p+1}$ and $g=x$, every nonzero primitive cycle has product
$P_O$ satisfying $P_O^{p+1}=P_O$, hence $P_O^p=1$ and $P_O=1$.
Only the fixed zero meets the support of $g$. If $\delta h=x$, the
valuation at zero would give

$$(p+1)\operatorname{ord}_0h-\operatorname{ord}_0h=1,$$

which is impossible. But $g^p=f(x)/x=\delta x$, so the repaired
$p$-saturated conclusion is true in this example. This is X2's
already proved M6 obstruction, not a new counterexample or new result.

Constant factors also do not furnish an MS6 counterexample: Section 4
proves that a constant satisfying (CP) must be 1. These checks do not
constitute an exhaustive counterexample classification.

## 3. A finite algebraic transfer gives an integer-power rational one

**Lemma 3.1.** Suppose $L/K$ and $H$ satisfy property 2 of Theorem 1.
Let $m=[K(H):K]$. Then $g^m=\delta a$ for some $a\in K^\times$.

**Proof.** Let

$$A(Y)=Y^m+a_1Y^{m-1}+\cdots+a_m\in K[Y]$$

be the monic minimal polynomial of $H$. Since $H\ne0$, $a_m\ne0$.
Applying $\widetilde\sigma$ to $A(H)=0$ shows that

$$B(Y)=g^{-m}(\sigma A)(gY)$$

is another monic polynomial of degree $m$ over $K$ having root $H$.
Minimality gives $B=A$. Comparing constant terms yields
$a_m=g^{-m}\sigma a_m$, or $g^m=\delta a_m$. This argument does not
use a separable norm or linear disjointness. $\square$

Conversely, if $g^{P}=\delta a$ with $P=p^e$, adjoin the unique
$P$-th root $H$ of $a$ in a purely inseparable closure of $K$.
The embedding $\sigma:K\hookrightarrow K$ extends uniquely to that
closure. There,

$$(\widetilde\sigma H)^P=\sigma a=g^P a=(gH)^P,$$

so $\widetilde\sigma H=gH$ and $K(H)$ is forward stable. This proves
property 3 $\Rightarrow$ property 2 without (CP).

An arbitrary integer-power rational relation is not unconditionally
the same as a finite stable transfer: a nontrivial constant root of
unity $\zeta$ has $\zeta^m=1$ for some $m$, but cannot satisfy
$\widetilde\sigma H=\zeta H$ in such a finite extension. Indeed, the
same minimal-polynomial argument gives
$\sigma a_j=\zeta^j a_j$ for each nonzero coefficient. Rational-map
degrees give $d\deg a_j=\deg a_j$, so each $a_j$ is constant.
Then $H$ is algebraic over the algebraically closed field $k$, hence
$H\in k$, contradicting $\zeta\ne1$. The (CP) hypothesis below
removes this phase obstruction.

## 4. Large prime periods and constant phases

The elementary facts in this section are used only to control a fixed
finite exceptional set. There is no uniform assertion about
multiplicities of all primitive periodic points.

**Lemma 4.1 (bounded multiplicity at a fixed finite exceptional set).**
Let $E$ be a finite union of periodic cycles in $\mathbf P^1(k)$.
For all sufficiently large prime integers $n\ne p$, the contribution
of points in $E$ to the fixed-point intersection length of $f^n$ is
bounded by a constant independent of $n$.

**Proof.** Once the prime $n$ exceeds every period in $E$, only fixed
points of $f$ in $E$ can be fixed by $f^n$. At a fixed point choose a
local parameter $z$ and write the germ as $F(z)=\lambda z+O(z^2)$.
If $\lambda=0$, the fixed-point multiplicity of every iterate is 1.
If $\lambda\ne0,1$, its order $t$ in $k^\times$ is finite. For a
prime $n>t$, $\lambda^n\ne1$, again giving multiplicity 1.

If $\lambda=1$, the germ is not the identity because $\deg f>1$.
Thus $F(z)=z+\alpha z^r+O(z^{r+1})$ for some $r\ge2$ and
$\alpha\ne0$. Induction under composition gives

$$F^{\circ n}(z)=z+n\alpha z^r+O(z^{r+1}).$$

For $p\nmid n$ its multiplicity is exactly $r$. The same local
argument applies at infinity, where a polynomial has multiplier zero.
Summing over the fixed points in $E$ proves the bound. $\square$

**Lemma 4.2.** Every sufficiently large prime integer $n\ne p$ is
the exact period of some affine periodic point of $f$.

**Proof.** On $\mathbf P^1$, the graph of $f^n$ meets the diagonal
with total length $d^n+1$. This also follows directly from the degree
$d^n$ polynomial $f^n(x)-x$ and the simple fixed point at infinity.
Apply Lemma 4.1 to the finite set of fixed points of $f$, including
infinity. Their bounded contribution cannot account for $d^n+1$.
Any other fixed point of $f^n$ has exact period $n$, since $n$ is
prime, and is affine. $\square$

**Corollary 4.3.** If $\zeta\in k^\times$ is a constant satisfying
(CP), then $\zeta=1$.

**Proof.** If its order is $t>1$, choose a prime $n$ so large that
Lemma 4.2 applies, $n>t$, and $n$ exceeds the periods of all exceptional
cycles in (CP). The product on a primitive $n$-cycle is $\zeta^n$.
But $\gcd(n,t)=1$, so this cannot be 1. $\square$

## 5. The curve fixed-point bound, with inseparability retained

Here is the precise classical input and its application. For a smooth
projective surface, the Hodge index theorem says that the intersection
pairing on divisor classes orthogonal to an ample divisor is negative
definite modulo numerical equivalence. The algebraic theorem and proof
are in Patrick Brosnan's official
[UMD 808J notes, Section 3.3, Corollary 3.14 and Theorem 3.15](https://math.umd.edu/~pbrosnan/notes/Surfaces/shit.html).
The underlying algebraically closed field is specified in
[Section 3.1](https://math.umd.edu/~pbrosnan/notes/Surfaces/sect0016.html),
and the arbitrary-characteristic scope of the main treatment is stated
in [Section 1.1](https://math.umd.edu/~pbrosnan/notes/Surfaces/sect0002.html).
This is a standard input, not a novelty claim. The following calculation
spells out the needed application, including a possibly inseparable map.

**Lemma 5.1.** Let $Y$ be a smooth connected projective curve over $k$
of genus $\gamma$, and let $\phi:Y\to Y$ be a morphism of degree
$q>1$, possibly inseparable. If $N(\phi)$ is the sum of fixed-point
intersection multiplicities, then

$$|N(\phi)-(q+1)|\le2\gamma\sqrt q. \tag{5.1}$$

**Proof.** In $Y\times Y$, let $F_1=\{a\}\times Y$,
$F_2=Y\times\{a\}$, $\Gamma=\Gamma_\phi$, and let $\Delta$ be
the diagonal. Their intersection numbers are

$$F_1^2=F_2^2=0,\quad F_1F_2=1,\quad
\Gamma F_1=1,\quad \Gamma F_2=q,\quad
\Delta F_1=\Delta F_2=1.$$

The normal bundle of the graph is $\phi^*T_Y$: along the graph, the
quotient of $T_Y\oplus\phi^*T_Y$ by the image of
$v\mapsto(v,d\phi(v))$ is isomorphic to $\phi^*T_Y$ through
$(v,w)\mapsto w-d\phi(v)$. This remains true if $d\phi=0$.
Therefore

$$\Gamma^2=q(2-2\gamma),\qquad \Delta^2=2-2\gamma.$$

The divisor $F_1+F_2$ is ample (it is the external tensor product of
positive-degree line bundles on the two curves). Set

$$A=\Gamma-qF_1-F_2,\qquad B=\Delta-F_1-F_2.$$

Both are orthogonal to $F_1+F_2$, and direct expansion gives

$$A^2=-2\gamma q,\qquad B^2=-2\gamma,\qquad
AB=N(\phi)-q-1.$$

The graph and diagonal are distinct irreducible curves because
$q>1$, so $\Gamma\Delta=N(\phi)$ is the finite intersection length.
The Cauchy--Schwarz inequality for the negative of the Hodge pairing
gives $(AB)^2\le A^2B^2=4\gamma^2q$. This includes $\gamma=0$,
when both primitive classes are numerically zero. $\square$

In particular, for a degree-$d$ self-map $T$ of $Y$,

$$N(T^n)\le d^n+1+2\gamma d^{n/2}. \tag{5.2}$$

The count is not the number of distinct fixed points. Keeping local
intersection multiplicities is what makes the comparison below valid
without a separability restriction on $f$ or $T$.

## 6. No prime-to-p torsion survives (CP)

**Lemma 6.1.** Let $\ell\ne p$ be a prime, and suppose
$W\in K^\times$ satisfies (CP) and

$$W^\ell=\delta h\qquad(h\in K^\times). \tag{6.1}$$

Then $W\in\delta K^\times$.

**Proof.** First suppose $h=a^\ell$ in $K$. Then
$(W/\delta a)^\ell=1$, so $W/\delta a=\zeta\in\mu_\ell(k)$.
Outside the finitely many cycles meeting the support of $a$, the
products of $\delta a$ telescope to 1. Thus $\zeta$ satisfies (CP).
Corollary 4.3 gives $\zeta=1$, proving the assertion in this case.

Now suppose $h$ is not an $\ell$-th power. The polynomial
$Y^\ell-h$ is irreducible over $K$. To check the exact Kummer step,
let $y$ be a root. Since $\mu_\ell\subset k$ and $\ell\ne p$,
$K(y)$ contains every root and is a separable splitting field.
Its Galois group embeds into the group $\mu_\ell$, by its action on
$y$. Its degree is consequently either 1 or the prime $\ell$.
Degree 1 would make $h$ an $\ell$-th power, which was excluded.

Let $L=K(y)$, $y^\ell=h$, and let $Y$ be the smooth projective
curve with function field $L$. It is connected, and the corresponding
finite morphism $\pi:Y\to\mathbf P^1$ has degree $\ell$. Its
smooth model exists over the perfect field $k$; no higher-dimensional
resolution assertion is involved.

Equation (6.1) makes

$$\widetilde\sigma x=f(x),\qquad
\widetilde\sigma y=W(x)y \tag{6.2}$$

a well-defined field embedding $L\hookrightarrow L$, since
$(Wy)^\ell=W^\ell h=\sigma h$. It corresponds to a morphism
$T:Y\to Y$ with $\pi T=f\pi$. Its degree is exactly $d$:

$$[L:k(f(x))]=\ell d,
\qquad [\widetilde\sigma L:k(f(x))]=[L:k(x)]=\ell,$$

so $[L:\widetilde\sigma L]=d$. This degree calculation includes
inseparable $f$.

Let $E$ be the finite union of all exceptional primitive cycles for
(CP), all primitive cycles meeting a zero or pole of $W$ or $h$ or a
branch point of $\pi$, and the fixed point at infinity. Each listed
support is finite; only finitely many primitive cycles meet it.
Nonperiodic support points need not be added to $E$.

If an ordinary base cycle $O$ of length $r$ is disjoint from $E$,
then $\pi$ is etale over $O$. Each fiber has $\ell$ distinct points
with nonzero finite $y$-coordinate. By (6.2), $T^r$ multiplies this
coordinate by $\prod_{a\in O}W(a)=1$. Thus $T^r$ fixes every one
of these fiber points, not merely the fiber as a set.

For every $n$ divisible by $r$, all $\ell$ points above each
$a\in O$ are fixed by $T^n$. Their local fixed-point multiplicities
are equal to that of $f^n$ at $a$: etaleness identifies each completed
local ring with $k[[z]]$ by a base uniformizer, and the commutative
square $\pi T^n=f^n\pi$ identifies the two return germs. Hence the
orders of their differences from the identity are identical. This
does not require $T$ to be separable.

Choose prime integers $n\ne p$ sufficiently large for Lemma 4.1
to apply to this fixed $E$. Its contribution to $N(f^n)=d^n+1$ is
at most a constant $C$. Counting all lifts of the other fixed points,
with the multiplicities just checked, gives

$$N(T^n)\ge\ell(d^n+1-C). \tag{6.3}$$

But (5.2), with $\gamma=g(Y)$, gives

$$N(T^n)\le d^n+1+2\gamma d^{n/2}. \tag{6.4}$$

The two inequalities contradict one another along arbitrarily large
prime $n$, since $\ell>1$ and $d>1$. Thus the non-$\ell$-th-power
case cannot occur. This completes the proof. $\square$

**Proof of Theorem 1.** Write $m=p^t s$ with $p\nmid s$, and set
$G=g^{p^t}$. In $\mathcal C_f$, the order $r$ of $[G]$ divides
$s$. If $r>1$, choose a prime $\ell\mid r$ and put
$W=G^{r/\ell}$. Powers preserve (CP), and $W^\ell\in\delta K^\times$.
Lemma 6.1 implies $W\in\delta K^\times$, contradicting the order
$r$ of $[G]$. Therefore $r=1$, proving (1.1).

Property 1 of the theorem implies property 3 by this argument.
Lemma 3.1 gives property 2 $\Rightarrow$ property 1, and the
purely inseparable construction in Section 3 gives property 3
$\Rightarrow$ property 2. $\square$

## 7. The exact missing bridge and the limits of the reduction

To complete MS6 by the proved reduction, it remains to establish:

> For every frozen $p,d,c,g$, (CP) implies that the class
> $[g]\in K^\times/\delta K^\times$ is torsion.

Equivalently under (CP), one may construct a single finite
$\sigma$-stable field extension and a nonzero transfer $H$.
An arbitrary pointwise solution on periodic fibers is not such an
extension, and no uniform algebraic relation for those solutions has
been obtained in this report. The additive polynomial coboundary
theorem supplies neither a rational logarithm nor this multiplicative
torsion assertion.

For the skew map $S(x,y)=(f(x),g(x)y)$, (CP) does imply that, outside
finitely many base cycles of least period $n$, the exact base return
$S^n$ fixes the corresponding vertical fibers pointwise on their
domains of definition. Merely
having setwise periodic vertical fibers would be automatic for all
$g$ and carries no such product information. Even pointwise fixation
by some unspecified iterate is automatic here: every nonzero cycle
multiplier in $\overline{\mathbf F}_p$ has finite order. The exact
least-base-period return must therefore be retained. No verified theorem
turning the pointwise assertion into a rational first integral, even
after a finite purely inseparable cover, has been supplied or invoked.

Likewise, a theorem which starts with an already algebraic Mahler-type
series cannot supply the missing existence step. X2's separately
checked sources and boundary decisions are recorded in
[its saturation-source report](../x2_multiplicative_saturation_sources/REPORT.md).

Theorem 1 is an auxiliary classical-cover/intersection reduction. It
is not a fifth paper, an independent admitted contract, a proof of
MS6, or a replacement for the refuted unsaturated M6 assertion.

## 8. Source and execution audit

The proof-writer skill was used to freeze the all-parameter statement,
keep the missing implication explicit, and give the actual field,
cover, local-multiplicity, and intersection arguments. A narrow use of
the research-lit skill checked the standard arbitrary-characteristic
surface input; it did not run a second unrestricted MS6 novelty search.

Actual source access for that premise:

- The active tool inventory had no Zotero/Obsidian interface. A
  filename-only check of the local `papers/` and `literature/` roots
  found no relevant Hodge/Kummer/intersection source. No unrelated
  local PDF was read or used.
- Five bounded web-discovery queries across the Hodge-index premise
  check included one arXiv-domain query. No arXiv search hit was
  imported as a theorem. The previously checked expected local arXiv
  fetch-script locations were unavailable; web access was the fallback.
- Brosnan's official Section 3.3 was actually read through Lemma 3.11,
  Corollaries 3.12 and 3.14, Theorem 3.15, and all displayed proofs.
  Sections 1.1 and 3.1 were read for scope, and Section 3.2, Theorem
  3.4 and its displayed proof, was also inspected. Only the classical
  Hodge statement is imported; Lemma 5.1 writes out this report's
  graph application.
- Piotr Achinger's official 2026 lecture PDF was discovered and its
  metadata/table of contents were accessible, but attempts to read
  the needed later theorem pages repeatedly timed out. It is not a
  proof source for this report. No claim is supported by that unread
  theorem or by a search snippet.
- X2 separately checked Milne's etale-cohomology fixed-point formula.
  This report does not rely on an unverified square-root bound being
  part of that formula: Section 5 derives the bound from Hodge index.
  No priority or exhaustive-literature conclusion is drawn here.

All calculations above are hand proofs. No mathematical program,
parameter census, external model/API, nested worker, Git operation,
manuscript/PDF generation, or old/shared-file edit was performed.
The only authored path in this task is this report. Final reverse
implication status: **NOT CURRENTLY JUSTIFIED**, with the torsion/
finite-transfer existence bridge precisely isolated.
