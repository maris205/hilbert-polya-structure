# Hostile review A — round 1

**Verdict: REVISE.**  I found no counterexample to the endpoint law or the
sharp path-dual minimum.  The mathematical spine survives hostile checking,
but the distributed PDF is stale relative to the corrected source and visibly
contains a corrupted recurrence.  That is release-blocking.  The ownership and
reproducibility record also needs tightening before `HOLD_EXTERNAL` can be
reconsidered.

## Severity-ranked findings

### 1. MAJOR — `main.pdf` is the uncorrected round-0 artifact

The current `main.pdf` and `main_round0_original.pdf` are byte-identical
(SHA-256
`60d29efdca38b64fe8721a0e6d20fe9996b3da24f3d2e397628f64fc702595ca`).
Both predate `main.tex`: the PDFs/log are timestamped 13:58:46, whereas the
source is timestamped 14:00:52.  This is not a harmless metadata discrepancy.
On rendered page 2, equation (6) contains the literal text
`L(D-v)quad(|V(D)|>=2)`, and the induction line displays a comma after
`|Leaf(D)|`.  The present source has the intended `\qquad` and `\,`, and an
isolated settled build from that source renders both expressions correctly and
differs from the checked-in `main.pdf`.

**Required repair.**  Preserve `main_round0_original.pdf` unchanged, rebuild
`main.pdf` from the current source with the documented full LaTeX/BibTeX
sequence, and visually inspect page 2 at equations (6) and the displayed
induction inequality.  Update `BUILD.md` with the post-correction hash, size,
page count, and clean-log status.  Do not certify the artifact until the source
and rendered PDF agree.

### 2. MODERATE — the abstract makes a false universal nonuniformity claim

The abstract says that triangulation endpoints “are not” equiprobable, and
`NARRATIVE_REPORT.md` calls them “highly nonuniform,” without a range
qualification.  The paper's own exact table refutes this for the stated
theorem range: endpoint multiplicities are constant for `n=3,4,5`
(respectively `1`, `2`, and `4`).  Nonuniformity first appears at `n=6`, where
the multiplicities range from `8` to `12`.

**Required repair.**  Replace the abstract sentence by “the triangulation
endpoints need not be equiprobable (nonuniformity first occurs at `n=6`)” and
make the same qualification in `NARRATIVE_REPORT.md`.

### 3. MODERATE — the exact-control claim overstates pressure on `H=L`

The advertised replay is reproducible and matches the frozen transcript:
6,609 assertions over all 68,185 histories through `n=9`.  It genuinely checks
marked final-face counts against the hook quotient and directly checks the
minimum/equality class.  However, `verify_p146.py` never computes `L(D)`, never
runs the leaf-deletion recurrence, and never independently enumerates the
child-before-parent orders.  Thus the `CLAIMS_EVIDENCE.md` entry saying that
`H(T)=L(D_T)` receives exact pressure at every endpoint is inaccurate: the
observed histories do pressure the hook formula, but not the separate
leaf-order interpretation.

As an independent hostile check, I enumerated every labelled tree through
seven vertices (18,249 trees), compared the leaf-deletion recurrence with the
sum of all rooted hook counts, brute-forced child-before-parent extensions
through six vertices, and tested `L(D)>=2^(m-1)` with equality iff the tree is a
path.  All 315,476 exact integer assertions passed.  This supports the theorem,
but it is not part of the paper's reproducible packet.

**Required repair.**  Add an independent memoized leaf-order counter to the
verifier and compare it with both the observed endpoint count and the sum of
rooted hook counts.  For a small bounded range, directly enumerate the rooted
linear extensions as a second implementation.  Also assert weak-dual
connectivity, not only the tree edge count.  Regenerate the frozen transcript
and correct the claims--evidence wording.

### 4. MODERATE — bibliography/source verification is internally inconsistent
and too weak for the closest-owner gate

`SOURCE_VERIFICATION.md` names “T. Eder” and “G. Palfrader”; the publisher DOI
record and the already-correct BibTeX entry give **Günther Eder** and **Peter
Palfrader**.  In addition, the `abbrv` bibliography suppresses every DOI and
the Regev arXiv identifier.  Consequently the recent Stanley DOI correction in
`references.bib` is invisible in the PDF, and the Regev item prints only a
title and year.  Stanley is cited only at book level for the generic tree hook
formula, without a theorem/section locator.  Finally, the owner log records
three search phrases and a non-hit but no auditable candidate/exclusion table
for the closest triangulation-shelling and tree-pruning-history literature.

**Required repair.**  Correct the author initials in `SOURCE_VERIFICATION.md`;
use a bibliography style or explicit `url`/`note` fields that prints the two
DOIs and arXiv:1311.1955; give an exact Stanley locator for the imported hook
formula; and record the closest shelling/stacking-order and leaf-pruning-history
sources with claim-by-claim overlap decisions.  Retain zero credit for ear
clipping, weak duals, and the generic hook formula, and retain
`HOLD_EXTERNAL`; the current non-hit is not an ownership clearance.

### 5. MINOR — three proof invariants should be stated rather than inferred

The proofs are correct, but the central converse is compressed at exactly the
place where a reader will try to break it.

- In the triangulation construction, state the induction invariant: after
  each deletion, the remaining convex polygon plus the already cut-off ear
  triangles triangulates the original polygon.  This makes it explicit that
  the next neighbour chord is new, noncrossing, and that exactly `n-3`
  distinct diagonals are obtained.
- In Lemma 2, state that a child-before-parent prefix removes a descendant-
  closed set, so the remaining faces form the connected ancestor-closed
  subtree containing `r` and triangulate the current convex polygon.  Only
  then does “dual leaf” imply a unique currently deletable ear tip.
- In the `H(T)=L(D_T)` paragraph, partition leaf-deletion orders by their
  **surviving** vertex, not by their “last vertex”: the survivor is not itself
  deleted under the stated definition of `L`.

These are short local repairs, but they close the endpoint-construction,
root-face-bijection, and `H=L` interfaces explicitly.

## Interfaces that survived attempted falsification

- **Equiprobability:** at current size `k`, every current vertex is an ear of a
  convex `k`-gon, so every ordered list of `n-3` distinct labels is legal and
  has probability `1/(n(n-1)...4)=6/n!`.
- **Rooted hook denominator:** with `q=n-3=m-1`, branch interleaving gives
  `q!/prod_{v!=r} s_v^(r)`; the root is correctly excluded and the empty
  product handles `n=3`.
- **Leaf-order identity:** after choosing the unique survivor `r`, a leaf
  deletion sequence is exactly a child-before-parent order in the dual rooted
  at `r`; summing over survivors gives `H(T)=L(D_T)`.
- **Sharp equality:** the recurrence gives
  `L(D)>=|Leaf(D)|2^(m-2)>=2^(m-1)`.  Equality forces exactly two leaves, hence
  a path; a path attains equality recursively.  The cases `m=1,2` are
  consistent.

The existing build log is otherwise clean (three pages, embedded fonts, no bad
boxes or unresolved references).  A separate reproducibility repair is still
needed: two successive clean builds of the corrected source produced different
PDF hashes because creation/modification dates are embedded.  Suppress volatile
PDF metadata (or build under a fixed `SOURCE_DATE_EPOCH`) and require a
two-clean-build byte comparison in `BUILD.md`.
