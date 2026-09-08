# Round 5: three characteristic-p mechanisms

Date: 2026-09-08. Source-first freeze, before any candidate computation.
This lane compares three mechanisms and deepens only CF1 and CF3. CF2
receives a direct-source ownership screen. No old programs or proof checks
are rerun. The three existing admissions M1, AS2 and IR1 are untouched.

## CF1 — a Kummer-trivialized semi-linear skew map

For every prime $p$ and every polynomial $a\in\mathbb F_p[x]$, including
zero and constants, define the single morphism

$$
F_a(x,y)=(x^p,y^p+a(x)y)
$$

on the entire $\mathbb A^2(\overline{\mathbb F}_p)$. Its native clock is
$F_a^n$, for every integer $n\ge1$. Let $N_a(n)$ count distinct geometric
fixed points, not scheme length. Let
$Z_a(t)=\exp(\sum_{n\ge1}N_a(n)t^n/n)$.

The full candidate theorem to prove or reject is:

1. Every fixed set is finite. Put $r=p^{v_p(n)}$ and
   $R_a(n)=\#\{x\in\mathbb F_{p^n}:a(x)\ne0,
   \operatorname{Norm}_{\mathbb F_{p^n}/\mathbb F_p}(a(x))=1\}$. Then
   $$N_a(n)=p^{2n}-(p^n-p^{n-r})R_a(n).$$
2. For the smooth affine curve
   $C_a^*=\{(x,t):t^{p-1}=a(x),\ t\ne0\}$,
   $(p-1)R_a(n)=\#C_a^*(\mathbb F_{p^n})$. The curve is empty when $a=0$;
   it need not be geometrically connected otherwise.
3. If $a=0$, then $Z_a(t)=(1-p^2t)^{-1}$. If $a\ne0$, every positive
   integer power of $Z_a$ has the circle $|t|=p^{-2}$ as a natural boundary
   for meromorphic continuation. In particular $Z_a$ is transcendental
   over $\mathbb C(t)$.
4. Actual primitive-cycle counts are
   $n^{-1}\sum_{d\mid n}\mu(n/d)N_a(d)$, without a clock change.

The arithmetic carrier is an actual finite Kummer cover of the Frobenius
base, not a fitted point-count table. Over that cover, $y=tz$ conjugates
the fiber dynamics to $z\mapsto z^p+z$. This is already a strong
classical-reconstruction risk. Deduct finite-field norm/root counts,
linearized-polynomial root multiplicities, the Weil bound for curves,
Bridy's additive-map zeta mechanism, and the repository's C404 all-$p$-tower
natural-boundary argument. Neither a new polynomial coefficient nor a
Kummer curve of higher genus by itself creates an independent paper.

The cheapest falsifiers are the zero-polynomial stratum, $p=2$, nonunit
fibers $a(x)=0$, constants with nontrivial norm, and inseparability of the
linearized fixed polynomial at $p\mid n$. All are analytic. Stop without
admission if the full statement is only a short composition of these
classical/owned mechanisms; do not relabel the count formula as the full
zeta theorem if the latter fails to close.

## CF2 — Laurent-series Hénon horseshoes (shallow source screen)

Let $K$ range over finite extensions of $\mathbb F_p((T))$, with $p$ odd,
and use its non-Archimedean absolute value. For every $b\in K^*$ and
$A\in K$ with $|A|>\max(1,|b|^2)$, define

$$H_{A,b}(x,y)=(A+by-x^2,x).$$

The domain is the entire ordinary $K^2$, not a chosen symbolic subset or
Berkovich extension. One application of $H_{A,b}$ is one clock step.
The complete target is the all-$n$ distinct $K$-point count and ordinary
zeta: $N(n)=2^n$, $Z(t)=(1-2t)^{-1}$ when $A$ is a square in $K$;
$N(n)=0$, $Z(t)=1$ otherwise.

Allen–DeMark–Petsche's arXiv:1610.04271v3 explicitly includes these local
fields. Its parameter region $\mathcal H_{\rm III}$, Theorem 1(a,e), and
Theorem 28 are the first ownership test. A periodic point has a bounded
two-sided orbit, so full filled-Julia coding would close the entire
ordinary domain. Stop at direct coverage; do not silently extend to
residue characteristic two, other parameter regions, or infer an Euler
factor from the binary-shift count. No proof construction or CPU screen
is planned for this branch.

## CF3 — ordinary geometric cycles of a compact Wehler automorphism

For each odd prime power $q$, let $X\subset\mathbb P^2\times\mathbb P^2$
over $\mathbb F_q$ be a smooth geometrically integral complete intersection
of bidegrees $(1,1)$ and $(2,2)$, with both coordinate projections finite
separable of degree two. Let $\sigma_x,\sigma_y$ be their deck
involutions and $f=\sigma_x\circ\sigma_y$. For the counting question,
include exactly the confined members: $\operatorname{Fix}(f^n)$ is
zero-dimensional for every $n\ge1$. This is an explicit parameter
condition, not a consequence being silently inferred from a complex
entropy calculation; no classification of the nonconfined members is
promised here.

Domain: all distinct geometric points $X(\overline{\mathbb F}_q)$,
including ramification points. Clock: the single fixed composition $f^n$,
not the whole involution group and not $f^n$ composed with Frobenius.
Observables: $N_X(n)=\#\operatorname{Fix}(f^n)$ and
$Z_X(t)=\exp(\sum_{n\ge1}N_X(n)t^n/n)$.

The full question is a rational/nonrational classification of $Z_X$ for
this complete confined class, supported by an all-$n$ ordinary-count
mechanism. The candidate assertion to test is that $Z_X$ is nonrational
for every such member. A Lefschetz/intersection-length formula alone,
an asymptotic, or a theorem proving merely infinitely many periods is
not closure. The arithmetic bridge is genuine surface cohomology plus
local arithmetic fixed-point multiplicities; no target correspondence
is inferred from their availability.

Deduct Hutz's general dynatomic cycles, multiplier/formal-period
restrictions, and Wehler applications, plus classical surface trace
formulas. The older NG3 question concerns all rational points of the
different affine Markoff-type $W_k$ family and one Coxeter word; that is
not this compact geometric ordinary-zeta problem. Nevertheless, changing
the base field alone is not the proposed increment: the missing item is
the complete multiplicity correction tower.

First falsifier: for a geometric periodic point defined over a finite
extension, an iterate of its tangent map is the identity. Establish
whether this forces nonreduced fixed schemes and rules out replacing
ordinary counts by the cohomological trace. Stop if the remaining
all-orbit/all-$p$-power multiplicities have no uniform closing theorem.
Do not reopen the exhausted one-variable W4 route, promote this helper
obstruction, or claim global literature openness from failed retrieval.

## Shared boundaries

Only this directory may be written. No CPU algebra/census, GPU, paid API,
legacy model override, external manuscript upload, C-number, manuscript,
global admission or Git action is part of this freeze. Proof/source
review is internal AI-assisted work, not human peer review.
NO_BAD_EULER_OR_ROOT_NUMBER remains unconditional.
