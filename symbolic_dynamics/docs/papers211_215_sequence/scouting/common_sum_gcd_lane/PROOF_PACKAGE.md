# Proof package: valid deductions and an unclosed conjunction

## Claim and status

For exactly the map in `INTAKE.md`, the normalization, fixed/recurrent set,
generic height bound, unbounded-depth construction and inverse identity
below are **PROVABLE AS STATED**. A sharp general $M$-clock, a pointwise
basin/endpoint classification, and an independently evaluated all-target
image or fibre extremum are **NOT CURRENTLY JUSTIFIED**.

This is author mathematics, not an independent review or a paper admission.
Root contributed the literal, gcd preservation, first-step pairwise gcd
normalization, the fixed-point lead and the depth-four witness. The lane
author completed the proofs, gave the CRT unbounded-depth construction and
the explicit inverse-boundary counterexample.

## Assumptions, notation and strategy

Let $M\ge1$ be an integer and $(a,b,c)\in X_M$. Set $g=\gcd(a,b,c)$.
Let $h(a,b,c)$ be the least nonnegative iterate at which the orbit is fixed,
and let $H(M)=\max_{x\in X_M}h(x)$. For a positive integer $n$, let
$\Omega(n)$ count prime factors with multiplicity, with $\Omega(1)=0$.

Dependency map: gcd identities give normalization and divisor descent;
descent gives fixed-only recurrence; Egyptian denominators give the complete
fixed list. Independently, a two-coordinate invariant slice and elementary
CRT build exact predecessors of arbitrary depth. A final total-sum slicing
identity records exactly what the inverse desk did and did not evaluate.
All numeric witnesses are hand arithmetic, not software experiments.

## 1. Normalization and generic termination

Write $(a',b',c')=T(a,b,c)$ and $S=a+b+c$. Associativity of gcd gives

$$\gcd(a',b')=\gcd(a,b,S)=\gcd(a,b,c)=g.$$

The same calculation applies to the other two pairs, so all three new
pairwise gcds equal $g$, and the common gcd is preserved. Homogeneity gives

$$T(ga,gb,gc)=gT(a,b,c).$$

Thus division by the initial $g$ is a fixed change of scale, not a moving
normalization; after the first step the normalized coordinates are pairwise
coprime. Every coordinate divides its predecessor. Whenever the state is
not fixed, at least one positive coordinate becomes a proper divisor.
Consequently the nonnegative integer potential

$$\Omega(a/g)+\Omega(b/g)+\Omega(c/g)$$

strictly decreases outside fixed points. This proves termination and

$$h(a,b,c)\le\Omega(a/g)+\Omega(b/g)+\Omega(c/g)
\le 3\left\lfloor\log_2(M/g)\right\rfloor.$$

The estimate is not claimed sharp. A periodic orbit cannot include a strict
coordinate decrease, so the recurrent states are exactly the fixed states.
For a primitive input, the three output coordinates are pairwise coprime
and each divides $S$, hence their product divides $S$. This is a useful
contraction constraint, not an evaluated worst-case clock.

Primewise independence is false as a state description. At prime $3$,
$(3,2,1)$ and $(3,2,5)$ both have valuation vector $(1,0,0)$, but their
first output coordinates are respectively $3$ and $1$. The units in the
other coordinates matter; a sliding minimum of valuations does not describe
this map.

## 2. Complete fixed set, with the classical object deducted

A primitive positive triple $(r_1,r_2,r_3)$ is fixed exactly when every
$r_i$ divides $R=r_1+r_2+r_3$. Set $u_i=R/r_i$. Each $u_i$ is an integer
at least two and

$$\frac1{u_1}+\frac1{u_2}+\frac1{u_3}=1.$$

Sort the denominators as $2\le u\le v\le w$. The equation implies
$1\le3/u$, so $u\le3$. If $u=3$, both remaining reciprocals are at most
$1/3$, and equality forces $v=w=3$. If $u=2$, then
$1/v+1/w=1/2$. Positivity excludes $v=2$, and $1/2\le2/v$ gives
$v\le4$. The two remaining cases yield $(v,w)=(3,6)$ or $(4,4)$.
Thus the denominator triples, up to permutation, are precisely

$$(3,3,3),\qquad(2,3,6),\qquad(2,4,4).$$

Because every $u_i$ divides $R$,
$\gcd(R/u_1,R/u_2,R/u_3)=R/\operatorname{lcm}(u_1,u_2,u_3)$.
Primitivity therefore forces $R=\operatorname{lcm}(u_1,u_2,u_3)$.
Recovering the $r_i$ gives exactly the permutations of

$$(1,1,1),\qquad(1,1,2),\qquad(1,2,3).$$

Each displayed triple directly satisfies the fixed equations. Restoring
the arbitrary preserved gcd gives all fixed states of $X_M$. Their number is

$$|\operatorname{Fix}(T)|
=M+3\lfloor M/2\rfloor+6\lfloor M/3\rfloor.$$

At $M=1$ there is only $(1,1,1)$ and $H(1)=0$.

This is the already-established arithmetical-structure object on $K_3$.
The exact general static definition and Egyptian correspondence are in
Harris–Louwsma, Introduction, Eqs. (1)–(2); see `SOURCE_AND_COLLISION.md`.
The elementary three-denominator classification and its scale count are
deducted background, not a new fixed-point enumeration primitive.

## 3. Exact arbitrary-depth predecessor construction

The slice $(2,b,c)$ with $b,c$ odd is invariant in its first coordinate,
and its remaining update is

$$K(b,c)=\bigl(\gcd(b,c+2),\gcd(c,b+2)\bigr).$$

**Predecessor lemma.** Suppose $b,c$ are odd, $\gcd(b,c)=1$ and
$c\mid b+2$. There are arbitrarily large odd integers $k$ such that

$$K(b,ck)=(b,c),\qquad \gcd(b,ck)=1,\qquad b\mid ck+2.$$

*Proof.* Put $q=(b+2)/c$. Both $b$ and $q$ are odd, and
$\gcd(b,q)=1$: any common divisor divides both $b$ and $b+2$, hence divides
$2$. Since $c$ is invertible modulo $b$, the congruence
$ck\equiv-2\pmod b$ has a solution. For $b=1$ this is the vacuous
congruence. By the Chinese remainder theorem the simultaneous conditions

$$ck\equiv-2\pmod b,\qquad k\equiv1\pmod q,
\qquad k\equiv1\pmod2$$

have an arithmetic progression of solutions, because $b,q,2$ are pairwise
coprime. This includes arbitrarily large positive $k$. Then

$$\gcd(ck,b+2)=c\gcd(k,q)=c,\qquad
\gcd(b,ck+2)=b.$$

Moreover $\gcd(b,k)=1$ since a common divisor would divide $2$ and the
odd number $b$; together with $\gcd(b,c)=1$ this yields
$\gcd(b,ck)=1$. The final divisibility is the first congruence. ∎

Choose $k>1$ large enough that $ck>b$. The divisibility orientation has
reversed: the old $b$ now divides $ck+2$. The lemma may therefore be applied
again with the two coordinate roles exchanged. The symmetry of the fixed
map $K$ justifies this exchange in the construction; the forward map is
unchanged and has no scheduler. Alternating the construction gives a
strictly increasing sequence of exact predecessor triples.

Start with the fixed triple $(2,1,1)$, to which the lemma applies. Each
new triple is distinct from its target, and its image is that target. If
the target has depth $j$, the source has depth exactly $j+1$. Therefore,
for every integer $r\ge0$, there is a finite positive triple with first
coordinate $2$ and depth $r$. Taking $M$ to be its largest coordinate places
the entire descending orbit inside $X_M$. It follows that

$$\sup_{M\ge1}H(M)=\infty.$$

This disproves every universal constant clock, not just a four-step guess.
It does **not** evaluate $H(M)$, establish an asymptotic rate, classify all
basins or provide an all-target inverse atlas.

For a concrete hand check extending the root witness,

$$(2,123,6025)\to(2,123,25)\to(2,3,25)\to(2,3,5)
\to(2,1,5)\to(2,1,1).$$

Indeed $6027=49\cdot123$ and
$\gcd(6025,125)=25$; the following first new values use
$\gcd(123,27)=3$, $\gcd(25,5)=5$, $\gcd(3,7)=1$ and
$\gcd(5,3)=1$. The other coordinates stay as shown. The terminal triple
is fixed, and all prior states differ from their successors, so this depth
is exactly five. No code evaluated this witness or any larger cube.

## 4. Short inverse desk: exact encoding, no independent axis

For fixed positive integers $S,M,d$, define

$$A_{d,S,M}(z)=
\begin{cases}
\displaystyle\sum_{\substack{1\le q\le\lfloor M/d\rfloor\\
\gcd(q,S/d)=1}}z^{dq},&d\mid S,\\
0,&d\nmid S.
\end{cases}$$

For any target $(x,y,z_0)\in X_M$ the exact coefficient identity is

$$|T^{-1}(x,y,z_0)|=
\sum_{S=3}^{3M}[z^S]\,
A_{x,S,M}(z)A_{y,S,M}(z)A_{z_0,S,M}(z).$$

To prove it, condition a source on its total $S$. A coordinate $a$ has
$\gcd(a,S)=d$ exactly when $a=dq$ with the bounds and coprimality appearing
in $A_{d,S,M}$. Multiplication chooses the three coordinates, and the
coefficient enforces their total. Distinct totals cannot count a source
twice. This is generic reduced-residue slicing and coefficient extraction,
not an evaluated image or extremum theorem.

The necessary first-step pairwise-gcd condition is not sufficient for a
target to lie in the same bounded cube's image. For $M=3$, the primitive
target $(1,1,3)$ satisfies that condition but has no source. A source must
have $c=3$ and total $S$ divisible by $3$. The possibility $S=3$ leaves
$a+b=0$; $S=6$ forces $(a,b)=(1,2)$ or $(2,1)$, whose even coordinate has
gcd $2$ with $S$; $S=9$ forces $(a,b)=(3,3)$. All fail.

## Corrections, missing claims and stop

No constant upper bound was adopted as a theorem; the original hand depth
four did not justify one. The CRT result decisively rules out that direction.
Neither the displayed inverse expression nor the special backward family
supplies a general image criterion, evaluated maximum fibre or a materially
separate all-target contribution. The all-$M$ sharp clock and full basin
identification also remain open in this desk.

Disposition: **NO_PROMOTION / ZERO_RESERVES**. Stop without the optional
pilot. The valid deductions remain negative evidence; they do not exhaust
gcd dynamics or arithmetical structures and are not a manuscript acceptance.
