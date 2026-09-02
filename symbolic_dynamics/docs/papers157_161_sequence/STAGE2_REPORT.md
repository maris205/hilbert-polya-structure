# Stage 2 report — P157–P161

**Date:** 2026-09-02 UTC.  **Route:** A.  **Batch status:** five of five live
anonymous short papers are `ROUND-2 INTERNAL ACCEPT`; external state remains
`HOLD_EXTERNAL`.

## Outcome and breadth

This round screened/tested **145 genuinely distinct literal dynamical
systems** across arithmetic, stochastic graph, algebraic, combinatorial,
geometric, word/automaton, poset, tiling, and topology lanes.  This is a
breadth count of literal systems subjected to exploratory or exact probes;
it is **not** a claim that 145 dynamical subclasses were proved or validated.
Parameter choices, stronger reruns, repair variants, and repeated owner
queries were not counted as new systems.

Correct but owner-covered or proof-engine-colliding candidates were killed
rather than promoted to fill the five-paper quota.  The most consequential
case was the initially selected BST P160: its mathematics passed, but a direct
owner found in Hostile Review A forced retirement and a genuinely new
replacement search.  RCS survived the replacement and independent alternate
lanes.

## Five live theorem packages

| paper | literal dynamical system | explicit theorem-level progress | author assertions | final artifact |
|---:|---|---|---:|---|
| P157 / NHI | iterate `F(x)=3x^2-2x^3` on every residue of `Z/2^n Z` | exact parity-selected valuation law `v_2(e(F^t(x)))=min(n,2^t v_2(e(x)))`; all clock shells and sharp height `ceil(log_2 n)`; complete normalized-unit one-step image criterion and every-target fibres, including endpoint and small-quotient boundaries | 2,563,880 | 4 pages, 349,380 bytes, SHA-256 `6b0c1fb81c065a9213df4cb4af7b731e25e02e3306e6220a154899166e9129dd` |
| P158 / CIC | start from `K_n` and intersect at every epoch with the complete bipartite graph of a fresh fair vertex cut | exact absorption CDF `A_R(n)/2^(tn)` and first-hit/tail consequences; exact complementary-history characterization; every labelled target fibre `(R)_r 2^r A_(R-r)(z)` with the `r=R,z>0` obstruction; complete labelled image EGF | 77,530 | 4 pages, 371,703 bytes, SHA-256 `2ec5779cb4b1c2f8515104c6114431df89155e8e3dfde7749a48ab113b9bb0d5` |
| P159 / OVP | on graphs carried by all vertex subsets of `[n]`, delete every current odd-degree vertex simultaneously | sharp clock `floor(n/2)` and complete even-graph fixed locus; strict target-uniform inverse rank `B_n(s,m)`; all-time target fibres through powers of `B_n`, with the distinct even-target sum; exact time-image, phase, fixed, and depth censuses | 3,167,525 | 5 pages, 363,444 bytes, SHA-256 `72c0ca96d3afde550b05677e61454ba5c9fcdb819c6332c92baaa0045fe4b05d` |
| P160 / RCS | for fixed positive `(a,b)`, delete the first `a` Ferrers rows and first `b` columns of an integer partition, translate the southeast remainder, and repeat | closed iterate `T^t(lambda)=(lambda_(at+1)-bt,...)_+`; point clock and sharp capped height `min{t:(at+1)(bt+1)>N}`; separate exact empty fibre and every-time/every-nonempty-target fibre GF; every-weight cap threshold; conjugation and ordered `(a,b)` recovery from three target probes | 3,462,895 | 4 pages, 316,629 bytes, SHA-256 `ce59fbfca3f50ee917089175817885fc5630b807483b7a16a5d291c69292e352` |
| P161 / ORT | over `F_p`, `p=3 mod 4`, slide an ordered noncollinear triangle window by `(A,B,C) -> (B,C,H(A,B,C))`, sending degeneracy to a fixed sink | oriented right-angle depth split; exact four-cycle census on nonright triangles; sharp stable image; complete sink and triangle fibres; image size, depth CDF, zeta function, and the `p=3` empty periodic-triangle boundary | 1,317,843 | 4 pages, 304,462 bytes, SHA-256 `1fcf260e266257c04d0f47aa90a6d47821eefa22834bd32d60fc4a1451d7f214` |

The five live PDFs contain **21 pages** and **1,705,618 bytes**.  Their
paper-local author verifiers execute **10,589,673** deterministic exact
assertions.  These exact runs are bounded falsification and regression
evidence; the all-parameter results are supported by written proofs.

## Historical retired P160 candidate — excluded from live totals

The initial P160 candidate, **BST** (binary-projective Steiner triangle
collapse), remains preserved only as historical negative evidence under
`papers/retired/160-binary-projective-steiner-triangle-collapse/`.

- Its formulas passed **4,836,144** author assertions.
- Its frozen manuscript is **4 pages**, 355,500 bytes, SHA-256
  `a988139ec5b9cd600ced9f7eeffdeb42e5b8f8268c1161670661cdc3d0cc84b5`.
- Hostile Review A found a **1 Critical direct-owner collision**: Aryapoor
  (2013) covers the unordered distinct-triple map, the projective equality
  case, and the exact inverse family.
- Decision: `KILL_STANDALONE_PAPER / REOPEN_P160_SLOT / HOLD_EXTERNAL`.

The BST assertions, four pages, bytes, PDF, and review severities are not
included in the live five-paper assertion total, page/byte total, review
aggregates, or canonical PDF manifest.  The kill concerns ownership and paper
value, not a mathematical counterexample.

## Owner subtraction and retained residuals

- **P157:** the standard idempotent-lifting cubic and generic quadratic
  improvement are zero credit; Burban--Drozd is treated as a direct prior
  record, not an origination attribution.  The residual is the complete
  parity-resolved temporal and normalized-unit inverse atlas over `2^n`.
- **P158:** cuts, biclique/bicluster language, inclusion--exclusion, and
  generic random-intersection framing are background.  The residual is the
  exact repeated-cut absorption plus complete corrected labelled history
  fibres and image EGF.
- **P159:** handshaking, incidence rank, even-graph counts, and existing
  sequential parity deletion are subtracted.  The residual is the strict
  parallel inverse rank and its target-resolved all-time transfer/depth atlas.
- **P160:** Barnes--Savage's local row/column deletion, generalized and
  rational-slope Durfee rectangles, Chen--Ji--Zang's static two-boundary
  symbol/decomposition, and the two-Pochhammer factorization are zero credit.
  The residual starts at fixed-crop all-time dynamics, arbitrary prescribed
  targets, a separate empty branch, exact cap support, and ordered recovery.
- **P161:** the orthocentric quartet and finite-field metric geometry are
  background.  Only the anisotropic singular boundary, oriented layers,
  stable image, and complete fibre conjunction are retained.

All owner searches are bounded and terminology-dependent.  A non-hit is not
evidence of novelty, priority, owner absence, freedom to operate, or release
readiness.

## Hostile-review closure

The following aggregates include only the five live papers.

| review | Critical | Major | Minor | final state |
|---|---:|---:|---:|---|
| A, aggregate | 0 | 2 | 5 | all closed in Round 1 |
| B, aggregate | 0 | 0 | 2 | all closed in Round 2 |

P160 Review A's two Major findings were closed by replacing the invalid
`gamma=(1^d)` support witness with `gamma=(d)` and by subtracting the full
Gordon--Houten/Andrews/Chen--Ji--Zang static rectangle chain.  Independent
P160 Review B then returned **0 Critical / 0 Major / 0 Minor**.  The only
P160 Round-2 source addition was the visible sentence
`This artifact remains HOLD_EXTERNAL`, made for lifecycle consistency during
final QA.  It is not a Review-B finding and changes no mathematics, source
subtraction, reference, verifier, or transcript.

The two live Review-B Minors were P157's reproducible microtype warning and
P159's stale lifecycle sentence; both were closed.  No live review item
remains unresolved.

## Reproduction and integrity

Every live author verifier was replayed from the final tree and reproduced
its transcript byte for byte.  Two fresh source-only directories per paper
reproduced each canonical PDF byte for byte: **10/10** builds pass.  All **21**
pages are A4 and passed paper-local 144-dpi visual review; all **125** font
rows are embedded, subsetted, and Unicode mapped; identifying PDF metadata is
blank; every paper visibly carries `HOLD_EXTERNAL`.

The final paper-local manifests contain **37, 30, 33, 42, and 33** entries,
respectively, and pass **175/175**.  The batch canonical PDF manifest contains
exactly the five live PDFs and passes **5/5**.  Round-0, Round-1, and Round-2
PDF hashes are recorded in `FINAL_QA_REPORT.md`.

## Terminal decision

P157–P161 are complete as five distinct, owner-subtracted, anonymous internal
theorem packages under their narrowed claim ceilings.  They remain in the
Route-A internal portfolio.  Nothing in discovery, proofs, owner search,
reviews, verification, cold builds, PDFs, or manifests authorizes external
posting, circulation, contact, or submission.  Status remains
`HOLD_EXTERNAL`.
