# Claim-driven executable plan

## Frozen conventions

- State: head–tail director `[p]` in `RP2`; unit vectors are representatives.
- Flow: `L=diag([[a,b],[c,-a]],0)` in physical time.
- Shape: `lambda=(r^2-1)/(r^2+1)` with finite `r>0`.
- Sphere convention: at `r=1`, `RP2` denotes a marked material director; an
  unmarked sphere has no intrinsic shape director.
- Generator: `B=W+lambda E`, with `E=(L+L^T)/2` and `W=(L-L^T)/2`.
- Baseline: `51fb3d46f96b854314811c1ad62d3103cd5d54e5`.
- Evaluator SHA-256: `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
- Epoch/scope: `1788220800`; `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Gates

1. Prove `[p(t)]=[exp(tB)q0]` directly from normalization.
2. Reconstruct `B2^2=delta I` and every sign/zero chamber exactly.
3. Separate `gamma!=0` head–tail, nonvertical oriented-vector, equatorial,
   mixed, and vertical-fixed periods.
4. Prove the complete hyperbolic source–saddle–sink cell decomposition,
   including the two `RP1` stable/unstable manifolds and endpoint exclusions.
5. Prove the nilpotent fixed `RP1`, algebraic convergence, and identity face.
6. Enumerate 625 rational parameter cells and 320 independent orbit rows.
7. Cross-check with a producer-independent implementation using exact key sets
   and boundary semantics, plus exact SymPy.
8. Reject repaired semantic, duplicate/drop-replace, and stale-hash mutations.
9. Retain three substantive, deterministic, warning-free PDF revisions.
10. Close the exact 27-payload manifest and strict Route-A nonclaims.

Finite rows are regression oracles.  They do not prove the all-real-parameter
theorem, whose proof is the Cayley–Hamilton/projective argument in the paper
and theorem package.
