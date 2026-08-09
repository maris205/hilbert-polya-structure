# HCS-C24 experiment plan

## Material Passport

- Origin Skill: `ars-codex academic-research-suite / experiment-agent`
- Origin Mode: `plan`
- Origin Date: `2026-08-09T10:40:00Z`
- Verification Status: `UNVERIFIED`
- Version Label: `code_plan_v1`

This file codifies the frozen C24 plan inherited from
`../docs/hcs_c24_system_switch.md`.  It does not claim that later result fields
were known when the system and cutoffs were selected.

## Claim-driven question

For the literal labeled permutation \((1234)/(4321)\), decide in one large
round whether its chronology-preserving, unsmoothed metaplectic transfer
extension can be an ordinary nuclear Fredholm object.

The round has three ordered gates:

1. reconstruct the exact Rauzy system, genus, stratum, changing intersection
   forms, and closed-loop symplectic action;
2. enumerate primitive labeled directed cycles through elementary length 12, keeping
   every cyclic phase and selecting eventually-positive labeled objects by an invariant
   eventual-positivity test;
3. prove either noncompactness of the metaplectic operator class or a
   legitimate ordinary determinant theorem.

## Frozen object and conventions

- alphabet: \(\{1,2,3,4\}\);
- permutation: top `1234`, bottom `4321`; no substitution is allowed;
- moves: `t` means top winner, `b` means bottom winner;
- edge matrix: \(B_e=I+E_{\ell,w}\);
- chronology: later edges multiply on the left;
- cycle quotient: cyclic phase only, never reversal;
- primitivity/eventual-positivity selector: every cyclic phase matrix has a strictly positive
  power by the 4-by-4 Wielandt bound 10;
- cutoff: elementary lengths 1 through 12;
- repetition audit: \(r=1,\ldots,6\);
- clock: \(\ell(w)=\log\lambda_{\rm PF}(B_w)\);
- forbidden inputs: primes, zeta zeros, affine clock fitting, unfolding,
  averaged cocycles, oscillator cutoffs, and heat regularization.

## Registered measurements

- Rauzy state/edge counts and every edge transport identity;
- directed primitive labeled free-cycle counts by length;
- phase-by-phase positivity exponent;
- complete winner set and central first-return decomposition;
- chronological matrix and fixed-frame symplectic conjugate;
- reciprocal characteristic polynomial;
- exact \(\det(I-B_w^r)\) for \(r\le6\);
- rational isolating interval for the Perron root;
- number of cycles on \(\det(I-B_w)=0\);
- exact and atomic metaplectic essential-norm gates.

## Independent verification

The checker may not import the producer.  It must:

- use the seven-word hyperelliptic automaton;
- verify cycle completeness independently from
  \(P_n=n^{-1}\sum_{d\mid n}\mu(d)\operatorname{tr}(A^{n/d})\);
- reconstruct every released monodromy from edge tokens;
- verify rational root intervals and singular-locus counts;
- reject the registered chronology, transposition, power, phase, and trace
  mutations.

Exact equality is required.  No statistical tolerance is relevant.

## Pass, kill, and pivot rules

- `PASS_ORDINARY_FREDHOLM` requires a canonical ordinary compact/nuclear
  operator and a legal trace expansion.
- `KILL` occurs if a nonzero branch compression or nonzero norm-summable
  discrete metaplectic aggregate forces noncompactness.
- A pointwise character Euler product on the labeled return coding also dies
  if its primitive labeled cycles lie on \(\det(I-M)=0\).
- A distributional, semifinite, or continuously smoothed object survives only
  as a new source-lock problem; no arbitrary regularizer is admitted.

Regardless of sign, the release must state the Route-A boundary and must not
invoke Route B without an A2/A3 object.
