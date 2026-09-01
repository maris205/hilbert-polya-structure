# P150 — zero-totalized Lyness dynamics over odd finite fields

Status: **ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL**.

This anonymous internal short note classifies the literal self-map

```text
L(x,y)=(y,(1+y)inv0(x)),  inv0(0)=0,
```

on the whole affine plane over every odd finite field.  The proof gives a
pointwise disjoint five-stratum partition, the sharp tail polynomial, the
complete `1/2/4/5` cycle census and zeta function, the codomain-wide `0/1/q`
fibre law, and the entire singular in-tree.  Classical Lyness
five-periodicity, QRT/cluster interpretations, and general finite-field
rational dynamics are explicitly subtracted as zero-credit background.

The accepted current PDF is 5 A4 pages, 403,358 bytes, and has SHA-256
`26d0a73adb71b2e303ea637b5874939914cffd53f09a2230ded5775484c33dca`.
The paper-local exact control passes 2,144,131 Boolean assertions over 31 odd
finite-field boxes and 110,095 state/target cells in each enumeration role.

## Reproduce

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p150.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p150.py > /tmp/p150_replay.txt
cmp -s /tmp/p150_replay.txt verification_output.txt
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

`main_round0_original.pdf` freezes the first settled own-author build.
`main_round1.pdf` freezes the repair after Hostile Review A: it makes the
five-orbit integrality argument and the `q=3`/characteristic-five boundaries
explicit, and adds Lyness (1942) plus Kanki (2013) to the replayable
zero-credit source audit.  These repairs change no theorem statement.

## Review closure

Hostile Review A returned **0 Critical / 0 Major / 2 Minor**; both items were
repaired in round 1.  Hostile Review B rederived all theorem interfaces,
replayed the primary-source ledger, cold-ran 2,144,131 assertions, produced
two isolated source-only builds byte-identical to `main.pdf`, and accepted all
5/5 pages visually.  It returned **0 Critical / 0 Major / 1 Minor** solely
because the then-current `FINAL_QA.md` still described the historical
round-zero artifact as current.  The round-2 Markdown closure fixes that
provenance defect; no substantive review item remains.

All 5/5 bibliography entries are cited and resolved.  During this Markdown
closure, root separately froze `main_round2.pdf`; a read-only comparison
confirms that it is byte-identical to current `main.pdf` at the accepted
size and digest.  This closure did not create or modify it.  Exact enumeration is
falsification pressure, not a proof or an ownership certificate.  The owner
search is a bounded non-hit, not novelty or release clearance.  No public
posting, specialist contact, submission, Git action, or other external
release is authorized.
