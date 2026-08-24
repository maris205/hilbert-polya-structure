# Route-A refinement batch plan: C134--C138

Status: **complete; five paper packages independently replayed and release-closed**.

Date: 2026-08-24

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

This round continues Route A with five separate dynamical subtypes.  Every
paper must close one named gate left by C129--C133 through an all-period,
parameter-uniform, or cross-level theorem.  A finite replay ledger is only a
sentinel for the implementation and is never used as the proof of an infinite
statement.  Coordinates belonging to different candidates are not combined.

## Frozen sequence and required progress

1. **C134 -- faithful character-torus Hardy family.**  Replace C129's one
   fifth-root translation character by the full Laurent character and the
   exact infinite-order anchor `q=(3+4i)/5`.  For
   `W_t(X)=B diag((1/2)X^t0,(1/3)X^t1,(1/5)X^t2)`, prove

   ```text
   det(I-z W_t(X))
    =1-(1/2)X^t0 z-(1/6)X^(t0+t1) z^2
       -(1/30)X^(t0+t1+t2) z^3.
   ```

   The first three logarithmic Fredholm jets therefore recover every
   branch-labelled integer translation in the frozen separated family.  The
   scaled systems with translations given by permutations of `(-2k,0,2k)` on
   radius-`3k` bidiscs retain gap `11k/16`.  In particular `k=1` and `k=6`
   alias under C129's modulo-five phase but are separated by the faithful
   family.  Label erasure and finite-precision inversion remain explicit
   boundaries.
2. **C135 -- directed-edge nonlattice suspension.**  Replace C130's
   destination-symbol roof by

   ```text
   tau = [[1,sqrt(2)],[sqrt(3),sqrt(6)]].
   ```

   Prove the exact multivariate determinant, all-period trace and primitive
   product.  Linear independence of the four radical basis coordinates makes
   the roof injective on admissible directed-edge-count vectors and separates
   the former collision `000111/001011`.  The primitive pair
   `001011/001101` has the same edge counts, and every closed binary word has
   `N01=N10`; those facts forbid an orbit-injectivity or orientation-recovery
   overclaim.
3. **C136 -- CRT-compatible metaplectic character family.**  Enlarge C131's
   standard odd-level convention to primitive additive characters
   `c in (Z/rZ)^*`.  For coprime odd `M,N`, with
   `a=N^(-1) mod M` and `b=M^(-1) mod N`, prove under the canonical CRT
   unitary that Fourier, chirp, Weyl and H\'enon metaplectic operators factor
   exactly into the `(M,a)` and `(N,b)` factors, with no scalar anomaly.  The
   final theorem also factors the involutive antiunitary
   `Theta_[r,c]=F_[r,c] K_r`, including exact evolution reversal and Weyl
   coordinate swap.  Multifactor coherence is strictly for fixed ordered
   leaves and is independent of split schedule and parenthesization after the
   canonical associator; no permutation, braiding, or symmetric-monoidal
   theorem is claimed.  The `(3,5)` control shows that naive standard `c=1`
   tensor factors are not even related by one global phase.  Noncoprime or
   even levels, corrected standard-factor cocycles, and semiclassical trace
   asymptotics remain outside scope.
4. **C137 -- uniform M\"obius--Bergman rectangle.**  Promote C132's single
   digit pair to

   ```text
   (a,b) in [3,7/2] x [6,7].
   ```

   Prove uniform closed-image separation `1/45`, trace norm at most `89/16`,
   and the trace-norm Lipschitz estimate
   `4|a-a'|+(5/32)|b-b'|`.  Retain the all-word trace and primitive product
   uniformly.  The equal-count noncyclic words `aaabb/aabab` have matrix-trace
   gap `a(b-a)^2 >= 175/8`, giving a uniform nonlinear order gap.  The larger
   rectangle `[3,4] x [6,7]` has zero boundary gap and is the exact negative
   control.
5. **C138 -- magnetic theta-graph scattering.**  Add oriented magnetic phases
   to C133's Kirchhoff theta graph while retaining its metric clock and signed
   amplitudes.  Prove unitary propagation, common-phase gauge invariance,
   antiunitary flux reversal `alpha -> -alpha`, the exact even secular
   polynomial in `rho`, and the all-period winding-resolved primitive product.
   Individual oriented cycles retain reciprocal magnetic phases, whereas the
   full determinant is even under flux reversal.  Zero flux must recover C133;
   nontrivial pi flux and a pi/2 fixed-flux reversal defect provide exact
   controls.

## Uniform artifact contract

Every package must contain the source audit, research question, theorem
package, experiment and paper plans, narrative report, two-round improvement
log, deterministic producer, independent checker, separate symbolic
cross-check, canonical byte replay, hostile semantic mutation suite,
results/test/hostile reports, evaluator-schema YAML, LaTeX source, three
preserved paper snapshots, final PDF, compile report, exact evidence receipt,
and a content-addressed release manifest.

The intended release layout is 27 payload files plus one self-excluded
manifest.  Final release additionally requires two isolated fixed-date PDF
builds, embedded fonts, zero layout/reference/citation warnings, visual page
inspection, manifest disk closure, and absence of build caches.

## Final content-addressed ledger

| paper | evidence SHA-256 | PDF SHA-256 | pages | manifest SHA-256 | mutation rejection |
|---|---|---|---:|---|---:|
| C134 | `45fa45b4668464564abb79db54b0e76b76c3acab5ae163acadb81a31d7bdc21d` | `404b2618ff7e51c6018a7b9c007b0d683dd3ade8ac6af0484f3f782692d651d5` | 2 | `7ebffe3e141628585077e340e3c3860a46fb555443b1dabdd7b9fcff701e7c18` | 48/48 |
| C135 | `9980adaab9eb511fca367b83620d557ee2227a5e9c979b6c7c8ae9a73aebee36` | `0a0ab1a405e2fdec843d26a6fa1de81d74ce12768721dd21dcee29502882c808` | 2 | `401529017d3aed50d291ff979ef22ad59664126d82bc13c47ccb4a540fe4e076` | 43/43 |
| C136 | `5b3f4a6494c8f4559a99b520247c1b83f1504884a31aaeb1fcdc3c153bbac47b` | `ab83e92b78e5857946d501c579bc3d53ca233ea5d32bf1c1865506ce776a460d` | 4 | `df52aaa1c947907903a2b8a3abcab1c0fcf628b002af691f25fd6a367aaa16ac` | 84/84 |
| C137 | `415863573ee584d72b4a47adf1e923ef04c94cef64c843c736a8e4e90802cfdd` | `71619e35d0395c53e946bf18c97e320a0f80f88ffcca1ef3fc207020b18b8a2a` | 3 | `709a3ccc2c717e69bfaf2e509a93d477717bcaeaa3dcfbd16d9b78e62a374a8b` | 41/41 |
| C138 | `733c703d9bb7b4a69dbe12ebc6d09e65dabff227b636b439c27f1d5e4a9c93c8` | `abc8fb4dff98646b07ff030a900467f1d5cfe5c0ce9db317d57205bb7689f0c6` | 3 | `664d07b1783b5f423133f19ea5b8dddc9b39f95b1434fb29428855bf95ad7905` | 45/45 |

The release contains 14 final paper pages and rejects 261/261 hostile
mutations (`256` repaired-hash semantic mutations plus five independent
stale-hash sentinels).  Every package has 28 physical release files: 27
manifested payloads plus its self-excluded manifest.

## Reproduction entry points

- [C134 package](henon_faithful_character_torus_route_a/README.md)
- [C135 package](henon_edge_roof_suspension_route_a/README.md)
- [C136 package](henon_crt_metaplectic_compatibility_route_a/README.md)
- [C137 package](henon_uniform_mobius_bergman_family_route_a/README.md)
- [C138 package](henon_magnetic_quantum_graph_route_a/README.md)
- [uniform batch review](BATCH_REVIEW_C134_C138.md)

## Strict Route-A boundary

| paper | A1 | A2 | A3 | A4 |
|---|---|---|---|---|
| C134 | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` |
| C135 | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` |
| C136 | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` |
| C137 | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` |
| C138 | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_UNITARY_OR_SCATTERING_CANDIDATE` |

Every candidate remains `ROUTE_A_EXPLORATORY` with
`route_b_invocation_allowed=false`.  None has a frozen external target
divisor, missing/extra-zero census, target functional equation, target
counting law, arithmetic local factor, Euler factor, root number, automorphy
claim, or Hilbert--P\'olya operator.
