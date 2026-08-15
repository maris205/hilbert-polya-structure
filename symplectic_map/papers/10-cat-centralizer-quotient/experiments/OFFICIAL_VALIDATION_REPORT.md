# Official Validation Report

## Disposition

**REGISTERED_EXACT_AUDIT_PASS / INDEPENDENT_RESULT_REVIEW_PENDING**

The single Paper-10 registered audit completed on the authorized tree and
reproduced the complete frozen nine-modulus ledger.  This report authorizes
independent read-only result-integrity review.  It does not yet constitute
the final result manifest and does not authorize a candidate rerun.

## Gate chain

| Gate | Bound evidence | Status |
|---|---|---|
| Source lock | `aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2` | PASS |
| Independent source review | `a551784d205d9ef52ce6a493ab66cb7295a4a9dadbeb8bb2353fc58e3011dff5` | PASS |
| Closed reviewed tree | `87b08f11fc67eae47bdf745f8286700376f3debc5ac3fd190075a5fa2632f436` | PASS |
| Pre-execution tests | `5a5b82c5aaed3dd5aca2c180bd4d1bf589e3b9a8ae4cc3dc9bf30cb04787227b` | 12/12 PASS |
| Round-1 deployment review | byte-exact prefix SHA `5ae1d50d434c75a24e7e045d4ff220423d603c6547b8dad1138694c5e6dbb764` | FAIL preserved |
| Round-2 deployment review | full history SHA `990b1762e2aea6c379288854cca918cc4bbe87b7ea7ccadef7458ecfcf6988f0` | DEPLOYMENT_PASS |
| Authorized preflight | `d0aea91f5a95797f3edfcb5b30d49c50f18a16dd20cde1a44b58fe32c6f9cc99` | PASS |
| Durable claim | `48d767edd9e3dc8f67ba1563ec03d50ef53983447263d0ce8857cfd7ff3326da` | STARTED then terminalized |
| Raw result | `8dceb1b8a63db462c1fd55a242ea35de974f73b6c80da68517b91c9eebb214ff` | PASS |
| Terminal | `6cebc4224d3f275edc2ee6a847f1f7ba71d2f7793959281bcfe853fdb708ffe3` | COMPLETED_CERTIFIED |
| Post-run tests | `c0124c04106ba81c12ad89814e1547d6e16d3f7eb1f9864d21ec0178ca7e8195` | 12/12 PASS |

The Round-1 reviewer found that the initial semantic validator admitted a
hollow fabricated row.  Deployment remained locked.  The repair added exact
recursive schemas and types, non-Boolean residue integers, uniqueness and
partition checks, exact proof/control keys, and canonical comparison of each
row against a fresh fixed-$q$ dual-engine recomputation.  The reviewer's
exact hollow-row construction became a negative test.  Round 2 independently
reproduced the repair and issued `DEPLOYMENT_PASS`; the original failure text
remains the byte-exact prefix of the review history.

## Machine controls

All ten registered controls are exact `true`:

- ordered fixed-modulus completion;
- dual-engine agreement;
- frozen-ledger agreement;
- closure, freeness, transitivity, and base-map bijectivity of every torsor;
- one full-centralizer cyclic quotient class at every fixed modulus;
- symplectic quotient count equal to the norm-image size;
- identity induced action on both quotient layers;
- exact prime reversing groups with no cyclic/noncyclic mixing;
- one-class composite proves-too-much controls; and
- absence of a native quotient clock or intrinsic prime selector.

The complete row values are reproduced in
`experiments/OFFICIAL_EXPERIMENT_RESULTS.md` and the raw finite objects are
stored in `results/EXPERIMENT_RESULTS.json`.

## Scope validation

The finite audit is not the proof of the all-$q$ statements; theorem authority
remains `notes/PROOF_PACKAGE.md`.  The audit is a development-seen exact
falsification and implementation control over the fixed tuple
`(2,3,5,7,11,4,6,9,10)`.

The result supports only the scoped negative conclusion.  It does not create
a new centralizer theorem, dynamical-zeta theorem, prime selector, Hecke or
quantum mechanism, transfer/Fredholm determinant, prime/zero comparison, or
RH claim.  Finer equivariant, orbifold, stacky, groupoid, and twisted-sector
objects are not tested and are not rejected.

## Next integrity gate

A fresh reviewer must, without invoking the candidate:

1. verify the source, code-review, tree, JUnit, preflight, claim, result, and
   terminal hashes;
2. strict-parse the raw JSON and check exact inventories and schemas;
3. independently recompute the frozen ledger, torsor/norm/quotient/reversing
   relations from the stored records;
4. confirm every forbidden-operation counter is zero and the terminal
   classification is exact; and
5. append one canonical hash-bound `CENTRALIZER_RESULT_REVIEW_V1` authority
   only if all checks pass.

Only then may the one-shot strict result manifest be built.  No candidate
rerun is authorized at any stage.
