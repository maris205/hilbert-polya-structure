# HCS-C25 experiment plan

## Material Passport

- Origin Skill: `ars-codex academic-research-suite / experiment-agent`
- Origin Mode: `plan`
- Origin Date: `2026-08-10T00:00:00Z`
- Verification Status: `UNVERIFIED_AT_FREEZE`
- Version Label: `c25_code_plan_v1`

This plan was frozen before the C25 certificate and independent checker were
released.  It records the large decision gate and does not retroactively tune
the system to the output.

## Claim-driven question

Take the actual countable full-branch Rauzy first-return model and weighted
transfer operator used by Avila--Gouëzel--Yoccoz (AGY).  After adjoining the
unsmoothed infinite-dimensional oscillator representation of its symplectic
cocycle, can either of the following standard realizations be an ordinary
compact/nuclear Fredholm object?

1. the published bounded-derivative `C^1` transfer space, vector-valued in
   the oscillator fibre;
2. the naturally normalized `L^2` transfer realization over the invariant
   probability measure.

The secondary structural question is whether two distinct chronological
Rauzy branches can project to the same matrix and then cancel through the
central sign of the metaplectic cover.

## Frozen object and conventions

- labeled alphabet: `1,2,3,4`;
- literal seed permutation: top `1234`, bottom `4321`;
- AGY section base state: top `1342`, bottom `4321` (state 4 in the sorted
  seven-state graph);
- `t`: top winner; `b`: bottom winner;
- edge matrix: `B_e = I + E_(loser,winner)`;
- chronology: later edges multiply on the left;
- auxiliary complete loop: `eta = tbttbtbb`;
- section word: `gamma_star = t^64 eta^8`;
- inverse branch: radial projectivization of `B_gamma^T`;
- dimension: `d=4`, hence inverse Jacobian `J = exp(-4 r)`;
- fibre: the unsmoothed oscillator Hilbert space `L^2(R^2)`;
- determinant target: an ordinary nuclear/trace-class Fredholm determinant
  for the twisted transfer operator;
- forbidden inputs: primes, Riemann zeros, fitted clocks, averaged transition
  matrices, oscillator cutoffs, heat kernels, and post-selected branches.

The long initial top run and eight complete blocks are a deterministic
source-lock witness, not a fitted periodic-orbit search.

## Gates

### Gate 1: source-locked AGY section

Reconstruct the seven-state labeled Rauzy graph and verify that
`gamma_star` is closed, eight-complete, strongly positive by the AGY
`3d-4` criterion, and neat both by the AGY sufficient condition and by an
exact no-proper-border check.  Verify the chronological matrix, transported
intersection form, positivity, determinant, and projective inverse-branch
formulas.

### Gate 2: all-length chronology decoder

Given a matrix of a path from a fixed permutation, transpose it and inspect
the two candidate winner/loser rows at the current state.  Prove that exactly
the true first edge has componentwise winner-row dominance, subtract the
loser row, update the permutation, and iterate.  Matrix-entry sum must
strictly decrease until the identity is reached.

Pass requires an all-length proof.  Finite stress tests are mutation tests,
not the logical basis of the claim.

### Gate 3: exact branch compression

For the AGY raw transfer operator on bounded `C^1` fibre-valued functions,
place a `C^1` bump strictly inside one inverse-branch image and evaluate the
output at one point.  The full branch sum must compress exactly to a nonzero
scalar multiple of one infinite-dimensional metaplectic unitary.

Independently, normalize by the invariant density on `L^2(mu)`.  Prove
boundedness for `Re(s)>=0`, isolate one branch by its cylinder projection,
and test the unitary-axis coisometry identity.

## Registered outputs

- exact seven-state/fourteen-edge graph;
- all elementary matrices and form-transport identities;
- `eta` and `gamma_star` tokens, winner sets, complete-block boundaries, and
  no-border certificate;
- exact `B_gamma_star`, determinant, entry positivity, and projective rational
  witness points;
- decoder theorem metadata and exhaustive/mutated finite checks;
- raw `C^1` branch-compression theorem;
- normalized `L^2` branch-compression and coisometry theorem;
- Route-A tuple and explicit surviving scope.

## Independent verification

The checker may not import the producer.  It must independently rebuild the
Rauzy graph and matrices, reconstruct the section witness, replay the decoder,
and reject at least chronology, transpose, winner/loser, Jacobian-exponent,
section-word, and border mutations.  Exact equality is required.

## Pass, kill, and pivot rules

- `PASS_ORDINARY_FREDHOLM` requires a source-locked compact/nuclear operator
  and a legal determinant theorem.
- `KILL_C1` occurs if the exact bump/evaluation compression is nonzero.
- `KILL_L2` occurs if a nonzero branch compression survives on the bounded
  normalized operator.
- `NO_COLLISION_ESCAPE` occurs if the all-length decoder is proved.
- Failure of the deterministic section witness invalidates this application
  rather than authorizing a replacement chosen from a scan.
- Holomorphic spaces without branch-supported localizers, distributional or
  flat traces, semifinite determinants, and geometrically forced continuous
  smoothing remain new candidates.  They are not repaired versions of the
  operator tested here.

Route B is forbidden unless a genuine Route-A determinant first survives.
