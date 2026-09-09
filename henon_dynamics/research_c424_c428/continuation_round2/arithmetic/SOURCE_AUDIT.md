# AR2-1 source and local-ownership audit

Actual access on 2026-09-08 UTC. This is a bounded source-first collision
audit for one frozen question, not a claim of exhaustive literature coverage
or a separate ARS research pipeline. ARS was used only for source-quality,
scope and citation fact-checking. Native author reasoning is identified
separately in `PROOF_PACKAGE.md`. No source absence is treated as novelty.

## Scope of the question being compared

For every field `k` of characteristic not two, every nonzero constant `a`,
and every nonconstant Laurent `c`, classify every ordinary periodic point
of `H(x,y)=(y,y^2+c-a x)` in **all** of `k(t)^2`, with least periods and
coexistence. One application is one tick. The constant-parameter family,
nonconstant determinants, completions, arbitrary algebraic extensions,
geometric fixed schemes, and more-than-two-pole parameters are not
substituted for this domain.

## Local ownership: inspected before the mathematical diagnostic

| Existing result | Actual source access in this lane | Deduction |
|---|---|---|
| C418, nonconstant polynomial quadratic Hénon parameters | Full `CONTRACT.md`, full `PROOF_PACKAGE.md`, full `SOURCE_AUDIT.md` under `henon_dynamics/continuation_c414_c418_round2/function_field/` | All one-pole parameters, the common-degree/constant-offset proof, the eight-state sign graph, all seven cycle rows, ordinary sign lift and all characteristic-three overlaps are already owned. Negative-power-only parameters are the same theorem after inversion of `t`. |
| C417, monic cubic integral cycles | Its `SCOUT_REPORT.md` under `continuation_c414_c418_round2/cubic_arithmetic/` and the first three extracted PDF pages were inspected during prescreening | The full monic cubic family is already owned; it was not reopened as a second question. |
| C412 and AM1 | Current batch admission and continuation plan read in full; C418's explicit ownership discussion also read | Their integer/real-annulus sign/offset mechanisms and the admitted integer-valued degree-two family are not a residual contribution here. No old payload was rerun or edited. |
| First-round Adler result | Current batch admission decision read in full | Its full global-identity theorem was already closed and classified auxiliary-only. It is not described as still mathematically open and was not reopened. |

The local PDFs were not treated as structurally verified documents.
The two actual preflight results are preserved in `c418_pdf_preflight.json`
and `c417_pdf_preflight.json`; both are `UNAVAILABLE` because `pypdf` was
not installed. The separate first-three-page `pdftotext` previews were
actually read, but no stable PDF page-coordinate anchors are claimed from
them. The substantive C418 ownership comparison rests on the full Markdown
proof, not an assumed successful PDF check. No package was installed.

## Closest external primary sources

### S1. Ingram: finiteness, bad-place bounds and local pole clustering

Patrick Ingram, *Canonical heights for Hénon maps*, Proceedings of the
London Mathematical Society 108(3), 780--808 (2014), DOI
[10.1112/plms/pdt026](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/plms/pdt026).
The publisher confirms online publication on 22 July 2013. The actual
primary theorem text was read in the
[arXiv PDF](https://arxiv.org/pdf/1111.3609): introduction, Theorems
1.1--1.4, the proof of Theorem 1.2 in Section 3, and Lemma 4.2 with proof.

Theorem 1.2 concerns `(y,x+f(y))`; its `a_source=1` corresponds to this
lane's `a=-1`, not arbitrary determinant. It proves nonisotrivial
function-field finiteness and a bound in terms of bad places. Crucially,
Section 3 explicitly assumes `d>=3` and routes the quadratic case to
Theorem 1.4/Section 4. Its concluding degree-at-least-three numerical
estimate is **not** substituted at `d=2` here. Lemma 4.2 supplies the
half-pole and nearby-root clustering mechanism in the quadratic
normalization. These are fully deducted. The source
does not supply the Laurent all-determinant compatibility/point atlas
asserted here. That last statement is a comparison of the actual inspected
theorems, not proof that no other result in the literature does so.

### S2. Gauthier--Vigny: the broader characteristic-zero finiteness theorem

Thomas Gauthier and Gabriel Vigny, *The Geometric Dynamical Northcott
Property for Regular Polynomial Automorphisms of the Affine Plane*,
Bulletin de la Société Mathématique de France 150(4), 677--698 (2022),
DOI 10.24033/bsmf.2858. Publication metadata were verified against the
[official SMF sample](https://smf.emath.fr/sites/default/files/2023-05/GAUTHIER_VIGNY__sample.pdf).
The Main Theorem and its following characteristic-zero corollary were
actually read in the [primary v1 PDF](https://arxiv.org/pdf/2010.16291v1).

The corollary covers every nonisotrivial regular plane polynomial
automorphism of degree at least two over a characteristic-zero function
field: canonical-height-zero points are periodic and form a finite set.
Thus bare finiteness for all constant determinants in the present
characteristic-zero Laurent family is already owned. The inspected
statement does not give the finite explicit Laurent parameter/point
classification or the mixed-sign determinant restriction claimed here.

Access precision: an initial full publisher-PDF request failed. An
unverified `v2` PDF URL also failed; the arXiv submission record was then
checked and lists **only v1**, 30 October 2020. The actual theorem
comparison uses that successfully read v1, not a fictitious newer version.
No assertion of reading the entire published proof is made.

### S3. Allen--DeMark--Petsche: the completed-field horseshoe

Kenneth Allen, David DeMark and Clayton Petsche, *Non-Archimedean Hénon
maps, attractors, and horseshoes*, Research in Number Theory 4, article 5
(2018), DOI
[10.1007/s40993-018-0105-2](https://link.springer.com/article/10.1007/s40993-018-0105-2).
The publisher confirms 31 January 2018. The
[primary arXiv PDF](https://arxiv.org/pdf/1610.04271) was actually read at
the standing field assumptions, region `H_III`, Theorem 1, and Theorem 28
with its proof.

Its field is complete and locally compact with odd residue characteristic.
For its normalization `(A+B y-x^2,x)`, region `|A|>max(1,|B|^2)` and a
square `A`, Theorem 28 gives a conjugacy on the filled Julia set with the
full two-sided binary shift. The current map is conjugate to `A=-c,B=-a`
by `(x,y)->(-y,-x)`. Local binary symbolic dynamics, including the local
square obstruction, is therefore source-owned in the stated setting.
This is not a theorem that every locally labelled orbit belongs to
`k(t)^2`; intersecting two completions is not automatic rationality.
The all-field Laurent-unit compatibility and explicit rational labels
must be proved separately, as they are in the author package.

## Author deductions needed to apply the subtraction

These statements are elementary author reasoning, not attributed verbatim
to any of S1--S3.

* The nonconstant quadratic family is nonisotrivial in characteristic zero:
  its two fixed points have Jacobian traces `2y_1,2y_2`, whose product is
  `4c`. This nonconstant quantity would be constant after a conjugacy to a
  constant-coefficient map, a contradiction. The discriminant cannot
  vanish identically unless `c` is constant. Thus S2 is genuinely relevant
  to the frozen family, not just a theorem with an unchecked hypothesis.
* In S1's `a=-1` specialization the only bad places here are zero and
  infinity. The local roots of `z^2+c` differ by `2 sqrt(-c)`; at the two
  poles its absolute value exceeds one, and at all other places it does
  not. This bad-place observation does not authorize applying the
  degree-at-least-three Section 3 numerical estimate to a quadratic map.
* Replacing a nonconstant polynomial `P` by a transcendental Laurent
  function in the **sign/constant-offset part** of C418 is a short base
  change: its proof after that reduction uses only independence of `P,1`.
  It is not new. What fails for the Laurent domain is the assertion that
  all rational cycles necessarily have that one fixed sign product.
* The displayed mixed four-cycle is an elementary low-period
  rationalization; its existence alone cannot establish an independent
  research increment. No novelty is claimed for that witness.

## Actual bounded retrieval ledger

Local discovery used `rg --files`/`rg` first. Available tool metadata were
searched for Zotero/Obsidian retrieval, with no callable match. A local
`arxiv_fetch` helper was sought in the available locations and not found;
ordinary primary-site browsing was used instead. No plugin installation,
library subscription, or external write was requested or performed.

The following actual query groups were executed. Search hits were used as
leads; the three substantive comparisons above were verified by primary
theorem text. Search ranking, crawl dates, and irrelevant lexical matches
were not treated as source evidence.

| Group | Actual queries | Disposition |
|---|---|---|
| Initial two-pole/function-field group | `"Hénon" "Laurent polynomial" periodic`; `"Henon" "two poles" periodic points`; `"Henon" "function fields" periodic rational Laurent`; `"canonical heights for Hénon maps" Ingram rational function` | Found Ingram-related primary access; exact Laurent/two-pole wording did not surface a matching theorem. |
| Broader collision group | `"Hénon" "Laurent" "rational" periodic points`; `"Henon" "S-unit" periodic`; `"Henon" "two places" function field`; `"Gauthier" "Vigny" "Northcott" plane automorphisms` | Located the broader Gauthier--Vigny source, which was not allowed to be omitted from the subtraction. |
| Freshness and repeated technical group | `"Hénon" "Laurent" periodic 2026` with a 180-day filter; `"Henon" "Laurent polynomial" "periodic points"`; `"Hénon" "two poles" function field`; `"Hénon" "S-unit" periodic` | No directly pertinent newer full-class theorem was returned. Numerous Hénon--Heiles differential-equation and person-name matches were rejected as wrong objects. This is only a bounded search observation. |
| Metadata and low-period collision group | `"Non-Archimedean Hénon maps, attractors, and horseshoes" journal 2018`; `"The Geometric Dynamical Northcott Property" "2022" Gauthier Vigny`; `"Henon" "rational" "4-cycles" function field`; `"Hénon" "periodic" "two poles" Laurent` | Primary journal records were then opened. Low-period bifurcation/ODE hits did not establish a global Laurent theorem; the witness remains unclaimed as novel. |

The nominal broad-review abstract quota was not filled with irrelevant
papers: this lane is a bounded collision audit, not a full literature
review. In particular, no claim of reviewing 10--15 relevant abstracts or
all citations to these sources is made. Additional source collision could
still defeat admission and is part of independent review.

## Claim-to-source/subtraction table

| Claim or mechanism | Disposition after this actual audit |
|---|---|
| No good-place poles; local half-pole branches | Classical/source-level; not residual novelty |
| All nonisotrivial characteristic-zero maps in the frozen family have finitely many rational periodic points | S2-owned; not new |
| Bad-place quantitative bounds at `a=-1` | S1-owned; not new |
| Completed-field full binary horseshoe | S3-owned; not new |
| One-pole seven-row atlas and ordinary sign lift | C418-owned; not new |
| Pure-sign Laurent base-change atlas | Short C418 deduction; not a separate contract |
| Four-cycle witness, finite-cycle zeta formula | Elementary witnesses/consequences; not separate novelty |
| Cross-orbit mixed sign product forces `UV in k*` and a monomial pair | Author residual claim, proved in the package; not found in inspected statements |
| A genuinely mixed orbit forces `a in {+/-1,+/-2,+/-1/2}` | Author residual claim, with all-field hand proof; independent review required |
| 64 actual rational labels and two exact if-and-only-if edge guards for every five-term parameter | Author residual parameterwise classification, beyond bare finite cardinality; its paper-level materiality is not established by correctness alone |

## Admission judgment, not a novelty certificate

The source-first gate did not reveal an exact ownership collision for the
three residual claims in the last rows. It **did** eliminate finiteness,
local coding, one-pole classification, the low-period example and zeta
packaging as possible novelty. The remaining theorem concerns the entire
Laurent parameter class and a new global compatibility obstruction, not
the next coefficient value of an old map. Nevertheless, much of its proof
architecture is inherited from C418, and its exceptional part is an exact
finite graph rather than a flattened sharp cycle/parameter table.

**Author recommendation: HOLD FOR NONAUTHOR SUBSTANTIVE REVIEW.** The
mathematical theorem is formulated and proved; no admission is asserted.
Review must decide both correctness and whether the independent residual
is substantial enough under this batch's stricter paper criterion. If the
full normal-form cycle-stratum table is indispensable, the current result
should remain auxiliary/hold rather than count as an admitted contract.
Do not repair a negative materiality judgment by running a larger census.

`NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged and unconditional.

## Independent-review correction before admission

The first source-ledger version incorrectly substituted `d=2` into the
numerical estimate at the end of Ingram's Section 3. The nonauthor reviewer
identified the section-wide `d>=3` assumption and its explicit routing of
quadratics to Theorem 1.4/Section 4. The author then re-opened and read that
primary passage (Section 3 opening, printed page 9), and checked the same
warning already present in C418's local source audit. The unsupported
quadratic numerical comparison has been removed from S1 and its
application paragraph above. No replacement numerical bound is claimed.
The error was in the source audit, not an input to the independent hand
proof or a change to its 64-state theorem. The frozen mathematical proof
bytes remain unchanged. This correction is acknowledged, not silently
presented as if the initial ledger had been accurate.
