# Hostile Review B — P173

**Manuscript:** *Random Quotient-Leakage Erosion: Every-Target Fibres and a
Complementary Jordan Ladder*  
**Review role:** independent Reviewer B; not an author and not a re-user of
the author or Review-A verifier  
**Review date:** 2026-09-03 UTC  
**Lifecycle held fixed:** `SPIKE_2_COLLISION_RISK / HOLD_EXTERNAL`

## Verdict

```text
PASS / DUAL_REVIEW_CLOSED
SPIKE_2_COLLISION_RISK / HOLD_EXTERNAL
```

## Final Round-2 delta acceptance — CLOSED

**Read-only acceptance date:** 2026-09-03 UTC  
**Open findings after acceptance:** **Critical 0 / Major 0 / Minor 0**  
**Disposition:** `PASS / SPIKE_2_COLLISION_RISK / HOLD_EXTERNAL`

The Round-2 delta satisfies every mandatory criterion in Sections 6–8.  The
three findings are closed:

| finding | status | acceptance evidence |
|---|---|---|
| `P173-B-MAJ-01` | **CLOSED** | exact Evans/Van Peski attribution, zero-credit language, owner-log queries, and the square-versus-rectangular non-transfer boundary are present and consistent |
| `P173-B-MAJ-02` | **CLOSED** | P172 is reciprocally subtracted on every named claim surface, including the specified-box/one-terminal-`J_2` versus linear-injection/complementary-ladder contrast |
| `P173-B-MIN-01` | **CLOSED** | the proof now uses an unconditional conjugation bijection between raw endpoint events, explicitly including zero-mass layers and `t=0` |

### Final.1 External owner subtraction accepted

The first uniform-kernel boundary in `main.tex` now says that Evans supplies
the elementary-divisor dimension-chain precursor and Van Peski supplies the
labelled descending-subspace refinement, uniform square kernel, and
fixed-target injection count.  It gives those ingredients and ordinary
Markov powering zero credit.  The closing boundary repeats the subtraction
and states the decisive non-transfer parameter:

```text
Van Peski: current dimension a -> codomain dimension a,
           in a filtration of one Haar local-field matrix;
P173:      current dimension a -> codomain dimension n-a,
           with fresh maps in one fixed n-space.
```

The closing text does not claim that Evans or Van Peski supplies the
fixed-ambient complementary-codimension schedule, its diagonal symmetry, or
its Jordan ladder.  `SOURCE_VERIFICATION.md` additionally records that the
rows coincide at `n=2a` but the chains do not coincide away from that layer.
This is the required non-transfer boundary, not a novelty inference.

`references.bib` contains the conventional complete Evans journal record
(author, title, journal, volume, issue, pages, year, DOI) and the Van Peski
thesis record (author, title, thesis type, department, university, May 2018,
advisor, and primary author URL).  `SOURCE_VERIFICATION.md` pins the fuller
record dates—November 2002 and 7 May 2018—and the exact theorem/equation
mapping.  A shadow audit asked whether the journal month and thesis day must
also be duplicated as BibTeX fields.  No change is required: neither field is
needed to resolve the cited primary record, neither bibliography entry is
incorrect, and the exact dates are already present on the dedicated source
surface.

The live stochastic-matrix owner log includes all three required query
families:

```text
p-adic elementary divisors subspace Markov chain kernel
filtered vector spaces random matrix kernel Markov chain
cokernel partition labelled subspace chain
```

It maps Evans Theorem 3.5 and Van Peski Theorem 3.3.4 with (3.42)–(3.55) to
the zero-credit claims and retains only the bounded fixed-ambient rectangular
schedule and complementary ladder.  It expressly says that a query miss is
not evidence of novelty, publishability, ownership clearance, or circulation
safety.

The wording that ordinary powers receive zero credit is accepted.  It is
standard Markov composition once the labelled one-step chain is known; the
package does not misstate it as a separate residual theorem supplied by an
unrelated source.

### Final.2 Reciprocal P172 subtraction accepted

`main.tex` and `SOURCE_VERIFICATION.md` now contain the full reciprocal row:
P172 owns the fresh-map/nested-erosion/small-quotient/labelled-recovery/
triangular-Jordan/absorption shell, all of which earns zero separation credit.
They also state the non-transfer boundary: P172 has specified-box set-image
occupancy, a total-image mark, and one terminal `J_2`; P173 has a literal
rectangular linear-injection realization and a complementary-dimension
ladder, and no coefficient substitution transfers one matrix to the other.

The same distinction is now visible on every named local surface:
`README.md`, `NARRATIVE_REPORT.md`, `PAPER_PLAN.md`, `CLAIMS_EVIDENCE.md`, and
`SELF_QA.md`.  In particular, the strict final delta added the compact
specified-box/one-terminal-`J_2` versus linear-injection/complementary-ladder
contrast to `README.md`, `PAPER_PLAN.md`, and `CLAIMS_EVIDENCE.md`; those had
previously recorded the subtraction but not the entire non-transfer sentence.
The retained “linear injection fibre” on summary surfaces is understood only
as the literal fixed-ambient rectangular realization, not as contribution
credit for the generic kernel/injection formula.  This agrees with the source
ledger's explicit statement that generic uniform-kernel fibres, ordinary
labelled powering, and the elementary ambient lift are not residual claims.

No local surface upgrades the lifecycle, calls a bounded non-hit novelty, or
claims that the P172 or Van Peski/Evans theorems transfer the complementary
ladder.  The process lines saying delta acceptance was pending are accurate
descriptions of the audited pre-acceptance snapshot; they are historical
bookkeeping, not open claim defects.

### Final.3 Null-event proof accepted

The proof of Theorem 1(ii) no longer conditions on the possibly null event
`dim U_t=b`.  For equal-dimensional `B,B'<=U`, it chooses a stabilizer element
`g` with `gB=B'` and conjugates every map in a complete history.  This is an
unconditional probability-preserving bijection

```text
{U_t=B} <-> {U_t=B'},
```

explicitly including the case in which both events have probability zero.
Summing the resulting raw equalities over the Gaussian target layer proves
the displayed division, including `t=0`.  The Minor is fully repaired without
changing the theorem statement.

### Final.4 Executable and build delta

Both exact controls were replayed from fresh processes and compared
byte-for-byte with their preserved transcripts:

```text
author verifier:   13,307 assertions, canonical match
Review-B verifier: 9,995,101 assertions, canonical match
```

`main.pdf` and `main_round2.pdf` are byte-identical, four A4 pages, 333,340
bytes, with blank title/author/subject/keyword/creator/producer metadata.  The
settled third LaTeX pass has no warning, unresolved citation/reference, bad
box, or rerun request.  The expected pre-settlement citation warnings in the
earlier BibTeX passes do not survive the final log or PDF.

Delta-accepted pre-closeout pins:

```text
b28cfc0fa8b848cce50e48cbf12bb63dd7ac95d7fae7fb0b700ce34d7e0b35d4  main.tex
0e209fec1fd2fe3e6f93804a801836ec3dc97663319a70ca3ec8b93ff1981366  references.bib
01235b8279d922b0d120f869f32ef8be1ee6aea105dafbc5ea25155be1ef039c  main.pdf
01235b8279d922b0d120f869f32ef8be1ee6aea105dafbc5ea25155be1ef039c  main_round2.pdf
77a5deceded3016f1eb37b04e3fee454709c9df79f902d65658903985d05183b  SOURCE_VERIFICATION.md
027a22e317515e1f509c3628a67007c070d5dc76500c68b0b8108df2c87138d3  README.md
d39169ab2189405fd2f04d81142f9890389a9bdf85525c5635ab63fce14cf9f1  NARRATIVE_REPORT.md
9670e22162b88b4d960341b08d1c938a2cd86683997de2ee8300773684688a2f  PAPER_PLAN.md
6ef5b1b25b5c837142626a7f0ecb3271da578e1b8f85b32aa027ea38fbf2384d  CLAIMS_EVIDENCE.md
d5d2f089a5cdf209dbac7c0a7fb3bdb40cd4393d22bcb09cf5eb73c565c0a414  SELF_QA.md
287b239b8210839dedda7e81dadcbdeb8920fdd78149ad33e9a9bfb6da1d6f9c  IMPROVEMENT_LOG.md
f7beabc0c51a3faec0a96b741f150e15dfdbb9720b567f9d223de932533a2a4e  BUILD.md
e3ef22cff0bf3d08be6d5dfa77018cab4b613bca4038cfa7e590ff67a788c604  OWNER_SEARCH_LOG.md
```

This is a delta closure, not an external owner clearance.  Review B has no
remaining mathematical, source, collision, proof, or executable repair.  The
maximum accepted disposition is therefore

```text
PASS / SPIKE_2_COLLISION_RISK / HOLD_EXTERNAL
```

**Initial Round-1 findings before repair:** **Critical 0 / Major 2 / Minor 1**.

The exact theorem package survived an independent derivation and 9,995,101
executable assertions.  I found no counterexample to the ambient fibre, the
dimension quotient, the every-time labelled formula, the full algebraic
spectrum, the quotient Jordan inventory, or the absorption statements.

The Round-1 paper was not acceptable in its then-current owner ledger.  A
primary source then omitted from the package gives a labelled descending-subspace
Markov chain whose transition is the kernel of a uniform square map and whose
fixed-target probability is the same injection count used here.  In addition,
the paper-local firewall failed to subtract sibling P172 even though the batch
firewall and P172 itself explicitly record the collision.  Those omissions
were Major because they materially narrowed which parts of P173 could be
presented as residual.  A smaller proof-language defect conditioned on
zero-probability events.

No finding permits a lifecycle upgrade.  This review makes no novelty,
priority, noninfringement, or circulation claim.

## Stable input audited

The review was performed against the coordinator-designated Round-1 snapshot:

```text
cef3dcdcb27156c489ea852fce37056cc6a447707f0750d29cabd317c3343dcf  main.tex
80923d6bc774cbbc7062ea92b51053010379d3c40507216a87649774aa450b71  references.bib
86ce849e9b01ed316d4a8bf37eac9ade52b949b98e0aae2d02b59e5e4a356642  verify_p173.py
b32f20b843b22d719633620971f12cdc67a1e3ca02003aff41ea3b15261421d0  verification_output.txt
1a66075c7d64ae943cbbd42503b81964ea7fabe85e2ee7515001a052aa5cce22  main.pdf
1a66075c7d64ae943cbbd42503b81964ea7fabe85e2ee7515001a052aa5cce22  main_round1.pdf
```

The Round-1 repairs recorded against Review A were treated as input, not as
Reviewer-B work.  I confirmed the repaired `n=0` endpoint, the two independent
endpoint eigenvectors for `n>=1`, the corrected exponent typography, and the
Fulman–Goldstein/Balakin distinction.  The manuscript and PDF were not edited
in this review.

## Finding ledger

| ID | Severity | Finding | Required disposition |
|---|---:|---|---|
| `P173-B-MAJ-01` | Major | Evans (2002) owns the dimension-chain precursor, and Van Peski (2018), Theorem 3.3.4 and (3.42)–(3.55), directly own the labelled uniform-kernel transition and fixed-target injection count in the square-codomain case.  Neither source appears in the local package. | Add exact primary metadata and theorem mapping; give the kernel/injection/labelled-chain architecture zero credit; state the rectangular fixed-ambient non-transfer boundary on every claim surface. |
| `P173-B-MAJ-02` | Major | P173 does not reciprocally name or subtract sibling P172, although P172 and the batch firewall explicitly identify their shared fresh-map erosion, quotient/labelling, triangular/Jordan, and absorption shell. | Add a P172 row and exact zero-credit/non-transfer language to the manuscript and all local ledgers; narrow the retained residual accordingly. |
| `P173-B-MIN-01` | Minor | The proof of Theorem 1(ii) conditions on “ending in dimension `b`,” including at `t=0`; for unreachable layers this conditioning event has probability zero. | Replace the conditional argument by an unconditional, measure-preserving conjugation bijection between the raw endpoint events. |

## 1. Independent derivation of the fibre law

Fix `B <= U <= V`, with `dim U=a`, `dim B=b`, and put `d=a-b`.  The update
depends only on

```text
rho_U : End(V) -> Hom(U,V/U),       T |-> pi_U T|_U.
```

This map is onto: choose any lift of a prescribed map on a basis of `U`, then
extend arbitrarily to a basis of `V`.  Its target has dimension `a(n-a)`, so
every leakage map has exactly

```text
q^(n^2-a(n-a))
```

ambient lifts.  Moreover,

```text
U intersect T^(-1)(U) = ker rho_U(T).
```

The kernel equals `B` precisely when the induced map

```text
U/B -> V/U
```

is injective.  Its domain has dimension `d`, its codomain dimension `n-a`,
and the number of injections is

```text
product_{i=0}^{d-1} (q^(n-a)-q^i)
```

when `d<=n-a`, and zero otherwise.  This proves both the ambient fibre

```text
q^(n^2-a(n-a)) C_{n,q}(a,b)
```

and the fixed-target probability

```text
C_{n,q}(a,b) / q^(a(n-a)).
```

The empty-product case `b=a` gives the diagonal.  A target outside `U` is
impossible by nestedness.  I find no missing lift factor or labelling
division.

## 2. Dimension quotient and every-time labelled targets

There are exactly `[a choose b]_q` labelled `b`-subspaces inside a fixed
`a`-space.  Summing the equal fixed-target probabilities therefore gives

```text
Q_ab = [a choose b]_q C_{n,q}(a,b) / q^(a(n-a)).
```

The rank distribution of a uniform map supplies the row-sum identity, and it
also follows directly by partitioning all leakage maps by their kernels.

For the all-time statement, the robust argument is unconditional.  Given
`B,B'<=U` with equal dimension, choose `g` in the stabilizer of `U` with
`gB=B'`.  Conjugation of a complete fresh-map history,

```text
(T_1,...,T_t) |-> (gT_1g^(-1),...,gT_tg^(-1)),
```

preserves its probability and carries every intermediate state to its
`g`-image.  It is consequently a bijection between the raw events
`{U_t=B}` and `{U_t=B'}`, including when both have probability zero.  Their
common probability sums over the `[a choose b]_q` possible targets to
`(Q^t)_ab`, proving

```text
P^t(U,B) = (Q^t)_ab / [a choose b]_q.
```

This derivation validates the theorem but also exposes `P173-B-MIN-01`: the
current proof phrases the same step as conditioning on an endpoint dimension
even when the conditioning event is null.

## 3. Full algebraic spectrum

Order labelled subspaces by nondecreasing dimension.  Every transition is to
a contained subspace, so the full transition matrix is triangular.  At an
`a`-space, remaining at that exact state is the event that the leakage map is
zero, hence

```text
P(U,U) = q^(-a(n-a)).
```

There are `[n choose a]_q` states in that layer.  The diagonal of a triangular
matrix is its algebraic eigenvalue multiset, so the manuscript's full
spectrum and multiplicities follow.  This argument does not determine the
full labelled Jordan form, and the manuscript correctly declines to assert
one.

## 4. Quotient Jordan inventory

Write `lambda_a=q^(-a(n-a))`.  Strict concavity and symmetry of `a(n-a)` show
that diagonal repetitions are exactly:

- the endpoints `0,n`;
- each complementary pair `b,n-b` with `1<=b<n/2`;
- no repetition at the positive even midpoint `n/2`.

For a complementary pair, put `a=n-b` and `lambda=lambda_b=lambda_a`.
Solve `(Q-lambda I)x=0` in increasing row order.  Rows below `b` force zero;
normalizing `x_b=1`, every intermediate coordinate satisfies

```text
x_k = (sum_{j<k} Q_kj x_j) / (lambda-Q_kk) > 0,
        b<k<a.
```

The denominator is positive by strict concavity.  The numerator stays
positive because every adjacent loss entry `Q_{k,k-1}` is positive.  At the
resonant row `a`, the compatibility sum is strictly positive—in particular
it contains `Q_{a,a-1}x_{a-1}`—so this lower birth cannot extend to an
eigenvector.  The eigenvector born at row `a` remains.  Algebraic
multiplicity two and geometric multiplicity one therefore give exactly one
`J_2(lambda)`.

At eigenvalue one and `n>=1`, the all-ones vector and the indicator of the
full-dimension state are independent right eigenvectors.  Thus the two
endpoint occurrences are two `J_1(1)` blocks.  At `n=0` the endpoints are the
same state and `Q=(1)`, so there is one `J_1(1)`.  A positive even midpoint is
simple.  These blocks exhaust all `n+1` quotient dimensions.

The subspace of functions constant on dimension layers is invariant under
the full chain.  The quotient `J_2` blocks therefore prove full-operator
nondiagonalizability, but not the rest of its Jordan multiplicities.  The
manuscript observes this boundary correctly.

## 5. Absorption and boundary cases

The quotient codomain is zero at `U=0` and at `U=V`, so both are fixed.  If
`0<a<n`, then

```text
Q_aa = q^(-a(n-a)) < 1
```

and `Q_{a,a-1}>0`.  A finite nested chain can never return after a strict
loss, and every proper positive layer has positive exit probability; it
therefore reaches zero almost surely.  The CDF is the unique zero-target
entry `(Q^t)_{a0}`, and first-step conditioning gives the displayed mean
recursion.

The small boundaries check separately:

- `n=0`: one subspace and one `J_1(1)`;
- `n=1`: only `0,V`, both fixed, and two endpoint `J_1(1)` blocks;
- `n=2`: the only transient dimension has
  `Q_10=(q-1)/q`, `Q_11=1/q`, and mean `q/(q-1)`.

No absorption or endpoint repair is required.

## 6. External owner stress test

The existing Fulman–Goldstein, Balakin, and Goldman–Rota records are
appropriately used after the Round-1 repair.  They do not, however, close the
nearest-chain search.

### 6.1 Exact primary records omitted from P173

1. **Steven N. Evans**, “Elementary divisors and determinants of random
   matrices over a local field,” *Stochastic Processes and their
   Applications* **102**(1) (November 2002), 89–102, DOI
   [`10.1016/S0304-4149(02)00187-4`](https://doi.org/10.1016/S0304-4149(02)00187-4).
   Primary records: [publisher page](https://www.sciencedirect.com/science/article/pii/S0304414902001874)
   and [Berkeley technical report 614](https://statistics.berkeley.edu/tech-reports/614).
   Theorem 3.5 gives the dimension Markov chain associated with the
   elementary-divisor filtration of a Haar random matrix over a local field.

2. **Roger Van Peski**, *Random Matrix Theory over Integers of Local Fields*,
   undergraduate thesis, Department of Mathematics, Princeton University,
   May 7, 2018, advisor Ju-Lee Kim,
   [primary author PDF](https://www.math.columbia.edu/~rv2549/Princeton_Thesis_D3-2.pdf).
   Theorem 3.3.4, equations (3.42)–(3.55), refines the filtration to labelled
   subspaces.  Conditional on `W_{r+1}<=W_r`, with dimensions `b<=a`, its
   proof realizes `W_{r+1}` as the kernel of a uniform map
   `W_r -> F_q^a` and obtains the fixed-target probability

   ```text
   [a choose b]_q |GL_{a-b}(F_q)| / |M_a(F_q)|
     = product_{i=0}^{a-b-1}(q^a-q^i) / q^(a^2).
   ```

   A further factor `[a choose b]_q` produces its dimension transition.
   Equations (3.52)–(3.54) explicitly identify the uniform kernel and count
   injections from `W_r/W_{r+1}`.  This is not merely a generic rank citation;
   it is a direct labelled-chain and fixed-target owner for the square-map
   version of the proof engine.

Evans supplies the earlier dimension-chain result; Van Peski supplies the
labelled subspace theorem and direct uniform-kernel derivation.  The review
does not attribute Van Peski's labelled refinement to Evans without evidence.

### 6.2 Mandatory zero-credit wording

The repaired package must state, in substance:

> Evans's elementary-divisor filtration owns the dimension-chain precursor,
> and Van Peski's Theorem 3.3.4 owns the descending labelled-subspace Markov
> architecture, its reduction to the kernel of a uniform square map, and the
> fixed labelled-kernel/injection count.  Those ingredients, Gaussian
> dimension lumping, and ordinary powering of that kernel receive zero
> contribution credit here.

It is also safer to assign the every-time uniform labelling division zero
credit: once the one-step labelled kernel is invariant under the stabilizer,
the power identity is standard Markov composition plus conjugation.

### 6.3 Exact non-transfer boundary

The cited chain is generated by the coefficient/elementary-divisor
filtration of **one** Haar matrix over the ring of integers of a local field.
At current dimension `a`, its proof produces a uniform **square** map
`W_r -> F_q^a`.  P173 instead resamples a fresh ambient element of `End(V)` at
each epoch and sees the rectangular leakage map

```text
U -> V/U,              dimensions a -> n-a,
```

inside one fixed `n`-dimensional ambient space.  At the middle layer `n=2a`,
Van Peski's fixed-target row is literally the same injection law; away from
that layer the codomain schedule differs, and after a loss the two chains do
not remain the same.

Neither source states P173's fixed-ambient rectangular matrix `Q`, the
diagonal symmetry `lambda_a=lambda_{n-a}`, the resulting complementary
`J_2` ladder, or the corresponding fixed-ambient absorption law.  The
elementary ambient extension factor is routine linear algebra and is already
zero credit, not a residual rescue.  Thus the owner finding forces
subtraction but does not presently transfer the complementary-codimension
spectral theorem wholesale.

### 6.4 Acceptance criteria for `P173-B-MAJ-01`

The finding closes only when all of the following are visible and consistent:

- `main.tex` cites both exact records at the first uniform-kernel reduction
  and again states their zero-credit/non-transfer role at the claim boundary;
- `references.bib` contains the exact Evans journal metadata and Van Peski
  thesis metadata/primary URL;
- `SOURCE_VERIFICATION.md` maps Evans Theorem 3.5 and Van Peski Theorem 3.3.4,
  (3.42)–(3.55), to the claims above without saying either source proves
  P173's rectangular complementary ladder;
- the owner log records at least the query families
  `p-adic elementary divisors subspace Markov chain kernel`,
  `filtered vector spaces random matrix kernel Markov chain`, and
  `cokernel partition labelled subspace chain`;
- `README.md`, `NARRATIVE_REPORT.md`, `PAPER_PLAN.md`,
  `CLAIMS_EVIDENCE.md`, and `SELF_QA.md` use the same subtraction and retain
  `SPIKE_2_COLLISION_RISK / HOLD_EXTERNAL`;
- no bounded search non-hit is presented as novelty or freedom-to-operate
  evidence.

## 7. Internal collision stress test

The Round-1 manuscript names P109, P162, P165, and P168, and its stated
non-transfer boundaries for those papers are reasonable.  It omits the
nearest same-batch comparator:

**P172, *Fresh-Map Self-Image Erosion: Labelled Kernels and a Forced Jordan
Block*.**  P172 updates a labelled subset by intersection with the image of a
fresh uniform endomap.  It explicitly subtracts P173 in its manuscript,
source ledger, and hostile-review closure.  The batch
`SYSTEM_COLLISION_FIREWALL.md` also has a dedicated P172-versus-P173 row.

The following shell is therefore already occupied and must receive zero
separation credit in P173:

- freshly resampled ambient maps;
- monotone nested erosion;
- a cardinality/dimension quotient with equal-probability labelled lift;
- every-time recovery from powers of the small quotient;
- triangular spectral extraction and a forced Jordan obstruction;
- standard finite-chain absorption formulas.

The non-transfer boundary is real but narrower.  P172 uses noninvertible
set-map image occupancy, Stirling/specified-box target fibres, an image-size
mark, and one terminal `J_2`.  P173 uses a linear quotient-kernel/injection
fibre, a fixed ambient rectangular codomain schedule `a -> n-a`, and a
complementary-dimension `J_2` ladder.  No coefficient substitution in P172's
occupancy matrix produces P173's `Q` or its full complementary resonance
inventory.

### Acceptance criteria for `P173-B-MAJ-02`

- Add an explicit P172 row to the internal subtraction in `main.tex` and
  `SOURCE_VERIFICATION.md`.
- Propagate the same row to `README.md`, `NARRATIVE_REPORT.md`,
  `PAPER_PLAN.md`, `CLAIMS_EVIDENCE.md`, and `SELF_QA.md`; do not rely solely
  on the batch firewall.
- State the shared shell above as zero credit and the set-occupancy versus
  quotient-injection non-transfer boundary explicitly.
- Narrow the retained residual from generic “fresh state-dependent quotient
  kernels/all-time labelled transition recovery” to the literal
  fixed-ambient **complementary-codimension schedule**, its resulting
  complementary Jordan ladder, and any other claim that remains after both
  P172 and Van Peski/Evans are deducted.
- Keep `SPIKE_2_COLLISION_RISK / HOLD_EXTERNAL`; the reciprocal subtraction
  is not an upgrade.

## 8. Minor proof repair

### `P173-B-MIN-01` — conditioning on a null layer

The current proof of Theorem 1(ii) says that, conditional on starting at `U`
and ending in dimension `b`, all endpoints are equally likely, and then says
this includes `t=0`.  At `t=0,b<a`, and at other unreachable time/loss pairs,
the conditioning event has probability zero and that conditional
distribution is undefined.

This is a proof-wording issue only.  Replace the conditional sentence by the
unconditional conjugation-of-histories bijection in Section 2 of this review.
Acceptance requires explicitly noting that the bijection proves equality of
raw endpoint probabilities even on zero-mass layers, after which division by
`[a choose b]_q` is legitimate.  No theorem statement or formula needs to
change.

## 9. Independent executable audit

The Review-B control lives at
`docs/papers172_176_sequence/reviews/p173_review_b/`.  It imports only the
Python standard library and imports no author, scout, or Review-A module.

Its literal representation is a bitset of normalized projective-point
incidences.  Each ambient matrix acts on projective points, and the update is
formed from that action.  This differs materially from complete vector-set
enumeration and from RREF/annihilator representations.

Coverage:

- complete literal enumeration for `q=2,n=0..4` through epoch 6;
- complete literal enumeration for `q=3,n=0..3` through epoch 5;
- all ambient matrices, all labelled sources and targets, all fibre counts,
  quotient rows, diagonals, and every-time labelled powers in those boxes;
- exact rational formula/Jordan/absorption checks for
  `q={2,3,4,5,7,8,9,11}`, `n=0..14`;
- 128 complementary pairs with a direct source-to-complement entry and 208
  pairs whose Jordan obstruction is mediated through intermediate layers;
- dedicated `n=0`, `n=1`, and `n=2` sentinels.

The largest literal box uses 67 labelled subspaces and all 65,536 endomorphisms
of `F_2^4`, for 4,390,912 source-map updates.  Canonical output is
byte-reproducible and terminates with:

```text
ASSERTIONS=9995101
RESULT=PASS_INTENDED_FORMULAS; MANUSCRIPT_BOUNDARY_AND_SOURCE_GATES_EXTERNAL
```

Artifact pins before manifest generation:

```text
916391331b0afa561e3faa26fda6b91ee0a26e5b58273c1db902efa8315f2e87  verify_review_b.py
8c699a45e97ca3462a2607f372760dbd7cb51f6c61515b4cd3a92bb0968fe607  CANONICAL.txt
```

Finite verification is counterexample pressure; it does not prove the
all-parameter theorem or settle source ownership.

## 10. Historical required repair sequence — completed in Round 2

1. Implement `P173-B-MAJ-01` with the exact primary records, theorem mapping,
   zero-credit language, non-transfer boundary, and owner-log queries.
2. Implement `P173-B-MAJ-02` reciprocally against P172 on every local claim
   surface and narrow the residual.
3. Replace the null-event conditional wording under `P173-B-MIN-01`.
4. Rebuild a deterministic next-round PDF while preserving the current
   Round-1 PDF; rerun both author and independent controls.
5. Submit the delta to Reviewer B for read-only closure.  Closure may yield
   `PASS / SPIKE_2_COLLISION_RISK / HOLD_EXTERNAL`, never an automatic green
   or external-release decision.

## 11. Initial-review boundary

This was an independent derivation, source audit, and independently
implemented executable control.  No external second-model verdict is claimed.
The manuscript, bibliography, source ledger, and PDFs were not changed.
Before all three findings closed, the only defensible disposition was:

```text
MAJOR_REPAIRS_REQUIRED / MATHEMATICS_SURVIVES
SPIKE_2_COLLISION_RISK / HOLD_EXTERNAL
```

The final delta acceptance at the top of this file supersedes that initial
repair verdict and leaves zero open findings without changing the external
hold.
