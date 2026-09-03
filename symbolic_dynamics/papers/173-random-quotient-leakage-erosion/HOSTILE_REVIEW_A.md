# Hostile Review A — P173 Random Quotient-Leakage Erosion

**Review date:** 2026-09-03 UTC  
**Reviewer role:** independent non-author reviewer A  
**Verdict:** `MAJOR_REPAIRS_REQUIRED_BEFORE_INTERNAL_ACCEPTANCE`  
**Mathematical triage:** `CORE_PROVABLE; N=0_JORDAN_STATEMENT_FALSE_AS_WRITTEN`  
**Lifecycle (unchanged):** `SPIKE_2_COLLISION_RISK / HOLD_EXTERNAL`

## Outcome

The quotient-map reduction, common ambient-lift exponent, fixed labelled
target count, dimension lumping, every-time division, full algebraic
spectrum, complementary transient Jordan ladder, and absorption formulas all
survive an independent derivation and an alternate exact implementation.
In particular, the Jordan coupling remains nonzero even when the direct
one-step transition between complementary dimensions vanishes.

The present Round-0 manuscript is nevertheless not provable literally as
stated.  It puts `n=0` in scope but says unconditionally that eigenvalue one
has two `J_1` blocks.  At `n=0`, zero and `V` are the same subspace and
`Q=(1)`, so there is only one block.  I also found a visible malformed
exponent in the central definition and a primary-source attribution that
misidentifies Balakin's sparse matrix ensemble as support for the uniform
rectangular count.  The owner boundary needs one explicit subspace source
and an auditable P109/P162/P165/P168 table.

### Severity count

| Severity | Count |
|---|---:|
| Critical | 0 |
| Major | 2 |
| Minor | 2 |

No manuscript or PDF was edited during this review.

## Frozen review inputs

| Artifact | SHA-256 |
|---|---|
| `main.tex` | `a92bd9855eaff59ee226ab27021cacf157ca0ce6cde8e6ed6e9b13b451d8db27` |
| `main.pdf` | `d876f022bdc1e04ec57b0f9438db78b1f84abb1691c61dbd78d53083df48d359` |
| `main_round0_original.pdf` | `d876f022bdc1e04ec57b0f9438db78b1f84abb1691c61dbd78d53083df48d359` |
| author `verify_p173.py` | `875822e6cce2e6bd04af8dfd40d7b82f9d5a02e981828325c2e20fe918e719c9` |
| author `verification_output.txt` | `e9281160c7acb8b405012a13cce23d10491b61c430975f477ecfe8136ef3b988` |

The two intake PDFs are byte-identical and the current PDF has three A4
pages.  Its metadata author, creator, and producer fields are blank.

## Independent derivation

### P173-A-T01 — quotient uniformity and ambient lift exponent: pass

Fix `U<=V` of dimension `a` and write `c=n-a`.  The observation map

```text
rho_U : End(V) -> Hom(U,V/U),     T -> pi_U T|_U
```

is linear and onto.  Indeed, choose a complement `V=U direct-sum W`, identify
`W` with `V/U`, lift any `f:U->V/U` into `W`, and extend that lift by zero on
`W`.  The codomain has dimension `ac`, so rank-nullity gives

```text
dim ker(rho_U)=n^2-a(n-a).
```

Every quotient map therefore has exactly
`q^(n^2-a(n-a))` ambient endomorphism lifts, and a uniform ambient `T`
induces a uniform element of `Hom(U,V/U)`.  This proves the claimed exponent
without an independence assumption on chosen matrix coordinates.

The reviewer control enumerates every quotient-map signature in independent
annihilator coordinates and checks that every signature receives exactly
that common number of ambient lifts.  **No mathematical repair is required.**

### P173-A-T02 — every labelled target fibre: pass after the typesetting repair

For a prescribed `B<=U`, with dimensions `b<=a`, a map `L:U->V/U` has kernel
exactly `B` precisely when its descent

```text
U/B -> V/U
```

is injective.  If `d=a-b`, the number is zero for `d>n-a`; otherwise it is

```text
product_(i=0)^(d-1) (q^(n-a)-q^i).
```

Multiplication by the common ambient-lift factor proves the fixed-target
fibre, and division by `q^(n^2)` gives the one-step probability.  A target
outside `U` is impossible because the update is a kernel contained in `U`.
This also covers `a=0`, `a=n`, `b=a`, and the impossible-rank range.

The proof and code use this correct product.  Equation (2) alone prints a
comma inside the exponent; that local but mandatory defect is finding
`P173-A-m01` below.

### P173-A-T03 — dimension quotient and every-time labelled division: pass

There are `[a choose b]_q` possible `b`-targets inside a fixed `a`-space, so
summing the common target probability gives exactly

```text
Q_ab = [a choose b]_q C_nq(a,b) / q^(a(n-a)).
```

The kernel description also proves nesting at every epoch.  For a fixed
initial `U`, its stabilizer in `GL(V)` is transitive on the `b`-subspaces of
`U`.  Conjugating every freshly sampled endomorphism by one stabilizer element
is a measure-preserving bijection of histories and transports endpoints.
Consequently the mass `(Q^t)_ab` is uniform over those
`[a choose b]_q` endpoints for every `t>=0`.  This yields

```text
P^t(U,B)=(Q^t)_ab/[a choose b]_q
```

for `B<=U`, and zero otherwise.  At `t=0`, only the equal-dimensional target
`B=U` remains, so there is no hidden endpoint exception.  **No repair is
required.**

### P173-A-T04 — full algebraic spectrum: pass

Order all labelled subspaces by nondecreasing dimension.  Every transition
lands in a subspace of the source, hence `P` is triangular.  Its diagonal at
an `a`-space is the probability that the quotient map is zero:

```text
P(U,U)=q^(-a(n-a)).
```

There are `[n choose a]_q` labelled `a`-spaces.  The asserted algebraic
multiset follows directly from the diagonal, including the addition of
multiplicities when `a` and `n-a` have the same value.  The manuscript
correctly does not claim the full Jordan form of `P`.  **No repair is
required.**

### P173-A-T05 — complete quotient Jordan ladder: pass for `n>=1`

Put `lambda_a=q^(-a(n-a))`.  Strict concavity and symmetry of `a(n-a)` show
that its only repeated quotient diagonals are the pairs `b,n-b`.  Fix
`1<=b<n/2`, put `a=n-b`, and solve `(Q-lambda_b I)x=0` from low to high
dimension with `x_b=1`.

For `b<k<a`, one has `lambda_k<lambda_b`, and

```text
x_k = (sum_(j<k) Q_kj x_j)/(lambda_b-lambda_k) > 0.
```

Positivity follows inductively from `Q_(k,k-1)>0`.  At row `a`, the diagonal
again equals `lambda_b`, but the compatibility sum is positive because it
contains `Q_(a,a-1)x_(a-1)`.  Thus the eigenvector born at `b` is destroyed;
the one born at `a` remains.  Algebraic multiplicity two and geometric
multiplicity one give exactly one `J_2` block.

This argument is essential in the indirect cases.  For example, at
`(q,n,b,a)=(2,7,1,6)`, the direct entry `Q_(6,1)` is zero because a five-rank
injection into a one-dimensional quotient is impossible.  Nevertheless the
positive adjacent chain through dimensions `2,3,4,5` makes the terminal
compatibility sum nonzero.  The independent control obtains kernel
nullities `(1,2,2)` for the first three powers of `Q-lambda I`.

At eigenvalue one, the proof should use the correct row-stochastic
orientation explicitly.  For `n>=1`, the constant column vector and the
indicator of dimension `n` are independent right eigenvectors.  Since the
algebraic multiplicity is two, the endpoint value is semisimple.  Saying only
that there are two fixed rows is too compressed: an absorbing row directly
supplies a left eigenvector, not automatically the right eigenvectors used in
the preceding recursion.  This clarification is included in the mandatory
`n=0` repair rather than counted separately.

When `n` is even and positive, the midpoint occurs once and is one `J_1`.
These blocks exhaust `n+1` dimensions.  At `n=0`, however, the two proposed
endpoint vectors coincide and only one block exists; see `P173-A-M01`.

### P173-A-T06 — absorption: pass

At dimensions zero and `n`, the quotient is zero, so those states are fixed
(and coincide when `n=0`).  If `0<a<n`, then
`Q_aa=q^(-a(n-a))<1`, while `Q_(a,a-1)>0`.  Hence the holding time before a
strict dimension loss is almost surely finite.  There can be at most `a`
strict losses before zero, proving almost-sure absorption without an
irreducibility assumption.

The all-time target formula at the unique zero subspace gives
`Pr_a(tau_0<=t)=(Q^t)_a0`, and first-step conditioning gives the stated exact
mean recurrence.  For `n=2`, direct substitution yields
`((q-1)/q,1/q,0)` in the sole transient row and mean `q/(q-1)`.
The `n=1` chain has two fixed states.  **No mathematical repair is required.**

## External owner and source stress

### Uniform rank/nullity owner

Fulman and Goldstein explicitly take a matrix uniformly from all rectangular
matrices over `F_q` and study its nullity distribution.  This directly owns
the dimension-level rank/nullity ingredient after transpose when necessary:

- Jason Fulman and Larry Goldstein, *Stein's Method and the Rank Distribution
  of Random Matrices over Finite Fields*, Annals of Probability 43 (2015),
  1274--1314, [arXiv:1211.0504](https://arxiv.org/abs/1211.0504),
  DOI `10.1214/13-AOP889`.

Conditional uniformity of the kernel over subspaces of one dimension follows
from `GL(U)` symmetry; the fixed labelled kernel formula is the standard
orbit refinement.  The extra factor counting ambient extensions is elementary
linear algebra.  None of these ingredients should receive standalone
contribution credit.

### Balakin is not the uniform-matrix owner claimed in the prose

The primary MathNet record states that Balakin's entries are independent but
have a sparse, `n`-dependent law with a distinguished probability at zero;
they are not uniform field elements.  Balakin is relevant broader random-rank
background, but does not directly own the uniform quotient-map count used in
Equation (2):

- G. V. Balakin, *The Distribution of the Rank of Random Matrices over a
  Finite Field*, Theory of Probability and Its Applications 13 (1968),
  594--605, [primary MathNet record](https://www.mathnet.ru/eng/tvp/v13/i4/p631),
  DOI `10.1137/1113076`.

This mismatch is finding `P173-A-M02`.  Fulman--Goldstein remains a valid
direct owner, so correcting the attribution does not restore contribution
credit to the rank/nullity calculation.

### Gaussian subspace census

The Gaussian coefficient is the classical subspace census and must remain
zero credit.  Because it supplies both the dimension quotient and the full
spectral multiplicities, the source ledger should cite a primary subspace
enumeration source rather than leave it unreferenced.  A suitable already
verified internal source is Jay Goldman and Gian-Carlo Rota, *On the
Foundations of Combinatorial Theory IV: Finite Vector Spaces and Eulerian
Generating Functions*, Studies in Applied Mathematics 49 (1970), 239--258,
DOI `10.1002/sapm1970493239`.

### Direct-process search boundary

A bounded search using the literal update, random quotient kernels, subspace
Markov chains, and complementary Jordan blocks did not locate a primary
source asserting the full process package.  This is only a non-hit.  It has no
positive force for novelty, priority, freedom to operate, or external release.
`HOLD_EXTERNAL` must remain.

## Internal P1--P171 firewall

The four requested comparators own substantial reusable ingredients, so the
current `SPIKE_2_COLLISION_RISK` assessment is justified.

| Internal owner | What is already owned | Why the literal theorem does not transfer wholesale |
|---|---|---|
| P109, nilpotent image subspace dynamics | the full finite subspace-lattice carrier, Gaussian target counts, quotient/graph fibre geometry, exact absorption layers | P109 applies one fixed deterministic nilpotent image map `U->N(U)` and counts phase-state sources of `N^t(U)=W`; P173 resamples an ambient map and counts map histories/kernels from a fixed source.  Its complementary stochastic spectrum is absent from P109. |
| P162, random translation intersection | random self-intersection/erosion language, rank-controlled histories, all-time target laws, absorption | P162 acts on arbitrary subsets of `F_2^d`; history span collapses all translations and fibres are controlled by affine cosets and target stabilizers.  P173 acts on linear subspaces and resamples a state-dependent quotient homomorphism.  The P162 history polynomial does not specialize to `Q`. |
| P165, low-weight support shortening | deterministic descending dynamics on codes/subspaces, sharp absorption height, every-time image criteria | P165 extracts a coordinate support from the current code and explicitly has no complete target-fibre formula.  It has neither uniform quotient kernels nor the complementary eigenvalue collision. |
| P168, quartic inverse-span dynamics | a complete subspace carrier over `F_(p^4)`, Gaussian census, deterministic functional graph, every-target fibres | P168's patched-inverse span is a deterministic, dimension-increasing map with fixed/two-cycle geometry.  No parameter substitution converts its inverse-line classification into random kernel erosion or `Q`. |

There is no literal equality and no coefficient substitution importing the
whole P173 theorem from one comparator.  On the other hand, carrier,
quotient-fibre language, random erosion, Gaussian incidence, and absorption
are already exhausted across them.  The defensible residual is therefore
only the conjunction of the fresh state-dependent quotient process,
all-time labelled transition law, and complementary-dimension Jordan
resonance.  It is not a claim that each ingredient is new.  The manuscript's
generic phrase “earlier ... notes” should be made auditable as required by
`P173-A-m02`.

## Independent executable pressure

Reviewer evidence lives in
`docs/papers172_176_sequence/reviews/p173_review_a/`.  It imports no author or
scouting code.  Literal subspaces are unique RREF row bases over prime fields;
ambient matrices are field-entry tuples; and membership in `U` is tested by
an annihilator basis of `V/U`.  This is structurally different from the
author/scout materialized vector sets and binary matrix masks.

The exact control covers:

- every ambient map, every source, every target, every quotient signature,
  and labelled powers through six epochs for `q=2`, `n=0..3`;
- the same literal fibre and lift audit through five epochs for
  `q=3`, `n=0..2`;
- the full diagonal/spectral census in every literal box;
- exact quotient/Jordan/absorption tests for
  `q in {2,3,4,5,7,8,9,11}`, `n=0..14`;
- explicit constant and full-space endpoint eigenvectors;
- `128` direct and `208` indirect complementary pairs; and
- the corrected one-block `n=0` endpoint inventory.

Two fresh processes produced byte-identical transcripts.  The canonical run
reports `36,390` exact assertions.

| Reviewer artifact | SHA-256 |
|---|---|
| `verify_review_a.py` | `aab50dab0d8a1344a72b5358d4ae72dc4917004dc7fefd8f1b07803f09f06076` |
| `CANONICAL.txt` | `955b32d2da25522553a5954a48d91b19f318339921bc3313c3a65e05fec19460` |

The paper-local verifier also replays, and a source comparison found no
substantial exact copied block from the scouting program (the longest exact
contiguous match was five lines).  I therefore do not issue the provenance
finding that applied to P176.  The new reviewer implementation nevertheless
supplies the requested stronger representation-level independence.

## Finding ledger

### P173-A-M01 — the complete Jordan statement is false at `n=0`

**Severity:** Major  
**Status:** mandatory theorem, proof, support-document, and verifier repair

The setup allows an `n`-dimensional space without imposing `n>=1`, the final
proof explicitly includes `n=0`, and `SELF_QA.md` says that boundary is
covered.  Nevertheless the abstract and Theorem 1(iii) say that eigenvalue
one has two `J_1` blocks because zero and `V` are separately fixed.  At
`n=0`, `0=V`, there is one state, and `Q=(1)`.  Its Jordan form is one
`J_1(1)`, not two.

**Mandatory repair:** retain `n=0` with an explicit exception in the abstract,
Theorem 1(iii), Jordan proof, boundary paragraph, and self-QA, or impose a
standing `n>=1` hypothesis and consistently remove `n=0` from scope.  The
cleaner repair is to keep the degenerate case and state one block there.  For
`n>=1`, exhibit the constant vector and the dimension-`n` indicator as the
two independent right eigenvectors; do not rely only on “two fixed rows.”
Extend the author verifier so its claimed Jordan PASS actually tests the
`n=0` block count.

### P173-A-M02 — primary owner attribution conflates nonuniform and uniform ensembles

**Severity:** Major (source/ownership integrity)  
**Status:** mandatory citation, source-ledger, and claim-boundary repair

Main-text lines 67--68 present Balakin together with Fulman--Goldstein as
support for uniform finite-field rank/nullity, and lines 251--254 say that
“Balakin's rank distribution” owns the counts used in Equation (2).
Balakin's primary record instead specifies a sparse, `n`-dependent entry
law.  Fulman--Goldstein does use the uniform rectangular ensemble and is the
appropriate cited owner for the dimension-nullity law.

**Mandatory repair:** cite Fulman--Goldstein for the uniform rectangular law;
either remove Balakin from that sentence or identify it accurately as broader
nonuniform finite-field random-rank background.  Update
`SOURCE_VERIFICATION.md` to record the ensembles, not just metadata.  Add a
primary Gaussian-subspace citation such as Goldman--Rota, and explicitly say
that the fixed labelled kernel is the symmetry refinement and the ambient
lift exponent is elementary.  Preserve zero contribution credit and
`HOLD_EXTERNAL`.

### P173-A-m01 — Equation (2) contains a visible comma in the exponent

**Severity:** Minor  
**Status:** mandatory source and PDF repair

Line 78 of `main.tex` has

```tex
(q^{,n-a}-q^i)
```

instead of `q^{n-a}` (or the spacing form `q^{\,n-a}`).  LaTeX accepts the
comma as mathematics, and the PDF visibly extracts it as `q^{,n-a}`.  This is
the definition used by the theorem, even though the proof at line 163 and
both verifiers use the correct expression.

**Mandatory repair:** remove the comma, rebuild, and visually inspect the
central display.  No theorem change beyond this token is needed.

### P173-A-m02 — internal subtraction is correct in direction but not auditable

**Severity:** Minor  
**Status:** mandatory package-document firewall repair

The manuscript and `SOURCE_VERIFICATION.md` refer only to unnamed “earlier
subspace-lattice and random-intersection notes.”  That wording safely assigns
credit away, but it does not let a later reviewer reconstruct the collision
decision against P109, P162, P165, and P168.

**Mandatory repair:** add the four-row comparator table above, or an
equivalent literal/engine table, to `SOURCE_VERIFICATION.md`; name what each
paper owns and the exact hypothesis preventing wholesale transfer.  The
generic manuscript sentence may remain once the package ledger is explicit.
Do not upgrade the residual or weaken `SPIKE_2_COLLISION_RISK`.

## Mandatory repair list

1. Correct the `n=0` quotient Jordan inventory everywhere and add the missing
   author-verifier sentinel; explicitly justify the two right eigenvectors
   for `n>=1`.
2. Correct the Balakin/Fulman--Goldstein ensemble attribution, add a primary
   Gaussian-subspace owner, and sharpen the zero-credit statement.
3. Replace `q^{,n-a}` by `q^{n-a}` and rebuild/inspect the PDF.
4. Add an explicit P109/P162/P165/P168 internal collision table to the source
   ledger.

After these repairs, the mathematical core can proceed to a fresh Round 1
and independent Review B.  No repair may convert the bounded direct-owner
non-hit into novelty evidence.  Preserve
`SPIKE_2_COLLISION_RISK / HOLD_EXTERNAL`.

## Author-response closure ledger — Round 1 delta acceptance

**Delta checked:** 2026-09-03 UTC  
**Mode:** read-only manuscript/PDF acceptance; only this ledger was appended  
**Closure verdict:** `ALL_REVIEW_A_FINDINGS_CLOSED`  
**Lifecycle:** `SPIKE_2_COLLISION_RISK / HOLD_EXTERNAL` (unchanged)

The accepted Round-1 source and executable locks are:

```text
main.tex                    cef3dcdcb27156c489ea852fce37056cc6a447707f0750d29cabd317c3343dcf
references.bib              80923d6bc774cbbc7062ea92b51053010379d3c40507216a87649774aa450b71
verify_p173.py              86ce849e9b01ed316d4a8bf37eac9ade52b949b98e0aae2d02b59e5e4a356642
verification_output.txt     b32f20b843b22d719633620971f12cdc67a1e3ca02003aff41ea3b15261421d0
main.pdf / main_round1.pdf   1a66075c7d64ae943cbbd42503b81964ea7fabe85e2ee7515001a052aa5cce22
main_round0_original.pdf    d876f022bdc1e04ec57b0f9438db78b1f84abb1691c61dbd78d53083df48d359
```

`main.pdf` and `main_round1.pdf` are byte-identical; the original Round-0
PDF remains distinct and preserved.  The repaired PDF is four A4 pages with
blank author, creator, and producer metadata.

| Finding | Status | Read-only acceptance evidence |
|---|---|---|
| `P173-A-M01` | **CLOSED** | The abstract and Theorem 1(iii) now distinguish `n=0` (one `J_1(1)`) from `n>=1` (two semisimple endpoint blocks).  The proof explicitly supplies the constant right eigenvector and the full-dimension indicator right eigenvector and explains their independence.  The boundary paragraph and `SELF_QA.md` agree.  The author control now tests `Q=(1)` and endpoint nullity one at `n=0`. |
| `P173-A-M02` | **CLOSED** | The uniform rectangular rank/nullity law is assigned to Fulman--Goldstein.  Balakin is accurately retained only as sparse, nonuniform random-rank background.  Goldman--Rota is added as the primary Gaussian finite-vector-space census.  Fixed-kernel symmetry and the ambient-lift exponent remain explicitly zero-credit elementary refinements in both manuscript and source ledger. |
| `P173-A-m01` | **CLOSED** | Equation (2) now contains `q^{n-a}-q^i`.  PDF text extraction confirms the displayed exponent has no comma, and the later proof uses the same expression. |
| `P173-A-m02` | **CLOSED** | `SOURCE_VERIFICATION.md` now contains an explicit four-row P109/P162/P165/P168 carrier/engine/nontransfer table.  The residual is not widened, `SPIKE_2_COLLISION_RISK` remains visible, and the bounded owner-search non-hit is still denied novelty force. |

A fresh deterministic author replay matched `verification_output.txt` byte
for byte and reported `13,307` assertions with `RESULT PASS`.  A fresh
replay of the independent Review-A control also remained byte-identical to
its canonical transcript (`36,390` assertions).  No omitted Review-A repair
was found.  This closes the four Review-A findings only; it does not certify
novelty, remove the collision-risk flag, authorize circulation, or replace
independent Review B.

Review B was subsequently completed and delta-closed.  The final paper-level
status is `DUAL_REVIEW_CLOSED / SPIKE_2_COLLISION_RISK / HOLD_EXTERNAL`.
