# OFS temporal deduction checked through the protected-cell recursion

2026-09-06 UTC. The main scout `batch197_fosp_gate` supplied the $K$-map
route and sharp witness. This desk `batch197_lzk_gate` checked its closure,
small cases, parity bounds and sharpness in the representation below.
Both workers are proof contributors, not independent manuscript reviewers.

## Exact claim and status

Conditional only on the all-size protected-cell recursion proved in
[OFS_RECURSION_AND_FIBRES.md](OFS_RECURSION_AND_FIBRES.md), this deduction
is **PROVABLE AS STATED**: the declared labelled polygon OFS has one
fixed state for $n=3$, exactly one two-cycle for each $n\ge4$, and
maximum entry time $n-2$ for $n\ge5$. The two quadrilateral states are
already recurrent, so their maximum entry time is zero. No larger pilot
or external source theorem is used to prove these all-size statements.

All tree sizes $N$ in this document are **numbers of leaves**, so
$N=n-1$. This differs from the internal-node variable $m=n-2$ in the
fibre formula. A leaf $e$ has $N=1$ and serves only as an auxiliary base.
Let $L_l$ be the left comb with $l$ leaves, put $c=L_2=(e,e)$, and
write $j(S,A)=\operatorname{first}(S,A)$. The exact $F,G,P$ are the
maps defined in the recursion document; in particular $G(B)=F((e,B))$.

## 1. Two elementary identities from the exact recursion

For $l\ge2$, define

$$D_l(R)=j(G(R),L_{l-1}).$$

The recursion gives

$$F((L_l,R))=(e,D_l(R)),\qquad
G((L_l,R))=(c,D_l(R)).\tag{1}$$

To verify the product in this formula, the left-spine list is
$e^{l-1}R$. For $l=2$, its product is $F((e,R))=G(R)$.
For $l>2$, the all-leaf initial block has output $L_{l-1}$, and
the last gluing replaces the first leaf of $G(R)$ by that left comb.
This covers $R=e$ as well. In particular

$$G((c,R))=(c,G(R)).\tag{2}$$

Every $G(B)$ for a nonleaf $B$ has the form $(L_l,Q)$ with $l\ge2$;
the only exception to this left-nonleaf form is $G(e)=c$. Thus (1)
shows that there is a unique leaf-count-preserving map $K$ such that

$$G^2(B)=(c,K(B))\quad\text{for every }B.\tag{3}$$

Here $K(e)=e$. More explicitly, if $G(B)=(L_l,Q)$ with $B\ne e$,
then

$$K(B)=D_l(Q)=j(G(Q),L_{l-1}).\tag{4}$$

Associativity of composition and (2) imply commutation:

$$G^2(G(B))=G(G^2(B))=G((c,K(B)))=(c,G(K(B))),$$

which compared with (3) at $G(B)$ gives

$$KG=GK.\tag{5}$$

For $X=(L_l,R)$ with $l\ge2$, (1) and (4) give

$$K(X)=G(D_l(R)),\qquad
K((c,R))=(c,K(R)).\tag{6}$$

## 2. The closed $K$-class and its clock

For $N\ge3$, let

$$\mathcal C_N=\{(L_l,R):l\ge2,\ l+|R|=N\},$$

where $|R|$ denotes leaf count. Set $\mathcal C_1=\{e\}$ and
$\mathcal C_2=\{c\}$ as auxiliary base classes.

First, $K$ maps every tree with $N\ge3$ leaves into $\mathcal C_N$.
Indeed use (4). If $Q$ is nonleaf, $G(Q)$ already has a nonleaf left
comb and first-leaf substitution by $L_{l-1}$ preserves that property.
If $Q=e$, (4) gives $K(B)=L_l$, and size $N\ge3$ forces $l=N\ge3$.

Second,

$$K(\mathcal C_N)\subseteq\{(c,Y):Y\in\mathcal C_{N-2}\}
 \quad(N\ge3).\tag{7}$$

For $N\ge4$, the tree $D_l(R)$ in (6) lies in
$\mathcal C_{N-1}$. If $R=e$, it is $L_l$ with $l=N-1\ge3$;
if $R$ is nonleaf, $G(R)$ has a nonleaf left comb and the substitution
only lengthens it. Applying the second identity of (1) to this tree
gives root $c$. Its right child is again of the form $D_s(Q)$.
The same two-case reasoning places this child in $\mathcal C_{N-2}$
whenever $N-2\ge3$. At $N=4$ the right child has two leaves and is
necessarily $c$. At $N=3$, $\mathcal C_3=\{L_3\}$ and direct
use of (1) gives $K(L_3)=L_3=(c,e)$. Thus no small case is omitted.

Define the canonical trees

$$Z_1=e,\quad Z_2=c,\quad Z_N=(c,Z_{N-2})\quad(N\ge3).$$

Equation (6) shows they are $K$-fixed. By (7), every member of
$\mathcal C_N$ reaches $Z_N$, and (6) then reduces its subsequent
clock to the smaller right child. Induction gives

$$d_K(X)\le\left\lfloor\frac{N-2}{2}\right\rfloor
 \quad(X\in\mathcal C_N,\ N\ge3).\tag{8}$$

The bases $N=3$ and $N=4$ have bounds zero and one. For $N\ge5$,
one application enters $(c,\mathcal C_{N-2})$, giving
$1+\lfloor(N-4)/2\rfloor=\lfloor(N-2)/2\rfloor$.
As arbitrary trees enter $\mathcal C_N$ in one step,

$$d_K(B)\le\left\lfloor\frac N2\right\rfloor\quad(N\ge3).\tag{9}$$

The one- and two-leaf auxiliary trees are already fixed. This proves
that $Z_N$ is the unique recurrent state of $K$ at each leaf count,
not merely one possible fixed point.

## 3. Transfer to $F$ and the unique two-cycle

For all $R$, the exact recursion and (4) give

$$F^2((e,R))=(e,K(R)).\tag{10}$$

For every tree $T$ whose left child is nonleaf, not only for
$T\in\mathcal C$, let $P_T=P(\operatorname{LS}(T))$. The recursion
gives $F(T)=(e,P_T)$ and $G(T)=(c,P_T)$, hence

$$F^2(T)=G(P_T)=K(T).\tag{11}$$

Every first image has either the form $(e,R)$ or belongs to
$\mathcal C_N$. The former evolves by (10), and the latter by (11).
The unique $K$ limit and (5) imply $G(Z_N)=Z_{N+1}$: commutation
makes $G(Z_N)$ $K$-fixed at the next leaf count, where the fixed point
is unique. It follows that for $N\ge3$ the two trees

$$Z_N\quad\text{and}\quad A_N=(e,Z_{N-1})\tag{12}$$

are exchanged by $F$. They are distinct since $Z_N$ has a nonleaf
left child while $A_N$ has a leaf there. Equations (8)–(11) show that
every orbit enters this pair. Thus there is exactly one two-cycle and
no other recurrent state. At $N=2$, the triangle $c$ is fixed.

## 4. Uniform upper bound, including the necessary odd phase

For a first-image state in $\mathcal C_N$, (8) and (11) give
an $F$ entry-time bound $2\lfloor(N-2)/2\rfloor\le N-2$.
For a first-image state $(e,R)$, where $|R|=N-1$, the even iterates
give the bound $2\lfloor(N-1)/2\rfloor$ by (9)–(10). The odd
iterates satisfy, using commutation,

$$F^{2t+1}((e,R))=G(K^t(R))=K^t(G(R)).$$

Since $G(R)\in\mathcal C_N$ for $N\ge3$, they give the independent
bound $1+2\lfloor(N-2)/2\rfloor$. Taking the smaller bound yields

$$\min\left\{2\left\lfloor\frac{N-1}{2}\right\rfloor,
 1+2\left\lfloor\frac{N-2}{2}\right\rfloor\right\}=N-2.$$

For $N=3$, $R$ has two leaves and is already $K$-fixed, so the same
upper bound remains valid using that base directly. Therefore every
first-image state enters the two-cycle in at most $N-2$ further
steps, and every original state enters in at most

$$N-1=n-2.\tag{13}$$

Using only the even clock would miss the required improvement for odd
$N$; the commuting odd representation is essential to this upper bound.

## 5. Sharp witness and the two parity cases

Put $S_3=(e,c)$, the right comb on three leaves, and recursively
$S_{N+1}=(S_N,e)$ for $N\ge3$. Thus $S_N$ is a right comb of three
leaves followed by left-comb attachments of $N-3$ leaves.

Directly from its left-spine list, for $N\ge4$,

$$F(S_N)=(e,S_{N-1}),\qquad G(S_N)=(c,S_{N-1}).$$

Also $G(S_3)=L_4$. Hence

$$K(S_4)=L_4,\qquad
K(S_N)=(c,S_{N-2})\quad(N\ge5).\tag{14}$$

Let $C(Y)=(c,Y)$, so (6) says $KC=CK$. For every $N\ge4$, the
left child of $S_N$ is nonleaf and (11) applies, including before it
has entered $\mathcal C_N$.

If $N=2k\ge4$, (14) gives

$$F^{N-2}(S_N)=K^{k-1}(S_N)=C^{k-2}(L_4).$$

This is not $Z_N=C^{k-2}(Z_4)$ because $L_4\ne Z_4=(c,c)$.
Its left child is nonleaf, so it is not $A_N$ either.

If $N=2k+1\ge5$, (14) first gives
$K^{k-1}(S_N)=C^{k-1}(S_3)$. Equation (1), followed by repeated
use of (2), now gives

$$F^{N-2}(S_N)
 =F(C^{k-1}(S_3))=(e,C^{k-2}(G(S_3)))
 =(e,C^{k-2}(L_4)).$$

This is not $A_N=(e,C^{k-2}(Z_4))$ because again $L_4\ne Z_4$,
and it is not $Z_N$ because its left child is a leaf.

Thus in both parities the witness remains nonrecurrent after $N-2$
steps. Bound (13) forces its exact entry time to be $N-1=n-2$.
This proves sharpness for every $n\ge5$. The triangle and quadrilateral
exceptions were resolved explicitly above.

## Verification and novelty boundary

These are deductive checks of the author's proposed route, with the
geometric recursion supplied in the companion desk proof. No numerical
execution of the new $K$, clock or witness formulas is claimed here.
The author is separately preparing checks on only the original complete
$n=3,\ldots,10$ boxes. Those receipts must be read as actual evidence
before a computational verification claim is made.

The existence of these proofs does not by itself clear historical/source
collision, confer a paper number, or substitute for a noncontributor
candidate gate and subsequent manuscript reviews. Plain rotation/Pop and
the old literal UUDU image identification remain excluded or refuted as
documented; old static Catalan/avoidance enumeration remains deducted.

**Final same-day evidence update:** the new affected standalone author
pair has now completed and was fully inspected as recorded in
[REPORT.md](REPORT.md), with 62,087 assertions per run on the original
boxes and an actual raw comparison. No producer was rerun by this desk;
the source/value and noncontributor gates are unchanged.
