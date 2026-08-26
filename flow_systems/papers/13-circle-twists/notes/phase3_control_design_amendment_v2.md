# Paper 13 Phase-3 control-design amendment v2 — completion diagonal and corona

Status: **FROZEN DESIGN CANDIDATE / INDEPENDENT EXACT-BYTE REVIEW REQUIRED**  
Version: **P13-CONTROLS-v2.0-AMENDMENT-v2**  
Date: **2026-08-15 (Asia/Shanghai)**  
Bounded design audit: **C0 / M0 / m0**  
Control implementation or execution performed here: **no**  
`route_b_invocation_allowed: false`

## Material Passport

- Origin Mode: separate deterministic-control design amendment
- Origin Date: 2026-08-15
- Verification Status: UNVERIFIED
- Version Label: `p13_control_design_amendment_v2`
- Scope: schema, exact rows, oracles, package totals, tests, manifest DAG, and
  reproduction gates only; no theorem, proof, code, result, Route,
  composition, manuscript, citation, standalone, release, Git, or public-sync
  claim

## 1. Authority, precedence, and hard boundary

This separate design amendment is authorized only by Section 7 of
`notes/phase3_v2_design_gate.md`.  That gate was rehashed immediately before
this file was written.  The exact controlling tuple is:

| Artifact | SHA-256 | Design use |
|---|---|---|
| `notes/phase3_control_design_lock.md` | `900c541713b1711bdab7fa0d264355b6d8ee27014094e60eac6aabe38190604c` | immutable v1 base design |
| `notes/phase3_control_design_amendment_v1.md` | `5c9caea983b0047c4b16d0437c23b117a6b8150bbeb67b79c60fb9b2ba6a737e` | exact-row v1 closure |
| `notes/phase3_control_design_review.md` | `bf56b96e19b682600ed5de43f7df51ef381fe82d4e12363f66cd1e7d2a5a5184` | final amended-v1 `PASS C0/M0/m0` review |
| `notes/phase3_standalone_amendment_v2.md` | `99c796bffe24f262d8ac8458b21fd253451bca51bac4b283660dab319992ed82` | v2 theorem and owner design |
| `notes/phase3_standalone_amendment_v2_ownership_addendum.md` | `d9523d1692d60fbdff7bbf5ab6c00d44bdcd26f02dc5cdeeba8c7ba43d78a39f` | Paper-2 credit and owner precedence |
| `notes/phase3_v2_methodology_review.md` | `96a5067015847ff88155b91658ae94e9ef5a6355ae176c1945644b3e729f4f74` | final methodology closure, `PASS C0/M0/m0` |
| `notes/phase3_v2_devils_advocate.md` | `1c6bbb0bc7d3fc366de4d8a4eb869d4d4708f19647f10d780be095ac9e81f110` | final devil/domain closure, `PASS C0/M0/m0` |
| `notes/phase3_v2_source_feasibility.md` | `3ce4e8db7914c0053a31b7e0e08e8f0fe02e0b2db15620f194c1ccae5ffeb320` | final source/ownership closure, `PASS C0/M0/m0` |
| `notes/phase3_v2_design_gate.md` | `0094462b1e06cde0cf1fcc3536c608dcd96ef1e9eb0d85a0714df1666b799706` | exact Section-7 authorization |

The ownership addendum has precedence only on its declared surfaces.  All
untouched signs, gauge directions, analytic obligations, owner firewalls,
source ceilings, and blocked statuses in the base v2 remain binding.

This file designs controls only.  It creates no implementation file, result
directory, CSV, manifest, test run, or proof receipt.  It binds no changing
P13-8A--C proof path or digest.  Implementation remains fail-closed until an
independent reviewer returns `PASS C0/M0/m0` on the final bytes of this file
and a later exact implementation authorization is issued.

## 2. Immutable v1 package and narrow v2 delta

The still-unimplemented amended-v1 package remains the base.  All eleven v1
CSV headers and all 2,548 v1 CSV body rows are preserved byte-identically
under the original schema

```text
paper13-circle-twists-controls/1
```

In particular, the complete twelve-row body of `target_summary.csv` remains
the immutable v1 snapshot.  Its `PACKAGE_TOTAL=2548` row is not rewritten or
reinterpreted as a v2 package total.  The new CSV below contains a distinct
v2 summary family that is authoritative only for the augmented package.

No v1 row ID, literal, reason, oracle, tolerance, order, quoting consequence,
or count changes.  The preserved body inventory is:

| # | Immutable v1 CSV | Body rows | Columns | Negative rows |
|---:|---|---:|---:|---:|
| 1 | `nerve_factorization_controls.csv` | 280 | 17 | 0 |
| 2 | `circle_multiplier_cocycle_controls.csv` | 500 | 20 | 0 |
| 3 | `lift_integer_defect_controls.csv` | 500 | 20 | 0 |
| 4 | `gauge_coboundary_controls.csv` | 196 | 19 | 0 |
| 5 | `twisted_convolution_controls.csv` | 78 | 23 | 0 |
| 6 | `twisted_involution_controls.csv` | 54 | 26 | 0 |
| 7 | `completion_gauge_controls.csv` | 756 | 28 | 0 |
| 8 | `action_period_nonretention_controls.csv` | 56 | 20 | 0 |
| 9 | `negative_domain_controls.csv` | 20 | 12 | 20 |
| 10 | `actual_standard_support_transfer_controls.csv` | 96 | 21 | 27 |
| 11 | `target_summary.csv` | 12 | 11 | 0 |
| **v1 snapshot** |  | **2548** | -- | **47** |

The sole CSV addition is

```text
completion_corona_controls_v2.csv
```

under schema `paper13-circle-twists-controls/2`.  The augmented manifest uses
`paper13-circle-twists-controls-manifest/2`.  The existing UTF-8-without-BOM,
LF, `csv.writer(QUOTE_MINIMAL)`, exact-integer, canonical-JSON, and prohibited-
metadata rules remain unchanged.

## 3. Mathematical and evidence ceiling of the new controls

The new rows are finite scalar models, exact phase-term diagnostics, analytic
branch ledgers, owner/credit ledgers, and fail-closed policy detectors.  They
do **not** prove any of the following:

1. `|Q_p^bare|=2^aleph_0` or any continuum-cardinality statement;
2. the multiplier identity for a `c0` sum over an arbitrary index set;
3. the component maximal or reduced norm chain;
4. the infinite-branch intersection or faithful corona theorem;
5. extension of a dense gauge identity through completions, multiplier
   algebras, or corona quotients; or
6. the unconditional fixed-prime theorem.

The infinite and fixed-prime rows serialize the theorem's exact analytic
branch predicates so that later implementation drift can be detected.  Their
oracle is not a finite computation and earns no proof, novelty, standalone,
or Route credit.  Finite tail quotients are explicitly only quotient-norm
analogues; they are never identified with an actual multiplier corona.

Paper 2 owns the continuum lower bound and bare-set packet transfer.  Its
rederivation receives zero P13 credit.  Paper 13 may receive only supporting
credit for the elementary upper-bound/equality closure, exact owner retyping,
and direct standard-topology consequences.  P13-8B/C alone carry the still-
unresolved standalone gate after standard ingredients are subtracted.

## 4. Exact new-CSV schema and shared field rules

### 4.1 Exact filename, header, bytes, and row IDs

`completion_corona_controls_v2.csv` has the following exact 41-column header:

```text
schema_version,row_id,control_family,owner_case,q_class,q_model_size,epsilon,input_id,input_norm,coordinate_norm_class,multiplier_member,algebra_member,finite_c0_member,tail_window_size,quotient_distance,quotient_image_nonzero,quotient_map_injective,gauge_id,gauge_lhs_exp_mod24,gauge_rhs_exp_mod24,gauge_commutes,max_evidence_status,reduced_evidence_status,cardinality_credit_owner,topology_owner,fixed_prime_branch,evidence_scope,summary_artifact,summary_rows,summary_columns,summary_negative_rows,summary_test_methods,case_kind,negative_reason,fixture,violated_lock,expected_detector,observed_detector,oracle,tolerance,status
```

There are exactly 117 body rows.  If `n` is the one-based global row number,
then

```text
row_id="V2-" + n as four zero-padded base-ten digits
```

Thus the IDs are `V2-0001` through `V2-0117`.
Rows are emitted by the family order in Section 4.4, never by map, locale, or
string sorting.  Every row has:

```text
schema_version=paper13-circle-twists-controls/2
tolerance=0
```

Every field not assigned by its family rule is the empty field.  No optional
field may contain `NA`, `null`, a space, or an inferred default.  Booleans are
only `true` or `false`.  `status=PASS` is emitted only after the family oracle
is independently recomputed from the closed input tables; generation aborts
on a false predicate rather than emitting a `FAIL` row.

In the descriptive tables below, the word `empty` denotes the empty CSV field;
the five letters `empty` are never serialized.

The exact `control_family` and `case_kind` pairs are:

| Family | `case_kind` | Rows |
|---|---|---:|
| `FINITE_C0_MODEL` | `DIAGNOSTIC` | 18 |
| `INFINITE_ANALYTIC_BOUNDARY` | `DIAGNOSTIC` | 18 |
| `FINITE_TAIL_QUOTIENT_MODEL` | `DIAGNOSTIC` | 12 |
| `GAUGE_COMMUTATION_MODEL` | `DIAGNOSTIC` | 24 |
| `OWNER_CREDIT_LEDGER` | `DIAGNOSTIC` | 8 |
| `MAX_REDUCED_EVIDENCE_LEDGER` | `DIAGNOSTIC` | 4 |
| `FIREWALL_NEGATIVE` | `NEGATIVE` | 20 |
| `V2_PACKAGE_SUMMARY` | `SUMMARY` | 13 |
| **Total** |  | **117** |

The literal family oracles are, in the same order:

```text
FINITE_C0_CONSTANT_COORDINATE_MODEL
INFINITE_CONSTANT_NORM_C0_CORONA_BRANCH
FINITE_TAIL_SUP_QUOTIENT_DISTANCE
FROZEN_COMPONENT_DIAGONAL_GAUGE_TERM
OWNER_CREDIT_TOPOLOGY_EXACT_TOKEN
MAX_REDUCED_EVIDENCE_SEPARATION
EXPECTED_DETECTOR_TOKEN
V2_COUNT_SCHEMA_NEGATIVE_TOTAL
```

### 4.2 Exact scalar inputs and completion order

The scalar fixtures are Gaussian-integer models.  No square root or floating
point operation is used.

| `input_id` | Exact scalar `(re,im)` | `input_norm` | `coordinate_norm_class` |
|---|---|---:|---|
| `ZERO` | `(0,0)` | `0` | `CONSTANT_0` |
| `ONE` | `(1,0)` | `1` | `CONSTANT_1` |
| `I` | `(0,1)` | `1` | `CONSTANT_1` |

Their order is `ZERO,ONE,I`.  These are scalar diagnostic models, not a
dense family in either time completion.  The completion order is exactly

```text
epsilon=(max,r)
```

Whenever a row has `epsilon=max`, only `max_evidence_status` is nonempty;
whenever it has `epsilon=r`, only `reduced_evidence_status` is nonempty.
The four evidence-ledger rows in Section 6.2 are the sole exception and use
their explicit table.  No row silently copies maximal evidence into a
reduced field or conversely.

### 4.3 Coordinate and `c0` predicates

For a scalar input `a`, every finite or analytic diagonal model has coordinate
norm `|a|`, so the stored coordinate class is `CONSTANT_0` or `CONSTANT_1` as
given above.  The exact arbitrary-index membership predicate serialized by
the analytic rows is

```text
D(a) in A_std  iff input_norm == 0 or q_class == FINITE
```

The bounded multiplier predicate is `true` because the coordinate norms are
constant and bounded.  For infinite rows the quotient-distance branch is

```text
dist(D(a),A_std)=input_norm,
quotient_image_nonzero=(input_norm != 0),
quotient_map_injective=true
```

These are analytic theorem-branch values, not a finite derivation of the
arbitrary-index multiplier identity or corona theorem.

### 4.4 Canonical family blocks and row ranges

The complete row order and ID ranges are:

| Block | Family | Enumeration | IDs |
|---:|---|---|---|
| 1 | `FINITE_C0_MODEL` | finite owner, input, `epsilon` | `V2-0001`--`V2-0018` |
| 2 | `INFINITE_ANALYTIC_BOUNDARY` | infinite owner, input, `epsilon` | `V2-0019`--`V2-0036` |
| 3 | `FINITE_TAIL_QUOTIENT_MODEL` | quotient model, input, `epsilon` | `V2-0037`--`V2-0048` |
| 4 | `GAUGE_COMMUTATION_MODEL` | `K24`, `TG`, `epsilon` | `V2-0049`--`V2-0072` |
| 5 | `OWNER_CREDIT_LEDGER` | literal table order | `V2-0073`--`V2-0080` |
| 6 | `MAX_REDUCED_EVIDENCE_LEDGER` | literal table order | `V2-0081`--`V2-0084` |
| 7 | `FIREWALL_NEGATIVE` | literal registry order | `V2-0085`--`V2-0104` |
| 8 | `V2_PACKAGE_SUMMARY` | twelve artifacts, package total | `V2-0105`--`V2-0117` |

## 5. Exact model and analytic rows

### 5.1 Rows 1--18: finite symbolic `c0` membership

The ordered finite cases are:

| `owner_case` | `q_class` | `q_model_size` |
|---|---|---:|
| `GENERIC_COMMON_LATTICE_QF1` | `FINITE` | `1` |
| `GENERIC_COMMON_LATTICE_QF2` | `FINITE` | `2` |
| `GENERIC_COMMON_LATTICE_QF4` | `FINITE` | `4` |

For one-based positions `q in {1,2,3}`, `a in {1,2,3}`, and epsilon
position `h in {1,2}`, the row number is

```text
n=6*(q-1)+2*(a-1)+h
```

In addition to the closed owner/input/epsilon tables, every row has:

```text
multiplier_member=true
algebra_member=true
finite_c0_member=true
quotient_distance=0
quotient_image_nonzero=false
quotient_map_injective=false
cardinality_credit_owner=NOT_APPLICABLE
topology_owner=Q_BARE_INDEX_ONLY
fixed_prime_branch=GENERIC_FINITE_BRANCH
evidence_scope=FINITE_SCALAR_C0_MODEL_ONLY
oracle=FINITE_C0_CONSTANT_COORDINATE_MODEL
```

The selected evidence token is

```text
max: FINITE_SCALAR_MAX_NORM_DIAGNOSTIC_ONLY
r:   FINITE_SCALAR_REDUCED_NORM_DIAGNOSTIC_ONLY
```

The oracle independently verifies the scalar norm, constant coordinate
class, boundedness, finite-`c0` membership, zero quotient distance, and the
fact that the finite-branch corona composite is the zero, noninjective map.
This finite branch says nothing about an infinite index set.

### 5.2 Rows 19--36: infinite analytic boundary and fixed-prime branch

The ordered cases are:

| `owner_case` | `q_class` | `q_model_size` | `cardinality_credit_owner` | `fixed_prime_branch` | `evidence_scope` |
|---|---|---|---|---|---|
| `GENERIC_COMMON_LATTICE_QINF_N` | `INFINITE` | `COUNTABLY_INFINITE` | `NOT_APPLICABLE` | `GENERIC_INFINITE_BRANCH` | `ANALYTIC_INFINITE_BRANCH_LEDGER_NOT_FINITE_PROOF` |
| `GENERIC_COMMON_LATTICE_QINF_UNCOUNTABLE` | `INFINITE` | `UNCOUNTABLE_SYMBOLIC` | `NOT_APPLICABLE` | `GENERIC_INFINITE_BRANCH` | `ANALYTIC_INFINITE_BRANCH_LEDGER_NOT_FINITE_PROOF` |
| `FIXED_PRIME_RATIONAL_WITT_QP` | `CONTINUUM` | `2^ALEPH_0` | `PAPER2_LOWER_BOUND_INHERITED_ZERO_P13_CREDIT` | `UNCONDITIONAL_FIXED_PRIME_PAPER2_LOWER_PLUS_P13_UPPER` | `FIXED_PRIME_ANALYTIC_BRANCH_LEDGER_NOT_CONTROL_PROOF` |

Rows again enumerate owner, `ZERO,ONE,I`, and `max,r`.  If `q`, `a`, and
`h` are their one-based owner, input, and epsilon positions, respectively,
the global row number is

```text
n=18+6*(q-1)+2*(a-1)+h
```

Every row has:

```text
multiplier_member=true
algebra_member=(input_norm == 0)
finite_c0_member=
quotient_distance=input_norm
quotient_image_nonzero=(input_norm != 0)
quotient_map_injective=true
topology_owner=Q_BARE_INDEX_ONLY
oracle=INFINITE_CONSTANT_NORM_C0_CORONA_BRANCH
```

The selected evidence token is

```text
max: ANALYTIC_MAX_BRANCH_REQUIRES_THEOREM_PROOF
r:   ANALYTIC_REDUCED_BRANCH_REQUIRES_THEOREM_PROOF
```

Thus the nonzero rows record `multiplier_member=true` and
`algebra_member=false` separately.  The fixed-prime rows are unconditional in
the theorem design: the obsolete finite/infinite `Q_p` alternative is not
carried forward.  Their continuum premise is explicitly Paper-2 inherited
lower-bound evidence plus the authorized direct P13 upper/equality closure;
the control row itself proves neither premise.

### 5.3 Rows 37--48: finite tail quotient-distance models

The ordered models are:

| `owner_case` | Core size `m` | `tail_window_size=n` | `q_class` | `q_model_size` |
|---|---:|---:|---|---:|
| `FINITE_QUOTIENT_CORE0_TAIL1` | 0 | `1` | `FINITE_QUOTIENT_MODEL` | `1` |
| `FINITE_QUOTIENT_CORE2_TAIL3` | 2 | `3` | `FINITE_QUOTIENT_MODEL` | `5` |

For each model define exactly

```text
E_(m,n)=C^(m+n) with the sup norm,
J_(m,n)=C^m direct_sum 0^n,
x_a=(a,...,a) in E_(m,n)
```

`J_(m,n)` is a coordinate ideal and `E_(m,n)/J_(m,n)=C^n`.  Because
`n>=1`, exact Gaussian arithmetic gives

```text
dist(x_a,J_(m,n))=input_norm,
quotient_image_nonzero=(input_norm != 0),
a |-> x_a+J_(m,n) is injective
```

Rows enumerate model, input, and `epsilon`.  For one-based model position
`b in {1,2}`, input position `a in {1,2,3}`, and epsilon position
`h in {1,2}`:

```text
n_global=36+6*(b-1)+2*(a-1)+h
```

The fields `multiplier_member`, `algebra_member`, and `finite_c0_member` are
empty.  Other fixed values are:

```text
quotient_distance=input_norm
quotient_image_nonzero=(input_norm != 0)
quotient_map_injective=true
cardinality_credit_owner=NOT_APPLICABLE
topology_owner=NO_ACTUAL_OR_STANDARD_OWNER_FINITE_MODEL
fixed_prime_branch=NOT_APPLICABLE
evidence_scope=FINITE_IDEAL_QUOTIENT_MODEL_NOT_MULTIPLIER_CORONA_PROOF
oracle=FINITE_TAIL_SUP_QUOTIENT_DISTANCE
```

The selected evidence token is

```text
max: FINITE_TAIL_MAX_QUOTIENT_MODEL_ONLY
r:   FINITE_TAIL_REDUCED_QUOTIENT_MODEL_ONLY
```

The quotient in this block is not named or identified as `M(A)/A`.  These
rows test exact distance and injectivity logic in finite ideal quotients, not
corona faithfulness.

### 5.4 Rows 49--72: frozen gauge-commutation terms

Use the inherited exact phase set and the new ordered term grid

```text
K24=(-6,-1,0,6),
TG=(-1,0,1)
```

The term IDs are `TERM_MINUS1,TERM_0,TERM_1` in `TG` order.  Gauge IDs in
`K24` order are

```text
ALPHA_K_MINUS6,ALPHA_K_MINUS1,ALPHA_K_0,ALPHA_K_6
```

Set `tau=1`, `sigma=delta alpha_k`, and retain the exact orientation

```text
sigma overline(tau)=delta alpha_k
```

On the symbolic time term at `t`, independently compute both sides of

```text
U_(alpha,q) d_(q,sigma)=d_(q,tau) U_alpha
```

as the least nonnegative exponent

```text
e(k,t)=(-k*t^2) mod 24
```

For one-based `j in {1,...,4}`, `s in {1,2,3}`, and epsilon position
`h in {1,2}`:

```text
n_global=48+6*(j-1)+2*(s-1)+h
```

Every row has:

```text
owner_case=GENERIC_ORIGIN_FREE_COMPONENT_GAUGE_TERM
q_class=FINITE_SYMBOLIC_COMPONENT
q_model_size=1
input_id=<term ID from TG>
input_norm=1
coordinate_norm_class=CONSTANT_1
gauge_lhs_exp_mod24=e(k,t)
gauge_rhs_exp_mod24=e(k,t)
gauge_commutes=true
cardinality_credit_owner=NOT_APPLICABLE
topology_owner=ORIGIN_FREE_COMPONENT_OWNER
fixed_prime_branch=GENERIC_NOT_FIXED_PRIME
evidence_scope=FINITE_GAUGE_TERM_DIAGNOSTIC_NOT_COMPLETION_SQUARE_PROOF
oracle=FROZEN_COMPONENT_DIAGONAL_GAUGE_TERM
```

The exact fixture field is constructed as

```text
K=<base-ten k>;T=<base-ten t>;TAU=ONE;ORIENTATION=SIGMA_OVERLINE_TAU_EQ_DELTA_ALPHA
```

with no whitespace.  The selected evidence token is

```text
max: DENSE_MAX_GAUGE_IDENTITY_EXTENSION_REQUIRES_PROOF
r:   DENSE_REDUCED_GAUGE_IDENTITY_EXTENSION_REQUIRES_PROOF
```

The oracle recomputes both exponents from `k,t`, verifies the orientation
token, and checks equality.  It does not certify extension through a full or
reduced completion, a `c0` sum, a multiplier algebra, or a corona.

## 6. Exact owner, credit, and evidence ledgers

### 6.1 Rows 73--80: actual/bare/standard/discrete and Paper-2 firewall

These eight rows are emitted literally in table order.  Fields not displayed
are empty.  Every row has

```text
evidence_scope=OWNER_CREDIT_LEDGER_ONLY
oracle=OWNER_CREDIT_TOPOLOGY_EXACT_TOKEN
```

| ID | `owner_case` | `q_class` | `cardinality_credit_owner` | `topology_owner` | `fixed_prime_branch` | Exact `fixture` |
|---|---|---|---|---|---|---|
| `V2-0073` | `PAPER2_LOWER_BOUND_OWNER` | `CONTINUUM_LOWER_BOUND` | `PAPER2_PROP_UNCOUNTABLE_ZERO_P13_CREDIT` | `Q_P_BARE_NO_TOPOLOGY` | `INHERITED_FIXED_PRIME_PREMISE` | `CLAIM=QP_CONTINUUM_LOWER_BOUND` |
| `V2-0074` | `P13_EQUALITY_CLOSURE_OWNER` | `CONTINUUM` | `P13_UPPER_BOUND_EQUALITY_SUPPORTING_ONLY` | `Q_P_BARE_NO_TOPOLOGY` | `UNCONDITIONAL_FIXED_PRIME_BRANCH` | `CLAIM=QP_EXACT_CARDINALITY_EQUALITY` |
| `V2-0075` | `ACTUAL_QUOTIENT_OWNER` | `ACTUAL` | `PAPER9_ACTUAL_OWNER` | `Q_P_ACTUAL_INDISCRETE_SECOND_COUNTABLE_NONHAUSDORFF` | `FIXED_PRIME_OWNER_SPLIT` | `CLAIM=ACTUAL_QUOTIENT_TOPOLOGY` |
| `V2-0076` | `BARE_INDEX_OWNER` | `BARE` | `PAPER2_LOWER_PLUS_P13_UPPER_RETYPE` | `Q_P_BARE_NO_TOPOLOGY` | `FIXED_PRIME_OWNER_SPLIT` | `CLAIM=BARE_CARDINALITY_ONLY` |
| `V2-0077` | `STANDARD_UNIT_OWNER` | `STANDARD` | `PAPER12_STANDARD_OWNER_P13_DIRECT_CONSEQUENCE` | `STD_GAMMA_P_NONSECONDCOUNTABLE_NONSIGMACOMPACT` | `FIXED_PRIME_OWNER_SPLIT` | `CLAIM=STANDARD_UNIT_TOPOLOGY_FAILURES` |
| `V2-0078` | `STANDARD_ARROW_OWNER` | `STANDARD_ARROW` | `PAPER12_STANDARD_OWNER_P13_DIRECT_CONSEQUENCE` | `STD_ARROW_P_NONSECONDCOUNTABLE_NONSIGMACOMPACT` | `FIXED_PRIME_OWNER_SPLIT` | `CLAIM=STANDARD_ARROW_TOPOLOGY_FAILURES` |
| `V2-0079` | `DISCRETE_QUOTIENT_OWNER` | `DISCRETE` | `PAPER12_DISCRETE_OWNER_P13_DIRECT_CONSEQUENCE` | `Q_P_DISC_NONSECONDCOUNTABLE_NONSIGMACOMPACT` | `FIXED_PRIME_OWNER_SPLIT` | `CLAIM=DISCRETE_QUOTIENT_TOPOLOGY_FAILURES` |
| `V2-0080` | `GENERIC_BARE_COMPONENT_INDEX_OWNER` | `BARE` | `NOT_APPLICABLE` | `Q_BARE_NO_TOPOLOGY` | `GENERIC_BRANCH` | `CLAIM=ARBITRARY_INDEX_OWNER` |

The oracle compares each row with this closed literal table.  It does not
infer an owner from a claim name.  No topology value in rows 77--79 may be
copied to row 75 or 76.

### 6.2 Rows 81--84: maximal/reduced evidence status

These four rows are emitted literally.  They record obligations, not passed
proof evidence.  Every row has

```text
q_class=ARBITRARY_Q_BARE
topology_owner=COMPONENT_RECORDS_B_Q_MAX_OR_R
evidence_scope=EVIDENCE_STATUS_LEDGER_NOT_NORM_PROOF
oracle=MAX_REDUCED_EVIDENCE_SEPARATION
```

| ID | `owner_case` | `epsilon` | `max_evidence_status` | `reduced_evidence_status` | Exact `fixture` |
|---|---|---|---|---|---|
| `V2-0081` | `COMPONENT_MAX_NORM` | `max` | `DIRECT_COMPONENT_MAX_RESTRICTION_CHAIN_REQUIRED` | empty | `CLAIM=COMPONENT_MAX_UPPER_AND_REGULAR_LOWER` |
| `V2-0082` | `COMPONENT_REDUCED_NORM` | `r` | empty | `EVERY_UNIT_REGULAR_RESTRICTION_REQUIRED` | `CLAIM=EVERY_UNIT_REDUCED_RESTRICTION` |
| `V2-0083` | `TIME_AMENABLE_ENDPOINT_EQUALITY` | `both` | `TIME_MAX_NORM_ENDPOINT_REQUIRED` | `TIME_REDUCED_NORM_ENDPOINT_REQUIRED` | `CLAIM=TIME_AMENABILITY_ENDPOINT_EQUALITY` |
| `V2-0084` | `MAX_REDUCED_SERIALIZATION` | `separate` | `SEPARATE_MAX_EVIDENCE_STATUS_REQUIRED` | `SEPARATE_REDUCED_EVIDENCE_STATUS_REQUIRED` | `CLAIM=MAX_REDUCED_SERIALIZED_SEPARATELY` |

The oracle rejects an empty required side, a copied common token, a swapped
token, or any value containing `PASS`, `PROVED`, or `CONTROL_EVIDENCE`.
Different future proof or Route evidence for `max` and `r` therefore remains
visible and triggers the ownership addendum's pre-Route split rule.

## 7. Exact v2 negative registry

Rows `V2-0085`--`V2-0104` are the following twenty negatives in exact order.
Each fixture is one ASCII field with its displayed semicolon clause order and
no comma, quote, CR, LF, or whitespace.  Every row has:

```text
owner_case=FIREWALL_ATTEMPT
evidence_scope=FAIL_CLOSED_V2_CLAIM_AND_MANIFEST_FIREWALL
case_kind=NEGATIVE
oracle=EXPECTED_DETECTOR_TOKEN
tolerance=0
status=PASS
```

| ID | `negative_reason` | Exact `fixture` | Exact `violated_lock` | `expected_detector` |
|---|---|---|---|---|
| `V2-0085` | `FINITE_SIGN_PROJECTION_AS_CONTINUUM_PROOF` | `MODEL=SIGN_COORDS_16;CLAIM=QP_CARDINALITY_CONTINUUM` | `FINITE_CONTROLS_NEVER_PROVE_CONTINUUM` | `REJECT_FINITE_AS_CONTINUUM_PROOF` |
| `V2-0086` | `FINITE_C0_WINDOW_AS_ARBITRARY_INDEX_PROOF` | `MODEL=QF4;CLAIM=ARBITRARY_INDEX_MULTIPLIER_IDENTITY` | `FINITE_CONTROLS_NEVER_PROVE_ARBITRARY_INDEX_THEOREM` | `REJECT_FINITE_AS_ARBITRARY_INDEX_PROOF` |
| `V2-0087` | `FINITE_TAIL_QUOTIENT_AS_CORONA_PROOF` | `MODEL=CORE2_TAIL3;CLAIM=FAITHFUL_MULTIPLIER_CORONA` | `FINITE_QUOTIENT_MODEL_NOT_ACTUAL_CORONA` | `REJECT_FINITE_AS_CORONA_PROOF` |
| `V2-0088` | `PAPER2_LOWER_BOUND_CREDIT_TO_P13` | `SOURCE=PAPER2_PROP_UNCOUNTABLE;CREDIT=P13_NOVELTY` | `PAPER2_LOWER_BOUND_ZERO_P13_CREDIT` | `REJECT_INHERITED_CARDINALITY_CREDIT` |
| `V2-0089` | `ACTUAL_QUOTIENT_GIVEN_DISCRETE_TOPOLOGY` | `OWNER=Q_P_ACTUAL;TOPOLOGY=DISCRETE` | `Q_P_ACTUAL_RETAINS_INDISCRETE_TOPOLOGY` | `REJECT_ACTUAL_DISCRETE_PROMOTION` |
| `V2-0090` | `BARE_SET_GIVEN_TOPOLOGY` | `OWNER=Q_P_BARE;TOPOLOGY=INDISCRETE` | `Q_P_BARE_HAS_NO_TOPOLOGY` | `REJECT_BARE_TOPOLOGY` |
| `V2-0091` | `STANDARD_FAILURE_ASSIGNED_TO_ACTUAL` | `SOURCE=STD_GAMMA_P;TARGET=Q_P_ACTUAL;CLAIM=NONSECONDCOUNTABLE` | `STANDARD_TOPOLOGY_NOT_TRANSPORTED_TO_ACTUAL` | `REJECT_STANDARD_ACTUAL_OWNER_CONFLATION` |
| `V2-0092` | `DISCRETE_QUOTIENT_IDENTIFIED_WITH_ACTUAL` | `SOURCE=Q_P_DISC;TARGET=Q_P_ACTUAL;MAP=TOPOLOGICAL_IDENTITY` | `ACTUAL_AND_DISCRETE_QUOTIENT_OWNERS_DISTINCT` | `REJECT_DISCRETE_ACTUAL_IDENTITY` |
| `V2-0093` | `BOUNDED_MULTIPLIER_PRODUCT_IDENTIFIED_WITH_C0_ALGEBRA` | `OWNER=INFINITE_Q;CANDIDATE=PRODUCT_BOUNDED_EQ_C0_SUM` | `MULTIPLIER_PRODUCT_DISTINCT_FROM_C0_ALGEBRA` | `REJECT_MULTIPLIER_ALGEBRA_CONFLATION` |
| `V2-0094` | `NONZERO_INFINITE_DIAGONAL_DECLARED_C0` | `Q=INFINITE;INPUT=ONE;CLAIM=ALGEBRA_MEMBER` | `CONSTANT_NONZERO_NORM_NOT_C0` | `REJECT_CONSTANT_NORM_C0_MEMBERSHIP` |
| `V2-0095` | `FINITE_Q_CORONA_MAP_DECLARED_INJECTIVE` | `Q=QF2;INPUT=ONE;CLAIM=CORONA_MAP_INJECTIVE` | `FINITE_BRANCH_DIAGONAL_LIES_IN_ALGEBRA` | `REJECT_FINITE_BRANCH_CORONA_INJECTIVITY` |
| `V2-0096` | `CORONA_KERNEL_LARGER_THAN_INTERSECTION` | `Q=INFINITE;CANDIDATE=KERNEL_STRICTLY_CONTAINS_PREIMAGE_A` | `QUOTIENT_KERNEL_EQUALS_PREIMAGE_OF_ALGEBRA` | `REJECT_QUOTIENT_KERNEL_MISMATCH` |
| `V2-0097` | `V2_GAUGE_ORIENTATION_REVERSED` | `RELATION=TAU_OVERLINE_SIGMA_EQ_DELTA_ALPHA;MAP=U_ALPHA_SIGMA_TO_TAU` | `GAUGE_DIRECTION_SIGMA_OVERLINE_TAU_EQ_DELTA_ALPHA` | `GAUGE_DIRECTION_MISMATCH` |
| `V2-0098` | `MAX_REDUCED_EVIDENCE_CONFLATED` | `MAX_STATUS=COPIED_COMMON_PASS;REDUCED_STATUS=COPIED_COMMON_PASS` | `MAX_REDUCED_EVIDENCE_SERIALIZED_SEPARATELY` | `REJECT_MAX_REDUCED_EVIDENCE_CONFLATION` |
| `V2-0099` | `V1_CONDITIONAL_QP_BRANCH_USED_AS_V2_RESULT` | `SOURCE=V1_QP_FINITE_CONDITIONAL;CLAIM=V2_FIXED_PRIME_BRANCH` | `V1_CONDITIONAL_ROWS_ARE_IMMUTABLE_HISTORICAL_DIAGNOSTICS` | `REJECT_V1_CONDITIONAL_AS_V2_BRANCH` |
| `V2-0100` | `FIXED_PRIME_CONTINUUM_INFERRED_FROM_PERIOD_ONLY` | `INPUT=H_LOG_P_Z;CLAIM=QP_CONTINUUM` | `FIXED_PRIME_CARDINALITY_REQUIRES_PAPER2_LOWER_AND_P13_UPPER` | `REJECT_PERIOD_ONLY_CARDINALITY_INFERENCE` |
| `V2-0101` | `GLOBAL_TWISTED_GROUPOID_CSTAR_PROMOTION_V2` | `OWNER=STD_GLOBAL;CANDIDATE=TWISTED_GROUPOID_CSTAR` | `COMPONENTWISE_AUTHOR_RECORD_NOT_GLOBAL_TWISTED_GROUPOID_CSTAR` | `REJECT_GLOBAL_TWISTED_FRAMEWORK_PROMOTION` |
| `V2-0102` | `CONCURRENT_PROOF_HASH_BINDING_V2` | `MANIFEST=PROOF_PATH_AND_NON_NULL_SHA256` | `CONTROL_MANIFEST_EXCLUDES_CONCURRENT_PROOF_BINDING` | `REJECT_PROOF_HASH_BINDING` |
| `V2-0103` | `MANIFEST_SELF_HASH_BINDING_V2` | `MANIFEST=ARTIFACT_LIST_INCLUDES_MANIFEST_JSON_SHA256` | `MANIFEST_NEVER_HASHES_ITSELF` | `REJECT_MANIFEST_SELF_HASH` |
| `V2-0104` | `V2_DESIGN_OR_GATE_UNBOUND` | `MANIFEST=OMIT_V2_DESIGN_HEAD_OR_AUTHORIZATION_GATE` | `MANIFEST_BINDS_V2_DESIGN_AND_GATE` | `REJECT_UNBOUND_V2_AUTHORITY` |

The implementation must parse and construct each attempted promotion before
detection.  Algebraic rows recompute scalar norms, membership, quotient, or
phase predicates; owner and credit rows compare the parsed source/target with
the exact owner table; manifest rows mutate a valid manifest object and then
run the binding/self-cycle validator.  `observed_detector` is emitted only
after detection and must equal `expected_detector`.  Directly copying the
expected token is forbidden.

These twenty labels are the complete new nonempty `negative_reason` set.
They supplement, without changing, the 22 allowed v1 reason labels and the 47
v1 negative rows.

## 8. Exact v2 summary rows

Rows `V2-0105`--`V2-0117` are the authoritative augmented-package summary.
Every row has

```text
control_family=V2_PACKAGE_SUMMARY
case_kind=SUMMARY
oracle=V2_COUNT_SCHEMA_NEGATIVE_TOTAL
```

Fields not shown are empty.  `owner_case` freezes the artifact ordinal.

| ID | `owner_case` | `summary_artifact` | `summary_rows` | `summary_columns` | `summary_negative_rows` | `summary_test_methods` | `evidence_scope` |
|---|---|---|---:|---:|---:|---:|---|
| `V2-0105` | `ARTIFACT_01` | `nerve_factorization_controls.csv` | 280 | 17 | 0 | empty | `V1_BODY_BYTE_IDENTITY` |
| `V2-0106` | `ARTIFACT_02` | `circle_multiplier_cocycle_controls.csv` | 500 | 20 | 0 | empty | `V1_BODY_BYTE_IDENTITY` |
| `V2-0107` | `ARTIFACT_03` | `lift_integer_defect_controls.csv` | 500 | 20 | 0 | empty | `V1_BODY_BYTE_IDENTITY` |
| `V2-0108` | `ARTIFACT_04` | `gauge_coboundary_controls.csv` | 196 | 19 | 0 | empty | `V1_BODY_BYTE_IDENTITY` |
| `V2-0109` | `ARTIFACT_05` | `twisted_convolution_controls.csv` | 78 | 23 | 0 | empty | `V1_BODY_BYTE_IDENTITY` |
| `V2-0110` | `ARTIFACT_06` | `twisted_involution_controls.csv` | 54 | 26 | 0 | empty | `V1_BODY_BYTE_IDENTITY` |
| `V2-0111` | `ARTIFACT_07` | `completion_gauge_controls.csv` | 756 | 28 | 0 | empty | `V1_BODY_BYTE_IDENTITY` |
| `V2-0112` | `ARTIFACT_08` | `action_period_nonretention_controls.csv` | 56 | 20 | 0 | empty | `V1_BODY_BYTE_IDENTITY` |
| `V2-0113` | `ARTIFACT_09` | `negative_domain_controls.csv` | 20 | 12 | 20 | empty | `V1_BODY_BYTE_IDENTITY` |
| `V2-0114` | `ARTIFACT_10` | `actual_standard_support_transfer_controls.csv` | 96 | 21 | 27 | empty | `V1_BODY_BYTE_IDENTITY` |
| `V2-0115` | `ARTIFACT_11` | `target_summary.csv` | 12 | 11 | 0 | empty | `V1_BODY_BYTE_IDENTITY` |
| `V2-0116` | `ARTIFACT_12` | `completion_corona_controls_v2.csv` | 117 | 41 | 20 | empty | `V2_NEW_BODY` |
| `V2-0117` | `PACKAGE` | `PACKAGE_TOTAL_V2` | 2665 | `MIXED` | 67 | 176 | `V2_PACKAGE_AGGREGATE` |

The self-summary row contains only count and width metadata.  It has no byte
count or digest.  The package row is recomputed from the twelve preceding
artifact rows; it is not copied from constants.  The v1 `target_summary.csv`
continues to verify its own immutable v1 snapshot, while this block verifies
the augmented package.

## 9. Aggregate artifact, row, negative, and reproduction targets

The exact augmented targets are:

```text
DESIGN_SCHEMA_V1=paper13-circle-twists-controls/1
DESIGN_SCHEMA_V2=paper13-circle-twists-controls/2
MANIFEST_SCHEMA=paper13-circle-twists-controls-manifest/2
HEADER_WIDTHS=17,20,20,19,23,26,28,20,12,21,11,41
CSV_ARTIFACTS=12
GENERATED_ARTIFACTS_INCLUDING_MANIFEST=13
MANIFEST_BINDING_PATHS=24
V1_CSV_BODY_ROWS_BYTE_IDENTICAL=2548
V2_NEW_CSV_BODY_ROWS=117
CSV_BODY_ROWS=2665
V1_EXPLICIT_NEGATIVE_ROWS=47
V2_NEW_EXPLICIT_NEGATIVE_ROWS=20
EXPLICIT_NEGATIVE_ROWS=67
EXPECTED_NEGATIVES_DETECTED=67
NEGATIVE_FAILURES=0
UNITTEST_METHODS=176
UNITTEST_FAILURES=0
UNITTEST_ERRORS=0
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
TOLERANCE_POLICY=EXACT_ZERO
```

The arithmetic is exact:

```text
2548+117=2665,
47+20=67,
11+1=12 CSV artifacts,
12+1 manifest=13 generated artifacts,
128+48=176 unittest methods
```

## 10. Exact 176-test audit budget

The amended suite exposes exactly 176 independently discoverable
`unittest` methods.  A loop inside one method counts as one.  The original 128
method allocation is retained: all 91 v1 per-CSV methods still verify the
same eleven bodies, while the 13 package/manifest, 8 reproduction, and 12
tamper methods use the augmented artifact set and v2 manifest; the 4 recursive
entry/cache/cleanup methods remain.  The old target-summary tests continue to
verify the v1 snapshot rather than overwriting it.

The 48 new methods are:

| New v2 test family | Exact methods | Required surface |
|---|---:|---|
| `v2_schema_registry_order` | 4 | exact 41-column header, family registry, contiguous IDs, block order/formulas |
| `finite_c0_coordinate_models` | 5 | three finite owners, three scalar inputs, constant coordinate norms, multiplier/algebra membership, zero finite corona map |
| `infinite_analytic_boundary` | 6 | two generic infinite owners, zero/nonzero split, multiplier-versus-algebra distinction, quotient distance/injectivity branch, fixed-prime unconditional rows, finite-controls ceiling |
| `finite_tail_quotient_models` | 5 | two `(m,n)` ideals, exact sup quotient distance, zero/nonzero image, injective scalar model, not-an-actual-corona scope |
| `v2_gauge_commutation` | 4 | `K24 x TG`, frozen orientation, independent left/right exponents, completion-extension firewall |
| `max_reduced_evidence` | 4 | max token, reduced token, amenable endpoint pair, separate evidence/Route split rule |
| `owner_credit_firewall` | 5 | Paper-2 zero-credit rule, actual/bare split, standard unit/arrow owners, discrete quotient, generic bare index |
| `v2_negative_registry` | 5 | exact 20-row registry/order, finite-as-theorem rejections, owner/credit rejections, multiplier/corona/gauge/evidence rejections, manifest authority/self/proof rejections |
| `v2_summary_aggregates` | 3 | twelve artifact rows, self-row, `2665/67/176` package arithmetic |
| `v2_manifest_dag` | 3 | schema and exact binding union, implementation/artifact hashes, no proof/self cycle |
| `v2_reproduction_tamper_cache` | 4 | verify-only immutability, three-way 13-artifact equality, v2 design/gate/new-CSV tamper rejection, pre/post cache and residue rejection |
| **New methods** | **48** | exact |

The full allocation is therefore:

```text
INHERITED_OR_AMENDED_V1_METHODS=128
NEW_V2_METHODS=48
UNITTEST_METHODS=176
```

Adding, removing, merging, or parametrically hiding a discoverable method
requires a new versioned design amendment and independent review.

## 11. Manifest v2 and dependency DAG

### 11.1 Exact manifest authority bindings

The future `results/manifest.json` has schema
`paper13-circle-twists-controls-manifest/2`.  Its `design_head` is

```text
{path: notes/phase3_control_design_amendment_v2.md,
 sha256: <externally computed final digest of this file>}
```

This file does not embed its own digest.  The manifest additionally binds the
following exact v2 authority set:

| Binding path | SHA-256 |
|---|---|
| `notes/phase3_control_design_lock.md` | `900c541713b1711bdab7fa0d264355b6d8ee27014094e60eac6aabe38190604c` |
| `notes/phase3_control_design_amendment_v1.md` | `5c9caea983b0047c4b16d0437c23b117a6b8150bbeb67b79c60fb9b2ba6a737e` |
| `notes/phase3_control_design_review.md` | `bf56b96e19b682600ed5de43f7df51ef381fe82d4e12363f66cd1e7d2a5a5184` |
| `notes/phase3_standalone_review.md` | `0397e1555a1ff07d30f06c3182b6cf570228ccd3e8db9e3c96666d118079c224` |
| `notes/phase3_standalone_amendment_v2.md` | `99c796bffe24f262d8ac8458b21fd253451bca51bac4b283660dab319992ed82` |
| `notes/phase3_standalone_amendment_v2_ownership_addendum.md` | `d9523d1692d60fbdff7bbf5ab6c00d44bdcd26f02dc5cdeeba8c7ba43d78a39f` |
| `notes/phase3_v2_methodology_review.md` | `96a5067015847ff88155b91658ae94e9ef5a6355ae176c1945644b3e729f4f74` |
| `notes/phase3_v2_devils_advocate.md` | `1c6bbb0bc7d3fc366de4d8a4eb869d4d4708f19647f10d780be095ac9e81f110` |
| `notes/phase3_v2_source_feasibility.md` | `3ce4e8db7914c0053a31b7e0e08e8f0fe02e0b2db15620f194c1ccae5ffeb320` |
| `notes/phase3_v2_design_gate.md` | `0094462b1e06cde0cf1fcc3536c608dcd96ef1e9eb0d85a0714df1666b799706` |
| `papers/2-flow-zeta/paper/manuscript.tex` | `72c34a0a30279ed7c070917a2c9242b8e9cb0a37a56779c246fa2cae04097fdc` |
| `papers/2-flow-zeta/notes/proof_audit.md` | `aaab83c32eb9d6c172be192dbb14acc6ed927a972d61c24a90dbfe94ecd0dbae` |

The twelve Phase-1/Phase-2/source binding paths and hashes in base-design
Section 2 remain mandatory and are unioned with this table.  The manifest's
canonical `bindings` array is the path-sorted union; duplicate paths are
rejected.  The two sets are disjoint, so `bindings` has exactly 24 entries.
Any mismatch is fail-closed.

### 11.2 Exact canonical manifest blocks

The future canonical JSON contains these semantic blocks:

```text
schema_version = paper13-circle-twists-controls-manifest/2
package_id = paper13-circle-twists-controls-v2
design_head = {path, sha256}
bindings = path-sorted exact union from Section 11.1 and base Section 2
proof_binding = {
  concurrent_phase3_proof_hash_included: false,
  policy: POST_PROOF_AUDIT_BINDS_SEPARATELY
}
implementation = path-sorted [{path, bytes, sha256}] for six files
artifacts = ordered [{path, schema, columns, rows, negative_rows, bytes, sha256}]
legacy_v1 = {
  csv_bodies_byte_identical: true,
  csv_count: 11,
  body_rows: 2548,
  negative_rows: 47,
  target_summary_role: V1_SNAPSHOT_ONLY
}
aggregates = the exact Section-9 targets
reproduction = {
  deterministic: true,
  random_used: false,
  network_used: false,
  fresh_generations: 2,
  byte_identical_copies: 3
}
status = PASS
```

The six future implementation paths remain exactly:

```text
code/generate_controls.py
code/test_controls.py
code/README.md
experiments/reproduce.sh
experiments/README.md
results/README.md
```

The twelve artifact entries use the Section-8 order and exact path rule
`results/<summary_artifact>`.  The first eleven have schema `/1`;
`completion_corona_controls_v2.csv` has schema `/2`.  The manifest records
the byte count and SHA-256 of every implementation file and CSV, but not
itself.

No proof path, proof byte count, proof digest, proof-derived value, or key
matching `proof.*sha` is permitted.  The required false sentinel remains
legal and does not authorize a proof binding.  A later integrated audit may
bind a stable proof digest and the stable controls-manifest digest as two
separate inputs; the controls manifest is never mutated to add the proof.

### 11.3 Acyclic dependency graph

The only allowed dependency graph is:

```text
frozen Phase-1/2/source locks -------------------+
frozen amended-v1 design/review ----------------+
frozen v2 theorem/ownership/reviews/gate -------+--> frozen v2 control design
Paper-2 owner locks ----------------------------+              |
                                                               v
                                               six implementation files
                                                               |
                                                               v
                                                    twelve CSV artifacts
                                                               |
                                                               v
                                                     manifest.json

stable P13-8A--C proof -------------------------+--> later integrated audit
stable controls manifest ----------------------+--> later integrated audit
```

The manifest does not list itself.  Neither summary CSV contains a digest.
The v2 design does not contain its own digest.  Implementation files contain
no manifest digest.  The proof and control branches meet only in a later
independent audit, so there is no self-hash, proof race, or proof/control
circularity.

## 12. Verify-only, fresh-generation, tamper, and no-cache gates

The sole future top-level entry remains
`papers/13-circle-twists/experiments/reproduce.sh`.  In addition to every v1
requirement, it must satisfy this exact augmented contract:

1. verify the checked-in twelve CSVs and manifest read-only before any fresh
   generation; record and compare their bytes before and after verify-only;
2. reject a missing or extra file or directory and reject a v1-body byte that
   differs from the amended-v1 specification;
3. generate into two distinct newly created empty `mktemp -d` roots;
4. verify each fresh package independently;
5. byte-compare all thirteen generated artifacts across checked-in, fresh A,
   and fresh B;
6. discover and run exactly 176 `unittest` methods;
7. retain `LC_ALL=C`, `TZ=UTC`, `PYTHONHASHSEED=0`,
   `PYTHONDONTWRITEBYTECODE=1`, and `python3 -B`;
8. reject recursive entry and require external serialization of top-level
   runs; and
9. remove both temporary roots by exit trap on success or failure.

`--verify-only` may open artifacts only for reading.  It may not repair,
rewrite, normalize, touch, chmod, rename, regenerate, or update the manifest.
Any attempted write is a failure.  Its before/after metadata receipt compares
relative path, file type, mode, size, and nanosecond modification time;
access time is excluded because a read may update it.

At minimum, isolated tamper tests must reject:

- new-CSV content, header, row count, row order, owner token, evidence token,
  negative detector, or summary aggregate drift;
- any byte drift in the eleven preserved v1 CSV bodies;
- missing/extra CSVs, manifest entries, files, or directories;
- the v2 design-head digest, authorization-gate digest, amended-v1 chain,
  theorem/ownership/review lock, Paper-2 lock, implementation digest, or
  artifact digest drifting or disappearing;
- a manifest self-entry or self-digest;
- any proof path, proof digest, non-null concurrent-proof sentinel, or
  proof-derived oracle value;
- substitution of v1 conditional `Q_p` rows for the v2 unconditional branch;
  and
- verify-only rewriting a byte or metadata.

Before and after every checked-in verification, fresh generation, test run,
and failure-path cleanup, the checked-in tree and both temporary roots must be
free of:

```text
__pycache__
*.pyc
*.pyo
.pytest_cache
.mypy_cache
```

Any pre-existing cache in a controlled root is rejected rather than deleted
or ignored.  Any newly created cache or task temporary residue is a failure.
No retry is automatic.

## 13. Design audit and gate consequence

| Required v2 surface | Frozen receipt | Finding |
|---|---|---|
| Prior package preservation | eleven `/1` CSV bodies and v1 snapshot summary byte-identical | none |
| New artifact | one 41-column `/2` CSV, 117 exact rows and contiguous IDs | none |
| Finite `c0` diagnostics | `QF1,QF2,QF4`, zero/unit/phase inputs, max/r split | none |
| Infinite analytic boundary | generic countable/uncountable and fixed-prime rows; never a finite surrogate | none |
| Coordinate norm | exact constant-zero/constant-one models and membership consequences | none |
| Multiplier versus algebra | separate booleans and a dedicated conflation negative | none |
| Quotient/corona | finite tail distance models plus separately typed analytic corona branch | none |
| Gauge covariance | exact `K24 x TG x {max,r}` term square and extension firewall | none |
| Max/reduced status | separate obligation tokens and pre-Route split protection | none |
| Paper-2 credit | exact inherited lower-bound owner and zero-credit negative | none |
| Owner firewall | actual, bare, standard unit/arrow, and discrete quotient ledgers and negatives | none |
| Fixed-prime branch | unconditional analytic branch; v1 conditional rows retained only as historical diagnostics | none |
| Finite-controls ceiling | continuum, arbitrary-index, norm-chain, and corona proof promotions rejected | none |
| Summary and totals | `12 CSV / 2665 rows / 67 negatives / 176 tests` | none |
| Manifest DAG | design/gate/locks/implementation/artifacts bound; no proof/self hash | none |
| Reproduction integrity | verify-only, two fresh roots, three-way bytes, tamper and no-cache gates | none |

Finding register for this design amendment:

| Severity | Count | Open item |
|---|---:|---|
| Critical (`C`) | 0 | none |
| Major (`M`) | 0 | none |
| Minor (`m`) | 0 | none |

```text
P13_CONTROL_DESIGN_AMENDMENT_V2=FROZEN_CANDIDATE
V2_CONTROL_DESIGN_INDEPENDENT_REVIEW_REQUIRED=true
V2_CONTROL_DESIGN_PASSED=false
BASE_DESIGN_SHA256=900c541713b1711bdab7fa0d264355b6d8ee27014094e60eac6aabe38190604c
DESIGN_AMENDMENT_V1_SHA256=5c9caea983b0047c4b16d0437c23b117a6b8150bbeb67b79c60fb9b2ba6a737e
FINAL_V1_DESIGN_REVIEW_SHA256=bf56b96e19b682600ed5de43f7df51ef381fe82d4e12363f66cd1e7d2a5a5184
V2_DESIGN_GATE_SHA256=0094462b1e06cde0cf1fcc3536c608dcd96ef1e9eb0d85a0714df1666b799706
V1_CSV_BODIES_CHANGED=false
V2_NEW_CSV=completion_corona_controls_v2.csv
CSV_ARTIFACTS=12
GENERATED_ARTIFACTS=13
MANIFEST_BINDING_PATHS=24
CSV_BODY_ROWS=2665
EXPLICIT_NEGATIVES=67
UNITTEST_METHODS=176
FINITE_CONTROLS_PROVE_CONTINUUM=false
FINITE_CONTROLS_PROVE_ARBITRARY_INDEX_MULTIPLIER=false
FINITE_CONTROLS_PROVE_CORONA_FAITHFULNESS=false
CONCURRENT_PROOF_HASH_INCLUDED=false
MANIFEST_SELF_HASH_PRESENT=false
CONTROL_IMPLEMENTATION_AUTHORIZED=false
CONTROL_IMPLEMENTATION_PERFORMED=false
CONTROL_EXECUTION_PERFORMED=false
STANDALONE_PASS=false
NOTE_OR_MERGE_BINDING=true
ROUTE_A_AUTHORIZED=false
ROUTE_B_INVOCATION_ALLOWED=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
CRITICAL_OPEN=0
MAJOR_OPEN=0
MINOR_OPEN=0
```

The exact bytes are ready for an independent design review.  This candidate
does not pass its own review gate.  No implementation, execution, result,
proof-by-control inference, Route, composition, manuscript, citation,
standalone, release, Git, or public synchronization is authorized.
