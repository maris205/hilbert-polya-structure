# Improvement log

Status: `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Round 0 -> Round 1

Hostile Review A returned `REVISE — 0 Critical / 0 Major / 2 Minor`.

| Finding | Implemented repair | Closure evidence |
|---|---|---|
| m1: the written greedy scheduler referenced undefined `O_(m+1)` in the final-closing phase | Made the loop boundary explicit: when all openers have appeared, emit the remaining closers; the three ordinary cases now run only while an opener remains | `main.tex`, Lemma 2 proof; verifier already used this guard |
| m2: the finite power-clock profile appeared outside its frozen location | Removed the tail row from Table 1 and removed the separate dynamics paragraph; retained the finite sequence and non-theorem disclaimer only inside Limitations | `main.tex`, Limitations; transcript sentinel `power_of_two_clock=NOT_CLAIMED` retained |

The theorem ceiling, verifier, frozen transcript, references, and Round-0 PDF
remain unchanged. Round-1 execution evidence is recorded after cold replay and
source-only builds.

## Round-1 execution evidence

- A scrubbed-process replay completed 16,473,121 assertions, printed
  `power_of_two_clock=NOT_CLAIMED`, and was byte-identical to
  `verification_output.txt`; transcript SHA-256 is
  `b398a0cade8b64cdab92ee6c638e7607f3310cf9e304a52e8df07ca7d57e410c`.
- Two independent source-only four-command builds were mutually and
  canonically byte-identical. Settled logs contained no warning, bad box,
  unresolved item, or rerun request.
- All four pages were rasterized and inspected; PDF metadata, A4 geometry,
  anonymity, encryption/forms/JavaScript, and font embedding checks passed.
- `main_round1.pdf` and `main.pdf` are byte-identical at SHA-256
  `54fb1fb0a2519950d3b5725ea5e02c09eb89de13048bf7a97c62d41a9f99ebd1`
  (345,390 bytes). Round 0 remains unchanged.

## Round 1 -> Round 2

Hostile Review B returned
`ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 Minor`. It independently
rederived the threshold, total scheduler, all-rank sections, weighted fibres,
and strict rank loss; verified both Review-A repairs; cold-replayed
16,473,121 assertions; rebuilt from a source-only copy; and inspected all
four pages. It requested no repair. Accordingly, no manuscript,
bibliography, verifier, transcript, claim, or proof change was made between
Rounds 1 and 2. `main_round2.pdf`, `main_round1.pdf`, and `main.pdf` are the
same accepted artifact at SHA-256
`54fb1fb0a2519950d3b5725ea5e02c09eb89de13048bf7a97c62d41a9f99ebd1`
(345,390 bytes). The external state remains `HOLD_EXTERNAL`.
