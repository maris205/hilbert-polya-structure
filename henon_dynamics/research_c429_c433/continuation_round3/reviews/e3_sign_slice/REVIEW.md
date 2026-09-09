# R3 E3: independent review of the Fricke sign-slice interface

2026-09-09 UTC. Current-team nonauthor review of the complete D2 R3
[report](../../d2_sign_character_separation/REPORT.md) and
[proof package](../../d2_sign_character_separation/PROOF_PACKAGE.md).
This is a mathematical/source-applicability review, not a formal paper
evaluation or an external-model review.

## Verdict and exact scope

**PROVABLE AS STATED for Propositions 1, 3 and 4 and Corollary 2.
Zero open mathematical or source-applicability must-fixes.**

The verified claims are the complete two-parameter character computation,
the symmetric-line and formal-germ limitation, the one-way sufficient
specialization test, and the odd-period symmetry/character interface.
In particular,

$$
d_2|_{A=B=0}=[D^2-C^2],\qquad
p_2|_{A=B=0}=[C^2+4D]
$$

are the actual restricted cycle-sign and phase-parity characters, with
no missing component or undetermined constant factor. They are independent
over both $\mathbb Q(C,D)$ and $\overline{\mathbb Q}(C,D)$.

**SF2 remains NOT CURRENTLY JUSTIFIED.** The authors neither prove its
all-finite-composita exclusion nor give an actual generic inclusion.
The new interface is suitable for auxiliary acceptance only. It is not
a complete tower-independence theorem, an actual higher-group computation,
or grounds for paper admission.

The accepted FG2 presentation and full étale fibre, R2 NI/all-period
ordinary counts, and R2 character/Goursat algebra are imported at their
accepted scope. This review checks their use, not their proofs again.
C4's separately assigned R3 smooth-fold problem is outside this review.

## Frozen byte binding

Both complete author files were read and their stable SHA-256 hashes
verified before this review was written:

```text
REPORT.md
3e17d8c0b430c8e35e69bf5f6e4662872741e0fa173828d7225e370c055e9c46

PROOF_PACKAGE.md
5449f038c53ad6be18d7a50080afbb42414c6db8e8d4f12b84f2e9d87c03a35d
```

The mathematical verdict binds these bytes, not later changes or other
agents' summaries.

## 1. The full eleven-cycle restriction

Let $\Sigma=\{A=B=0\}$ and $K=\mathbb Q(C,D)$. The accepted FG2
fibre at $(0,0,0,1)$ provides all $22$ distinct étale point sheets.
Consequently the generic point of the irreducible $\Sigma$ lies in
the required finite étale locus, and its point/cycle pullbacks have
ranks $22/11$. The surface is generically smooth there. The accepted
identification of $T$-fixed points with surface critical points makes
the constructed $T^2$ points exact native period two.

The reviewer independently substituted into the accepted finite-$q$
presentation and checked all cases. Since $C$ is nonzero in $K$,
$X=0$ forces $Y=0$ and gives the single axis cycle

$$
(X,Y,Z,q)=(0,0,C,-D/C^2).
$$

Its actual phase points satisfy $z^2-Cz-D=0$. If $X\ne0$, the
first two cycle equations give $q^2Z^2=1$, hence

$$
Z=\varepsilon/q,\quad Y=\varepsilon X,\quad
X^2=(1-\varepsilon Cq)/q^2,
$$

and direct substitution in the last equation gives exactly

$$
(D-2\varepsilon C)q^2+(3+\varepsilon C)q-1=0.
$$

Each quadratic $Q_\varepsilon$ has rank two and nonzero discriminant
$C^2-2\varepsilon C+9+4D$. Its element $q$ is a unit; the norm of
$1-\varepsilon Cq$ is $(D+\varepsilon C)/(D-2\varepsilon C)$,
which is nonzero in $K$. Thus adjoining $X$ produces a finite étale
rank-four algebra $B_\varepsilon$. Irreducibility of these algebras
is neither assumed nor needed. The phase radicand is nonzero since
$16h_\varepsilon(1/4)=D+2\varepsilon C-4$.

The omitted $r=-1$ chart is essential. In physical coordinates its
opposite phase is $(-x,-y,-z)$. The return equations give
$yz=xz=0$ and $xy=-C$, hence $z=0$ and $x^2+y^2=D$.
Writing $\xi=x^2$ modulo simultaneous negation gives precisely

$$
B_0=K[\xi]/(\xi^2-D\xi+C^2),\qquad x^2=\xi,
\quad y=-C/x.
$$

Its two distinct cycle labels are disjoint from the finite-$q$
labels. The axis label, these two labels, and the four labels for
each sign exhaust the already known rank eleven. Thus

$$
B_\Sigma=K\times B_0\times B_+\times B_-
$$

is a complete decomposition, not a selected subcover. No loss of
labels is hidden at the chart boundary.

## 2. Trace forms, phase parity and constant factors

For a rank-$b$ finite étale $R/K$, the trace matrix of
$R[s]/(s^2-a)$ in a basis $e_i,se_i$ has blocks $2G$ and $2G_a$,
where $\det G_a=\det G\operatorname{Norm}_{R/K}(a)$. Its
discriminant squareclass is therefore exactly
$[\operatorname{Norm}_{R/K}(a)]$: the remaining factor is
$2^{2b}(\det G)^2$. This works for products as well as fields and
introduces no sign or constant ambiguity. Product trace forms are
block diagonal, so their discriminant classes multiply.

For the cycle algebra, the two root sum/product identities give

$$
\operatorname{Norm}_{Q_\varepsilon/K}(1-\varepsilon Cq)
=\frac{D+\varepsilon C}{D-2\varepsilon C}.
$$

The factor $q^{-2}$ has square norm. Multiplying these two
contributions with $\operatorname{disc}(B_0)=D^2-4C^2$ gives
$D^2-C^2$ exactly modulo squares. Omitting $B_0$ would leave the
wrong class.

The sign on all $22$ points is the total phase parity: a swap of
two size-two blocks is even, whereas an internal phase flip is
odd. The axis point algebra contributes $C^2+4D$. The omitted
chart contributes $\operatorname{Norm}_{B_0/K}(\xi)=C^2$.
For either rank-four component the phase norm is

$$
\operatorname{Norm}_{B_\varepsilon/K}(1-4q)
=\operatorname{Norm}_{Q_\varepsilon/K}(1-4q)^2.
$$

This proves the asserted phase class without an invalid
substitution of $q=\infty$ into the old formula.

The valuation tests also pass. At the generic divisor $D=C$,
$D^2-C^2$ has valuation one and $C^2+4D$ is a unit. At the
generic divisor $C^2+4D=0$, their roles reverse. These prime
divisors remain prime after algebraic closure of the constants.
The two characters are therefore independent geometrically and
arithmetically; they are not merely arithmetically distinct
through a constant quadratic twist.

## 3. The symmetric-line limitation is legitimate

The generic point of $\Lambda=\{A=B=C=0\}$ remains in the
FG2 étale locus, again using $D=1$. The representative $D^2-C^2$
is a unit near its generic point, so restriction to $C=0$ gives
a split cycle-sign cover. The phase class becomes $[4D]=[D]$.

The separate FG2 label description agrees: three rational axis
cycles and four copies of a quadratic pair yield four simultaneous
transpositions, hence positive cycle sign. The fact that the
generic-$C$ component decomposition changes at $C=0$ does not
invalidate the finite étale character restriction.

In $\mathbb Q(D)[[C]]$, the polynomial $u^2-(D^2-C^2)$ has the
root $u=D$ modulo $C$ and unit derivative $2D$. Hensel lifting
therefore gives the asserted square root on the full formal
neighborhood. This is a precise blindness of that test; it is
neither generic splitting of $F_2$ nor failure of SF2.

## 4. All specialization hypotheses in Proposition 3

The one-way implication (ST)$\Rightarrow$SF2 passes. The following
points are necessary and are supported by the accepted inputs and
the argument actually written.

1. NI supplies every higher exact-period coordinate sheet, distinct
   and étale over the Cayley point $b_C=(0,0,0,4)$, together with
   the whole finite Galois normalization. It is not a statement
   about one unramified root or one place.
2. Since $b_C\in\Sigma$, for each $n$ the generic point of
   $\Sigma$ lies in the étale, coordinate-regular, distinct and
   exact-period loci. For fixed finite $N$, their finite
   intersection still contains that generic point. There is no
   claim that an infinite intersection is open.
3. The $F_2$ cover has its own suitable open from the FG2 point at
   $D=1$. It need not use the same closed point as the higher
   covers: the opens all meet at the generic point of $\Sigma$.
4. A hypothetical generic inclusion into $L_3\cdots L_N$ extends
   over a common open containing that generic point to a morphism
   of finite étale normalizations. Finite composita preserve this
   étaleness. The restricted $F_2$ algebra is the nontrivial field
   $K(\sqrt{D^2-C^2})$, not a split product.
5. Projection to any connected component of the higher restricted
   cover remains a unital map from that field, and is therefore
   injective. Thus the quadratic field survives in every chosen
   compatible component.

The coordinate-generation paragraph closes a potentially serious
gap. For the original Galois splitting cover, the residue field of
a component is Galois over $K$, with automorphisms obtained from
its decomposition group; inertia is trivial. If a residual
automorphism fixes every specialized coordinate, any corresponding
lift fixes each specialized point label. Distinctness forces the
lift to fix every generic point label. Since those coordinates
generate the original splitting field, the lift is the identity.
The residue extension therefore has no subextension left over
after adjoining the specialized coordinates. Applied to the union
of all labels for $3\le n\le N$, this identifies its field with
the compatible compositum $M_3\cdots M_N$.

Arithmetic constants cause no hidden exception. NI is originally
stated geometrically. The arithmetic normalization becomes the
disjoint union of its conjugate geometric normalizations after
separable constant extension; normalization commutes with this
extension in characteristic zero, and étaleness descends faithfully
flatly. Thus the same generic-slice open exists arithmetically.
The residual coordinate argument retains, rather than discards,
any constants present in the original coordinate splitting field.
No regularity or trivial-constant-field theorem for higher layers
or their composita is being assumed. The geometric version of ST
is proved separately after extending constants; an arithmetic
exclusion is not silently promoted to a geometric exclusion.

The converse warning is correct: the distinct generic classes
$f$ and $f+a$, for $f=D^2-C^2$, agree on $a=0$, although both
character covers are étale at the generic point of that slice.
The odd valuation on $a=-f$ proves generic distinctness.

## 5. Odd-period symmetry and actual-image limitations

Direct substitution verifies that $g=(-x,-y,z)$ commutes with
each Vieta involution on $\Sigma$. Its fixed locus is $x=y=0$,
where $T$ is $z\mapsto C-z$ and has period at most two.
The accompanied full-family base map $(A,B)\mapsto(-A,-B)$
preserves the generic exact-period incidence closure, so this
symmetry acts on the selected specialized sheets without importing
extra vertical components.

For odd $n\ge3$, if $gP=T^jP$, commutation gives $n\mid2j$,
hence $n\mid j$. That would fix $P$ under $g$, which is
impossible. Thus $g$ pairs distinct native cycles. The action of
$C_2\times C_n$ is free and $h=gT$ has orbit length $2n$,
with $h^n=g$ and $h^{n+1}=T$ on $P_n$.

The Galois action consequently lies in $C_{2n}\wr S_{s_n}$,
$s_n=\nu_n/(2n)$, and the sign of its permutation on $h$-orbits
is a well-defined character of the actual Galois group. The orbit
algebra and its discriminant define that character even if it is
trivial. The accepted count bounds supply $s_n\ge2$.

Inside the ambient centralizer, the two native cycles in one
$h$-orbit correspond to even and odd $h$-exponents. Accordingly

$$
\chi_{\mathrm{native\ cycle},n}=(-1)^{\sum a_i},\qquad
\psi_n=\operatorname{sgn}(\sigma).
$$

An odd rotation and a block transposition show independence there.
By the accepted R2 abelianization, the only nontrivial quadratic
character on $C_n\wr S_{2s_n}$ for odd $n$ is native cycle sign.
Its restriction is rotation parity, not $\psi_n$. Thus the
ambient pair-orbit sign does not extend to that larger group.

Crucially, none of this proves that the actual higher group attains
the ambient centralizer, that $\psi_n$ is nontrivial there, or
that its restriction is independent of the native sign. The
authors explicitly retain these qualifications. The phrase
"additional canonical character test" is correctly understood as
an additional test to check, not a proved additional nontrivial
quadratic subfield of $M_n$.

## 6. Branch boundary and source subtraction

At the generic slice branch $D=-\varepsilon C$, one root is
$q=\varepsilon/C$, with $X=Y=0$ and $Z=C$. The other root is
$1/3$, distinct generically. Hence the two labels distinguished
by the sign of $X$ meet the axis label as stated. This
symmetry-enhanced collision is not asserted to be C4's isolated
global smooth fold. Locating $D=\pm C$ does not establish how
any whole higher splitting field ramifies there.

The following primary passages were independently inspected:

- [Cantat–Loray, arXiv:0711.1579v2](https://arxiv.org/pdf/0711.1579v2),
  §3.1, pp. 20–21, and §9.4/Remark 9.13, pp. 64–67. The former
  accounts for even-sign and coordinate-permutation symmetries.
  The source uses the opposite cubic sign convention; simultaneous
  negation of the three coordinates and of $A,B,C$ identifies it
  with this family. The quadratic transformation applies to a
  special two-parameter family and has explicit finite-index word
  equivariance. Neither it nor periodicity under the whole modular
  group identifies the fixed native word $s_zs_ys_x$ with another
  clock. D2 uses the symmetry by direct substitution, not an
  unproved fixed-word transfer.
- [Doyle et al., arXiv:1703.04172](https://arxiv.org/pdf/1703.04172),
  §3.2, pp. 5–6, and §3.4, pp. 6–8. These passages distinguish
  marked-point and orbit quotients and separate primitive from
  satellite parabolic degeneration for polynomial families in one
  variable. Their formal-period, multiplier and branch results do
  not automatically apply to the ordinary exact-period Fricke
  surface cover. D2 correctly uses them as source context and a
  transfer boundary, not a Fricke branch-disjointness theorem.

The FG2 chart/omitted chart and R2 NI/count/algebra remain credited
accepted inputs. Trace discriminants, finite étale specialization
and wreath centralizers are classical tools. The newly checked
interface is the exact restricted character pair and its careful
use in a still-unproved sufficient exclusion test. This review
does not claim an exhaustive literature novelty result.

## Final disposition and execution record

Accept the stated auxiliary claims, with zero open repairs. Keep
SF2, actual higher-group character classification, and the relevant
all-finite-composita exclusion open. No paper admission follows.

The research-review and local batch workflow kept the inspection
on actual proofs, preserved accepted earlier results, and separated
auxiliary correctness from paper-level closure. Only this assigned
new review file was written. Mathematical executions: **0**.
Primary-source browsing was performed. No old certificate rerun,
author/shared-file edit, Git operation, manuscript/PDF write,
external-model invocation or additional agent was performed for
this R3 review.
