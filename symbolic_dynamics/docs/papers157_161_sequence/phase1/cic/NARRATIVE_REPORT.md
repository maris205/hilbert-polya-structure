# Narrative report — cut-intersection collapse

## One-sentence result

Intersecting `K_n` with fresh fair vertex cuts has an exact absorption law and
a complete labelled target atlas because an edge survives precisely between
vertices with complementary binary histories.

## Organizing insight

After `t` epochs every vertex carries a `t`-bit word.  The `2^t` words form
`R=2^(t-1)` complementary pairs.  A pair occupied on both sides creates one
connected complete bipartite component; a one-sided occupied pair contributes
only isolates.  Thus the stochastic history space is exactly an occupancy
problem on distinguished antipodal pairs.

The empty target gives the absorption CDF through
`A_R(n)=n![x^n](2e^x-1)^R`.  Reserving oriented complementary pairs for the
nontrivial components of an arbitrary target gives its exact fibre
`(R)_r 2^r A_(R-r)(z)`.  The same proof exposes a subtle resource boundary:
when all `R` pairs are consumed by components, no isolate is possible.

## Claim hierarchy

1. The complete every-labelled-target fibre is the central result.
2. The absorption CDF and first-hit law are a temporal specialization.
3. The corrected image classification and its EGF are structural
   consequences.
4. The union-bound tail supplies almost-sure absorption and mean convergence,
   not a contribution claim.

## Evidence state

The focused verifier enumerates every word history and every labelled graph
in its frozen boxes, including all zero fibres and the `r=R,z>0` counterexample.
It passes 35,278 assertions.  The canonical transcript SHA-256 is
`728c32e557e920c46022f3fe8d24fce1e5e303a3d43d823b6d22ae20d7a85fe8`.

## Scope boundary

Cuts, binary codes, bicluster graphs, random-intersection vocabulary,
labelled EGFs, and inclusion–exclusion are owned inputs.  The residual is only
their exact conjunction for this literal cumulative-cut process.  A bounded
non-hit is not a novelty or release certificate.
