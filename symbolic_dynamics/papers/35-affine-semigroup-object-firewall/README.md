# An Affine Semigroup Object Firewall

Paper 35 / Candidate `SD-C37`.

This paper benchmarks the positive `ax+b` semigroup against a literal
symbolic primitive-orbit and Fredholm claim. It distinguishes four objects
that share arithmetic notation but not periodic or operator ownership:

1. the positive right Cayley graph, which has a strict height and no closed
   paths;
2. its formal symmetrization, which introduces universal two-step
   backtracks;
3. the Hashimoto reduction, which removes backtracks but retains affine
   relation cycles;
4. the Bost--Connes Gibbs operator, whose zeta partition trace is diagonal
   energy data rather than the same graph-step primitive determinant.

The theorem is uniform in the two-generator affine monoids
`P_r=<u,v | vu=u^r v>^+`, `r>=2`. The canonical baseline uses the composite
value `r=4`, so no prime-labeled generator is built into the source.

## Frozen decision

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

overall: ROUTE_A_REJECTED
route_b_invocation_allowed: false
candidate: SD-C37
```

## Frozen research packages

- Mathematics: `/tmp/paper35_math_package.md`, SHA-256
  `e04f11dbb0ced5ad55a878cc4364c8a8d1ca33cb4cbb919b8e6b2149b83ebd25`.
- Literature: `/tmp/paper35_literature_audit.md`, SHA-256
  `f2a11df03f72a0277205a805f077996d17ef2d51b235ad993c1619ac3a1d2653`.
- Exact prototype: `/tmp/paper35_exact_prototype/`; canonical authority
  integration passes `84/84` tests and `10/10` evaluator gates. There are
  `34` final result files; the `47`-entry canonical code/result ledger has
  SHA-256
  `8ca89e858fadd9069916eeba3584aeae005ba0f1189dc7ec7c51c6cdde6b7e36`.

## Canonical exact evidence

- `520` positive height rows and `520` primitive symmetric backtracks;
- `699,040` frozen words, `126,553` admissible words, and `88` primitive
  cyclically nonbacktracking closed classes;
- `8` affine relation witnesses of length `r+3`;
- `48` quotient rows, all retaining the affine relation and `U_q^q`, with
  `14` small-modulus non-simple polygons;
- `23` scientific artifacts reproduced byte-identically in fresh A/B and
  cache-free cold C runs;
- scientific aggregate
  `94df5a68ef2a3a9a05bedddea2b6f210e437622a3d77cb1f9ec4aff351a55fed`;
- strict Route-A card SHA-256
  `d67c1fd276b1065a0504866cb758dea9a6940994d77be2c04d50d82785844d9c`.

No target-zero data, critical-line fit, prime support projector, or Route-B
step is permitted.
