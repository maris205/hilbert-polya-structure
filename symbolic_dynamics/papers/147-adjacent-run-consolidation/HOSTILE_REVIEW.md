# Consolidated hostile-review closure — P147

**Status:** **ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL**  
**Scope:** anonymous internal review closure; no external-release authority

## Review ledger

| round | verdict | Critical | Major | Minor |
|---|---|---:|---:|---:|
| Hostile Review A | REVISE | 0 | 1 | 3 |
| Hostile Review B | ACCEPT | 0 | 0 | 0 |

Review A found no counterexample, but required one proof repair and three
interface/source repairs.  Review B was independent of both the authoring pass
and Review A, rederived the repaired theorem, and closed every item.

## Review-A findings and closure

| item | repair | Review-B result |
|---|---|---|
| A1, Major: the doubling-ancestry selector was informal | The proof now defines every orbit state, dispatches depth zero, proves the one-step ancestor claim, recursively selects the produced parts, and obtains `2^t <= n`. | CLOSED |
| A2, Minor: the fibre target was not explicitly typed | The definition and theorem now require `beta in Comp(n)` and positive divisor choices, so source and target remain in the same exact-total layer. | CLOSED |
| A3, Minor: the all-size extremal witness was only described in prose | Both remainder branches now have indexed orbit displays, with explicit `n=1,2,3` bases and the terminal triple in the half-remainder case. | CLOSED |
| A4, Minor: the owner ledger was stale and source-imprecise | The Knopfmacher--Prodinger DOI/host description was corrected; Bevan--Threlfall and Hopkins--Tangboonduangjit were screened and subtracted as different random-growth and static-restriction neighbours. | CLOSED |

## Accepted residual after owner subtraction

No contribution credit is assigned to the literal equal-run rule alone,
Carlitz compositions or their enumeration, static run statistics, ordinary
run-length encoding, random composition evolution, or static adjacent-
restriction families.  The accepted residual is exactly the conjunction of:

1. the simultaneous weight-preserving self-map on `Comp(n)`;
2. the sharp all-size clock `max tau = floor(log2 n)`, with a formal
   doubling-ancestry proof and explicit equality witnesses; and
3. the complete target-resolved, source-length-refined divisor-path fibre
   polynomial.

The source audit is a bounded primary-source non-hit, not a novelty, priority,
authorship, freedom-to-operate, or release certificate.

## Review-B evidence

- Cold replay matched `verification_output.txt` byte for byte and passed
  **2,690,869** deterministic integer assertions over all 262,143 positive
  compositions of totals `1..18` and every target in each exact-total layer.
- An additional independently coded witness replay reached `n=100,000`
  without a clock or weight failure.
- An isolated deterministic
  `pdflatex -> bibtex -> pdflatex -> pdflatex` build reproduced the current
  PDF byte for byte.
- The current `main.pdf`/`main_round1.pdf` is 4 A4 pages, 338,052 bytes, with
  SHA-256
  `1d9c5ceb72891e1c509ebeb8adfdb23d110958f129ea7ae32d3c9d427253ce20`.
- All four current pages were rasterized and inspected.  No clipping,
  collision, blank page, corrupt glyph, unresolved marker, identifying
  metadata, or other visible defect was found.

## Decision and freeze boundary

P147 is internally accepted at Round 2 with **0 surviving Critical, Major, or
Minor findings**.  Root archived `main_round2.pdf` as a read-only,
byte-identical copy of the accepted current PDF and regenerated the final
paper-local manifest.  That historical-copy and manifest step does not reopen
the theorem review.  External status remains **`HOLD_EXTERNAL`**.
