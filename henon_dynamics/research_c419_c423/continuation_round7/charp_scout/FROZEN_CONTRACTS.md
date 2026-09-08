# Round-seven characteristic-p scout: three bounded questions

Frozen 2026-09-08 before the hand checks below are written and before any
mathematical program execution. These are AI-generated screening contracts,
not admissions. The source-derived Painlevé conjecture is expressly not a new
conjecture. Only this directory is writable by this delegate.

## P7 — finite-field q-Painlevé I uniform native periods

For every prime power $q$, $s,t_0\in\mathbb F_q^*$ and
$r=\operatorname{ord}_{\mathbb F_q^*}(s)$, use states
$\gamma=(j,x,y,t,s)$ with $t\in t_0\langle s\rangle$, and

$$
(j,x,y)\in\bigl(\{0\}\times(\mathbb F_q^*)^2\bigr)
\sqcup\bigsqcup_{j=1}^4\bigl(\{j\}\times\{0\}\times\mathbb F_q\bigr).
$$

Always update $t'=st$, $s'=s$. The remaining coordinates update as follows;
the rows exhaust the state set.

| Input condition | $(j',x',y')$ |
| --- | --- |
| $j=0$, $sx\ne y$ | $(0,t/(x-s^{-1}y),sx/y)$ |
| $j=0$, $sx=y$ | $(1,0,t/x)$ |
| $j=1$ | $(2,0,st(1-sy))$ |
| $j=2$ | $(3,0,sy)$ |
| $j=3$ | $(4,0,s(sy-t)/t)$ |
| $j=4$, $y\ne0$ | $(0,-s^2t/y,1)$ |
| $j=4$, $y=0$ | $(1,0,0)$ |

This is the state encoding of the initial-value surfaces in
[Joshi–Roffelsen v2, Definitions 2.1–2.2 and Algorithm 1](https://arxiv.org/html/2508.18578v2).
The torus alone is not the domain. The native clock is one displayed update;
the reduced period divides the native least period by $r$.

**Single question:** prove or disprove, for every allowed parameter and every
ordinary state, that its native least period $\ell$ satisfies

$$\ell/r\le q+1+2\sqrt q.$$

This is source Conjecture 1.2.A. Counts, if used, are distinct states fixed by
the native iterate; they are not fixed-scheme lengths, nor field-Frobenius
counts. No shift to generic fibres, small $r$, or torus-only orbits is allowed.

**Cheap gate:** determine exactly whether the proved monodromy invariant
already supplies an all-parameter genus-one fibration with the singular-fibre
control needed for this bound. A genus assertion still marked conjectural
must not be treated as a proof. No new finite-field enumeration is authorized.
**Replacement boundary:** park if the required fibration/singular-fibre
statement is absent and no new complete mechanism is available. An invariant
or a few checked orders cannot become a smaller paper.

## N7 — whether ordinary finite-field returns detect Nagata wildness

For every prime $p$, extension degree $e\ge1$, and $Q=p^e$, let
$\Delta=xz+y^2$ and let the integer polynomial map reduced over $\mathbb F_Q$ be

$$
\mathcal N(x,y,z)=(x-2y\Delta-z\Delta^2,\ y+z\Delta,\ z)
\quad\text{on }\mathbb F_Q^3.
$$

The native clock is one application of $\mathcal N$. The observable is
$N_{p,e}(n)=\#\operatorname{Fix}(\mathcal N^n|\mathbb F_Q^3)$ for every
$n\ge1$, hence its ordinary permutation zeta and complete cycle multiplicities.
No geometric fixed-scheme length is substituted: the polynomial map can have
positive-dimensional fixed loci.

**Single question:** does this entire family of ordinary return data
distinguish the Nagata map from tame polynomial automorphisms? A complete
negative answer requires an explicit tame comparator for every prime,
valid simultaneously over all its finite extensions and every native time.
This does not ask whether the original characteristic-zero Nagata map is tame.

**Cheap gate:** examine the algebraic family
$\mathcal N_a=(x-2ay\Delta-a^2z\Delta^2,y+az\Delta,z)$,
its composition law, and its fixed locus, with characteristic two separate.
No enumeration or computer algebra is authorized.
**Replacement boundary:** reject as a short classical-action reconstruction
if this gate supplies the full answer. No scheme-theoretic question may be
silently substituted to preserve a paper slot.

## R7 — all-ring temporal returns of reversible Rule 54

Fix characteristic two. For every $L\ge2$, the domain is
$X_L=\mathbb F_2^{2L}$ with all indices modulo $2L$. Define

$$\chi(a,b,c)=a+b+c+ac\quad\text{in }\mathbb F_2.$$

$E_L$ simultaneously replaces the even coordinate $x_i$ by
$\chi(x_{i-1},x_i,x_{i+1})$ and leaves odd coordinates unchanged;
$O_L$ updates the odd coordinates by the same rule and leaves the even ones
unchanged. The fixed map is $U_L=O_L\circ E_L$.

The native clock is one full even-then-odd sweep, not a half step or a spatial
shift. This is the reversible staggered rule, not the synchronous elementary
cellular automaton bearing the same number. The observable is

$$
A_L(n)=\#\operatorname{Fix}(U_L^n|X_L),\qquad
Z_L(u)=\exp\left(\sum_{n\ge1}A_L(n)u^n/n\right).
$$

All are ordinary Boolean configurations. The finite Boolean scheme obtained
by imposing $x_i^2=x_i$ is reduced; the unrelated ambient affine fixed scheme
is not the counted object.

**Single question:** obtain and prove an exact structural formula for
$A_L(n)$ for all $L\ge2,n\ge1$ from a complete soliton/scattering
classification, including colliding sectors and shorter-period stabilizers.
Listing the $2^{2L}$ configurations, taking the characteristic polynomial of
that full permutation, or an unbounded transfer matrix rewritten as a formula
does not satisfy the substantive target.

**Cheap gate:** separate closed-ring temporal spectra from stochastic-boundary
spectra and infinite-chain correlators in the owners; check whether conserved
left/right soliton numbers and their phase shifts actually give a complete,
bijective all-configuration parametrization. No census is authorized.
**Replacement boundary:** reject on insufficient Route-A arithmetic relevance
or park on missing complete parametrization. A unidirectional shift sector
must not replace the full question. This mechanism has only native
characteristic-two arithmetic, no variable-prime or target-Euler bridge.

## Shared exclusions and execution receipt

P7, N7 and R7 respectively test elliptic-fibration arithmetic, a nonlinear
finite additive action, and interacting reversible soliton scattering. They
are not degree-only variants of one map. The earlier exact fixed-word Markoff
question is a repository collision and is excluded before this freeze, not
counted as a fourth candidate.

Default execution budget remains zero mathematical programs, zero GPU/API
runs, zero old proof reruns, zero Git writes, zero manuscripts or admissions.
Any actual hand result and each source's access depth are reported separately.
