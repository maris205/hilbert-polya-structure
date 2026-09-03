# P172 build and verification ledger

**Round:** historical author Round 0 followed by final Round 2  
**Lifecycle:** `HOLD_EXTERNAL`

## Independent verifier

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 verify_p172.py
result: PASS
assertions: 48,575
literal boxes: every subset and every restriction through n=6
labelled powers: t=0,...,4
exact rational Jordan boxes: n=2,...,9
stdout SHA-256: a279b8841d9d3d05055520fe4a49998c078c16d9156d1a5ed1354a3d81cd0756
```

The verifier imports no scouting, manuscript, or prior-paper code.  Its
enumeration is falsification pressure and does not replace the proofs.

## Round-0 build

The settling sequence was

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The final logs contain zero LaTeX/package warnings, bad boxes, unresolved
references/citations, or rerun requests.

```text
pages: 3
bytes: 259,538
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
PDF SHA-256: ac16b12438b1c2db313cc55af630887112ce53833cb7afb76deb656329164ecb
round0 copy byte-identical: yes
font rows: 20
embedded/subsetted/Unicode rows: 20/20
encrypted: no
forms: none
JavaScript: no
```

All three pages were rasterized at 120 dpi and visually inspected.  The
theorem continuation, matrices, fractions, bibliography, running heads, and
page numbers are legible and remain inside the page box.  Metadata author,
title, subject, keywords, creator, and producer fields are blank.

## Frozen Round-0 hashes

```text
0cc73c64296af9861526d3f56041d38e9df174601e4b65ca87694ae43fb52ce6  main.tex
a61ba6d2ee8f9b05d229a7491364eb22ab75a103018dde53f72763904d54fbfe  references.bib
108b6054eb1aafcbd33384724443796893890dd0d40e01dbb61404dff520b6a2  verify_p172.py
a279b8841d9d3d05055520fe4a49998c078c16d9156d1a5ed1354a3d81cd0756  verification_output.txt
ac16b12438b1c2db313cc55af630887112ce53833cb7afb76deb656329164ecb  main.pdf
ac16b12438b1c2db313cc55af630887112ce53833cb7afb76deb656329164ecb  main_round0_original.pdf
```

Cold builds and dual-review round copies are intentionally deferred to the
batch review stage.

## Review-round builds

Review A produced a three-page Round-1 PDF of 261,507 bytes with SHA-256
`ef34c142ea0350d86501d04cc829b8ba8a5e87ea21970b6f180e4bcd7276e62b`.
Review B's owner/formalization repairs produced the accepted four-page
Round-2 PDF of 274,791 bytes with SHA-256
`91e8cc76f007eafba48a343aae116eeda03daa8bf3e1bcdbe50d2fc2e2013c83`.
The Round-2 settling logs contain no warning, bad box, unresolved citation or
reference, rerun request, or fatal error.  Two final temporary directories,
each initialized with only `main.tex` and `references.bib`, reproduced the
canonical PDF byte for byte; their settled LaTeX and BibTeX logs are retained
as `build_final_cold{1,2}_*.log` and contain no warning or error.  Review-B
delta acceptance closed every finding.
