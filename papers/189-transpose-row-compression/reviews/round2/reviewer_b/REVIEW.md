# P189 Hostile Review B - Round 2

## Verdict

`PASS`

| severity | count |
|---|---:|
| Critical | 0 |
| Major | 0 |
| Minor | 0 |

No actionable mathematical, source, citation, control, or rendered-artifact
defect was found in the bound Round-1 manuscript object.  This review is
process-separated from both the author verifier and Review A.  It does not
assert novelty, clearance, or release readiness.  `OWNER_AMBER /
HOLD_EXTERNAL` remains in force.

## Bound material reviewed

```text
main.tex:
c9c4417012fcc9663ac3c3ac3fe9f5113fdf4fe4213846d2a6815b7657724457

main_round1.pdf:
6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81

references.bib:
fbed4d833c2855548bc721b793ad74da2e5fcf994fccbc35e2fdbae74bb1ac4c

author verifier:
b87fde66e16b164544eb6bc0463e4b4d4e82fae8531b43c322cbb96df0db7a5c

author canonical:
9474855682c21a356876b12aef70d8cc12af929bb5846b3c259a4f037048ef25

review A verifier:
4954766bcdf4a56f15544b7157f1be7afa607b5ea6ab58c419cbb87ab06d5b8b

review A canonical:
7fed29f8dd04c2493772596e788a9763222dc5a31d7be70ecdbef28e8d717139
```

The verifier hard-fails if any of those bound artifacts drift.  No author file
was modified during Review B.

## Independent method

Review B uses `Matrix = tuple[column-bit-tuples]`, not the author's packed
integer carrier and not Review A's row-support `frozenset` carrier.
The literal transition is reconstructed from displayed row sums into
initial-segment columns.  Recurrent states and depths are recovered by
memoized orbit repeat detection on the literal successor map, not by indegree
peeling.  Partition conjugation is checked separately by explicit Ferrers cell
reflection, and `W_n` is attacked by both direct partition sums and the
multiset generating function coefficient identity.

Two fresh Python processes reproduced `CANONICAL.txt` byte for byte:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_review_b.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_review_b.py | cmp - CANONICAL.txt
sha256sum -c SHA256SUMS
```

Reviewer-owned verifier and transcript hashes:

```text
verify_review_b.py:
e4738b3d9c7f08c191ec1d1b3554d15078b9efd4b35a992782b65777d42bfeca

CANONICAL.txt:
9b0302b918a3d0e905d50ca4e9780594f68023d39f8f7252d47364c6848cbdf9

canonical lines/bytes:
53 / 2921
```

## Claim Attack Ledger

| target | source location | hostile question | result |
|---|---|---|---|
| Literal definition and carrier | `main.tex:63-97` | Are row labels, transpose direction, and synchronous semantics consistent with `F(A)_{ij} = 1{i <= r_j(A)}`? | PASS.  The column-bit implementation matches the displayed rule exactly on every state in the complete `n=1,2,3,4` carriers. |
| Height calculus and all-time form | `main.tex:104-153` | Can `D` lose labelled information, can `(h^*)^*` fail away from partitions, or can `F^4=F^2` fail? | PASS.  Time-one, time-two, and time-three decoded column heights are exactly `r`, `r^*`, and `r^downarrow`; `F^4=F^2` holds on all 66,066 matrices in the exhaustive boxes. |
| False strengthenings | `main.tex:146-153` | Are the paper's warnings against `F^2=F` and `F^3=F` real? | PASS.  The reviewer witness `00/01` at `n=2` satisfies both `F^2(A) != F(A)` and `F^3(A) != F(A)`. |
| Recurrent states, fixed states, two-cycles | `main.tex:166-208` | Can a non-Ferrers cycle or a period above two survive? | PASS.  Direct orbit decomposition identifies exactly the Ferrers targets as recurrent; every recurrent state is fixed by `F^2`, and every nonfixed recurrent state closes in a strict two-cycle. |
| Depth partition and `W_n` | `main.tex:157-216` | Does labelled row order disappear too early, and does the coefficient identity count depth at most one exactly? | PASS.  Orbit distance equals the stated `L_0/L_1/L_2` predicate on every state, the `n=2` witnesses `A_{1n}` and `A_{21}` give depths one and two, and the direct partition sum agrees with the generating-function coefficient through `n=10` while the transfer recurrence reaches `n=12`. |
| Time-one fibres | `main.tex:225-252` | Are holes, zero/full columns, and every target handled exactly? | PASS.  Every literal indegree in the exhaustive boxes matches the stated product formula; the hole witness `00/01` has zero time-one fibre. |
| Time-two fibres | `main.tex:236-265` | Is the multiplicity taken from `lambda = mu^*`, not from `mu`, and do non-Ferrers targets have zero fibre? | PASS.  The multinomial-by-labelled-rows factor matches every literal two-step indegree; the initial-segment but non-Ferrers witness `01/00` has positive time-one fibre and zero time-two fibre exactly as claimed. |
| Self-conjugate count and fibre mass | `main.tex:202-208,264-265` | Do the `2^n` fixed-state count and both fibre masses survive an independent census? | PASS.  Direct self-conjugate partition counts match `2^n` through `n=10`, and the summed time-two fibre formula gives `2^(n^2)` for every tested `n<=10`. |
| Control lines and declared limits | `main.tex:269-317` | Do the table values, assertion scale, scope fences, and `HOLD_EXTERNAL` declaration match the bound object? | PASS.  The table and boundary numbers agree with the independent exhaustive boxes, the PDF/source explicitly retain square/labelled/synchronous scope, and `OWNER_AMBER / HOLD_EXTERNAL` is present in both source and rendered artifact. |

## Citation and Render Audit

The manuscript cites exactly four bibliography keys, and the `references.bib`
key set matches exactly.  On 2026-09-04, the local bibliographic metadata
matched the corresponding official or primary records:

- Cambridge University Press: <https://www.cambridge.org/core/books/theory-of-partitions/7BC70DD4C1A06AA6179CEDEAD2F0C2DC>
- ScienceDirect: <https://www.sciencedirect.com/science/article/pii/S0012365X12005195>
- ScienceDirect: <https://www.sciencedirect.com/science/article/pii/S0012365X15003647>
- arXiv: <https://arxiv.org/abs/2011.09932>

`pdfinfo`, `pdffonts`, and direct page raster inspection found a four-page A4
PDF with blank metadata fields, no metadata stream, no encryption, forms, or
JavaScript, and 29 embedded/subsetted/Unicode-mapped font rows.  All four
rendered pages were visually intact at 180 dpi.  Page 4 is short but is a
valid references page rather than a truncation defect.

## Findings

### Critical

None.

### Major

None.

### Minor

None.

The `PASS` verdict applies only to the exact bound Round-1 source/PDF and the
claims actually stated there.  It authorizes no manuscript mutation or
external action.
