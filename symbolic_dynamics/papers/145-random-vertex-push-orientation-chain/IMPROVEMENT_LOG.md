# P145 improvement log — hostile round 1 remediation

**Date:** 2026-09-01 UTC
**Input review:** `HOSTILE_REVIEW_A.md`
**Disposition:** every required round-1 repair implemented
**Status:** round-2 internally accepted; `HOLD_EXTERNAL`; no paper-local Git
operation

## Outcome first

The theorem survived only after substantial owner subtraction.  The connected
component is now named and cited as the standard folded-hypercube walk, and
its Cayley presentation, spectrum, bipartiteness, and random-walk setting are
all zero-credit inputs.  The residual has been narrowed to the labelled
multi-component weighted-product factorisation and the known-`n`
component-order inverse with a real `(n,Q)` recovery algorithm.

The revised verifier passes byte-for-byte with 155,901 exact assertions.  The
settled paper is 5 pages with six citations and no build warnings.

## Finding-to-fix map

### Review S1 — blocking folded-hypercube ownership omission

Implemented:

- Added the pivot quotient isomorphism
  `theta_*([a])=(a_v+a_*)_(v!=*)` and the exact generator images.
- Identified every nontrivial connected factor with `FQ_(s-1)` and explicitly
  assigned the identification no residual credit.
- Added the degree-weighted disconnected kernel
  `sum_i (s_i/n) P_i + (m_1/n)I`.
- Added direct primary/official sources:
  Xu--Meng (Cayley presentation and spectrum), Xu--Ma (bipartiteness/cycles),
  and Chen--Li--Lin (folded-hypercube random walks).
- Reframed the return formula as a spectral-moment consequence of the owned
  factor spectrum.
- Reduced the contribution language in the abstract, scope, theorem
  narrative, plan, claims ledger, and README.

Files: `main.tex`, `references.bib`, `SOURCE_VERIFICATION.md`,
`NARRATIVE_REPORT.md`, `PAPER_PLAN.md`, `CLAIMS_EVIDENCE.md`, `README.md`.

### Review S2 — inverse verifier used the hidden answer

Implemented:

- Added `recover_component_orders(total, compressed)`.
- Its only mathematical inputs are the known ambient total and `Q_G`.
- It scans candidate sizes from `n` down to 2 and decides solely by exact
  integer-polynomial divisibility; isolates are the residual of the known
  total.
- Across all 28,628 partitions through total 30, the hidden partition is used
  only after recovery as the expected output.
- Frozen coverage now records 624,834 exact candidate division attempts and
  144,024 successful public-input peels.

The root controls were also repaired honestly.  The old “strict order” and
“no-smaller collision” assertions were deleted.  Exact code now claims only
squarefreeness through `s=30`; nearest-root ordering and collision exclusion
remain analytic proof obligations.  During remediation an attempted stronger
pairwise-coprimality control failed because distinct `E_s` can share roots
away from the larger factor's nearest root.  The manuscript now explicitly
states that no pairwise-coprimality claim is made.

Files: `verify_p145.py`, `verification_output.txt`, `main.tex`,
`CONTROL_RESULTS.md`, `CLAIMS_EVIDENCE.md`, `NARRATIVE_REPORT.md`.

### Review S2 — hidden loops, duplicate labels, and product weights

Implemented:

- `s=1`: a labelled isolate push is an identity loop.
- `s=2`: both labelled choices give the same nonzero quotient translation;
  the unnormalised operator doubles it, while the normalised kernel agrees
  with the usual `FQ_1` walk.
- `s>=3`: the coordinate and all-ones generators are distinct.
- Transition-matrix eigenvalues are explicitly distinguished from a
  loop/parallel-edge-suppressed simple adjacency spectrum.
- The verifier checks pivot-generator images for `s=1..12`.

Files: `main.tex`, `verify_p145.py`, `CONTROL_RESULTS.md`,
`SOURCE_VERIFICATION.md`, `PAPER_PLAN.md`.

### Review S3 — tautological `P_4/K_4` witness

Implemented:

- Constructed the actual three-edge path and six-edge complete graph.
- Derived both labelled cut-generator orbits and transition matrices.
- Computed their characteristic polynomials exactly with a
  Faddeev--LeVerrier/Newton recurrence over `Fraction`.
- Both independently give `z^8-z^6`.

Files: `verify_p145.py`, `main.tex`, `CONTROL_RESULTS.md`,
`CLAIMS_EVIDENCE.md`.

### Review S3 — starting-orientation wording and sharp known-`n` boundary

Implemented:

- Recast starting orientation as a category distinction: all affine push
  orbits carry conjugate unmarked translation kernels, so a transition
  spectrum has no marked initial orientation to reconstruct.
- Added the necessity witness for known `n`: all positive-order edgeless
  graphs have the same one-state identity kernel and spectrum `{1}`.
- Constructed edgeless orders 1--6 in the verifier.

Files: `main.tex`, `verify_p145.py`, `NARRATIVE_REPORT.md`,
`CLAIMS_EVIDENCE.md`, `CONTROL_RESULTS.md`, `README.md`.

## Source and owner-search record

`SOURCE_VERIFICATION.md` now contains six verified citations, exact source
roles, inspected pages/abstracts, the owner translation, low-dimensional
conventions, and the exact bounded inverse-search queries.  The inverse-search
non-hit is explicitly not novelty, priority, ownership, or clearance evidence.

## Frozen control delta

| Item | Round 0 | Round 1 |
|---|---:|---:|
| Canonical format | `P145_EXACT_CONTROL_V1` | `P145_EXACT_CONTROL_V2` |
| Assertions | 473,328 | 155,901 |
| Input-only recoveries | 0 | 28,628 |
| Candidate division attempts | not recorded | 624,834 |
| Successful public-input peels | 0 | 144,024 |
| Fake root-order/collision pairs | 812 | removed |
| Constructed `P_4/K_4` kernels | 0 | 2 kernels / 1 witness |
| Low-dimensional quotient sizes | 0 | 12 |
| Unknown-`n` edgeless orders | 0 | 6 |

The lower assertion count is intentional: hundreds of thousands of
tautological known-factor/root-hypothesis assertions were removed rather than
relabelled as evidence.

## Build and preservation

- Four-stage local build: pass.
- Fresh isolated build from only `main.tex` and `references.bib`: pass and
  byte-identical to `main.pdf`.
- Settled warnings: 0.
- PDF: 5 A4 pages, six cited references, all 30 font rows embedded.
- `main_round0_original.pdf` preserved unchanged at SHA-256
  `abf75d832a1bd874ce31155d8c71e55e8cf3bb23f17029b82b6a88e645a49dea`.
- `main.pdf` and `main_round1.pdf` are byte-identical at SHA-256
  `aed3fcd367940666cc2b5489f83ac1d54a72a60e6351ccd4b9d34c73117eeb14`.

No external action or paper-local Git mutation was performed.

## Round 2

An independent hostile reviewer accepted the owner-repaired package with zero
critical, zero major, and one nonblocking bibliographic minor.  The review and
its independent mathematics sub-audit reconstructed the folded-hypercube
quotient, disconnected labelled kernel, nearest-root inverse, genuine shared-
root case, and all three nonidentifiability witnesses; cold replay, isolated
build, and every-page inspection passed.

The minor was closed by preserving the primary journal spelling
`Cheng-Kuan Lin` and linking the journal PDF that visibly fixes pages
1987--1994.  A proof sentence was also clarified so that integral quotient
closure follows from the algorithm's exact `Z[y]` divisibility test and the
literal remaining product, not from the factors' constant terms.  Neither
change alters a theorem, verifier, transcript, or owner boundary.  The rebuilt
artifact is frozen as `main_round2.pdf`; status remains `HOLD_EXTERNAL`.
