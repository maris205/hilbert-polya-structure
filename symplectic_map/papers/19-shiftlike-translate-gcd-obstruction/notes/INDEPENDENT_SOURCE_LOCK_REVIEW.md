# Independent Source-Lock Review

Date: 2026-08-19 UTC

Project: `papers/19-shiftlike-translate-gcd-obstruction`

Role: fresh independent source-lock reviewer, temporally after
`SOURCE_LOCK_AUTHOR_STOP`

## Verdict and reviewer independence

I read all twelve frozen Paper-19 inputs to EOF after the source-lock author
stopped. I authored none of those twelve files, am not the source-design
reviewer, and am not the source-lock author. My earlier zero-write
candidate-theorem adversary role created no project artifact and conferred no
lifecycle authority. For this gate I restarted from the frozen twelve-file
universe, rehashed it, parsed the completed lock independently, replayed every
theorem and proof dependency, and refreshed the bounded literature search.

Every conjunctive source-lock obligation passes. There are zero blocking,
required, cosmetic, or advisory findings. The bounded negative literature
result remains exactly that: no direct collision was found in the checked
primary sources through 2026-08-19; unindexed, non-English, unpublished, and
private work is not excluded, and no absolute priority follows.

This review records only the source-lock gate. It does not authorize a paper
plan or any later scientific, publication, release, repository, submission,
communication, or identity effect.

## Exact U12 input universe

Immediately before this review file was created, the project had exactly
twelve regular files in exactly three descendant directories:
`experiments`, `notes`, and `refine-logs`. It had zero symlinks and zero other
entry types. Every file was valid UTF-8, non-symlink, and terminal-LF.

| Project-relative path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `experiments/EXPERIMENT_PLAN.md` | `85a38df6f2fbf056aa2ca38de02566e3ddf3d165704c17446e6c05c74779ef2f` | 8,034 | 197 |
| `experiments/EXPERIMENT_TRACKER.md` | `cbf456ab962ba39e9a9f5b1abbc8c68f078e73caf5928661cb1a2304359ff480` | 3,237 | 103 |
| `experiments/source_lock.json` | `bba41a3df39f41f367e8fbfaec3703c09c56f1f63af8904e908d262f41179aba` | 30,695 | 1 |
| `notes/CITATION_VERIFICATION.md` | `6bc87aaac7caaf47b448d0f1e8a9da886999c8990cdec0f7d8bf47119be84a06` | 10,897 | 200 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `dd26db0e9446e9258734ec5f10d2cc05aef5e921a9a487bfd0051c849cbf0aae` | 10,474 | 88 |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | `4b2f309d6a84bf53bd6b28319fba2a47386e4d3c1ac96c86375a1a43a155c724` | 24,917 | 469 |
| `notes/NOVELTY_ASSESSMENT.md` | `612fb2a1e0168e314e5f00872e23a88bfd44a577e56153695e0664305fda7e9b` | 10,172 | 195 |
| `notes/PROOF_PACKAGE.md` | `619d9fde3bbf206ae404b8c5f6bbf8f20ab08904f14026dd7ccd31d2951e600b` | 32,247 | 892 |
| `notes/RESEARCH_QUESTION.md` | `9a7c5039f19f1b86a09b1eb25b32bfd8e05a39903c8899bb02169818129df715` | 21,278 | 580 |
| `refine-logs/FINAL_PROPOSAL.md` | `d863f893f41d74f5ed46ff0448d3424c44057a448cbd06f407be0e50f5ec08b7` | 10,765 | 328 |
| `refine-logs/INITIAL_PROPOSAL.md` | `21a72723d938fe860ee68e8f522e8ab50a0f0b86537598303bd39354ee2e7980` | 8,338 | 246 |
| `refine-logs/REVIEW_SUMMARY.md` | `aae1fcc983ec32b52d006e93f2e99253e260571b114c769f0742d11dae6e619b` | 12,404 | 332 |

The U12 total is 183,458 bytes and 3,631 LF.

I also defined an external twelve-file aggregate independently of the lock.
Its exact record grammar is

`project-relative-path<TAB>sha256<TAB>bytes<TAB>LF<TAB>regular_file<TAB>true<TAB>terminal_lf_boolean<LF>`

with records sorted by project-relative path, lowercase Boolean spelling,
and no header. Its SHA-256 is

`dda2d2cdc3e48cdb239557e65b77cbddae395bc3c3939ed07ef88cc97b8687ea`.

This aggregate is an external review identity only. It is not silently
substituted for the lock's different eleven-binding aggregate grammar.

## Eleven-binding ledger replay

The lock enumerates exactly eleven inputs: the ten author files plus the
fresh independent source-design review. Each live path, type, non-symlink
state, SHA-256, byte count, LF count, UTF-8 state, BOM count, CR count, NUL
count, terminal-LF state, category, and required terminal line agrees with
the ledger.

The live binding total is exactly 152,763 bytes and 3,630 LF. Using the
lock-declared grammar

`project-relative-path<TAB>sha256<TAB>bytes<TAB>LF<TAB>regular_file<TAB>true<TAB>true<LF>`

and stripping the declared project base
`papers/19-shiftlike-translate-gcd-obstruction/` from each stored workspace
path, the independently recomputed aggregate is

`87562a1d2d1245aab027674635e2f4f2bb28ed9adbcdd3e091df410f68230621`,

exactly the value in `/binding_contract/aggregate_sha256`.

The source-design review remains byte-identical and its final nonempty line is
exactly `SOURCE_DESIGN_PASS`. The ten-author-file aggregate under its earlier
four-field grammar independently recomputes to

`5d963e353fa915a0832adeb380cd69c1f8cc76becf8825a546bf243f83937fea`

with 127,846 bytes and 3,161 LF.

## Strict canonical JSON audit

The completed `experiments/source_lock.json` has external identity

- SHA-256: `bba41a3df39f41f367e8fbfaec3703c09c56f1f63af8904e908d262f41179aba`;
- bytes: 30,695;
- LF: 1.

I parsed the complete one-line file with a duplicate-object-name callback
that rejects a second key at every nesting depth and a nonfinite callback
that rejects `NaN`, `Infinity`, and `-Infinity`. Independent probes for one
duplicate key and all three nonfinite constants were rejected.

Re-serialization as UTF-8 JSON with `ensure_ascii=false`, `allow_nan=false`,
recursive key sorting, separators `,` and `:`, and exactly one appended LF
was byte-for-byte identical to the live file. The file has no BOM, CR, or NUL
and exactly one terminal LF. All current object keys are ASCII, so recursive
Unicode code-point ordering and ordinary lexical key ordering coincide.

The lock does not bind itself and contains neither a predeclared self SHA-256
nor a self byte count. Its `after_lock` inventory explicitly excludes both
self identities. Reporting the completed lock identity above therefore does
not create a fixed-point or self-reference defect.

## Before, after, and future universe audit

The temporal file-system chain is exact:

1. the author stopped with ten regular Markdown files;
2. the source-design reviewer added only
   `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md`, producing U11;
3. every U11 file remained byte-identical, and the source-lock author added
   only `experiments/source_lock.json`, producing U12;
4. the sole authorized post-stop review write is this file,
   `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md`, producing U13.

The exact U11-to-U12 path-set difference consists only of
`experiments/source_lock.json`. No unlisted intermediate project artifact,
directory, symlink, or other object exists. This exact delta, together with
the unchanged eleven live bindings, confirms that the lock author changed
only the lock inside the Paper-19 project.

Batch dashboards are outside the bound project universe, and the lock sets
`batch_dashboard_mutation_authorized=false`. I did not modify either
dashboard. The review cannot use dashboard prose to override the frozen
project contracts.

The lock's future path equation permits only this review file. It forbids the
listed paper, plan-review, publication-scope, publication-lock, code, data,
result, figure, asset, and build paths. The lock status is exactly
`SOURCE_LOCK_AUTHOR_STOP`; the current source-lock author has no remaining
write authority.

## Definitions, orientation, and arithmetic bridge

The displayed inverse of the type-`nu` shift-like map is correct, and direct
substitution gives

`x_(n+k)=P(x_(n+k-nu))+a x_n`.

`V_m` has exactly the equations `0<=n<m` in the torus with coordinates
through `x_(k+m-1)`. `T_m` contains states at times `0,...,m`. Forward
uniqueness makes projection from `V_m intersect Gamma^(k+m)` to `T_m` a
bijection. Geometric dimension is assigned only to contained torus
translates, never to `T_m`.

The finite-rank bridge also closes with arbitrary torsion. Representatives of
a `Q`-basis generate `Gamma_0`; after clearing one rational relation and
killing the resulting individual torsion element, every `gamma in Gamma` has
a positive power in `Gamma_0`. Thus `Gamma` lies in `Gamma_0^div`. The field
generated by the coefficients and finitely many generators is finitely
generated over `Q` and embeds into `C`; the remaining elements are algebraic,
so the embedding extends to an algebraic closure. No claim that an arbitrary
large ground field embeds in `C` is used.

Laurent is used only qualitatively: absence of a positive-dimensional
contained translate makes the intersection with the relevant division group
finite. No effective count, algorithm, or recurrence-specific exceptional
set is attributed to `EXT-L`.

## Part A theorem replay

### `TA1`: equality-subgroup rigidity -- PASS

With at least two actual nonconstant monomials, a nonzero middle character
would make the `s+1>=3` characters
`0,e_1u,...,e_su` distinct, while the two endpoint terms can cover at most
two of them. A singleton remains, so every middle character is zero. The
remaining identity forces the copy relation between old and future
characters.

Modulo those copy relations, the middle-coordinate relations kill exactly
the distinct initial residues

`R_m={n-nu mod k:0<=n<m}`.

The quotient is free on the other `k-m` initial coordinates. Consequently
the predecessor relation lattice is saturated of rank `2m`. At equality
`dim H=k-m`, the actual character kernel has the same rank, contains that
saturated lattice, and therefore equals it. The embedded connected subgroup
is exactly `H_m`, not merely isogenous to it. No lower-dimensional or
inclusion-maximal classification follows.

### `TA2`: normalized translate scheme -- PASS

The free initial coordinates give one and only one representative with all
free initial scalars equal to one. Direct residue membership gives

`A_m=[max(0,m-nu),min(m,k-nu))`

and

`alpha_m=min(m,k-m,nu,k-nu)`

without a gcd assumption.

For `y_n=xi_(k+n-nu)`, the reconstruction

- places `y_n` directly on the killed initial middle coordinate when
  `n<nu`;
- solves `xi_(n-nu)=a^(-1)(y_n-P(y_(n-nu)))` when `n>=nu`; and
- defines `xi_(k+j)=P(y_j)+a xi_j`.

Outputs already represented by a later `y` agree by substitution. The first
open family is exactly nonvanishing of the solved killed initials. Every
remaining output is either a later nonzero `y`, automatically `a` at an
active tail, or is governed by
`P(y_j)+a y_(j+nu-k)!=0` for `k-nu<=j<m`. Thus the root equations and two
open families are necessary and sufficient, with no omitted or duplicated
coordinate.

### `TA3--TA4`: fixed and universal geometry -- PASS

The active interval has length at most both `nu` and `k-nu`. Therefore two
indices in either open condition cannot both be active; after fixing any
active root tuple, every forbidden equation has a free variable and cuts a
proper closed subset, possibly the empty set. A finite union cannot cover the
remaining irreducible torus. When `alpha_m=m`, both inequality index ranges
are empty. This proves nonemptiness for every root tuple and does not use the
discarded one-root shortcut.

For squarefree `P`, the root assignments give exactly
`delta^alpha_m` nonempty smooth irreducible open-torus components of dimension
`m-alpha_m`. For arbitrary `P`, reduction gives exactly `r^alpha_m`
geometric components, and an active root of multiplicity `mu` retains its
local `z^mu` nilpotent direction.

Over the fixed actual-support coefficient torus, the leading and constant
coefficients are units. The monic root algebra is finite free of rank
`delta`, and the unit constant term makes `X` invertible. The universal
scheme is the asserted open in a product of root schemes and a free torus;
it is flat relative lci and smooth over the discriminant complement. At a
fixed fiber, local factorization by units gives exactly the displayed
completed **fiber** ring. No Hilbert, Fano, fine-moduli, discriminant-
irreducibility, or total-singular-locus assertion is present.

### `CA1`: coefficientwise arithmetic -- PASS

At `m=k-1`, `alpha_m=1` and `E_m` is nonempty for every coefficient tuple.
A geometric translating point is defined over a finite algebraic extension,
and adjoining its finitely many scalars and the infinite-order element `2`
gives a compatible finitely generated group. Varying the saturated one-torus
parameter through `2^N` gives distinct points of `T_(k-1)`. Paper 17 owns the
terminal `T_k` finiteness input. The claim correctly says compatible field and
compatible group, not every fixed group or the original field.

## Part B theorem replay

### `TB1--TB3`: exclusive labels, gcd cores, and arbitrary rank -- PASS

The four group-algebra terms have nonzero coefficients. Character
independence permits only the all-zero row `Z` or one of the three pairings

`A=(0,v,dv)`, `B=(v,0,v)`, `C=(dv,v,0)`

with `v!=0`. This nonzero requirement makes the labels exclusive and fixes
all scalar signs. The support bits obey

`s_(j+q)=s_j+s_(j+L)` over `F_2`.

With `g=gcd(k,nu)`, `q=k/g`, and `L=(k-nu)/g`, original indices split into
`g` independent cores, with `q>=2`, `1<=L<q`, and `gcd(q,L)=1`.

In each active triple, connect exactly the two nonzero vertices with
`d`-exponent weight one or zero. A nonzero signed cycle weight would imply
`v=d^s v` in the rationalized torsion-free character lattice, so every
component has an integer height. Giving disconnected components independent
formal colors is essential even if their actual character values happen to
coincide. Label by label the colored word satisfies

`F_(j+q)=F_j+T F_(j+L)`.

Thus the proof handles arbitrary rank and multiple scaling components rather
than assuming a one-dimensional torus.

### `TB4`: extinction after `q^2` core equations -- PASS

Choose a minimum-height vertex in one component. Backward as an output it can
only lie in a `B` triple; otherwise it is zero or has a lower-height middle.
The chain reaches an initial residue `r in [0,q-1]`. Forward minimum-height
persistence again forces `B`, making the middle character globally zero.
Consecutive zeros separated by `q` propagate the triangle

`u_(r+tL+jq)=0`, `1<=t<=q`, `0<=j<=q-t`.

At `t=q` this kills `r+qL`, while the persistence column keeps `r+Lq`
nonzero. Since `qL=Lq`, every component is impossible. No finite enumeration
or rank-one shortcut is used.

### `TB5`: unique `q^2-1` shadow and explicit semigroup formulas -- PASS

If the minimum initial residue were at most `q-2`, the complete `q^2`
contradiction would still fit, so it is `q-1`. The shortened zero triangle is

`u_(q-1+tL+jq)=0`, `1<=t<=q-1`, `0<=j<=q-1-t`.

For every `s in [0,q-2]`, choose the unique `t in [1,q-1]` with
`tL=s+1 mod q`, write `tL=hq+s+1`, and set `j=L-1-h`. The bounds
`h<=L-1` and `h>=t+L-q` give `0<=j<=q-1-t`, so the triangle covers
`[Lq,(L+1)q-2]`. The remaining point

`N_*=(L+1)q-1`

lies on the nonzero persistence column. Every nonzero component must contain
this same vertex; disjointness leaves exactly one component.

After normalizing the central delta block, the backward and forward series
are

`G(z)=(1+Tz^L)/(1+Tz^L+z^q)`

and, with `p=q-L`,

`H(z)=z^(q-1)/(1+Tz^p+z^q)`.

Their coefficients have the exact forms

`sum_(alpha q+beta L=t-q) binom(alpha+beta,beta)_(mod 2) T^beta`

and

`sum_(alpha q+beta p=t-q+1) binom(alpha+beta,beta)_(mod 2) T^beta`.

If `gcd(q,s)=1` and `D<qs`, two distinct nonnegative representations of
`D=alpha q+beta s` would differ by a nonzero multiple of `(s,-q)` and force
`D>=qs`. The complete backward range has `D<=Lq-1`; the complete involved
forward range has `D<=pq-1`. Every involved coefficient is therefore zero or
one monomial. At the next degree `D=pq`, the only representations are
`(p,0)` and `(0,q)`, producing `1+T^q`. This proves existence, uniqueness,
and the first collision analytically.

For an abstract torsion-free over-lattice, the involved characters span one
cyclic subgroup but unused direct summands are not excluded. Only after the
other original residues vanish do ambient coordinate restrictions generate
the actual `X*(H)`. Since `w=F_(N_*)` occurs, one gets
`X*(H)=Z w`; `w` is primitive and the actual torus has dimension one.

### `TB6`: original-window bookkeeping -- PASS

At `m=kq=gq^2`, every residue has exactly `q^2` core equations and all
characters `u_0,...,u_(kq+k-1)` vanish. The general endpoint is not
`u_(2kq-1)`.

At `m=kq-1`, residues `0,...,g-2` have `q^2` equations and residue `g-1`
has `q^2-1`. Only the last residue may carry the unique shadow. The residue
coordinate ranges together cover every ambient coordinate, so there is no
invisible character coordinate.

### `TB7--TB8`: seven labels and scalar obstruction -- PASS

For `q>=3`, set `z_*=N_*-2L`. Direct substitution into the coefficient
formulas gives

| Equation | Colored triple | Label |
|---:|---|---|
| `L-1` | `(T^(q-1),T^(q-2),0)` | `C` |
| `q-1` | `(1,0,1)` | `B` |
| `z_*-q` | `(T^2,T,0)` | `C` |
| `z_*+L-q` | `(T,1,0)` | `C` |
| `z_*` | `(0,0,0)` | `Z` |
| `z_*+L` | `(0,1,T)` | `A` |
| `z_*+q` | `(0,T,T^2)` | `A` |

If `2L<q`, the relevant forward degree is below `p`; if `2L>q`, the
backward degree `2L-q` is below `L`. Neither has a semigroup representation.
Equality `2L=q` contradicts coprimality for `q>=3`, proving the central zero.

The lowest selected equation is `(q-2)L-1>=0`, and

`q^2-2-(z_*+q)=(q-2)(q-L)-1>=0`.

Thus every selected equation lies in `[0,q^2-2]`. Small-parameter
coincidences occur only between displayed `C` labels and create no conflict.

The first shared `C/B` scalar gives `bc^(d-1)=-1`. The later `C/A` scalar
gives `a=-1`. The adjacent `C/C/A` labels make the old, middle, and future
scalars at the `Z` equation all equal to `c`. That recurrence reads

`c=c+bc^d+ac=-c`,

so `2c=0`, contradicting characteristic zero and `c!=0`. Consequently
`V_(kq-1)` has no positive-dimensional torus translate for `q>=3`. No
shorter-window survivor is proved, so the result is not an exact, optimal,
shortest, minimal, or sharp scalar clock.

### `TB9`: `q=2` iff and general-`g` fill -- PASS

For `q=2`, coprimality forces `L=1`, and the unique shadow is

`(d w,w,0,w,d w)`

with labels `CBA`. Its shared scalar coordinates make
`a=-1` and `bc^(d-1)=-1` necessary. Under those conditions,

`(b s^d,s,c,-s,b(-s)^d)`

satisfies all three recurrence identities for every `s!=0`. The exponent
vector `(d,1,0,1,d)` contains one, so the one-parameter subgroup is primitive
and saturated.

When `g>1`, every inactive residue needs four equations and six nonzero
scalar coordinates. The map

`Phi(x,y)=(y,c+b y^d-x)`

is a polynomial automorphism with inverse `(c+b x^d-y,x)`. Every required
finite iterate coordinate is a nonzero polynomial because it is a coordinate
of a polynomial automorphism. Over the infinite field, finitely many proper
coordinate-zero hypersurfaces cannot cover `A^2`; generic initial pairs fill
all inactive residues. The residues are independent, so the construction is
a translate in the full original `V_(kq-1)`, not merely a five-coordinate
core lift.

The planar `g=1,k=2` instance remains Paper 16's endpoint. At `m=kq`, `TB4`
still excludes all positive-dimensional translates.

### `CB1`: arithmetic consequences -- PASS

With the exact `EXT-L` bridge, `T_(kq)` is finite for all `q>=2` and every
finite-rank group. `T_(kq-1)` is finite for `q>=3` and for nonresonant
`q=2`. On the resonant `q=2` locus, a compatible finite extension and
finitely generated group meet the saturated translate infinitely, while the
next window remains finite. These are qualitative statements only.

## Citation, novelty, and source traceability

The sole indispensable external theorem remains Michel Laurent,
“Equations diophantiennes exponentielles,” *Inventiones mathematicae* 78
(1984), 299--327, DOI `10.1007/BF01388597`. I independently confirmed the
publisher identity and retained only its qualitative torus role.

I refreshed exact-formula and title/abstract searches on the lock date in
three independent clusters:

1. maximum-dimensional/normalized torus translates in sparse shift-like
   recurrences, using four formulations around “shift-like,” “torus
   translate,” “normalized translate scheme,” finite rank, and entire-coset
   containment;
2. the formulas `F_(n+q)=F_n+T F_(n+L)`, `q^2` extinction, colored Laurent
   components, and gcd-reduced character recurrences, again using four
   formulations; and
3. `kq-1`, `CBA`, seven-label scalar obstruction, and 2026 dynamical
   Mordell--Lang recurrence work, using four formulations.

The refresh independently confirmed the already bound scope boundaries:

- Bera, arXiv:1805.03142, studies complex shift-like dynamics rather than
  finite-rank contained translates;
- Dill--Gallinaro, arXiv:2506.07550, studies intersections with translates,
  not entire-translate containment in these recurrence windows; and
- Zhang, arXiv:2605.27058, studies semilinear rank-two iteration-exponent
  sets for one-variable polynomials, not the Paper-19 survivor varieties.

No checked primary source states `H_m` equality rigidity, the explicit
normalized `E_m`, the colored arbitrary-rank `q^2/q^2-1` theorem, the central
delta formulas, or the seven-label scalar obstruction. The source roles are
context or collision controls only; no additional external proof theorem is
silently imported.

All normative local theorem, proof, anti-claim, score, page, citation,
portfolio, lifecycle, and zero-science sources are among the eleven exact
bindings. The predecessor artifacts are explicitly identified portfolio or
predecessor subjects rather than unbound Paper-19 source inputs.

## Portfolio bindings

The predecessor identities recompute from the live terminal artifacts:

| Paper | Terminal-review SHA-256 | Final-PDF SHA-256 | Boundary |
|---:|---|---|---|
| 16 | `e355172b4533011d549453d02ee9939fb2dabc16fef035206ad4911fdf18eb76` | `b4ffdaf30e2d0684b875863393e6937c26f51ce89c6f47567a24ed9a123e5e4f` | Owns planar `CBA`, exact `T_4/T_3`, and the stronger effective bound. |
| 17 | `941e8b47e4436fdd9bff6f48ebf6e8c1174d07f545a220ead9ad02d73b23ed9d` | `080282e18b085cc87bb590db239c4c8f8f80fd86147ded1aa775e67504b17f2e` | Owns `dim H<=k-m`, the special equality family, terminal `T_k` finiteness, and special-coefficient sharpness. |
| 18 | `251d78d2989c0c76b6f1a3090c9aeccf9c66a7171829ca6b795c9ca97d359713` | `e9044c2a9e6452b58b9e345a17c33a211feed909414798fa4696e169b24be06b` | Marked trace and ramification work has no theorem-level collision. |

All three terminal reviews still end `FINAL_INTEGRITY_PASS` followed by
`RELEASE_CONFIRMED`. Paper 19 deducts the predecessor claims before scoring
its equality-moduli and all-`g` support-one contributions. It neither absorbs
nor re-markets Papers 16--18.

## Scores, `STOP-S1`, anti-claims, and article mass

The conservative candidate scores `7.9 / 8.2 / 9.1` exceed the conjunctive
thresholds `7.5 / 7.5 / 9.0` without a waiver. The fresh source-design review
scores `8.2` novelty, `8.4` standalone value, `9.2` proof readiness, and
`8.8` unity/page feasibility. My replay finds no reason to reduce any score
below its gate.

`STOP-S1` remains active in every required theorem, proposal, review,
tracker, and no-run role. The false implication

`unique q^2-1 character shadow => universal scalar lift`

is explicitly refuted first at `(k,nu,d)=(3,1,2)` and then universally for
`q>=3`. No surviving claim revives exact scalar sharpness.

The lock contains exactly eighteen unique entries `AC01--AC18`, in order,
and every exclusion agrees with the bound prose. In particular, there is no
dimension for `T_m`, lower-dimensional classification, Hilbert/Fano claim,
unqualified component count, nonsquarefree smoothness claim, varying-support
family, every-group sharpness, effective Laurent count, planar novelty,
positive-characteristic or zero-coefficient extension, arbitrary polynomial-
automorphism extension, absolute priority, or external lifecycle effect.

The section budget sums to exactly 29 substantive pages and has a credible
unpadded range of 26--29 pages. Part A and Part B are unified by the question
whether an extremal character pattern admits translating scalars. The U12
inventory contains no bibliography, TeX, manuscript, appendix, code, data,
result, figure, asset, build, PDF, or cache. Zero scientific or computational
experiments, zero numerical tables, and zero figures are required. The
read-only parsers, hashes, formula checks, and literature queries used for
this review are audits, not scientific evidence.

## Remaining authority fences

After this file is added, all twelve reviewed inputs remain immutable. This
review is the only authorized U12-to-U13 addition and ends the current review
write authority.

`SOURCE_LOCK_PASS` does **not** authorize any of the following:

- a paper plan or paper-plan review;
- a bibliography, TeX source, manuscript, or appendix;
- code, data, results, scientific execution, symbolic enumeration, or
  external service;
- a figure, asset, numerical table, compilation, build, or PDF;
- publication-stage scope, finalization, release, or repository push;
- submission, upload, external message, dashboard transition, or identity
  disclosure.

Every later stage requires separate explicit authority not conferred by the
source lock or this review. The current external effect remains none.

SOURCE_LOCK_PASS
