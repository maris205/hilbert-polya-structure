# E6/R3 — Independent full-local-inertia review

2026-09-09 UTC. Separate nonauthor, whole-proof review of
[FULL_LOCAL_INERTIA.md](../../a3_interlevel_contacts/FULL_LOCAL_INERTIA.md).
The complete 199-line submitted proof was read. The earlier
[second-layer review](../e6_interlevel_contacts/REVIEW.md) and all
pair-certificate/ramification reviews remain frozen. This is current-team
mathematical review, not human peer review, external-model-family evidence,
formal evaluation, or an admission decision.

## 1. Verdict: the all-level local claim is proved

**PASS. Zero open mathematical or source-applicability must-fixes.**

For every odd prime $p$ and every $e\ge1$, let

$$
k=\overline{\mathbb F}_p,\quad K=k((s)),\quad v(s)=1,
\qquad P_s(z)=(1+s)z+z^2.
$$

The canonical small factor $M_e\equiv z^{p^e}\pmod s$ of
the native period-$p^e$ quotient is irreducible over $K$.
Its root field is its splitting field, with Galois group
$C_{p^e}$, and the extension is totally ramified of degree $p^e$.
The equivalent nonvanishing of its first reduced native AS quotient
also follows from the accepted torsor criterion.

This proof closes the full **local** inertia statement, not only
level two. It does not close global PC424-D: transitivity on the
global set of native cycles remains a separate problem. The earlier
review's open all-level boundary described its own frozen A–C proof;
this new supplement supplies the previously missing additional argument.

No pair AS polynomial, polynomial discriminant value $144$, old
degree-nine computation, full higher-level degree premise, or conjectured
contact pattern is used in this proof.

## 2. Accepted inputs and quantifiers

Set $r=(p-1)/p$, $c=2r$, and $D=2(p-1)$. For each $j\ge1$,
$S_j$ is the set of $p^j$ distinct roots of $M_j$ in one fixed
separable closure with the unique extension of $v$. The first-pass
interface supplies one native cycle, root valuation $r$, the exact
factorization $Q_j=M_jV_j$ with $V_j(0,0)\ne0$, and a Galois
rotation subgroup $H_j\le C_{p^j}$. It does not supply higher-level
Galois transitivity.

The independently accepted second-layer input is exactly Theorem C
and equation (23) of
[PROOF_SUPPLEMENT.md](../../a3_interlevel_contacts/PROOF_SUPPLEMENT.md):

$$
H_2=C_{p^2},\qquad
v(P_s^{\circ p}(x)-x)=D
\quad\text{for every }j\ge2\text{ and every }x\in S_j.
$$

The displacement statement genuinely has the quantifier $j\ge2$;
it is not merely the level-two special case. Its proof was checked
again at the exact input passage: prime-level cross contacts give it
without assuming any higher $M_j$ irreducible. The preceding review
has already closed this input's independent proof obligation.

The current supplement proves $H_e=C_{p^e}$ for an arbitrary
$e\ge3$ by comparison with $S_2$. It does not inductively assume
$H_{e-1}$ full. The base cases $e=1$ and $e=2$ are explicitly
the accepted prime-level and second-layer results.

All valuations in the contact and multiplier calculations are the
base-extended valuation $v(s)=1$. They are not integer valuations
on a putative degree-$p^e$ field, so the calculation never presupposes
that field degree in order to normalize them.

## 3. Exactly p clusters at the chosen threshold

For distinct points of valuation $r$ from either root set,

$$
\frac{P_s(x)-P_s(y)}{x-y}=1+s+x+y
\in1+\{u:v(u)\ge r\}.
$$

Finite iterates preserve valuation and have the same residue-one
difference quotient. The one-step displacement has valuation $c$,
because $v(sx)=1+r>2r=v(x^2)$. A prime-to-$p$ number of steps
has valuation exactly $c$: dividing the telescoping sum by the first
displacement produces nonzero constant residue.

A nonzero multiple of $p$ steps within a level-$j$ orbit, $j\ge2$,
is a sum of $p$-step displacements of valuation $D$, and hence
has valuation at least $D>c$. Steps divisible by $p^j$ give the
same point and are treated by equality, not a finite-distance claim.

It follows that $x\sim y$ iff $x=y$ or $v(x-y)>c$ partitions
$S_j$ into exactly $p$ clusters: the native indices modulo $p$.
Each has $p^{j-1}$ elements; any two different clusters are at
valuation distance exactly $c$, whereas every pair of distinct
points in one cluster has valuation distance greater than $c$.
The native map permutes these clusters as one $p$-cycle.

The relation is intrinsic, with labels changing only by cyclic
reindexing when the initial point changes. Since the absolute Galois
group preserves each root set and the unique valuation, it acts on
the clusters. Its action is the native rotation index modulo $p$.
No conclusion about $H_j$ being full is needed to construct them.

## 4. Level-two multiplier and legitimate derivative ratio

For $\beta\in S_2$, put $\mu=(P_s^{\circ p^2})'(\beta)$.
Differentiate the exact polynomial identity

$$
P_s^{\circ p^2}(z)-z
 =(P_s^{\circ p}(z)-z)M_2(z)V_2(z)
$$

with respect to $z$. Because $M_2(\beta)=0$, evaluation leaves

$$
\mu-1=(P_s^{\circ p}(\beta)-\beta)M_2'(\beta)V_2(\beta).
$$

The initial factor is nonzero with valuation $D$ and the cofactor
is a unit. In $M_2'(\beta)$ there are exactly $p(p-1)$
differences with indices prime to $p$, each of valuation $c$.
The remaining $p-1$ differences have indices $ap$, $1\le a<p$.
Their valuation is exactly $D$, not just at least $D$: telescope
$a$ successive $p$-step displacements, divide by the first, and
use the residue-one iterate quotient to obtain residue $a\ne0$.
Thus

$$
T_2:=v(\mu-1)=D+p(p-1)c+(p-1)D
 =2(p-1)(2p-1)<\infty.
$$

This checks all $p^2-1$ derivative factors and the extra initial
factor separately. $T_2$ is a multiplier-increment valuation, not
a field different or a computed polynomial discriminant.

Now fix $e\ge3$. Both iteration counts $p^e,p^{e-1}$ are
multiples of the actual period $p^2$ of $\beta$. Differentiating
the quotient's polynomial identity at this common zero gives

$$
Q_e(\beta)
 =\frac{\mu^{p^{e-2}}-1}{\mu^{p^{e-3}}-1}
 =(\mu-1)^{(p-1)p^{e-3}}.
$$

The denominator is nonzero, because in characteristic $p$ it is
$(\mu-1)^{p^{e-3}}$. The endpoint $e=3$ has denominator
$\mu-1$ and no negative exponent. This is division by a proved
nonzero derivative, not substitution into a $0/0$ rational value.

## 5. The averaged contact proves existence, not equal distances

The Hensel cofactor $V_e(\beta)$ is a unit: it has nonzero
constant reduction and $\beta$ has positive valuation. The monic
product of all $p^e$ roots of $M_e$ therefore gives

$$
\frac{1}{p^e}\sum_{\alpha\in S_e}v(\beta-\alpha)
 =\frac{T_2(p-1)}{p^3}
 =\frac{2(p-1)^2(2p-1)}{p^3}.
$$

The root weights are all one: the accepted generic factor is separable
and has $p^e$ distinct roots, even before irreducibility is proved.
Every contact is finite, since ordinary periods $p^e$ and $p^2$
differ. Summation is over the full native root set, not an assumed
Galois orbit or one of its possible smaller field factors.

Subtracting the threshold $c$ gives

$$
\frac{2(p-1)(p^2-3p+1)}{p^3}>0.
$$

For every odd prime $p\ge3$, $p^2-3p+1\ge1$; at the
smallest prime the margin is $4/27$. Thus at least one root
$\alpha$ has $v(\alpha-\beta)>c$.

This inference requires only a finite average and strict positivity.
It does **not** claim every cross contact equals that average.
In particular it does not transfer the earlier equal-contact rule
below the separation threshold into this deeper-contact situation.
Oddness is respected; the displayed margin is not positive at $p=2$.

## 6. Matching: uniqueness, cardinality and both equivariances

Let $\mathcal T_j=S_j/{\sim_j}$ be the set of $p$ clusters.
Relate $C\in\mathcal T_e$ and $D'\in\mathcal T_2$ when
some $x\in C,y\in D'$ satisfy $v(x-y)>c$.

One such pair makes **every** pair in $C\times D'$ satisfy
that inequality. Indeed the differences through $x$ and $y$ are
all of valuation greater than $c$, and the strong triangle inequality
preserves the strict bound. The zero-difference cases cause no problem.

No second cluster $C'\ne C$ can relate to $D'$: points of
$C'$ have distance valuation exactly $c$ from $C$, whereas
points of $D'$ have distance greater than $c$ from $C$.
The unequal-valuation triangle rule forces distance exactly $c$
between $C'$ and $D'$. Interchanging the two root sets proves
the analogous uniqueness for $D'$. This argument does not require
the two clusters to have equal numbers of roots.

Choose the close pair from §5. Its pairs of native iterates with
indices $0,\ldots,p-1$ remain close by the isometry. They meet
each of the $p$ clusters once on each side, because the native
actions are $p$-cycles. Hence the relation is nonempty on every
cluster and is bijective, not merely injective on an unspecified
subset. It defines a unique map

$$
\Phi_e:\mathcal T_e\xrightarrow{\sim}\mathcal T_2.
$$

Two distinct equivariance statements hold:

- **Native:** a related pair stays related under $P_s$; uniqueness
  then gives $\Phi_e(P_sC)=P_s\Phi_e(C)$. The initially selected
  pair only demonstrates coverage and does not define an arbitrary
  label-dependent matching.
- **Galois:** for $g\in\operatorname{Gal}(K^{\mathrm{sep}}/K)$,
  the root sets and valuation are preserved. Thus a related pair
  goes to a related pair, and uniqueness gives
  $\Phi_e(gC)=g\Phi_e(C)$.

The proof needs no inclusion of the full root fields, no extension of
a selected rootwise matching, and no claim that $p^{e-1}$ roots in
one higher cluster biject with $p$ roots in a level-two cluster.
It matches **clusters**, whose numbers are both $p$.

## 7. Full local image and the remaining global boundary

By the accepted second layer, the absolute Galois image on $S_2$
is $C_{p^2}$, so its image on $\mathcal T_2$ is the full
$C_p$. The Galois-equivariant bijection forces a transitive
absolute Galois action on $\mathcal T_e$.

A proper subgroup of the cyclic group $C_{p^e}$ is contained in
$pC_{p^e}$. Its native rotation indices are all divisible by $p$,
so it fixes every cluster of $\mathcal T_e$ individually. Since
there are $p>1$ clusters, that action cannot be transitive. Therefore
$H_e=C_{p^e}$ for every $e\ge3$.

This is a group-theoretic consequence of nontrivial mod-$p$ action,
not an inference that cluster transitivity forces root transitivity
for an arbitrary permutation group. The cyclic $p$-group embedding
is essential and is an accepted input.

Together with the two base levels, $M_e$ is irreducible for every
$e\ge1$. The root field already contains the whole native orbit,
so is the splitting field. Its degree is $p^e$. Finite extensions
of this complete discretely valued field with perfect residue field
are defectless; algebraic closedness makes the residue degree one.
Thus the extension is totally ramified and the full group is inertia.
The degree/ramification normalization is within
[Elder–Keating, §2](https://arxiv.org/html/2503.16830v1).

The final AS equivalence was checked against the actual
[accepted A4 criterion, §§1–2](../../../lanes/a4_witt_local_data/PROOF_SUPPLEMENT.md).
The native degree-$p$ quotient records the rotation character modulo
$p$; this image is nonzero precisely when the cyclic $p^e$ image
is full. Over $k((s))$, with $k$ algebraically closed, a nonzero
AS class has a nonzero reduced polar representative. Hence the
claimed all-level nonvanishing follows, but no explicit higher
AS polynomial or complete Witt vector has been calculated here.

The matched objects are local clusters of the canonical small cycle.
They are not the global quotient's sheets representing different
native cycles. The proof neither shows global cycle-quotient
transitivity nor classifies all geometric dynatomic components.
Full global PC424-D therefore remains unresolved by this theorem.

## 8. Sources, execution boundary and final hashes

The source-dependent small-cycle theorem is subtracted, not promoted
to a new Galois statement. Its odd-prime/order-one specialization
was checked in [Lindahl–Rivera-Letelier, Theorem C](https://arxiv.org/html/1311.4478v3);
the interpretation is the small/open-unit-disk cycle. The accepted
local Hensel and separability packaging remains an explicit dependency.
Primary pages above were accessed on 2026-09-09. The multiplier,
average, matching and group-action steps were checked directly.
No literature-priority certification or paper-admission decision is
made by this review.

The research-review skill supplied the independent evidence/claim
audit. Its external-model step was excluded by the current-session,
no-upload assignment. No mathematical execution, pair-code rerun,
external model/API, extra agent, author/shared/Git edit, evaluation
or PDF build occurred. Only this new assigned review file was written.

| Binding artifact | SHA-256 |
| --- | --- |
| New `a3_interlevel_contacts/FULL_LOCAL_INERTIA.md` | `0a4f4ff66b633de268d741142502c1b4244868b9eccd3eb040ae472e0b296250` |
| Accepted `a3_interlevel_contacts/PROOF_SUPPLEMENT.md` | `7e9494aa53bb96f5927b8a6ab8e27c5d318d35a9c0f1751663acb9b91f0c1bdb` |
| Frozen `reviews/e6_interlevel_contacts/REVIEW.md` | `02728a25605b5d2cfb9b2d0c8eaced14df82dcd29084e18f8d81ae1c20b9024d` |

Hashes bind the inspected versions, not their mathematical truth.

**ZERO_OPEN_MUST_FIXES; ALL_ODD_PRIME_ALL_LEVEL_LOCAL_INERTIA_VERIFIED;
GLOBAL_PC424_D_UNCLOSED.**

`NO_BAD_EULER_OR_ROOT_NUMBER`.
