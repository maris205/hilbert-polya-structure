# Paper 22 — Independent Source-Lock Review

## Reviewer identity, scope, and independence

Review date: 2026-08-24 UTC.

I am a fresh independent source-lock reviewer. I authored none of:

- the ten-file Paper 22 source-design author package;
- `papers/22-hamiltonian-cubic-spectral-collapse/notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md`;
- `BATCH_06_PAPER22_CANDIDATE_REVIEW_R1.md`; or
- `BATCH_06_PAPER22_CANDIDATE_REVIEW_R2.md`.

I used no network access, no CAS, no symbolic package, no scientific run, no
build, no TeX/Bib/PDF workflow, no manuscript action, no Paper 23 action, and
no external effect. I read to EOF the ten author files, the independent
source-design review, the two immutable candidate reviews, the lock itself, the
relevant Batch 06 status/idea permissions, and the Paper 21 source-lock/review
schema used only as a structural reference.

## Lock identity and two-pass canonical JSON audit

Target lock:

- `papers/22-hamiltonian-cubic-spectral-collapse/experiments/source_lock.json`
- bytes `32258`
- LF count `1`
- SHA-256
  `6f79231121f78e1c6b55da148c5710c2005e0ae36f92b0771740d127a253ad88`

Pass 1 used a strict UTF-8 byte audit plus duplicate-key-rejecting,
nonfinite-rejecting JSON parse. Pass 2 used an independent recursive-descent
JSON parser and serializer. Both passes agreed on every lock-critical fact:

- valid UTF-8, no BOM, no CR, no NUL;
- exactly one physical JSON line;
- exactly one terminal LF byte;
- duplicate keys rejected;
- NaN/Infinity/-Infinity absent;
- recursive Unicode code-point key order satisfied;
- compact separators satisfied;
- byte-exact canonical round trip satisfied.

The body before the terminal LF reserializes to exactly `32257` bytes in both
passes, and appending one LF reproduces the locked `32258`-byte file exactly.

Self-identity exclusion is correct:

- `self_identity_exclusion.bytes = null`
- `self_identity_exclusion.sha256 = null`

The expected future reviewer artifact is also correctly self-excluded at author
stop:

- `artifact_bytes = null`
- `artifact_lf = null`
- `artifact_sha256 = null`

## Bound ten-file author package

All ten bound author files are regular files, not symlinks. All ten are mode
`0644`, UTF-8, LF-only, BOM-free, CR-free, NUL-free, and terminate with a
single final LF.

| Path | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `experiments/EXPERIMENT_PLAN.md` | 5812 | 146 | `914542c082f3bc65c47db822c6d7d3bceca8b55041117548b10b1cef96cc2873` |
| `experiments/EXPERIMENT_TRACKER.md` | 3318 | 63 | `07c147aaa323bb7d445d3fb669a9c75b896a006f53aed1d8f11e3e0637d35f4c` |
| `notes/CITATION_VERIFICATION.md` | 4916 | 65 | `d2b89b3313d54e612c3aa6e1e0a454c034d312268fd431217638417d90afa2bc` |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | 6915 | 94 | `b1184e0dffd4ccd633e9ced15c227e5bad3e9074627fd7442bd78896c1f48416` |
| `notes/NOVELTY_ASSESSMENT.md` | 7486 | 140 | `dbd33f68af27f0ba57982e5bb6f2dde8d01099188e2d240e0319199ee52b2699` |
| `notes/PROOF_PACKAGE.md` | 23639 | 951 | `2d290cbc316b42be8c978a527d9fa24751c992f532747067aeaf64d79eef6846` |
| `notes/RESEARCH_QUESTION.md` | 5266 | 138 | `fc2269c6abe58b077b1c0b33bf07f93661f59a2ca72733330b9d67c38cb63175` |
| `refine-logs/FINAL_PROPOSAL.md` | 5764 | 162 | `f58efbf336df21ab32296fc3c022be2200d4a0c7679e935652a405600c182679` |
| `refine-logs/INITIAL_PROPOSAL.md` | 4052 | 124 | `1d23119b72630a34446a0a331e1f3be5bf8e8362385c88b63c7f568aa411097d` |
| `refine-logs/REVIEW_SUMMARY.md` | 3234 | 80 | `96ee47f7cfa3f5324521335ebba6b6a21e009631fd0d668a3de7061dcf8a934d` |

Aggregate recomputation, done twice independently:

- author file count `10`
- content bytes `70402`
- total LF `1963`
- framed bytes `70850`
- framed SHA-256
  `c4bef57da2a64bb0bd479b3dba1b5c55154e40d96d4b9ffd7cb5103f7fd6e906`
- sorted-text ledger bytes `1035`
- sorted-text ledger SHA-256
  `da31e04936835b915fdfd3b350138b3fb904815bf1d81b8a20f653094c41967e`

The auxiliary sorted-text ledger that reproduces the locked digest is the
byte-sorted UTF-8 stream of lines

`SHA256<space>bytes<space>lf-count<space>relative-path<LF>`.

## Excluded review/provenance identities

Excluded source-design review identity matches the lock exactly:

- `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md`
- bytes `12590`
- LF `390`
- SHA-256 `a8dd5800afbf1b950453bd8fef7538b8c4a97e8a971d4db5e0c4705aa9917e56`
- terminal line `SOURCE_DESIGN_PASS`

Excluded immutable candidate provenance also matches exactly:

- `BATCH_06_PAPER22_CANDIDATE_REVIEW_R1.md`
  - bytes `22934`
  - LF `570`
  - SHA-256
    `8d6cb168b303563cfc3719e176ca9b677b060c91a2527d48f4b49488d827e268`
  - terminal line `PAPER22_CANDIDATE_GATE_PASS_R1`
- `BATCH_06_PAPER22_CANDIDATE_REVIEW_R2.md`
  - bytes `18787`
  - LF `669`
  - SHA-256
    `de7a20a707c5b8926802cb2b5f0db1fd355970a808e908884fa30bbe948b1349`
  - terminal line `PAPER22_CANDIDATE_GATE_PASS_R2`

The hashes recorded in `refine-logs/REVIEW_SUMMARY.md` and in the lock match
the actual root candidate-review files exactly.

## Exact inventory and forbidden absences

I independently recomputed the project-root inventory. The actual universe at
review time is exactly:

- regular files `12`
- directories `3`
- symlinks `0`

Regular files:

- `experiments/EXPERIMENT_PLAN.md`
- `experiments/EXPERIMENT_TRACKER.md`
- `experiments/source_lock.json`
- `notes/CITATION_VERIFICATION.md`
- `notes/CLAIMS_EVIDENCE_MATRIX.md`
- `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md`
- `notes/NOVELTY_ASSESSMENT.md`
- `notes/PROOF_PACKAGE.md`
- `notes/RESEARCH_QUESTION.md`
- `refine-logs/FINAL_PROPOSAL.md`
- `refine-logs/INITIAL_PROPOSAL.md`
- `refine-logs/REVIEW_SUMMARY.md`

Directories:

- `experiments`
- `notes`
- `refine-logs`

Forbidden absences all hold:

- no `build/`, `code/`, `data/`, `figures/`, `manuscript/`, `paper/`,
  `publication/`, `release/`, `results/`, `submission/`, or `transport/`;
- no TeX, BibTeX, PDF, compiled, transport, upload, release, submission, or
  external-action artifact inside the Paper 22 tree;
- no pre-existing
  `papers/22-hamiltonian-cubic-spectral-collapse/notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md`
  before this review write.

This matches the lock’s exact `12` regular files / `3` directories / `0`
symlink inventory and preserves the exclusion of the current reviewer artifact
from the author aggregate.

## Independent mathematical replay

I rederived the theorem-critical algebra independently from the displayed
family and checked it against `notes/PROOF_PACKAGE.md` and the lock.

### 1. Gradients, inverses, and symplecticity

For

- `V(q)=prod_{i=1}^r q_i^2 + q_1^g`
- `W(p)=prod_{i=1}^r p_i^2 + p_r^g`

the gradients are exactly

- `∂V/∂q_1 = 2 q_1 prod_{j=2}^r q_j^2 + g q_1^{g-1}`
- `∂V/∂q_i = 2 q_i prod_{j!=i} q_j^2` for `2<=i<=r`
- `∂W/∂p_i = 2 p_i prod_{j!=i} p_j^2` for `1<=i<r`
- `∂W/∂p_r = 2 p_r prod_{j=1}^{r-1} p_j^2 + g p_r^{g-1}`

The subtraction inverses are

- `S^{-1}(q,p)=(q,p-∇V(q))`
- `T^{-1}(q,p)=(q-∇W(p),p)`

and the Jacobian blocks

- `J_S=[[I,0],[H_V,I]]`
- `J_T=[[I,H_W],[0,I]]`

preserve the standard symplectic form because `H_V` and `H_W` are symmetric.

### 2. Exact support rows and matrices

With `M=2*1*1^T-I_r`, `h=g-1`, and `m=r-2`, the only competitive rows are the
first `V` row `h e_1^T` and the last `W` row `h e_r^T`; every other gradient
row is the corresponding row of `M`.

Thus:

- `A` is `M` with row `1` replaced by `h e_1^T`
- `B` is `M` with row `r` replaced by `h e_r^T`
- `C=BA`

The recomputed complete-step matrix entries are exactly:

- first row: `C_11=h+4m+4`, `C_1j=4m+2` for `2<=j<=r`
- middle rows `2<=i<r`:
  `C_i1=2h+4m+2`, `C_ij=4m+δ_ij` for `2<=j<=r`
- last row: `C_rj=2h` for `1<=j<r`, `C_rr=h`

For `x_i=u_i/u_1` (`2<=i<=r`) and `sigma=sum_{i=2}^r x_i`, this yields:

- `(Cu)_1/u_1 = h+4m+4+(4m+2)sigma`
- `(Cu)_i/u_1 = 2h+4m+2+4m sigma + x_i` for `2<=i<r`
- `(Cu)_r/u_1 = h(2+2 sigma - x_r)`

The sigma convention is correctly locked with `x_1` excluded.

### 3. Both strict selectors and the invariant cone

The explicit sufficient selector cone is

`K={u>0 : x_i>=1 (2<=i<=r), sigma<(h-1)/2}`.

The first selector margin is exactly

`h u_1 - (u_1 + 2 sum_{i=2}^r u_i) = u_1(h-1-2 sigma)`,

so the first phase is strict on the open height face.

For the second phase, with `v=Au`,

- `v_1/u_1 = h`
- `v_i/u_1 = 2+2 sigma - x_i` for `2<=i<=r`

and the pure-minus-mixed margin is exactly

`Delta_T/u_1 = (2h-4m) sigma - (h+1) x_r - 4m - 2`.

Using `x_r<=sigma-m`, this becomes

`>= (h-4m-1) sigma + m(h-3) - 2`.

The two sign cases give the exact positive lower bounds

- `((h+1)(h-2m-3))/2` when `h-4m-1<0`
- `(2m+1)(h-2m-3)` when `h-4m-1>=0`

so the second selector is strict on the full stated cone, including the least
parameter `h=2m+4`.

### 4. Seed and every cone wall

At the seed `u_0=1`,

- `sigma(u_0)=m+1`
- `m+1 < (2m+3)/2 <= (h-1)/2`

so the seed lies strictly inside the cone.

I rederived all three strict wall inequalities:

- middle lower walls:
  `((Cu)_i-(Cu)_1)/u_1 = (h-1-2 sigma) + (x_i-1) > 0`
- last lower wall:
  `((Cu)_r-(Cu)_1)/u_1`
  has the exact positive lower bounds
  `((h+2)(h-2m-3))/2` or `2(m+1)(h-2m-3)`
- height wall:
  `H_2=(h-1)(Cu)_1 - 2 sum_{i=2}^r (Cu)_i`
  satisfies
  `H_2/u_1 >= (h-2m-3)(h+4m^2+4m+2) > 0`

At the least allowed threshold `h=2m+4`, every decisive factor
`h-2m-3` equals `1`; no hidden equality remains.

### 5. Carried coordinates and leading forms

I rechecked both carry phases:

- `C-I` is entrywise positive, so `Cu>u` for every positive `u`
- `A*1 > 1`
- every row of `A` is nonnegative and nonzero, so `u_n>u_{n-1}` implies
  `Au_n>Au_{n-1}`
- `BAu_n-u_n = (C-I)u_n > 0`

Hence the phase-labelled recurrence is exactly

- `v_{n+1}=Au_n`
- `u_{n+1}=Cu_n`

The noncancellation step is correctly done in the polynomial domain:

- `LH(fg)=LH(f)LH(g)!=0`
- strict degree uniqueness prevents cancellation by lower-degree summands

This is the right mechanism for the coefficient corollary with

- `alpha prod q_i^2 + beta q_1^g`
- `gamma prod p_i^2 + delta p_r^g`
- `alpha,beta,gamma,delta in K^x`

because the derivative scalars `2alpha`, `g beta`, `2 gamma`, and `g delta`
remain nonzero in characteristic zero and the supports do not change.

### 6. Visibility and exact degree identity

I independently verified that `C-A` is entrywise positive. Therefore every
full-step `q`-degree strictly exceeds its corresponding intermediate
`p`-degree.

For the last coordinate:

- `q_r-q_1` is exactly the strict last-lower-wall quantity above
- for each `2<=i<r`,
  `((Cu)_r-(Cu)_i)/u_1`
  has the exact positive lower bounds
  `((h+2)(h-2m-3))/2` or `(2m+1)(h-2m-3)`

Thus the last `q`-coordinate strictly dominates all other `q` and `p`
coordinates for `n>=1`, and only for `n>=1`. The tied initial case at `n=0`
is correctly disclosed.

Therefore the exact degree identity is

- `deg(F^n)=e_r^T C^n 1` for `n>=0`

with strict global visibility only for `n>=1`.

Since `C` is positive and both the seed `1` and the observable `e_r^T` see the
Perron direction, the first dynamical degree identity

- `lambda_1(F)=rho(C)`

is valid exactly as locked.

### 7. The unit space, equal-middle quotient, cubic, and exact multiplicity

For

`U={z : z_1=z_r=0, sum_{i=2}^{r-1} z_i = 0}`,

there are `m` middle coordinates and one relation, so

- `dim U = m-1 = r-3`

and the mixed matrix satisfies `Mz=-z`. Since the modified endpoint rows still
vanish on `U`,

- `A|_U = -I`
- `B|_U = -I`
- `C|_U = I`

For the equal-middle complement

`E={(a,b,...,b,c)^T}`,

characteristic zero makes `U ∩ E = {0}` and hence `K^r = U ⊕ E`.

In the locked coordinate convention `(a,b,c) -> (a,b,...,b,c)`, the exact
restrictions are

- `A_E = [[h,0,0],[2,2m-1,2],[2,2m,1]]`
- `B_E = [[1,2m,2],[2,2m-1,2],[0,0,h]]`

and therefore

`Q=B_E A_E = [[h+4m+4,2m(2m+1),2(2m+1)],[2h+4m+2,4m^2+1,4m],[2h,2mh,h]]`.

The recomputed invariants are:

- `tr(Q)=2h+4m^2+4m+5`
- principal-minor sum `= h^2-8hm(m+1)+2h+4`
- `det(Q)=h^2(2m+1)^2`

Hence

`P_{m,h}(t)=t^3-(2h+4m^2+4m+5)t^2+(h^2-8hm(m+1)+2h+4)t-h^2(2m+1)^2`

and

`chi_C(t)=(t-1)^(r-3) P_{m,h}(t)`.

At `t=1`,

`P_{m,h}(1)=-4m(m+1)(h+1)^2 != 0`,

so the quotient has no eigenvalue `1`. Therefore the eigenvalue `1` has exact
algebraic and geometric multiplicity `r-3`, with no hidden quotient eigenvalue
and no hidden unit Jordan block.

Because `1 in E`, the exact degree sequence obeys the cubic annihilator

`d_{n+3}=T_0 d_{n+2}-S_0 d_{n+1}+D_0 d_n`,

where

- `T_0=2h+4m^2+4m+5`
- `S_0=h^2-8hm(m+1)+2h+4`
- `D_0=h^2(2m+1)^2`
- `d_0=1`
- `d_1=h(2m+3)`

This is an annihilator only; the lock correctly does not promote it to a
universal irreducibility or minimality claim.

### 8. Boundary `g=2r`, Paper 21 reduction, and bounded coefficient scope

At the seed, the first pure-minus-mixed score is exactly

`g-2r`.

Thus:

- at `g=2r`, the first selector ties exactly;
- simultaneously `sigma(1)=r-1=(g-2)/2`, so the seed lies on the open height
  boundary;
- at `g=2r+1`, the selector gap is `1` and the height slack is `1/2`.

This is correctly locked only as seed/selected-face sharpness, not as a global
failure theorem.

Under the formal Paper 21 specialization `r=3` (`m=1`, `h=g-1`), I recovered
exactly

- `Q=[[g+7,6,6],[2g+4,5,4],[2(g-1),2(g-1),g-1]]`
- `t^3-(2g+11)t^2+(g^2-16g+19)t-9(g-1)^2`

matching the Paper 21 predecessor object exactly. The lock correctly treats
this only as predecessor consistency and not as a new Paper 22 theorem.

## Citation, collision, anti-claim, zero-science, and lifecycle audit

The citation boundary is closed correctly:

- `primary_source_count = 6`
- sources `S01`–`S06` are bound only for contextual use
- no citation is used as proof of any selector, carry, visibility, quotient,
  cubic, threshold, or coefficient statement
- no firstness, classification, or priority claim is authorized

The internal collision ledger is also consistent:

- Papers `12`–`19` remain bounded noncollisions by object type
- Paper `20` is the direct owned rank-two predecessor
- Paper `21` is the direct owned rank-three predecessor and exact base case
- the new delta is the `r>=4` stable `(r-3)`-dimensional unit space plus the
  fixed three-dimensional quotient carrying the Perron class

The anti-claim and STOP-rule firewall remains intact: no maximal cone, no
arbitrary-support generalization, no universal cubic minimality or
irreducibility, no rank-three novelty claim, no global threshold theorem, no
positive-characteristic claim, no entropy/genericity/classification claim, and
no external-effect authority.

The zero-science counters remain closed exactly as locked:

- `scientific_runs = 0`
- `numerical_runs = 0`
- `cas_runs = 0`
- `datasets = 0`
- `figures = 0`
- `scientific_network_calls = 0`
- `external_uploads = 0`
- `results_authorized = false`
- `experiments_authorized = false`

The live permission/lifecycle boundary is also correct:

- sole authorized reviewer write path:
  `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md`
- `source_lock_authorized = false`
- `source_lock_review_authorized = true`
- `paper_plan_authorized = false`
- `manuscript_authorized = false`
- `bibliography_authorized = false`
- `build_authorized = false`
- `publication_authorized = false`
- `release_authorized = false`
- `paper23_authorized = false`
- all external-effect flags remain false

Read together, `BATCH_06_IDEA_REPORT.md`, `BATCH_06_STATUS.md`, and the lock
all keep the next downstream step bounded to a fresh source-lock review/pass
only; no later paper-plan, manuscript, build, release, Paper 23, or external
authority opens here.

## Verdict

I found no blocker in:

- raw-byte lock identity;
- duplicate/nonfinite/canonical JSON rules;
- self-null identity exclusion;
- ten-file identities, aggregate, and auxiliary ledger;
- excluded design-review and candidate-review provenance;
- exact `12` regular files / `3` directories / `0` symlink inventory;
- forbidden-path absences;
- gradients, selectors, seed, every cone wall, carry induction, and
  noncancellation;
- `n>=1` visibility, the tied `n=0` case, and the exact degree identity;
- `U`, `E`, `Q`, `P_{m,h}`, `P(1)`, exact unit multiplicity, and the cubic
  recurrence;
- the `g=2r` seed-face boundary;
- the `r=3` Paper 21 reduction;
- the four-nonzero-coefficient fixed-support corollary;
- citation-role discipline;
- Papers `12`–`21` collision handling;
- anti-claims, zero-science counters, permissions, and lifecycle closure.

The source lock is internally consistent, byte-exactly canonical, and
mathematically aligned with the frozen proof package under the stated bounded
scope. The sole permitted review artifact is therefore justified.

SOURCE_LOCK_PASS
