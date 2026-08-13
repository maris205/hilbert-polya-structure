# Derivation Package

## Target

Derive the exact reduced-word trace of a finite recurrent prime-atom
symbolic graph whose loops carry the identity and whose two directed cross
edges over every undirected adjacency carry positive group labels.  Then
derive the first obstruction created by the chiral adjoint and delimit what
the trace-log determinant, finite regular representations, and word-ball
proxies do and do not establish.

The immediate outputs are:

1. an all-order base identity
   \((\operatorname{Tr}_N\otimes\tau)(L_s^r)=\sum_i p_i^{-rs}\);
2. the associated local/formal tau-determinant product;
3. the exact first chiral backtracking contribution;
4. a specificity audit against inverse-paired, finite-group, abelian, random
   label, and non-arithmetic inventory controls.

## Status

**COHERENT AFTER REFRAMING / EXTRA ASSUMPTION**

The base recurrent labelled transfer is coherent and has an exact all-order
Euler ledger.  The stronger hope that the same cancellation survives chiral
self-adjointization is false: the adjoint introduces inverse labels and
creates positive identity contributions at power two.  The chiral branch is
therefore an exact obstruction result, not a completed construction.

## Invariant Object

The invariant object throughout is the canonical group-valued cyclic trace

\[
 \mathfrak t(A)=(\operatorname{Tr}_N\otimes\tau)(A),
 \qquad
 \tau\!\left(\sum_{g\in G}a_g\lambda(g)\right)=a_e.
\]

The base moments are \(\mathfrak t(L_s^r)\).  The chiral audit uses the same
trace on \(M_{2N}(\mathbb C G)\), not an unrelated scalar determinant.
Finite-matrix and word-ball objects are explicitly treated as proxies for
this invariant rather than replacements for it.

## Assumptions

- The vertex set is a finite entropy-ordered atom prefix
  \(V_N=\{p_1,\ldots,p_N\}\).
- Each vertex has one identity-labelled loop.
- The underlying cross graph is a bidirectional chain, hence strongly
  connected.
- Every *directed* cross edge \(e\) has a label \(g_e\) in a positive
  semigroup \(P\subset G\) satisfying \(e_G\notin P\).  The frozen candidate
  takes distinct free generators, one per directed edge.
- Loop weights are \(d_i(s)=p_i^{-s}\).
- The cross-edge weight on \(i\to j\) is

  \[
  c_{ij}^{(\alpha)}(s)=\alpha d_i(s)+(1-\alpha)d_j(s),
  \]

  with candidate value \(\alpha=1/2\).
- Matrix entries use the convention `[target, source]`.
- The group trace is the coefficient at the identity; no target spectral
  data enter any definition.

## Notation

- \(E_\circ\): loop edges.
- \(E_\times\): directed cross edges.
- \(\lambda(g)\): left regular group operator.
- \(L_s\): labelled transfer with entries

  \[
  (L_s)_{ii}=d_i(s)\lambda(e),\qquad
  (L_s)_{ji}=c_{ij}(s)\lambda(g_{ij}).
  \]

- \(B_t=\begin{psmallmatrix}0&L_t\\L_t^*&0\end{psmallmatrix}\), with
  \(L_t=L_{1/2+it}\).
- A mixed path is a closed vertex path using at least one cross edge.
- \(D_\tau(z)\): the trace-log determinant in its formal or honest local
  convergence domain.
- \(\Delta\): Fuglede--Kadison determinant, used only where its analytic
  definition is justified; finite/rooted quantities are called proxies.

## Derivation Strategy

Use the group label of a closed path as the organizing variable.

1. Expand every matrix power into labelled closed paths.
2. Separate loop-only paths from mixed closed paths.
3. Use positivity of every cross label to exclude the identity from every
   mixed base word.
4. Insert the exact moment identity into the trace-log series.
5. Form the adjoint explicitly; identify its inverse-labelled return edge.
6. Compute the power-two chiral trace before considering higher powers.
7. Test which assumptions are essential by replacing the label group and
   inventory independently.

No approximation enters Steps 1--6.  Numerical approximation enters only in
finite regular/word-ball singular and hermitization diagnostics.

## Derivation Map

1. `positive cross labels` + `mixed closed path` imply a nonempty positive
   group word.
2. `identity-coefficient trace` kills that word exactly.
3. The only surviving length-\(r\) paths are the \(N\) loop repetitions,
   yielding the Euler moment.
4. Summing moments with `-z^r/r` yields the finite Euler product inside the
   trace-log disk.
5. The adjoint replaces \(g_e\) with \(g_e^{-1}\); every matrix entry then
   supplies a two-step return \(g_e^{-1}g_e=e\).
6. Hence the first mixed chiral term is quadratic and positive.
7. Free abelian positive labels preserve Step 2, so freeness and
   noncommutativity are not the true invariant; the positive-cone condition
   is.
8. Finite groups and inverse-paired labels violate the positive-cone
   condition through relations and restore mixed identity words.
9. Finite word-ball determinants remain algebraically loop-only, but free
   group balls are non-Følner; this cannot be promoted to a global FK/Brown
   theorem.

## Main Derivation

### Step 1 — Exact base path expansion (identity)

For a closed length-\(r\) vertex path

\[
 \omega=(i_0\to i_1\to\cdots\to i_r=i_0),
\]

the corresponding matrix-power term is a scalar coefficient
\(w_s(\omega)\) times the left-regular operator of the composed group label
\(g(\omega)\).  Therefore

\[
 \mathfrak t(L_s^r)
 =\sum_{\omega\ \mathrm{closed},\ |\omega|=r}
   w_s(\omega)\,\mathbf 1_{\{g(\omega)=e\}}.
\]

This is an exact expansion of the matrix trace and the group trace.

### Step 2 — Positive-word annihilation (proposition)

If \(\omega\) is mixed, delete its identity-labelled loop steps.  The
remaining label is a product of \(m\ge1\) elements of \(P\).  By the positive
semigroup assumption this product is not the identity.  Thus

\[
 \tau(\lambda(g(\omega)))=0
 \qquad\text{for every mixed closed }\omega.
\]

For the frozen free-group labels the proof is even more elementary: the
reduced word contains \(m\) positive letters and no inverse letter, hence
has reduced length \(m>0\).

### Step 3 — Euler moment ledger (theorem for the frozen finite graph)

The only surviving closed paths are loop-only paths.  At vertex \(i\), the
unique such length-\(r\) path has weight \(d_i(s)^r\).  Consequently, for
every integer \(r\ge1\),

\[
 \boxed{
 \mathfrak t(L_s^r)=\sum_{i=1}^N d_i(s)^r
 =\sum_{i=1}^N p_i^{-rs}.}
\]

The experiment enumerates this identity with opaque loop and edge variables
through \(r=10\).  At \(r=10\), all 6,724 mixed closed paths are present in
the graph trace and all are killed by \(\tau\).

### Step 4 — Local trace-log determinant (identity in its domain)

Whenever the logarithm is defined by the convergent power series (or purely
formally),

\[
\begin{aligned}
 \log D_\tau(z)
 &=-\sum_{r\ge1}\frac{z^r}{r}\mathfrak t(L_s^r)\\
 &=-\sum_{i=1}^N\sum_{r\ge1}\frac{(z p_i^{-s})^r}{r}\\
 &=\sum_{i=1}^N\log(1-zp_i^{-s}).
\end{aligned}
\]

Hence

\[
 \boxed{D_\tau(z)=\prod_{i=1}^N(1-zp_i^{-s})}
\]

as a formal identity.  As a scalar trace-series identity, it also converges
absolutely at `z=1` for `Re(s)>1`, giving the finite-prefix Euler product
directly.  Interpreting the exponential trace series as an analytic
*operator* determinant requires a chosen small-norm/invertible logarithm
branch; that narrower statement is not silently extended past its domain.
This step does **not** provide global analytic continuation or a global
Fuglede--Kadison/Brown-measure identity.

### Step 5 — Chiral adjoint introduces inverse labels (identity)

The chiral square is

\[
 B_t^2=
 \begin{pmatrix}
  L_tL_t^*&0\\0&L_t^*L_t
 \end{pmatrix}.
\]

For every entry \(a_{ji}=c_{ij}\lambda(g_{ij})\) of \(L_t\), the Hilbert--
Schmidt trace contains

\[
 a_{ji}^*a_{ji}
 =|c_{ij}|^2\lambda(g_{ij}^{-1}g_{ij})
 =|c_{ij}|^2 I.
\]

Therefore

\[
 \boxed{
 \mathfrak t(B_t^2)
 =2\sum_i|d_i(t)|^2
  +2\sum_{i\to j\in E_\times}|c_{ij}(t)|^2.}
\]

With opaque real cross weights, the first mixed term is exactly

\[
 \boxed{2\sum_{i\to j}y_{ij}^2.}
\]

Thus the first `gg^-1` and `g^-1g` contributions occur at power two.  They
are positive and cannot be removed by the canonical group trace.

### Step 6 — Endpoint and symmetric phase dependence (identity)

Write \(u_i=p_i^{-1}\) and
\(\theta_{ij}(t)=t\log(p_j/p_i)\).  For an undirected adjacent pair,

\[
\begin{aligned}
 |c_{ij}^{(\alpha)}|^2+|c_{ji}^{(\alpha)}|^2
 &=\bigl(\alpha^2+(1-\alpha)^2\bigr)(u_i+u_j)\\
 &\quad+4\alpha(1-\alpha)\sqrt{u_i u_j}
        \cos\theta_{ij}(t).
\end{aligned}
\]

At \(\alpha=0\) or \(1\), the interference coefficient vanishes.  Indeed,
the whole transfer differs from height zero by a left or right diagonal
unitary.  Every interior \(0<\alpha<1\), including the symmetric
\(\alpha=1/2\), admits genuine chiral moment/singular motion.  This motion is
caused by the same adjoint backtracking terms that violate the clean Euler
ledger.

### Step 7 — Control logic (exact propositions and numerical observations)

- **Inverse-paired free labels:** reverse edges carry \(g^{-1}\), so mixed
  base identities occur already at \(r=2\).  Exact.
- **Finite nonabelian `S3`:** the chosen distinct labels first create mixed
  identity paths at \(r=4\).  The admissible two-edge composite on
  `1<->2` is a transposition, so its square is the first identity.  Exact.
- **Finite abelian `C5`:** positive labels first close through the finite
  relation at \(r=10\).  The chain requires an even number of cross steps,
  while `C5` requires a multiple of five, hence `lcm(2,5)=10`.  Exact.
- **Positive free abelian `Z`:** all mixed base paths remain nonzero positive
  exponents at every order.  Exact; this refutes free-group specificity.
- **Random positive free labels:** repeated labels still cannot cancel; all
  32 seeds pass through \(r=8\).  Exact for the tested range, with the
  all-order positive-word proof applying to every seed.
- **Non-arithmetic inventories:** the base ledger proof does not inspect
  the masses.  Shuffled, composite, and random inventories also show chiral
  motion.  Exact ledger plus numerical motion is therefore non-selective.

### Step 8 — Finite-section/FK boundary (reframed interpretation)

Compressed word-ball matrices have a positive-labelled skew graph with no
finite directed cross cycle.  Their ordinary eigenvalues and determinants
therefore collapse to the loop diagonal exactly, even while their singular
distributions move strongly with height.  This is a finite-dimensional
`PROVES_TOO_MUCH` effect.

Free-group balls are not a Følner sequence.  Hence the normalized finite
section determinant is not, without another theorem, a global FK
approximation.  Rooted regularized hermitization is a more relevant local
proxy.  At the small probe \(z=0.25\), its error against the local Euler
trace-log value decreases from approximately \(2.21\times10^{-4}\) at
radius 1 to \(5.81\times10^{-9}\) at radius 4.  At \(z=1\), height zero, the
proxy instead separates from the loop value by approximately
`0.675, 0.940, 1.082, 1.156`, while the ordinary finite determinants remain
loop-exact.  This is numerical evidence that the local trace-log identity
must not be promoted globally.

## Remarks and Interpretation

- The construction genuinely restores recurrence in the *symbolic base*.
  The group extension removes mixed cycles from the identity sector rather
  than removing them from the graph.
- The essential algebraic datum is a positive cone, not noncommutativity.
  A free group is a natural universal implementation but not a selective
  arithmetic mechanism.
- More precisely, the all-order base statement is a conical/positive monoid
  cocycle theorem: no group inverses or commutators are used until the
  adjoint is introduced.
- Chiral self-adjointization and clean holomorphic trace ledgers pull in
  opposite directions: the adjoint necessarily exposes backtracking norm
  squares.
- Ordinary eigenvalues of finite positive-word compressions are maximally
  misleading here; singular and rooted hermitization data contain the hidden
  radical geometry.

## Boundaries and Non-Claims

- No Riemann-zero table is read, fitted, or used for validation.
- No global FK determinant formula is claimed.
- No Brown measure is computed or certified.
- No analytic continuation, functional equation, Gamma factor, target
  divisor, or zero-counting law is obtained.
- The chiral family is not a Hilbert--Pólya operator.
- Finite-group regular traces verify group algebra, not a large-group limit.
- Word-ball normalized empirical measures are not accepted as canonical
  von Neumann spectral measures because the free group is nonamenable.

## Open Risks

- A different graded or relative chiral trace might cancel the quadratic
  backtracks, but all-order cancellation may also erase the desired divisor.
- Passing to an infinite atom inventory requires trace-ideal and determinant-
  class estimates not supplied by this finite prototype.
- The rooted hermitization proxy needs a convergence theorem before any Brown
  or FK interpretation beyond the local series disk.
- Since positive abelian labels already work, an additional intrinsic source
  principle is required to select the label system and prevent the argument
  from proving too much.
