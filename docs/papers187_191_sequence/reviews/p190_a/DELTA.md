# P190 Review A — standalone Round-1 delta acceptance

## Disposition

**PASS_DELTA_ACCEPTED.**

Formal counterexamples: **0**.  Critical findings: **0**.  Major findings:
**0**.  Open Minor findings: **0**.  The two historical Minor findings were
presentation-only and are both closed.

## Bound delta objects

| object | SHA-256 |
|---|---|
| Round-0 `main_round0_original.pdf` | `5fb58fae99f49f14653f5eee283e2f66c3af87c06fca65e1b982e5936123eb66` |
| Round-1 `main.tex` | `73cb3d23aa88247ecbc22a75651f48f94aaf94113ccb649b1f13d64f9c37d300` |
| Round-1 `main_round1.pdf` | `81c785768621a2c3450fc67eeabc9b91d8cfda67d1061aad851844b5dd68905d` |

## Historical repairs and acceptance

### P190-A-MI-01

In Eq. (11), change

```tex
(A^{h_j})_{,y_{i_j}^*,\,y_{i_{j+1}}}
```

to

```tex
(A^{h_j})_{y_{i_j}^*,\,y_{i_{j+1}}}.
```

Round 1 makes exactly that replacement.  Source inspection, PDF text, and
visual inspection of page 3 confirm the two-index expression with no leading
comma.  The row-current/column-next orientation is preserved.

**Disposition: ACCEPTED.**

### P190-A-MI-02

Round 1 changes `\paragraph{CRediT.}` to `\paragraph{CRediT}`.  Source
inspection, PDF text, and visual inspection of page 4 confirm exactly one
rendered full stop.

**Disposition: ACCEPTED.**

## Acceptance checklist

- [x] The Round-1 source makes only the two presentation repairs above;
      remaining text-layer diff hunks are deterministic spacing/reflow.
- [x] Eq. (11) has exactly the two intended indices and no leading comma.
- [x] The PDF text layer and visual rendering show exactly one full stop after
      `CRediT`.
- [x] The theorem, proof, bibliography, owner language, and
      `OWNER_AMBER / HOLD_EXTERNAL` lifecycle boundary are unchanged.
- [x] A source-only deterministic rebuild is clean and its Round-1 PDF is
      frozen with source/PDF hashes.
- [x] Review A binds the Round-1 source and PDF, reruns its independent
      control twice in fresh processes, and records byte-identical output.

## Final disposition

- P190-A-MI-01: `ACCEPTED`.
- P190-A-MI-02: `ACCEPTED`.
- New Critical/Major/Minor findings: `0/0/0`.
- Review A verdict: `PASS_DELTA_ACCEPTED`.
- Lifecycle: `OWNER_AMBER / HOLD_EXTERNAL`.

Delta acceptance does not convert the bounded owner search into novelty or
release clearance.
