# Paper 17 Phase-2 deterministic-control design lock

Status: **FROZEN DESIGN CANDIDATE / INDEPENDENT EXACT-BYTE DESIGN REVIEW REQUIRED**  
Version: `P17-P2-CONTROLS-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Design-author self-audit: **C0 / M0 / m0**  
Publication disposition: **sole batch Technical Note candidate**  
Standalone disposition: **false**

Control implementation, control execution, design review, Route A/B,
composition, manuscript or figure work, release, Git, archive, and public
synchronization performed or authorized here: **false**.

## Material Passport

- Origin Skill: ARS experiment-agent plan mode plus academic-pipeline
  integrity/reproducibility and reviewer methodology/devil protocols
- Origin Mode: deterministic-control design only
- Origin Date: 2026-08-16
- Verification Status: `UNVERIFIED`
- Version Label: `p17_phase2_control_design_v1`
- Upstream Gate: `notes/phase2_control_design_gate.md`
- Upstream Gate SHA-256:
  `093ca31fa840b992a105cbfd4911353e3df49ba7e05ae8e43d541059999b6647`
- Scope: versioned schema, finite fixtures, exact serialization, independent
  oracle, test/mutation, reproduction, and manifest design only

## 1. Authority, exact-byte receipts, and hard boundary

The complete authority tuple was read and independently re-hashed before this
design was frozen. The byte receipts are:

| Artifact | SHA-256 |
|---|---|
| Papers 14--18 historical batch design lock | `2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8` |
| Papers 14--18 batch amendment v1 | `afd933440abed3eff4872d6ffe671213d531cb6ceb4c08ebd87c3048d37b1802` |
| Papers 14--18 batch amendment v2 | `3aa08c2cc2e38b02c83316d188f418d157abd43cf881e447cc28bf083ed3684b` |
| `notes/research_protocol.md` | `5ca581cff6f2fe088744a522646466ef2f5ce124ad3cdf50367cc5ed33347cea` |
| `notes/candidate_lock.md` | `2db53e92961cdfa7e43e4e06b7cdd81a2d87d97d15957d793b720bd86c71a604` |
| `notes/phase1_amendment_v1.md` | `3ada0e70a0d3f53bd68e1a44e63c24870215987176d538c513400dc99ef95f3d` |
| `notes/phase1_amendment_v2.md` | `2ce675880b171ee598f8a796edf55f9c695e2e6d0973620371d3ba460c7d1957` |
| `notes/phase1_framework_source_precheck.md` | `9991dc5e27ea8577d4236d38feeb63bfc110e3a3b242b3c17be8607da01f9e64` |
| `notes/phase1_methodology_devils_review.md` | `811e51fc96baedf81a3e4185fa49519ff6c15bad37d866d8186054a24c25653e` |
| `notes/phase1_independent_math_review.md` | `bdf89476d49ab8a5b3bb7deff9f8738079bd185fd38a00bc1c9ba175677ad6d4` |
| `notes/phase1_final_gate.md` | `025ee0404484bfa906094adc940528fc6c2c564c39783e1f1658ed9666f645df` |
| `notes/phase2_topos_quantale_proofs.md` | `f6c7475b854b3d00b37d3e7f2edca8e8f2f15d92d67ae8bbcdcd71be127b3bb1` |
| `notes/phase2_topos_quantale_peer_review.md` | `9ad4817e32c6da461d7e15eee1bd53d24368b7c55751738c86c8b033caeb796e` |
| `notes/phase2_control_design_gate.md` | `093ca31fa840b992a105cbfd4911353e3df49ba7e05ae8e43d541059999b6647` |

The fixed-prime provenance oracle additionally binds the upstream Paper-9
manuscript, whose re-hashed bytes are:

```text
papers/9-packet-separation/paper/manuscript.tex
sha256:24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb
```

The post-proof gate authorizes this design file only. It authorizes neither
the future paths described below nor any executable action. A separate
reviewer must review the final exact bytes of this file at the frozen future
path

```text
papers/17-open-groupoid-interfaces/notes/phase2_control_design_review.md
```

before a separate implementation gate may even be considered.

### 1.1 Epistemic red line

Every executable row below is a finite diagnostic, a falsifier, a typed
policy check, or a serialization receipt. No finite row, passing suite,
three-way byte identity, or manifest can prove any of the following:

- connectedness of the usual real line;
- `B(G(X,H)) ~= B_cont(H)`, `B(G(X,R)) ~= Set`, `B(G_L) ~= BZ`, or any
  category/topos equivalence;
- local compactness, the frame-tensor comparison `q_H`, or the correctness
  of the selected locale convention;
- Protin--Resende open-localic reconstruction or any other source theorem;
- non-etaleness or nonunitality of the usual nondiscrete-real owner from a
  discrete finite proxy;
- a universal statement about non-Hausdorff, disconnected, localic, or
  topological groupoids; or
- a C-star, Haar, measure, trace, determinant, numerical-scale, Route-B, or
  priority conclusion.

The locked symbolic rows validate only their literal token and scope label. Where
a `source_binding` column exists they also validate that exact row binding;
the C17-7 receipt instead relies only on the separately validated
package-level control-gate binding. They never turn a symbolic theorem into
executed evidence.

## 2. Versioned schemas and exact generated inventory

Every CSV row carries the literal schema value

```text
paper17-open-groupoid-controls/1
```

and the future manifest carries

```text
paper17-open-groupoid-controls-manifest/1
```

The complete ordered generated-artifact inventory is exactly:

```text
01 results/range_first_handedness_controls.csv
02 results/action_blind_open_records.csv
03 results/connected_disconnected_firewall.csv
04 results/domain_guard_controls.csv
05 results/quantale_localic_firewall.csv
06 results/actual_standard_owner_controls.csv
07 results/dilation_strict_marker_controls.csv
08 results/fixed_prime_provenance_controls.csv
09 results/target_summary.csv
10 results/manifest.json
```

No other file or directory is part of the generated package. The nine CSVs
are the only CSVs; the manifest is last. Artifact order is semantic and may
not be lexically resorted.

## 3. Canonical byte and scalar contract

### 3.1 CSV bytes

All nine CSVs use UTF-8 without BOM, LF line endings, and the Python
standard-library writer contract

```text
delimiter=","
quotechar='"'
quoting=csv.QUOTE_MINIMAL
doublequote=true
escapechar=None
lineterminator="\n"
```

Files are opened with `newline=""`. The following rules are exact:

- headers and columns appear in the order frozen in Section 6;
- fields have no leading or trailing whitespace;
- an inapplicable field is the empty CSV field, never `NA`, `null`, `None`,
  `-`, or a space;
- booleans are only `true` and `false`;
- integers are base-ten with no `+` and no leading zero except `0`;
- rational fields are always reduced `n/d`, with `d>0`, including `0/1`
  and all integral values such as `2/1`;
- finite ordered sets use `EMPTY` or their element tokens joined by `|` in
  the frozen carrier order;
- key/value records use `key=value` fields joined by `;` in the exact key
  order declared for that row family;
- row IDs use the exact prefix and zero-padded width frozen below;
- `case_kind` is exactly one of `DIAGNOSTIC`, `RECEIPT`, `NEGATIVE`;
- every nonnegative row has empty `negative_reason` and empty `detected`;
- every negative row has one registered nonempty `negative_reason` and
  literal `detected=true`;
- every persisted row has `status=PASS`; a failing derivation aborts without
  emitting a `FAIL` row; and
- timestamps, absolute paths, host names, process IDs, temporary paths,
  locale-dependent text, floats, `NaN`, infinities, and unordered mappings
  are prohibited from generated bytes.

`status`, `detected`, `negative_reason`, stored `subject_value` and
`oracle_value`,
`subject_composable`, `arrow_open`, `record_equal`, `licensed`, and
`inverse_value` are receipts, not oracles. Verification must ignore their
stored values while deriving them again from primitive semantic fields, then
require byte equality to the stored fields. Summary and manifest totals are
likewise recomputed receipts.

### 3.2 JSON bytes

The manifest uses UTF-8 without BOM and exactly

```text
json.dumps(object, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
```

No timestamp or environmental value is serialized. Arrays retain the exact
orders frozen here even though object keys are sorted.

### 3.3 Closed common tokens

The common literal oracle tokens are:

```text
D3_RELATION_AND_LEFT_ACTION
C4_BITSET_OPEN_QUANTALE
SOURCE_RECEIPT_PLUS_Z3_PERMUTATION
OWNER_DOMAIN_POLICY
BARE_Q_QH_LC_CONJUNCTION
CANONICAL_OWNER_PACKET_REGISTRY
INTEGER_CROSS_MULTIPLICATION_DILATION
P9_TWO_INPUT_POST_GENERIC_ALLOWLIST
RAW_COUNT_SCHEMA_INVENTORY
```

The common scope tokens are:

```text
FINITE_GROUP_DIAGNOSTIC_ONLY
FINITE_INDISCRETE_C4_CONSISTENCY_ONLY
FINITE_Z3_FALSIFIER_ONLY
SYMBOLIC_SOURCE_OWNED
SYMBOLIC_SOURCE_RECEIPT_ONLY
FINITE_DIAGNOSTIC_ONLY
NO_REAL_OR_LOCALIC_CERTIFICATION
ALGEBRAIC_RATIONAL_FIXTURE_ONLY
FIXED_PRIME_SUBSTITUTION_ONLY
COUNT_AND_SERIALIZATION_ONLY
```

No implementation may add an enum value without a versioned amendment and
independent review.

### 3.4 Canonical value and policy-claim grammar

The following grammars close the remaining string-valued fields:

```text
owner packet:
  owner=<owner_token>;topology=<topology_token>;topos=<topos_token>;quantale=<quantale_token>;base=<base_frame_token>

Boolean receipt:
  <claim_token>=true

policy attack subject, unless a mathematical subject is specified below:
  CLAIM[<negative_reason>]

policy rejection oracle:
  REJECTED

field comparison:
  <comparison_field>:<actual-token>|<standard-token>

base relation attack:
  base_relation=EQUAL
base relation oracle:
  base_relation=DISTINCT

strict-marker subject:
  strict_marker_preserved=true
strict-marker nonunit oracle:
  REJECTED
```

`WRONG_PRODUCT_ORDER` and `OPPOSITE_SHEET_ACTION` use their computed arrow
or sheet tokens instead of the policy-attack grammar. Owner-splice rows use
the complete mutated owner-packet grammar and the complete canonical packet
as oracle. All other `PROMOTION_ATTACK`, `WRONG_DOMAIN_ATTACK`,
`PLAIN_SCALE_PROMOTION`, and `PROVENANCE_PROMOTION_ATTACK` rows use the
policy-attack grammar exactly. These subject strings are display receipts;
the oracle derives the reason from the primitive typed columns.

## 4. Frozen primitive fixtures

### 4.1 Nonabelian `D3` fixture for range-first and handedness checks

Use

```text
D3={(i,j): i in {0,1,2}, j in {0,1}}
(i,j)*(k,l)=(i+(-1)^j*k mod 3, j+l mod 2).
```

The exact element order and tokens are

```text
H_D3=(d00,d10,d20,d01,d11,d21).
```

For the independent permutation representation, put

```text
r=(1,2,0), s=(0,2,1), d_ij=r^i o s^j,
```

where a permutation tuple lists the images of `(0,1,2)` and `g o h` means
apply `h` first. The generator uses the pair formula only; the verifier uses
permutation composition only.

The right-regular object carrier and left-regular sheet carrier are

```text
X_D3=(x00,x10,x20,x01,x11,x21),  x_g.h=x_(g*h),
S_D3=(s00,s10,s20,s01,s11,s21),  h.s_g=s_(h*g).
```

An arrow token is `a(xij;dkl)`. Its range is `xij`, its source is
`x_(ij*kl)`, meaning the serialized token `xpq` for the unique pair
`(p,q)=(i,j)*(k,l)` computed by the displayed pair law, and the range-first
product is

```text
a(x;h) a(x.h;k) = a(x;h*k).
```

There are exactly 18 ordered noncommuting pairs `(h,k)` in `D3`; they are
enumerated by the displayed `H_D3` order in the outer and inner loops and
filtered by `h*k != k*h`.

### 4.2 Same-carrier indiscrete `C4` action fixture

Use the ordered discrete time group and one ordered, nonempty, globally
indiscrete carrier

```text
C4=(0,1,2,3), X4=(x0,x1,x2,x3).
```

The exact right actions, in this order, are

```text
TRIVIAL:       x_j.t=x_j
TRANSITIVE:    x_j.t=x_((j+t) mod 4)
NONTRANSITIVE: x_j.t=x_((j+2*(t mod 2)) mod 4).
```

Subsets of `C4` are ordered by bitmask `0..15`, with bit `t` denoting
membership of `t`. Their token is `EMPTY` or the selected values joined by
`|` in `0,1,2,3` order. Define independently

```text
-U={-u mod 4:u in U},
U+V={u+v mod 4:u in U,v in V},
base(U) iff U=EMPTY or U=0|1|2|3.
```

The arrow-open descriptor token is `X4x[<subset-token>]`.

### 4.3 Disconnected-time falsifier

Use the genuinely nontrivial cyclic quotient of the regular discrete
integer action

```text
S3=(z0,z1,z2), n.z_a=z_((n+a) mod 3), n in (0,1,2).
```

This is an executable witness that a disconnected discrete time group can
have a nontrivial continuous discrete action. It is not a finite model of
connected `R`, and it does not prove a topos equivalence.

### 4.4 Rational dilation fixture

Use exact rational arithmetic only:

```text
L=2/1, L_prime=3/1, c=3/2,
RREP=(0/1,1/2,1/1,3/2),
TIME=(-1/1,0/1,1/1,2/1).
```

For `q in Q` and positive rational `A`, `mod_A(q)` is the unique rational
in `[0,A)` differing from `q` by an integral multiple of `A`. Define

```text
F0([r]_L)=[c*r]_(L_prime),
F1([r]_L,t)=([c*r]_(L_prime),c*t),
F0_inverse([r']_(L_prime))=[c^(-1)*r']_L,
F1_inverse([r']_(L_prime),t')=([c^(-1)*r']_L,c^(-1)*t').
```

The strict-scale fixture is ordered

```text
CSTRICT=(1/2,1/1,3/2,2/1), L_prime=c*L.
```

Only `1/1` preserves the literal time marker. The three other fixture
scales must each be rejected. This is a finite rational algebra check, not
a claim about every real scale or a proof that a plain topos/quantale
recovers `L`.

### 4.5 Fixed-prime fixture

The ordered symbolic prime tokens are

```text
P=(2,3,5).
```

No primality test, logarithm evaluation, approximation, enumeration of the
actual packet, or standard topology is part of the fixture. For token `p`,
the only admissible Paper-9 inputs are exactly

```text
actual_topology_input=INDISCRETE_FROM_PAPER9
stabilizer_input=(log p)Z
```

Here `p` is a metavariable only: the serialized value for prime token `n` is
exactly `(log n)Z`, so the three frozen values are `(log 2)Z`, `(log 3)Z`,
and `(log 5)Z`, with the displayed spaces inside `log n` and no other
whitespace. They may be substituted only after
`generic_theorem_state=PROVED_UPSTREAM_BEFORE_SUBSTITUTION`.

## 5. Independent-oracle architecture

The future generator and verifier have disjoint authority:

1. `code/generate_controls.py` computes the subject records and canonical
   bytes. It may not import `code/test_controls.py` or read an expected
   detector token to decide a semantic result.
2. `code/test_controls.py` may execute the generator as a subprocess but may
   not import it, call its helpers, or share a generated fixture module.
3. Before checking any row, the verifier quarantines persisted `status`,
   `detected`, `negative_reason`, `subject_value`, `oracle_value`,
   `subject_composable`, `arrow_open`, `record_equal`, `licensed`, and
   `inverse_value` wherever
   those columns occur. It reconstructs every derived field, result, and
   detector from primitive typed fields and the frozen policy, then compares
   the reconstruction with the stored bytes.
4. A negative fixture passes only when the independently recomputed semantic
   predicate rejects it. Supplying the expected detector name never changes
   that predicate.
5. Summary totals are recomputed from parsed raw rows; the summary and
   manifest may not validate one another circularly.

The independent representation for each CSV is fixed:

| CSV | Generator representation | Verifier/oracle representation |
|---|---|---|
| range-first/handedness | `D3` pair formula and right/left carrier tables | permutations of three vertices plus relational source/range graphs |
| action-blind opens | explicit arrow relations and images under groupoid product/inverse | `C4` subset bitmasks and modular set arithmetic |
| connected/disconnected | modular integer action table | powers of the frozen three-cycle permutation; receipts checked only as bindings |
| domain guards | emitted typed owner/claim records | closed owner-domain policy keyed by topology and evidence mode |
| quantale/localic | emitted three-bit gate records | independent Boolean conjunction plus receipt-type validation |
| actual/standard | emitted owner packets | immutable canonical packet registry keyed only by packet ID |
| dilation/marker | `fractions.Fraction` maps | reduced numerator/denominator cross-products and integer congruences |
| fixed-prime | emitted substitution/provenance records | two-input post-generic allowlist plus direct Paper-9 SHA-256 check |

The verifier must contain no fallback that treats a matching stored derived
field, `status`, `detected`, `negative_reason`, `oracle`, summary total, or
manifest value as semantic evidence. It selects an oracle from the fixed
artifact path and row family, then separately requires the stored `oracle`
token to match; that token never selects or weakens the check.

## 6. Exact per-CSV contracts

### 6.1 C17-1 — `range_first_handedness_controls.csv`

Exact 17-column header:

```text
schema_version,row_id,row_family,case_kind,group_token,object_x,h,object_y,k,sheet_a,subject_composable,subject_value,oracle_value,detected,negative_reason,oracle,status
```

Every row has `group_token=D3`,
`oracle=D3_RELATION_AND_LEFT_ACTION`, and
`scope=FINITE_GROUP_DIAGNOSTIC_ONLY` by the artifact-level contract. The
scope is not repeated as a column in this CSV. Canonical values are:

```text
arrow:       a(xij;dkl)
source/range source=<object-token>;range=<object-token>
nonproduct:  NONCOMPOSABLE
sheet:       sij
```

The exact row-family order and counts are:

| Order | Row family | Enumeration | Rows | Negative rows |
|---:|---|---|---:|---:|
| 1 | `ARROW` | `object_x` in `X_D3`, then `h` in `H_D3` | 36 | 0 |
| 2 | `UNIT` | `object_x` in `X_D3` | 6 | 0 |
| 3 | `INVERSE` | `object_x`, then `h` | 36 | 0 |
| 4 | `PAIR` | first arrow in `X_D3 x H_D3`, then second arrow in the same order | 1296 | 0 |
| 5 | `SHEET_ACTION` | `h`, then `sheet_a` in `S_D3` | 36 | 0 |
| 6 | `SHEET_ASSOC` | `h`, then `k`, then `sheet_a` | 216 | 0 |
| 7 | `WRONG_PRODUCT_ORDER` | the 18 ordered noncommuting `(h,k)` pairs | 18 | 18 |
| 8 | `OPPOSITE_SHEET_ACTION` | the same 18 ordered pairs | 18 | 18 |
| **Total** |  |  | **1662** | **36** |

IDs are `GH-0001` through `GH-1662` without gaps.

For `ARROW`, `subject_value` and `oracle_value` serialize source then range.
For `UNIT`, they serialize `a(x;d00)`. For `INVERSE`, they serialize
`a(x.h;h^(-1))`. For every `PAIR`, `subject_composable` is present; it is
`true` exactly when `object_y=object_x.h`. A composable row serializes the
product, and a noncomposable row serializes `NONCOMPOSABLE`. Exactly 216 of
the 1296 pair rows are composable.

`SHEET_ACTION` records `h.sheet_a`. `SHEET_ASSOC` records the left-action
identity `h.(k.a)=(h*k).a`. In `WRONG_PRODUCT_ORDER`, the subject is the
semantically constructed candidate `a(x00;k*h)` and the independent oracle
is `a(x00;h*k)`. In `OPPOSITE_SHEET_ACTION`, the subject is `(k*h).s00` and
the oracle is `(h*k).s00`. The negative rows are included only when the two
group products differ. Their reasons are respectively

```text
WRONG_GROUP_PRODUCT_ORDER             count=18
OPPOSITE_SHEET_ACTION_HANDEDNESS       count=18
```

For every nonnegative family, `subject_value` is the generator-computed
canonical token just described and `oracle_value` is the independently
computed token in the same grammar; equality is required. In particular,
the source/range record is exactly
`source=<source-token>;range=<range-token>`, and each sheet-family value is
the final `sij` token, not an unevaluated expression. In each negative
family, the two fields are the distinct evaluated arrow or sheet tokens
specified above. No expression containing `*`, `.`, parentheses, or an
inverse exponent is serialized except the fixed arrow-token punctuation.

The verifier obtains `h*k` by composing permutations, not by reading the
subject pair formula. A supplied reason token cannot make a commuting pair
pass as a negative.

### 6.2 C17-2 — `action_blind_open_records.csv`

Exact 16-column header:

```text
schema_version,row_id,row_family,case_kind,action_case,comparison_case,subset_u,subset_v,arrow_open,subject_value,oracle_value,record_equal,detected,negative_reason,oracle,status
```

All rows have `case_kind=DIAGNOSTIC`, empty `detected` and
`negative_reason`, `oracle=C4_BITSET_OPEN_QUANTALE`, and artifact scope
`FINITE_INDISCRETE_C4_CONSISTENCY_ONLY`. The action order is

```text
TRIVIAL,TRANSITIVE,NONTRANSITIVE.
```

The exact family order is:

| Order | Row family | Enumeration | Rows |
|---:|---|---|---:|
| 1 | `OPEN_DESCRIPTOR` | action, then `U` bitmask `0..15` | 48 |
| 2 | `INVOLUTION` | action, then `U` | 48 |
| 3 | `PRODUCT` | action, then `U`, then `V` | 768 |
| 4 | `BASE` | action, then `U` | 48 |
| 5 | `CROSS_OPEN` | comparison action `TRANSITIVE,NONTRANSITIVE`, then `U` | 32 |
| 6 | `CROSS_INVOLUTION` | comparison action, then `U` | 32 |
| 7 | `CROSS_PRODUCT` | comparison action, then `U`, then `V` | 512 |
| 8 | `CROSS_BASE` | comparison action, then `U` | 32 |
| **Total** |  |  | **1520** |

IDs are `AO-0001` through `AO-1520`. The per-action families leave
`comparison_case` and `record_equal` empty. Their values are generated from
the explicit arrow relation for that action, while the oracle values are:

```text
OPEN_DESCRIPTOR: X4x[U]
INVOLUTION:      -U
PRODUCT:         U+V
BASE:            true iff U=EMPTY or U=0|1|2|3.
```

These are value formulas, not serialized expression strings. For an
`OPEN_DESCRIPTOR` row, `arrow_open`, `subject_value`, and `oracle_value` are
the same evaluated `X4x[<subset-token>]` descriptor. For `INVOLUTION` and
`PRODUCT`, both value fields contain the evaluated output subset token in
the Section-3 ordered-set grammar. For `BASE`, both contain the evaluated
Boolean. No value field contains the literal characters `-U`, `U+V`, or
`base(U)`.

Cross rows set `action_case=TRIVIAL`, put the compared action in
`comparison_case`, and require `record_equal=true`. This asserts equality
of the named open record only, never equality of the underlying actions.
Their `subject_value` is recomputed from the compared action relation and
their `oracle_value` from the trivial relation. No cross row may copy the
preceding row's value.
`CROSS_OPEN` also places the evaluated compared-action descriptor in
`arrow_open`; the other three cross families leave `arrow_open` empty.
Cross involution/product/base values use the same evaluated subset/Boolean
serialization as their corresponding per-action families.
Before accepting any cross row, the verifier independently requires the
three frozen action relations themselves to be pairwise distinct, with the
transitive orbit count `1` and nontransitive orbit count `2`; record equality
therefore cannot pass through accidental action-table collapse.
The 48 open descriptors, 48 involutions, 768 products, and 48 base checks
for the three actions must agree exactly. This finite equality is a
consistency model for the locked direct calculation only; it is not a proof
of Theorem 5.1 for `R` or arbitrary `H`.

Explicit negative rows: `0`.

### 6.3 C17-3 — `connected_disconnected_firewall.csv`

Exact 16-column header:

```text
schema_version,row_id,row_family,case_kind,owner_domain,input_n,input_sheet,claim_token,subject_value,oracle_value,scope_token,source_binding,detected,negative_reason,oracle,status
```

All rows use `oracle=SOURCE_RECEIPT_PLUS_Z3_PERMUTATION`. Row-family order:

| Order | Row family | Exact contents | Rows | Negative rows |
|---:|---|---|---:|---:|
| 1 | `SYMBOLIC_RECEIPT` | the three receipt tokens below, in order | 3 | 0 |
| 2 | `Z3_ACTION` | `input_n=0,1,2`, then `input_sheet=z0,z1,z2` | 9 | 0 |
| 3 | `Z3_PROPERTY` | the three property tokens below | 3 | 0 |
| 4 | `PROMOTION_ATTACK` | the four attacks below | 4 | 4 |
| **Total** |  |  | **19** | **4** |

IDs are `CZ-0001` through `CZ-0019`. The three receipt rows are exactly:

```text
CONNECTED_REAL_CONCLUSION=B(G(X,R))~=Set
FINITE_CONTROL_LIMIT=NO_FINITE_PROOF_OF_CONNECTED_R_OR_TOPOS_EQUIVALENCE
DISCONNECTED_FIREWALL=DO_NOT_INFER_SET_FOR_ARBITRARY_DISCONNECTED_TIME
```

They use `owner_domain=ACTUAL_USUAL_R`,
`scope_token=SYMBOLIC_SOURCE_OWNED`, and
`source_binding=P17-P2-CONTROL-DESIGN-GATE-v1.0:C17-3`. Their oracle checks
the exact binding and literal only, never the theorem's truth.

`Z3_ACTION` uses `owner_domain=DISCRETE_Z_VIA_C3_QUOTIENT`,
`scope_token=FINITE_Z3_FALSIFIER_ONLY`, and stores the independently checked
sheet result: `subject_value` and `oracle_value` are both the evaluated
`z0`, `z1`, or `z2` token. `Z3_PROPERTY` uses that same owner and scope. The
property tokens, in order, are

```text
GENERATOR_NONTRIVIAL=true
REGULAR_QUOTIENT_TRANSITIVE=true
NONTERMINAL_THREE_SHEETS=true
```

The four negative reasons, once each and in this order, are:

```text
FINITE_PROXY_PROVES_CONNECTED_R
FINITE_PROXY_PROVES_TOPOS_EQUIVALENCE
DISCONNECTED_TIME_FORCES_SET
FINITE_PROXY_GENERALIZES_ALL_DISCONNECTED_H
```

Their corresponding primitive `claim_token` values, in the same order, are

```text
CERTIFY_CONNECTED_R
CERTIFY_TOPOS_EQUIVALENCE
FORCE_SET_FOR_DISCONNECTED_TIME
GENERALIZE_ALL_DISCONNECTED_H
```

The three receipt rows use, respectively, `CONNECTED_REAL_CONCLUSION`,
`FINITE_CONTROL_LIMIT`, and `DISCONNECTED_FIREWALL` as `claim_token`; the
three `Z3_PROPERTY` rows use, respectively, `GENERATOR_NONTRIVIAL`,
`REGULAR_QUOTIENT_TRANSITIVE`, and `NONTERMINAL_THREE_SHEETS`;
only `Z3_ACTION` leaves it empty. Receipt `subject_value` and `oracle_value`
both equal the complete displayed `NAME=value` literal. Property
`subject_value` and `oracle_value` both equal the complete displayed
`NAME=true` literal. These assignments are not inferred from row adjacency.

Each negative's `subject_value` is its prohibited promotion claim;
`oracle_value=REJECTED`. The detector uses the owner/scope policy and the
nontrivial three-cycle, not the reason string.
Every negative has `owner_domain=DISCRETE_Z_VIA_C3_QUOTIENT`, empty
`input_n,input_sheet,source_binding`, and
`scope_token=FINITE_Z3_FALSIFIER_ONLY`; its subject is exactly the
Section-3 `CLAIM[<negative_reason>]` string. Thus every column of all four
families is fixed.

### 6.4 C17-4 — `domain_guard_controls.csv`

Exact 15-column header:

```text
schema_version,row_id,row_family,case_kind,owner_domain,topology_token,claim_token,evidence_mode,subject_value,oracle_value,scope_token,detected,negative_reason,oracle,status
```

All rows use `oracle=OWNER_DOMAIN_POLICY`. The exact owner order is

```text
ACTUAL_USUAL_R,CONTROL_C3_DISCRETE,CONTROL_C4_DISCRETE
```

with topology/evidence pairs

```text
ACTUAL_USUAL_R:       USUAL_NONDISCRETE_R / SYMBOLIC_SOURCE_RECEIPT_ONLY
CONTROL_C3_DISCRETE:  FINITE_DISCRETE_C3 / FINITE_DIAGNOSTIC_ONLY
CONTROL_C4_DISCRETE:  FINITE_DISCRETE_C4 / FINITE_DIAGNOSTIC_ONLY.
```

The four claim tokens, in order, are

```text
OPEN_GROUPOID,NONETALE,NONUNITAL,LOCALIC_RECONSTRUCTION.
```

The family order and counts are:

| Order | Row family | Enumeration | Rows | Negative rows |
|---:|---|---|---:|---:|
| 1 | `OWNER_RECEIPT` | three owners | 3 | 0 |
| 2 | `CLAIM_SCOPE` | owner, then four claim tokens | 12 | 0 |
| 3 | `WRONG_DOMAIN_ATTACK` | ten attacks below | 10 | 10 |
| **Total** |  |  | **25** | **10** |

IDs are `DG-0001` through `DG-0025`. For the actual owner, the first three
claims have `oracle_value=SYMBOLIC_SOURCE_OWNED`; localic reconstruction has
`oracle_value=SYMBOLIC_QH_GATE_ONLY`. For either discrete proxy, the open
claim is `FINITE_DIAGNOSTIC_ONLY`, non-etale and nonunital are
`FALSE_IN_DISCRETE_PROXY`, and localic reconstruction is
`NOT_CERTIFIABLE_BY_FINITE_PROXY`.

The ten isolated negative reasons, once each and in order, are:

```text
C3_PROXY_CERTIFIES_R_NONETALE
C4_PROXY_CERTIFIES_R_NONETALE
C3_PROXY_CERTIFIES_R_NONUNITAL
C4_PROXY_CERTIFIES_R_NONUNITAL
DISCRETE_SINGLETON_OPEN_IMPORTED_TO_R
DISCRETE_LOCAL_CHART_IMPORTED_TO_R
USUAL_R_RELABELLED_DISCRETE
DISCRETE_PROXY_RELABELLED_USUAL_R
R_NONETALE_GENERALIZED_ALL_H
R_NONUNITAL_GENERALIZED_ALL_H
```

`OWNER_RECEIPT` serializes both value fields exactly as
`owner=<owner>;topology=<topology>;evidence=<evidence>` in that key order.
For `CLAIM_SCOPE`, `subject_value=<claim_token>=true` and `oracle_value` is
the exact policy result stated above. The ten attack rows have the following
complete typed inputs; the displayed nonstandard topology, evidence, and
claim tokens are admitted only in the named negative row:

| Reason | `owner_domain` | `topology_token` | `claim_token` | `evidence_mode` |
|---|---|---|---|---|
| `C3_PROXY_CERTIFIES_R_NONETALE` | `ACTUAL_USUAL_R` | `USUAL_NONDISCRETE_R` | `NONETALE` | `FINITE_C3_PROXY` |
| `C4_PROXY_CERTIFIES_R_NONETALE` | `ACTUAL_USUAL_R` | `USUAL_NONDISCRETE_R` | `NONETALE` | `FINITE_C4_PROXY` |
| `C3_PROXY_CERTIFIES_R_NONUNITAL` | `ACTUAL_USUAL_R` | `USUAL_NONDISCRETE_R` | `NONUNITAL` | `FINITE_C3_PROXY` |
| `C4_PROXY_CERTIFIES_R_NONUNITAL` | `ACTUAL_USUAL_R` | `USUAL_NONDISCRETE_R` | `NONUNITAL` | `FINITE_C4_PROXY` |
| `DISCRETE_SINGLETON_OPEN_IMPORTED_TO_R` | `ACTUAL_USUAL_R` | `USUAL_NONDISCRETE_R` | `OPEN_GROUPOID` | `DISCRETE_SINGLETON_OPEN` |
| `DISCRETE_LOCAL_CHART_IMPORTED_TO_R` | `ACTUAL_USUAL_R` | `USUAL_NONDISCRETE_R` | `OPEN_GROUPOID` | `DISCRETE_LOCAL_CHART` |
| `USUAL_R_RELABELLED_DISCRETE` | `ACTUAL_USUAL_R` | `FINITE_DISCRETE_C3` | `OPEN_GROUPOID` | `SYMBOLIC_SOURCE_RECEIPT_ONLY` |
| `DISCRETE_PROXY_RELABELLED_USUAL_R` | `CONTROL_C3_DISCRETE` | `USUAL_NONDISCRETE_R` | `OPEN_GROUPOID` | `FINITE_DIAGNOSTIC_ONLY` |
| `R_NONETALE_GENERALIZED_ALL_H` | `ACTUAL_USUAL_R` | `USUAL_NONDISCRETE_R` | `NONETALE_FOR_ALL_H` | `SYMBOLIC_SOURCE_RECEIPT_ONLY` |
| `R_NONUNITAL_GENERALIZED_ALL_H` | `ACTUAL_USUAL_R` | `USUAL_NONDISCRETE_R` | `NONUNITAL_FOR_ALL_H` | `SYMBOLIC_SOURCE_RECEIPT_ONLY` |

The ten base `CLAIM_SCOPE` rows, in attack order, are exactly
`ACTUAL/NONETALE`, `ACTUAL/NONETALE`, `ACTUAL/NONUNITAL`,
`ACTUAL/NONUNITAL`, `ACTUAL/OPEN_GROUPOID`, `ACTUAL/OPEN_GROUPOID`,
`ACTUAL/OPEN_GROUPOID`, `CONTROL_C3_DISCRETE/OPEN_GROUPOID`,
`ACTUAL/NONETALE`, and `ACTUAL/NONUNITAL`, where `ACTUAL` abbreviates the
exact `ACTUAL_USUAL_R` owner token only in this prose. Each attack changes
exactly one typed field from its listed base row with all other semantic
fields held byte-identical. Its
`subject_value` is exactly `CLAIM[<negative_reason>]` and
`oracle_value=REJECTED`. The oracle derives the rejection from the typed
owner, topology, claim, and evidence fields after blanking the supplied
reason. No discrete proxy can certify the
nondiscrete-real non-etale or nonunital claims.

`ACTUAL_USUAL_R` owner/claim rows use
`scope_token=SYMBOLIC_SOURCE_OWNED`; both proxy owner/claim rows use
`FINITE_DIAGNOSTIC_ONLY`; every attack uses
`NO_REAL_OR_LOCALIC_CERTIFICATION`.

### 6.5 C17-5 — `quantale_localic_firewall.csv`

Exact 18-column header:

```text
schema_version,row_id,row_family,case_kind,owner_domain,bare_quantale_receipt,q_h_receipt,local_compactness_receipt,promotion_attempt,licensed,subject_value,oracle_value,source_binding,scope_token,detected,negative_reason,oracle,status
```

All rows use `oracle=BARE_Q_QH_LC_CONJUNCTION`. The three Boolean input
columns are the only inputs to the executable gate predicate

```text
licensed = bare_quantale_receipt and q_h_receipt and local_compactness_receipt.
```

Every displayed three-bit token is read left-to-right in exactly that header
order: bare quantale, `q_H`, local compactness.

The booleans are typed receipts; the control does not establish any receipt's
underlying mathematical truth. Here `licensed=true` means only "the finite
packet may carry the already locked localic-reconstruction receipt after all
three named gates are present"; it is not a sufficient-hypothesis theorem or
a proof that the source theorem applies.

| Order | Row family | Enumeration | Rows | Negative rows |
|---:|---|---|---:|---:|
| 1 | `SOURCE_RECEIPT` | `BARE_QUANTALE`, `Q_H_COMPARISON`, `LOCAL_COMPACTNESS` | 3 | 0 |
| 2 | `GATE_TRUTH_TABLE` | bit triples `000,001,010,011,100,101,110,111` | 8 | 0 |
| 3 | `PROMOTION_ATTACK` | the seven unlicensed triples in the same order | 7 | 7 |
| 4 | `OWNER_SCOPE` | `ACTUAL_USUAL_R`, `CONTROL_Z_DISCRETE`, `ARBITRARY_TOPOLOGICAL_H` | 3 | 0 |
| **Total** |  |  | **21** | **7** |

IDs are `QL-0001` through `QL-0021`. The three source receipts use
`owner_domain=GENERIC_H`,
`source_binding=P17-P2-CONTROL-DESIGN-GATE-v1.0:C17-5`,
`scope_token=SYMBOLIC_SOURCE_RECEIPT_ONLY`, and bind separately:

```text
BARE_QUANTALE=O(G)~=O(H)_DIRECT
Q_H_COMPARISON=q_H_REQUIRED_SEPARATELY
LOCAL_COMPACTNESS=SOURCE_DOMAIN_REQUIRED_SEPARATELY
```

For each `SOURCE_RECEIPT`, the Boolean column named by that row is `true`,
the other two Boolean columns are empty, and `promotion_attempt,licensed`
are empty. `subject_value` and `oracle_value` both equal the complete
displayed `NAME=value` literal. The row has the generic owner, exact gate
binding, and receipt scope already fixed above.

The truth table has `promotion_attempt=false`; its subject and oracle values
are the recomputed `licensed` Boolean serialized as `true` or `false`.
It has empty `owner_domain,source_binding`. Promotion rows likewise have
empty `owner_domain,source_binding`, set `promotion_attempt=true` and
`licensed=false`, use the Section-3 prohibited-claim subject, and set
`oracle_value=REJECTED`. Their unique reasons, in bit-triple order, are:

```text
000 LOCALIC_WITHOUT_BARE_QH_LC
001 LOCALIC_WITH_ONLY_LC
010 LOCALIC_WITH_ONLY_QH
011 LOCALIC_WITHOUT_BARE_QUANTALE
100 BARE_QUANTALE_ALONE_PROMOTED
101 BARE_QUANTALE_LC_WITHOUT_QH
110 BARE_QUANTALE_QH_WITHOUT_LC
```

`ACTUAL_USUAL_R` and `CONTROL_Z_DISCRETE` owner rows say only
`SYMBOLIC_SOURCE_THEOREM_ONLY`; the arbitrary-`H` row says
`BARE_ONLY_NO_RECONSTRUCTION`. The exact `100` negative is the mandatory
bare-quantale-to-localic promotion attack. No row proves `q_H`, local
compactness, or reconstruction.

Source-receipt rows use `SYMBOLIC_SOURCE_RECEIPT_ONLY`. Truth-table and
promotion rows use `NO_REAL_OR_LOCALIC_CERTIFICATION`. The actual-`R` and
discrete-`Z` owner rows use `SYMBOLIC_SOURCE_OWNED`; arbitrary `H` uses
`NO_REAL_OR_LOCALIC_CERTIFICATION`. Every `OWNER_SCOPE` source binding is
the exact `P17-P2-CONTROL-DESIGN-GATE-v1.0:C17-5` token.
For `OWNER_SCOPE`, `promotion_attempt=false`; the actual-`R` and discrete-
`Z` rows have receipt/receipt/receipt/licensed values
`true,true,true,true`, and arbitrary `H` has `true,false,false,false`, in
header order. Both value fields contain the one exact owner-policy token
stated for that row.

### 6.6 C17-6 — `actual_standard_owner_controls.csv`

Exact 17-column header:

```text
schema_version,row_id,row_family,case_kind,packet_id,owner_token,topology_token,topos_token,quantale_token,base_frame_token,comparison_field,subject_value,oracle_value,detected,negative_reason,oracle,status
```

All rows use `oracle=CANONICAL_OWNER_PACKET_REGISTRY`. The two canonical
packets are exactly:

```text
ACTUAL:
  owner_token=ACTUAL_INDISCRETE_ORBIT
  topology_token=INDISCRETE
  topos_token=Set
  quantale_token=O(R)
  base_frame_token=2

STANDARD:
  owner_token=STANDARD_CIRCLE
  topology_token=STANDARD_CIRCLE
  topos_token=BZ
  quantale_token=O(S_LxR)
  base_frame_token=O(S_L)
```

Here `O(S_LxR)` is the canonical no-space CSV spelling of the mathematical
record `O(S_L x R)`. Thus the required comparison is literally preserved as

```text
actual:   Set / O(R)      / base 2,
standard: BZ  / O(S_LxR) / base O(S_L).
```

Family order:

| Order | Row family | Exact contents | Rows | Negative rows |
|---:|---|---|---:|---:|
| 1 | `OWNER_RECORD` | `ACTUAL`, then `STANDARD` | 2 | 0 |
| 2 | `FIELD_COMPARISON` | `owner,topology,topos,quantale,base` | 5 | 0 |
| 3 | `OWNER_SPLICE_ATTACK` | eleven isolated mutations below | 11 | 11 |
| **Total** |  |  | **18** | **11** |

IDs are `AS-0001` through `AS-0018`. Every comparison row has
`packet_id=CROSS_PACKET` and serializes
`subject_value=<comparison_field>:<actual-token>|<standard-token>` for its one field and
requires exact inequality. The negative registry is:

```text
ACTUAL_PACKET_OWNER_RELABELLED_STANDARD
STANDARD_TOPOLOGY_IMPORTED_ACTUAL
STANDARD_TOPOS_SPLICED_ACTUAL
STANDARD_QUANTALE_SPLICED_ACTUAL
STANDARD_BASE_SPLICED_ACTUAL
STANDARD_PACKET_OWNER_RELABELLED_ACTUAL
INDISCRETE_TOPOLOGY_IMPORTED_STANDARD
ACTUAL_TOPOS_SPLICED_STANDARD
ACTUAL_QUANTALE_SPLICED_STANDARD
ACTUAL_BASE_SPLICED_STANDARD
ACTUAL_STANDARD_BASES_IDENTIFIED
```

`OWNER_RECORD` puts its complete Section-3 owner-packet serialization in
both value fields and leaves `comparison_field` empty. `FIELD_COMPARISON`
uses `packet_id=CROSS_PACKET`, leaves the five packet columns empty, uses
`comparison_field=owner,topology,topos,quantale,base` in that order, and puts
the complete `<field>:<actual>|<standard>` record in both value fields.

For the first five negative rows, `packet_id=ACTUAL`, the other four packet
fields remain the canonical actual values, and the named field is replaced
respectively by the canonical standard `owner`, `topology`, `topos`,
`quantale`, or `base` value. For the next five, `packet_id=STANDARD`, the
other four fields remain canonical standard values, and the corresponding
field is replaced by the canonical actual value. Their
`comparison_field` values are respectively
`owner,topology,topos,quantale,base,owner,topology,topos,quantale,base`.
Each subject is the complete mutated packet and each oracle is the complete
canonical packet for its unchanged `packet_id`.

The final negative has `packet_id=CROSS_PACKET`, empty five packet-value
columns, `comparison_field=base`,
`subject_value=base_relation=EQUAL`, and
`oracle_value=base_relation=DISTINCT`. Thus each row changes exactly one
semantic field or the one comparison relation. The oracle is keyed by
`packet_id` and never accepts the remaining fields as a substitute owner.
These are actual/standard owner-splice negatives, not evidence that either
symbolic packet is mathematically correct.

### 6.7 C17-7 — `dilation_strict_marker_controls.csv`

Exact 19-column header:

```text
schema_version,row_id,row_family,case_kind,L,L_prime,scale_c,r,t,u,claim_token,subject_value,oracle_value,inverse_value,scope_token,detected,negative_reason,oracle,status
```

All rows use `oracle=INTEGER_CROSS_MULTIPLICATION_DILATION`. Rational values
use the canonical form in Section 3. `subject_value`, `oracle_value`, and
`inverse_value` serialize quotient representatives and arrow pairs with the
exact grammar

```text
q(<r>mod<L>)
g(q(<r>mod<L>);<t>)
```

with no spaces.

| Order | Row family | Enumeration | Rows | Negative rows |
|---:|---|---|---:|---:|
| 1 | `SYMBOLIC_RECEIPT` | `UNMARKED_DILATION_ALGEBRA_ONLY`, `STRICT_MARKER_EXTRA_STRUCTURE` | 2 | 0 |
| 2 | `OBJECT_MAP` | `r` in `RREP` | 4 | 0 |
| 3 | `ARROW_MAP` | `r`, then `t` | 16 | 0 |
| 4 | `SOURCE_COMPAT` | `r`, then `t` | 16 | 0 |
| 5 | `RANGE_COMPAT` | `r`, then `t` | 16 | 0 |
| 6 | `INVERSE_COMPAT` | `r`, then `t` | 16 | 0 |
| 7 | `PRODUCT_COMPAT` | `r`, then `t`, then `u` | 64 | 0 |
| 8 | `STRICT_MARKER` | `c` in `CSTRICT` | 4 | 3 |
| 9 | `PLAIN_SCALE_PROMOTION` | `TOPOS`, then `QUANTALE` | 2 | 2 |
| **Total** |  |  | **140** | **5** |

IDs are `DM-0001` through `DM-0140`. The receipt rows use
`scope_token=SYMBOLIC_SOURCE_RECEIPT_ONLY`. Their `subject_value` and
`oracle_value` both equal the complete receipt name, and the independent
oracle checks that literal only. The package-level manifest must separately
validate its binding to the control-design gate; this CSV deliberately has
no row-level `source_binding` column. Rows 2--7 use
`scope_token=ALGEBRAIC_RATIONAL_FIXTURE_ONLY`.

`OBJECT_MAP` and `ARROW_MAP` record the forward value and the result of the
declared inverse. `SOURCE_COMPAT`, `RANGE_COMPAT`, `INVERSE_COMPAT`, and
`PRODUCT_COMPAT` compare the two algebraic paths prescribed by the
range-first formulas. The generator uses rational operations; the oracle
clears denominators and checks integer equalities and congruences without
calling the generator's map helpers.

For `OBJECT_MAP`, `subject_value` is the evaluated serialized `F0` output,
`oracle_value` is the same output independently obtained by integer
congruence, and `inverse_value` is the serialized original quotient after
applying `F0_inverse`. For `ARROW_MAP`, the analogous three fields are the
evaluated `F1` output, the independently obtained output, and the serialized
original arrow after `F1_inverse`. For each compatibility family,
`subject_value` is the evaluated leftmost path below and `oracle_value` is
the evaluated rightmost path; `inverse_value` is empty. Intermediate
expressions and equality signs are never serialized.

The four compatibility families check these exact equalities:

```text
SOURCE:  F0([r+t]_L) = [c*r+c*t]_(L_prime) = s(F1([r]_L,t))
RANGE:   F0([r]_L) = [c*r]_(L_prime) = r(F1([r]_L,t))
INVERSE: F1([r+t]_L,-t) = F1([r]_L,t)^(-1)
PRODUCT: F1([r]_L,t+u) = F1([r]_L,t) F1([r+t]_L,u)
```

For `STRICT_MARKER`, `c=1/1` is diagnostic and accepted. Each other listed
scale is a separate negative row with common reason

```text
STRICT_MARKER_NONUNIT_SCALE count=3.
```

The two remaining reasons occur once each:

```text
PLAIN_TOPOS_NUMERICAL_SCALE_PROMOTION
PLAIN_QUANTALE_NUMERICAL_SCALE_PROMOTION
```

`claim_token=STRICT_TIME_MARKER` on every strict row. The two plain rows use
`claim_token=PLAIN_TOPOS_RECOVERS_L` and
`PLAIN_QUANTALE_RECOVERS_L`, respectively. Rows `OBJECT_MAP` through
`PRODUCT_COMPAT` leave `claim_token` empty; the receipt rows use their
receipt names as claim tokens.

Every `STRICT_MARKER` row has
`scope_token=ALGEBRAIC_RATIONAL_FIXTURE_ONLY` and
`subject_value=strict_marker_preserved=true`. At `c=1/1`,
`oracle_value=strict_marker_preserved=true`; at each nonunit scale,
`oracle_value=REJECTED`. Each `PLAIN_SCALE_PROMOTION` row has
`scope_token=NO_REAL_OR_LOCALIC_CERTIFICATION`, the exact Section-3
`CLAIM[<negative_reason>]` subject, `oracle_value=REJECTED`, and empty
`inverse_value`. The two receipt rows also have empty `inverse_value`.

Thus every nonunit scale in the frozen strict fixture is rejected, and no
row claims that a plain topos or bare/open quantale recovers numerical `L`.

### 6.8 C17-8 — `fixed_prime_provenance_controls.csv`

Exact 17-column header:

```text
schema_version,row_id,row_family,case_kind,prime_token,generic_theorem_state,actual_topology_input,stabilizer_input,claim_token,subject_value,oracle_value,source_binding,scope_token,detected,negative_reason,oracle,status
```

All rows use `oracle=P9_TWO_INPUT_POST_GENERIC_ALLOWLIST`. The exact source
binding is

```text
papers/9-packet-separation/paper/manuscript.tex@sha256:24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb
```

and must be checked directly before a fixed-prime row can validate.

| Order | Row family | Enumeration | Rows | Negative rows |
|---:|---|---|---:|---:|
| 1 | `GENERIC_PRECONDITION` | one exact receipt | 1 | 0 |
| 2 | `FIXED_PRIME_SUBSTITUTION` | primes `2,3,5` | 3 | 0 |
| 3 | `ALLOWED_P9_INPUT` | prime, then `INDISCRETENESS,LITERAL_STABILIZER` | 6 | 0 |
| 4 | `PROVENANCE_PROMOTION_ATTACK` | eleven attacks below | 11 | 11 |
| **Total** |  |  | **21** | **11** |

IDs are `FP-0001` through `FP-0021`. The precondition is exactly

```text
generic_theorem_state=PROVED_UPSTREAM_BEFORE_SUBSTITUTION
```

and is a receipt, not a proof. Each substitution row contains only
`INDISCRETE_FROM_PAPER9` and its prime-substituted literal `(log n)Z` from
Section 4.5; it evaluates neither `log n` nor any analytic structure. The
eleven unique negative reasons are:

```text
C_STAR_PROMOTION
HAAR_PROMOTION
MEASURE_PROMOTION
TRACE_PROMOTION
DETERMINANT_PROMOTION
ROUTE_B_PROMOTION
PRIORITY_PROMOTION
STANDARD_TOPOLOGY_PROMOTION
NUMERICAL_LOG_EVALUATION
FIXED_PRIME_SUBSTITUTION_BEFORE_GENERIC
NONLITERAL_STABILIZER_REWRITE
```

Each changes one claim, topology input, stabilizer input, or ordering flag
from a valid `p=2` substitution. The first seven are separate methods and
separate rows; C-star, Haar, measure, trace, determinant, Route-B, and
priority are never bundled behind one generic rejection.

The exact nonnegative field assignments are:

- `GENERIC_PRECONDITION` has empty `prime_token`, topology, and stabilizer;
  `claim_token=GENERIC_PRECONDITION`; and both value fields equal
  `generic_theorem_state=PROVED_UPSTREAM_BEFORE_SUBSTITUTION`.
- Each `FIXED_PRIME_SUBSTITUTION` has
  `claim_token=FIXED_PRIME_SUBSTITUTION`; for prime token `n`, both value
  fields equal
  `prime=n;topology=INDISCRETE_FROM_PAPER9;stabilizer=(log n)Z` with keys in
  that order and the one displayed space between `log` and `n`.
- For each prime, the `INDISCRETENESS` `ALLOWED_P9_INPUT` row has
  `claim_token=INDISCRETENESS` and both value fields equal
  `INDISCRETE_FROM_PAPER9`; its following `LITERAL_STABILIZER` row has that
  literal claim token and both value fields equal `(log n)Z`.

All substitution and allowed-input rows populate the exact proved generic
state and both valid input columns, even when a value field displays only
one allowed input. The eleven negative rows all have `prime_token=2`, the
Paper-9 binding and fixed-prime scope. Their complete semantic deltas from
the valid `p=2` substitution are:

| Reason | `claim_token` | Changed primitive and exact invalid value |
|---|---|---|
| `C_STAR_PROMOTION` | `C_STAR` | claim token only |
| `HAAR_PROMOTION` | `HAAR` | claim token only |
| `MEASURE_PROMOTION` | `MEASURE` | claim token only |
| `TRACE_PROMOTION` | `TRACE` | claim token only |
| `DETERMINANT_PROMOTION` | `DETERMINANT` | claim token only |
| `ROUTE_B_PROMOTION` | `ROUTE_B` | claim token only |
| `PRIORITY_PROMOTION` | `PRIORITY` | claim token only |
| `STANDARD_TOPOLOGY_PROMOTION` | `FIXED_PRIME_SUBSTITUTION` | `actual_topology_input=STANDARD_CIRCLE` |
| `NUMERICAL_LOG_EVALUATION` | `FIXED_PRIME_SUBSTITUTION` | `stabilizer_input=NUMERICAL_LOG_2` |
| `FIXED_PRIME_SUBSTITUTION_BEFORE_GENERIC` | `FIXED_PRIME_SUBSTITUTION` | `generic_theorem_state=NOT_PROVED_UPSTREAM_BEFORE_SUBSTITUTION` |
| `NONLITERAL_STABILIZER_REWRITE` | `FIXED_PRIME_SUBSTITUTION` | `stabilizer_input=LOG_2_Z_EQUIVALENT_REWRITE` |

Every other typed primitive remains byte-identical to the valid `p=2`
substitution. Each negative has the exact Section-3
`CLAIM[<negative_reason>]` subject and `oracle_value=REJECTED`; the invalid
sentinel tokens are never evaluated. This table, rather than the supplied
reason, selects the independent rejection branch.

The generic precondition uses
`source_binding=P17-P2-CONTROL-DESIGN-GATE-v1.0:C17-8` and
`scope_token=SYMBOLIC_SOURCE_RECEIPT_ONLY`. Every other row uses the exact
Paper-9 source binding above and
`scope_token=FIXED_PRIME_SUBSTITUTION_ONLY`.

### 6.9 `target_summary.csv`

Exact 12-column header:

```text
schema_version,row_id,artifact,expected_rows,expected_columns,expected_negative_rows,oracle_class,canonical_order_key,scope_token,artifact_order_index,status,notes
```

Rows `TS-0001` through `TS-0009` summarize the nine CSVs in Section-2 order,
including the self-row for `target_summary.csv`. `TS-0010` is
`PACKAGE_TOTAL`. The self-row expects 10 body rows and 12 columns. It has no
digest and creates no hash cycle. On all nine file rows,
`scope_token=COUNT_AND_SERIALIZATION_ONLY`, `status=PASS`, and `notes` is
empty. Their remaining columns are exactly:

| `row_id` | `artifact` | `expected_rows` | `expected_columns` | `expected_negative_rows` | `oracle_class` | `canonical_order_key` | `artifact_order_index` |
|---|---|---:|---:|---:|---|---|---:|
| `TS-0001` | `results/range_first_handedness_controls.csv` | 1662 | 17 | 36 | `D3_RELATION_AND_LEFT_ACTION` | `C17_1_FAMILY_ORDER` | 1 |
| `TS-0002` | `results/action_blind_open_records.csv` | 1520 | 16 | 0 | `C4_BITSET_OPEN_QUANTALE` | `C17_2_FAMILY_ORDER` | 2 |
| `TS-0003` | `results/connected_disconnected_firewall.csv` | 19 | 16 | 4 | `SOURCE_RECEIPT_PLUS_Z3_PERMUTATION` | `C17_3_FAMILY_ORDER` | 3 |
| `TS-0004` | `results/domain_guard_controls.csv` | 25 | 15 | 10 | `OWNER_DOMAIN_POLICY` | `C17_4_FAMILY_ORDER` | 4 |
| `TS-0005` | `results/quantale_localic_firewall.csv` | 21 | 18 | 7 | `BARE_Q_QH_LC_CONJUNCTION` | `C17_5_FAMILY_ORDER` | 5 |
| `TS-0006` | `results/actual_standard_owner_controls.csv` | 18 | 17 | 11 | `CANONICAL_OWNER_PACKET_REGISTRY` | `C17_6_FAMILY_ORDER` | 6 |
| `TS-0007` | `results/dilation_strict_marker_controls.csv` | 140 | 19 | 5 | `INTEGER_CROSS_MULTIPLICATION_DILATION` | `C17_7_FAMILY_ORDER` | 7 |
| `TS-0008` | `results/fixed_prime_provenance_controls.csv` | 21 | 17 | 11 | `P9_TWO_INPUT_POST_GENERIC_ALLOWLIST` | `C17_8_FAMILY_ORDER` | 8 |
| `TS-0009` | `results/target_summary.csv` | 10 | 12 | 0 | `RAW_COUNT_SCHEMA_INVENTORY` | `TARGET_SUMMARY_ROW_ORDER` | 9 |

The package row has `artifact=PACKAGE_TOTAL`, `status=PASS`, and

```text
expected_rows=3436
expected_columns=MIXED
expected_negative_rows=84
oracle_class=RAW_COUNT_SCHEMA_INVENTORY
canonical_order_key=SECTION_2_ARTIFACT_ORDER
scope_token=COUNT_AND_SERIALIZATION_ONLY
artifact_order_index=PACKAGE
notes=CSV_ARTIFACTS=9;GENERATED_ARTIFACTS=10
```

Every file row names its Section-6 oracle and exact family-order key. The
summary has zero negative rows. The verifier derives each file-row number
from the named raw CSV; for `TS-0009` it counts this CSV's raw header and ten
raw body rows without consulting that row's values. It derives package
totals from the nine parsed CSVs before comparing them to `TS-0010`; the
manifest is not an oracle for the summary.

### 6.10 Complete column dictionary and empty-field matrix

The shared columns have one meaning everywhere:

| Column | Exact meaning |
|---|---|
| `schema_version` | literal `paper17-open-groupoid-controls/1` |
| `row_id` | the family-independent sequential ID in the range frozen for that CSV |
| `row_family` | exact Section-6 family token; no aliases |
| `case_kind` | `RECEIPT`, `DIAGNOSTIC`, or `NEGATIVE` exactly as frozen |
| `subject_value` | generator-produced value or prohibited claim being tested |
| `oracle_value` | persisted copy of the expected value; ignored and independently recomputed during verification |
| `detected` | empty for nonnegatives; `true` for negatives after semantic rejection |
| `negative_reason` | empty for nonnegatives; one exact Section-7 token for negatives |
| `oracle` | the artifact's one exact Section-3 oracle token |
| `status` | `PASS` only after row construction validates; never used as an oracle |

The exact `case_kind` assignment is:

```text
C17-1: ARROW,UNIT,INVERSE,PAIR,SHEET_ACTION,SHEET_ASSOC = DIAGNOSTIC;
       WRONG_PRODUCT_ORDER,OPPOSITE_SHEET_ACTION = NEGATIVE
C17-2: every row = DIAGNOSTIC
C17-3: SYMBOLIC_RECEIPT = RECEIPT; Z3_ACTION,Z3_PROPERTY = DIAGNOSTIC;
       PROMOTION_ATTACK = NEGATIVE
C17-4: OWNER_RECEIPT = RECEIPT; CLAIM_SCOPE = RECEIPT;
       WRONG_DOMAIN_ATTACK = NEGATIVE
C17-5: SOURCE_RECEIPT,OWNER_SCOPE = RECEIPT; GATE_TRUTH_TABLE = DIAGNOSTIC;
       PROMOTION_ATTACK = NEGATIVE
C17-6: OWNER_RECORD,FIELD_COMPARISON = RECEIPT; OWNER_SPLICE_ATTACK = NEGATIVE
C17-7: SYMBOLIC_RECEIPT = RECEIPT; OBJECT_MAP through PRODUCT_COMPAT = DIAGNOSTIC;
       STRICT_MARKER is DIAGNOSTIC only for c=1/1 and NEGATIVE otherwise;
       PLAIN_SCALE_PROMOTION = NEGATIVE
C17-8: GENERIC_PRECONDITION,FIXED_PRIME_SUBSTITUTION,ALLOWED_P9_INPUT = RECEIPT;
       PROVENANCE_PROMOTION_ATTACK = NEGATIVE
```

Every file-specific column is defined here, including when it is empty:

- `range_first_handedness_controls.csv`: `group_token` is always `D3`.
  `object_x,h` are present on `ARROW`, `INVERSE`, `PAIR`, and
  `WRONG_PRODUCT_ORDER`; `object_x` alone is present on `UNIT`.
  `object_y,k` are additionally present on `PAIR`; on
  `WRONG_PRODUCT_ORDER`, `object_y=object_x.h` and `k` is present.
  `h,sheet_a` are present on `SHEET_ACTION`; `h,k,sheet_a` on
  `SHEET_ASSOC` and `OPPOSITE_SHEET_ACTION`, with `sheet_a=s00` in the
  latter. `subject_composable` is present only on `PAIR` and
  `WRONG_PRODUCT_ORDER`, where it is always `true`; all columns not named
  for the family are empty.

- `action_blind_open_records.csv`: `action_case` is present on every row.
  On per-action rows it is the row's action and `comparison_case` is empty;
  on cross rows it is `TRIVIAL` and `comparison_case` is the compared
  action. `subset_u` is present everywhere; `subset_v` only for `PRODUCT`
  and `CROSS_PRODUCT`. `arrow_open` is present only for
  `OPEN_DESCRIPTOR` and `CROSS_OPEN`. `record_equal=true` is present only
  on cross rows. `detected` and `negative_reason` are empty in all rows.

- `connected_disconnected_firewall.csv`: `owner_domain` is present in all
  rows. `input_n,input_sheet` are present only for `Z3_ACTION`.
  `claim_token` is present on receipt, property, and negative rows and empty
  on `Z3_ACTION`; negative values are the four tokens in Section 6.3.
  `scope_token` is present in every row. `source_binding` is present only
  for `SYMBOLIC_RECEIPT`; it is empty for executable/property/negative
  rows. Negative `subject_value` is the prohibited claim and
  `oracle_value=REJECTED`.

- `domain_guard_controls.csv`: `owner_domain`, `topology_token`,
  `claim_token`, `evidence_mode`, and `scope_token` are present in every
  `CLAIM_SCOPE` and `WRONG_DOMAIN_ATTACK` row. `OWNER_RECEIPT` leaves
  `claim_token` empty and serializes the owner/type record in
  `subject_value` and `oracle_value`. Every negative changes exactly one of
  the four typed input columns or the claim quantifier.

- `quantale_localic_firewall.csv`: `owner_domain` is present only on
  `SOURCE_RECEIPT` and `OWNER_SCOPE`; it is empty on the two truth-table
  families. A `SOURCE_RECEIPT` sets exactly its named receipt Boolean to
  `true` and leaves the other two receipt fields and `promotion_attempt`
  and `licensed` empty. Truth-table and attack rows populate all three
  receipt Booleans and `promotion_attempt`; `licensed` is populated on both. `OWNER_SCOPE`
  populates all three Booleans, `promotion_attempt=false`, and `licensed`:
  the actual-`R` and discrete-`Z` rows are `true,true,true,true`; arbitrary
  `H` is `true,false,false,false`. `source_binding` is present on receipt and
  owner rows and empty on truth-table/attack rows. `scope_token` is always
  present.

- `actual_standard_owner_controls.csv`: `packet_id` is present everywhere.
  All five packet-value columns are populated on `OWNER_RECORD` and
  the first ten `OWNER_SPLICE_ATTACK` rows; `comparison_field` is empty on
  owner records and names the one inspected or mutated field otherwise. `FIELD_COMPARISON`
  leaves the five packet-value columns empty and stores the two canonical
  field values in `subject_value`/`oracle_value`. The base-identification
  attack uses `packet_id=CROSS_PACKET`; its five packet-value columns are
  empty.

- `dilation_strict_marker_controls.csv`: both receipt rows leave all
  rational input columns empty. Rows `OBJECT_MAP` through
  `PRODUCT_COMPAT` always have `L=2/1,L_prime=3/1,scale_c=3/2`; `r` is
  present in all six families, `t` is empty only for `OBJECT_MAP`, and `u`
  is present only for `PRODUCT_COMPAT`. `STRICT_MARKER` has `L=2/1`, the
  enumerated `scale_c`, its computed `L_prime`, and empty `r,t,u`.
  `PLAIN_SCALE_PROMOTION` has `2/1,3/1,3/2` and empty `r,t,u`.
  `claim_token` follows the exact Section-6.7 assignment.
  `inverse_value` is populated only on `OBJECT_MAP` and `ARROW_MAP`.
  `scope_token` is present everywhere.

- `fixed_prime_provenance_controls.csv`: `GENERIC_PRECONDITION` has empty
  `prime_token`, topology, and stabilizer, and uses the control-gate C17-8
  binding. Substitution and allowed-input rows populate `prime_token`, the
  exact generic state, both Paper-9 inputs, and the Paper-9 source binding.
  Negative rows use `prime_token=2` and the Section-6.8 valid base record;
  the first seven change only `claim_token`, and the final four change only
  the exact topology, stabilizer, generic-state, or stabilizer primitive
  listed in the Section-6.8 table.
  `scope_token` is present in all rows.

- `target_summary.csv`: file rows have numeric
  `artifact_order_index=1..9`, the exact filename, count, width, negative
  count, oracle, family-order key, and scope; their `notes` field is empty.
  The package row uses `artifact_order_index=PACKAGE`, the exact aggregate
  values in Section 6.9, and the one frozen `notes` record. It contains no
  hash or byte count.

An unexpected nonempty field, or an empty field where this matrix requires a
value, is a schema failure before semantic validation.

## 7. Aggregate rows, columns, negatives, and canonical reasons

| CSV | Body rows | Columns | Explicit negatives |
|---|---:|---:|---:|
| `range_first_handedness_controls.csv` | 1662 | 17 | 36 |
| `action_blind_open_records.csv` | 1520 | 16 | 0 |
| `connected_disconnected_firewall.csv` | 19 | 16 | 4 |
| `domain_guard_controls.csv` | 25 | 15 | 10 |
| `quantale_localic_firewall.csv` | 21 | 18 | 7 |
| `actual_standard_owner_controls.csv` | 18 | 17 | 11 |
| `dilation_strict_marker_controls.csv` | 140 | 19 | 5 |
| `fixed_prime_provenance_controls.csv` | 21 | 17 | 11 |
| `target_summary.csv` | 10 | 12 | 0 |
| **Total** | **3436** | -- | **84** |

The exact package targets are:

```text
CSV_ARTIFACTS=9
GENERATED_ARTIFACTS_INCLUDING_MANIFEST=10
CSV_BODY_ROWS=3436
NONNEGATIVE_CSV_ROWS=3352
EXPLICIT_NEGATIVE_ROWS=84
EXPECTED_NEGATIVES_DETECTED=84
NEGATIVE_FAILURES=0
UNITTEST_METHODS=180
SEMANTIC_MUTATION_CLASSES=48
PACKAGE_MUTATION_CLASSES=42
ISOLATED_MUTATION_METHODS=90
UNITTEST_FAILURES=0
UNITTEST_ERRORS=0
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
```

The negative-reason vocabulary is closed. Counts are exact:

| Artifact | Reason tokens and exact multiplicities |
|---|---|
| range-first | `WRONG_GROUP_PRODUCT_ORDER=18`; `OPPOSITE_SHEET_ACTION_HANDEDNESS=18` |
| connected/disconnected | the four Section-6.3 tokens, each `=1` |
| domain guard | the ten Section-6.4 tokens, each `=1` |
| quantale/localic | the seven Section-6.5 tokens, each `=1` |
| actual/standard | the eleven Section-6.6 tokens, each `=1` |
| dilation/marker | `STRICT_MARKER_NONUNIT_SCALE=3`; both promotion tokens `=1` |
| fixed-prime | the eleven Section-6.8 tokens, each `=1` |

Any nonempty reason outside this registry, a wrong multiplicity, a reason on
a nonnegative row, or an empty reason on a negative row is a hard failure.

## 8. Exact 180-method `unittest` contract

`code/test_controls.py` must contain exactly 180 explicit source-level
methods whose names begin with `test_`. Dynamic method creation, `load_tests`,
pytest parametrization, and treating one `subTest` loop as multiple methods
are prohibited. The AST-counted source methods and the runtime-discovered
methods must both equal 180.

The exact allocation is:

| Test family | Methods |
|---|---:|
| C17-1 range-first and handedness conformance | 10 |
| C17-2 action-blind open records conformance | 10 |
| C17-3 connected/disconnected conformance | 6 |
| C17-4 domain-guard conformance | 6 |
| C17-5 quantale/localic conformance | 6 |
| C17-6 actual/standard conformance | 6 |
| C17-7 dilation/marker conformance | 8 |
| C17-8 fixed-prime/provenance conformance | 6 |
| Summary/package schema | 8 |
| Manifest/provenance | 10 |
| Deterministic reproduction/read-only | 8 |
| Oracle independence | 6 |
| Isolated semantic mutation registry | 48 |
| Isolated package/fail-closed mutation registry | 42 |
| **Total** | **180** |

### 8.1 Exact nonmutation method names

The 58 C17 conformance methods are exactly:

```text
TestC17_1RangeFirst.test_c17_1_schema_header_and_ids
TestC17_1RangeFirst.test_c17_1_family_order_and_counts
TestC17_1RangeFirst.test_c17_1_source_range_units
TestC17_1RangeFirst.test_c17_1_inverse_laws
TestC17_1RangeFirst.test_c17_1_composability_matrix
TestC17_1RangeFirst.test_c17_1_multiplication_associativity
TestC17_1RangeFirst.test_c17_1_left_sheet_action
TestC17_1RangeFirst.test_c17_1_sheet_action_associativity
TestC17_1RangeFirst.test_c17_1_wrong_order_rows_detected
TestC17_1RangeFirst.test_c17_1_oracle_recomputation

TestC17_2ActionBlind.test_c17_2_schema_header_and_ids
TestC17_2ActionBlind.test_c17_2_family_order_and_counts
TestC17_2ActionBlind.test_c17_2_same_carrier_three_actions
TestC17_2ActionBlind.test_c17_2_arrow_open_descriptors
TestC17_2ActionBlind.test_c17_2_involution_formula
TestC17_2ActionBlind.test_c17_2_product_formula
TestC17_2ActionBlind.test_c17_2_two_element_base
TestC17_2ActionBlind.test_c17_2_cross_action_open_and_inverse
TestC17_2ActionBlind.test_c17_2_cross_action_product_and_base
TestC17_2ActionBlind.test_c17_2_oracle_recomputation

TestC17_3ConnectedFirewall.test_c17_3_schema_header_and_ids
TestC17_3ConnectedFirewall.test_c17_3_receipts_are_nonexecuted
TestC17_3ConnectedFirewall.test_c17_3_z3_action_table
TestC17_3ConnectedFirewall.test_c17_3_nontrivial_transitive_nonterminal
TestC17_3ConnectedFirewall.test_c17_3_promotion_rows_detected
TestC17_3ConnectedFirewall.test_c17_3_oracle_recomputation

TestC17_4DomainGuards.test_c17_4_schema_header_and_ids
TestC17_4DomainGuards.test_c17_4_owner_registry
TestC17_4DomainGuards.test_c17_4_claim_scope_matrix
TestC17_4DomainGuards.test_c17_4_discrete_proxy_not_real_owner
TestC17_4DomainGuards.test_c17_4_wrong_domain_rows_detected
TestC17_4DomainGuards.test_c17_4_oracle_recomputation

TestC17_5QuantaleLocalic.test_c17_5_schema_header_and_ids
TestC17_5QuantaleLocalic.test_c17_5_three_separate_receipts
TestC17_5QuantaleLocalic.test_c17_5_truth_table
TestC17_5QuantaleLocalic.test_c17_5_bare_quantale_promotion_rejected
TestC17_5QuantaleLocalic.test_c17_5_owner_scope_rows
TestC17_5QuantaleLocalic.test_c17_5_oracle_recomputation

TestC17_6OwnerPackets.test_c17_6_schema_header_and_ids
TestC17_6OwnerPackets.test_c17_6_exact_actual_packet
TestC17_6OwnerPackets.test_c17_6_exact_standard_packet
TestC17_6OwnerPackets.test_c17_6_field_comparisons
TestC17_6OwnerPackets.test_c17_6_splice_rows_detected
TestC17_6OwnerPackets.test_c17_6_oracle_recomputation

TestC17_7Dilation.test_c17_7_schema_header_and_ids
TestC17_7Dilation.test_c17_7_fraction_canonicalization
TestC17_7Dilation.test_c17_7_object_arrow_round_trip
TestC17_7Dilation.test_c17_7_source_range_compatibility
TestC17_7Dilation.test_c17_7_inverse_compatibility
TestC17_7Dilation.test_c17_7_product_compatibility
TestC17_7Dilation.test_c17_7_strict_nonunit_rejections
TestC17_7Dilation.test_c17_7_plain_scale_firewall_and_oracle

TestC17_8FixedPrime.test_c17_8_schema_header_and_ids
TestC17_8FixedPrime.test_c17_8_paper9_binding
TestC17_8FixedPrime.test_c17_8_post_generic_order
TestC17_8FixedPrime.test_c17_8_only_two_allowed_inputs
TestC17_8FixedPrime.test_c17_8_promotion_rows_detected
TestC17_8FixedPrime.test_c17_8_oracle_recomputation
```

The remaining 32 nonmutation methods are exactly:

```text
TestTargetSummary.test_summary_schema_header_and_ids
TestTargetSummary.test_summary_nine_file_rows
TestTargetSummary.test_summary_self_row
TestTargetSummary.test_summary_package_row
TestTargetSummary.test_summary_raw_row_recompute
TestTargetSummary.test_summary_negative_recompute
TestTargetSummary.test_summary_column_width_recompute
TestTargetSummary.test_summary_contains_no_hash

TestManifest.test_manifest_schema_and_package_id
TestManifest.test_manifest_binding_lifecycle_order
TestManifest.test_manifest_design_gate_binding
TestManifest.test_manifest_paper9_source_binding
TestManifest.test_manifest_design_review_implementation_gate_bindings
TestManifest.test_manifest_all_implementation_paths_hashed
TestManifest.test_manifest_all_csv_artifacts_hashed
TestManifest.test_manifest_no_self_hash_or_self_entry
TestManifest.test_manifest_no_proof_or_proof_review_binding
TestManifest.test_manifest_aggregate_targets

TestReproduction.test_repro_checked_in_verify_only
TestReproduction.test_repro_fresh_generation_a_verify
TestReproduction.test_repro_fresh_generation_b_verify
TestReproduction.test_repro_checked_in_equals_a
TestReproduction.test_repro_a_equals_b
TestReproduction.test_repro_manifest_in_three_way_identity
TestReproduction.test_repro_checked_in_read_only_receipt
TestReproduction.test_repro_cleanup_and_no_cache

TestOracleIndependence.test_oracle_does_not_import_generator
TestOracleIndependence.test_generator_does_not_import_test_module
TestOracleIndependence.test_oracle_ignores_emitted_status
TestOracleIndependence.test_oracle_ignores_emitted_detector_and_reason
TestOracleIndependence.test_oracle_recomputes_values_from_primitive_fields
TestOracleIndependence.test_summary_recomputed_from_raw_inventory
```

### 8.2 Complete isolated semantic mutation registry — 48 methods

Every method below starts from a pristine valid semantic fixture, changes
exactly the stated semantic field or operation, clears all persisted receipt
fields, calls the independent oracle, and requires the exact reason. One
method may enumerate all witnesses of one mutation class (for example the 18
noncommuting pairs), but no method may cover two reason classes.

| ID | Exact `unittest` method | Single semantic delta / expected reason |
|---|---|---|
| S001 | `TestSemanticMutations.test_s001_wrong_group_product_order` | replace `h*k` by `k*h` / `WRONG_GROUP_PRODUCT_ORDER` |
| S002 | `TestSemanticMutations.test_s002_opposite_sheet_action_handedness` | reverse left-action order / `OPPOSITE_SHEET_ACTION_HANDEDNESS` |
| S003 | `TestSemanticMutations.test_s003_finite_proxy_proves_connected_r` | promote C3 fixture to real connectedness / `FINITE_PROXY_PROVES_CONNECTED_R` |
| S004 | `TestSemanticMutations.test_s004_finite_proxy_proves_topos_equivalence` | promote C3 fixture to a topos equivalence / `FINITE_PROXY_PROVES_TOPOS_EQUIVALENCE` |
| S005 | `TestSemanticMutations.test_s005_disconnected_time_forces_set` | change the Z-falsifier conclusion to `Set` / `DISCONNECTED_TIME_FORCES_SET` |
| S006 | `TestSemanticMutations.test_s006_finite_proxy_generalizes_disconnected_h` | universalize one quotient / `FINITE_PROXY_GENERALIZES_ALL_DISCONNECTED_H` |
| S007 | `TestSemanticMutations.test_s007_c3_proxy_certifies_r_nonetale` | substitute C3 evidence for actual `R` / `C3_PROXY_CERTIFIES_R_NONETALE` |
| S008 | `TestSemanticMutations.test_s008_c4_proxy_certifies_r_nonetale` | substitute C4 evidence for actual `R` / `C4_PROXY_CERTIFIES_R_NONETALE` |
| S009 | `TestSemanticMutations.test_s009_c3_proxy_certifies_r_nonunital` | substitute C3 evidence for actual `R` / `C3_PROXY_CERTIFIES_R_NONUNITAL` |
| S010 | `TestSemanticMutations.test_s010_c4_proxy_certifies_r_nonunital` | substitute C4 evidence for actual `R` / `C4_PROXY_CERTIFIES_R_NONUNITAL` |
| S011 | `TestSemanticMutations.test_s011_discrete_singleton_open_imported_to_r` | import a discrete singleton-open fact / `DISCRETE_SINGLETON_OPEN_IMPORTED_TO_R` |
| S012 | `TestSemanticMutations.test_s012_discrete_local_chart_imported_to_r` | import a discrete source chart / `DISCRETE_LOCAL_CHART_IMPORTED_TO_R` |
| S013 | `TestSemanticMutations.test_s013_usual_r_relabelled_discrete` | change only the actual topology token / `USUAL_R_RELABELLED_DISCRETE` |
| S014 | `TestSemanticMutations.test_s014_discrete_proxy_relabelled_usual_r` | change only the proxy topology token / `DISCRETE_PROXY_RELABELLED_USUAL_R` |
| S015 | `TestSemanticMutations.test_s015_r_nonetale_generalized_all_h` | change only the quantifier / `R_NONETALE_GENERALIZED_ALL_H` |
| S016 | `TestSemanticMutations.test_s016_r_nonunital_generalized_all_h` | change only the quantifier / `R_NONUNITAL_GENERALIZED_ALL_H` |
| S017 | `TestSemanticMutations.test_s017_localic_without_bare_qh_lc` | gate bits `000` with promotion / `LOCALIC_WITHOUT_BARE_QH_LC` |
| S018 | `TestSemanticMutations.test_s018_localic_with_only_lc` | gate bits `001` with promotion / `LOCALIC_WITH_ONLY_LC` |
| S019 | `TestSemanticMutations.test_s019_localic_with_only_qh` | gate bits `010` with promotion / `LOCALIC_WITH_ONLY_QH` |
| S020 | `TestSemanticMutations.test_s020_localic_without_bare_quantale` | gate bits `011` with promotion / `LOCALIC_WITHOUT_BARE_QUANTALE` |
| S021 | `TestSemanticMutations.test_s021_bare_quantale_alone_promoted` | gate bits `100` with promotion / `BARE_QUANTALE_ALONE_PROMOTED` |
| S022 | `TestSemanticMutations.test_s022_bare_quantale_lc_without_qh` | gate bits `101` with promotion / `BARE_QUANTALE_LC_WITHOUT_QH` |
| S023 | `TestSemanticMutations.test_s023_bare_quantale_qh_without_lc` | gate bits `110` with promotion / `BARE_QUANTALE_QH_WITHOUT_LC` |
| S024 | `TestSemanticMutations.test_s024_actual_packet_owner_relabelled_standard` | mutate actual owner only / `ACTUAL_PACKET_OWNER_RELABELLED_STANDARD` |
| S025 | `TestSemanticMutations.test_s025_standard_topology_imported_actual` | mutate actual topology only / `STANDARD_TOPOLOGY_IMPORTED_ACTUAL` |
| S026 | `TestSemanticMutations.test_s026_standard_topos_spliced_actual` | mutate actual topos only / `STANDARD_TOPOS_SPLICED_ACTUAL` |
| S027 | `TestSemanticMutations.test_s027_standard_quantale_spliced_actual` | mutate actual quantale only / `STANDARD_QUANTALE_SPLICED_ACTUAL` |
| S028 | `TestSemanticMutations.test_s028_standard_base_spliced_actual` | mutate actual base only / `STANDARD_BASE_SPLICED_ACTUAL` |
| S029 | `TestSemanticMutations.test_s029_standard_packet_owner_relabelled_actual` | mutate standard owner only / `STANDARD_PACKET_OWNER_RELABELLED_ACTUAL` |
| S030 | `TestSemanticMutations.test_s030_indiscrete_topology_imported_standard` | mutate standard topology only / `INDISCRETE_TOPOLOGY_IMPORTED_STANDARD` |
| S031 | `TestSemanticMutations.test_s031_actual_topos_spliced_standard` | mutate standard topos only / `ACTUAL_TOPOS_SPLICED_STANDARD` |
| S032 | `TestSemanticMutations.test_s032_actual_quantale_spliced_standard` | mutate standard quantale only / `ACTUAL_QUANTALE_SPLICED_STANDARD` |
| S033 | `TestSemanticMutations.test_s033_actual_base_spliced_standard` | mutate standard base only / `ACTUAL_BASE_SPLICED_STANDARD` |
| S034 | `TestSemanticMutations.test_s034_actual_standard_bases_identified` | replace base inequality by equality / `ACTUAL_STANDARD_BASES_IDENTIFIED` |
| S035 | `TestSemanticMutations.test_s035_strict_marker_nonunit_scale` | assert strict preservation for each nonunit fixture scale / `STRICT_MARKER_NONUNIT_SCALE` |
| S036 | `TestSemanticMutations.test_s036_plain_topos_numerical_scale_promotion` | add numerical-`L` recovery to plain topos / `PLAIN_TOPOS_NUMERICAL_SCALE_PROMOTION` |
| S037 | `TestSemanticMutations.test_s037_plain_quantale_numerical_scale_promotion` | add numerical-`L` recovery to plain quantale / `PLAIN_QUANTALE_NUMERICAL_SCALE_PROMOTION` |
| S038 | `TestSemanticMutations.test_s038_c_star_promotion` | add C-star conclusion / `C_STAR_PROMOTION` |
| S039 | `TestSemanticMutations.test_s039_haar_promotion` | add Haar conclusion / `HAAR_PROMOTION` |
| S040 | `TestSemanticMutations.test_s040_measure_promotion` | add measure conclusion / `MEASURE_PROMOTION` |
| S041 | `TestSemanticMutations.test_s041_trace_promotion` | add trace conclusion / `TRACE_PROMOTION` |
| S042 | `TestSemanticMutations.test_s042_determinant_promotion` | add determinant conclusion / `DETERMINANT_PROMOTION` |
| S043 | `TestSemanticMutations.test_s043_route_b_promotion` | add Route-B conclusion / `ROUTE_B_PROMOTION` |
| S044 | `TestSemanticMutations.test_s044_priority_promotion` | add priority conclusion / `PRIORITY_PROMOTION` |
| S045 | `TestSemanticMutations.test_s045_standard_topology_promotion` | import standard topology / `STANDARD_TOPOLOGY_PROMOTION` |
| S046 | `TestSemanticMutations.test_s046_numerical_log_evaluation` | replace literal stabilizer by numeric log / `NUMERICAL_LOG_EVALUATION` |
| S047 | `TestSemanticMutations.test_s047_fixed_prime_substitution_before_generic` | change only theorem ordering / `FIXED_PRIME_SUBSTITUTION_BEFORE_GENERIC` |
| S048 | `TestSemanticMutations.test_s048_nonliteral_stabilizer_rewrite` | rewrite `(log p)Z` / `NONLITERAL_STABILIZER_REWRITE` |

The mandatory wrong-handedness, wrong-domain, bare-quantale promotion,
actual/standard owner splice, strict nonunit-scale, and C-star/Haar/trace/
Route-B attacks therefore have distinct source-level methods and cannot be
hidden in a common loop.

### 8.3 Complete isolated package/fail-closed mutation registry — 42 methods

Each method copies the pristine package to its own temporary root, applies
one and only one delta, invokes the affected closed entry, requires a nonzero
result in the named gate class, and removes its root. P038 invokes
`--generate`; P035 and P036 invoke the top-level reproduction and fail before
its test step; every other method invokes `--verify-only`. No method may
depend on a failure caused by any previous mutation. Where one gate class
explicitly lists multiple equivalent representatives (P033 and P034), the method
restarts from a new pristine copy for each representative and applies only
that one delta before the call; representatives are not accumulated, and
they remain one gate class rather than being counted as extra methods.
For P020 and P025--P030, “change the first hex digit” means the exact map
`0 -> 1` and every other lowercase hex digit `-> 0`; all
manifest-object mutations except malformed-JSON P019 are reserialized by
the canonical Section-3.2 JSON contract before verification.
P035 launches its isolated child with `P17_REPRO_ACTIVE=1`. P036 removes
only that variable from its isolated child environment, pre-creates the
child copy's exact lock directory, and therefore reaches the concurrency
gate rather than the recursion gate.

| ID | Exact `unittest` method | One mutation and required rejection class |
|---|---|---|
| P001 | `TestPackageMutations.test_p001_csv_content_cell_tamper` | in `AO-0001`, replace `subject_value=X4x[EMPTY]` by `X4x[0]` / row-oracle failure |
| P002 | `TestPackageMutations.test_p002_csv_header_token_tamper` | in C17-1, rename header `row_id` to `row_identifier` / schema failure |
| P003 | `TestPackageMutations.test_p003_csv_header_reorder` | in C17-1, swap only `row_id,row_family` / schema failure |
| P004 | `TestPackageMutations.test_p004_csv_header_width` | in the summary, remove `notes` from the header and every row / width failure |
| P005 | `TestPackageMutations.test_p005_csv_row_reorder` | in C17-1, swap complete rows `GH-0001,GH-0002` / canonical-order failure |
| P006 | `TestPackageMutations.test_p006_duplicate_row_id` | change only `GH-0002`'s ID to `GH-0001` / identity failure |
| P007 | `TestPackageMutations.test_p007_csv_row_deleted` | delete complete row `AO-1520` / row-count failure |
| P008 | `TestPackageMutations.test_p008_csv_row_inserted` | append `AO-1520`'s non-ID fields with new ID `AO-1521` / inventory failure |
| P009 | `TestPackageMutations.test_p009_stale_file_row_count` | in `TS-0001`, change `expected_rows` from `1662` to `1661` / stale-count failure |
| P010 | `TestPackageMutations.test_p010_stale_file_column_count` | in `TS-0001`, change `expected_columns` from `17` to `16` / stale-count failure |
| P011 | `TestPackageMutations.test_p011_stale_file_negative_count` | in `TS-0001`, change `expected_negative_rows` from `36` to `35` / stale-count failure |
| P012 | `TestPackageMutations.test_p012_stale_package_row_total` | in `TS-0010`, change `3436` to `3435` only / aggregate failure |
| P013 | `TestPackageMutations.test_p013_stale_package_negative_total` | in `TS-0010`, change `84` to `83` only / aggregate failure |
| P014 | `TestPackageMutations.test_p014_missing_csv` | remove `range_first_handedness_controls.csv` / missing-file failure |
| P015 | `TestPackageMutations.test_p015_extra_csv` | add `unlisted.csv` with exact bytes `x\n` / extra-file failure |
| P016 | `TestPackageMutations.test_p016_extra_non_csv_file` | add `unlisted.txt` with exact bytes `x\n` / extra-file failure |
| P017 | `TestPackageMutations.test_p017_extra_directory` | add empty directory `unlisted/` / extra-entry failure |
| P018 | `TestPackageMutations.test_p018_missing_manifest` | remove manifest / missing-file failure |
| P019 | `TestPackageMutations.test_p019_manifest_malformed_json` | replace the manifest's first `{` byte by `[` / manifest-parse failure |
| P020 | `TestPackageMutations.test_p020_manifest_artifact_sha_tamper` | change the first hex digit of artifact element 1's `sha256` / manifest-hash failure |
| P021 | `TestPackageMutations.test_p021_manifest_artifact_bytes_tamper` | add one to artifact element 1's `bytes` integer / manifest-byte failure |
| P022 | `TestPackageMutations.test_p022_manifest_artifact_order` | swap artifact elements 1 and 2 / manifest-order failure |
| P023 | `TestPackageMutations.test_p023_manifest_self_hash_binding` | add top-level `manifest_sha256` with 64 zeroes / self-binding failure |
| P024 | `TestPackageMutations.test_p024_manifest_proof_binding_injection` | append the exact P17 proof-ledger path and digest from Section 1 to `bindings` / prohibited-proof-binding failure |
| P025 | `TestPackageMutations.test_p025_control_design_gate_binding_drift` | change the first hex digit of binding 1's digest / binding failure |
| P026 | `TestPackageMutations.test_p026_paper9_source_binding_drift` | change the first hex digit of binding 2's digest / provenance failure |
| P027 | `TestPackageMutations.test_p027_design_lock_digest_drift` | change the first hex digit of binding 3's digest / binding failure |
| P028 | `TestPackageMutations.test_p028_design_review_digest_drift` | change the first hex digit of binding 4's digest / binding failure |
| P029 | `TestPackageMutations.test_p029_implementation_gate_digest_drift` | change the first hex digit of binding 5's digest / binding failure |
| P030 | `TestPackageMutations.test_p030_implementation_file_digest_drift` | change the first hex digit of implementation element 1's digest / implementation-binding failure |
| P031 | `TestPackageMutations.test_p031_unhashed_implementation_path` | create `code/unlisted.py` with exact bytes `x\n`, hence no bytes/SHA entry / unhashed-path failure |
| P032 | `TestPackageMutations.test_p032_preexisting_dunder_pycache` | add empty `code/__pycache__/` before run / cache failure |
| P033 | `TestPackageMutations.test_p033_preexisting_compiled_bytecode` | separately add zero-byte `code/x.pyc` and `code/x.pyo` representatives / cache failure |
| P034 | `TestPackageMutations.test_p034_preexisting_tool_cache` | separately add empty `code/.pytest_cache/`, `.mypy_cache/`, and `.ruff_cache/` representatives / cache failure |
| P035 | `TestPackageMutations.test_p035_recursive_entry_environment` | preset `P17_REPRO_ACTIVE=1`, then enter reproduction / recursive-entry failure |
| P036 | `TestPackageMutations.test_p036_concurrent_lock_present` | pre-create the top-level lock directory, then enter reproduction / concurrent-entry failure |
| P037 | `TestPackageMutations.test_p037_verify_only_crlf_no_rewrite` | replace every LF in `target_summary.csv` by CRLF; require nonzero schema exit and an exactly unchanged byte/metadata receipt / read-only failure |
| P038 | `TestPackageMutations.test_p038_generate_into_nonempty_output` | pre-create output-root file `sentinel` with bytes `x\n` / new-empty-root failure |
| P039 | `TestPackageMutations.test_p039_symlink_result_entry` | replace `target_summary.csv` by a symlink to `range_first_handedness_controls.csv` / regular-file failure |
| P040 | `TestPackageMutations.test_p040_hardlink_result_entry` | replace `target_summary.csv` by a hard link to an outside seed copy of its pristine bytes / single-link failure |
| P041 | `TestPackageMutations.test_p041_manifest_unittest_aggregate_tamper` | change manifest `unittest_methods` from `180` to `179` / manifest-aggregate failure |
| P042 | `TestPackageMutations.test_p042_manifest_copy_count_tamper` | change manifest `byte_identical_copies` from `3` to `2` / manifest-aggregate failure |

P023, P024, and P031 are distinct: the manifest may bind neither itself, a
P17 proof/proof-review artifact, nor an implementation path lacking both
byte count and SHA-256. P014--P018 separately exercise missing, extra-file,
and extra-directory gates. P032--P034 exercise cache closure; the exact
top-level post-scan and cleanup are checked by the dedicated reproduction
method and by the outer entry itself. P035 and P036 distinguish recursion
from a concurrent independent top-level invocation. P041 and P042 prevent
stale manifest test/reproduction totals from being accepted.

## 9. Future paths and acyclic manifest contract

### 9.1 Fixed future implementation paths

Only a later, separate implementation gate may authorize creation of these
five implementation files:

```text
code/generate_controls.py
code/test_controls.py
code/README.md
experiments/reproduce.sh
experiments/README.md
```

and the ten generated artifacts in Section 2. In a future package, `code/`
must contain exactly its three listed regular single-link files and
`experiments/` exactly its two listed regular single-link files, except for
the owned lock during an active reproduction. An extra implementation entry
is an inventory failure even if no manifest element mentions it. No path
exists by implication; this design creates or authorizes none of them.

### 9.2 Binding lifecycle

The future manifest's exact ordered `bindings` array is:

```text
1 notes/phase2_control_design_gate.md
  sha256:093ca31fa840b992a105cbfd4911353e3df49ba7e05ae8e43d541059999b6647
2 ../9-packet-separation/paper/manuscript.tex
  sha256:24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb
3 notes/phase2_control_design_lock.md
  sha256:<externally computed final digest of this file>
4 notes/phase2_control_design_review.md
  sha256:<externally computed final digest after independent review>
5 notes/phase2_control_implementation_gate.md
  sha256:<externally computed final digest after that separate gate>
```

All manifest paths are stored relative to
`papers/17-open-groupoid-interfaces/`; the `../9-...` path above therefore
resolves to the exact Paper-9 file. The three angle-bracket descriptions are
design notation only and are forbidden in a produced manifest: generation is
unauthorized until all three real 64-lowercase-hex digests exist.

This lifecycle is acyclic:

```text
closed symbolic proof and peer review
  -> post-proof control-design gate
  -> this design lock
  -> independent design review
  -> separate implementation gate
  -> implementation files
  -> CSV artifacts
  -> manifest
```

The manifest binds the control-design gate rather than repeating the P17
proof tuple. It must contain no path, basename, or digest for
`phase2_topos_quantale_proofs.md`,
`phase2_topos_quantale_peer_review.md`, or any other P17 proof artifact.
The only keys whose spelling may contain `proof` are the two exact Boolean
policy keys in Section 9.3, both fixed to `false`; no other top-level or
nested key may contain that substring.
The gate supplies indirect upstream authority. This rule prevents a proof/
control hash cycle and keeps proof validation outside the finite control
package.

### 9.3 Exact manifest semantics

The canonical object contains exactly these top-level keys:

```text
schema_version
package_id
bindings
acyclic_policy
implementation
artifacts
aggregates
reproduction
status
```

Their semantics are fixed:

```text
schema_version = paper17-open-groupoid-controls-manifest/1
package_id = paper17-open-groupoid-controls

bindings = the exact five-element array in Section 9.2; every element has
           exactly path, bytes, sha256

acyclic_policy = {
  manifest_self_hash_included: false,
  manifest_self_entry_included: false,
  p17_proof_hash_included: false,
  p17_proof_review_hash_included: false,
  authority_policy: CONTROL_DESIGN_GATE_INDIRECT_PROOF_AUTHORITY
}

implementation = the exact five paths in Section 9.1, in that order; every
                 element has exactly path, bytes, sha256

artifacts = the nine CSVs in Section-2 order; every element has exactly
            path, schema, columns, rows, negative_rows, bytes, sha256

aggregates = {
  csv_artifacts: 9,
  generated_artifacts_including_manifest: 10,
  csv_body_rows: 3436,
  nonnegative_csv_rows: 3352,
  explicit_negative_rows: 84,
  expected_negatives_detected: 84,
  semantic_mutation_classes: 48,
  package_mutation_classes: 42,
  isolated_mutation_methods: 90,
  unittest_methods: 180
}

reproduction = {
  deterministic: true,
  random_used: false,
  network_used: false,
  ambient_clock_used: false,
  fresh_generations: 2,
  byte_identical_copies: 3,
  verify_only_rewrites: false
}

status = PASS
```

The manifest is not an element of `bindings`, `implementation`, or
`artifacts`; it has no self-digest or byte count. No implementation element
may omit `bytes` or `sha256`, and no additional implementation path is
allowed. Artifact paths are logical `results/<name>` paths even in fresh
temporary roots, so absolute temporary paths never affect bytes.

The manifest's `status=PASS` is accepted only after re-hashing every binding,
implementation file, and CSV and recomputing every aggregate. It is not a
root of trust.

## 10. Exact generator, verify-only, and reproduction contract

### 10.1 Closed command interface

The only future generator entry forms are:

```text
python3 -B code/generate_controls.py --generate --output-dir <existing-empty-directory>
python3 -B code/generate_controls.py --verify-only --output-dir <existing-package-directory>
```

Exactly one mode is required. No other positional argument or flag is
accepted. `--generate` refuses a missing, non-directory, symlinked, or
nonempty output path. For these commands the supplied output directory is
the physical counterpart of the logical `results/` directory: it contains
the ten Section-2 basenames directly, while the manifest records each as
`results/<basename>`. `--generate` writes only those ten basenames,
with the manifest written last after all CSV hashes are known. It never
reads a checked-in result as a template and performs no automatic retry.

`--verify-only` opens every package entry read-only and is forbidden to call
or reach any write, append, create, truncate, rename, replace, unlink,
directory-creation, chmod, or timestamp-changing operation. It cannot
repair, normalize, regenerate, reorder, or rewrite an artifact even when the
only defect is a line ending. A defect returns nonzero and leaves every byte
and metadata field unchanged.

Its fail-closed validation priority is exact: (1) arguments, recursion, root,
generated-result inventory, entry type, link, and cache checks; (2) raw CSV UTF-8/LF parsing,
header, width, ID, family order, primitive grammar, independent semantics,
negative registry, and raw summary recomputation; (3) manifest JSON parse,
exact key/array shape, self-binding prohibition, proof-binding prohibition,
and the special prohibition on any unlisted/unhashed implementation file;
(4) the five authority and five implementation byte/hash bindings; (5) the
nine artifact byte/hash bindings and all manifest aggregates. The first
failed phase supplies the Section-10.4 class. Thus a one-byte CSV mutation is
classified by its raw schema/semantic defect before its consequential stale
manifest digest, while a manifest-only digest mutation reaches phase 5.

The future test entry is exactly:

```text
python3 -B code/test_controls.py --checked-in results --fresh-a <A> --fresh-b <B>
```

It rejects any other arguments, checks the AST and runtime method count at
180, and runs each explicit method once. Test subprocesses inherit `-B`.

### 10.2 Exact top-level reproduction sequence

The sole future top-level entry point is

```text
papers/17-open-groupoid-interfaces/experiments/reproduce.sh
```

It accepts no arguments and performs these steps in order:

1. If `P17_REPRO_ACTIVE` is nonempty, exit as recursive before any write.
2. Export exactly `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `PYTHONHASHSEED=0`, and
   `PYTHONDONTWRITEBYTECODE=1`; set `P17_REPRO_ACTIVE=1`; use `umask 022`.
3. Resolve the physical Paper-17 root from the script's own fixed path,
   reject a symlinked script or Paper-17 root, and change to that root. The
   caller's working directory is never consulted again or serialized.
4. Reject every pre-existing cache/residue class listed below. Atomically
   create the directory `experiments/.p17-control-reproduce.lock` with one
   `mkdir` operation; if any entry already has that path, reject a concurrent
   run. Install an exit trap that removes only this exact lock directory and
   the two exact temporary roots created later.
5. Capture an in-memory checked-in results receipt consisting of ordered
   `(relative_path,type,bytes,sha256,mode,mtime_ns,nlink)` tuples for the ten
   generated artifacts after rejecting symlinks and multi-link result files.
   Run verify-only on `results/`. Capture the same receipt again and require
   exact equality. No absolute repository path enters generated bytes.
6. Create two distinct empty roots using
   `mktemp -d "${TMPDIR:-/tmp}/p17-controls.XXXXXX"`, call them A then B,
   and run generate then verify-only on A and then on B.
7. Compare all ten artifacts byte-for-byte in Section-2 order across
   checked-in/A, checked-in/B, and A/B. The manifest participates exactly
   like each CSV.
8. Run the exact test entry once with the three package roots; require 180
   discovered methods, zero failures, zero errors, and 84/84 detected
   explicit negatives.
9. Repeat the exact inventory/cache scan. Invoke the same cleanup routine
   used by the exit trap to remove A, B, and the lock, verify that all three
   are absent, then disarm the trap. Verify that the Paper-17 subtree contains
   no cache or task residue. The trap remains the failure-path fallback and
   may remove only those three already recorded exact paths. Exit zero only
   after the explicit cleanup and both absence checks succeed.

The closed cache/residue classes are:

```text
directory basename: __pycache__,.pytest_cache,.mypy_cache,.ruff_cache
file suffix:        .pyc,.pyo
task residue:       .p17-control-* except the one active lock while owned
```

The results directory itself must contain exactly the ten regular files in
Section-2 order as an inventory set, no symlink, hardlink (`nlink` must be
1), device, FIFO, socket, subdirectory, cache, or unlisted file. The code and
experiments directories must have the exact Section-9.1 inventories and are
also recursively checked, without following symlinks, for the closed
cache/residue classes. The pre-run and post-run scans cover the entire
Paper-17 subtree; only the currently owned lock is exempt while active. No
network, API, model, ambient clock, random source, locale sort, or external
source retrieval participates in artifact values or bytes. OS-selected
`mktemp` path entropy and observed receipt metadata are orchestration-only,
never feed a semantic computation, and are never serialized. Accordingly,
manifest `random_used=false` and `ambient_clock_used=false` refer exactly to
artifact generation and verification logic, not temporary-name allocation
or the read-only metadata comparison.

### 10.3 Three-way identity and verify-only meaning

`FRESH_GENERATIONS=2` means two independent generator processes into A and
B, not two copies or one generation followed by duplication.
`BYTE_IDENTICAL_COPIES=3` means checked-in, A, and B. Identity covers all
nine CSVs and the manifest, not merely their parsed semantics or hashes.

A passing verify-only receipt says only that the supplied finite package
matches this design and its current bindings. It is not proof of connected
`R`, a topos equivalence, local compactness, `q_H`, a localic/source theorem,
or any prohibited promoted structure.

### 10.4 Closed exit codes

```text
0  success
2  usage or unsupported flag
3  recursive or concurrent entry
4  output-root precondition failure
5  inventory, entry-type, cache, or residue failure
6  authority/provenance/implementation binding failure
7  CSV schema, order, row, count, semantic-oracle, or negative failure
8  manifest schema, hash, byte, order, self/proof/unhashed-path failure
9  three-way byte-identity failure
10 unittest source/runtime count, failure, or error
11 verify-only mutation or cleanup failure
```

Any unclassified exception maps to the narrowest applicable nonzero code;
it must never be converted to success. Console wording is noncanonical and
does not enter any generated byte.

## 11. Static design self-audit and independent-review gate

### 11.1 Recomputed family arithmetic

This design self-audit is static arithmetic only; no generator, verifier,
test, reproduction script, or control implementation was run.

```text
C17-1:
  36 + 6 + 36 + 1296 + 36 + 216 + 18 + 18 = 1662
  negatives = 18 + 18 = 36

C17-2:
  48 + 48 + 768 + 48 + 32 + 32 + 512 + 32 = 1520
  negatives = 0

C17-3:
  3 + 9 + 3 + 4 = 19
  negatives = 4

C17-4:
  3 + 12 + 10 = 25
  negatives = 10

C17-5:
  3 + 8 + 7 + 3 = 21
  negatives = 7

C17-6:
  2 + 5 + 11 = 18
  negatives = 11

C17-7:
  2 + 4 + 16 + 16 + 16 + 16 + 64 + 4 + 2 = 140
  negatives = 3 + 2 = 5

C17-8:
  1 + 3 + 6 + 11 = 21
  negatives = 11

summary:
  9 artifact/self rows + 1 package row = 10
  negatives = 0

body rows:
  1662 + 1520 + 19 + 25 + 21 + 18 + 140 + 21 + 10 = 3436

negative rows:
  36 + 0 + 4 + 10 + 7 + 11 + 5 + 11 + 0 = 84

nonnegative rows:
  3436 - 84 = 3352

test methods:
  58 + 8 + 10 + 8 + 6 + 48 + 42 = 180

isolated mutation methods:
  48 + 42 = 90
```

The header widths were independently recounted from their comma-delimited
tokens as

```text
17,16,16,15,18,17,19,17,12
```

in Section-2 CSV order.

### 11.2 C17 gate coverage

| Gate | Frozen design surface | Self-audit finding |
|---|---|---|
| C17-1 | nonabelian finite groupoid source/range/unit/inverse/all pairs/product; left sheets; semantic wrong-order/opposite negatives | none |
| C17-2 | one carrier; pairwise-distinct trivial/transitive/nontransitive actions; every `C4` subset product/involution/base; cross-action open-record equality | none |
| C17-3 | bound connected-real receipt plus nontrivial regular `Z/3Z` quotient and four promotion firewalls | none |
| C17-4 | nondiscrete-real/discrete-proxy owner matrix and ten wrong-domain attacks | none |
| C17-5 | separate bare, `q_H`, local-compactness receipts; full truth table; seven promotion attacks | none |
| C17-6 | exact actual/standard packets, separate owner/topology columns, eleven one-field splices | none |
| C17-7 | exact rational dilation/source/range/inverse/product; four strict scales; plain-output firewall | none |
| C17-8 | post-generic Paper-9 two-input allowlist; eleven C-star/Haar/measure/trace/determinant/Route-B/priority and provenance attacks | none |
| finite/proof firewall | explicit epistemic red line, receipt-only status, no direct P17 proof binding in manifest | none |
| oracle independence | disjoint representations; emitted receipt fields blanked; six dedicated independence methods | none |
| serialization | one schema, nine exact headers, row-family/ID order, canonical scalar and byte rules | none |
| reproduction | two fresh processes, three complete byte copies, checked-in read-only receipt | none |
| manifest | five acyclic bindings, all implementation/artifacts hashed, no self/proof/unhashed path | none |
| fail-closed | 48 semantic and 42 package mutation classes, each with one explicit method | none |

### 11.3 Mandatory independent exact-byte review

The future design reviewer must start from the final SHA-256 of this file and
must independently recompute, rather than copy:

1. every comma-counted header width;
2. every row-family count and ID endpoint;
3. each per-file and package body-row total;
4. every reason multiplicity and the 84-row negative total;
5. the 58 conformance, 32 other nonmutation, 48 semantic-mutation, and 42
   package-mutation methods, totaling 180;
6. the two-fresh/three-copy identity arithmetic; and
7. the exact artifact, binding, implementation, and manifest inventories.

It must also execute these design attacks on the specification itself:

- Can an invalid fixture pass merely by supplying `PASS`, `detected=true`,
  the expected reason, a copied `oracle_value`, or a matching summary?
- Does any purported independent oracle import, call, or restate the same
  implementation helper rather than use the frozen alternative
  representation?
- Does a finite/discrete proxy certify connectedness of `R`, a topos
  equivalence, real-time non-etaleness/nonunitality, local compactness,
  `q_H`, or localic reconstruction?
- Can bare `O(H)` alone reach the localic result?
- Can an actual/standard field or topology be spliced without rejection?
- Does one mutation method stand in for two registered mutation classes?
- Can a manifest bind itself, a P17 proof/proof review, or an unhashed
  implementation path?
- Can verify-only rewrite, normalize, repair, rename, delete, or regenerate a
  checked-in result?
- Can missing, extra, reordered, stale-count, symlink, hardlink, recursive,
  concurrent, cache, residue, or tampered inputs reach exit zero?

Acceptance of any such surface is a blocking design finding. The reviewer
must not create or run implementation code to compensate for an ambiguous
design; ambiguity requires a versioned design amendment. At the time this
lock is frozen:

```text
INDEPENDENT_CONTROL_DESIGN_REVIEW_REQUIRED=true
CONTROL_DESIGN_REVIEW_PERFORMED=false
CONTROL_DESIGN_REVIEW_PASS=false
```

## 12. Final authorization matrix

```text
P17_CONTROL_DESIGN_LOCK=FROZEN_CANDIDATE
DESIGN_SCHEMA=paper17-open-groupoid-controls/1
MANIFEST_SCHEMA=paper17-open-groupoid-controls-manifest/1
CSV_ARTIFACTS=9
GENERATED_ARTIFACTS=10
CSV_BODY_ROWS=3436
EXPLICIT_NEGATIVES=84
TEST_METHODS=180
SEMANTIC_MUTATION_CLASSES=48
PACKAGE_MUTATION_CLASSES=42
ISOLATED_MUTATION_METHODS=90
FRESH_GENERATIONS=2
BYTE_IDENTICAL_COPIES=3
MANIFEST_SELF_HASH_INCLUDED=false
P17_PROOF_HASH_INCLUDED=false
P17_PROOF_REVIEW_HASH_INCLUDED=false
INDEPENDENT_CONTROL_DESIGN_REVIEW_REQUIRED=true
CONTROL_DESIGN_REVIEW_PERFORMED=false
CONTROL_DESIGN_REVIEW_PASS=false
CONTROL_IMPLEMENTATION_AUTHORIZED=false
CONTROL_EXECUTION_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
FIGURE_WORK_AUTHORIZED=false
RELEASE_AUTHORIZED=false
ARCHIVE_AUTHORIZED=false
GIT_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
STANDALONE_PASS=false
TECHNICAL_NOTE_CANDIDATE=true
CRITICAL_OPEN=0
MAJOR_OPEN=0
MINOR_OPEN=0
```

This file freezes design bytes only. Implementation remains blocked until a
separate reviewer returns `C0/M0/m0` on this exact digest and a later owner
issues a separate implementation gate. Even a future deterministic PASS
would remain a finite diagnostic package and would not replace the symbolic
proof, source theorem, Route, manuscript, publication, or release gates.
