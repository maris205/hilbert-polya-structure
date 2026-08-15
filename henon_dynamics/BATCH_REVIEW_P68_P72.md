# Batch review: HCS-P68--HCS-P72

Date: 2026-08-16

System family: frozen area-preserving Hénon horseshoe only

Recommendation: **PIVOT**

## Completed papers

1. **HCS-P68 — Canonical reflection-packet Euler product.** The unique
   cohomology-invariant sampler produces an exact primitive/repetition Euler
   germ whose first entropy boundary is an exponential essential
   singularity.
2. **HCS-P69 — Orbit-resolved reflection cumulant pressure.** A rank-two
   reflected transfer matrix gives
   \(F_{2m+1}(q)=2q(1+q^2)^m\) and proves the exact nonlinear pressure gap
   \(P_{\rm orb}-P_{\rm mf}=\frac12\log\cosh s\).
3. **HCS-P70 — Orbit-resolved reflection Euler boundary.** Retaining every
   primitive factor yields exact radius \(R(q)=(1+q^2)^{-1/2}\), a strict
   displacement from the mean-field radius for \(q\ne1\), and an essential
   boundary for every positive weight.
4. **HCS-P71 — Relative Lind counterterm.** The full reverse-shift Lind zeta
   leaves residual pole coefficient \(3/4\) and branch exponent \(1/2\);
   their unique counterterm makes the packet/Lind ratio locally holomorphic
   and nonzero at the first positive boundary.
5. **HCS-P72 — Relative Lind essential-singularity ladder.** Exact
   Möbius/repetition regrouping proves that the normalized relative germ has
   an essential singularity at every
   \(\rho_m=2^{-1/(2m)}\), \(m\ge2\), with \(\rho_m\nearrow1\).

Every project contains README.md, paper/, code/, experiments/, results/, and
notes/, together with paper/paper.pdf. The final batch regression ran all
five executable packages in normal and optimized modes: 80/80 unit tests
passed, all independent checks passed, and the Git worktree remained clean.

## Current strongest Route-A status

For the new canonical packet/Lind chain, the evaluator tuple is

    (A0_NOT_ADDRESSED,
     A1_WEAK,
     A2_CERTIFIED_PREFIX,
     A3_PARTIAL_ANALYTIC_STRUCTURE,
     A4_FAIL)

with overall status ROUTE_A_EXPLORATORY. The batch supplies a genuine Euler
prefix and controlled analytic continuation, but no self-adjoint operator,
rational-prime semantics, prime-power amplitudes, or explicit formula. Route
B is not authorized.

## Strongest positive result

The five papers form one exact analytic chain:

    unique cyclic sampler
      -> reflected rank-two cumulant polynomial
      -> orbit-resolved primitive Euler product
      -> unique source-native first-boundary Lind counterterm
      -> all-channel continuation formula.

The terminal formula is

\[
\log C_{\rm rel}(t)
=H_{\rm rel}(1-\sqrt2t)
-\sum_{m\ge2}c_m\frac{2t^m}{1-2t^{2m}},
\qquad
c_m=\frac1m\prod_{\substack{p\mid m\\p\ {\rm odd}}}(1-p),
\]

and every coefficient \(c_m\) is nonzero. This is an all-integer theorem,
not a fitted finite prefix.

## Strongest obstruction

The unique P71 counterterm repairs only the first boundary. For every
\(m\ge2\),

\[
\log C_{\rm rel}(t)
=-\frac{c_m}{\sqrt2\,m(1-t/\rho_m)}+\text{holomorphic},
\qquad
\rho_m=2^{-1/(2m)}.
\]

Thus the relative germ has infinitely many essential singularities inside
the unit disk. This rules out the finite-state/whole-disk meromorphic
determinant route for this exact object. It does not rule out punctured,
slit-domain, non-trace-class, or infinitely renormalized operators.

## Reusable structure

The most reusable compiler is the scalar-channel regrouping

    primitive Möbius index k + repetition index r
      -> channel m=kr
      -> c_m=(1/m) sum_{k|m,k odd} k mu(k)
      -> odd-radical Euler product
      -> one independently isolated singular boundary per m.

It cleanly separates a local counterterm from the complete global
singularity divisor and should transfer to other weighted packet products
inside the same Hénon family.

## Most important ROUND2 clue

Treat the ladder as a prescribed exponential-singularity divisor. Construct
partial all-channel counterterms on a slit domain and test:

1. normal convergence on compact subsets;
2. independence of channel ordering;
3. compatibility with the weighted q-family;
4. ownership by an infinite-rank transfer operator.

This is the narrowest surviving determinant road.

## Current largest blocker

There is no canonical punctured-domain operator or convergent infinite
counterterm that owns all channels, and the channel index \(m\) still has no
intrinsic rational-prime/von-Mangoldt meaning. The analytic object is now
precise; the operator and arithmetic emitters are missing.

## Next batch priorities

1. **All-channel renormalization:** construct or refute a canonical
   Weierstrass-type counterterm for the complete positive/complex ladder,
   with order-independent compact convergence.
2. **Weighted singularity geometry:** extend the scalar-channel
   decomposition to the natural q-weighted P70 family and determine whether
   its moving singularity divisor has a usable two-variable analytic
   structure.
3. **Punctured operator ownership:** search for a nuclear/infinite-rank
   transfer model on a slit domain whose determinant reproduces the
   renormalized channels; only after that test any arithmetic labeling.

## Decision

**PIVOT.** The batch successfully crossed the canonical packet-to-Lind local
bridge and then proved a structural global no-go for ordinary whole-disk
determinants. Do not spend the next batch fitting larger finite matrices.
Remain in the same Hénon family, but pivot to all-channel renormalization and
punctured infinite-rank ownership.
