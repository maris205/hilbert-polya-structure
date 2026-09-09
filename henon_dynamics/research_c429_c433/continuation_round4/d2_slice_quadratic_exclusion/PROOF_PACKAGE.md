# Proof Package: the exact local quadratic obstruction

2026-09-09 UTC. R4 D2. First-pass and rounds 2–3 inputs are
read-only. No mathematical program is used.

## Claim

For the actual complete higher native-coordinate splitting fields
$M_n/K$ on $\Sigma=\{A=B=0\}$, where $K=\mathbb Q(C,D)$, prove

$$
\tag{ST}
K(\sqrt{D^2-C^2})\not\subseteq M_3\cdots M_N
\qquad\text{for every finite }N\ge3.
$$

One whole right-to-left word $T=s_zs_ys_x$ remains the native tick.
The separate geometric question extends constants to
$\overline{\mathbb Q}$. Accepted R3 proves ST is sufficient for
the original SF2 question; the converse is not assumed.

## Status

**NOT CURRENTLY JUSTIFIED** for ST and original SF2.

Propositions 1–5 below are complete auxiliary statements. Proposition
2 gives a sufficient extra hypothesis for ST, not a proof that the
actual Fricke covers satisfy it. Propositions 4–5 are explicitly
non-Fricke controls: they disprove certain proposed implications
from local group or sign information, not ST.

## Assumptions and notation

The following accepted inputs are used without reproving them.

- R3 Proposition 1 identifies the actual restricted cycle-sign class
  as $[D^2-C^2]$.
- R3 Proposition 3 defines $M_n$ through specialization of the
  complete generic exact-$n$ coordinate cover. It supplies the
  one-way transfer to SF2. No subset of local periodic branches is
  substituted for that cover.
- R3 Proposition 4 gives, for odd $n\ge3$, the commuting involution
  $g(x,y,z)=(-x,-y,z)$ on this complete specialized point set.
  The action of $h=gT$ is free of order $2n$, with
  $h^n=g$ and $h^{n+1}=T$.
- The accepted count gives $\nu_n=|P_n|$ and
  $s_n=\nu_n/(2n)\ge2$ for odd $n\ge3$. The controls in Proposition
  4 can therefore match the accepted number of points and free
  $h$-orbits. This does not make them Fricke coordinate covers.

Set $\kappa=\mathbb Q(C)$. For $\varepsilon\in\{1,-1\}$ let
$v_\varepsilon$ be the valuation of $K$ at $D-\varepsilon C$ and put

$$
t=D-\varepsilon C,\qquad
a_\varepsilon=2\varepsilon C,\qquad
R_\varepsilon=\kappa[[t]],\qquad
F_\varepsilon=\kappa((t)).
$$

The embedding of $K$ in $F_\varepsilon$ sends $D$ to
$\varepsilon C+t$. Fix a compatible embedding of a separable
closure of $K$ in a separable closure of $F_\varepsilon$. Define

$$
E_{n,\varepsilon}=F_\varepsilon M_n.
$$

Write the joint field of the first finitely many higher layers as

$$
H_{N,\varepsilon}:=E_{3,\varepsilon}\cdots E_{N,\varepsilon}.
$$

Each $E_{n,\varepsilon}/F_\varepsilon$ and
$H_{N,\varepsilon}/F_\varepsilon$ is finite Galois because each
$M_n/K$ is a splitting field. They are the chosen completed local
factors of the *whole* splitting fields, not one point's field.
Different choices of place give isomorphic local Galois extensions,
so the conditions used below are independent of that choice.
These fields exist even at bad reduction; no étaleness at
$v_\varepsilon$ is being assumed.

For a finite extension of complete discrete valuation fields,
$e(E/F)$ denotes its ramification index. For a finite Galois
extension, $I(E/F)$ denotes its inertia group. Every residue
characteristic in this package is zero.

## Strategy and dependency map

1. Compute the exact local target, retaining its residue-unit class.
2. Use characteristic-zero cyclic inertia on full splitting fields
   to prove the finite-compositum oddness criterion.
3. Classify all quadratic subfields of any one complete joint field,
   including the residual-unit ambiguity.
4. Test the inherited symmetry/sign information against explicit
   finite flat normal models with opposite target-containment
   answers.
5. Keep arithmetic and geometric local exclusions separate.

The external local-algebra input is the Stacks Project's
[Section 15.113](https://stacks.math.columbia.edu/tag/0EXQ) for
ramification indices and henselian degree formulas, and
[Lemma 15.114.5](https://stacks.math.columbia.edu/tag/09EE) for cyclic
inertia in residue characteristic zero. The statements and proofs
were read. Tame base-change/compositum context was also checked in
[Lemma 15.116.7](https://stacks.math.columbia.edu/tag/0EXW) and
[Lemma 15.116.8](https://stacks.math.columbia.edu/tag/0EXX).
These are classical local-algebra facts, not new results or a source
of Fricke-specific inertia information.

## Proposition 1. Exact local target, not just parity

For either $\varepsilon$, there is a canonical decomposition after
choosing $t$,

$$
F_\varepsilon^\times/F_\varepsilon^{\times2}
\simeq
\bigl(\kappa^\times/\kappa^{\times2}\bigr)\oplus\mathbb F_2,
\qquad
[u t^m]\longmapsto([\bar u],m\bmod2),
\tag{1}
$$

where $u\in R_\varepsilon^\times$ and $\bar u$ is its residue.
Under this decomposition,

$$
[D^2-C^2]=[a_\varepsilon t].
\tag{2}
$$

The class $[a_\varepsilon]$ is nontrivial in
$\kappa^\times/\kappa^{\times2}$ and remains nontrivial in
$\overline{\mathbb Q}(C)^\times/
\overline{\mathbb Q}(C)^{\times2}$.

### Proof

Every nonzero Laurent series is uniquely $t^m u$ with $m\in\mathbb Z$
and $u$ a unit. The unit $u/\bar u$ has residue one. The polynomial
$X^2-u/\bar u$ has a simple root $1$ modulo $t$, because $2$ is
invertible. Hensel lifting in the complete ring gives a square root
of $u/\bar u$. Thus the squareclass is represented by $\bar u t^m$.

A square has even $t$-valuation. If a constant unit in $\kappa^\times$
is a square in $F_\varepsilon$, its square root has valuation zero,
and reduction makes that constant a square in $\kappa$. These
observations prove both injectivity and surjectivity in (1).

Substitute $D=\varepsilon C+t$:

$$
D^2-C^2=t(2\varepsilon C+t)
=a_\varepsilon t(1+t/a_\varepsilon).
$$

The last factor is a square by the same Hensel argument, proving
(2). Finally $2\varepsilon C$ has odd valuation at $C=0$ in both
$\mathbb Q(C)$ and $\overline{\mathbb Q}(C)$. It cannot be a square
in either residue field. Extending the field of constants therefore
does not remove this functional unit class. $\square$

## Proposition 2. A whole-cover odd-inertia bridge

For every finite $N\ge3$ and either $\varepsilon$,

$$
e(H_{N,\varepsilon}/F_\varepsilon)
=
\operatorname{lcm}_{3\le n\le N}
e(E_{n,\varepsilon}/F_\varepsilon).
\tag{3}
$$

Consequently the following actual all-layer hypothesis is sufficient
for ST:

$$
\tag{OI}
\text{For one fixed }\varepsilon\in\{1,-1\},
\quad e(E_{n,\varepsilon}/F_\varepsilon)\text{ is odd for every }n\ge3.
$$

The same statement with constant field $\overline{\mathbb Q}$ is a
sufficient condition for geometric ST. Neither version of OI is
asserted for the actual Fricke tower here.

### Proof

Fix $\varepsilon,N$ and abbreviate $H=H_{N,\varepsilon}$ and
$F=F_\varepsilon$. The complete valuation on $F$ has a unique
extension to each finite field in question. By the cited
characteristic-zero inertia theorem, $I(H/F)$ is cyclic of order
$e(H/F)$, and $I(E_{n,\varepsilon}/F)$ is cyclic of order
$e(E_{n,\varepsilon}/F)$.

The restriction map sends $I(H/F)$ into
$I(E_{n,\varepsilon}/F)$. Its kernel is exactly the relative inertia
$I(H/E_{n,\varepsilon})$: both conditions say the automorphism fixes
$E_{n,\varepsilon}$ and acts trivially on the residue field of $H$.
The relative extension is Galois. Ramification indices multiply
in the tower, so the kernel has order
$e(H/F)/e(E_{n,\varepsilon}/F)$. The image therefore has the full
order of $I(E_{n,\varepsilon}/F)$, proving surjectivity.

The map from $I(H/F)$ into the product of all the single-layer
inertia groups is injective, since an automorphism fixing every
$E_{n,\varepsilon}$ fixes their compositum. If $\tau$ generates
$I(H/F)$, each of its projected elements generates the corresponding
single-layer inertia group. The order of the resulting tuple is the
least common multiple of their orders. Injectivity now proves (3).

Assume OI. Formula (3) makes every joint ramification index odd.
If the global target $K(\sqrt{D^2-C^2})$ were inside
$M_3\cdots M_N$, extending the fixed embedding to $F_\varepsilon$
would give

$$
F_\varepsilon(\sqrt{a_\varepsilon t})
\subseteq H_{N,\varepsilon}
$$

by Proposition 1. The left field has ramification index two:
$X^2-a_\varepsilon t$ is Eisenstein over $R_\varepsilon$.
Multiplicativity would make two divide the odd joint index, a
contradiction. This proves ST under OI. Repeating the argument over
$\overline{\mathbb Q}(C)((t))$ proves the separate geometric
conditional statement. $\square$

### Whole-point interpretation of the missing hypothesis

The action of the local splitting-field Galois group on the complete
geometric point set is faithful. A generator of its cyclic inertia
has order equal to the least common multiple of all its cycle
lengths on that set. Thus OI is equivalent to every such inertia
orbit having odd length, on every whole layer at the selected
branch. A positive point-permutation sign says only that the
number of even-length cycles is even. It does not prove this
odd-length condition.

The missing input can therefore be stated as actual full-point
inertia data; it cannot be discharged by one nonramifying germ,
one reduced component, or a sign computation. Proposition 4 exhibits
this distinction with a finite flat normal full-point model.

## Proposition 3. Exact residual-unit criterion for a joint field

Let $F=\kappa((t))$ and let $E/F$ be any finite Galois extension,
with residue field $\kappa_E$. Define its quadratic squareclass
inventory and unramified part by

$$
V(E/F)=\ker\left(F^\times/F^{\times2}
\longrightarrow E^\times/E^{\times2}\right),
\qquad
U(E/F)=\ker\left(\kappa^\times/\kappa^{\times2}
\longrightarrow\kappa_E^\times/\kappa_E^{\times2}\right).
\tag{4}
$$

Embed $U(E/F)$ into $F^\times/F^{\times2}$ by constant units.

There are exactly two possible forms:

$$
V(E/F)=U(E/F),
\quad\text{or}\quad
V(E/F)=U(E/F)\ \sqcup\ [a t]\,U(E/F)
\tag{5}
$$

for some $a\in\kappa^\times$. In the second case the ramified coset
is uniquely determined, although its representative $a$ need not be.

The second case occurs precisely when some character
$\operatorname{Gal}(E/F)\to\{1,-1\}$ is nontrivial on inertia.
For $E=H_{N,\varepsilon}$, the exact local target occurs precisely
when the second case holds and

$$
[a_\varepsilon/a]\in U(E/F),
\quad\text{equivalently}\quad
a_\varepsilon/a\text{ is a square in }\kappa_E.
\tag{6}
$$

### Proof

A constant $b\in\kappa^\times$ is a square in $E$ if and only if
its residue is a square in $\kappa_E$. The forward implication
follows by reducing a valuation-zero square root. For the reverse
implication, take a nonzero residue square root and apply Hensel
lifting to $X^2-b$ in the complete valuation ring of $E$.
The derivative at that residue root is nonzero. This proves that
the even-valuation part of $V(E/F)$ is exactly $U(E/F)$, by
Proposition 1.

The parity map in (1) sends the subgroup $V(E/F)$ to a subgroup of
$\mathbb F_2$. If that image is zero, the first alternative in (5)
holds. Otherwise choose a class $[a t]$ of odd valuation in the
kernel; it is possible to take $a\in\kappa^\times$ by (1).
The odd-valuation part of a subgroup is one coset of its
even-valuation part, proving the second alternative.

Every nontrivial element $[b]$ of $V(E/F)$ defines a quadratic
subfield $F(\sqrt b)$ of $E$, and all quadratic subfields arise in
this way. The associated sign character is nontrivial on inertia
exactly when that quadratic subfield is ramified. Over a complete
DVR of residue characteristic zero, a unit class gives either the
trivial field or an unramified quadratic field; an odd-valuation
class gives an Eisenstein ramified quadratic field. This identifies
the second alternative with the character condition. Finally
$[a_\varepsilon t]$ belongs to the displayed ramified coset exactly
when $[a_\varepsilon/a]$ belongs to its unit part, proving (6).
$\square$

The criterion applies to the *joint* field; no assertion identifies
its inventory with the span of inventories of the individual
layers. An argument using only inherited native phase and cycle
signs would require a proof that they exhaust the actual joint
quadratic characters. Accepted R3 explicitly does not give that
hypothesis.

Even inertia order is only a necessary condition for the ramified
coset in (5) to exist. Proposition 5 gives a cyclic quartic example
where inertia has order two but every quadratic character kills it.

## Proposition 4. Identical local permutations, opposite target answers

Fix either sign $\varepsilon$, an odd $n\ge3$, and any integer
$s\ge2$. Put $F=F_\varepsilon$, $R=R_\varepsilon$.
For $u\in\kappa^\times$ set

$$
E_u=F(w),\qquad w^2=u t,\qquad
R_u=R[w]/(w^2-u t).
$$

There is a finite flat normal $R$-algebra of rank $2ns$,

$$
\mathcal A_u=
R_u^{\,2n}\ \times\ R^{\,2n(s-2)},
\tag{7}
$$

where the second factor is omitted when $s=2$.
Its entire generic geometric point set has automorphisms $h,T,g$
satisfying

$$
|h|=2n,\qquad T=h^{n+1},\qquad g=h^n,\qquad
|T|=n,\quad |g|=2,\quad gT=Tg=h.
\tag{8}
$$

All points have native $T$-period $n$, all $h$-orbits have length
$2n$, and $g$ has no fixed point. The splitting field of the entire
generic point algebra is $E_u$.

Its nontrivial Galois/inertia element has positive sign on the
whole point set and on the native-cycle set, but negative sign
$\psi$ on the set of $h$-orbits. These permutation actions do not
depend on $u$.

Nevertheless $u=1$ and $u=a_\varepsilon$ give opposite answers to
containment of the exact target
$F(\sqrt{a_\varepsilon t})$. Both examples have ramification
index two and residue field $\kappa$. This distinction remains
after extending constants to $\overline{\mathbb Q}$.

### Proof

The polynomial $w^2-u t$ is Eisenstein over $R$. Its quotient
$R_u$ is isomorphic to $\kappa[[w]]$ via $t=w^2/u$, so it is a
complete DVR, finite free of rank two over $R$ and normal.
Equation (7) is a product of such rings and of copies of $R$;
hence it is finite flat, normal and has rank
$4n+2n(s-2)=2ns$.

The geometric points of its first factor can be labelled
$(j,\delta)$ with $j\in\mathbb Z/(2n)$ and
$\delta\in\{1,-1\}$ recording the image of $w$.
Let $h(j,\delta)=(j+1,\delta)$. On the remaining split factors,
divide their labels into $s-2$ blocks of size $2n$ and let $h$
cycle each block. These actions permute factors in (7), so they
extend to automorphisms of the whole finite flat model, not just
its generic fibre.

Define $T$ and $g$ by (8). Since $n$ is odd,
$\gcd(2n,n+1)=2$, so $T$ has order $n$ and every point has exact
$T$-period $n$. The map $g=h^n$ is a fixed-point-free involution.
Also $gT=h^{2n+1}=h$, proving all assertions in (8).
There are exactly $s$ free $h$-orbits and $2s$ native $T$-cycles.

The generic splitting field is $E_u$ because the first factors
require both images of $w$ and every other factor is split.
Its nontrivial automorphism $\tau$ sends
$(j,\delta)$ to $(j,-\delta)$ and fixes the split factors.
It is also the full inertia generator, since $E_u/F$ is totally
ramified quadratic. On points it is a product of $2n$
transpositions, an even number. Within each of the two affected
$h$-orbits, the $T$-cycles are the even and odd $j$ labels.
Thus $\tau$ exchanges two pairs of native $T$-cycles and has
positive native-cycle sign. On $h$-orbits it exchanges exactly
two orbits, so $\psi(\tau)=-1$.

For $u=a_\varepsilon$ the splitting field is the target itself.
For $u=1$, it is $F(\sqrt t)$, which is different from the target:
two nontrivial quadratic extensions are equal if and only if
their defining squareclasses have square ratio, whereas
$a_\varepsilon$ is nonsquare by Proposition 1. One quadratic
field cannot properly contain another quadratic field of the
same base. Both residues are $\kappa$, so even residue extension
data are identical. Proposition 1 also proves the ratio remains
nonsquare after the stated constant extension. $\square$

These models can take $s=s_n$ and match the accepted full point
count, free odd-period symmetry, and abstract sign formulas.
No positive inertia-sign value is being asserted for the actual
Fricke fields. The models are not asserted
to lie on a Fricke surface, to arise from the Vieta word, or to
satisfy its periodic equations. Their precise logical role is
only this: full-point finite flatness, the inherited $g,T$
relations, positive familiar signs, and the abstract inertia
permutation do not by themselves determine the exact quadratic
subfield. No actual inclusion in any $M_n$ follows.

## Proposition 5. Even inertia and constant-extension cautions

Let $F=\mathbb Q(C)((t))$ and set

$$
E=F(s,w),\qquad s^2=2,\qquad
w^2=(2-s)C t.
\tag{9}
$$

Then $E/F$ is cyclic quartic, with ramification index two and
residue field $\mathbb Q(C)(\sqrt2)$. Its unique quadratic
subfield is the unramified field $F(\sqrt2)$; thus it contains
no ramified quadratic field. In particular it does not contain
$F(\sqrt{2Ct})$.

After extending constants to $\overline{\mathbb Q}$, a local
field factor of (9) is exactly
$\overline{\mathbb Q}(C)((t))(\sqrt{2Ct})$.

### Proof

The field $F(s)/F$ is unramified quadratic: $X^2-2$ is separable
modulo $t$, and $2$ is nonsquare in $\mathbb Q(C)$. Over $F(s)$,
the polynomial $X^2-(2-s)C t$ is Eisenstein, giving a totally
ramified quadratic extension. Thus $[E:F]=4$, its index is two,
and its residue is $\mathbb Q(C)(s)$.

Define an $F$-automorphism $\sigma$ by

$$
\sigma(s)=-s,\qquad \sigma(w)=(1+s)w.
$$

It preserves the equations since

$$
(1+s)^2(2-s)=2+s.
$$

Its square fixes $s$ and sends $w$ to $-w$, using
$(1-s)(1+s)=-1$. Hence $\sigma$ has order four.
The four generated automorphisms exhaust the degree, proving
$E/F$ is cyclic quartic. Its only subgroup of index two is
$\langle\sigma^2\rangle$, whose fixed field is $F(s)$.
The inertia group is that same order-two subgroup, since it
fixes the residue $s$. Every sign character of the cyclic
quartic group kills it. This proves the absence of a ramified
quadratic subfield despite even inertia.

In $\overline F=\overline{\mathbb Q}(C)((t))$, choose either
constant value $s=\sqrt2$ or $s=-\sqrt2$. The nonzero constant
$2-s$ is a square in $\overline{\mathbb Q}$, so either field
factor of $E\otimes_F\overline F$ is $\overline F(\sqrt{Ct})$.
The constant $2$ is also a square there, making this exactly
$\overline F(\sqrt{2Ct})$. Its nontriviality follows from odd
$t$-valuation. $\square$

This example concerns local constant extension, not an actual
constant field in the Fricke tower. It forbids conflating an
arithmetic character-inventory exclusion with its geometric
counterpart. It does not contradict Proposition 2: the index
in (9) is even, so the odd-inertia hypothesis fails.

## Exact unresolved input and boundary checks

1. No actual $e(E_{n,\varepsilon}/F_\varepsilon)$ has been
   proved odd for all higher $n$ at either branch. OI is a
   sufficient hypothesis, not a renamed solution.
2. If even inertia occurs, a proof could instead exclude the
   ramified coset in Proposition 3, or determine its unit
   representative and show $a_\varepsilon/a$ is not a square
   in the actual joint residue field. None of these actual
   joint-field assertions has been established here.
3. Local presence does not imply a global inclusion. The map
   from global squareclasses to a completion need not be
   injective: $1+t$ is nonsquare in $\kappa(t)$ by its simple
   zero at $t=-1$ but is square in $\kappa((t))$ by Hensel
   lifting. Accordingly only local *exclusion* is exported.
4. The generic-to-slice specialization remains one-way by
   accepted R3. Neither local models nor specialized extra
   relations constitute a counterexample to generic SF2.
5. Arithmetic and geometric cases are separate. In particular,
   $\overline{\mathbb Q}(C)$ is not an algebraically closed
   residue field; the functional squareclass of $C$ persists.
6. The known layer-two collision on this slice, and the
   period-two germ's isolation, do not control every remote
   higher-period sheet. C4's distinct global-fold assignment
   is not used as an unproved input.
7. All statements use finite composita before taking an
   all-$N$ quantifier. No one common open neighborhood for
   infinitely many covers, no all-period genericity argument,
   and no finite census are asserted.

The original claims survive unchanged and remain unproved.
The deliverable is a sourced, complete local-algebra bridge and
a precise obstruction to completing it from the inherited
symmetry/sign data alone.
