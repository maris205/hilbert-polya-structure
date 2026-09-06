# P197--P201 algebra/order/logic/finite-ring breadth and kill ledger

## Scope and method

This read-only scouting round first checked the P1--P196 paper tree, the
recent phase-one ledgers, retired candidates, and the standing collision
firewalls.  It then enumerated literal finite maps with standard-library
code.  No random kernel was used.  Every census below is an exact exhaustive
census of the stated box.

The ranked order measures theorem signal before the internal owner penalty.
It is not a paper-number assignment.  Only one candidate is recommended for
a bounded theorem-contract proof spike; one further candidate is retained as
a reserve.  All other candidates are killed.

## Ranked slate

### Rank 1: self-displacement difference (`SDD`)

- **Carrier:** all functions (f:\mathbb F_p\to\mathbb F_p), for an odd
  prime (p).
- **Literal update:**
  
  \[
       (D_pf)(x)=f(x+f(x))-f(x).
  \]
- **Timing:** all (p) outputs are computed synchronously.
- **Tie-break:** none.
- **Hold condition:** none is imposed; a function holds exactly when it
  satisfies the displayed fixed equation.
- **Strict theorem signal:** the affine functions form an invariant stratum
  with
  
  \[
  (a,b)\mapsto(a^2,ab),\qquad
  (a,b)\mapsto(a^{2^t},b a^{2^t-1})
  \]
  
  at time (t).  This gives the exact 2-primary tail, odd-order period,
  iterate-fixed census, and every-target time-(t) affine fibres.  On the
  full carrier, fixed functions are exactly matchings of the projected
  nonzero orbits of (L(x,c)=(x+c,2c)).
- **Exact boxes:**
  
  | (p) | states | image | fixed | recurrent | max tail | cycle counts | max fibre |
  |---:|---:|---:|---:|---:|---:|---|---:|
  | 3 | 27 | 10 | 4 | 10 | 1 | (1:4,2:3) | 4 |
  | 5 | 3125 | 981 | 6 | 126 | 5 | (1:6,2:30,6:10) | 14 |
  | 7 | 823543 | 186740 | 22 | 2416 | 12 | (1:22,2:588,3:126,4:42,6:98,12:7) | 298 |
- **Smallest false strengthening:** the tempting formula
  (|\operatorname{Fix}(D_p)|=p+1) holds when (2) is primitive modulo
  (p), but fails already at (p=7), where the answer is (22).  The
  affine clock is not a full-carrier clock.
- **Cheapest useful pilot:** full graph at (p=5); fixed-orbit matching and
  an encoded streaming full graph at (p=7).
- **Collision:** same all-function carrier and “state-selected difference”
  vocabulary as P178, but a different literal selector and a non-Jordan
  proof mechanism.  Ordinary squaring on the affine stratum is zero-credit.
- **Disposition:** `PROMOTE_PROOF_SPIKE / OWNER_AMBER / HOLD_EXTERNAL`.

### Rank 2: Zadeh cyclic implication (`ZCI`)

- **Carrier:** ({0,1,\ldots,M}^m), with cyclic indices.
- **Literal update:**
  
  \[
       T(x)_i=\max\{M-x_i,\min(x_i,x_{i+1})\}.
  \]
- **Timing:** synchronous.
- **Tie-break:** none; `min` and `max` are literal chain operations.
- **Hold condition:** none beyond equality with the output.
- **Strict theorem signal:** put (u_i=2x_i-M).  The local rule becomes
  
  \[
  \Phi(u,v)=\max(-u,\min(u,v)).
  \]
  
  The first image has independent negative sites and satisfies
  (|u_i|\le|u_{i+1}|) at every negative site.  Thereafter magnitudes obey
  cyclic minimum erosion.  Thus (T^m) lies in the recurrent core consisting
  of a uniform allowed magnitude whose negative sites are an independent
  set of (C_m); (T) rotates those sites.  For (M\ge2), maximum tail is
  exactly (m), witnessed by ((0,\ldots,0,1)).  If
  (L_j=\operatorname{tr}\bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)^j), then
  
  \[
  |\operatorname{Rec}(T)|=\left\lceil\frac M2\right\rceil L_m+
  \mathbf1_{2\mid M},
  \]
  
  and for (t\ge1),
  
  \[
  |\operatorname{Fix}(T^t)|=
  \left\lceil\frac M2\right\rceil L_{\gcd(m,t)}+
  \mathbf1_{2\mid M}.
  \]
  
  Every labelled one-step fibre is the trace of an explicit local matrix
  product.
- **Exact boxes:**
  
  | ((M,m)) | states | image | recurrent | fixed | max tail | cycles | max fibre |
  |---|---:|---:|---:|---:|---:|---|---:|
  | (2,4) | 81 | 34 | 8 | 2 | 4 | (1:2,2:1,4:1) | 7 |
  | (3,5) | 1024 | 242 | 22 | 2 | 5 | (1:2,5:4) | 18 |
  | (5,6) | 46656 | 6993 | 54 | 3 | 6 | (1:3,2:3,3:3,6:6) | 83 |
- **Smallest false strengthening:** for (M=3), the maximum fibres for
  (m=3,\ldots,8) are (5,10,18,31,52,100); the last value kills the
  simplest recurrence suggested by the shorter boxes.  For (M=1), the
  maximum tail is (1), not (m).
- **Cheapest useful pilot:** (M=3,m=5).
- **Collision:** the same cyclic finite-chain implication setting as P196,
  with generic transfer traces already occupied by P187/P190/P196.  The
  magnitude/independent-set clock is different, but the adjacency is too
  close for immediate promotion.
- **Disposition:** `RESERVE_NEAR_P196`.

### Rank 3: conjugation-rack cellular automaton (`CRC`)

- **Carrier:** (G^m) for a finite group (G).
- **Literal update:**
  
  \[
       T(x)_i=x_{i+1}^{-1}x_ix_{i+1}.
  \]
- **Timing:** synchronous and cyclic.
- **Tie-break / hold:** no selector and no imposed hold.
- **Candidate invariant:** every coordinate stays in its original conjugacy
  class.  Fixed states are cyclic tuples of adjacent commuting elements.
- **Exact boxes:** for (S_3,m=3), (216) states, all recurrent and all
  image states, (48) fixed points, cycle counts
  (1:48,2:18,3:14,6:15), and every fibre is a singleton.  For
  (S_3,m=4), the census is
  (1296/1242/162/1242) for states/image/fixed/recurrent, maximum tail (1),
  cycle counts (1:162,2:168,3:32,6:104,8:3), and maximum fibre (3).
- **Smallest false strengthening:** the global map is not always a
  permutation; (S_3) at lengths (2) and (4) has missing targets.
- **Cheapest useful pilot:** (S_3^3).
- **Collision:** cyclic commuting counts transfer to P135, and class-two
  specializations become the central commutator layers already killed near
  P119/P175 and NL01--NL06.
- **Disposition:** `KILL_GROUP_WORD_TRANSFER`.

### Rank 4: least-nonsquare Vieta scheduler (`LNV`)

- **Carrier:** (\mathbb F_p^3), (p) odd.
- **Literal updates:**
  
  \[
  R_1(x,y,z)=(yz-x,y,z),\quad
  R_2(x,y,z)=(x,xz-y,z),\quad
  R_3(x,y,z)=(x,y,xy-z).
  \]
  
  Choose the least index whose old coordinate is a nonzero quadratic
  nonsquare and apply that (R_i).
- **Timing:** asynchronous, one selected coordinate per epoch.
- **Tie-break:** (1<2<3).
- **Hold condition:** hold when no coordinate is a nonzero nonsquare.
- **Invariant:** (x^2+y^2+z^2-xyz).
- **Exact boxes:** at (p=11): (1331) states, (848) images, (316)
  fixed, (666) recurrent, maximum tail (3), (316) one-cycles and
  (175) two-cycles, maximum fibre (4).  At (p=13):
  (2197/1513/487/1333), maximum tail (3), (487) one-cycles and
  (423) two-cycles, maximum fibre (4).
- **Smallest false strengthening:** fixed points are not just the explicit
  hold region; a selected Vieta involution can itself fix a point.
- **Collision:** literal Markoff/Vieta involutions and invariant, already
  owner-dense in AH07/AH08/MRK controls.
- **Disposition:** `KILL_DIRECT_MARKOFF_VIETA_OWNER`.

### Rank 5: constant-feedback translation of monic quadratics (`QCT`)

- **Carrier:** monic quadratics (X^2+aX+b\in\mathbb F_p[X]), (p) odd.
- **Literal update:** (f(X)\mapsto f(X+f(0))), or
  
  \[
       (a,b)\mapsto(a+2b,b^2+ab+b).
  \]
- **Timing:** both coefficients update synchronously.
- **Tie-break / hold:** none.
- **Reduction:** putting (a=2s) and (c=b-s^2) gives
  (c\mapsto c) and (s\mapsto s^2+s+c).
- **Exact boxes:** (p=11) has (121) states, (66) image states,
  (11) fixed, (39) recurrent, maximum tail (5), cycle counts
  (1:11,2:5,3:3,4:1,5:1), and maximum fibre (2).  At (p=13), the
  maximum tail is (6), periods through (6) occur, and maximum fibre is
  (2).
- **Smallest false strengthening:** the varying quadratic functional graphs
  preclude a uniform short clock.
- **Collision:** a disjoint union of ordinary univariate quadratic maps;
  generic polynomial dynamics and P125/P150/QFT controls are fatal.
- **Disposition:** `KILL_UNIVARIATE_QUADRATIC_REDUCTION`.

### Rank 6: star-Heyting cyclic implication (`SHI`)

- **Carrier:** (H_r^m), where (H_r=J(P_r)) and (P_r) consists of one
  bottom below (r) incomparable leaves.  Encode the empty ideal by
  (-1) and a nonempty ideal by its leaf mask (A).
- **Literal implication:** (-1\Rightarrow B=\top),
  (A\Rightarrow-1=-1) for nonempty (A), and for nonempty operands the
  leaf mask is ((\neg A)\lor B).  Set (T_i=A_i\Rightarrow A_{i+1}).
- **Timing:** synchronous and cyclic.
- **Tie-break / hold:** none.
- **Exact box:** (r=3,m=4) has (6561) states, (453) image and
  recurrent states, maximum tail (1), one fixed point, cycle counts
  (1:1,2:14,4:106), and maximum fibre (99).
- **Proof signal and risk:** this particular algebra satisfies
  (T^2=\rho T), but that identity must not be generalized to all Heyting
  algebras.
- **Collision:** exact P196 one-step-core/rotation architecture, with P110
  lattice pressure.
- **Disposition:** `KILL_P196_ARCHITECTURE`.

### Rank 7: Fodor cyclic implication (`FCI`)

- **Carrier:** ({0,\ldots,M}^m).
- **Literal update:**
  
  \[
  T_i=\begin{cases}M,&x_i\le x_{i+1},\\
  \max(M-x_i,x_{i+1}),&x_i>x_{i+1}.
  \end{cases}
  \]
- **Timing:** synchronous and cyclic.
- **Tie-break / hold:** none.
- **Exact box:** (M=3,m=5) has (1024) states, (106) images, (81)
  recurrent states, maximum tail (2), one fixed state, (16) five-cycles,
  and maximum fibre (24).  At (M=4,m=4), maximum fibre is (26) and
  the cycles are (1:1,2:4,4:12).
- **Smallest false strengthening:** it is not a one-step retraction; depth
  two occurs.
- **Collision:** still a short compression to a rotation core on P196's
  carrier and in its implication family.
- **Disposition:** `KILL_NEAR_P196`.

### Rank 8: Gaines--Rescher cyclic implication (`GRC`)

- **Carrier:** ({0,\ldots,M}^m).
- **Literal update:** (T_i=M) if (x_i\le x_{i+1}), and (T_i=0)
  otherwise.
- **Timing:** synchronous and cyclic.
- **Tie-break / hold:** none.
- **Exact box:** (M=3,m=4) has (256) states, (15) image states,
  (7) recurrent states, maximum tail (2), exactly one cycle of each
  length (1,2,4), and maximum fibre (34).
- **Collision:** after one step the state lies in ({0,M}^m), where
  the rule is literally the (q=2) instance of P196.
- **Disposition:** `KILL_FACTOR_P196_Q2`.

### Rank 9: Kleene--Dienes cyclic implication (`KDC`)

- **Carrier:** ({0,\ldots,M}^m).
- **Literal update:** (T_i=\max(M-x_i,x_{i+1})).
- **Timing:** synchronous and cyclic.
- **Tie-break / hold:** none.
- **Identity:** (T^2=\rho T), where (\rho) is left cyclic shift.
- **Exact box:** (M=3,m=5) has (1024) states, (197) image and
  recurrent states, maximum tail (1), two fixed points, (39) five-cycles,
  and maximum fibre (10).
- **Collision:** precisely the one-step constrained-core/shift silhouette
  declared zero-credit in P196.
- **Disposition:** `KILL_EXACT_ONE_STEP_ROTATION`.

### Rank 10: matrix anticommutator register (`MAR`)

- **Carrier:** (M_2(\mathbb F_p)^2).
- **Literal update:** ((A,B)\mapsto(B,AB+BA)).
- **Timing:** both new coordinates use the old pair synchronously.
- **Tie-break / hold:** none.
- **Exact boxes:** for (p=2), (256) states, (58) images, a unique
  recurrent fixed state, maximum tail (4), depth histogram
  (0:1,1:15,2:72,3:72,4:96), and maximum fibre (16).  For (p=3),
  (6561) states, (3313) images, (14) fixed and (625) recurrent
  states, maximum tail (8), cycle counts
  (1:14,3:101,6:6,8:4,12:12,24:4), and maximum fibre (81).
- **Smallest false strengthening:** the characteristic-two nilpotent picture
  fails already at (p=3).
- **Collision:** bilinear shift-register and commutator/anticommutator
  mechanisms are occupied by P7/P111/P119/P175 and NL01--NL06.
- **Disposition:** `KILL_BILINEAR_SHIFT_REGISTER`.

### Rank 11: Boolean elementary-symmetric coefficient map (`BES`)

- **Carrier:** (R^k), (R=\mathbb F_2^r), equivalently (k)-tuples of
  subsets of an (r)-set.
- **Literal update:** (T=(e_1,\ldots,e_k)), with all elementary symmetric
  polynomials evaluated in the Boolean ring.
- **Timing:** synchronous.
- **Tie-break / hold:** none.
- **Reduction:** independently at each atom, an input of weight (w) maps
  to ((\binom wj\bmod2)_{j=1}^k).  The new weight is
  (2^{\operatorname{popcount}(w)}-1), and the second image is a canonical
  fixed prefix.  Thus every tail is at most two.
- **Exact boxes:** (k=5,r=2) has (1024) states, (36) images, (9)
  fixed points, depth histogram (0:9,1:247,2:768), and maximum fibre
  (100).  For (k=4,r=2), the corresponding figures are
  (256/25/9), maximum tail (2), maximum fibre (36).
- **Collision:** pure Vieta/symmetric-data normal-form compression.
- **Disposition:** `KILL_VIETA_NORMAL_FORM_COMPRESSION`.

### Rank 12: binary-projective Steiner cyclic product (`BPS`)

- **Carrier:** (Q_d^m), (Q_d=\mathbb F_2^d\setminus\{0\}).
- **Literal product:** (x\star x=x), and
  (x\star y=x+y) when (x\ne y).  Set
  (T_i=x_i\star x_{i+1}).
- **Timing:** synchronous and cyclic.
- **Tie-break / hold:** none.
- **Exact boxes:** (d=3,m=4) has (2401) states, (1057) images,
  (175) recurrent, maximum tail (4), seven fixed points, (21)
  eight-cycles, and maximum fibre (7).  At (d=4,m=4), the figures are
  (50625/13665/855), maximum tail (4), (15) fixed points,
  (105) eight-cycles, and maximum fibre (15).
- **Collision:** the (m=3) slice is exactly the map in
  `papers/retired/160-binary-projective-steiner-triangle-collapse`.
  Enlarging the cyclic length does not clear a literal family owner.
- **Disposition:** `KILL_LITERAL_RETIRED_P160`.

## Additional lattice control

On (H_r^2), for the same star-Heyting algebra, consider

\[
                  T(A,B)=(A\cap B,A\Rightarrow B).
\]

The update is synchronous, with no selector or imposed hold.  In every
Heyting algebra,

\[
                  T^2(A,B)=(A\cap B,\top),
\]

which is fixed.  For (r=4), the exact census is (289) states, (83)
images, (17) fixed points, maximum tail (2), and maximum fibre (17).
This is a canonical lattice split/closure and is killed against P110/P182:
`KILL_CANONICAL_LATTICE_SPLIT`.

## Final recommendation

- Freeze only the bounded `SDD` theorem contract: affine all-time atlas plus
  the full-carrier fixed-orbit matching theorem.  Keep all full-carrier
  temporal claims outside the contract.
- Retain `ZCI` as a reserve only.  It has the cleanest complete dynamical
  theorem in this lane, but its immediate P196 adjacency is a sequence-level
  liability.
- Kill every remaining system for the reasons above.
- This document contains no novelty claim.
