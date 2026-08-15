# Batch review: HCS-P63--HCS-P67

Date: 2026-08-15  
System family: frozen area-preserving Hénon horseshoe only  
Recommendation: **CONTINUE**

## Completed papers

1. **HCS-P63 — Primitive coordinate height and flat pressure.**  Integral
   full-horseshoe exhaustion gives a uniform all-conjugate coordinate bound,
   proving that ordinary fixed-parameter Weil-height pressure is identically
   the unweighted half entropy.
2. **HCS-P64 — Reflection-boundary Mahler packet pressure.**  Marked primitive
   reflection roots converge to a non-invariant boundary Bernoulli law,
   cyclic orbit averaging recovers maximal entropy, and the extensive packet
   Mahler pressure is a proved nonconstant linear law.
3. **HCS-P65 — Minimal symmetry-defect pressure.**  Every finite one-sided
   observable is blind to the two sampling limits, while the first cross-axis
   radius-one observable gives an exact one-half pressure-gradient gap.
4. **HCS-P66 — Reflection-boundary cohomology anomaly.**  Marked packet
   pressure has a norm-two gauge anomaly with explicit finite-cylinder
   witnesses, whereas every complete periodic-orbit average annihilates
   coboundaries exactly.
5. **HCS-P67 — Unique gauge-invariant orbit sampler.**  Uniform cyclic
   averaging is the unique normalized real linear sampler annihilating all
   coboundaries and yields a universal canonical packet pressure for every
   continuous potential.

Every project contains `README.md`, `paper/`, `code/`, `experiments/`,
`results/`, and `notes/`, together with `paper/paper.pdf`. All five executable
packages pass ordinary and optimized tests in the batch regression.

## Current strongest Route-A status

The strongest inherited formal tuple remains

```text
(A0_NOT_ADDRESSED,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT [inherited symbolic subsystem],
 A3_PARTIAL_ANALYTIC_STRUCTURE,
 A4_FORMAL_HINT)
```

with overall status `ROUTE_A_EXPLORATORY`. P67 substantially strengthens A3
by fixing the unique gauge-invariant packet normalization, but it does not
promote A1 arithmetic semantics or supply a new A2 determinant. Route B is
not authorized.

## Strongest positive result

For the odd primitive reflection packet and every continuous symbolic
potential `f`, the only normalized linear finite-orbit sampler compatible
with cohomology is uniform cyclic averaging, and it gives

\[
\mathcal P_f(s)=\frac12\log2-s\int f\,d\mu_B.
\]

This statement is exact, gauge invariant at every finite period, stable in
uniform norm, and no longer tied to one ad hoc coordinate representative.

## Strongest obstruction

The batch rules out three tempting shortcuts:

- bounded individual coordinate height cannot create an extensive pressure;
- marked reflection sampling is not invariant and has the maximal norm-two
  boundary anomaly;
- every nonuniform normalized linear cycle sampler fails cohomology
  invariance on an explicit one-site transfer function.

Thus further normalization changes are not a productive main road.

## Reusable structure

The reusable chain is:

```text
totally real bounded primitive divisors
  -> marked boundary / orbit-averaged measure pair
  -> exact cross-axis calibration
  -> signed boundary anomaly eta_J-sigma_*eta_J
  -> rank-(n-1) cyclic incidence operator
  -> unique Haar sampler and universal packet pressure.
```

## Most important ROUND2 clue

Use the unique cyclic sampler to construct a relative reflection-packet
determinant or trace. Its logarithmic derivative must retain primitive versus
repeated orbit bookkeeping, signed amplitudes, and the canonical
coordinate-Mahler/instability potential before any arithmetic comparison.

## Current largest blocker

No source-native determinant or trace presently converts the canonical
packet functional into intrinsic rational-prime powers with
von-Mangoldt-type amplitudes and phases. The canonical normalization is now
available; the arithmetic emitter is not.

## Next batch priorities

1. Build and falsification-test the canonical reflection-packet relative
   zeta/determinant, deriving its exact logarithmic derivative and repetition
   law before asking for prime matching.
2. Compare the canonical coordinate-Mahler pressure with the physical
   instability roof and Galois-excess channel, using cohomology-invariant
   quantities only.
3. Test whether Frobenius/Galois data of the effective primitive reflection
   divisors provide intrinsic arithmetic labels without importing a prime or
   zeta-zero table.

## Decision

**CONTINUE.**  The five papers close a real normalization and sampling arc.
The next batch should move to the determinant/arithmetic bridge rather than
split the settled gauge theory into additional papers.
