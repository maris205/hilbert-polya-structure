# HCS-C59 exact experiment plan

Status: **PREFREEZE_CODE_RESULTS_PASS; POSTREFRESH_PASS;
FORMAL_DOCS_PASS; PAPER_PENDING; NOT_RELEASED.**

## 1. Objective and decision rule

The implemented experiment builds a deterministic, independently checked
certificate for the integrated C59 theorem in `THEOREM_PACKAGE.md`. The run
succeeds only when all eight gates below pass on one source-stable tuple and a
post-refresh hostile replay
confirms that the official files are byte-identical to the staged outputs.
The promoted tuple met that rule.

There is no partial-success theorem. A Gassmann scan without primitive orbit
sums, or one local branch without the other, is a formal failure.

This file is the **sole canonical G0--G7 numbering authority**. Differently
numbered historical discovery or engineering headings are not permitted in
schemas, certificate keys, mutation names, Route fields, or checklists.

## 2. Frozen inputs bound by the implementation

### Released predecessors

The producer and checker independently bind:

1. the complete C56 release manifest, Route/archive, certificate, schema,
   check report, degree-(27) eliminant, exact lex back-substitution shapes,
   line-incidence matrix, and labelled (W_{27}) generators;
2. the complete C58 release manifest, Route/archive, certificate, schema,
   check report, group evidence, exact eight-prime support, both (D_3)
   branches, and the embedded (I_3\supset P_3\supset Q_3) filtration;
3. the current Batch C59 target lock and protected guard; and
4. full predecessor inventories and self-excluded manifests, not selected
   leaf hashes alone.

Every path is a checker-owned basename or fixed predecessor-relative path.
Certificate-selected arbitrary paths are rejected.

### Exact constants

```text
|W(E6)| = 51840
H+ durable class: order162, index320, SmallGroup [162,11]
H- durable class: order162, index320, SmallGroup [162,19]
split witness prime = 692717
bad support = 3,5,181,283,997,1801,2346241,q
q = 14932047182473291995860108491583652133938007263719
```

The canonical integral notation is

```text
alpha_i = L d_i
eta_i = scaled integral quadratic orbit sum in alpha_i
tilde_eta_i = optional unscaled sum in d_i
eta_i = L^2 tilde_eta_i
```

The modular coefficient hashes bind `eta`, never `tilde_eta`.

## 3. G0 — released-authority rebind

**Claim.** Every C59 computation reads released C56/C58 objects and no mutable
scratch substitute.

**Producer.** Validate both release manifests, Route/archive identity, source
locks, implementation ancestry, certificate payload digests, schema/check
status, exact inventories, Batch target, and guard.

**Checker.** Independently recompute all hashes, canonical payload digests,
manifest path sets, statuses, semantic leaves, and exact subgroup arrays.

**Kill mutations.** Swap one (W_{27}) generator, one eliminant coefficient,
one filtration generator, one support prime, one predecessor path, one status,
one Batch theorem literal, and one guard byte. Every mutation must fail.

## 4. G1 — primitive integral orbit-sum resolvents

**Group subtests.**

1. Reconstruct (W_{27},H_+,H_-) from serialized arrays.
2. Recompute pair orbits through `{1,2}` and `{1,9}`.
3. Prove component sizes `27,27,81`, disjointness of the (H_+) components,
   support sizes `54,81`, stabilizer orders 162, and exact equality with the
   formal embedded subgroups.
4. Enumerate the two (G)-orbits of supports and obtain 320 families each.

**Arithmetic subtests at (p=692717).**

1. Prove primality and exclusion from all ramified and denominator sets.
2. Factor the eliminant as 27 distinct linear factors.
3. Reconstruct every line coordinate from the exact lex shapes.
4. Substitute every one of the 27 reconstructed lines into all four exact
   chart line equations.
5. Recompute all intersections and obtain a 27-vertex, 135-edge, 10-regular
   graph.
6. Enumerate the full graph automorphism group and prove equality, as a
   permutation set, with the released 51,840-element (W_{27}).
7. Evaluate all 320 conjugates of each scaled integral (eta) and require
   pairwise distinct values.
8. Multiply the 320 modular linear factors and match

   ```text
   H+ 21b304679d3b77a7b1fae4182e203d8f2652588efffa4a160cccd98ac3e81257
   H- 76fa8081c92e58839f60659fa7c9979d9b002fae5408cc30777341d21665acb2
   ```

The historical bounded graph enumeration and primitive pilot supported target
selection only. G1 is now passed by the complete promoted producer/checker
evidence, not by those pilots.

**Independence.** The promoted lanes separately reconstruct the finite-field,
incidence, support-family, and exact-group objects and do not consume the same
generated family list. The frozen backend contract uses FLINT, SymPy, and
NetworkX in the Python lane and a checker-owned exact GAP group backend.

**Kill mutations.** Change a seed, delete a component, replace (L), collide
two roots, alter a lex coefficient, toggle one incidence edge, remove one
chart equation, add one graph automorphism, or alter one modular coefficient.

## 5. G2 — complete Gassmann/minimality certificate

1. Enumerate all 350 subgroup conjugacy classes.
2. Recompute the full rational transitive permutation character for each.
3. Recover exactly

   ```text
   [12,15], [17,21], [29,36], [31,39], [41,42], [46,48],
   [57,58], [59,64], [112,120], [132,140], [301,303].
   ```

4. Prove 301/303 alone has minimum index 320.
5. Recompute order/index, core, normalizer, SmallGroup ID, abelianization,
   derived subgroup order, and full character equality.
6. Freeze GAP, TomLib, SmallGrp, CTblLib, and the transport to (W_{27}).

Equality on sampled Frobenius, cyclic, or element-class rows is insufficient
unless a separate proof shows that the samples determine the full character.

## 6. G3 — fixed-field and zeta bridge

The evidence and written proof together must certify:

1. (H_\pm)-invariance of (eta_\pm);
2. modular distinctness implies 320 characteristic-zero conjugates;
3. degree comparison gives (\mathbf Q(\eta_\pm)=K^{H_\pm});
4. trivial cores give common normal closure (K);
5. a field isomorphism would conjugate the two stabilizers; and
6. full character equality gives equal Dedekind zeta functions by Artin
   formalism.

No characteristic-zero expanded coefficient list, integral basis, class
number, or ring-of-integers isomorphism is inferred.

## 7. G4 — signed discriminant, signature, and exact support

1. Recompute the orbit-count vector

   ```text
   36,56,112,16,64,128,160,168
   ```

   for `I3,P3,Q3,I5,P5,tame-C3,reflection-C2,C-infinity` on both carriers.
2. Derive exponents `(624,496,192,160)` with exact fractions.
3. Rebind C58 unramifiedness outside the eight-prime support and use positive
   exponents to prove exact support.
4. Derive `(r1,r2)=(16,152)` and positive sign.
5. Rebuild the 11,658-digit integer and match its unsigned no-newline digest
   `7f3ed0f731e5905f9af8254df2114ad15c2bb7d96cfa9a8b464a58ae8ea3ae70`
   without printing it in the certificate.

## 8. G5 — complete ToM-140 local algebra

For every (D\backslash G/H) representative, compute

\[
J=D\cap gHg^{-1},\quad n=[D:J],\quad
e=[I:I\cap J],\quad f=[D:IJ].
\]

Compute the lower-filtration different contribution and require the exact
rows in `THEOREM_PACKAGE.md`, 36 factors per field, total degree 320,
(n=ef), and total (sum fd=624). Require degree multisets

```text
H+: 1^8 6^10 9^8 18^10
H-: 2^4 3^12 6^4 9^4 18^12.
```

## 9. G6 — complete ToM-206 algebra and branch independence

1. Exhaust embedded ToM-206 candidates and prove the unique normal ToM-140
   inertia.
2. Rebind the exact normal (I\supset P\supset Q) chain.
3. Recompute all double cosets and require 18 factors, total degree 320,
   (n=ef), and total (sum fd=624).
4. Require degree multisets

   ```text
   H+: 2^4 12^5 18^4 36^5
   H-: 4^2 6^6 12^2 18^2 36^6.
   ```

5. Derive nonisomorphism only from the factor-degree obstruction.
6. Record `d3_branch_selected=false` and
   `local_fields_classified_by_nefd_rows=false`.

## 10. G7 — independence, envelope, novelty, scope, release discipline

1. Producer and checker have disjoint theorem call graphs; shared utilities
   are canonical I/O, fingerprints, and backend preflight only.
2. Checker rebuilds every scalar payload leaf, exact key set, shape digest,
   and schema relation.
3. Mutations cover every gate and both evidence carriers.
4. Source, predecessor, evidence, certificate, schema, and check-report
   fingerprints are verified before and after every child process.
5. Staging, promotion, rollback, manifests, and scratch files follow the
   hardened dirfd/non-ABA design, with the same-UID no-concurrent-path-mutator
   premise documented where unavoidable.
6. All scope leaves are explicit Booleans, including
   `NO_BAD_EULER_OR_ROOT_NUMBER` semantics.
7. Source ledger explicitly credits James, Perlis, Bosma--de Smit,
   McReynolds, Mantilla-Soler, Komatsu, Stauduhar, and Fieker--Klueners.

The promoted payload has exactly these 15 top-level keys:

```text
artifact_contract
G0_released_authority_rebind
G1_primitive_orbit_resolvents
G2_gassmann_minimality
G3_fixed_fields_and_zeta
G4_global_arithmetic
G5_tom140_local_algebra
G6_tom206_local_algebra
G7_independence_scope_release
written_bridges
backend_contract
source_contract
scope_nonclaims
nonresults
status
```

The promoted `scope_nonclaims` object has exactly these 30 Boolean-false
leaves:

```text
integral_permutation_equivalence_claimed
rings_of_integers_isomorphic_claimed
class_number_equality_claimed
idele_group_isomorphism_claimed
local_equivalence_claimed
adelic_equivalence_claimed
d3_branch_selected
local_fields_classified_by_nefd_rows
expanded_characteristic_zero_resolvent_claimed
characteristic_zero_coefficient_hash_claimed
integral_basis_claimed
maximal_order_claimed
monogenicity_claimed
polynomial_discriminant_equals_field_discriminant_claimed
decomposition_frobenius_claimed
bad_artin_euler_claimed
local_epsilon_factor_claimed
local_root_number_claimed
global_root_number_claimed
artin_holomorphy_claimed
automorphy_claimed
rational_point_claimed
hasse_principle_claimed
weak_approximation_claimed
brauer_manin_claimed
motive_claimed
rh_claimed
hilbert_polya_operator_claimed
paper_complete_claimed
release_claimed
```

## 11. Frozen implementation inventory

The reviewed implementation inventory is exact and closed at 13 code files
and 8 result files.

### Code: 13 files

```text
code/c59_exact.py
code/c59_pipeline.py
code/c59_group.py
code/c59_resolvent.py
code/c59_producer.py
code/c59_checker.py
code/c59_checker_group.g
code/c59_checker_resolvent.py
code/c59_atomic_promote.py
code/c59_hash_manifest.py
code/run_all.sh
code/test_c59.py
code/README.md
```

### Results: 8 files

```text
results/c59_group_evidence.json
results/c59_resolvent_evidence.json
results/c59_certificate.json
results/c59_schema.json
results/c59_check_report.json
results/scoped_hash_manifest.json
results/RESULTS.md
results/TEST_REPORT.md
```

The two evidence carriers were immutable producer inputs during official
refresh. Neither opaque CAS prose nor certificate-selected paths are accepted.
The self-excluding scoped manifest has 20 entries: 13 code files, two prose
results, and five promoted result files other than the manifest. The exact
live code/results inventory has 21 entries.

## 12. Execution order

1. **Complete:** bind the target-lock formal roots and their historical Route
   aggregate.
2. **Complete:** review and freeze the implementation inventory.
3. **Complete:** build G0 and the source-architecture tests.
4. **Complete:** build independent group and primitive-resolvent evidence
   lanes.
5. **Complete:** assemble producer/checker payloads and the mutation suite.
6. **Complete:** run one pristine chain, official refresh, mandatory replay,
   and hostile post-refresh audit.
7. **Complete:** audit the refreshed formal roots and bind their aggregate.
8. **Pending:** build and audit the anonymous paper and complete the commit,
   full-project manifest, Route archive, promotion, and release gates.

No degree-(320) characteristic-zero coefficient expansion or maximal-order
calculation is a theorem prerequisite.

## 13. Current state

All gates G0--G7 have `PREFREEZE_CODE_RESULTS_PASS`, and the independent
post-refresh machine audit has `POSTREFRESH_PASS`. The exact inventory is
13 code files, 8 result files, 21 live leaves, and a 20-entry self-excluding
scope. The 48-test suite passed. The checker rebuilt 10,412 payload leaves,
rejected 20,894 certificate mutations plus 8 evidence-rebound mutations, and
bound:

```text
payload  a6428addfb14f00f3ed45781d9ba0944be177cfb7c257c958e7fa538fcaf366b
shape    788aa5e58d51f0d4edfa7a4e58de5748bd5a1ad1d28445d91045d5dd72c850d2
G0       ac445822702b5e376eed6fbfa86a4df81c7f8177ca35c8211282dca830123d5d
cert     3c4c756d912d49653353503701f5b8be412d0da53383ac9c9830b6e7a953ed9a
check    271d0123b170bef1317b63e97e3f679179b6e794185b78facd571150ba2123d3
schema   07a817bb2eade24862f0cf4dca8d1d0248eb4f473a137c07bd0200efeea8c6b4
group    0b01f9d47e5141d2bff88fbe4d58ed049d88751cbf8ab1df5469009b684c4958
resolver 667e0eeb04e5724b620bf513f9556a321dfd39f9215396ed1840ca83879ec6a6
manifest c4145ea23b57b1adcd8cfddb18c41c703e93ca8a6f84eeecb9457e0f4e046dda
```

The refreshed formal-document aggregate and its hostile audit have
`FORMAL_DOCS_PASS`. No paper, full-project release manifest, Route archive,
promotion, or release PASS is claimed.
