# Paper Plan

**Working title:** A Period-Three Residue Law on an Exceptional Hénon Family  
**One-sentence contribution:** On the complete normalized quartic Hénon fiber whose formal fixed-point trace multiset is $0^{\times4}$, a source-proved exact period-three trace moment is the first conjugacy-separating low-period invariant, and the same proof architecture yields an all-$m$ two-term law with an explicit finite slope certificate while universal slope nonvanishing remains open.  
**Candidate/lifecycle:** `henon_period3_residue_proof_note_v1`  
**Format:** proof-only specialist note in algebraic/complex dynamics  
**Target venue:** specialist journal, to be selected after asset and manuscript review  
**Date:** 2026-08-16 UTC  
**Planning budget:** 21.5 main-text pages through the conclusion, excluding references  
**Section count:** 7 numbered sections, plus abstract and references  
**Evidence mode:** theorem proof only; no experimental, registered-result, runtime, or computational-result evidence

## Authority and evidence firewall

This plan is derived only from the eight-file closed allowlist in
`experiments/proof_only_manuscript_lock.json` at SHA-256
`2c7f056b7f9566f754a06c30417105c0b1cefb2d0081f4bca8bb3a00adbf8eeb`
and the independent handoff at SHA-256
`407cec5bf295c29330c24ae461dca86ad1bf54d77f44d477d83a821bf7e41711`.
The sole scientific authority is `notes/PROOF_PACKAGE.md` at SHA-256
`36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9`.
The handoff verdict is `PROOF_ONLY_HANDOFF_PASS`; it authorizes proof-only
drafting but not finalization or submission.

The consumed registered audit may enter only as a short provenance and
non-evidence disclosure. It supplies no theorem, coefficient, comparison,
figure, or table. No manuscript asset may state or imply successful Track Q,
Track R, or adjudicator execution; Q/R agreement; a registered coefficient
match; result certification; empirical support; a retained traceback; or any
value of the prohibited diagnostics. The roots `code/`, `preexecution/`,
`results/`, and `runtime/` are recursively excluded as manuscript evidence.

## What / Why / So What

- **What:** prove a formal period-three two-term residue law for
  $f_{m,a}(x,y)=(y+(x^m-a)^2,x)$, give a transparent finite certificate for
  its slope $D_m$, and obtain the exact quartic formula
  $S_2^{(3)}(L)=-384(3375+4096L^3)$.
- **Why:** Cantat--Dujardin's quartic obstruction family has constant
  period-one and period-two data, so the first informative low-period layer
  is not visible without a scheme-theoretic period-three calculation.
- **So what:** on the entire normalized quartic fiber with formal fixed-point
  trace multiset $0^{\times4}$, the period-three moment is an affine coordinate in
  $L^3$ and hence is the minimal conjugacy separator. In general degree,
  the proof reduces universal recovery to the explicit and still-open
  combinatorial problem $D_m\neq0$.

## Claims--evidence matrix

Here “proved” means proved in the immutable source proof and independently
accepted for proof-only drafting. It never means experimentally or
computationally certified.

| Paper claim | Atomic scope | Proof evidence | Status | Planned location |
|---|---|---|---|---|
| PC1. On the complete normalized quartic fiber with formal fixed-point trace multiset $0^{\times4}$, the family is $p=(x^2-L)^2$; periods one and two are blind, while the exact-period-three second trace moment is $-384(3375+4096L^3)$ and separates normalized conjugacy classes minimally. | C1--C7, C14--C18 | Steps 1--4 and 10--13; Step 12 contains two source-level derivations, and Step 13 separately proves local multiplicity before length subtraction. | **PROVED, proof-only** | §§2--3 and §6; preview in Abstract, §1, and Fig. 1 |
| PC2. For every symbolic $m\geq2$, $S_m(a,\varepsilon)=C_m\varepsilon^{3m}+D_ma^{2m-1}\varepsilon^{2m}$, $C_m=0$ for odd $m$, and $D_m$ has the frozen finite nested-binomial certificate. | C1--C14 | Steps 1--10, with the complete recurrence-to-Laurent-to-binomial-to-transfer chain in Step 9. | **PROVED, proof-only** | §§3--5; Figs. 2--3 |
| Formal period-one and exact-period-two trace multisets are $0^{\times2m}$ and $2^{\times((2m)^2-2m)}$. | C2--C3 | Step 1, including $q^2=0$, the nonzero nilpotent possibility, the $2+q(x)q(y)$ correction, and diagonal subtraction. | **PROVED, scheme-theoretic** | §2; Fig. 1 |
| Normalized conjugacy is classified within this family by $a^{2m-1}$. | C4 | Step 2; both root-of-unity directions and monic-centered normal-form uniqueness. | **PROVED, normalized scope only** | §2 |
| The cyclic quotient is a free rank-$(2m)^3$ complete intersection and its moment equals a global residue. | C5--C7 | Steps 3--4; prior trace/residue theorem specialized to this system. | **PROVED, prior-method specialization** | §3 |
| Only two of the four weighted-support monomials survive. | C8--C11 | Steps 5--7 and Step 10: separated-algebra nilpotence plus all three nonfixed degeneration patterns and the exact diagonal branch. | **PROVED** | §4; Fig. 2 |
| $C_m=0$ for odd $m$. | C12 | Step 8 cyclic reversal. | **PROVED** | §4; Fig. 2 |
| The displayed $(H/A/D)$ expression equals $D_m$ for every $m\geq2$. | C13 | Full Step 9, including (9.14), the transfer-flow bijection, and the separate $j=0$ case. | **PROVED; transparency mandatory** | §5; Fig. 3 |
| The fixed contribution to the moment vanishes, while fixed-support multiplicity remains the full fixed-scheme length inside $\operatorname{Fix}(f^3)$. | C14, C17 | Step 10 for the moment; Step 13 for multiplicity. | **PROVED; obligations must remain separate** | §6 |
| Universal $D_m\neq0$ and hence period-three separation in every degree. | O1 | No degree-independent proof. | **OPEN NONCLAIM** | Abstract limitation, end of §5, Fig. 3, §7 |
| Period three separates all quartic Hénon maps or proves global $P(4)=3$. | X1--X2 | Outside the proved fiber. | **EXCLUDED** | Explicit limitation in §1 and §7 |
| Global residue, quotient-trace, dynatomic, or low-period Hénon methods are new. | X3 | Direct mature prior art. | **EXCLUDED** | §1 positioning and citations |

## Abstract plan (180--220 words)

- Open with the exact scoped result, not field-level background.
- State the normalized category, the quartic $0^{\times4}$ formal fixed-point trace
  fiber, and the known period-one/two obstruction.
- State the source-proved period-three formula and that its nonzero $L^3$
  slope is the first separating low-period moment on this fiber.
- Summarize the mechanism: cyclic complete intersection, trace--residue
  identity, weighted support, local degeneration, and an explicit finite
  coefficient certificate.
- End with the sharp limitation: $D_m\neq0$ for all $m$ is open, so the
  all-$m$ law is not an all-degree separation theorem.
- Include no runtime, audit, experiment, or result-certification language.

## §1 Introduction and prior-work positioning (2.0 pages)

- **Opening:** finite multiplier rigidity motivates asking which low periods
  first distinguish a concrete normalized fiber.
- **Direct precedent:** credit Cantat--Dujardin for the quartic family and its
  period-one/two blindness; identify $L=\lambda^2$ and $L^3=\lambda^6$.
- **Gap:** their general finite-period argument does not state this exact
  period-three moment, the full $0^{\times4}$ fiber classification, or the all-$m$
  coefficient certificate.
- **One-sentence contribution:** reproduce the sentence at the top of this
  plan nearly verbatim.
- **Contributions:** two numbered bullets matching PC1 and PC2, followed by a
  third scope bullet declaring universal nonvanishing open.
- **Method lineage:** Friedland--Milnor for normalized Hénon structure;
  Cattani--Dickenstein--Sturmfels for global-residue and quotient-trace
  machinery; Cvitanović et al. and Dullin--Meiss for prior exact/low-period
  Hénon work; Huguin and Hutz only for adjacent small-cycle/formal-period
  context.
- **Hero figure:** Fig. 1, placed after the contributions. It must show the
  theorem path and the proof-only evidence firewall before technical detail.
- **Front-loading check:** a skim reader sees the exact quartic formula, its
  restricted minimality, the general two-term law, and the open nonvanishing
  boundary on the first two pages.

## §2 Normalized family and formal low-period spectra (2.5 pages)

- Define the algebraically closed characteristic-zero base field, monic-
  centered Jacobian-$(-1)$ category, $p_{m,a}$, $q=p'$, $f_{m,a}$, and
  formal multiplication spectra on finite algebras.
- Prove the period-one spectrum on
  $k[x]/((x^m-a)^2)$; say $q^2=0$, never $q=0$ in general.
- Prove the period-two spectrum on the product algebra, retain the
  $2+q(x)q(y)$ nilpotent correction, and subtract the formal diagonal.
- Prove both directions of normalized conjugacy
  $f_{m,a}\sim f_{m,b}\iff a^{2m-1}=b^{2m-1}$, including the centering
  argument that removes translation.
- Cite Friedland--Milnor for the ambient normal-form framework and
  Cantat--Dujardin for the direct quartic obstruction.

## §3 Period-three cyclic scheme and trace--residue reduction (3.5 pages)

- Introduce the deformed cyclic equations
  $F_i=(x_i^m-a)^2+\varepsilon(x_{i-1}-x_{i+1})$.
- Compute the Jacobian determinant
  $t_\varepsilon=q_0q_1q_2+\varepsilon^2(q_0+q_1+q_2)$ and show that at
  $\varepsilon=1$ it equals $\operatorname{tr}Df^3$.
- Prove that pairwise-coprime leading monomials make the quotient free of
  rank $(2m)^3$, including the no-points-at-infinity statement.
- Specialize the complete-intersection trace--residue theorem to obtain
  $S_m=\operatorname{Tr}(t_\varepsilon^m)=\operatorname{Res}(t_\varepsilon^{m+1})$.
- Credit the residue/quotient-trace method as prior art rather than a new
  formalism.

## §4 Weighted support, vanishing branches, and the two-term law (3.0 pages)

- Use weights $\operatorname{wt}(x_i)=1$,
  $\operatorname{wt}(a)=m$, and
  $\operatorname{wt}(\varepsilon)=2m-1$ to list exactly four allowed
  parameter monomials.
- At $\varepsilon=0$, use the separated tensor algebra and $q_i^2=0$ to
  remove the $a^{3(2m-1)}$ term.
- Present the three nonfixed Puiseux root patterns separately: all distinct,
  exactly two equal, and all equal, with trace-valuation lower bounds
  $3/2$, $7/4$, and $3$. Refer forward to the exact diagonal branch in
  §6/Step 10 rather than folding it into the valuation argument.
- Deduce the two-term law and use cyclic reversal to prove $C_m=0$ for odd
  $m$.
- Place Fig. 2 after the four-support reduction.

## §5 Transparent finite coefficient certificate (7.0 pages)

This section is the paper-size gate and must remain checkable without an
opaque computer-algebra assertion.

1. State recurrence (R), reduction coefficient (9.1), base cases (9.2), and
   all four signed branches (9.3), with total-degree decreases.
2. Prove unique/order-independent reduction via the Laurent coefficient
   (9.4) and reciprocal expansion (9.5); explain why branch interleavings are
   not additional terms.
3. Expand (9.6), define $\mathcal C_{m,j}$ in (9.7), assemble (9.8), and
   give both the recursive certificate (9.9) and the complete admissible-
   tuple sum (9.10)--(9.13).
4. Display and prove the local signed binomial identity (9.14) by extracting
   the coefficient of $z^\alpha$ from
   $(1-z)^N(1-2z+z^2)^{-n-1}$, with generalized binomial coefficients
   defined.
5. Derive (9.17)--(9.19), the unique distinguished coordinate for $j\geq1$,
   the incoming-transfer bijection (9.20), guarded local factors (9.21), and
   orientation sign (9.22).
6. Obtain the $j\geq1$ collapse (9.23)--(9.24), then start a visibly separate
   $j=0$ paragraph covering both flow types (9.25) and the exceptional
   vanishing (9.26).
7. Conclude with the exact $(H/A/D/E)$ formulas (9.27)--(9.28) and immediately
   state that universal $D_m\neq0$ remains open.

Place Fig. 3 near the start as a reader map, not as proof evidence.

## §6 Complete quartic fiber and the minimal separator (3.0 pages)

- Classify the $0^{\times4}$ formal fixed-point trace fiber by root partitions
  $4$ and $2+2$, then centering, to obtain $p=(x^2-L)^2$ uniquely.
- Present the two source-level Step-12 routes:
  the all-$m$ specialization only as a cross-check, and the independent
  tensor--Laurent slope derivation together with the direct normal-form
  constant ledger as the actual quartic coefficient proof.
- State $S_2^{(3)}(L)=-1296000-1572864L^3$.
- Keep Step 10 and Step 13 distinct: first prove zero fixed **moment** from
  $q^2=0$; then prove local fixed-branch **multiplicity** using the
  invertible transverse Jacobian and exact order $r$.
- Only after multiplicity, subtract lengths (64-4=60). Only after pointwise
  exact-period subtraction, divide by three to obtain the cyclewise moment
  $-432000-524288L^3$.
- Combine the nonzero quartic slope with the normalized quotient coordinate
  $L^3$ and known period-one/two blindness to prove scoped minimality.

## §7 Scope, provenance, limitations, and conclusion (0.5 pages)

- Restate the quartic theorem and all-(m) certificate without copying the
  introduction.
- State explicitly that universal $D_m\neq0$, all-degree separation, a
  theorem for all quartic Hénon maps, and global $P(4)=3$ are not proved.
- Include the proof-only provenance substance required by
  `notes/PROOF_ONLY_MANUSCRIPT_SCOPE.md`: theorem authority and source review;
  consumed terminal audit with no rerun/raw result/result pass; and prior-art
  credit plus bounded novelty language.
- The failed audit disclosure should be brief and factual. The static cause
  attribution may be described only as an approximately $0.98$-confidence
  forensic inference because child stderr was not retained. Do not mention
  diagnostic values or suggest scientific agreement.
- End with the concrete open combinatorial question of proving or refuting
  $D_m\neq0$ uniformly.

## Figure plan and exact caption/label contract

All three figures are proof-navigation diagrams derived from theorem text.
None is a runtime, diagnostic, empirical, or computational-result plot. Each
must be supplied as vector PDF, selectable-text SVG, and 300 dpi PNG, with no
title inside the graphic and with claim-bearing distinctions redundant in
text, line style, shape, or hatch.

| ID | Stem and label | Role | Scientific source | Priority |
|---|---|---|---|---|
| Fig. 1 | `fig1_theorem_architecture`, `fig:theorem-architecture` | Hero theorem architecture and proof-only evidence boundary | Proof Steps 1--4, 10--13; proof-only scope and handoff | HIGH |
| Fig. 2 | `fig2_weighted_two_term_law`, `fig:weighted-two-term-law` | Weighted-support reduction and quartic specialization | Proof Steps 5--8 and 12 | HIGH |
| Fig. 3 | `fig3_step9_certificate_pipeline`, `fig:step9-certificate-pipeline` | Transparent Step-9 proof map | Proof Step 9 and handoff §6 | HIGH |

### Figure 1 exact contract

**Required visual content:** three connected theorem layers: formal period
one, formal exact period two, and formal period three; a quartic specialization
showing the $0^{\times4}$ fiber, length $60$, and affine $L^3$ separator; and a
separate dashed evidence firewall. The firewall must route the locked proof
and independent source/handoff reviews to theorem claims while routing the
failed audit only to a provenance/non-evidence box. It must explicitly say
that registered evidence was not used and that finalization is not
authorized.

**Exact caption:**

> Theorem architecture and evidence boundary. The formal period-one and exact-period-two multiplication spectra are constant on the normalized family, with nilpotent corrections retained before passing to spectra. The period-three cyclic complete intersection yields the two-term moment law and, on the complete normalized quartic fiber with formal fixed-point trace multiset $0^4$, the exact pointwise moment $-384(3375+4096L^3)$, formal exact-period-three length $60$, and minimal separation by $L^3$. Every arrow into a theorem box originates in the source-locked proof and independent proof reviews. The consumed registered audit contributes only the dashed provenance branch: it terminally failed, supplies no scientific evidence, and authorizes neither a result claim nor finalization.

### Figure 2 exact contract

**Required visual content:** the weight equation and its four nonnegative
solutions; two visibly crossed/eliminated terms with the exact proof reason;
the surviving two-term law; the odd-$m$ parity specialization; and the
quartic $m=2$ identity. A final open-boundary box must say that
$D_m\neq0$ for all $m$ is open and therefore no all-degree separator is
claimed.

**Exact caption:**

> Weighted support and the two-term law. Weighted homogeneity permits exactly four parameter monomials in $S_m(a,\varepsilon)$. The separated algebra at $\varepsilon=0$ removes $a^{3(2m-1)}$, and the three nonfixed degeneration patterns together with the exact diagonal branch remove $a^{2(2m-1)}\varepsilon^m$. The surviving terms are $C_m\varepsilon^{3m}$ and $D_ma^{2m-1}\varepsilon^{2m}$; cyclic reversal additionally gives $C_m=0$ for odd $m$. For $m=2$, source-level coefficient derivations give $S_2^{(3)}(L)=-1296000-1572864L^3$. The diagram makes no universal separation claim: $D_m\neq0$ for every $m\geq2$ remains open.

### Figure 3 exact contract

**Required visual content:** seven numbered proof stages matching the mandated
Step-9 order: recurrence/base cases; Laurent/order independence;
admissible tuples; local identity (9.14); distinguished coordinate and
incoming-transfer bijection; $j\geq1$ collapse plus separate $j=0$ flow;
and the final $(H/A/D/E)$ certificate. The separate $j=0$ branch must be
visually distinct. The final box must put `OPEN` beside universal
$D_m\neq0$.

**Exact caption:**

> Transparent coefficient-certificate pipeline. The four-branch recurrence and base cases terminate by strict total-degree decrease; the Laurent coefficient makes the reduction order independent and groups branch interleavings without double counting. Admissible tuples retain every sign, multiplicity, Laurent exponent, and parameter degree. The local identity (9.14), proved by one-variable coefficient extraction, collapses each signed fiber. For $j\geq1$, a unique distinguished coordinate and an incoming-transfer bijection give the guarded $H/A$ factors; $j=0$ is handled by a separate exhaustive flow classification, including the vanishing exceptional pattern. Assembly yields the finite formula for $D_m$. Universal $D_m\neq0$ is explicitly open, and no runtime or finite diagnostic is part of this proof.

The exact LaTeX environments are frozen in
`paper/figures/latex_includes.tex`; the manuscript must use those labels and
captions verbatim unless a new asset review is obtained.

## Citation plan

- **§1:** Cantat--Dujardin; Friedland--Milnor;
  Cattani--Dickenstein--Sturmfels; Cvitanović--Hansen--Rolf--Vattay;
  Dullin--Meiss; Huguin.
- **§2:** Friedland--Milnor and Cantat--Dujardin.
- **§3:** Cattani--Dickenstein--Sturmfels; optional Ueda for fixed-point
  background.
- **§4:** no citation needed for the paper-specific proof; cite residue
  prior art only when the method is invoked.
- **§5:** Cattani--Dickenstein--Sturmfels for method lineage, never for the
  paper-specific (H/A/D) formula.
- **§6:** Cantat--Dujardin for the direct family and lower-period
  obstruction; Hutz (2010) only if formal-period/dynatomic terminology is
  discussed.
- **Optional context only:** Hutz (2020), Guillot--Ramírez, Ueda, and
  Bianchi--He. Their roles must remain adjacent/background rather than direct
  support for PC1 or PC2.

Bibliographic metadata is frozen in `paper/references.bib`. The primary-
source role ledger remains `notes/CITATION_VERIFICATION.md` at its locked
input hash; the publication package must not strengthen its bounded no-hit
statement into a priority claim.

## Cross-review and minimum-fix audit

The paper-plan skill's external GPT-5.4 reviewer endpoint was not available in
this environment, so no independent reviewer output is fabricated. A
contract-level self-audit produced the following minimum fixes, already
incorporated:

1. Lead with PC1 rather than the more general PC2, because the quartic theorem
   is the sharp closed result.
2. Give Step 9 a full section and a reader-map figure; compressing it to a
   computer-algebra statement would violate the scope and collapse the
   recorded standalone-size gate.
3. Separate Step 10 zero moment from Step 13 local multiplicity before any
   length subtraction or cycle division.
4. Put the universal-nonvanishing open boundary in the abstract, Figure 2,
   Figure 3, §5, and the conclusion.
5. Keep the registered-audit history outside every theorem arrow and mention
   it only in a short provenance paragraph.
6. Use a specialist-journal page budget rather than forcing this proof-heavy
   note into an ML-conference template.

A fresh independent plan/figure review and exact `ASSET_PASS` remain required
before manuscript integration or finalization.

## Freeze checklist

- [x] One coherent theorem-first story; PC1 is the lead and PC2 the mechanism.
- [x] Every theorem claim maps to the source proof, not to a computation.
- [x] Step 9 transparency chain is allocated in full.
- [x] Step 10 moment and Step 13 multiplicity are distinct.
- [x] Three independent figures have exact caption/label contracts.
- [x] Universal nonvanishing and global-quartic overclaims are excluded.
- [x] Primary-source roles are bounded and citation metadata is verified.
- [x] Failed-audit provenance is non-evidence only.
- [ ] Fresh independent asset review returns `ASSET_PASS`.
- [ ] Manuscript drafting uses the frozen assets without editing
  `paper/manuscript.tex` in this asset-authoring stage.
