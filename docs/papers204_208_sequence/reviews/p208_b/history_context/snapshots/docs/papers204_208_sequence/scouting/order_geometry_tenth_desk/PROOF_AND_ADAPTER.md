# Tenth desk — exact reductions and failed whole-system adapters

2026-09-06 UTC. Author of this new desk algebra: `batch197_lzk_gate`.
Definitions are the unchanged three literals in
[the main scout's declaration](../order_geometry_tenth/DESK_DECLARATION.md).
This is scouting after the P207 A seal, not a contribution to that paper.

**Later same-day supplements:** the initial no-global-OFS-claim statements
below are preserved as the earlier desk boundary. The subsequently written
[protected-cell/fibre proof](OFS_RECURSION_AND_FIBRES.md) and
[temporal check](OFS_TEMPORAL_CHECK.md) now supply all-size OFS deductions.
They do not undo the explicit failed guesses here, clear the source/value
gate, or create a manuscript-review verdict.

## Claim and status

The claims proved here are the QAS polynomial factor identities, the DTC
full-carrier scalar/similarity reduction and elementary source decoder,
and explicit OFS obstructions to several proposed classical conjugacies.
These limited claims are **PROVABLE AS STATED**. An all-prime QAS or DTC
temporal classification, or an all-polygon OFS recurrence/fibre theorem,
is **NOT CURRENTLY JUSTIFIED** by this desk.

All finite-field formulas use the declared full labelled carriers over
the prime field $\mathbf F_p$. Repeated, collinear and isotropic vertices
are included. No positivity, norm division, new sink or extra pilot box
is introduced. Triangulations have the declared cyclic vertex labels.

## Strategy and dependencies

1. QAS: bilinearity of the determinant and the two-dimensional Plücker
   identity give a polynomial area factor. An explicit full-carrier
   example refutes scalar homothety. No temporal theorem follows from
   the factor alone.
2. DTC: anchor/edge coordinates are a full bijective change of variables;
   the two-dimensional dot/determinant identity gives a cubic base and
   a matrix product above it. Rank-one affine lifting gives the inverse,
   including all singular branches.
3. OFS: retain the actual original-diagonal schedule. Hand-computed
   quadrilateral/pentagon flips disprove named bijective/descending
   identifications. Reverse-flip traces are generic static information.

The mathematical arguments below do not assume a finite census. The
separate integer-polynomial checker confirms 23 coefficient identities
and is not a finite-state pilot.

## 1. QAS: a genuine factor, not a full scalar homothety

The literal is

$$A_i=\det(v_{i+1}-v_i,v_{i-1}-v_i),\qquad
v_i'=v_i+A_i(v_{i+1}+v_{i-1}-2v_i),$$

with indices modulo four. Put

$$H=A_0+A_2=A_1+A_3
 =\det(v_2-v_0,v_3-v_1),$$
$$D=A_2-A_0,\qquad E=A_1-A_3,\qquad
W=v_1+v_3-v_0-v_2,$$
$$\alpha=1-H,\qquad\gamma=1-3H,\qquad R=D^2+E^2.$$

Then the exact polynomial identities are

$$W'=\gamma W,$$
$$H'=H\alpha^2-\alpha(D^2+E^2),\qquad
D'=\gamma\alpha D,\qquad E'=\gamma\alpha E,$$
$$R'=\gamma^2\alpha^2R.$$

Thus $(H,R)$ is a closed two-scalar polynomial factor; the direction
$[D:E]$ persists when the common multiplier is nonzero. This is neither
a claim that $(H,R)$ determines the original quadruple nor a proof of
the factor's all-prime functional graph.

### 1.1 Direct derivation

First work over the rational function field in the eight vertex
coordinates, so division by two is legitimate without any geometric
nondegeneracy assumption. Write

$$v_0=c+u,\quad v_2=c-u,\quad
v_1=d+z,\quad v_3=d-z,\quad w=d-c,$$
$$h=2\det(u,z),\quad r=2\det(w,z),\quad
s=2\det(u,w).$$

Determinant expansion gives

$$A_0=h-r,\quad A_2=h+r,\quad
A_1=h+s,\quad A_3=h-s.$$

In particular $H=2h$, $D=2r$, $E=2s$, and $W=2w$.
The literal updates now give

$$c'=c+2hw+2ru,\qquad d'=d-2hw-2sz,$$
$$u'=(1-2h)u-2rw,\qquad z'=(1-2h)z-2sw.$$

The two-dimensional identity

$$\det(w,z)u+\det(u,w)z=\det(u,z)w$$

means $ru+sz=hw$. Consequently

$$w'=d'-c'=(1-6h)w.$$

Substitution into the three determinant definitions yields

$$h'=h(1-2h)^2-2(1-2h)(r^2+s^2),$$
$$r'=(1-6h)(1-2h)r,\qquad
s'=(1-6h)(1-2h)s.$$

For example, the first identity follows by expanding
$2\det((1-2h)u-2rw,(1-2h)z-2sw)$; the last cross-term
vanishes since $\det(w,w)=0$. For the second identity, expand
$2\det((1-6h)w,(1-2h)z-2sw)$; the term containing
$\det(w,w)$ again vanishes. The third follows by expanding
$2\det((1-2h)u-2rw,(1-6h)w)$.
Replacing $2h,2r,2s,2w$ by $H,D,E,W$ proves all displayed claims.

Each final identity is an equality of polynomials with integer
coefficients in the original eight coordinates. Equality in their
rational function field implies that every integer coefficient of the
difference is zero. Reduction modulo any prime therefore proves the
same identities also at $p=2$. This does not divide by two in a field
of characteristic two.

### 1.2 Explicit limits of the reduction

On the parallelogram subfamily $w=0$, both half-diagonals are scaled by
$1-2h$. That subfamily cannot represent the whole carrier. For example,
over $\mathbf F_3$ use

$$v=((0,0),(1,0),(0,1),(0,0)).$$

Its areas are $(0,1,1,0)$ and its image is

$$v'=((0,0),(2,1),(1,2),(0,0)).$$

Any common affine homothety must have translation zero because it fixes
$v_0=(0,0)$. It would send $(1,0)$ to a scalar multiple of $(1,0)$,
contrary to the displayed image. The two initially perpendicular edge
vectors also acquire nonzero dot product, so this example is not even a
common dot-product similitude. These are literal counterexamples, not
an exclusion of every possible nonlinear conjugacy.

The diamond $((1,0),(0,1),(-1,0),(0,-1))$ has every $A_i=2$ and
is sent to $-3$ times itself. Over $\mathbf F_3$ it collapses to the
constant zero quadruple. Over characteristic zero its side determinants
change from $1$ to $9$. Therefore QAS is not the literal side-area-
preserving centroaffine correspondence from the source audit. In
particular, that correspondence's regular-domain recurrence cannot be
imported by naming the same Plücker identity.

What remains: classify the actual coupled polynomial factor, lift its
orbits through the full vertex recurrence, and prove a separate evaluated
inverse or extremal theorem. None is supplied by the factor calculation.

## 2. DTC: full-carrier cubic base and elementary inverse

The literal is

$$B_i=(v_{i+1}-v_i)\mathbin\cdot(v_{i-1}-v_i),\qquad
v_i'=v_i+B_i(v_{i+1}-v_{i-1}),$$

with indices modulo three. Use the bijective coordinates

$$o=v_0,\quad x=v_1-v_0,\quad y=v_2-v_0,$$
$$a=x\cdot x,\quad b=y\cdot y,\quad c=x\cdot y,
\quad\Delta=\det(x,y),\quad J(s,t)=(-t,s).$$

The update is exactly

$$o'=o+c(x-y),$$
$$x'=(1-c)x+ay=(I+\Delta J)x,$$
$$y'=-bx+(1+c)y=(I+\Delta J)y.$$

Indeed $(B_0,B_1,B_2)=(c,a-c,b-c)$ gives the first forms by subtraction.
The coordinate identities
$ay-cx=\Delta Jx$ and $cy-bx=\Delta Jy$ give the second forms.
No determinant or norm is divided out.

Set $M_\Delta=I+\Delta J$ and $s_\Delta=1+\Delta^2$.
Since $J^2=-I$ and $J^{\mathsf T}=-J$,

$$\det M_\Delta=s_\Delta,\qquad
M_\Delta^{\mathsf T}M_\Delta=s_\Delta I.$$

Therefore

$$\Delta'=\Delta+\Delta^3,\qquad
(a',b',c')=s_\Delta(a,b,c).$$

These identities hold also in characteristic two. The entire edge
evolution is an explicitly specified matrix product over the cubic
scalar map. A description that merely enumerates that scalar map's
cycles and multiplies its matrices has not proved an all-prime rigid
temporal theorem.

### 2.1 Geometric centre and all singular branches

When $\Delta\ne0$, put

$$H=o+\frac c\Delta J(x-y).$$

Then $(H-o)\cdot x=(H-o)\cdot y=c$, precisely the two
independent altitude equations. This proves that $H$ is the algebraic
orthocenter. Also $-\Delta J(H-o)=c(x-y)$, hence

$$v_i'=H+M_\Delta(v_i-H)\quad(i=0,1,2).$$

If $s_\Delta\ne0$, the image is noncollinear and the similitude
preserves orthogonality, so the image has the same orthocenter $H$.
If $s_\Delta=0$, the same polynomial update remains valid, but its
matrix has rank one and the image is collinear. No noncollinear
orthocenter formula is asserted at the next step.

If $\Delta=0$, the edge vectors are unchanged. The complete map is
the rigid translation $o\mapsto o+c(x-y)$, with constant translation
vector along its orbit. Its period is one if this vector is zero and
$p$ otherwise. This includes repeated vertices and isotropic lines.
For example, over $\mathbf F_3$, $(o,x,y)=(0,(1,0),(2,0))$ has
nonzero translation $(1,0)$, so dropping the degenerate stratum would
erase genuine three-cycles. Over $\mathbf F_2$ the collinear
translation is always zero: a line has only two vectors, so either one
edge vanishes or the two edges agree.

### 2.2 Every source follows from cubic roots and rank-one lifting

Fix a target $(o',x',y')$ and put $\delta'=\det(x',y')$.
Each source must have area $\delta$ satisfying

$$\delta+\delta^3=\delta'.$$

If $s_\delta\ne0$, there is exactly one source for this root:

$$x=M_\delta^{-1}x',\qquad y=M_\delta^{-1}y',\qquad
o=o'-(x\cdot y)(x-y).$$

Its area equals $\delta'/s_\delta=\delta$, so these are
indeed consistent source coordinates. Distinct roots give distinct
sources. If $\delta'\ne0$, every root is of this nonsingular kind,
and the fibre is exactly the number of roots of the cubic, at most
three. For a collinear target the root $\delta=0$ always contributes
one source.

The remaining roots obey $\delta^2=-1$, hence $\delta\ne0$.
The matrix $M_\delta$ has rank one: its determinant is zero but its
diagonal entries are one. Write $L_\delta=\operatorname{im}M_\delta$
and choose a nonzero kernel vector $k$. Unless both target edges lie
in $L_\delta$, this root contributes no source. If they do, choose
any lifts $x_0,y_0$; all lifts have the unique form

$$x=x_0+\mu k,\qquad y=y_0+\nu k.$$

The remaining area equation is

$$\det(x_0,y_0)+\mu\det(k,y_0)
 +\nu\det(x_0,k)=\delta.$$

If $x'=y'=0$, every lift lies in the one-dimensional kernel, so no
lift has nonzero area $\delta$. Otherwise at least one lift lies
outside the kernel; at least one displayed coefficient is nonzero.
Thus there are exactly $p$ solutions of this one nonzero affine
equation in two scalar variables, and each determines its anchor
uniquely. This proof also covers $p=2$.

For odd $p$, when the two singular roots exist, their image lines are
distinct isotropic lines. Indeed
$J M_\delta=-\delta^{-1}M_\delta$ at a singular root, so their
eigenvalues are different. A nonzero target edge cannot belong to
both image lines. At $p=2$ there is only one singular root. Therefore
a collinear target has fibre $p+1$ exactly when its edges are not both
zero and lie in one singular image line; every other collinear target
has fibre one. This is an evaluated full-carrier source formula, but
its mechanism is only polynomial-root counting plus elementary
rank-one affine lifting. It is explicitly deducted, not offered as a
new independent inverse axis.

### 2.3 Exact collision boundary

ORT slides $(A,B,C)$ to $(B,C,H)$ on noncollinear anisotropic triangles
with an added sink. OT replaces vertices by opposite-side perpendicular
feet with a zero-norm retention rule. PDU is projective adjugation.
DTC is none of these literals. Their periods and exceptional counts
do not transfer.

The stronger reason to stop is structural: the displayed full-carrier
change of coordinates reduces the only unclosed temporal question to
the cubic base and its matrix/translation lift, while the whole inverse
is already elementary. The old CSP scout explicitly rejected the same
logical shortcut of treating an unresolved nonlinear scalar factor as
a proved temporal theorem. This is a proof/value boundary, not a claim
that CSP has the same scalar polynomial as DTC.

## 3. OFS: actual sweep, not classical rotation or plain pop-stack

Each unvisited original diagonal remains present until its own visit:
a flip removes only the chosen diagonal. Thus the declaration's
presence condition never skips an unvisited member, and every update
performs exactly $n-3$ flips. Every inserted diagonal crosses the
chosen original diagonal, so it cannot be any member of the initial
triangulation. Thus a visited original diagonal cannot reappear.
New diagonals never extend the original list.

**Explicit correction:** the earlier version of this paragraph said
"A previously visited diagonal can reappear." That warning is valid
for more general dynamic schedules but false for this original-only
schedule, by the preceding crossing argument. The failed assertion is
retained here as a correction rather than silently erased. The fan
protection and later recursive proofs use the correct stronger fact.

### 3.1 Hand witnesses

On a quadrilateral the two triangulations are exchanged. On a pentagon
write $ij$ for the internal diagonal with endpoints $i,j$. The five
triangulations and their literal sweeps are:

| Source | Ordered actual flips | Target |
|---|---|---|
| $\{02,03\}$ | $02\to13$, then $03\to14$ | $\{13,14\}$ |
| $\{02,24\}$ | $02\to14$, then $24\to13$ | $\{13,14\}$ |
| $\{03,13\}$ | $03\to14$, then $13\to24$ | $\{14,24\}$ |
| $\{13,14\}$ | $13\to24$, then $14\to02$ | $\{02,24\}$ |
| $\{14,24\}$ | $14\to02$, then $24\to03$ | $\{02,03\}$ |

Each row follows by listing the two triangles adjacent to the recorded
diagonal in the current pentagon, not in the initial pentagon. The
first two rows alone prove noninjectivity. Thus OFS cannot be
conjugate to polygon rotation or to any bijective promotion action.
The table also shows the labelled two-cycle
$\{02,24\}\leftrightarrow\{13,14\}$ and the three-step tail
from $\{03,13\}$. These are hand calculations, not new executed pilot
rows or an all-$n$ claim.

For a finite lattice the ordinary pop-stack operator is

$$\operatorname{Pop}(x)=\bigwedge
 (\{x\}\cup\{y:y\lessdot x\}).$$

It satisfies $\operatorname{Pop}(x)\le x$; every nonminimal element
has a lower cover, making the inequality strict. Therefore its only
recurrent state is the minimum. The quadrilateral two-cycle excludes
any conjugacy of full OFS with this operator. A composite of a
noninvertible sorting operation and rotation is a different question;
no such complete adapter is established or ruled out here.

### 3.2 What the generic flip inverse supplies

If the whole original ordered diagonal list is provided as a trace,
the update can be reversed one flip at a time. At a reverse step for
an old diagonal $d$, an admissible current triangulation must contain
exactly one diagonal crossing $d$; flipping that diagonal back to
$d$ restores the immediately preceding triangulation. Require the
finally reconstructed diagonal set to equal the recorded original
list and verify the declared forward schedule. These checks are
necessary and sufficient for the trace to describe a source.

Enumerating all possible original lists and applying this generic
trace check supplies a static inverse search, not an evaluated
targetwise fibre theorem or maximum. No global time bound, recurrent
classification or separate evaluated inverse has been proved here.
Q09, C14, TFE and LDL use different explicit selectors; their clocks
cannot be silently imported into this full recorded sweep.

### 3.3 A proved all-size phase factor, not convergence

For $n\ge4$, let $\epsilon(T)$ be one if vertex $0$ is an ear and
zero otherwise. Then

$$\epsilon(\operatorname{OFS}(T))=1-\epsilon(T).$$

If vertex $0$ is initially not an ear, list its neighbors in order as
$1=a_0<a_1<\cdots<a_r=n-1$, where $r\ge2$. The first scheduled flips
are precisely $(0,a_1),\ldots,(0,a_{r-1})$. At the $i$th such flip,
the two adjacent triangles are $(0,1,a_i)$ and $(0,a_i,a_{i+1})$:
the first is the original first triangle at $i=1$, and thereafter it
was formed by the preceding flip. Thus this flip creates $(1,a_{i+1})$.
The last creates $(1,n-1)$, which makes vertex $0$ an ear. Each of
these new diagonals crosses the old diagonal just removed, so none
belonged to the original triangulation. In particular $(1,n-1)$ is
not scheduled later and remains to the end.

If vertex $0$ is initially an ear, no original diagonal has endpoint
$0$, and $(1,n-1)$ is original. Its vertex-$1$ fan is now processed
first. With neighbors $0,2=b_0<b_1<\cdots<b_s=n-1$, the intermediate
flips $(1,b_i)$ for $i<s$ create $(2,b_{i+1})$ by the same adjacent-
triangle induction. The last flip, at $(1,n-1)$, has opposite vertices
$0$ and $2$ and creates $(0,2)$. This new diagonal was not original,
so it remains and makes vertex $1$ an ear in the output. The removed
$(1,n-1)$ cannot reappear: a diagonal crossing it must have endpoint
$0$, and the remaining scheduled diagonals have no such endpoint.
Thus vertex $0$ is not an ear in the output.

The factor proves every OFS period is even for $n\ge4$, and proves
that every first image has an ear at $0$ or $1$. It does not prove
that the period is two, that there is one recurrent component, or
that the height is $n-2$. Those remain separate obligations.

### 3.4 Corrected static avoidance count; literal image guess refuted

The main scout proposed a recursive full-binary-tree encoding rooted
at polygon edge $(0,n-1)$. Its accompanying possible image class is
the class of full binary trees avoiding a subtree
$((e,N),B)$ where $e$ is a leaf and $N$ is not a leaf. This subsection
counts that independently defined class, and does **not** identify
it with the OFS image. The proposed literal identification was later
refuted in the unchanged $n=6$ box, as recorded below.

Let $F(z)$ count the avoidance class by internal vertices, including
the leaf with weight one. Both subtrees must themselves avoid the
pattern. Among such possible left subtrees, exactly those of form
$(e,N)$ with $N\ne e$ are forbidden, contributing $z(F-1)$. Hence

$$F=1+z\bigl(F-z(F-1)\bigr)F
 =1+z(1-z)F^2+z^2F.$$

This recursively determines all coefficients starting with
$1,1,2,4,9,22,57,154,429$. If $C(w)=1+wC(w)^2$ is the Catalan
series, substitution gives

$$F(z)=\frac{1}{1-z^2}
 C\!\left(\frac{z}{(1-z)(1+z)^2}\right).$$

This is the displayed $k=2$ specialization of Mansour's Corollary
2.1. Its count is therefore explicitly deducted as old static
enumeration. Even a proof that OFS has exactly this image would still
need a separate analysis of what new mechanism remains after this
deduction; matching a sequence alone is not an adapter.

In fact the standard rooted-tree word dictionary
$W((L,R))=U W(L)D W(R)$ does not identify the image with this class.
At $n=6$, the source $\{03,04,13\}$ has the literal hand sweep

$$03\longmapsto14,\qquad04\longmapsto15,
\qquad13\longmapsto24,$$

so $\{14,15,24\}$ is an image. Its rooted tree is
$(e,((e,(e,e)),e))$, with word $UDUUDUDD$; it contains the forbidden
subtree $((e,(e,e)),e)$ and the word factor $UUDU$. The three flips
respectively use quadrilaterals with vertex sets
$\{0,1,3,4\}$, $\{0,1,4,5\}$ and $\{1,2,3,4\}$, verifying
the witness without relying on the finite census. The main scout's
actual tree follow-up independently reports this same first mismatch.
Thus the literal image equality is **REFUTED**, although the static
class and its generating function remain well-defined. Any alternative
bijection is a new obligation, not an unrecorded repair.

A prior exploratory guess here used
$F_{\rm bad}=1/(1-z-z^2C(z))$, corresponding to an unrestricted
Catalan decoration. Its coefficients begin
$1,1,2,4,9,22,58$, and its coefficient at internal size six conflicts
with the actual main-scout OFS image count $57$ at polygon size eight.
That guess is **REFUTED**, not silently repaired into a proof. No
scientific input or pilot cutoff was changed in making this correction.

## Corrections and open risks

- QAS: the triangle common-area homothety does not extend to the full
  four-point carrier. Only the displayed factor is proved.
- DTC: nonzero area is not invariant at singular multipliers; the
  collinear translation branch must remain. The complete inverse is
  elementary and does not repair the unresolved all-prime time axis.
- OFS: local flip reversibility does not make the state-dependent
  whole sweep bijective. Plain rotation, bijective promotion and plain
  finite-lattice pop-stack are excluded, not every conceivable adapter.
- No source no-hit is novelty clearance. No candidate is admitted,
  numbered or reserved by this desk. Any future paper using these new
  QAS/DTC lemmas must record this worker as a proof contributor, not
  assign it independent manuscript review.
