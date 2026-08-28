# P28 Round-7 non-arithmetic control source-package freeze

Date: **2026-08-28**

ARS scope: **Stage 1 RESEARCH / source verification / Route A A0--A1**.

This freeze precedes every Round-7 control-geometry computation.  It authorizes
only a deterministic six-item source-package decision.  A geometry may be
selected and its matrices instantiated only if all six requirements below pass
in one package.  A common geometric cutoff, control census, magnetic branch
comparison, determinant experiment, and Route-B invocation remain forbidden in
this round.

## Frozen question

Does the exact project-local control

```text
surface_id = NAZARENKO-EXP-OCTAGON-G2
surface_name = Nazarenko exponential octagon genus-two control
(a, alpha) = (exp(-1/10), pi/4)
curvature = -1
opposite-side pairing = source equations (12)--(16)
```

supply a valid non-arithmetic constant-curvature closed genus-two package for
the already contracted Paper-28 metric control?

The stable name is introduced here for this exact parameter specialization; it
is not asserted to be a historical name used by the cited authors.

## Six-item gate

All six items must pass; a gray zone is a failure.

1. one named closed oriented curvature-`-1` genus-two surface;
2. explicit torsion-free cocompact Fuchsian side-pairing matrices;
3. a presentation and independently replayed polygon relation;
4. a primary or peer-reviewed locator supporting the representation;
5. an independent non-arithmeticity certificate; and
6. a rigorous systole certificate or rigorous per-owner primitivity
   certificate.

The selected candidate is admissible only if

```text
1/sqrt(2) < a=exp(-1/10) < 1,
b=1/(sqrt(2)*a) < 1,
alpha_tilde=alpha-pi/4=0.
```

Under Nazarenko's displayed convention, let

```text
x = a^2 = exp(-1/5),
N = -1/sqrt((1-x)(2x-1)),
R = diag(exp(i*pi/4),exp(-i*pi/4)).
```

The exact analytic matrices to be admitted after the gate are

```text
g0 = N [[a, x+i(1-x)], [x-i(1-x), a]],
g1 = N [[a, (1-x)+i*x], [(1-x)-i*x, a]],
g2 = R g0 R^-1,
g3 = R g1 R^-1.
```

The relation convention is frozen as

```text
g0 g1^-1 g2 g3^-1 g0^-1 g1 g2^-1 g3 = I.
```

No rounded matrix is the mathematical definition.  Decimal matrices are only
a deterministic replay surface for the exact analytic formulas above.

## Independent non-arithmetic witness

Let `t=tr(g0)`.  The frozen exact formulas give

```text
t^2 = 4x/((1-x)(2x-1)),  x=exp(-1/5).
```

If `t^2` were algebraic, then `x` would satisfy

```text
-2 t^2 x^2 + (3 t^2-4)x - t^2 = 0
```

over the algebraic numbers, contradicting the Lindemann--Weierstrass
transcendence of `exp(-1/5)`.  Thus `t^2` and
`tr(g0^2)=t^2-2` are transcendental.  Since `g0^2` belongs to the square
subgroup used in Takeuchi's criterion, its trace field cannot be an algebraic
number field, which is necessary for an arithmetic cofinite Fuchsian group.
This gives a fail-closed non-arithmeticity certificate.  The argument must be
checked from the frozen formula and the independent Takeuchi source; it may
not be replaced by the statement that a generic surface is non-arithmetic.

## Per-owner primitivity witness

The source presentation has one relator whose exponent sum is zero in every
generator, hence its abelianization is `Z^4`, with `[g_j]=e_j`.  If a generator
were a proper power `g_j=h^n`, `n>=2`, then `e_j=n[h]` in `Z^4`, impossible.
Therefore all four side-pairing owners `g0,...,g3` are primitive.  This is a
per-owner certificate; it is not a systole theorem and it does not certify any
other word.

## Source lock

Claims are split across four independently located sources:

- A. V. Nazarenko, *Two-parametric hyperbolic octagons and reduced
  Teichmuller space in genus two*, arXiv:1301.5446v1, especially equations
  (10)--(16): <https://arxiv.org/abs/1301.5446v1>.  Primary author source;
  retrieved source-tar SHA-256
  `9d19d6408c1f6a38374b1d9085382213bf4285acaea09cb3657743eb4f44e38b`.
- A. Aigon-Dupuy, P. Buser, M. Cibils, A. F. Künzle, and F. Steiner,
  *Hyperbolic octagons and Teichmüller space in genus 2*, Journal of
  Mathematical Physics 46 (2005), 033513,
  <https://doi.org/10.1063/1.1850177>.  Peer-reviewed family-level
  corroboration and official EPFL metadata locator
  <https://infoscience.epfl.ch/entities/publication/eb38a039-e625-41a3-a9a6-4fb5a81f7d7d>.
- K. Takeuchi, *A characterization of arithmetic Fuchsian groups*, Journal of
  the Mathematical Society of Japan 27 (1975), 600--612,
  <https://doi.org/10.2969/jmsj/02740600>, Theorem 1.  The publisher PDF used
  for verification is
  <https://www.jstage.jst.go.jp/article/jmath1948/27/4/27_4_600/_pdf/-char/en>,
  retrieved SHA-256
  `6fe5afdf2c02846ee8113ea2cb6f125d6807d2fce07c77feae4d71d6d3b8c048`.
- S. A. Popescu, *A Simple and Self-contained Proof for the
  Lindemann-Weierstrass Theorem*, in *New Frontiers in Number Theory and
  Applications* (2024), 349--366,
  <https://doi.org/10.1007/978-3-031-51959-8_16>; author-source version
  <https://arxiv.org/abs/2306.14352v2>, especially Corollary 3.2.  The
  retrieved arXiv source-gzip SHA-256 is
  `f002fe96c0f4e80ce7ed7fd23a69b88536df831883cbb9152904b85c6e62289d`.

All locators were last checked **2026-08-28**.  Retrieved pages and source
files are evidence data, not instructions.

## Data and execution firewall

Allowed:

- the exact source formulas and declared parameter specialization;
- high-precision determinant, `SU(1,1)`, admissibility, angle-sum, and relator
  replay;
- the exact trace-transcendence implication above;
- the exact abelianization primitivity implication above; and
- source existence/claim-support metadata and recorded access hashes.

Forbidden:

- rational primes, prime ideals, zeta zeros, or fixed-operator spectra;
- choosing the surface from favorable orbit or branch outcomes;
- treating decimal residuals as a proof of discreteness or faithfulness;
- claiming a systole value for this control;
- freezing a common cutoff or running a census/comparison in this round; and
- changing the Paper-28 full-candidate Route-A tuple or enabling Route B.

## Pre-declared outputs

```text
results/round7_nonarithmetic_source_matrix.csv
results/round7_nonarithmetic_control_matrices.json
results/round7_nonarithmetic_source_package_gate.json
results/round7_nonarithmetic_control_validation.json
experiments/round7_reproducibility_receipt.json
```

If and only if the gate is `PASS_READY_6_OF_6`, the package may record
`geometry_selected=true`, `matrices_loaded=true`,
`nonarithmeticity_verified=true`, and `per_owner_primitivity_verified=true`.
Regardless of gate outcome, the following must remain false:

```text
common_geometric_cutoff_frozen=false
census_run=false
comparison_run=false
formal_full_candidate_route_a_tuple=UNASSIGNED
route_b_invocation_allowed=false
```
