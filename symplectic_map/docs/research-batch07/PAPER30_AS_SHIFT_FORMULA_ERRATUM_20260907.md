# AS orbit-shift formula: preserved error and narrow repair

Date: 2026-09-07. Status: `AUTHOR_ERRATUM_PENDING_INDEPENDENT_CHECK`.
Feasibility status of the repaired lemma: `PROVABLE AS STATED` (author assessment).
This record preserves a real error in an earlier accepted proof. It does not
rewrite the frozen author input or either completed stage record.

## Claim and affected inputs

The affected author input is
[the Frobenius coinvariant probe](PAPER30_AS_FROBENIUS_COINVARIANT_PROBE_20260907.md),
336 lines, SHA256
`05aba58b468f3c4a5a9201f032200adb96e5acc6216ca65920066d2b2b3fe4d6`.
Its Step 3 proves the strong-balanced highest-orbit obstruction. The displayed
formula there for an arbitrary $r$-step shift is false. The preceding one-step
formula (4) is correct. The
[previous independent report](PAPER30_AS_FROBENIUS_COINVARIANT_INDEPENDENT_CHECK_20260907.md),
SHA256 `5fc8746299f3c3868ecffa5bdacb6d105fec7adad86ffcd40124f0544804ef15`,
did not detect this mistake and accepted the invalid $r$-step calculation.
That historical result remains unchanged; this document supplies the new finding.

The intended strong-balanced conclusion does not require arbitrary shifts.
Only two minimum-degree representatives can be relevant, and they are adjacent.
The one-step formula suffices to repair the argument without changing the
lemma's assumptions or conclusion. Independent closure of this repair is pending.

## Assumptions and notation

Use the binary orbit basis for $F=(x^2+c-y,x)$ over an algebraically closed
field of odd characteristic $p$, with $\lambda\in\mathbb F_p^*$.
For a finite nonempty word let $(a,b)$ be its exponent pair and
$\mu=a+b$ its ordinary polynomial degree. Its correct right shift is
$$
T_+(a,b)=\left(2a+\eta,\frac{b-\eta}{2}\right),
\qquad \eta=b\bmod2\in\{0,1\}.
\tag{E1}
$$
A strong-balanced pair satisfies $2a\ge b$ and $2b\ge a$.
Every occurring coinvariant orbit is represented once at its least ordinary
degree, and $D$ is the maximum of these least degrees.

## 1. The actual error — `REFUTED`

The old expression used the same number $t=b\bmod2^r$ both for the amount
removed from $b$ and for the amount added to $2^ra$. The latter must reverse
the order of the transferred binary digits.
For example, starting with $(a,b)=(0,1)$, two applications of (E1) give
$$
(0,1)\longmapsto(1,0)\longmapsto(2,0).
$$
The old $r=2$ expression instead gives $(1,0)$ at the last step.
Equivalently, $\sigma^2X_{-1}=X_1$ has highest term $x^2$, not $x$.

More precisely, if
$b\bmod2^r=\sum_{j=0}^{r-1}\eta_j2^j$, then the first coordinate after
$r$ right shifts is
$2^ra+\sum_{j=0}^{r-1}\eta_j2^{r-1-j}$, whereas the second is
$(b-\sum_j\eta_j2^j)/2^r$.
The erroneous general formula and its general divisibility argument are
not used below or in subsequent work.

## 2. Adjacent-minima lemma — author `PROVED`

The degree contribution of a single occupied site, along successive shifts,
is a translate of
$$
\ldots,8,4,2,1,1,2,4,8,\ldots.
$$
Its first differences are strictly increasing:
$\ldots,-4,-2,-1,0,1,2,4,\ldots$.
For a nonempty finite word, the degree sequence is a nonempty finite sum
of these translated sequences. Its first differences are therefore strictly
increasing as well. A strictly increasing difference sequence can equal zero
at at most one index. It follows that the minimum is attained at one position
or at two adjacent positions, never at two nonadjacent positions.

This strengthens the discrete-convexity observation already present in the
old proof; it adds no hypothesis on the binary word, $c$, $p$ or $\lambda$.

## 3. Repaired strong-balanced obstruction — author `PROVED`

The unchanged degree-triangular orbit basis shows that a degree-$D$ source
word with exponent pair $(a,b)$ contributes the unique ordinary degree-$pD$
word $(pa,pb)$ to its $p$th power, with nonzero coefficient. If $(a,b)$ is
strong-balanced, $(pa,pb)$ has least orbit degree $pD$. Thus no normal-form
term of degree less than $pD$ can belong to its orbit.

Suppose the degree-$pD$ word of a second source belongs to that target orbit.
Both representatives have degree $pD$, which is the least degree of the
target orbit. If they are identical, uniqueness of exponent pairs already
identifies the two sources. Otherwise the adjacent-minima lemma says they
are one shift apart. Orient that shift to the right, and apply (E1):
$$
(pa,pb)\longmapsto
\left(2pa+\eta,\frac{pb-\eta}{2}\right),\qquad \eta\in\{0,1\}.
$$
Both coordinates of the target are divisible by $p$. Its first coordinate
therefore forces $\eta=0$. Since $p$ is odd, $pb$ even implies $b$ even.
Dividing the two coordinates by $p$ gives exactly
$(2a,b/2)=T_+(a,b)$. The two original sources were themselves in the same
orbit, contrary to the choice of one representative per source orbit.

All competing degree-$pD$ sources are excluded, while all lower-degree
sources and lower normal-form terms were already excluded by minimality.
The surviving target coefficient is nonzero, including its nonzero
$\lambda$-power weight. The upper bound $\delta(\phi v)\le pD$ follows
from $\deg(h^p)=pD$. Hence the original conclusion
$$
\delta(\phi v)=pD>D
$$
holds under precisely the original strong-balanced assumptions. $\square$

## Boundary and required closure

Only the false multi-shift formula and the collision step are affected.
The basis, the Artin–Schreier bridge, the one-step degree formulas,
single-letter calculations and the characteristic-three kernel argument
do not use this expression. Their unchanged proofs are not reopened here.

This erratum does not itself classify the odd-reflection exceptions or the
full Frobenius fixed space. A fresh narrow check must examine this repair
together with any new theorem that depends on it; the old PASS is not reused
as evidence that this newly discovered defect was absent.
