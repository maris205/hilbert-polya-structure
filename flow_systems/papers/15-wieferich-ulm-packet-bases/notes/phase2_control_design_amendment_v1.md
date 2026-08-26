# Replacement Paper 15 deterministic-control design amendment v1

Status: **FROZEN AMENDMENT CANDIDATE — M1--M3 CLOSED BY DESIGN / INDEPENDENT EXACT-BYTE RE-REVIEW REQUIRED**  
Version: `P15R-CONTROLS-AMENDMENT-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Amendment self-audit: **C0/M0/m0 against the three remanded findings**  
Control implementation or execution performed here: **no**  
Universal prime recovery: **OPEN_NOT_AUTHORIZED**  
Route B: **false**

## Material Passport

- Origin Skill: ARS experiment-agent, reproducibility and integrity protocols,
  plus academic-paper-reviewer methodology, domain, and devil's-advocate roles
- Origin Mode: plan / deterministic exact-arithmetic control-design amendment
- Origin Date: 2026-08-16
- Verification Status: UNVERIFIED_PENDING_INDEPENDENT_REREVIEW
- Version Label: `p15r_control_design_amendment_v1`
- Scope: the three causal/immutability/lifecycle acceptance surfaces M1--M3
  only; no generator, verifier, test, result, theorem, Route, manuscript, or
  release claim

## 1. Exact authority and effective-design rule

This amendment binds the complete final bytes of the only three records that
authorize it:

| Authority | Package-relative path | Lines | Bytes | SHA-256 |
|---|---|---:|---:|---|
| frozen base design | `notes/phase2_control_design_lock.md` | 1183 | 62887 | `db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d` |
| independent design review | `notes/phase2_control_design_peer_review.md` | 488 | 22894 | `3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec` |
| remediation gate | `notes/phase2_control_design_remediation_gate.md` | 188 | 7023 | `98f2fe2aabe20a41ba540adaad8061c92f3fc7f1bef5b296f5eaea3df01bae16` |

All three were read completely and re-hashed before this amendment was
written.  The effective design is the base design at the displayed digest,
with only the clauses explicitly marked **SUPERSEDES** below replaced.  An
omitted base clause remains binding byte-for-byte and semantically.  This
amendment does not embed its own digest.

The sole supersessions are:

1. base Sections 5 and 7 are strengthened by Sections 3--7 below for semantic
   negative construction and causality;
2. the byte-only verify-only snapshot language in base Section 12 is replaced
   by Section 8 below;
3. the generation-root authorization, test-only injection registry, and
   external-lock/trap clauses of base Section 12 are replaced by Sections
   9--11 below.

No other generated-row value, registered negative row, method name,
registered S/P detector, path, artifact, binding, owner, theorem ceiling, or
lifecycle edge changes.
This amendment is not a fifteenth authority binding or a new manifest node.
The mandatory append-only closure addendum will bind this amendment's
external digest; the unchanged manifest `design_review` binding then
authenticates that effective-design receipt transitively without a new edge.

## 2. Frozen invariants retained without reinterpretation

The following values remain exact:

```text
DESIGN_SCHEMA=paper15r-wieferich-ulm-controls/1
MANIFEST_SCHEMA=paper15r-wieferich-ulm-controls-manifest/1
CSV_ARTIFACTS=8
GENERATED_ARTIFACTS_INCLUDING_MANIFEST=9
CSV_BODY_ROWS=120
EXPLICIT_NEGATIVE_ROWS=35
SEMANTIC_MUTATION_CLASSES=35
PACKAGE_MUTATION_CLASSES=28
UNITTEST_METHODS=173
AUTHORITY_BINDINGS=14
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
TOLERANCE_POLICY=EXACT_ZERO
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
ROUTE_B_AUTHORIZED=false
MANIFEST_SELF_HASH=false
MANIFEST_FUTURE_RESULT_EDGE=false
CONCURRENT_PROOF_HASH_CYCLE=false
```

The eight CSV paths, their headers and order, the nine generated paths, the
six implementation paths, all `VC/EO/FK/TC/SG/OF/PC/TS` row values and order,
all `S01..S35` and `P01..P28` method names and detector tokens, the fourteen
authority paths, the sixteen manifest aggregate keys, and the exact DAG

```text
A -> D -> R -> G -> I -> C -> M -> V
```

with its base-design additional bindings remain unchanged.  Mutation-only
roots and operational receipts introduced below are neither generated
artifacts nor manifest nodes.

## 3. M1 global causal-negative protocol — SUPERSEDES the weaker test sequence

### 3.1 Terms and forbidden inputs

A **primitive seed** is the typed field map printed in Sections 5--7.  It is
constructed from those literals, not copied from a negative CSV row and not
selected by a negative `row_id`.  `P_i` is the closed predicate named in the
same registry row.  `Delta_i` and `Delta_i^-1` are the sole forward and inverse
operators for method `S_i`.

“Valid seed” means a complete, canonically serialized input to that one
class-specific `P_i`: every allowlisted predicate field is present, typed,
and accepted.  It is method-owned and is not an additional package body row;
nonprojection cells are empty and cannot supply acceptance.  The ordinary
positive-row families retain responsibility for full package-row coverage.

The semantic decision projection excludes, at minimum, this common set:

```text
schema_version
row_id
mutation_id
case_kind
negative_reason
oracle
status
the method's expected detector
every persisted PASS/rejection receipt
```

It additionally excludes the following schema-specific receipt/tag fields:

```text
VC: scope_ceiling, tolerance
EO: witness_kind, scope_ceiling
FK: model_kind, kernel_order, height_orders_d0_to_N,
    tail_order, phi_of_root, root_in_kernel, scope_ceiling
TC: model_kind, finite_model_id, discrete_tail_order,
    compact_quotient_order, statement_scope
SG: row_kind, scope_ceiling
OF: row_kind, claim_under_test
PC: record_kind, binding_path, binding_sha256,
    claim_class, allowed_state
```

Excluded values may be parsed for ordinary schema validation, but they are
not passed to `P_i`, cannot select a predicate, cannot select a detector, and
cannot change accept/reject.  In particular, `claim_under_test` on
`OF-007..015` duplicates the registered reason vocabulary and is deliberately
non-causal; the typed source/target owner transition is causal.  The
`prohibited_promotion` field on `PC-018..026` is causal only after the grammar
in Section 4.6 has parsed it into a typed assertion; its string is never used
as a reason-token or detector lookup key.

### 3.2 Exact chain run by every one of the existing 35 methods

Each existing Section-7 method, with no additional `test_*` method, performs
these steps in order:

1. Construct `s_i` from the registry's primitive literals.  Embed it by the
   same exact-header rule used in step 3, freeze its canonical seed bytes,
   independently reparse it, type-check every scalar/vector/operator, and
   require `P_i(s_i)=ACCEPT`.  Failure here is `E_INVALID_SEED` and stops;
   the expected semantic detector is not consulted.
2. Apply `Delta_i` exactly once.  Compare the before/after typed maps and
   require the changed-field set to equal the registry's `changes={...}` set.
   No second write or normalization is permitted.  For S02/S03 only, changing
   a normalization rule and recomputing its dependent `kappa` is one declared
   atomic operator with the exact two-field footprint shown below.
3. Embed the post-image into the existing artifact's exact header.  Set
   `schema_version` to the frozen literal
   `paper15r-wieferich-ulm-controls/1`, set the allowlisted predicate fields
   from the registry map, and set every other header field empty.  Serialize
   one header plus one body row by the base Section-4 CSV byte contract.  A
   separately implemented parser reads those bytes back; it shares no
   serializer helper, predicate helper, or generator object.
4. Project only the registry's allowlisted typed fields.  Independently parse
   the registered persisted negative row, erase every excluded field, and
   require its typed projection to equal the post-image projection.  `row_id`
   may locate this audit receipt only after the post-image exists; it is never
   read by `P_i` and never indexes a detector.
5. Require `P_i(post_i)=REJECT(f_i)`.  Only after this rejection may the
   method-owned registry translate the typed failure `f_i` to the frozen
   detector and compare it with the required detector.  A detector emitted
   before a rejection is `E_PREMATURE_DETECTOR` and fails the method.
6. Apply the printed `Delta_i^-1`, serialize and independently reparse again,
   require exact typed equality with `s_i`, and require
   `P_i(s_i)=ACCEPT`.  Merely suppressing the detector is not acceptance.
7. Repeat the decision with `row_id` blank and changed, with `case_kind` set
   successively to empty, `DIAGNOSTIC`, `RECEIPT`, and `NEGATIVE`, and with
   every expected/receipt field blank, wrong, or swapped.  The rejected
   post-image must remain rejected and the inverse seed must remain accepted.

Thus a branch of the form `if case_kind == NEGATIVE` or a map keyed by
`row_id`, reason, expected detector, oracle, or persisted status fails the
same registered method.  The detector registry is an assertion about the
already-caused failure, never evidence for it.

### 3.3 Canonical inverse receipt

For every S-row below, `Delta^-1` means the exact replacement printed after
`inverse:`.  The method records in memory only:

```text
seed canonical bytes
post-image canonical bytes
recovered canonical bytes
typed failure enum
```

It requires recovered bytes to equal seed bytes byte-for-byte.  These bytes
are method-owned temporary data, are never written under `code/`,
`experiments/`, or `results/`, and never enter the manifest.

## 4. Closed typed predicate definitions

### 4.1 Valuation predicates

`VC_DOMAIN(p,r,branch)` accepts exactly:

```text
branch=DIAGONAL                 iff p=r
branch=ODD_OFF_LOCAL            iff p!=r and r is odd
branch=TWO_OFF_LOCAL            iff p!=2 and r=2
```

No other branch symbol is in the grammar.  `VC_ODD` independently computes
`v=v_r(p^(r-1)-1)` by repeated division and accepts exactly
`raw_valuation=v`, `normalization_subtrahend=1`, and `kappa=v-1`.
`VC_TWO` independently computes `v=v_2(p^2-1)` and accepts exactly
`raw_valuation=v`, subtrahend `3`, and `kappa=v-3`.  `VC_SIGN` accepts an
empty sign off the quadratic branch and, on it, `1` for `p mod 4=1` or `-1`
for `p mod 4=3`.

### 4.2 Order predicates

`EO_BOUNDED` factors `ell-1`, independently minimizes the multiplicative
order, enumerates all characters of `C_16` of order at most eight, restricts
them to the specified `C_8`, and obtains an image of order four.  Its typed
claim grammar is

```text
BOUNDED_ORDER_RESTRICTION_<NOT_SURJECTIVE|SURJECTIVE>
```

and only `NOT_SURJECTIVE` agrees with that enumeration.

`EO_EXACT` recomputes the full order and both valuations.  Its claim grammar
is

```text
DIVISIBILITY_<DOES_NOT_IMPLY|IMPLIES>_EXACT_DEPTH_M
```

`IMPLIES` is accepted only when both independently computed valuations equal
`m`; divisibility alone is never sufficient.

### 4.3 Finite-root predicate

`FK_ROOT` parses the exponent and numerator vectors, enumerates the exact
finite source group, reduces every coordinate modulo its `r^e_i`, and
independently computes both

```text
r^depth * root_vector = tail_vector
Phi(root_vector) = 0 mod r^target_exponent.
```

Both equalities are required.  The stored `phi_of_root` and
`root_in_kernel` receipts are not read.

### 4.4 Torsion/type predicates

`TC_CLOSURE` uses a recursive-descent parser with tokens
`ann`, `closure`, `Tor`, `r^omega`, `DISCRETE_K`, and `COMPACT_B`, balanced
parentheses, and one typed equality.  It accepts only

```text
ann(closure(Tor(COMPACT_B))) = r^omega(DISCRETE_K)
```

with annihilator direction compact subgroup to discrete subgroup.  Raw
`Tor(COMPACT_B)` does not satisfy the operand type.

`TC_FINITE` parses exactly

```text
FINITE_MODEL_<DOES_NOT_PROVE|PROVES>_INFINITE_COMPACT_THEOREM
```

into `{source_scope=FINITE_MODEL, polarity, target_scope=INFINITE_COMPACT}`.
The finite-model authority permits only `DOES_NOT_PROVE`.

`TC_OWNER` parses both sides of the equality in Section 4.4 and accepts the
correct annihilator identity in either serialized equality order.  Removing
`ann(...)` changes one side from a discrete annihilator subgroup to a compact
torsion-closure subgroup; direct equality with `r^omega(DISCRETE_K)` is
therefore rejected without consulting a row token.

### 4.5 Signature predicates

`SG_SCOPE` recomputes every supplied prefix from primitive `(p,r)` values,
classifies evidence as `FINITE_COLLISION`, `FINITE_PAIR_SEPARATION`,
`FINITE_RANGE`, or `NO_INFINITE_EVIDENCE`, and parses conclusions into a
typed scope and quantifier.  The exact grammatical forms used here are:

```text
NO_GLOBAL_CONCLUSION
B_<prime>_ISOMORPHIC_B_<prime>
r=<prime>;B_<prime>_NOT_ISOMORPHIC_B_<prime>
UNIVERSAL_RECOVER_P
FINITE_RANGE_ONLY
SIGNATURE_MAP_GLOBALLY_INJECTIVE
OPEN_NOT_AUTHORIZED
SIGNATURE_MAP_KNOWN_INJECTIVE
```

A finite collision licenses only `NO_GLOBAL_CONCLUSION`; a finite pair
separation licenses only that pair statement; a finite range licenses only
`FINITE_RANGE_ONLY`; and absent infinite evidence licenses only
`OPEN_NOT_AUTHORIZED`.  Global or universal quantifiers are not inferred.
For S16 specifically, the exact `[2;3;5;7;11;13]` vector is both the frozen
coordinate prefix and the row's six-prime tested registry; `SG_SCOPE`
recomputes the full six-by-six finite matrix and still classifies only
`FINITE_RANGE`.

### 4.6 Owner and proof-ceiling predicates

`OF_OWNER` treats every owner spelling as a nominal enum, not a substring.
For these nine method-owned packets the operation is the typed constant
`COPY_RECORD_WITHOUT_LICENSE` and no morphism/capability receipt is present.
An identity transition `source_owner=target_owner` is accepted.  A transition
between distinct nominal owners is rejected.  The predicate therefore does
not read the duplicated `claim_under_test` reason string.  Its typed failure
contains the exact source-owner capability and target-owner requirement
(label support, ambient marker, actual topology, flow, Haar, measure, trace,
operator, or determinant); detector selection follows that typed pair only
after rejection.

`PC_CEILING` lexes, then parses, one of two grammars:

```text
<target>_<NONPROMOTION|PROMOTION>
<source>_<NOT_AS|AS>_<target>
```

where the typed vocabularies are

```text
target = GRH | DENSITY | ABSOLUTE_PRIORITY | ROUTE_B |
         UNIVERSAL_RECOVERY | SYMBOLIC_PROOF | EXECUTED_THEOREM |
         CHEBOTAREV_PROOF | ULM_PROOF
source = FINITE_CONTROL | SOURCE_RECEIPT
```

The parser splits only at the reserved full delimiters `_NONPROMOTION`,
`_PROMOTION`, `_NOT_AS_`, and `_AS_`; it does not search for a reason
substring and does not consult the S-registry.  The authority state is the
typed table

```text
GRH assumption                    NOT_AUTHORIZED
density from finite witnesses     NOT_AUTHORIZED
absolute priority from search     NOT_AUTHORIZED
Route B                           false
universal recovery                OPEN_NOT_AUTHORIZED
finite control -> symbolic proof  false
source receipt -> executed theorem false
finite control -> Chebotarev proof false
finite control -> Ulm proof       false
```

`NONPROMOTION` and `NOT_AS` agree with this table and are accepted;
`PROMOTION` and `AS` contradict it and are rejected.  The failure enum is
derived from the typed source/target pair.  The original lexical token is
not a detector or a reason receipt.

## 5. Complete arithmetic causal registry S01--S10

Notation: maps contain only predicate inputs; vector and scalar spellings are
the base canonical spellings.  The compact aliases are
`N=target_exponent`, `tail=tail_vector`, `root=root_vector`,
`source=source_owner`, `target=target_owner`, `claim=claim_under_test`,
`kp=kappa_prefix_p`, `kq=kappa_prefix_q`, and
`conclusion=authorized_conclusion`.  `post` is also the projection that must
be obtained from the registered negative row after all excluded fields are
erased.

| ID / persisted receipt | Primitive valid seed | Sole substantive mutation and exact post-image | Predicate / inverse / detector |
|---|---|---|---|
| `S01` / `VC-013` | `{p=3,r=3,branch=DIAGONAL}` | `Delta=change branch DIAGONAL -> ODD_OFF_LOCAL_INVALID`; `changes={branch}`; post `{p=3,r=3,branch=ODD_OFF_LOCAL_INVALID}` | `VC_DOMAIN`; inverse `branch=DIAGONAL`; `E_BRANCH_DOMAIN` |
| `S02` / `VC-014` | `{p=7,r=5,branch=ODD_OFF_LOCAL,raw_valuation=2,normalization_subtrahend=1,kappa=1}` | atomic `Delta=replace odd normalizer -1 by -0 and recompute dependent kappa`; `changes={normalization_subtrahend,kappa}`; post `{p=7,r=5,branch=ODD_OFF_LOCAL,raw_valuation=2,normalization_subtrahend=0,kappa=2}` | `VC_ODD`; inverse exact `subtrahend=1,kappa=1`; `E_NORMALIZATION_ODD` |
| `S03` / `VC-015` | `{p=7,r=2,branch=TWO_OFF_LOCAL,raw_valuation=4,normalization_subtrahend=3,kappa=1}` | atomic `Delta=replace quadratic normalizer -3 by -2 and recompute dependent kappa`; `changes={normalization_subtrahend,kappa}`; post `{p=7,r=2,branch=TWO_OFF_LOCAL,raw_valuation=4,normalization_subtrahend=2,kappa=2}` | `VC_TWO`; inverse exact `subtrahend=3,kappa=1`; `E_NORMALIZATION_TWO` |
| `S04` / `VC-016` | `{p=3,r=2,branch=TWO_OFF_LOCAL,principal_sign=-1}` | `Delta=erase sign -1 -> empty`; `changes={principal_sign}` | `VC_SIGN`; inverse `principal_sign=-1`; `E_TWO_SIGN` |
| `S05` / `EO-013` | `{p=2,r=2,m=3,ell=17,claim=BOUNDED_ORDER_RESTRICTION_NOT_SURJECTIVE}` | `Delta=claim NOT_SURJECTIVE -> SURJECTIVE`; `changes={claim_under_test}` | `EO_BOUNDED`; inverse exact `...NOT_SURJECTIVE`; `E_BOUNDED_EXTENSION` |
| `S06` / `EO-014` | `{p=2,r=3,m=1,ell=19,claim=DIVISIBILITY_DOES_NOT_IMPLY_EXACT_DEPTH_M}` | `Delta=polarity DOES_NOT_IMPLY -> IMPLIES`; `changes={claim_under_test}` | `EO_EXACT`; inverse exact `...DOES_NOT_IMPLY...`; `E_EXACT_DOUBLE_VALUATION` |
| `S07` / `FK-015` | `{r=2,N=3,kappa=1,source_exponents=[1;2;3;4],image_numerators=[4;2;1;1],depth=1,tail=[0;0;0;8],root=[1;0;0;4]}` | `Delta=erase the away correction in coordinate 1`; `changes={root_vector}`; post root `[0;0;0;4]` | `FK_ROOT`; inverse root `[1;0;0;4]`; `E_ROOT_NOT_IN_KERNEL` |
| `S08` / `FK-016` | `{r=2,N=3,kappa=2,source_exponents=[1;2;3;5],image_numerators=[4;2;1;1],depth=2,tail=[0;0;0;8],root=[0;3;0;2]}` | `Delta=erase the away correction in coordinate 2`; `changes={root_vector}`; post root `[0;0;0;2]` | `FK_ROOT`; inverse root `[0;3;0;2]`; `E_ROOT_NOT_IN_KERNEL` |
| `S09` / `FK-017` | `{r=3,N=2,kappa=1,source_exponents=[1;2;3],image_numerators=[3;1;1],depth=1,tail=[0;0;9],root=[2;0;3]}` | `Delta=erase the away correction in coordinate 1`; `changes={root_vector}`; post root `[0;0;3]` | `FK_ROOT`; inverse root `[2;0;3]`; `E_ROOT_NOT_IN_KERNEL` |
| `S10` / `FK-018` | `{r=3,N=2,kappa=2,source_exponents=[1;2;4],image_numerators=[3;1;1],depth=2,tail=[0;0;9],root=[0;8;1]}` | `Delta=erase the away correction in coordinate 2`; `changes={root_vector}`; post root `[0;0;1]` | `FK_ROOT`; inverse root `[0;8;1]`; `E_ROOT_NOT_IN_KERNEL` |

The S07--S10 predicate recomputes the four post-image values
`Phi(root)=4,2,3,1`; it never consumes those persisted answers.

## 6. Complete type, signature, and owner causal registry S11--S26

| ID / persisted receipt | Primitive valid seed | Sole substantive mutation and exact post-image | Predicate / inverse / detector |
|---|---|---|---|
| `S11` / `TC-008` | `{source=COMPACT_B,operation=ann(closure(Tor(COMPACT_B)))=r^omega(DISCRETE_K),target=DISCRETE_K}` | `Delta=replace the typed operand closure(Tor(COMPACT_B)) by Tor(COMPACT_B)`; `changes={operation}`; post `ann(Tor(COMPACT_B))=r^omega(DISCRETE_K)` | `TC_CLOSURE`; inverse restores exact `closure(...)`; `E_CLOSURE_REQUIRED` |
| `S12` / `TC-009` | `{source=FINITE_COMPACT_DUAL_MODEL,operation=FINITE_MODEL_DOES_NOT_PROVE_INFINITE_COMPACT_THEOREM,target=COMPACT_B}` | `Delta=flip typed polarity DOES_NOT_PROVE -> PROVES`; `changes={operation}`; post exact `FINITE_MODEL_PROVES_INFINITE_COMPACT_THEOREM` | `TC_FINITE`; inverse restores `DOES_NOT_PROVE`; `E_FINITE_MODEL_CEILING` |
| `S13` / `TC-010` | `{source=DISCRETE_K,operation=r^omega(DISCRETE_K)=ann(closure(Tor(COMPACT_B))),target=COMPACT_B}` | `Delta=remove outer ann operator from the right AST`; `changes={operation}`; post exact `r^omega(DISCRETE_K)=closure(Tor(COMPACT_B))` | `TC_OWNER`; inverse restores exact `r^omega(DISCRETE_K)=ann(closure(Tor(COMPACT_B)))`; `E_OWNER_TYPE` |
| `S14` / `SG-009` | `{p=2,q=5,prime_prefix=[2;3;5;7;11;13],kp=[0;0;0;0;0;0],kq=[0;0;0;0;0;0],distinguishing_prime=empty,conclusion=NO_GLOBAL_CONCLUSION}` | `Delta=conclusion -> B_2_ISOMORPHIC_B_5`; `changes={authorized_conclusion}` | `SG_SCOPE(FINITE_COLLISION)`; inverse `NO_GLOBAL_CONCLUSION`; `E_PREFIX_NONPROMOTION` |
| `S15` / `SG-010` | `{p=2,q=3,prime_prefix=[2;3;5;7;11;13],kp=[0;0;0;0;0;0],kq=[0;0;0;0;1;0],distinguishing_prime=11,conclusion=r=11;B_2_NOT_ISOMORPHIC_B_3}` | `Delta=conclusion -> UNIVERSAL_RECOVER_P`; `changes={authorized_conclusion}` | `SG_SCOPE(FINITE_PAIR_SEPARATION)`; inverse exact pair conclusion; `E_RECOVERY_CEILING` |
| `S16` / `SG-011` | `{prime_prefix=[2;3;5;7;11;13],conclusion=FINITE_RANGE_ONLY}` | `Delta=conclusion -> SIGNATURE_MAP_GLOBALLY_INJECTIVE`; `changes={authorized_conclusion}` | `SG_SCOPE(FINITE_RANGE)`; inverse `FINITE_RANGE_ONLY`; `E_RANGE_NONPROMOTION` |
| `S17` / `SG-012` | `{prime_prefix=empty,conclusion=OPEN_NOT_AUTHORIZED}` | `Delta=conclusion -> SIGNATURE_MAP_KNOWN_INJECTIVE`; `changes={authorized_conclusion}` | `SG_SCOPE(NO_INFINITE_EVIDENCE)`; inverse `OPEN_NOT_AUTHORIZED`; `E_OPEN_PROBLEM` |
| `S18` / `OF-007` | `{source=MARKED_EXACT_SEQUENCE,target=MARKED_EXACT_SEQUENCE}` | `Delta=target -> BARE_COMPACT_QUOTIENT`; `changes={target_owner}` | `OF_OWNER`; inverse target=source; `E_OWNER_SPLICE` |
| `S19` / `OF-008` | `{source=AMBIENT_U_P,target=AMBIENT_U_P}` | `Delta=target -> BARE_COMPACT_QUOTIENT`; `changes={target_owner}` | `OF_OWNER`; inverse target=source; `E_AMBIENT_IMPORT` |
| `S20` / `OF-009` | `{source=ACTUAL_PACKET_Q_P,target=ACTUAL_PACKET_Q_P}` | `Delta=target -> BARE_COMPACT_QUOTIENT`; `changes={target_owner}` | `OF_OWNER`; inverse target=source; `E_ACTUAL_IMPORT` |
| `S21` / `OF-010` | `{source=STANDARDIZED_FLOW,target=STANDARDIZED_FLOW}` | `Delta=target -> BARE_COMPACT_QUOTIENT`; `changes={target_owner}` | `OF_OWNER`; inverse target=source; `E_FLOW_IMPORT` |
| `S22` / `OF-011` | `{source=BARE_COMPACT_QUOTIENT,target=BARE_COMPACT_QUOTIENT}` | `Delta=target -> HAAR_OWNER`; `changes={target_owner}` | `OF_OWNER`; inverse target=source; `E_HAAR_PROMOTION` |
| `S23` / `OF-012` | `{source=BARE_COMPACT_QUOTIENT,target=BARE_COMPACT_QUOTIENT}` | `Delta=target -> MEASURED_OWNER`; `changes={target_owner}` | `OF_OWNER`; inverse target=source; `E_MEASURE_PROMOTION` |
| `S24` / `OF-013` | `{source=BARE_COMPACT_QUOTIENT,target=BARE_COMPACT_QUOTIENT}` | `Delta=target -> TRACE_OWNER`; `changes={target_owner}` | `OF_OWNER`; inverse target=source; `E_TRACE_PROMOTION` |
| `S25` / `OF-014` | `{source=BARE_COMPACT_QUOTIENT,target=BARE_COMPACT_QUOTIENT}` | `Delta=target -> OPERATOR_OWNER`; `changes={target_owner}` | `OF_OWNER`; inverse target=source; `E_OPERATOR_PROMOTION` |
| `S26` / `OF-015` | `{source=BARE_COMPACT_QUOTIENT,target=BARE_COMPACT_QUOTIENT}` | `Delta=target -> DETERMINANT_OWNER`; `changes={target_owner}` | `OF_OWNER`; inverse target=source; `E_DETERMINANT_PROMOTION` |

## 7. Complete proof-ceiling causal registry S27--S35

Every seed and post-image below is parsed by `PC_CEILING`; no entry is
recognized by an S-number, negative-row membership, reason-token map, or
substring detector.

| ID / persisted receipt | Primitive valid seed token | Sole substantive mutation and exact post-image token | Inverse / detector |
|---|---|---|---|
| `S27` / `PC-018` | `GRH_NONPROMOTION` | flip parsed polarity; `changes={prohibited_promotion}`; `GRH_PROMOTION` | inverse restores `GRH_NONPROMOTION`; `E_GRH` |
| `S28` / `PC-019` | `DENSITY_NONPROMOTION` | flip parsed polarity; `changes={prohibited_promotion}`; `DENSITY_PROMOTION` | inverse restores `DENSITY_NONPROMOTION`; `E_DENSITY` |
| `S29` / `PC-020` | `ABSOLUTE_PRIORITY_NONPROMOTION` | flip parsed polarity; `changes={prohibited_promotion}`; `ABSOLUTE_PRIORITY_PROMOTION` | inverse restores `ABSOLUTE_PRIORITY_NONPROMOTION`; `E_PRIORITY` |
| `S30` / `PC-021` | `ROUTE_B_NONPROMOTION` | flip parsed polarity; `changes={prohibited_promotion}`; `ROUTE_B_PROMOTION` | inverse restores `ROUTE_B_NONPROMOTION`; `E_ROUTE_B` |
| `S31` / `PC-022` | `UNIVERSAL_RECOVERY_NONPROMOTION` | flip parsed polarity; `changes={prohibited_promotion}`; `UNIVERSAL_RECOVERY_PROMOTION` | inverse restores `UNIVERSAL_RECOVERY_NONPROMOTION`; `E_RECOVERY_CEILING` |
| `S32` / `PC-023` | `FINITE_CONTROL_NOT_AS_SYMBOLIC_PROOF` | flip parsed relation `NOT_AS -> AS`; `changes={prohibited_promotion}`; `FINITE_CONTROL_AS_SYMBOLIC_PROOF` | restore `NOT_AS`; `E_PROOF_CEILING` |
| `S33` / `PC-024` | `SOURCE_RECEIPT_NOT_AS_EXECUTED_THEOREM` | flip parsed relation `NOT_AS -> AS`; `changes={prohibited_promotion}`; `SOURCE_RECEIPT_AS_EXECUTED_THEOREM` | restore `NOT_AS`; `E_SOURCE_RECEIPT_CEILING` |
| `S34` / `PC-025` | `FINITE_CONTROL_NOT_AS_CHEBOTAREV_PROOF` | flip parsed relation `NOT_AS -> AS`; `changes={prohibited_promotion}`; `FINITE_CONTROL_AS_CHEBOTAREV_PROOF` | restore `NOT_AS`; `E_CHEBOTAREV_CEILING` |
| `S35` / `PC-026` | `FINITE_CONTROL_NOT_AS_ULM_PROOF` | flip parsed relation `NOT_AS -> AS`; `changes={prohibited_promotion}`; `FINITE_CONTROL_AS_ULM_PROOF` | restore `NOT_AS`; `E_ULM_CEILING` |

This completes a 35-of-35 valid-seed, single-mutation, canonical-reparse,
typed-rejection, detector-after-rejection, inverse-accept registry.  There
remain exactly 35 semantic rows and exactly the same 35 semantic methods.

## 8. M2 recursive verify-only state receipt — SUPERSEDES byte-only snapshots

### 8.1 Receipt domain and record

Every valid or malformed `--verify-only` immutability check operates in a
method-owned synthetic repository `R` containing only the exact baseline
authority, lifecycle, implementation, and results files needed by that call.
Immediately before the call and immediately after it returns, regardless of
exit status, the independent test walks the whole `R` tree recursively with
`lstat`, beginning with `R` itself.  The root record's relative path is `.`;
descendants use `/` and are ordered by unsigned UTF-8 path bytes.

Each in-memory record is the exact tuple

```text
(relative_path,
 entry_type,
 mode,
 size,
 sha256_or_empty,
 mtime_ns,
 ctime_ns,
 st_nlink,
 st_dev,
 st_ino)
```

where `entry_type` is the closed enum `DIRECTORY` or `REGULAR` in a valid
baseline, `mode` is `stat.S_IMODE(st_mode)`, and SHA-256 is present only for
a regular file and covers its complete bytes.  A special, symlink, socket,
FIFO, or device entry is itself a receipt failure.  Access time is neither
recorded nor compared.  All integers are exact integers, not floats.

The before and after path sets and every tuple member must be identical.
Comparison includes the root `.` and all intermediate directories, not only
files the verifier happens to open.  Therefore a create/unlink changes the
parent directory receipt even when the final name set and all file bytes are
restored.  The receipt is retained in process memory only, is never placed
under the synthetic repository, never serialized in a CSV/manifest, and
never contains or reports `R`'s absolute path.  Diagnostics contain only a
relative path and field name; temporary basenames and outside paths are
forbidden.

This comparison is mandatory under uid 0.  Permission bits are not treated
as enforcement: mode, timestamps, identity, and inventory are observed
facts.  A valid verify-only call must return success and an identical
receipt.  A malformed verify-only call must return its semantic failure and
still have an identical receipt.  A receipt difference always adds
`E_VERIFY_ONLY_METADATA`; it is never masked by unchanged bytes or the
semantic detector.

The malformed fixture is exact: start from a valid isolated baseline, change
only `VC-001.kappa` from `0` to `1` with canonical CSV serialization, retain
the old manifest artifact digest, take the before receipt, and call ordinary
`--verify-only`.  It must reach the already frozen `E_ARTIFACT_SHA256` class,
perform no repair, and leave the complete malformed receipt identical.
`P01` still independently owns the package-mutation class; this reuse is only
the malformed immutability side of `test_rep_010`.

### 8.2 Existing-method falsifier

The existing method `test_rep_010` is assigned the single metadata-integrity
class; it is not renamed and no method is added.  It first proves equality on
one valid and one malformed verify-only call, then uses five serial fresh
baselines.  In each, bytes remain identical and exactly the stated
non-byte surface is changed between receipts:

| Variant | Exact falsifier | Required observation |
|---|---|---|
| mode | change one regular result file from mode `0444` to `0644` | `mode` differs; `E_VERIFY_ONLY_METADATA` |
| mtime | set that file's `mtime_ns` to its prior value plus exactly `1000000000`, without changing bytes | `mtime_ns` differs; `E_VERIFY_ONLY_METADATA` |
| ctime | change the same file `0444 -> 0644 -> 0444` while preserving bytes and restoring `mtime_ns` | final mode/size/hash/mtime match but `ctime_ns` differs; `E_VERIFY_ONLY_METADATA` |
| transient sidecar | create a zero-byte regular `p15r_transient_probe`, mode `0600`, directly under writable synthetic root `R`, then unlink it before the after walk | final inventory matches but the root `.` directory `mtime_ns` and/or `ctime_ns` differs; `E_VERIFY_ONLY_METADATA` |
| root | change only synthetic root `R` from mode `0700` to `0750` | the `.` record differs; `E_VERIFY_ONLY_METADATA` |

Each variant must first demonstrate that its selected receipt field actually
changed; an environment whose filesystem cannot expose the requested change
fails closed with `E_METADATA_RECEIPT_UNOBSERVABLE`, never PASS.  Cleanup is
method-owned and occurs only after the mismatching after-receipt is retained.
This one method therefore falsifies mode-only, timestamp-only, ctime-only,
transient-create/unlink, and omitted-root implementations without changing
the 173-method budget.

## 9. M3 generation-root capability — SUPERSEDES path-only authorization

### 9.1 Capability object

Every generation call now requires both the unchanged CLI
`--generate --output-dir ABSOLUTE_NEW_DIR` and one operational directory
capability.  The creator opens the already-created output directory using

```text
O_RDONLY | O_DIRECTORY | O_NOFOLLOW
```

and passes that open descriptor to the generator.  The exact environment
handoff is

```text
P15R_GENERATION_ROOT_FD=<base-ten inherited descriptor number>
P15R_GENERATION_PURPOSE=<purpose enum below>
P15R_GENERATION_UID=<newline-free base-ten id -u value>
P15R_GENERATION_DEV=<base-ten fstat(fd).st_dev>
P15R_GENERATION_INO=<base-ten fstat(fd).st_ino>
```

The held directory descriptor, together with the exact `uid/dev/ino/purpose`
receipt, is the capability token.  It is not a pathname capability and is
never serialized.  The descriptor is inherited explicitly: the shell
wrapper reserves descriptor 9 for a canonical call, while Python-owned
mutation methods use `pass_fds` for their method-owned descriptor.  No other
open descriptor is authority.

### 9.2 Creator and validation order

For canonical A/B the wrapper creates a distinct private parent using
`mktemp -d`, confirms by `lstat` that the parent and new child output root
are nonsymlink directories owned by the current uid with mode `0700`, opens
the child descriptor, and constructs the five-variable receipt from
`fstat`.  For a mutation root, the owning `test_package_*` method performs
the same steps inside its already required nonsymlink mode-`0700`,
current-uid private parent and sets `P15R_TEST_CONTEXT=1` in the generator
child only.  This context-with-`MUTATION_*`-capability combination is an
explicit generator-call authorization, not a wrapper injection mode; the
top-level wrapper still rejects `P15R_TEST_CONTEXT` unless one of Section
11's three exact injection modes owns it.

Before examining whether the root is empty, the generator performs exactly:

1. parse the unchanged CLI and reject missing/extra/repeated modes;
2. require all five capability variables and reject any extra
   `P15R_GENERATION_*` variable;
3. parse decimal fields canonically and `fstat` the descriptor without
   following a path;
4. require directory type, current-uid ownership, mode `0700`, and exact
   `uid/dev/ino` equality with the receipt;
5. `lstat` `--output-dir`, require it absolute, nonsymlink, owned by the same
   uid, mode `0700`, and the same device/inode as the open descriptor;
6. `lstat` its parent and require the private-parent ownership, nonsymlink,
   and mode contract;
7. validate the purpose and ordinary/test-context relationship;
8. enumerate through the held descriptor with `os.listdir(fd)` and
   `lstat(name, dir_fd=fd)`; only now classify nonemptiness; and
9. create every generated basename with descriptor-relative
   `O_CREAT|O_EXCL|O_NOFOLLOW` and write through the returned file descriptor.

After step 4, the generator never reopens the output directory by path and
never uses a path join for a generated write.  A rename/symlink substitution
of `--output-dir` therefore cannot redirect a write.  Capability failure is
`E_OUTPUT_CAPABILITY`; only an authorized but nonempty descriptor reaches
`E_NONEMPTY_OUTPUT`.

The exact purpose enum is:

```text
CANONICAL_A
CANONICAL_B
MUTATION_P(0[1-9]|1[0-9]|2[0-6])_V1
MUTATION_P27_V[1-5]
MUTATION_P28_V[1-2]
```

The last three lines are anchored Python `re.fullmatch` productions, not
literal parentheses or range shorthand in a serialized value.  They expand
to exactly P01--P26 variant 1, P27 variants 1--5, and P28 variants 1--2; no
other purpose is legal.

`CANONICAL_A/B` are legal only with `P15R_REPRO_ACTIVE=1` and without
`P15R_TEST_CONTEXT`; they are the exact two fresh generations.  Every
`MUTATION_*` purpose is legal only with `P15R_TEST_CONTEXT=1`, is owned and
destroyed by its named method, is never passed as `fresh-a` or `fresh-b`, is
never compared as one of the three canonical copies, and never increments a
manifest aggregate.  Canonical A/B are passed read-only to the suite and are
never repurposed as mutation roots.

The capability creator retains root ownership until its governing wrapper or
method exits.  It closes the generation descriptor after the generator child
returns and unsets all five `P15R_GENERATION_*` variables before another
call.  Canonical A/B remain available only for their frozen verification and
three-way comparisons; mutation roots remain only for their owning method.
On final success, any intervening failure, or handled signal, the governing
trap validates each root path against its saved device/inode, removes only
that validated root under the base temporary-root cleanup rule, and proves
the root and its private parent absent.  No capability file exists; the
descriptor and in-memory numeric receipt are the complete operational
artifact.

### 9.3 Exact P25 root

`test_package_p25_nonempty_generation_root` creates a fresh private parent
and child `out` under the mutation rules above, opens the child capability,
and sets purpose `MUTATION_P25_V1`.  It then creates through that descriptor
exactly one member:

```text
basename=occupied
entry_type=REGULAR
mode=0600
size=0
nlink=1
owner=current uid
```

There are no other child entries.  Capability validation steps 1--7 must
pass; step 8 observes `occupied` and emits exactly `E_NONEMPTY_OUTPUT`.
Outside-root rejection cannot mask it.  The method closes the descriptor,
unlinks only `occupied`, removes `out`, verifies both absent, and removes its
private parent.  No root, receipt, purpose, device, inode, or temporary name
is printed or serialized.

## 10. M3 ownership-token lock/trap/signal state machine — SUPERSEDES the ambiguous transition

### 10.1 Exact states and token

The lock path remains exactly
`/tmp/p15r-wieferich-ulm-controls-UID_DEC.lock`; UID validation and
concurrent exit class 74 remain unchanged.  The state variable is the closed
enum

```text
UNOWNED -> ACQUIRING -> OWNED -> CLEANING -> ABSENT
```

with `UNOWNED -> ABSENT` for a no-lock ordinary exit and
`ACQUIRING -> UNOWNED` when atomic `mkdir` reports a pre-existing lock.

The wrapper first initializes state `UNOWNED`, an empty candidate path, and
an empty token, and installs the exit and signal traps.  It then creates a
private candidate directory with one `candidate=$(mktemp -d ...)` shell
simple command; trap delivery is deferred until that assignment completes.
The handler treats a nonempty candidate variable as removable only after
`lstat` proves that it is the exact new nonsymlink, empty, mode-`0700`
directory owned by the current uid.  The wrapper validates those facts and
derives a 64-lowercase-hex ownership token as SHA-256 of the length-delimited
byte tuple

```text
P15R-LOCK-OWNER-v1, UID_DEC,
candidate st_dev, candidate st_ino, candidate basename
```

The `mktemp` uniqueness is operational isolation under the base rule; the
token is not fixture randomness.  The token is known to the cleanup handler
before the state changes to `ACQUIRING` and is never emitted.  An owned lock
contains exactly one regular file `.owner`, mode `0600`, nlink 1, current
uid, with bytes

```text
P15R-LOCK-OWNER-v1 <64-lowercase-hex-token>\n
```

This file is operational ownership metadata, not generated metadata.

### 10.2 Trap installation and race-free acquisition

The already installed exit trap and signal handlers remain armed before the
state changes to `ACQUIRING`.  The handled termination set is exactly
`HUP INT QUIT PIPE ALRM TERM USR1 USR2`; the ordinary exit trap is signal 0.
`KILL` and `STOP` are uncatchable by definition.  Job-control stop/continue
signals do not request exit and do not relinquish an owned lock.

One standard-library acquisition helper receives the already-known token
through a private inherited pipe.  It blocks the handled termination set for
the indivisible critical section:

1. call `mkdir` on the exact lock path with mode `0700`;
2. on `EEXIST`, create nothing, report `PREEXISTING` through the private
   pipe, and return;
3. on success, create `.owner` with
   `O_WRONLY|O_CREAT|O_EXCL|O_NOFOLLOW`, mode `0600`, write the exact token
   bytes, `fsync` the owner file and lock-directory descriptor, close them,
   and `lstat` both entries;
4. report only `{CREATED, lock_dev, lock_ino, owner_dev, owner_ino}` through
   the private pipe; and
5. unblock signals only after the token is durable in the directory.

The wrapper invokes the helper as one shell simple assignment to the private
receipt variable.  Trap dispatch is deferred until the helper exits and that
assignment is complete, so an ACQUIRING handler always sees exactly one of
empty-before-start, `PREEXISTING`, `CREATED`, or `E_CLEANUP`; it never guesses
from the lock path.  A pending handler processes `PREEXISTING` by changing to
`UNOWNED` before inspecting cleanup state, and processes `CREATED` by the
matching-token ACQUIRING rule below.

If any step after this helper's successful `mkdir` fails, the helper removes
only the `.owner` it created and its own just-created directory, verifies
absence, and reports `E_CLEANUP`.  The pipe is captured, never forwarded to
stdout/stderr, and carries no path or token.

While the helper runs the shell remains `ACQUIRING`.  A handled signal is
recorded as pending; shell trap delivery while waiting is deferred until the
helper completes.  Therefore every observable post-`mkdir` state is either
token-complete or already absent.  On `PREEXISTING`, the wrapper changes
`ACQUIRING -> UNOWNED`, touches no member of the pre-existing directory, and
returns the frozen concurrent-entry class 74.  On `CREATED`, the wrapper
independently `lstat`s the directory and `.owner`, compares the token bytes
and all returned inode receipts, then alone changes
`ACQUIRING -> OWNED`.  A pending signal before that assignment invokes the
ACQUIRING cleanup rule in Section 10.3; it cannot strand a token-complete
owned lock.

### 10.3 Ownership-checked cleanup

The exit handler is idempotent and branches only on state:

- `UNOWNED` or `ABSENT`: remove no lock path.
- `ACQUIRING`: if the lock path is absent, remove no lock; if present, remove
  the lock only if it is a nonsymlink current-uid directory containing
  exactly one nonsymlink current-uid mode-`0600` nlink-1 `.owner` whose
  complete bytes equal this process's token.  Otherwise remove nothing.
- `OWNED`: additionally require the stored lock and owner device/inode
  receipts to match, then change to `CLEANING`.
- `CLEANING`: unlink exactly `.owner` with no symlink following, `rmdir`
  exactly the validated lock directory, and require `lstat(lock_path)` to
  return `ENOENT`; only then change to `ABSENT`.

No recursive delete or glob is legal.  Unexpected contents, identity drift,
token mismatch, failed unlink/rmdir, or non-absence emits `E_CLEANUP`, leaves
unknown/foreign material untouched, and fails the run.  Explicit successful
cleanup uses this same handler before normal exit; the later exit-trap call
sees `ABSENT` and is a no-op.  Ordinary failure, P24's owned failure,
generator/test failure, and every handled termination signal use the same
path.  After cleanup a signal handler restores the default signal action and
terminates; it never skips the absence check.

On an `UNOWNED` exit after candidate creation, after the lock reaches
`ABSENT`, or when an `ACQUIRING` attempt finds no lock, the handler removes
only the exact validated empty candidate directory and requires its `lstat`
result to be `ENOENT`.  Candidate mismatch or residue is `E_CLEANUP`; no
broad temporary-parent removal is permitted.  Thus the token source itself
is covered before, during, and after acquisition on success, failure, and
handled signals.

A pre-existing lock is never removed: it cannot contain the fresh private
candidate token, and the `PREEXISTING` transition never enters `OWNED`.
Operational lock paths, tokens, candidate names, descriptors, devices,
inodes, and temporary roots are neither serialized nor printed.

## 11. Existing-method state-machine falsifiers and exact injection registry

`P24` remains the package-class owned-failure test: after fresh A is
generated and verified, its forced failure requires `OWNED -> CLEANING ->
ABSENT`, removes fresh A and the exact owned lock, and emits `E_CLEANUP` as
already frozen.

The existing `test_rep_009` is assigned the acquisition/signal-boundary
falsifier; it is not renamed and no method is added.  In a copied package
with the already frozen isolated lock basename `p15r-isolated.lock`, it runs
two serial fresh subfixtures:

1. inject `TERM` immediately after the helper's token-complete `CREATED`
   receipt but before the shell's `OWNED` assignment; the ACQUIRING handler
   must remove only the matching token, emit `E_SIGNAL_ACQUIRE`, and prove
   candidate, owner file, and lock absent; and
2. pre-create an isolated lock with a different well-formed token, attempt
   acquisition, and require exit class 74 with the foreign directory and
   every byte identical.

The helper's signal-blocked `mkdir`-through-token critical section has no
externally visible tokenless-owned state; subfixture 1 attacks its first
observable return boundary.  Parent snapshots before/after exclude only the
deliberately retained foreign-lock fixture until the method removes its own
fixture during final cleanup.

Accordingly, the test-only injection registry now has exactly three mutually
exclusive wrapper modes:

```text
P15R_TEST_CREATE_POST_CACHE=1
P15R_TEST_ABORT_AFTER_FRESH_A=1
P15R_TEST_SIGNAL_AFTER_LOCK_TOKEN=1
```

The third is legal only for `test_rep_009`; it causes the helper to notify
the parent with `TERM` only after writing the complete `CREATED` receipt to
the private pipe and before helper exit, hence before the shell can assign
`OWNED`.  The first two retain their exact P20/P24 timing.  All three require
`P15R_TEST_CONTEXT=1` and the base-validated isolated lock parent/path.  Any
pair or trio, any value other than literal `1`, use outside its owning
method, or any ordinary-run use is exit class 2.  Generation capability
variables from Section 9 are not test-injection variables and remain
mandatory for every generation call.

This assignment leaves exactly ten `test_rep_001..010` methods, 28 package
methods, and 173 total methods.

## 12. Effective reproduction order

The base Section-12 ten-step reproduction order remains in force with these
clarifications inserted, without changing the two-generation or three-copy
arithmetic:

1. install cleanup/signal traps and establish the race-free ownership-token
   lock before any project write;
2. take and compare the recursive Section-8 receipt around every isolated
   valid or malformed verify-only call;
3. create canonical A and B separately, passing `CANONICAL_A` then
   `CANONICAL_B` directory-descriptor capabilities;
4. keep mutation capabilities method-owned and disjoint from A/B;
5. run all base structural, semantic, byte-identity, and exact 173-method
   checks unchanged; and
6. use the ownership-checked cleanup state machine for success, failure,
   handled signal, P24, and the acquisition-boundary falsifier.

The generator, verifier, and wrapper still use no network, fixture
randomness, probabilistic algorithm, ambient repository scan, timestamp in
generated bytes, or tolerance.  No control is implemented or executed by
this amendment.

`E_INVALID_SEED`, `E_PREMATURE_DETECTOR`,
`E_VERIFY_ONLY_METADATA`, `E_METADATA_RECEIPT_UNOBSERVABLE`,
`E_OUTPUT_CAPABILITY`, and `E_SIGNAL_ACQUIRE` are fail-closed infrastructure
tokens inside the existing semantic/reproduction methods and generation
preflight.  They add no S-row, P-class, test method, CSV cell, manifest
aggregate, or promised package-mutation class.

## 13. M1--M3 closure self-audit and authorization stop

| Finding | Closure in this amendment | Count/path effect | Self-result |
|---|---|---|---|
| M1 semantic-negative causality | 35 complete primitive seed -> accept -> sole typed mutation -> canonical CSV reparse -> receipt-free projection -> closed predicate rejection -> post-rejection detector -> exact inverse -> acceptance chains; persisted negative projection tied after mutation | 35 rows, 35 methods, 173 total unchanged | CLOSED_BY_DESIGN |
| M2 verify-only metadata | whole-synthetic-repository recursive `lstat` receipt including `.`, directories, type/mode/size/hash/mtime/ctime/link/device/inode; valid and malformed calls; `test_rep_010` five serial falsifiers | no generated/schema/path/method change | CLOSED_BY_DESIGN |
| M3 root capability | held directory descriptor plus exact uid/dev/ino/purpose receipt; validation before emptiness; descriptor-relative writes; explicit P25 and mutation/canonical separation | P25 remains one of 28; A/B and three copies unchanged | CLOSED_BY_DESIGN |
| M3 lock/trap/signal | token known before ACQUIRING, token-complete signal-blocked helper, preinstalled traps, ownership-checked cleanup, final absence, foreign lock preservation, `test_rep_009` boundary falsifier | external operational state only; 173 unchanged | CLOSED_BY_DESIGN |

```text
P15R_CONTROL_DESIGN_AMENDMENT_V1=FROZEN_CANDIDATE
BASE_SHA256=db590ae254c0b4a2cd1b192023569a02906636202c234b5f296e18514205600d
REVIEW_SHA256=3e1805985f4e53ce0e47a5fbb0fcdb02c855c4a33c32bc4159667a4734be7eec
REMEDIATION_GATE_SHA256=98f2fe2aabe20a41ba540adaad8061c92f3fc7f1bef5b296f5eaea3df01bae16

M1_SEMANTIC_REGISTRY_ROWS=35
M1_VALID_SEEDS=35
M1_SINGLE_SUBSTANTIVE_MUTATIONS=35
M1_CANONICAL_REPARSES=35
M1_TYPED_REJECTIONS=35
M1_INVERSE_ACCEPTS=35
M1_ROW_ID_CAUSAL=false
M1_CASE_KIND_CAUSAL=false
M1_EXPECTED_FIELDS_CAUSAL=false

M2_RECEIPT_RECURSIVE=true
M2_ROOT_INCLUDED=true
M2_DIRECTORY_METADATA_INCLUDED=true
M2_VALID_AND_MALFORMED_CALLS=true
M2_UID0_BYTE_ONLY_ESCAPE=false
M2_FALSIFIER_METHOD=test_rep_010

M3_CAPABILITY=DIRECTORY_FD_PLUS_UID_DEV_INO_PURPOSE
M3_P25_AUTHORIZED_MUTATION_ROOT=true
M3_MUTATION_ROOTS_CANONICAL=false
M3_ACQUISITION_SIGNAL_RACE=false
M3_FOREIGN_LOCK_REMOVAL=false
M3_ACQUISITION_FALSIFIER_METHOD=test_rep_009

REMAND_SELF_AUDIT=C0_M0_m0
INDEPENDENT_REREVIEW_REQUIRED=true

CSV_ARTIFACTS=8
GENERATED_ARTIFACTS=9
CSV_BODY_ROWS=120
EXPLICIT_NEGATIVES=35
SEMANTIC_MUTATIONS=35
PACKAGE_MUTATIONS=28
UNITTEST_METHODS=173
AUTHORITY_BINDINGS=14
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
ROUTE_B_AUTHORIZED=false
MANIFEST_DAG_CHANGED=false

CONTROL_IMPLEMENTATION_AUTHORIZED=false
CONTROL_EXECUTION_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
FIGURE_WORK_AUTHORIZED=false
RELEASE_AUTHORIZED=false
ARCHIVE_AUTHORIZED=false
GIT_OPERATION_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
```

This self-audit is not the required independent re-review.  The exact
effective `base + amendment` tuple remains implementation-ineligible until a
separate reviewer appends the authorized closure addendum and reaches
`PASS C0/M0/m0` on its own recomputation.
