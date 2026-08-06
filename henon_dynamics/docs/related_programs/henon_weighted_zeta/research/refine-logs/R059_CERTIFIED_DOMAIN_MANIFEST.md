# R059 Certified-Domain Cycle/Operator Manifest

**Frozen:** 2026-08-02, after a disclosed read-only float64 development
precheck but before 100-digit classification or restricted-operator production  
**Protocol SHA-256:** f94801f5b7abd5baaebd4c859a3662af4cf6d63954b1f4b18aaa6e8d3596f2b6  
**Compute:** 32 AMD EPYC vCPU, 60 GB RAM  
**Frontier-model component:** none; this is deterministic symbolic dynamics,
high-precision orbit refinement, and sparse finite-volume computation

## 1. Problem anchor

R058 proves a conservative hyperbolic survivor but does not yet identify which
members of the existing period-1--12 catalog witness its periodic words, nor
does it compare cycles and an operator on that same certified domain. R059
adds an exact contraction/conjugacy theorem on the explicitly defined
four-h-set survivor, and separately audits the catalog and finite-resolution
operator data without making global claims about the full Hénon map.

## 2. Frozen claims

**C1 primary -- finite-period numerical symbolic witness bridge.** Through
period 12, the frozen 747-orbit (a=6) catalog should contain exactly one
unambiguous 100-digit numerical witness for every primitive periodic word of
the R058 four-state SFT and no extra numerically strict h-set-contained word.
This is not an interval/Krawczyk certificate.

Minimum convincing evidence is equality of canonical word sets period by
period, not merely equality of aggregate counts. The exact expected primitive
counts are


| Period | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| (P_n(A)) | 1 | 0 | 1 | 2 | 2 | 2 | 4 | 5 | 8 | 11 | 18 | 25 |

There are 79 expected primitive symbolic orbits through period 12.
The complete expected word sets were generated from (A) without loading the
catalog and frozen in `R059_EXPECTED_SYMBOLIC_WORDS.json`; their canonical
word-set SHA-256 is
`9adbee4ad2bf15227e6ae1c7462b298f215dacf7d7957919d106ef72f9c40a07`.

**Development disclosure.** Before the final protocol freeze, a read-only
float64 planning audit exposed a 79-orbit match with the full expected period
count vector. C1 is therefore a high-precision confirmation and mechanism
audit of a disclosed development observation, not a held-out replication or
independent discovery.

**C2 supporting -- common-domain finite-resolution consistency.** The
periodic-point Fredholm expansion restricted to those witnesses should agree
within the frozen tolerances with Gauss--Legendre and two independently seeded
Sobol finite-volume operators assembled on the same four-h-set union.

**Anti-claim.** Even a full pass does not provide rigorous root/boundary
interval certification, held-out replication, global catalog completeness
outside the explicit four-h-set survivor, a Markov partition for the full
Hénon nonwandering set, continuous operator convergence, or any Riemann/zeta
correspondence. The exact conjugacy and all-period uniqueness statement is
restricted to the explicitly defined four-h-set survivor and follows from the
R059 contraction theorem.

## 3. Experiment blocks

### B0. Parent integrity and 100-digit orbit refinement -- MUST-RUN

- Bind the R058 protocol, theorem audit, covering result, graph result,
  independent checker, and the merged period-12 catalog by SHA-256.
- Refine all 747 catalog records at 100 decimal digits with at most 30 Newton
  steps.
- Classify every record as `NUMERIC_INSIDE`, `NUMERIC_OUTSIDE`,
  `UNRESOLVED_NEAR_BOUNDARY`, or `ROOT_FAILED`; the last two classes fail G0.
- A coordinate within $10^{-30}$ of an $X$- or $Y$-endpoint is
  `UNRESOLVED_NEAR_BOUNDARY`.
- A failed refinement or ambiguity is retained; no boundary perturbation is
  allowed.

### B1. Primitive symbolic words and catalog witnesses -- MUST-RUN

- Independently enumerate all primitive canonical (A)-words through period
  12.
- Classify phase $i$ as
  $(\operatorname{sign}q_i,\operatorname{sign}q_{i-1})$ only after strict
  membership in $X_s\times Y_t$.
- Compare complete canonical word sets, multiplicities, transition legality,
  and primitive periods.
- Main table: expected words, observed words, missing, extra, ambiguous, and
  minimum boundary margin for every period.

### B2. Restricted cycle algebra -- MUST-RUN

- Use only the predeclared strict h-set-contained witnesses.
- Compute unstable-multiplier Euler determinants for
  $\beta=0,1/2,1$, and periodic-point Fredholm coefficients through degree
  12.
- The $\beta=0$ coefficients must equal
  $\det(I-zA)=1-z-z^3-z^4$
  exactly through the trusted degree.
- The period-12 Fredholm resonance must exist in the unit disk and change by at
  most 0.01 from cutoff 11 before it is used as the operator reference.

### B3. Aligned four-h-set finite-volume operators -- MUST-RUN

- Partition every h-set separately into $m\times m$ cells for
  $m=24,32,48,64,96,128$; all h-set boundaries are exact by construction.
- Run tensor Gauss--Legendre order 8 and randomized-shift Sobol with 64 samples
  per cell at seeds 20260801 and 20260802.
- Preserve both dyadic chains $24\to48\to96$ and
  $32\to64\to128$.
- Persist all 18 sparse matrices, schemas, SHA-256 values, row-sum diagnostics,
  and dominant eigenpair residuals.
- Main figure target: leading modulus versus $m$, with the restricted
  period-12 Fredholm value as a fixed horizontal reference.

### B4. Independent checker and failure audit -- MUST-RUN

- The checker must not import the R059 orbit-classification or operator
  assembly helpers.
- Re-enumerate primitive words independently from binary sign cycles.
- Reclassify the persisted high-precision coordinates and verify all word
  hashes/multiplicities.
- Reload every matrix without pickle, verify SHA/schema/substochasticity, fully
  rebuild small microgrids, and reconstruct frozen source rows on every
  production configuration.
- Negative G4 outcomes remain first-class results.

## 4. Frozen decision gates

1. **G0 integrity:** all parent hashes and 747 numerical refinements pass, with
   zero `UNRESOLVED_NEAR_BOUNDARY` and `ROOT_FAILED` cases.
2. **G1 symbolic bridge:** exact period-by-period canonical word-set equality,
   exact frozen counts, legal transitions, matching primitive periods, and no
   duplicate witnesses.
3. **G2 cycle algebra:** exact beta=0 determinant and a stable-enough
   period-12 Fredholm reference.
4. **G3 operator integrity:** 18 nontrivial substochastic matrices, no sampled
   boundary hits, valid hashes/schemas, and residuals at most $10^{-8}$.
5. **G4 finite-resolution consistency:** finest cross-method and cross-chain
   gaps at most 2%, non-increasing dyadic changes on all six trajectories, and
   finest Fredholm gaps with median at most 5% and maximum at most 10%.

C1 may pass while C2 fails. No aggregate average may hide a failed method,
chain, word, or endpoint case.

## 5. Run order and budget

| Milestone | Goal | Stop/go gate | Expected cost |
|---|---|---|---:|
| M0 | parent/preflight audit | all SHA and exact symbolic controls pass | <1 min |
| M1 | 747 high-precision refinements + word bridge | G0/G1 | 2--15 min |
| M2 | restricted cycle/Fredholm expansion | G2 | <1 min |
| M3 | 18 aligned sparse operators | G3 | 10--60 min |
| M4 | independent checker + analysis | checker integrity | 5--30 min |

The largest operator has (4\times128^2=65{,}536) states. The current
machine is sufficient; expected peak memory is below 10--15 GB even with a
small number of concurrent configurations. No hardware increase is requested.

## 6. Failure interpretation

- Missing symbolic words: the frozen numerical catalog does not yet witness
  the full certified symbolic lower bound at that period; rerunning or changing
  boundaries is forbidden inside R059.
- Extra/multiple witnesses: retain multiplicity and fail the one-to-one
  numerical bridge. This does not alter the separate exact contraction theorem,
  but it requires diagnosing whether the witness is numerical, boundary, or
  catalog contamination.
- Cycle algebra failure: classification or canonicalization is wrong, so the
  operator comparison is not interpretable.
- G4 failure: report a common-domain finite-resolution negative result. The
  exact R059 survivor theorem remains valid, while operator convergence stays
  open.

## 7. Post-freeze production record

The frozen protocol was not changed after production. The exact-theorem audit
and production payloads have the following SHA-256 values:

| Artifact | SHA-256 |
|---|---|
| results/symbolic_contraction_r059.json | bb7eeab3ed27254e3be44b9f8bd9d09b4c80fa01cd72d7e3b2c7d9f6143cee35 |
| results/certified_domain_r059.json | 7d521ed68e843e356ce230bfb0e81b57bf1a67c2f1948e068dd26f20ac20c77b |
| results/certified_domain_r059.csv | 22c37b76f09a45a298c216e827ff2a7d53a77c45afd1d8525460ad87eaa27b84 |
| results/restricted_operator_r059.json | 71c70968ec95e2eb191af12edc266184dda9e82ce6d4b6f07d495bab15439b8e |
| results/restricted_operator_r059.csv | 8b8de60df0dbe9a234ece2bd57527c05fe700a231da68322c0b28bf60c41b5f7 |
| results/restricted_operator_r059_check.json | c26e53e1f6a1d0bf684f6f6408fd01c663e91aab9d8515cfd1f99b7d01769720 |
| results/certified_domain_r059_check.json | 2c850f98f80b3a99993e7aeed2ef64c13e55f60e6d9c98584c0d4d0e069ae40e |

G0--G3 pass; the independent symbolic checker and independent operator checker
both return all_checks_pass=true.
G4 remains false only because the two specified Sobol dyadic trajectories fail
the predeclared monotonic-change condition. This production outcome is retained
as a negative finite-resolution result.
