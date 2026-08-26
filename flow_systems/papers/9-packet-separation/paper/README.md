# Paper 9 manuscript release

**Title:** *Indiscrete Prime Packets in Deninger's Rational-Witt Flow:
Simultaneous Approximation and a Topological Corrigendum*

**Author:** Liang Wang, School of Artificial Intelligence and Automation,
Huazhong University of Science and Technology (HUST),
wangliang.f@gmail.com

## Claim boundary

For each fixed rational prime p, the manuscript proves that the genuine
finite-kernel rational-Witt packet, every inherited periodic orbit, and the
time-orbit quotient are nontrivial indiscrete spaces, and that the exact
restricted orbit relation is not closed. The naive adelic prime orbit with
its inherited double-quotient topology is also nontrivial indiscrete.

The result does not classify the full global suspension, retopologize the
intrinsic Connes--Consani scaling circle, or prove a universal obstruction for
non-Hausdorff groupoids, Haar systems, completions, or traces. It makes no
determinant, analytic-continuation, functional-equation, zero-fitting,
quantization, Hilbert--Pólya, or Route-B claim.

## Release contents

- **paper.pdf** — 21-page A4 release PDF.
- **manuscript.tex** — XeLaTeX source with independent English and
  Simplified-Chinese abstracts.
- **references.bib** — seven cited primary sources with
  manifestation-specific technical-locator notes.
- **figures/constant_class_convergence.tex** — native TikZ diagram of the
  simultaneous-approximation and constant-class mechanism.
- **figures/topology_owner_split.tex** — native TikZ map separating actual,
  naive adelic, intrinsic scaling, and proxy topology owners.

No external raster or vector figure is imported into the manuscript.

## Build

From this directory, run:

    xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
    bibtex paper
    xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
    xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex

The audited clean build used XeTeX/TeX Live 2022-dev, BibTeX, TeX Gyre
Termes, TeX Gyre Termes Math, TeX Gyre Cursor, and Noto Serif CJK fonts.

## Verification record

The release candidate was audited on 2026-08-14 (CST):

- 21 A4 pages, PDF 1.5;
- no unresolved citation or cross-reference, BibTeX warning, overfull box,
  undefined control sequence, or missing glyph;
- six harmless underfull-box notices remain;
- every PDF font reports emb=yes, sub=yes, and uni=yes;
- pdfinfo, pdftotext, pdffonts, delimiter-balance, citation-count, and log
  scans pass;
- representative raster pages 1--2, 6, and 8--21 were visually inspected for
  clipping, collisions, figures, equations, tables, declarations, and
  references.

The deterministic control suite was reproduced from the project directory
with ./experiments/reproduce.sh: 20/20 tests passed, eight CSV artifacts
contained 240 rows, verify-only validation passed, and two fresh generations
were byte-identical. The exact results/packet_separation_manifest.json
SHA-256 is
52e7a4242f91fcff1b622c9455e90ad3380ae40e742e15bf5b922a3dd4415668.

The manuscript binds the final proof audit
c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8,
independent Phase-3 peer review
447a6d575a27c87e3874591dfa3eae5f71ea1714819ada43263ffac44c53a678,
and final composition blueprint
9258fa741ad8cb60d7b5de4f9220ab64a7aa44a5490ed88c185094c4418a41f5.

## Release hashes

| File | SHA-256 |
|---|---|
| manuscript.tex | 24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb |
| references.bib | 0e4054e00ea1d09ce71d8f16fa2a051216d34f76aa437663012e726caf950f35 |
| figures/constant_class_convergence.tex | abece8b050760a3a85afb88f12875f5eed6a39a7ccbc51e92d4e9adade4f9cb7 |
| figures/topology_owner_split.tex | 53b4c678011d90d9cc20cba5e6b37720c14b1f9462cf2e9e1a2e2e81f8b7f1dc |
| paper.pdf | c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02 |

## Human-confirmation boundary

The journal-facing CRediT, competing-interest, funding, acknowledgement, and
final AI-disclosure wording remains subject to confirmation by the human
author before submission. Repository inclusion is not that confirmation.

## Source-PDF distribution boundary

Citation reproducibility and redistribution permission are separate
questions. A public GitHub sync must exclude ../notes/sources/*.pdf unless a
redistribution licence has been documented for that exact manifestation.
Local research copies are not deleted by this packaging step. Source
manifests, SHA-256 inventories, URLs, exact locators, and preflight sidecars
remain available for audit and may be synchronized.
