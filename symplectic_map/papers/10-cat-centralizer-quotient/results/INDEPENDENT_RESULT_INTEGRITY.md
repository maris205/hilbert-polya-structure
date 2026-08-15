# Independent Result-Integrity Review

## Verdict

**RESULT_PASS**

The single registered Paper-10 exact audit is internally complete, hash
bound to the reviewed execution tree, and exactly reproduces the frozen
nine-modulus ledger.  A fresh finite-ring enumerator reconstructed every
stored matrix, vector, orbit partition, norm record, determinant fiber,
torsor record, quotient transition, and prime reversing-group record without
importing or invoking the candidate.  The reconstructed objects agree with
the raw result, not merely with its summary counts.

No registered or candidate audit was run during this review.  No candidate
module was imported.  The review used only read-only parsing, hashing, and an
in-memory standard-library enumerator.  No source, code, raw result, report,
claim, terminal, or test artifact was modified; this review file is the sole
write.

## Bound evidence

| Artifact | Independently reproduced SHA-256 | Status |
|---|---|---|
| Source lock | `aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2` | exact |
| Independent source-lock review | `a551784d205d9ef52ce6a493ab66cb7295a4a9dadbeb8bb2353fc58e3011dff5` | exact, source PASS |
| Framed execution tree | `87b08f11fc67eae47bdf745f8286700376f3debc5ac3fd190075a5fa2632f436` | exact |
| Deployment-review history | `990b1762e2aea6c379288854cca918cc4bbe87b7ea7ccadef7458ecfcf6988f0` | exact, Round-2 PASS |
| Pre-execution tests | `5a5b82c5aaed3dd5aca2c180bd4d1bf589e3b9a8ae4cc3dc9bf30cb04787227b` | exact, 12/12 |
| Authorized pre-execution audit | `d0aea91f5a95797f3edfcb5b30d49c50f18a16dd20cde1a44b58fe32c6f9cc99` | exact |
| Durable registered claim | `48d767edd9e3dc8f67ba1563ec03d50ef53983447263d0ce8857cfd7ff3326da` | exact |
| Raw official result | `8dceb1b8a63db462c1fd55a242ea35de974f73b6c80da68517b91c9eebb214ff` | exact |
| Certified terminal | `6cebc4224d3f275edc2ee6a847f1f7ba71d2f7793959281bcfe853fdb708ffe3` | exact |
| Post-run tests | `c0124c04106ba81c12ad89814e1547d6e16d3f7eb1f9864d21ec0178ca7e8195` | exact, 12/12 |
| Official result report | `1ece7db3fbee75bcecaecb0ad05f89fe88699c4231bea80581f382f33ed3aa6e` | exact |
| Official validation report | `f94dbfb28a71aea4dac5e89a8bc2a622bba092b66098c2fc2217ceba19a8ad5a` | exact |

The execution-tree digest was independently reproduced using the frozen
length-framed path-and-file-byte construction over the exact eight reviewed
design files and the exact closed 22-file code inventory.  All bound files
are regular files, no symlink or nonregular entry is present, and no stale
write-temporary exists.

## Strict parsing and inventory

The source lock, authorized preflight, claim, raw result, and terminal all
strict-parse with duplicate-key rejection.  The claim, preflight, raw result,
and terminal retain their prescribed canonical JSON bytes.  Before this
review was written, `results/` contained exactly these seven regular files:

- `CODE_REVIEW.md`;
- `EXPERIMENT_RESULTS.json`;
- `POSTRUN_TESTS.xml`;
- `PRE_EXECUTION_AUDIT.json`;
- `PRE_EXECUTION_TESTS.xml`;
- `registered_run.claim.json`; and
- `registered_run.json`.

There was no premature manifest, previous result-review authority, extra
result, cache, directory, symlink, or nonregular object.  The raw result has
the exact outer, audit, row, direct-engine, algebra-engine, control, and proof
contract schemas.  Its embedded pre-execution gates and deployment-review
gate are value-exact copies of the authorized preflight.  Both JUnit files
contain the exact required 12 test names, with zero failures, errors, or
skips.

## Independent finite reconstruction

For each frozen modulus, the reviewer independently enumerated all residue
vectors and all two-by-two residue matrices.  The exact-order shell was
selected by `q/gcd(q,x,y)=q`; the cyclic locus was selected by the unit
condition on `x^2-xy-y^2`; the full centralizer was obtained by direct
commutation with the fixed cat matrix; and the symplectic centralizer was its
determinant-one subgroup.  The second engine independently used
`aI+bA`, norm `a^2+3ab+b^2`, and the base map to the first column.

The resulting raw table is:

| q | `|E_q|` | `|CV_q|` | `|C_q|` | `|C_q^1|` | `ord_q(A)` | A-orbits | `CV/C` | `CV/C^1` | `E/C` | `E/C^1` | reversing `E`-orbits | norm image |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 3 | 3 | 3 | 3 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 3 | 8 | 8 | 8 | 4 | 4 | 2 | 1 | 2 | 1 | 2 | 1 | 2 |
| 5 | 24 | 20 | 20 | 10 | 10 | 2 | 1 | 2 | 2 | 4 | 2 | 2 |
| 7 | 48 | 48 | 48 | 8 | 8 | 6 | 1 | 6 | 1 | 6 | 1 | 6 |
| 11 | 120 | 100 | 100 | 10 | 5 | 20 | 1 | 10 | 3 | 12 | 2 | 10 |
| 4 | 12 | 12 | 12 | 6 | 3 | 4 | 1 | 2 | 1 | 2 | -- | 2 |
| 6 | 24 | 24 | 24 | 12 | 12 | 2 | 1 | 2 | 1 | 2 | -- | 2 |
| 9 | 72 | 72 | 72 | 12 | 12 | 6 | 1 | 6 | 1 | 6 | -- | 6 |
| 10 | 72 | 60 | 60 | 30 | 30 | 2 | 1 | 2 | 2 | 4 | -- | 2 |

Every number equals both the raw row and its source-locked expected row.  The
retained/discarded fractions also reproduce exactly: the cyclic locus is the
whole shell at `q=2,3,7,4,6,9`, and has retained fraction `5/6` with discard
fraction `1/6` at `q=5,11,10`.

The complete object-level comparisons passed:

1. the direct commutant equals the complete quadratic-algebra matrix set;
2. the full centralizer equals the algebra-unit set, and its determinant-one
   subgroup equals the norm-one set;
3. the direct cyclic locus equals the torsor image, all cyclic vectors have
   exact additive order `q`, and closure, freeness, transitivity, and base-map
   bijectivity all hold;
4. every norm-table entry satisfies matrix determinant equal to algebra norm,
   the determinant and algebra norm images coincide, and the stored delta
   fibers equal the symplectic orbit partition;
5. every stored cyclic-A, full-centralizer, symplectic-centralizer, cyclic
   locus, and full-shell orbit is exactly the independently reconstructed
   partition, including membership and multiplicity; and
6. at the five frozen primes, the brute reversing group equals the constructed
   centralizer/reversor union, is closed, obeys the reversing relation, and
   never mixes cyclic and noncyclic shell strata.

The prime full-shell strata are therefore independently recovered: one full
centralizer orbit at the inert/binary controls `2,3,7`; two at ramified `5`;
and three at split `11`.  Reversing symmetry leaves one, one, two, one, and
two shell orbits in prime order.  This confirms the stored ramified and split
discard boundaries rather than silently replacing the full shell by the
cyclic locus.

## Quotient dynamics and scoped conclusion

For every one of the nine moduli, the reconstructed full cyclic quotient has
one class and its induced cat-map transition is the identity.  The
symplectic cyclic quotient has the independently reconstructed norm-image
class count, but every one of its classes is also fixed.  Thus both quotient
layers have native primitive period one.  The formal factor `(1-z)^(-1)` is
intrinsic only as an abstract identity-map factor; substituting `z=q^(-s)`
or assigning length `log q` requires the external modulus label stored in the
result contract.

The predeclared composites `4,6,9,10` all reproduce the same one-class full
cyclic quotient and identity transition.  Hence the compression mechanism is
not prime-specific and supplies no intrinsic prime selector.  This directly
supports the frozen terminal classification:

`CENTRALIZER_CYCLIC_TORSOR_CERTIFIED / A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.

The finite audit is only a fixed-control falsification and implementation
check; all-`q` theorem authority remains the proof package.  It does not test
or reject Burnside, equivariant, group-action, orbifold, stacky, groupoid, or
twisted-sector refinements, and it does not open a Hecke, transfer,
Fredholm, quantum, prime/zero-comparison, or RH route.

## Registered lifecycle and forbidden-operation audit

The preflight records zero registered audits and an empty executed-modulus
list.  The durable claim records exactly `REGISTERED_RUN_0001`, one registered
exact audit, the frozen ordered modulus tuple, and state `STARTED`.  The
terminal binds that claim and the raw-result hash, records the same ordered
tuple as both started and completed, reports no failure code, and ends in
`COMPLETED_CERTIFIED`.  The raw result records one registered exact audit and
zero candidate numerical runs or reruns.  The closed inventory contains no
second claim, result, or terminal, so all durable evidence is consistent with
the mandated single-run lifecycle.

All forbidden-operation counters retain exact zero/false values: network and
external-data access, generated prime or modulus targets, prime tables,
Riemann-zero data, random draws, numerical `s`, `log q`, or `q^(-s)`
evaluation, matrix or parameter search, equivariant/stacky/twisted
construction, Hecke/transfer/Fredholm/quantum construction, all-`q`
inference, novelty inference, and Route-B opening.

The result is therefore authorized for the one-shot strict manifest build;
no Paper-10 scientific rerun is authorized.

CENTRALIZER_RESULT_REVIEW_V1 {"candidate_id":"cat_centralizer_cyclic_torsor_v1","execution_code_sha256":"87b08f11fc67eae47bdf745f8286700376f3debc5ac3fd190075a5fa2632f436","result_sha256":"8dceb1b8a63db462c1fd55a242ea35de974f73b6c80da68517b91c9eebb214ff","reviewer_independent":true,"source_lock_sha256":"aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2","verdict":"RESULT_PASS"}
