# Hostile-review repair resolution ledger

Resolution date: 2026-08-29  
Inputs read in full: `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`  
Artifact role: author-stage repair ledger, not a third hostile review and not
final QA  
External dissemination, novelty, and priority: **HOLD**

## Outcome

Every local mathematical, ownership-wording, endpoint, and presentation
repair requested by Reviews A and B has been implemented. The paper now has
one main theorem only: exact first-gap increment together with its pointwise
and sharp global depth consequences. All other statements are explicitly an
owned input, a zero-credit one-step fact, or a low-credit corollary.

No theorem-level counterexample was reported by either reviewer, and the
repair did not change the mathematical contract or verifier. The unresolved
database-level temporal-owner gate remains open; keeping external status
**HOLD** is the resolution, not a novelty conclusion.

## Review A resolution

| Review A item | Disposition | Implemented repair and evidence |
|---|---|---|
| M-MATH-1: undefined “unique attractor” | **RESOLVED** | `main.tex` now defines a globally absorbing fixed point (synonym: globally attracting in finite time) to mean finite-time capture of every state. The result says `(n)` is globally absorbing and is the unique fixed/periodic point. The undefined phrase was removed from manuscript and support claims. |
| M-OWN-1: missing standard map/first-hook owner | **RESOLVED** | Added Gutschwager, *Annals of Combinatorics* 15 (2011), 81–94, DOI `10.1007/s00026-011-0084-7`. The map object and `hl_1(lambda)=lambda_1+ell(lambda)-1` are itemized as directly owned and zero credit. Global absorption is separated as an elementary low-credit consequence. |
| M-OWN-2: co-equal headline overstatement | **RESOLVED** | Abstract, introduction, theorem environments, README, plan, narrative, and evidence ledger now identify gap increment + sharp depth as the sole main theorem. Absorption, layer transport, conjugation timing, periodic census, and zeta are labelled low-credit corollaries. The note remains compact at four pages. |
| M-OWN-3: bounded search cannot clear novelty | **CONTAINED; RELEASE GATE OPEN** | Removed “the contribution begins” and all inference from negative search. The paper says only that no exact temporal owner was located in the bounded search and explicitly says this is not novelty/priority evidence. A broader database/citation-chain audit remains required before any release; external status stays HOLD. |
| MIN-1: balanced-path last step | **RESOLVED** | For `n>=2`, the sharpness proof now uses `(a,b)->(a+1,b-1)` exactly `b-1` times (zero for `b=1`) and then the separate hook step `(n-1,1)->(n)`, for `b` total steps. It separately treats `(1)` as terminal at `n=1`. All support files use the same wording. |
| MIN-2: fixed-weight zeta ambiguity | **RESOLVED** | Corollary 4.3 fixes `n>=1`, writes `H_n:P(n)->P(n)`, and defines `zeta_{H_n}`. It explicitly excludes a zeta function on the disjoint union of all weights. |
| MIN-3: unsupported use of “classical” | **RESOLVED** | The owner proposition is titled “Previously recorded one-step result; zero credit,” and its proof says Goupil previously recorded the product. Support ledgers use “owned” or “direct owner.” |
| MIN-4: layer “recurrence” overreading | **RESOLVED** | Corollary 4.1 is now a “fibre-weighted layer transport.” It states that the formula is depth-state-weighted over the image and is not a closed scalar recurrence in `A_t(n)` alone. |

## Review B resolution

| Review B item | Disposition | Implemented repair and evidence |
|---|---|---|
| MAJOR(math): undefined/overbroad attractor | **RESOLVED** | Same precise global-absorption definition and theorem wording as the Review A repair; every orbit reaches `(n)` in finite time. |
| MAJOR(owner-scope): residual “contribution” wording | **RESOLVED LOCALLY** | Replaced originality-flavoured transition language by a neutral proof-package description. The bounded search is explicitly nonprobative and external HOLD is repeated. Full temporal-owner clearance remains open. |
| MINOR 1: layer formula is not scalar-closed | **RESOLVED** | Renamed and explicitly qualified as a depth-state-weighted, nonclosed transport identity in manuscript and support files. |
| MINOR 2: terminal padding convention | **RESOLVED** | Immediately before defining `g`, the manuscript says to pad a one-part partition by `lambda_2=0`; this is used for the one-row terminal gap. |
| MINOR 3: verifier-local “boundary shell” | **RESOLVED** | No theorem or claim heading uses that phrase. The manuscript states only the concrete killed rectangular overclaim; the internal verifier witness name remains executable-control terminology. |

## Additional author-stage repairs required by the revision gate

### Itemized zero-credit owners

- **Gutschwager:** principal-hook length partition and first-hook identity.
- **Goupil:** adjacent-gap image and exact product fibre formula.
- **Chern--Yee:** direct diagonal-hook context and an involution preserving
  every diagonal-hook length; this is not inflated into ownership of the
  temporal iteration.
- **Andrews/standard theory:** Ferrers, Durfee, and Frobenius background.

The bibliography now gives the verified DOI metadata for Gutschwager and
Chern--Yee and the arXiv record for Goupil. Every owned item is assigned zero
credit. No exact owner for the iterated temporal claims was located in the
bounded primary-source pass; absence of a hit is not a novelty result.

### Deterministic source controls

`main.tex` now loads T1 encoding and Latin Modern and sets

```tex
\pdfinfoomitdate=1
\pdftrailerid{}
\pdfsuppressptexinfo=15
```

before package loading. Settled `pdfinfo` contains no creation or modification
date.

## Fresh exact-verifier gate

The unchanged verifier was rerun after the repairs:

```bash
python3 -B code/verify.py > "$verify_tmp"
cmp -s "$verify_tmp" code/verification_output.txt
```

Result:

- verifier exit `0`;
- `cmp` exit `0`, byte-for-byte match without a hash;
- 45 stdout lines and 6,053 bytes;
- wall time 11.438 s;
- `PASS: 10,110,035 exact assertions`.

Neither `code/verify.py` nor `code/verification_output.txt` was modified.

## Four-stage build and settled diagnostics

Run from the P113 directory:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All four stages exited `0`. The settled artifact is A4 PDF 1.5, four pages,
325,001 bytes. The settled `main.log`/`main.blg` scan found:

- 0 LaTeX/package/class/font warnings;
- 0 BibTeX `Warning--` lines;
- 0 undefined references or citations;
- 0 multiply defined labels;
- 0 overfull or underfull boxes;
- 0 TeX errors.

`pdffonts` lists 23 fonts: 23/23 embedded, 23/23 subsetted, and 23/23 with
Unicode maps. All four pages were rendered at 140 dpi and inspected. No
clipping, collision, margin escape, missing glyph, broken rule, or unreadable
formula was found.

## Files changed by this repair

- `main.tex`, `references.bib`, `main.pdf`;
- `README.md`, `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`;
- `CLAIMS_EVIDENCE.md`, `CONTROL_RESULTS.md`, `BUILD.md`;
- this new `HOSTILE_REVIEW.md` ledger.

The two input reviews were not edited. No final hash, batch QA, final-QA
artifact, Git operation, or external release clearance was performed.
