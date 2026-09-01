# Improvement log — P147

**Status:** **ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL**

## Artifact progression

| stage | artifact | result |
|---|---|---|
| Round 0 | `main_round0_original.pdf` | 3 A4 pages, 330,830 bytes, SHA-256 `c21bc9029f7dd697a623f489d446fcfa9329bd96f1bb6ea34e9c363a545a6aa3` |
| Review-A repair / current | `main.pdf`, `main_round1.pdf` | byte-identical; 4 A4 pages, 338,052 bytes, SHA-256 `1d9c5ceb72891e1c509ebeb8adfdb23d110958f129ea7ae32d3c9d427253ce20` |
| Round-2 review gate | `HOSTILE_REVIEW_B.md` | ACCEPT, 0 Critical / 0 Major / 0 Minor |
| Final archive | `main_round2.pdf` | read-only and byte-identical to accepted current PDF; SHA-256 `1d9c5ceb72891e1c509ebeb8adfdb23d110958f129ea7ae32d3c9d427253ce20` |

## Implemented Review-A repairs

1. Replaced the compressed backward-clock paragraph by a state-indexed
   ancestry selector, including the depth-zero boundary and the recursive
   doubling chain.
2. Typed every fibre target as an element of `Comp(n)` and made positive
   divisor choices explicit.
3. Added indexed orbits for both all-size equality-witness branches and
   isolated the small base cases.
4. Corrected the Knopfmacher--Prodinger source route/DOI and added the closest
   recent random-evolution and static adjacent-restriction neighbours.
5. Kept classical Carlitz enumeration, static run facts, and the literal rule
   itself at zero contribution credit.

## Closure evidence

- Review A: REVISE, 0 Critical / 1 Major / 3 Minor.
- Review B: ACCEPT, 0 / 0 / 0; all four findings explicitly CLOSED.
- Frozen verifier: 2,690,869 integer assertions, byte-identical cold replay,
  final status `PASS`.
- Independent long-range witness pressure: every `1 <= n <= 100000` passed.
- Isolated build: byte-identical to the accepted current PDF.
- Visual QA: every one of the four current pages inspected clean.

The closure-log pass did not change the theorem source, bibliography,
verifier, transcript, or PDF.  Root subsequently regenerated and verified the
final SHA manifest.  External dissemination remains `HOLD_EXTERNAL`.
