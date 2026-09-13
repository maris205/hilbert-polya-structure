# Source-design review summary

## Frozen candidate provenance

Candidate identifier: planar_newton_envelope_bidirectional_degree_v1

Title: Newton-Envelope Contraction for Planar Hamiltonian Product Shears: Selector Rigidity and Bidirectional Degree Growth

Two independent local candidate reviews were consumed before this source package was authored.

| Review | SHA-256 | Bytes | LF | Terminal |
|---|---|---:|---:|---|
| BATCH_06_PAPER26_CANDIDATE_REVIEW_R1.md | cc81cc410d9122bdaf6ebf8b20e57bce3cbe4fcaed17c3cc0ed5f596d9844dbe | 29824 | 611 | PAPER26_CANDIDATE_GATE_PASS_R1 |
| BATCH_06_PAPER26_CANDIDATE_REVIEW_R2.md | 164273106733f611c0d35a60cb693d5ffbf8cf1300ffb658a00abb555fbda2e1 | 26605 | 1112 | PAPER26_CANDIDATE_GATE_PASS_R2 |

The original source author did not invoke an external model, web search, numerical run, or computer algebra system. This bounded R2 repair consumes the independent R0 and R1 zero-write findings described below; it does not create a review.

## Review issues and dispositions

### 1. Tropical prediction was not yet an exact polynomial theorem

Risk: a Newton-envelope maximum can overestimate degree if top forms cancel, especially on a wall.

Disposition: the final proof begins with a coefficient-uniform exposed-face lemma. The unique minimal-\(x\) monomial supplies the exact nonzero coefficient
\[
c_{x_0,y_0}^{\,2}x_0y_0(1-x_0-y_0)
\]
in the face Hessian determinant. The characteristic-zero Jacobian criterion makes the full face-gradient pair algebraically independent. Injective substitutions and pure powers then close both forward and inverse top-form inductions.

Status: resolved without genericity.

### 2. Carries and final degree visibility were implicit

Risk: an exact fresh-gradient vector does not by itself identify the total degree of the four-coordinate iterate.

Disposition: the proof records both half-steps and uses
\[
\mathcal A_i(u)>\|u\|_\infty.
\]
For the upper carry it now sets \(A=(A_1,A_2)^\top=\mathcal A(u)\) and proves
\[
2A_1-A_2=H(u)-2u_1+u_2\ge3u_2>0,
\]
\[
2A_2-A_1=H(u)+u_1-2u_2\ge3u_1>0.
\]
Together with \(e,f\ge2\), these inequalities show that both components of \(BA\) strictly exceed both components of \(A\). Forward, the final position block is visible. Backward, the reversed phases make the final momentum block visible. Old position and momentum blocks are compared explicitly at every induction step.

Status: resolved.

### 3. The initial period-two language conflated selectors and ratios

Risk: an alternating selector word might be misreported as a nontrivial projective two-cycle.

Disposition: the projective map is proved globally contracting in log distance. It has one fixed ray and no nontrivial numerical cycle. At a wall, strict orbits alternate adjacent chambers while converging to the fixed ray. The terminology is frozen throughout all ten source files.

Status: resolved.

### 4. Pointwise derivative control was weaker than uniform contraction

Risk: the chamberwise logarithmic derivative is below one at each point, but its supremum could still equal one.

Disposition: for each fixed support exponent, the derivative magnitude extends continuously to the compactified positive half-line and tends to zero at both endpoints. Its maximum is strictly below one. Finiteness of \(E\) gives one constant; continuity and interval splitting patch across all walls.

Status: resolved.

### 5. The inverse theorem appeared to require a second asymptotic analysis

Risk: forward \(B\mathcal A\) and inverse \(\mathcal A B\) could have changing selectors, so a fixed \(AB/BA\) spectral observation was insufficient.

Disposition: positive homogeneity and the ordinary seed give the exact identity
\[
u^+_{n+1}=c_\star Bv^-_n.
\]
This directly compares the full vector sequences and their exponential rates. It does not transfer scalar-max recurrences. Section 16 now derives the inverse recurrence independently from
\[
D_\xi=A_\xi B=B^{-1}C_\xi B,
\]
handles \(s_\star\ne1\) visible-coordinate stabilization and the \(s_\star=1\) ordinary fixed seed, and treats both strict-wall products \(N_+=D_+D_-\), \(N_-=D_-D_+\) with their forward similarities and common trace and determinant.
The inverse fixed-wall case now states the selector condition in Newton coordinates: \(\kappa s_\star=r_\star\) lies on the wall, and \(Bv^-_n\) remains on that tied Newton ray.

Status: resolved.

### 6. A coarse wall algebraic-degree bound obscured stronger rigidity

Risk: treating a two-step monodromy mechanically suggested a quartic per-step algebraic number.

Disposition: adjacent wall matrices act identically on the primitive wall ray. Fixed-ray invariance makes their common multiplier rational; integrality of the matrices and primitivity of the ray make it a positive integer \(\mu\). The monodromy Perron root is \(\mu^2\), so the per-step value is \(\mu\). The uniform bound is quadratic, not quartic.

Status: resolved.

### 7. Portfolio overlap with Papers 24 and 25 needed subtraction

Risk: wall monodromy resembles Paper 24, while support-based Perron arithmetic resembles Paper 25.

Disposition: the final proposal leads with the arbitrary-face cancellation certificate and global contraction. Paper 24's special forced selector word is used only as a collision boundary. Paper 25's unbounded support-rank constructions are explicitly contrasted with rigidity in the narrower planar separated family.

Status: resolved locally; external novelty verification remains required.

### 8. Counterexamples needed theorem-level visibility

Risk: axis exponents, exponent one, mixed \(W\), or positive characteristic could be mistaken for easy extensions.

Disposition: each excluded regime is tied to the exact proof step it breaks. The axis example loses face-gradient independence; exponent one loses strict carry; mixed \(W\) loses diagonal decreasing dynamics; zero coefficients require recollecting the actual support; positive characteristic can kill Hessian or derivative coefficients. The scope boundary now says “zero coefficients or positive characteristic.” No optimality claim is made.

Status: resolved as a scope boundary.

## R0 zero-write finding and R1 disposition

The fresh independent source-design R0 review reproduced the original ten-file universe and the 120597-byte framed aggregate with SHA-256
\[
\text{af72f2bc534623c5c21f35bf139085aa0fea730c8d5b57c726ede41484f47002}.
\]
It returned FAIL / WRITE NOTHING with zero blocker, zero major finding, one minor proof-completeness finding, and zero other ambiguity. It created no review file and changed no source byte.

The finding was exact: the final sentence of the old Section 16 attributed inverse scalar recurrences to projective conjugacy or to the bridge, although
\[
\max(e v_1,f v_2)
\]
need not equal
\[
\max(v_1,v_2).
\]
Therefore the bridge could not serve as a scalar-recurrence proof.

The R1 disposition preserves every theorem assumption and conclusion while supplying the missing derivation. Section 16 now:

1. defines \(D_\xi=A_\xi B=B^{-1}C_\xi B\) and derives the actual inverse chamber recurrence;
2. proves the interior Cayley–Hamilton law and separates \(s_\star\ne1\) stable visibility from the \(s_\star=1\) ordinary fixed-seed geometric case;
3. proves that an ordinary strict inverse wall orbit has \(s_\star\ne1\);
4. defines both \(N_+=D_+D_-\) and \(N_-=D_-D_+\);
5. proves \(N_\pm=B^{-1}M_\pm B\), their common trace and determinant, and parity-wise visible-coordinate stabilization;
6. derives \(d^-_{n+4}=\tau d^-_{n+2}-\Delta d^-_n\);
7. states explicitly that all recurrence orders remain upper bounds and that the bridge proves only vector/rate comparison.

The propagated claim, question, plan, tracker, and final-proposal wording now point to this independent inverse proof. No claim, example, source, assumption, novelty statement, or authority was added.

## R1 zero-write finding and R2 disposition

The newly fresh source-design R1 reviewer and its two independent theorem/coherence auditors reproduced the repaired ten-file universe and the 131307-byte framed aggregate with SHA-256
\[
\text{87ca48e0d3fb3f851f9c10afdd05ac7dd63b283cad0da81d8d87c22c36c92142}.
\]
They returned FAIL / WRITE NOTHING with zero blocker, zero major finding, two minor findings, and one wording ambiguity. No review artifact was created and no source byte was changed.

The bounded R2 repair makes exactly three corrections:

1. the Research Question scope boundary replaces the contradictory “zero characteristic or positive characteristic” with “zero coefficients or positive characteristic”;
2. Section 6 supplies the two cross-component inequalities (6.3)–(6.4) before using \(e,f\ge2\) to promote upper-phase visibility;
3. the inverse fixed-wall statement uses the scaled Newton coordinate \(\kappa s_\star=r_\star\) and records that \(Bv^-_n\) stays on the tied Newton ray.

### Read-only downstream revalidation

- C03, C04, and B03 remain supported: the minimal-\(x\) Hessian coefficient is nonzero for collected nonzero coefficients in characteristic zero; zero coefficients are removed by recollecting \(E\), while positive characteristic remains excluded.
- C11, Protocol P4, and T07 remain supported: (6.1)–(6.4) prove both lower carry and cross-coordinate upper domination, so \(B\mathcal A(u)\) strictly dominates the whole momentum-degree vector.
- C24, Protocols P7–P8, and T14/T19/T20 remain supported: inverse selectors are evaluated at the Newton ratio \(r=\kappa s\); the corrected fixed-wall ray statement is consistent with the conjugacy, and the separate \(D_\xi\) and \(N_\pm\) scalar-recurrence proof is unchanged.
- Review issues 2, 5, and 8 are reclosed respectively by the explicit upper-carry inequalities, the scaled inverse wall coordinate plus the already complete inverse recurrence proof, and the corrected zero-coefficient/positive-characteristic boundary.

No theorem assumption, theorem conclusion, recurrence order, novelty statement, citation role, fixture, or anti-claim was enlarged.

## Skill-constrained workflow

The source design followed six local skill contracts, narrowed by the no-run and local-only gate:

- research-refine-pipeline fixed the sequence from problem anchor to final proposal and then to a claim-driven validation plan.
- research-refine required one dominant contribution, explicit assumptions, alternatives, failure modes, and a final proposal that incorporates review objections.
- experiment-plan required every proposed check to map to a claim and a kill criterion; because computation was forbidden, all checks are exact symbolic protocols.
- proof-writer required hypotheses before conclusions, named lemmas, explicit dependencies, edge cases, and no hidden genericity.
- formula-derivation required notation discipline, line-by-line transformations, and separation of formal identities from interpretation.
- research-lit required conservative source handling; with network use forbidden, the citation ledger contains only locally frozen metadata and explicitly reserves external verification.

No skill default was allowed to override the gate by launching a review, search, experiment, compilation, or extra artifact.

## Ten-file coherence audit

The package assigns one role to each authorized file:

- notes/RESEARCH_QUESTION.md freezes the map class, theorem target, boundaries, and portfolio subtraction.
- notes/PROOF_PACKAGE.md supplies the complete proof chain and exact fixtures.
- notes/CLAIMS_EVIDENCE_MATRIX.md maps every promoted claim to dependencies and kill conditions.
- notes/NOVELTY_ASSESSMENT.md gives local-only novelty language and collision threats.
- notes/CITATION_VERIFICATION.md limits frozen primary metadata to contextual use.
- experiments/EXPERIMENT_PLAN.md turns the theorem into reproducible symbolic validation protocols.
- experiments/EXPERIMENT_TRACKER.md records exact obligations without inventing run results.
- refine-logs/INITIAL_PROPOSAL.md preserves the initial risks and superseded coarse expectations.
- refine-logs/FINAL_PROPOSAL.md presents the integrated theorem and 26-page proof-first architecture.
- this summary records review dispositions and the source-stage boundary.

No manuscript, bibliography, lock, independent review, build product, or ledger entry belongs to this package.

## Mathematical closure checklist

- Symplecticity and inverse signs: closed.
- Arbitrary positive exposed-face Hessian determinant: closed.
- Gradient algebraic independence: closed.
- Forward leading-form induction and carry visibility: closed, including the explicit cross-component upper-carry inequalities (6.3)–(6.4).
- Inverse leading-form induction and carry visibility: closed.
- Exact shifted bridge and degree comparison: closed.
- Forward and inverse projective conjugacy: closed.
- Pointwise and support-uniform log contraction: closed.
- Interior, wall, tie, and ordinary-seed classification: closed with inverse Newton walls evaluated at \(r=\kappa s\).
- Interior quadratic and wall integer spectra: closed.
- Forward and inverse interior/parity scalar recurrences: closed separately as upper bounds; inverse closure uses \(D_\xi\), both \(N_\pm\), seed cases, and stable visible coordinates rather than the bridge.
- One-face and three-support exact fixtures: closed.
- Counterexamples and anti-claims: frozen, including zero-coefficient recollection and the positive-characteristic exclusion.
- Local portfolio separation: closed.
- Global novelty: intentionally open pending external verification.

## Handoff boundary

These ten files remain sufficient to plan a 22–30 page proof-first manuscript. Parent consumption and a newly fresh R2 source-design review are required before any later stage. No source lock, paper, bibliography, compilation, external novelty search, or manuscript action is opened by this repair. A later authorized stage must not weaken the support, characteristic, phase-order, or seed hypotheses without reopening the corresponding proof.

PAPER26_SOURCE_DESIGN_REPAIR_AUTHOR_STOP_R2
