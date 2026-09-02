# Round-1/2 improvement log — P160 RCS

**Input:** `HOSTILE_REVIEW_A.md`  
**Disposition:** `ANONYMOUS ROUND-2 / INTERNAL ACCEPT / HOLD_EXTERNAL`

## M1 — support witness

The Round-0 phrase “add any number of parts of size one to `gamma`” was
incorrect because `gamma` must have at most `h` parts. It is replaced in the
manuscript and all proof/claim ledgers by

```text
gamma=(d), beta=empty for d>0; both empty for d=0.
```

This has one part and is valid whenever `t>=1`, hence `h>=1`. The alternative
`beta=(1^d)` is valid as well because only its largest part is bounded.

## M2 — source subtraction

Three primary records were directly verified and added:

- Gordon–Houten (1968), DOI `10.1016/S0021-9800(68)80089-4`;
- Andrews (1971), DOI `10.1112/jlms/s2-3.3.563`;
- Chen–Ji–Zang (2015), DOI `10.1016/j.aim.2014.10.017`, arXiv `1305.2116`.

Generalized/rational-slope rectangles, static two-boundary symbols and
decompositions, and two-Pochhammer factorization are now zero credit. The
residual begins only at the fixed `(a,b)` literal crop iterated through all
time plus arbitrary prescribed target, separate empty branch, exact cap
support, and ordered recovery.

## Cross-package synchronization

The manuscript, bibliography, author ledgers, all eight phase-one RCS ledgers,
and the three central contract/collision/owner ledgers were synchronized. P113
was added to the collision firewall. The independent review is preserved
unchanged; `main_round0_original.pdf` is preserved unchanged.

## Round-1 validation result

- Author verifier: two byte-matching replays, 3,462,895 assertions.
- Review-A verifier: two byte-matching replays, 7,332,616 assertions.
- Settled and two source-only builds: byte-identical, zero real warning/bad box.
- Four 144-dpi pages, 22 embedded/subsetted/Unicode font rows, and anonymity
  metadata: pass.
- `main_round1.pdf`: 4 pages, 294,530 bytes, SHA-256
  `3bbbb6f3243171d612f86a17cd88b58f56bc5ec80c3533dc30464343931def03`.

## Hostile Review B and Round 2

Independent Review B returned `ACCEPT — 0 Critical / 0 Major / 0 Minor` and
required no repair. Its 11,287,366-assertion verifier passed twice in the
review evidence and was rerun by the author-side freeze; the canonical output
SHA-256 is
`b6034231aa620d0de80a56bfcda69f8ddfe047e343498896426699252b918b8a`.

Batch final-QA preparation observed that the other four live manuscripts show
the literal lifecycle token while P160 expressed the same prohibition only in
prose. Round 2 therefore adds exactly the visible sentence `This artifact
remains HOLD_EXTERNAL`. This is explicitly not a Review-B finding and not a
mathematical, proof, source, or verifier change.

The settled PDF and two source-only cold builds are byte-identical. All four
pages, 23 embedded/subsetted/Unicode font rows, anonymous metadata, and the
visible HOLD token pass. `main.pdf` and `main_round2.pdf` are 316,629 bytes at
SHA-256
`ce59fbfca3f50ee917089175817885fc5630b807483b7a16a5d291c69292e352`.
The Round-0 and Round-1 PDFs remain unchanged.
