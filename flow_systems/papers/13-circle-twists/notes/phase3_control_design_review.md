# Paper 13 Phase-3 deterministic-control design review

Status: **REVISE DESIGN BEFORE IMPLEMENTATION**  
Verdict: **C0 / M1 / m0**  
Review date: **2026-08-15 (Asia/Shanghai)**  
Review mode: independent static design/integrity audit  
Control code created or run: **no**  
Results or Route artifacts created: **no**  
`route_b_invocation_allowed: false`

## Material Passport

- Origin Skill: ARS experiment-agent plus academic-pipeline integrity workflow
- Origin Mode: plan / independent deterministic-control design review
- Origin Date: 2026-08-15
- Verification Status: ANALYZED
- Version Label: `p13_control_design_review_v1`
- Scope: exact-byte design review only; no implementation, execution, proof,
  result, Route, manuscript, standalone, or release judgment

## 1. Exact reviewed authority and boundary

The frozen design candidate was read and rehashed as:

| Artifact | SHA-256 | Receipt |
|---|---|---|
| `notes/phase3_control_design_lock.md` | `900c541713b1711bdab7fa0d264355b6d8ee27014094e60eac6aabe38190604c` | exact requested bytes: MATCH |
| `notes/phase1_amendment_v1.md` | `ea5242ba6a8a1f2f867e8b258abc802fdeaace54db76629f0a9f0629e3e90d27` | controlling design requirements: MATCH |
| `notes/phase2_final_review.md` | `ffcfbac5768fc409b3fa9e5df4f3b46a2366f553373664c78f4364d456854cd9` | design-only authorization gate: MATCH |

All twelve upstream binding paths listed in design-lock Section 2 were also
rehashed. Every digest matches the value frozen there, including the active
protocol/candidate/state tuple, amendment and Phase-1 gate, all three final
Phase-2 reports, source manifest and checksum ledger, and the local-source
`.gitignore`.

The Phase-1 amendment requires the pre-implementation design to freeze the
schema, every column, exact row formula, canonical order and serialization,
oracle, exact row count, negative labels, tolerance, manifest bindings, and
aggregate artifact/row/test/negative counts. The Phase-2 gate authorizes this
design and its independent review only. It expressly withholds implementation
and execution authorization until a reviewed design lock exists. Consistent
with that boundary, this review performed static arithmetic, convention,
schema, oracle, and dependency-DAG checks only. It did not create or execute
control code and did not generate results.

## 2. Eleven-CSV schema, order, and row arithmetic recomputation

I token-counted every frozen header in its displayed order and independently
recomputed every enumeration product. The declared header widths, row-ID
ranges, enumeration orders, and counts are arithmetically consistent:

| # | CSV | Header columns | Canonical row order | Independent row formula | Body rows | Negative rows |
|---:|---|---:|---|---:|---:|---:|
| 1 | `nerve_factorization_controls.csv` | 17 | owner, unit, degree `1,2`, declared profile order, numeric `t,u` | `(1+2+3+4) * (2*5 + 2*3*3)` | 280 | 0 |
| 2 | `circle_multiplier_cocycle_controls.csv` | 20 | `K24`, then numeric `T1^3` | `4*5^3` | 500 | 0 |
| 3 | `lift_integer_defect_controls.csv` | 20 | same `K24 x T1^3` order | `4*5^3` | 500 | 0 |
| 4 | `gauge_coboundary_controls.csv` | 19 | `K24`, then numeric `T3^2` | `4*7^2` | 196 | 0 |
| 5 | `twisted_convolution_controls.csv` | 23 | `C1,C2`; `KG`; numeric `TOUT` | `2*3*13` | 78 | 0 |
| 6 | `twisted_involution_controls.csv` | 26 | `C1,C2`; `KG`; numeric `TSTAR` | `2*3*9` | 54 | 0 |
| 7 | `completion_gauge_controls.csv` | 28 | `V1,V2`; `KG`; `m=0,1`; `SHIFT^2`; `TEVAL` | `2*3*2*3^2*7` | 756 | 0 |
| 8 | `action_period_nonretention_controls.csv` | 20 | fourteen listed action/component cases, then `K24` | `14*4` | 56 | 0 |
| 9 | `negative_domain_controls.csv` | 12 | literal `ND-0001`--`ND-0020` registry order | `20` | 20 | 20 |
| 10 | `actual_standard_support_transfer_controls.csv` | 21 | eight declared `Q` cases, four functions, three gauges | `8*4*3` | 96 | 27 |
| 11 | `target_summary.csv` | 11 | Sections 5.1--5.11 artifact order, then package row | `11+1` | 12 | 0 |

The header token counts agree with the widths declared in Sections 5.1--5.11.
The row-ID terminal values also agree with the recomputed body counts:
`NF-0280`, `CM-0500`, `LI-0500`, `GC-0196`, `TC-0078`, `TI-0054`,
`CG-0756`, `AP-0056`, `ND-0020`, `ST-0096`, and `TS-0012`.

The package-row arithmetic closes exactly:

```text
280 + 500 + 500 + 196 + 78 + 54 + 756 + 56 + 20 + 96 + 12
  = 2548.
```

The negative ledger also closes:

```text
negative_domain: 20
support transfer: 3 infinite/conditional-infinite cases
                  * 3 nonzero functions * 3 gauges = 27
package total: 20 + 27 = 47.
```

The remaining 69 support-transfer rows are positive: 96 total minus 27
negative. Zero-function rows remain positive even on an infinite branch,
as required by the `f=0 or Q finite` statement.

## 3. Exact-arithmetic, signs, and oracle audit

### 3.1 Phase and coboundary arithmetic

With `zeta=exp(2*pi*i/24)`, storing only the exponent gives

```text
sigma_k(t,u):  2*k*t*u mod 24,
alpha_k(t):   -k*t^2 mod 24.
```

The frozen coboundary orientation recomputes as

```text
-k*t^2 - k*u^2 + k*(t+u)^2 = 2*k*t*u,
```

so `delta alpha_k=sigma_k` and the declared
`U_alpha:A_sigma -> A_1` token has the correct direction. The cocycle sides
also agree before reduction modulo 24:

```text
2*k*(t*u + (t+u)*v)
  = 2*k*(u*v + t*(u+v)).
```

The centered representative `pr24` has range `{-12,...,11}`. Its lifted
defect is an integer multiple of 24, so `D24/24` correctly records the
multiple of `2*pi`; nonzero branch wraps are diagnostics, not failures. This
keeps the phase cocycle and real-lift statements distinct without a floating
oracle.

### 3.2 Finite product, star, and regular diagnostics

For `KG=(-6,0,6)`, every phase used in product/star/regular rows is a fourth
root of unity, hence all declared real and imaginary components lie in the
Gaussian integers. The fixture supports imply:

- the two `f*g` supports lie in `[-3,3]` and `[-3,4]`;
- the two triple-product supports lie in `[-5,5]` and `[-4,6]`; and
- `TOUT=[-6,6]` and `TSTAR=[-4,4]` include the required exterior-zero
  sentinels.

The product uses `sigma(u,t-u)`, the star uses
`overline{sigma(t,-t)} overline{f(-t)}`, and the regular action uses
`xi(t-s)`. The projective law and the pointwise gauge identity have the
frozen signs:

```text
lambda_sigma(s)lambda_sigma(u)
  = sigma(s,u)lambda_sigma(s+u),

M_alpha lambda_sigma(s) M_overline(alpha)
  = alpha(s)lambda(s).
```

For `chi_m(t)=zeta^(6*m*t)`, `U_beta=C_chi U_alpha` and circle multiplication
preserves the finite squared norm exactly. These rows remain finite matrix-
element or finite-lattice diagnostics and do not establish a continuous
completion theorem.

### 3.3 Negative-domain fixtures

All twenty negative reasons are distinct and the advertised sign/domain
sentinels discriminate the forbidden alternatives. In particular:

- at `k=-1,t=u=1`, conjugating the frozen coboundary changes exponent `22`
  to `2`, so the wrong sign is detected;
- at `k=6,u=1,t=2`, `sigma(u,t-u)` has exponent `12` while
  `sigma(u,t)` has exponent `0`;
- at `k=6,t=1`, the omitted star phase is `-1`;
- `V1,s=1,t=0` distinguishes `xi(t-s)` from `xi(t+s)`;
- `V2,k=6,s=1,t=0` distinguishes the two intertwiner conjugation orders;
  and
- the registered `R^2` multiplier has commutator exponent `1 mod 4`, so it
  is a valid excluded-dimension falsifier.

The dense-`Q`, heterogeneous-stabilizer, reverse-`J`, finite-as-infinite,
fixed-prime-cardinality, owner-framework, control-as-proof, and concurrent-
proof-binding rows correctly encode fail-closed claim or manifest boundaries.

### 3.4 Finite/infinite support oracle

The four piecewise-linear functions have the stated exact supports. In
particular, `max(1-|2*t-3|,0)` is positive on `(1,2)` and has support
`[1,2]`, so the displayed two-bump support is correct.

The support oracle is mathematically typed as follows:

- the zero function has empty compact support for every `Q`;
- for nonzero `f`, each standard orbit contributes a nonempty compact
  component times `supp(f)`;
- finitely many such components give compact support;
- infinitely many nonempty open components give an open cover with no finite
  subcover; and
- a circle-valued gauge is nowhere zero and preserves support exactly.

The `QINF_N` and `QINF_Z` rows invoke that analytic infinite-coproduct branch
directly; they do not substitute a large finite set. The `QP_FINITE_*` and
`QP_INFINITE_*` rows are conditional alternatives and do not decide the
actual cardinality of `Q_p`. The corresponding evidence-scope labels and the
finite-control-as-proof negative keep the controls within the Phase-1 and
Phase-2 ceilings.

## 4. Aggregate test-budget recomputation

The exact `unittest` method allocation sums to 128:

```text
7+7+7+7+10+9+11+8+10+10+5+13+8+12+4 = 128.
```

The allocation covers every CSV family, package/schema/manifest validation,
two fresh generations, three-copy comparisons, fail-closed tampering,
recursive entry, cache rejection, and temporary cleanup. A loop inside a
method remains one discoverable method, so the budget is unambiguous at the
method-count level. The fixed aggregate targets `11` CSVs, `12` generated
artifacts including the manifest, `2548` CSV body rows, `47` detected
negatives, two fresh generations, and three byte-identical copies are
mutually consistent.

## 5. Manifest dependency-DAG audit

The intended dependency graph is acyclic:

```text
frozen Phase-1/Phase-2/source gates + frozen design lock
    -> six implementation files
    -> eleven CSV artifacts
    -> manifest over implementation + CSV hashes/byte counts

stable proof -------------------------------> later integrated audit
controls manifest --------------------------> later integrated audit
```

The manifest does not list itself, and `target_summary.csv` contains only its
own row count/width rather than a digest, so there is no manifest or summary
self-hash cycle. The changing Phase-3 proof is correctly excluded from the
control manifest; the later integrated audit, rather than a mutation of the
manifest, is the proper place to bind stable proof and manifest hashes.

The deterministic byte contract is strong: fixed CSV/JSON
serialization, no timestamps or host/process/temp data, two empty temporary
roots, verify-only read-only handling, three-way byte comparison, fixed
locale/time/hash settings, missing/extra/tamper checks, recursive-entry and
cache guards, and exit-trap cleanup.

The required boolean key `concurrent_phase3_proof_hash_included` does not
match the prohibited pattern `proof.*sha`: after `proof` it contains `hash`,
not the ordered substring `sha`. Its frozen value is `false`. No proof path,
proof digest, manifest self-digest, or summary self-digest is required, so the
manifest proof-race and self-cycle policies are internally consistent.

## 6. Findings and bounded repairs

### M1 — Several declared CSV columns lack a byte-determining row rule

**Location:** design-lock Sections 5.8--5.11, especially lines 390--395,
402--430, 440--478, and 498--507.  
**Requirement violated:** Phase-1 amendment Section 12 requires an exact row
formula and canonical serialization for every output before implementation.

The counts and row enumeration are exact, but not every field value is. The
following columns admit multiple implementations that all satisfy the prose
while producing different canonical bytes:

1. `action_period_nonretention_controls.csv` says that two class fields are
   "zero sample classes" and three algebra/completion fields contain a
   "common finite diagnostic signature", but freezes neither literal values
   nor a computation that produces those signatures.
2. `negative_domain_controls.csv` contains `violated_lock`, but the 20-row
   registry provides no value for that column. Several fixture descriptions
   also leave their canonical serialized fixture token unspecified.
3. `actual_standard_support_transfer_controls.csv` does not define the value
   domain or row formula for `support_components` or
   `fixed_prime_conditional`. Its displayed compactness expression should
   also state the final disjunct explicitly as
   `q_class == QP_FINITE_CONDITIONAL`, rather than leaving a bare token.
4. `target_summary.csv` does not provide the eleven literal
   `canonical_order_key` and `scope` values or a complete literal twelve-row
   table. Consequently its bytes cannot be derived uniquely from the design.

This is not a mathematical counterexample and does not alter the correct
aggregate counts. It is a reproducibility/design-lock defect: an
implementation author would have to invent values after the independent
review, contrary to the pre-implementation freeze.

**Bounded repair:** issue a versioned design amendment that supplies a closed
value domain and exact derivation or literal token for every field above.
For the action/period signatures, make the computation independent rather
than copying a common expected string. For the negative ledger, add the exact
`violated_lock` and canonical `fixture` value to every row. For support rows,
freeze `support_components`, `fixed_prime_conditional`, and the explicit
membership/equality predicate. For the summary, freeze all twelve rows in
full. Recompute the design hash and obtain a new independent exact-byte
review before implementation.

## 7. Severity register and gate consequence

| Severity | Count | Disposition |
|---|---:|---|
| Critical (`C`) | 0 | no mathematical/domain collapse or destructive integrity flaw found |
| Major (`M`) | 1 | must be repaired in a versioned design lock before implementation |
| Minor (`m`) | 0 | none |

```text
REVIEWED_DESIGN_SHA256=900c541713b1711bdab7fa0d264355b6d8ee27014094e60eac6aabe38190604c
HEADER_WIDTHS_RECOMPUTED=17,20,20,19,23,26,28,20,12,21,11
CSV_ARTIFACTS_RECOMPUTED=11
GENERATED_ARTIFACTS_RECOMPUTED=12
CSV_BODY_ROWS_RECOMPUTED=2548
EXPLICIT_NEGATIVES_RECOMPUTED=47
UNITTEST_METHODS_RECOMPUTED=128
MANIFEST_SELF_HASH_PRESENT=false
CONCURRENT_PROOF_DIGEST_PERMITTED=false
CONTROL_IMPLEMENTATION_AUTHORIZED=false
CONTROL_EXECUTION_PERFORMED=false
CRITICAL_OPEN=0
MAJOR_OPEN=1
MINOR_OPEN=0
```

Disposition: **REVISE**. The numerical design, mathematical sign oracles,
finite/infinite owner ceilings, test allocation, and intended dependency DAG
are coherent, but the exact-byte design lock is not yet implementation-ready.
No code or result generation is authorized on this digest. A bounded amended
design resolving M1 must be rehashed and independently re-reviewed at
`C0/M0/m0`; proof, Route, manuscript, standalone, release, Git, and public
synchronization gates remain separate.

## Addendum A — amended-v1 exact-byte closure re-lock

Addendum date: **2026-08-15 (Asia/Shanghai)**  
Effective amended-tuple verdict: **PASS / C0 / M0 / m0**  
Review operation: append-only; the 320-line review prefix is historical and
unchanged  
Control implementation or execution performed in this addendum: **no**

### A.1 Exact amended tuple and prefix integrity

This addendum independently reviews the bounded amendment that answers M1.
The exact tuple rehashed at intake is:

| Artifact | SHA-256 | Receipt |
|---|---|---|
| immutable base `notes/phase3_control_design_lock.md` | `900c541713b1711bdab7fa0d264355b6d8ee27014094e60eac6aabe38190604c` | MATCH |
| authoritative pre-addendum review prefix `notes/phase3_control_design_review.md` | `64ce1cd97e122d0fb197731d62dbf37b734d11b6b6b3ee11a97808335c632cd6` | MATCH before append |
| `notes/phase3_control_design_amendment_v1.md` | `5c9caea983b0047c4b16d0437c23b117a6b8150bbeb67b79c60fb9b2ba6a737e` | MATCH |

The amendment has 506 lines and 22,269 bytes. It binds the exact immutable
base and authoritative review-prefix digests and supersedes only the open
AP/ND/ST/TS byte-value rules. All other base-design requirements remain in
force. The earlier M1 verdict above remains the historical decision on the
unamended bytes; this addendum is the effective disposition for the amended
three-artifact tuple.

### A.2 AP exact-value and independent-oracle re-lock

The amended AP row index is closed and preserves the base order. For case
ordinal `c in {1,...,14}` and the position `j in {1,...,4}` of
`k` in `K24=(-6,-1,0,6)`, the formula

```text
n=4*(c-1)+j
```

gives `AP-0001` through `AP-0056` with no collision or gap. The four owner
metadata fields are copied from the immutable 14-row table; no inferred sort
can reorder the heterogeneous four-component tail.

The amendment supplies one exact literal for each formerly open class or
signature field:

```text
TIME_QUADRATIC_GAUGE_CLASS_ZERO_SAMPLE
ISOTROPY_QUADRATIC_RESTRICTION_CLASS_ZERO_SAMPLE
TWISTED_TEST_GAUGE_STAR_TERM_CHECK_PASS
FULL_TRANSPORT_CHARACTER_PHASE_CHECK_PASS
REDUCED_TRANSPORT_INTERTWINER_CHECK_PASS
```

It also closes `dense_h_scope`, both stored booleans, row kind, empty negative
reason, oracle, tolerance, and status. The dense token occurs exactly on the
`HETEROGENEOUS_ACTION/dense_component` rows; all other rows receive
`NOT_DENSE_H_CONTROL`.

The five signature predicates are independent of their output tokens and
recompute correctly:

1. With `A_k(t)=-k*t^2` and `S_k(t,u)=2*k*t*u`,

   ```text
   A_k(t)+A_k(u)-A_k(t+u)-S_k(t,u)=0
   ```

   identically, so all 49 `T3^2` pairs and the normalization value close for
   every `k`.
2. The same expression has coefficient vector `(0,0,0)` in ordered
   monomials `(x^2,x*y,y^2)`. Restriction to `{0}`, a lattice, `R`, or dense
   `Q` therefore remains a formal coboundary calculation and imports no Haar
   or completion statement.
3. The product, cocycle, and gauge-star exponents reduce respectively to

   ```text
   2*k*(u*v+(u+v)*w-v*w-u*(v+w)) = 0,
   -k*(u+v)^2+2*k*u*v+k*u^2+k*v^2 = 0,
   -k*t^2-(-2*k*t^2)-k*t^2 = 0.
   ```

   Thus the test-algebra token follows from fixture-derived term checks, not
   from copying a baseline label.
4. `C_m(t)=6*m*t` is additive modulo 24,
   `C_m(t)+C_m(-t)=0`, and `B_km=C_m+A_k` gives the exact character/choice
   phase checks. This remains a finite phase diagnostic, not a full-norm
   result.
5. The projective and intertwiner exponents satisfy

   ```text
   S_k(s,t-s)+S_k(u,t-s-u)
     =S_k(s,u)+S_k(s+u,t-s-u),

   A_k(t)+S_k(s,t-s)-A_k(t-s)=A_k(s),
   ```

   including zero coefficients outside the finite vector supports. This is
   exactly the registered matrix-element diagnostic ceiling.

The two stored AP booleans are emitted only after these predicates close.
Consequently all 56 AP rows now have byte-determining values and an
independent exact oracle. The action, literal-stabilizer, dense-subgroup, and
completion owner ceilings do not regress.

### A.3 ND literal-field and detector re-lock

All twenty `ND-0001`--`ND-0020` rows now carry an exact ASCII `fixture` and
an exact `violated_lock`. Every fixture uses the frozen semicolon-delimited
clause order and contains no comma, quote, CR, or LF, so `QUOTE_MINIMAL`
produces one unquoted field exactly as displayed. The reason, expected
detector, and disposition remain the immutable base tokens.

The exact 12-column coverage is complete: the global schema supplies one
field; the amendment table supplies `row_id`, `negative_reason`, `fixture`,
and `violated_lock`; the base table supplies `expected_detector` and
`expected_disposition`; the detector computes `observed_detector`; and the
amendment fixes `case_kind`, `oracle`, `tolerance`, and `status`. Thus the
amendment's informal phrase "remaining six variable columns" is non-operative:
the explicit rules determine all twelve header positions without a missing or
duplicate field.

The detector is not permitted to echo the expected token. It must first parse
and construct the fixture, recompute the algebraic/topological/policy failure,
and emit the observed token only afterward. The sign sentinels remain
discriminating: ND-0006 compares exponents `22` and `2`; ND-0008 compares
`12` and `0`; ND-0009 omits a factor `-1`; and ND-0010/0011 distinguish the
registered translation and intertwiner directions. ND-0012 retains the
quarter-turn `R^2` commutator and its one-dimensional exclusion.

The ND-0013 rational window is a finite, exactly ordered diagnostic and does
not assert density. ND-0020 changes the required proof sentinel from `false`
to `true` and supplies a non-null proof digest, so it is a genuine prohibited
manifest mutation rather than a rename of the allowed false sentinel. The
twenty rows therefore remain twenty detected negatives, with no new reason or
owner promotion.

### A.4 ST complete row derivation and branch re-lock

The amended ST index

```text
n=12*(q-1)+3*(f-1)+g
```

for eight orbit cases, four functions, and three gauges yields `ST-0001`
through `ST-0096` exactly. The three closed input tables determine every
previously open value:

- `support_components` is exactly `EMPTY`, `[-1,1]`, `[1,3]`, or
  `[-3,-1]|[1,2]` by function;
- `fixed_prime_conditional=true` occurs exactly on the two `QP_*` cases;
- every gauge has `gauge_nowhere_zero=true`; and
- each orbit case has one exact cardinality and evidence-scope token.

The three nonempty interval fields contain commas and therefore acquire the
required surrounding CSV quotes; `EMPTY` remains unquoted. This follows from
the inherited `csv.QUOTE_MINIMAL` contract and introduces no alternative byte
form.

The formerly bare finite disjunct is now the explicit equality predicate

```text
(q_class == "FINITE")
or (q_class == "QP_FINITE_CONDITIONAL").
```

Hence

```text
standard_support_compact = is_zero or finite_q_class,
lands_in_standard_cc     = standard_support_compact,
support_preserved        = gauge_nowhere_zero.
```

The negative predicate selects exactly the two ordinary infinite cases and
the conditional-infinite fixed-prime case, crossed with three nonzero
functions and three gauges:

```text
3*3*3=27 negative rows,
96-27=69 positive rows.
```

Zero-function rows remain positive on all infinite branches. The two
fixed-prime alternatives remain conditional and do not decide `Q_p`; the
ordinary infinite cases use the analytic infinite-coproduct branch rather
than a finite surrogate. M1's ST field and predicate gaps are closed without
changing the theorem/control firewall.

### A.5 Literal TS body re-lock

The amendment supplies the complete literal body under the unchanged
11-column header. I independently token-counted all twelve displayed rows:
each has exactly eleven fields in header order, and none contains a comma
inside a body field. Consequently none requires quoting.

Rows `TS-0001`--`TS-0011` preserve the base artifact order, exact body-row
counts, header widths, negative counts, `COUNT_SCHEMA_NEGATIVE_TOTAL`,
`EXACT_ZERO`, and one exact canonical-order/scope token. `TS-0012` retains
`PACKAGE_TOTAL`, `2548`, `MIXED`, `47`, `ARTIFACT_ORDER_ABOVE`, and the
no-theorem-credit scope. The self-row records only `12` body rows and `11`
columns; it carries no digest. The literal table therefore closes the final
M1 byte ambiguity without creating a summary or manifest self-cycle.

### A.6 Aggregate, test-budget, serialization, and manifest non-regression

No header or enumeration changed. The complete body-row arithmetic remains

```text
280+500+500+196+78+54+756+56+20+96+12=2548,
```

and the negative total remains `20+27=47`. The eleven CSVs plus one manifest
remain twelve generated artifacts. The unchanged method allocation still
sums to

```text
7+7+7+7+10+9+11+8+10+10+5+13+8+12+4=128.
```

The new derivations fit inside the already frozen AP, ND, ST, summary, and
package assertions; no test-method count change is required. UTF-8 without
BOM, LF, exact-zero arithmetic, `csv.writer`, canonical JSON, two fresh
generations, three-copy byte identity, fail-closed tampering, no-cache, and
cleanup requirements are unchanged.

For the amended package, the manifest's singular `design_lock` points to the
amendment path and digest. The amendment cryptographically commits to the
immutable base and authoritative review-prefix hashes; the twelve original
Phase-1/Phase-2/source bindings remain unchanged. This changes the identity
of the authoritative design head, not the manifest schema or its dependency
semantics.

The proof block remains exactly

```text
proof_binding = {
  concurrent_phase3_proof_hash_included: false,
  policy: POST_PROOF_AUDIT_BINDS_SEPARATELY
}
```

The false sentinel does not match the prohibited `proof.*sha` key pattern,
and no proof path or non-null proof digest is allowed. The manifest does not
list or hash itself; no CSV contains its own digest. Stable proof and stable
controls-manifest hashes remain separate inputs to a later integrated audit.
The dependency DAG is therefore acyclic, proof-race safe, and unchanged in
substance. Route remains prohibited.

### A.7 M1 closure, final severity, and gate consequence

| Prior M1 surface | Amended-tuple result |
|---|---|
| AP class/signature literals | closed by five exact tokens |
| AP oracle independence | closed by five separately recomputed predicates |
| ND `violated_lock` and fixtures | closed for 20/20 literal rows |
| ND detector independence | closed by construct/recompute-before-emit rule |
| ST support/conditional fields | closed by exact tables and quoting rule |
| ST finite/negative predicates | closed by explicit equality tests |
| TS order/scope values | closed by a full literal 12-row body |
| Counts, negatives, tests, schemas | unchanged and independently reconciled |
| Manifest proof/self-hash policy | unchanged, acyclic, and exact |

Final amended-tuple finding register:

| Severity | Count | Open item |
|---|---:|---|
| Critical (`C`) | 0 | none |
| Major (`M`) | 0 | none |
| Minor (`m`) | 0 | none |

```text
P13_CONTROL_DESIGN_AMENDED_RELOCK=PASS
BASE_DESIGN_SHA256=900c541713b1711bdab7fa0d264355b6d8ee27014094e60eac6aabe38190604c
AUTHORITATIVE_REVIEW_PREFIX_SHA256=64ce1cd97e122d0fb197731d62dbf37b734d11b6b6b3ee11a97808335c632cd6
DESIGN_AMENDMENT_V1_SHA256=5c9caea983b0047c4b16d0437c23b117a6b8150bbeb67b79c60fb9b2ba6a737e
M1_CLOSED=true
REGRESSION_FOUND=false
CSV_ARTIFACTS=11
GENERATED_ARTIFACTS=12
CSV_BODY_ROWS=2548
EXPLICIT_NEGATIVES=47
UNITTEST_METHODS=128
MANIFEST_SELF_HASH_PRESENT=false
CONCURRENT_PROOF_DIGEST_PERMITTED=false
IMPLEMENTATION_REVIEW_PREREQUISITE_SATISFIED=true
CONTROL_IMPLEMENTATION_PERFORMED=false
CONTROL_EXECUTION_PERFORMED=false
ROUTE_AUTHORIZED=false
CRITICAL_OPEN=0
MAJOR_OPEN=0
MINOR_OPEN=0
```

Effective disposition: **PASS / C0/M0/m0** on the exact amended tuple. M1 is
closed and no regression was found. This addendum satisfies the independent
design-review prerequisite for a later bounded implementation against the
amendment as the authoritative design head; it does not itself implement or
run controls. Proof, controls execution, standalone, Route, composition,
manuscript, citation, release, Git, and public synchronization remain under
their separate gates.
