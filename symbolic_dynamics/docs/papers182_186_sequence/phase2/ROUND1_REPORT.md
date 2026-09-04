# Round-1 report — Route A, P182–P186

**Freeze date:** 2026-09-03 UTC.  **Decision:**
`5/5 REVIEW-A CLOSED / ROUND1_FROZEN / REVIEW-B AUTHORIZED / HOLD_EXTERNAL`.

Five process-separated nonauthor reviews attacked the immutable Round-0
packages with reviewer-owned exact representations.  The reviews made
17,948,001 exact assertions.  They found no formal counterexample and opened
three Minor wording/scope findings in two papers; all three were repaired,
rebuilt, and accepted by the original review process before Round 1 froze.

## Review-A and repair ledger

| paper | reviewer control | assertions | C/M/m at first pass | Round-1 action | final open findings |
|---:|---|---:|---:|---|---:|
| P182 | closure-generated vector-member bitsets, including genuine `GF(4)` | 1,705,929 | 0/0/0 | byte-identical receipt | 0 |
| P183 | unordered-pair four-state tuples plus direct history partitions | 1,509,739 | 0/0/0 | byte-identical receipt | 0 |
| P184 | valuation-stratified modular predecessor equations | 521,367 | 0/0/0 | byte-identical receipt | 0 |
| P185 | weighted equality partitions/RGS classes | 2,104,528 | 0/0/1 | made transient ranges, `t=0`, stabilization, and the empty product explicit | 0 |
| P186 | positive gap compositions plus weak-slot inverse reconstruction | 12,106,438 | 0/0/2 | disambiguated gap survival and restored the `n>=2` extremal scope in the abstract | 0 |
| **total** | **five process-separated controls** | **17,948,001** | **0/0/3** | **all requested repairs accepted** | **0** |

The controls are bounded falsification pressure, not proofs and not
statistically independent error processes.  The all-parameter conclusions
remain supported by the written proofs.

## Immutable Round-1 binding

| paper | `main.tex` SHA-256 | Round-1 PDF SHA-256 | relation to Round 0 |
|---:|---|---|---|
| P182 | `9d496bf69fc3d7426c1f95bb7bacdaf0ea0cd6c7e3b36c5d3c55f64236f088c7` | `880abab7db480447c0874e5da6434f7a1d0a8dfbe2ec0b2a23974b573023aa07` | byte-identical |
| P183 | `9ee13796fc2a69fd9d064c55d0adf1e9fad26d3811e29f767e38d548908e6678` | `6834170a0ee554a9f4c75040aad762326e24fa5a532e7987c57025be02bd235b` | byte-identical |
| P184 | `6f11630dfbb68ff3ac30e652130497b3c473a45869c968fb0679136ba2b8b44a` | `991e9eae521268083d5eabb02d5ff536a40eefe000aa970ce23d6c97ea8888ab` | byte-identical |
| P185 | `e17e073a15d839a3178bc5ed922227bd24cea41d4c6ceff4e6066090651da6f6` | `fcd6257debd3a3e8744571a390296fe02566cc6655957011778400582bea03c3` | revised and rebuilt |
| P186 | `e7f407c5200e2e308885d61bd1328c8e3d20f57e50f219ab5ad104609cee0394` | `449ddc9983cec9618e8a7cead63730d3ed29e1dbb5f36a630948eac3618f2b48` | revised and rebuilt |

The P185/P186 author controls were replayed twice after the source edits and
remained byte-identical to their canonicals.  Their deterministic builds have
no LaTeX/BibTeX warnings or bad boxes, and live PDFs equal the Round-1
receipts.  Review A then rebound its controls to the revised source/PDF hashes
and accepted every delta condition with zero new finding.

## Lifecycle boundary

Round-1 closure authorizes Hostile Review B only.  It is not a novelty,
priority, ownership-completeness, freedom-to-operate, or release decision.
Every paper remains `OWNER_AMBER / HOLD_EXTERNAL`.
