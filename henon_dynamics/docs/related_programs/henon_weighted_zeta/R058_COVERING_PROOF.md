# R058 Covering, Survivor, Hyperbolicity, and Entropy Proof Package

## Claim

Let

\[
H_6(x,y)=(1-6x^2-y,x),
\]

and define

\[
X_\pm=\pm[1/3,5/8],
\qquad
Y_\pm=\pm[5/16,81/128],
\qquad
N_{st}=X_s\times Y_t.
\]

Let \(A\) be the matrix

\[
A=
\begin{pmatrix}
1&0&1&0\\
1&0&0&0\\
0&1&0&1\\
0&1&0&0
\end{pmatrix}
\]

in state order \(--,-+,+-,++\).

Then there is a nonempty compact \(H_6\)-invariant set
\(\Lambda\subset\bigcup_{s,t}N_{st}\) such that:

1. \(\Lambda\) is uniformly hyperbolic;
2. the itinerary map from \((\Lambda,H_6)\) onto the two-sided subshift
   \((\Sigma_A,\sigma)\) is continuous and surjective;
3. consequently,

   \[
   h_{\rm top}(H_6|_\Lambda)
   \ge
   \log\frac{1+\sqrt5}{2}.
   \]

No claim of conjugacy, entropy equality, or Markov partition is included.

## Status

PROVABLE AS STATED, conditional only on the standard finite
h-set covering-chain existence theorem stated explicitly in Step 5. The local
covering, forbidden-transition, cone, and matrix hypotheses are verified
directly below with exact rational bounds.

## Assumptions

- A strict two-dimensional h-set covering \(N_i\xRightarrow{H_6}N_j\) uses
  exit coordinate \(x\), entry coordinate \(y\), strict avoidance of target
  entry faces, strict exit-face crossing, and nonzero one-dimensional degree.
- The finite covering-chain theorem is used in the following form:

  > If \(N_0\xRightarrow{f}N_1\xRightarrow{f}\cdots
  > \xRightarrow{f}N_m\), then there exists \(z\in N_0\) with
  > \(f^k(z)\in N_k\) for \(0\le k\le m\).

- The standard invariant-cone criterion may be applied to a diffeomorphism on
  a compact invariant set when forward unstable and backward stable cones are
  strictly invariant, disjoint, and uniformly expanded.

## Notation

- \(F(x,y)=1-6x^2-y\), so \(H_6(x,y)=(F(x,y),x)\).
- \(X_-=[-5/8,-1/3]\), \(X_+=[1/3,5/8]\).
- \(Y_-=[-81/128,-5/16]\), \(Y_+=[5/16,81/128]\).
- \(N=\bigcup_{s,t}N_{st}\).
- \(r_x=7/48\), \(r_y=41/256\), and \(\kappa=1/2\).
- \(C^u=\{|\eta|\le\kappa|\xi|\}\) and
  \(C^s=\{|\xi|\le\kappa|\eta|\}\) in normalized h-set coordinates.

## Proof Strategy

First prove exactly which rectangle transitions are strict h-set coverings.
Then establish uniform forward/backward cone bounds. Use finite covering
chains and compactness to realize every bi-infinite admissible word. The
resulting itinerary factor supplies the entropy lower bound, and the cone
criterion supplies uniform hyperbolicity.

## Dependency Map

1. The transition graph depends on exact exit-face ranges and
   \(X_s\subset\operatorname{int}Y_s\).
2. Every covering relation depends on strict entry avoidance, opposite
   exit-face placement, and nonzero degree.
3. Bi-infinite realization depends on finite covering-chain existence,
   invertibility of \(H_6\), compactness, and continuity.
4. The entropy bound depends on a continuous surjective factor onto
   \(\Sigma_A\).
5. Uniform hyperbolicity depends on strict invariant disjoint cones and
   expansion in both time directions.

## Proof

### Step 1. Geometry of the entry coordinate

For either sign \(s\),

\[
X_s\subset\operatorname{int}Y_s
\]

because the inner and outer gaps are \(1/48\) and \(1/128\). Moreover,

\[
\pi_yH_6(x,y)=x.
\]

Thus, if the source is \(N_{st}\), the image entry coordinate lies strictly
inside \(Y_s\). It cannot lie in \(Y_{-s}\), since the two sign intervals are
disjoint. Hence a possible target must have second sign \(s\). This excludes
eight of the sixteen ordered state pairs.

### Step 2. The six strict exit crossings

At \(|x|=1/3\),

\[
F(x,y)=\frac13-y,
\]

and at \(|x|=5/8\),

\[
F(x,y)=-\frac{43}{32}-y.
\]

Evaluating these affine functions on \(Y_-\) and \(Y_+\) gives the following
strict crossings.

| Source | Target | Degree | Exit margin | Entry margin |
|---|---|---:|---:|---:|
| \(--\) | \(--\) | \(+1\) | \(11/128\) | \(1/128\) |
| \(--\) | \(+-\) | \(+1\) | \(1/48\) | \(1/128\) |
| \(-+\) | \(--\) | \(+1\) | \(13/384\) | \(1/128\) |
| \(+-\) | \(-+\) | \(-1\) | \(11/128\) | \(1/128\) |
| \(+-\) | \(++\) | \(-1\) | \(1/48\) | \(1/128\) |
| \(++\) | \(-+\) | \(-1\) | \(13/384\) | \(1/128\) |

For example, on a negative-entry source \(y\in Y_-\), the inner exit face has

\[
F\ge\frac13+\frac5{16}=\frac{31}{48}>\frac58,
\]

while the outer exit face has

\[
F\le-\frac{43}{32}+\frac{81}{128}
=-\frac{91}{128}<-\frac58.
\]

Thus it crosses both \(X_+\) and \(X_-\). On a positive-entry source,

\[
\max_{\lvert x\rvert=1/3,\,y\in Y_+}F
=\frac1{48}<\frac13,
\]

so the positive target exit interval is not reached, whereas the negative
interval is crossed. The sign of \(x\) determines whether the crossing degree
is \(+1\) or \(-1\).

To connect these inequalities to the strict h-set definition, normalize source
and target rectangles to \([-1,1]^2\). The image entry coordinate lies in
\((-1,1)\). On the two source exit faces, the image exit coordinate lies on
opposite strict sides of \([-1,1]\). Collapse the entry component linearly to
zero, collapse its dependence in the exit component, and homotope the
remaining monotone exit map to a linear map of the same nonzero degree. During
this homotopy, the strict entry and exit inequalities remain valid. Therefore
each row of the table is a strict covering relation.

### Step 3. No additional state transition occurs

The eight target-entry sign mismatches were excluded in Step 1. The only two
remaining nonlisted pairs have source entry sign \(+\) and target exit sign
\(+\). For every such source,

\[
F(x,y)
\le
1-6(1/3)^2-\frac5{16}
=\frac1{48}
<\frac13.
\]

Hence the image cannot meet \(X_+\). The exact transition graph is therefore
the matrix \(A\) in the claim.

### Step 4. Exact cone conditions

The normalized derivative matrices are

\[
D\widehat H=
\begin{pmatrix}
-12x&-123/112\\
112/123&0
\end{pmatrix},
\]

\[
D\widehat{H^{-1}}=
\begin{pmatrix}
0&123/112\\
-112/123&-12y
\end{pmatrix}.
\]

If \((\xi,\eta)\in C^u\), then \(|x|\ge1/3\) gives

\[
|\xi'|
\ge
\frac{773}{224}|\xi|,
\qquad
\frac{|\eta'|}{|\xi'|}
\le
\frac{25088}{95079}
<\frac12.
\]

Furthermore,

\[
\frac{\|D\widehat H(\xi,\eta)\|^2}
{\|(\xi,\eta)\|^2}
\ge
\frac{597529}{62720}
>1.
\]

If \((\xi,\eta)\in C^s\), then \(|y|\ge5/16\) gives under the inverse

\[
|\eta_{-1}|
\ge
\frac{1621}{492}|\eta|,
\qquad
\frac{|\xi_{-1}|}{|\eta_{-1}|}
\le
\frac{15129}{45388}
<\frac12,
\]

and

\[
\frac{\|D\widehat{H^{-1}}(\xi,\eta)\|^2}
{\|(\xi,\eta)\|^2}
\ge
\frac{2627641}{302580}
>1.
\]

The two cones are disjoint except at zero because \(\kappa^2=1/4<1\).

### Step 5. Every admissible bi-infinite word is realized

Let \(\omega=(\omega_n)_{n\in\mathbb Z}\in\Sigma_A\). For each \(m\ge1\),
the word

\[
\omega_{-m},\omega_{-m+1},\ldots,\omega_m
\]

is a finite chain of the strict covering relations proved in Step 2. By the
finite covering-chain theorem, there exists \(z_m\in N_{\omega_{-m}}\) such
that

\[
H_6^k(z_m)\in N_{\omega_{-m+k}}
\qquad
(0\le k\le2m).
\]

Set \(p_m=H_6^m(z_m)\in N_{\omega_0}\). The latter h-set is compact, so some
subsequence converges to a point \(p\in N_{\omega_0}\). Fix an integer \(j\).
For all sufficiently large \(m\), \(H_6^j(p_m)\in N_{\omega_j}\). The map
\(H_6\) is a diffeomorphism with

\[
H_6^{-1}(X,Y)=(Y,1-6Y^2-X),
\]

so every fixed positive or negative iterate is continuous. Since each h-set
is closed,

\[
H_6^j(p)\in N_{\omega_j}.
\]

This holds for every \(j\in\mathbb Z\). Hence \(p\) realizes \(\omega\).

### Step 6. Compact invariant survivor and factor map

Define

\[
\Lambda=\bigcap_{n\in\mathbb Z}H_6^{-n}(N).
\]

It is compact and invariant. Step 5 shows it is nonempty and realizes every
word of \(\Sigma_A\). Because the four h-sets are pairwise disjoint, each
point of \(\Lambda\) has a unique state at every time. Define its itinerary
\(\pi(p)\).

The h-sets have positive mutual separation. Therefore every finite itinerary
window is locally constant on a sufficiently small neighborhood in
\(\Lambda\), which makes

\[
\pi:\Lambda\to\Sigma_A
\]

continuous. It is surjective by Step 5 and obeys

\[
\pi\circ H_6=\sigma\circ\pi.
\]

Thus \((\Sigma_A,\sigma)\) is a factor of \((\Lambda,H_6)\).

### Step 7. Entropy lower bound

Entropy cannot increase under a continuous factor map, so

\[
h_{\rm top}(H_6|_\Lambda)
\ge h_{\rm top}(\sigma|_{\Sigma_A}).
\]

Exact computation gives

\[
\det(\lambda I-A)
=(\lambda^2-\lambda-1)(\lambda^2+1),
\]

hence

\[
\rho(A)=\frac{1+\sqrt5}{2}.
\]

The entropy of a finite subshift of finite type is the logarithm of the
spectral radius of its adjacency matrix. Therefore

\[
h_{\rm top}(H_6|_\Lambda)
\ge
\log\frac{1+\sqrt5}{2}.
\]

### Step 8. Uniform hyperbolicity

On \(\Lambda\), every forward transition stays within the frozen h-set family,
so the forward unstable cone estimate of Step 4 applies at every time. The
backward stable cone estimate applies at every time as well. The cones are
strictly invariant, disjoint, and uniformly expanded in their respective time
directions.

The invariant-cone criterion therefore produces continuous one-dimensional
bundles \(E^u\) and \(E^s\) with

\[
T_\Lambda\mathbb R^2=E^u\oplus E^s,
\]

uniform forward expansion on \(E^u\), and uniform forward contraction on
\(E^s\). The normalized norms on the four separated h-sets are uniformly
equivalent to the Euclidean norm. Consequently \(\Lambda\) is uniformly
hyperbolic.

The three conclusions in the claim follow. \(\square\)

## Corrections or Missing Assumptions

- The earlier equal-width candidate \(Y_s=X_s\) is not used. It touches target
  entry faces and does not satisfy the frozen strict covering definition.
- The proof uses wider \(Y\)-intervals and explicitly invokes the finite
  covering-chain theorem.

## Open Risks

- Before changing the result JSON from theorem-pending to theorem-pass, an
  independent reader must verify that the stated covering-chain theorem uses
  the same strict h-set convention and that the compactness argument is
  accepted for bi-infinite itineraries.
- The proof establishes a surjective factor, not uniqueness of realization.
  No conjugacy wording may be introduced without an additional shrinking or
  uniqueness theorem.
