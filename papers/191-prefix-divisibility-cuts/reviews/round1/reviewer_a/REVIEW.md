# P191 process-separated Hostile Review A

## Verdict

**PASS — DELTA ACCEPTED.**  The complete mathematical package survives an
independent composition-tuple reconstruction and 2,864,221 exact assertions
with no formal counterexample.  Round-0 Review A found one Minor metadata
error in the companion source ledger.  The requested-only delta now removes
the false 27 August 2026 entry-modification claim and accurately labels
22 July 2026 as the latest official A398023 entry revision.  The manuscript,
theorem, proof, references, and PDF remain byte-identical.

Open counts: `Critical 0 / Major 0 / Minor 0`.  Historical findings:
`1 Minor, accepted`.  Lifecycle: `OWNER_AMBER / HOLD_EXTERNAL`.

## Process separation and pinned input

The reviewer did not author P191 and did not edit its source package.  The
reviewer verifier imports no author or scouting code.  It uses:

- recursively generated positive composition tuples, never cut masks;
- the simultaneous update as a direct merge-and-flush transition on old
  parts;
- global inverse-candidate enumeration by binning every recursive source;
- a memoized backward interval-factor DP; and
- a second brute enumeration of all interval refinements to attack that DP.

The six required inputs are pinned in `PINNED_INPUTS.sha256`; five remain the
immutable Round-0 objects, while the source-ledger row binds the accepted
delta:

| object | SHA-256 |
|---|---|
| `main_round0_original.pdf` | `d8675928ecfe528b950af5402097b5f69657efc9cba7c8eb0bb5c27ec96df78b` |
| `main.tex` | `bdccfa1e266988c1215c7a6735f25f334a39eb99963320b7d8bf43e0d5e6db84` |
| `code/verify.py` | `70efeb7bdb522b501d64775d3ad1c300d70d9ffc83d94d65ff7924e633c59d50` |
| `code/CANONICAL.txt` | `c4643a6639ddf269dee59c97acc53aee504d081a0279d0bbe2898183f674373c` |
| `PROOF_PACKAGE.md` | `f89ab89d2f9fa2f82eb6482129f4803870c3b3240d7a9eb8b31bd8579511d9ef` |
| corrected `SOURCE_VERIFICATION.md` | `26a0e2d9112a938d8dcc388e378f5cf1f89cdea99b4f3941729db094d70373b9` |

A clean execution of the author verifier matched its pinned canonical.  That
is source-package QA only; all findings and theorem pressure below come from
the reviewer implementation and proof reconstruction.

## Finding register and delta disposition

### Critical — 0

No Critical finding.

### Major — 0

No Major finding.

### Minor — 0 open; 1 historical and accepted

#### P191-A-MI-01 — OEIS entry modification date is misreported

Round-0 `SOURCE_VERIFICATION.md` said OEIS A398023 was “submitted 16 July
2026 and modified 27 August 2026.”  The official OEIS entry history instead
has its latest entry revision as #12 on 22 July 2026; the 27 August footer was
database-wide.  The accepted delta changes only that table metadata to
“submitted 16 July 2026; approved/latest entry revision 22 July 2026;
accessed 4 September 2026.”  The old ledger SHA-256 was
`71e6ed195bc75584e071ff5f27975ab756eb66287acd99299fbeea596c9a1c70`;
the accepted ledger SHA-256 is
`26a0e2d9112a938d8dcc388e378f5cf1f89cdea99b4f3941729db094d70373b9`.

The reviewer control asserts that the false phrase occurs zero times, the
correctly labelled history phrase occurs exactly once, and the existing
`OWNER_AMBER / HOLD_EXTERNAL` and bounded-non-hit boundaries remain.  Finding
`P191-A-MI-01` is therefore closed and accepted.

## Hostile theorem matrix

| surface | process-separated attack | outcome |
|---|---|---|
| carrier/totality | Recursive first-part construction of every positive tuple for `N=1..18`; exact `2^(N-1)` census | Pass |
| simultaneous update | Direct block merging uses each old part and old prefix before flushing retained boundaries | Pass |
| coarsening/recurrence | General orbit detection, part-count monotonicity, strict loss when nonfixed, permanent first cut | All periods one |
| fixed recurrence | Statewise fixed predicate versus an independent divisor-step count | Pass |
| `N<=3` | Exact carrier sets, exact fixed sets, exact deepest sets | Every state fixed |
| sharp height | Every source tail for every `N<=18` | `max(0,N-3)` |
| unique extremizer | Exact deepest set plus every time slice through the fixed endpoint | Unique `(1,2,1^(N-3))` for `N>=4` |
| global fibres | Every recursively generated source binned by its direct merge target | Complete target indegrees |
| interval factors | Backward DP versus brute interval refinements in all 342 `(p,q,terminal)` boxes | Pass |
| factorized fibres/image | Factor product versus global indegree for every target through `N=18`, including zero fibres | Pass |
| final endpoint | Correct `K_*` versus deliberately wrong tested-final factor; `(1,N-1)` separates them for every `N>=3` | Untested boundary necessary and correct |
| one-part target | Empty internal-factor product and sole final factor | Pass |
| mass | Sum of factorized counts and global inverse candidates | Both `2^(N-1)` in every box |

The final-endpoint test is not cosmetic.  For example, `(1,N-1)` is fixed
for every `N>=3` even though its final part generally does not divide `N`,
because that endpoint is not a cut.  The reviewer transcript records a
strict positive gap from the deliberately wrong tested-final DP in every such
box.

## Artifact, source, and owner result

- A source-only cold build from only `main.tex` and `references.bib` produced
  a 4-page, 380,787-byte A4 PDF with SHA-256
  `d8675928ecfe528b950af5402097b5f69657efc9cba7c8eb0bb5c27ec96df78b`,
  byte-identical to `main_round0_original.pdf`.
- `main.tex`, `references.bib`, `main_round0_original.pdf`, `main_round1.pdf`,
  and the live `main.pdf` did not change during the source-ledger-only delta;
  both immutable/live Round-1 PDF receipts retain the same PDF hash above.
- The settled log is clean; all 28 font rows are embedded, subsetted, and
  Unicode-mapped; metadata identity fields are blank; no page is clipped,
  corrupt, overlapping, or unintentionally blank.
- The five cite keys match the five bibliography keys.  The manuscript's
  citation to A398023 accurately distinguishes the static `i | s_i` condition
  from P191's dynamic `a_i | s_i` rule.
- Bounded owner pressure found no inspected primary/authoritative record for
  the literal iterative map plus the sharp clock and every-target atlas.
  Coverage is incomplete, so non-hit is not novelty or clearance.

See `PROOF_REDERIVATION.md`, `SOURCE_OWNER_AUDIT.md`, and
`BUILD_PDF_QA.md` for the detailed records.

## Reproduction

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  papers/191-prefix-divisibility-cuts/reviews/round1/reviewer_a/verify_review_a.py
```

Two fresh post-delta processes match `CANONICAL.txt` byte for byte.
`SHA256SUMS` is non-self-referential and binds every other file in this review
directory.  Current verdict: `PASS_DELTA_ACCEPTED`.
