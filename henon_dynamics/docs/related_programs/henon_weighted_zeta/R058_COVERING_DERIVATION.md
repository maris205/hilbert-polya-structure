# R058 Covering and Cone Derivation Package

## Target

Derive a fully exact route from four rational rectangles for

\[
H_6(x,y)=(1-6x^2-y,x)
\]

to a conservative uniformly hyperbolic survivor and a symbolic entropy lower
bound. The derivation must keep local covering arithmetic, orbit realization,
hyperbolicity, and entropy as separate logical steps.

## Status

COHERENT AS STATED, subject to the separately audited finite covering-chain
realization theorem recorded in the proof package.

## Invariant Object

The organizing object is the maximal all-time survivor

\[
\Lambda=\bigcap_{n\in\mathbb Z}H_6^{-n}(N),
\qquad
N=\bigcup_{s,t\in\{-,+\}}N_{st},
\]

where \(N_{st}=X_s\times Y_t\) is the frozen four-h-set family.

The finite true-image SCCs are not the invariant object in this derivation.
They remain a separate supporting experiment.

## Assumptions

- The map is exactly \(H_6(x,y)=(1-6x^2-y,x)\).
- Exit and entry coordinates are \(x\) and \(y\), respectively.
- The frozen intervals are

  \[
  X_\pm=\pm[1/3,5/8],
  \qquad
  Y_\pm=\pm[5/16,81/128].
  \]

- The four h-sets are \(N_{st}=X_s\times Y_t\).
- Covering relations use strict exit crossing, strict avoidance of the target
  entry boundary, and nonzero one-dimensional degree.
- Cone inequalities are evaluated in affinely normalized h-set coordinates.
- The covering-chain realization theorem is applied only after all its
  hypotheses are verified.

## Notation

- \(s,t,r\in\{-,+\}\) are signs.
- \(N_{st}\) denotes the state with \(x\in X_s\) and \(y\in Y_t\).
- A transition \(st\to rs\) has target entry sign equal to the source exit
  sign because the second coordinate of \(H_6\) is \(x\).
- \(A\) is the frozen four-state adjacency matrix in state order
  \(--,-+,+-,++\).
- \(r_x=7/48\) and \(r_y=41/256\) are the exit and entry half-widths.
- \(\kappa=1/2\) is the frozen cone width.
- \(\Sigma_A\) is the two-sided subshift of finite type defined by \(A\).

## Derivation Strategy

The route is:

1. choose entry intervals slightly wider than the exit intervals so that
   \(H_y=x\) lies strictly inside the target entry interval;
2. evaluate both exit faces exactly and determine the six nonzero-degree
   crossings;
3. exclude all other state transitions exactly;
4. normalize each h-set and derive strict forward/backward cone inequalities;
5. use covering-chain realization to obtain every admissible bi-infinite
   itinerary;
6. use the itinerary factor map for the entropy lower bound and the cone
   criterion for uniform hyperbolicity.

No numerical fitting or floating-point enclosure enters this chain.

## Derivation Map

1. The interval inclusions \(X_s\subset\operatorname{int}Y_s\) give strict
   target-entry avoidance.
2. The function \(1-6x^2-y\) is monotone in \(x\) on each one-sign interval
   \(X_s\), so exit-face interval bounds determine covering degree.
3. The same coordinate identity \(H_y=x\) removes eight forbidden transitions;
   the remaining two are excluded by a sharp upper bound on \(H_x\).
4. The exact adjacency matrix yields
   \((\lambda^2-\lambda-1)(\lambda^2+1)\).
5. Normalized derivative bounds give invariant disjoint horizontal and
   vertical cones with uniform expansion.
6. Finite covering chains plus compactness realize all bi-infinite admissible
   words.
7. The itinerary map is a continuous surjective factor onto \(\Sigma_A\), so
   entropy cannot be smaller than \(\log\rho(A)\).

## Main Derivation

### Step 1. Strict entry geometry

For either sign,

\[
X_s\subset\operatorname{int}Y_s.
\]

The inner and outer margins are

\[
\frac13-\frac5{16}=\frac1{48},
\qquad
\frac{81}{128}-\frac58=\frac1{128}.
\]

Because

\[
H_y(x,y)=x,
\]

every image of \(N_{st}\) lies strictly between the entry faces of a target
whose second sign is \(s\). It cannot meet a target whose second sign is
\(-s\).

### Step 2. Exit-face values

At the inner exit magnitude \(|x|=1/3\),

\[
H_x=\frac13-y.
\]

At the outer exit magnitude \(|x|=5/8\),

\[
H_x=-\frac{43}{32}-y.
\]

For \(y\in Y_-\), the inner face lies strictly to the right of \(X_+\), while
the outer face lies strictly to the left of \(X_-\). Thus both target exit
signs are crossed.

For \(y\in Y_+\), the inner face lies to the right of \(X_-\) but remains left
of \(X_+\), while the outer face lies left of \(X_-\). Thus only \(X_-\) is
crossed.

The source sign changes orientation but not the set of target exit signs.
Therefore

\[
--\to --,+-,
\qquad
-\to -+,++,
\]

\[
-+\to --,
\qquad
+\to -+.
\]

### Step 3. Exact forbidden transitions

Eight transitions have target entry sign different from the source exit sign;
they are impossible because \(H_y=x\in X_s\subset Y_s\) and
\(Y_-\cap Y_+=\varnothing\).

For the remaining two forbidden transitions, the source entry sign is positive
and the target exit sign is positive. On those sources,

\[
\max H_x
=1-6(1/3)^2-\frac5{16}
=\frac1{48}
<\frac13.
\]

Hence \(X_+\) cannot be reached.

### Step 4. Symbolic growth

In the frozen state order,

\[
A=
\begin{pmatrix}
1&0&1&0\\
1&0&0&0\\
0&1&0&1\\
0&1&0&0
\end{pmatrix}.
\]

Exact symbolic algebra gives

\[
\det(\lambda I-A)
=(\lambda^2-\lambda-1)(\lambda^2+1).
\]

Thus

\[
\rho(A)=\varphi=\frac{1+\sqrt5}{2},
\qquad
h_{\rm top}(\Sigma_A)=\log\varphi.
\]

This is a symbolic identity. It becomes a dynamical lower bound only after
orbit realization.

### Step 5. Normalized forward cone

The half-width ratios are

\[
\frac{r_y}{r_x}=\frac{123}{112},
\qquad
\frac{r_x}{r_y}=\frac{112}{123}.
\]

Translations do not affect derivatives, so in normalized coordinates

\[
D\widehat H=
\begin{pmatrix}
-12x&-123/112\\
112/123&0
\end{pmatrix}.
\]

For the horizontal cone

\[
C^u=\{(\xi,\eta):|\eta|\le\tfrac12|\xi|\},
\]

and \(|x|\ge1/3\),

\[
|\xi'|
\ge
\left(4-\frac{123}{224}\right)|\xi|
=\frac{773}{224}|\xi|.
\]

Therefore

\[
\frac{|\eta'|}{|\xi'|}
\le
\frac{112/123}{773/224}
=\frac{25088}{95079}
<\frac12.
\]

The squared norm expansion is at least

\[
\frac{(773/224)^2}{1+(1/2)^2}
=\frac{597529}{62720}
>1.
\]

### Step 6. Normalized backward cone

For

\[
H^{-1}(X,Y)=(Y,1-6Y^2-X),
\]

the normalized derivative is

\[
D\widehat{H^{-1}}=
\begin{pmatrix}
0&123/112\\
-112/123&-12Y
\end{pmatrix}.
\]

On every frozen h-set, \(|Y|\ge5/16\). For the vertical cone

\[
C^s=\{(\xi,\eta):|\xi|\le\tfrac12|\eta|\},
\]

\[
|\eta_{-1}|
\ge
\left(\frac{15}{4}-\frac{56}{123}\right)|\eta|
=\frac{1621}{492}|\eta|.
\]

Hence

\[
\frac{|\xi_{-1}|}{|\eta_{-1}|}
\le
\frac{123/112}{1621/492}
=\frac{15129}{45388}
<\frac12,
\]

with squared backward expansion at least

\[
\frac{(1621/492)^2}{1+(1/2)^2}
=\frac{2627641}{302580}
>1.
\]

The stable and unstable cones intersect only at the zero vector.

### Step 7. From local covering to all-time survivors

Each allowed transition is a strict one-dimensional h-set covering with
degree \(+1\) on \(X_-\) sources and degree \(-1\) on \(X_+\) sources. The
finite covering-chain theorem therefore supplies an orbit segment for every
finite admissible word.

For a bi-infinite admissible word, realize successively longer finite windows
centered at time zero. Their time-zero points lie in one compact h-set.
A convergent subsequence and continuity of every fixed positive and negative
iterate give a point realizing the entire word.

### Step 8. Entropy and hyperbolicity

Every point in \(\Lambda\) has a unique state at each time because the four
h-sets are pairwise disjoint. The itinerary map

\[
\pi:\Lambda\to\Sigma_A
\]

is continuous, surjective, and satisfies

\[
\pi\circ H_6=\sigma\circ\pi.
\]

Therefore

\[
h_{\rm top}(H_6|_\Lambda)
\ge h_{\rm top}(\Sigma_A)
=\log\varphi.
\]

The strict forward and backward cone conditions yield continuous invariant
one-dimensional unstable and stable bundles with uniform expansion and
contraction. Hence \(\Lambda\) is uniformly hyperbolic.

## Remarks and Interpretation

- The wider \(Y\)-intervals are essential. Using \(Y_s=X_s\) would place
  \(H_y=x\) on target entry faces and would not satisfy the frozen strict
  covering definition.
- The four-state coding is conservative. The period catalog suggests richer
  two-symbol behavior, but R058 certifies only the exact subset supported by
  these rectangles.
- The entropy result is a lower bound because surjective coding is enough;
  uniqueness of a point for every symbolic itinerary is not required.
- The graph replication block is not used in the proof.

## Boundaries and Non-Claims

- No topological conjugacy is claimed.
- No entropy equality is claimed.
- The h-sets are not called a Markov partition.
- The certified survivor is not identified with the whole finite-grid SCC.
- No graph or transfer-operator convergence follows.
- No zeta, prime, Riemann-zero, RH, or Hilbert--Pólya statement follows.

## Open Risks

- The finite covering-chain theorem and the compactness passage to
  bi-infinite words require an independent theorem audit before the entropy
  wording is enabled in the result JSON.
- The cone proof uses an equivalent piecewise affine normalized norm. A final
  paper statement should mention equivalence with the Euclidean norm on the
  compact, separated h-set union.
