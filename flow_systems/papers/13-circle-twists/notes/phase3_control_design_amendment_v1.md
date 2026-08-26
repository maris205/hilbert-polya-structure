# Paper 13 Phase-3 control-design amendment v1 — exact-row closure

Status: **FROZEN AMENDMENT CANDIDATE / INDEPENDENT RE-LOCK REQUIRED**  
Version: **P13-CONTROLS-v1.0-AMENDMENT-v1**  
Date: **2026-08-15 (Asia/Shanghai)**  
Bounded design audit: **C0 / M0 / m0**  
Control implementation or execution performed here: **no**  
`route_b_invocation_allowed: false`

## Material Passport

- Origin Skill: ARS experiment-agent plus academic-pipeline integrity workflow
- Origin Mode: plan / bounded deterministic-control design repair
- Origin Date: 2026-08-15
- Verification Status: UNVERIFIED
- Version Label: `p13_control_design_amendment_v1`
- Scope: exact-row byte closure only; no theorem, proof, code, result, Route,
  manuscript, standalone, release, Git, or public-sync claim

## 1. Authority, precedence, and exact reviewed tuple

This amendment closes the sole Major in the final independent design review.
It does not modify or replace the original design bytes. On conflict, it
supersedes only the underdetermined field-value rules for
`action_period_nonretention_controls.csv`,
`negative_domain_controls.csv`,
`actual_standard_support_transfer_controls.csv`, and
`target_summary.csv`. Every other original rule remains binding.

| Artifact | SHA-256 | Receipt |
|---|---|---|
| `notes/phase3_control_design_lock.md` | `900c541713b1711bdab7fa0d264355b6d8ee27014094e60eac6aabe38190604c` | immutable base design |
| `notes/phase3_control_design_review.md` | `64ce1cd97e122d0fb197731d62dbf37b734d11b6b6b3ee11a97808335c632cd6` | final authoritative review, `C0/M1/m0` |

The final review withdraws any separate regex concern: the existing proof
sentinel and proof-binding policy are internally consistent. This amendment
therefore closes **M1 only** and does not rename or otherwise alter that
sentinel or policy.

## 2. Invariants preserved exactly

This amendment changes no header, schema, row order, row ID, row count,
negative count, tolerance, oracle token, test allocation, serialization rule,
implementation path, source/gate binding, or Route boundary. The inherited
targets remain:

```text
DESIGN_SCHEMA=paper13-circle-twists-controls/1
MANIFEST_SCHEMA=paper13-circle-twists-controls-manifest/1
HEADER_WIDTHS=17,20,20,19,23,26,28,20,12,21,11
CSV_ARTIFACTS=11
GENERATED_ARTIFACTS_INCLUDING_MANIFEST=12
CSV_BODY_ROWS=2548
EXPLICIT_NEGATIVE_ROWS=47
EXPECTED_NEGATIVES_DETECTED=47
NEGATIVE_FAILURES=0
UNITTEST_METHODS=128
UNITTEST_FAILURES=0
UNITTEST_ERRORS=0
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
TOLERANCE_POLICY=EXACT_ZERO
CONTROL_IMPLEMENTATION_AUTHORIZED=false
CONTROL_EXECUTION_PERFORMED=false
```

The global UTF-8/LF/`csv.writer` and canonical JSON rules in the base design
remain unchanged.

## 3. Exact AP values and independent derivations

This section completes every previously underdetermined value in the frozen
20-column `action_period_nonretention_controls.csv` header. The 14-case table,
`K24=(-6,-1,0,6)`, 56-row enumeration, and IDs `AP-0001`--`AP-0056` remain
unchanged.

### 3.1 Exact row index and inherited metadata

Let `c` be the one-based case ordinal in the base design's 14-row action
table, and let `j` be the one-based position of `k` in `K24`. Then

```text
n = 4*(c-1)+j,
row_id = "AP-" + n as four zero-padded decimal digits.
```

`action_case`, `component_id`, `stabilizer_literal`, and
`orbit_count_class` are copied from exactly row `c` of that immutable table;
`k_index` is `K24[j]`. No map, sort, or label inference may replace this
enumeration.

### 3.2 Closed literal value domain

For every AP row, the previously unspecified class/signature values are the
following exact literals:

```text
global_time_sample_class
  = TIME_QUADRATIC_GAUGE_CLASS_ZERO_SAMPLE

isotropy_restriction_sample_class
  = ISOTROPY_QUADRATIC_RESTRICTION_CLASS_ZERO_SAMPLE

test_algebra_sample_signature
  = TWISTED_TEST_GAUGE_STAR_TERM_CHECK_PASS

full_sample_signature
  = FULL_TRANSPORT_CHARACTER_PHASE_CHECK_PASS

reduced_sample_signature
  = REDUCED_TRANSPORT_INTERTWINER_CHECK_PASS
```

The remaining AP values are derived exactly as follows:

```text
dense_h_scope
  = FINITE_RATIONAL_WINDOW_DIAGNOSTIC_ONLY
      iff action_case == HETEROGENEOUS_ACTION
          and component_id == dense_component;
  = NOT_DENSE_H_CONTROL otherwise.

named_output_signature_matches_baseline = true
restriction_coboundary_match            = true
case_kind                                = DIAGNOSTIC
negative_reason                          = empty field
oracle                                   = QUADRATIC_RESTRICTION_SIGNATURE_DIAGNOSTIC
tolerance                                = 0
status                                   = PASS
```

The two booleans and five literal class/signature values must not be copied
blindly into output. They are serialized only after the independent exact
derivations below return true. A false derivation aborts generation; it does
not emit an alternative token or a `FAIL` row.

### 3.3 Independent exact derivations

All exponent comparisons are integer comparisons modulo 24 and are computed
from the input `k`, not read from another CSV.

Define `A_k(t)=-k*t^2` and `S_k(t,u)=2*k*t*u`. The five derivation predicates
are:

1. `TIME_CLASS_OK(k)`. Verify `A_k(0)=0` and, for every `(t,u)` in
   `T3^2`,

   ```text
   A_k(t)+A_k(u)-A_k(t+u)-S_k(t,u) == 0 mod 24.
   ```

   The global-time literal is emitted iff all 50 checks pass: one
   normalization check plus 49 pair checks.

2. `ISOTROPY_CLASS_OK(k)`. Independently compare coefficients in the
   integer polynomial ring `Z[k,x,y]`:

   ```text
   -k*x^2-k*y^2+k*(x+y)^2-2*k*x*y == 0.
   ```

   The coefficient vector in ordered monomials `(x^2,x*y,y^2)` must be
   exactly `(0,0,0)`. Because this is a formal identity, it restricts to the
   literal subgroup in every AP row, including `{0}`, `LZ`, `R`, and `Q`,
   without asserting a Haar or completion theorem on the dense subgroup.

3. `TEST_SIGNATURE_OK(k)`. Recompute from the base-design `C1,C2` fixtures,
   without reading the TC or TI ledgers:

   - for every support triple `(u,v,w)`, verify the cocycle exponent

     ```text
     S_k(u,v)+S_k(u+v,w)-S_k(v,w)-S_k(u,v+w) == 0 mod 24;
     ```

   - for every product support pair `(u,v)` with `t=u+v`, verify the
     termwise gauge-product exponent

     ```text
     A_k(t)+S_k(u,v)-A_k(u)-A_k(v) == 0 mod 24;
     ```

   - for every `t` in the fixture support and its reflected support, verify
     the gauge-star exponent

     ```text
     A_k(t)-S_k(t,-t)+A_k(-t) == 0 mod 24.
     ```

   The test-algebra literal is emitted iff every termwise check passes. This
   derivation is valid for all four `K24` values and requires no numerical
   evaluation of a 24th root.

4. `FULL_SIGNATURE_OK(k)`. For `m=(0,1)` define `C_m(t)=6*m*t`. On every
   `(t,u)` in `T3^2`, independently verify

   ```text
   C_m(t)+C_m(u)-C_m(t+u) == 0 mod 24.
   ```

   Set `B_km(t)=C_m(t)+A_k(t)` and, for every `t` in `T3`, verify

   ```text
   B_km(t)-A_k(t)-C_m(t) == 0 mod 24,
   C_m(t)+C_m(-t)        == 0 mod 24.
   ```

   The full-transport literal is emitted iff all character, choice-map, and
   modulus-one phase checks pass. It is a finite character-phase diagnostic,
   not a full-norm theorem.

5. `REDUCED_SIGNATURE_OK(k)`. Using `V1,V2`, `SHIFT^2`, and `TEVAL`, compare
   coefficient and exponent pairs independently for

   ```text
   S_k(s,t-s)+S_k(u,t-s-u)
     == S_k(s,u)+S_k(s+u,t-s-u) mod 24,

   A_k(t)+S_k(s,t-s)-A_k(t-s)
     == A_k(s) mod 24.
   ```

   A vector coefficient outside its finite support is exactly integer zero.
   The reduced-transport literal is emitted iff every projective-law and
   intertwiner matrix element agrees. It remains a finite matrix-element
   diagnostic.

Finally,

```text
restriction_coboundary_match = ISOTROPY_CLASS_OK(k)

named_output_signature_matches_baseline
  = TIME_CLASS_OK(k)
    and ISOTROPY_CLASS_OK(k)
    and TEST_SIGNATURE_OK(k)
    and FULL_SIGNATURE_OK(k)
    and REDUCED_SIGNATURE_OK(k).
```

This construction independently derives each AP signature from exact
identities and fixtures; it never treats the common expected token as its
own oracle.

## 4. Exact ND `violated_lock` and canonical fixture tokens

The 20-row order, header, reasons, expected detectors, dispositions, oracle,
tolerance, and count remain unchanged. The table below freezes the exact
ASCII value of both previously open fields. Each `fixture` is one field; its
semicolon-delimited `KEY=VALUE` clauses appear in the displayed order, with
no whitespace. None contains a comma, quote, CR, or LF.

| `row_id` | `negative_reason` | Exact `fixture` field | Exact `violated_lock` field |
|---|---|---|---|
| `ND-0001` | `NON_T0_COEFFICIENT_TARGET` | `DOM=INDISC2;COD=INDISC2;MAP=a:0|b:1` | `T0_TARGET_REQUIRED_FOR_TIME_FACTORIZATION` |
| `ND-0002` | `MEASURABLE_ONLY_PHASE` | `ALPHA_RULE=LE0_TO_1_GT0_TO_MINUS1;WITNESS=SEQ_1_OVER_N` | `COCHAINS_MUST_BE_GLOBALLY_CONTINUOUS` |
| `ND-0003` | `DISCONTINUOUS_PHASE` | `ALPHA_RULE=EQ0_TO_1_NE0_TO_MINUS1;WITNESS=SEQ_1_OVER_N` | `COCHAINS_MUST_BE_GLOBALLY_CONTINUOUS` |
| `ND-0004` | `UNNORMALIZED_ONE_COCHAIN` | `ALPHA_0=-1` | `ONE_COCHAIN_NORMALIZATION_ALPHA_0_EQ_1` |
| `ND-0005` | `UNNORMALIZED_TWO_COCHAIN` | `SIGMA_T_0=-1` | `TWO_COCHAIN_NORMALIZATION_BOTH_AXES_EQ_1` |
| `ND-0006` | `WRONG_COBOUNDARY_SIGN` | `K=-1;T=1;U=1;CANDIDATE=CONJUGATE_DELTA` | `COBOUNDARY_SIGN_DELTA_A_EQ_A_T_A_U_OVERLINE_A_TPLUSU` |
| `ND-0007` | `WRONG_GAUGE_ORIENTATION` | `K=-1;MAP=U_OVERLINE_ALPHA;TYPE=A_SIGMA_TO_A_ONE` | `GAUGE_DIRECTION_SIGMA_OVERLINE_TAU_EQ_DELTA_A` |
| `ND-0008` | `TWISTED_PRODUCT_WRONG_SIGMA_ARGUMENT` | `K=6;U=1;T=2;CANDIDATE=SIGMA_U_T` | `TWISTED_PRODUCT_KERNEL_SIGMA_U_TMINUSU` |
| `ND-0009` | `TWISTED_STAR_OMITS_COCYCLE` | `K=6;T=1;CANDIDATE=CONJ_F_MINUS_T` | `TWISTED_STAR_FACTOR_OVERLINE_SIGMA_T_MINUST` |
| `ND-0010` | `REGULAR_TRANSLATION_WRONG_DIRECTION` | `VECTOR=V1;S=1;T=0;CANDIDATE=XI_T_PLUS_S` | `LEFT_REGULAR_TRANSLATION_T_MINUS_S` |
| `ND-0011` | `INTERTWINER_CONJUGATIONS_SWAPPED` | `VECTOR=V2;K=6;S=1;T=0;CANDIDATE=M_BARALPHA_LAMBDA_SIGMA_M_ALPHA` | `INTERTWINER_M_ALPHA_LEFT_M_BARALPHA_RIGHT` |
| `ND-0012` | `R2_NONSYMMETRIC_COMMUTATOR` | `OMEGA=EXP_I_PI_S1_T2_OVER2;S=1|0;T=0|1;COMM_EXP_MOD4=1` | `P13_3_ONE_DIMENSIONAL_R_ONLY` |
| `ND-0013` | `DENSE_H_HAAR_COMPLETION_PROMOTION` | `H=Q;WINDOW=REDUCED_ABS_LE_2_DEN_LE_6;PROMOTION=HAAR_COMPLETION` | `DENSE_Q_NO_HAAR_OR_COMPLETION_PROMOTION` |
| `ND-0014` | `HETEROGENEOUS_AS_COMMON_LATTICE` | `STABILIZERS=ZERO|LZ|R|Q;CANDIDATE=COMMON_LZ` | `P13_8_COMMON_STABILIZER_H_EQ_LZ` |
| `ND-0015` | `ACTUAL_STANDARD_REVERSE_IDENTITY` | `MAP=IDENTITY;DIRECTION=G_ACTUAL_TO_G_STD;CLAIM=CONTINUOUS` | `J_DIRECTION_G_STD_TO_G_ACTUAL_ONLY` |
| `ND-0016` | `INFINITE_Q_FINITE_SURROGATE_AS_PROOF` | `Q=Q_1000;CLAIM=INFINITE_Q_COMPACTNESS_DECISION` | `FINITE_CONTROLS_NEVER_PROVE_INFINITE_CLAIMS` |
| `ND-0017` | `FIXED_PRIME_Q_CARDINALITY_INFERENCE` | `OWNER=FIXED_PRIME;INPUT=H_LOG_P_Z;CLAIM=QP_FINITE_OR_INFINITE` | `QP_CARDINALITY_UNSPECIFIED` |
| `ND-0018` | `STANDARD_ACTUAL_GROUPOID_CSTAR_TRANSFER` | `OWNER=G_ACTUAL;CANDIDATE=STANDARD_GROUPOID_CSTAR` | `TRANSPORTED_RECORDS_NOT_ACTUAL_GROUPOID_CSTAR` |
| `ND-0019` | `FINITE_CONTROL_UNIVERSAL_H2_PROOF` | `GRID=K24_X_T1_CUBED;CLAIM=UNIVERSAL_H2_ZERO` | `FINITE_CONTROLS_NEVER_PROVE_UNIVERSAL_H2` |
| `ND-0020` | `CONCURRENT_PROOF_HASH_BINDING` | `MUTATION=proof_binding.concurrent_phase3_proof_hash_included:true;PAYLOAD=NON_NULL_PROOF_DIGEST` | `CONTROL_MANIFEST_EXCLUDES_CONCURRENT_PROOF_BINDING` |

The remaining six variable columns are copied from the immutable base table:
`expected_detector` and `expected_disposition` use its exact tokens;
`observed_detector` is computed by the detector below; and the constants are

```text
case_kind=NEGATIVE
oracle=EXPECTED_DETECTOR_TOKEN
tolerance=0
status=PASS
```

The implementation must parse and construct the canonical fixture before
detection. Algebraic rows recompute normalization, exponents, coefficients,
or shifted-vector values. Finite-topology rows enumerate opens and preimages.
Policy rows compare the parsed attempted promotion with the exact
`violated_lock` allow/deny rule. Only then is `observed_detector` emitted.
`status=PASS` requires exact equality with `expected_detector`; directly
copying the expected token into `observed_detector` is forbidden.

For `ND-0013`, `REDUCED_ABS_LE_2_DEN_LE_6` means the ordered set of reduced
rationals `a/b` with `1<=b<=6`, `gcd(|a|,b)=1`, and `|a|<=2b`, sorted by
numeric value and then `(b,a)`. This window is diagnostic-only and cannot
establish density. For `ND-0020`, the fixture mutates the existing sentinel
from `false` to `true` and supplies a non-null proof digest; it does not
rename the sentinel or change the original manifest policy.

## 5. Exact ST field rules

The 21-column header, eight-by-four-by-three enumeration, 96 rows, and 27
negatives remain unchanged. Let `q`, `f`, and `g` be their one-based
positions in the base design's orbit, function, and gauge lists. Then

```text
n = 12*(q-1)+3*(f-1)+g,
row_id = "ST-" + n as four zero-padded decimal digits.
```

### 5.1 Closed value tables

The exact orbit values are:

| `q_case` | `q_class` | `q_cardinality` | `fixed_prime_conditional` | `evidence_scope` |
|---|---|---|---|---|
| `QF1` | `FINITE` | `1` | `false` | `FINITE_COMPONENT_DIAGNOSTIC` |
| `QF2` | `FINITE` | `2` | `false` | `FINITE_COMPONENT_DIAGNOSTIC` |
| `QF4` | `FINITE` | `4` | `false` | `FINITE_COMPONENT_DIAGNOSTIC` |
| `QF7` | `FINITE` | `7` | `false` | `FINITE_COMPONENT_DIAGNOSTIC` |
| `QINF_N` | `INFINITE` | `INF` | `false` | `ANALYTIC_INFINITE_COPRODUCT_BRANCH_ONLY` |
| `QINF_Z` | `INFINITE` | `INF` | `false` | `ANALYTIC_INFINITE_COPRODUCT_BRANCH_ONLY` |
| `QP_FINITE_CONDITIONAL` | `QP_FINITE_CONDITIONAL` | `FINITE_UNSPECIFIED` | `true` | `CONDITIONAL_QP_BRANCH_ONLY` |
| `QP_INFINITE_CONDITIONAL` | `QP_INFINITE_CONDITIONAL` | `INFINITE_ASSUMED` | `true` | `CONDITIONAL_QP_BRANCH_ONLY` |

The exact function values are:

| `function_id` | `is_zero` | Exact `support_components` field |
|---|---|---|
| `ZERO` | `true` | `EMPTY` |
| `TENT_CENTER` | `false` | `[-1,1]` |
| `TENT_SHIFT` | `false` | `[1,3]` |
| `TWO_BUMP` | `false` | `[-3,-1]|[1,2]` |

Because the last three support fields contain commas, the inherited
`csv.writer(QUOTE_MINIMAL)` rule serializes each with surrounding double
quotes. `EMPTY` is unquoted. Ordered gauge values are:

| `gauge_id` | `gauge_nowhere_zero` |
|---|---|
| `ONE` | `true` |
| `ALPHA_K_MINUS6` | `true` |
| `ALPHA_K_6` | `true` |

### 5.2 Explicit equality predicate and complete row derivation

The finite-class predicate is the exact string comparison

```text
finite_q_class
  = (q_class == "FINITE")
    or (q_class == "QP_FINITE_CONDITIONAL").
```

No truthiness, substring, prefix, set-size, or bare-token interpretation is
permitted. The remaining fields are

```text
actual_support_quasicompact = true
standard_support_compact    = is_zero or finite_q_class
lands_in_standard_cc        = standard_support_compact
support_preserved           = gauge_nowhere_zero

fixed_prime_conditional
  = (q_case == "QP_FINITE_CONDITIONAL")
    or (q_case == "QP_INFINITE_CONDITIONAL")

negative_row
  = (is_zero == false)
    and ((q_case == "QINF_N")
         or (q_case == "QINF_Z")
         or (q_case == "QP_INFINITE_CONDITIONAL"))

case_kind = NEGATIVE iff negative_row else POSITIVE

negative_reason
  = CONDITIONAL_NONZERO_QP_INFINITE_NOT_COMPACT
      iff is_zero == false
          and q_case == "QP_INFINITE_CONDITIONAL";
  = NONZERO_INFINITE_Q_NOT_COMPACT
      iff is_zero == false
          and (q_case == "QINF_N" or q_case == "QINF_Z");
  = empty field otherwise.

oracle    = ZERO_OR_FINITE_Q_SUPPORT_BRANCH
tolerance = 0
status    = PASS
```

`status=PASS` requires recomputation of the displayed predicates from the
three closed input tables. It may not be assigned from `case_kind`. This
preserves exactly 27 negatives and 69 positives, including positive zero rows
on every infinite branch.

## 6. Full literal `target_summary.csv` body

The following is the complete canonical 12-row body under the immutable
11-column header. It is literal CSV data in file order; no cell may be
inferred or substituted. There are no commas inside any body field, so no
body field is quoted.

```csv
paper13-circle-twists-controls/1,TS-0001,nerve_factorization_controls.csv,280,17,0,COUNT_SCHEMA_NEGATIVE_TOTAL,EXACT_ZERO,owner_case|unit_id|degree|cochain_profile|t|u,FINITE_TIME_ONLY_WITNESS_NOT_TOPOLOGICAL_PROOF,PASS
paper13-circle-twists-controls/1,TS-0002,circle_multiplier_cocycle_controls.csv,500,20,0,COUNT_SCHEMA_NEGATIVE_TOTAL,EXACT_ZERO,k_index|t|u|v,FINITE_PHASE_GRID_DIAGNOSTIC_NOT_H2_PROOF,PASS
paper13-circle-twists-controls/1,TS-0003,lift_integer_defect_controls.csv,500,20,0,COUNT_SCHEMA_NEGATIVE_TOTAL,EXACT_ZERO,k_index|t|u|v,FINITE_LIFT_WRAP_DIAGNOSTIC_NOT_CONTINUOUS_LIFT_PROOF,PASS
paper13-circle-twists-controls/1,TS-0004,gauge_coboundary_controls.csv,196,19,0,COUNT_SCHEMA_NEGATIVE_TOTAL,EXACT_ZERO,k_index|t|u,FINITE_COBOUNDARY_SIGN_DIAGNOSTIC_NOT_H2_PROOF,PASS
paper13-circle-twists-controls/1,TS-0005,twisted_convolution_controls.csv,78,23,0,COUNT_SCHEMA_NEGATIVE_TOTAL,EXACT_ZERO,fixture_id|k_index|t,FINITE_LATTICE_SIGN_DIAGNOSTIC_ONLY,PASS
paper13-circle-twists-controls/1,TS-0006,twisted_involution_controls.csv,54,26,0,COUNT_SCHEMA_NEGATIVE_TOTAL,EXACT_ZERO,fixture_id|k_index|t,FINITE_LATTICE_SIGN_DIAGNOSTIC_ONLY,PASS
paper13-circle-twists-controls/1,TS-0007,completion_gauge_controls.csv,756,28,0,COUNT_SCHEMA_NEGATIVE_TOTAL,EXACT_ZERO,fixture_id|k_index|character_m|s|u|t,FINITE_MATRIX_ELEMENT_DIAGNOSTIC_ONLY,PASS
paper13-circle-twists-controls/1,TS-0008,action_period_nonretention_controls.csv,56,20,0,COUNT_SCHEMA_NEGATIVE_TOTAL,EXACT_ZERO,action_case_ordinal|k_index,FINITE_ACTION_SIGNATURE_DIAGNOSTIC_ONLY,PASS
paper13-circle-twists-controls/1,TS-0009,negative_domain_controls.csv,20,12,20,COUNT_SCHEMA_NEGATIVE_TOTAL,EXACT_ZERO,row_id,FAIL_CLOSED_DOMAIN_AND_CLAIM_FIREWALL,PASS
paper13-circle-twists-controls/1,TS-0010,actual_standard_support_transfer_controls.csv,96,21,27,COUNT_SCHEMA_NEGATIVE_TOTAL,EXACT_ZERO,q_case|function_id|gauge_id,ANALYTIC_BRANCH_LEDGER_FINITE_CONTROLS_NOT_PROOF,PASS
paper13-circle-twists-controls/1,TS-0011,target_summary.csv,12,11,0,COUNT_SCHEMA_NEGATIVE_TOTAL,EXACT_ZERO,artifact_ordinal,PACKAGE_METADATA_NO_SELF_DIGEST,PASS
paper13-circle-twists-controls/1,TS-0012,PACKAGE_TOTAL,2548,MIXED,47,COUNT_SCHEMA_NEGATIVE_TOTAL,EXACT_ZERO,ARTIFACT_ORDER_ABOVE,PACKAGE_AGGREGATE_NO_THEOREM_CREDIT,PASS
```

The header remains exactly

```text
schema_version,row_id,artifact,expected_rows,expected_columns,expected_negative_rows,oracle_class,tolerance_policy,canonical_order_key,scope,status
```

and precedes those twelve lines with the inherited LF serialization.

## 7. Manifest, proof, and Route boundary — unchanged

After this amendment receives an independent zero-finding re-lock, the
manifest's singular `design_lock={path,sha256}` object binds this amendment's
path and final digest. This amendment in turn binds the immutable base design
and final review in Section 1. The twelve Phase-1/Phase-2/source bindings in
the base design remain unchanged.

The proof block remains exactly

```text
proof_binding = {
  concurrent_phase3_proof_hash_included: false,
  policy: POST_PROOF_AUDIT_BINDS_SEPARATELY
}
```

The base-design prohibition remains exactly: no key matching `proof.*sha`,
no proof path, and no non-null proof digest is permitted. As the final review
records, the required false sentinel does not itself match that forbidden-key
pattern. This amendment does not rename the key, alter the predicate, add a
proof digest, or change the post-proof audit policy.

No manifest or CSV embeds its own digest. No changing proof hash is bound.
No Route YAML or Route audit is authorized. The acyclic later handoff remains

```text
stable proof ----------------------> later integrated audit
stable controls manifest ----------> later integrated audit.
```

## 8. M1 closure and gate consequence

| Final-review M1 surface | Amendment receipt | Status |
|---|---|---|
| AP class and signature literals | five exact tokens plus complete constant/conditional fields | closed |
| AP independent derivation | five separately recomputed exact predicates; no output-token oracle | closed |
| ND `violated_lock` | exact token for all 20 rows | closed |
| ND canonical fixtures | exact semicolon grammar and literal value for all 20 rows | closed |
| ST `support_components` | four exact fields with quoting consequence | closed |
| ST `fixed_prime_conditional` | exact two-case equality predicate and full table | closed |
| ST finite-class predicate | explicit equality against `FINITE` and `QP_FINITE_CONDITIONAL` | closed |
| TS underdetermination | complete literal 12-row body and immutable header | closed |
| Proof sentinel/policy | preserved unchanged per final authoritative review | closed/no change required |
| Counts/schema/negatives/tests | `2548 / 11 CSV / 47 / 128`, unchanged | closed |

Finding register for this bounded amendment:

| Severity | Count | Open item |
|---|---:|---|
| Critical (`C`) | 0 | none |
| Major (`M`) | 0 | none |
| Minor (`m`) | 0 | none |

```text
P13_CONTROL_DESIGN_AMENDMENT_V1=FROZEN_CANDIDATE
BASE_DESIGN_SHA256=900c541713b1711bdab7fa0d264355b6d8ee27014094e60eac6aabe38190604c
FINAL_REVIEW_SHA256=64ce1cd97e122d0fb197731d62dbf37b734d11b6b6b3ee11a97808335c632cd6
M1_AP_EXACT_VALUES_CLOSED=true
M1_AP_INDEPENDENT_DERIVATIONS_CLOSED=true
M1_ND_FIELDS_CLOSED=20/20
M1_ST_FIELDS_CLOSED=true
M1_TS_LITERAL_ROWS_CLOSED=12/12
SCHEMA_CHANGED=false
COUNTS_CHANGED=false
MANIFEST_SEMANTICS_CHANGED=false
PROOF_SENTINEL_CHANGED=false
ROUTE_AUTHORIZED=false
CONTROL_IMPLEMENTATION_AUTHORIZED=false
CONTROL_EXECUTION_PERFORMED=false
CRITICAL_OPEN=0
MAJOR_OPEN=0
MINOR_OPEN=0
```

The amended tuple is ready for an independent exact-byte re-lock.
Implementation remains blocked until that review returns `C0/M0/m0` on the
base design, final review, and this amendment. Proof, controls execution,
standalone, Route, composition, manuscript, citation, release, Git, and
public synchronization remain under their separate gates.
