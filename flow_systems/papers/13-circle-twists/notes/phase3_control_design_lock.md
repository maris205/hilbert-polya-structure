# Paper 13 Phase-3 deterministic-control design lock

Status: **FROZEN DESIGN CANDIDATE / INDEPENDENT DESIGN REVIEW REQUIRED**  
Version: **P13-CONTROLS-v1.0**  
Date: **2026-08-15 (Asia/Shanghai)**  
Design audit: **C0 / M0 / m0**  
Control implementation or execution performed here: **no**  
`route_b_invocation_allowed: false`

## Material Passport

- Origin Skill: ARS experiment-agent plus academic-pipeline integrity workflow
- Origin Mode: plan / deterministic-control integrity design
- Origin Date: 2026-08-15
- Verification Status: UNVERIFIED
- Version Label: `p13_control_design_v1`
- Upstream Gate: `phase2_final_review.md`, SHA-256
  `ffcfbac5768fc409b3fa9e5df4f3b46a2366f553373664c78f4364d456854cd9`
- Scope: schema and reproducibility design only; no theorem, proof, code, result,
  Route, manuscript, or release claim

## 1. Authority and hard boundary

The Phase-2 integrated gate authorizes a separate deterministic-control
**design lock only**. This file freezes that design for the ten inherited CSV
names and the new central support-transfer CSV. It does not authorize an
implementation or a run. A later independent reviewer must accept this exact
file before implementation can begin.

The controls are witnesses, sign checks, finite falsifiers, and deterministic
provenance records. They do not prove any universal continuous-cohomology
claim, any statement about every action, density of a subgroup, compactness of
an infinite coproduct, or the finiteness of the rational-Witt orbit set. In
particular:

- the finite time grids do not prove `H^2_tw(R;T)=0`;
- the finite rational window for `H=Q` does not prove density or license Haar,
  regular-representation, locally compact, or completion claims on `Q`;
- an `R^2` row is an excluded-domain counterexample to a dimension-free proof,
  not an object of the one-dimensional theorem;
- infinite-`Q` support rows use the analytic branch predicate
  `f=0 or Q is finite`; they never replace infinity by a large finite number;
  and
- the fixed-prime rows are conditional in the bare set `Q_p` and make no
  finiteness, infinitude, cardinality, topology, enumeration, or measure claim.

## 2. Exact upstream gate tuple

The future manifest must bind the following exact, independently rehashed
bytes. A mismatch is fail-closed.

| Binding path | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `519563a28c3f11e3b3853f6875a84191444a68cd2c032c4cfcf69ca4152d5064` |
| `notes/candidate_lock.md` | `8cc0d08971762aa784afe1c844215353f170a75a3c0ab892415458ab010d0266` |
| `notes/pipeline_state.md` | `d98bf49d2eb5c1905ea3625251d787b247f3cf19577ff40f8bc0136186280fd5` |
| `notes/phase1_amendment_v1.md` | `ea5242ba6a8a1f2f867e8b258abc802fdeaace54db76629f0a9f0629e3e90d27` |
| `notes/phase1_final_gate.md` | `8a97a0bedcb048f1c9aa7db18d43bde45b17f1d7e92d38d2eeace688c64aee19` |
| `notes/phase2_novelty_search.md` | `444507f623a998152fdc8e427ee8a3f917c11d5823278b110d431dbcacac6eea` |
| `notes/phase2_convention_owner_audit.md` | `498830945b10a9213da945710d21b7ea74d9e0747864e23ca6223efc9bb74f52` |
| `notes/phase2_framework_source_audit.md` | `b47b1d6319c8419d96ca8679e3ff13b531a58f06a8b14afd95ec11f773345592` |
| `notes/phase2_final_review.md` | `ffcfbac5768fc409b3fa9e5df4f3b46a2366f553373664c78f4364d456854cd9` |
| `notes/sources/framework_source_manifest.md` | `4712cabd696d6d00205eb1eddd3c0d2dbf6706bfa14c097690a278941128606e` |
| `notes/sources/framework_sources.sha256` | `7fe6067bfc8e16e8b0447df295a887d48c2c04fa5ba25c9cca8acc7afade733f` |
| `notes/sources/.gitignore` | `c36e58e6a0e338579a7be747879a2891b023bfb79a676da58afca5e1b94c86be` |

The manifest must additionally bind this design file by its externally
computed final SHA-256. This file does not embed its own digest.

## 3. Global exact-arithmetic and serialization contract

### 3.1 Schema and phase representation

Every CSV row carries the literal schema value
`paper13-circle-twists-controls/1`. The manifest schema is
`paper13-circle-twists-controls-manifest/1`.

Let `zeta=exp(2*pi*i/24)` be notation only. The implementation must never
evaluate this exponential. A circle phase is stored as its least
nonnegative exponent `e mod 24` in `{0,...,23}`. Set

```text
sigma_k(t,u) exponent = 2*k*t*u mod 24,
alpha_k(t) exponent  = -k*t^2 mod 24.
```

Thus `sigma_k(t,u)=exp(i*kappa_k*t*u)` and
`alpha_k(t)=exp(-i*kappa_k*t^2/2)` with `kappa_k=pi*k/6`, and the frozen
coboundary sign gives `delta alpha_k=sigma_k` exactly. The main phase-index
set is

```text
K24 = (-6,-1,0,6).
```

For exact convolution and operator diagnostics use
`KG=(-6,0,6)`. All resulting exponents are multiples of six and are mapped
without floating point as

```text
0 -> (1,0), 6 -> (0,1), 12 -> (-1,0), 18 -> (0,-1)
```

in the Gaussian integers. Rational values, if introduced by a future
implementation, must use reduced `numerator/denominator` strings with a
positive denominator. No binary floating-point result is an oracle.

For the lift ledger define the centered representative

```text
pr24(n) = ((n+12) mod 24)-12 in {-12,...,11}.
```

If `r_ab=pr24(2*k*a*b)`, the lifted cocycle defect numerator is

```text
D24 = r_tu + r_(t+u,v) - r_uv - r_(t,u+v).
```

The exact oracle is `D24 mod 24 = 0`; `D24/24` is the integer multiplying
`2*pi`. This makes the `exp(iq)`/`2*pi*Z` distinction explicit without a
transcendental tolerance.

### 3.2 CSV bytes

All eleven CSVs use UTF-8 without BOM, LF line endings, and the Python
standard-library `csv.writer` contract

```text
delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL,
doublequote=true, escapechar=None, lineterminator="\n"
```

with files opened using `newline=""`. Additional canonical rules are:

- exact header order as frozen below;
- no leading or trailing whitespace in fields;
- empty optional value serialized as the empty field, never `NA`, `null`, or
  a space;
- booleans serialized only as `true` or `false`;
- integers serialized in base ten with no leading `+` and no leading zero,
  except the literal `0`;
- row IDs use the fixed prefix and zero-padded width stated below;
- enumeration order, not locale order or hash-map order, controls rows;
- where present, `case_kind` is one of `POSITIVE`, `DIAGNOSTIC`,
  `NEGATIVE`, `SUMMARY`;
- where present, every nonnegative row has an empty `negative_reason`;
- where present, every negative row has exactly one registered reason below;
- `status` is `PASS` only when the row's independent oracle matches its
  stored result; and
- where present, `tolerance` is the literal `0`. The summary's corresponding
  `tolerance_policy` is `EXACT_ZERO`. There is no approximate comparison in
  v1.

The future JSON manifest uses UTF-8, LF, and
`json.dumps(..., ensure_ascii=False, sort_keys=True, indent=2) + "\n"`.
Timestamps, absolute paths, host names, process IDs, temporary paths, and
unordered mappings are prohibited from generated bytes.

## 4. Shared finite fixtures

Time grids are ordered numerically:

```text
T1=(-2,-1,0,1,2), T2=(-1,0,1), T3=(-3,-2,-1,0,1,2,3),
TOUT=(-6,-5,...,5,6), TSTAR=(-4,-3,...,3,4),
SHIFT=(-1,0,2), TEVAL=(-3,-2,-1,0,1,2,3).
```

The two ordered finite-sequence fixtures, with omitted entries equal to
zero, are

```text
C1:
  f={-2:1,-1:-2,0:3,1:1}
  g={-1:2,0:-1,2:1}
  h={-2:-1,0:2,1:1,2:-2}

C2:
  f={-1:1,0:2,2:-1}
  g={-2:2,1:-1,2:2}
  h={-1:-2,0:1,2:1}
```

For product/star diagnostics only, define the finite-lattice sum

```text
(f star_sigma g)(t)=sum_u f(u)g(t-u)sigma(u,t-u).
```

It is deliberately labelled `FINITE_LATTICE_SIGN_DIAGNOSTIC_ONLY`; it is
not the Lebesgue integral on `C_c(R)`.

The ordered regular-representation vectors are

```text
V1={-2:1,0:2,1:-1},
V2={-1:1,1:1,2:2}.
```

For `m in (0,1)`, set `chi_m(t)=zeta^(6*m*t)=i^(m*t)` and
`beta=chi_m*alpha`. These exact character rows test the direction of choice
independence, never the universal completion theorem.

## 5. Exact per-CSV contracts

### 5.1 `nerve_factorization_controls.csv`

Exact 17-column header:

```text
schema_version,row_id,owner_case,degree,cochain_profile,unit_id,t,u,actual_exp_mod24,time_exp_mod24,normalized,factors_through_time,case_kind,negative_reason,oracle,tolerance,status
```

Owner/unit order is

```text
SINGLETON:(star);
TRIVIAL_TWO:(a,b);
PERIOD_THREE_SAMPLE:(p0,p1,p2);
HETEROGENEOUS_SAMPLE:(free0,period0,fixed0,dense0).
```

Degree-one profiles are `A_ZERO(t)=0` and
`A_LINEAR3(t)=3*t mod 24` on `T1`. Degree-two profiles are
`S_ZERO(t,u)=0` and `S_QUADRATIC1(t,u)=2*t*u mod 24` on
`T2 x T2`. The actual exponent is generated from the time profile and must
equal it for every listed unit.

Row formula and count:

```text
10 units * (2 profiles * 5 degree-one times
          + 2 profiles * 3 * 3 degree-two times) = 280.
```

Order is owner, unit, degree `1,2`, profile in the order above, then numeric
`t,u`; degree-one `u` is empty. IDs are `NF-0001` through `NF-0280`.
Oracle: exact phase equality plus profile-wide normalization. Negatives: `0`.
The documented scope is
`FINITE_TIME_ONLY_WITNESS_NOT_TOPOLOGICAL_PROOF`.

### 5.2 `circle_multiplier_cocycle_controls.csv`

Exact 20-column header:

```text
schema_version,row_id,k_index,t,u,v,sigma_tu_exp,sigma_tplusu_v_exp,sigma_uv_exp,sigma_t_uplusv_exp,lhs_exp_mod24,rhs_exp_mod24,norm_t0,norm_0u,cocycle_holds,case_kind,negative_reason,oracle,tolerance,status
```

Rows enumerate `k` in `K24`, then lexicographic numeric `(t,u,v)` in
`T1^3`. Both sides are added modulo 24 using the four displayed sigma
fields. Row count is `4*5^3=500`; IDs are `CM-0001` through `CM-0500`.
Oracle: both normalization axes and exact cocycle equality. Negatives: `0`.

### 5.3 `lift_integer_defect_controls.csv`

Exact 20-column header:

```text
schema_version,row_id,k_index,t,u,v,r_tu,r_tplusu_v,r_uv,r_t_uplusv,defect_numerator_24,defect_multiple_2pi,is_integer_multiple,normalization_axes,cocycle_mod24,case_kind,negative_reason,oracle,tolerance,status
```

Rows use the same `K24 x T1^3` order as the cocycle ledger. The four `r`
fields use `pr24`; the defect fields use Section 3.1 exactly. A nonzero
`defect_multiple_2pi` is an expected branch-wrap diagnostic, not a negative.
Row count is `4*5^3=500`; IDs are `LI-0001` through `LI-0500`.
Oracle: `D24` divisible by 24, normalized axes zero, and the phase cocycle
zero modulo 24. Negatives: `0`.

### 5.4 `gauge_coboundary_controls.csv`

Exact 19-column header:

```text
schema_version,row_id,k_index,t,u,alpha_t_exp,alpha_u_exp,alpha_tplusu_exp,delta_alpha_exp,sigma_tu_exp,quotient_sigma_over_one_exp,gauge_direction,normalized_alpha,coboundary_match,case_kind,negative_reason,oracle,tolerance,status
```

Rows enumerate `K24`, then `(t,u)` in `T3^2`. The coboundary exponent is
`alpha(t)+alpha(u)-alpha(t+u) mod 24`. The literal gauge direction in every
row is `A_SIGMA_TO_A_ONE`, expressing `U_alpha:A_sigma->A_1` when
`sigma=delta alpha`. Row count is `4*7^2=196`; IDs are `GC-0001` through
`GC-0196`. Oracle: exact normalization, coboundary equality, quotient
orientation, and direction token. Negatives: `0`.

### 5.5 `twisted_convolution_controls.csv`

Exact 23-column header:

```text
schema_version,row_id,fixture_id,k_index,t,fg_re,fg_im,left_assoc_re,left_assoc_im,right_assoc_re,right_assoc_im,gauge_product_re,gauge_product_im,untwisted_of_gauged_re,untwisted_of_gauged_im,fg_support_within_minkowski,associativity_holds,gauge_product_holds,case_kind,negative_reason,oracle,tolerance,status
```

For each `(fixture,k,t)` compute `f star_sigma g`, both bracketings of
`f,g,h`, and

```text
U_alpha(f star_sigma g) = (U_alpha f) star_1 (U_alpha g)
```

in exact Gaussian integers. Rows enumerate `C1,C2`, `KG`, then `TOUT`.
Row count is `2*3*13=78`; IDs are `TC-0001` through `TC-0078`.
Oracle: coefficient equality, associativity, gauge-product equality, and the
Minkowski support bound. Negatives: `0`. Every row is `DIAGNOSTIC` with
oracle class `FINITE_LATTICE_SIGN_DIAGNOSTIC_ONLY`.

### 5.6 `twisted_involution_controls.csv`

Exact 26-column header:

```text
schema_version,row_id,fixture_id,k_index,t,f_starstar_re,f_starstar_im,f_re,f_im,fg_star_re,fg_star_im,gstar_fstar_re,gstar_fstar_im,actual_star_re,actual_star_im,time_star_re,time_star_im,sigma_inverse_symmetry,star_involutive,anti_multiplicative,actual_time_star_match,case_kind,negative_reason,oracle,tolerance,status
```

The star is

```text
f_star_sigma(t)=conj(sigma(t,-t))*conj(f(-t)).
```

Rows enumerate `C1,C2`, `KG`, then `TSTAR`. They check
`(f_star)_star=f`, `(f star_sigma g)_star=g_star star_sigma f_star`, the
time-only actual fibre formula against the one-object formula, and
`sigma(t,-t)=sigma(-t,t)`. Row count is `2*3*9=54`; IDs are `TI-0001`
through `TI-0054`. Oracle: exact Gaussian equality. Negatives: `0`. Scope is
again a finite sign diagnostic, not a `C_c(R)` proof.

### 5.7 `completion_gauge_controls.csv`

Exact 28-column header:

```text
schema_version,row_id,fixture_id,k_index,character_m,s,u,t,projective_lhs_re,projective_lhs_im,projective_rhs_re,projective_rhs_im,intertwiner_lhs_re,intertwiner_lhs_im,intertwiner_rhs_re,intertwiner_rhs_im,xi_norm_sq,character_times_xi_norm_sq,projective_holds,intertwiner_holds,choice_map_holds,character_isometry_holds,completion_scope,case_kind,negative_reason,oracle,tolerance,status
```

Use the frozen point representation

```text
(lambda_sigma(s)xi)(t)=sigma(s,t-s)xi(t-s)
```

and test

```text
lambda_sigma(s)lambda_sigma(u)
  = sigma(s,u)lambda_sigma(s+u),
M_alpha lambda_sigma(s) M_overline(alpha)
  = alpha(s)lambda(s),
U_beta=C_chi U_alpha,
sum_t |chi(t)xi(t)|^2=sum_t |xi(t)|^2.
```

Rows enumerate `V1,V2`, `KG`, `m=(0,1)`, lexicographic
`(s,u)` in `SHIFT^2`, and `t` in `TEVAL`. Row count is
`2*3*2*3^2*7=756`; IDs are `CG-0001` through `CG-0756`.
Oracle: exact Gaussian matrix-element identities and exact integer squared
norms. Negatives: `0`. Every row carries
`completion_scope=FINITE_MATRIX_ELEMENT_DIAGNOSTIC_ONLY`; it cannot prove
existence, equality, or choice independence of the full/reduced completions.

### 5.8 `action_period_nonretention_controls.csv`

Exact 20-column header:

```text
schema_version,row_id,action_case,component_id,stabilizer_literal,orbit_count_class,k_index,global_time_sample_class,isotropy_restriction_sample_class,test_algebra_sample_signature,full_sample_signature,reduced_sample_signature,dense_h_scope,named_output_signature_matches_baseline,restriction_coboundary_match,case_kind,negative_reason,oracle,tolerance,status
```

The 14 ordered action/component cases are:

| Order | `action_case` | `component_id` | `stabilizer_literal` | `orbit_count_class` |
|---:|---|---|---|---|
| 1 | `SINGLETON_TIME_OWNER` | `star` | `R` | `ONE` |
| 2 | `TRIVIAL_TWO_POINT` | `all` | `R` | `TWO` |
| 3 | `FREE_TRANSLATION` | `free` | `{0}` | `ONE` |
| 4 | `TRANSITIVE_PERIOD_1` | `periodic` | `Z` | `ONE` |
| 5 | `TRANSITIVE_PERIOD_2` | `periodic` | `2Z` | `ONE` |
| 6 | `FIXED_PRIME_2` | `packet` | `(log 2)Z` | `QP_UNKNOWN` |
| 7 | `FIXED_PRIME_3` | `packet` | `(log 3)Z` | `QP_UNKNOWN` |
| 8 | `COMPOSITE_LABEL_6` | `label_control` | `(log 6)Z` | `UNSPECIFIED` |
| 9 | `ARBITRARY_LABEL_A` | `label_control` | `L_a Z` | `UNSPECIFIED` |
| 10 | `NONTRANSITIVE_COMMON_L` | `all` | `LZ` | `FINITE_3` |
| 11 | `HETEROGENEOUS_ACTION` | `free_component` | `{0}` | `HETEROGENEOUS` |
| 12 | `HETEROGENEOUS_ACTION` | `periodic_component` | `LZ` | `HETEROGENEOUS` |
| 13 | `HETEROGENEOUS_ACTION` | `fixed_component` | `R` | `HETEROGENEOUS` |
| 14 | `HETEROGENEOUS_ACTION` | `dense_component` | `Q` | `HETEROGENEOUS` |

Each case is crossed with `K24`, giving `14*4=56` rows, ordered by the
table and then `k`; IDs are `AP-0001` through `AP-0056`. The quadratic
global class and its literal restriction are recorded only as zero
**sample** classes, and the three algebra/completion fields record only the
common finite diagnostic signature. The dense row carries
`dense_h_scope=FINITE_RATIONAL_WINDOW_DIAGNOSTIC_ONLY`; all other rows carry
`NOT_DENSE_H_CONTROL`. Oracle: exact restricted coboundary polynomial
identity and equality of the registered sample signatures. Negatives: `0`.

### 5.9 `negative_domain_controls.csv`

Exact 12-column header:

```text
schema_version,row_id,case_kind,negative_reason,fixture,violated_lock,expected_detector,observed_detector,expected_disposition,oracle,tolerance,status
```

There are exactly 20 rows, in the following order. The future implementation
must construct the listed fixture rather than merely copy the expected
detector string. `status=PASS` means the expected rejection occurred.

| ID | Registered `negative_reason` | Exact fixture or attempted promotion | Expected detector | Disposition |
|---|---|---|---|---|
| `ND-0001` | `NON_T0_COEFFICIENT_TARGET` | unit-dependent map to the two-point indiscrete target | `REJECT_T0_FACTORIZATION_USE` | `DOMAIN_EXCLUDED` |
| `ND-0002` | `MEASURABLE_ONLY_PHASE` | `alpha(t)=1` for `t<=0` and `alpha(t)=-1` for `t>0` | `REJECT_CONTINUITY_DOMAIN` | `DOMAIN_EXCLUDED` |
| `ND-0003` | `DISCONTINUOUS_PHASE` | `alpha(0)=1` and `alpha(t)=-1` for `t!=0`, witnessed along `t_n=1/n` | `REJECT_CONTINUITY_DOMAIN` | `DOMAIN_EXCLUDED` |
| `ND-0004` | `UNNORMALIZED_ONE_COCHAIN` | `alpha(0)=-1` | `REJECT_ONE_COCHAIN_NORMALIZATION` | `ROW_REJECTED` |
| `ND-0005` | `UNNORMALIZED_TWO_COCHAIN` | `sigma(t,0)=-1` | `REJECT_TWO_COCHAIN_NORMALIZATION` | `ROW_REJECTED` |
| `ND-0006` | `WRONG_COBOUNDARY_SIGN` | conjugate of the frozen `delta alpha`, `k=-1,t=u=1` | `COBOUNDARY_MISMATCH` | `ROW_REJECTED` |
| `ND-0007` | `WRONG_GAUGE_ORIENTATION` | `U_overline(alpha):A_sigma->A_1` | `GAUGE_DIRECTION_MISMATCH` | `ROW_REJECTED` |
| `ND-0008` | `TWISTED_PRODUCT_WRONG_SIGMA_ARGUMENT` | replace `sigma(u,t-u)` by `sigma(u,t)`, `k=6,u=1,t=2` | `PRODUCT_GAUGE_OR_ASSOCIATIVITY_MISMATCH` | `ROW_REJECTED` |
| `ND-0009` | `TWISTED_STAR_OMITS_COCYCLE` | omit `overline(sigma(t,-t))`, `k=6,t=1` | `STAR_INVOLUTION_MISMATCH` | `ROW_REJECTED` |
| `ND-0010` | `REGULAR_TRANSLATION_WRONG_DIRECTION` | use `xi(t+s)` in place of `xi(t-s)` on `V1,s=1,t=0` | `PROJECTIVE_LAW_MISMATCH` | `ROW_REJECTED` |
| `ND-0011` | `INTERTWINER_CONJUGATIONS_SWAPPED` | swap `M_alpha` and `M_overline(alpha)` on `V2,k=6,s=1,t=0` | `INTERTWINER_MISMATCH` | `ROW_REJECTED` |
| `ND-0012` | `R2_NONSYMMETRIC_COMMUTATOR` | `omega(s,t)=exp(i*pi*s_1*t_2/2)`, `s=(1,0)`, `t=(0,1)`; commutator exponent mod 4 is `1` | `NONTRIVIAL_R2_COMMUTATOR` | `ONE_DIMENSION_ONLY` |
| `ND-0013` | `DENSE_H_HAAR_COMPLETION_PROMOTION` | promote finite rational-window `Q` diagnostics to a Haar/completion theorem | `REJECT_DENSE_H_ANALYTIC_PROMOTION` | `CLAIM_BLOCKED` |
| `ND-0014` | `HETEROGENEOUS_AS_COMMON_LATTICE` | apply the common-`LZ` support theorem to `{0},LZ,R,Q` components | `REJECT_COMMON_STABILIZER_HYPOTHESIS` | `CLAIM_BLOCKED` |
| `ND-0015` | `ACTUAL_STANDARD_REVERSE_IDENTITY` | assert continuity of `G_actual->G_std` without proof | `REJECT_J_DIRECTION` | `CLAIM_BLOCKED` |
| `ND-0016` | `INFINITE_Q_FINITE_SURROGATE_AS_PROOF` | replace infinite `Q` by a finite `Q_1000` and infer compactness/noncompactness | `REJECT_FINITE_AS_INFINITE_PROOF` | `CLAIM_BLOCKED` |
| `ND-0017` | `FIXED_PRIME_Q_CARDINALITY_INFERENCE` | infer `Q_p` finite or infinite from the period label | `REJECT_QP_CARDINALITY_INFERENCE` | `CLAIM_BLOCKED` |
| `ND-0018` | `STANDARD_ACTUAL_GROUPOID_CSTAR_TRANSFER` | rename transported records as standard actual-groupoid completions | `REJECT_OWNER_FRAMEWORK_TRANSFER` | `CLAIM_BLOCKED` |
| `ND-0019` | `FINITE_CONTROL_UNIVERSAL_H2_PROOF` | promote the finite phase grid to `H^2_tw(R;T)=0` | `REJECT_CONTROL_AS_PROOF` | `CLAIM_BLOCKED` |
| `ND-0020` | `CONCURRENT_PROOF_HASH_BINDING` | insert any non-null proof hash or proof path into the controls manifest | `REJECT_PROOF_HASH_BINDING` | `MANIFEST_REJECTED` |

All rows have `case_kind=NEGATIVE`, `tolerance=0`, and exact detector-token
equality as their oracle. Explicit negatives: `20`.

### 5.10 `actual_standard_support_transfer_controls.csv`

Exact 21-column header:

```text
schema_version,row_id,q_case,q_class,q_cardinality,function_id,is_zero,support_components,gauge_id,gauge_nowhere_zero,actual_support_quasicompact,standard_support_compact,lands_in_standard_cc,support_preserved,fixed_prime_conditional,evidence_scope,case_kind,negative_reason,oracle,tolerance,status
```

Ordered orbit-set cases are

```text
QF1:FINITE:1,
QF2:FINITE:2,
QF4:FINITE:4,
QF7:FINITE:7,
QINF_N:INFINITE:INF,
QINF_Z:INFINITE:INF,
QP_FINITE_CONDITIONAL:QP_FINITE_CONDITIONAL:FINITE_UNSPECIFIED,
QP_INFINITE_CONDITIONAL:QP_INFINITE_CONDITIONAL:INFINITE_ASSUMED.
```

Ordered continuous piecewise-linear functions and exact supports are

```text
ZERO: 0, support EMPTY;
TENT_CENTER: max(1-|t|,0), support [-1,1];
TENT_SHIFT: max(1-|t-2|,0), support [1,3];
TWO_BUMP: max(1-|t+2|,0)+max(1-|2*t-3|,0),
          support [-3,-1]|[1,2].
```

Ordered gauges are `ONE`, `ALPHA_K_MINUS6`, `ALPHA_K_6`. All are
circle-valued and nowhere zero. Rows enumerate orbit case, function, then
gauge, so the count is `8*4*3=96`; IDs are `ST-0001` through `ST-0096`.

The exact oracle is

```text
actual_support_quasicompact = true,
standard_support_compact = is_zero or q_class is FINITE
                           or QP_FINITE_CONDITIONAL,
lands_in_standard_cc = standard_support_compact,
support_preserved = true.
```

The two `QP_*` branches are explicitly conditional; they do not decide the
actual `Q_p`. Finite rows use `evidence_scope=FINITE_COMPONENT_DIAGNOSTIC`.
`QINF_N` and `QINF_Z` use
`ANALYTIC_INFINITE_COPRODUCT_BRANCH_ONLY`; the two fixed-prime branches use
`CONDITIONAL_QP_BRANCH_ONLY`.

A row is `NEGATIVE` exactly when the function is nonzero and its orbit case
is `QINF_N`, `QINF_Z`, or `QP_INFINITE_CONDITIONAL`. This gives
`3 orbit cases * 3 nonzero functions * 3 gauges = 27` detected negative
rows. The first two use reason `NONZERO_INFINITE_Q_NOT_COMPACT`; the
fixed-prime branch uses
`CONDITIONAL_NONZERO_QP_INFINITE_NOT_COMPACT`. All other rows are
`POSITIVE`. Tolerance is `0` throughout.

### 5.11 `target_summary.csv`

Exact 11-column header:

```text
schema_version,row_id,artifact,expected_rows,expected_columns,expected_negative_rows,oracle_class,tolerance_policy,canonical_order_key,scope,status
```

Rows `TS-0001` through `TS-0011` summarize, in Sections 5.1--5.11 order,
each of the eleven CSVs, including the self-row for `target_summary.csv`.
`TS-0012` is `PACKAGE_TOTAL`. The self-row expects 12 body rows and 11
columns; it contains no digest and creates no hash cycle. The package row
uses `expected_columns=MIXED`, `canonical_order_key=ARTIFACT_ORDER_ABOVE`,
and the aggregate values frozen in Section 7. Row count: `12`. Negatives:
`0`.

## 6. Oracle, case-kind, negative-reason, and tolerance registry

The literal `oracle` and row-kind policies are frozen as follows. Every
listed non-summary row has `tolerance=0`; the summary has
`tolerance_policy=EXACT_ZERO`.

| Artifact | Literal `oracle` / `oracle_class` | `case_kind` policy | Negative rows |
|---|---|---|---:|
| `nerve_factorization_controls.csv` | `TIME_PHASE_EQUALITY_AND_NORMALIZATION` | all `DIAGNOSTIC` | 0 |
| `circle_multiplier_cocycle_controls.csv` | `NORMALIZED_COCYCLE_MOD24` | all `DIAGNOSTIC` | 0 |
| `lift_integer_defect_controls.csv` | `LIFT_DEFECT_IN_2PI_Z` | all `DIAGNOSTIC` | 0 |
| `gauge_coboundary_controls.csv` | `FROZEN_SIGN_COBOUNDARY_AND_DIRECTION` | all `DIAGNOSTIC` | 0 |
| `twisted_convolution_controls.csv` | `FINITE_GAUSSIAN_PRODUCT_ASSOC_GAUGE` | all `DIAGNOSTIC` | 0 |
| `twisted_involution_controls.csv` | `FINITE_GAUSSIAN_STAR_LAWS` | all `DIAGNOSTIC` | 0 |
| `completion_gauge_controls.csv` | `FINITE_REGULAR_INTERTWINER_CHARACTER` | all `DIAGNOSTIC` | 0 |
| `action_period_nonretention_controls.csv` | `QUADRATIC_RESTRICTION_SIGNATURE_DIAGNOSTIC` | all `DIAGNOSTIC` | 0 |
| `negative_domain_controls.csv` | `EXPECTED_DETECTOR_TOKEN` | all `NEGATIVE` | 20 |
| `actual_standard_support_transfer_controls.csv` | `ZERO_OR_FINITE_Q_SUPPORT_BRANCH` | Section 5.10 rule | 27 |
| `target_summary.csv` | `COUNT_SCHEMA_NEGATIVE_TOTAL` | no `case_kind` column; summary rows only | 0 |

For every artifact with an `oracle` column, the literal above is repeated in
each row. In `target_summary.csv`, the literal appears as `oracle_class`.

The complete allowed nonempty `negative_reason` set is the 20 labels in
Section 5.9 plus these two support labels:

```text
NONZERO_INFINITE_Q_NOT_COMPACT
CONDITIONAL_NONZERO_QP_INFINITE_NOT_COMPACT
```

No other nonempty label is legal in v1. Duplicate use is permitted only for
the 27 support rows prescribed above. There are exactly 47 negative rows:
20 domain/firewall rows plus 27 support-obstruction rows. Every negative
must be detected; an expected negative that passes the prohibited claim is a
test failure.

All v1 arithmetic is exact and every present CSV `tolerance` field is `0`;
the summary uses `EXACT_ZERO`. The
implementation must fail if it encounters a nonzero tolerance, a float,
`NaN`, infinity, a decimal approximation to `pi`, or a call to a
transcendental function in an oracle path. Human-readable formulas such as
`log(2)Z` and `2*pi*Z` are domain labels, not evaluated numbers.

## 7. Aggregate artifact, row, test, and negative targets

| CSV | Body rows | Columns | Negative rows |
|---|---:|---:|---:|
| `nerve_factorization_controls.csv` | 280 | 17 | 0 |
| `circle_multiplier_cocycle_controls.csv` | 500 | 20 | 0 |
| `lift_integer_defect_controls.csv` | 500 | 20 | 0 |
| `gauge_coboundary_controls.csv` | 196 | 19 | 0 |
| `twisted_convolution_controls.csv` | 78 | 23 | 0 |
| `twisted_involution_controls.csv` | 54 | 26 | 0 |
| `completion_gauge_controls.csv` | 756 | 28 | 0 |
| `action_period_nonretention_controls.csv` | 56 | 20 | 0 |
| `negative_domain_controls.csv` | 20 | 12 | 20 |
| `actual_standard_support_transfer_controls.csv` | 96 | 21 | 27 |
| `target_summary.csv` | 12 | 11 | 0 |
| **Total** | **2548** | -- | **47** |

The exact package targets are:

```text
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
```

The three copies are checked-in results, fresh generation A, and fresh
generation B. Byte identity covers all eleven CSVs and the manifest.

## 8. Exact 128-test audit budget

The future suite must expose exactly 128 independently discoverable
`unittest` methods; a parametrized loop inside one method counts as one.
All must pass. The fixed budget is:

| Test family | Exact methods | Required surface |
|---|---:|---|
| `nerve_factorization` | 7 | schema, rows/order, both degrees, normalization, unit independence, T0-scope label, oracle recomputation |
| `circle_multiplier_cocycle` | 7 | schema, rows/order, both axes, four `k`, both cocycle sides, oracle recomputation |
| `lift_integer_defect` | 7 | centered range, `2*pi` divisibility, nonzero wrap coverage, normalization, mod-24 cocycle, order, oracle recomputation |
| `gauge_coboundary` | 7 | alpha normalization, frozen sign, quotient orientation, gauge direction, rows/order, four `k`, oracle recomputation |
| `twisted_convolution` | 10 | fixtures, exact Gaussian closure, product, two bracketings, associativity, gauge product, support, zero exterior rows, scope label, oracle recomputation |
| `twisted_involution` | 9 | fixtures, exact Gaussian closure, inverse symmetry, star-star, anti-product, actual/time match, exterior rows, scope label, oracle recomputation |
| `completion_gauge` | 11 | vectors, projective law, translation direction, intertwiner direction, character law, `beta/alpha`, choice map, norm square, scope label, rows/order, oracle recomputation |
| `action_period_nonretention` | 8 | 14-case registry, singleton, labels, nontransitive case, heterogeneous four-way case, dense diagnostic firewall, signatures, restriction oracle |
| `negative_domain` | 10 | exact registry/order, regularity negatives, normalization/sign negatives, product/star negatives, regular/intertwiner negatives, `R^2`, dense/heterogeneous, owner/support, proof/manifest promotions |
| `support_transfer` | 10 | eight `Q` cases, four functions, three gauges, zero branch, finite branch, infinite analytic branch, conditional `Q_p` branches, support preservation, negative count, oracle recomputation |
| `target_summary` | 5 | schema, 11 self/artifact rows, package row, aggregate arithmetic, no self-hash |
| Package/schema/canonical/manifest | 13 | exact artifact set, manifest schema, headers, per-file rows, total rows, negatives, unique IDs, canonical sort, CSV bytes, artifact hashes, byte counts, bindings, no unbound result |
| Deterministic reproduction | 8 | checked-in verify-only, fresh A generate/verify, fresh B generate/verify, checked-in/A compare, A/B compare, checked-in read-only receipt |
| Fail-closed tamper/drift | 12 | content, header, row count, reorder, missing CSV, extra CSV, extra directory, manifest, active-lock, gate/source, implementation, prohibited proof-hash tamper |
| Recursive entry / cache / cleanup | 4 | recursive-entry rejection, pre-run cache rejection, post-run cache rejection, temporary-root cleanup |
| **Total** | **128** | exact |

The suite may use internal assertions freely, but adding or removing a test
method requires a versioned design amendment and independent review.

## 9. Manifest and implementation binding policy

### 9.1 Future fixed paths

Only a later authorized implementation may create these six implementation
files:

```text
code/generate_controls.py
code/test_controls.py
code/README.md
experiments/reproduce.sh
experiments/README.md
results/README.md
```

and these twelve generated files:

```text
results/<the eleven CSV names frozen above>
results/manifest.json
```

The manifest binds SHA-256 and byte count for all six implementation files
and all eleven CSVs. It does not list itself as an artifact and does not
embed its own digest. The implementation and manifest may read the gate
files in Section 2 only to hash/verify them; source PDF content is not an
input to any control oracle.

### 9.2 Exact manifest semantics

The canonical manifest has these semantic blocks:

```text
schema_version
package_id = paper13-circle-twists-controls
design_lock = {path, sha256}
bindings = sorted [{path, sha256}] from Section 2
proof_binding = {
  concurrent_phase3_proof_hash_included: false,
  policy: POST_PROOF_AUDIT_BINDS_SEPARATELY
}
implementation = sorted [{path, bytes, sha256}]
artifacts = ordered [{path, schema, columns, rows, negative_rows, bytes, sha256}]
aggregates = the exact Section-7 targets
reproduction = {
  deterministic: true,
  random_used: false,
  network_used: false,
  fresh_generations: 2,
  byte_identical_copies: 3
}
status = PASS
```

No key matching `proof.*sha`, no proof path, and no non-null proof digest is
permitted. The Phase-3 proof lane may be changing concurrently; the controls
manifest therefore binds no proof byte. After the proof becomes stable, an
independent integrated audit binds the stable proof SHA and controls-manifest
SHA as two separate upstream artifacts. The manifest is not mutated to add
the proof later.

Any drift in the design digest, any Section-2 binding, any implementation
digest, any artifact name/header/order/count/hash, any aggregate, or the
proof-binding policy makes `--verify-only` fail nonzero.

### 9.3 Reproduction contract

The only future top-level entry point is
`papers/13-circle-twists/experiments/reproduce.sh`. It must:

1. refuse recursive entry when `P13_REPRO_ACTIVE` is already set;
2. require external serialization of top-level runs;
3. export `LC_ALL=C`, `TZ=UTC`, `PYTHONHASHSEED=0`, and
   `PYTHONDONTWRITEBYTECODE=1`, and invoke `python3 -B`;
4. verify the checked-in package without writing it;
5. generate into two distinct `mktemp -d` roots and verify each;
6. byte-compare all twelve generated artifacts across all three copies;
7. run exactly the 128 tests;
8. reject missing/extra files or directories, cache files, and binding drift;
   and
9. remove both temporary roots through an exit trap and finish with no
   `__pycache__`, `.pyc`, `.pyo`, or task temporary residue.

`--verify-only` must open checked-in artifacts read-only and must not repair,
rewrite, normalize, or regenerate them. The generator may write only into a
new empty output directory supplied explicitly. No retry is automatic.

## 10. Design audit table and gate consequence

| Required surface | Frozen receipt | Finding |
|---|---|---|
| Eleven-CSV inventory | ten inherited names plus `actual_standard_support_transfer_controls.csv` | none |
| Schema/version/columns | one package schema; exact header for every CSV | none |
| Row formulas/order/serialization | exact enumeration and RFC-style bytes frozen | none |
| Circle normalization and quadratic family | mod-24 exact `sigma_k`, `alpha_k`, frozen coboundary sign | none |
| `exp(iq)` lift boundary | centered lift and exact `2*pi*Z` defect ledger | none |
| Product/star/gauge | exact Gaussian finite-lattice sign diagnostics | none |
| Regular/intertwiner/choice | exact finite matrix elements and character isometry | none |
| Singleton/action/period cases | singleton, free, periodic, prime, composite, arbitrary, nontransitive | none |
| Heterogeneous/dense cases | four stabilizers; dense row explicitly diagnostic-only | none |
| `R^2` noncollapse | exact quarter-turn commutator negative | none |
| Support-transfer boundary | zero, finite, infinite analytic, and conditional `Q_p` branches | none |
| Finite-versus-proof firewall | repeated at row, negative, manifest, and gate levels | none |
| Aggregate targets | 12 generated artifacts, 2548 CSV rows, 128 tests, 47 negatives | none |
| Manifest/proof race | exact source/design bindings; concurrent proof hash prohibited | none |
| Determinism/fail-closed/no-cache | two fresh copies, three-way byte identity, tamper and residue gates | none |

Finding register:

| Severity | Count | Open item |
|---|---:|---|
| Critical (`C`) | 0 | none |
| Major (`M`) | 0 | none |
| Minor (`m`) | 0 | none |

```text
P13_CONTROL_DESIGN_LOCK=FROZEN_CANDIDATE
DESIGN_SCHEMA=paper13-circle-twists-controls/1
MANIFEST_SCHEMA=paper13-circle-twists-controls-manifest/1
CSV_ARTIFACTS=11
GENERATED_ARTIFACTS=12
CSV_BODY_ROWS=2548
EXPLICIT_NEGATIVES=47
TEST_METHODS=128
TOLERANCE_POLICY=EXACT_ZERO
CONCURRENT_PROOF_HASH_INCLUDED=false
CONTROL_IMPLEMENTATION_AUTHORIZED=false
CONTROL_EXECUTION_PERFORMED=false
CRITICAL_OPEN=0
MAJOR_OPEN=0
MINOR_OPEN=0
```

The design is ready for an independent exact-byte review. Implementation
remains blocked until that review returns zero findings on this digest. Even
after implementation and deterministic reproduction pass, mathematical
proof, standalone status, Route, manuscript, and release remain under their
separate gates.
