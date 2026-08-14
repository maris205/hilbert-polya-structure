# PROOF PACKAGE — SD-C22

## Frozen statement

Close the explicit SD-C21 trial-division verifier by sending a successful
terminal state directly back to its input state.  For a prime $p$ let
$m=\lfloor\sqrt p\rfloor$.  The resulting component is a simple directed
cycle $\Gamma_p$ of length

\[
\ell(p)=2+\sum_{d=2}^{m}\left\lceil\frac pd\right\rceil.
\]

Give its edges nonnegative roofs $\tau(e)$ with exact arithmetic total
$\sum_{e\in\Gamma_p}\tau(e)=\log p$.  On the natural counting space
$\ell^2(V)$ define the source-weighted vertex adjacency

\[
L_s\delta_u=e^{-s\tau(u\to v)}\delta_v,
\qquad \operatorname{Re}s>0.
\]

## Dependency graph

```text
expanded Q-state transition table
        |
        +--> exact prime-cycle census --> harmonic asymptotic
        |                                  |
        |                                  v
        |                         log(p)/ell(p) -> 0
        |                                  |
        +--> cyclic weighted block --------+
                           |
                           +--> noncompactness / no Schatten class
                           +--> essential approximate unit circle
                           +--> raw factor 1-z^ell(p) p^(-s)
                           |
                           +--> first-return contraction p^(-s)
                                      |
                                      +--> Paper-04 diagonal collapse
```

## Theorem ledger

### P1. Exact cycle census

For fixed $d\le m$, the path enters $Q_{p,d,2}$, visits quotient states
$q=2,\ldots,\lfloor p/d\rfloor+1$, and then advances to $d+1$.  This branch
uses $\lceil p/d\rceil$ edges from $T_{p,d}$ through the last $Q$-state to
$T_{p,d+1}$.  Adding the input edge and contracted return edge proves

\[
\ell(p)=2+\sum_{d=2}^{m}\left(1+\left\lfloor\frac pd\right\rfloor\right).
\]

The elementary bounds are

\[
p(H_m-1)+2\le\ell(p)\le p(H_m-1)+m+1.
\]

The lower bound is strict for $p\ge5$ and is an equality for $p=2,3$.
Since $m=\sqrt p+O(1)$ and $H_m=\log m+\gamma+O(m^{-1})$,

\[
\ell(p)=\frac12p\log p+(\gamma-1)p+O(\sqrt p).
\]

### P2. One weighted cycle

Let $B$ be a weighted cyclic permutation on an $\ell$-cycle with edge
weights $w_j=e^{-s\tau_j}$ and total roof $T=\sum_j\tau_j$.  Then

\[
B^\ell=e^{-sT}I,\qquad
\operatorname{spec}(B)=\{e^{-sT/\ell}\omega:\omega^\ell=1\},
\]

the singular values are $|w_1|,\ldots,|w_\ell|$, and

\[
\det(I-zB)=1-z^\ell e^{-sT}.
\]

### P3. Clock dilution and essential norm

For every nonnegative exact allocation, at least one edge $e_p$ satisfies

\[
\tau(e_p)\le\frac{\log p}{\ell(p)}.
\]

The vectors $\delta_{s(e_p)}$ are orthonormal across the disjoint prime
blocks, while

\[
\|L_s\delta_{s(e_p)}\|
  =e^{-\sigma\tau(e_p)}
  \ge p^{-\sigma/\ell(p)}\longrightarrow1.
\]

Thus $L_s$ is not compact.  Since all weights have modulus at most one and
the lower bound persists after deleting finitely many blocks,
$\|L_s\|_{\mathrm{ess}}=1$.

### P4. No finite Schatten repair

On $\Gamma_p$, Jensen's inequality gives, for every $q>0$,

\[
\sum_{e\in\Gamma_p}e^{-q\sigma\tau(e)}
\ge \ell(p)e^{-q\sigma\log p/\ell(p)}.
\]

The right-hand side tends to infinity and in particular does not tend to
zero.  Summing over prime blocks shows that the accepted restriction belongs
to no $\mathcal S_q$, $0<q<\infty$.

### P5. Essential approximate spectrum

Each finite prime block has normalized eigenvectors at eigenvalues
$p^{-s/\ell(p)}\omega$, $\omega^{\ell(p)}=1$.  Because
$p^{-s/\ell(p)}\to1$ and roots of unity of unbounded orders approximate every
$\lambda\in\mathbb T$, select one eigenvector per disjoint block with
eigenvalue tending to $\lambda$.  The vectors are orthonormal and hence weakly
null, giving a singular Weyl sequence.  Therefore

\[
\mathbb T\subset\sigma_{\mathrm{ap,ess}}(L_s),
\]

and $I-zL_s$ is not Fredholm for $|z|=1$.

### P6. Orbit product and first return

The finite-block identity gives the normally convergent graph-step product

\[
D_{\mathrm{orb}}^{\mathrm{raw}}(s,z)
=\prod_p(1-z^{\ell(p)}p^{-s}),
\qquad \operatorname{Re}s>1,\ |z|\le1.
\]

At $z=1$ this is $1/\zeta(s)$.  It is a combinatorial orbit product, not the
ordinary Fredholm determinant of the noncompact $L_s$.  First return to
$\Sigma=\{I_p\}$ yields

\[
R_s\delta_{I_p}=p^{-s}\delta_{I_p},
\qquad
\det(I-zR_s)=\prod_p(1-zp^{-s}).
\]

The return map is trace class for $\operatorname{Re}s>1$ but has contracted
the verifier to the already-known prime diagonal.  Graph-step and return-step
markers coincide only at $z=1$, unless $z^{\ell(p)}$ is explicitly
transported through induction.

### P7. Exact compactness criterion for disjoint cycles

For disjoint cycles indexed by $a$ with lengths $\ell_a$ and prescribed total
roofs $T_a$, a fixed allocation is compact exactly when
$\min_e\tau_{a,e}\to\infty$.  Some nonnegative allocation with those totals
is compact exactly when $T_a/\ell_a\to\infty$.  Necessity follows from the
minimum-roof edge; sufficiency follows from uniform allocation.

For $T_p=\log p$ and $\ell(p)\sim\frac12p\log p$, the ratio tends to zero,
the opposite extreme.

### P8. Universal total-decider control

Let a total deterministic decider accept an infinite support $S$ and let its
closed accepted computation for $n\in S$ have length $\ell_M(n)$.  Under
exact total roof $\log n$, a compact allocation can exist only if
$\log n/\ell_M(n)\to\infty$ along the accepted subsequence.  If
$\ell_M(n)/\log n\to\infty$, its block radii tend to one and clock dilution
recurs.  Any decider can be given an acceptance-independent uniformly
prescribed delay, for example $n$ dummy steps on input $n$.  Hence this
compiler mechanism is support-agnostic: it is not prime selectivity.

## Claim boundary

- This is not a new abstract compactness criterion for weighted shifts.
- It does not rule out dynamical zeta functions in general.
- It rules out the ordinary whole-vertex Fredholm determinant for the frozen
  source-weighted adjacency on counting $\ell^2(V)$.
- Positive roofs tending to zero remain legitimate in countable-state
  suspension theory; the conclusion is operator-theoretic.
- First return is legitimate, but it changes the object and collapses the
  arithmetic computation.
- Overlapping recurrent grammars, cancellations, quotient spaces, and
  regularized or semifinite determinants are outside the theorem.

## Frozen route verdict

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_PASS_ANALYTIC,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```
