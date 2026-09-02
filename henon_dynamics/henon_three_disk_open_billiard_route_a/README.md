# HCS-C294 — equilateral three-disk open billiard

Frozen obstruction identifier: `HEN-O278`.

This package proves a complete collision coding theorem in the strict
no-eclipse chamber

`r>0, d>4r/sqrt(3)`.

Every cyclically reduced cyclic word determines exactly one periodic-ray
iterate: a primitive oriented, non-grazing, isolated hyperbolic geometric ray
plus a positive traversal multiplicity.  Primitive cyclic words correspond
exactly to primitive rays.  Thus `[01]` and `[0101]` have the same geometric
support but multiplicities one and two.  The proof is variational and works
for every period; finite enumeration is used only to audit conventions.
Consequently the number of collision-marked `n`-bounce returns is

`F_n=2^n+2(-1)^n`,

the primitive ledger follows by Möbius inversion, and the source-local
collision-code zeta is

`1/((1-2z)(1+z)^2)`.

The package also proves time-reversal behavior, uniform geometric length
bounds, a positive optical monodromy atlas, and a sharp parameter-boundary
atlas.  The Route-A tuple is

`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`.

The overall verdict is `ROUTE_A_REJECTED`; Route B is locked.  No target
arithmetic local data, Euler factor, root number, target functional equation,
zero match, automorphy claim, or Hilbert--Pólya operator appears.

Run `python -B code/c294_release_manifest.py` for the full deterministic
release audit.  The final article is `paper/main.pdf`.
