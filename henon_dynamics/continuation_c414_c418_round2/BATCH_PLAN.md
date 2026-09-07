# C414–C418: five admitted contracts and manuscript outline

Contract state: **FIVE_SUBSTANTIAL_CONTRACTS_ADMITTED**, by
[ADMISSION_DECISIONS.md](ADMISSION_DECISIONS.md).
Outline state: **FROZEN_AFTER_INDEPENDENT_OUTLINE_REVIEW**.
The [independent outline review](REVIEW_OUTLINE.md) is **PASS / CLOSED**;
its one normalization-precision correction and one filename correction
were checked by the original reviewer. This status-only update does
not alter the accepted contracts or section plans below.
No manuscript or PDF is counted complete by this document. All new
paper paths are under this continuation's `papers/` directory.
The frozen original research tree and all older batches are unchanged.

The user-authorized checkpoint is five complete papers, C414–C418.
The positive-word reserve, two-clock companion and rejected forward
scouts are not a sixth paper. Do not begin C419 or Route B.

## Shared format and claim discipline

Each manuscript is an anonymous, standalone English mathematical
`article`, 11pt, approximately one-inch margins, with one source file
per substantive section. There is no selected journal or conference,
no nine-page limit, mandatory one-page related-work section, decorative
hero image or minimum page count. Length follows a complete readable
argument. Theorems belong near the front; full proofs belong in the
body or a included, typeset appendix, not solely an external note.

Use `paper-plan`, then `paper-write`, then `paper-compile`, with the
repository batch workflow's current-team review and release rules.
Their legacy GPT-5.4/ICLR examples are not claimed as executed external
review or imposed as an unrelated venue. Claim/evidence mapping,
verified citations, reverse-outline clarity, real PDF checks and
preservation of prior files remain applicable. No placeholder author
identity, bibliography entry, experiment or prior-work result is invented.

Native finite-cycle zetas in C416–C418 are corollaries, not independent
contracts. C414 is a height Dirichlet series, not a periodic zeta.
C415 counts ordinary geometric fixed points of one specified map,
not scheme lengths or arbitrary forward polynomial counts.

## Numbering, exact object and ownership

| Paper / working title | Object, domain and clock | Author / path |
|---|---|---|
| C414 — Canonical-height distributions for constant-coefficient Hénon maps | Every $H=(y,f(y)-a x)$ over $\mathbb F_q$, $\deg f=d\ge2$, $a\ne0$; all polynomial points $\mathbb F_q[t]^2$; forward-plus-backward canonical height | root; `papers/C414_height_distribution/` |
| C415 — Degree-$2p$ resonance in Hénon–Frobenius dynamics | Every odd $p$, $q=p^e$, $e\ge3$, degree-$2p$ polynomial $g$ and $a\ne0$ over $\mathbb F_q$; $H=(y,y^q+g(y)-a x)$, $S=H^{-1}\Phi_q$ on geometric affine two-space; ordinary positive $S$ time | positive_characteristic; `papers/C415_degree_2p/` |
| C416 — Every rational cycle of the discrete-sine Hénon family | Exact integer-valued polynomial $s_d$ for every odd $d\ge3$; $H_d=(y,-x+s_d(y))$ on all $\mathbb Q^2$; ordinary point cycles, no sign quotient | nonlinear_geometry; `papers/C416_discrete_sine/` |
| C417 — Rational cycles of monic integral conservative cubic Hénon maps | Every $f=t^3+bt^2+ct+a\in\mathbb Z[t]$; $H_f=(y,f(y)-x)$ on all $\mathbb Q^2$; ordinary cycles and total coexistence | arithmetic; `papers/C417_integral_cubic/` |
| C418 — Rational periodic loci for nonconstant quadratic Hénon maps over function fields | Any $k$ with $\operatorname{char}k\ne2$, every $a\in k^*$ and $c\in k[t]\setminus k$; $H_{a,c}=(y,y^2+c-a x)$ on all $k(t)^2$; ordinary signed lifts | root; `papers/C418_function_field/` |

## C414: one-sentence contribution and claims–evidence map

All polynomial-point canonical heights for the entire constant-coefficient
Hénon family have one coefficient-independent distribution, whose exact
Dirichlet series determines every pole in the positive half-plane,
the imaginary-axis natural boundary and oscillatory height counts.

| Claim | Already reviewed evidence | Planned location |
|---|---|---|
| Orbit degree valleys and coefficient-uniform height strata | `../research_c414_c418/spectral/HEIGHT_PROOF_PACKAGE.md`, degree/valley steps | §§2–3 |
| Exact height series, convergence and fully aggregated residues | Same proof; `../research_c414_c418/arithmetic/REVIEW_HEIGHT_PROOF.md`; residue review in `positive_characteristic/` of that tree | §§4–5 |
| Meromorphic natural boundary and oscillating $q^{\lfloor B\rfloor}B$ asymptotics | Same accepted proof and nonauthor review | §§5–6 |

Structure: abstract; introduction and source distinction; definitions
and full main statements; unique edge/turn valley normal forms; exact
distribution and generating series; all pole orders/residues and
boundary proof; counting asymptotics and limitations. Do not lose
axial/aggregated cancellations by listing only uncombined denominators.
The mean exponent is not a target zero-counting correspondence.

Citations: verified Ingram/Kawaguchi and height-zeta sources from the
accepted source audit; retain the Hsia/Silverman original-access limits
and the actual Takehira version attribution. No new numerical experiment
is needed. A compact edge-versus-turn table may clarify the partition;
no artificial plotted height samples replace the full formulas.

## C415: full coefficient family, not a degree-six special case

One mixed perfected-ring induction determines the reduced fixed-point
law for every degree-$2p$ correction, including the coefficient-support
boundary that a leading-degree argument alone misses.

| Claim | Already reviewed evidence | Planned location |
|---|---|---|
| Exact ordinary fixed count from the reduced cyclic recurrence | `../research_c414_c418/positive_characteristic/FULL_DEGREE_2P_PROOF.md` and cited C404 conversion | §§2–3 |
| High-support strict-gap branch for every allowed coefficient | Same full proof plus inherited strict-gap lemma | §4 |
| Low-support mixed perfected tail, semilinearity and descent | Same full proof; `../research_c414_c418/arithmetic/REVIEW_CHARP_PROOF.md` | §§5–6 |
| Complete formula and natural-boundary corollary with actual root-order restriction | Same proof and closed affected review | §§6–7 |

Structure: abstract and exact scope; source ownership and main theorem;
ordinary versus scheme count and cyclic elimination; high-support
branch; low-support two-term/tail induction; closed coefficient formula;
native return series and limitations. Define $w=p^{v_p(n)}$ before
using $N_n=q^{2n-w}D_w$. Preserve odd $p$, $e\ge3$, all coefficients,
fractional tail degree bounds and actual descent. Do not recast the
pure $p$th-power face or degree-six predecessor as new contracts.

Citations: accepted source audit and the actually applicable C404
predecessor results. Manuscript-stage source correction: the tentative
C405 reference was unrelated and is omitted, as checked in the C415
nonauthor manuscript review; no theorem or contract changes. Include
essential conversion/degree arguments in
the typeset article so it is readable without the scout. A high/low
support comparison table is useful; no finite-prime census is needed.

## C416: complete ordinary rational cycles at every odd degree

The exact clipped bulk multiplicities, signed boundary returns and
escape exhaustion together classify every rational cycle of the
discrete-sine family at every odd degree.

| Claim | Already reviewed evidence | Planned location |
|---|---|---|
| Rational integrality and uniform escape box | `../research_c414_c418/nonlinear_geometry/PROOF_PACKAGE.md`, initial steps | §§2–3 |
| Every clipped bulk cell and central exception | Same proof and `symbolic_bulk.py` evidence described in its review | §§4–5 |
| Signed boundary section, all endpoints and long-cycle closure | Same proof; `../research_c414_c418/REVIEW_GEOMETRY_ROOT.md` | §§6–7 |
| Full cycle table, total formulas and ordinary return law | Same proof plus the independent certificate review in `positive_characteristic/` | §§7–8 |

Structure: exact family and headline census; source comparison;
rational integrality and second-difference escape proof; affine bulk
cells with clipping; both central phases; all signed boundary routing
and endpoint complement; assembly and limitations. The manuscript must
include the actual proof tables and routing necessary for exhaustion,
including the growing cycle, not only state totals and link scripts.

Set $R=(d+1)/2=3q+s$ locally; this $q$ is not a finite-field size.
Negative-phase conjugacy must convert actual point labels. Sign-negative
section cycles lift with doubled ordinary time. Keep the small-radius
cases and the no-alias proof. All positive bulk/17-exception material
already in Kim–Krieger–Postolache–Szeto Proposition 5.2 is credited.
Their Theorem 5.1's growing-cycle existence is also deducted. Source
comparison remains limited to the actual v2, including its inconsistent
displayed degree-thirteen numbers; do not claim an unseen final journal
error or global priority. Tables serve the proof; no AI illustration.

## C417: complete cubic coexistence and sharp eleven points

The integer third root of the global secant reduces every coefficient
triple to a complete exact graph classification, yielding all seven
cycle templates and a sharp eleven-point bound with its full equality
locus.

| Claim | Reviewed evidence | Planned location |
|---|---|---|
| Global finite periodic-set extrema and secant-root reduction | `cubic_arithmetic/PROOF_PACKAGE.md`, §§1–4 | §§2–3 |
| All large graphs and proved finite complement | Same proof, §§5–7; `cubic_arithmetic/REVIEW_CUBIC_ROOT.md` and independent checker | §§4–5 |
| Seven exact word/coefficient templates and least periods | Same proof, §8 | §6 |
| Sharp eleven-point bound and unique translated equality family | Same proof, §9 | §7 |

Structure: all-family theorem and scope; source comparison; integrality
and global secant; uniform large-diameter symbolic graphs; finite
complement with complete exact algorithm and result tables; short-word
interpolation proof; equality, reproducibility and limitations. Include
the finite certificate as readable pseudocode and exact ranges, not
only an external execution claim. State that each cycle, not the full
periodic set, has at most three coordinate symbols. Include the
four-global-symbol coexistence counterexample to the tempting shortcut.

Citations: verified Pezda, Ingram, the primary arithmetic question
survey where relevant, and C412 as a repository predecessor with its
actual non-journal status. Subtract general boundedness and interpolation.
The polynomial $(t^3-7t)/6$ distinguishes the existing discrete-sine
example from monic integral coefficients. Two finite-case tables and
the seven-template table are material; no new coefficient scan.

## C418: global rationality, determinants and characteristic exceptions

For every nonconstant polynomial parameter and nonzero constant
determinant over any field of characteristic different from two, an
explicit rationality graph gives every quadratic-Hénon cycle and the
sharp fourteen-point characteristic-three exception.

| Claim | Reviewed evidence | Planned location |
|---|---|---|
| All $k(t)$ periodic coordinates are polynomial; $c=-P^2+C$ has unique $C$ and $P$ unique up to sign | `function_field/PROOF_PACKAGE.md`, Steps 1–3; independent reduction/source review | §§2–3 |
| Injective signed labels and exact partial permutation | Same proof, Steps 4–5, including closed converse clarification | §4 |
| Seven all-field graph types and ordinary least-period lifts | Same proof, Steps 6–7; independent hand classification | §5 |
| Every overlap, sharp 14/8/6 bounds and $a^4=1$ restriction | Same proof, Steps 8–9 | §§6–7 |

Structure: main atlas and exact field hypotheses; arithmetic/local
source distinction; finite poles and across-cycle degree rigidity;
square completion and exact graph; minimum-state exhaustion and sign
lifts; all parameter collisions, examples and sharp bounds; ordinary
return corollary and limitations. The eight-state edge table and seven-
type atlas are essential comparison/proof tables; a picture adds little.
State all fourteen characteristic-three points via an explicit common
reconstruction rule, retaining their one four-cycle and two five-cycles.

Citations: Ingram's verified journal metadata with actual v1 text scope,
Allen–DeMark–Petsche's accessed v3, and C412's nearby sign encoding.
Preserve the normalization $\alpha=-a$ and the local versus rational
domain distinction. No arbitrary coefficient extension, characteristic
two claim, nonconstant determinant or number-field uniform boundedness
claim. The exact script is corroboration; the all-field theorem is
the analytic argument independently checked without that script.

## Review and release assignments

The coordinator owns this plan, global indexes, pinned evaluations,
final deterministic builds, release evidence, Git and final admission
decisions. Authors own only their allocated manuscript directories;
any new root checks use explicitly named separate review files.

An independent current-team reader reviews the full outline before
drafting. Manuscript review then checks actual complete TeX/Bib and
PDF text against proof/source inputs, with at least one substantive
nonauthor review per paper. A prior proof PASS does not certify a
new manuscript transcription. Any blocking finding is repaired and
the affected reasoning returns to its reviewer. Do not add fixed
numbers of rewrite rounds or redundant full proof/code reruns.

Final releases require two builds in fresh directories with recorded
deterministic settings, identical PDF bytes, text/font/warning checks,
and actual visual inspection of every final page. All payload members
then enter an exact ledger and self-excluding manifest. Only authorized
new paths and related C-stream indexes are staged; inherited untracked
material and old frozen snapshots remain untouched. No target success
is inferred from an exact source zeta, counting exponent or build PASS.
