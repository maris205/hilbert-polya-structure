# Paper 13 Phase-3 v2 independent devil/domain review

Review date: **2026-08-15 (Asia/Shanghai)**  
Reviewer lane: **independent devil's-advocate, domain, methodology, and owner-integrity review**  
Reviewed candidate: `notes/phase3_standalone_amendment_v2.md`  
Reviewed SHA-256: **`99c796bffe24f262d8ac8458b21fd253451bca51bac4b283660dab319992ed82`**  
Reviewed size: **428 lines / 17,701 bytes**  
Verdict: **MAJOR REVISION REQUIRED — C0 / M1 / m1**

## 1. Scope, independence, and write boundary

I read the complete ARS academic-paper-reviewer router and the devil's-
advocate and domain-reviewer role instructions before beginning this lane. I
then independently rehashed and reconstructed the exact Paper-9, Paper-11,
Paper-12, and Paper-13 locks needed for the proposed strengthening. I did not
read partial v2 draft bytes. Review began only after the candidate was declared
stable at the hash above.

This lane reviewed theorem design, mathematical feasibility, owner typing,
source hypotheses, proof firewalls, and downstream gate discipline. It did not
write a proof, control design, code, results, Route YAML, manuscript, or release
artifact; it did not execute controls or retain, alter, or publish a source PDF.
This report is the only file written by the lane.

The exact companion locks rechecked for the load-bearing claims were:

| Artifact | SHA-256 | Review use |
|---|---|---|
| Paper 2 manuscript | `72c34a0a30279ed7c070917a2c9242b8e9cb0a37a56779c246fa2cae04097fdc` | internal prior: Proposition `prop:uncountable`, exact sign/procyclic continuum lower bound and packet-orbit transfer |
| Paper 2 proof audit | `aaab83c32eb9d6c172be192dbb14acc6ed927a972d61c24a90dbfe94ecd0dbae` | independently accepted internal proof and exact topology ceiling |
| Paper 9 manuscript | `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb` | `Q_p`, `U_p/H_p`, actual indiscrete topology, procyclic `H_p` |
| Paper 9 proof audit | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | exact normalized set model and order-two argument |
| Paper 11 manuscript | `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002` | actual global-QC support, time algebra, regular sign |
| Paper 11 proof audit | `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28` | owner-safe completion boundary |
| Paper 12 manuscript | `c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163` | section-free standardization, `J`, actual/discrete quotient split |
| Paper 12 proof audit | `c2b0fc4ce4764b476de8623c7a1b37e33d51da4a1c318c133313956abf4af6ab` | four-way owner typing and origin-choice ledger |
| Paper 13 core proof | `62dac0782ba74fea9e8318e0835f7f20eede4cc9963c67471797a006b00decbd` | frozen twist, gauge, regular, and time norm interface |
| Paper 13 support proof | `f8a0672026b2efaaf07af20d90a17e870e8d0e2f849af0eb78d6dcb1573fb811` | frozen generic finite/infinite support theorem |
| Binding standalone review | `0397e1555a1ff07d30f06c3182b6cf570228ccd3e8db9e3c96666d118079c224` | existing `NOTE_OR_MERGE`, C0/M1/m0 |

## 2. Decision

The v2 operator-algebraic strengthening is mathematically coherent after the
repairs below. I found no critical defect, but I found one Major provenance and
standalone-delta defect: sealed Paper 2 already proves the entire sign-subgroup/
procyclic continuum lower-bound argument and transfers it to the fixed-prime
packet orbit set. P13-8A is therefore not a new Paper-13 theorem package. At
most, Paper 13 adds the elementary continuum upper bound and reconciles that
inherited result with the later Paper-9/Paper-12 owner names.

The actual-versus-standard topology split, the component `c0` completion, the
bounded multiplier product, the constant-norm diagonal, the algebra/corona
intersection, gauge covariance, and the fixed-prime completion consequence all
retain viable proof routes. P13-8B/C may remain candidate new content, but they
must carry the standalone burden without receiving novelty credit from P13-8A.

One additional displayed definition is not literally well typed: the product indexed only
by odd primes is declared to be a subset of a product indexed by all primes
different from `p`, without specifying the omitted coordinate. This is a
one-line repair and does not change P13-8A, but the project's exact-owner
discipline makes the repair mandatory before a zero-finding re-lock.

```text
critical: 0
major: 1
minor: 1
v2_design_verdict: MAJOR_REVISION_REQUIRED
P13_8A_MATHEMATICALLY_FEASIBLE: true
P13_8B_MATHEMATICALLY_FEASIBLE: true
P13_8C_MATHEMATICALLY_FEASIBLE: true
SOURCE_GATE_STILL_REQUIRED: true
V2_CONTROL_DESIGN_STILL_REQUIRED: true
STANDALONE_PASS: false
NOTE_OR_MERGE_BINDING: true
ROUTE_AUTHORIZED: false
MANUSCRIPT_AUTHORIZED: false
RELEASE_AUTHORIZED: false
route_b_invocation_allowed: false
```

## 3. Open findings

### M1 — P13-8A duplicates a sealed Paper-2 theorem and is assigned false new-credit weight

**Severity**: Major  
**Dimension**: internal precedent / provenance / standalone contribution  
**Evidence Anchor**: `text: phase3_standalone_amendment_v2.md:80-108 "P13-8A — exact fixed-prime cardinality theorem"`  
**Counter-evidence Anchor**: `equation: papers/2-flow-zeta/paper/manuscript.tex:391-435, Proposition prop:uncountable`  
**Confidence**: 5 — the sealed Paper-2 proof and v2 Steps 1--4 agree line for line.

The v2 authority table and source/novelty gates omit Paper 2. That omission is
load-bearing. On locked manuscript bytes, Paper 2 already defines

```text
G_p=product_(ell!=p) Z_ell^x,
H_p=p^Zhat,
S_p={full-coordinate sign families, with omitted coordinates fixed to 1},
```

proves `|S_p|=2^aleph_0`, proves that procyclic `H_p` has at most one
nonidentity involution, obtains `|S_p intersect H_p|<=2`, and concludes that
the image of `S_p` in `G_p/H_p` has cardinality `2^aleph_0`. It then transfers
that lower bound through the source-audited set parametrization to the
fixed-prime packet orbit set. These are exactly v2 P13-8A Steps 1--4. Paper 2
also records the same no-topology-promotion ceiling.

V2's only additional cardinal step is

```text
|U_p| <= (2^aleph_0)^aleph_0 = 2^aleph_0,
```

which upgrades the already inherited lower bound to equality. That elementary
upper bound, plus reconciliation of Paper 2's `B_p` notation with Paper 9's
intrinsic `Q_p^actual` and Paper 12's `Q_p^bare/Q_p^disc` split, is useful owner
hygiene. It is not a new central cardinality theorem and cannot contribute
standalone weight.

This is Major because the amendment presents P13-8A as conjectured Paper-13
content and asks a later reviewer to assess a "combined unconditional
fixed-prime cardinality and corona-survival theorem." The missing internal
prior changes the exact author-owned delta and therefore the publication
disposition, even though the proposed equality is true.

**Exact repair.** The amended design must:

1. add the sealed Paper-2 manuscript and proof-audit hashes to the authority,
   premise, internal-precedent, and bounded-novelty ledgers;
2. relabel P13-8A as an **inherited Paper-2 continuum lower bound**, followed
   only by an elementary at-most-continuum equality closure and exact
   Paper-9/Paper-12 owner retyping;
3. give P13-8A no novelty or standalone credit and remove wording that makes
   the cardinality theorem part of the new dependency break;
4. revise the later standalone gate so that **P13-8B and P13-8C alone** must
   be judged sufficiently nonformal and central; and
5. keep `NOTE_OR_MERGE` binding unless a fresh post-proof reviewer finds that
   the completion/corona result itself, without counting cardinality as new,
   closes the prior M1.

P13-8B/C are not automatically disqualified by the internal prior. They do
strictly extend the test-support statement to a multiplier/corona theorem.
But they also reduce to a faithful component embedding plus the standard
constant-norm diagonal of a `c0` sum. Whether that is enough for standalone
treatment remains a substantive later judgment; this design review cannot
predeclare that it closes M1.

### m1 — the odd-prime sign product lacks its embedding into the full product

**Severity**: Minor  
**Dimension**: exact set typing / cardinality owner  
**Evidence Anchor**: `text: phase3_standalone_amendment_v2.md:82-87 "S_p=product_(ell in I_p) {+1,-1} subset U_p."`  
**Confidence**: 5 — direct comparison of the two product index sets.

The candidate defines `I_p` to contain the odd primes different from `p`.
When `p` is odd, `U_p` also has a `Z_2^x` coordinate. An element of

```text
product_(ell in I_p) {+1,-1}
```

is formally a function on `I_p`, whereas an element of

```text
U_p=product_(ell!=p) Z_ell^x
```

is a function on the larger index set of all primes different from `p`.
Therefore the first product is not literally a subset of the second until an
embedding is declared. The intended embedding is evident and injective, so the
gap does not weaken the cardinal estimate; it only leaves the displayed owner
map under-specified.

**Exact repair.** Replace the displayed definition by either of the following
fully typed forms. The minimal change preserving `I_p` is:

```text
S_p := {epsilon=(epsilon_ell)_(ell!=p) in U_p :
          epsilon_ell in {+1,-1} for ell in I_p,
          epsilon_ell=+1 for ell notin I_p and ell!=p}.
```

Equivalently, because both signs are units also in `Z_2`, redefine `I_p` to be
all rational primes different from `p` and keep the product display. After
either repair, state that the inclusion `S_p -> U_p` is this coordinatewise
embedding. No later formula or cardinal bound needs to change.

## 4. Cardinality and owner stress test

Subject to m1's explicit inclusion, the cardinality equality is true. Its
provenance is not new: items 1--4 below are inherited from sealed Paper 2,
while item 5 is the elementary upper-bound closure supplied by the v2 design.

1. The coordinate set `I_p` is countably infinite, so the sign product has
   cardinality `2^aleph_0`.
2. The locked Paper-9 owner proves that `H_p=p^Zhat` is procyclic. A procyclic
   profinite group has at most one nonidentity element of order two.
3. The repaired `S_p` has exponent two, hence `|S_p intersect H_p|<=2`.
4. For `s_1,s_2 in S_p`, equality of their images in `U_p/H_p` is equivalent
   to `s_2^(-1)s_1 in S_p intersect H_p`. Thus every restricted quotient fibre
   has at most two points, and the image has cardinality `2^aleph_0`.
5. Each `Z_ell^x` has cardinality at most the continuum and the prime index is
   countable, so `|U_p|<= (2^aleph_0)^aleph_0=2^aleph_0`.
6. The inherited lower bound and elementary upper bound give
   `|U_p/H_p|=2^aleph_0` without CH.

The post-Paper-2 owner typing is otherwise exact. Paper 9 supplies a set bijection between
the intrinsic orbit quotient and `U_p/H_p`; it does not supply a product
homeomorphism. Cardinality therefore belongs to `Q_p^bare`. The actual quotient
`Q_p^actual` retains its indiscrete topology and is second countable even at
continuum cardinality. The amendment correctly places non-second-countability
and non-`sigma`-compactness only on:

- the discrete standard orbit quotient `Q_p^disc`;
- the coproduct unit space `Std(Gamma_p)`; and
- the standard arrow space `Std(Gamma_p) x R`.

For the latter two spaces, the uncountably many nonempty open components rule
out a countable base. A compact subset meets only finitely many components;
therefore a countable union of compact subsets meets at most countably many
components and cannot cover the continuum-indexed coproduct. These conclusions
do not imply that a global groupoid C-star construction is unavailable.

## 5. Component completion and norm stress test

The componentwise design is correctly a `c0` direct sum rather than a bounded
product. Every standard orbit is an intrinsic open compact Hausdorff torsor,
and its transformation groupoid is a locally compact Hausdorff component with
Lebesgue range-fibre measure. No global choice of orbit origins is required to
define either the component or the time-only function `d_(q,sigma)(f)`.

The proposed full/reduced isometry is feasible, but its later proof must make
the following load-bearing steps explicit; algebraic injectivity alone is not
enough. These are proof/source receipts already covered in substance by
Sections 5 and 9 of the amendment, so I do not register a second finding at the
design stage:

1. Define the reduced norm as the supremum of the regular norms over every
   unit in `O_q`. For every unit `x`, exhibit the source-fibre unitary under
   which the restriction of the component regular representation to
   `d_(q,sigma)(f)` is exactly `Lambda_sigma(f)`. This proves the reduced
   equality, not merely one inequality at a preferred origin.
2. For the maximal inequality, compute the exact groupoid `I`-norm

   ```text
   ||d_(q,sigma)(f)||_I=||f||_1.
   ```

   Then show that every representation counted by the component universal
   norm restricts to an `L^1(R,sigma)`-continuous star representation. This
   gives `||d(f)||_max <= ||f||_C*(R,sigma)`.
3. Use the component regular representation for the reverse inequality and
   use amenability only on the standard time group `R` to identify its full
   and reduced norms. Do not infer full/reduced equality of the entire
   component groupoid unless a separately matched theorem supplies it.
4. Source-clear the exact continuous-cocycle convention for the component
   full and reduced records, or define them by a proved choice-independent
   gauge transport from the audited untwisted compact-orbit records.

The amendment correctly does not use non-second-countability as an obstruction
to all global C-star constructions. Its BHM statement matches the locked
primary source: the untwisted locally compact Hausdorff Haar-groupoid framework
does not require second countability. The conservative component definition is
therefore an owner/source choice pending a global twisted convention audit, not
an impossibility theorem.

## 6. `c0`, multiplier, intersection, and corona stress test

The operator-algebraic dichotomy is internally correct once the component
isometries are proved.

- For an arbitrary index set,

  ```text
  M(direct_sum_q^c0 B_q) ~= product_q^bounded M(B_q).
  ```

  The bounded product of the `B_q` themselves embeds coordinatewise in this
  multiplier product; it is not silently identified with the full multiplier
  algebra when the components are nonunital.
- Every coordinate of `D_sigma^epsilon(a)` lies in `B_q` and has norm
  `||a||`. Hence the family is bounded and defines a multiplier.
- A bounded family belongs to the `c0` sum precisely when, for each positive
  threshold, only finitely many coordinates exceed it. A nonzero constant-norm
  family therefore lies in the `c0` sum exactly when `Q` is finite.
- The kernel of the corona composite is exactly

  ```text
  {a:D_sigma^epsilon(a) in A_(std,sigma)^epsilon}.
  ```

  It is zero for infinite `Q`; an injective C-star homomorphism is automatically
  isometric. For finite `Q`, the diagonal lies in the algebra and its corona
  image is zero.

Thus the completion statement is strictly stronger than the test-support
membership statement: it identifies where the completed time algebra goes
after it leaves the standard `c0` algebra.

## 7. Gauge, trivializer, and origin-choice stress test

The amendment has the correct frozen gauge orientation

```text
sigma overline(tau)=delta alpha,
U_alpha:A_sigma->A_tau.
```

Multiplication by `alpha(t)` on every standard component intertwines the two
time-only embeddings. Once the component maps extend isometrically, their
`c0` sum is a C-star isomorphism, and it extends canonically to multiplier
algebras and descends to corona quotients. Consequently algebra membership,
the zero intersection, and corona injectivity are invariant under gauge.

The intrinsic twisted diagonal is canonical at the registered owner. What is
not canonical is:

- a selected trivializer identifying it element-by-element with the untwisted
  time algebra;
- the resulting Fourier coordinate after that choice; and
- a simultaneous identification of all torsors/components with one fixed
  `R/H` model using chosen origins.

The amendment states this distinction correctly and does not use an origin or
enumeration in the definition of the diagonal.

## 8. Route, controls, and proof-firewall audit

The ten-owner Route registry remains type-safe at this design stage. Owners
8 and 9 are expanded rather than silently duplicated; the future YAMLs are
required to serialize maximal and reduced claims separately. Owner 8 receives
no arithmetic credit. Owner 9 may receive only source-origin arithmetic
relation credit from the exact packet and the newly proved cardinality; the
uniform continuum conclusion does not distinguish primes and supplies no
A2--A4 promotion. Route B remains false.

The amendment correctly does not improvise v2 control arithmetic. It records
the exact reviewed v1 design tuple, marks that tuple insufficient for P13-8A--C,
and requires a separate exact v2 design and independent review before any
implementation. That future design must, at minimum:

- replace the obsolete conditional-`Q_p` diagnostic branch without treating a
  finite sign projection as proof of continuum cardinality;
- distinguish a bounded product from a `c0` sum without claiming that a finite
  truncation proves the infinite corona theorem;
- recompute all changed CSV, row, negative, summary, artifact, and test totals;
- update any negative fixture that currently treats all `Q_p` cardinality
  conclusions as forbidden, narrowing it instead to unsupported inference from
  the period or from a finite diagnostic alone; and
- retain the existing acyclic policy: no concurrent proof path or proof digest
  in the controls manifest, and no self-digest.

Because those requirements are deferred rather than falsely frozen here,
there is no v2 control-count arithmetic to approve in this review. No control
implementation is authorized.

## 9. Strongest counter-argument and standalone ceiling

The strongest publication-level counter-argument is now sharper than the
candidate records: P13-8A is not a new ingredient at all. Sealed Paper 2 owns
the sign/procyclic continuum lower bound and packet-orbit transfer. The at-most-
continuum estimate adds equality but no plausible standalone centre. The only
remaining candidate contribution is therefore P13-8B/C: a faithful component
embedding combined with the constant-norm diagonal and multiplier/corona
algebra of a `c0` sum. A later reviewer may still judge that completion-level
statement routine. Correctness and exact owner typing do not themselves
establish standalone weight.

The amendment correctly does not overturn `NOTE_OR_MERGE`, but its next version
must remove cardinality from the proposed new conjunction and bind Paper 2 as
internal prior. A fresh bounded precedent audit and post-proof independent
standalone adjudication must assess the **completion/corona theorem alone**.
That later reviewer, not this design review, must decide whether P13-8B/C create
the required nonformal dependency break.

## 10. Finding register and gate consequence

| Severity | Count | Open item |
|---|---:|---|
| Critical (`C`) | 0 | none |
| Major (`M`) | 1 | sealed Paper-2 continuum theorem omitted; P13-8A receives false new-credit weight |
| Minor (`m`) | 1 | exact inclusion of the odd-prime sign product in `U_p` is not specified |

```text
REVIEWED_V2_SHA256=99c796bffe24f262d8ac8458b21fd253451bca51bac4b283660dab319992ed82
CRITICAL_OPEN=0
MAJOR_OPEN=1
MINOR_OPEN=1
V2_DEVIL_DOMAIN_VERDICT=MAJOR_REVISION_REQUIRED
OPEN_FINDINGS=M1_INTERNAL_PAPER2_PRECEDENT,m1_SIGN_SUBGROUP_COORDINATE_EMBEDDING
P13_8A_TRUTH_STATUS=FEASIBLE_NOT_PROVED
P13_8B_TRUTH_STATUS=FEASIBLE_NOT_PROVED
P13_8C_TRUTH_STATUS=FEASIBLE_NOT_PROVED
STANDALONE_PASS=false
NOTE_OR_MERGE_BINDING=true
PROOF_AUTHORIZED_BY_THIS_REVIEW=false
CONTROL_DESIGN_AUTHORIZED_BY_THIS_REVIEW=false
CONTROL_IMPLEMENTATION_AUTHORIZED=false
ROUTE_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_OR_PUBLIC_SYNC_AUTHORIZED=false
```

**Final verdict: `C0/M1/m1`, major revision required.** Bind and correctly
credit the sealed Paper-2 theorem, remove P13-8A from the new standalone delta,
apply the exact coordinate-embedding repair, freeze new bytes, and re-lock them
independently. Until that occurs, the candidate's own zero-finding gate keeps
v2 proof and control-design work closed.

## 11. Closure addendum — ownership-corrected v2 exact-byte re-lock

Closure review date: **2026-08-15 (Asia/Shanghai)**  
Review mode: **narrow re-lock of this report's M1 and m1, with analytic,
owner, Route, and control-gate regression checks**  
Preserved report-prefix SHA-256:
`f75d35885dac9b665f87604e027701c1081a088ee9a71808cd0fba14d73c3005`  
Base-v2 SHA-256:
`99c796bffe24f262d8ac8458b21fd253451bca51bac4b283660dab319992ed82`  
Ownership-addendum SHA-256:
`d9523d1692d60fbdff7bbf5ab6c00d44bdcd26f02dc5cdeeba8c7ba43d78a39f`  
Narrow re-lock verdict: **PASS — C0/M0/m0**

### 11.1 Exact tuple, precedence, and review boundary

Before this closure was appended, the complete report reproduced the displayed
prefix hash exactly. The base-v2 and ownership-addendum files also reproduced
their displayed hashes. The addendum's new load-bearing authority locks were
rechecked directly:

| artifact | verified SHA-256 | re-lock use |
|---|---|---|
| Paper 2 manuscript | `72c34a0a30279ed7c070917a2c9242b8e9cb0a37a56779c246fa2cae04097fdc` | Proposition `prop:uncountable`, lines 391--436, including the full-coordinate sign proof and packet-orbit transfer |
| Paper 2 proof audit | `aaab83c32eb9d6c172be192dbb14acc6ed927a972d61c24a90dbfe94ecd0dbae` | independently accepted symbolic argument and topology/noncanonicity ceiling |

The addendum is narrow precedence, not a silent rewrite: only its declared
ownership, research-question, ambient-typing, novelty, Route-aggregation, and
status surfaces override the corresponding base-v2 wording. All untouched
signs, analytic proof obligations, falsifiers, source ceilings, and proof
firewalls remain binding.

This closure decides only whether the exact addendum repairs this report's M1
and m1 without introducing a new devil/domain defect. It does not prove
P13-8A--C, execute a precedent search, pass the source gate, design or run
controls, decide standalone weight, or authorize Route or manuscript work.

### 11.2 Finding-by-finding closure

| prior finding | exact amended repair | decision |
|---|---|---|
| M1 — sealed Paper-2 theorem omitted and P13-8A given false new-credit weight | Addendum Section 2 binds the exact Paper-2 manuscript/proof hashes and assigns Paper 2 the continuum lower bound and set-level packet-orbit transfer. Paper 13 receives no novelty, priority, author-delta, standalone, or Route credit for rederiving that proof. Its P13-8A delta is restricted to the elementary continuum upper bound/equality, Paper-9/Paper-12 retyping, direct standard-topology consequences, and later use as an inherited premise. Sections 2, 3, and 5 require P13-8B/C alone, after subtraction of ordinary `c0`, multiplier, crossed-product, and corona facts, to bear the standalone burden. | **CLOSED** |
| m1 — odd-prime sign product lacked an embedding in the full product | Addendum Section 4 defines each element as a family indexed by every prime `ell != p`, permits signs on `I_p`, and fixes every remaining coordinate to `1`. Its following sentences explicitly fix the unused `2`-adic coordinate when `p` is odd and note that no such coordinate exists when `p=2`. Thus the displayed set is a literal subgroup of `U_p`, with the same continuum cardinality and intersection argument. | **CLOSED** |

The repair to M1 is substantive rather than merely citational. Even a complete
Paper-13 rederivation of the sign argument is now exposition only. The amended
question and contribution matrix prevent that inherited theorem from being
counted indirectly inside a supposedly new conjunction.

### 11.3 Analytic and owner regression check

| surface attacked | amended status | regression decision |
|---|---|---|
| cardinal arithmetic | Paper 2 supplies the continuum lower bound; the base-v2 elementary upper bound remains a P13 proof obligation. Together they yield exact equality without CH. | no regression |
| actual versus bare/standard topology | `Q_p^actual` remains indiscrete and second countable; cardinality belongs to `Q_p^bare`; non-second-countability and non-`sigma`-compactness remain only on the discrete quotient and standard coproduct unit/arrow owners. | no topology promotion |
| arbitrary-index component record | Addendum Section 4 explicitly defines `Q^bare`, `Std(X)`, and the component `c0` sum over that bare set. It does not replace the `c0` algebra by a product or require an enumeration. | owner closed |
| full/reduced component norm | The test-level homomorphism, every-unit regular restriction, exact `I`-norm/`L^1` bridge for the maximal upper bound, regular lower bound, and time-group amenability step remain mandatory future proof receipts. | obligation preserved, not pre-proved |
| multiplier and corona | The component algebra is still the `c0` sum; its multiplier is the bounded product of component multiplier algebras. Constant coordinate norm still gives the exact intersection and corona kernel, conditional on the component isometries. | no `c0`/product conflation |
| gauge and choices | The frozen orientation `sigma overline(tau)=delta alpha` and component intertwining remain unchanged. The intrinsic diagonal is origin-free; trivializer, Fourier, and common-torsor presentations remain noncanonical choices. | no choice promotion |
| global framework boundary | BHM's lack of a second-countability requirement remains acknowledged. Componentwise records are retained because no exact global twisted framework/convention has yet been audited, not because non-second-countability universally forbids a groupoid C-star algebra. | source ceiling preserved |

Accordingly, the addendum creates no new analytic claim and relaxes no
load-bearing hypothesis. The common-lattice, cocompact, nonempty-owner,
continuous normalized multiplier, and max/reduced distinctions remain exactly
as frozen in the base design.

### 11.4 Route, source, and control-firewall regression check

The ten-owner registry remains a provisional design rather than a numerical
target. Owner 9 must serialize Paper 2 as inherited cardinality evidence and
assign the sign proof no P13 novelty or Route credit. Owners 8--9 may aggregate
`max` and `r` only when final proof and source review give both completions the
same evidence status and Route verdict; otherwise an independently reviewed
pre-Route owner/count amendment is mandatory. No A2--A4 promotion is gained,
and Route B remains false.

The source gate is strengthened, not passed: it must cover internal
nonredundancy against Papers 1--12 with Paper 2 explicit, plus bounded external
precedent for component crossed products, arbitrary-index `c0` sums,
multiplier diagonals, and corona embeddings. Its strongest possible novelty
result remains `SUPPORTED_WITHIN_SEARCH`.

The control firewall also remains intact. The reviewed v1 control tuple is
still insufficient for P13-8A--C. A separate exact v2 control design and its
independent review must precede implementation, must recompute every changed
row/negative/summary/artifact/test total, and must distinguish finite
diagnostics from proofs of continuum cardinality or corona survival. It may
bind no concurrent proof digest and may not create a circular proof/control
dependency.

### 11.5 Strongest surviving counter-argument and standalone ceiling

After subtracting Paper 2 and the standard operator-algebra ingredients, the
only proposed standalone centre is the fully typed max/reduced component norm,
origin-free actual-to-standard multiplier diagonal, finite/infinite
intersection, faithful corona image, and gauge-covariant fixed-prime
specialization. That package is coherent enough to remain a proof candidate,
but a later reviewer may still find it a routine assembly of standard facts.
This zero-finding ownership re-lock therefore does not close the binding
publication-level `NOTE_OR_MERGE` finding and does not predeclare standalone
status.

### 11.6 Zero-finding coverage receipt and gate consequence

| dimension checked | exact receipt |
|---|---|
| Paper-2 ownership/nonredundancy | lower-bound proof and packet transfer are exactly inherited; no P13 credit survives |
| sign-coordinate typing | full index family and the omitted `2`-coordinate are explicit |
| analytic theorem design | full/reduced, multiplier, intersection, corona, gauge, and source hypotheses remain feasible but unproved |
| owner topology | actual, bare, standard coproduct, and discrete quotient conclusions remain separated |
| Route typing | inherited evidence and conditional max/reduced aggregation are explicit; all Route authorizations remain false |
| control arithmetic/firewall | a new reviewed design is still required; finite controls cannot prove infinite theorems; no proof hash may be bound concurrently |
| standalone and downstream status | `NOTE_OR_MERGE` remains binding; source, proof, controls, Route, manuscript, and release gates remain closed |

No new Critical, Major, or Minor devil/domain finding arose on the exact
base-v2 plus ownership-addendum tuple.

```text
PRESERVED_REVIEW_PREFIX_SHA256=f75d35885dac9b665f87604e027701c1081a088ee9a71808cd0fba14d73c3005
BASE_V2_SHA256=99c796bffe24f262d8ac8458b21fd253451bca51bac4b283660dab319992ed82
OWNERSHIP_ADDENDUM_SHA256=d9523d1692d60fbdff7bbf5ab6c00d44bdcd26f02dc5cdeeba8c7ba43d78a39f
M1_CLOSED=true
m1_CLOSED=true
CRITICAL_OPEN=0
MAJOR_OPEN=0
MINOR_OPEN=0
DEVIL_DOMAIN_RELOCK_VERDICT=PASS
PAPER2_CONTINUUM_LOWER_BOUND_INHERITED=true
P13_CARDINALITY_STANDALONE_CREDIT=false
P13_8B_C_STANDALONE_CANDIDATE_ONLY=true
STANDALONE_PASS=false
NOTE_OR_MERGE_BINDING=true
V2_SOURCE_GATE_PASSED=false
V2_PROOF_AUTHORIZED=false
V2_CONTROL_DESIGN_AUTHORIZED=false
CONTROL_IMPLEMENTATION_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_INVOCATION_ALLOWED=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

**Final narrow re-lock verdict: PASS — C0/M0/m0.** This is one independent
devil/domain receipt on the exact base-v2 plus ownership-addendum tuple. It
authorizes no downstream action by itself.
