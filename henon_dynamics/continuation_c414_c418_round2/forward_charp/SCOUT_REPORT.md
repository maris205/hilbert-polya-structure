# Native forward characteristic-p scout — second continuation

2026-09-07. This continues C414–C418 with three existing contracts frozen
and two substantive vacancies. This lane owns only `forward_charp/` in the
new continuation. It does not reopen the admitted degree-2p Hénon theorem,
re-run the old cubic fifth-iterate factorization, or overlap the coordinator's
independent Frobenius-clock question. No new contract is admitted here.

## Frozen questions and cheap stopping rules

The common convention is ordinary iteration of the stated map, never its
generic inverse-image tree. For a map over $\mathbb F_q$, write $N_n$ for
the number of distinct geometric fixed points of its $n$th iterate and
$M(n,r)$ for those fixed points rational over $\mathbb F_{q^r}$. The two
positive integers $n,r$ remain independent. Local fixed-point multiplicity
means the order of $f^n(z)-z$ in a local coordinate, not the local degree
of the map itself. The source zeta convention is
$\exp(\sum_{n\ge1}N_n t^n/n)$.

| Contract | Exact whole family and domain | Proposed mechanism and complete question | Cheap decisive boundary |
|---|---|---|---|
| F1: reopened wild cubic | Every $q=3^s$, $s\ge1$, every $a\in\mathbb F_q^*$; $f_a=x^3+ax^2$ on $\mathbb A^1(\overline{\mathbb F}_3)$ | Use the fixed finite critical point, first-return multipliers and ramification numbers to classify every periodic cycle's local multiplicity and derive all $N_n,M(n,r)$. | Compute the fixed-point multiplier parameter map and test the actual local-ramification theorem's hypotheses. A PCF label or a longer factorization list is not closure. |
| F2: nonadditive étale polynomials | Every odd $p$, every finite $\mathbb F_q$ of characteristic $p$, every $m\ge2$ with $p\nmid m$, and every degree-$m$ polynomial $P\in\mathbb F_q[x]$; $F_P=x+P(x)^p$ on the affine line | All multipliers are one; replace the multiplier-order problem by an exact global trace-polynomial/ramification classification and derive all ordinary counts and finite-extension returns. | Prove the exact inseparable factor of $F_P^n-x$ for every $n$, then determine whether its remaining roots are uniformly simple. Constant derivative alone is insufficient. |
| F3: one wild critical point with a pole | Every odd $p$, every finite $\mathbb F_q$ of characteristic $p$, every $a\in\mathbb F_q^*$; $R_a=x^p+a/x$ on the entire projective line | Use the single fixed wild critical point at infinity, explicit pole structure and local return germs to obtain all $N_n,M(n,r)$ and multiplicities. | Compute the fixed-point multiplier parameter map and the parabolic residue. A moduli/continued-fraction classification or the count with scheme multiplicity is not the desired theorem. |

These are one reopened question and two different-family screens, not
three paper numbers. F2 is a one-dimensional separable forward problem,
not a support subcase of the admitted Hénon resonance result. The fresh
repository collision check nevertheless found that its quadratic-$P$
subfamily and its general telescoping identity were already screened in
earlier rounds. F3 is rational with a genuine pole, but its $a=1$ map is
also the old PSL inverse-tower companion's source. Changing its clock to
native forward return would require a new complete theorem; neither
enlarging parameters nor relabeling that clock supplies an increment.

## F1: the PCF reopening has a precise limitation

Over $\overline{\mathbb F}_3$, PCF by itself supplies no special finiteness:
a map's coefficients and any algebraic point lie in some finite extension,
and that finite projective set is forward invariant. Every point is
preperiodic. The stronger fact here is $f_a'(x)=-ax$, so the only finite
critical point is zero and it is fixed. Infinity is also fixed, with wild
local degree three. At zero, the local degree of $f_a^n$ is $2^n$, but
the fixed-point intersection multiplicity is **one**, since the derivative
of $f_a^n-x$ there is $-1$. These two multiplicities must not be conflated.

For a nonzero fixed point $\alpha$,

$$\alpha^2+a\alpha-1=0,\qquad\lambda=f_a'(\alpha)=-a\alpha,$$

so

$$\lambda^2-a^2\lambda-a^2=0. \tag{F1.1}$$

Conversely, every $\lambda\in\overline{\mathbb F}_3\setminus\{0,-1\}$
is realized by choosing $a^2=\lambda^2/(\lambda+1)$ and
$\alpha=-\lambda/a$. All these quantities lie in a finite extension.
Thus even fixed points in this critically fixed family realize unbounded
orders of roots of unity as the allowed coefficient field varies. A finite
critical portrait does not imply a uniformly bounded list of multipliers.
This excludes that shortcut, not the possibility of a theorem using an
unbounded but explicitly controlled arithmetic parameter.

The discriminant of the nonzero fixed-point quadratic is $a^2+1$.
Consequently $N_1=3$ unless $a^2=-1$, when $N_1=2$. The latter case
occurs over even-degree extensions of $\mathbb F_3$ and has the nonzero
fixed point $\alpha=a$. Its exact germ is

$$f_a(a+z)-a=z+az^2+z^3. \tag{F1.2}$$

The published minimal-ramification criterion does apply to this particular
germ: its first lower ramification number is one, and its iterative residue
is $1-1/a^2=2\ne0$. Hence its multiplicity in $f_a^n-x$, for
$n=3^e s$ with $3\nmid s$, is $(3^{e+1}+1)/2$. This is a direct
application to one fixed-point stratum, not an independent paper or a
classification of all first-return germs. Source access and the exact
criterion are recorded in `SOURCE_AUDIT.md`.

For a general nonzero cycle $C$ of least period $\ell$,

$$\lambda_C=(-a)^\ell\prod_{x\in C}x\ne0.$$

Let $r_C$ be its multiplicative order and $G_C$ its local first-return
germ. If $n=\ell m$ and $r_C\nmid m$, the local fixed-point
multiplicity is one. Otherwise it is

$$1+i_{v_3(m/r_C)}(G_C^{r_C}),\qquad
i_e(G)=\operatorname{ord}_z(G^{3^e}(z)-z)-1.$$

Iteration by the remaining factor prime to three leaves the first nonzero
order unchanged. This exact reduction identifies what is missing: a
classification of these ramification sequences, the number of cycles with
each such datum, and their Frobenius actions. Neither the two-point critical
portrait nor the generic inverse Galois group supplies that classification.
The previously certified $a=1,n=5$ example is inherited without rerunning it.

## F2: constant derivative removes multiplier variation, not multiplicities

Put $D=pm$. The identity $F_P'=1$ makes every periodic multiplier one.
For every positive $n$, telescoping gives the exact polynomial identity

$$F_P^n(x)-x=A_n(x)^p,\qquad
A_n(x)=\sum_{j=0}^{n-1}P(F_P^j(x)). \tag{F2.1}$$

Moreover

$$\deg A_n=mD^{n-1},\qquad
A_n'(x)=\sum_{j=0}^{n-1}P'(F_P^j(x)),\qquad
\deg A_n'=(m-1)D^{n-1}. \tag{F2.2}$$

The last degree follows because $p\nmid m$ and the final summand has
strictly larger degree than all the others. Thus $A_n'\ne0$: the global
inseparable exponent of $F_P^n-x$ is exactly $p$ at **every** time, not
an inferred finite prefix. It does not follow that $A_n$ is squarefree.
The ordinary count is $\deg\operatorname{rad}(A_n)$, and replacing this
by $D^n/p$ discards the additional local multiplicities.

An exact cheap subcheck uses $P=x^2+c$ for every odd characteristic.
Then $N_1=2$ for $c\ne0$ and $N_1=1$ for $c=0$. Set $H=x^2+c$,
$F=x+H^p$ and $S=x+F$. For $n=2$,

$$A_2=2H-2xS+S^2,\qquad A_2'=2S.$$

At a common zero, $S=H=0$, forcing $x=c=0$. Hence $A_2$ is squarefree
for $c\ne0$; for $c=0$, its only repeated root is zero, of multiplicity
two. It follows that $N_2=4p$ for $c\ne0$ and $N_2=4p-1$ for $c=0$.
This is symbolic all-characteristic algebra, not a finite-field census.
It demonstrates both the exact global factor and the additional root
defect within the whole family.

At any periodic point, the first-return difference is a $p$th power by
(F2.1), so its first nonlinear order is at least $p$. In particular its
first lower ramification number is at least $p-1>1$, although its
multiplier order is one. Thus the generic minimal-ramification criterion
requiring first lower number one is inapplicable to **every** such germ.
An all-period trace-root and ramification theorem beyond (F2.1)–(F2.2)
has not been established. Moreover, (F2.1) and the derivative identity in
(F2.2) already occur in the repository's earlier nonaffine-characteristic-p
rejection proof. The degree-leading-term observation and two-step quadratic
check do not turn that inherited reduction into a new paper.

In characteristic $p$, a future radical computation must also not identify
$\operatorname{rad}(A_n)$ with $A_n/\gcd(A_n,A_n')$ without treating
factors of multiplicity divisible by $p$ separately. The latter quotient
can omit such a factor entirely.

## F3: wild unicriticality does not bound noncritical multipliers

The map $R_a$ is separable, has degree $p+1$, and has no finite critical
point: on $x\ne0$ its derivative is $-a/x^2$, while its simple pole at
zero is unramified in the target coordinate $1/R_a$. Infinity is its
single critical point, is fixed, and has local degree $p$. It contributes
one ordinary and simple fixed point to every positive iterate. Zero maps
to infinity and is not periodic. The fixed-point scheme on the projective
line has length $(p+1)^n+1$; this is not its ordinary point count.

For a nonzero finite fixed point $\alpha$,

$$a=\alpha^2-\alpha^{p+1},\qquad
\lambda=-a/\alpha^2=\alpha^{p-1}-1. \tag{F3.1}$$

Every $\lambda\ne0,-1$ is realizable over some finite extension by
choosing $\alpha^{p-1}=\lambda+1$ and $a=-\lambda\alpha^2$.
Consequently, a single fixed wild critical point also permits unbounded
fixed-point multiplier orders. Its known continued-fraction/moduli
classification is not a forward-cycle classification.

For $\lambda=1$, choose $\alpha^{p-1}=2$, $a=-\alpha^2$. The local
germ has quadratic coefficient $-1/\alpha$. For $p\ge5$, its cubic
coefficient is $1/\alpha^2$, so its iterative residue is zero: this
explicit critically fixed stratum is **not** minimally ramified. In
characteristic three there is also the cubic Frobenius term; the residue
instead equals $-\alpha^2=1$, which is nonzero. These exact coefficient
facts are an adversarial test of the proposed mechanism, not an all-cycle
result. The full native-return theorem remains unproved.

## Actual cheap-check receipt

One new symbolic local-jet command was executed. It checks (F1.2) through
degree five over the exact quotient $\mathbb F_3[a]/(a^2+1)$; no large
iterate polynomial or finite-field orbit census is involved. The actual
command was:

```bash
python -B -c 'import sympy as s; z,a=s.symbols("z a"); modulus=s.Poly(a*a+1,a,modulus=3); trunc=lambda f: s.Add(*(s.rem(s.Poly(s.expand(f).coeff(z,k),a,modulus=3),modulus).as_expr()*z**k for k in range(6))); g=z+a*z*z+z**3; h=z; h=trunc(h+a*h*h+h**3); h=trunc(h+a*h*h+h**3); h=trunc(h+a*h*h+h**3); print("parabolic cubic third-iterate jet modulo (3,a^2+1,z^6):",s.expand(h-z)); assert s.expand(h-z)==-z**5'
```

Actual stdout:

```text
parabolic cubic third-iterate jet modulo (3,a^2+1,z^6): -z**5
```

Exit status: 0. This verifies the first $3$-power step of the cited
fixed-germ stratum, not the all-cycle theorem. The all-$e$ statement comes
from the applicable classical theorem, not this finite check. The command
was not rerun. Old $n=5$ cubic factors, old derivative-one jets and all
sealed checks were not executed. F2/F3's displayed reductions are direct
symbolic calculations, not claimed computer-verification outputs.

## Final bounded disposition

All three whole-family forward-count questions are **NOT CURRENTLY
JUSTIFIED**. No complete new proof package, paper number or admission is
produced. F1's PCF reopening and F3's unicritical replacement fail the
bounded-multiplier shortcut; F2 gives a useful all-period inseparable-factor
identity, but its root radicals and higher local multiplicities remain
unclassified. These statements do not claim the questions are globally
open or impossible, and do not count the short established reductions as
new papers.

The bounded primary-source and repository comparison is complete in
[SOURCE_AUDIT.md](SOURCE_AUDIT.md). All three frozen questions stop at
their stated boundary; no fourth family, larger factor table, manuscript,
formal evaluation or global-state mutation is undertaken by this lane.
All source-system statements remain separate from target Euler factors,
root numbers, automorphy, zero/divisor correspondence and Hilbert–Pólya
claims.
