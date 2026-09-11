# Theorem spike RHT — random projective-hyperplane toggling

**Lane status:** `RECOMMEND_THEOREM_SPIKE / OWNER_AMBER / HOLD_EXTERNAL`  
**Scope:** binary projective spaces of dimension at least two; no paper number
is allocated here.

## Literal finite dynamics

Let (V=\mathbb F_2^d), (d\ge2), and let
(E=V\setminus\{0\}), so (|E|=m=2^d-1).  A state is a subset
(A\subseteq E).  At every epoch independently choose a **nonzero** linear
form (ell\in V^*\setminus\{0\}), uniformly among the
(N=2^d-1) choices, and toggle its projective hyperplane:

\[
 A\longmapsto A\mathbin\triangle H_\ell,
 \qquad H_\ell=\{x\in E:\ell(x)=0\}.
\]

The zero form is not sampled.  Thus every mask is an actual projective
hyperplane with (2^{d-1}-1) points; this boundary matters to the period and
the two nontrivial eigenvalues.

## Exact theorem

Write ({\bf1}\in\mathbb F_2^E) for the all-one word and

\[
 c_a=(a(x))_{x\in E},\qquad
 C=\{c_a:a\in V^*\}.
\]

Then (C) is the binary simplex code of dimension (d), and put
(W=\langle {\bf1},C\rangle).

1. **Complete communicating-class theorem.**  The closed irreducible classes
   are exactly the (2^{m-d-1}) cosets of (W), each of size (2^{d+1}).
   Every class is bipartite by subset-cardinality parity and has period two.
   Under the coordinates

   \[
   \epsilon {\bf1}+c_a\longleftrightarrow(\epsilon,a)
   \quad(\epsilon\in\mathbb F_2, a\in V^*),
   \]

   its transition-support graph is the crown graph
   (K_{2^d,2^d}) with one perfect matching deleted.  The chain is simple
   random walk on that graph.

2. **Every-time, every-target kernel.**  If (t\ge1), then a transition
   (A\to B) in (t) steps is possible exactly when a unique (L\in V^*)
   satisfies

   \[
   A\triangle B=(t\bmod2){\bf1}+c_L.                 \tag{1}
   \]

   Its ordered-history count is

   \[
   a_t(L)=
   \begin{cases}
   2^{-d}\{N^t+N(-1)^t\},&L=0,\\
   2^{-d}\{N^t-(-1)^t\},&L\ne0.
   \end{cases}                                      \tag{2}
   \]

   Hence (P^t(A,B)=a_t(L)/N^t) when (1) holds and is zero otherwise.
   Within the parity-compatible (C)-coset, the exact total-variation
   distance to uniform is

   \[
      \left\|P^t(A,\cdot)-U_{A+(t\bmod2){\bf1}+C}\right\|_{\rm TV}
      ={1\over 2^dN^{t-1}}.                         \tag{3}
   \]

3. **Full spectrum, including multiplicities.**  On the entire
   (2^m)-state carrier the four eigenvalues and multiplicities are

   \[
   \begin{array}{c|c}
   \lambda&\operatorname{mult}(\lambda)\\ \hline
   1&K\\
   -1&K\\
   1/N&NK\\
   -1/N&NK
   \end{array}
   \qquad K=2^{m-d-1}.                              \tag{4}
   \]

   In particular there are no transient states, no hidden eigenvalues, and
   no Jordan blocks.

4. **Component-level reconstruction.**  The support degree is (N), so any
   unlabelled communicating component recovers (d=\log_2(N+1)).  Together
   with the total state count it recovers the number (K) of projective-code
   cosets.  This is reconstruction inside this family, not a global graph
   characterization claim.

## Proof

For every nonzero form,

\[
 \mathbf{1}_{H_\ell}={\bf1}+c_\ell.                 \tag{5}
\]

Differences of two masks give (c_a+c_b=c_{a+b}).  Since (d\ge2), for
each nonzero (u) one can choose nonzero distinct (a,b) with (a+b=u),
so the masks generate (C); (5) then also gives ({\bf1}).  Moreover
({\bf1}\notin C): a linear form cannot equal one on every nonzero vector,
because (a(x)=a(y)=1) would force (a(x+y)=0).  Thus
(\dim W=d+1), proving the class count.  Every mask has odd cardinality
(2^{d-1}-1), so each move changes parity, while repeating one mask gives a
two-step return.  This proves period two.

In the displayed coordinates a step adds ((1,\ell)) with
(ell\ne0).  A vertex ((0,a)) is therefore adjacent to every
((1,b)) except (b=a), which proves the crown-graph identification.

After (t) steps the total increment is

\[
 (t\bmod2){\bf1}+c_{\ell_1+\cdots+\ell_t}.
\]

Fourier inversion on the additive group (V^*) counts ordered nonzero
summands.  The trivial character contributes (N^t); every nontrivial
character sums to (-1) on (V^*\setminus\{0\}).  Their total at (L=0)
is (N), and at (L\ne0) is (-1), proving (2).  Subtracting (2^{-d})
from the one exceptional and (N) ordinary probabilities gives (3).

For the full spectrum use Boolean characters
(chi_S(A)=(-1)^{|S\cap A|}), (S\subseteq E), and put
(sigma(S)=\sum_{x\in S}x\in V).  Then

\[
 \lambda_S={1\over N}\sum_{\ell\ne0}
 (-1)^{|S\cap H_\ell|}
 =\begin{cases}
 (-1)^{|S|},&\sigma(S)=0,\\
 (-1)^{|S|+1}/N,&\sigma(S)\ne0.
 \end{cases}                                        \tag{6}
\]

The linear map (S\mapsto(|S|\bmod2,\sigma(S))) has rank (d+1): its
columns are ((1,x)), (x\ne0), and these span
(mathbb F_2\oplus V) when (d\ge2).  Every fibre therefore has size
(K).  Sorting (6) by parity and zero/nonzero sum yields (4).

## Exact falsifiers and boundaries

- `d=1` is excluded: the sole projective hyperplane is empty, so the chain
  is the identity rather than a crown walk.
- Sampling the zero form would replace the crown walk by a uniform jump to
  the opposite simplex-code coset and would erase the (±1/N) modes.
- Sampling complements of hyperplanes would change the parity convention;
  it is not the literal system proved here.
- The verifier exhausts every Boolean character for (d=2,3,4), all starts
  for (d\le3), separating starts for (d=4), and all histories through
  three steps.  It checks the class sizes, four multiplicities, and (1)--(2)
  exactly.

## Collision and claim ceiling

Simplex-code identification, projective hyperplane incidence, Fourier
diagonalization of abelian walks, crown graphs, and their spectra are all
zero-credit background.  P145 already owns a finite cut-space/vertex-push
walk and generic Fourier machinery.  RHT does **not** claim those ingredients;
its residual is the literal random projective-hyperplane toggle together with
the disjoint-crown conjugacy, the exact history kernel (2), and the global
multiplicity lift (4).  A source stating that same conjunction kills the
spike.  The owner search is bounded and cannot establish novelty.
