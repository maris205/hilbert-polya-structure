# C429–C433: five admitted questions and manuscript outline

2026-09-09 UTC. Research state: **FIVE_INDEPENDENT_CONTRACTS_ADMITTED**,
by [the actual admission decisions](ADMISSION_DECISIONS.md).
Outline state: **APPROVED_AFTER_THREE_TARGETED_REPAIRS**.
Root closes the gate at the actual 2026-09-09 20:24 UTC checkpoint after
reading the complete independent review and its targeted verification.
See [the preserved initial finding and repair readback](REVIEW_OUTLINE.md).
The C-numbers below are now the one-to-one manuscript allocation;
the five exclusive drafting tasks are authorized for activation.
No completed manuscript, PDF, evaluation or paper is claimed by this status.
The mathematical questions are frozen, but an outline correction may
change presentation without changing their scope or manufacturing results.

## Shared format and actual workflow

Use anonymous English mathematical articles, 11pt with approximately
one-inch margins, modular LaTeX, ordinary numbered mathematical citations,
explicit hypotheses, complete proofs and honest source subtraction.
No journal/ML conference, artificial page cap, minimum section quota,
synthetic experiment, invented author identity, funding or human review
is selected. Disclose AI-assisted preparation and current-team internal
review; neither is described as external peer review or acceptance.

The selected paper-writing workflow uses paper-plan's claim/evidence
mapping, paper-figure for useful exact mathematical comparison tables,
paper-write for complete LaTeX, paper-compile for actual PDF checks,
and two actual nonauthor manuscript review/revision passes under
auto-paper-improvement-loop. Root has read those entry instructions and
the complete writing-principles reference. Current-team review replaces
legacy GPT-5.4/MCP examples under the user's standing model/agent
contract; no external model/upload or configuration change is performed.
Do not invent revisions, empirical results, rising scores or successful
checks when the actual evidence says otherwise. Two reviews do not
mean two gratuitous reruns of unchanged mathematics.

Every central new argument must be typeset in the article or its
included appendix. A local Markdown link is not a substitute for a
proof. A precisely stated previously proved theorem may be cited with
its complete accessible reference and actual status. Newly shared
lemmas must have clear ownership and noncircular dependencies; calling
another result a companion paper does not make it published literature.
Do not present working-note IDs or file counts as mathematical novelty.

Bibliographic metadata comes from the actual checked primary records,
existing verified entries or publisher/DOI/DBLP responses, never memory.
Record inaccessible sources and unverified DOI/retraction/venue checks
honestly. Use only cited references. A specific unverified prerequisite
blocks that claim, not unrelated manuscript work. The source comparison
is bounded and makes no worldwide-firstness guarantee.

Tables below are exact theorem/hypothesis mappings, not numerical data.
Generate only tables/diagrams that clarify an actual relationship. No
plotting script, JSON fixture or decorative figure is required for a
proof-only article. If a genuine diagram is useful, its caption must
state the proved relation and all exceptions; do not draw a field
nesting or dynamical conjugacy that the theorem does not establish.

After the independent outline gate closes, authors draft within their
exclusive paths and make actual first PDFs. Root assigns separate full
manuscript reviews, adjudicates all required repairs and verifies their
affected reasoning. The unchanged Route-A v0.2.0 evaluator is read with
its required reference routing before any new formal evaluation. No
grade is assigned by this outline. Missing target controls remain
NOT_TESTABLE/INCOMPLETE, not PASS.

The final release requires two fresh deterministic builds per paper,
byte comparisons, font/text/warning checks, actual visual inspection of
every final page, exact payload ledgers and self-excluding manifests,
and independent membership verification. Preserve real baseline/revised
PDFs and failed attempts. Root integrates exact paths only after writers
stop and inspections pass, then synchronizes the configured repository
without force-push or unrelated paths. Five completed papers form a
saved continuous-run checkpoint, not a stop or an external submission.

## Activated assignments and ownership

All paths are relative to this batch. All five authors completed their
read-only input preparation before this gate closed. Root now activates
the following exclusive writing assignments; each actual handoff remains
subject to the separate full-manuscript reviews and release gates.

| Paper / working title | One independent contract | Author / exclusive path |
| --- | --- | --- |
| C429 — Polynomial periodic-data rigidity in finite characteristic | PC424-L: ordinary cycle-sum kernel equals polynomial coboundaries for all unicritical polynomials, all primes | A2 / `papers/C429_polynomial_periodic_rigidity/` |
| C430 — Native Galois fields of small wild cycles | UL4: all-level cyclic local periodic fields, oriented first-character stabilization and first-level separation | D1 / `papers/C430_native_galois_fields/` |
| C431 — Haar limits of optimal wild cycles | OM4: the full optimal-cycle measures converge over the original complete-field family to a type-I adding-machine Haar limit | A1 / `papers/C431_optimal_cycle_measures/` |
| C432 — Everywhere-local reversibility without a global reversor | RLG5: the original all-place reversibility implication fails for an explicit Hénon word, with every polynomial reversor controlled | C4 / `papers/C432_local_global_reversibility/` |
| C433 — Finite detection of multiplicative periodic data | FCP10: exact degree-only finite decision of cofinite ordinary products for all derivative-zero polynomial maps and rational weights | A3 / `papers/C433_inseparable_finite_products/` |

Authors own only their allocated new manuscript directories. Root owns
this outline, state, admission, final evaluation/release and Git.
Reviewers use disjoint review paths. The old proof, source and review
files remain frozen. No sixth slot is extracted from a shared lemma.

## C429: the full unicritical additive equality

One-sentence contribution: for every prime $p$, every $d\ge2$, every
$c\in\overline{\mathbb F}_p$ and every polynomial $h$, the ordinary
cycle sums for $f=x^d+c$ vanish exactly when $h=Q\circ f-Q$ for
a polynomial $Q$, with explicit two-return certificates.

The native skew map is $(x,y)\mapsto(f(x),y+h(x))$ on the full
affine plane. Count each primitive-cycle point once, including periods
divisible by $p$. No extension of the observable class to rational $h$
or of the base class to arbitrary polynomials is claimed.

| Main claim | Accepted proof input | Planned location |
| --- | --- | --- |
| Normal-form detection and the complete quadratic equality | `continuation_round3/a1_periodic_normal_form/PROOF_PACKAGE.md` and its explicitly routed inherited lemmas | §§2–4 |
| Every degree with $d\not\equiv1\pmod p$ | `continuation_round4/a2_unicritical_carry_extension/PROOF_PACKAGE.md` | §5 |
| The formerly derivative-blind congruence class | `continuation_round5/a2_excluded_congruence/PROOF_PACKAGE.md` | §§6–7 |
| Characteristic two and full finite certificates | `continuation_round5/a2_excluded_congruence/CHARACTERISTIC_TWO.md` | §7 and exact bound table |

Structure: exact theorem and motivation; credited source/normal-form
inputs; cyclic algebra and pairing; stable leading coefficient and
adjacent-level argument; full degree extension; Hasse detector and
adaptive cut; characteristic-two anchors and effective corollaries;
limitations. Give the actual stabilization proof, not just a matrix
formula followed by an appeal to computation.

For an integer $M\ge1$ with $\deg h\le M$, including the zero
polynomial as a separate trivial input, define

$$F_j=f^{\circ j}-x,\qquad
H_j(h)=\sum_{i=0}^{j-1}h\circ f^{\circ i}.$$

The exact finite tests at each of the two specified return levels are:

| Regime | Required divisibility at each level $j$ |
| --- | --- |
| $p\nmid d(d-1)$ | $F_j\mid F_j'H_j(h)$ |
| $p\mid d$ | $F_j\mid H_j(h)$, since $F_j'=-1$ |
| $p\mid d-1$ | $F_j\mid D^{[P]}F_j\,H_j(h)^P$, $P=p^{v_p(d-1)}$ |

Here $D^{[P]}u(x)$ is the coefficient of $z^P$ in $u(x+z)$.
Passing the applicable pair of tests is equivalent to the polynomial
coboundary condition; these are not only necessary conditions.
For the first two rows, equivalently $d\not\equiv1\pmod p$, use
$n=3\lfloor\log_d M\rfloor+4$ and $n+1$, detecting a primitive
period at most $n+1$ with iterate degree at most $d^5M^3$.
For $d\equiv1\pmod p$, put $P=p^{v_p(d-1)}$ and use
$j=7\lfloor\log_d(PM)\rfloor+22$ and $j+1$, testing
$F_j\mid D^{[P]}F_j\,H_j(h)^P$, with primitive-period bound
$j+1$ and iterate-degree bound $d^{23}(PM)^7$. Preserve the
ordinary-root equivalence and all zero/constant branches. The displayed
degree bounds concern the iterates, not every unreduced product in a
test or an optimized running-time bound.

The proof/parameter/bound table should compare the three derivative
regimes and name their actual hypotheses, not suggest equal costs.
Credit classical residue/normal-form/Hasse machinery and the actual
bounded source comparison in `continuation_round3/NOVELTY_CHECK_PC_L.md`
and the later admission source updates. Known Livšic questions are not
claimed newly posed; the entire all-parameter equality is the increment.
This is one paper, not separate quadratic, degree and characteristic papers.

## C430: the fixed-base local arithmetic of every small wild cycle

One-sentence contribution: for every odd prime $p$, over
$K=\overline{\mathbb F}_p((s))$,
every canonical small $p^e$-cycle of $(1+s)z+z^2$ generates a
cyclic degree-$p^e$ splitting field, with a stabilized native-oriented
degree-$p$ character for $e\ge2$ and separation from level one.

| Main claim | Accepted proof input | Planned location |
| --- | --- | --- |
| Canonical factors, contacts and full all-level local inertia | `continuation_round3/a3_interlevel_contacts/PROOF_SUPPLEMENT.md`, `FULL_LOCAL_INERTIA.md` | §§2–4 |
| Native-oriented AS-class stabilization and first-level intersection | `continuation_round3/a3_interlevel_contacts/ORIENTED_QUOTIENT_STABILIZATION.md` | §5 |
| First and second field ramification invariants | `continuation_round4/a3_first_quotient_ramification/PROOF_PACKAGE.md`, `SECOND_LAYER_BREAKS.md` | §6 |
| Eventual higher native quotient tower, as an explicitly dependent same-paper consequence | `continuation_round5/a3_eventual_quotient_tower/PROOF_PACKAGE.md` and its cited OM4 contact/compact-limit input | §7 or a fully included appendix |

State the exact Hensel factor $M_e$ of the quotient of successive
$p$-power returns, over one fixed $K$ and one separable closure.
Prove degree $p^e$, splitting and native generator simultaneously;
a root valuation with denominator $p$ alone does not prove them.
Orient every Artin--Schreier generator by $\sigma(y)-y=+1$.
The conclusions $[a_e]=[a_2]$ and $F_e=F_2$ concern classes and
embedded degree-$p$ fields, not identical raw resolvent series or
nesting of the entire $L_e$. State $L_1\cap L_e=K$ for all $e\ge2$.

Retain the accepted field upper breaks of $L_2/K$,
$(2(p-1),2p(p-1))$, and its different
$(p-1)(2p^3-2p^2+3p-1)$. Do not replace a field different with
the root-order discriminant or resurrect the withdrawn intermediate value.
An exact field/character table may distinguish $L_e$, $F_e$ and the
eventual $K_j$. It must not depict the original $L_e$ as nested.

If the eventual tower is included, state precisely
$\forall j\ \exists E_j\ \forall e\ge E_j$ equality of native
characters modulo $p^j$ on the whole Galois group. It gives a unique
continuous surjection to $\mathbb Z_p$ and nested kernel fields;
it gives neither $E_j=j$ nor $K_j=L_j$. Credit the necessary C431
contact/limit theorem explicitly, or typeset its required lemma locally.
The core UL4 proof does not depend on this later corollary.

Sources: the actual comparisons in
`continuation_round4/NOVELTY_CHECK_UNIFORM_LOCAL.md`,
`continuation_round4/x2_uniform_local_source_admission/REPORT.md`, and
`continuation_round5/x1_eventual_tower_sources/REPORT.md`.
Deduct Lindahl--Rivera-Letelier geometry, Keating's actual denominator/
norm-field mechanisms, classical ramification and character extraction.
Global dynatomic components, all Witt coordinates and full higher
field intersections remain outside this local contract.

## C431: convergence of the complete optimal-cycle sequence

One-sentence contribution: for every allowed complete algebraically
closed characteristic-$p$ field and multiplier near one, the full
sequence of optimal wild cycle measures converges to Haar measure
on a compact type-I $\mathbb Z_p$ adding-machine limit.

The domain is the Berkovich projective line over every complete
algebraically closed ultrametric $K$ of odd characteristic, with
$P_\lambda(z)=\lambda z+z^2$ and $0<|\lambda-1|<1$.
The measures are real probabilities
$\mu_e=p^{-e}\sum_{\alpha\in\Pi_e}\delta_\alpha$, not
characteristic-$p$ traces or measures on all periodic points.

| Main claim | Accepted proof input | Planned location |
| --- | --- | --- |
| All-higher-level contact identity and growing anchor estimate | `continuation_round4/a1_optimal_cycle_measures/PROOF_PACKAGE.md` | §§2–4 |
| Compactness, Hausdorff/Wasserstein limit and exact support | same A1 proof plus `continuation_round4/d1_isometric_cycle_limit/PROOF_PACKAGE.md` | §§4–5 |
| Aperiodicity, adding-machine conjugacy and unique Haar limit | complete D1 proof with its actual noncircular contact input | §6 |

Structure: the original question and exact main theorem; the canonical
small cycles and native distances; arbitrary-$K$ coefficient realization;
the unbounded-anchor contact calculation; couplings and compact limit;
aperiodicity and inverse-limit conjugacy; consequences and limitations.
Do not replace the full sequence by a convergent subsequence or the
arbitrary complete field by a formal coefficient-field special case.

With $s=\lambda-1$, $v(s)=1$, $r=(p-1)/p$ and $\beta\in\Pi_d$,
retain the exact $c_d=(p-1)p^{-d-1}v((P_\lambda^{\circ p^d})'(\beta)-1)$,
the all-$e>d$ average contact identity and
$c_d\ge d r^3+r^2(1+1/p)$. State
$d_H(\Pi_d,\mathcal A),W_\infty(\mu_d,\mu)\le|s|^{c_d}\to0$.
Define the coupling and metric before using these bounds. The closure
of all old cycles is not uniquely ergodic merely because the limit is.
Aperiodicity needs its actual contact proof.

An exact implication table can separate compact containing closure,
limit set, uniform cycle measures and Haar measure; it replaces any
decorative numerical convergence plot. Sources and ownership are in
`continuation_round4/NOVELTY_CHECK_OPTIMAL_MEASURES.md` and
`continuation_round4/x1_optimal_measure_sources/REPORT.md`.
State precisely which version of Lindahl--Rivera-Letelier's Problem 1.3
is answered, without claiming verified current-open status. Deduct the
classical isometric inverse-limit/Haar step and distinguish other
crucial/equilibrium measures. UL4 inertia is not a premise of this
standalone proof; only the later C430 tower consequence uses this result.

## C432: the original all-place reversibility implication fails

One-sentence contribution: an explicit four-factor Hénon word over
$\mathbb Q(\sqrt7)$ has a polynomial reversor in every completion
but none over the number field, even when all polynomial degrees and
orders of the proposed reversor are allowed.

The full source is
`continuation_round5/c4_reversor_local_global/PROOF_PACKAGE.md`
with its report, complete E5 mathematics and B1 substantiality review
routed from admission Section 5. Keep the rightmost-first convention.
For $H_{c,d}(x,y)=(y,cy^d-x)$ take

$$F_a=H_{a,7}H_{a^{-2},15}H_{a^2,15}H_{a^{-1},7}.$$

The whole polynomial reversor set over every number field $L$
with $a\in L^\times$ is $\{F_a^jR_t:j\in\mathbb Z,\ t\in L^*,\ t^8=a^2\}$,
where $R_t(x,y)=(t^{-1}y,tx)$. At $a=4$, the Wang class $16$
is an eighth power in every actual completion of $K=\mathbb Q(\sqrt7)$
but not in $K$. Do not restrict hypothetical reversors to affine maps,
involutions or a bounded degree in stating the negative theorem.

| Main claim | Proof component | Planned location |
| --- | --- | --- |
| Exhaustive polynomial reversing coset | full-group amalgam/axis proof, primitive degree labels, pointwise-axis centralizer $\mu_8$ | §§2–4 |
| Original-field descent of every reversor | removal of a native field-defined power and exact scalar equation | §4 |
| Every finite and infinite local witness, but no global one | complete Wang-class checks over the actual completions | §5 |
| Failure of the simpler two-factor ansatz | retained nonlinear-global-reversor control | §6 |

Deduct Wang, Jung--van der Kulk, reversing-symmetry normal forms and
Cantat--Dujardin's already checked scalar-twist centralizer mechanism
for arbitrary pairs. The increment is its complete realization for
the constrained inverse pair $(F,F^{-1})$, including exclusion of
alternative polynomial reversors. A short exact local-place table
should separate odd, dyadic and the two real places of this field;
$\mathbb Q(\sqrt7)$ has no complex places. The table uses the actual
field facts and does not replace their proofs. No minimal-degree or universal
classification of all reversible words is claimed.

## C433: the complete derivative-zero multiplicative finite decision

One-sentence contribution: all but finitely many ordinary cycle products
of any rational weight for any derivative-zero polynomial equal one
exactly when explicit polynomial tests through a degree-only bound pass.

Use the entire final 713-line
`continuation_round10/a3_inseparable_finite_cp/REPORT.md`, the complete
E8 review and X2 source/substance report. Its full proof is self-contained;
do not replace it by a citation to untyped working notes or describe
the shared root/R9/A1 mechanism as independent origination.

| Main claim | Full proof passage | Planned location |
| --- | --- | --- |
| Nonmonic normalization and exact ordinary CP ideal | author §§3–4 | §§2–3 |
| General-polynomial Laurent representation and fixed-$S$ cutoff | author §§5–6 | §§4–5 |
| Unknown exceptional-period bound from split ranks and persistence | author §7 | §6 |
| Exact coefficient-independent finite decision | author §8 | §7 |

For every prime and every $f\in\overline{\mathbb F}_p[x]$ with
$f'=0$, $d=\deg f\ge2$, and $g=A/B$ with nonzero coprime
$A,B\in\overline{\mathbb F}_p[x]$, set
$m=\max(\deg A,\deg B)$, $b=\lceil m/(d-1)\rceil+1$,
$D=2b^2$, $N=6b^2+1$, and define

$$F_n=f^{\circ n}-x,\qquad
H_n=\prod_{i=0}^{n-1}A(f^{\circ i}(x))-
    \prod_{i=0}^{n-1}B(f^{\circ i}(x)),\qquad
S_* =\prod_{r=1}^{D}F_r.$$

Condition (CP) says that all but finitely many ordinary primitive
affine cycles $O$ avoid the zeros and poles of $g$ and satisfy
$\prod_{x\in O}g(x)=1$. Count every distinct point once using the
original one-step map. State exactly
$\mathrm{(CP)}\iff F_n\mid S_*H_n$ for every $1\le n\le N$.
Every positive return is tested; the condition retains native wild
periods, unequal degrees, all support multiplicities and $m=0$.
The skew map $(x,y)\mapsto(f(x),g(x)y)$ is defined on
$(\mathbb A^1\setminus V(AB))\times\mathbb G_m$ with values in
$\mathbb A^1\times\mathbb G_m$. This one-step domain need not be
forward invariant; iteration along an admissible cycle is well-defined.
There is no claimed global inverse or extension across poles.

A product-visible return point satisfies $F_n(x)=0$ and $H_n(x)\ne0$
for some $n$; its cycle is product-visible. For the comparison with
derivative-filtered data, the contributing condition is
$e_n(x)H_n(x)\ne0$, with $e_n(x)=\operatorname{ord}_x F_n$
interpreted in the field, not pointwise $F_n'(x)H_n(x)\ne0$.
Native Jacobian visibility alone means $p\nmid e_r(x)$ at the
point's native period $r$. In the present derivative-zero class,
$F_n'=-1$ and $e_n(x)=1$ at every return, so derivative filtering
cannot discard a product-visible return.

Show the locally finite Laurent extraction, the two-block state
bound and high-site contraction, both full-rank evaluation maps,
and the arbitrarily long nonzero return argument in full. A finite
exceptional set is not assumed to have bounded size; each visible
cycle's length is bounded first: under (CP), every product-visible
cycle has native period at most $D$. A cycle containing both a numerator
zero and a denominator zero is a finite support exception whose
period need not satisfy that bound. Include that distinction in the
statement and final proof, not only the limitations paragraph.

An exact comparison table should distinguish fixed-$S$ certificates,
derivative-filtered visible CP and the ordinary derivative-zero
decision. It must credit Kiefer et al.'s arbitrary-field word cutoff,
classical residue/normal-form facts and the actual integrated development.
If a separable-map warning is included, prove its precise local example;
no all-level rational-observable counterexample has been constructed.
No proof of MS6, rational/algebraic transfer existence or optimized
running time is asserted. Tests can have degree $d^N$.

## Closed outline gate and continuing checkpoint

The independent reviewer read the entire original outline and actual
admission statements, checked the claim-to-proof links and material
source deductions, and tested specifically for C430/C431 circularity,
C429 characteristic/degree loss, C432 ansatz-only reversors, and C433
ordinary/visible/support confusion. Three mandatory interface repairs
were accepted by root, applied without changing the admitted mathematics,
and independently read back: zero outline must-fixes remain. The review
binds the repaired 374-line mathematical plan before this status-only
activation edit. It is not one of the two required manuscript reviews.

Baseline builds use the common fixed epoch `SOURCE_DATE_EPOCH=1788912000`
(2026-09-09 00:00:00 UTC), with `TZ=UTC` and `LC_ALL=C` where compatible.
The epoch is a deterministic build setting, not an execution timestamp.
Record actual commands and warnings. Do not install packages, overwrite
old snapshots, or invent successful builds. A first PDF is a review input,
not either of the two final clean reproducibility builds.

No new mathematics run is allocated by this plan. A later computation
requires an actual discriminating question, bounded inputs and cost;
compilation/format/release checks are recorded separately from mathematical
experiments. No automatic notification, external submission, paid API,
Route B work, changed evaluator or unrelated workspace mutation is authorized.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional for every paper.
