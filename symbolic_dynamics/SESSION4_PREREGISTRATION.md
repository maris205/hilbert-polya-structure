# Session 4 Preregistration and Source Lock

## Identity

- Session: `SD-S4-2026-08-12`
- Family: symbolic dynamics only
- Evaluation framework: Route-A evaluator v0.2.0 and Route-B evaluator v0.2.0
- Primary question: arithmetic symbolic skeleton versus geometric realization
- Status at freeze: candidate definitions frozen; no numerical candidate result
  inspected

## Scope boundary

Allowed variations are finite/countable alphabet, grammar, roof, locally
constant potential, symbolic suspension, transfer operator, and an intrinsic
finite-group or unitary cocycle.

Independent Hénon, symplectic, Hamiltonian-flow, quantum-graph,
operator-algebra, or scattering constructions are outside this session.  Any
such implication is written only to [`ROUND2_CLUES.md`](ROUND2_CLUES.md).

## Global data lock

### Allowed data

- symbolic words, cycles, adjacency matrices, and exact matrix products;
- finite-field arithmetic used by `SD-C01`;
- the mathematical definition of prime squares used by `SD-C02`;
- synthetic conjugation-symmetric control polynomials generated from the fixed
  seeds below;
- primary literature and the six local prior-work papers, with all claims
  independently graded;
- Riemann–von Mangoldt zero counting as a theorem-level asymptotic benchmark.

### Forbidden data

- tables of Riemann zeros in candidate definition, parameter selection,
  training, validation, or testing;
- finite prime tables used to design an adjacency rule;
- assigning a symbol to each rational prime;
- assigning \(\log p\) as a roof or von Mangoldt weights as a potential by
  hand;
- phases chosen from target zeros;
- refitting after a control or cutoff failure;
- coordinatewise assembly of arithmetic, orbit, determinant, and operator
  claims from different systems.

All target-zero error fields in Route-A A2 are therefore `not_applicable`;
this session tests structural compatibility and obstructions rather than a
finite zero fit.

## Randomness lock

- master seed: `20260812`
- renewal on-circle synthetic control: `20260813`
- renewal off-circle synthetic control: `20260814`
- unitary-cocycle control: `20260815`
- shuffled-word control: `20260816`

Only complete seed ledgers are reported.  No best-seed selection is allowed.

## SD-C01 — finite-state arithmetic skeleton

### Frozen object

- phase space: the two-sided full shift \(\Sigma_q=\mathbb F_q^{\mathbb Z}\),
  with `q` restricted in experiments to `2, 3, 5`;
- dynamics: left shift \(\sigma\);
- primitive objects: aperiodic necklaces of length \(n\);
- repetition: word repetition \(\gamma\mapsto\gamma^r\);
- roof: \(\tau\equiv\log q\) per symbol, so
  \(T_{\gamma}=n\log q\);
- potential/cocycle: unit weight and trivial cocycle for the arithmetic
  skeleton;
- determinant convention:
  \[
  D_q(s)=\zeta_{\sigma}(q^{-s})^{-1}=1-q^{1-s}.
  \]
- function space: cylinder functions for the full shift; for the finite-memory
  obstruction, the transfer block acts on
  \(\mathbb C^{|V|}\otimes\mathbb C^d\);

The broader obstruction class consists of a finite directed multigraph with
positive edge roofs \(\tau_e\), complex edge weights \(w_e\), and a
finite-dimensional unitary edge cocycle \(U_e\).  On
\(\mathbb C^{|V|d}\),
\[
B(s)_{ij}=\sum_{e:i\to j}w_e e^{-s\tau_e}U_e,
\qquad D_G(s)=\det(I-B(s)).
\]

### Fixed tests and stop rule

1. Verify the primitive-necklace/irreducible-polynomial count identity.
2. Verify the Euler product and repetition ledger through finite degree.
3. Prove that every nonzero finite-memory determinant above is an exponential
   polynomial with \(n_D(R)=O(R)\).
4. Test finite unitary twists and nonlattice roofs as controls.

If the \(O(R)\) theorem is proved, all finite-memory variants stop as global
completed-\(\xi\) divisor candidates; larger finite matrices are not a reopening
criterion.

## SD-C02 — squarefree admissible shift

### Frozen object

Let \(\mathscr B=\{p^2:p\text{ rational prime}\}\), and set
\[
X_{\rm sf}=\left\{x\in\{0,1\}^{\mathbb Z}:
\operatorname{supp}(x)\bmod p^2
\ne\mathbb Z/p^2\mathbb Z\quad\text{for every }p\right\}.
\]
The dynamics is the left shift.  The roof is one, the potential is zero, and
the determinant convention is the inverse Artin–Mazur zeta whenever periodic
point counts are finite.  The function space used for word and periodic-point
tests is the locally constant cylinder algebra on \(X_{\rm sf}\).

### Fixed tests and stop rule

1. Determine every periodic point exactly.
2. Compute the resulting Artin–Mazur zeta.
3. Compare with the full binary shift, golden-mean shift, finite-modulus
   approximants, and shuffled finite windows.

If the only periodic point is the all-zero point, the candidate stops at A1;
high word entropy is not allowed to substitute for a primitive-orbit ledger.

## SD-C03 — weighted renewal shift

### Frozen object

The graph has a base vertex and one first-return loop of length \(n\) for each
\(n\ge1\) with aggregate complex loop weight \(a_n\).  Its first-return series
and determinant convention are
\[
F(z)=\sum_{n\ge1}a_nz^n,
\qquad D_{\rm ren}(z)=1-F(z),
\qquad \zeta_{\rm ren}(z)=D_{\rm ren}(z)^{-1},
\]
inside the disk of absolute convergence.  Positive systems have
\(a_n\ge0\); signed/complex systems retain the actual phases.  The function
space is the renewal-cylinder algebra, completed only within the declared
absolute-convergence disk; no unspecified Banach-space continuation is used.

### Fixed tests and stop rule

1. Prove the inverse-design statement for every holomorphic germ
   \(H(0)=1\).
2. Prove the positive-real-zero statement under an explicit crossing
   hypothesis.
3. Reconstruct both on-circle and off-circle synthetic target polynomials.
4. Run positive, randomized-phase, and matched-degree controls.

Exact reconstruction of both controls is a `PROVES_TOO_MUCH` failure, not a
success.  No Riemann target is then fitted.

## SD-C04 — Gauss/Mayer transfer candidate

### Frozen object

- phase space: \(\Sigma_{\mathbb N}=\mathbb N^{\mathbb N}\), coding regular
  continued fractions;
- inverse branches: \(\phi_n(z)=(n+z)^{-1}\);
- intrinsic periodic roof:
  \(T_\gamma=2\log\lambda_+(M_\gamma)\), where \(M_\gamma\) is the continued-
  fraction matrix product;
- transfer operator:
  \[
  (\mathcal L_sf)(z)=\sum_{n\ge1}(n+z)^{-2s}
  f\!\left((n+z)^{-1}\right);
  \]
- function space: Mayer's holomorphic Banach-space realization, with the exact
  domain and continuation claims taken only from verified primary sources;
- determinant convention:
  \[
  D_{\rm MG}(s)=\det(I-\mathcal L_s^2)
  =\det(I-\mathcal L_s)\det(I+\mathcal L_s).
  \]

### Fixed tests and stop rule

1. Enumerate primitive symbolic words and exact matrix repetitions.
2. Test cyclic invariance, reversal metadata, matrix-trace collisions, and
   cutoff stability.
3. Approximate the transfer determinant only in a source-supported
   convergence half-plane; label this numerical, never certified continuation.
4. Audit whether rational primes or prime powers index primitive cycles.

If the rational-prime ledger is absent, Route B is forbidden even if the
Fredholm determinant is rigorous.  Any geometric/scattering interpretation is
recorded only as a `ROUND2_CLUE`.

## Route-B lock

`route_b_invocation_allowed: false` for all initial four candidates at
preregistration.
It can change only in an append-only Route-A evaluation that reaches
`A4_ROUTE_B_READY` for the same object, clock, normalization, and determinant.

## Literature-discovery addendum — 2026-08-12T08:31:50Z

The initial four-object lock was preserved.  Two objects discovered during the
source audit were added before any experiment on either object was run.  They
are evaluated separately and are never combined coordinatewise with
`SD-C01`–`SD-C04`.

### SD-C05 — recursive wheel-sieve level shift

Define \(Q_1=2\), and, at level \(k\),

\[
 W_k(r)=\mathbf 1_{\gcd(r,Q_k)=1},\qquad
 q_{k+1}=\min\{n>q_k:W_k(n\bmod Q_k)=1\},\qquad
 Q_{k+1}=Q_kq_{k+1}.
\]

The graph records the deterministic level transition \(k\to k+1\).  Its
intrinsic scale increment is

\[
 \tau_k=\log(Q_{k+1}/Q_k)=\log q_{k+1}.
\]

No prime table, prime-labelled edge, reset edge, potential, or cocycle is
allowed.  The function space for finite checks is the cylinder algebra on the
one-sided path/Bratteli space, and the empty periodic ledger uses the
Artin–Mazur convention \(D_{\rm AM}=1\).  The fixed tests are: verify the recursion against independent
primality through the declared cutoff, count periodic paths exactly, and test
whether a stationary natural extension exists without adding a reset or
prime-indexed components.  If all edges strictly increase the level and hence
there are no periodic paths, the object stops at A1.  Its endogenous prime
generation is not transferable to another candidate.

### SD-C06 — Knauf number-theoretical spin-chain recursion

Set \(h_0=1\) and freeze the binary recursion

\[
 h_{k+1}(\sigma,0)=h_k(\sigma),\qquad
 h_{k+1}(\sigma,1)=h_k(\sigma)+h_k(1-\sigma),
\]

with finite partition functions

\[
Z_k(s)=\sum_{\sigma\in\{0,1\}^k}h_k(\sigma)^{-s}.
\]

At depth \(k\), the function space is
\(\mathbb C^{\{0,1\}^k}\), the clock is \(H_k=\log h_k\), the potential and
cocycle are trivial for the unsigned object, and the determinant convention is
explicitly “finite Dirichlet partition function, not a periodic-orbit
determinant.”  The projective-limit cylinder algebra is used only as the
symbolic state space; no limiting transfer-operator determinant is assumed.

The exact unsigned limit stated in the primary source is tested in its
convergence half-plane against

\[
 Z(s)=\frac{\zeta(s-1)}{\zeta(s)}.
\]

The source's Liouville-weighted observable

\[
 \widetilde Z_k(s)=\sum_\sigma
 \lambda(h_k(\sigma))h_k(\sigma)^{-s}
\]

is audited as an additional arithmetic observable, not credited as an
intrinsic symbolic cocycle.  The fixed tests compare exact multiplicities with
Euler-\(\varphi\) values below the proved finite-depth range and test finite-depth
convergence at preregistered real \(s>2\).  No Riemann zeros are loaded.  The
reported continuation/convergence issue for the signed object is not treated
as solved by numerics.  This candidate stops before Route B unless the same
recursion supplies a canonical primitive-orbit determinant and passes A0–A4.

`route_b_invocation_allowed: false` for `SD-C05` and `SD-C06`.

### SD-C05 implementation-freeze clarification

The frozen file
`wheel_sieve_level_shift/experiments/frozen_config.json` was written before
the SD-C05 run.  It uses the canonical residue-level unpacking implicit in
\(W_k\): vertices are the unit residues \(R_k\), and the lift
\(r\mapsto r+jQ_k\) keeps every branch except the unique one divisible by
\(q_{k+1}\).  This is not an added stationary reset or a second candidate; it
makes the initially stated level-increasing wheel graph reproducible.  Every
edge still raises the level by one, so the preregistered A1 stop rule is
unchanged.  For the empty periodic ledger the standard Artin–Mazur convention
is \(\zeta_{\rm AM}=D_{\rm AM}=1\).
