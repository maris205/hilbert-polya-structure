# Final batch QA — Route A, P182–P186

**Audit close:** 2026-09-04 UTC.  **Decision:**
`PASS_INTERNAL / ROUND2_DUAL_REVIEW_FREEZE / HOLD_EXTERNAL`.

The closed batch contains exactly five anonymous short papers, five
paper-local author controls, ten process-separated hostile-review controls,
three immutable PDF receipts per paper, and two physical source-only cold
builds per paper.  Every all-parameter conclusion rests on a written proof.
The finite programs are bounded falsification and regression controls, not
experiments, proofs, novelty evidence, or statistically independent error
processes.

## Paper-local replay gate

| paper | author control assertions | canonical transcript SHA-256 | terminal result |
|---:|---:|---|---|
| P182 | 1,667,850 | `993df5e5a286ff4ce42d28c36f417a57b1d212ebdcfd7345524a6498a3ace5e0` | byte-identical replay / PASS |
| P183 | 47,033 | `f21652d061f409a0833be4900d6cbafee6a034b3121a03750984073893c2dea1` | byte-identical replay / PASS |
| P184 | 109,478 | `616f48c16bc1d335c658bcfded8b0b004b5dafdec79b77cb17a333ce3067acda` | byte-identical replay / PASS |
| P185 | 10,430,175 | `8caaa2ca1ff4329d0c5b03d84d127c6ef7e060cd6c19a3314a8cd879130975ac` | byte-identical replay / PASS |
| P186 | 12,104,596 | `e73a433e8dae091a04b743ee2b27a039964797d296dd1dc9b8cec2e767ba57dd` | byte-identical replay / PASS |
| **total** | **24,359,132** | — | **5/5 PASS** |

## Ten hostile-review packages

| paper | Review A assertions / disposition | Review B assertions / disposition | final package state |
|---:|---|---|---|
| P182 | 1,705,929 / zero findings | 2,421,778 / zero findings | 2/2 manifests and replays PASS |
| P183 | 1,509,739 / zero findings | 1,274,441 / zero findings | 2/2 manifests and replays PASS |
| P184 | 521,367 / zero findings | 3,987,801 / zero findings | 2/2 manifests and replays PASS |
| P185 | 2,104,528 / one Minor repaired and accepted | 3,677,711 / zero new findings | 2/2 manifests and replays PASS; zero open |
| P186 | 12,106,438 / two Minor repaired and accepted | 16,766,548 / zero new findings | 2/2 manifests and replays PASS; zero open |
| **total** | **17,948,001** | **28,128,279** | **46,076,280 assertions; 10/10 packages; zero open** |

P185's accepted repair made the transient time range and the identity,
empty-product, and stabilized fibre cases explicit.  P186's accepted repairs
made the `g>t` survival condition and the `n>=2` unique-extremal boundary
explicit.  The final author-plus-reviewer assertion total is **70,435,412**.
These counts are distinct from the Stage-1 breadth search and cannot be
interpreted as a number of validated subclasses.

The terminal paper manifests expanded the original 15-row author receipts to
19 rows by adding `IMPROVEMENT_LOG.md`, `FINAL_QA.md`, `main_round1.pdf`, and
`main_round2.pdf`.  Four affected reviewer harnesses were rebound to those
bytes.  The added lifecycle rows remain hard-fail hash checks but are excluded
from the original scientific assertion census, preserving its denominator.
The theorem sources, frozen PDFs, mathematical attacks, transition digests,
and review findings did not change.

## Two source-only builds per paper

Each cold directory was initialized with only the current `main.tex` and
`references.bib`, then built through a settled LaTeX/BibTeX cycle.  Both
physical builds per paper reproduce the live/Round-2 bytes exactly; final logs
contain no warning, bad-box, error, or unresolved citation/reference marker.

| paper | pages | bytes | font rows | final PDF SHA-256 | result |
|---:|---:|---:|---:|---|---|
| P182 | 4 | 329,096 | 25 | `880abab7db480447c0874e5da6434f7a1d0a8dfbe2ec0b2a23974b573023aa07` | 2/2 exact |
| P183 | 4 | 377,864 | 27 | `6834170a0ee554a9f4c75040aad762326e24fa5a532e7987c57025be02bd235b` | 2/2 exact |
| P184 | 4 | 353,576 | 25 | `991e9eae521268083d5eabb02d5ff536a40eefe000aa970ce23d6c97ea8888ab` | 2/2 exact |
| P185 | 3 | 273,283 | 22 | `fcd6257debd3a3e8744571a390296fe02566cc6655957011778400582bea03c3` | 2/2 exact |
| P186 | 3 | 306,590 | 24 | `449ddc9983cec9618e8a7cead63730d3ed29e1dbb5f36a630948eac3618f2b48` | 2/2 exact |
| **total** | **18** | **1,640,409** | **123** | — | **10/10 exact** |

All 123 font rows are embedded, subsetted, and Unicode mapped.  The cold
PDFs have distinct inodes; neither cold build is a symlink or hard link to
the other.

## Immutable PDF receipts

| paper | Round 0 SHA-256 | Round 1 SHA-256 | Round 2/live SHA-256 |
|---:|---|---|---|
| P182 | `880abab7db480447c0874e5da6434f7a1d0a8dfbe2ec0b2a23974b573023aa07` | `880abab7db480447c0874e5da6434f7a1d0a8dfbe2ec0b2a23974b573023aa07` | `880abab7db480447c0874e5da6434f7a1d0a8dfbe2ec0b2a23974b573023aa07` |
| P183 | `6834170a0ee554a9f4c75040aad762326e24fa5a532e7987c57025be02bd235b` | `6834170a0ee554a9f4c75040aad762326e24fa5a532e7987c57025be02bd235b` | `6834170a0ee554a9f4c75040aad762326e24fa5a532e7987c57025be02bd235b` |
| P184 | `991e9eae521268083d5eabb02d5ff536a40eefe000aa970ce23d6c97ea8888ab` | `991e9eae521268083d5eabb02d5ff536a40eefe000aa970ce23d6c97ea8888ab` | `991e9eae521268083d5eabb02d5ff536a40eefe000aa970ce23d6c97ea8888ab` |
| P185 | `45a2ce36879d17dafb42fd4a08c2afbc6213c8c140ffdee145f4e27f4c8a9129` | `fcd6257debd3a3e8744571a390296fe02566cc6655957011778400582bea03c3` | `fcd6257debd3a3e8744571a390296fe02566cc6655957011778400582bea03c3` |
| P186 | `6c85285c7c2f5fb96b9558de3b77e784a079bde08cc9ad23ec3139f17c676431` | `449ddc9983cec9618e8a7cead63730d3ed29e1dbb5f36a630948eac3618f2b48` | `449ddc9983cec9618e8a7cead63730d3ed29e1dbb5f36a630948eac3618f2b48` |

Every live PDF equals its Round-2 receipt.  P182–P184 needed no manuscript
change; P185/P186 preserve the distinct Round-0 bytes and the accepted
Round-1 repairs.

## Source, manifest, mechanical, and visual gate

- The five paper manifests contain 19 non-self entries each and pass
  **95/95**.  The ten reviewer manifests contain four non-self entries each
  and pass **40/40**.
- The bibliography and citation-key sets agree exactly for **15/15** entries.
  All 14 citation commands and 16 key occurrences were inspected in context.
- The registered integrity population closes **47/47** groups with zero open
  issue.  Semantic extraction completeness remains
  `not_machine_detectable`.
- The public-Web originality screen covers 61/116 distinct prose blocks with
  64 queries and no qualifying surfaced match.  It is heuristic only;
  self-plagiarism remains `NOT_CHECKED`.
- All final PDFs are anonymous, A4, unencrypted, and free of identifying
  metadata, JavaScript, forms, unresolved references, and draft markers.
- All 18 final pages were rendered at 220 dpi and inspected.  No clipping,
  overlap, blank/truncated page, missing glyph, malformed mathematics,
  illegible reference, or running-furniture defect was found.

The terminal gate itself performs 2,287 mechanical assertions.  Two fresh
executions produced stdout byte-identical to `qa/CANONICAL.txt`, whose
SHA-256 is
`27f92e7c20e8385f481b4c4611984830491511e063b41beb555115e2f0316823`.
The gate caught and closed two provenance-format issues before passing: stale
15-row bindings in four reviewer harnesses and non-standalone acceptance
tokens in two Review-A delta records.

## Release boundary

This gate establishes internal theorem-package and artifact consistency only.
It does not establish novelty, priority, ownership completeness, freedom to
operate, bibliographic exhaustiveness, or external readiness.  No posting,
circulation, contact, or submission is authorized.  All five papers remain
`OWNER_AMBER / HOLD_EXTERNAL`.
