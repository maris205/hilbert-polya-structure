# Stochastic, semigroup, and rewrite Phase-2 scout

**Status:** twelve literal systems screened; no paper number frozen; external
release **HOLD_EXTERNAL**  
**Date:** 2026-08-30  
**Write boundary:** this report and the three unique
`proof_spikes/stoch_*.py` controls only.  No shared ledger, manuscript, or Git
state was changed.

This is an idea-generation and cheap-theorem-pilot record, not a novelty,
priority, or ownership certificate.  A bounded literal-source search that
finds no direct hit grants permission for another proof/owner gate only.

## Executive result

Exactly **12** systems were made literal before ranking.  Three deterministic
standard-library pilots passed **79,345 exact assertions**:

| pilot | assertions | result |
|---|---:|---|
| `stoch_idempotent_commutation.py` | 1,687 | exact normal forms/fibres and block-time support; two tempting time-law simplifications killed |
| `stoch_one_defect_queue.py` | 231 | exact central-binomial defect probability and two-point absorption law |
| `stoch_rees_motif_kill.py` | 77,427 | hoped-for nonlocal Green phase killed: the phase is exactly an adjacent `XY` count |

The intake ranking is:

- **PROMOTE TO PROOF/OWNER GATE, not to a paper number:** S01 and S02.
- **RESERVE:** S06, S07, and S10.
- **KILL:** S03, S04, S05, S08, S09, S11, and S12.

The two promotes use different carriers and proof engines.  S10 is explicitly
same-engine reserve behind S02 and cannot coexist with it in one five-paper
batch without a substantially different theorem package.

The assertion counts are bounded falsification gates, not infinite-family
proofs.  S01 exhausts all words through length eight, fibres through bound
nine, and blocks `a<=5,b<=6`; S02 checks `2<=n<=24` plus independent frontier
recursions; S03 checks associativity through `m=6`, all words through length
twelve for `m<=7`, and the unwrapped law through length seventeen.  Every
infinite-family formula below is therefore a **theorem contract** until proved
symbolically by one of its stated routes.

## Zero-credit firewall

The following are supporting machinery only: reset/regeneration, a finite
state reduction, a transfer matrix, a stationary law, Perron--Frobenius
pressure, and generic LLN/CLT/LDP.  The nearest external owners include
probabilistic rewriting
([Avanzini--Dal Lago--Yamada](https://arxiv.org/abs/1802.09774),
[Kassing--Giesl](https://arxiv.org/abs/2409.17714)); finite-semigroup walks
([Brown](https://arxiv.org/abs/math/0006145),
[Ayyer--Schilling--Steinberg--Thiery](https://arxiv.org/abs/1401.4250),
[Rhodes--Schilling](https://arxiv.org/abs/1711.10689)); random-input
synchronization ([Nicaud](https://arxiv.org/abs/1404.6962),
[Gusev](https://arxiv.org/abs/1404.6731)); and abelian-network halting and
recurrence ([Bond--Levine](https://arxiv.org/abs/1409.0169),
[Chan--Levine](https://arxiv.org/abs/1804.03322)).  Trace/heap rationality is
also direct background
([Krob--Mairesse--Michos](https://arxiv.org/abs/cs/0112012)).

Internally, P89/P93/P101/P104/P116 close reset, reflection, cap--floor,
monomial contraction, and finite-gap max-plus reuse.  P99/P111 close ordinary
signed-shear or word-area repackaging.  P35/P100 and the previous T4 reserve
make affine-register/valuation systems high-risk.  P79/P86 close hidden
finite-memory and local finite-field processes.  These subtractions are
applied system by system below.

## Ranked ledger

| ID | literal system | early signal | decision |
|---|---|---|---|
| S01 | random redexes `BA -> AB`, `AA -> A` | confluent normal form but strategy-dependent full interval of times; exact fibres | **PROMOTE** |
| S02 | two-stage legal queue with the single defect `(1,1) --B*--> (0,0)` | central-binomial rare defect and exact two-point absorption law | **PROMOTE** |
| S03 | two-generator Rees sandwich over `C_m` | phase is only `#XY mod m` | **KILL** |
| S04 | block-preserving rotation/collapse automaton | rank two but phase is trailing-reset age | **KILL** |
| S05 | left/right partial shifts of an interval | rank is ordinary random-walk range | **KILL** |
| S06 | `x -> x+1`, `x -> 2x` on `Z/(2^k r)` | rank entrance couples to an ordered odd-part affine phase | **RESERVE** |
| S07 | competing rewrites `CB -> BC`, `BA -> AB` | one critical overlap creates schedule-dependent terminal laws | **RESERVE** |
| S08 | a fixed signed-tropical Fibonacci pair | orientation-sensitive first balance, but a finite sign-pattern semigroup | **KILL** |
| S09 | opposite ordinary unipotent shears | exact cancellation is a simple random walk | **KILL** |
| S10 | three-stage tandem queue with one `(1,1,1)` defect | weighted Weyl-chamber defect probability; same engine as S02 | **RESERVE** |
| S11 | iid delayed subtractive Euclid | negative-binomial time is only geometric idle delay | **KILL** |
| S12 | two nilpotent ordinary matrices | only two alternating words survive and grow | **KILL** |

## Twelve literal system contracts

### S01. Commutation--idempotence random rewrite — PROMOTE

- **Phase and update.**  On words over `{A,B}` of length at most `N`, choose
  uniformly among all current redex occurrences and apply either
  `BA -> AB` or `AA -> A`.  The focused size family starts from
  `B^b A^a`, with `a>=1`, `b>=0`.
- **Pair-specific anomaly.**  The system terminates and is confluent, with
  normal form `A B^b` whenever an `A` is present.  Nevertheless its random
  absorption time depends on the reduction strategy.  The exact pilot found

  ```text
  #{w: |w|<=N and NF(w)=A B^b} = binom(N+1,b+1)-1,
  supp T(B^b A^a) = {a+b-1,...,ab+a-1},
  P[T=a+b-1] = 1/a                         (b>0).
  ```

  Thus the fibre is closed while the time law is genuinely non-degenerate
  and has every intermediate value.
- **Owner/internal subtraction.**  General termination, confluence, and
  probabilistic-rewrite semantics receive zero credit.  Pure commutation
  height is trace-monoid background.  The residual would have to be the
  specific interaction of one oriented commutation with one idempotent
  deletion, including a closed absorption PGF or comparably strong extremal
  law.  This is not a push--pop system (P93), an eroder (P100), or a fixed
  finite-memory kernel.
- **Two routes.**  (1) A rewriting route uses the invariant number of `B`s,
  survival of at least one `A`, critical-pair control, and crossing/deletion
  genealogies.  (2) A probabilistic-combinatorial route treats redex histories
  as weighted linear extensions and derives recurrences/involutions for time
  support and extremal masses.
- **Kill condition.**  Kill if a direct owner gives this reduction-time law;
  if the general PGF admits no structure beyond state-by-state recursion; or
  if the monoid is covered by an existing random-walk theorem with the same
  fibres and time outputs.

### S02. One-defect two-stage abelian queue — PROMOTE

- **Phase and update.**  Start at `(n,0)` in `N^2`.  Among legal updates choose
  uniformly:

  ```text
  A(x,y) = (x-1,y+1)                         if x>0,
  B(x,y) = (x,y-1)                           if y>0,
  B*(1,1) = (0,0)                            instead of B(1,1).
  ```

  The process stops at `(0,0)`.  Removing the starred exception gives the
  schedule-independent abelian baseline of duration `2n`.
- **Pair-specific anomaly.**  For `n>=2`, with

  ```text
  rho_n = binom(2n-2,n-1)/4^(n-1),
  P(T_n=2n-2)=rho_n,       P(T_n=2n)=1-rho_n.
  ```

  Hence `E T_n=2n-2rho_n`,
  `Var(T_n)=4rho_n(1-rho_n)`, and the effect of a single local
  noncommuting state has probability asymptotic to
  `1/sqrt(pi(n-1))`, not an exponential or constant probability.
- **Owner/internal subtraction.**  Abelian-network halting and odometers are
  owned background.  The residual is only this one-defect schedule law and
  its exact boundary/frontier transform.  There is no reset carrier, PF
  pressure, or CLT claim, and the process is not P114 peeling or P101
  cap--floor synchronization.
- **Two routes.**  (1) The workload `2x+y` proves the two-point support, while
  a harmonic recursion gives the defect probability and the boundary value
  `h(1,k)=2^{-k}`.  (2) Unfold the reflected queue into a symmetric walk and
  use a bridge/reflection or cycle-lemma count to obtain the central binomial
  coefficient directly.
- **Kill condition.**  Kill if the exact defect law is already owned; if the
  bridge reduction leaves no network-specific second theorem; or if a
  complete proof cannot produce a structural frontier law in addition to the
  two-point distribution.

### S03. Binary Rees sandwich motif — KILL

- **Phase and generators.**  Let
  `S_m=M[C_m; {0,1},{0,1}; P]`, with additive group `C_m` and
  `p_(lambda,j)=lambda*j mod m`, for `m>=2`.  Multiplication is

  ```text
  (i,g,lambda)(j,h,mu)=(i,g+lambda*j+h,mu).
  ```

  Use `X=(0,0,1)` and `Y=(1,0,0)`.
- **Observed anomaly and its collapse.**  Literal multiplication gives
  `phase(w)=#XY(w) mod m`; before reduction this looked like a Green-class
  phase.  In fact
  `#{w in {X,Y}^n:#XY(w)=k}=binom(n+1,2k+1)`.  At fair bias its unwrapped mean
  and variance are `(n-1)/4` and `(n+1)/16` for `n>=2`.
- **Subtraction.**  Completely simple/Rees structure and finite-semigroup
  walks are owner territory.  The remaining statistic is an adjacent motif,
  colliding with the finite-memory firewall and P111-style word statistics.
- **Two routes.**  Direct Rees multiplication and a binary-run decomposition
  independently give the same formula.
- **Kill condition.**  Already met: the hoped nonlocal rank--group coupling is
  exactly a length-two word statistic.

### S04. Rank-two block-collapse automaton — KILL

- **Phase and generators.**  On `Q_m=Z_m x {0,1}`, set
  `R(i,b)=(i+1,b)` and `C(i,b)=(0,b)`; compose iid letters chronologically.
- **Anomaly.**  Before the first `C` the image rank is `2m`; afterwards it is
  exactly two and never one.  The two-point image is
  `{(t,0),(t,1)}`, where `t` is the trailing `R`-run since the last `C`.
- **Subtraction.**  Although the automaton is globally nonsynchronizing, it
  is two independent reset automata.  Random-input synchronization and P89/
  P116 reset structure own the mechanism.
- **Two routes.**  Image-set composition and renewal-age decomposition.
- **Kill condition.**  Already met: rank greater than one does not prevent a
  blockwise reset/regeneration reduction.

### S05. Two partial interval shifts — KILL

- **Phase and generators.**  In the symmetric inverse monoid on
  `{0,...,m-1}`, let `L(i)=i-1` for `i>0` and undefined at zero; let
  `R(i)=i+1` for `i<m-1` and undefined at `m-1`.
- **Anomaly.**  For prefix sums `S_0=0,S_1,...,S_n` of the `+/-1` word,

  ```text
  rank(w) = max(0, m-[max_t S_t-min_t S_t]),
  displacement(w)=S_n.
  ```

  The zero-map entrance is exactly the first time the walk range reaches
  `m`.
- **Subtraction.**  Finite inverse-semigroup harmonic analysis is established
  background ([Malandro](https://arxiv.org/abs/1110.5679)); here the literal
  transient reduces further to the classical range of a one-dimensional
  random walk and collides with P93 reflection.
- **Two routes.**  Intersect the domains of the partial maps, or apply the
  reflection principle to the prefix walk.
- **Kill condition.**  Already met: both advertised outputs are direct
  random-walk statistics.

### S06. Affine doubling with an odd minimal image — RESERVE

- **Phase and generators.**  On `Z/mZ`, with `m=2^k r`, `k>=1` and odd
  `r>1`, take `R(x)=x+1` and `D(x)=2x` under iid chronological composition.
- **Pair-specific anomaly.**  Every word has the affine form
  `x -> 2^s x+c`, where `s=#D` but `c` records the order of the letters.
  Its rank is `m/2^min(s,k)`, so the `k`th `D` is the entrance to the
  nonsynchronizing minimal rank `r`; after entrance, `c mod r` and
  `2^s mod r` retain a nontrivial group phase.  The entrance time is simple,
  but the ordered odd-part phase need not be.
- **Owner/internal subtraction.**  General finite-semigroup and finite-linear
  dynamics are zero credit.  P35 affine semigroups, P100 valuation erasure,
  P104 parity, and the previous affine-register T4 reserve are severe
  collisions.
- **Two routes.**  (1) Induct on the affine normal form `(s,c)`.  (2) Apply
  CRT to the 2-primary collapse and odd invertible component, then use group
  characters for the phase law.
- **Kill condition.**  Kill if the phase is conjugate to T4, if it reduces to
  total letter counts or a standard affine-group walk, or if no output remains
  after the rank/negative-binomial entrance is subtracted.

### S07. Competing critical-pair rewrite — RESERVE

- **Phase and update.**  On fixed-content words with `a` letters `A`, `b`
  letters `B`, and `c` letters `C`, choose a redex occurrence uniformly and
  apply `CB -> BC` or `BA -> AB`.  The focused initial word is
  `C^c B^b A^a`.
- **Pair-specific anomaly.**  The potential
  `I(C before B)+I(B before A)` drops by one each step, but the overlap `CBA`
  is nonconfluent:

  ```text
  CBA -> BCA,      CBA -> CAB.
  ```

  Thus two individually sorting rules create a schedule-dependent terminal
  distribution rather than merely a random duration.
- **Owner/internal subtraction.**  Probabilistic rewriting and adjacent-swap
  chains are background; P90 makes any Rule-184/TASEP reduction fatal.  The
  residual would need an exact block-family terminal law or fibre
  factorization, not a generic absorbing-chain computation.
- **Two routes.**  Resolve interacting critical pairs by heaps/linear
  extensions, or derive a lattice-path recursion for the two moving
  interfaces.
- **Kill condition.**  Kill on equivalence to a standard multispecies
  exclusion/sorting chain, or if the terminal law has no closed form beyond
  exponential-state DP.

### S08. Fixed signed-tropical Fibonacci phase — KILL

- **Phase and generators.**  In the symmetrized max-plus semiring, write
  `0+`, `0-`, and `0o` for positive, negative, and balanced elements of
  magnitude zero.  The size parameter is the product length `n`; take

  ```text
  X = [[0+,0+],[0+,-infinity]],
  Y = [[0+,0-],[0+,-infinity]].
  ```

- **Anomaly.**  `Y tensor X` has a balanced top-left entry from equal
  opposite-sign paths, whereas `X tensor Y` is unbalanced.  Cancellation is
  genuinely orientation-sensitive.
- **Subtraction.**  Symmetrized-tropical deterministic spectral theory is
  active ([Akian--Gaubert--Kiani--Tavakolipour](https://arxiv.org/abs/2412.10602));
  random signed-Fibonacci products are also direct neighbors.  With all
  magnitudes fixed at zero, the generated sign-pattern semigroup is finite,
  so a first-balance law would be only finite memory and collide with P79/
  P116.
- **Two routes.**  Signed path cancellation and literal finite-semigroup
  multiplication.
- **Kill condition.**  Already met for this literal pair: there is no
  unbounded magnitude clock after the finite-memory contribution is removed.

### S09. Opposite ordinary shears — KILL

- **Phase and generators.**  Take
  `U_+=[[1,1],[0,1]]` and `U_-=[[1,-1],[0,1]]` iid with fair signs, with
  product length `n` as the size parameter.
- **Anomaly.**  Every word equals `[[1,S_n],[0,1]]`; for even `n` it is the
  identity with mass `binom(n,n/2)/2^n`.
- **Subtraction.**  This is exactly a simple random walk embedded in a matrix
  entry, with direct collisions against P99 shear and P111 word statistics.
- **Two routes.**  Unipotent multiplication and binomial reflection/local
  limit calculations.
- **Kill condition.**  Already met: the matrix carrier adds no temporal
  theorem to the underlying walk.

### S10. One-defect three-stage tandem queue — RESERVE SAME ENGINE

- **Phase and update.**  Start from `(n,0,0)`.  Uniformly choose among legal
  transfers `A:x->y`, `B:y->z`, and `C:z->sink`, except that at `(1,1,1)` the
  update `C*` sends the entire state to `(0,0,0)`.
- **Pair-specific anomaly.**  The workload `3x+2y+z` decreases by one under
  ordinary updates.  Therefore
  `T_n` is supported on `{3n-5,3n}`; the lower mass is the probability that a
  weighted three-dimensional legal-schedule path reaches the defect and
  selects `C` there.  A determinant/tableau form for this mass would be a
  stronger higher-rank analogue of S02.
- **Owner/internal subtraction.**  All abelian-network and tandem-queue
  baselines are zero credit.  This is the same one-defect engine as S02 and is
  held only as a higher-dimensional fallback.
- **Two routes.**  Workload plus a harmonic recursion on the legal region;
  weighted Weyl-chamber paths/reflections or nonintersecting-path
  determinants for the defect mass.
- **Kill condition.**  Kill if the mass lacks a closed form, if it is a known
  queueing/tableau probability, or if its proof package is not materially
  different from S02.  At most one of S02/S10 may advance.

### S11. Iid-delayed subtractive Euclid — KILL

- **Phase and generators.**  On positive pairs `(x,y)`, choose `L` or `R`
  fairly at every tick:

  ```text
  L(x,y)=(x-y,y) if x>y, else (x,y),
  R(x,y)=(x,y-x) if y>x, else (x,y),
  ```

  and stop at `x=y=gcd(x_0,y_0)`.
- **Anomaly.**  If `ell(x,y)` is the deterministic subtractive-Euclid length,
  each effective subtraction waits for an independent geometric success, so

  ```text
  E[z^T] = (z/(2-z))^ell(x,y).
  ```

- **Subtraction.**  Continued fractions/randomized Euclid own the arithmetic
  object; the randomness here creates only idle self-loops and collides with
  the historical arithmetic-clock and random-waiting firewalls.
- **Two routes.**  Continued-fraction quotient sums and a sum of independent
  geometric waiting times.
- **Kill condition.**  Already met: after deleting idle ticks the process is
  deterministic, so the stochastic law is scientifically thin.

### S12. Alternating survival of two nilpotent matrices — KILL

- **Phase and generators.**  Under ordinary multiplication take

  ```text
  A=[[0,2],[0,0]],       B=[[0,0],[1,0]].
  ```

  Both square to zero; choose them iid fairly, with product length `n` as the
  size parameter.
- **Anomaly.**  A length-`n` product is nonzero exactly for the two alternating
  words, with survival probability `2^(1-n)`.  Conditional on survival, its
  unique nonzero entry has magnitude `2^#A`; deterministic alternation grows
  while the iid product becomes zero almost surely.
- **Subtraction.**  Matrix mortality/joint spectral behavior is background.
  Here survival is the regular language of alternating words, colliding with
  finite memory and the rare-alternating-word controls already used in P116.
- **Two routes.**  Literal matrix units and a two-state forbidden-repeat
  automaton.
- **Kill condition.**  Already met: both the rare event and conditional growth
  are a length-two word constraint.

## Exact-pilot falsification ledger

1. **S01:** `BAA` has times two and three with masses `1/2,1/2`; therefore
   content and normal form do not determine time.  `BBAA` has masses
   `1/2,1/8,3/8` at times three, four, five; therefore the full interval law
   is not uniform.
2. **S02:** the defect probabilities begin `1/2,3/8,5/16,35/128,...` and
   satisfy `rho_(n+1)/rho_n=(2n-1)/(2n)`.  Both the constant-probability and
   geometric-probability conjectures are false.
3. **S03:** associativity, literal products, dynamic programming, and the
   closed motif histogram agree exactly.  The proposed nonlocal Green phase
   is false; it is `#XY mod m`.

No floating-point value is used as evidence.  The pilots use only integers,
`fractions.Fraction`, exhaustive words, and independent structural formulas.

## Recommendation

Advance S01 and S02 only to a bounded primary-owner search and full proof
contract.  S01 still needs a closed general absorption law stronger than its
exact recursion; S02 needs a second structural theorem, preferably a closed
frontier distribution or a parameter-recovery statement.  Keep S06 and S07
as different-carrier reserves and S10 only as a same-engine fallback.  The
seven kills should remain in the ledger so that rank-two reset, Rees motifs,
random-walk range, signed shear, idle-delay Euclid, and alternating nilpotent
products are not regenerated under new names.

External posting, specialist contact, novelty, priority, authorship, and
venue decisions remain **HOLD_EXTERNAL**.
