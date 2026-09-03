# Exact evidence and validation plan

## Claim/evidence map

The analytic proof owns the infinite-dimensional PDE theorem. Finite computation owns only convention and implementation receipts:

| Claim surface | Analytic owner | Finite receipt |
|---|---|---|
| Bessel quotient monotonicity | coefficient-pairing/Turán proof | 17 exact coefficient ratios |
| critical expansion | analytic implicit-function calculation | 9 exact quotient coefficients |
| stationary roots for all (K>2D) | strict monotonicity proof | 4 exact rational brackets |
| Bessel evaluations | positive-series tail proof | 7 exact lower/upper rows |
| full uniform spectrum | Fourier calculation | 162 rational blocks |
| global flow and dissipation | parabolic/max-principle proof | no discretized surrogate |

## Deterministic lanes

1. The producer writes canonical JSON with a self-excluding SHA-256 payload digest.
2. The checker does not import the producer. It rebuilds every exact row and locks all coordinate sets and semantic fields.
3. The SymPy lane independently checks series division, critical coefficients, the Turán derivative equivalence, zero flux, and cosine/sine Fourier blocks.
4. The replay lane produces the artifact in two isolated temporary directories and compares bytes.
5. The hostile lane attacks semantic fields, nested rows, repaired hashes, stale hashes, duplicate/nonfinite JSON, and duplicate/alias/anchor/merge/non-string/timestamp/type/unknown-field YAML.
6. Each executable explicitly refuses both `python -O` and `python -OO`.

## Certified Bessel intervals

For \(x\geq0\), truncate the positive series

\[
I_0(x)=\sum_{m\geq0}\frac{x^{2m}}{4^m(m!)^2},\qquad
I_1(x)=\sum_{m\geq0}\frac{x^{2m+1}}{2\,4^m m!(m+1)!}.
\]

After term 20, the next-term ratios are bounded by

\[
q_0=\frac{x^2}{4(22)^2},\qquad
q_1=\frac{x^2}{4(22)(23)}.
\]

On the frozen panel these are below one. A geometric majorant bounds each tail, and positive denominators turn the four Bessel bounds into a certified ratio interval. No floating point is stored or used.

## Publication closure

The release script locks exactly 27 payloads plus its self-excluded manifest, recompiles rounds 0, 1, and 2 twice apiece in fresh directories at epoch 1788393600, and requires byte identity. It rejects LaTeX warnings and layout defects, checks embedded/subset fonts, extracts sentinel text without control bytes or TeX garbage, rasterizes every page, and enforces `main.pdf == main_round2.pdf`.
