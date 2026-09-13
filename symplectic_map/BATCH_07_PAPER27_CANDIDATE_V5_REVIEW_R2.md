# Paper 27 candidate v5 — fresh formal R2 review

Audit disposition: PASS  
Auditor role: fresh, independent `batch07_charter_auditor` (formal R2)  
Audit date: 2026-08-28 UTC  
Controlling gate: `BATCH07_PAPER27_CANDIDATE_V5_DUAL_REVIEW_REQUIRED`  
Candidate: `positive_newton_translation_reciprocity_v5`

## Restricted read boundary

This review was restarted from the physical EOF after each frozen correction and
used the current `BATCH_07_STATUS.md` through E0050, plus
`BATCH_07_CHARTER_REVIEW.md` and exactly the following allowed notes:

1. `papers/12-henon-period3-residue/notes/RESEARCH_QUESTION.md`
2. `papers/12-henon-period3-residue/notes/CLAIMS_EVIDENCE_MATRIX.md`
3. `papers/12-henon-period3-residue/notes/PROOF_PACKAGE.md`
4. `papers/26-hamiltonian-newton-envelope-contraction/notes/RESEARCH_QUESTION.md`
5. `papers/26-hamiltonian-newton-envelope-contraction/notes/CLAIMS_EVIDENCE_MATRIX.md`
6. `papers/26-hamiltonian-newton-envelope-contraction/notes/PROOF_PACKAGE.md`

No previous candidate-review file or candidate artifact was read.  No Paper 27
project, any other project source, PDF, temporary/closed/future root, or
unlisted path was read or probed.  I performed only read-only text and byte
inspection and hand algebra; there was no build, compile, scientific script,
network lookup, numerical/CAS run, cache creation, or external effect.  The
only write in this review is this PASS artifact, created once after the census
below was all zero.

## Authority and governance check

The user continuation authorizes the serial Papers 27--31 batch.  The current
queue still has no Paper 27 path, number consumption, source-design file,
manuscript, build root, PDF, or external effect.  E0033 makes the headline a
strict unique-exposed-selector theorem; references to a certified wall face
are auxiliary Hessian boundary tests unless a separate deterministic
refinement, target inclusion, and reflected certificate are supplied.  Thus a
finite selector-word statement is seed-indexed and is not a support-only
universal automaton claim.

The append chain has an explicit historical correction.  E0048 was issued with
premature sequence 48 and is marked invalid.  E0049 is the authoritative
logical successor of E0046 at sequence 47, with a physical parent hash binding
the unchanged bytes that contain invalid E0048; E0050 then follows at logical
sequence 48 and binds E0049's current bytes.  Sequence monotonicity is therefore
checked on the authoritative chain after the explicit invalid-event
disposition, while the invalid historical bytes remain preserved.  No active
append/schema finding remains.

The broad Material Passport stage and the immediate candidate subgate are
hierarchical: the latter controls the transition.  Serial lifecycle, no
downstream authority, one-shot/cache/build safeguards, and no-external-effect
rules remain intact.  The E0043 portfolio lock reserves only unconsumed
discovery IDs for the later positions and does not create projects.

## Theorem-critical rederivation

The authoritative family is over a characteristic-zero coefficient field with
nonempty collected finite supports

\[
E_V,E_W\subset\mathbb Z_{\ge2}^r,\qquad r\ge3,
\]

and
\(H(q,p)=V(q)+W(p)\),
\(S_V(q,p)=(q,p+\nabla V(q))\),
\(T_W(q,p)=(q+\nabla W(p),p)\),
\(F=T_W\circ S_V\).  Degree space is ordered real space; weighted
polynomial seeds have positive integer degree pairs and pairwise independent
leading variable blocks.  Every edge explicitly requires a nonempty integer
pair cell and the stated observable spans.

For an exposed vertex \(\alpha\) and \(\beta\),

\[
A_\alpha=\mathbf1\alpha^T-I,
\qquad B_\beta=\mathbf1\beta^T-I.
\]

The forward order is \(A_\alpha\) then \(B_\beta\), with carries
\(A_\alpha u>w\) and \(B_\beta A_\alpha u>u\).  The inverse order is the
subtraction sequence \(T_W^{-1}\) then \(S_V^{-1}\), so the reflected proof
uses the same matrices with signs changed only in coefficients.

### Face survival

For a positive exposed face \(F\), choose a generic secondary linear weight
with unique minimizer \(\alpha_0\).  In the grouped Hessian determinant, the
all-\(\alpha_0\) tuple is the unique lowest secondary-weight group and has

\[
c_{\alpha_0}^{,r}(-1)^r(1-|\alpha_0|)\prod_i(\alpha_0)_i\ne0.
\]

The coordinatewise \(\ge2\) condition and characteristic zero are exactly
what make this witness nonzero.  Hence every exposed face gradient tuple has
nonzero Jacobian and is algebraically independent.  Substitution into an
independent leading tuple is injective, and coordinate pure powers, scalars,
and inverse minus signs preserve independence.  Strict carry inequalities then
exclude old/fresh top-degree cancellation.  This establishes coefficient-
uniform forward and inverse transport, including an explicitly admitted face;
unqualified wall continuation is not claimed.

### Translation and recurrence

On a strict edge,

\[
v=A_\alpha u=(\alpha\!\cdot u)\mathbf1-u,
\]

and therefore

\[
B_\beta A_\alpha u
=u+\bigl(((|\beta|-1)\alpha-\beta)\!\cdot u\bigr)\mathbf1.
\]

Writing \(u_n=u_0+t_n\mathbf1\), with one global origin \(t_0=0\), gives

\[
t_{n+1}=\lambda_{\alpha,\beta}t_n+\mu_{\alpha,\beta},\quad
\lambda_{\alpha,\beta}=(|\alpha|-1)(|\beta|-1),\quad
\mu_{\alpha,\beta}=((|\beta|-1)\alpha-\beta)\!\cdot u_0.
\]

On a stationary strict phase \(\lambda>1\), so the displayed affine tail is
valid and a positive carry makes the degree parameter increase.  The formula
is phase-local only through the pair \((\alpha,\beta)\); changing phase does
not change the global origin convention.

### Finite selector changes

For \(u(t)=u_0+t\mathbf1\), V score differences are affine in \(t\), and
equal-total pairs have invariant differences.  Let

\[
d_V=|\{|\alpha|:\alpha\in E_V\}|,\qquad
d_W=|\{|\beta|:\beta\in E_W\}|.
\]

E0050 gives the stronger global argument.  Put

\[
g(t)=h_V(u(t))-t.
\]

All \(|\alpha|-1>0\), hence \(g\) is strictly increasing.  Since
\(v(t)=h_V(u(t))\mathbf1-u(t)\),

\[
\beta\!\cdot v(t)-\eta\!\cdot v(t)
=(|\beta|-|\eta|)g(t)-(\beta-\eta)\!\cdot u_0.
\]

Every unequal-total W wall is crossed at most once globally; equal-total W
ties are invariant.  The V envelope has at most \(d_V-1\) changes and the W
envelope at most \(d_W-1\).  Counting a simultaneous pair event once gives

\[
\#\{\text{selector changes}\}\le d_V+d_W-2.
\]

Thus no strict positive-support orbit has an infinite or nontrivial periodic
selector word; after the finite transient it has one stationary pair and the
affine \(\lambda/\mu\) tail.  E0046's \(d_Vd_W-1\) bound is a valid conservative
intermediate estimate and is superseded, not contradicted, by E0050.  The
inverse proof interchanges V and W.

### Reflection and observable spans

With coordinate reversal \(R\) and \(Rstate(u,w)=(Rw,Ru)\), the reflected
inverse edge uses \(R\alpha\) in its W phase and \(R\beta\) in its V phase.
The identities

\[
B_{R\alpha}R=RA_\alpha,
\qquad A_{R\beta}R=RB_\beta
\]

hold on the declared real observable spans.  Equality of both phase-resolved
degree vectors for all integer seeds forces these restrictions at the first
step; full matrix identities are asserted only when the corresponding spans
are all of \(\mathbb R^r\).  On a proper span a different support label with
the same action is allowed, so no literal global reflected-face claim is
smuggled in.  Conversely, edge-by-edge identities plus reflected score/carry
and target certificates give all-iterate equality by induction.  This is a
degree/phase statement, not a map-level reversor or scalar-total-degree claim.

### Four-section lower-ideal condition

For an edge, the four score projections are

\[
\pi_u(C_e^+),\quad \{A_\alpha u\},\quad \{Ru\},\quad
\{RA_\alpha u\},
\]

corresponding to V+, W+, W-, and V-.  With \(\ell\) retained and \(\rho\)
lower/new, every section uses the same orientation
\(\min(\ell-\rho)\cdot x\ge\Delta>0\).  E0044 excludes cores touching
selector or carry walls.  E0045 correctly types carry/target tests on a
compact normalized pair core \(\widehat\Sigma_e^+\) in \((u,w)\), while
lower-row score margins are evaluated on its projections.  A multi-edge
perturbation is claimed only when the normalized pair map and its reflected
maps send each source core into the declared target core; absent that
certificate the result is explicitly one-edge/pointwise.  This prevents an
x-only margin from being promoted to an all-iterate claim.

### Fixture and lattice checks

The asymmetric \(r=3\) supports and matrices in E0025/E0027 give the strict
C1\(\to\)C2\(\to\)C2 word, positive target/carry/reflected gaps, and the
reflected identities.  The C1 u-witnesses
\((2,1,1),(2,1,2),(3,1,1)\) and C2 witnesses
\((1,1,1),(1,1,2),(1,2,2)\) have nonzero determinants; positive integer w
seeds exist in the same pair cells.  The ordinary C2 seed is a stationary
baseline with unique exposed maximizers (inactive submaximal ties do not count
as walls).  The gamma off-component and absent \(R\gamma\) witness is local,
not a global reversor assertion.

## Boundaries, anti-claims, and collision locks

The packet explicitly excludes zero-coordinate or exponent-one supports,
empty supports/cells, zero coefficients after collection, positive
characteristic, unsupported ties, failed carries, unlisted reflected phases,
and arbitrary-support extensions.  It makes no unconditional field algorithm,
support-only universal automaton, map-level reversor/global classification,
entropy or higher-dynamical-degree claim, scalar-only reciprocity claim,
same-seed claim for a non-`Rstate`-fixed pair, recurrence minimality claim, or
external-effect claim.  Auxiliary wall Hessian survival is not used to extend
the strict selector theorem without deterministic certificates.

The status contains the complete P12--P26 collision table and the v5-specific
claim-level additions.  In particular, P26's planar envelope/contraction and
P25's support-rank/Perron factorization are absorbed and explicitly separated;
v5 owns the positive-support all-ones translation, the global finite
no-switching bound, phase-pair affine tails, and reflected observable-span
criterion.  E0043 reserves unconsumed, pairwise disjoint future axes:
P28 `primitive_selector_cycle_monodromy_v1`, P29
`toric_cohomological_degree_spectrum_v1`, P30
`symplectic_transfer_reciprocity_v1`, and P31
`zero_coordinate_gradient_cancellation_v1`, each with explicit exclusions
from P27.  No future project or number is consumed.

The bounded source search, query families, limitations, and no-priority
wording are present in the frozen status.  No source is used as proof of the
theorem; the collision record is a negative-control lock.

## Independent gate scores

| Gate | Independent assessment | Result |
|---|---:|---|
| Novelty after P12--P26 absorption | 8.1 / 10 | PASS |
| Standalone mathematical value | 8.0 / 10 | PASS |
| Proof readiness | 9.1 / 10 | PASS |
| Credible proof-first content mass | 26--30 pages | PASS |

The novelty score credits the higher-dimensional arbitrary-support family, the
global no-switching bound, and the reflected observable-span iff rather than
the inherited Hessian or ordinary degree machinery.  Standalone value remains
above threshold because the finite transient classification and phase-pair
reciprocity are useful conclusions even after P26 is fully absorbed.  Proof
readiness is above 9 because the face-Jacobian induction, exact translation
calculation, global wall monotonicity, reflected phase order, and typed core
qualification form a complete proof spine with explicit failure boundaries.
The page estimate counts only mathematical definitions, lemmas, proofs,
fixtures, and scientific limitations; governance/provenance prose is not
counted.

## Finding census

| Finding category | Count |
|---|---:|
| Authorization and Papers 27--31 scope | 0 |
| Nonempty positive-support and integer-seed assumptions | 0 |
| Strict selector-word scope / no universal automaton overclaim | 0 |
| Face Hessian, Jacobian, and coefficient-uniform survival | 0 |
| Translation identity and affine \(\lambda/\mu\) recurrence | 0 |
| Global finite-change bound and inverse swap | 0 |
| Reflected phase labels, signs, and observable-span converse | 0 |
| Four-section margins, pair-core typing, and invariance qualifier | 0 |
| Fixture arithmetic and lattice-span witnesses | 0 |
| Anti-claims and excluded-regime boundaries | 0 |
| P12--P26 absorption and source/collision lock | 0 |
| P28--P31 portfolio noncollision lock | 0 |
| Numerical thresholds and proof-page estimate | 0 |
| Serial lifecycle, no-write/no-effect, and forbidden-read boundary | 0 |
| Append-only/event schema (E0048 quarantine, E0049 seq47, E0050 seq48) | 0 |

Severity census: Blocker **0**; Major **0**; Minor **0**; Ambiguity **0**.

## Conclusion

The current E0050 packet is a self-contained, nonempty positive-support
candidate with a correct face-survival argument, exact translation and affine
tail, globally finite strict selector word, properly scoped reflected
observable-span reciprocity, and a typed four-section lower-ideal condition.
All nine candidate gates and all numerical thresholds pass, and the
authoritative event chain is contiguous after E0048's explicit invalidation.
This review creates no Paper 27 project or downstream authority.

BATCH07_PAPER27_CANDIDATE_V5_REVIEW_R2_PASS
