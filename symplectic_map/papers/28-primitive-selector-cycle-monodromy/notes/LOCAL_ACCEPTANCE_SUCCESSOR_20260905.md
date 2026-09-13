# Paper28 local acceptance — reviewed manuscript successor

Date: 2026-09-05.
Decision: LOCAL_ACCEPTANCE_GRANTED.
Scope: the exact anonymous local PDF and source version below.
No external submission, upload, hosting or release is authorized or performed.

## Accepted deliverable

[Accepted PDF](../build-capsule-successor-20260905/r0/work/main.pdf):
836,405 bytes, SHA-256
ebbd943cba592de21658248779ea3fb4da2cbcbf9a297131df5a358e731b38ca.
The independently built r1 PDF is byte-identical.
The paper has 23 physical content pages plus two reference pages, 25 total.
References begins on fresh page24 after the exact final scientific sentence
on page23. This satisfies the locked 22–30 content-page requirement.

The accepted source is the three-file paper-successor-20260905 version:

| File | Bytes | LF | SHA-256 |
| --- | ---: | ---: | --- |
| main.tex | 84,983 | 1,855 | 7beb4f783cd370dc4b0d9d1e9178e3e48ce1ef9ed1497e0e9883b10739d4a1f9 |
| math_commands.tex | 444 | 14 | 16b1e55f52f21b63811a0d34eb64eba955533334f8e5f58005841d6da0a85ce5 |
| references.bib | 6,104 | 204 | e6a6bdb24a7db3a75b481c8363aa7733cb3dd4c1e8a121d9d9526eb83228882e |

The original paper/ trio remains frozen and unchanged. The successor adds
substantive proof detail and worked decoding within three existing subsections;
the main theorem, all original text, architecture, typography, macro file and
bibliography are unchanged. Historical exact page-allocation predictions are
not substituted for this measured content-page result.

## Evidence supporting acceptance

1. Original scientific/source review remains applicable to the preserved
   baseline. The entire mathematical insertion delta separately passed
   [SOURCE_SUCCESSOR_REVIEW_20260905.md](SOURCE_SUCCESSOR_REVIEW_20260905.md),
   SHA-256 a6c4c4de718dfab8afba7c19026678eb0a4241878e969c403606b722de04b76d.
   Its only counting-language ambiguity was corrected and rechecked.
2. The new executable profile and three targeted validator corrections
   independently passed
   [HERMETIC_BUILD_SUCCESSOR_REVIEW_20260905.json](HERMETIC_BUILD_SUCCESSOR_REVIEW_20260905.json),
   SHA-256 b31e863e82ae31265ad1e9ae295c659aff8765623004fcb4e9834f30d5dd5ee2.
   The 103-case author regressions and independent memory checks are recorded
   there with their distinct scopes; no page/safety threshold was lowered.
3. Actual execution completed exit0 in two fresh isolated roots. All18
   children exited0 and were reaped. Both automated PDF reports passed with
   zero findings. The controller checked convergence, final logs, readonly
   inputs, exact cross-root work equality and final bindings.
   [Actual result](HERMETIC_BUILD_SUCCESSOR_RESULT_20260905.md) identifies the
   commands, outcome and output records.
4. The independent final review actually displayed all25 recorded page
   images and checked the final delivery evidence:
   [FINAL_PDF_SUCCESSOR_REVIEW_20260905.md](FINAL_PDF_SUCCESSOR_REVIEW_20260905.md),
   SHA-256 8a27036539f0a967430eb01438c12b216d005829bff4a0899a8cf7220419f748.
   It reports FINAL_PDF_SUCCESSOR_REVIEW_PASS and
   INDEPENDENT_LOCAL_ACCEPTANCE_READY. It checked all250 evidence-seal rows,
   both49-row final work seals, both actual PDF bytes, all18 status records,
   current source/control identities, and stored readonly before/after maps.
   It did not falsely claim to rerun the parser or rescan the resource tree.

The accepted output has anonymous metadata, embedded fonts, the full proof
in the main text, complete references, valid bookmark/link destinations and no
observed clipping, overlap or missing glyphs. No final overfull box or
undefined-reference/citation defect remains. Seven inherited underfull
table-spacing warnings are retained and individually disposed as
ACCEPTED_COSMETIC_NO_SOURCE_CHANGE: loose spacing but readable, not a waiver
of unknown warnings.

## Preservation and batch disposition

The sealed controller outcome and validator reports keep their original
prospective VISUAL_REVIEW_PENDING values. This later acceptance record and
independent review supply the final disposition; those sealed records are
not rewritten to pretend they performed a visual review.

All earlier failures, dependency recordings, original controllers/validator
and locks remain unchanged. No old failed root was retried or repaired.
Paper27 remains accepted and untouched. Paper28 now counts as the second
accepted local paper of Batch07: 2/5. Papers29–31 and the final cross-paper
audit remain required; this acceptance does not mark the whole batch complete.
