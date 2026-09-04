# Round-0 freeze report — Route A, P182–P186

**Freeze date:** 2026-09-03 UTC.  **Decision:**
`5/5 ROUND0_FROZEN / PRE-REVIEW INTEGRITY PASS / HOLD_EXTERNAL`.

Exactly five pairwise-separated finite dynamical systems survived the breadth,
transfer, and owner gates.  Every paper has an anonymous theorem manuscript, a
written proof package, a claims-to-evidence ledger, a bounded source audit, a
paper-local exact falsification control, a canonical transcript, a deterministic
PDF build, and an immutable `main_round0_original.pdf` receipt.

## Frozen papers

| paper | literal system | theorem-level progress | author assertions | pages | Round-0 PDF SHA-256 |
|---:|---|---|---:|---:|---|
| P182 | cyclic comparator on triples of subspaces, `(A,B,C) -> (C,A meet B,A+B)` | universal `T^4=T^2`; exact image, recurrence, cycles, depths, every-target fibres, fibre histogram and extremizers | 1,667,850 | 4 | `880abab7db480447c0874e5da6434f7a1d0a8dfbe2ec0b2a23974b573023aa07` |
| P183 | random incoming-star copy on labelled loopless digraphs | conflict deletion; independent-set absorption CDF; first-occurrence endpoint kernel; labelled-action and distinct-source one-step fibres | 47,033 | 4 | `6834170a0ee554a9f4c75040aad762326e24fa5a532e7987c57025be02bd235b` |
| P184 | `x -> x+p^a/gcd(x,p^a) (mod p^a)` | all valuation regimes including zero and the equality layer; complete cycle/tail census; exact empty/double-target atlas | 109,478 | 4 | `991e9eae521268083d5eabb02d5ff536a40eefe000aa970ce23d6c97ea8888ab` |
| P185 | strict-prefix diversity feedback on length-`n` words | all-time delay normal form; image tower; exact clock/depth CDF; target-local inverse product and sharp deepest set | 10,430,175 | 3 | `45a2ce36879d17dafb42fd4a08c2afbc6213c8c140ffdee145f4e27f4c8a9129` |
| P186 | rank subtraction followed by support on subsets | ordered-gap erosion; exact basins/clock; all-time images and coefficient-sum fibres; Fibonacci first image and bounded-gap depth census | 12,104,596 | 3 | `6c85285c7c2f5fb96b9558de3b77e784a079bde08cc9ad23ec3139f17c676431` |
| **total** | **five distinct systems** | **five complete Round-0 theorem packages** | **24,359,132** | **18** | — |

Each author verifier was rerun by the root coordinator and matched its retained
canonical stdout byte for byte.  All five paper manifests pass.  The assertion
count is a bounded regression/falsification disclosure, not proof of a uniform
theorem and not evidence of novelty.

## Pre-freeze correction ledger

Three defects were found before the immutable receipts were created:

1. P182's fibre-histogram exponent contained the TeX typo
   `g_{d-b}^{,2}`; the source was corrected to `g_{d-b}^{2}` and rebuilt.
2. P185 cited Mansour--Vajnovszki as *Information Processing Letters*
   113(16); publisher/DOI metadata give 113(17).  The bibliography and source
   ledger were corrected before the retained Round 0.
3. P186's coefficient-sum upper limit contained a stray comma.  It was removed,
   and the author control and PDF were rerun before the retained Round 0.

No earlier erroneous PDF is presented as a Round-0 receipt.  The hashes in the
table bind the corrected first frozen sources.

## Mechanical gate

- Live PDF and `main_round0_original.pdf` are byte-identical for all five
  papers.
- All 18 pages use A4 media boxes.  The 123 font rows are embedded, subsetted,
  and carry Unicode mappings.
- Title, Author, Creator, and Producer PDF metadata are blank; JavaScript and
  encryption are absent.
- Settled logs contain no actual warning, bad box, unresolved citation, or
  unresolved reference.  The only raw case-insensitive `warning` match is the
  installed package name `infwarerr`, not a diagnostic.
- The five bibliographies contain 15 entries; bibliography and citation-key
  sets agree exactly within every paper.

## Release boundary

Round-0 closure authorizes process-separated hostile review only.  It does not
establish novelty, priority, ownership completeness, freedom to operate, or
external readiness.  Every paper remains `OWNER_AMBER / HOLD_EXTERNAL`.

