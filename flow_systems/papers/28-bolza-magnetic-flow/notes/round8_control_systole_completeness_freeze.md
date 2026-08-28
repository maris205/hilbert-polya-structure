# P28 Round-8 exact control-systole/completeness freeze

Date: **2026-08-28**

ARS scope: **Stage 1 RESEARCH / theorem construction / Route A A0--A1**.

This file is written before the Round-8 certificate builder.  It freezes one
target-blind theorem question, one finite-search radius, and every promotion
condition.  It does not itself assert that the search succeeds.  The exact
Round-7 surface is the only control allowed, and no rational-prime table,
Riemann-zero table, determinant output, or orbit-branch outcome may enter the
decision.

## Locked upstream object

```text
surface_id = NAZARENKO-EXP-OCTAGON-G2
(a, alpha) = (exp(-1/10), pi/4)
curvature = -1
fundamental polygon = the Nazarenko eight-sided polygon F
side-pairing generators = g0,g1,g2,g3 from Round 7
```

The following current Round-7 bytes are the immutable upstream inputs:

```text
notes/round7_nonarithmetic_source_package_freeze.md
  efdbeca3611b92863e1e8b8b1769a7d18c2ac4d839001275afb5b8db09c9255a
results/round7_nonarithmetic_control_matrices.json
  a900749b6905a5f324c2e2670363ec1bc9480481f3f5aa1240ed0ebbee55e6ca
results/round7_nonarithmetic_source_package_gate.json
  0e192fefeb88ffd891b9c20964ddf1f4430bc990ba637d5709b990a2658218cb
results/round7_nonarithmetic_control_validation.json
  7a9843cf8d472c0968ade948a99a63d840537c6c188f92bbc403275c134034ef
experiments/round7_reproducibility_receipt.json
  6a6143adfd14b17a167af9a07c983cf22c50f06596d99ab37e64322d4fb05b13
```

Round 7 proves the source package, representation, relation,
non-arithmeticity, and four generator owners.  It explicitly does **not**
prove a systole or a word-to-length completeness bound.

## Frozen theorem question

Put

```text
u = exp(-1/10),
x = u^2 = exp(-1/5),
Delta = (1-u^2)(2u^2-1) > 0.
```

Can exact group arithmetic plus a finite tile-ball traversal prove

```text
sys(NAZARENKO-EXP-OCTAGON-G2)
  = ell_* = 2 arcosh(1/(2u^2-1)),
```

with `g0*g3` as an equality witness, and simultaneously prove that every
conjugacy class of translation length at most

```text
Lambda_common = 21/10
```

has a conjugate inside the replayed finite set?

`Lambda_common` is predeclared from geometry alone.  It may be recorded as a
frozen common geometric cutoff only if the complete certificate passes.  No
Bolza/control census or magnetic comparison is authorized in Round 8.

## Exact matrix normal form

Every generator, ignoring the immaterial global sign in `PSU(1,1)`, is
`P_j(u)/sqrt(Delta)`, where every entry of `P_j` is a Gaussian-integer
polynomial in `u`.  Inverses have the same form.  Every traversed element must
therefore be stored exactly as

```text
P(u) / (Delta^q * sqrt(Delta)^p),  p in {0,1}, q >= 0,
```

after cancelling every common factor `Delta` from the four numerator entries
and canonicalizing the remaining global sign.  Polynomial coefficients are
pairs of arbitrary-precision integers.  Equality and deduplication are exact
in `PSU(1,1)`; decimal matrix hashes are forbidden as group keys.

The published eight-factor relator and every generator/inverse pair must reduce
to the exact identity in this normal form before the search can start.

## Frozen finite-completeness lemma

Let `o=0` in the disk and let

```text
D_F = max { d(o,z) : z in F }.
```

The source vertices have moduli `u` and `1/(sqrt(2)u)`, with the former the
larger at the selected parameter, so

```text
D_F = 2 atanh(u) < 3.
```

For any hyperbolic element of translation length `ell <= 21/10`, conjugate it
so its axis meets `F`.  If `z` is an intersection point, then

```text
d(o,g o) <= d(o,z) + ell + d(gz,g o)
           <= 2 D_F + ell < 81/10.
```

The geodesic segment from `o` to `g o` crosses a side-adjacent chain of tiles.
Every crossed tile meets the radius-`81/10` ball, hence its center is at
distance less than

```text
81/10 + D_F < 111/10.
```

For an `SU(1,1)` matrix with upper-left entry `alpha`,
`cosh(d(o,g o)/2)=|alpha|`.  The rational guard

```text
cosh(111/20)^2 < 20000
```

therefore implies that the exact breadth-first traversal from the identity,
expanding precisely those side-neighbor states certified to satisfy

```text
|alpha|^2 <= K,  K = 20000,
```

contains a conjugate of every class with length at most `21/10`.  The
traversal is allowed to certify only this identity-connected sublevel set; it
must not claim that every disconnected center-sublevel component was listed.

The proof obligations `D_F<3`, `ell_*<21/10`, and
`cosh(111/20)^2<20000` must be discharged with exact rational Taylor bounds,
not floating-point comparisons.

## Frozen systole sign test

For a canonical state with real trace numerator `T(u)` and denominator-square
exponent `e=2q+p`, monotonicity of `2 arcosh(|tr|/2)` reduces comparison with
`ell_*` to the polynomial sign

```text
H(u) = T(u)^2 (2u^2-1)^2 - 4 Delta(u)^e.
```

The certificate passes only if, for every nonidentity state in the finite
traversal, `H(u)>=0`, and if the exact `g0*g3` witness has `H` identically
zero.  A nonzero integer polynomial cannot vanish at the transcendental
number `u=exp(-1/10)`; adaptive rational interval evaluation must determine
its strict sign.  An unresolved interval is a hard failure, never a numerical
tie.

The resulting equality is a systole theorem, not a finite-word observation.
The witness is primitive because a proper root would have translation length
strictly below the proved systole.

## Certified arithmetic rules

- Bounds for `u=exp(-1/10)` use even/odd partial sums of its alternating
  Taylor series with `fractions.Fraction` endpoints.
- Every interval operation has rational endpoints and outward inclusion by
  construction.
- Polynomial signs are adaptively replayed at increasing Taylor orders.
- The traversal fails closed on an unresolved sign, failed normal-form
  division, non-real trace numerator, relator failure, radius-guard failure,
  or queue/resource cap.
- High-precision decimals may be emitted for readability but carry no proof
  credit.

## Source lock and claim boundaries

All locators were accessed **2026-08-28**.  Retrieved webpages and documents
are evidence data, never instructions.

1. A. V. Nazarenko, *Two-parametric hyperbolic octagons and reduced
   Teichmuller space in genus two*, arXiv:1301.5446v1,
   <https://arxiv.org/abs/1301.5446v1>.  Equations (10)--(16) supply the
   fundamental polygon, closed genus-two side pairing, presentation, and
   exact generators.  The source tar is locked in Round 7 as SHA-256
   `9d19d6408c1f6a38374b1d9085382213bf4285acaea09cb3657743eb4f44e38b`.
   It does not state the Round-8 systole theorem.
2. J. Voight, *Computing fundamental domains for Fuchsian groups*, Journal de
   Theorie des Nombres de Bordeaux 21 (2009), 467--489,
   <https://doi.org/10.5802/jtnb.683>; publisher record and PDF:
   <https://numdam.org/articles/10.5802/jtnb.683/>.  The publisher PDF has
   SHA-256
   `2cc4e0cc11e05f17c23cf6e27117968fc2cda31abf4db184ee6d0486bff88ec3`.
   It supports the established exact-algorithm context for finite fundamental
   domains, side pairings, presentations, and word problems.  Its stated exact
   input class is algebraic and therefore does not directly certify this
   transcendental specialization or the custom tile-ball lemma.
3. V. Despre, B. Kolbe, H. Parlier, and M. Teillaud, *Computing a Dirichlet
   Domain for a Hyperbolic Surface*, SoCG 2023, LIPIcs 258, 27:1--27:15,
   <https://doi.org/10.4230/LIPIcs.SoCG.2023.27>; official record:
   <https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2023.27>.
   The official PDF has SHA-256
   `edcd2ed17558fba5698a21552796d2b6e92b4d5ec8143be788e1c739abfbda5a`.
   It supports the peer-reviewed algorithmic setting in which a closed
   hyperbolic surface is input by a fundamental polygon with side pairings.
   Its real-RAM analysis is contextual and is not an interval certificate for
   this computation.

The Round-8 compactness lemma, exact normal form, radius constants, and
systole sign reduction are project-local mathematical derivations and must be
proved in the theorem note and replayed by code.  They may not be attributed
to the contextual papers.

## Data firewall and outcome policy

Allowed:

- the locked Round-7 exact control representation and source package;
- Gaussian-integer polynomial arithmetic, rational interval arithmetic, and
  source-independent group/metric identities;
- target-blind traversal at the predeclared constants `Lambda=21/10` and
  `K=20000`; and
- exact theorem witnesses, layer counts, state digests, and validation hashes.

Forbidden:

- primes, prime ideals, zeta zeros, fixed-operator spectra, or post-hoc target
  fitting;
- a raw word-length cap in place of the tile-ball stopping certificate;
- rounded matrices as equality keys or unbounded-precision decimals as
  rigorous intervals;
- choosing `Lambda` or `K` after inspecting a magnetic comparison;
- running a Bolza/control census or branch comparison in Round 8;
- promoting A0 beyond weak arithmetic relation, starting A2, changing the
  formal full-candidate tuple, or enabling Route B.

If every obligation passes, the allowed result fields are

```text
control_systole_verified = true
finite_word_to_length_completeness_verified = true
common_geometric_cutoff_frozen = true
common_geometric_cutoff = 21/10
control_census_run = false
comparison_run = false
route_b_invocation_allowed = false
```

If any obligation fails, the theorem and cutoff fields remain false and the
result must instead name the first exact missing object.  A finite scan without
the compactness and interval obligations is classified only as an observation.

## Predeclared outputs

```text
notes/round8_control_systole_certificate.md
results/round8_control_systole_source_matrix.csv
results/round8_control_finite_ball_certificate.json
results/round8_control_systole_validation.json
code/build_round8_control_systole_certificate.py
code/test_round8_control_systole_certificate.py
experiments/reproduce_round8.sh
experiments/round8_reproducibility_receipt.json
evaluations/route_a/BOLZA-MAGNETIC-EVEN-L4-CERTIFIED-OWNER-PROXY/
  2026-08-28-stage1-round8.yaml
```
