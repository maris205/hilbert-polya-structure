# Build instructions

Status: `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

Requirements: a standard TeX Live installation with amsart, natbib, hyperref,
cleveref, microtype, and Latin Modern; Python 3 for the verifier.

From this directory run:

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

Exact replay:

    PYTHONDONTWRITEBYTECODE=1 python3 verify.py

The replay must match CANONICAL.txt and terminate with 29,590 assertions and
PASS_EXACT_REPLAY.

The TeX preamble removes timestamps, trailer IDs, and producer-side pTeX
metadata. Microtype protrusion is retained, but font expansion is explicitly
disabled to avoid pdfTeX's non-scalable-font expansion warning in a cold
build. The fifth command is required to leave the source-only log free of
cross-reference rerun requests in the pinned environment. A second five-step
build in the same environment must reproduce the same SHA-256 digest. The
first settled round is frozen as
main_round0_original.pdf.

## Round-2 freeze

Hostile Review A's three Minor findings were closed in Round 1. Hostile
Review B returned `ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 Minor` and
requested no mathematical repair. The later final cold-QA exposed a latent
font-expansion warning. Round 2 therefore changes only
`\usepackage[expansion=false]{microtype}`: expansion is disabled, protrusion
remains active, and the settled five-command log has zero warnings and zero
bad boxes. No theorem, proof, bibliography, verifier, or transcript changed.

- Round 1: five A4 pages, 375,182 bytes, SHA-256
  `aafab23ed519a68e3d03df44999aa8dc525db0f3e2a860abb67825e556fd839b`.
- Current = Round 2: five A4 pages, 373,090 bytes, SHA-256
  `72b99fe5f4813434cccb3aef9f8a023d0e7ca471029ce9831b4228dfe8db90cd`.
