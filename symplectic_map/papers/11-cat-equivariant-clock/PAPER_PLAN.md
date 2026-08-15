# Paper Plan

## Frozen identity and release boundary

**Working title:** *An Equivariant-Zeta Audit of Cat-Map Centralizer
Quotients*.

**Article type:** short theory-and-exact-audit boundary note.

**One-sentence contribution:** on the regular cat-map centralizer torsor,
standard equivariant constructions form a definition-sensitive
retention--compression hierarchy---point-order Burnside data retain source
order, orbit-order and Morita quotient data are static, and labelled
permutation/enhanced carriers retain the translating element only inside a
modulus-dependent effective action---so none of the audited outputs supplies
an intrinsic modulus or prime clock.

**Required terminal classification:**
`EQUIVARIANT_RETENTION_COMPRESSION_TRADEOFF_CERTIFIED /
A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.

**Novelty calibration:** **2/10**. The 2008 rational point-order Burnside
series, 2013 labelled $G$-permutation invariant, 2015 integral orbit-order
series and orbifold reductions, and 2018 enhanced carrier are direct prior
art. The defensible delta is only their proof-complete specialization to the
already frozen Paper-10 regular centralizer torsor, together with an exact
retention ledger, action-kernel boundary, composite controls, and one
structural counterexample. The paper must not claim a new equivariant,
Burnside, orbifold, enhanced, stacky, or group-action zeta.

> **Asset gate:** source, implementation, registered result, independent
> result review, separate post-run analyzer review, and the dual-tree result
> manifest are closed. This plan authorizes only publication planning,
> citation assets, and exactly three deterministic figures. It does not
> authorize a candidate or analyzer rerun, a tenth modulus, a new group or
> matrix search, a numerical value of $s$, a numerical logarithm, a numerical
> value of $q^{-s}$, or Route B.

### Frozen evidence bindings

| Role | Path | SHA-256 / state |
|---|---|---|
| Paper-11 source lock v2 | `experiments/source_lock.json` | `331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b` |
| independent source rereview | `notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md` | `2f75d6934e3d61bdc941ee6689102a1cb08a959270a7cd87965579f1ec5cc622` (`SOURCE_LOCK_PASS`) |
| proof package | `notes/PROOF_PACKAGE.md` | `3d723fdb02c89f9b2f281da807bcd745c5991393d25e223f95d6673961c20948` |
| claims--evidence matrix | `notes/CLAIMS_EVIDENCE_MATRIX.md` | `0ea191ebb1f6f0f915db096a68606099d4a315d80d333adadd3e396b11885490` |
| novelty assessment | `notes/NOVELTY_ASSESSMENT.md` | `1dbd6e4dc07fbc1e126334f6484a71b77852f0583749ba64259bd0e603669c95` |
| raw registered result | `results/EXPERIMENT_RESULTS.json` | `bef8aa5d632ed11b1ca58a123bbfe967a5426e2049d862118a373e4c1dc005fe` |
| independent result review | `results/INDEPENDENT_RESULT_INTEGRITY.md` | `c91737c8bf860bd559eebebe08420fc5d095800c47d132381f584e918e714a20` (`RESULT_PASS`) |
| separate analyzer review | `results/POSTRUN_ANALYZER_REVIEW.md` | `ba63afc8c88903f15ec6ac5d82f0cd65430710ca9c132b489a7cd4f70e7660a8` (`ANALYZER_PASS`) |
| dual-tree strict manifest | `results/result_manifest.json` | `a0b409061c34eff0d68fdc326fe4ec6ff9295895444b857ee161fd77e417292c` (`PASS`) |
| independent postrun scope audit | `notes/INDEPENDENT_POSTRUN_SCOPE_AUDIT.md` | `f7b365c9e6c8933cf3cbcaf3c96692cbacdaabcc84400bdc629f1d482cb243e4` (`PASS_WITH_SCOPE_CORRECTION`) |
| official result report | `experiments/OFFICIAL_EXPERIMENT_RESULTS.md` | `06f547fdfbbfb3bd51a57041758a49f18acceca9dda8e19967c2364500d64918` |
| official validation report | `experiments/OFFICIAL_VALIDATION_REPORT.md` | `754a36c0e2e6b5c5002ecb8b3473d0af0e077b4f5b88da2bc6851bdafad23221` |
| upstream Paper-10 terminal integrity | `../10-cat-centralizer-quotient/paper/FINAL_INTEGRITY.md` | `e0a4803ff8e2063ebf5766803212579b44cd80c15572b166c1389f0242f8e6ce` (`COMPLETE_LOCAL_FINAL_REVIEW_PASS`) |
| upstream Paper-10 terminal PDF | `../10-cat-centralizer-quotient/paper/paper_final.pdf` | `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378` |

A changed bound input invalidates the plan/figure package. Figure scripts
strictly hash these read-only files before loading display data. They do not
import the candidate or analyzer packages.

## Scope, terminology, and nonclaims

### In scope

1. For a finite abelian group $C$, $a\in C$, and
   $X=\coprod_K n_K(C/K)$, derive the exact source periods
   $d_K=[\langle a\rangle:\langle a\rangle\cap K]$, cycle counts
   $[C:K\langle a\rangle]$, and the identity dynamics on $X/C$.
2. Keep the 2008 fixed-point/point-order rational Burnside series and the
   2015 fixed-$C$-orbit/orbit-order integral Burnside series separate.
3. Apply cardinality and the additive exact-period orbifold map only to the
   exponent classes; explicitly avoid a false ring-homomorphism claim.
4. Compute the $(\mathbb Z\times C)$ stabilizer
   $\langle\{0\}\times K,(1,a^{-1})\rangle$ and show that all represented
   types recover $a$ exactly modulo the action kernel
   $N=\bigcap_{n_K>0}K$.
5. Separate labelled-carrier retention from quotient-stack and inertia
   compression. Translation by $a$ is $2$-isomorphic to identity on
   $[X/C]\simeq\coprod_Kn_KBK$, whose inertia multiplicity is static.
6. Specialize to the Paper-10 regular torsor $X_q\simeq G_q$, with
   $n_q=|G_q|$, $r_q=\operatorname{ord}_{G_q}(a_q)$, and
   $m_q=n_q/r_q$.
7. Report the one registered nine-row audit in the frozen order
   $(2,3,5,7,11,4,6,9,10)$ as implementation/falsification evidence, not as
   proof of the all-$q$ theorem.
8. Use $r_2=r_4=3$, $r_6=r_9=12$, and the four composite controls to show
   that retained order is neither a modulus identifier nor a prime selector.
9. Use the separately typed effective action
   $C_6/C_2\sqcup C_6/C_3$ to show that exact labelled twist recovery does
   not imply a period-six source factor.
10. Record the unique locked scalar exception at $q=2$: because $m_2=1$,
    point-cardinality reduction is $(1-t^{r_2})^{-1}=(1-t^3)^{-1}$.
    This local coincidence does not define a family-uniform construction and
    does not identify the modulus, since $r_2=r_4=3$.

### Exact naming firewall

- **point-order rational Burnside zeta:** the 2008 fixed-point construction;
- **orbit-order integral Burnside zeta:** the distinct 2015 fixed-orbit
  construction;
- **labelled $G$-permutation invariant:** the 2013 finite
  $(\mathbb Z\times G)$-set construction;
- **enhanced carrier / enhanced orbifold zeta:** the 2018 constructions;
- **orbifold reduction:** an additive exact-period exponent reduction, not a
  homomorphism for Cartesian Burnside multiplication;
- **inertia sectors:** static isotropy data, not return times.

The phrase “the equivariant zeta” is forbidden because it conflates distinct
objects.

### Explicit nonclaims

- No new equivariant, Burnside, orbifold, enhanced, stacky, or group-action
  zeta and no historical-priority claim.
- No universal theorem about every equivariant, weighted,
  representation-valued, analytic, Ruelle, or Fried refinement.
- No canonical comparison of the varying groups $G_q$, Burnside rings, or
  enhanced coefficient categories.
- No extension of Miles' acting-group zeta or Walton's finite-field quotient
  theorem to composite residue rings.
- No intrinsic Euler factor, modulus clock, prime selector, prime/zero
  correspondence, Riemann hypothesis, transfer/Fredholm, Hecke, quantum, or
  Route-B claim.
- No candidate rerun, data fitting, statistical inference, new scan, or
  numerical evaluation of $s$, $\log q$, or $q^{-s}$.

Safe verbs are **audit**, **specialize**, **separate**, **derive**, **record**,
and **certify within the frozen scope**. Avoid **first**, **discover**, **new
zeta**, **canonical**, and **prove all refinements fail**.

## Claims--evidence matrix

| ID | Manuscript claim | Theorem authority | Exact-audit evidence | Direct literature boundary | Status |
|---|---|---|---|---|---|
| C1 | A $C/K$ component has period $d_K=[H:H\cap K]$, $[C:HK]$ source cycles, and one quotient fixed point. | `PROOF_PACKAGE`, Step 0. | Exhaustive cyclic-$C_n$ regression and structural control reconstruction recorded in the result review. | Zegowitz 2017 supplies the established shortening/gluing boundary. | `ELEMENTARY_SPECIALIZATION` |
| C2 | Point-order and orbit-order Burnside series are different: $P_m^C=\sum_{d_K=m}n_K[C/K]$, while $\widetilde P_1^C=[X]$. | Proof and exact-period inversion. | Separate raw-result namespaces and dual engines. | Gusein-Zade--Luengo--Melle-Hern\'andez 2008 and 2015 are direct prior art. | `PROVED_PRIOR_DEFINITIONS` |
| C3 | Additive orbifold reductions are $\prod_K(1-t^{d_K})^{-n_K|K|/d_K}$ and $(1-t)^{-\sum_Kn_K|K|}$; no Burnside multiplicativity is used. | Corrected v2 proof and nonmultiplicativity witness. | Exact rational exponent records. | Gusein-Zade et al. 2015. | `PROVED_REPAIR_CLOSED` |
| C4 | The labelled $(\mathbb Z\times C)$ carrier recovers $a$ modulo $N=\bigcap K$, and exactly iff the $C$-action is effective. | Stabilizer calculation. | Full twisted tables and action-kernel checks. | Gusein-Zade 2013 is the direct construction. | `PROVED_CONDITIONAL_RETENTION` |
| C5 | $[X/C]\simeq\coprod_Kn_KBK$ has static inertia; translation by $a$ is $2$-isomorphic to identity. | Action-groupoid proof. | Exact groupoid/naturality records. | Enhanced and orbifold fixed-sector constructions are prior in Ebeling--Gusein-Zade 2018 and Gusein-Zade et al. 2015. | `PROVED_MORITA_BOUNDARY` |
| C6 | On the regular torsor, the four scalar outputs are $(1-t^{r_q})^{-m_q}$, $(1-t^{r_q})^{-1/r_q}$, $(1-t)^{-n_q}$, and $(1-t)^{-1}$; the first has the accidental unit exponent $m_2=1$ at the locked row $q=2$. | Regular-torsor specialization plus the postrun scope audit. | Exact nine-row dual-engine values, including the unique locked pair $(q,j)=(2,\kappa\mathrm{pt})$ with source support and unit exponent. | 2008/2015 constructions are direct prior art. | `PROVED_FAMILY_TRADEOFF_WITH_Q2_EXCEPTION` |
| C7 | The 2013 triple $(1,1,a_q^{-1})$ and enhanced tuple $(1,1,a_q,1)$ retain the local labelled twist, but in a coefficient category varying with $q$. | Twisted stabilizer and enhanced-carrier proof. | Unique fixer $g=a_q^{-k}$ and exact recovery in every row. | Gusein-Zade 2013; Ebeling--Gusein-Zade 2018. | `POSITIVE_BOUNDARY_WITH_COST` |
| C8 | The nine-row ledger has the exact frozen $(n_q,r_q,m_q)$ values and collisions $r_2=r_4$, $r_6=r_9$. | Paper-10 theorem plus frozen proof. | Registered result, independent reconstruction, strict dual-tree manifest. | No novelty inference from the finite rows. | `FINITE_CONTROL_ONLY` |
| C9 | The effective $C_6/C_2\sqcup C_6/C_3$ action recovers the labelled twist but has only period-two and period-three source factors; its five inertia sectors are static. | General theorem plus direct calculation. | Separately typed structural control, two engines. | Diagnostic example, not a new invariant. | `STRUCTURAL_COUNTEREXAMPLE` |
| C10 | No one scalar-reduction type supplies source support and unit exponent uniformly across the locked family; the $q=2$ exception is not modulus-specific because $r_2=r_4=3$. Hence the audited outputs supply no common intrinsic modulus/prime clock, and Route B remains unopened. | C6--C9, the independent postrun scope audit, and the varying-category boundary. | K011's implemented family-level predicate, K009 collisions, K001--K012 pass, and zero externality counters. | Scoped family-level conclusion only; no forbidden per-row nonattainment claim. | `A0_FAIL_COMPONENT_SCOPE_CORRECTED` |

## Reader, structure, and page budget

The intended reader works in arithmetic dynamics, equivariant topology, or
finite-group dynamics and may know only one of the several objects called an
equivariant zeta. Use a theory-first, definition-separated diagnostic
structure. Target **9--11 main-text pages**, excluding references and
appendices, plus **3--5 appendix pages**. The exact venue is not fixed; the
plan therefore uses conservative journal-style exposition rather than an
ML-venue claim template.

### Abstract (160--190 words)

- Lead with the Paper-10 regular centralizer torsor and the question of
  whether equivariant or stacky refinement restores the erased clock.
- State the three retention levels: static quotient/orbit data, source-order
  Burnside data, and labelled twist carriers.
- State the exact regular-torsor four-output ledger, the unique locked
  $q=2,m_2=1$ scalar exception, and the action-kernel condition. Phrase the
  negative result family-uniformly, never as a per-row no-exception claim.
- Preview the two order collisions and effective $C_6$ counterexample.
- End with the scoped A0 failure and Route-B boundary. Do not include a
  novelty boast or a numerical analytic parameter.

### 1. Introduction: one word, several inequivalent invariants (1.2 pages)

Frame the open boundary left by Paper 10: the coarse centralizer quotient
has one fixed class, but perhaps a standard equivariant refinement retains
the clock. Front-load the answer: some refinements retain source order or a
labelled twist, while the compressed outputs remain static; retained data
do not identify the modulus. Cite the 2008, 2013, and 2015 constructions at
the first claim, not in a delayed literature dump. State three contributions:
(i) definition separation, (ii) the regular-torsor retention ledger, and
(iii) the action-kernel/collision controls. Figure 1 is the hero figure.

### 2. Six carriers and their exact definitions (1.6 pages)

Define ordinary source and coarse quotient zetas, point-order and orbit-order
Burnside exact classes, additive exponent reductions, the labelled
$(\mathbb Z\times C)$ carrier, enhanced carrier, and quotient-stack inertia.
Give the inverse Artin--Mazur sign convention. Display the regular-orbit
nonmultiplicativity witness
$\mathbf u^2=|C|\mathbf u$ but
$\Phi(\mathbf u^2)\ne\Phi(\mathbf u)^2$. Cite the exact construction at each
definition: 2008, 2013, 2015, and 2018. Figure 1 supports this section.

### 3. General finite abelian $C$-set theorem (1.7 pages)

For $X=\coprod_Kn_K(C/K)$ and $H=\langle a\rangle$, derive $d_K$,
$[C:HK]$, the source and quotient products, both Burnside exact-class
sequences, and both additive orbifold reductions. Compute
$\widehat K_a=\langle\{0\}\times K,(1,a^{-1})\rangle$ and prove recovery
modulo the action kernel. Identify the quotient stack and its static inertia.
Place the elementary proof sketches in the main text; move full divisor
inversion and groupoid naturality details to Appendix A.

### 4. The regular cat-map centralizer torsor (1.5 pages)

Import, without reproving or rerunning, the Paper-10 terminal theorem
$X_q=\mathrm{CV}_q\simeq G_q$ and the left translation
$\phi_q=L_{a_q}$. Define $n_q,r_q,m_q$ and
$\mathbf u_q=[G_q/1]$. Derive the point-order and orbit-order Burnside
factors, their four scalar reductions, the labelled triple, enhanced tuple,
identity-only fixed sector, terminal action groupoid, and shortening/gluing
counts. State explicitly that point-cardinality has support $r_2=3$ and unit
exponent at $q=2$ because $m_2=1$, but this coincidence is neither uniform
in $q$ nor modulus-identifying. Emphasize that $B(G_q)$ and stronger
coefficient categories vary with $q$.

### 5. Exact nine-row retention ledger (1.5 pages)

Present the frozen tuple $(2,3,5,7,11,4,6,9,10)$ and exact
$(n_q,r_q,m_q)$ rows. Explain the one registered audit, separate theorem and
enumeration engines, independent object-level reconstruction, post-run
analyzer separation, and strict manifest. Surface the collisions
$r_2=r_4=3$ and $r_6=r_9=12$. Treat finite rows as fixed
implementation/falsification controls. Figure 2 is the primary evidence
display; a compact textual ledger may be included in the manuscript, but no
fourth figure asset is authorized.

### 6. Effectivity, inertia, and a counterexample to clock recovery (1.3 pages)

Compare three cases: a regular effective orbit; a trivial one-point action
with quotient stack $BC_q$ and $q$ static inertia sectors; and the effective
$C_6/C_2\sqcup C_6/C_3$ action. Show that the last case recovers the labelled
generator but has source factors only at periods two and three. Figure 3
makes the action kernel, labelled-twist condition, and static inertia
boundary explicit.

### 7. Related work, limitations, and Route-A disposition (1.1 pages)

Organize by construction family rather than paper-by-paper: Burnside
fixed-point/fixed-orbit zetas; labelled/enhanced carriers; quotient
shortening, twists, and group-action zetas; analytic equivariant Ruelle/Fried
boundaries. State that the paper does not compare all possible refinements,
does not identify coefficient rings across $q$, and does not create an
intrinsic Euler factor. Close A0 only within the named definitions and leave
Route B unopened.

### 8. Conclusion (0.5 pages)

Restate the retention--compression tradeoff without repeating the abstract.
Separate the positive result (labelled effective twist recovery) from the
negative result (no common modulus/prime clock). State the low-novelty scope
and the exact terminal classification in prose.

### Appendices (3--5 pages)

- **Appendix A:** complete finite-$C$-set and divisor-inversion proofs.
- **Appendix B:** twisted stabilizers, action kernels, enhanced carrier, and
  groupoid naturality.
- **Appendix C:** exact nine-row schema, result hashes, and one-shot lifecycle.
- **Appendix D:** structural $C_6$ calculation and bibliographic verification
  note.

## Figure plan: exactly three deterministic publication figures

Every figure is generated from a strict hash-checking read-only contract by
its own script, then emitted as vector PDF, selectable-text/vector SVG, and
300 dpi PNG. All claim-bearing distinctions use text, geometry, line style,
or hatch in addition to color. No title is placed inside a figure.

### Figure 1: Information-retention hierarchy

**Filename/label:** `fig1_retention_hierarchy.pdf`,
`fig:retention-hierarchy`.

**Message:** objects commonly called “equivariant zeta” retain different
information; compression and retention do not coincide.

**Layout:** (A) a left-to-right carrier hierarchy from source/coarse quotient
through orbit-order Burnside, point-order fixed-point Burnside, additive
orbifold reductions, labelled $(\mathbb Z\times C)$ permutation, enhanced
carrier, and quotient-stack/inertia outputs; (B) an information matrix with
rows `support/order`, `orbit type`, `labelled twist`, `isotropy`, and
`native dynamics`; (C) the regular-torsor formulas showing precisely where
$r_q$, $m_q$, $a_q$, or only period one remains.

**Caption boundary:** name the 2008, 2013, 2015, and 2018 definitions as
prior art. The hierarchy is definition-sensitive, not a claim that one
construction universally dominates another. The point-cardinality branch
must read “support $r_q$; exponent $m_q$; unit when $m_q=1$,” and the
regular-torsor formula panel must visibly mark the locked $q=2$ exception.

### Figure 2: Nine-row $(n_q,r_q,m_q)$ ledger and collisions

**Filename/label:** `fig2_nine_row_retention.pdf`,
`fig:nine-row-retention`.

**Message:** the regular-torsor size, source order, and cycle multiplicity are
different quantities; retained order collides across prime/composite moduli,
and cardinality restores multiplicity.

**Layout:** (A) exact grouped bars for $n_q,r_q,m_q$ in frozen order; (B) a
collision map that joins only $q=2$ with $q=4$ at $r=3$ and $q=6$ with
$q=9$ at $r=12$; (C) an exact annotated support/exponent ledger for source,
point cardinality, point orbifold, orbit cardinality, and orbit orbifold
outputs.

**Caption boundary:** all rows are development-seen controls. No fit,
ordering by magnitude, interpolation, or all-$q$ inference is permitted. The
caption must state that $q=2$ is the sole locked row/type pair combining
source support and unit exponent, that no reduction type does so uniformly,
and that $r_2=r_4=3$ prevents the exceptional support from identifying the
modulus.

### Figure 3: Effectivity, action kernel, and static inertia

**Filename/label:** `fig3_effectivity_counterexamples.pdf`,
`fig:effectivity-counterexamples`.

**Message:** labelled twist recovery is exactly an effectivity statement and
does not by itself create a full-order source factor; inertia retains
isotropy but has static dynamics.

**Layout:** (A) regular $C/1$: trivial kernel, exact labelled twist, source
period $\operatorname{ord}(a)$, one identity inertia sector; (B) trivial
one-point action: kernel $C$, quotient stack $BC$, labelled twist recovered
only modulo $C$, $|C|$ static inertia sectors; (C) effective
$C_6/C_2\sqcup C_6/C_3$: kernel one, labelled generator recovered, source
periods three and two but no period-six factor, quotient
$BC_2\sqcup BC_3$ with five static sectors. A shared footer states
$N=\bigcap K$ and “recover $a$ modulo $N$.”

**Caption boundary:** the $C_6$ object is a separately typed structural
control, not a tenth arithmetic modulus or a candidate.

## Citation plan

The publication bibliography and verification record live in
`paper/references.bib` and `paper/CITATION_VERIFICATION.md`. Cite direct
collisions at the claim site:

- `GuseinZadeLuengoMelle2008` for the rational fixed-point/point-order
  Burnside predecessor;
- `GuseinZade2013` for the labelled finite $(\mathbb Z\times G)$-set and
  triple $(H,m,\alpha)$;
- `GuseinZadeLuengoMelle2015` for the fixed-point versus fixed-orbit
  distinction, integral orbit-order zeta, additive orbifold reductions, and
  the monodromy-in-$G$ clock collapse;
- `EbelingGuseinZade2018` for enhanced carriers and enhanced orbifold fixed
  sectors;
- `Zegowitz2017` for shortening and gluing;
- `Miles2017` and `Walton2018` only as adjacent acting-group and finite-field
  quotient/twist boundaries;
- `BaakeNeumaerkerRoberts2013` only for the inherited rational-lattice
  centralizer context; and
- selected 2023--2026 primary records only to mark analytic Ruelle/Fried or
  cyclic-nerve boundaries, never as novelty evidence.

The DOI-authoritative Walton record is *Journal of Number Theory* **192**,
386--405 (2018). The frozen design-side citation sidecar's **189**, 202--223
entry is a historical bibliographic typo. The publication-layer correction
changes no source, theorem, result, or novelty conclusion.

## Reproducibility, visual QA, and review gates

1. A shared loader validates every frozen hash, strict-parses the source,
   raw result, and result manifest, and checks the exact nine rows,
   collisions, structural control, externality counters, review
   dispositions, and Paper-10 terminal status.
2. Scientific values are exact integers, rational numerator/denominator
   pairs, or symbolic theorem labels. There is no random draw or
   floating-point scientific computation.
3. Each of the three generators reads only the validated display payload;
   no generator imports or executes the candidate or analyzer.
4. The full package is rendered twice with a fixed hash seed, source date,
   SVG salt, metadata, font family, and private Matplotlib configuration.
   All nine outputs must be byte-identical between runs.
5. Mechanical QA requires one-page vector PDFs, embedded subset Unicode
   fonts, no Type-3 fonts, no raster PDF objects, selectable SVG text, no SVG
   image nodes, and PNG metadata within the 300 dpi tolerance.
6. Original-resolution visual inspection checks clipping, overlap,
   legibility, semantic arrows, grayscale/color redundancy, exact row order,
   collision labels, and the structural-control namespace boundary.
7. `FIGURE_TRACE.json`, `PROVENANCE.md`, `FIGURE_QA.md`, `ASSET_TREE.json`,
   `DETERMINISM_AUDIT.json`, and `FIGURE_MANIFEST.json` freeze the complete
   asset graph.
8. A fresh independent reviewer must bind the frozen evidence, plan,
   bibliography, generators, all nine rendered outputs, QA files, asset tree,
   and manifest. Only `ASSET_PASS` authorizes manuscript integration.

## Next steps

- [x] Freeze the claim/evidence and citation boundary.
- [x] Generate and mechanically inspect exactly three figures.
- [x] Complete original-resolution visual QA and freeze provenance.
- [ ] Obtain independent plan/figure asset review.
- [ ] Hand the passed `latex_includes.tex` and manifest identities to the
  separate manuscript stage.
