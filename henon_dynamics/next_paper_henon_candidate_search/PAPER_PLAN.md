# Paper plan: constructive holomorphic coding for the area-preserving Hénon map

Date: 2026-08-06  
Status: **historical C02C paper plan; C02D gate closed `NO_GO`, manuscript
remains held, and breadth-first search resumes with HCS-C12A WP0**  
Primary source: `../docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf`  
Paper type: theory plus reproducible computer-assisted certificates  
Target venue: specialist dynamical-systems journal, to be selected only after
the main theorem delta is established  
Indicative length: 24--30 pages plus reproducibility appendix

## Working title

**Holomorphic Coding and Projective Derivative Cocycles for a Certified
Area-Preserving Hénon Horseshoe**

The title deliberately makes no Hilbert--Pólya or Riemann-hypothesis claim.

## C02D closure addendum

The conditional T4/C02D gate below has now been executed. The standard
BPS/Rugh kernel is already exact at one chronological step, so the C02C
length-\(N\) endpoint data describe \(\mathcal L^N\) word kernels or exact
higher-block recodings rather than the pre-registered same-clock
finite-memory approximation. A separate orbitwise scalar repetition
obstruction was also proved. The formal result is `ROUTE_A_REJECTED`; see
`../henon_pinning_trace_obstruction/`. The remainder of this file is retained
as the historical C02C conditional manuscript plan.

## One-sentence contribution

For the certified local horseshoe of the exact area-preserving Hénon map

\[
H_6(q,p)=(1-6q^2-p,q),
\]

we turn an explicit contracting complex itinerary-polydisc model into
finite-window holomorphic endpoint solvers and finite-dimensional crossed
maps with exponentially localized boundary influence, exact chronological
composition, an explicit matching/Hill trace identity, and exact complex-base
projective disks.  These form an effective project-specific bridge toward a
graph-directed transfer operator; they do not yet constitute an infinite
operator or Fredholm-determinant theorem.

T1--T3 are now proved.  The scoped WP0 audit also shows that the real
signed-root SFT/existence theorem, qualitative complex pinning and the
absolute-denominator Fredholm mechanism are prior art.  The manuscript
therefore remains on hold until a signed, trace-compatible cylinder/operator
approximation theorem uses the explicit \(H_6\) constants to produce a
genuinely new aggregate estimate.

## 1. Why this is the foundational paper

Paper 5 supplies the mother object: an exact reversible, symplectic Hénon map,
its periodic-orbit viewpoint, and the question of whether a natural spectral
structure can emerge.  It does not supply a certified complex Markov system or
an analytic transfer operator.  The present route keeps that exact map and
replaces fitted spectral analogies with a sequence of falsifiable analytic
bridges:

\[
\begin{array}{c}
\text{real certified horseshoe}
\longrightarrow
\text{complex orbit-coordinate domain}
\longrightarrow
\text{finite-window holomorphic gluing}
\\[2mm]
\longrightarrow
\text{graph-directed analytic branches}
\longrightarrow
\text{nuclear transfer operator}
\longrightarrow
\text{periodic-orbit Fredholm determinant}.
\end{array}
\]

The current work proves the first three finite-dimensional nodes through the
crossed/pinning matching identity, but not the graph-directed operator node.
The source audit shows that existence and composition alone are not a
publishable delta.  The remaining paper question is whether the explicit
domains, localization constants and trace residue yield a quantitative
trace-compatible approximation theorem beyond general Axiom-A theory.

## 2. Claims--evidence matrix

| Claim | Evidence | Current status | Planned location |
|---|---|---|---|
| The signed-root orbit solver strictly preserves the specified complex sequence polydiscs and contracts by at most \(2/\sqrt{17}\). | Exact disk arithmetic, theorem proof, producer 14/14, independent checker 18/18; Sterling--Dullin--Meiss already covers the conjugate real SFT and real uniqueness. | **PROVED EFFECTIVE SPECIALIZATION; NOVELTY UNCONFIRMED** | §3 |
| The true projective derivative cocycle is pole-free and contracts separated complex fibre disks over the real survivor. | Exact rational disk proof and algebraic monodromy identity; 17 primitive cycles through period 8 are regression checks only. | **PROVED over a real symbolic base** | §4 |
| Uniform fibre-image disks remain valid for every complex base coordinate \(q\in D_\varepsilon\). | Exact reciprocal-disk image, pole clearance, child separation and fibre derivative \(\delta=(224/773)^2\). | **PROVED; no joint complex base--fibre contraction or infinite skew-product theorem** | §4--§5 |
| Every locally admissible extended sign block with two frozen complex endpoint variables has a unique jointly holomorphic internal solution on the full endpoint disks. | Parameter-dependent contraction proof; complete finite-window adversarial ledger and independent Newton checker. | **PROVED** | §5.1 |
| Endpoint influence decays exponentially with distance and finite-window solutions obey explicit extension bounds. | Neumann-path proof gives \(\beta\kappa^{i-1}\) and \(\beta\kappa^{N-i}\), with \(\beta=1/(\sqrt{17}-2)\); 432 persisted center rows and 120 boundary probes summarized in the certificate audit the bounds. | **PROVED; enumeration is regression evidence only** | §5.2 |
| Every admissible cyclic word already has a unique signed-root fixed sequence. | T1 applies directly to finite cyclic \(I\), including periods one and two. | **PROVED** | §3 |
| Endpoint/pinning closure agrees with the proved cyclic solution and recovers the chronological monodromy and trace Jacobian. | Continuant proof, exact matching/Hill identity, 120 cyclic words through period 8, and independent period-1/2 chronology checks. | **PROVED** | §5.3 |
| The endpoint solvers define finite-dimensional crossed/pinning maps with an exact two-coordinate composition law and a frozen signed formal flat-trace denominator. | Exact crossed identity, direct-versus-glued control, scalar-average and reversed-order expected failures; general crossed composition and the absolute-denominator residue mechanism are prior art. | **PROVED as project bookkeeping; not an operator or standalone novelty claim** | §6 |
| These maps yield a graph-directed holomorphic system with trace-compatible cylinder approximants and a quantitative truncation error. | No function space, Cauchy kernel or approximation norm is frozen yet. | **OPEN / current manuscript gate** | §6 or sequel |
| A nuclear operator and Fredholm determinant follow with an exact periodic-orbit trace formula. | General theory already supplies such determinants in closely related analytic hyperbolic settings; the frozen \(H_6\) specialization, weight, and quantitative delta are unaudited. | **OPEN; not a current claim** | sequel |
| The action--Maslov phase is a new nonlocal orbit invariant. | Exact diagonal-dominance theorem gives \(\mu=\#\{q_i<0\}\). | **FALSE; obstruction** | short scope proposition / appendix |
| Raw finite-field local factors determine a canonical global Euler product. | Matched reversible controls and the missing Frobenius/iterate bridge. | **REJECTED** | omit from main story; search appendix only |

## 3. Main theorem ladder

### T0. Exact dynamical setup

Fix the local certified survivor of \(H_6\), the admissible no-two-positive
symbolic sequences, the chronological recurrence

\[
q_i=\varepsilon_i
\sqrt{\frac{1-q_{i-1}-q_{i+1}}6},
\]

and the true derivative matrices.  State explicitly that this is a local
horseshoe, not the full bounded Hénon set.

### T1. Complex signed-root polydisc theorem — proved

For

\[
c=\frac{23}{48},\qquad \rho=\frac7{48},\qquad
K_\varepsilon=\prod_i\overline D(\varepsilon_i c,\rho),
\]

prove that the principal signed-root map is holomorphic on a neighborhood of
\(K_\varepsilon\), strictly self-maps it, and has Lipschitz constant

\[
\kappa=\frac2{\sqrt{17}}<1.
\]

The two exact radicand disks are

\[
\overline D\!\left(\frac16,\frac7{144}\right),\qquad
\overline D\!\left(\frac{47}{144},\frac7{144}\right),
\]

with strict image margins

\[
\mu_{\mathrm{mix}}=\frac{\sqrt{17}-4}{12},\qquad
\mu_{--}=\frac58+\frac{\sqrt{10}-\sqrt{47}}6.
\]

The proof must retain both neighbor occurrences for cyclic periods one and
two; no averaged or de-duplicated chronology is allowed.

### T2. Finite-window holomorphic endpoint solver — proved

Freeze an extended sign word
\(\varepsilon_0,\ldots,\varepsilon_{N+1}\) and require the local rule

\[
\neg(\varepsilon_{i-1}=\varepsilon_{i+1}=+1),
\qquad 1\le i\le N.
\]

Let

\[
D_\sigma=\overline D(\sigma c,\rho),\qquad \sigma\in\{-1,+1\},
\]

and freeze two boundary variables
\((u,v)=(q_0,q_{N+1})\in D_{\varepsilon_0}\times
D_{\varepsilon_{N+1}}\).  Define the internal signed-root map on

\[
\prod_{i=1}^N\overline D(\varepsilon_i c,\rho)
\]

using \(u\) and \(v\) at the two ends.  The proved statement is:

1. **Uniform self-mapping on the full frozen disks.**  The T1 radicand cases
   already show that the complete domain
   \(D_{\varepsilon_0}\times D_{\varepsilon_{N+1}}\) works for every locally
   admissible block and every \(N\).  Do not introduce a post-hoc shrink unless
   an alternative radius is frozen as a separate theorem variant.
2. **Unique endpoint solution.**  There is a unique internal vector
   \(Q_\varepsilon(u,v)\), and it depends jointly holomorphically on \((u,v)\).
3. **Derivative localization.**  Set
   \(a_0=1/\sqrt{17}\) and \(\kappa=2/\sqrt{17}\).  The internal derivative
   matrix \(A\) has \(\|A\|_\infty\le\kappa\), while an endpoint enters one
   boundary row with coefficient at most \(a_0\).  A Neumann-path argument
   gives the explicit bounds
   \[
   \left|\partial_u Q_{\varepsilon,i}\right|
   \le \frac{a_0\kappa^{i-1}}{1-\kappa},
   \qquad
   \left|\partial_v Q_{\varepsilon,i}\right|
   \le \frac{a_0\kappa^{N-i}}{1-\kappa}.
   \]
   The derivation reconciles the endpoint formulation with the doubled
   chronological occurrences at cyclic periods one and two.  The interface
   response constant
   \[
   \beta=\frac{a_0}{1-\kappa}=\frac1{\sqrt{17}-2}<1
   \]
   is a useful explicit composition bound to audit.
4. **Extension consistency.**  When a window is enlarged, its restriction to
   the old interior differs from the old endpoint solution by the certified
   exponentially small boundary term.  Do not claim literal equality when
   the effective boundary data change.
5. **Two-coordinate interface law.**  Since the recurrence is second order,
   gluing adjacent windows must match the consecutive phase-space pair
   \((q_k,q_{k+1})\) through two equations.  The chronological two-variable
   matching agrees exactly with solving the union directly; a one-endpoint or
   averaged matching rule is inadmissible.
6. **Cyclic comparison.**  The endpoint diagonal/matching equations recover
   the unique cyclic fixed sequence already established by T1, including the
   correct derivative bookkeeping at periods one and two.

T2 is a necessary technical bridge and follows from T1 via
parameter-dependent contraction and the Neumann series.  Pinning
coordinates and iterated half-inverses already exist in the literature for
analytic hyperbolic surface maps, so T2 is not a standalone novelty claim.  It
becomes paper-level only if the explicit Hénon constants and pinning/trace
Jacobian support T4's quantitative approximation theorem.  The frozen C02C
producer and independent checker found no domain or two-coordinate
composition failure through their complete prescribed ledgers.

### T3. Finite-dimensional pinning/crossed maps and projective extension — proved effective specialization

For the T2 solution \(Q_\varepsilon(u,v)=(Q_1,\ldots,Q_N)\), the exact
crossed-map identity

\[
H_6^N\bigl(Q_1(u,v),u\bigr)
=\bigl(v,Q_N(u,v)\bigr).
\]

holds.  The two-coordinate interface equations give exact chronological
composition of these pinning relations, and cyclic diagonal closure recovers
the already-proved periodic orbit.  Differentiating the identities recovers
the full monodromy and the determinant identity relating the pinning matching
Jacobian to \(\det(I-DH_6^n)\).

Before an operator is defined, freeze its target flat-trace convention.  A
natural baseline to audit is

\[
\operatorname{tr}^{\flat}\mathcal L_g^n
=\sum_{x\in\operatorname{Fix}(H_6^n)\cap\Lambda_*}
\frac{g_n(x)}{\det(I-DH_6^n(x))},
\]

where \(\Lambda_*\) is the certified local survivor and

\[
g_n(x)=\prod_{j=0}^{n-1}g(H_6^j x)
\]

is ordered chronologically.  The signed holomorphic denominator above is the
baseline convention; replacing it by an absolute value is a different object
and would require a separately frozen orientation/quotient construction.  The
potential \(g\), clock, and normalization must be specified before
computation.  If an instability weight is intended, prove its exact relation
to this denominator rather than changing weights after seeing finite sections.

For the true coordinate values supplied by T2, also analyze the derivative
slope map

\[
\phi_q(m)=\frac1{-12q-m}
\]

The C02C derivation recomputes containment and separation for the complex
coordinate disks \(q\in D_{\varepsilon_i}\).  The exact child disk is

\[
D\left(-\varepsilon\frac{288512}{1393719},
             \frac{115360}{1393719}\right),
\]

the fibre derivative is at most \((224/773)^2\), and ordered composition is
identified with the Hénon monodromy.  The corresponding unscaled base
sensitivity bound is \(12(224/773)^2>1\), so no false joint product
contraction is claimed.  T3 is now an effective specialization; the stronger
paper delta has moved to T4's quantitative trace approximation.

### T4. Graph-directed operator and trace-compatible approximation — current manuscript gate

C02D must now define a graph-directed function space and operator.  Do not
assume an ordinary direct-sum Hardy or
Bergman composition operator: pinning constructions may require mixed
interior/exterior holomorphic variables and Cauchy-kernel operators.  Freeze
the exact spaces, edge kernels, orientation signs, potential/clock, one-step
operator, intended fixed-point trace, and approximation norm before the first
finite-section computation.  The first operator question is whether
fixed-one-step-clock finite-memory kernel approximants converge in that norm
with the frozen flat trace.  They must not be confused with the time iterate
\(\mathcal L^N\) or an exact \(N\)-block recoding.  Nuclearity,
global trace identities, and Fredholm determinants are later gates, not
consequences of T1 alone.

## 4. Hard novelty boundary

Complex Hénon horseshoes and analytic Fredholm determinants for hyperbolic
systems already exist in substantial generality.  WP0 compared the present
claims with Sterling--Dullin--Meiss's exact real SFT theorem,
Hubbard--Oberste-Vorth, Oberste-Vorth, Rugh's pinning-coordinate and
generalized Fredholm constructions, and Baladi--Pujals--Sambarino's iterated
analytic pinning maps.

WP4 has already ruled that none of T1--T3, taken alone, clears the current
manuscript threshold.  In particular, the real signed-root SFT/existence is
known, and the matching/Hill identity is retained as explicit bookkeeping
rather than counted as novelty.  The complex endpoint domains, localization
constants and projective disks remain a proved effective specialization with
unconfirmed novelty.

For this manuscript plan the only unresolved admission route is T4: a natural
operator plus a trace-compatible *aggregate* cylinder approximation theorem
that uses the explicit \(H_6\) constants and remains contractive after the
exponential growth in admissible cylinders is included.  A coding-only paper
may be reconsidered only after a new independent journal-level novelty review;
it is not authorized by the present WP4 ruling.

If T4 gives only stable finite spectra, single-branch convergence, or a
routine restatement of general nuclearity, retain C02C as research
infrastructure and return to the breadth-first RH search.  Do not publish a
renamed instance of general theory.

## 5. Proposed paper structure

### §0 Abstract

- Lead with the strongest explicit Hénon pinning/trace or quantitative error
  theorem that survives the source-delta audit, not RH.
- State the exact contraction \(2/\sqrt{17}\) and the strongest explicit
  boundary-decay bound obtained in T2.
- Explain that the result preserves chronological Hénon recurrence and is a
  foundation for, not yet a proof of, a Fredholm determinant construction.
- Length: 180--220 words.

### §1 Introduction — 2.5 pages

- Start from Paper 5's exact area-preserving Hénon model and the missing
  rigorous analytic coding bridge.
- Separate the dynamical question from spectral fitting.
- State T1--T3 in reader-level form by page 2, distinguishing the endpoint
  lemma from the operator-enabling crossed-map theorem.
- Give three falsifiable contributions: explicit domain, finite-window
  holomorphic solver/localization, and chronological projective cocycle.
- Include Figure 1 as a status map of proved and open bridges.

### §2 Related theory and theorem delta — 3 pages

- Area-preserving Hénon symbolic dynamics and reversibility.
- Complex Hénon horseshoes and pinning coordinates.
- Analytic transfer operators and generalized Fredholm determinants.
- Constructive/computer-assisted hyperbolic dynamics.
- End with a theorem-comparison table; do not organize paragraph by paragraph
  as a bibliography.

### §3 Certified real subsystem and complex orbit domain — 4 pages

- Define the local survivor, alphabet, and recurrence.
- State and prove T1, including the two radicand disks and short-cycle
  chronology.
- Put interval-enclosure implementation details in the appendix.

### §4 Projective derivative cocycle — 3 pages

- Derive the exact slope map from the derivative matrix.
- Prove the parent-disk contraction and separated child disks.
- Explain why itinerary-dependent \(q\) forbids replacing the cocycle by four
  fitted constant Möbius generators.
- Give the chronological monodromy identity.

### §5 Finite-window endpoint solving and crossed-map gluing — 7 pages

- §5.1 Uniform endpoint-domain theorem and holomorphic dependence.
- §5.2 Explicit boundary derivative and exponential localization bounds.
- §5.3 Two-coordinate interface matching, crossed-map composition, and
  equivalence with the already-proved cyclic solution.
- Include proof sketches in the main text; move repetitive interval cases and
  long resolvent estimates to appendices.

### §6 Consequences and operator boundary — 3 pages

- State exactly which finite-dimensional analytic objects T2--T3 produce.
- Freeze the flat-trace weight and, if established, give a trace-compatible
  approximation proposition.
- State nuclearity/Fredholm questions as open unless fully proved.
- Include the C05 gauge/Maslov obstruction as a short scope-control
  proposition only if it sharpens why the paper uses instability/derivative
  data rather than an arbitrary absolute action phase.

### §7 Reproducibility, limitations, and conclusion — 2 pages

- Commands, exact constants, hashes, independent implementation, and resource
  use.
- Limitations: local survivor, fixed parameter \(a=6\), no full bounded set,
  no global arithmetic divisor, no Hilbert--Pólya operator.
- End with the single next operator theorem, not a broad list of aspirations.

## 6. Figure and table plan

| ID | Type | Content | Data source | Priority |
|---|---|---|---|---|
| Fig. 1 | hero dependency diagram | Paper 5 exact map → real survivor → T1 complex polydisc → T2 endpoint lemma → T3 crossed/pinning composition → T4 trace-compatible operator approximation; T1--T3 green, T4 blue/open, later HP nodes gray, C03/C05 dead ends red | manual, theorem statuses | high |
| Fig. 2 | complex-domain geometry | The two radicand disks, the principal-square-root images, target signed disks, and exact margins | `results/c02_complex_base/complex_polydisc.json` | high |
| Fig. 3 | localization plot | Certified endpoint derivatives versus distance, with the two explicit Neumann-path envelopes and several sign blocks | `results/c02c_finite_window/open_windows.csv` | high |
| Fig. 4 | cocycle diagram | Chronological Hénon Jacobians, projective slope maps, and monodromy fixed slope for one primitive orbit | `results/c02_projective/periodic_monodromy.csv` | medium |
| Table 1 | theorem comparison | Assumptions, explicit domains, quantitative constants, finite-window gluing, and trace theorem across prior work and this paper | verified primary sources | high |
| Table 2 | claims/certificates | Each theorem claim, exact/numerical evidence, independent check, and artifact | current result directories | high |

**Figure 1 caption draft.**  “Logical status of the constructive Hénon
program.  This work proves the explicit complex itinerary, finite-window
endpoint and crossed-map matching bridges.  A trace-compatible infinite
operator approximation, nuclearity, Fredholm determinant, arithmetic divisor
and Hilbert--Pólya structure remain outside the current claim.”

This figure lets a skim reader see both the contribution and the non-claim
before encountering technical details.

## 7. Citation plan

- §1: Paper 5; the certified local horseshoe sources already frozen in the
  repository; representative area-preserving Hénon symbolic work.
- §2.1: Sterling--Dullin--Meiss equations (1), (3), (7), §5 and Theorem 3;
  state the explicit conjugacy to \(b=1,k=6\) and credit the real SFT and
  signed-root uniqueness theorem as prior art.
- §2.2: Hubbard--Oberste-Vorth and Oberste-Vorth on complex Hénon maps and
  complex horseshoes.
- §2.3: Rugh, *The correlation spectrum for hyperbolic analytic maps*
  (Nonlinearity 5, 1992), for pinning coordinates; Baladi--Pujals--Sambarino,
  Proposition 2.6 of *Dynamical zeta functions for analytic surface
  diffeomorphisms with dominated splitting*, for iterated analytic pinning
  maps and closure; distinguish BPS's orientation-twisted absolute determinant
  denominator from the proposed signed convention; Rugh on generalized
  Fredholm determinants for Axiom-A systems.  Use Bowen--Series and
  Guillopé--Lin--Zworski only where the Schottky comparison is mathematically
  exact.
- §3--§5: primary sources behind the repository's R058/R059 certificates and
  standard holomorphic fixed-point/implicit-function results.
- §6: Roberts--Vivaldi only if the finite reversible-map obstruction is
  discussed; otherwise leave C03 out of this paper.

Every bibliographic record must be verified from the published source or an
existing repository bibliography before BibTeX is written.

## 8. Falsifiers and stop rules

1. **Domain failure:** an admissible finite block and legal endpoint pair in
   the full frozen disks leaves the proposed internal polydisc.  This would
   contradict the intended T1 reduction; do not rescue it with a post-hoc
   shrink.  Record the exact case and stop T2.
2. **Localization failure:** endpoint derivatives do not admit a uniform
   exponential bound.  Report the worst word and distance; do not replace the
   chronological recurrence by an averaged transition matrix.
3. **Gluing failure:** direct union-solving and chronological two-coordinate
   interface gluing disagree beyond certified error.  Treat this as a theorem
   blocker; do not replace the pair by a scalar endpoint average.
4. **Prior-art collision:** a general theorem supplies T2--T4 verbatim and the
   Hénon specialization adds neither effective constants nor a new identity.
   Stop the manuscript and retain infrastructure.
5. **Pinning/trace failure:** endpoint solvers exist but do not yield exact
   crossed-map composition, cyclic-diagonal equivalence, or a natural frozen
   flat-trace weight.  Do not call T2 alone an operator construction.
6. **Operator failure:** finite-window analytic maps exist but no natural
   trace-compatible topology is found.  The current plan then returns to
   candidate search.  A coding-only paper requires a new external novelty
   review and is not the default fallback.
7. **HP firewall:** no Riemann-zero comparison, prime fitting, or Route B until
   a natural determinant exists and passes Route-A entry conditions.

## 9. Reproducible work packages

### WP0 — scoped source-location theorem-delta audit — complete for routing

- Compare the real signed-root/SFT claim directly with
  Sterling--Dullin--Meiss Theorem 3, including the conjugacy to \(b=1,k=6\).
- Compare T1--T4 directly with Baladi--Pujals--Sambarino Proposition 2.6,
  Hubbard--Oberste-Vorth, Oberste-Vorth and Rugh 1996.  Cross-check Rugh 1992's
  mechanism indirectly through BPS and the verified bibliographic record;
  the publisher full text was unavailable for a direct page audit.
- Freeze the only potentially publishable delta: explicit \(H_6\) constants,
  quantitative pinning/trace Jacobian or error bounds, and reproducible
  certification.
- Stop before C02C implementation if the delta is empty.
- Require a direct journal-level Rugh 1992/full novelty review before any
  eventual manuscript freeze; this is outside the completed routing audit.

### WP1 — analytic endpoint lemma — complete

- Freeze endpoint symbols and disks, internal local admissibility, norm, and
  exact output claims.
- Write the parameter-dependent contraction and Neumann-path proof using the
  full endpoint disks and the explicit \(a_0,\kappa,\beta\) constants.
- Derive extension-error estimates symbolically before enumerating words.

### WP2 — independent and adversarial checker — complete

- Enumerate admissible blocks through a frozen length.
- Compute interval enclosures for self-mapping, endpoint derivatives,
  extension discrepancies, and both interface matching equations.
- Treat enumeration as a regression/adversarial audit of the analytic proof,
  not evidence for existence or a substitute for the uniform Neumann bound.
- Include deliberately truncated ledgers and cyclic periods one and two.

### WP3 — crossed-map and trace-Jacobian theorem — complete

- Prove the crossed-map identity, exact two-interface composition, and
  cyclic-diagonal equivalence.
- Prove the matching-Jacobian/monodromy determinant identity for the certified
  local survivor and the frozen signed flat-trace weight.
- Recompute projective child disks for complex \(q\), derive project-specific
  quantitative error/distortion estimates, and submit them to WP4's novelty
  review.

### WP4 — paper versus infrastructure ruling — complete

- Update the WP0 comparison with the proved constants and trace identities.
- Decision: `RETAIN_EFFECTIVE_SPECIALIZATION; MANUSCRIPT_HOLD;
  NOVELTY_DELTA_UNCONFIRMED`.
- The effective constants and identities authorize design of a separate T4
  experiment, but do not by themselves clear the paper novelty threshold.

### WP5 — separate operator experiment plan — next authorized package

- WP4 authorizes protocol design, but not a paper claim: freeze the mixed
  holomorphic function space, kernels, orientation signs, one-step operator,
  norm, target trace, and a common-space finite-memory approximation that
  keeps the one-step clock before any computation.
- Test trace-compatible convergence without target data, counting the
  exponential growth of admissible cylinders in the aggregate error rate.
- Keep nuclearity and determinant continuation in this separate plan.

## 10. Review feedback incorporated

An independent mathematical audit verified the C02B theorem, including the
infinite-dimensional \(\ell^\infty\) holomorphy and the doubled period-one and
period-two chronology.  It identified no mathematical blocker, but it rejected
an immediate jump to nuclearity and identified a direct collision risk with
Rugh/Baladi--Pujals--Sambarino pinning theory.  Its minimum-fix
recommendation---audit prior art first, then prove only the explicit Hénon
endpoint bounds, two-coordinate crossed-map/trace Jacobian, and quantitative
delta---defines WP0--WP4 above.  The persisted review is
`refine-logs/PAPER_PLAN_AUDIT.md`.

The C02C theorem statement and the matching/Hill and complex-projective
derivations received separate independent mathematical audits.  A further
paper-level review is required after T4 has a frozen theorem statement and
before manuscript drafting begins; the external review endpoint normally used
by the paper workflow was not available in this environment.

## 11. Immediate next actions

- [x] Complete WP0's primary-source theorem-delta table.
- [x] Freeze and execute `code/C02C_FINITE_WINDOW_PROTOCOL.md`.
- [x] Prove the full-disk endpoint, localization, gluing, matching/Hill and
  complex-projective statements.
- [x] Run a separate producer and Newton-based independent checker, including
  truncation, tamper, scalar-average and reversed-chronology controls.
- [x] Decide the T2--T3 gate:
  `RETAIN_EFFECTIVE_SPECIALIZATION; MANUSCRIPT_HOLD;
  NOVELTY_DELTA_UNCONFIRMED`.
- [x] Freeze a separate C02D operator protocol: exact mixed
  interior/exterior function spaces, Cauchy kernels, orientation convention,
  potential, approximation norm, common-space embeddings, coding
  multiplicities and target trace.
- [x] Prove or falsify a trace-compatible cylinder truncation/error theorem
  with aggregate \(\tau_{\mathrm{eff}}<1\) before drafting LaTeX.
- [x] If C02D adds no theorem beyond a routine specialization, stop this lane
  and resume breadth-first candidate generation.
