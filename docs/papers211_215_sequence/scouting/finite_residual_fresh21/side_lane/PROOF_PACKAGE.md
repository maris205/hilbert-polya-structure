# Recutting side lead: finite-carrier obstruction

2026-09-11 UTC. Author: /root/round211_functional_surgery_residual/fresh21_finite_lane.
This is source authorship and hand deduction, not independent review or admission.

## Claim and status

**PROVABLE AS STATED:** the source's elementary centroaffine recutting
formula does not define a total update on the finite set of labelled
quadrilaterals over $\mathbf F_5$ with all adjacent determinants nonzero.
Consequently the prescribed cyclic sweep cannot be imported to that whole
carrier without an additional, non-source totalization convention.

**NOT CURRENTLY JUSTIFIED:** any fresh all-parameter temporal theorem or
materially separate fibre theorem for a finite autonomous recutting system.
No replacement convention, invariant subcarrier, or new literal is proposed.

## Assumptions, notation and source

Write $[A,B]=a_1b_2-a_2b_1$. The finite carrier considered only for this
source-import check is
$$
C=\{(P_1,P_2,P_3,P_4)\in(\mathbf F_5^2)^4:
[P_i,P_{i+1}]\ne0\ \text{for every cyclic }i\}.
$$
Arnold–Fuchs–Tabachnikov's displayed reflection formula (9) is
$$
R_{A,B}(X)=\frac{[A,X]A+[X,B]B}{[A,B]}.
$$
Their Section 3.2 replaces $P_j$ by $R_{P_{j-1},P_{j+1}}(P_j)$ and
composes the elementary operations in order $1,2,\ldots,n$.
The original source uses real/complex geometry; reduction to this finite
carrier is the desk's proposed source-import check, not a published theorem.
Source: [arXiv v1, formula (9) and Section 3.2](https://arxiv.org/html/2112.08124v1).
See raw/web05.json and raw/web04.json for actual returned text.

## Strategy and dependency map

Direct counterexample. Carrier membership uses four $2$ by $2$ determinants.
Undefinedness uses the source denominator and a nonzero numerator.
A second linearity check rules out interpreting the missing division as an
unambiguous linear reflection swapping the same two frame vectors.
No finite enumeration, program, external theorem, or source figure is used.

## Proof

1. Choose
$$
P_1=(0,1),\quad P_2=(2,0),\quad P_3=(0,2),\quad P_4=(1,0).
$$
Their successive determinants are $-2,4,-2,1$, which reduce to
$3,4,3,1$ in $\mathbf F_5$. All are nonzero, hence this tuple belongs to $C$.

2. The very first elementary recutting uses $A=P_4=(1,0)$ and
$B=P_2=(2,0)$. These vectors have $[A,B]=0$. At $X=P_1=(0,1)$, its
numerator is
$$
[A,X]A+[X,B]B=(1,0)-2(2,0)=(-3,0)=(2,0)\ne(0,0).
$$
Formula (9) therefore requires division of a nonzero vector by zero.

3. When $[A,B]\ne0$, formula (9) interchanges $A$ and $B$.
No linear map can interchange the present $A$ and $B=2A$:
if $R(A)=2A$, linearity gives $R(B)=2R(A)=4A$, whereas interchange would
require $R(B)=A$. Since $4A\ne A$ in $\mathbf F_5^2$, this is impossible.

Thus the source operation is undefined at the first scheduled step of an
element of $C$. The cyclic sweep is not a total map on $C$. $\square$

## Corrections, missing assumptions and limits

The statement concerns this explicit carrier only. It does not prove that
every finite-field recutting carrier fails, nor that no regular invariant
subcarrier exists. Establishing one would be a new obligation, not a consequence
of the word integrable. No singular skip, sink, projective completion, coordinate
power replacement, or post-hoc restriction is authorized or introduced here.

On any finite subcarrier on which all the source involutions are everywhere
defined and preserve the subcarrier, reversing the involution order gives
the sweep's inverse. That conditional observation is generic composition
bookkeeping; singleton fibres obtained from it are not a separate theorem
mechanism. No period classification is deduced from the published invariants.

## Open risks

No open step remains in the displayed counterexample. Source reading is an
HTML excerpt read, not a full-paper/PDF/figure/proof audit. The original
unarchived truncated read01 remains a documentary limitation; later exact
bounded reads do not reconstruct it.
