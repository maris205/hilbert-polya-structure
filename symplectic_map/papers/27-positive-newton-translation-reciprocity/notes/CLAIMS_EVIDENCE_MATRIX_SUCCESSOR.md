# Paper 27 successor claims--evidence matrix

author_disposition: AUTHOR_STOP_FOR_FRESH_INDEPENDENT_PROOF_SCOPE_REVIEW
controlling_event: B07-E0234-P27-RECOVERY-PLAN-PASS-CONSUMPTION-AND-S1-PROOF-SCOPE-AUTHORIZATION
candidate_id: positive_newton_translation_reciprocity_v5
artifact_role: prospective claim and dependency control; not a review PASS
external_effect: none

## 1. Status vocabulary

The exact statuses used below are:

- **PROVED-SUCCESSOR:** proved symbolically in PROOF_PACKAGE_SUCCESSOR.md;
- **INHERITED-PROVED:** retained from the old package and rederived in the
  successor;
- **ABSORBED-BACKGROUND:** classical or contextual material that receives no
  novelty or page-mass credit;
- **FIXTURE-VERIFIED:** illustrative arithmetic derived from frozen inputs;
- **BOUNDARY-WITNESS:** an exact counterexample outside or at the edge of the
  headline hypotheses;
- **ASSUMPTION:** an explicit theorem hypothesis;
- **ANTI-CLAIM:** a statement the paper must not make;
- **TYPESETTING-REQUIRED:** a later source/build obligation, not mathematics;
- **REVIEW-REQUIRED:** not promoted until a wholly fresh review is all zero.

No citation or fixture substitutes for a universal proof.  No row below
authorizes a manuscript edit or build.

## 2. Assumptions and typed inputs

| ID | Exact item | Status | Evidence anchor | Planned manuscript location | Fresh review test |
|---|---|---|---|---|---|
| A01 | \(K\) has characteristic zero. | ASSUMPTION | successor proof §1 | setup/main theorem | Confirm every derivative/Jacobian use depends on this. |
| A02 | \(r\ge3\). | ASSUMPTION | successor proof §1 | setup/main theorem | Ensure \(r=2\) remains only a boundary. |
| A03 | \(E_V,E_W\) are finite, nonempty, collected subsets of \(\mathbb Z_{\ge2}^r\), with nonzero coefficients. | ASSUMPTION | successor proof §1 | setup/main theorem | Reject zero/unit exponent or uncollected-term drift. |
| A04 | Incoming leading tuples occupy disjoint algebraically independent blocks. | ASSUMPTION / CONSTRUCTION | successor proof §2.5 | typed setup | Check seed construction is injective. |
| A05 | Every invoked arrow has a nonempty strict homogeneous integer domain. | ASSUMPTION | successor proof §§2.3–2.4 | typed cells | Check no empty cell is treated as evidence. |
| A06 | Literal reflected labels belong to the appropriate support and are uniquely selected. | ASSUMPTION | successor proof §§2.2, 5 | reciprocity theorem | Separate support availability from matrix algebra. |
| A07 | Fixed lower/new comparison-row sets and all projection domains are frozen before evaluating a robustness radius. | ASSUMPTION | successor proof §6 | robustness theorem | Reject invented or post hoc numerical rows. |
| A08 | An infinite-branch conclusion is invoked only for an infinite certified strict branch. | ASSUMPTION | successor proof §4 | theorem and wall section | Finite termination at a tie/carry failure must remain allowed. |

## 3. Typed-edge and survival claims

| ID | Exact claim | Status | Proof/evidence anchor | Planned manuscript location | Kill condition / reviewer test |
|---|---|---|---|---|---|
| T01 | \(A_\alpha=\mathbf1\alpha^{\mathsf T}-I\), \(B_\beta=\mathbf1\beta^{\mathsf T}-I\), and the formal pair map is \(\Phi_e(u,w)=(B_\beta A_\alpha u,A_\alpha u)\). | INHERITED-PROVED | proof (2.1)–(2.3) | setup | Recompute componentwise gradient weights. |
| T02 | Source \(V\)-selector, first carry, source \(W\)-selector, and second carry are four distinct printed families. | PROVED-SUCCESSOR | proof (2.2) | typed cells | Any opaque PairGaps replacement kills the claim. |
| T03 | Reflected \(W\)-first and \(V\)-second selectors/carries are printed in inverse phase order. | PROVED-SUCCESSOR | proof (2.4)–(2.7) | typed cells/reciprocity | Wrong order or silently assumed support closure kills it. |
| T04 | Target selectors/carries and transformed membership are explicit composed linear forms. | PROVED-SUCCESSOR | proof (2.10)–(2.12) | typed arrows | A source-only margin cannot prove this. |
| T05 | A complete arrow certificate gives \(\Phi_e(\mathcal C_{e\to f}^+)\subseteq\mathcal S_f^+\). | PROVED-SUCCESSOR | typed inclusion lemma (2.14) | typed arrows | Missing any target/reflected/\(D_f\) row kills inclusion. |
| T06 | Multiple possible targets require separate arrow domains. | PROVED-SUCCESSOR / DEFINITION | proof after (2.14) | typed arrows | Node notation must not conceal a partition. |
| T07 | Every positive integer pair seed has disjoint algebraically independent leading-block realization. | PROVED-SUCCESSOR | seed lemma §2.5 | setup/fixture | Check injectivity of the exponent map. |
| T08 | A positive exposed face has nonzero grouped Hessian determinant for every nonzero coefficient choice in the class. | INHERITED-PROVED | proof (3.1)–(3.4) | survival section | Unique secondary-lowest group and coefficient must be checked. |
| T09 | The grouped Hessian proof does not select a vertex on a tied primary face. | PROVED-SUCCESSOR / SCOPE | proof §3.1 | survival warning | Any tied-selector promotion kills it. |
| T10 | The face-gradient tuple is algebraically independent in characteristic zero. | ABSORBED-BACKGROUND plus typed use | Jacobian lemma §3.2 | survival section | Classical lemma gets no novelty credit. |
| T11 | Algebraic independence of incoming initial forms makes selected substitution injective in the associated graded ring. | PROVED-SUCCESSOR | proof §3.3 | survival section | Noninjective or merely generic substitution kills it. |
| T12 | Fresh internal noncancellation and fresh/old separation are logically distinct. | PROVED-SUCCESSOR | proof §§3.3–3.4 | survival section | A carry cannot replace the Jacobian argument or conversely. |
| T13 | Forward and reflected-inverse leading tuples survive every finite certified prefix in the correct phase order. | INHERITED-PROVED, expanded | survival lemma §3.5 | survival section | Missing selector/carry/target certificate stops the word. |

## 4. Translation, envelope, equality, and tail

| ID | Exact claim | Status | Proof/evidence anchor | Planned manuscript location | Kill condition / reviewer test |
|---|---|---|---|---|---|
| T14 | Every certified two-phase step satisfies \(u'=u+\delta_{\alpha,\beta}(u)\mathbf1\), and strict integer branches have \(\delta\ge1\). | INHERITED-PROVED | proof (4.1)–(4.3) | translation section | Second carry must equal \(\delta>0\). |
| T15 | Within a total class, one representative is frozen; an internal tie persists on the diagonal ray. | PROVED-SUCCESSOR | proof §4.1 | envelope section | A tie-only line cannot count as a strict selector. |
| T16 | The \(W\)-envelope uses \(N_s=-\min_{|\beta|=s}\beta\cdot u_0\). | PROVED-SUCCESSOR | proof (4.5), (4.8) | envelope section | Wrong sign changes the selector order. |
| T17 | \(g(t)=h_V(u_0+t\mathbf1)-t\) is strictly increasing. | INHERITED-PROVED | proof (4.7) | envelope section | Positivity of slopes must be explicit. |
| T18 | Strictly active totals are ordered by slope, and discrete sampling can skip but never repeat a wall. | PROVED-SUCCESSOR | proof §§4.2–4.3 | envelope section | Returning to a lower slope or counting a tie kills it. |
| T19 | \(N_{\rm pair}\) counts update indices where the ordered selector pair changes; simultaneous component switches count once. | PROVED-SUCCESSOR / DEFINITION | proof (4.11) | theorem/envelope section | Component-change sum must not be mislabeled as pair count. |
| T20 | \(N_{\rm pair}\le(q_V-1)+(q_W-1)\le d_V+d_W-2\). | PROVED-SUCCESSOR | proof (4.12) | main theorem | Check all cardinalities and the union bound. |
| T21 | Equality in \(d_V+d_W-2\) holds iff all total classes are uniquely available, each owns and receives a sampled strict interval, and no update switches both sides. | PROVED-SUCCESSOR | exact equality theorem §4.3 | envelope theorem | Tie-only upper-hull contact or simultaneous switching kills equality. |
| T22 | The equality theorem characterizes an existing branch but realizes no prescribed pattern. | ANTI-CLAIM boundary | proof after equality theorem | limitations | Any universal realization language is forbidden. |
| T23 | On the stationary tail, \(t_{n+1}=\lambda t_n+\mu\) with \(\lambda=(|\alpha|-1)(|\beta|-1)\), \(\mu=((|\beta|-1)\alpha-\beta)\cdot u_0\), and the closed solution uses the global origin. | INHERITED-PROVED, expanded | proof (4.13)–(4.14) | tail section | Resetting \(u_0\) at the last switch changes the claim. |

## 5. Reciprocity and robustness

| ID | Exact claim | Status | Proof/evidence anchor | Planned manuscript location | Kill condition / reviewer test |
|---|---|---|---|---|---|
| T24 | A nonempty strict homogeneous linear cell containing an integer point has \(U_e=\mathbb R^r\). | PROVED-SUCCESSOR | full-span lemma §5 | reciprocity section | Scaling and each coordinate perturbation must stay integral and strict. |
| T25 | \(\det A_\alpha=(-1)^r(1-|\alpha|)\ne0\), hence \(V_e=\mathbb R^r\). | PROVED-SUCCESSOR | proof (5.1) | reciprocity section | Positive support and characteristic-independent real matrix identity required. |
| T26 | Label-to-matrix maps are injective, so global reflected identities force \(R\alpha,R\beta\). | PROVED-SUCCESSOR | proof (5.2)–(5.3) | reciprocity section | A nonliteral/proper-span example is impossible here. |
| T27 | Finite-word phase reciprocity is equivalent to literal reflected support availability, unique selection, carries, and target certificates edge by edge. | PROVED-SUCCESSOR | finite-word theorem §5 | reciprocity section | Scalar degree equality or one unrelated seed is insufficient. |
| T28 | The four robustness projections are \(u,A_\alpha u,Ru,RA_\alpha u\). | PROVED-SUCCESSOR / DEFINITION | proof (6.1) | robustness section | A projection/domain change is a new theorem input. |
| T29 | With fixed row families, \(m_\pm,L_\pm\) are exact minima/maxima of the composed rows. | PROVED-SUCCESSOR / DEFINITION | proof (6.2) | robustness section | No unlisted row or post hoc set change. |
| T30 | \(\rho_e(z)=\min(m_+,m_-)/(2\max\{1,L_+,L_-\})\) preserves more than half of every listed margin under \(\ell_\infty\) state perturbation. | PROVED-SUCCESSOR | half-margin theorem (6.3)–(6.4) | robustness section | Perturbing supports/rows or omitting the dual-norm bound kills it. |
| T31 | The robustness result is one fixed edge and one forward/reflected step only. | ANTI-CLAIM boundary | proof end §6 | theorem/limitations | No target-core inference, multi-edge induction, or global invariant. |
| T32 | No numerical radius is claimed before a concrete finite row family and state are supplied. | SCOPE / REVIEW-REQUIRED | proof §6 | robustness remark | Invented numerical margins are forbidden. |

## 6. Fixture and boundary evidence

| ID | Exact datum | Status | Evidence anchor | Planned manuscript location | Independent check |
|---|---|---|---|---|---|
| F01 | \(C_{21}=I+\mathbf1(90,19,22)\) and \(C_{22}=I+\mathbf1(18,55,70)\). | FIXTURE-VERIFIED | proof (7.1) | fixture | Multiply \(B_2A_1,B_2A_2\) by hand. |
| F02 | \(K_1,K_2,T_{21},T_{22}\) are the complete printed source/target score rows. | FIXTURE-VERIFIED | proof (7.2)–(7.3) | fixture | Recompute all row products. |
| F03 | \(\kappa_{21},\kappa_{22},\tau_{21},\tau_{22}\) are the complete target carry rows. | FIXTURE-VERIFIED | proof (7.4)–(7.5) | fixture | Recompute both matrix differences and row products. |
| F04 | P1–P3 and Q1–Q3 are six full pairs, all with \(w=\mathbf1\). | FIXTURE-VERIFIED / canonical completion | proof §7.2 | fixture | Check first carries, not merely \(u\)-scores. |
| F05 | Every source score, forward carry, reflected score, and reflected carry in §7.3 is positive. | FIXTURE-VERIFIED | proof §7.3 | fixture tables | Recalculate each entry. |
| F06 | Every target/reflected-target score and both target carries in §7.4 are positive. | FIXTURE-VERIFIED | proof §7.4 | fixture tables | Recalculate each entry and phase order. |
| F07 | The literal typed path is \(e_1\to e_2\to e_2\) and the reflected path has the same phase-indexed cells. | FIXTURE-VERIFIED | proof §§7.2–7.4 | fixture graph | Confirm full transformed pair, not only \(u'\). |
| F08 | Seed determinants are \(1,-1\); separately \(\det A_1=11,\det A_2=12\). | FIXTURE-VERIFIED | proof (7.6)–(7.7) | fixture | Do not conflate seed and phase-matrix determinants. |
| F09 | At \(u=(1,10,1),w=\mathbf1\), missing \(R\gamma\) gives \((57,48,57)\ne(83,74,83)\) at \(n=1\). | BOUNDARY-WITNESS | proof (7.8) | reciprocity boundary | Verify no tie or failed carry causes the mismatch. |
| F10 | Characteristic-\(2\) derivative disappearance is a positive-characteristic failure. | BOUNDARY-WITNESS | proof §8 | limitations | Must remain outside headline class. |
| F11 | \(u=(2,2,1)\) is a strict retained-row example but ties \(a_1,\gamma\) when their comparison row is deleted. | BOUNDARY-WITNESS | proof §§6, 8 | robustness boundary | Recompute all retained rows. |
| F12 | \(u=(2,1,1),w=(18,1,1)\) makes the first carry non-strict. | BOUNDARY-WITNESS | proof §8 | survival boundary | Do not assert degree survival. |
| F13 | \(V=(q_1+q_2+q_3)^3,W=(p_1-p_2)^3\) exhibits actual fresh-term cancellation outside the class. | BOUNDARY-WITNESS | proof §8 | limitations | Expand the cancellation in source. |

## 7. Background, citation, and portfolio roles

| ID | Item | Status | Evidence role | Planned manuscript location | Constraint |
|---|---|---|---|---|---|
| P01 | Symplecticity of separated shears from symmetric Hessian blocks. | ABSORBED-BACKGROUND | old package plus direct Jacobian calculation | setup | No novelty credit. |
| P02 | Characteristic-zero Jacobian criterion. | ABSORBED-BACKGROUND | proof §3.2; later verified citation if used | survival | State classical status explicitly. |
| P03 | Newton/support-function and affine-envelope language. | ABSORBED-BACKGROUND | old publication scope | related work/setup | No priority claim. |
| P04 | Papers 20–26 own stationary spectral, selector-exchange, support-rank, and planar Newton-envelope axes. | PORTFOLIO EXCLUSION | inherited portfolio lock | related work/limitations | Do not import their headline claims. |
| P05 | Paper28 owns rooted primitive pair words, normal-fan iff, monodromy, and decoder. | PORTFOLIO EXCLUSION | Batch07 recovery boundary | limitations | A finite typed word here is a proof index, not a word-realization theorem. |
| P06 | Failed Papers29–31 candidate material receives no page or novelty credit. | PORTFOLIO EXCLUSION | immutable Batch07 history | omitted from manuscript except necessary positioning | No replacement-axis drift. |

## 8. Anti-claims and source/build obligations

| ID | Forbidden or required statement | Status | Control anchor | Later verification |
|---|---|---|---|---|
| X01 | No proper-span/nonliteral observable-selector example under a nonempty strict homogeneous integer cell. | ANTI-CLAIM | proof §5 | Search source for contradictory language. |
| X02 | No global reflection closure, reversor, conjugacy, or classification. | ANTI-CLAIM | proof §§1, 8 | Static source review. |
| X03 | No universal equality-pattern realization. | ANTI-CLAIM | proof §4.3 | Static source review. |
| X04 | No support, exponent-row, label-set, or projection-domain perturbation. | ANTI-CLAIM | proof §6 | Static source review. |
| X05 | No target-core inclusion inferred from M5, multi-edge invariant, or all-iterate robustness. | ANTI-CLAIM | proof §6 | Static source review. |
| X06 | No positive-characteristic or \(r=2\) theorem. | ANTI-CLAIM | proof §§3.6, 8 | Static source review. |
| X07 | No entropy, higher dynamical degree, minimal scalar recurrence, or Perron-degree claim. | ANTI-CLAIM | inherited boundary | Static source review. |
| X08 | Fixture arithmetic is illustrative, not universal evidence. | ANTI-CLAIM | proof §9 | Theorem proofs must precede/use no fixture premise. |
| G01 | The manuscript must force a page boundary before references and emit BATCH07_REFERENCE_START_PAGE as a log sentinel. | TYPESETTING-REQUIRED | recovery plan §5 | Build validator; not visible prose. |
| G02 | Measured proof-content pages must be 24–28, references excluded. | TYPESETTING-REQUIRED | recovery plan §5 | Sentinel minus one. |
| G03 | All six modules must contribute 9.5–13 genuine pages; current allocation is 11.7. | REVIEW-REQUIRED | successor proof §10 | Fresh source reviewer and build page check. |
| G04 | Zero overfull boxes and no undispositioned warnings. | TYPESETTING-REQUIRED | recovery plan §5 | Two-root build logs. |
| G05 | No governance text, internal paths, hashes, event IDs, reviewer identities, or provenance narrative in the manuscript. | TYPESETTING-REQUIRED | recovery plan §5 | Static source review. |
| G06 | Local anonymous evidence only; no submission, upload, hosting, push, message, identity disclosure, or other external effect. | GOVERNANCE | E0234 | Every later gate. |

## 9. Dependency crosswalk

The theorem dependency order is:

\[
\mathrm{A01\!-\!A08}
\to \mathrm{T01\!-\!T07}
\to \mathrm{T08\!-\!T13}
\to \mathrm{T14\!-\!T23}.
\]
Here A08 is the direct infinite-certified-branch guard on T18–T23; those
branch-count, equality, and tail claims are unavailable on a finite or
uncertified word.
The independent reciprocity branch is
\[
\mathrm{T02\!-\!T07}
\to\mathrm{T24\!-\!T27},
\]
and the local robustness branch is
\[
\mathrm{T02\!-\!T05}+\mathrm{A07}
\to\mathrm{T28\!-\!T32}.
\]
F01–F13 verify exact arithmetic and failure boundaries only.  P01–P06
position or exclude claims; they prove none of T01–T32.

## 10. Review stop

A wholly fresh proof/scope reviewer must rederive every PROVED-SUCCESSOR and
INHERITED-PROVED row, audit every fixture entry, confirm every anti-claim and
page allocation, and return an all-zero census before any source lock or
manuscript edit opens.  This matrix claims no independent PASS and creates no
lock, source, build, PDF, release, Paper28, or external authority.

BATCH07_P27_CLAIMS_EVIDENCE_MATRIX_SUCCESSOR_AUTHOR_STOP
