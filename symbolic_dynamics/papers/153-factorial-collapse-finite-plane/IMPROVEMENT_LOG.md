# Improvement log

**Status: ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL.**

## Round 0 -> Round 1

Hostile Review A returned `REVISE — 0 Critical / 0 Major / 2 Minor`.

| Finding | Implemented repair | Closure evidence |
|---|---|---|
| m1: the quantified column notation was ambiguous at `t=0` | Replaced the interval-like notation by the indexed set `{-j: 0 <= j < t}` and stated explicitly that it is empty at `t=0` | `main.tex`, Corollary 3; source-only build and visual check recorded in `FINAL_QA.md` |
| m2: promised house declarations were absent from the manuscript | Added explicit Limitations, Data Availability, Ethics Statement, Author Contributions, Conflict of Interest, Funding, and External Status paragraphs | `main.tex`, final section; `HOLD_EXTERNAL` remains visible |

The theorem ceiling, verifier, canonical transcript, references, and frozen
Round-0 PDF were not changed by these repairs.

## Round-1 execution evidence

- A scrubbed-process verifier replay completed 18,942,551 assertions and was
  byte-identical to both frozen transcript copies; transcript SHA-256 is
  `fd900d9d0c1233a265834ce7efc25c43e2c9360a5cb3bbb5eaef4d125f67d6f9`.
- Two independent source-only four-command builds were mutually and
  canonically byte-identical.  The logs had no bad box, undefined item,
  rerun request, or build error; Review B later isolated the persistent
  font-expansion warning recorded and closed below.
- PDF checks: A4, five pages, unencrypted, no forms or JavaScript, blank
  descriptive metadata, all fonts embedded/subset/Unicode mapped, clean
  anonymity scan, and all pages visually inspected.
- `main_round1.pdf` and the Round-1 working `main.pdf` were byte-identical at
  that checkpoint, with SHA-256
  `81e56c67a1029add2bc93aaf67add40cbc68016a82e8eb2a1b7025cad2d3bb7a`
  (394,720 bytes). The Round-0 digest remains unchanged.

## Review B -> Round 2

Review B returned `REVISE — 0 Critical / 0 Major / 2 Minor`.

| Finding | Round-2 repair | Closure evidence |
|---|---|---|
| m1: the corollary statement used the repaired indexed root set, but its proof reverted to interval notation at `t=0` | Replaced the proof sentence by `{-j: 0 <= j < t}` for `0 <= t < p` and stated the empty `t=0` boundary | `main.tex`, Corollary 3 proof |
| m2: a persistent pdfTeX font-expansion warning contradicted the zero-warning QA claim | Disabled microtype font expansion at package load while retaining protrusion; this removes the engine-order warning deterministically | `main.tex` preamble, `BUILD.md`, and final cold logs |

The mathematical theorem, verifier, transcript, bibliography, and frozen
Round-0/Round-1 PDFs remain unchanged.

## Round-2 execution evidence and acceptance

- A fresh scrubbed-process replay remains byte-identical to both transcript
  copies: 18,942,551 assertions, SHA-256
  `fd900d9d0c1233a265834ce7efc25c43e2c9360a5cb3bbb5eaef4d125f67d6f9`.
- Two independent source-only builds reproduce `main.pdf` and
  `main_round2.pdf` byte for byte: 5 A4 pages, 392,821 bytes, SHA-256
  `ef8c82be2935ed23c406a7c688138400d9c76924d11f9d5c089893e8747049a5`.
- The final logs contain no build, citation, reference, rerun, bad-box, or
  font-expansion warning.  All 30 font rows are embedded/subsetted/Unicode
  mapped, identifying metadata is blank, and all five pages pass visual QA.
- `main_round0_original.pdf` and `main_round1.pdf` retain their recorded
  historical bytes and hashes.

Both Review-B Minors are closed in source.  Together with the two previously
closed Review-A Minors, surviving severity is 0 Critical / 0 Major / 0 Minor.
P153 is accepted internally at Round 2 and remains `HOLD_EXTERNAL`.
