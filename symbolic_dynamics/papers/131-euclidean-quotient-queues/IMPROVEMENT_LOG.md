# Improvement log — P131

## Hostile-gate repairs implemented in round 0

- replaced the false “all positive rationals” carrier by `Q cap (0,1)`;
- fixed the subtractive-Euclidean stopping and terminal equality convention;
- proved the marker clock, cyclic terminal decoder, and cut position;
- displayed coefficient-level depth formulas and the total-layer identity;
- gave both explicit inverse branches and all `N=2,3` boundaries;
- kept Burnside counts by word length and made no unsupported zeta upgrade;
- added current continued-fraction and cyclic-composition owners as zero
  credit;
- added a proposed subtractive `L/R` path-block derivation and a separate
  rational-pair verifier.

## Hostile Review A — round-one repairs

- defined recurrent states and depth before the terminal-core theorem;
- replaced the ambiguous equality step by its two literal coordinate updates
  and defined the terminal core's surviving marked-gap cut;
- defined a normalized raw-path self-map `Psi`, proved
  `E(Phi(q))=Psi(E(q))` in every size, and proved the clock/core and both
  predecessor alternatives directly on full strings;
- upgraded the verifier from run-length comparison to literal output-string,
  raw-core, and raw-predecessor comparisons, increasing the canonical control
  from 2,097,489 to 6,101,926 assertions;
- named P117, P122, and P126 in the manuscript, admitted the literal
  composition carrier collision, and restricted value to the raw
  Euclidean-path engine and its theorem conjunction;
- added the singleton-target branch `eta(b)=(1,b-1)` and a marked-cut example.

Independent hostile Review B and final QA were subsequently completed; their
final disposition is recorded below.  External release remains on hold.

## Hostile Review B — round-two boundary repair

Review B returned `GO_INTERNAL / HOLD_EXTERNAL` with critical 0, major 0,
and one minor.  It observed that P126 and P131 have isomorphic finite
functional graphs at the exceptional levels `N=2,3`.  Round 2 therefore
replaces the unqualified nonconjugacy sentence by the exact statement:
levelwise nonconjugacy holds for every `N>=4`, hence the graded families are
nonconjugate, while no small-level separation is claimed.  No theorem formula,
code, reference, or verifier output changed.

## Final closure

- consolidated Reviews A and B into `HOSTILE_REVIEW.md`; all Review-A major
  conditions and the sole Review-B minor are closed;
- fresh-ran `code/verify.py`: **6,101,926 assertions**, `STATUS=PASS`, and
  stdout byte-identical to `code/verification_output.txt` with SHA-256
  `caa4df1e70fd2bdb86aa5aeb1308c2baa74b5d5e560d73980f1f6886c91bc8c6`;
- repeated the isolated `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` build
  from only `main.tex` and `references.bib`; the resulting PDF byte-matches
  both `main.pdf` and `main_round2.pdf`;
- finalized the two PDFs at **314,641 bytes**, four A4 pages, SHA-256
  `07c7d40c21e42dde6dd416ca1aa11aef60847d6e2e506df3db4a2e4bbfd7b4af`;
- passed settled-log, four-page visual, font-embedding, anonymity, metadata,
  form/JavaScript/encryption, and text-sentinel checks;
- added `FINAL_QA.md` and `SHA256SUMS` as the closure record.

Final status is `GO_INTERNAL / HOLD_EXTERNAL`.  The bounded owner screen is
not novelty or priority evidence and does not authorize external release.
