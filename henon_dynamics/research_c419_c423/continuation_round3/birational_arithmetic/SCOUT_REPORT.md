# Round-three birational arithmetic scout: no additional admission

2026-09-07. Same C419--C423 batch. M1, AS2 and IR1 stay admitted and
untouched; this lane adds zero contracts and zero manuscripts. These are
research dispositions, not claims that the unsolved problems are
impossible or globally novel. The main workflow contribution is refusing
to turn two finite exhaustive diagnostics into all-parameter theorems.

| Candidate | Exact progress | Decisive remaining issue | Disposition |
|---|---|---|---|
| B1: $H_c(x,y)=(y,-x+y+c/y^2)$, every integer $c$, ordinary nonzero integral cycles | One complete divisor-graph diagnostic for $1\le c\le512$: 8 fixed cycles and no others; necessary divisor and primitive-scaling reductions | No global exclusion of nonconstant primitive cycles | `REJECT_UNCLOSED_ARITHMETIC_RIGIDITY` |
| B2: $f_{a,b}(x,y)=(y,(y+a)/(x+b))$, every integer $(a,b)$ with $b\ne0$, ordinary two-sided integral cycles | Uniform elementary height bound; one complete 272-parameter diagnostic; exact unbounded parameter family of genuine 3-cycles | No exhaustive all-parameter recurrent-core/period theorem; a unit-denominator section misses nonfixed cycles | `REJECT_HEIGHT_BOUND_WITH_UNCLOSED_CORE` |
| B3: $(y,(y^d+c)/x)$, $d\ge3$, $c\in\mathbb Z$, ordinary nonzero rational cycles | Shallow source/local-collision screen; same negative-valuation/power-gap route as NG2 | No distinct substantial mechanism after old NG2 is deducted | `REJECT_SHORT_COMPANION_EXTENSION` |

The two deep-screening slots were B1 and B2. B3 received no mathematical
CPU and was not substituted for either failed complete question. The
contracts, complete parameter domains, clocks, exclusions and finite
test scopes were written in [FROZEN_CONTRACTS.md](FROZEN_CONTRACTS.md)
before their respective computations. Source ownership and actual read
scopes are recorded in [SOURCE_AUDIT.md](SOURCE_AUDIT.md).

## 1. B1: divisibility is not uniform arithmetic rigidity

For a native integral cycle $(x_i)_{i\in\mathbb Z/n\mathbb Z}$, all
$x_i\ne0$ and
$$c=x_i^2(x_{i-1}+x_{i+1}-x_i).$$
Consequently $x_i^2\mid c$ for every coordinate when $c\ne0$. For one
fixed $c$, every possible periodic state therefore belongs to the finite
graph on
$$D_c^2,\qquad D_c=\{r\in\mathbb Z\setminus\{0\}:r^2\mid c\}.$$
This proves finite decidability for each parameter, but it is explicitly
below the frozen eligibility threshold.

If $g=\gcd_i|x_i|$, the displayed recurrence gives $g^3\mid c$.
Dividing every $x_i$ by $g$ produces a primitive integral cycle for
$c/g^3$. A fixed point is $(r,r)$ with $c=r^3$. The simultaneous sign
change conjugates $H_c$ to $H_{-c}$, so the single diagnostic used
positive parameters only. The $c=0$ linear order-six boundary was
deducted before selection and is not a result of this scout.

The predeclared run enumerated all 6,980 potential ordered states over
$1\le c\le512$, retained 407 legal edges and extracted every graph
cycle, with no maximum period. It found exactly the eight fixed cycles
at $c=1,8,27,64,125,216,343,512$. This is a complete assertion for
those parameters, not a proof of the fixed-only guess for arbitrary $c$.
See [exact_probe.py](exact_probe.py) and its generated
[B1_EXACT_PROBE_OUTPUT.json](B1_EXACT_PROBE_OUTPUT.json).

The missing implication is precise: nothing proved here forces a
primitive periodic coordinate word to be constant. Specialized integer
values of universally coprime Laurent factors may share prime factors,
and generic rational height growth does not exclude exceptional
periodic specializations. Almost good reduction is also not such an
exclusion theorem. The classical Laurent/height discussion and local
reduction statement are actually present in
[Hone, Section 4](https://sigma-journal.com/2007/022/sigma07-022.pdf) and
[Kanki, Proposition 4.1](https://arxiv.org/pdf/1209.1715), respectively;
they are not strengthened by inference here.

There is an additional scope warning. Any ordinary rational periodic
word with rational coefficient can be multiplied by a positive common
denominator $L$ so that both its coordinates and $L^3c$ are integers.
Thus a fixed-only theorem for the whole integral coefficient family
would also exclude all nonconstant ordinary rational cycles throughout
the rational coefficient family. The finite divisor computation does
not provide that genuinely global theorem. B1 stops without a second
or enlarged parameter census.

## 2. B2: bounded height, but no complete periodic core

Use the displayed rational map and its inverse
$$f_{a,b}^{-1}(x,y)=((x+a)/y-b,x).$$
A periodic word in the frozen domain has all $x_i\ne0$ and
$x_i+b\ne0$, with
$$ (x_i+b)x_{i+2}=x_{i+1}+a. \tag{1}$$
These restrictions matter: a cleared cyclic equation with both sides
zero can otherwise insert an indeterminate $0/0$ “cycle”. Blow-up or
singularity-continuation points are not added to the ordinary affine
periodic set.

### 2.1 The elementary uniform height bound

Let $A=|a|$, $B=|b|$ and $M=\max_i|x_i|$. If $M\le A$, the desired
bound is immediate. Otherwise choose $|x_i|=M>A$. Equation (1) gives
$$|x_{i-2}+b|M\le M+A<2M.$$
The factor is a nonzero integer, so it equals $\varepsilon=\pm1$.
Therefore
$$x_{i-2}=-b+\varepsilon,\qquad
  x_{i-1}=\varepsilon x_i-a.$$
One step earlier, the nonzero integer denominator implies
$$|x_{i-1}|\le |x_{i-2}+a|=|a-b+\varepsilon|.$$
It follows that every ordinary integral periodic coordinate satisfies
$$\boxed{|x_i|\le2|a|+|b|+1.} \tag{2}$$
This proves a finite graph exists for each parameter. It does not
classify the recurrent part of those graphs as parameters vary.

### 2.2 The one exact finite diagnostic

All 272 parameter pairs $-8\le a,b\le8$, $b\ne0$, were tested once,
using every legal integer coordinate in (2), every ordered pair and
every directed cycle. There was no period cutoff and no floating-point
rounding. The run examined 229,520 potential states, retained 34,997
edges, and found 71 fixed cycles and 16 native two-cycles. It found no
longer cycle within the declared sample. See
[b2_exact_probe.py](b2_exact_probe.py) and
[B2_EXACT_PROBE_OUTPUT.json](B2_EXACT_PROBE_OUTPUT.json).

Six nonfixed sampled cycles avoid the proposed section
$x+b\in\{-1,1\}$ entirely; for example $(a,b)=(-5,-4)$ with word
$(1,2)$. Consequently the maximum-coordinate argument cannot make
that section a global entrance theorem for all nonfixed cycles: when
$M\le|a|$, the argument supplies no entrance.

### 2.3 A hand-derived three-cycle family makes the gap concrete

For every integer $k\ge2$, set
$$b=2k,\quad a=-4k^2+k+2,\qquad
 (r,s,t)=(2k-1,-4k-1,-k-1). \tag{3}$$
The three instances of (1) follow from the explicit identities
$$
\begin{aligned}
(r+b)t&=(4k-1)(-k-1)=-4k^2-3k+1=s+a,\\
(s+b)r&=(-2k-1)(2k-1)=-4k^2+1=t+a,\\
(t+b)s&=(k-1)(-4k-1)=-4k^2+3k+1=r+a.
\end{aligned}
$$
Every coordinate is nonzero and the three denominators are
$4k-1,-2k-1,k-1$, all nonzero for $k\ge2$. The coordinates are
distinct, so the native period is exactly three. In particular
$$f_{-12,4}:(3,-9)\longmapsto(-9,-3)
\longmapsto(-3,3)\longmapsto(3,-9).$$
This is outside the finite parameter sample, and directly refutes any
attempt to upgrade that sample's observed periods $\{1,2\}$ to a
global conclusion. It does **not** refute the predeclared at-most-three
test hypothesis; that hypothesis remains unproved globally.
For $k\ge3$, every denominator in (3) has absolute value at least two,
so even this unbounded family of native three-cycles avoids the
unit-denominator section entirely.

This family was derived algebraically after the finite diagnostic, not
found by enlarging its parameter box. It is included as a proof of the
gap, not a replacement candidate consisting of a period-three table.
No claim is made that periods 1, 2 and 3 exhaust B2, or that higher
integral periods exist. The full question still requires either a
uniform recurrent-core description or an all-period exclusion theorem.

### 2.4 Classical subtraction and stopping point

Bedford--Kim already study this exact map. Their
[2006 Theorems 1 and 2](https://www.math.fsu.edu/~kim/periodicity.pdf)
classify global finite order/degree growth; their
[2009 paper](https://arxiv.org/pdf/math/0611297) supplies the
automorphism and invariant-curve mechanisms, and their
[periodic-orbit paper](https://arxiv.org/pdf/0709.4501) treats complex
isolated counts with multiplicity. None of these statements can simply
be relabeled as an integral-specialization classification.

Conversely, neither (2) nor (3) provides a substantial independent
replacement for that classification. The unresolved component contains
all cycles staying under the $|a|$ scale and avoiding the proposed
section. No parameter-uniform transition lemma for that component was
obtained. B2 therefore stops without another census or a shortened
period-specific replacement.

## 3. B3 stays a shallow, rejected extension

The source/local-collision screen considered
$$L_{d,c}(x,y)=(y,(y^d+c)/x),\quad d\ge3,\quad c\in\mathbb Z,$$
on the ordinary nonzero rational two-sided domain. Its most immediate
new-looking arithmetic observation is the same valuation mechanism
used by earlier NG2: at a negative minimum valuation $v_p(x_i)=r<0$,
$v_p(x_i^d+c)=dr$, but the two neighbors give
$v_p(x_{i-1}x_{i+1})\ge2r>dr$, a contradiction. Thus any rational
periodic coordinates would be integers. The remaining proposed route
is an integer maximum and a power-gap comparison.

This is too close to the already retained coefficient-free rank-two
small companion to justify a new deep slot on its own. No complete
all-$(d,c)$ classification was developed here, and none is claimed.
In particular B3 is rejected for insufficient distinct residual
substance, not by a claim that a located publication proves every
coefficient-forced case.

## 4. Delivery and reopen conditions

Only this new lane directory was written. No accepted contract,
CURRENT/global index, old artifact, Git state, manuscript, C-number,
evaluation label, external paid model or GPU was mutated/used.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.

Safe reopen conditions are mathematical, not numerical:

- B1 needs an actual all-parameter primitive-cycle lemma (or a coherent
  exhaustive replacement after a genuine counterexample), not more
  values of $c$ or a generic canonical-height heuristic.
- B2 needs a complete all-parameter core/period theorem accounting for
  the section-avoiding cycles, not merely the height bound, (3), or a
  larger coefficient rectangle.
- B3 needs a genuinely different global mechanism and enough residual
  substance after NG2 is deducted; changing a forcing coefficient or
  exponent does not meet that condition by itself.

The author recommends no admission from this lane. A separate current-
team, non-author review should check this refusal and its evidence; it
is not represented as already completed in this author report.
