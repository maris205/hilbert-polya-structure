# E6/R3 — Independent interlevel-contact and degree review

2026-09-09 UTC. Nonauthor, proof-only review of
[A3 REPORT.md](../../a3_interlevel_contacts/REPORT.md) and
[PROOF_SUPPLEMENT.md](../../a3_interlevel_contacts/PROOF_SUPPLEMENT.md).
Both author-complete files were read in full. This is a new proof
review, not a rerun of the accepted pair certificate or its later
ramification deduction. Current-team review is not human peer review,
external-model-family evidence, formal evaluation, or paper admission.

## 1. Verdict and exact scope

**PASS. Zero open mathematical or source-applicability must-fixes in
Theorems A–C and the stated additional displacement consequence.**

Fix an odd prime $p$, $k=\overline{\mathbb F}_p$, $K=k((s))$,
$R=k[[s]]$, $v(s)=1$, $r=(p-1)/p$, and
$P_s(z)=(1+s)z+z^2$. Let $M_j$ be the accepted canonical small
factor of native least period $p^j$.

For every $e\ge2$, every root $\alpha$ of $M_e$ and every root
$\beta$ of $M_1$, the new proof establishes

$$
v(\alpha-\beta)=d_0:=\frac{2(p-1)^2}{p^2},
\qquad [K(\alpha):K]\ge p^2,
$$

and

$$
v(P_s^{\circ p}(\alpha)-\alpha)=2(p-1).
$$

In particular, **$M_2$ is irreducible of degree $p^2$ for every
odd prime $p$**, and its cyclic local splitting group is full inertia.
This is a proved uniform second layer, not merely a conditional contact
criterion or a finite-prime extrapolation.

The general criterion, Theorem A, is also valid: if $2\le\nu\le e$
and $d=v(\alpha-\beta)$ satisfies

$$
p^\nu d\in\mathbb Z\setminus p\mathbb Z,
\qquad d<2r-\frac{p-1}{p^\nu},
$$

then $[K(\alpha):K]\ge p^\nu$. Theorem B is a separately valid
conditional control from the polynomial discriminant value $144$
at $(p,e)=(3,2)$; it is not needed for Theorem C.

The all-level full-inertia claim for $e\ge3$ and global PC424-D
remain open. The first-level contact has exact denominator $p^2$,
so the proposed first-level-contact shortcut with $\nu=e$ is
actually false for $e\ge3$. This is a failure of that sufficient
condition, not a counterexample to full inertia.

## 2. Dependency audit: no hidden pair or full-degree premise

The actual accepted interface was checked in
[first-pass A3, Steps 1–4 and the prime-level ramification paragraph](../../../lanes/a3_wild_tower/REPORT.md).
It supplies precisely:

- $Q_j=(P_s^{\circ p^j}-z)/(P_s^{\circ p^{j-1}}-z)\in R[z]$
  and its coprime Hensel factorization $Q_j=M_jV_j$, with
  $\deg M_j=p^j$ and $V_j(0,0)\ne0$.
- Distinct generic roots of $M_j$, forming one native cycle of
  ordinary least period $p^j$, all of valuation $r$.
- A cyclic root/splitting field of degree $p^h$, $1\le h\le j$,
  whose actual Galois generator is the rotation by $p^{j-h}$
  native steps. Higher-level irreducibility is not an input.
- The prime-level field $F=K(\beta)$ has degree $p$ and break
  $p-1$.

Root-field cyclicity here does not assume transitive Galois action:
all roots are polynomial iterates of one root, so its field is the
splitting field; the Galois action commutes with the single native
cycle and embeds in its rotation group. At higher levels a one-step
native rotation is not automatically a field automorphism.

The degree-$p$ first-level break has no level-two input either:
$v_F(\beta)=p-1$ and $v_F(\tau\beta-\beta)=2(p-1)$;
the prime-to-$p$ leading-exponent lemma gives break $p-1$.

Theorem C uses only these inputs and Theorem A. It does **not** use
the value $144$, the accepted $(3,2)$ degree-nine result, a level-two
AS nonzero class, or the previously computed breaks $(4,28)$.
Theorem B is reviewed below only as a conditional argument from its
stated scalar discriminant premise; no underlying program or output
was rerun or re-audited in this task.

The small-cycle and minimally ramified reduction inputs are
source-owned: the odd-prime, residue-multiplier-order-one case is
within [Lindahl–Rivera-Letelier, Theorem C and Proposition 4.4](https://arxiv.org/html/1311.4478v3).
Their cycle statements are used in the small/open-unit-disk setting,
not as uniqueness of all cycles in the affine line or as Galois
transitivity. The local Hensel/separability interface above remains
an explicitly accepted dependency.

## 3. Native displacement separation

For distinct small-orbit points $x,y$, even at different levels,

$$
\frac{P_s(x)-P_s(y)}{x-y}=1+s+x+y
\in1+\{u:v(u)\ge r\}.
$$

Each finite iterate has the same property by multiplying the factors.
All iterate differences preserve valuation. Also
$v(P_s(x)-x)=2r$, since $1+r>2r$.

Consecutive one-step displacements, divided by the first one, are
one modulo valuation at least $r$. Telescoping over a number of
steps prime to $p$ has nonzero constant residue, and therefore
valuation exactly $2r$. Telescoping over $p$ steps cancels the
constant sum in characteristic $p$, leaving valuation at least
$3r$. Any positive multiple of $p$ is a sum of such $p$-step
displacements and obeys the same lower bound. Zero differences
are allowed with valuation $+\infty$.

Thus, under a hypothetical proper root degree $p^h$ with $h<e$,
every nonidentity automorphism of $K(\alpha)/K$ moves $\alpha$
by valuation at least $3r$, because every available native rotation
index is divisible by $p$. Every nonidentity automorphism of
$F/K$ moves $\beta$ by exactly $2r$.
The argument needs this strict separation, not an exact higher-step
displacement or a higher ramification filtration.

## 4. Contact-degree criterion and noncyclic compositum

Write $L=K(\alpha)$, $[L:K]=p^h$, and $B=LF$.
These are finite separable Galois $p$-extensions. Complete discrete
valuation and perfect residue field give degree equal to ramification
index times residue degree; algebraic closedness makes the latter one.
Consequently $B/K$ is totally ramified and $[B:K]\le p^{h+1}$.

The element $\eta=\alpha-\beta$ is nonzero and of positive
valuation: the ordinary periods differ and both points have positive
valuation. Exact denominator $p^\nu$ for $v(\eta)$ forces
$p^\nu\mid[B:K]$, hence $h\ge\nu-1$.

If $h=\nu-1$, the degree inequalities force $[B:K]=p^\nu$,
$L\cap F=K$, and

$$
\operatorname{Gal}(B/K)
 \cong C_{p^{\nu-1}}\times C_p.
$$

In the application $\nu=2$, this is **$C_p\times C_p$, not
$C_{p^2}$**. Restrictions to the two factors can be chosen
independently. Since $h<e$, any automorphism nontrivial on $F$
has

$$
v(\tau\eta-\eta)
=v((\tau\alpha-\alpha)-(\tau\beta-\beta))=2r;
$$

the two summands have unequal valuations, or the first is zero.
An automorphism trivial on $F$ but nontrivial on $L$ has
displacement at least $3r$. The minimum over all nonidentity
automorphisms is therefore exactly $2r$.

The prime-valuation lemma applies to this possibly noncyclic group.
With $v_B=p^\nu v$, write $a=v_B(\eta)$; it is positive and
prime to $p$. The original coefficient field $k\subset K$ is
fixed pointwise, and $O_B=k[[t]]$. For any nonidentity $\tau$,
its $p$-power order forces uniformizer multiplier one, so
$\tau(t)=t(1+u)$ with $b_\tau=v_B(u)\ge1$.
For $j>0$ the exact monomial difference order is

$$
j+p^{v_p(j)}b_\tau.
$$

The leading $t^a$ term of $\eta$ has difference order
$a+b_\tau$; every later term has order at least
$j+b_\tau>a+b_\tau$. These bounds tend to infinity, so
the infinite tail cannot cancel the leading coefficient.
This verifies the lemma with fixed coefficients and no hidden
assumption that $B/K$ is cyclic.

Taking the minimum gives the compositum's first lower break

$$
b_B=p^\nu(2r-d)>p-1.
$$

The first upper break equals the first lower one. Upper numbering
is compatible with the quotient $\operatorname{Gal}(F/K)$:
as long as the full upper group of $B/K$ is whole, its quotient
image is whole. Thus the quotient cannot have an earlier first
break. Its known break $p-1$ contradicts the displayed bound.
This proves $h\ge\nu$.

The required general-Galois quotient theorem, integer valuation
normalization and degree formula were checked in
[Elder–Keating, §2 before Lemma 2.1](https://arxiv.org/html/2503.16830v1).
That passage applies before specializing to cyclic extensions and
allows arbitrary perfect residue fields. A cyclic-only break formula
has not been applied to $C_p\times C_p$.

## 5. Derivative-ratio evaluation at the common zero

The first-level factorization is the exact polynomial identity

$$
P_s^{\circ p}(z)-z=z(z+s)M_1(z)V_1(z).
$$

Let $\mu=(P_s^{\circ p})'(\beta)$, where the derivative is
with respect to the dynamical coordinate $z$, not the parameter $s$.
At $M_1(\beta)=0$, differentiating the product leaves only

$$
\mu-1=\beta(\beta+s)M_1'(\beta)V_1(\beta).
$$

The cofactor is a unit because its reduction at $(0,0)$ is nonzero
and $v(\beta)>0$. Both $\beta$ and $\beta+s$ have valuation
$r$, since $r<1$. The $p-1$ distinct first-level root differences
in $M_1'(\beta)$ all have valuation $2r$. Hence

$$
v(\mu-1)=2r+(p-1)2r=2(p-1)<\infty.
$$

In particular $\mu\ne1$, with no higher-level hypothesis.
Set $n=p^e$, $m=p^{e-1}$ and $F_a(z)=P_s^{\circ a}(z)-z$.
For $e\ge2$, both $n$ and $m$ are multiples of the actual period
$p$ of $\beta$. Thus the chain rule gives

$$
F_n'(\beta)=\mu^{p^{e-1}}-1,
\qquad F_m'(\beta)=\mu^{p^{e-2}}-1\ne0.
$$

Differentiating $F_n=F_mQ_e$ and then substituting $\beta$
therefore yields

$$
Q_e(\beta)=\frac{F_n'(\beta)}{F_m'(\beta)}
 =(\mu-1)^{p^{e-1}-p^{e-2}}.
$$

This divides by a proved nonzero derivative, not by the zero value
$F_m(\beta)$. The $e=2$ endpoint has denominator $\mu-1$;
no negative iterate exponent or unproved simple-zero premise occurs.

The factorization $Q_e=M_eV_e$ similarly has $V_e(\beta)$ a
unit. Taking valuations of the monic root product consequently gives

$$
\sum_{i=1}^{p^e}v(\beta-\alpha_i)
 =v(M_e(\beta))=2(p-1)^2p^{e-2}.
$$

It is not necessary to assume these $p^e$ roots form a single
Galois orbit. They are the accepted single **native** orbit and are
distinct; contacts with $\beta$ are finite because periods differ.

## 6. Equalization, denominator and the uniform conclusion

For any two distinct roots of $M_e$, their difference is a finite
sum of native one-step displacements of valuation $2r$. Its
valuation is therefore at least $2r$; cancellation can only raise it.
Exact equality for every within-level pair is not assumed.

The average of the preceding $p^e$ cross contacts is
$d_0=2(p-1)^2/p^2<2r$. At least one contact is below $2r$.
For every other level-$e$ root, its mutual difference from that
chosen root has strictly larger valuation than the contact. The
strong triangle inequality forces its contact with the fixed
$\beta$ to be identical. Thus all contacts equal their average.
The argument works for each first-level $\beta$, proving the
claimed quantifiers over both root sets.

For odd $p$, $p\nmid2(p-1)^2$, so the denominator is exactly
$p^2$, not merely a divisor of $p^2$. Furthermore

$$
p^2(2r-d_0)=2(p-1)>p-1.
$$

Theorem A applies with $\nu=2$. If the root degree had been $p$,
the hypothetical compositum would have degree $p^2$, the positive
integer value of $\eta$ would be $2(p-1)^2$, and its first break
would be $2(p-1)$, contradicting its prime-level quotient's break
$p-1$. This supplies the needed second factor of $p$; the
denominator bound alone would not supply it for $L$ itself.

At $e=2$ the accepted upper degree bound is $p^2$, so equality
and irreducibility follow. At larger $e$ this argument proves only
the lower bound $p^2$. Oddness is used essentially in the numerator
check; no assertion at $p=2$ is justified by this proof.

Evaluating the first-level factorization at $\alpha$ now gives
$2r+p d_0=2(p-1)$ for its $p$-step displacement, including all
$e\ge2$. For $e\ge3$, however, $p^ed_0$ is divisible by $p$.
The submitted refutation of its proposed higher-denominator contact
law is therefore exact, and its retained higher-level gap is honest.

## 7. Separate discriminant-only control and provenance

Theorem B is also logically sound without the old AS conclusion.
Conditionally on $v(\operatorname{Disc}M_2)=144$ at $p=3$,
six native differences have valuation $4/3$ and the two step-three
differences have one common valuation $D$. The residue-two
telescoping argument equates the latter, and native isometry gives
equal derivative valuations at all nine roots even if $M_2$ factors.
Thus $144=9(6\cdot4/3+2D)$ gives $D=4$.
The first-level factorization then gives total cross contact $8/3$;
the three prime-level roots are mutually at valuation distance $4/3$,
so the same strict-ultrametric argument gives every contact $8/9$.
Theorem A applies. This does not identify a polynomial discriminant
with a field different or assume Galois transitivity before proving it.

This conditional route is redundant after Theorem C but is kept
visibly separate. Agreement with the old certified pair is a control,
not evidence needed for the computation-free uniform theorem.

Primary-source passages cited above were accessed on 2026-09-09.
The new derivative, contact and compositum arguments were checked
directly. Classical cycle theory and ramification remain source-owned;
this review makes no literature-priority certification. The outcome
is accepted auxiliary progress toward the unchanged full contract,
not a separate paper admission or target-arithmetic promotion.

The research-review skill was used for nonauthor evidence/claim
separation and explicit gap checking. Its external-model step was
excluded by the current-session, no-upload assignment. No extra
agent, external model/API, mathematical execution, old-code rerun,
author/shared/Git edit, evaluation or PDF build was used. Only this
new assigned review file was written. Earlier E6 reviews are frozen.

| Final reviewed author file | SHA-256 |
| --- | --- |
| `a3_interlevel_contacts/REPORT.md` | `9a9cf14da77922550349c7b43ef52529402a555794ee91773de67161844b05f8` |
| `a3_interlevel_contacts/PROOF_SUPPLEMENT.md` | `7e9494aa53bb96f5927b8a6ab8e27c5d318d35a9c0f1751663acb9b91f0c1bdb` |

Hashes bind the inspected versions; they are not mathematical evidence.

**ZERO_OPEN_MUST_FIXES; UNIFORM_SECOND_LAYER_VERIFIED;
ALL_LEVEL_FULL_INERTIA_AND_GLOBAL_PC424_D_UNCLOSED.**

`NO_BAD_EULER_OR_ROOT_NUMBER`.
