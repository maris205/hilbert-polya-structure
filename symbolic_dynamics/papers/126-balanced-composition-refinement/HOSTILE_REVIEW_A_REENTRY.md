# P126 hostile Review A — narrow round-one re-entry

## Decision

**CLOSED / GO_INTERNAL.  External release remains HOLD.**

All two MAJOR and four MINOR findings from `HOSTILE_REVIEW_A.md` are closed
against the same round-zero yardstick.  I found no residual Review-A defect and
no regression in the theorem ceiling, verifier, build, or rendered paper.  This
is a narrow re-entry decision: it clears Review A for the internal track; it is
not a novelty, priority, submission, or external-release clearance, and it does
not replace the still-pending independent Review B.

Residual severity count:

- **CRITICAL: 0**
- **MAJOR: 0**
- **MINOR: 0**

I was the independent nonauthor who wrote the round-zero Review A.  For this
re-entry I independently checked the current manuscript, bibliography, support
documents, verifier and canonical transcript, the three pinned proof-spike
inputs, both frozen PDFs, and every page of the round-one PDF.  I did not modify
the manuscript, bibliography, verifier, canonical output, PDFs, or support
documents.  The only file created in this pass is this report.

## Frozen round-one artifacts

The requested locks match exactly:

- `main.tex`:
  `c93d504af40fbf6e162db4cf3b996457bb7d892ea1ab3e2c8ef89dd7273fd270`;
- `references.bib`:
  `4272430bd26581c7c6aead83f7ae2cacab37f5177d551e293447a0e071105292`;
- `main.pdf` and `main_round1.pdf`:
  `e5d7ab3986a635a490804a8a81d7b3873b5c8403456fccf138af30315751ed3e`.

The live PDF is byte-identical to `main_round1.pdf`.  The immutable round-zero
snapshot remains present at
`d48125fc509fc972b2b705226c33d7915a529523917fd786a5eda2190106ca1e`.
The unchanged paper-local verifier and canonical transcript have SHA-256 values
`5f58da9c3418502d64cd2fc7e3918c9a8bb464c456bc936539bb2afc7ee83ef0`
and
`978191ccbc9a120ca34a298ab79f828175a069b7574388823885fb5712bd2090`,
respectively.

## Finding-by-finding closure

| Round-zero finding | Current evidence | Verdict |
|---|---|---|
| MAJOR A1 — missing external owner/interface subtraction | `main.tex:86--107` now gives category-specific subtraction with all nine bibliography items cited: Lindenmayer--Rozenberg for simultaneous parallel rewriting; Matsoukas for discrete binary fragmentation; Berstel--Perrin, Honkala, and Freydenberger--Reidenbach for codes, ambiguity, and unique decoding; Heubach--Mansour, Malandro, and Banderier--Hitczenko for parts-in-a-set, bounded-part, and restricted-composition enumeration; and Chinn--Heubach for the no-part-2 class.  The text explicitly assigns zero contribution credit to the parallel-morphism/concatenation interface, binary splitting and the divide-and-conquer clock, generic suffix-code principles, prescribed/bounded-part generating functions and Fibonacci counts, and the one-step no-part-2 sequence.  BibTeX resolves and cites 9/9 entries.  `main.tex:103--107` retains bounded-non-hit language rather than a novelty claim. | **CLOSED** |
| MAJOR A2 — missing P094/P108/P113/P115/P122/P123/P125 firewall | `main.tex:109--119` names all seven neighbors and subtracts recognizability, Fibonacci/clock/fibre geometry, integer-sum absorption and product-fibre transport, the all-iterate image/fibre/log-threshold silhouette, target-local fibre DP plus Garden enumeration, generic refinement, and pointwise fibre/image-layer packages.  The residual is restricted to this literal infinite-alphabet balanced morphism's all-iterate canonical kernel, exact one-run fibre product, and temporal image bijection.  The same ceiling is carried consistently in `README.md`, `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`, and `CONTROL_RESULTS.md`. | **CLOSED** |
| MINOR A1 — composition length versus integer weight | The maximum-fibre injection at `main.tex:285--289` now says “restricted compositions of weights” and “total weight.”  The remaining uses of “length” refer legitimately to word length, codeword length, or one-run length. | **CLOSED** |
| MINOR A2 — empty, identity-iterate, and coefficient boundaries | The empty composition is included at `main.tex:71--72`; the decoded empty word is fixed as `s=0,r_0=0` at `main.tex:254--259`; its one-factor fibre is `R_K(0)=1` at `main.tex:261--269`; `R_1(r)=1` for every `r>=0` appears at `main.tex:173--181`; the harmless negative-index convention `I_{j,t}=0` for `j<0` appears at `main.tex:310--315`; and `t=0`, `I_{0,0}=1`, and `I_{n,0}=2^{n-1}` are explicit at `main.tex:329--331`. | **CLOSED** |
| MINOR A3 — compressed terminal-marker induction | `main.tex:138--151` now displays the nested-ceiling transition `last W_{t+1}(m)=last W_t(ceil(m/2))=ceil(ceil(m/2)/2^t)=ceil(m/2^{t+1})`.  It also states that for `m>2^t`, every level `j<t` has smallest descendant at least `floor(m/2^j)>=2`, so no leaf appears early and all `2^t` leaves exist.  This is exactly the missing audit trail. | **CLOSED** |
| MINOR A4 — three pinned hashes and fresh comparison | `CLAIMS_EVIDENCE.md:21--34` and `CONTROL_RESULTS.md:70--80` correctly map the three historical gate inputs to their hashes and distinguish them from current paper artifacts.  Direct hashing and a fresh rerun independently confirm the values and canonical byte comparison below. | **CLOSED** |

The owner repair preserves the round-zero claim ceiling.  In particular, the
paper does not sell the logarithmic clock, generic parallel morphism, generic
binary fragmentation, suffix coding, bounded-part Fibonacci recurrence,
parts-in-a-set OGF, or the no-part-2 sequence as residual value.  Its bounded
owner non-hit is expressly not promoted to novelty or priority.

## Provenance and fresh exact controls

Direct hashing of the three actual phase-one proof-spike files gives:

- `BALANCED_COMPOSITION_REFINEMENT_REPORT.md`:
  `fe4796bb730ac51c40e3ce2dd36f898ef13910da6ece50561b6a13eacc9f32b7`;
- `verify_balanced_composition_refinement.py`:
  `fba237ac83d1a6f470f890824406a52b8a6eaa6189d02dca8f31bcfcd12999a2`;
- `BALANCED_COMPOSITION_REFINEMENT_CANONICAL.txt`:
  `c04de425fd715d549cdd2bfec5a4dc3a7eaf2c49719076059f2e9fc78b15c3f1`.

These exactly match the corrected itemized ledger.  A fresh execution of the
pinned proof-spike verifier made **5,512,265 exact assertions**, exited zero,
and produced stdout byte-identical to its pinned canonical transcript.

I also reran from the paper directory:

```text
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
```

It exited zero with:

```text
balanced composition refinement exact control: PASS
assertions=8756710
```

Fresh stdout has SHA-256
`978191ccbc9a120ca34a298ab79f828175a069b7574388823885fb5712bd2090`
and is byte-for-byte identical to `code/verification_output.txt`.  The current
program still checks the literal clock through weight 18; complete kernel,
decoder, every source/target fibre, maximum, and image through weight 15 for
`0<=t<=5`; codeword sentinels through `m=256,t=8`; and the rational image
recurrence through weight 90 for `t<=8`.  Finite checks remain falsification
evidence, not proof or ownership evidence.

## Isolated build and PDF audit

I copied only `main.tex` and `references.bib` to a fresh temporary directory
and ran `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.  Every stage exited zero.
The settled log has zero errors, LaTeX/package warnings, undefined
citations/references, rerun requests, and overfull/underfull boxes.  BibTeX has
zero warnings and resolves all nine cited entries.

The isolated PDF is byte-identical to both packaged round-one PDFs and has:

- 4 A4 pages;
- 319,631 bytes;
- SHA-256
  `e5d7ab3986a635a490804a8a81d7b3873b5c8403456fccf138af30315751ed3e`.

I rendered and inspected all four pages.  The added owner subtraction and
seven-paper firewall are visible on page 1; the nested-ceiling and no-early-leaf
argument is visible on page 2; all empty/identity/negative-index boundary
statements and corrected weight terminology are visible on pages 2--3; all nine
references are visible and resolved on page 4.  There is no clipping, overlap,
malformed formula, missing glyph, unresolved marker, broken link, or orphaned
heading.

All 24 listed font rows are embedded, subsetted, and Unicode-mapped.  Author,
Title, Subject, and Keywords metadata fields are blank; creation/modification
dates are omitted; there is no metadata stream, form, JavaScript, encryption,
or author leakage.

## Final re-entry disposition

The Review-A acceptance criterion was the exact conjunction

\[
\boxed{\text{all-time canonical kernel}
\; + \; \text{exact one-run fibre product}
\; + \; \text{temporal image bijection}}
\]

after itemized external-owner and internal-corpus subtraction.  Round one now
meets that criterion, and every requested exposition/provenance repair is
mechanically visible and reproducible.

**Review A is CLOSED.  Verdict: GO_INTERNAL, with independent Review B still
pending and external release remaining HOLD.**

The pre-existing support status “Review-A re-entry pending” is a pre-sign-off
state, not a residual defect; the user restricted this pass to creation of this
review report, so no support status was advanced here.
