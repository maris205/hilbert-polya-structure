# Paper 28 proof-only validation tracker

Controlling candidate: V4  
Execution state: `ZERO_SCIENTIFIC_EXECUTION`  
External effect: none  
Source-design review: pending

## Activity ledger

| Check | Method | State | Evidence location | Runtime/data |
|---|---|---|---|---|
| P28-X01 symplectic blocks | manual Jacobian identity | `MANUAL_DERIVATION_COMPLETE` | `notes/PROOF_PACKAGE.md`, Lemma P1 | none |
| P28-X02 selected matrices | manual differentiation and multiplication | `MANUAL_DERIVATION_COMPLETE` | Lemmas P2--P3 | none |
| P28-X03 incidence scores | manual dot products | `MANUAL_DERIVATION_COMPLETE` | Lemma P5 | none |
| P28-X04 singleton side | empty-intersection logic | `MANUAL_DERIVATION_COMPLETE` | Lemmas P4--P5 | none |
| P28-X05 momentum chamber | coordinatewise inequalities | `MANUAL_DERIVATION_COMPLETE` | Lemma P6 | none |
| P28-X06 carry induction | manual induction | `MANUAL_DERIVATION_COMPLETE` | Lemmas P6--P7 | none |
| P28-X07 prefix cocycle | manual rank-one multiplication | `MANUAL_DERIVATION_COMPLETE` | Lemma P9 | none |
| P28-X08 digit decoder | integer bounds and injectivity | `MANUAL_DERIVATION_COMPLETE` | Lemma P10 | none |
| P28-X09 side information | information-boundary audit | `MANUAL_DERIVATION_COMPLETE` | Theorem clause T6 | none |
| P28-X10 least period | quotient argument | `MANUAL_DERIVATION_COMPLETE` | Lemma P11 | none |
| P28-X11 scalar indices | closed-form substitution | `MANUAL_DERIVATION_COMPLETE` | Lemma P12 | none |
| P28-X12 failure boundaries | exact counterexamples | `MANUAL_DERIVATION_COMPLETE` | Boundary register | none |

“Complete” here means that the source-design author supplied a written manual
derivation.  It is not an independent PASS.  Every row remains subject to the
fresh source-design reviewer.

## Registered fixture values

| Quantity | Frozen value |
|---|---|
| word | \(((A,X),(B,X),(A,Y))\) |
| \((\ell,r,\rho,K,H)\) | \((3,4,2,1,2)\) |
| \(D,\lambda,C_0,g,\mu\) | \((11,100,13,1,127)\) |
| \(u_0\) | \((2,1,1,1)\) |
| canonical \(m_0\) | \((1,1,1,1)\) |
| boundary \(m_0\) | \((10,10,10,10)\) |
| boundary residual | \(800\) at the removed complete-state \(n=0\) recurrence |

## Prohibited evidence states

No row may be changed to `EMPIRICALLY_CONFIRMED`, `CAS_VERIFIED`,
`SEARCH_EXHAUSTED`, `GPU_COMPLETE`, or an equivalent label.  No executable,
cache, generated data, plot, table of sampled outcomes, or machine
certificate belongs to this project gate.  A finite check may reveal an
error, but it cannot raise proof confidence by itself.

## Resource accounting

- CPU/GPU scientific jobs: 0
- CAS sessions: 0
- scripts or notebooks: 0
- datasets: 0
- random seeds: 0
- generated figures: 0
- external messages/uploads: 0
- theorem claims depending on computation: 0

## Next admissible transition

A fresh reviewer must read the complete ten-file source-design package,
rederive every theorem-critical step, and return either an all-zero
`SOURCE_DESIGN_PASS` artifact or `FAIL_WRITE_NOTHING`.  This tracker cannot
grant source lock, paper-plan, manuscript, build, or release authority.

BATCH07_PAPER28_EXPERIMENT_TRACKER_FROZEN

## Controlling append-only evidence-location correction

Authority: `B07-E0174-P28-SOURCE-DESIGN-REVIEW-FAIL-CORRECTION-AUTHORIZATION`.
The original activity rows and zero-resource census remain unchanged.  Their
evidence-location cells are superseded by the following exact map:

| Check | Canonical evidence location |
|---|---|
| P28-X01 symplectic blocks | Proof P1 |
| P28-X02 selected matrices | Proof P2 |
| P28-X03 incidence scores | Proof P7 |
| P28-X04 singleton side | Proofs P6--P7 |
| P28-X05 momentum chamber | Proofs P3--P4 |
| P28-X06 carry induction | Proofs P3--P5 |
| P28-X07 prefix cocycle | Proof P9 |
| P28-X08 digit decoder | Proof P10 |
| P28-X09 side information | Proof P11 |
| P28-X10 least period | Proof P12 |
| P28-X11 scalar indices | Proof P13 |
| P28-X12 failure boundaries | Exact failure fixtures following P13 |

The state `MANUAL_DERIVATION_COMPLETE` is the controlling permitted state for
all completed author derivations.  It is not an independent PASS and does not
report a scientific run.

BATCH07_PAPER28_EXPERIMENT_TRACKER_CORRECTION_FROZEN
