# CSS: exact split/descent subtraction, no admitted time axis

2026-09-09 UTC. Author and proof contributor:
/root/round211_fresh_residual_scout.
This is source-only scouting, not an independent review or candidate gate.

## Literal, status, and dependencies

Exactly one literal was selected after old-map subtraction:
for every odd prime power $q$, on the entire finite carrier
$\operatorname{Mat}_2(\mathbb F_q)^2$,
$$F(A,B)=([A,B],A^2+B^2),\qquad [A,B]=AB-BA. \tag{1}$$
Both outputs use the old pair. Singular, noncommuting, and zero matrices
are included. No invertible-only completion, overflow convention, pilot,
or characteristic-two extension is implicit.

The algebra below is **PROVABLE AS STATED**. A full all-$q$ recurrent-set,
entrance-time, or cycle-count theorem is **NOT CURRENTLY JUSTIFIED**.
The author disposition is
**NO_PROMOTION / KILL_SPLIT_CONJUGACY_AND_UNCLOSED_DESCENT_TIME**.

Dependencies: direct product expansion gives the exact coordinate adapter;
associativity gives the fixed-set decoder; rank and kernel/image counting
give the zero fibre; elementary semilinear descent gives the nonsplit
identity fibre; Cayley--Hamilton gives the trace recurrence. All are
deductions, with no premise from finite computation.

## 1. A full conjugacy in the split case, only a descent sector otherwise

Write $K=\mathbb F_q$. If $-1$ is a square in $K$, choose $i\in K$ with
$i^2=-1$ and put
$$H(A,B)=(X,Y)=(B+iA,B-iA).$$
This is a bijection on the entire pair carrier, with inverse
$$A=(X-Y)/(2i),\qquad B=(X+Y)/2.$$
The denominators are nonzero because $q$ is odd. Direct expansion, without
commuting $A$ and $B$, gives
$$XY=A^2+B^2+i[A,B],\qquad YX=A^2+B^2-i[A,B].$$
Consequently, for the old product-exchange literal
$$P(X,Y)=(XY,YX),$$
one has
$$HF=PH,\qquad HF^t=P^tH\quad(t\ge0). \tag{2}$$
Thus all exact orbit lengths, entrance times, and every time-$t$ fibre
transfer bijectively in the split case. This is a conjugacy of **source
and target**, stronger than CAC's old target-only product mixing.

If $-1$ is nonsquare, let $E=K(i)=\mathbb F_{q^2}$ and let
$\sigma(z)=z^q$, entrywise on matrices. Since the roots of $z^2+1$ are
$i,-i$ and $i\notin K$, $\sigma(i)=-i$. Now $H$ is a bijection from the
original $q^8$ states onto exactly
$$\mathcal D=\{(X,\sigma X):X\in\operatorname{Mat}_2(E)\}.$$
The same inverse formulas land in $K$ because their entries are fixed by
$\sigma$. The sector is invariant:
$$P(X,\sigma X)=(X\sigma X,\sigma X X)
              =(X\sigma X,\sigma(X\sigma X)).$$
Equation (2) holds onto this sector, equivalently the original map is
conjugate to
$$N(X)=X\sigma X\quad\hbox{on all }\operatorname{Mat}_2(E). \tag{3}$$
Here matrix Frobenius means entrywise field Frobenius, **not** matrix
$q$-th powering. The full pair carrier over $E$ has $q^{16}$ states,
so it is not being identified with the $q^8$-state original. No fixed
semilinear-operator powering formula for the iterates of (3) is asserted.

An alternative uniform notation is the quadratic etale algebra
$K[z]/(z^2+1)$ with involution $z\mapsto-z$; it is $K\times K$ in the
split case and $E$ in the nonsplit case. This notation does not erase
the different rational-point conditions.

## 2. What is actually known about time here

For formal words $u_0=x,v_0=y$, define
$$u_{t+1}=u_tv_t,\qquad v_{t+1}=v_tu_t.$$
Evaluation at $(X,Y)$ gives exactly $P^t(X,Y)$. These are the two
Thue--Morse substitution words. This is an all-time word-evaluation
identity, not a classification of the resulting finite matrix orbits.
The old C12 literal and the primary morphism composition mechanism already
supply this skeleton; renaming the coordinates adds no temporal credit.

There is a more compact necessary trace recurrence. If
$(X_t,Y_t)=P^t(X_0,Y_0)$, then for $t\ge1$ their traces and determinants
coincide. Put
$$s_t=\operatorname{tr}X_t=\operatorname{tr}Y_t,\qquad
d_t=\det X_t=\det Y_t.$$
These scalars lie in $K$ also on the nonsplit descent sector. Multiplicativity
gives
$$d_{t+1}=d_t^2,\qquad d_t=d_1^{\,2^{t-1}}.$$
Cayley--Hamilton gives $X_t^2=s_tX_t-d_tI$ and the same identity for $Y_t$.
Using cyclic trace and expanding the product yields
$$\begin{aligned}
s_{t+2}
 &=\operatorname{tr}(X_tY_tY_tX_t)
  =\operatorname{tr}(X_t^2Y_t^2)\\
 &=s_t^2s_{t+1}-2s_t^2d_t+2d_t^2\\
 &=s_t^2(s_{t+1}-2d_t)+2d_t^2. \tag{4}
\end{aligned}$$
In particular the determinant-one stratum gives the standard Thue--Morse
trace recurrence. The matrix identity is valid over the stated fields;
the transfer-matrix paper's real/unimodular spectral conclusions are
not imported as finite-field recurrence theorems.

Neither (4) nor the word representation evaluates a full finite-field
cycle atlas. Trace/determinant do not identify a matrix pair. No
surjectivity onto arbitrary initial trace triples, exact lifted period,
sharp entrance time, or impossibility of a future theorem is asserted.
The map is not simply forced to zero: $(0,I)$ is fixed, and on
$(0,bI)$ it follows $(0,b^2I)$, an explicitly spent scalar-power sector.

## 3. Exact fixed set and all-$q$ count

For matrices over any field, the equations $XY=X$ and $YX=Y$ are equivalent
to: $X,Y$ are idempotents with the same kernel.

For necessity, associativity gives
$X^2=(XY)X=X(YX)=XY=X$ and similarly $Y^2=Y$.
If $Xv=0$, then $Yv=YXv=0$, and the reverse implication follows from
$XY=X$. For sufficiency, if the kernels agree, then
$(I-Y)v\in\ker Y=\ker X$ and hence $XYv=Xv$; interchange $X,Y$ for the
other equation.

In the split case, there is one fixed pair of common rank zero and one
of rank two. For common rank one, choose the common kernel line in
$q+1$ ways. Each idempotent with that kernel is the unique projection
onto a complementary line; there are $q$ complementary lines for each
of $X,Y$, independently. Therefore
$$|\operatorname{Fix}F|=q^2(q+1)+2. \tag{5}$$

In the nonsplit case, the fixed objects are idempotents $X$ whose kernel
equals $\sigma(\ker X)$. A $\sigma$-stable line in $E^2$ is defined over
$K$: a nonvertical line has slope fixed by $\sigma$, and the vertical
line is also defined over $K$. Thus there are $q+1$ such lines.
For a fixed kernel there are $q^2$ complementary $E$-lines, each specifying
one idempotent $X$; $\sigma X$ is then forced. The zero and identity
idempotents again contribute two. This proves the same formula (5).

This is a fixed-point classification, not a recurrent-set classification.
Its mechanism is ordinary projections plus descent, not a fresh time law.

## 4. Complete source representation and exact zero fibres

For any target $(C,D)$, put $U=D+iC,V=D-iC$ in the relevant field.
Equation (2) gives the exact source bijections:
in the split case solve
$$XY=U,\qquad YX=V; \tag{6}$$
in the nonsplit case solve
$$X\sigma X=U,\qquad Y=\sigma X. \tag{7}$$
The inverse $H^{-1}$ recovers every original source once. Equation (7)
already implies the second product equation by applying $\sigma$.

In the split case, for fixed $X$ the kernel of $Y\mapsto(XY,YX)$ is
$$\operatorname{Hom}(K^2/\operatorname{im}X,\ker X),$$
of dimension $(2-\operatorname{rank}X)^2$. Each nonempty target fibre
for that $X$ has exactly the kernel's size. Hence the zero target is
maximal after summing over $X$. It is uniquely maximal, because for every
nonzero target the $X=0$ summand vanishes, whereas at zero that summand
has size $q^4$.

There is one rank-zero matrix, $(q^2-1)^2/(q-1)$ rank-one matrices,
and $(q^2-1)(q^2-q)$ rank-two matrices. The rank-one count follows from
$X=uv^{\mathsf T}$ with nonzero $u,v$ modulo reciprocal nonzero scaling.
Thus
$$|F^{-1}(0,0)|=
q^4+q\frac{(q^2-1)^2}{q-1}+(q^2-1)(q^2-q)
=3q^4-2q^2 \quad(-1\text{ square}). \tag{8}$$
This is exactly the old mutually-annihilating-matrix inverse primitive
and its old kernel-sum maximum argument.

In the nonsplit case write $Q=|E|=q^2$. The equation $X\sigma X=0$
excludes invertible $X$. It has the zero solution. For rank-one $X$
with image line $L$, it is equivalent to
$$\ker X=\sigma L.$$
Indeed $\operatorname{im}\sigma X=\sigma L$, and both this image and
$\ker X$ have dimension one. For each of the $Q+1$ choices of $L$,
the nonzero maps $E^2/\sigma L\longrightarrow L$ number $Q-1$.
This includes $L=\sigma L$ without double counting. Hence
$$|F^{-1}(0,0)|=1+(Q+1)(Q-1)=q^4
\quad(-1\text{ nonsquare}). \tag{9}$$

Equations (6)--(7) are source-set representations, not evaluated
every-target or every-time fibre atlases. In particular, the split maximum
proof must not be transferred to the nonlinear semilinear equation (7).

## 5. A precise nonsplit counterexample to transferring the zero maximum

For the original target $(0,I)$, equation (7) is $X\sigma X=I$.
These matrices are exactly
$$X=G\,\sigma(G)^{-1},\qquad G\in\operatorname{GL}_2(E). \tag{10}$$
A short proof of this degree-two matrix Hilbert-90 case is included.
Given $X\sigma X=I$, the $K$-linear semilinear map
$J(v)=X\sigma(v)$ is an involution of $E^2$. Because the characteristic
is odd, its plus and minus eigenspaces give a direct sum over $K$.
Multiplication by $i$ interchanges them, since $J(iv)=-iJ(v)$.
They therefore each have $K$-dimension two. A $K$-basis of the plus
space is an $E$-basis of $E^2$: a dependence with coefficients
$a_j+ib_j$ separates into the direct plus/minus sum and forces every
$a_j,b_j$ to vanish. Put those basis vectors into the columns of $G$.
Then $X\sigma(G)=G$, proving (10). Conversely (10) directly gives
$X\sigma X=I$.

Two matrices $G,H$ yield the same $X$ exactly when
$G^{-1}H=\sigma(G^{-1}H)$, that is, when they differ on the right by
an element of $\operatorname{GL}_2(K)$. Counting ordered bases gives
$$\begin{aligned}
|F^{-1}(0,I)|
 &=\frac{|\operatorname{GL}_2(\mathbb F_{q^2})|}
         {|\operatorname{GL}_2(\mathbb F_q)|}\\
 &=q(q+1)(q^2+1)>q^4
 \quad(-1\text{ nonsquare}). \tag{11}
\end{aligned}$$
This is an exact elementary descent count. It proves zero is **not**
a maximum-fibre target in the nonsplit case. It does not prove $(0,I)$
is globally maximal. In the split case the same target has
$|\operatorname{GL}_2(K)|$ sources, since $Y=X^{-1}$; this does not
contradict the zero maximum there.

## 6. Residual decision

The split subfamily is a full conjugate of historical C12, so neither
time nor inverse data can be counted again. The nonsplit family is not
silently discarded as a full-pair conjugacy: its descent condition changes
fibre counts and defeats the split zero maximum. The correct surviving
obligation would be a full finite-field temporal/lift theorem for (3)
together with a materially separate evaluated inverse/extremal result.

That temporal theorem has not been proved here. The available fixed count,
two selected target fibres, and trace recurrence arise from ordinary
idempotents, rank counting, Hilbert 90, and the already-owned Thue--Morse
product skeleton. They do not justify a pilot or a paper seat. No
second literal, finite cutoff, computational result, external novelty
clearance, or independent acceptance is manufactured.

