# Theorem spikes for the P177--P181 algebra lane

**Lifecycle:** internal scouting only; `HOLD_EXTERNAL`.

This file records two derivations that survived arithmetic falsification long
enough to merit a theorem package.  It does not assign a paper number.  The
first is recommended for the common pool, subject to an external owner audit.
The second is retained as a strong reserve because its forward mechanism is
too close to P166 and its enumerative input is directly owned by the
Kung--Stong matrix cycle index.

## SFD: state-selected finite differences

### Literal system

Let (p) be a prime and let

\[
 V_p=\{f:\mathbb F_p\longrightarrow\mathbb F_p\}.
\]

Define

\[
 (T_pf)(x)=f(x+f(0))-f(x).                                      \tag{S1}
\]

The state really selects the direction at every epoch; the update is not a
fixed linear finite-difference operator.

### Theorem S

Put ((\tau f)(x)=f(x+1)), (N=\tau-I), and
(J^t=N^tV_p).  For (0\leq t\leq p),

\[
 \dim_{\mathbb F_p}J^t=p-t.                                    \tag{S2}
\]

The map in (S1) has the following complete description.

1. (T_p^p=0), the bound is sharp, and zero is the unique recurrent
   state.  Thus the maximum depth is (p).

2. Its entire image tower is

   \[
   \operatorname {im}T_p^t=J^t,
   \qquad |\operatorname {im}T_p^t|=p^{p-t}
   \quad(0\leq t\leq p).                                      \tag{S3}
   \]

3. For (1\leq t<p) and (g\in V_p),

   \[
   |(T_p^t)^{-1}(g)|=
   \begin{cases}
   p^p-(p^{p-t}-1)(p-1)^t,&g=0,\\
   (p-1)^t,&0\ne g\in J^t,\\
   0,&g\notin J^t.
   \end{cases}                                                 \tag{S4}
   \]

   At (t=0) every fibre is a singleton, while for every (t\geq p)
   the zero fibre is all of (V_p) and every other fibre is empty.

4. If (D_d) is the number of states of exact depth (d), then

   \[
   D_0=1,\qquad
   D_d=(p-1)^{d-1}\bigl(p^{p-d}+p-2\bigr)
   \quad(1\leq d\leq p).                                     \tag{S5}
   \]

5. Let (P e_f=e_{T_pf}) be the deterministic transition operator over
   (mathbb C).  Its characteristic polynomial is

   \[
   \chi_P(\lambda)=(\lambda-1)\lambda^{p^p-1}.                 \tag{S6}
   \]

   Besides the single (J_1(1)), the exact number (m_s) of
   (J_s(0))-blocks is

   \[
   m_s=(p-1)^2p^{p-s-1}\quad(1\leq s<p),
   \qquad m_p=p-1.                                             \tag{S7}
   \]

   In particular the sharp clock is visible algebraically as exactly
   (p-1) top zero-Jordan blocks.

### Proof

The translation module is the regular module

\[
 V_p\simeq\mathbb F_p[C_p]
     \simeq\mathbb F_p[z]/(z^p),\qquad z=\tau-I.
\]

Hence (S2) holds and (N^p=0).  For (a\in\mathbb F_p), set
(D_a=\tau^a-I).  If (a\ne0), then

\[
 D_a=N\,U_a(N),\qquad U_a(0)=a\ne0,                            \tag{S8}
\]

so (U_a(N)) is a unit and (D_aJ^i=J^{i+1}).  If (a=0), then
(D_a=0).  Along an orbit, (T_pf=D_{f(0)}f).  A path that ever selects
zero reaches zero immediately; every path with (t) nonzero selections is
a unit times (N^t).  This proves (T_p^p=0) and the inclusion in (S3).

The reverse direction supplies both surjectivity and all fibres.  Fix
(0\ne g\in J^t) and a word
((a_0,\ldots,a_{t-1})\in(\mathbb F_p^*)^t).  Starting with (f_t=g),
solve backwards

\[
 D_{a_i}f_i=f_{i+1},\qquad f_i(0)=a_i.                          \tag{S9}
\]

On (J^i), the first map in (S9) is onto (J^{i+1}) and has the
one-dimensional kernel of constant functions.  Evaluation at zero is
nonzero on that kernel, so the anchor in (S9) chooses exactly one lift.
Thus every nonzero direction word gives one source and different words give
different sources.  This proves the nonzero clause of (S4), hence (S3); mass
conservation gives the zero clause.  Taking consecutive differences of the
zero-fibre cumulative counts gives (S5).

Sharpness has an explicit witness.  With the polynomial functions
(e_j(x)=\binom{x}{j}), put

\[
 f_*(x)=\sum_{j=0}^{p-1}e_j(x).
\]

Pascal's identity gives (Ne_j=e_{j-1}), and every nonzero iterate before
time (p) has value one at zero.  Therefore the selected direction remains
one, (T_p^{p-1}f_*=e_0\ne0), and (T_p^pf_*=0).

Finally, (operatorname {rank}P^t=|\operatorname {im}T_p^t|).  Removing
the unique recurrent (J_1(1)) leaves nilpotent ranks

\[
 r_t=p^{p-t}-1\quad(0\leq t\leq p).
\]

The standard second difference
(m_s=r_{s-1}-2r_s+r_{s+1}), with
(m_p=r_{p-1}), yields (S7).

### Boundary and transfer audit

- The proof includes (p=2): the image sizes are `4/2/1`, the depth
  layers are `1/2/1`, and the zero blocks are (J_1(0),J_2(0)).
- A fixed difference (f\mapsto f(x+1)-f(x)) was already killed as A05 in
  the P172--P176 algebra scout.  The augmentation-ideal filtration,
  finite-difference nilpotence, image ranks, and generic rank-to-Jordan
  conversion receive zero contribution credit here.
- P164 also has a nonlinear front followed by one fixed cyclic-difference
  tail.  Its fixed tail, repeated-root algebra, image staircase, and affine
  kernel machinery receive zero credit.
- The residual is narrower and literal: direction selection occurs at every
  epoch, the selected anchor makes every backward integration unique, and
  this produces the nonuniform zero/nonzero all-time atlas (S4) and the
  (p-1) top-block multiplicity.  Neither A05 nor P164 supplies that
  state-selected lift system.
- Bounded exact-phrase and formula searches found no direct owner of (S1).
  This is only an `OWNER_THIN` result, never a novelty result.

**Disposition:** `PROMOTE_INTERNAL / HOLD_EXTERNAL`, the lane's sole
recommendation.

## SST: singularity-stopped scalar translation

### Literal system

Let (q=p^e), (n\geq1), and (X=M_n(\mathbb F_q)).  Define

\[
 S(A)=\begin{cases}
 A+I_n,&\det A\ne0,\\
 A,&\det A=0.
 \end{cases}                                                   \tag{M1}
\]

For a matrix (A), let

\[
 R_A=\{t\in\mathbb F_p:\det(A+tI_n)=0\}.                      \tag{M2}
\]

### Theorem M

Every affine central line (A+\mathbb F_pI_n) is invariant.  If (R_A)
is empty, that line is one directed (p)-cycle.  Otherwise every singular
position is fixed and the consecutive nonsingular positions immediately
preceding it form a directed path into it.  Consequently the only periods
are (1,p), and the sharp maximum preperiod is (p-1).

For a singular target (B), let (g(B)) be the number of consecutive
nonsingular matrices (B-I_n,B-2I_n,\ldots) before the preceding singular
matrix.  Then, for (t\geq1),

\[
 |(S^t)^{-1}(B)|=1+\min\{t,g(B)\}.                              \tag{M3}
\]

For a nonsingular target (B),

\[
 |(S^t)^{-1}(B)|=
 \mathbf1\{B-jI_n\text{ is nonsingular for every }1\leq j\leq t\}.
                                                                    \tag{M4}
\]

In particular,

\[
 |S^{-1}(B)|=
 \mathbf1_{\det B=0}+\mathbf1_{\det(B-I_n)\ne0}\in\{0,1,2\}. \tag{M5}
\]

The remaining formulas enumerate the whole graph.  Put

\[
 \gamma_n=|\operatorname {GL}_n(q)|,
 \qquad L_q(u)=\prod_{j\geq1}(1-u/q^j)^{-1},
\]

and let (a_r=a_r(n,q)) be the number of matrices for which (R_A) is
one prescribed (r)-subset of (mathbb F_p).  Then

\[
 a_r=\gamma_n[u^n]\frac{L_q(u)^{1-p}(L_q(u)-1)^r}{1-u}.         \tag{M6}
\]

Write (b_\ell) for the number of positive gaps of length (ell), or
equivalently the number of (J_\ell(0))-blocks of the transition operator.
For (1\leq\ell\leq p-1),

\[
 b_\ell=\mathbf1_{\ell=p-1}a_1+
 \sum_{r=2}^{p-\ell}a_r\binom{p-\ell-2}{r-2}.                 \tag{M7}
\]

Let

\[
 F=q^{n^2}-\gamma_n,\qquad C=a_0/p,\qquad B_+=\sum_\ell b_\ell.
\]

There are (F) fixed points, (C) directed (p)-cycles,
(b_\ell) fixed-rooted paths with (ell) transient vertices, and
(F-B_+) isolated fixed points.  Hence

\[
 |\operatorname {im}S^t|
 =F+pC+\sum_{\ell=1}^{p-1}\max(\ell-t,0)b_\ell,               \tag{M8}
\]

and at time one the counts of targets with fibres (0,1,2) are

\[
 B_+,\qquad q^{n^2}-2B_+,\qquad B_+.                           \tag{M9}
\]

For the deterministic transition operator (Qe_A=e_{S(A)}),

\[
 \chi_Q(\lambda)
 = (\lambda^p-1)^C(\lambda-1)^F
   \lambda^{\sum_\ell\ell b_\ell}.                            \tag{M10}
\]

Thus (M7) is also the complete zero-Jordan inventory.

### Proof

Translation by (I_n) has order (p), so the central lines partition
(X).  On such a line the zero set of the determinant polynomial is exactly
(R_A).  Rule (M1) advances one step at a nonsingular position and stays at
a singular position.  This proves the line classification and the pointwise
formulas (M3)--(M5).  A single nilpotent Jordan block (A) has
(R_A=\{0\}), proving sharp height (p-1).

For (M6), the Kung--Stong cycle index of the full matrix algebra factors
over monic irreducible polynomials.  Its total unmarked series is
(L_q(u)/(1-u)).  Each of the (p) selected linear factors corresponding
to prime-field eigenvalues contributes (L_q(u)).  Requiring a selected
factor to be absent replaces it by (1); requiring it to be present
replaces it by (L_q(u)-1).  Removing all (p) unrestricted factors and
forcing exactly the prescribed (r) to be nonempty gives (M6).

For (r=1), every central line has one gap of length (p-1), and anchoring
its singular endpoint at zero gives (a_1) such lines.  For (r\geq2),
anchor a terminal singular position at zero and the preceding singular
position at (-\ell-1); the intervening (ell) positions are forbidden
and the other (r-2) roots can occupy
(p-\ell-2) positions.  This gives (M7), without a stabilizer division.
Equations (M8)--(M10) now follow by reading each directed path and cycle.

### Boundary and transfer audit

- The formulas include (p=2) and (n=1).  The pilot explicitly checks
  ((p,n)=(2,1),(3,1),(5,1),(2,2),(3,2),(5,2),(2,3),(3,3)).
- Kung, Stong, Fulman, and Morrison own the matrix cycle-index input and
  prescribed-eigenvalue generating functions.  Formula (M6) receives zero
  contribution credit.
- P166 already reduces a statistic-controlled translation to finite
  translation orbits and derives forward structure and target-local fibres.
  That entire reduction transfers to (M1).  The new determinant-root gap
  marks change the enumerator but do not change the forward proof engine.
- P153 already combines a field translation clock with a stopping/collapse
  schedule and all-time fibres.  Its factorial schedule is different, but
  the translation-path shell also receives zero credit.
- Exact searches found no literal match for (M1), but absence of a hit is
  not novelty.  After the owner and internal deductions, the residual is the
  gap-refined use of the known matrix cycle index, not a clean new mechanism.

**Disposition:** `RESERVE_STRONG / KILL_IF_MECHANISM_NOVELTY_REQUIRED`.
It is not recommended ahead of SFD.

## Exact control

The independent standard-library verifier checks all formulas used above on
the stated prime-field boxes.  Its canonical terminus is:

```text
TRANSITION_DIGEST=30db71534328fcb0a43b8d0a2ce7acda3fc271808e057b851a5c5adfa6038cc9
TRANSITIONS=900976
FRESH_TRANSITIONS=884933
RAW_BOXES=104
FRESH_BOXES=92
ASSERTIONS=1375295
RAW_CANDIDATES=11
FRESH_CANDIDATES=9
REDISCOVERY_SENTINELS=2
RESULT=PASS
```

Enumeration is evidence against arithmetic mistakes, not proof and not an
ownership certificate.
