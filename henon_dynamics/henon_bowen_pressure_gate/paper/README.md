# Paper package

This directory contains the manuscript

> **A Certified Bowen-Pressure Gate for an Area-Preserving H\'enon
> Horseshoe**

The paper proves a rigorous enclosure of the positive pressure root on the
source-locked \(H_6\) survivor, identifies that root's geometric meaning, and
records the negative Route-A consequence.  The earlier finite-section value
is only compared with the bracket; its equality or convergence is not
claimed.

Build from this directory with

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The released [main.pdf](main.pdf) has nine A4 pages.  The final build has no
undefined references or citations, LaTeX/package warnings, or overfull and
underfull boxes.  See [COMPILATION_REPORT.md](COMPILATION_REPORT.md) for the
toolchain, hashes, and semantic audit.

The dimension statements use two explicitly local interfaces:

- Pesin--Sadovskaya (2001), Remark 4.1, for the unstable slice of a
  (u)-conformal diffeomorphism on a locally maximal hyperbolic set;
- Barreira (2013), Introduction, Theorem 1.2, for the total dimension of a
  locally maximal surface hyperbolic set.

No compact-surface extension of the plane H\'enon map is assumed.
