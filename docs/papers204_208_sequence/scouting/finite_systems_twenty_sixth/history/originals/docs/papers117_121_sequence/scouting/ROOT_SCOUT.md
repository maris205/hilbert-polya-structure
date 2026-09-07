# Root breadth scout: twelve explicit P117–P121 candidates

**Date:** 2026-08-30  
**Status:** idea-generation and cheap theorem pilots complete; no paper number
frozen.  
**External actions:** `HOLD_EXTERNAL`.

The root lane defined twelve literal updates.  Three deterministic scripts
executed **1,043,867 assertions**.  The scripts are scouting evidence only;
any promoted paper must ship a fresh canonical verifier aligned with its final
claims.

## R1 — parity two-path toggling on ordered DAGs

- **Phase/update:** a strict upper-triangular matrix \(A\in M_n(\mathbb F_2)\),
  viewed as an ordered DAG; set \(T(A)=A+A^2\).  Thus an arc is toggled exactly
  when it has an odd number of directed two-step witnesses.
- **Early signal:** all states are periodic.  The exact iterate is
  \(T^t(A)=\sum_{j\preceq t}A^{2^j}\), where \(j\preceq t\) means binary
  submask.  The pointwise period is the least \(2^s\) for which
  \(A^{2^{2^s}}=0\); the maximum period is the least \(2^s\) with
  \(2^{2^s}\ge n\).  Enumeration through \(n=6\) verified 372,549 assertions
  and period counts \(1,2,4\) exactly as predicted.
- **Owner subtraction:** scalar \(x\mapsto x^2+x\) over finite fields already
  has direct functional-graph work
  ([Wadsanthata–Panraksab](https://doi.org/10.1080/00150517.2019.12427669));
  generic finite-linear graphs are also zero-credit.  The residual is the
  noncommutative ordered-DAG phase, the path-parity interpretation, and its
  sharp double-exponential period filtration.  P97 and P103 remain internal
  collision checks.
- **Two routes:** additive-polynomial/Lucas composition in the one-generated
  matrix algebra; independent cancellation involutions on families of
  concatenated directed paths.
- **Kill condition:** a direct owner for this exact ordered-DAG map, or failure
  to turn the period filtration into more than the scalar iterate identity.
- **Disposition:** **promote to owner/proof gate (A−)**.

## R2 — odd-run reversal on labelled binary cycles

- **Phase/update:** a labelled cyclic binary word of length \(n\); in parallel,
  flip every bit belonging to a cyclic run of odd length.
- **Early signal:** every orbit has period at most two.  A state is recurrent
  exactly when all cyclic run lengths have the same parity.  For odd \(n\),
  only the two constant words recur; for \(n=2m\), the exact fixed-state count
  is \(2^{m+1}-2\), while the period-two census is an explicit odd-composition
  sum.  The maximum preperiod is
  \((n-1)/2\) for odd \(n\) and \(\lfloor(n-2)/4\rfloor\) for even \(n\).
  Exhaustion through \(n=16\) verified 262,188 assertions and sharp witnesses.
- **Owner subtraction:** targeted searches located run enumeration and
  parity-CA background, but no direct owner for this variable-neighbourhood
  synchronous map.  That bounded non-hit is not a novelty claim.  Ordinary
  word erosion, fixed-radius CA, P80, P90, and P100 receive zero credit.
- **Two routes:** a cyclic composition coalescent that retains equal-parity
  boundaries; a boundary-set parity encoding giving the recurrent census and
  an independent minimal-length argument for sharp transients.
- **Kill condition:** the claimed even-length sharp bound fails beyond the
  proof invariant, or the rule turns out to be a named block automaton with
  the same temporal census.
- **Disposition:** **promote to owner/proof gate (A)**.

## R3 — permutation bond contraction

- **Phase/update:** the disjoint union \(\bigsqcup_{k\le n}S_k\); contract every
  maximal positional run whose successive values differ by one to one entry,
  then standardize.
- **Early signal:** maximum depth is \(n-1\), and exactly \(2^{n-1}\)
  permutations attain it for \(2\le n\le9\).  The bounded script verified
  409,130 assertions.  One-step fibres admit a three-state orientation model
  over the target's signed bond path.
- **Owner subtraction:** enumeration of permutations with adjacencies is
  classical background, and P105 already occupies deletion-standardization on
  permutations.  Only the iterative contraction depth and signed fibre model
  could count.
- **Two routes:** monotone-interval inflation with a path partition function;
  recursive two-preimage construction of extremals.
- **Kill condition:** inability to clear P105 at the mechanism level, even if
  the numerical theorem is true.
- **Disposition:** **reserve (B); internal collision is currently too high**.

## R4 — odd-common-neighbour toggling on Eulerian graphs

- **Phase/update:** an Eulerian simple graph with adjacency matrix \(A\) over
  \(\mathbb F_2\); toggle \(ij\) when \(i,j\) have an odd number of common
  neighbours, so again \(A\mapsto A+A^2\).
- **Early signal:** Eulerianity is invariant and the additive-polynomial
  iterate survives.
- **Owner/internal subtraction:** graph-polynomial and parity-path background,
  P97 support squaring, and R1 use exactly the useful engine.
- **Two routes:** matrix powers and parity pairing of walks.
- **Kill condition/disposition:** same-engine batch collision is immediate;
  **kill** in favour of R1.

## R5 — odd-degree support toggle in uniform hypergraphs

- **Phase/update:** for an \(r\)-uniform hypergraph \(H\), let \(O(H)\) be its
  odd-degree vertices and replace
  \(H\) by \(H\triangle\binom{O(H)}r\).
- **Early signal:** the next odd-degree support is controlled solely by
  \(\binom{|O|-1}{r-1}\bmod2\).
- **Owner/internal subtraction:** Lucas parity is standard; graph parity and
  closure lanes are crowded.
- **Two routes:** incidence-vector algebra and direct double counting.
- **Kill condition/disposition:** the support either clears or stays in one
  step, leaving no independent temporal output; **kill (theorem-thin)**.

## R6 — Robin-Hood balancing of integer partitions

- **Phase/update:** among weakly decreasing \(n\)-part compositions of \(m\),
  subtract one from a largest part, add one to a smallest part, and resort,
  stopping when the range is at most one.
- **Early signal:** depth equals half the \(L^1\) distance to the balanced
  endpoint.
- **Owner/internal subtraction:** this is the classical unit majorization
  transfer, and P113 just occupied partition absorption.
- **Two routes:** majorization energy and explicit surplus–deficit matching.
- **Kill condition/disposition:** the clock is essentially the definition;
  **kill (direct owner + thin)**.

## R7 — fixed-point deletion and standardization

- **Phase/update:** delete every fixed point of a permutation and standardize
  the remaining pattern.
- **Early signal:** exhaustive checks show every nonfixed state lands on a
  derangement after one update.
- **Owner/internal subtraction:** rencontres enumeration and P105
  deletion-standardization consume all remaining content.
- **Two routes:** rank comparison and permutation-matrix deletion.
- **Kill condition/disposition:** depth never exceeds one; **kill**.

## R8 — parallel sink reversal on path orientations

- **Phase/update:** orient a labelled path and simultaneously reverse every
  edge incident with a sink.
- **Early signal:** the edge word reduces to a parallel particle update with a
  short exact period law.
- **Owner/internal subtraction:** source-to-sink firing, chip firing, and
  rotor/orientation dynamics are direct owners; on a path the useful factor is
  Rule 184, already occupied by P90.
- **Two routes:** chip-firing potentials and particle-word conjugacy.
- **Kill condition/disposition:** literal conjugacy to occupied dynamics;
  **kill**.

## R9 — synchronous mex recomputation on layered DAGs

- **Phase/update:** bounded labels on a finite DAG; every vertex replaces its
  label by the mex of its out-neighbours' current labels.
- **Early signal:** dependency shells freeze from sinks upward.
- **Owner/internal subtraction:** Sprague–Grundy recursion is classical and
  the transient is the DAG height, colliding with feed-forward clocks and
  P114.
- **Two routes:** induction on height and triangular dependency matrices.
- **Kill condition/disposition:** no non-height temporal invariant emerged;
  **kill**.

## R10 — unnormalised Dodgson condensation

- **Phase/update:** an \(n\times n\) matrix over a finite field is sent to its
  \((n-1)\times(n-1)\) array of contiguous \(2\times2\) minors.
- **Early signal:** Toeplitz and rank-stratified inputs show factorized iterates
  with characteristic-dependent zeros.
- **Owner/internal subtraction:** Desnanot–Jacobi/Dodgson condensation owns the
  determinant identities; dimension loss supplies a forced, low-credit clock.
- **Two routes:** determinant condensation identities and nonintersecting path
  expansions.
- **Kill condition:** no sharp bad-characteristic fibre anomaly after direct
  identities are removed.
- **Disposition:** **fragile reserve (C)**.

## R11 — cyclic adjacent-gcd smoothing

- **Phase/update:** for a cyclic divisor word \((a_i)\) of a fixed integer
  \(N\), set \(a_i'=\gcd(a_i,a_{i+1})\).
- **Early signal:** the \(t\)-th iterate is the gcd of a cyclic window of
  length \(t+1\), hence consensus time is the covering radius of minimal
  valuation positions.
- **Owner/internal subtraction:** this is a semilattice erosion; P100 already
  occupies valuation deletion.
- **Two routes:** primewise min-plus morphology and direct divisor-lattice
  induction.
- **Kill condition/disposition:** the exact iterate is an ordinary closure
  window; **kill**.

## R12 — numerical-semigroup blowup iteration

- **Phase/update:** from a numerical semigroup
  \(S=\langle m,n_2,\ldots,n_k\rangle\), pass to
  \(\langle m,n_2-m,\ldots,n_k-m\rangle\) with redundant/nonpositive
  generators removed.
- **Early signal:** on Arf and maximal-embedding-dimension families, the
  multiplicity sequence is the transient clock.
- **Owner/internal subtraction:** blowups and multiplicity sequences are
  classical singularity/numerical-semigroup machinery; the visible clock is
  already the named invariant.
- **Two routes:** Apéry-set transport and value-semigroup geometry.
- **Kill condition/disposition:** no residual beyond the classical
  multiplicity sequence; **kill**.

## Root-lane ranking

| rank | candidate | early exact signal | disposition |
|---:|---|---|---|
| 1 | R2 odd-run reversal | recurrence census + sharp parity-dependent transient | promote A |
| 2 | R1 ordered-DAG parity toggle | pointwise and maximal double-exponential period filtration | promote A− |
| 3 | R3 bond contraction | sharp depth + extremal census + fibre spin model | reserve B |
| 4 | R10 Dodgson condensation | possible bad-characteristic factor anomaly | reserve C |
| 5–12 | R4–R9, R11–R12 | owned, same-engine, one-step, or height-only | kill |

No GPU pilot applies: these are theoretical finite systems.  The deterministic
exact spikes replace an empirical pilot and remain bounded falsification
evidence, not proof and not a novelty certificate.
