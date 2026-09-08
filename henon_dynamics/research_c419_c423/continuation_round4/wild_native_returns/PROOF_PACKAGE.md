# Wild native returns: proved obstructions and unclosed target

Date: 2026-09-08. This is an AI-assisted scouting proof package, not a
manuscript, an independent review or a new admission. The original scope
is in [FROZEN_CONTRACTS.md](FROZEN_CONTRACTS.md).

## Claim and status

The full target for $b_p(x)=x+x^{-p}$ on
$\mathbb P^1(\overline{\mathbb F}_p)$, for every odd prime $p$, is an
all-native-period ordinary geometric fixed-point formula and the
resulting zeta classification. Status: **NOT CURRENTLY JUSTIFIED**.

The auxiliary claims proved below are:

1. $b_3$ is a separable Lattès map, whereas $b_p$ is not dynamically
   affine for every $p\geq5$.
2. Every finite periodic return of $b_p$ has displacement equal to a
   $p$th power. Every generalized residue index defined in the cited
   Nordqvist framework vanishes there; the iterative residue also
   vanishes. Its nonzero-residue tower theorems cannot close this family.
3. For every divisor $r$ of $p+1$ with $2\leq r\leq p$, an explicit
   rotational family of true least-period-$r$ cycles has first-return
   multiplicity $p(r-1)$. Thus for **every** $p\geq5$ the shortcut that
   all finite primitive cycles have multiplicity $p$ is false.

Status of these auxiliary claims: **PROVABLE AS STATED**. They are
limited rejection/feasibility certificates, not the original full-count
theorem. No mathematical program was executed.

## Assumptions and notation

Let $p$ be odd, $k=\overline{\mathbb F}_p$, and $b=b_p$. The map acts on
all projective points. Composition is the clock. For a periodic point
$a$ and a return time $n$, $M_n(a)$ is the local order of $b^n-\mathrm{id}$,
computed in a local coordinate. It is not the ordinary count
$N_b(n)=\#\operatorname{Fix}(b^n)$.

For a tangent-to-identity germ $h(z)$, put
$q=\operatorname{ord}_z(h(z)-z)-1$. Its residue index is the coefficient
of $z^{-1}$ in $1/(z-h(z))$. In odd characteristic its iterative residue
is $(q+1)/2-\operatorname{ind}(h)$. Generalized indices below use the
exact definition in [Nordqvist, Definition 2.2](https://arxiv.org/html/1909.10782v3).

## Strategy and dependencies

The affine/non-affine boundary uses a direct elliptic lift, local degrees,
and the five-family classification in
[Bridy, §§2–5](https://arxiv.org/html/1306.5267v2). Local residue
obstructions are elementary Laurent-series calculations compared with
[Nordqvist–Rivera-Letelier, Theorem 2](https://arxiv.org/html/1904.04494v3)
and [Nordqvist, Theorems A/B and Corollary C](https://arxiv.org/html/1909.10782v3).
The explicit cycles use finite root-of-unity sums and formal Taylor
expansions, not a finite-field enumeration.

## 1. Structural boundary for $b_p$

The numerator $x^{p+1}+1$ and denominator $x^p$ are coprime, hence
$\deg b=p+1$. On $k^*$, $b'(x)=1$. At zero, in the target coordinate
$1/b$, the map is

$$\frac{x^p}{1+x^{p+1}},$$

so the local degree is $p$. At infinity the local map is

$$g(u)=\frac1{b(1/u)}=\frac{u}{1+u^{p+1}},\qquad u=1/x,$$

whose local degree is one. Thus zero is the unique critical point, and
it maps to the unramified fixed point infinity. In particular there is
no point of local degree $p+1$.

### 1.1. The characteristic-three lift

Over $\overline{\mathbb F}_3$, let $E$ be the smooth projective curve

$$E:\quad y^2=x^3-x$$

with origin $O$ at infinity. Its affine partial derivative with respect
to $x$ is nonzero. Its projective completion has a unique smooth point
at infinity, so this nonsingular cubic is an elliptic curve. Define

$$X=x+y^{-2},\qquad Y=y+y^{-3}.$$

In its function field, characteristic three gives

$$X^3-X=y^2+y^{-6}-y^{-2}
=y^2+2y^{-2}+y^{-6}=Y^2.$$

Consequently $(X,Y)$ defines a nonconstant rational map $E\dashrightarrow E$.
It extends across missing points because the source is a smooth
projective curve and the target is proper: apply the valuative criterion
to each source discrete valuation ring. At $O$, the function $y$ has
pole order three, while $y^{-3}$ vanishes, so $Y$ has a pole and the
extension sends $O$ to $O$. An origin-preserving elliptic morphism is a
group homomorphism.

The map $\pi:E\to\mathbb P^1$ defined by $y$ has degree three, since
its pole divisor is $3O$. It is separable: the equation for $x$ is
$x^3-x-y^2=0$ with $x$-derivative $-1$. The three automorphisms
$x\mapsto x+c$, $y\mapsto y$, for $c\in\mathbb F_3$, fix $O$ and
give its quotient group. The identity for $Y$ says

$$\pi\circ\psi=b_3\circ\pi.$$

Degree multiplicativity now gives $3\deg\psi=4\cdot3$, so
$\deg\psi=4$. This is prime to the characteristic; the isogeny is
separable. The diagram is therefore a Lattès realization, including
the quotient branch points. Its ordinary zeta classification is already
covered by Bridy's separable Lattès theorem; this small-prime case is
not a new contract.

### 1.2. Exclusion for every $p\geq5$

Every polynomial of degree at least two has a totally ramified fixed
point at infinity. A power map with either sign of the exponent has a
totally ramified point. These properties survive projective conjugacy.
The local-degree calculation above excludes both possibilities for $b_p$.
It therefore excludes the power, Chebyshev, additive and subadditive
families in Bridy's classification.

For a Lattès realization, use the defining quotient
$\pi:E\to E/\Gamma\simeq\mathbb P^1$ and affine isogeny $\psi$.
The elliptic automorphism orders listed in Bridy's §5 have only prime
factors two and three. Hence for $p\geq5$ the quotient is tame and
every $e_\pi(P)$ is prime to $p$. Degree multiplicativity gives
$\deg\psi=p+1$, so $\psi$ is separable; a separable isogeny is
unramified, as is its composition with a translation. Choose any point
$P$ above zero. Local-degree multiplicativity in the diagram would give

$$e_\pi(\psi(P))=e_b(0)e_\pi(P)=p\,e_\pi(P),$$

contradicting tameness of $\pi$. Thus $b_p$ is not dynamically affine
for every $p\geq5$. This excludes an existing theorem's hypotheses; it
does not prove nonrationality or establish global priority.

## 2. Exact return identity and the zero-residue obstruction

As rational functions, telescoping gives, for every $n\geq1$,

$$b^n(x)-x=\sum_{j=0}^{n-1}\frac1{b^j(x)^p}
=S_n(x)^p,\qquad S_n(x)=\sum_{j=0}^{n-1}\frac1{b^j(x)}. \tag{1}$$

Any finite periodic orbit avoids zero: a point reaching zero then
reaches infinity permanently. At a finite point $a$ with $b^n(a)=a$,
all summands defining $S_n$ are regular and $S_n(a)=0$. Since a map of
degree $(p+1)^n$ is not the identity, $S_n$ is not identically zero.
For $z=x-a$, the return germ is exactly

$$h(z)=b^n(a+z)-a=z+R(z)^p,\qquad
R(z)=S_n(a+z)=c z^m+O(z^{m+1}),\quad c\ne0. \tag{2}$$

Its multiplicity is $pm$ and $q=pm-1$. The congruent indices in
Nordqvist's Definition 2.2 are
$\ell_j=jp-1$, $1\leq j\leq m$. The corresponding Laurent series is

$$\frac{z^{q-\ell_j}}{z-h(z)}
=-\frac{z^{p(m-j)}}{R(z)^p}. \tag{3}$$

Every exponent in this series is a multiple of $p$; none is $-1$.
Thus **all** these generalized indices are zero, including the ordinary
residue at $j=m$. The iterative residue is $pm/2-0=0$ in $k$.

This gives the following precise applicability verdicts.

- If $m=1$, then $q=p-1$ satisfies the small-multiplicity range of
  Nordqvist–Rivera-Letelier's Theorem 2, but the required nonzero
  iterative residue fails. The germ is not $q$-ramified.
- If $m\geq2$, then $q=pm-1>p$. The second residue required by
  Nordqvist's Theorem A is zero. The first nonzero generalized index
  required by Theorem B does not exist among its admissible indices.
  Corollary C's nonzero iterative-residue condition also fails.
- The case $p\mid q$ mentioned alongside those theorems does not
  apply, since $q\equiv-1\pmod p$.

The same argument applies to every later return at the finite point,
not just its first return: $n$ was arbitrary in (1). These are failures
of specified classical sufficient/equivalent conditions, not a claim
that no possible ramification theory can handle the germs.

There is also no shortcut at infinity. The displayed germ $g$ satisfies

$$g(u)-u=-\frac{u^{p+2}}{1+u^{p+1}},\qquad
\frac1{u-g(u)}=u^{-p-2}+u^{-1}.$$

Therefore its initial multiplicity is $p+2$, its ordinary index is one,
and its iterative residue is $(p+2)/2-1=0$. Its second index, obtained by
multiplying the last Laurent series by $u^p$, is zero. The cited generic
and $q$-ramified criteria do not determine its full tower either.

## 3. A uniform, exact failure of constant primitive multiplicity

Fix $r\mid p+1$ with $2\leq r\leq p$. Let $\xi\in k$ have exact
order $r$, and choose $a\in k^*$ satisfying

$$a^{p+1}=\frac1{\xi-1}.$$

Such $a$ exists because $k$ is algebraically closed. For
$a_j=\xi^j a$, the divisibility $r\mid p+1$ gives

$$b(a_j)=a_j(1+a_j^{-(p+1)})
=a_j(1+a^{-(p+1)})=\xi a_j=a_{j+1}.$$

The $r$ points are distinct and $a_r=a$, so their native least period
is exactly $r$. This is a proof for all the stated primes and roots,
not an experiment at a few fields.

Every iterate has derivative identically one. Therefore for
$0\leq j<r$ its expansion at $a$ is

$$b^j(a+z)=a_j+z+O(z^p).$$

Taking reciprocals is valid since $a_j\ne0$. For each $0\leq k<p$,
the coefficient of $z^k$ in $S_r(a+z)$ is consequently

$$(-1)^k\sum_{j=0}^{r-1}a_j^{-k-1}
=(-1)^k a^{-k-1}\sum_{j=0}^{r-1}\xi^{-j(k+1)}. \tag{4}$$

For $0\leq k<r-1$ the root-of-unity sum vanishes: its ratio is
different from one and its geometric-series numerator is zero. At
$k=r-1$ the sum is $r$, which is nonzero in $k$ since $p\nmid r$.
Because $r-1<p$, all these coefficients lie inside the valid expansion.
Thus $S_r(a+z)$ has order exactly $r-1$. Equation (1) proves

$$M_r(a)=p(r-1). \tag{5}$$

Taking $r=(p+1)/2$ for every $p\geq5$ gives true least-period
$(p+1)/2$ cycles with

$$M_r(a)=\frac{p(p-1)}2>p.$$

This disproves the proposed constant-$p$ shortcut at **every** prime in
the non-dynamically-affine range. It does not classify other cycles,
and it does not compute the $p$-power repetition towers even of these
rotational cycles. Equation (5) is an auxiliary obstruction, not an
additional paper-sized result.

## 4. Why the two neighboring entries do not supply a second deep slot

For $c_p=x+x^{1-p}$, the identity $c_p=xH(x)^p$ with
$H=1+x^{-1}$ yields at every finite nonzero periodic point a return of
the form

$$h(z)-z=(a+z)T(z)^p.$$

This is exactly the local mechanism in
[the old multiplicative proof, §4](../../../continuation_c407_c408_round3/wild_ordinary/PROOF_PACKAGE.md).
Its proof uses only regularity and nonvanishing of $H$ along the cycle,
so the local calculation survives rational $H$. In particular its
nonzero residue is supplied by the extra factor $(a+z)^{-1}$, which is
absent in (3). The old theorem's global polynomial hypothesis must not
be silently deleted, nor does its local tower count the new primitive
cycles. This rational variant repeats that first-return bottleneck and
is not treated as an independently closed problem.

For $a_p=x^p+x^{-1}$, the precise missing data remain those in
[the third-round proof, Step A4](../../continuation_round3/positive_charp_new/PROOF_PACKAGE.md).
The freshly checked local theorems require a known first parabolic
return and nonzero residue conditions; they supply neither all-cycle
multiplier orders nor those first-return coefficients. No new mechanism
meeting its re-entry gate was found. Its old non-affinity and period-one
calculation are not rerun or counted as fourth-round progress.

## 5. Exact unclosed obligation and stopping decision

To close W4-B one still needs, for every $p\geq5$ and every native
$n$, the distribution of first-return orders of $S_n$ and the ensuing
zero-residue wild towers, including infinity. Even knowing all the
rotational cycles in §3 does not identify every primitive cycle.

The equation

$$N_b(n)=(p+1)^n+1-
\sum_{a\in\operatorname{Fix}(b^n)}(M_n(a)-1)$$

is an intersection-multiplicity bookkeeping identity, not a solution:
the defect distribution on its right remains unknown. Bridy's general
separable-map assertion is Conjecture 1.6 in the inspected preprint,
not a theorem available to fill that gap.

Disposition: W4-A `HOLD_NO_NEW_MECHANISM`; W4-B
`NOT_CURRENTLY_JUSTIFIED`; W4-C `REJECT_MECHANISM_REPEAT`. Zero new
admissions are recommended. No numerical expansion, finite-field census,
old program rerun, new manuscript or formal Route-A evaluation follows.
