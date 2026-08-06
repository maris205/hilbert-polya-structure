# Exact-certificate results

Date: 2026-08-06  
Outcome: **`C02D_NO_GO`**  
Producer: **PASS**  
Independent checker: **PASS**

## Certified geometry

| Quantity | Exact value |
|---|---:|
| \(X\)-center magnitude | \(23/48\) |
| \(X\)-radius | \(7/48\) |
| \(Y\)-center magnitude | \(121/256\) |
| \(Y\)-radius | \(41/256\) |
| \(X_\sigma\Subset Y_\sigma\) margin | \(1/128\) |
| allowed radicand centers | \(763/4608,773/4608,1499/4608\) |
| common radicand radius | \(235/4608\) |
| minimum radicand modulus | \(11/96\) |
| minimum square-map boundary gap | \(1/288\) |
| certified square-root image clearance | \(1/360\) |
| squared derivative bound | \(2/33\) |
| derivative bound | \(2/\sqrt{66}\) |

All six chronological graph edges were reconstructed. The expected-fail
\((t,r)=(+,+)\) radicand disk has center \(37/4608\) and radius
\(235/4608\), so it crosses zero exactly as the symbolic exclusion predicts.

## Obstruction 1: window semantics

The exact one-step map is

\[
F(x,y)=(y,1-6y^2-x),
\]

and each elementary BPS block uses the one-step pinning function

\[
P_s(w,z)=s\sqrt{(1-w-z)/6}.
\]

There is no infinite-memory coefficient in this exact block to truncate.
C02C's identity

\[
F^N(u,Q_1(u,v))=(Q_N(u,v),v)
\]

identifies \(Q_1,Q_N\), on the common domain, with the iterated pinning data
of a word summand of \(\mathcal L^N\). The standard alternatives are an exact
time iterate or an exact higher-block recoding. Neither is the same-clock
finite-memory approximation frozen by C02D. This is a scoped semantic no-go,
not a claim about every conceivable lifted operator.

## Obstruction 2: ordinary orbitwise scalar sign repair

The symbolic expansion in the derivation package proves the general identity

\[
\det DR=-d\det(I-M),
\qquad
\frac d{\det DR}=-\frac1{\det(I-M)}.
\]

Three independent rational substitutions regression-check that algebraic
proof; the samples are not themselves a proof of the identity.

Thus the frozen BPS raw pinning kernel has trace \(-T_n\). A primitive cycle
would require scalar correction \(-1\), but its double repetition receives
the multiplicative correction \((-1)^2=+1\), while the required correction
is still \(-1\). The requested ordinary orbitwise scalar edge-cocycle repair
is therefore impossible. This does not rule out an accidental equality of
aggregate trace sums caused by cancellations among distinct orbits.

An odd supertrace or reciprocal determinant records the desired coefficient
algebraically, but it is classical graded machinery. The reciprocal is
generally meromorphic and does not constitute a new entire Fredholm
determinant.

## Independent checker and controls

The checker independently reconstructed the domain constants, edges,
radicand disks, boundary quadratics, determinant identities, repetition
contradiction, and canonical payload hash. It does not import the producer.

| Expected-fail control | Result |
|---|---|
| delete one chronological edge | rejected |
| replace \(1/360\) by \(1/359\) | rejected |
| assert an ordinary orbitwise scalar repair exists | rejected |
| replace the payload SHA-256 | rejected |

Payload SHA-256:
`e38faddf55a913ef089e059f1bbb3994631f1b9ba1a1bd0a379b6b9cd391f5fa`.

Stored certificate SHA-256:
`0cdd7db178ea86beb305629df9c1f479efe97af5488be24ebebc501cb1b9c62f`.

## Route-A interpretation

The frozen tuple is

\[
(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
\mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}),
\]

with overall `ROUTE_A_REJECTED`. A1 retains the intrinsic symbolic periodic
orbits of the local survivor but no prime-like information. A2 fails for the
specified orbitwise scalar repair and approximation convention. A3 has no global
completed analytic structure. A4 retains only the classical symplectic and
reversible-map hint. Route B remains closed.

## Research decision

Do not extend this lane by increasing a matrix size. A fixed-clock analytic
mode projection could be defined honestly, but general signed-trace and
finite-rank approximation theories make a routine \(H_6\) specialization a
weak novelty target. Preserve the domain lemma and both obstructions, then
return to breadth-first candidate generation rooted in Paper 5.
