# HCS-C52 release test report

## Baseline

- Independent semantic gates: **16/16 PASS**.
- Targeted unit and mutation tests: **44/44 PASS**.
- Manifest scope: full project, including paper, Route-A archive, and
  integrity reports.
- Runner mode: direct executable `./code/run_c52.sh`.

## Independent algorithms

The producer and checker do not share the characteristic-zero elimination
engine.

- Producer: custom exact pair arithmetic in
  \(\mathbf Q(\rho)=\mathbf Q[\rho]/(\rho^2+\rho+1)\) and dense RREF.
- Checker: SymPy `DomainMatrix` over an independently constructed algebraic
  number field.
- Secondary checker control: both roots \(14,196\) of
  \(x^2+x+1\) modulo 211.
- Producer enumerates the 16 cycle-dihedral permutations and all \(3^7\)
  canonical phase vectors.
- Checker scans all \(8!\) permutations, derives the 16 support
  automorphisms of the 8-cycle, and then solves the phase equations by a
  recurrence.

Both exact engines verify:

- 82 relation rows, exact rank 81, quotient dimension 83;
- 1,968 relation-image membership tests;
- 94,464 ambient monomial group-law tests;
- the complete character and multiplicity table;
- a non-vacuous general scalar lift: monomial factor \(t^{-3}\), residue
  orientation factor \(t^3\), net exponent zero.  Deleting or inverting the
  orientation factor gives exponents \(-3\) and \(-6\).

The Chow--Künneth checker independently recomputes the six Lefschetz
projector compositions, transpose indices, all 24 Reynolds product-pair
counts, \(\pi_5^2=\pi_5\), and
\((\pi_5e_G)^2=\pi_5e_G\).

## Fail-closed coverage

Mutations cover source hashes, the closing edge, averaged chronology,
group order/type/phases/multiplication, the order-24 convention, Lefschetz
normalization and composition, raw-Reynolds Tate contamination, Jacobian
rank and bigrading, deleted/inverted residue orientation, relation-space
invariance, representation law, character traces and multiplicities,
rank/Hodge ledgers, primewise-projector misuse, the exact
\(\mathbf Q[G]\)-only no-go scope, C53 future gates, unknown/missing keys,
container/type smuggling, and RH/automorphism-group overclaims.

Every rehashed mutation is rejected by the intended semantic gate and the
frozen-payload gate, with no `ERROR` status.  Injected failures after the
second and third artifact-promotion moves both restore all prior targets and
leave no `.new` or `.bak` files.

## Frozen release artifacts

```text
payload_sha256 = 78d362e62efacc78dac511d9607d93f21f065a86f1d41c62c10c101b652558f1
certificate_sha256 = a2b0b281bfb311f979c7ed65e441a184ebe338b05f5fec8a60768610965c9c94
independent_check_sha256 = a4a0180a3e40a8eb82159fcea474221dafabddd728ebf1c2112435b21ad5c6f1
```

The certificate status is `RELEASE_CANDIDATE`.  The final runner
reconstructs these artifacts, executes all gates and mutations, and verifies
the full-project manifest without modifying stable bytes.
