# Theorem package and hostile gate: cyclic Gram gate

## Literal system

Let (V=\mathbb F_2^m), (m\geq1), with the standard nondegenerate
symmetric form (x\cdot y=\sum_i x_i y_i), and put (Q=|V|=2^m).  On
(V^3), define

\[
T(u,v,w)=\bigl((u\cdot v)w,(v\cdot w)u,(w\cdot u)v\bigr).       \tag{1}
\]

This is a deterministic finite dynamical system; no quotient by an
orthogonal group or by coordinate rotation is taken.

## Exact theorem

Let

\[
\mathcal C=\{(u,v,w):u\cdot v=v\cdot w=w\cdot u=1\},
\qquad R=|\mathcal C|=\frac{Q^3}{8}.                         \tag{2}
\]

Then:

1. On (\mathcal C), (T(u,v,w)=(w,u,v)).  If a state is not in
   (\mathcal C), its second iterate is zero.
2. The recurrent set is (\{0\}\sqcup\mathcal C).  There are

   \[
   1+\frac Q2\quad\hbox{fixed points},\qquad
   \frac{R-Q/2}{3}\quad\hbox{three-cycles}.                 \tag{3}
   \]

3. The zero fibre is

   \[
   F_0=|T^{-1}(0)|=\frac{Q^3}{8}+\frac{9Q^2}{4}-\frac{3Q}{2}. \tag{4}
   \]

   The exact depth layers are

   \[
   |D_0|=1+R,\qquad |D_1|=F_0-1,\qquad
   |D_2|=\frac{3Q(Q-1)(Q-2)}4.                              \tag{5}
   \]

   Thus the height is one at (m=1) and two for (m\geq2).
4. The following is the complete every-target fibre atlas.  Permuting the
   three target coordinates does not change the stated count.

   * Zero has fibre (F_0).
   * A target ((x,y,z)) with all three coordinates nonzero has fibre one
     exactly when (x\cdot y=y\cdot z=z\cdot x=1), and fibre zero otherwise.
   * A target with exactly two nonzero coordinates (x,y) has fibre zero
     unless (x\cdot y=0).  Subject to that condition its fibre is (Q/2)
     when (x=y), and (Q/4) when (x\ne y).
   * For (m\geq2), a target with exactly one nonzero coordinate (x) has

     \[
     \frac Q4\left(\frac Q2-r_x\right),\qquad
     r_x=\begin{cases}1,&x\cdot x=1,\\2,&x\cdot x=0.
     \end{cases}                                           \tag{6}
     \]

     At (m=1) this fibre is zero.
   * Every case not listed above has fibre zero.

   Zero is the unique largest fibre.
5. For every target (y) and every time (t),

   \[
   |(T^t)^{-1}(y)|=
   \begin{cases}
   1,&t=0,\\
   |T^{-1}(y)|,&t=1,\\
   Q^3-R,&t\geq2\text{ and }y=0,\\
   1,&t\geq2\text{ and }y\in\mathcal C,\\
   0,&t\geq2\text{ otherwise}.
   \end{cases}                                             \tag{7}
   \]

   Hence (\operatorname{im}T^t=\{0\}\sqcup\mathcal C) for every
   (t\geq2), and

   \[
   \zeta_T(z)=(1-z)^{-(1+Q/2)}
   (1-z^3)^{-(R-Q/2)/3}.                                   \tag{8}
   \]

The theorem is proved below.  Its portfolio decision is nevertheless
**`KILL_INTERNAL_P125_NL03`**; correctness is not allocation value.

## Proof

Write

\[
a=u\cdot v,\qquad b=v\cdot w,\qquad c=w\cdot u.
\]

Every pairwise inner product among the three output coordinates equals
(abc).  If (abc=1), all three gates are one and (1) is the cyclic
rotation ((u,v,w)\mapsto(w,u,v)).  If (abc=0), all pairwise products
after one update are zero, so every gate in the next update vanishes.  This
proves the temporal dichotomy and identifies the recurrent set once
(|\mathcal C|) is known.

To count (\mathcal C), first choose an ordered pair ((u,v)) with
(u\cdot v=1).  There are ((Q-1)Q/2) such pairs.  When (u=v), the vector
has odd weight; there are (Q/2) choices, and (w\cdot u=1) has (Q/2)
solutions.  For the remaining (Q(Q-2)/2) pairs, (u,v) are linearly
independent and the two equations (w\cdot u=w\cdot v=1) have (Q/4)
solutions.  Therefore

\[
|\mathcal C|=\frac{Q^2}{4}+\frac{Q(Q-2)}2\frac Q4
=\frac{Q^3}{8}.
\]

A recurrent triple is fixed by rotation precisely when (u=v=w=x).  Its
three Gram bits are one exactly when (x\cdot x=1), and exactly half of all
vectors have odd weight.  Together with zero this gives the fixed count in
(3); all remaining recurrent states form three-cycles.

We next solve the inverse problem directly.  If all target coordinates
((x,y,z)) are nonzero, all three source gates must equal one and the source
must be ((y,z,x)).  The three required equations are exactly
(x\cdot y=y\cdot z=z\cdot x=1), proving the three-coordinate line of the
atlas.

For a target ((x,y,0)) with (x,y\ne0), a source must have the form
((y,v,x)) with

\[
v\cdot x=v\cdot y=1,qquad x\cdot y=0.                    \tag{9}
\]

If (x=y), the single affine hyperplane has (Q/2) points (and
(x\cdot x=0) follows from (9)).  If (x\ne y), the two linear forms are
independent and their common affine fibre has (Q/4) points.  If
(x\cdot y=1), the third output cannot vanish.  This proves the
two-coordinate line.

For a target ((x,0,0)), a source must have (w=x) and must choose
(u,v\in H=x^\perp) with (u\cdot v=1).  The radical of the restricted
form on (H) is

\[
\operatorname{rad}(H)=H\cap\langle x\rangle,
\]

of cardinality (r_x=1) when (x\cdot x=1), and (r_x=2) when
(x\cdot x=0).  For each of the (Q/2-r_x) nonradical choices of (u),
the nonzero functional (v\mapsto u\cdot v) on (H) takes the value one on
(Q/4) vectors.  This proves (6) for (m\geq2); the one-dimensional
boundary is immediate.

It remains to total the tree.  There are (Q/2) odd vectors and (Q/2-1)
nonzero even vectors.  Summing (6) over the three one-coordinate supports
gives

\[
S_1=\frac{3Q(Q-2)^2}{8}.
\]

For one fixed two-coordinate support, the equal even pairs contribute
((Q/2-1)(Q/2)).  Among all ordered nonzero orthogonal pairs, the distinct
ones number ((Q-2)^2/2) and contribute (Q/4) each.  Over all three
supports this gives

\[
S_2=\frac{3Q^2(Q-2)}8.
\]

Thus the number of states mapping first to a nonzero transient state, hence
having depth two, is

\[
S_1+S_2=\frac{3Q(Q-1)(Q-2)}4.
\]

The carrier partitions into the recurrent core, the zero fibre, and this
depth-two set.  Subtracting from (Q^3) yields (4), and (5) follows.  The
inverse atlas also shows that a recurrent target has its unique cyclic
predecessor and no transient predecessor.  Equations (7)--(8), the unique
maximum assertion, and the full rooted component description now follow.
\(\square\)

## Exact controls

`verify_scout.py` exhausts every state and every target for (m=1,2,3,4,5).
It checks literal arrows, the recurrent rotation, two-step collapse, fixed
and three-cycle counts, every depth layer, every line of the fibre atlas,
and the unique maximal zero fibre.  The boundary signatures include

| (m) | states | image | fixed | cycles of length 3 | (F_0) | depth 2 |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 8 | 2 | 2 | 0 | 7 | 0 |
| 2 | 64 | 24 | 3 | 2 | 38 | 18 |
| 3 | 512 | 149 | 5 | 20 | 196 | 252 |
| 4 | 4,096 | 873 | 9 | 168 | 1,064 | 2,520 |
| 5 | 32,768 | 5,585 | 17 | 1,360 | 6,352 | 22,320 |

Enumeration is falsification evidence, not the proof above.

## Hostile internal decision

The literal map is not P125: it acts on three vectors, uses three bilinear
gates, and retains whole vectors in a cyclic output.  That literal difference
is insufficient for another portfolio paper.  The following major engines
are already occupied by P125's quadratic-state shear:

| proof/presentation engine | P125 | V02 transfer |
|---|---|---|
| small formed-space quotient | ((Q(x),Q(y),B(x,y))) | three pairwise Gram bits |
| quotient-controlled clock | depth at most two | depth at most two |
| recurrent linear action | two shear matrices, periods 1--4 | coordinate rotation, periods 1 and 3 |
| arbitrary-target inversion | two form-membership candidates | affine hyperplane intersections |
| global census | character/hyperplane/Witt counts | hyperplane/radical/Gram counts |
| final package | fibres, layers, components, zeta | the same six chapter axes |

Five substantive proof sections and essentially the entire presentation
architecture transfer.  V02's new radical split and large fibres are clean,
but they are a refinement inside the same finite-formed-space state-gate
programme, not an independent mechanism.

There is a second collision with the killed `NL03` lane from P162--P166:
that carrier sends a triple to its three pairwise class-two commutators and
then collapses; its inverse engine is the joint value distribution of three
bilinear forms.  V02 multiplies those three scalar gates by cyclically
opposite vectors and thereby creates a recurrent core, but the owner-thin
part is still the same shared-triple bilinear constraint census.

**Final decision:** `KILL_INTERNAL_P125_NL03`.  Do not allocate a paper
number, do not call the external search miss novelty, and do not recommend
V02 over the cleaner and more independent M01 residue.
