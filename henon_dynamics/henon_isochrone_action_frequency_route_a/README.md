# HCS-C295 — Hénon isochrone action–frequency atlas

This package gives a proof-complete, source-local certificate for planar motion in

\[
H=\frac{p_r^2}{2}+\frac{L^2}{2r^2}
  -\frac{\mu}{b+\sqrt{b^2+r^2}},\qquad \mu,b>0.
\]

With \(\ell=|L|\), it closes the allowed bound-energy domain, radial action, radial period, apsidal frequency ratio, noncircular closure criterion, and all circular, radial, escape, signed-momentum, and Kepler-limit faces.  The main result is an all-parameter theorem; the 108 exact orbit cells and eight boundary cells are only regression witnesses.

The frozen Route-A tuple is

`(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`

and the overall verdict is `ROUTE_A_REJECTED`.  Route B is locked.  The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

From this directory:

```bash
python -B code/c295_isochrone_producer.py
python -B code/c295_isochrone_checker.py
python -B code/c295_isochrone_sympy_crosscheck.py
python -B code/c295_isochrone_replay.py
python -B code/c295_isochrone_mutation.py
python -B code/c295_release_manifest.py
```

The last command repeats every gate, performs six isolated LuaLaTeX builds, checks exact release membership, and writes the self-excluding manifest.  Build intermediates are kept outside the package.

## Artifact map

- `THEOREM_PACKAGE.md` — formal theorem, proof, boundary atlas, and claim risks.
- `SOURCE_AUDIT.md` — source ownership and literature-priority boundary.
- `results/c295_isochrone_evidence.json` — deterministic exact/algebraic certificate.
- `evaluations/route_a/HCS-C295/2026-09-02.yaml` — strict frozen evaluation.
- `paper/main.pdf` — final round-two paper.
- `C295_RELEASE_MANIFEST.json` — exact 27-payload/28-physical-file closure.

No target Euler factors, bad-prime data, root numbers, automorphy, target zero match, or Hilbert–Pólya operator are asserted.
