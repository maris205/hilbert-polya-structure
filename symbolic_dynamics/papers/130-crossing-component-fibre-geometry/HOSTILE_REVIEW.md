# Consolidated hostile review — P130 round 2

Date: 2026-08-31  
Manuscript: *Crossing-component fibre geometry*  
Internal disposition: **GO_INTERNAL**  
External disposition: **HOLD_EXTERNAL**

This document consolidates two independent nonauthor reviews and records the
author-side closure of their findings.  It does not replace either frozen
review report and does not make a novelty, priority, authorship, submission or
external-release decision.

## Severity ledger

| Stage | CRITICAL | MAJOR | MINOR | Gate at that stage |
|---|---:|---:|---:|---|
| Hostile Review A, round 0 | 0 | 2 | 2 | Repair required |
| Hostile Review B, round 1 | 0 | 0 | 2 | `GO_INTERNAL`, minors to close |
| Round-2 open findings | **0** | **0** | **0** | **GO_INTERNAL** |

External release remains independently blocked: **HOLD_EXTERNAL**.

## Review-A closure

Round one closed all four findings recorded in `HOSTILE_REVIEW_A.md`.

1. The forward localization now proves comparable parents cannot be distinct:
   an inner parent would be a strict intermediate container between the
   selected chord and its alleged immediate outer parent.
2. The converse no longer asserts a false uniform-gap equality.  It separates
   a selected child's exact gap from an unselected child's strict
   gap-subinterval and closes disjointness, coverage and nonmerging by a
   leaf-to-root induction repeated at the virtual root.
3. The owner boundary now zero-credits Igusa's exact parallel-set
   specialization and compatible-merge criterion.
4. The Alman--Lian--Tran all-size sequence ownership is tied to explicit
   theorem locators rather than inferred from a finite coefficient prefix.

The mathematical re-entry was independently reconstructed in Review B; no
enumeration was used as a substitute for the all-size inverse proof.

## Review-B closure

Round two closes both minor findings in `HOSTILE_REVIEW_B.md`.

1. The Igusa statement is now limited to each **nonempty**
   immediate-sibling list, including a nonempty top-level list.  A degree-zero
   list is explicitly the singleton `A_0=1` bookkeeping factor and is not
   identified with an Igusa parallel set.
2. The P110 firewall now describes its literal system as cyclic partition
   shift--join dynamics.  The two-element chord block remains only a narrow
   witness comparison, not a description of P110's update rule.

No new mathematical, ownership, presentation or reproducibility gap was
introduced by these wording repairs.

## Mathematical disposition

The checked claim ceiling is deliberately narrow:

- the fixed-cut component-support map is factored through the consecutive
  section and retracts onto noncrossing matchings;
- the all-size four-stage inverse proves a bijection between each target fibre
  and independent noncrossing sibling partitions with connected decorations;
- consequently, every target has the pointwise product
  `|Phi^{-1}(T)|=product_v a_{d_T(v)}`, including the empty target;
- strict supermultiplicativity, with its explicit missing all-crossing
  witness, makes the consecutive target the unique largest-fibre target;
- the formal noncrossing transform, Catalan image, component counts, A111088,
  generic uncrossing and generic parallel-set structure remain zero-credit
  background.

The fixed cut, virtual root, degree-zero factor and formal-OGF boundary are
explicit.  The paper does not claim an unrooted canonical map, asymptotic
result, general parallel-set theorem, novelty or priority.

## Exact-control disposition

A fresh stable-snapshot run of

```sh
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py > fresh.txt
cmp fresh.txt code/verification_output.txt
```

passed byte for byte.  The verifier performs **735,609 assertions** over all
states and all targets through seven chords: 146,600 states, 626 targets and
146,600 independently reconstructed sources.  It checks the inverse in both
directions and the target-wise fibres, rather than only aggregate counts.

- verifier SHA-256:
  `abd519009e877fa1fa98ece4e6cc290a5fb55bda47f07d4e79b9ccad43568a3d`
- canonical and fresh stdout SHA-256:
  `89b6142c21feac945f9d0dd362b5edf78aed78530596330be0c237e9088d60b4`

This finite computation is falsification evidence; the all-size proof remains
Theorem 2.1.

## Build and artifact disposition

The four-stage `pdflatex`/`bibtex`/`pdflatex`/`pdflatex` sequence passed both
locally and in a fresh isolated directory initialized with only `main.tex`
and `references.bib`.  The isolated and local settled PDFs are byte-identical.

| Artifact | Pages | Bytes | SHA-256 |
|---|---:|---:|---|
| `main_round0_original.pdf` | 4 | 342,739 | `4d914ae6857739b11955dc9ec0db356e8bca5ae5cb67c1fd852ff3d4c2e796c9` |
| `main_round1.pdf` | 4 | 345,749 | `6580b2822113677f5256d0dffcd95b8048e2c0fe6442d434e9fd4b28a1b9a0cb` |
| `main.pdf` = `main_round2.pdf` | 4 | 346,056 | `c5a4fd3976a733c62a7f8f4e90b773cc6300970b9a25ac95b33f68a491f9c3fa` |

All four final pages were rendered and inspected.  There is no clipping,
collision, missing glyph, malformed theorem break or anonymity leak.  All 25
font records are embedded, subsetted and Unicode-mapped.  Title, author,
subject and keyword metadata are blank; there are no embedded files, forms,
JavaScript or encryption.

## Final gate

The two historical reviews remain frozen evidence.  Every internal finding is
closed, the exact control is stable, and the source/PDF/support package is
mechanically consistent.  Final internal verdict: **GO_INTERNAL**.

No external novelty review or release authorization is supplied here.  Final
external verdict: **HOLD_EXTERNAL**.
