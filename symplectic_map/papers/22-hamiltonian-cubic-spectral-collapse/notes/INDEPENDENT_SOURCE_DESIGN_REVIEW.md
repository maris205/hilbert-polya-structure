# Paper 22 — Independent Source-Design Review

## Reviewer identity, scope, and independence

Review date: 2026-08-24 UTC.

I am a fresh independent source-design reviewer. I authored none of:

- `BATCH_06_STATUS.md`
- `BATCH_06_IDEA_REPORT.md`
- `BATCH_06_PAPER22_CANDIDATE_REVIEW_R1.md`
- `BATCH_06_PAPER22_CANDIDATE_REVIEW_R2.md`
- any file in the ten-file author package below

This is not a self-review.

Per the bounded source-design role, I used no network access, no CAS
certificate, no scientific experiment, no build, and no external action. I
read the four governing Batch-06 records, hashed and inventoried the exact ten
author files, read all ten to EOF, and independently recomputed the theorem-
critical identities and lifecycle boundaries required by the handoff.

## Governing bindings

- `BATCH_06_STATUS.md`
  - SHA-256:
    `05a20ac05572fd0b82686bca8bfa089405cec5665d5e39a31e0ed490d8c113db`
- `BATCH_06_IDEA_REPORT.md`
  - SHA-256:
    `89403d42cb30c43a9f0cca28cb2fcb8427e187145a2ad3ca0af10fbc15536e08`
- `BATCH_06_PAPER22_CANDIDATE_REVIEW_R1.md`
  - SHA-256:
    `8d6cb168b303563cfc3719e176ca9b677b060c91a2527d48f4b49488d827e268`
  - terminal line: `PAPER22_CANDIDATE_GATE_PASS_R1`
- `BATCH_06_PAPER22_CANDIDATE_REVIEW_R2.md`
  - SHA-256:
    `de7a20a707c5b8926802cb2b5f0db1fd355970a808e908884fa30bbe948b1349`
  - terminal line: `PAPER22_CANDIDATE_GATE_PASS_R2`

The R1/R2 hashes recorded in `refine-logs/REVIEW_SUMMARY.md` match the actual
candidate-review files exactly.

## Exact author package inventory

The author-reported aggregate at this stage is an exact ten-file regular-file
universe. The set reported in `refine-logs/REVIEW_SUMMARY.md` matches the
actual package exactly.

All ten paths are regular files, not symlinks. All ten are mode `0644`,
UTF-8, LF-only, contain no carriage returns, and end with a final LF byte
`0a`.

| Path | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `experiments/EXPERIMENT_PLAN.md` | 5812 | 146 | `914542c082f3bc65c47db822c6d7d3bceca8b55041117548b10b1cef96cc2873` |
| `experiments/EXPERIMENT_TRACKER.md` | 3318 | 63 | `07c147aaa323bb7d445d3fb669a9c75b896a006f53aed1d8f11e3e0637d35f4c` |
| `notes/CITATION_VERIFICATION.md` | 4916 | 65 | `d2b89b3313d54e612c3aa6e1e0a454c034d312268fd431217638417d90afa2bc` |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | 6915 | 94 | `b1184e0dffd4ccd633e9ced15c227e5bad3e9074627fd7442bd78896c1f48416` |
| `notes/NOVELTY_ASSESSMENT.md` | 7486 | 140 | `dbd33f68af27f0ba57982e5bb6f2dde8d01099188e2d240e0319199ee52b2699` |
| `notes/PROOF_PACKAGE.md` | 23639 | 951 | `2d290cbc316b42be8c978a527d9fa24751c992f532747067aeaf64d79eef6846` |
| `notes/RESEARCH_QUESTION.md` | 5266 | 138 | `fc2269c6abe58b077b1c0b33bf07f93661f59a2ca72733330b9d67c38cb63175` |
| `refine-logs/INITIAL_PROPOSAL.md` | 4052 | 124 | `1d23119b72630a34446a0a331e1f3be5bf8e8362385c88b63c7f568aa411097d` |
| `refine-logs/FINAL_PROPOSAL.md` | 5764 | 162 | `f58efbf336df21ab32296fc3c022be2200d4a0c7679e935652a405600c182679` |
| `refine-logs/REVIEW_SUMMARY.md` | 3234 | 80 | `96ee47f7cfa3f5324521335ebba6b6a21e009631fd0d668a3de7061dcf8a934d` |

Reviewer-computed aggregate over exactly these ten author files:

- file count: `10`
- total bytes: `70402`
- total LF: `1963`
- symlink count: `0`

## Package-consistency and permission audit

I found no package-membership drift. The ten files consistently describe the
same source-design-only stage:

- no manuscript, bibliography, source lock, paper plan, publication lock,
  build, PDF, code, dataset, figure, release object, upload, submission,
  external message, or Paper 23 authority;
- zero scientific runs, zero numerical orbits, zero CAS or symbolic runs, and
  zero author-side network actions;
- tracker items `A01`–`A20` remain planned and are not misrepresented as
  independently completed;
- the later article budget is consistently framed as a proof-first `24–28`
  content-page plan within the authorized `22–30` substantive-page window;
- Paper 20 and Paper 21 are consistently disclosed as direct predecessors, and
  Paper 22 is consistently framed as a separated successor whose new range
  begins at `r>=4`.

I found no unauthorized future artifact inside the ten-file author package.

## Independent mathematical recomputation

I recomputed the theorem-critical algebra independently and found the ten files
mutually consistent with the candidate-gate locks.

### 1. Gradients, inverses, and symplecticity

For

`V_{r,g}(q)=prod_i q_i^2 + q_1^g`

and

`W_{r,g}(p)=prod_i p_i^2 + p_r^g`,

the displayed gradients are correct:

- `∂V/∂q_1 = 2 q_1 prod_{j=2}^r q_j^2 + g q_1^{g-1}`
- `∂V/∂q_i = 2 q_i prod_{j!=i} q_j^2` for `2<=i<=r`
- `∂W/∂p_i = 2 p_i prod_{j!=i} p_j^2` for `1<=i<r`
- `∂W/∂p_r = 2 p_r prod_{j=1}^{r-1} p_j^2 + g p_r^{g-1}`

The subtraction inverses are correct, and the Jacobian blocks

`J_S = [[I,0],[H_V,I]]`, `J_T = [[I,H_W],[0,I]]`

preserve the standard symplectic form because both Hessians are symmetric.

### 2. Exact support rows and matrices `A`, `B`, `C`

The mixed support row in coordinate `i` is the `i`-th row of

`M_r = 2 11^T - I_r`,

with diagonal entry `1` and off-diagonal entries `2`. The only competitive
extra rows are `h e_1^T` in the first `V` row and `h e_r^T` in the last `W`
row, where `h=g-1`. Thus the only selector comparisons are exactly the two
claimed ones.

Recomputing `C=BA` gives:

- row `1`: `C_{11}=h+4m+4`, `C_{1j}=4m+2` for `2<=j<=r`
- middle rows `2<=i<r`:
  `C_{i1}=2h+4m+2`,
  `C_{ij}=4m+delta_{ij}` for `2<=j<=r`
- last row:
  `C_{rj}=2h` for `1<=j<r`, `C_{rr}=h`

with `m=r-2`. Therefore, for `x_i=u_i/u_1` and `sigma=sum_{i=2}^r x_i`,

- `(Cu)_1/u_1 = h+4m+4+(4m+2)sigma`
- `(Cu)_i/u_1 = 2h+4m+2+4m sigma + x_i` for `2<=i<r`
- `(Cu)_r/u_1 = h(2+2 sigma - x_r)`

These formulas agree across `PROOF_PACKAGE.md`, `FINAL_PROPOSAL.md`,
`CLAIMS_EVIDENCE_MATRIX.md`, `RESEARCH_QUESTION.md`, and the handoff summary.

### 3. Cone normalization and both selectors

The cone normalization is correctly locked as

- `x_i=u_i/u_1` for `2<=i<=r`
- `sigma=sum_{i=2}^r x_i`

and never includes `x_1`.

The first selector margin is exactly

`u_1(h-1-2 sigma)`,

so strictness follows from the cone height condition.

For the second phase, acting on `v=Au`, the pure-minus-mixed margin recomputes
to

`Delta_T/u_1 = (2h-4m)sigma - (h+1)x_r - 4m - 2`.

Using `x_r<=sigma-m`, this becomes

`>= (h-4m-1)sigma + m(h-3) - 2`,

and the two sign cases for `h-4m-1` produce the exact positive factors

- `((h+1)(h-2m-3))/2` when `h-4m-1<0`
- `(2m+1)(h-2m-3)` when `h-4m-1>=0`

so the second selector is strict on the full open cone, including the
threshold `h=2m+4`.

### 4. Seed and every invariant-cone wall

At the seed `u_0=1`, one has `sigma=m+1`, and

`m+1 < (2m+3)/2 <= (h-1)/2`,

so the seed lies strictly in the cone.

I independently checked the three wall calculations:

- middle lower wall:
  `(Cu)_i-(Cu)_1 = u_1(delta + x_i - 1) > 0`
  with `delta=h-1-2 sigma`
- last lower wall:
  after `x_r<=sigma-m`, the exact two cases reduce to the positive factors
  `((h+2)(h-2m-3))/2` and `2(m+1)(h-2m-3)`
- upper height wall:
  `H_2=(h-1)(Cu)_1 - 2 sum_{i=2}^r (Cu)_i`
  reduces to
  `(h-2m-3)(h+4m^2+4m+2) > 0`

At the least admissible parameter `g=2r+1`, equivalently `h=2m+4`, every
factor `h-2m-3` becomes exactly `1`, so there is no hidden equality on the
claimed threshold line.

### 5. Carried coordinates and leading forms

`C-I` is entrywise positive, and `A` has nonnegative nonzero rows. Hence:

- `Cu>u` for every positive `u`
- `A1 > 1` at the seed
- if `u_n>u_{n-1}`, then `Au_n > Au_{n-1}`
- `BAu_n-u_n=(C-I)u_n > 0`

This closes the phase-labelled carry induction:

- `v_{n+1}=Au_n`
- `u_{n+1}=Cu_n`

The leading-form argument is also correctly upgraded beyond the positive-
coefficient semiring. The package uses the integral-domain property of the
polynomial ring, so the selected highest homogeneous term survives without
assuming positive signs. This is the correct mechanism for the four-nonzero-
coefficient corollary.

### 6. Visibility, exact degree, and PF formula

`C-A` is entrywise positive, so every full-step `q`-degree dominates the
corresponding `p`-degree. For a middle index `i`,

`((Cu)_r-(Cu)_i)/u_1`

reduces to the two positive lower bounds

- `((h+2)(h-2m-3))/2`
- `(2m+1)(h-2m-3)`

according to the sign of `h-4m`. Therefore the last `q`-coordinate is strictly
visible only for full iterates `n>=1`.

This matches the exact source lock:

- strict global visibility is only for `n>=1`
- `deg(F^n)=e_r^T C^n 1` still holds at `n=0` because every coordinate degree
  initially equals `1`

Since `C` is positive, Perron–Frobenius yields

`lambda_1(F)=rho(C)`.

### 7. Invariant unit space, quotient, cubic, and multiplicity

For

`U={z: z_1=z_r=0, sum_{i=2}^{r-1} z_i = 0}`,

there are `m` middle coordinates and one linear relation, so

`dim U = m-1 = r-3`.

Because every `z in U` has total sum zero and zero endpoints,

- `Az=-z`
- `Bz=-z`
- `Cz=z`

For the equal-middle complement

`E={(a,b,...,b,c)^T}`,

the package's coordinate convention is consistent throughout. Recomputing the
restrictions gives

`A_E = [[h,0,0],[2,2m-1,2],[2,2m,1]]`

and

`B_E = [[1,2m,2],[2,2m-1,2],[0,0,h]]`,

so

`Q=B_E A_E`

is exactly

`[[h+4m+4, 2m(2m+1), 2(2m+1)], [2h+4m+2, 4m^2+1, 4m], [2h, 2mh, h]]`.

The principal invariants recompute to:

- `tr(Q)=2h+4m^2+4m+5`
- sum of principal `2x2` minors:
  `h^2-8hm(m+1)+2h+4`
- `det(Q)=h^2(2m+1)^2`

Hence

`P_{m,h}(t)=t^3-(2h+4m^2+4m+5)t^2+(h^2-8hm(m+1)+2h+4)t-h^2(2m+1)^2`

and

`chi_C(t)=(t-1)^(r-3) P_{m,h}(t)`.

Substitution at `t=1` gives exactly

`P_{m,h}(1)=-4m(m+1)(h+1)^2 != 0`,

so the eigenvalue `1` has exact algebraic and geometric multiplicity `r-3`.
The exact degree sequence therefore has the displayed cubic annihilator, with
no unsupported claim of universal irreducibility or universal minimality.

### 8. Boundary `g=2r`, predecessor reduction `r=3`, and coefficient lock

At the seed, the first pure-minus-mixed score is exactly `g-2r`. Thus:

- at `g=2r`, the first selector ties;
- simultaneously,
  `sigma(1)=r-1=(g-2)/2`,
  so the seed lies on the open cone boundary;
- at `g=2r+1`, the selector gap is `1` and the height slack is `1/2`.

This proves sharpness only for the stated seed and selected face, exactly as
the source claims.

Setting formally `r=3`, so `m=1` and `h=g-1`, the quotient matrix becomes

`[[g+7,6,6],[2g+4,5,4],[2(g-1),2(g-1),g-1]]`

and the cubic becomes

`t^3-(2g+11)t^2+(g^2-16g+19)t-9(g-1)^2`,

which matches the Paper 21 predecessor object exactly. The ten-file package
uses this only as predecessor consistency and does not relabel it as a new
Paper-22 theorem.

For the coefficient corollary, the package correctly restricts the extension
to the four nonzero coefficients on the fixed two supports:

- `alpha prod q_i^2 + beta q_1^g`
- `gamma prod p_i^2 + delta p_r^g`

with `alpha beta gamma delta != 0`.

No broader arbitrary-support or positive-characteristic statement is made.

## Citation, collision, and successor audit

The source-design package stays within the candidate-review citation boundary:

- `notes/CITATION_VERIFICATION.md` binds only contextual primary or
  authoritative records already checked in candidate R1;
- no theorem-critical step is outsourced to a citation;
- no firstness or global priority claim is made.

The internal collision story is also coherent:

- Papers 12–19 are consistently separated by object type;
- Paper 20 is consistently the rank-two direct predecessor;
- Paper 21 is consistently the rank-three direct predecessor and exact base
  case;
- the new Paper-22 contribution is consistently the `r>=4` stable
  `(r-3)`-dimensional identity space plus three-dimensional spectral collapse.

I found no hidden Paper-20/21 overlap, no silent Paper-21 correction claim,
and no inconsistent successor/consolidation wording.

## Verdict

I found no blocker in:

- inventory identity;
- regular-file / non-symlink status;
- mode / encoding / line-ending checks;
- candidate-review bindings;
- theorem statement and anti-claims;
- selector, cone-wall, carry, leading-form, visibility, quotient, cubic, or
  multiplicity algebra;
- `g=2r` and `r=3` boundary handling;
- coefficient and characteristic-zero limits;
- Papers 12–21 collision disclosure;
- citation-role discipline;
- 22–30 page feasibility; or
- permission firewall.

The source-design package is internally consistent, mathematically closed at
the stated source-design level, and properly bounded as a proof-first,
source-design-only Paper-22 artifact.

SOURCE_DESIGN_PASS
