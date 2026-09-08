# AS1 round-nine spectral probe: exact memory and a nonuniform frustration bound

2026-09-08 UTC. AI-assisted hand derivation by an independent bounded
helper lane. No mathematical program was executed. This is an author
proof draft, not an independent review of its own claims.

## Claim

Keep the fixed matrices, finite projective transfer matrices and original
whole-secondary-circle [AS1 contract](../../arithmetic_spectral/FROZEN_CONTRACTS.md).
The bounded probe asks whether nonperipheral spectra approach nonreal
points of the unit circle, or whether a uniform spectral/resolvent
exclusion holds there as the congruence depth increases.

The full spectral-accumulation question remains unresolved. The precise
new auxiliary results proved below are:

1. The untwisted matrices retain exact admissible symbolic memory
   $m_k=\lceil k/3\rceil$. In the normalized supremum norm, for every
   $\zeta\in S^1\setminus\{1\}$,
   $$
   \frac{m_k}{4\pi}
   \le \| (\zeta I-L_{1,k})^{-1}\|_{\infty}
   \le m_k+\frac1{|\zeta-1|}
               +\frac2{|\zeta+\varphi^{-2}|}.                 \tag{A}
   $$
   The lower bound holds already on the closed graph component. Thus a
   depth-uniform full-space supremum-norm resolvent bound on any nonreal
   unit-circle arc is false, even for the trivial character.
2. For arbitrary finite characters, an explicit two-cycle frustration
   inequality holds. If $z$ is any eigenvalue of $L_{\chi,k}$, then
   $$
   1-|z|\ge
   \frac{|\chi(g_0)-1|^2}{128\varphi^2(1+K_k)},\qquad
   K_k=\varphi^2(1+s_k\varphi^{s_k}),\quad
   s_k=1+2\lceil k/6\rceil,                                 \tag{B}
   $$
   where $g_0=\lambda_b^2/\lambda_{ab}$. This estimate is not uniform
   in depth. Fixed-cycle phase data cannot supply a positive uniform
   lower bound on a prescribed nonreal arc, by the already proved
   finite-character approximation theorem.

## Status

**PROVABLE AS STATED** for (A), (B), and the exact memory lemma below.

**NOT CURRENTLY JUSTIFIED** for either nonreal spectral accumulation or
uniform spectral exclusion over all characters and depths. No conclusion
about continuation of the exponentiated full AS1 zeta follows from this
helper alone. A failure of one resolvent norm criterion does not imply a
failure of analytic continuation.

## Assumptions and imported inputs

The complete accepted [round-seven proof](../../continuation_round7/spectral_scout/AS1_PROOF_PACKAGE.md)
and [nonauthor review](../../continuation_round7/spectral_review/INDEPENDENT_REVIEW.md)
were read. Their all-depth peripheral theorem is an input, not rerun.

For $k\ge1$, the state set is $X_k=\mathbb Z/2^k\mathbb Z$. With an
even initial state required for $A$, the projective maps and multipliers
are
$$
f_B(r)=\frac{2+4r}{3+2r},\quad h_B(r)=3+2r,
\qquad
f_A(r)=\frac{1+3r}{3+r},\quad h_A(r)=3+r.
$$
The denominators are units, $B$ sends every state to an even state, and
$A$ sends an even state to an odd state. On their allowed domains,
$$
f_C(r)-f_C(s)=\frac{8(r-s)}{h_C(r)h_C(s)}.                     \tag{1}
$$
The directed graph has one closed strongly connected component $C_k$,
containing the $B$ fixed residue $r_B$. Every state reaches $r_B$ after
$m_k$ consecutive $B$ steps. Every active periodic word has its unique
projective cycle in $C_k$. These graph facts and the characteristic-unit
identities are imported from the accepted proof.

For a character $\chi$ of $(\mathbb Z/2^k\mathbb Z)^\times$, let
$T_{\chi,k}$ be the accepted transfer matrix. Set
$$
v(r)=\begin{cases}\varphi,&r\text{ even},\\1,&r\text{ odd},\end{cases}
\quad V_k=\operatorname{diag}(v),\quad
L_{\chi,k}=\varphi^{-1}V_k^{-1}T_{\chi,k}V_k.
$$
Its row coefficients have the form $p_C(r)\chi(h_C(r))$, where
$$
\begin{array}{c|cc}
 &p_B&p_A\\\hline
r\text{ even}&\varphi^{-1}&\varphi^{-2}\\
r\text{ odd}&1&0.
\end{array}                                                  \tag{2}
$$
Thus $P_k=L_{1,k}$ is a Markov operator and
$\|L_{\chi,k}\|_\infty\le1$. The normalized supremum norm is the
original $T$-space norm $\max_r |F(r)|/v(r)$ under the diagonal
identification. Every restriction to $C_k$ uses ordinary supremum norm
after normalization.

The imported peripheral theorem says that the only unit-modulus
eigenvalue of $P_k$ is $1$. No additional peripheral eigenvalue is
being inferred from the arguments below.

## Notation

- $m=m_k=\lceil k/3\rceil$ is the exact memory length used here.
- $\tau=-\varphi^{-2}$ is the second eigenvalue of the two-state parity
  Markov chain.
- $\sigma_j(r)\in\{A,B\}$ denotes the $j$th most recent edge label in
  any incoming path of length $m$ ending at $r\in C_k$, where $j=0$
  is the most recent label. Lemma 1 proves this is well-defined.
- $h(A)=1$, $h(B)=\tau$, and $h_j(r)=h(\sigma_j(r))$.
- $\lambda_b$ and $\lambda_{ab}$ are the odd characteristic roots of
  the chronological returns $B$ and $BA$. Their reductions give the
  cocycle products on their projective cycles. Their quotient $g_0$
  is the generator used in the accepted all-depth theorem.

## Proof strategy and dependency map

1. The factor-eight difference identity permits backwards recovery of
   one symbol while losing three binary digits. This proves exact
   finite memory and realization of every admissible finite block.
2. Past-coordinate observables form a long shift chain under $P_k$.
   A phase-weighted sum gives approximate eigenvectors in the
   supremum norm, with a bounded defect and linearly growing norm.
3. After $m$ untwisted steps, all functions map into the two-dimensional
   parity subspace. A finite resolvent identity gives the matching
   linear upper bound and separates the nilpotent memory from spectra.
4. A normalized eigenvector loses little modulus along sufficiently
   likely paths when its eigenvalue is near the unit circle. A local
   variance identity then estimates edge phase defects on the $b$ and
   $ab$ cycles, giving (B).
5. The already proved finite-character phase approximation demonstrates
   why those two finite cycle tests alone do not become uniform.

## Proof

### Step 1. Exact backwards decoding and realization

**Lemma 1.** For every $r\in C_k$, all incoming paths of length $m$
ending at $r$ have the same sequence of $m$ labels. Every finite label
block of length $m$ having no adjacent $AA$ occurs in this way for some
$r\in C_k$.

An incoming path of every finite length exists because $C_k$ is strongly
connected and nonempty. Consider two incoming paths with the same
endpoint modulo $2^k$. Their last labels agree: odd output requires
$A$, and even output requires $B$. For that common label, (1) shows
that the predecessor residues agree modulo $2^{k-3}$ whenever $k>3$.
Both denominators in (1) are odd, so this assertion follows by cancelling
the explicit factor $8$, not by assuming invertibility of $f_C$ modulo
$2^k$. The predecessor parities consequently agree if $k-3\ge1$.

Repeat this cancellation. Recovery of $m$ labels requires only
$k-3(m-1)\ge1$, which holds for $m=\lceil k/3\rceil$. At the
last stage no recovery of an additional predecessor is required. This
proves uniqueness also for $k=1,2,3$, where $m=1$.

For realization, begin at the even state $r_B$ and apply the desired
block in chronological order. Its first symbol is allowed whether it
is $A$ or $B$, and every later symbol is allowed precisely because the
block has no adjacent $AA$. The endpoint belongs to $C_k$, since this
component is closed. The just-proved uniqueness identifies its decoded
past block with the prescribed one. No cyclic admissibility at the two
ends of this finite block is required. $\square$

For every edge $r\to r'=f_C(r)$ in $C_k$, Lemma 1 gives
$$
\sigma_0(r')=C,\qquad
\sigma_j(r')=\sigma_{j-1}(r)\quad(1\le j<m).                 \tag{3}
$$
To verify (3), append the edge to any incoming path of length $m-1$
at $r$, then apply uniqueness of the recovered $m$ labels.

### Step 2. A bounded-defect approximate eigenvector at every phase

Equation (2) and (3) imply
$$
P_k h_0=\tau h_0,\qquad P_k h_j=h_{j-1}\quad(1\le j<m).    \tag{4}
$$
For the first identity, an odd state has $h_0=1$ and its sole successor
has value $\tau$. At an even state the expected successor value is
$\tau/\varphi+1/\varphi^2=\tau^2=\tau h_0$. This verifies both
parities directly. Also $\|h_j\|_\infty=1$ by block realization.

Fix $\zeta\in S^1$ and set, on $C_k$,
$$
G_{m,\zeta}=\sum_{j=0}^{m-1}\zeta^j h_j.
$$
The shift identity (4) telescopes to
$$
(\zeta I-P_k)G_{m,\zeta}
   =\zeta^m h_{m-1}-\tau h_0,\qquad
\|(\zeta I-P_k)G_{m,\zeta}\|_\infty\le1+|\tau|.          \tag{5}
$$
This identity remains valid when $m=1$; in that case both endpoint
observables are $h_0$.

We next prove the norm lower bound rather than assume cancellation is
small. Let $I=\{0,2,4,\ldots\}\cap\{0,\ldots,m-1\}$ and
$M=|I|\ge m/2$. Averaging over $t\in[0,2\pi]$ gives
$$
\frac1{2\pi}\int_0^{2\pi}
\sum_{j\in I}\max\{\operatorname{Re}(e^{-it}\zeta^j),0\}\,dt
=\frac{M}{\pi}.
$$
Each summand has integral $2$, which proves the displayed equality.
Hence there is $t$ and a subset
$J=\{j\in I:\operatorname{Re}(e^{-it}\zeta^j)>0\}$ with
$$
\left|\sum_{j\in J}\zeta^j\right|\ge M/\pi.               \tag{6}
$$
The block placing $A$ at positions $J$ and $B$ elsewhere is admissible:
the set $J$ has no neighboring indices. By Lemma 1 it is realized by a
state $r_J$. The all-$B$ block is realized by $r_B$. Therefore
$$
G_{m,\zeta}(r_J)-G_{m,\zeta}(r_B)
=(1-\tau)\sum_{j\in J}\zeta^j,
$$
and the triangle inequality together with (6) gives
$$
\|G_{m,\zeta}\|_\infty
\ge\frac{(1-\tau)M}{2\pi}
\ge\frac{(1-\tau)m}{4\pi}.                                \tag{7}
$$
The argument uses two actual states rather than dropping the
possibly nonzero all-$B$ baseline.

For $\zeta\ne1$, the imported peripheral theorem makes
$\zeta I-P_k$ invertible, also on $C_k$. Combining (5) and (7), and
using $1-\tau=1+|\tau|$, yields
$$
\|(\zeta I-P_k|_{C_k})^{-1}\|_\infty\ge m/(4\pi).        \tag{8}
$$
The full-space resolvent has at least this norm. Indeed the restriction
map $R:\ell^\infty(X_k)\to\ell^\infty(C_k)$ has norm one,
intertwines $P_k$ with its closed-component operator, and each function
on $C_k$ has a norm-preserving extension to $X_k$. Apply these facts to
the two resolvents. This proves the lower half of (A).

### Step 3. Matching upper bound and why this is not spectral accumulation

Let $H_0$ be the subspace of functions depending only on parity. For
every word of length $m$, (1) gives contraction by $2^{-3m}$, so its
terminal state modulo $2^k$ is independent of the initial state among
states on which that word is admissible. Whether a word is admissible
depends only on its first symbol and the initial parity, followed by
the no-$AA$ rule.

For the untwisted Markov operator, the probability of an allowed word
$w$ with terminal state $r_w$ telescopes to
$$
p_w(r)=\frac{v(r_w)}{\varphi^m v(r)}.
$$
It therefore depends on the initial state only through parity. Summing
the word contributions proves
$$
P_k^m\ell^\infty(X_k)\subset H_0.                           \tag{9}
$$
In particular, the operator induced on the quotient by $H_0$ is
nilpotent of index at most $m$. On $H_0$, (4) and $P_k1=1$ give
the two eigenvalues $1$ and $\tau$. Thus all other eigenvalues of the
untwisted operator are exactly zero. This rank/quotient consequence,
not a new peripheral argument, identifies the source of the growth in
(8): finite-memory nilpotence and nonnormality.

The stationary functional of the two-state chain is a convex average,
so its projection $\Pi_1$ onto the constants has supremum norm one.
The other spectral projection on $H_0$ is $I-\Pi_1$, of norm at most
two. Consequently
$$
\|(\zeta I-P_k|_{H_0})^{-1}\|_\infty
\le\frac1{|\zeta-1|}+\frac2{|\zeta-\tau|}.                 \tag{10}
$$
For $\zeta\in S^1\setminus\{1\}$, the finite resolvent identity is
$$
(\zeta I-P_k)^{-1}
=\sum_{j=0}^{m-1}\zeta^{-j-1}P_k^j
 +\zeta^{-m}(\zeta I-P_k)^{-1}P_k^m.
$$
Each $P_k^j$ has norm at most one, and (9) permits use of (10) on the
last term. This proves the upper half of (A). On a compact arc avoiding
$1$, both bounds have order $m$, uniformly in the point of that arc.

The approximate eigenvectors constructed here coexist with the exact
untwisted nonzero spectrum $\{1,\tau\}$. They are therefore a concrete
counterexample, within these actual matrices, to interpreting
approximate eigenvectors with growing matrix dimension as nearby true
eigenvalues without a conditioning bound. The zero-eigenvalue nilpotent
part contributes nothing to positive-power traces. $\square$

### Step 4. Quantitative modulus transport for a twisted eigenvector

Let $L=L_{\chi,k}$, let $z$ be an eigenvalue, and choose
$LF=zF$ with $\|F\|_\infty=1$. Put
$$
\rho=|z|,\quad \delta=1-\rho,\quad a(r)=1-|F(r)|.
$$
The norm bound implies $0\le\rho\le1$. Choose $r_*$ with
$|F(r_*)|=1$.

If one allowed path of length $t$ from $r_*$ to $r$ has Markov
probability $q>0$, expanding $L^tF=z^tF$ at $r_*$ and using the
triangle inequality gives
$$
\rho^t\le q|F(r)|+(1-q),\qquad
a(r)\le\frac{1-\rho^t}{q}\le\frac{t\delta}{q}.             \tag{11}
$$
Other paths may have the same endpoint; selecting one term is still a
valid upper bound because every remaining term has modulus at most
its Markov probability.

The word $B^m$ reaches $r_B$ with probability at least $\varphi^{-m}$.
Let $\ell=\lceil k/6\rceil$ and $s=1+2\ell$. The word
$B(AB)^\ell$ reaches the even fixed state $r_0$ of the chronological
two-step return $AB$, namely $f_B\circ f_A$. The initial $B$ makes
the path admissible from either parity. The subsequent $\ell$
two-step returns contract by $2^{-6\ell}$, so their endpoint is
the fixed residue modulo $2^k$. The path probability is at least
$\varphi^{-s}$ by (2). Since $s\ge m$, (11) yields
$$
a(r_B)\le s\varphi^s\delta,\qquad
a(r_0)\le s\varphi^s\delta.                                 \tag{12}
$$
Write $r_1=f_A(r_0)$, the odd second vertex of this two-cycle.
The eigenvalue equation at $r_0$, singling out the $A$ edge of
probability $\varphi^{-2}$, gives
$$
a(r_1)\le\varphi^2(1-\rho|F(r_0)|)
\le\varphi^2(\delta+a(r_0)).                                 \tag{13}
$$
Thus all three vertices in (12)--(13) satisfy
$a(r)\le K\delta$, where
$K=\varphi^2(1+s\varphi^s)=K_k$.

### Step 5. Edge variance and the two-cycle frustration inequality

At a state $r$, write $t_C=\chi(h_C(r))F(f_C(r))$. Equation (2)
and the eigenvalue equation give the exact variance identity
$$
\sum_Cp_C(r)|t_C-zF(r)|^2
=\sum_Cp_C(r)|t_C|^2-|zF(r)|^2
\le1-\rho^2|F(r)|^2
\le2(\delta+a(r)).                                          \tag{14}
$$
At each of the three selected cycle vertices the right-hand side is
at most $2(1+K)\delta$. Every allowed individual edge has probability
at least $\varphi^{-2}$. Hence each of their edge defects is at most
$$
E=\varphi\sqrt{2(1+K)\delta}.                               \tag{15}
$$

First suppose $\delta\le1/(2K)$. All three values $|F(r)|$ are then
at least $1/2$. On the $B$ self-loop, (15) gives
$$
|\chi(\lambda_b)-z|\le2E.                                  \tag{16}
$$
On the two-cycle, write its edge weights as $q_A,q_B\in S^1$ and
its two defect equations as
$$
q_AF(r_1)=zF(r_0)+e_A,\quad
q_BF(r_0)=zF(r_1)+e_B,\quad |e_A|,|e_B|\le E.
$$
Eliminating $F(r_1)$ gives
$$
(q_Aq_B-z^2)F(r_0)=ze_A+q_Ae_B.
$$
The cocycle product is $q_Aq_B=\chi(\lambda_{ab})$, so
$$
|\chi(\lambda_{ab})-z^2|\le4E.                             \tag{17}
$$
Equations (16)--(17) imply
$$
|\chi(g_0)-1|
=|\chi(\lambda_b)^2-\chi(\lambda_{ab})|
\le8E.
$$
Squaring and using (15) proves
$|\chi(g_0)-1|^2\le128\varphi^2(1+K)\delta$.

If instead $\delta>1/(2K)$, the same final inequality follows from
$|\chi(g_0)-1|^2\le4$ and
$128\varphi^2(1+K)\delta>64\varphi^2(1+K)/K>4$.
This proves (B) for every eigenvalue, including zero and the small
depths where $\chi(g_0)=1$. $\square$

For a nonzero $z=\rho\zeta$ in the small-$\delta$ case, (16) also
gives the explicit phase estimate
$$
|\chi(\lambda_b)-\zeta|\le2E+\delta.                       \tag{18}
$$
It is a necessary condition for a near-peripheral eigenvalue, not a
construction of one.

### Step 6. The exact failure boundary of the frozen mechanism

At depth $k\ge4$, the accepted generator lemma says that a nontrivial
$\chi(g_0)$ is a root of unity of order dividing $2^{k-3}$. Its
smallest possible nonzero distance from $1$ is
$2\sin(\pi/2^{k-3})$. Thus (B) gives a positive finite-depth gap
when $\chi(g_0)\ne1$, but its displayed lower bound decays with depth.
This is not a replacement proof of the accepted sharp peripheral
classification and supplies no uniform spectral gap.

More importantly, for every fixed $\zeta\in S^1$ and every
$\varepsilon>0$, the accepted finite-character approximation theorem
applied to the two words $b,ab$ provides some depth and character with
$$
|\chi(\lambda_b)-\zeta|<\varepsilon,\qquad
|\chi(\lambda_{ab})-\zeta^2|<\varepsilon.
$$
These imply $|\chi(g_0)-1|<3\varepsilon$. If
$\zeta\notin\{1,-1\}$, the required conductors become unbounded
as the error tends to zero, again by the accepted theorem.
Consequently no positive uniform phase-frustration lower bound on a
nonreal arc can be extracted from these two cycle discrepancies alone.

This is only failure of the proposed sufficient mechanism. It does not
show that the chosen characters have eigenvalues near $\zeta$;
longer cycles may still impose an obstruction. Conversely (A) says a
uniform full-space supremum-norm resolvent bound is actually false,
not merely unproved. The two conclusions have different logical strength.

## Corrections or missing assumptions

No additional assumption is needed for the proved auxiliary statements.
The original full spectral and analytic questions would require a
different quantitative assertion, such as:

1. a gap for the nonzero spectra uniform in depth on each nonreal arc,
   together with a trace/determinant or conditioned resolvent bound that
   survives the congruence weights;
2. or actual nonperipheral eigenvalue accumulation, established by a
   true spectral argument with dimension/conditioning control, followed
   by a separate full-sum noncancellation theorem.

The ordinary supremum-norm resolvent bound with a constant independent
of depth cannot be such an assertion, by (A). An estimate permitted to
grow with $k$, a quotient norm suppressing nilpotent memory, or a
trace-level estimate is not ruled out. No estimate of these kinds is
proved here for nontrivial characters uniformly over the tower.

## Open risks and scope

- This helper has not yet received nonauthor review. The coordinator may
  review the actual proof rather than treat the author's status as PASS.
- (A) concerns a specified norm and actual finite matrices; it is not a
  universal Banach-space obstruction.
- A nilpotent Jordan component affects resolvent norms but not the
  positive-power eigenvalue traces. Nothing in (A) forces support of the
  coordinator's weighted eigenvalue measure near nonreal unit phases.
- Finite-dimensional approximate eigenvectors and periodic trace
  approximations are both insufficient to infer true spectral points as
  dimensions grow. The present untwisted example demonstrates the former
  insufficiency explicitly and does not repeat the latter gap.
- The matrix definitions, contraction identity, cycle roots, peripheral
  theorem and finite-character density remain inherited ownership.
  The new local deductions use elementary matrix algebra, finite Markov
  averaging, exact residue decoding and triangle/variance inequalities.
  They are not claimed as new general operator theory.
- No AS1 admission, fifth independent contract, manuscript, formal
  Route-A evaluation, target Euler factor, root number or A2 promotion.

## Source and execution receipt

The inherited sources actually read for this probe are the entire
original frozen contract, entire round-seven author proof, entire
round-seven independent review, round-nine plan, and the relevant
repository state/instructions. Prior primary-paper source checks are
credited only as the earlier review's checks, not this lane's accesses.

The new proofs are self-contained conditional on those accepted local
inputs. No external theorem or unverified publication is inserted to
fill a step. ARS was restricted to source-status/fact-check discipline;
its empirical evidence ladder is not treated as mathematical proof.
No optional programmatic bibliography, full pipeline, cross-model or
human-read profile was activated. `proof-writer` governs the exact
claim/status separation. There is no global novelty clearance.

Actual fresh web search submissions: **0**. Direct external source
opens: **0**. PDF downloads: **0**. Mathematical executions: **0**.
Old computations or accepted-proof reruns: **0**. Git writes: **0**.
