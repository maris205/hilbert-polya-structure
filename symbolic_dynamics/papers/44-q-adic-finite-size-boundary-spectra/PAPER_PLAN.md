# Paper 44 writer plan

## Working title and manuscript role

**q-adic Finite-Size Boundary Spectra of Multiplicative Shifts of Finite
Type: Exact General Remainders and Golden Cantor Boundaries**

**One-sentence contribution.**  For every primitive finite zero--one
adjacency matrix and every integer radix $q\ge 2$, the exact order-one
prefix remainder of the associated multiplicative shift extends to a
continuous real-valued map on $\mathbb Z_q$ whose image is the complete
accumulation set; in the binary golden control, the same coefficients give a
strongly separated Cantor image of dimension
$\log 2/(2\log\varphi)$ and a unit-circle natural boundary for the ordinary
cutoff generating function.

This is a standalone theory-and-verification manuscript with an explicit
source-ownership firewall.  It is not a priority claim.  The multiplicative
shift, chain product, Fibonacci word counts, leading entropy, leading
Hausdorff/Minkowski dimensions, boundary-complexity terminology, and every
valid prior leading or boundary result receive zero candidate credit.

- **Format:** anonymous 11pt A4 mathematical preprint.
- **Final layout:** six main sections through the conclusion on page 9;
  Appendices A--C and the references complete a 16-page manuscript.
- **Scientific sections:** six, followed by three appendices.
- **Date:** 2026-08-18 UTC.

## Claims--evidence matrix

| ID | Claim | Evidence and owner | Status | Main location |
|---|---|---|---|---|
| C1 | The exact increment is $c_{\nu_q(N)}$, the centered remainder has the residue-series identity, and its complete accumulation set is $E_{A,q}(\mathbb Z_q)$. | Exact chain partition, valuation census, Perron gap, uniform convergence, compactness, and the explicit representatives $N_j=(x\bmod q^j)+q^j$; proof owner `preauthority/PROOF_PACKAGE.md`. | Proved under primitive $A$. | Section 3; Appendix A.1--A.3 |
| C2 | In the binary golden control, the digit coefficients alternate, dominate their full tails, and yield a Cantor image with Hausdorff and box dimension $\log2/(2\log\varphi)$. | Binet expansion, the exact $\mathbb Q(\sqrt5)$ certificate $6557^2-5\cdot2929^2=99044>0$, cylinder separation, and Bernoulli mass distribution; proof owner `PROOF_PACKAGE.md`. | Proved for the frozen golden control only. | Section 4; Appendix A.4--A.5 |
| C3 | The ordinary cutoff generating function has a nonzero radial leading coefficient at every primitive dyadic root and hence the unit circle is a natural boundary. | Rational residue generating functions, dominated Abelian passage, the exact coefficient $-\gamma_{v-1}/(2^{v-1}(1-\xi))$, density of primitive dyadic roots, and the analytic-continuation contradiction on every boundary arc; proof owner `PROOF_PACKAGE.md`. | Proved for the frozen golden control only. | Section 5; Appendix A.6 |
| C4 | Two physically distinct evaluators reproduce the finite exact and certified-interval projections and all designated adversarial mutations are rejected. | Canonical authority report, exact comparison, result ledger, proof/source/type/independence/Route/integrity audits. | Retrospective verification; never promoted to proof of C1--C3. | Appendix B; artifact bindings in Appendix C.3 |
| C5 | The paper preserves the exact ownership boundary and reconciles a contradicted one-dimensional displayed formula in the Ban--Hu--Lai author manuscript with the bounded exact remainder. | Full-shift control $A=J_d$, local exact identity, frozen source audit, and explicit version-of-record caveat. | Correction/reconciliation, zero novelty credit; version of record and errata not represented as line-checked. | Section 2.1; source reconciliation in Appendix C.2 |

## Known weaknesses and mandatory scope boundaries

1. The bounded literature search has evidence grade at most `B-`; absence of
   an exact hit is not evidence of priority.  `STOP_DUPLICATE` remains a live
   external publication condition.
2. Primitivity is essential to the supplied Perron-decay proof.  Reducible,
   irreducible-periodic, countable-state, and higher-step variants are not
   inferred.
3. Cantor geometry and natural-boundary conclusions are proved only for
   $q=2$ and the golden adjacency.
4. The dimension concerns the real image $E_{A,2}(\mathbb Z_2)$, not the
   original multiplicative shift.  Ordinary continuous-scale Minkowski
   content is not claimed.
5. $G(z)=\sum_{N\ge0}E(N)z^N$ marks prefix cutoffs.  It is not an
   Artin--Mazur zeta function, a transfer trace, or a Fredholm determinant;
   the dense singularities are not isolated meromorphic poles.
6. Finite exact replay and certified intervals test implementations.  The
   infinite theorems remain owned by the proof replay.
7. Candidate selection and all post-output rendering are retrospective and
   supply no prospective, blinded, outcome-independent, ranking,
   authorization, novelty, or priority evidence.

## Section architecture and final page map

### Abstract and 1. Introduction (page 1)

- Start with the exact finite-size theorem, not generic symbolic-dynamics
  background.
- Name the primitive hypothesis, real-valued $q$-adic completion, complete
  accumulation image, golden dimension, and natural boundary.
- Give the strongest exact quantitative value
  $\log2/(2\log\varphi)$.  Do not mention finite replay in the abstract.
- State the ownership subtraction in one sentence and include no citations.

- Hook: leading entropy suppresses the bounded arithmetic structure left by
  integer cutoffs.
- Define the question and surface the one-sentence contribution before the
  first figure.
- Separate three theorem contributions C1--C3 from a plainly labeled
  implementation-audit paragraph C4.  State there that finite replay bears
  no evidentiary weight for the infinite theorems.  Frame C5 as source
  reconciliation rather than scientific novelty.
- End the introduction with a one-line notation preview defining
  $\mathbb Z_q=\varprojlim_n\mathbb Z/q^n\mathbb Z$, $Z(N)$ as the prefix
  count, and $E(N)=\log Z(N)-hN$, so Section 2 never uses unexplained symbols.
- Insert Figure 1, which compares the exact integer chain update with the
  inverse-limit boundary map.
- End with the scope firewall and roadmap.

### 2. Prior ownership and a same-object correction (begins page 2)

- Organize by ownership family: multiplicative shifts and leading dimension;
  pattern products and entropy; digital-summatory neighbors; boundary
  complexity and affine extensions.
- Include a comparison table assigning zero credit to the source, chain
  product, entropy, leading dimensions, and prior boundary terminology.
- Identify the checked artifact exactly as arXiv:2210.09115v1, submitted
  2022-10-17.  Reproduce its $d=1$, $N=p^{kn}$ displayed specialization
  accurately, test it against $A=J_d$, and reconcile it with the exact
  bounded remainder.
- Include a compact notation dictionary mapping the manuscript's
  $X_{\Sigma_A}^{p}$, $|\mathcal P([1,p^{kn}],X_{\Sigma_A}^{p})|$,
  $\lambda_A$, and $h$ to the present $X_A^{(q)}$, $Z(N)$, $\rho(A)$, and
  $h$, with $p=q$ and $N=p^{kn}$.
- Use this exact caveat in the main text: “We checked only the author
  manuscript arXiv:2210.09115v1, submitted 17 October 2022.  We did not
  line-check the version of record or any erratum, and make no claim about
  their displayed formulas.”  Do not transfer the author-manuscript formula
  to the journal version.

### 3. Exact finite-$N$ calculus and the $q$-adic boundary (begins page 4)

- Define $X_A^{(q)}$, $W_\ell$, $Z(N)$, $c_v$, $d_v$, $h$, and
  $E(N)$ with types and conventions.
- Prove the chain product and one-site increment.
- Derive the exact valuation census and residue identity.
- State Theorem A and give the full main-text proof skeleton: Perron summable
  majorant, uniform convergence, compactness inclusion, and explicit reverse
  representatives.
- Define $\mathbb Z_q:=\varprojlim_n\mathbb Z/q^n\mathbb Z$ explicitly.
  Distinguish a real-valued function on this inverse limit from a $q$-adic
  numerical series; $q$ need not be prime.

### 4. Golden boundary geometry (begins page 5)

- Derive $W_\ell=F_{\ell+2}$, $r=-\varphi^{-2}$, and both exact formulas
  for $\gamma_k$.
- State and prove the all-level tail domination using the exact algebraic
  certificate, not finite samples.
- Use Figure 2 to show digit cylinders, sibling gaps, and geometric scale.
- Prove Cantor topology and exact Hausdorff/box dimension with upper covers
  and a Bernoulli measure lower bound.

### 5. Dense radial singularities (begins page 7)

- Define the ordinary cutoff generating function and residue rational
  functions.
- Derive the exact radial leading coefficient at primitive dyadic roots,
  including
  the $Q=4,\xi=i$ normalization control.
- Explain why dense radial divergence implies a natural boundary but not a
  collection of isolated meromorphic poles.
- Use Figure 3 to make the ordinary-marker/type firewall visually explicit.

### 6. Scope and conclusion (begins page 9)

- State the scientific limits and type firewall in the main narrative.
- Conclude with what the exact finite-size boundary theorem adds after all
  prior ownership is removed.
- Point to Appendix C.5 for the release-specific Route outcome and
  retrospective chronology; do not put that process record back into the
  theorem-first conclusion.

### Appendix A. Proof details (begins page 9; continues through page 12)

- Full proofs of Perron decay, exact summation by parts, both accumulation
  inclusions, golden mode expansion, strong separation, dimension, dominated
  radial passage, and the natural-boundary contradiction.

### Appendix B. Exact computational replay (begins page 13)

- Describe the physically distinct source-graph and chain/Binet/cyclotomic
  evaluators without presenting one as proof of the other.
- Insert one compact canonical post-output block, mechanically traceable to stored
  authority files, containing exactly the relevant counts, hashes, Route
  tuple, verdict, Route-B lock, and evidence boundary.
- Report 580 finite cases (548 theorem-domain, 32 scope rejections), 33
  overlapping interval pairs, the exact `99044` control, 19 mutation
  families/20 instances/52 designated invocations/0 survivors, eight frozen
  external-auditor mutations/0 survivors, and both Route checks `6/6`.
- Preserve `FINITE_RESULTS_DO_NOT_PROVE_INFINITE_THEOREMS` in prose.  Keep one
  table and one interpretive paragraph here; the artifact hash map and
  chronology belong to Appendix C.

### Appendix C. Types, source reconciliation, and reproducibility (begins page 14; references begin page 16)

- Object/marker/type table and prohibited identifications.
- Exact authority artifact/hash map for the canonical experimental block.
- Retrospective chronology, source-search ceiling, and protected-input
  statement.
- Reproduction commands are read-only and never run in the authority tree.

## Figure and table plan

| ID | Type | Content | Data source | Purpose |
|---|---|---|---|---|
| Figure 1 | Pure TikZ hero diagram | Exact $q$-adic chains at cutoff $N$, the unique chain extension at $N+1$, the valuation increment, and the continuous map $\mathbb Z_q\to\mathbb R$ whose image is the accumulation set.  Caption says in plain language: one cutoff step changes exactly one valuation level, and the levelwise changes assemble into the continuous boundary map. | Frozen definitions and Theorem A; no generated data. | A skim reader sees the finite-to-boundary mechanism before technical details. |
| Figure 2 | Pure TikZ cylinder tree | Alternating golden coefficients, two separated children at each level, tail-sized cylinders, and scale/cardinality labels $t^n,2^n$. | Theorem B and the exact tail certificate. | Visualizes why all-level separation yields the dimension. |
| Figure 3 | Pure TikZ analytic/type diagram | Residue series $\to R_{2^v}(z)\to$ primitive dyadic radial coefficients $\to$ dense natural boundary, with crossed-out zeta/determinant retyping. | Theorem C and type contract. | Separates the proved analytic statement from forbidden operator language. |
| Table 1 | Ownership comparison | Prior-owned components versus eligible exact subleading components. | Frozen literature audit. | Makes zero-credit subtraction auditable. |
| Table 2 | Canonical replay block | Exact stored counts, statuses, and hashes. | `outputs/reports/EXPERIMENT_REPORT.md`, `outputs/results/exact_comparison.json`, `outputs/RESULT_LEDGER.json`, Route/audit files. | Ensures no experimental number is invented. |

All figures are vector TikZ source.  There are no raster assets, generated
plots, hard-coded empirical curves, external screenshots, or decorative
images.

## Citation plan and verification boundary

| Key | Placement | Role |
|---|---|---|
| `fan2012level` | Sections 1--2 | Multiplicative golden-mean setting and leading counts/dimension; zero credit. |
| `kenyon2012hausdorff` | Sections 1--2 | General multiplicative-integer invariant fractal framework; zero credit. |
| `madritsch2012summatory` | Section 2 | Digital-summatory method neighbor, not an exact collision. |
| `ban2019pattern` | Sections 1--3 | Direct admissible-chain products, entropy, and leading error control; zero credit. |
| `ban2023boundary` | Section 2 | Boundary-complexity ownership; the checked correction target is separately identified as arXiv:2210.09115v1, submitted 2022-10-17, with no claim about unverified version-of-record/erratum formulas. |
| `ban2025affine` | Section 2 | Broader recent affine multiplicative-shift dimension ownership. |

Every record is checked against the DOI metadata and the frozen source audit.
The bibliography contains only cited entries.  Online-first metadata are not
used to silently replace the print year bound by the source audit.

## Plan review

A read-only GPT-5.4 xhigh review returned `PLAN_NOT_READY` with no
Critical, six Major, and five Minor findings.  Its scores were logical flow
8/10, claim/evidence alignment 7/10, missing-evidence handling 6/10, source
positioning 7/10, page feasibility 6/10, and skim-facing strength 6/10.
The plan now implements every finding:

1. finite replay is removed from the abstract and separated from the theorem
   contributions in the introduction;
2. C3 uses “nonzero radial leading coefficient” and names the continuation
   contradiction;
3. the checked Ban--Hu--Lai artifact has an exact version/date, an explicit
   no-transfer caveat, and a notation dictionary;
4. detailed mutations, hashes, and chronology move to Appendices B--C;
5. the title exposes the general/golden scope asymmetry;
6. the introduction previews notation, $\mathbb Z_q$ is defined as an inverse
   limit, and Figure 1 receives a plain-language caption requirement.

No review statement supplies blind, prospective, novelty, priority, or
authorization credit.  A second read-only xhigh repair recheck found no
remaining Critical, Major, or Minor issue on the seven blocking topics and
returned `PLAN_READY`.  Drafting proceeds only under these repaired
constraints.

## Writer invariants

- The authority directory remains byte- and metadata-identical to
  `PROTECTED62_SNAPSHOT.tsv`; the snapshot contains exactly 62 protected
  regular files.
- The canonical result block has one main-text occurrence and is copied only
  from already stored outputs.
- No provisional commit sentinel is introduced.  The current P44 State-A
  authority uses `PREAUTHORITY_NO_COMMIT`/`NONE`, and the manuscript preserves
  those exact values without adding a different placeholder.
- The final writer manifest is C-sorted, unique, self-excluding, and binds
  source, figures, proof appendices, plan, handoff, improvement record,
  compilation report, and the candidate PDF as explicitly classified.
- Two independent clean builds use a fixed `SOURCE_DATE_EPOCH` and must
  produce byte-identical PDFs before the candidate is sealed.
