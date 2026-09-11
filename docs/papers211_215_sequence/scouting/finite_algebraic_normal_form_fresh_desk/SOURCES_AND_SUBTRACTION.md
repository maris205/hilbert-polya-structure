# Sources, old literals and subtraction boundary

## Primary bodies actually read

1. **Heinz Rutishauser, “Solution of Eigenvalue Problems With the
   LR-Transformation.”** Primary historical chapter, printed pp. 47–81.
   [Chapter scan](https://cs.uwaterloo.ca/~y328yu/classics/Rutishauser.pdf).
   The [NIST publication catalogue](https://nvlpubs.nist.gov/nistpubs/Legacy/MP/nbsmiscellaneouspub240.pdf)
   search entry identifies Applied Mathematics Series 49, January 15, 1958.
   That catalogue was not read in full.

   Actual body reading: local PDF pages 1–3, printed pp. 47–49, rendered
   and viewed. They define normalized lower/upper factorization, reverse
   the factors, and state the iteration and similarity identities.
   No later convergence theorem was read or imported. The first page
   mentions an earlier preliminary report: this is not an earliest-priority
   claim.

   Source size is 9,399,955 bytes; SHA-256:
   1ed19def114812c8e6b815b0a44b81016ff3ed2a5aa882cd45ecf3328e7da48a.
   It is a 35-page scan; 2018 PDF metadata describes the scan, not publication.
   Selected-page text extraction returned only page breaks. Earlier web
   screenshots did not deliver inspectable images through the interface;
   subsequent local three-page views are the actual body reading.
   Source/render files remain temporarily at
   /tmp/finite-algebraic-source-RLpHxE/ and are not manuscript artifacts.

2. **Masataka Kanki, Yuki Takahashi and Tetsuji Tokihiro, “Graphs emerging
   from the solutions to the periodic discrete Toda equation over finite
   fields.”** NOLTA, IEICE 7(3), 338–353 (2016).
   [DOI](https://doi.org/10.1587/nolta.7.338);
   [publisher body](https://www.jstage.jst.go.jp/article/nolta/7/3/7_338/_pdf);
   [arXiv record](https://arxiv.org/abs/1511.04509v3).

   Actual extracted-body scope: printed pp. 338–344 and the beginning of
   p. 345, including equations (1)–(2), Definition 1, Proposition 1 and its
   branch-count proof, Examples 1–3, equation (12) and quotient Definitions
   3–4. The article was published July 1, 2016. ArXiv v1 is November 14,
   2015; v3 June 11, 2016. The paper studies possible evolutions as a
   relation, including branching. Our one- and two-site obstruction
   calculations use its literal equations, not numerical searches.

   Nonzero successor counts are source-owned. Later general graph proofs
   were not imported; a correspondence is not silently converted into a
   canonical deterministic update.

3. **Mary Clair Thompson and Tin-Yau Tam, “Rutishauser’s LR algorithm and
   Bruhat iteration.”** Linear and Multilinear Algebra 63(10), 2061–2070
   (2015), [DOI](https://doi.org/10.1080/03081087.2014.940345).
   Only publisher abstract and dates were retrieved. The full article
   and the author thesis were not read as proof sources. Both were
   navigation leads superseded by actual historical-body reading.

Secondary, aggregator and unrelated search returns are preserved only
as raw retrieval provenance; they are not mathematical premises. Missing
an exact finite-field LR hit is not novelty evidence.

## Exact old originals read, not executed

| Original | Scope and literal | Subtraction |
|---|---|---|
| docs/papers172_176_sequence/scouting/fresh_nonlinear_algebra/SCOUT_AND_KILL_LEDGER.md | Full ledger, including M08/CCR and M04/AGD. | Companion retraction already killed; Gram variants excluded. |
| Same directory: verify_scout.py | Actual lines 485–526 include the M08 function at 503–518, row-major update $(0,-\det,1,\operatorname{tr})$, parameters 2, 3, 5. | Exact old literal, no import or replay. The proof here handles all finite fields directly. |
| docs/papers197_201_sequence/scouting/algebra_lane/BREADTH_AND_KILL_LEDGER.md | Full original, including Vieta, conjugation rack, coefficient translation and Boolean symmetric compression. | Prevents old nonlinear/normal-form relabelling; old census not used as proof. |
| docs/papers204_208_sequence/scouting/algebra/SCOUT_REPORT.md | Full original, including transpose commutator, matrix polynomial and commutator/sum register. | Already screened algebra updates excluded. |
| papers/175-diagonal-feedback-commutator/main.tex | Actual lines 1–230 contain update and time/fibre statements. | Occupied feedback lane excluded, not equated to every matrix map. |
| Current scouting/nonlinear_lane/PROOF_AND_SUBTRACTION.md | Full original group/polynomial deductions. | Additional screened formulas, not a new primary-source proof. |

Initially guessed fresh_nonlinear_algebra/pilot.py did not exist. The
failed rg/sed command is preserved. Filename discovery then found
verify_scout.py, and its actual M08 definition was read. Neither old file
was created or modified.

Additional read-only navigation included the nonlinear and
finite-nonlinear-feedback handoffs, the P174 pivoted Möbius manuscript
prefix and an algebra-fourth report. They shaped search but are not
premises of the proofs. This does not reverify every old census or source.

## Selected original pins

| File | SHA-256 |
|---|---|
| Old fresh nonlinear SCOUT_AND_KILL_LEDGER.md | 5ddaf1adead201367f40c5628392b963bdecd0abe0c2a56e0096879afe709805 |
| Old fresh nonlinear verify_scout.py | 8664a7827c790a2c01b091ffd53a482017f9fb262a789ec486d6e96dfb7b84dc |
| P197 algebra BREADTH_AND_KILL_LEDGER.md | 84c6cebf3668a264fd22744c5880502af67999544261d67637a96d3656de939e |
| P204 algebra SCOUT_REPORT.md | 2bf930d9d90004332dea2ac562b3104ad8f2062a67b1df2d2172ac6315b566b3 |
| P175 main.tex | d660c01649ba648ab2cd915ab6bceacfef695789eb7856c1c7823dbce95cceb5 |

## Action and claim limits

No candidate reaches root source/parameter binding; no scientific pilot
was performed. Search/read/hash/source-render operations are documentation
evidence. No external model review occurred and no Zotero/Obsidian library
was available. No absent client was credited with a successful run.
The root's at-most-two, no-children and compact-handoff scope overrides
optional generic workflow expansion.

The first artifact-composition attempt failed JavaScript parsing before
any apply_patch execution because Markdown delimiters conflicted with
template delimiters. No partial file was created by that attempt; the
successful retry removed the conflict. This is an artifact-production
failure, not a mathematical test or evidence gate.

Documentation checks also preserved two failures: jq was unavailable (the
compound read/hash command still ended with status zero, so that status is
not treated as JSON-check success); the first Node fallback had a parsing
typo. The corrected read-only Node check exited zero, parsed all five web
and thirteen local request/return pairs, and resolved the local document
links. These failures and the successful fallback are included in the
local record's document_checks field. They are not scientific runs.
