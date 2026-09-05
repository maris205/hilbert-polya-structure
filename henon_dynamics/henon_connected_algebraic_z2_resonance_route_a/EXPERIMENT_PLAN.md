# Frozen exact experiment contract

Universal target: all finite-index HNF lattices. Finite certificate population:
all 127 HNF triples of index at most twelve plus fifteen triples with
`(a,c)=(3,6),(6,3),(6,6)`, all permitted b. There are 142 rows, twenty resonant
and 122 nonresonant. Each row carries its entire quotient matrix, left/right
unimodular Smith witnesses, positive diagonal, characteristic polynomial,
rank, component count and kernel Gram data.

Independent verification uses no producer import and no symbolic package:
Bareiss determinants certify unimodularity, direct multiplication checks Smith
factorization, and Faddeev--LeVerrier verifies every characteristic coefficient.
A separate SymPy lane uses its own Smith algorithm and a 90-digit Fourier
product, then compares Jensen integration to a Hurwitz-zeta evaluation.

All torus grids with denominator 1–24 are enumerated: 4900 denominator-labelled
records. The same rational point can occur in several grids; this is not a
count of distinct rational points in their union.
Eight paired Dirichlet heads H=1,2,4,8,16,32,64,128 carry reduced rational
sums and explicit positive remainder bounds. Neighboring shear, prime/composite
indices and composite denominators are mandatory controls. Repaired-hash
attacks and raw/type-locked YAML attacks must be rejected, including during
release `--write`. No GPU or random seeds are relevant.
