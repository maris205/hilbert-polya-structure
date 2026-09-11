# P192 Review-A delta

**Decision:** `ACCEPTED_REPAIR`  
**Mathematical delta:** no change to the four proved axes.  
**Finding census:** `0 Critical / 1 Major / 3 Minor`, all resolved.  
**Open findings:** `0 Critical / 0 Major / 0 Minor`.  
**Acceptance:** complete after four exact findings were repaired across three
author repair rounds and independently rechecked.

| ID | Severity | Surface | Required and accepted change | State |
|---|---|---|---|---|
| P192-A1 | Major | `main.tex`, `references.bib`, `SOURCE_VERIFICATION.md` | Cited Campion Loth--Rattan, DOI `10.1112/blms.70170`; zero-credited its deterministic conditional Hurwitz/string-reordering algorithm; distinguished its equal-lower-endpoint case, move convention, monotone-factorization order change, and reversible whole-string bijection from P192's least-current-collision terminating map; retained `OWNER_RED_AMBER/HOLD_EXTERNAL`. | ACCEPTED |
| P192-A2 | Minor | `main.tex` | Stated `n>=2`; restricted the displayed witness and sweep proof to `n>=3`; covered `n=2` with the sole fixed factorization, sharp tail zero, and self-fibre `1=n-1`. | ACCEPTED |
| P192-A3 | Minor | `BUILD.md`, `SELF_QA.md`, `README.md`, `CLAIMS_EVIDENCE.md` | Distinguished the immutable three-page Round-0 baseline from the four-page repaired current PDF; synchronized live hashes, source/citation counts, paths, and Review-A provenance without overwriting the baseline. | ACCEPTED |
| P192-A4 | Minor | `FIGURE_PLAN.md`, `PAPER_PLAN.md` | Replaced the two remaining stale three-page/current-Round-0 descriptions with an explicit immutable three-page Round-0 versus current four-page accepted-repair distinction; retained the external gate. | ACCEPTED |

## Accepted hash-level delta

```text
main.tex:
  Round 0  5171a6dcacce38068b04a6c2a3fe8a7332068c5b320dca99ad3607f5a9c1f7c5
  accepted 30cd2c9bc853d9b195f89527db4794681e4d3dcacd8c45f5aea0b49a98ab12f9
references.bib:
  Round 0  e1019cd6e8df5455dc3fe4716af479bc6819fb5223a98f27b600adabf75a7faf
  accepted 70d17104f92450aaca7c1322f96b5343d975fef7f6becef726c514642768cdd5
SOURCE_VERIFICATION.md:
  Round 0  3aaac8e9b55e83e231d2af0cab766a74e7f49e2fa716ff8450bfc05e1e7dec9e
  accepted c8bc72dd399cc57dd8cc6f153975853d2fb53cf0005c25b7dc283a6fe2e05cce
main.pdf:
  accepted e06aac2579f0d90a15c1a7a2c8fa09ce57286f15818a10c2466cd06d210d6b57
main_round0_original.pdf (immutable):
  aa0ade6d64cb2cbd87545bde50ed15ba2b9729e3235aa7395b4be892b1cb76f1
```

Both author controls and the independent Review-A verifier replay bytewise
after repair.  Two fresh source-only builds reproduce the accepted PDF, all
four pages pass visual inspection, and the history-set law remains a
conjecture only.

This acceptance is internal.  It does not authorize external circulation,
novelty or priority language, or owner clearance.  The binding state remains
`OWNER_RED_AMBER / HOLD_EXTERNAL`.
