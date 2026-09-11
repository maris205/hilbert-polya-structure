# Lyness entrance: subtraction proof, not a nomination

2026-09-09 UTC. Author: /root/round211_functional_surgery_residual.
OWNER_AMBER / HOLD_EXTERNAL. No new pilot, candidate ID, or admission.

## Claim

The five-period, nonzero-rescaling entrance to the zero-totalized Lyness
family is exactly conjugate to the already retained P150 map. Its all-target
inverse calculation is the same elementary scalar equation already proved
in P150. An elliptic-curve extension cannot be substituted for a proof about
the whole zero-totalized affine plane.

## Status

PROVABLE AS STATED, with the explicit parameter and carrier scope below.
A new all-parameter temporal theorem for the remaining parameter values is
NOT CURRENTLY JUSTIFIED in this desk. This is a missing result here, not a
claim that such a result is impossible or absent from the literature.

## Assumptions and notation

Let $q$ be an odd prime power, let $a\in\mathbb F_q^\times$ and
$b\in\mathbb F_q$, and put $\iota(0)=0$ and $\iota(x)=x^{-1}$ for $x\ne0$.
Use the parameter scaffold
$$T_{a,b}(x,y)=(y,(ay+b)\iota(x)),\qquad (x,y)\in\mathbb F_q^2.$$
It is used to subtract the old entrance; no specific residual value of
$b/a^2\ne1$ is nominated or instantiated in a scientific test.
Write $L=T_{1,1}$ and $S_a(x,y)=(ax,ay)$.

## Proof strategy and dependency map

Direct substitution proves the scaling identity and the inverse law.
P150's actual manuscript supplies the already-proved full affine temporal
atlas for $L$. The source's elliptic-curve translation is used only to
identify a different carrier; no algebraic-geometric theorem is imported
as an all-affine result.

1. Scaling uses only $a\ne0$ and the definition of $\iota$.
2. The inverse formula uses one forced coordinate and scalar inversion.
3. P150 collision uses the scaling identity at $b=a^2$.
4. The domain obstruction uses the non-singleton fibre from step 2.

## Proof

**Step 1: the whole-carrier adapter.**
For every $x\in\mathbb F_q$,
$\iota(ax)=a^{-1}\iota(x)$: this follows from multiplicative inversion
when $x\ne0$, and both sides are zero when $x=0$. Therefore
$$
T_{a,b}S_a(x,y)
=(ay,(a^2y+b)a^{-1}\iota(x))
=S_aT_{1,b/a^2}(x,y).
$$
The map $S_a$ is bijective with inverse $S_{a^{-1}}$, so this is a
conjugacy on the entire affine plane, not only on the rational open locus.

**Step 2: every-target fibres.**
If $T_{a,b}(x,y)=(u,v)$, then $y=u$ and
$$(au+b)\iota(x)=v.$$
At $u=-b/a$, all $q$ possible $x$ work if $v=0$ and none work if $v\ne0$.
At $u\ne-b/a$, the coefficient $au+b$ is nonzero. If $v=0$, the only
solution is $x=0$. If $v\ne0$, the only solution is
$x=(au+b)/v$, which is nonzero. Consequently
$$
|T_{a,b}^{-1}(u,v)|=
\begin{cases}
q,&(u,v)=(-b/a,0),\\
0,&u=-b/a,\ v\ne0,\\
1,&u\ne-b/a.
\end{cases}
$$
The image size is $q(q-1)+1$. The maximum fibre is uniquely $q$.
This is the same case split as P150's inverse equation; moving the
exceptional first coordinate is not an independent inverse mechanism.

**Step 3: exact subtraction at the five-period parameter.**
If $b=a^2$, step 1 gives $T_{a,a^2}S_a=S_aL$. All pointwise entry times,
least periods, component incidence, and fibre sizes are transported by this
bijection. P150 already gives the disjoint all-plane partition into a
recurrent generic locus, the recurrent coordinate axes, and three
exceptional layers of exact depths $1,2,3$. Its manuscript also proves the
cycle census and the complete exceptional in-tree. Thus nonzero rescaling
does not yield a new temporal or inverse theorem.

**Step 4: why the elliptic statement does not close the affine problem.**
On a finite group $G$, a translation $P\mapsto P+Q$ is bijective with
inverse $P\mapsto P-Q$. If $d$ is the order of $Q$, cancellation shows that
$P+tQ=P$ exactly when $tQ=0$, so every point has period $d$ and there are
$|G|/d$ cycles. This elementary conclusion applies when the source provides
a genuine smooth projective elliptic-curve group and the Lyness extension
is the stated translation. It does not give the affine boundary
convention. In fact step 2 proves that $T_{a,b}$ has a fibre of size $q>1$,
so it is not a permutation of $\mathbb F_q^2$. Its fibres cannot be replaced
by the singleton fibres of a translation. No claim is made that all
remaining $b$ are conjugate to P150.

## Original proof read boundary

Actually read P150 main.tex lines 1–435, including the definition, partition
proof, five iterates, exceptional arrows, exact tails, cycle proofs and
every-target inverse proof through the complete exceptional component.
Later controls/declarations, verifier and canonical output were not audited
or replayed. Also read the old algebraic replacement SCOUT.md lines 1–135,
as provenance for the existing ZTL literal, not as a substitute for proof.

The two after-reading pins are in INPUT_PINS_NATIVE.json. They are
after-reading observations, not a claimed before/after bracket.

## Primary source and scope

Hone, *Efficient ECM factorization in parallel with the Lyness map*,
arXiv:2002.03811, actual PDF text through extracted line 447 (pp. 1–3
and the opening portion of p. 4) was returned and read. Later projective
formulae and the complete seven-page PDF were not read. Equations (2),
(4), (15), and (19) distinguish the rational formula, nonzero rescaling,
curve translation, and exceptional base points. This source is background;
the all-affine adapter above is proved directly.
[Author preprint](https://arxiv.org/pdf/2002.03811).

The accompanying *ECM factorization with QRT maps* record was read only at
metadata/abstract level, not as another proof input.
[Author record](https://arxiv.org/abs/2001.09076).
Additional search snippets, including 2026 cluster-deformation material,
are navigation only. Six bounded name/formula/singularity/recent queries
do not establish exhaustive coverage or source absence.

## Corrections, exclusions and open risks

The hypothesis $a\ne0$ is essential to this adapter; the $a=0$ family is not
another entrance in this task. The proof is not a universal conjugacy for
all $b$. Generic rational periodicity is not asserted across zero
denominators. No new all-carrier recurrent classification for
$b/a^2\ne1$ was proved. Reopening that direction would require a separately
specified residual contract and actual source subtraction; no experiment
is justified by this desk alone.
