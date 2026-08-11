# C30 paper package

This directory contains the standalone article

> *Formal Inverses Are Not Positive-Time Rauzy Dynamics: Exact Cone, Roof,
> and Trace Obstructions*.

The paper records the negative HCS-C30 promotion gate. It separates the AGY
forward length action $B^{-T}$, the reversed transfer action $B^T$, and the
raw covariant homology control; proves exact all-phase cone failures for the
two C25 length-six witnesses and the C26 length-twenty-four relation; and
derives the roof, repetition, same-space nuclearity, and flat-trace boundaries.
It also states precisely why the C29 finite group-trace determinant remains a
valid combinatorial object.

## Files

- `main.tex` — standard `article` entry point.
- `sections/` — modular manuscript sections and appendices.
- `references.bib` — primary-source bibliography only.
- `main.pdf` — compiled paper.
- `COMPILATION_REPORT.md` — reproducible build and warning audit.

## Build

From this directory, run:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The paper uses only common TeX Live packages. The source-locked arithmetic is
reconstructed by the project-level producer/checker; this paper directory does
not duplicate or modify that code, its results, or the release manifest.

## Claim boundary

The paper rejects identification of the frozen formal inverse cycles with
positive-time periodic orbits of the original AGY natural extension. It does
not retract the finite C29 group-trace moment calculation, and it does not
claim a no-go theorem for every anisotropic or clean-fixed-manifold
regularization. A positive symmetric edge clock is explicitly classified as
a new non-backtracking graph suspension.
