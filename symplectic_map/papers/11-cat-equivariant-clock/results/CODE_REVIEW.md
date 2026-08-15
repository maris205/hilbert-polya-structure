# Independent Pre-execution Deployment Review

Review date: 2026-08-15 UTC.

## Verdict

**DEPLOYMENT_FAIL**

The source-locked mathematics, signs, inverse convention, and frozen ledgers
are internally consistent, but the reviewed executable tree has three
deployment blockers: the purported invariant engines share the same
implementation path, the registered-result schema omits required
modulus-externality fields and accepts a hollow control ledger, and importing
the command-line entry point imports the candidate before the durable claim.
No deployment authority is issued.

No registered command, candidate entry point, result-manifest command,
network operation, or external dataset was run.  Review activity was limited
to read-only source inspection, independent framing/hashing, strict JSON and
JUnit parsing, and static mathematical/code analysis.  The registered audit
count remains exactly zero; `registered_moduli_executed` remains empty and
the candidate numerical-run count remains zero.

## Bound evidence

| Artifact | Independently reproduced SHA-256 | Status |
|---|---|---|
| Paper-11 source lock v2 | `331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b` | exact; strict JSON, no duplicate keys, floats, or nonfinite values |
| Independent source review R2 | `2f75d6934e3d61bdc941ee6689102a1cb08a959270a7cd87965579f1ec5cc622` | exact; `SOURCE_LOCK_PASS` |
| Framed reviewed design/code tree | `5ee0bdd9f3410a6ed17ab500522d9bc6a205b5444559b5eb02cb3e1c6a52acae` | independently recomputed over all 35 bound paths |
| Frozen JUnit evidence | `e81c286143316a19dc132b5fa6975ffd8f51dde14ec9c81f80b4f0bafc646b59` | exact; supplied evidence contains 13 tests, zero failures/errors/skips |
| Frozen safe preflight | `cee63544b76cccf2dd75057307a21147d0abd0cbefa856218927765c9f2e70d6` | exact; source/design/upstream/scanner/test gates pass, review missing, registered count zero |

The preflight's local, citation, Paper-9, and Paper-10 bindings were checked
against the source-locked paths.  The closed code inventory, expected AST
digests, fixed matrix, ordered nine-modulus tuple, prime/composite split, and
separate structural-control namespace are exact.

## Mathematical checks that passed

Static inspection independently confirmed the following source-locked
formulas and conventions.

- For a cyclic orbit `C/K` and `H=<a>`, the implementation uses
  `d_K=|H|/|H intersect K|` and `M_K=|C|/|HK|`; source factors occur at
  `d_K`, while the coarse quotient is identity with support one.
- Point-order and orbit-order Burnside records remain distinct.  In the
  regular Paper-10 torsor they have exact supports `r_q` and `1`,
  respectively; the four exponentwise scalar signatures are
  `(r_q,m_q)`, `(r_q,1/r_q)`, `(1,n_q)`, and `(1,1)`.
- The additive orbifold reduction is labelled
  `ADDITIVE_EXACT_PERIOD_REDUCTION_NOT_RING_HOMOMORPHISM`; no executable
  claim asserts preservation of Burnside multiplication, a pre-lambda
  structure, or a power structure.
- Under `(k,g).x=g*a^k*x`, the unique twisted fixer is `g=a^(-k)`, the
  labelled stabilizer triple stores `a^(-1)`, and the enhanced return twist
  stores `a`.  General cyclic-C-set recovery is only the coset modulo the
  action kernel; the regular action recovers the exact labelled matrix.
- The regular action groupoid has one isomorphism class and trivial
  stabilizer, its inertia has only the identity sector, and translation by
  `a` is represented as 2-isomorphic to the identity with induced period
  one.  No rigidification construction is claimed.
- The structural `C6/C2 disjoint-union C6/C3` control has kernel one, source
  supports two and three with no support six, coarse support one with
  exponent two, point-orbifold weights `3/2` at support two and `2/3` at
  support three, and five static inertia sectors.  It is not a tenth
  arithmetic row.  The nine regular rows preserve the two frozen period
  collisions and all four composite controls.

These checks do not cure the implementation-independence and evidence-schema
defects below.

## Deployment blockers

### B1 — the two invariant engines are one crosswired implementation

`equivariant_clock/invariants.py` defines all source, coarse, point/order,
orbit/order, twisted, enhanced, orbifold, groupoid, generator-ambiguity, and
shortening records in the single function `_common_records` (line 46).
`enumeration_engine` and `formula_engine` (lines 269--274) merely call that
same function with a Boolean flag.

The flag independently changes only selected fixed-count, twisted-count,
mark, and naturality branches.  Both alleged engines construct, among other
fields, the source/coarse factors, orbit sequence and inversion, Burnside
zeta exponents, stabilizer/triple and enhanced metadata, all scalar orbifold
factors, groupoid counts and induced period, and generator-ambiguity records
from the same statements.  A shared support, sign, exponent, inverse, or
schema defect therefore appears identically on both sides and passes
`dual_invariant_engines_match`.

The result validator compounds this crosswire: `_validate_row` recomputes
`audit_modulus(q)` with the same shared function and then requires byte
equality.  It detects tampering relative to the implementation, but it is no
independent check on the implementation.  This is exactly the
`shared implementation paths` failure mode named for milestone M2 in the
frozen experiment plan.

Minimum repair: implement a genuinely explicit engine from points, actions,
fixed sets, orbit partitions, twisted witnesses, sector incidence, and
groupoid arrows, and a separate theorem engine from `n_q`, `r_q`, `m_q` and
the proved cyclic-orbit formulas.  Do not share scientific factor,
inversion, twist, or groupoid construction code.  Add one-sided mutation
tests showing that a support, exponent, `a`/`a^-1`, sector, and period defect
in either engine is rejected.

### B2 — the raw-result contract is incomplete and its control gate is hollow

The frozen Result Artifact Contract requires the raw result to contain the
three explicit facts
`ambient_ring_varies_with_q=true`,
`intrinsic_prime_selector=false`, and
`external_modulus_specialization_required=true`.  The candidate audit and
`AUDIT_KEYS` contain neither `ambient_ring_varies_with_q` nor
`external_modulus_specialization_required`.  A related proof-only record and
the field `intrinsic_prime_selector_found=false` do not satisfy this exact
raw-result contract.  Thus a result generated by the current candidate
cannot meet the frozen evidence schema for the external/non-specific
modulus boundary.

In addition, `manifest.py` lines 257--259 accept any nonempty dictionary
whose values are literally `true` as `controls`.  Consequently
`{"hollow":true}` passes that field even though the registered candidate
defines the exact `K001`--`K012` ledger, including the period-collision,
composite, scalar-tradeoff, and no-selector controls.  Fresh row equality
does not establish that the required named controls are present.

Minimum repair: add the three exact externality fields to the candidate and
exact audit schema, validate their exact Boolean types/values, require the
exact `K001`--`K012` key set, and independently recompute every control in
the result validator.  Add negative tests for missing/extra/renamed controls
and each missing or inverted externality field.

### B3 — candidate import occurs before the durable claim

Although `run_registered` contains a local candidate import after immediate
claim validation, that import is not lazy in the actual process import
graph.  `cli.py` line 13 imports `manifest` at module load; `manifest.py`
line 9 imports `candidate`, and lines 26 and 28 import the structural and
arithmetic scientific engines.  Every script imports `equivariant_clock.cli`
before argument dispatch.  Candidate and scientific module bodies are
therefore executed before preflight and before the exclusive durable claim,
including for `code-hash` and `safe-preflight`.

The current modules have no top-level registered calculation, so this review
does not increment the registered count.  Nevertheless, the lifecycle does
not enforce its claimed boundary: the reviewed candidate has already been
imported when the post-claim local import is reached.

Minimum repair: remove candidate/scientific imports from the CLI and manifest
preflight import graph; dispatch command-specific manifest imports only when
needed, and import candidate plus scientific result validators only inside
the post-claim protected region.  Add a fresh-process regression asserting
that `equivariant_clock.candidate`, `invariants`, and `finite_module` are
absent from `sys.modules` through safe preflight and appear only after a
successfully validated durable claim.  Put immediate claim validation inside
the terminalizing `try` region so every post-claim exception is recorded
fail-closed.

## Required disposition

Keep registered execution locked and the registered count at zero.  Repair
all three blockers, freeze a new reviewed tree, regenerate the JUnit and safe
preflight artifacts, and request a fresh independent deployment review.  The
source lock and its R2 source review need not change unless the repaired code
requires a source-contract change.

EQUIVARIANT_CLOCK_CODE_REVIEW_V1 {"candidate_id":"cat_equivariant_retention_tradeoff_v1","reviewed_code_sha256":"5ee0bdd9f3410a6ed17ab500522d9bc6a205b5444559b5eb02cb3e1c6a52acae","reviewer_independent":true,"source_lock_sha256":"331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b","source_review_sha256":"2f75d6934e3d61bdc941ee6689102a1cb08a959270a7cd87965579f1ec5cc622","test_evidence_sha256":"e81c286143316a19dc132b5fa6975ffd8f51dde14ec9c81f80b4f0bafc646b59","verdict":"DEPLOYMENT_FAIL"}

EQUIVARIANT_CLOCK_CODE_REVIEW_V2 {"candidate_id":"cat_equivariant_retention_tradeoff_v1","review_round":2,"reviewed_code_sha256":"5ee1918a57fee56a2ca5a117c5749f614efbfd6baed96ae45480d6091a4741eb","reviewer_independent":true,"round1_review_sha256":"ac517ce6f5d206416ec8d19399f6bd3d7216b023d6c9a34a9acb087d016a3ee6","source_lock_sha256":"331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b","source_review_sha256":"2f75d6934e3d61bdc941ee6689102a1cb08a959270a7cd87965579f1ec5cc622","test_evidence_sha256":"4cf187fbd29f8a2b89dae2035a0971086b70108e395629ef198fcfc4869307ff","verdict":"DEPLOYMENT_PASS"}
