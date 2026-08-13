# Paper Plan

**Working title:** *Finite-Rank Obstructions for Locally Constant Multiplier
Clocks: A Certified PCF Markov--Baker Case Study*

**One-sentence contribution:** We prove that every fixed finite-state,
finite-memory, locally constant scalar multiplier clock has finite rational
rank and therefore cannot realize all rational-prime logarithms exactly, and
we certify this obstruction on a compact piecewise-symplectic PCF
Markov--baker whose periodic lengths intersect the rational-prime logarithms
only at \(\log 2\).

**Paper type:** nonlinear-dynamics / mathematical-physics theory paper with a
certified-computation case study.

**Venue posture:** technical preprint for a narrow nonlinear-dynamics or
mathematical-physics outlet; no venue-fit claim before external review.

**Format:** generic 11pt LaTeX `article`, one-inch margins, author--year
`natbib`, following the organization of `papers/1-symp-vs-diss/paper` rather
than an ICLR/NeurIPS/ICML class.  The eventual production directory should use
`paper/manuscript.tex`, `paper/references.bib`, and reproducible vector assets
under `paper/figures/`.  Author metadata remains a placeholder at the planning
stage.

**Date:** 2026-08-13.

**Main-text budget:** approximately 11.25 pages from abstract through the end
of the conclusion, within the requested 10--13-page range; references and
technical appendices are outside this planning budget.

**Numbered section count:** 7.

## Narrative and framing

The paper should tell one story: an exact symbolic/symplectic carrier can be
mathematically valid while its frozen multiplier clock is arithmetically too
low-rank to support an exact all-prime ledger.  The general finite-rank
theorem is the contribution.  The three-state PCF Markov--baker is a fully
audited worked example and sharp rank-one certificate, not a novel natural
extension or a new parent zeta formula.

The manuscript must front-load the separation between three questions:

1. **Carrier:** does the finite branch history admit a compact, almost-
   everywhere invertible, piecewise-symplectic realization?
2. **Intrinsic orbit ledger:** are primitive cycles, repetitions, boundary
   quotients, and named determinant conventions internally exact?
3. **Arithmetic clock:** can the locally constant scalar multiplier lengths
   realize all rational-prime logarithms term by term?

The answers are respectively: yes on branch interiors and almost everywhere;
yes as an exact structural ledger; and no by a finite-rank theorem.  This
forces the final formal boundary

```text
carrier status: PASS_PIECEWISE_EXACT_SYMPLECTIC_INTERIORS
PRE_A0_STRUCTURAL_PASS
A0_FAIL / STRUCTURAL_ONLY
A1_WEAK (exact intrinsic ledger, but no A0 arithmetic labels)
A2--A4: STOP_SCOPED
Route B: FORBIDDEN
```

The abstract, introduction, hero figure, discussion, and conclusion must use
these labels consistently.  No sentence may convert the exact structural
ledger into an arithmetic A1 pass.

## Claims--evidence matrix

| ID | Claim to make in the paper | Evidence and artifact | Epistemic status | Main location |
|---|---|---|---|---|
| C1 | For a fixed finite graph with a finite-memory locally constant nonzero scalar multiplicative cocycle, every periodic instability length lies in a finite-dimensional \(\mathbb Q\)-span; at most that span dimension many distinct rational-prime logarithms can occur exactly. | Full finite-block recoding and unique-factorization proof in `PROOF_PACKAGE.md`; sharper \(V_{\mathrm{cyc}}\) bound and finite-loop sharpness example. | **PROVED AS STATED.** This is an exact termwise theorem, not a statistical assertion. | Sec. 3, full proof in main text. |
| C2 | The frozen three-state PCF branch history has a compact labeled three-rectangle realization that is almost-everywhere invertible and symplectic on every branch interior. | Exact PCF, Perron--Frobenius, strip-tiling, determinant-one, \(J^{\mathsf T}\Omega J=\Omega\), forward/inverse, and closed-boundary checks in `results/exact_preflight.json`; 89 passing tests; dyadic and folded-tent positive controls. | **PROVED for the formal piecewise-affine model / implementation certified.** Not a global \(C^1\) symplectomorphism and not an identification with the full inverse-limit continuum. | Sec. 4; algebraic details in App. A--B. |
| C3 | The unquotiented SFT ledger and parent-core ledger differ by exactly one declared boundary replacement: the symbolic period-two orbit \(1\leftrightarrow2\) is replaced by the parent fixed point \(d\), multiplying the zeta by \(1+z\). | Direct canonical-word enumeration and independent trace/Möbius inversion agree through period 20; `results/ledger.json`; independent 100-digit inverse-branch audit in `results/parent_audit.json` with maximum residual \(9.706\times10^{-98}\). | **EXACTLY VERIFIED, but prior-art reproduction.** The boundary-discrepancy mechanism and parent determinant are not novelty claims. | Sec. 5; Fig. 2. |
| C4 | The inherited factor-orientation diagnostic is exactly nilpotent, \(W^3=0\), so \(\det(I-zW)=1\) and every positive-period signed trace vanishes; these signs are not symplectic orientations or quantum phases. | Exact symbolic audit in `results/exact_preflight.json`; all-positive-sign null preserves \(A\), areas, unsigned cycles, and symplecticity while removing nilpotence. | **EXACT DIAGNOSTIC / convention-sensitive.** No A4 evidence. | Sec. 5; determinant-convention display. |
| C5 | For the frozen constant-slope candidate, every primitive period \(2k\) orbit has \(|\Lambda_u|=2^k\) and length \(k\log2\); hence the exact rational-prime intersection is only \(p=2\), and \(Z_u(s)=1/(1-2^{1-s})\). | Candidate corollary in `PROOF_PACKAGE.md`; exact period-1--20 ledger; exact graph determinant in `results/ledger.json`. | **PROVED.** This is the branch-baker cocycle, not the nonlinear parent derivative cocycle. | Sec. 5, Corollary and Fig. 2. |
| C6 | The mathematical and software certificates reproduce the frozen predictions without split dependence. | Six exact preflight gates; 226 primitive SFT cycles through period 20; dyadic total 747 through period 12; three split-specific runs of \(65{,}536\times256=16{,}777{,}216\) per-step checks, each with maximum roundtrip error \(1.388\times10^{-16}\), zero edge mismatches, and zero boundary failures; six matched controls. | **CERTIFIED COMPUTATION.** Deterministic implementation stress, not independent sampling or interval certification. | Sec. 6; Table 3. |
| C7 | The candidate is a structural positive control and an arithmetic negative result: A0 fails and formal A1 remains weak. | `results/analysis_{development,validation,test}.json`, `results/final_result_manifest.json`, `results/VALIDATION_REPORT.md`, and final Route-A YAML. | **FORMAL SCOPE DECISION:** `A0_FAIL / STRUCTURAL_ONLY`, `A1_WEAK`, `ROUTE_A_REJECTED`. | Abstract, Sec. 1, Sec. 7. |

### Claims that must not appear

- No global no-go theorem for arbitrary smooth symplectic maps, variable
  derivatives, point-dependent or Hölder roofs, countable-state systems,
  infinite memory, or growing model families.
- No exclusion of approximate, statistical, density-level, or cancellation-
  based prime resemblance.
- No Riemann dynamical determinant, Riemann-zero comparison, functional
  equation, Hilbert--Pólya operator, canonical action, or natural
  quantization.
- No claim that a generalized baker construction, the parent zeta, the single
  boundary-period correction, or generic baker quantization is new.
- No substitution of the nonlinear quadratic-parent derivative cocycle for
  the constant-slope branch-baker monodromy.
- No use of `A1_PASS`; the only formal label is `A1_WEAK`.

## Main-text structure and page budget

| Part | Planned pages | Running total |
|---|---:|---:|
| Abstract | 0.35 | 0.35 |
| 1. Introduction | 1.20 | 1.55 |
| 2. Prior Work and Claim Boundary | 1.10 | 2.65 |
| 3. Finite-Memory Clocks and the Finite-Rank Obstruction | 2.00 | 4.65 |
| 4. A Compact PCF Markov--Baker Carrier | 1.85 | 6.50 |
| 5. Periodic Ledger, Boundary Quotient, and Candidate Corollary | 1.75 | 8.25 |
| 6. Certified Verification and Matched Controls | 2.10 | 10.35 |
| 7. Discussion and Conclusion | 0.90 | 11.25 |

### Abstract (about 180--220 words; 0.35 page)

- **Sentence 1 -- achievement:** state the finite-rank obstruction for one
  fixed finite-state, finite-memory, locally constant scalar multiplier
  clock.
- **Sentence 2 -- why it matters:** explain that exact symbolic carriers and
  rational dynamical zetas do not by themselves supply a rational-prime
  clock.
- **Sentence 3 -- approach:** introduce the three-state PCF Markov factor and
  compact labeled Markov--baker as a fully auditable rank-one case.
- **Sentence 4 -- evidence:** report exact branch symplecticity, two agreeing
  primitive-cycle enumerations, the unique boundary quotient, six controls,
  and the independent high-precision audit.
- **Sentence 5 -- memorable result and boundary:** report 226 primitive SFT
  cycles through period 20 and
  \(|\Lambda_u|=2^k\), so only \(\log2\) intersects the rational-prime
  logarithms; conclude `A0_FAIL / STRUCTURAL_ONLY` and `A1_WEAK`, while
  explicitly limiting the theorem to locally constant scalar clocks.
- **Self-contained check:** define “multiplier clock” in plain language before
  using the term; do not mention internal file names, split seeds, or Route A
  without a short explanation.

### 1. Introduction (1.20 pages)

- **Opening hook:** “A finite symbolic model may carry every orbit exactly and
  still carry too little metric information to support an arithmetic
  correspondence.”  Avoid a generic Hilbert--Pólya opening.
- **Problem:** separate orbit-carrier validity from the exact instability
  clock needed for a termwise rational-prime ledger.
- **Gap:** classical kneading determinants, generalized bakers, natural
  extensions, and baker quantizations establish rich dynamical structure, but
  none of those facts prevents a frozen locally constant length group from
  having finite rational rank.
- **One-sentence contribution:** reproduce the exact sentence at the top of
  this plan, without broadening its hypotheses.
- **Approach preview:**
  1. prove the general finite-memory finite-rank theorem;
  2. build the exact PCF branch-history carrier;
  3. separate unsigned, parent, factor-orientation, Lefschetz, and multiplier
     objects;
  4. certify the case with exact enumeration, an independently implemented
     parent audit, and matched controls.
- **Contribution bullets:**
  1. the theorem, sharper cycle-space bound, and sharp finite-rank example;
  2. a convention-safe, source-locked PCF Markov--baker certificate;
  3. the proved rank-one corollary and formal `A0_FAIL / A1_WEAK` outcome.
- **Result preview:** surface
  \(L(C)=k\log2\), \(Z_u(s)=1/(1-2^{1-s})\), the period-1--20 total 226,
  and the single boundary quotient before the section roadmap.
- **Hero figure:** place Fig. 1 at the end of the introduction or top of page
  2.  A skim reader should see “valid carrier \(\not\Rightarrow\) adequate
  arithmetic clock” without reading the construction.
- **Key citations:** Berry--Keating only for motivation; Alsedà et al. for the
  directly colliding parent determinant; Bose and Bruin--Kalle for classical
  baker/natural-extension context.
- **Front-loading check:** by the end of the first page, the reader must know
  the theorem assumptions, the rank-one candidate outcome, and the fact that
  no Riemann-zero comparison was run.

### 2. Prior Work and Claim Boundary (1.10 pages)

Organize by methodological family, not as a paper-by-paper list.

1. **PCF interval maps, kneading, and periodic boundary corrections.** Place
   the \(RLR^\infty\) parent determinant and one-orbit boundary discrepancy
   squarely inside prior art.  Cite Alsedà et al., Hofbauer, and weighted
   kneading work.
2. **Natural extensions and generalized baker maps.** Explain that compact
   branch-history realizations and piecewise-affine baker constructions are
   classical platforms.  This paper audits one such platform; it does not
   introduce the general method.
3. **Signed/weighted determinants and baker quantization.** Separate factor
   orientation from symplectic orientation, Maslov phases, and quantum
   boundary phases.  Generic quantizability is downstream precedent, not an
   A4 result.
4. **Arithmetic spectral motivation.** Use one restrained paragraph to
   distinguish rational-prime logarithms from generic prime-orbit theorems
   and to motivate the exact termwise test.  Do not turn the related-work
   section into a Riemann-zero survey.

Include Table 1, “Known prior-art collisions and frozen treatment.”  End the
section with the narrow novelty statement: the contribution is the explicit
finite-clock obstruction certificate, its sharp rank bound, and an audited
worked case.  Do not claim the theorem is historically first without a wider
theorem-focused literature search.

### 3. Finite-Memory Clocks and the Finite-Rank Obstruction (2.00 pages)

- **Definitions:** finite directed graph \(G\), memory \(m\), allowed block
  set \(\mathcal B_m\), nonzero scalar block multipliers
  \(\mu_b\in\mathbb C^\times\), periodic orbit \(C\),
  \[
  L(C)=\sum_{b\in C}\log|\mu_b|,
  \qquad
  V=\operatorname{span}_{\mathbb Q}
  \{\log|\mu_b|:b\in\mathcal B_m\}.
  \]
  Define the smaller periodic space \(V_{\mathrm{cyc}}\) before stating the
  sharp bound.
- **Theorem 1 (main contribution):** every periodic length belongs to \(V\),
  \(\dim_{\mathbb Q}V<\infty\), and the number of distinct exact rational-
  prime logarithms in the periodic clock is at most
  \(\dim_{\mathbb Q}V_{\mathrm{cyc}}\leq\dim_{\mathbb Q}V\).
- **Full proof in the main text:**
  1. recode finite memory as an edge-local cocycle on the finite higher-block
     graph;
  2. express every orbit length as an integer combination of finitely many
     local log-moduli;
  3. prove \(\mathbb Q\)-linear independence of distinct \(\log p\) by
     clearing denominators, exponentiating, and applying unique
     factorization;
  4. conclude the cardinality bound.
- **Sharpness paragraph:** one vertex with \(r\) self-loops weighted by
  \(p_1,\ldots,p_r\) realizes \(r\) independent prime-log lengths.  State
  immediately that this inserts a finite prime list and is not an arithmetic-
  origin construction.
- **Essential assumptions:** locally constant, finite memory, one fixed finite
  graph, scalar multiplicative cocycle, modulus-based additive clock, exact
  termwise containment.
- **Out-of-scope classes:** point-dependent or Hölder roofs, countably many
  states, infinite memory, growing finite models, matrix spectral radii or
  singular-value clocks, approximate matching, and phase-sensitive
  cancellation.
- **Theory comparison:** Table 2 should make the theorem boundary visible at
  a glance.
- **Proof placement:** no part of Theorem 1's logical proof goes to the
  appendix.  Only a short standard higher-block construction diagram or
  expanded notation may move to App. C.

### 4. A Compact PCF Markov--Baker Carrier (1.85 pages)

- **Exact parent:** define \(f_u(x)=1-ux^2\), with \(u\) the unique real root
  in \((3859/2500,15437/10000)\) of
  \(u^3-2u^2+2u-2=0\), set \(d=u-1\), and record
  \(0\mapsto1\mapsto-d\mapsto d\mapsto d\).
- **Partition and matrices:**
  \[
  I_0=[-d,0],\quad I_1=[0,d],\quad I_2=[d,1],
  \]
  \[
  A=\begin{pmatrix}0&0&1\\0&0&1\\1&1&0\end{pmatrix},
  \qquad
  W=\begin{pmatrix}0&0&1\\0&0&-1\\-1&-1&0\end{pmatrix}.
  \]
  Call \(W\) the *factor-orientation matrix* every time it first appears in a
  new section.
- **PF geometry:** derive \(\lambda=\sqrt2\), normalized left/right vectors
  \((1/2,1/2,1/\sqrt2)\), and rectangle areas
  \((1/4,1/4,1/2)\).
- **Carrier construction:** define the labeled compact disjoint union of three
  rectangles, source vertical strips, destination horizontal strips, and the
  branch derivative
  \[
  DB_{ij}=\operatorname{diag}
  (\sigma_{ij}\sqrt2,\sigma_{ij}/\sqrt2).
  \]
- **Proposition 2:** every allowed branch has determinant one and preserves
  the standard symplectic form; the half-open map is almost-everywhere
  invertible, while the closed-boundary object is a relation.  If “exact
  symplectic” is retained, explicitly exhibit the exact difference of the
  standard Liouville primitives on each affine branch rather than treating
  \(J^{\mathsf T}\Omega J=\Omega\) alone as the definition.
- **Claim boundary immediately after the proposition:** piecewise affine on
  branch interiors, not a global \(C^1\) symplectomorphism; branch-history
  carrier, not a homeomorphism with the full topological inverse-limit
  continuum; no smooth-submersion factor.
- **Proof placement:** main text gives PF tiling, determinant/symplectic
  calculation, and inverse idea.  App. A gives exact root isolation and
  endpoint images; App. B gives strip offsets, complete forward/inverse
  formulas, half-open conventions, and boundary relation tables.

### 5. Periodic Ledger, Boundary Quotient, and Candidate Corollary (1.75 pages)

- **Primitive/repetition separation:** introduce
  \(N_n=\operatorname{tr}(A^n)\) and
  \(N_n=\sum_{d\mid n}dP_d\).  State that direct canonical-word enumeration
  and independent Möbius inversion agree through period 20.
- **Exact ledger:** display the vector compactly or in Fig. 2,
  ```text
  0,2,0,1,0,2,0,3,0,6,0,9,0,18,0,30,0,56,0,99,
  ```
  totaling 226 unquotiented primitive SFT orbits.
- **Boundary quotient:** prove that replacing the symbolic period-two ghost
  \(1\leftrightarrow2\) by the fixed point \(d\) gives primitive-count delta
  \((+1,-1,0,\ldots)\), factor
  \((1-z^2)/(1-z)=1+z\), and
  \[
  \zeta_A(z)=\frac1{1-2z^2},
  \qquad
  \zeta_f(z)=\frac{1+z}{1-2z^2}.
  \]
  Label this a prior-art reproduction baseline.
- **Convention-safe determinant display:** keep all objects distinct:
  \[
  \det(I-zW)=1\quad(W^3=0),
  \qquad D_{\mathrm{or,parent}}(z)=1-z,
  \qquad \zeta_{\mathrm{Lef}}(z)=\frac1{1-z}.
  \]
  The corresponding factor-orientation multiplier product is one.  Never
  call \(1-z\) a Lefschetz zeta.
- **Corollary 3 (candidate clock):** bipartiteness forces every closed walk to
  have period \(2k\); hence
  \[
  |\Lambda_u(C)|=2^k,\qquad L(C)=k\log2,
  \]
  and only \(p=2\) can satisfy \(L(C)=\log p\).  Derive
  \[
  Z_u(s)=\det(I-2^{-s/2}A)^{-1}
        =\frac1{1-2^{1-s}}
        =\frac{2^s}{2^s-2},
  \qquad \operatorname{Re}s>1,
  \]
  followed by its elementary meromorphic continuation.
- **Interpretation:** this is a complete conclusion for the frozen constant-
  slope baker clock, not for the nonlinear parent derivative cocycle.
- **Proof placement:** determinant calculations and Corollary 3 stay in the
  main text.  App. C may contain the full period-1--20 representative ledger
  and enumeration pseudocode.

### 6. Certified Verification and Matched Controls (2.10 pages)

- **Protocol before results:** briefly explain source locking, the one
  mechanical development-seed correction before any execution, the
  validation/test hash gates, and the prohibition on prime and zero data.
  Keep hashes and full access logs in App. D.
- **Exact preflight:** report six of six gates: algebra, candidate cycle
  ledger, controls, the single boundary quotient, static isolation, and zeta
  convention separation.
- **Independent parent audit:** emphasize independent closed-word enumeration
  and high-precision monotone inverse branches; 100 decimal digits, residual
  \(9.706\times10^{-98}<10^{-75}\), and exactly one declared periodic
  duplicate through period 20.  Call this a high-precision consistency audit,
  not interval certification.
- **Floating implementation stress:** three mechanically derived seeds,
  \(65{,}536\) interior points, 256 per-step forward/identified-inverse checks,
  \(16{,}777{,}216\) completed checks per split, maximum error
  \(1.388\times10^{-16}\), zero edge mismatches, and zero boundary failures.
  State that these checks are deterministic software audits, not independent
  statistical observations or long-time chaotic reversal.
- **Six controls and their roles:**
  1. dyadic baker: positive orbit/inverse control, 747 primitive necklaces
     through period 12;
  2. folded tent baker: both stable and unstable coordinates reverse on a
     decreasing branch while determinant stays \(+1\);
  3. matched dissipative map: same future graph but determinant \(1/2\) and
     non-surjective image;
  4. label erasure: loses unique past reconstruction;
  5. anti-symplectic branch: one-coordinate sign reversal gives determinant
     \(-1\) and must be rejected;
  6. all-positive-sign null: same unsigned carrier but no nilpotent factor-
     orientation cancellation.
- **Table 3:** map each exact/numerical audit to the claim it supports and the
  inference it does *not* support.
- **Statistical statement:** no \(p\)-values, confidence intervals, effect
  sizes, or binomial success claims are appropriate.  Cross-split identity
  checks implementation stability only.
- **Proof/evidence placement:** main text retains the summary table and one
  paragraph per audit family.  App. D contains seeds, hashes, environment,
  software versions, static-isolation details, and complete control outputs.

### 7. Discussion and Conclusion (0.90 page)

- **What the result establishes:** a compact piecewise-symplectic carrier and
  exact intrinsic ledger can coexist with a provably inadequate arithmetic
  clock.
- **Formal assessment:** say exactly `A0_FAIL / STRUCTURAL_ONLY` and
  `A1_WEAK`; retain the carrier as a structural positive control and
  arithmetic negative control.  A2--A4 and Route B remain closed.
- **Why the no-go is useful:** it eliminates an entire fixed finite-state,
  finite-memory, locally constant scalar-clock design class before any
  target-data fitting or quantization.
- **Limitations:** repeat the essential theorem boundary in compact prose;
  mention direct prior art for the parent determinant, boundary discrepancy,
  generalized baker platform, and generic baker quantization.
- **Future work:** only independently motivated new candidates may test
  point-dependent roofs, countable-state extensions, growing models,
  coupling, smoothing, or higher dimension.  Each requires a new source lock
  and arithmetic-origin audit; none is an extension experiment inside this
  frozen candidate.
- **Final sentence:** end on the carrier/clock separation, not on speculative
  Riemann-zero matching.

## Proof placement and appendix plan

| Formal item | Main-text treatment | Appendix support |
|---|---|---|
| Theorem 1: finite-rank clock obstruction | Full statement, assumptions, all four proof steps, sharper \(V_{\mathrm{cyc}}\) bound, and sharpness example | Optional higher-block diagram only; no logical step outsourced |
| Proposition 2: compact piecewise-symplectic carrier | PF tiling, branch Jacobian, determinant/symplectic calculation, and almost-everywhere inverse idea | App. A: Sturm/root and PCF endpoint algebra; App. B: offsets, complete forward/inverse formulas, boundary tables, Liouville exactness calculation if claimed |
| Boundary-quotient identity | Full one-cycle replacement and Euler-factor derivation | App. C: full primitive ledger and canonical representatives |
| \(W^3=0\) and convention separation | Explicit matrices and exact determinant identities | App. C: expanded trace calculation if useful |
| Corollary 3: rank-one candidate clock | Full proof and multiplier product in main text | App. C: row-wise period/multiplier ledger |
| Certified-computation claims | Compact evidence table and interpretation limits | App. D: source-lock amendment, seeds, hashes, environment, full audit/control outputs |

The theorem proof, candidate corollary, single boundary correction, and
determinant-convention dictionary are non-negotiable main-text material.  If
the paper exceeds 13 pages, move implementation detail rather than any of
these logical components.

## Figure and table plan

### Figure 1 -- Hero figure: valid carrier, insufficient clock

- **Type:** three-panel vector schematic, high priority.
- **Panel A, parent and symbolic graph:** show the exact critical itinerary
  \(0\to1\to-d\to d\), the three intervals \(I_0,I_1,I_2\), and the four
  allowed graph edges encoded by \(A\).
- **Panel B, compact carrier:** show three labeled rectangles of areas
  \(1/4,1/4,1/2\); vertical source strips mapping to horizontal destination
  strips; simultaneous coordinate reversal on negative-sign branches; and a
  small boundary annotation showing \(1\leftrightarrow2\mapsto d\).  Label
  each branch `det = 1`, not “globally smooth.”
- **Panel C, arithmetic obstruction:** place all candidate periodic lengths on
  the one-dimensional lattice \(k\log2\), contrast it with the rationally
  independent family \(\{\log p\}\), and highlight the sole exact intersection
  \(\log2\).  A final arrow should read “carrier verified; exact all-prime
  clock excluded.”
- **Data source:** exact source-lock constants plus `results/ledger.json`; no
  external prime table is needed--only symbolic labels such as
  \(\log2,\log3,\log5,\ldots\) in the explanatory schematic, or omit all but
  \(\log2\) and a generic \(\log p\) family to preserve the data boundary.
- **Visual rules:** vector PDF, colorblind-safe palette, distinct line styles,
  readable in grayscale, no decorative internal title.
- **Draft caption:** “Carrier validity does not imply arithmetic adequacy.
  The PCF interval partition yields a three-state branch history (left), whose
  Parry-affine realization is compact and symplectic on each branch interior
  (center).  Nevertheless every period-\(2k\) orbit has instability length
  \(k\log2\), so the exact rational-prime logarithms intersect the clock only
  at \(\log2\) (right).  The boundary cycle
  \(1\leftrightarrow2\) is separately quotiented to the parent fixed point
  \(d\).”
- **Why it earns the hero position:** it conveys the theorem/case-study story
  and the carrier-versus-clock distinction before the reader reaches formal
  notation.

### Figure 2 -- Exact primitive ledger and boundary quotient

- **Type:** two-panel exact stem/bar plot, high priority.
- **Panel A:** period \(n=1,\ldots,20\) versus primitive orbit count, with
  separate markers for the unquotiented SFT and parent-core quotient.  Show
  the vanishing odd-period SFT counts and use a log-compatible presentation
  without hiding zeros.
- **Panel B:** primitive-count delta, highlighting only \(+1\) at period 1
  and \(-1\) at period 2; annotate the unstable/stable multiplier moduli
  \(2^k\) and \(2^{-k}\) along even periods.
- **Data source:** `results/ledger.json` only.
- **Draft caption:** “Two independent exact enumerations give 226 primitive
  SFT cycles through period 20.  The parent quotient changes only the declared
  boundary pair: it adds the fixed point \(d\) at period 1 and removes the
  symbolic orbit \(1\leftrightarrow2\) at period 2; all higher primitive
  counts agree.  Every unquotiented period-\(2k\) multiplier has moduli
  \(2^k\) and \(2^{-k}\).”

### Table 1 -- Known prior-art collisions and claim treatment

Rows: \(RLR^\infty\) parent determinant; monotonicity-boundary period
discrepancy; weighted kneading/boundary correction; generalized baker/natural
extension; baker quantization.  Columns: closest verified source, what it
already establishes, what this paper reproduces, and what remains the narrow
contribution.  This table prevents the worked example from being mistaken for
the novelty claim.

### Table 2 -- Scope and sharpness of the finite-rank theorem

Rows: fixed finite locally constant scalar clock; finite-memory recoding;
explicit finite prime-weight loops; point-dependent/Hölder roof; countable or
infinite-memory shift; growing sequence of finite models; matrix spectral-
radius/singular-value clock; approximate matching.  Columns: finite rational
rank forced?, exact termwise theorem applies?, reason, and paper treatment.

### Table 3 -- Certified evidence and inference boundary

Rows: PCF/root identities; branch symplecticity/inverse; primitive ledger;
single boundary quotient; signed nilpotence; 100-digit parent audit; three
floating splits; six controls; static isolation.  Columns: frozen target,
observed result, status, claim supported, and prohibited inference.  Use
`results/exact_preflight.json`, `results/ledger.json`,
`results/parent_audit.json`, the three `float_stress_*.json` files, and
`results/final_result_manifest.json`.

## Citation plan

### Verified primary sources already available

The following metadata are recorded as verified in
`notes/NOVELTY_AUDIT.md`; later BibTeX must be obtained from the DOI,
publisher, or authoritative record rather than generated from memory.

| Source | Verified locator | Planned use |
|---|---|---|
| Alsedà, Bobok, Misiurewicz, and Snoha, *The Real Teapot* (2025) | <https://doi.org/10.1017/etds.2025.15> | Direct collision for \(K_{\sqrt2}=RLR^\infty\) and the parent determinant; Secs. 1, 2, and 5 |
| Hofbauer, *Periodic points for piecewise monotonic transformations* (1985) | <https://doi.org/10.1017/S014338570000287X> | Period discrepancy at monotonicity boundaries; Secs. 2 and 5 |
| Rugh and Tan, *Kneading with weights* (2015) | <https://doi.org/10.4171/JFG/24> | Weighted boundary/determinant convention context; Sec. 2 |
| Bose, *Generalized baker's transformations* (1989) | <https://doi.org/10.1017/S0143385700004788> | Classical generalized-baker construction; Secs. 1, 2, and 4 |
| Bruin and Kalle, *Natural extensions for piecewise affine maps via Hofbauer towers* | <https://arxiv.org/abs/1306.5451> | Natural-extension construction context; Secs. 2 and 4; verify and prefer the published version before bibliography freeze |
| Balazs and Voros, *The quantized baker's transformation* (1989) | <https://doi.org/10.1016/0003-4916(89)90259-5> | Generic baker quantization as prior precedent, and why it does not open A4; Secs. 2 and 7 |
| Berry and Keating, *The Riemann Zeros and Eigenvalue Asymptotics* (1999) | <https://doi.org/10.1137/S0036144598347497> | Restrained arithmetic-spectral motivation only; Sec. 1 |

### References requiring verification before use

- Artin--Mazur's original dynamical-zeta reference: **[VERIFY exact published
  metadata]** before citing the name historically.
- Milnor--Thurston kneading theory (1988): **[VERIFY exact title, venue, and
  published version]**.
- Saraceno's parity-symmetric baker quantization (1990): **[VERIFY exact
  bibliographic metadata]**; cite only if the A4-prior-art paragraph needs a
  second source.
- A standard symbolic-dynamics source for higher-block presentations and
  Möbius orbit inversion: **[VERIFY and select one authoritative text or
  primary source]**.  The theorem proof must remain self-contained even after
  adding this citation.

### Section-level citation scaffolding

- **Sec. 1:** Berry--Keating for motivation; Alsedà et al. and Bose to signal
  immediately that the parent determinant and baker construction are prior
  art.
- **Sec. 2:** all direct-collision sources, synthesized by family; do not write
  a chronological bibliography dump.
- **Sec. 3:** one verified standard higher-block/SFT citation if useful; the
  unique-factorization argument needs no exotic arithmetic citation.
- **Sec. 4:** Bose and Bruin--Kalle for construction context.
- **Sec. 5:** Alsedà et al., Hofbauer, and Rugh--Tan around the parent and
  boundary identities.
- **Sec. 6:** artifacts and reproducibility record, not literature claims.
- **Sec. 7:** Balazs--Voros (and Saraceno only after verification) to explain
  why generic quantization does not overcome A0.

### Citation integrity rules

- Do not claim “first” or “novel theorem” until a theorem-focused literature
  search has checked finite-rank length-group obstructions beyond the targeted
  novelty audit.
- Prefer published versions over arXiv when both are available.
- Build `references.bib` only from verified metadata; never synthesize author,
  title, year, pages, or DOI fields from memory.
- Every prior-art collision must be cited at the first corresponding formula,
  not only in a general related-work paragraph.

## Known prior-art collision and novelty posture

The manuscript must include an explicit disclosure, preferably in Sec. 2 and
again beside the relevant formula in Sec. 5:

1. the parent-core determinant
   \((1-2z^2)/(1+z)\), equivalently
   \(\zeta_f(z)=(1+z)/(1-2z^2)\), appears directly for the
   \(RLR^\infty\) case in *The Real Teapot*;
2. symbolic/parent period discrepancies at monotonicity boundaries are
   classical in Hofbauer's framework;
3. weighted boundary corrections predate this case;
4. generalized baker/natural-extension constructions are classical;
5. baker quantization is classical and supplies no arithmetic evidence here.

Accordingly, the paper is not sold as a new PCF zeta, a new natural extension,
or a new quantized baker.  Its defensible novelty is deliberately narrow: an
explicit finite-memory finite-rank obstruction, the sharper periodic-space
bound and sharpness discussion, and a convention-safe certified worked
example.  The frozen novelty estimate is modest (roughly 4--5/10 for the case,
potentially about 6/10 for the clean theorem/certificate package), so precise
scope is more credible than broad rhetoric.

## Terminology and notation lock

- Use **PCF Markov--baker** or **branch-history carrier** consistently.
- Use **piecewise symplectic on branch interiors** by default.  Use **exact
  symplectic** only after defining the chosen Liouville primitive and proving
  branchwise exactness.
- Use **factor orientation** for \(W\); never shorten it to “symplectic
  orientation,” “phase,” or “Maslov sign.”
- Use **parent-core Artin--Mazur zeta**, **unsigned SFT/baker zeta**,
  **factor-orientation determinant/object**, **Lefschetz zeta**, and
  **multiplier-clock product** as five named, separate conventions.
- Use **high-precision consistency audit**, not interval certification.
- Use **per-step forward/identified-inverse stress**, not 256-step chaotic
  reversal.
- Use **exact termwise all-prime obstruction**; never abbreviate it to “prime
  obstruction” without the theorem assumptions in the same paragraph.
- Reserve \(n\) for orbit period, \(k=n/2\) for the candidate's even-period
  index, \(L(C)\) for instability length, \(A\) for unsigned adjacency, and
  \(W\) for factor-orientation weights.

## Reproducibility and disclosure plan

- State that no external prime table or Riemann-zero data were accessed.
- Disclose the source-lock version-2 development-seed correction as a
  mechanical transcription repair made before any candidate execution; do
  not conceal it or overemphasize it in the main narrative.
- Put the source-lock hash, code-tree hash, split seed derivation, environment,
  access log, and verification-chain details in App. D or a reproducibility
  statement.
- Report all 89 tests and the six exact preflight gates, but do not equate test
  count with scientific proof.
- Disclose AI-assisted coding/review according to the eventual outlet's
  policy, outside the core scientific claims.
- Use anonymous/placeholder author metadata until the manuscript-production
  stage applies the established project configuration.

## Self-review of mathematical consistency

- [x] The one-sentence contribution includes every essential theorem
  qualifier: fixed, finite-state, finite-memory, locally constant, scalar,
  multiplicative, and exact rational-prime logarithms.
- [x] The sharper bound uses \(V_{\mathrm{cyc}}\), while the simpler theorem
  remains valid with \(V\).
- [x] The candidate corollary uses only the constant-slope baker cocycle and
  does not substitute the nonlinear parent derivative.
- [x] The boundary quotient removes \(1\leftrightarrow2\), adds \(d\), and
  multiplies the unsigned zeta by
  \((1-z^2)/(1-z)=1+z\).
- [x] The zeta and determinant formulas agree with the frozen ledger:
  \(\det(I-zA)=1-2z^2\),
  \(\zeta_A=(1-2z^2)^{-1}\),
  \(\zeta_f=(1+z)/(1-2z^2)\),
  \(W^3=0\), and \(\det(I-zW)=1\).
- [x] The multiplier product
  \(Z_u(s)=1/(1-2^{1-s})=2^s/(2^s-2)\) is assigned only to the
  unquotiented constant-slope SFT/baker and initially to
  \(\operatorname{Re}s>1\).
- [x] The factor-orientation parent object \(1-z\) is kept distinct from the
  Lefschetz zeta \(1/(1-z)\).
- [x] The period-1--20 primitive vector totals 226; the dyadic period-1--12
  control totals 747.
- [x] The computational figures match the final JSON: 100 digits,
  \(9.706\times10^{-98}\) maximum parent residual, 293 maximum inverse
  iterations, \(16{,}777{,}216\) checks per split,
  \(1.388\times10^{-16}\) maximum roundtrip error, zero edge mismatches, and
  zero boundary failures.
- [x] Carrier geometry is separated from formal Route-A A1; the plan never
  upgrades `A1_WEAK` to a pass.
- [x] The plan neither opens A2--A4/Route B nor claims a Riemann determinant,
  global smooth symplectomorphism, or canonical quantization.

## Page-feasibility self-review

The 11.25-page main-text allocation is feasible in the Paper-1-style 11pt
article format if the manuscript follows these constraints:

1. keep the abstract below 220 words and the introduction near 1.2 pages;
2. use one hero figure, one ledger figure, and three compact tables;
3. keep the full core theorem proof in approximately 1.25 pages;
4. move root isolation, affine offsets, full orbit representatives, seeds,
   hashes, software environment, and detailed control outputs to appendices;
5. avoid a standalone long Riemann/Hilbert--Pólya survey;
6. combine discussion and conclusion into one numbered section.

If a compiled draft exceeds 13 main-text pages, cut in this order:

1. shorten protocol prose and move all hash/access details to App. D;
2. compress the control descriptions into Table 3;
3. move expanded determinant algebra and enumeration pseudocode to App. C;
4. compress the prior-art table captions and related-work exposition.

Do **not** cut the full finite-rank proof, candidate corollary, unique boundary
factor, determinant-convention separation, known-collision disclosure, or
`A0_FAIL / A1_WEAK` limitation paragraph.  Those are the paper's logical and
integrity backbone.

## Review readiness and next steps

This plan has been self-audited against the source lock, proof package, final
results, validation report, novelty audit, raw result JSON, and final Route-A
evaluation.  A separate outline review should still challenge whether the
finite-rank theorem is sufficiently distinguished from an elementary linear-
algebra observation and whether the paper's modest novelty supports the
chosen outlet; the minimum response is tighter positioning, not broader
claims or new post-hoc experiments inside the frozen candidate.

- [ ] Verify the remaining bibliography items and generate
  `paper/references.bib` from authoritative metadata.
- [ ] Generate Fig. 1, Fig. 2, and Tables 1--3 as reproducible vector assets.
- [ ] Draft `paper/manuscript.tex` section by section using this plan.
- [ ] Compile in the Paper-1-style `article` layout and enforce the 10--13
  main-page budget.
- [ ] Run mathematical, novelty, integrity, and claim-language review before
  finalization.

