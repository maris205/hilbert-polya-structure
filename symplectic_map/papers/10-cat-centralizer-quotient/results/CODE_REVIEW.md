# Independent Pre-execution Deployment Review

## Verdict

**DEPLOYMENT_FAIL**

The frozen mathematics and the current executable tree are internally
consistent, but the result-semantic gate is hollow: it accepts a fabricated
row whose embedded finite objects do not encode matrices, vectors, or norm
records at all.  Because the same validator is used before committing the
official result and again by the post-run/manifest closure, this is a
deployment blocker rather than a documentation issue.

No registered or candidate audit was run during this review.  The only
dynamic reproduction called the read-only `_validate_row` function on an
in-memory fabricated object, with bytecode writing disabled.  The result
directory contained only the two supplied pre-execution artifacts before
this review file was written; no claim, official result, or terminal file
existed.

## Bound evidence

| Artifact | Independently reproduced SHA-256 | Status |
|---|---|---|
| Source lock | `aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2` | exact |
| Independent source review | `a551784d205d9ef52ce6a493ab66cb7295a4a9dadbeb8bb2353fc58e3011dff5` | exact, source PASS |
| Framed reviewed tree | `273ccc3e9d11dbc3335678034fb8da2a4278f4655af3b86d0a0380479e09946f` | independently recomputed |
| JUnit evidence | `860318fc02648708326d4fdd136be8093ab028fe68bb58b07d23115b2164e07c` | exact, 12/12 |
| Safe preflight | `27c7c3b0deb4a895cf8aed7d576bfd63cb5fafe03f14471e77c53f0ba6ca3d1a` | exact, registered count zero |

Static review confirmed that the fixed nine-modulus ledger matches the proof
package; the direct matrix engine and algebra/torsor engine implement the
intended definitions; the full shell is kept distinct from the cyclic locus;
the full and determinant-one centralizers are separate; the norm-image
counts encode the `phi(q)` versus `phi(q)/2` boundary; reversing controls are
prime-only; and both quotient transitions are required to be the identity,
with the modulus specialization explicitly external.  The claim is written
durably before the normal candidate import, and the exclusive claim/result/
terminal writers fsync both file and parent directory.

## Reproducible blocker: hollow embedded row passes

The defect is in `centralizer_q/manifest.py::_validate_row`:

- `dual_checks` need only be a nonempty dictionary whose values are `true`;
  its required key set is not checked.
- Engine dictionaries have no exact schema, matrix/vector shape, uniqueness,
  partition multiplicity, orbit membership, or internal recomputation gate.
- A norm-table record passes when both required fields are absent, because
  `None == None`.
- Most counts use raw list length, so repeated placeholders satisfy them.

The following validator-only construction was executed against the reviewed
tree and printed `FORGED_ROW_ERRORS=[]`:

```python
q = 2
expected = dict(zip(LEDGER_FIELDS, EXPECTED_LEDGER[q], strict=True))
ledger = dict(expected)
ledger.update({"retained_fraction": {}, "discarded_fraction": {},
               "norm_image_size": 1})

direct = {
    "q": q,
    "commutant": [0, 0, 0],
    "full_centralizer": [0, 0, 0],
    "symplectic_centralizer": [0, 0, 0],
    "exact_order_shell": [[], [], []],
    "cyclic_locus": [[], [], []],
    "discarded_shell": [],
    "cyclic_A_orbits": [[]],
    "full_CV_orbits": [[]],
    "symplectic_CV_orbits": [[]],
    "full_shell_orbits": [[]],
    "symplectic_shell_orbits": [[]],
    "norm_image_from_determinants": [1],
    "full_quotient_transition": {
        "identity": True, "class_count": 1, "transition": [0]
    },
    "symplectic_quotient_transition": {
        "identity": True, "class_count": 1, "transition": [0]
    },
    "reversing": {
        "shell_orbit_count": 1,
        "constructed_equals_brute": True,
        "group_closed": True,
        "cyclic_noncyclic_mixing": False,
    },
}
algebra = {
    "q": q,
    "ring_matrices": [0, 0, 0],
    "unit_matrices": [0, 0, 0],
    "norm_one_matrices": [0, 0, 0],
    "torsor_image": [[], [], []],
    "norm_image": [1],
    "norm_table": [{}, {}, {}, {}],
}
row = {
    "q": q,
    "expected": expected,
    "ledger": ledger,
    "frozen_expected_match": True,
    "dual_checks": {"hollow": True},
    "direct_engine": direct,
    "algebra_engine": algebra,
    "pass": True,
}
errors = []
_validate_row(row, q, errors)
assert errors == []
```

This is sufficient to defeat the claimed strict semantic gate.  A result
review and manifest can hash such a fabricated artifact, but hashing does not
restore the missing semantics.

## Minimum repair required before re-review

1. Require exact key sets and exact types recursively for the ledger,
   `dual_checks`, both engines, transitions, reversing record, torsor record,
   rational records, norm-table entries, fibers, and orbit containers.
2. Validate every point as a unique length-two integer residue vector and
   every matrix as a unique 2-by-2 integer residue matrix; reject duplicates,
   malformed residues, and empty placeholders.
3. Recompute the finite relations from embedded data: shell/cyclic/discard
   partitions with multiplicity control, group and orbit partitions,
   determinant/norm entries, norm image, delta fibers, quotient transitions,
   reversing equality/no-mixing, and all ledger counts.
4. Require the exact frozen `dual_checks` and control key sets, and validate
   the complete proof-only contract rather than trusting a nested `pass`
   boolean.  Add negative tests containing this hollow-row construction and
   missing norm-table fields.
5. Freeze the repaired tree, regenerate pre-execution evidence, and request a
   fresh independent deployment review.  Keep the registered count at zero.

CENTRALIZER_CODE_REVIEW_V1 {"candidate_id":"cat_centralizer_cyclic_torsor_v1","reviewed_code_sha256":"273ccc3e9d11dbc3335678034fb8da2a4278f4655af3b86d0a0380479e09946f","reviewer_independent":true,"source_lock_sha256":"aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2","test_evidence_sha256":"860318fc02648708326d4fdd136be8093ab028fe68bb58b07d23115b2164e07c","verdict":"DEPLOYMENT_FAIL"}

## Independent Pre-execution Deployment Review — Round 2

## Verdict

**DEPLOYMENT_PASS**

The repaired validator recomputes each frozen row with the reviewed exact
engines and requires canonical byte-equivalence before its recursive
structural and semantic checks. The exact Round-1 hollow row and 36 additional
missing, extra, duplicate, inconsistent, bool-as-int, matrix, point, orbit,
norm, delta, torsor, reversing, transition, fraction, and partial-dual
mutations were all rejected. Reordered, duplicated, missing, and extra modulus
rows were rejected by the outer ordered-ledger gate.

The supplied 12/12 JUnit evidence was independently parsed, the same 12 tests
were independently rerun successfully, and source/upstream bindings, fixed
ledger mathematics, executable isolation, one-shot lifecycle, review parsing,
and manifest inventory controls passed. No registered or candidate audit was
executed; the result inventory remains the three pre-execution artifacts and
reports zero registered audits. The Round-1 6119-byte prefix remains exact.

CENTRALIZER_CODE_REVIEW_V2 {"candidate_id":"cat_centralizer_cyclic_torsor_v1","review_round":2,"reviewed_code_sha256":"87b08f11fc67eae47bdf745f8286700376f3debc5ac3fd190075a5fa2632f436","reviewer_independent":true,"round1_review_sha256":"5ae1d50d434c75a24e7e045d4ff220423d603c6547b8dad1138694c5e6dbb764","source_lock_sha256":"aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2","test_evidence_sha256":"5a5b82c5aaed3dd5aca2c180bd4d1bf589e3b9a8ae4cc3dc9bf30cb04787227b","verdict":"DEPLOYMENT_PASS"}
