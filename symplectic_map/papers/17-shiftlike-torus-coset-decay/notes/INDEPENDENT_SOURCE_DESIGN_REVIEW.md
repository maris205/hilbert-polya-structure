# Independent Source-Design Review

## Review identity, authority, and verdict

This is the separately authorized independent source-design review of
**Sharp Torus-Coset Decay for Sparse Shift-Like Recurrences: Constant Anchors
and the Exact Zero-Constant Boundary**.

The review was conducted after the explicit `SOURCE DESIGN AUTHOR STOP` on
2026-08-17. Before that stop, the Paper17 root was not opened, listed, or
statted. After the stop, the ten author files were hashed before opening, read
to EOF, independently rehashed before this review was created, and audited
against the two Batch05 control files, the authorized terminal Paper16
artifacts, the applicable review/proof instructions, and a bounded
primary-source search.

**Independent verdict: GO.** The decision is conjunctive. The corrected Part A
and Part B theorems close; Laurent's exact qualitative role and the
finite-rank/division-group bridge close; the geometric and arithmetic
quantifiers remain separated; the Paper16 overlap is properly deducted; all
fifteen anti-claims are preserved; and about 22 substantive pages are
credible without padding.

This review authorizes no manuscript, computation, experiment, source lock,
build, submission, or expansion beyond the reviewed theorem package.

## Frozen source integrity

The author-stop manifest contained exactly ten regular UTF-8/LF files in
exactly three directories. The declared total, independently recomputed, is
`109602` bytes and `2525` LF characters. No carriage returns, symlinks, or
additional pre-review paths were present.

| Path | Bytes | LF | SHA-256 | Result |
|---|---:|---:|---|---|
| `experiments/EXPERIMENT_PLAN.md` | 6234 | 140 | `6d3c765e8d9991ccaccbde358fa4c8119003c27201645ac08654d173a1d470f8` | MATCH |
| `experiments/EXPERIMENT_TRACKER.md` | 2465 | 59 | `ef600f790719a402b294bb06229463a62450653f1f662ff635ebcd9ca82d9206` | MATCH |
| `notes/CITATION_VERIFICATION.md` | 10066 | 173 | `28e6bc4d461a876e326c08e2a2481fd9f3b30ea3192ddc6c576185e88f317ddf` | MATCH |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | 10963 | 83 | `becba75688dc6e77c18a301f37daa34a17328cf54968f3707a6b76ad1774fea9` | MATCH |
| `notes/NOVELTY_ASSESSMENT.md` | 10258 | 200 | `d67777768a84199c48170a8eada1c61af10652c81e080c7c341b90629b2c5e29` | MATCH |
| `notes/PROOF_PACKAGE.md` | 30089 | 852 | `a5649bdc97d6853ddfe2716dc5531cf3d4a581fd9e55b4296c9cfe6ccadbcc77` | MATCH |
| `notes/RESEARCH_QUESTION.md` | 13539 | 368 | `894259da46aa6e886af06741c8798503c5d7e8229295a1c76a8f53e399bdc82f` | MATCH |
| `refine-logs/FINAL_PROPOSAL.md` | 8233 | 257 | `f91e41b0af9bf2ede85516f4362ae3880015b16080326d788e268d359c718bc4` | MATCH |
| `refine-logs/INITIAL_PROPOSAL.md` | 6920 | 185 | `7cbf74c1db067b58184055dba18ff3fd0d467141bb3868005715612d108edf14` | MATCH |
| `refine-logs/REVIEW_SUMMARY.md` | 10835 | 208 | `af07dea511210fa75f48db5d580106fd25d7984c3262d9a1f279b5baeab51aa9` | MATCH |

All ten files were read to EOF. The second hash pass immediately before this
review was identical to the first. This review is the sole authorized new
file and does not modify an author file.

## Corrected theorem package reviewed

Let `Omega` be algebraically closed of characteristic zero. Fix `k>=2`,
`1<=nu<=k-1`, and `a!=0`, and put

`S(z_1,...,z_k)=(z_2,...,z_k,P(z_{k-nu+1})+a z_1)`.

The zero-based scalar recurrence is

`x_{n+k}=P(x_{n+k-nu})+a x_n`.

For `m>=0`, `V_m` is the closed subvariety of `G_m^(k+m)` cut out by the
equations indexed `0<=n<m`. For a characteristic-zero field `K` and a
finite-rank subgroup `Gamma<=K*`,

`T_m(S,Gamma)={z in Gamma^k:S^j(z) in Gamma^k for 0<=j<=m}`.

Projection to the first `k` scalar coordinates identifies
`V_m intersect Gamma^(k+m)` with `T_m`. Thus `m` counts transitions, not
states.

### Part A

Suppose

`P(X)=c+sum_(j=1)^s b_j X^(e_j)`

in collected form, with `0<e_1<...<e_s`, all `a,c,b_j` nonzero, and actual
nonconstant support `s>=2`. For every `0<=m<=k` and every connected torus
translate `xi H subset V_m`,

`dim H<=k-m`.

There is no gcd hypothesis. If `a=1` and `P(1)=0`, equality is attained for
every `m` by the saturated connected subtorus obtained from

`R_m={n-nu mod k:0<=n<m}`,

fixing `x_r=1` for `r in R_m` and copying `x_(k+n)=x_n`. This condition is
sufficient, not necessary.

Consequently `T_k(S,Gamma)` is finite for every finite-rank `Gamma`, including
groups with infinite torsion, over every characteristic-zero field. For each
prescribed exponent support and each `k,nu`, separately chosen rational
coefficients and `Gamma=<2>` give infinite `T_(k-1)`. This sharpness is an
existence statement about compatible coefficients and a compatible group.

### Part B

Fix `k=2`, `nu=1`, and `c=0`, and write

`P(X)=sum_(e in E) b_e X^e`

with finite nonempty actual support `E subset Z_(>=1)`.

1. If `E={1}` and `P=beta X`, every finite `V_m^0` contains the
   one-dimensional coset
   `{(t,rt,...,r^(m+1)t):t in G_m}` for any nonzero root
   `r^2=beta r+a`. This is the only no-finite-geometric-window support class.
2. If `E={1,d}`, `d>=2`, and `P=beta X+delta X^d`, then `V_2^0` contains a
   positive-dimensional connected torus translate if and only if
   `a=-beta^2`. On that locus the unique such geometric subset is

   `C_d={((delta/beta^2)t^d,t,beta t,delta beta^d t^d):t in G_m}`.

   For all coefficients, including resonance, `V_3^0` contains no
   positive-dimensional torus translate.
3. Every other nonlinear actual support has no positive-dimensional torus
   translate in `V_2^0`. This includes nonlinear monomials, binomials with
   lower exponent at least two, and supports of size at least three.

Thus off the unique nonlinear resonance `T_2` is finite for every finite-rank
`Gamma`; on the resonance `T_3` is finite for every such `Gamma`. The existence
of `C_d` does not imply infinite intersection with every fixed `Gamma`.
Infinitude is shown only by the separate compatible example
`beta=delta=1`, `a=-1`, `Gamma=<2>`.

## Independent scheme and setup audit

| Gate | Independent finding | Result |
|---|---|---|
| Map orientation | The displayed inverse recovers `z_1` from `w_k-P(w_(k-nu))`; the scalar recurrence uses the same one-based/zero-based conversion. | PASS |
| Window semantics | The `m` equations introduce exactly `x_k,...,x_(k+m-1)`; states run from time `0` through `m`. | PASS |
| Closed-subvariety semantics | Each equation is Laurent-polynomial on the ambient torus, hence defines a closed subscheme there. | PASS |
| Reduced/integral structure | Successively eliminating the monic future variables identifies the coordinate ring with an iterated localization of the initial Laurent-polynomial ring. Hence `V_m` is integral, and the use of “subvariety” is legitimate. | PASS |
| Base change | The equations, character restrictions, and coset containments commute with extension to an algebraic closure. | PASS |
| Coset restriction | Pullback along `xi H -> G_m^(k+m)` sends each ambient coordinate to a nonzero scalar times a character, so the group-algebra identities are scheme-valid. | PASS |
| Connected/disconnected scope | Passing from a diagonalizable subgroup to its identity component preserves dimension; each component translate remains contained. | PASS |

The localization observation is worth retaining as a one-sentence manuscript
sanity check, but its absence as a separately numbered author lemma is not a
gap in the source theorem.

## Part A proof replay

| Obligation | Independent replay | Result |
|---|---|---|
| Actual support | Collected distinct exponents and nonzero coefficients are fixed before the character count. | PASS |
| Middle singleton | If the middle character is nontrivial, `1,chi^e_1,...,chi^e_s` are `s+1>=3` distinct characters; two endpoint terms cover at most two. | PASS |
| `P(xi)!=0` branch | The surviving nonzero trivial-character term forces both endpoint characters trivial. | PASS |
| `P(xi)=0` branch | The two endpoint terms force `chi_(n+k)=chi_n` and the scalar identity `xi_(n+k)=a xi_n`; no relation is lost. | PASS |
| Kernel relations | Every equation gives `A_n=epsilon_(k+n-nu)` and `B_n=epsilon_(k+n)-epsilon_n`. | PASS |
| Integral independence | The `A_n` pivots form an interval of span `m-1<=k-1`; each disjoint endpoint pair of a `B_n` is separated by `k`, so it has an endpoint outside the pivot interval. That outside coordinate occurs in no other relation. | PASS |
| Dimension | The ambient-coordinate map onto `X*(H)` has kernel rank at least `2m`, hence `dim H<=k+m-2m=k-m`. | PASS |
| Future pullback | `chi_(k+n)=chi_n` makes every future character an initial character before a future middle coordinate is reduced modulo `k`. | PASS |
| Residues/no gcd | The killed initial set is the translation `{n-nu mod k}`, not the orbit `{-j nu}`. Translation is injective on an interval of length at most `k`. | PASS |
| Equality inclusion | With `a=1,P(1)=0`, every active middle coordinate equals `1` and every output copies its lag endpoint. | PASS |
| Saturation | Projection to the free initial coordinates splits the character-lattice quotient; the kernel is a direct summand. | PASS |
| Endpoint sharpness | At `m=k-1`, the sole free initial residue is `k-1-nu`; varying it through `2^N` gives distinct points in `T_(k-1)`. | PASS |

The proof remains valid at both endpoints `m=0` and `m=k`. In particular, at
`m=k` the pivot interval has span exactly `k-1`, still too short to contain a
pair separated by `k`.

## Part B collision/transition matrix

The binomial audit was replayed without assuming the author's labels. For a
local equation with support `{p,q}`, `p<q`, and nontrivial middle character,
the two middle powers are distinct. A no-singleton partition must pair each
endpoint with a different power. There are exactly two orientations:

- `B`: lag `=p` times middle, output `=q` times middle;
- `C`: lag `=q` times middle, output `=p` times middle.

The trivial-middle label `A` separately retains both the nonroot-kill and
root-copy scalar branches.

| Adjacent labels | Character compatibility | Outcome |
|---|---|---|
| `AA` | Both middle characters vanish and the copies close all endpoints. | zero only |
| `AB`, `AC` | The second nontrivial label would make the zero lag a positive multiple of a nonzero middle. | impossible |
| `BA`, `CA` | The second label requires the nonzero first output to be zero. | impossible |
| `BB` | `u_1=pq u_1`. | impossible since `pq>1` |
| `BC` | `u_1=q^2 u_1`. | impossible since `q>=2` |
| `CB` | `u_1=p^2 u_1`. | survives only at `p=1` |
| `CC` | `u_1=pq u_1`. | impossible since `pq>1` |

The support collision matrix is therefore:

| Actual support | First possible rigid window | Exceptional geometry | Independent result |
|---|---:|---|---|
| `{1}` | none | diagonal-type one-dimensional coset for every `m` | PASS |
| `{d}`, `d>=2` | `V_2^0` | none; `(d^2-1)u=0` closes | PASS |
| `{p,q}`, `2<=p<q` | `V_2^0` | none | PASS |
| `{1,d}`, `d>=2`, `a!=-beta^2` | `V_2^0` | none | PASS |
| `{1,d}`, `d>=2`, `a=-beta^2` | `V_3^0` | unique `C_d` in `V_2^0` | PASS |
| `|E|>=3` | `V_2^0` | none; a second equation closes root-copy | PASS |

For the sole `CB` word the character vector is `(d u,u,u,d u)`. Its scalar
pairings force `xi_2=beta xi_1` and `a xi_1=-beta xi_2`, hence exactly
`a=-beta^2`; the remaining scalar equations give every coordinate of `C_d`.
All ambient characters are multiples of `u`, while `u` itself is an ambient
character, so the connected positive-dimensional torus is one-dimensional and
its `x_1` character is primitive. The image is therefore the whole displayed
`C_d`, not a proper positive-dimensional subcoset.

A third label cannot extend `(d u,u,u,d u)`: `A` requires zero middle, `B`
forces `(d-1)u=0`, and `C` forces `(d^2-1)u=0`. This independently closes the
third-step claim. If the first four characters are already trivial, the third
equation forces the fifth trivial as well.

## Laurent, finite rank, arbitrary fields, and torsion

The exact indispensable external input is the qualitative torus consequence
of Michel Laurent, “Equations diophantiennes exponentielles,” *Inventiones
mathematicae* 78 (1984), 299--327, DOI
`10.1007/BF01388597`. The journal EuDML record is `143175`; `182179` is the
separate Bordeaux seminar account and is not substituted for the article.

For a closed torus subvariety `X` and the division group of a finitely
generated subgroup, Laurent's theorem places the intersection in finitely many
torus cosets contained in `X`. If `X` contains no positive-dimensional torus
coset, only zero-dimensional cosets remain, so the intersection is finite.
The project uses no effective count from this theorem.

The internal extension is valid:

1. For finite-rank `Gamma`, choose representatives of a basis of
   `Gamma tensor_Z Q` and generate `Gamma_0` from them.
2. For every `gamma in Gamma`, an integral multiple of its rational relation
   differs from a word in `Gamma_0` by torsion; a further element-dependent
   power kills that torsion. Hence `Gamma subset Gamma_0^div`.
3. This is elementwise and requires neither finite generation nor bounded
   torsion. In particular, arbitrary roots of unity are already in the
   division group of the identity.
4. The field generated over `Q` by the finitely many coefficients and
   `Gamma_0` generators is finitely generated and embeds in `C`. Every element
   of `Gamma` is algebraic over it because a positive power lies in
   `Gamma_0`.
5. Extending that embedding to an algebraic closure carries all relevant
   points injectively to the complex theorem. No embedding of the whole
   possibly large ground field is claimed.

The Cartesian-power group used for `V_m` is simply the division hull of
`Gamma_0^(k+m)`, so no extra Diophantine input is hidden. ESS's finite-rank
unit-equation theorem is a compatible adjacent source, but is neither needed
nor misrepresented as the torus Mordell--Lang input. General quantitative
torus-coset results are likewise adjacent; this project deliberately proves
only qualitative finiteness and does not claim that the broader literature has
no effective theorem.

## Geometric versus arithmetic quantifiers

| Statement | Correct quantifier | Review |
|---|---|---|
| Coset dimension | Every connected geometric torus translate contained in `V_m` over an algebraic closure. | PASS |
| Disconnected subgroup | Every connected component separately; dimension equals that of the identity component. | PASS |
| Finiteness | Every finite-rank `Gamma` over every characteristic-zero field when the relevant `V_m` has no positive-dimensional coset. | PASS |
| Part A sharpness | For every support and `k,nu`, there exist compatible coefficients and a specified rank-one group with infinite `T_(k-1)`. | PASS |
| Resonance geometry | A positive-dimensional `C_d` exists on `a=-beta^2`, independently of an arithmetic group. | PASS |
| Resonance arithmetic | There exists a compatible coefficient/group example with infinite `T_2`; no claim is made for every fixed `Gamma`. | PASS |
| Linear phase | Every geometric window contains a coset; arithmetic infinitude still uses a compatible group example. | PASS |

No source file calls `T_m` itself positive-dimensional or turns geometric
containment into a universal arithmetic-infinitude claim.

## Primary-source collision and citation audit

The bounded search was refreshed through 2026-08-17 using primary articles,
author preprints, and publisher records. Search terms combined “shift-like,”
“finite rank,” “torus coset,” “sparse recurrence,” “Hénon,” “survivor
variety,” and the exact resonance relation. No direct theorem-level collision
was found. This is a bounded no-hit statement, not a priority claim.

| Source family | Verified role | Collision result |
|---|---|---|
| Laurent 1984 | Qualitative division-group/torus-coset structure. | External engine only. |
| Evertse's author survey and ESS | Confirm arbitrary-characteristic-zero/division-group context and finite-rank unit-equation background. | Foundational/adjacent, not recurrence geometry. |
| Bedford--Pambuccian 1998 | Introduces the higher-dimensional shift-like family and analytic dynamics. | Terminology/provenance only. |
| Bera; Bera--Verma | Polynomial shift-like complex dynamics, degeneration, Fatou and unstable-manifold questions. | No finite-rank survivor theorem. |
| Bell--Ghioca | A fixed orbit intersected with a subgroup; structure of return times. | Different quantifiers and object. |
| Ji--Xie--Zhang | Cyclotomic affine/Hénon rigidity and periodic/preperiodic applications. | No finite-window support classification. |
| Mello--Yasufuku | Semigroup-orbit multiplicative dependence and integrality/non-density. | Fixed-orbit/conditional axes, no collision. |
| Karimov--Kelmendi--Ouaknine--Worrell | Linear multiple reachability with a torus-subvariety method. | Linear/algorithmic neighbor only. |
| Kaur 2026 | Transcendental shift-like complex dynamics. | No arithmetic torus-window result. |

The sources support only the roles assigned to them. They do not support the
`k-m` relation law, the equality subtori, the `{1,d}` resonance, or the closing
window, and the project does not cite them as if they did.

## Paper16 portfolio boundary

The authorized terminal Paper16 sources and provenance hashes were checked.
Paper16 owns, for the planar nonzero-constant generalized Hénon family:

- for actual nonconstant support `s>=2`, an explicit `T_2` cardinality bound
  and rank-one `T_1` sharpness; and
- for support one, the fully absorbed explicit `T_4` bound and rank-one `T_3`
  sharpness theorem originating in Paper14.

Paper17's `k=2,nu=1,m=2,c!=0,s>=2` consequence is a weaker qualitative shadow
and receives no novelty credit. Paper17 neither improves nor absorbs Paper16,
and it does not revive Paper14.

The surviving portfolio-distinct contribution is the all-`k`, all-`nu`,
all-window geometric deficit with equality, together with the exact planar
`c=0` phase expressly outside Paper16. The common constant-anchor deletion
mechanism makes those parts one article rather than a disguised replacement
for Paper16.

## Fifteen anti-claim gate

| # | Prohibited statement | Finding |
|---:|---|---|
| 1 | `T_m` itself is positive-dimensional. | ABSENT |
| 2 | Resonance makes `T_2` infinite for every `Gamma`. | ABSENT |
| 3 | `a=1,P(1)=0` is necessary for equality. | ABSENT |
| 4 | A `gcd(k,nu)` hypothesis or phase is required. | ABSENT |
| 5 | Killed residues form the iterated orbit `{-j nu}`. | ABSENT |
| 6 | Nonlinear monomials have no finite window. | ABSENT |
| 7 | Laurent supplies an effective project-specific count or algorithm. | ABSENT |
| 8 | The standard character-partition lemma alone is novel. | ABSENT |
| 9 | The theorem extends to positive characteristic, `a=0`, rational/Laurent maps, or arbitrary polynomial automorphisms. | ABSENT |
| 10 | Actual support is affine-conjugacy invariant. | ABSENT |
| 11 | Every finite-rank group is finitely generated or has bounded torsion. | ABSENT |
| 12 | Paper17 improves Paper16's explicit planar bound. | ABSENT |
| 13 | A bounded search proves global priority. | ABSENT |
| 14 | Part A classifies all equality or maximal cosets. | ABSENT |
| 15 | Heights, periodic-point classifications, or effective enumeration follow. | ABSENT |

All fifteen are explicit exclusions, not merely omissions.

## Article unity and non-padding gate

The article-sized object is the anchor-loss mechanism, not terminal Laurent
finiteness by itself. A nonzero constant contributes an immovable trivial
character and forces one torus-direction loss per recurrence; removing it
leaves a four-term pairing problem whose sole nonlinear survivor is classified
and then closed. That logical dependency is strong enough to unite Parts A and
B.

A credible content budget is:

| Block | Substantive pages |
|---|---:|
| Motivation, exact scope, and bounded related work | 2.5--3.0 |
| Shift-like/survivor setup, scheme sanity, and Laurent bridge | 2.5--3.0 |
| Common character framework | 1.5--2.0 |
| Part A upper bound and integral independence | 3.5--4.0 |
| Equality, saturation, and arithmetic sharpness | 1.5--2.0 |
| Part B complete local partition calculus | 3.0--3.5 |
| Resonance uniqueness, third closure, and phase theorem | 3.5--4.0 |
| Examples, Paper16 boundary, and limitations | 1.5--2.0 |
| **Credible total** | **19.5--22.5** |

Thus “about 22 content pages” is credible but should be treated as an upper
target, not a quota. Twenty-four to twenty-eight pages would require genuinely
new divisor or maximal-coset structure and is not supported by this package.
The current design needs no appendix, long background survey, experiment,
figure, or example catalogue.

The experiment plan and tracker correctly record zero scientific runs, zero
CAS, zero code, zero data, and zero results. No computational evidence is used
for a universal claim.

## Conservative independent scores

| Axis | Gate | Independent score | Decision |
|---|---:|---:|---|
| Novelty after the full Paper16 deduction | 7.5 | **8.0/10** | PASS |
| Standalone/unified article value | 7.5 | **7.6/10** | PASS |
| Proof confidence | 9.0 | **9.2/10** | PASS |

The standalone score is intentionally close to threshold: terminal finiteness
alone would fail, and the planar anchored specialization is already dominated.
The score passes only because the exact all-window dimension law, saturated
equality family, and exhaustive zero-anchor phase form one closed theorem
package. The proof score reflects a complete independent symbolic replay, not
CAS or sampling.

## Final decision

Every required source-design gate passes. The project may retain the slug
`17-shiftlike-torus-coset-decay` and the title/subtitle reviewed above. Any
future manuscript must preserve the exact finite-rank/division-group scope,
the `P(xi)=0` branch, the translated residue set, the complete `A/B/C` table,
the resonance sign, the compatible-group quantifiers, the Paper16 deduction,
and all fifteen anti-claims.

SOURCE_DESIGN_PASS
