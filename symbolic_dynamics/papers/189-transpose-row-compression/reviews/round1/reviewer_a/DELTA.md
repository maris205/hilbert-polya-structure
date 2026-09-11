# P189 Review-A delta and acceptance template

**Review verdict:** `PASS`  
**Required manuscript delta:** none  
**Lifecycle after review:** `OWNER_AMBER / HOLD_EXTERNAL`

## Frozen bindings

```text
main.tex:
c9c4417012fcc9663ac3c3ac3fe9f5113fdf4fe4213846d2a6815b7657724457
main_round0_original.pdf:
6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81
```

These are the only theorem source and rendered artifact assessed.  The review
made no edit to either one.

## Actionable findings

| ID | severity | location | required action | acceptance evidence |
|---|---|---|---|---|
| — | Critical | — | none | count `0` |
| — | Major | — | none | count `0` |
| — | Minor | — | none | count `0` |

## Acceptance gates

- [x] Literal map and label/transposition conventions agree at
  `main.tex:63–77`.
- [x] Height calculus and every `n>=1`, `A`, `q>=1` all-time quantifier agree
  at `main.tex:90–143`.
- [x] `F^4=F^2`, recurrent/Fix/two-cycle claims, and all three depth sets and
  populations agree at `main.tex:122–216`.
- [x] Both every-target fibre formulas, zero-fibre criteria, images, and masses
  agree at `main.tex:225–265`.
- [x] The `n=1` boundary and `n>=2` sharp-height boundary are explicit and
  correct.
- [x] Exact table/control claims agree at `main.tex:269–292`.
- [x] Four bibliography records and their citation scopes are verified; owner
  non-hit wording remains bounded and non-novelty.
- [x] Four rendered pages pass the 220-dpi visual audit.
- [x] Two fresh reviewer-verifier processes match the canonical transcript.
- [x] `HOLD_EXTERNAL` remains active.

## Reviewer replay

From this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_review_a.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_review_a.py | cmp - CANONICAL.txt
sha256sum -c SHA256SUMS
```

Expected terminal values:

```text
exact_assertions=1493113
critical_findings=0
major_findings=0
minor_findings=0
verdict=PASS
external_status=OWNER_AMBER/HOLD_EXTERNAL
```

Reviewer-owned hashes before the non-self manifest:

```text
4954766bcdf4a56f15544b7157f1be7afa607b5ea6ab58c419cbb87ab06d5b8b  verify_review_a.py
7fed29f8dd04c2493772596e788a9763222dc5a31d7be70ecdbef28e8d717139  CANONICAL.txt
```

No repair, Round-1 manuscript mutation, publication acceptance, novelty
finding, or release authorization follows from this template.
