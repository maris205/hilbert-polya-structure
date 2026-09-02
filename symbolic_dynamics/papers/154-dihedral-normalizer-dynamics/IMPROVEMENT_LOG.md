# Improvement log

Status: `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Round 0 -> Round 1

Hostile Review A returned `REVISE — 0 Critical / 0 Major / 3 Minor`.

| Finding | Implemented repair | Closure evidence |
|---|---|---|
| m1: equations (3) and (6) left carrier/time domains implicit | Added `t >= 0`, `0 <= k <= a`, `e | m`, and `0 <= j < 2^k e` to the iterate; added `t >= 1`, `1 <= k <= a`, and the full target domain to the fibre theorem and proof | `main.tex`, Theorem 1(i),(iii) and Section 3 |
| m2: direct-owner author-name metadata was unresolved | Retained the article's printed citation `Hader Baqer Shelash`; recorded `Hayder` and contact-address surname `Ameen` as variants against the article and official index | `SOURCE_VERIFICATION.md`; zero-credit assignment unchanged |
| m3: documented source-only build ended one pass before a settled log | Added the required final `pdflatex` pass and changed reproducibility language from four-step to five-step | `BUILD.md`; actual cold evidence is recorded in `FINAL_QA.md` |

The theorem ceiling, verifier, canonical transcript, references, and frozen
Round-0 PDF were not changed beyond the quantified-domain clarification.

## Round-1 execution evidence

- A scrubbed-process verifier replay completed 29,590 assertions and was
  byte-identical to both frozen transcript copies; transcript SHA-256 is
  `25ab2e157715ddce077402e8f9383a7d52c261401d6579035eb43e8e945e9219`.
- Two independent source-only five-command builds were mutually and
  canonically byte-identical. The settled logs contained no LaTeX/package
  warning, bad box, undefined item, or rerun request.
- PDF checks: A4, five pages, unencrypted, no forms or JavaScript, blank
  descriptive metadata, all fonts embedded/subset/Unicode mapped, clean
  anonymity scan, and all pages visually inspected.
- `main_round1.pdf` and `main.pdf` are byte-identical at SHA-256
  `aafab23ed519a68e3d03df44999aa8dc525db0f3e2a860abb67825e556fd839b`
  (375,182 bytes). The Round-0 digest remains unchanged.

## Round 1 -> Round 2

Hostile Review B returned
`ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 Minor`. It independently
rederived the theorem package, verified all three Review-A repairs, replayed
29,590 assertions, rebuilt from a source-only copy, and inspected all five
pages. It requested no mathematical repair.

After Review B, the independent final cold-QA detected the latent pdfTeX
warning that automatic font expansion is available only for scalable fonts.
Round 2 closes this build-only issue by changing the preamble to
`\usepackage[expansion=false]{microtype}`. Protrusion remains active. The
five-command build is now free of warnings and bad boxes. The theorem text,
proofs, claims, bibliography, verifier, and both transcript copies are
unchanged.

- Preserved Round 1: 375,182 bytes, SHA-256
  `aafab23ed519a68e3d03df44999aa8dc525db0f3e2a860abb67825e556fd839b`.
- Current = Round 2: 373,090 bytes, SHA-256
  `72b99fe5f4813434cccb3aef9f8a023d0e7ca471029ce9831b4228dfe8db90cd`.

The external state remains `HOLD_EXTERNAL`.
