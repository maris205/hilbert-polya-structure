# P166 improvement log

External lifecycle: `HOLD_EXTERNAL`.

## Round 0 — author freeze

The anonymous four-page manuscript, bibliography, author verifier, frozen
canonical transcript, and PDF passed author QA.  The Round-0 PDF was frozen
as `main_round0_original.pdf`.

## Hostile Review A — accepted without findings

Independent Review A returned:

```text
decision: ACCEPT
findings: 0 Critical / 0 Major / 0 minor
reviewer assertions: 11,795,304
reviewer fresh byte-identical replays: 2/2
reviewer verifier SHA-256: 2f717ff4cd557e353b94826c85238cff19497d622f4d498b1b549cdc786be4ef
reviewer canonical SHA-256: bee2274c898591173b9fdda41b728f627c7dc30faedbf2eea70efee967ecf46d
```

The review independently re-derived the phase conjugacy, cycle-mass
exhaustion, exact period and depth censuses, last-shell equality structure,
every-target fibre formula, marked enumerator, maximum fibre, and all stated
boundaries.  Its owner, internal-collision, source, build, font, metadata,
anonymity, and visual audits also passed.

## Round 1 — no-change freeze

Review A required no repair.  Accordingly:

- `main.tex` and `references.bib` are byte-identical to Round 0;
- `code/verify.py` and `code/CANONICAL.txt` are byte-identical to Round 0;
- `main.pdf` is byte-identical to `main_round0_original.pdf`;
- `main_round1.pdf` is a byte-identical lifecycle copy;
- no theorem, proof, scope statement, citation, or build setting changed.

The common PDF SHA-256 is
`f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c`.
## Hostile Review B — internal accept without findings

Fresh Review B returned:

```text
decision: ACCEPT_INTERNAL
findings: 0 Critical / 0 Major / 0 minor
reviewer assertions: 14,005,344
reviewer fresh byte-identical process replays: 2/2
author-regression replays: 2/2 byte-identical
reviewer verifier SHA-256: bd00021b6e802fd1fac7654697df826f7d1b0890051910010e5531d2cd06c5cd
reviewer canonical SHA-256: cca342885005ce13989fcd93e8f224b92eae2d13a87856b19cbef9880d7df689
```

The second reviewer independently attacked the anchor-factor cancellation,
all exact-depth and period formulas, all-zero EGF correction, maximum-fibre
attainability, composite moduli, owner subtraction, internal collision, and
the complete build/PDF/anonymity surface.  No repair was requested.

## Round 2 — no-change internal-accept freeze

- `main.tex`, `references.bib`, `code/verify.py`, and
  `code/CANONICAL.txt` remain byte-identical to Round 0;
- `main.pdf`, `main_round0_original.pdf`, `main_round1.pdf`, and
  `main_round2.pdf` are byte-identical;
- the common PDF SHA-256 remains
  `f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c`;
- no theorem, proof, scope statement, citation, verifier, or build setting
  changed in either review transition.

The paper is internally accepted after two hostile reviews, remains
`HOLD_EXTERNAL`, and has no paper-local `SHA256SUMS` yet by explicit
lifecycle instruction.
