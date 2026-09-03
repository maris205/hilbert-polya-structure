# P169 — Successor Transfer on Canonically Ordered Set Partitions

**Status:** `ROUND2 DUAL-REVIEW FREEZE / GREEN_OWNER_THIN / HOLD_EXTERNAL`  
**Format:** anonymous `amsart` 10pt short theory note  
**Final repaired PDF:** 5 A4 pages, 392,380 bytes

## Result

On a canonically ordered set partition, every nonsingleton block
simultaneously sends its maximum to the cyclic successor block.  The frozen
theorem package gives:

- the exact restricted-growth update: increment the final occurrence of each
  repeated letter modulo the block count;
- sharp stratum clock `min(n-2,2k-2)` for `1<k<n`, and global clock `n-2`;
- complete dense/sparse recurrent forms, counts, and exact nontrivial period
  `k`;
- an explicit five-state matrix product for the fibre of every target and an
  exact image test;
- the interlacing witness `025|134` versus `035|124`, with equal ordered
  size/minimum/maximum data but fibres two and one;
- explicit handling of `n=1`, `k=1`, `k=n`, `n=2k`, singleton blocks, and the
  cyclic wrap.

The theorem is deliberately owner-thin.  Restricted-growth encodings and
whirling, directed-cycle chip firing, Bulgarian solitaire, promotion/jeu de
taquin/rowmotion, box-ball systems, set-partition stack sorting, Stirling
counts, and generic transfer matrices are background.  The bounded source
search grants no external lifecycle permission.

## Core artifacts

- `main.tex` — complete anonymous manuscript with explicit matrix entries.
- `main.pdf` — settled canonical Round-2 PDF after both hostile reviews.
- `main_round0_original.pdf` — immutable author Round-0 freeze.
- `main_round1.pdf` — immutable post-Review-A source-repair freeze.
- `main_round2.pdf` — byte-identical final dual-review freeze.
- `references.bib` — exactly eight cited, primary-source-verified records.
- `verify_p169.py` — standalone standard-library verifier.
- `verification_output.txt` — frozen verifier stdout.
- `PAPER_PLAN.md` — claim-aligned short-note plan.
- `NARRATIVE_REPORT.md` — temporal/inverse narrative and owner boundary.
- `CLAIMS_EVIDENCE.md` — frozen claim/evidence and edge-case ledger.
- `SOURCE_VERIFICATION.md` — primary-source metadata and subtraction record.
- `BUILD.md` — replay, build, cold-build, PDF, and hash ledger.
- `SELF_QA.md` — author-side mathematical, source, anonymity, and visual QA.
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md` — two independent hostile
  review records.
- `IMPROVEMENT_LOG.md` — exact source and packaging repair record.
- `SHA256SUMS` — paper-local integrity manifest.

The independent pre-paper gate froze the contract before drafting and is not
relabelled as either manuscript review.  Review A found one formal-source
currency repair; Review B accepted every theorem and found one packaging
inconsistency, now closed.  Neither review changed a theorem, formula, proof,
example, verifier, claim ceiling, or lifecycle decision.

## Reproduce the verifier

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p169.py > replay.txt
cmp replay.txt verification_output.txt
sha256sum verify_p169.py verification_output.txt
```

Expected result:

```text
decision: AUTHOR_ROUND0_PASS
assertions: 1,217,025
verifier SHA-256: e4566e997ec656f3eaa41fa4f23953773222293cf23189ebd6c7d9a64aab950b
transcript SHA-256: e59891873e682c0a271a28197e681f6ba813f394f4104140b02d5eb4e5ce258f
```

## Rebuild the PDF

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The final settled PDF SHA-256 is
`419e91685b4a663fb8ab711abca28517436a2477a92184add424575d8bac77d3`.
Two Review-B source-only directories reproduced this artifact byte for byte.
The immutable Round-0 PDF retains SHA-256
`df03b864b47ae963c467831ba7f5b47231663f1e369facf21eee1d468b17c9c2`.
