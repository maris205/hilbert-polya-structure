# Mathematical owner review — ASFS-20260915-WHR01

**Candidate ID:** ASFS-20260915-WHR01  
**Review date:** 2026-09-15  
**Review state:** COMPLETE — NO UNRESOLVED MATHEMATICAL FINDING.  
**Candidate status:** STOP — COMPLETE HAMILTONIAN RETURN OWNER; INFINITE COMMON-TIME PRIME PACKETS.  
**Calibration status:** NOT_CALIBRATED.

## Scope and provenance

This is a bounded mathematical review of the [frozen card](../candidate-card.md),
not a journal review, Route evaluation, or human peer review. The reviewer has
write authority only for this report and does not edit the author manuscript.
The review uses the ARS domain-review discipline of explicit criteria,
evidence-anchored findings, and separately recorded limitations; no full ARS
panel, external model API, or journal-criteria binding is invoked.

The reviewer is a separately delegated native agent using the inherited
session model and reasoning configuration, in the same model family as the
author/controller. Context is not blind: the reviewer sees inherited project
history, the controller's task message, and the frozen candidate card. That
message already describes expected ownership and stopping tests. No author
manuscript or other 164 review has been read at this criteria commitment.
Later author/controller messages and revision visibility will be recorded
below. Separate agent roles do not establish independent error processes.
No accountable human referee is assigned. criteria_binding_unavailable;
there is no venue-alignment or calibration claim.

## Frozen review criteria

Authority is the current user instruction, local AGENTS guidance, [plan](../../../plan.md),
the [prior-work lineage](../../../docs/prior_work/README.md), and the candidate
card. The following criteria are fixed before the author manuscript is read.

| Criterion | Required evidence | Blocking defect for the corresponding claimed result |
| --- | --- | --- |
| H1: Full Hamiltonian owner | Explicit all-integer carrier, canonical form, displayed vector field, regularity of the fixed energy level, and two-sided ODE completeness | An omitted state, wrong Hamiltonian convention, critical point on the claimed regular level, or finite-time escape |
| H2: Return-domain ownership | Exact full section, maximal bi-return domain, all nonreturning energy states, and proof that no excluded state supports a closed orbit | Treating the return saturation as the entire energy surface without proof, or selecting a periodic subset to restore the ledger |
| H3: Symplectic return and actual roof | Actual first-return formula, smooth positive elapsed-time roof, preserved section form, inverse, and accumulated-time divergence | An inserted roof, unproved variable-time symplecticity, or a Zeno return sequence |
| H4: Full orbit multiplicity and repetitions | Complete nonconstant closed-orbit classification, primitive convention, time orientation, repeated transverse derivatives, and exact map/flow correspondence | Extra closed orbits, hidden continuous packets, or counting map points as distinct flow orbits |
| H5: Arithmetic and analytic scope | Exact divisor source lineage, generic-constraint controls, clock naturalness limits, and the ordinary unweighted product's stated convergence or failure | Importing prime timing or a different operator, claiming a universal analytic no-go from one divergent ordinary product, or issuing formal Route credit |

## Review execution record

The criteria above were committed while only the frozen card existed in the
author package. After the author announced that the five core files were
ready, this reviewer read the full 419-line [paper](../paper.md), the full
card including its later adjudication, [README](../README.md),
[claim ledger](../claim-ledger.md), and the then-current
[evidence index](README.md). The author's readiness message stated that
an author-side read-only adversary had contributed pre-author feedback;
that adversary's report was not read by this reviewer. The controller's
messages supplied expected owner boundaries before manuscript reading,
so this is not a blind or author-persuasion-blind review.

After the criteria commitment, the reviewer delegated one narrowly scoped,
read-only calculus check to
/root/research_controller/hamiltonian_owner_reviewer/return_map_formula_check.
That helper received the frozen formula and inherited context but did not
read the author manuscript, package files or other review, and wrote no
files. Its direct integral/Jacobian derivation was received after this
reviewer had read the manuscript and independently checked its equations.
The calculation is recorded below as reviewer support, not a separate full
review or independent error-process certification. All agents used the
inherited model family/configuration. No external-model API, numerical
experiment or external literature theorem was used in this review.

No manuscript amendment was requested: the mathematical findings required
no correction. This report was completed after its criteria-only state;
there is no outstanding author response or mathematical review item.

## Criterion-bound assessment

Each criterion uses the frozen repository/card authority above. Judgements
concern whether the stated mathematical scope is supported, not whether the
candidate succeeds as a natural arithmetic-clock programme.

| Criterion | Judgement | Typed evidence anchor | Reason and boundary | Decision bearing |
| --- | --- | --- | --- | --- |
| H1 | MEETS | equation: paper (2)--(6), Proposition 1 | Componentwise bounded force gives two-sided completeness; the only zero-witness critical point has energy 0, and positive integer witnesses have no critical point | Supports the regular complete H=1 owner, not a finite-volume or compactness claim |
| H2 | MEETS | equation: paper (4)--(8), Proposition 2 | The whole section is retained before classification; the maximal bi-return domain, full saturation and every omitted energy state are separately determined | Supports full closed-orbit coverage without identifying saturation and energy surface |
| H3 | MEETS | equation: paper (7)--(11), Propositions 2--3 | The return period is actual Hamiltonian time; the complete variable-time Jacobian preserves area, the inverse is global, and the roof is uniformly positive | Supports the exact complete suspension and its stated conjugacy only |
| H4 | MEETS | equation: paper (12)--(13), Proposition 4 | Full transverse periodic equations force Q=P=0; the remaining oscillator oval is one oriented primitive orbit per prime, with all transverse repeats hyperbolic | Supports finite multiplicity per prime, while retaining infinite multiplicity at the common time |
| H5 | MEETS | equation: paper (14), Corollary 5; table: paper Section 5 controls | The source is the stated divisibility constraint; the r=1 terms already prevent absolute convergence, and the prose does not infer a universal trace/regularization no-go | Supports the scoped STOP; source-naturalness remains OPEN and formal Route coordinates remain UNASSIGNED |

## Verified strengths and direct calculations

### S1. The full energy owner and return owner are distinguished correctly

**Evidence Anchor:** equation: paper (2)--(8), Propositions 1--2.

The sign convention is internally correct: contracting the displayed
vector field with dq wedge dp + dQ wedge dP gives dH. On a prime
component, E=p^2/2+log cosh(q)>=0. For E=0 the complete energy states
are exactly q=p=0, QP=1; both transverse coordinates are nonzero, and
their exponential motion cannot close. E<0 is impossible there. For
E>0, every oscillator state reaches the positive-crossing section in both
time directions. On composite components, p strictly decreases at rate
at least one, ruling out every full closed orbit and any second positive
section crossing. The omitted-state statement therefore checks the
entire complement, not merely initial states chosen on the section.

### S2. Variable return time does not spoil symplecticity or completeness

**Evidence Anchor:** equation: paper (9)--(11), Proposition 3.

The paper's clockwise angular-speed formula yields T(E)>=2 pi without
an endpoint approximation. Independently, set
u=sqrt(log cosh q) and then u=sqrt(E) sin(theta) in its return integral.
The reviewer helper's calculation, checked directly here, gives

\[
T(E)=4\int_0^{\pi/2}
h(2E\sin^2\theta)\,d\theta,
\qquad h(z)=\sqrt{\frac{z}{1-e^{-z}}},\quad h(0)=1.
\]

The apparent singularity of h at 0 is removable. This formula is smooth
on E>0 and directly verifies the positive lower bound; in fact it gives
T(E)>2 pi there and T(E) tends to 2 pi as E decreases to zero. That
strict inequality is a supporting check, not a requested expansion of
the author's weaker sufficient bound.

For r=QP, tau=T(1-r), and c=T'(1-r), direct differentiation gives

\[
DF(Q,P)=
\begin{pmatrix}
e^\tau(1-cr)&-e^\tau cQ^2\\
e^{-\tau}cP^2&e^{-\tau}(1+cr)
\end{pmatrix},
\qquad \det DF=1.
\]

Preservation of r makes the inverse with opposite exponents valid on
all QP<1. This agrees with the manuscript's wedge cancellation. The
conserved E makes the return spacing constant along each orbit; the
uniform lower bound rules out accumulation even across the entire
domain. The flow-box argument and unique preceding positive crossing
establish precisely the stated saturation conjugacy.

### S3. The complete periodic equations retain, rather than select, centres

**Evidence Anchor:** equation: paper (12)--(13), Proposition 4.

For any positive closed time t, e^t Q=Q and e^{-t}P=P force Q=P=0
on the original full energy surface. This imposes E=1. On a prime
component the energy oval is one oriented orbit, and its opposite
section crossing is not a second orbit. Equally, the full return map
has no nonzero periodic point at any iterate. At the origin the time
derivative terms vanish, so the repeated transverse multipliers are
e^{rT(1)} and e^{-rT(1)}. The statement is correctly restricted to
Poincare monodromy, not the full autonomous derivative's trivial
time/energy directions.

### S4. The adverse analytic conclusion has exactly the warranted scope

**Evidence Anchor:** equation: paper (14), Corollary 5.

At every finite complex s the absolute values of the infinitely many
primitive r=1 terms equal the same strictly positive number. This is a
direct all-packet obstruction to absolute convergence, requiring no
prime asymptotic or numerical extrapolation. The paper correctly stops
the ordinary unweighted product and does not call this a universal
impossibility of every weighted, regularized, or separately constructed
analytic owner. Its genuine autonomous clock still lacks prime-size
information; this failure does not erase its actual Hamiltonian ownership.

## Weaknesses and coverage receipt

No mathematical defect or unsupported strengthening was found in the
reviewed claim scope. No severity is manufactured to fill a quota.

**Coverage:** Weaknesses.

| Dimension examined | Check performed | Basis for no defect finding |
| --- | --- | --- |
| H1 | Vector-field sign, energy critical points, and componentwise continuation estimates | Equations and all-state estimates agree; disconnected labels require no uniform-in-n bound |
| H2 | Composite section hits; prime E>0, E=0 and E<0 cases; all full-energy closed orbits | Exhaustive cases are explicitly proved, and the nonreturning complement is not silently discarded |
| H3 | Actual least return, smoothness, area Jacobian, global inverse, and two-sided accumulated time | Direct formulas and the independent integral/Jacobian check support the stated scope |
| H4 | Positive-time periodic equations, orientation, fixed-point versus orbit counting, and every repeat | The full equations eliminate extra packets; transverse and autonomous degeneracy claims are separated |
| H5 | Divisibility lineage, all eight control rows, generic zero-set risk, ordinary-series failure, and Route language | Limitations and comparator changes are explicit; no logarithmic timing, trace or Route pass is inferred |

Venue fit, global literature novelty, contact/quantum construction,
weighted or regularized traces, and source-naturalness beyond the stated
constraint mechanism are NOT ASSESSED or OPEN, not missing evidence for
a positive claim made by this paper.

## Reviewed snapshot and final disposition

SHA-256 values from a read-only Node fs/crypto digest of the actual four
core claim surfaces at completion:

| File | SHA-256 |
| --- | --- |
| paper.md | e1cf01200d077fbce3d60ec9f697fda5efef65836e6a710d51f7190bbdc400ae |
| candidate-card.md | f14f7e29c1a5388302953680a90e93b0cef6a5f76182c5ca3264a600d4a46766 |
| claim-ledger.md | 17e54cd2b6019452944c6959605f4167a22adca1ecbf5547ecc934e9f59a06bd |
| README.md | 8ea39ab1ab68bb539448236183eaa7aca5e0e993830ea393a9334ce3647b294a |

The same-object ledger remains intact: the full Hamiltonian energy owner
and return suspension are related by a proved restriction/conjugacy with
complete omitted-state accounting, not silently identified as equal
carriers. The review supports retaining the geometry and exact arithmetic
support, while stopping the common-time clock/ordinary-product contract.
No parameter, energy, potential, roof or owner change is recommended to
preserve this candidate. Formal Route coordinates remain UNASSIGNED;
Route B is NOT INVOKED. No unresolved mathematical or author-response
item remains in this bounded review.

Reviewer mechanical receipt: a read-only Node fs/path check of this report
resolved all 7 local Markdown links, found no unintended trailing whitespace
or blank-split table, confirmed the candidate ID and completed review state,
and reproduced all four core-file hashes above without mismatch. A scoped
git diff --check was also clean; because this new package is untracked, the
filesystem checks, not that Git command alone, cover its actual content.
The receipt adds no mathematical claim or new link target.

Process deviation disclosure: this round's 168 scope specified No Git
actions. The recorded read-only git diff --check, and the earlier scoped
git status --short used by this reviewer, departed from that agreement.
Neither command staged, committed, reset, restored, rolled back, or changed
Git state. Their actual use is retained here transparently rather than
removed from the record. This is a read-only workflow deviation, not an
unresolved mathematical gap. No further Git action or proof rerun was
performed for this disclosure amendment.
