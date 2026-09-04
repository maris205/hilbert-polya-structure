# Narrative report: HCS-C360

## Result

The Berger ansatz is preserved by Ricci flow.  In the declared normalization,

\[
A'=-8+4C/A,\qquad C'=-4C^2/A^2,
\qquad r'=8r(1-r)/A,
\]

where `r=C/A`.  Thus anisotropy moves monotonically toward the round ray.  Off
that ray, `C/sqrt(abs(1-r))` is constant.  Introducing
`u=sqrt(1-r)` below the ray and `v=sqrt(r-1)` above it gives

\[
u'=-4(1-u^2)^2/k,\qquad v'=-4(1+v^2)^2/k.
\]

These equations integrate elementarily.  Squashed solutions are ancient;
stretched solutions begin at a finite backward anisotropic singularity; all
positive solutions become round and extinct in finite forward time.  Both
charts yield `A,C ~ 4(T-t)`, while `(T-t)R -> 3/2` and
`(T-t)K_13 -> 1/4`; curvature therefore really diverges with a Type-I bound.

For volume-normalized flow, `A^2 C` is constant while the same ratio equation
holds.  On a fixed-volume leaf, `A=K r^{-1/3}` and hence
`r'=(8/K)r^{4/3}(1-r)`.  This proves forward completeness and exponential
convergence to the unique round point on that leaf.

## Why this is a large step

The deliverable is not a local stability computation.  It joins curvature,
global maximal intervals, two elementary endpoint formulae, ancientness,
singularity type, normalization, and boundary geometry into one theorem.

## Route-A conclusion

The geometry is exact but carries no intrinsic rational-prime objects,
prime-power repetition law, logarithmic-prime clock, determinant bridge,
target analytic continuation, or natural target-zero operator.  All five
Route-A checkpoints fail and Route B remains locked.

## Evidence boundary

The JSON ledger checks exact formulae and deterministic numerical evaluations
of transcendental endpoint expressions.  It does not prove global existence,
asymptotics, or convergence; those follow from the analytic charts in the
theorem package and paper.
