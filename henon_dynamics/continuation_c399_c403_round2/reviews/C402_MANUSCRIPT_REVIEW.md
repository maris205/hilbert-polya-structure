# C402 independent internal manuscript review

Date: 2026-09-05. Reviewed title: *Finite-state residue traces for Hénon maps with polynomial coordinate weights*.

## Outcome, provenance, and criteria boundary

**No blocking mathematical defect and no actionable minor defect found in the frozen manuscript.** The manuscript preserves the proof contract's full period and parameter quantifiers, residue convention, coordinate-only numerator, and ownership boundaries. Its explicit five-state quadratic calculation is correct. This is a bounded internal mathematical/citation review, not journal acceptance, a global novelty certificate, or a guarantee of correctness.

This reviewer did not author the manuscript, but previously reviewed its proof package and has now read that earlier report, the author's claim/citation map and initial-build receipt. The coordinator disclosed that two superscript commas were already repaired and that the coordinator had checked the manuscript. The verdict below is based on this reviewer's actual full-text reading and independent algebraic checks, not the coordinator's judgment. This is **not blind review or an independent error-process replication**. No human expert, external model/API, or full ARS panel was invoked. Calibration is `NOT_CALIBRATED`; the venue/track criteria binding is `criteria_binding_unavailable`.

The research-review skill's evidence collection, critical checking, and written handoff were used within the explicitly assigned internal mathematical-review scope. Its legacy external-model and ML-experiment defaults were not invoked. The ARS integrity discipline, applicable general research-quality criteria, and all seven AI-research failure modes were checked below. No numerical acceptance score is requested or supplied. The review did not alter author files, shared state, evaluations, or Git, rerun the mathematical checker, or compile the manuscript.

## Read coverage and frozen artifact identity

The eleven TeX/Bib inputs were read completely: **942 lines**, including all **822 lines of the eight section files**. This includes the abstract, ownership discussion, all theorem/proof text, displayed calculations, examples, scope, and declarations. Also read completely: `CONTRACT_SCOUT.md` (485 lines), `exact_check.py` (216 lines), `EXACT_CHECK_OUTPUT.json` (398 lines), the previous `NONLINEAR_RETURN_PROOF_REVIEW.md` (276 lines), `PAPER_PLAN.md`, `INITIAL_BUILD_RECEIPT.md` (96 lines), and `paper/BIBLIOGRAPHY_AUDIT.md` (56 lines). The initial receipt contains the complete claim map; the bibliography audit contains the four-reference/nine-context map. Both maps were compared with actual TeX rather than accepted as substitutes for reading it.

For the internal cited note, only its header and the relevant lines 515–675 were read in this manuscript review; no full-package content audit is claimed. `BUG_FINDING_C108.md` was identity-checked by hash, not separately read in full during this manuscript review. The historical defect's complete relevant account in the contract and the saved JSON's historical entry were read, and the checker was inspected for contamination from historical artifacts. The manuscript PDF was hash-checked; **this reviewer did not inspect its rendered pages or certify final build reproducibility**. Initial-build execution, page count, log and font claims remain the author's recorded production evidence, not fresh reviewer execution.

Artifact paths below are relative to `henon_dynamics/continuation_c399_c403_round2/`, unless explicitly stated otherwise.

| Artifact | SHA-256 |
| --- | --- |
| `nonlinear_return/paper/main.pdf` | `af77cd78166be37ca7629826038f0c2f48a0b52e85cac459e5972209edcba943` |
| `nonlinear_return/paper/SOURCE_SHA256.txt` | `0330552ffd0c3b6303a3ca4b201e78be8c261f5ffbf593c22a892a43c1af675e` |
| `nonlinear_return/paper/BIBLIOGRAPHY_AUDIT.md` | `e56d02c90220d8f0a94e36b88094737013d89f9daa101f936ed6e60d0cbc9852` |
| `nonlinear_return/INITIAL_BUILD_RECEIPT.md` | `1601398e614a7e15cf15fea834e562cecf0216633a8ce81681825a6309cff9ef` |
| `nonlinear_return/PAPER_PLAN.md` | `5085da97725df7706b190ffa6f12637b7b87771c4666bba686a628c473a77352` |
| `nonlinear_return/CONTRACT_SCOUT.md` | `b8780f67d4a9a23e66d2d0fe3f5a2c3c77a50c53a5930697baa00b23e8c28dfb` |
| `nonlinear_return/exact_check.py` | `f84450460221084ec5a19bead703872105d8d6b6532a4274d8b9c5e25519fe9f` |
| `nonlinear_return/EXACT_CHECK_OUTPUT.json` | `ba0911e8be0ef4de0a50fee2b6079db8844809fa03ad5743ad1a40eb871f94af` |
| `nonlinear_return/BUG_FINDING_C108.md` (identity only) | `04f42e7579ff8c64cbb7a61fea6d5ccc45b954b36b1be37499214bec51ea6dfa` |
| `reviews/NONLINEAR_RETURN_PROOF_REVIEW.md` | `736a2db8c411e9db4196b27ffae30b0b750b6db3d6b10aebddeaf37c3430e5a8` |
| `../henon_time_ordered_ruelle_cocycle/DERIVATION_PACKAGE.md` (relevant portions read) | `73c8c09e8971d0b33a4078fd84d65c8af07757f42b264a6718f52b002e94f74a` |

The complete input manifest, with paths relative to `nonlinear_return/paper/`, is:

```text
678195ea9f9c19faac96fdaeec7891b85d47a28ee0fe1c930a668067ab7830fb  main.tex
ec9da64838686d8994ad084c80c5f5ed953b7b75ee256ca570ef1d83ece253d0  math_commands.tex
32c0c9ccb7ec48f76de55613360385256cb3981f26cc880d07b56c87e07d82ac  references.bib
a2c4349d4a6dec3e87ebeb01a7a534b5c937b9aa8d95aac8fb1dfa7faef46169  sections/0_abstract.tex
21f80602ea075d829a1b9eb5335926f8a2a13f741dab490e8f9303707affb276  sections/1_introduction.tex
2d7b8750a9e88c6d15b265237fb0f916e300fcce8779af1b2b8367b6b656aa85  sections/2_setup.tex
437dd733c53901f5efcf0f2720da5335ccc2473cab9da639b767e3b53254208e  sections/3_residues.tex
98cfad6d405e89dd8f3c4a1b91f81ee3ef52953fa124e2804e8fc63dcd73aeed  sections/4_flow.tex
e0be0c74e901383ad81b6ccd21f9e1e2ec0451fbe672fc9b8353cf251e2d2230  sections/5_consequences.tex
f3b8ddc0275842b63d945ff74bd6bb4605634874fa9246111334d0931eec10b5  sections/6_scope.tex
991070c829f056bae1a1c34b103c2ade1b758ff14935e43a221e5326f4b5d75b  sections/7_declarations.tex
```

`sha256sum -c SOURCE_SHA256.txt` returned `OK` for all eleven inputs at final report preparation. Actual citation commands were independently enumerated: nine commands, with multiplicities `cattani1996residues:4`, `molinari2008determinants:2`, `bornemann2010fredholm:2`, `timeordered2026notes:1`. All four Bib entries are used; no further citation key or unregistered citation context was found.

## Complete mathematical claim review

Anchors in this table are actual TeX file/line anchors relative to `nonlinear_return/paper/`; labels identify mathematical objects even if later layout changes. They are not unverified PDF page anchors. Each disposition reflects examination of the accompanying proof, not a theorem-title-only check.

| Claim / principal failure risk | Typed anchor | Disposition and independent check |
| --- | --- | --- |
| Standing scope and all-period quantifier | `sections/2_setup.tex:4`, `eq:parameters`; `:100`, `thm:main`; abstract | Monic `p` has degree `d>=2`; `m>=0` is an upper bound for the univariate polynomial `q`, including zero; `a` is nonzero complex. The observable is the first-coordinate polynomial, not an arbitrary bivariate weight. The assertion is for every original `n>=1` with the same matrix, not a period subsequence or fitted recurrence. |
| Complete fixed scheme and cyclic correspondence | `sections/2_setup.tex:20`, `eq:cyclic`; `:32`, `eq:scheme-correspondence` | The recurrence reconstructs all coordinates polynomially from `(x_0,x_{n-1})`, and the cyclic equations impose exactly `H^n=id` on that pair. This gives a scheme-level inverse, not merely a bijection of simple roots. Labels are retained; no quotient by cyclic rotation is introduced. |
| Colliding neighbours for periods one and two | `sections/2_setup.tex:25`, `eq:period-one`, `eq:period-two` | For `n=1`, the lower term is `(1+a)x_0`; for `n=2`, the same neighbour receives both coefficients. The displayed equations add the incidences and do not pretend there are two distinct neighbouring variables. |
| Signed point trace versus degenerate residue | `sections/2_setup.tex:48`, `eq:pointwise-trace`; `:56`, `def:residue-trace` | The ordinary quotient is used only when the denominator is nonzero. The universal object is the negative full global residue, retaining higher local residues at nonreduced points. The all-period ordinary pointwise interpretation explicitly requires nondegeneracy at every period; it is not silently inferred from one period. |
| Finite complete intersection, length and normal form | `sections/3_residues.tex:5`, `lem:normal-form` | Pure powers `x_i^d` are pairwise relatively prime leading monomials, yielding a Gröbner basis, standard basis exponents below `d`, length `d^n`, and no projective common zero at infinity. The residue equals the top standard-monomial coefficient. Monic reduction introduces no parameter or Jacobian division, so the statement survives all permitted specializations. |
| Return order, Hill identity and constant negative sign | `sections/3_residues.tex:49`, `eq:monodromy`; `:57`, `lem:hill` | The derivative product is `A_{n-1}...A_0`, with determinant `a^n`. At `n=1`, `det J=v_0-1-a`; at `n=2`, it is `v_0v_1-(1+a)^2`. Both equal `-det(I-M)`. For `n>=3`, substituting the two off-diagonals into the cited scalar identity gives `tr M-1-a^n`, the same sign. No parity-dependent sign is substituted. |
| Torus coefficient extraction and convergence | `sections/3_residues.tex:109`, `eq:radius`; `:114`, `lem:local-expansion` | Monicity and `d>=2` permit a radius satisfying `abs(p(x))>(1+abs(a))R`; this choice is independent of period. For each fixed period, the product geometric series is uniformly absolutely convergent on that torus, permitting coefficient extraction. The proof does not assert an unnecessary uniform-in-period product convergence bound. |
| Local configuration formula and necessary degree inequality | `sections/3_residues.tex:116`, `eq:configuration-sum`; `:173`, `eq:local-degree-condition` | Expanding the two lower terms supplies the binomial factor and `a^{L_i}`. Variable `i` receives the neighbour exponents `R_{i-1}+L_{i+1}`. A nonzero local coefficient requires `d(L_i+R_i)<=m-d+1+R_{i-1}+L_{i+1}`. Coincident neighbours at `n=1,2` add exponents and binomially reproduce the already-combined lower term. |
| Total flow, negative and zero surplus | `sections/4_flow.tex:8`, `lem:uniform-flow`; `:25`, `eq:total-flow` | Summing gives `(d-1)sum e_i<=n mu`. Negative surplus excludes all nonzero configurations; zero surplus forces all flows to vanish. Thus defining the main cutoff with `max(0,mu)` does not admit spurious nonzero terms in the negative case. |
| Column-stochastic redistribution and row bound | `sections/4_flow.tex:38`, `eq:redistribution`; `:62`, `eq:row-sum` | For a fixed positive-surplus configuration, each column distributes its outgoing `L/e` and `R/e`; coincident destinations are added. Zero columns may be completed stochastically since their flow coordinate is zero. This makes `Pe` the incoming flow. `P` is not claimed row-stochastic. Each entry of `P^k` is at most one, and at most `min(n,2k+1)` starting vertices can reach a given row in `k` steps, so its row sum is at most `2k+1`. |
| Vanishing tail and period-independent cutoff | `sections/4_flow.tex:43`, `eq:iterated-flow`; `:50`, `eq:tail-flow`; `:75`, `eq:geometric-flow-bound` | First keep the finite period and configuration fixed. The tail is bounded by `d^{-K}` times the vector's `l1` norm and tends to zero. Only afterwards sum the uniform row bound to obtain `e_i<=mu(d+1)/(d-1)^2`. Taking the integer floor gives the stated cutoff. No row-stochastic assumption, illicit order of limits, or period-dependent final constant is used. |
| All closed walks and exact edge-state bijection | `sections/4_flow.tex:85`, main proof; `:100`, `eq:edge-bijection` | `E_i=(R_{i-1},L_i)` and `E_{i+1}=(R_i,L_{i+1})` match exactly the two local edge indices. Labelled closed walks and bounded flow configurations are mutually inverse also for periods one and two. The square state box may contain extra states, but every nonzero closed-walk product obeys the proved bound; the extra products vanish. No factor `1/n` belongs in the trace identity. |
| Polynomial coefficient ring and all specializations | `sections/2_setup.tex:110`, `eq:coefficient-ring`; `sections/4_flow.tex:120` onward | The reversed monic polynomial has constant coefficient one. Its negative integer powers have integer-polynomial coefficient expressions, and each entry extracts finitely many coefficients. Together with the monic normal-form argument, this proves the claimed coefficient ring without a generic-root continuation shortcut. Degree drops in `q` and `q=0` are harmless. |
| Negative trace and reciprocal determinant | `sections/4_flow.tex:118`, `eq:trace-closure`; `:142`, `eq:logdet` | The unsigned residue is `tr W^n`, while the frozen signed sequence is its negative. Substitution into the formal logarithm gives `D=det(I-zW)^{-1}`. The manuscript never identifies this with the ordinary determinant of `W` or `-W`. |
| Low-degree threshold and attribution | `sections/4_flow.tex:154`, `rem:threshold` | Below `d-1`, all residues vanish; at the threshold, the zero-flow term gives `rho_n=q_{d-1}^n` and `D=(1-q_{d-1}z)^{-1}`. The corrected exponent contains no comma. The low-degree cancellation is marked classical, not the claimed increment. |
| All-quadratic determinant and explicit deletion proof | `sections/5_consequences.tex:12`, `prop:quadratic`; `:26`, `eq:quadratic-support`; `:56`, `eq:five-state` | Independently checked every deletion group, all entries of the five-state block, the noncyclic bridge, and the three cyclic blocks; detailed certificate below. The factorization has degree at most four, is independent of `c,w`, and remains valid when parameters remove more edges. |
| Nontrivial and degenerate examples | `sections/5_consequences.tex:92`, `ex:nontrivial`; `:114`, `ex:parabolic` | All displayed coefficients and determinant factors agree with the frozen JSON and independent hand derivations below. At the double fixed point the residue is `q'(1)=3`, not a value of an undefined ordinary quotient. |
| Ordinary trace-class existence iff nilpotence | `sections/5_consequences.tex:140`, `prop:trace-class` | The paragraph and proof explicitly concern existence of a representative. Entire Fredholm determinant plus its germ expansion imply the entire identity `D_T(z)det(I-zW)=1`. A nonconstant polynomial has a complex root, giving a contradiction. Constant determinant implies all eigenvalues zero and hence nilpotence by Cayley–Hamilton; conversely `T=0` represents the zero sequence. This neither constructs a natural dynamical operator nor excludes supertraces or other weights. |
| Limits, reproducibility and metadata honesty | `sections/6_scope.tex:1`; `sections/7_declarations.tex:1` | Full complex scheme, signed denominator, autonomous fixed polynomial, and coordinate-only observable are preserved. No real-subset, absolute-denominator, minimal-state, global-priority, Euler-factor, automorphy or target zero-set claim is added. Saved exact checks are explicitly finite evidence, not the all-period proof; author and funding fields remain honestly unconfirmed. |

The manuscript's proof expansion is faithful to the original contract. In particular, the explicit deletion groups and bridge calculation expose the finite symbolic mechanism rather than strengthening the result beyond its proved scope.

## Independent certificate for the new explicit five-state passage

For `d=m=2`, the support condition is `r+v>=2(l+s)-1` for an edge `(r,l)->(s,v)`. Equivalently, an outgoing edge requires the target value `v-2s` to reach `2l-1-r`; an incoming edge requires the source value `r-2l` to reach `2s-1-v`.

The maxima of the two source/target expressions over the successive retained graphs are `3`, then `2`, then `1`. Therefore:

| Current graph | States deleted and sufficient obstruction |
| --- | --- |
| All sixteen states | `(0,3),(1,3)` require outgoing thresholds `5,4`, above `3`; `(3,0),(3,1)` require incoming thresholds `5,4`, above `3`. |
| After first group | `(0,2),(2,3)` require outgoing threshold `3`, above `2`; `(2,0),(3,2)` require incoming threshold `3`, above `2`. |
| After second group | `(1,2)` requires outgoing threshold `2`, `(2,1)` incoming threshold `2`, and `(3,3)` both thresholds `2`, all above `1`. |

These exclusions hold before each group is removed, as stated in the manuscript. They leave precisely `(0,0),(0,1),(1,0),(1,1),(2,2)`. Expanding the reversed polynomial verifies `c_{0,0}=v-bu`, `c_{1,0}=b^2u-bv-cu+w`, `c_{2,0}=-b^3u+b^2v+2bcu-bw-cv`, `c_{1,1}=u`, `c_{2,1}=v-2bu`, and the additional coefficient `c_{3,2}=u`. Including the binomial and `a` factors gives exactly every entry of `W_*` as printed; no factor two is missing.

The bridge `(2,2)` can only be reached from `(1,0)` and only exits to `(0,1)`, whose only outgoing edge is its own loop. It cannot belong to a cycle. Ordering the retained states as `(1,0),(0,0),(1,1),(2,2),(0,1)` makes the matrix block upper triangular, with diagonal blocks `[u]`, `[[A,u],[au,0]]`, `[0]`, and `[au]`. Consequently

`det(I-zW)=(1-uz)(1-auz)(1-Az-au^2z^2)`.

This argument preserves power traces and `det(I-zW)`, not an unrelated bare determinant `det W`. Its support exclusions and coefficient identities are parameter-polynomial identities; specialization only removes edges, so no generic-nonvanishing hypothesis is hidden in the graph proof.

## All references and all actual citation contexts

Four identities and all nine citation contexts were checked. **This means complete coverage of the bibliography/context population, not full reading of all cited publications.** Relevant mathematical statements were directly accessed in the three named primary author manuscripts and in the local note. Publisher or institutional records were used separately for publication metadata.

| Key | Verified identity | Actual content access and limitation |
| --- | --- | --- |
| `cattani1996residues` | Eduardo Cattani, Alicia Dickenstein and Bernd Sturmfels; 1996 chapter in *Algorithms in Algebraic Geometry and Applications*, Progress in Mathematics 143, 135–164, edited by L. González-Vega and T. Recio, Birkhäuser Basel; [publisher/DOI record](https://link.springer.com/chapter/10.1007/978-3-0348-9104-2_8). | Read the needed pure-power hypotheses, Theorem 2.3, Corollary 1.18, and Lemma 4.2 with its proof in the [1994 author preprint](https://arxiv.org/pdf/alg-geom/9404011). The paywalled published chapter body was not read; numbering is explicitly tied to the preprint. |
| `molinari2008determinants` | Luca Guido Molinari; *Linear Algebra and its Applications* 429(8–9) (2008), 2221–2226, DOI `10.1016/j.laa.2008.06.015`; [author's institutional record](https://air.unimi.it/handle/2434/43334). | Read equation (1), the associated block identity assumptions and its scalar specialization in [author preprint v3](https://arxiv.org/pdf/0712.0681v3). Nonzero neighbour coefficients fit `a!=0`; periods one and two are independently proved in this manuscript. No later-looking PDF-generated footer was used to change the publication year. |
| `bornemann2010fredholm` | Folkmar Bornemann; *Mathematics of Computation* 79(270) (2010), 871–915; [institutional publication record](https://portal.fis.tum.de/en/publications/on-the-numerical-evaluation-of-fredholm-determinants/) and [DOI record](https://doi.org/10.1090/S0025-5718-09-02280-7). | Read the opening trace-class discussion and equation (3.3) in §3 of the [author manuscript](https://arxiv.org/pdf/0804.2543), not all 43 pages or the whole section. The `I+zA` convention becomes `I-zA` by substitution. DOI BibTeX retrieved directly with `curl`, exit 0, reports September 2009; the institutional record supplies the 2010 volume year. Thus the draft's online/volume-year distinction is supported. Direct AMS article-page retrieval returned 403, not a claimed full-body read. |
| `timeordered2026notes` | *HCS-C22: T1–T3 derivation package*, local header dated 2026-08-09; honestly identified as an unpublished accompanying note without invented authors, journal or DOI. | Read the header and relevant Lemma 4/Theorem 5 material at repository path `henon_dynamics/henon_time_ordered_ruelle_cocycle/DERIVATION_PACKAGE.md`, lines 515–675. The introductory ownership deduction is confined to that note's specified family and numerators. No uninspected part is used to supply the present proof. |

The determinant properties in Bornemann's section are an exposition of classical theory, not claimed as his new discovery or this manuscript's innovation. The source-owned residue algorithms and cyclic determinant identity are likewise explicitly acknowledged. No new reference was added merely from an uninspected book locator.

| Context | Actual TeX anchor | Checked support and boundary |
| --- | --- | --- |
| R1 | `sections/1_introduction.tex:26` | CDS Theorem 2.3/Lemma 4.2 support the existing Laurent/normal-form algorithms; the text does not attribute period-independent matrix size to them. |
| R2 | `sections/1_introduction.tex:32` | Molinari equation (1) supports the cyclic Jacobian-to-return-product conversion, not the polynomial-weight closure theorem. |
| R3 | `sections/1_introduction.tex:36` | The internal Lemma 4/Theorem 5 contain the stated prior Hill, unit-weight, return-derivative numerator and signed degenerate-residue layer for their particular family. |
| R4 | `sections/1_introduction.tex:42` | Bornemann's accessed §3 opening supports the classical ordinary trace-class determinant input. No natural operator realization is inferred. |
| R5 | `sections/3_residues.tex:35` | CDS Lemma 4.2 applies after the pure-power leading terms and finite complete intersection are verified in the local proof. |
| R6 | `sections/3_residues.tex:72` | Molinari equation (1) specializes to the stated right/left coefficients and sign for `n>=3`; short periods are handled directly. |
| R7 | `sections/3_residues.tex:132` | CDS Theorem 2.3 supports the global coefficient representation under the stated initial-form condition; the manuscript proves its own large-circle geometric reorganization. |
| R8 | `sections/4_flow.tex:164` | CDS Corollary 1.18 supports the classical low-degree cancellation attribution; the manuscript also proves this family case directly by total flow. |
| R9 | `sections/5_consequences.tex:157` | Bornemann §3/equation (3.3) supplies entire determinant and local trace expansion; the subsequent pole contradiction and nilpotence equivalence are explicitly proved. |

The cited locators and surrounding claims fit the inspected sources. The nine actual contexts agree exactly with the author's inventory. These checks establish bounded attribution and dependency fit, not exhaustive later-literature novelty or a retraction/plagiarism-service certificate.

## Complete finite-result and implementation-surface audit

The finite-output population is not empty: the manuscript reports saved symbolic comparisons and displays two exact examples. The checker and all saved JSON entries were read, but **the checker was not executed in this review**. The following table exhausts the seven cases and 27 normal-form/edge-trace pairs; the values listed are the saved unsigned residues, not a new reviewer run.

| Saved case key | Periods | All saved common values |
| --- | --- | --- |
| `quadratic_constant` | 1–4 | `0, 0, 0, 0` |
| `quadratic_threshold` | 1–4 | `2, 4, 8, 16` |
| `quadratic_superthreshold` | 1–5 | `11/3, 61/9, 359/27, 2329/81, 15611/243` |
| `cubic_superthreshold` | 1–4 | `0, 0, 0, 0` |
| `cubic_nondegenerate_weight` | 1–3 | `1/2, 1/4, 7/8` |
| `quartic_threshold` | 1–3 | `1, 1, 1` |
| `parabolic_period_one` | 1–4 | `3, 5, 6, 9` |

The total is `4+4+5+4+3+3+4=27`. “Through period five” in §6 describes the maximum checked horizon, not five periods for each of the seven cases. The checker constructs the literal cyclic equations and computes their Gröbner normal form separately from its edge-matrix construction; the double fields agree in every saved row. This is two finite algebraic computations of the defined observable, not an empirical statistical test or proof of an all-period identity.

The remaining registered saved surfaces were all checked:

- Two nondegenerate quotient-algebra weighted sums, with `(n,dimension,value)=(2,4,61/9)` and `(3,8,359/27)`, agree with their normal-form values. The source code constructs `m_g` and `m_detJ`, asserts nonzero determinant for the latter before inversion, and evaluates their product's trace. It does not use that inverse at the parabolic example.
- Six symbolic Hill checks at periods `1,...,6` have saved difference zero. Code adds coincident Jacobian entries rather than overwriting them and multiplies the derivative matrices in the stated chronological order.
- The free-coefficient quadratic determinant comparison has saved difference zero and the same factorization as Proposition `prop:quadratic`. Its symbolic parameters include all `b,c,u,v,w,a`, not one numerical specialization. The manuscript now also supplies the independent graph/block proof checked above.
- The saved environment is Python 3.12.3 and SymPy 1.14.0. The contract records successful prior execution. These facts are saved provenance and code/output consistency, not fresh reviewer observation of execution. No rerun or new experiment was claimed by the manuscript or by this review.

Every displayed finite mathematical value in the manuscript was additionally checked by hand. In `ex:nontrivial`, the two scalar blocks contribute `1+(2/3)^n`; the two-dimensional block has trace recurrence `S_0=2`, `S_1=2`, `S_n=2S_{n-1}+(2/3)S_{n-2}`. This reproduces all five displayed fractions and the determinant factors. In `ex:parabolic`, `F_{1,0}=(X-1)^2` gives the derivative residue `q'(1)=3` and signed trace `-3`; the quadratic block recurrence together with the two unit loops gives `3,5,6,9` and `(1-z)^2(1-z-z^2)`. The general low-degree/threshold values follow from the already-checked zero-flow formula. No decimal fitting, omitted sign change, or discarded degenerate point is used.

The historical C108 quantity `-1664/1725` is segregated in the saved historical entry and the contract's defect discussion. It is neither a value of the new theorem nor a claimed contribution in the manuscript. The inspected checker imports its algebraic dependencies and constructs its own systems; it does not load a historical C108 trace file as input. The manuscript does not mention or reuse that wrong trace. This review does not retroactively certify, repair, or rerun the historical artifact.

## Strongest counterargument and ownership disposition

The strongest substantive objection is that the residue method, fixed-period normal-form algorithm, cyclic Hill identity, and ordinary Fredholm entire-function obstruction are classical; the unit-weight cancellation is also prior-owned. A theorem that merely combines those facts at finitely many periods would not justify the manuscript's claimed increment. The actual proof supplies the missing uniform ingredient: a local exponent bound independent of the original period, followed by an exact edge-state bijection valid for every degree-bounded coordinate polynomial and all permitted specializations. The quadratic graph calculation is a concrete consequence of that one theorem, not an independently inflated contribution.

No inspected primary passage or relevant internal-note passage directly establishes that same full set of quantifiers. This bounded observation is **not** a worldwide priority finding, an assessment of journal-level significance, or proof that no alternative classical construction yields the same result. The manuscript makes no global “first” assertion. Its finite matrix and rational generating function also do not furnish the target arithmetic controls, Euler factors or a Hilbert–Pólya realization. This review changes neither target admission nor the batch's arithmetic-completion status and supplies no A2/A3 score.

## Coverage receipt for the empty defect list

The following categorical dispositions concern this internal manuscript-review scope only; they are not calibrated venue scores. The report records no weaknesses because none was substantiated, not because a quota was waived without checking.

| General review dimension | Scoped disposition | Coverage evidence / limitation |
| --- | --- | --- |
| Originality and ownership | Bounded attribution meets scope; global novelty NOT ASSESSED | Classical inputs and internal prior layer separated from the uniform-flow claim; all four sources and nine contexts checked. No exhaustive novelty search or journal calibration was performed. |
| Technical correctness | MEETS inspected proof scope | Full theorem chain, short periods, degeneracy, flow tail/row bound, trace sign, five-state graph and trace-class boundary checked above. This remains fallible model review, not a formal proof certificate. |
| Methodological clarity and reproducibility | MEETS manuscript scope | Full written argument, actual checker and entire saved output read; no omitted experiment protocol is needed for a proof. New execution and final production reproducibility NOT ASSESSED here. |
| Evidence validity | MEETS registered population | All 27 saved pairs, two quotient sums, six Hill checks, symbolic determinant and all displayed example values covered; finite evidence not promoted to an all-period proof. |
| Literature fit and source integrity | MEETS bounded source/context check | All identity and precise dependency contexts registered with actual access limits; no paywalled full-body, whole-book or external-service attestation fabricated. |
| Significance and claim proportionality | MEETS internal scope discipline; venue significance NOT ASSESSED | One bounded source theorem and its consequences; no target realization, global priority, genericity escape or minimal-state claim. |
| Presentation, ethics and disclosure | MEETS source-text review; final layout NOT ASSESSED | All prose/declarations read; anonymous authorship/funding fields remain pending explicit confirmation; AI and internal-review status disclosed. Final all-page QA remains with the coordinator. |

## All seven AI-research failure modes

| Failure mode | Scoped disposition | Evidence and explicit limit |
| --- | --- | --- |
| 1. Implementation bug passing self-review | No suspected unresolved defect on inspected surfaces | Checker read against literal equations, additive short-period incidences, derivative order, coefficient cutoff, and quotient-inverse guard; all saved surfaces reconciled. This is not execution replication or a claim of bug-free repository code. |
| 2. Hallucinated citation | CLEAR on registered identity/claim-fit population | Four real entries, nine actual contexts, correct primary locators and version distinctions. Access limitations are explicit; no full-publication or retraction-clean certificate is issued. |
| 3. Hallucinated experimental result | CLEAR on registered finite-output population | All manuscript numbers/counts match the saved JSON and inspected code; displayed examples also checked algebraically. Saved successful execution is attributed to its recorded provenance. |
| 4. Shortcut reliance | CLEAR for named proof risks | The uniform flow argument and bijection prove all periods; finite examples do not. The proof uses column stochasticity plus a separately proved row bound, handles `n=1,2`, and never assigns an ordinary quotient at a zero denominator. |
| 5. Implementation bug reframed as novelty | CLEAR for this manuscript | The historical C108 defect and wrong trace are absent from the contribution and numerical example surface. The claimed result is the explicit all-period proof, with classical ownership deducted. |
| 6. Methodology fabrication | CLEAR on reported methods | Actual code matches the reported finite symbolic operations and limitations; there is no invented dataset, stochastic protocol, rerun, compilation by this reviewer, human confirmation or external-model review. |
| 7. Early frame lock | No suspected frame-lock defect in this scope | The review directly tested the principal counterarguments and manuscript-specific additions. The source theorem remains separate from target arithmetic ambitions, and global novelty/significance remain open rather than manufactured. |

These are scoped failure-mode dispositions, not a full ARS Stage 2.5/4.5 execution or an accountable external peer-review certification. The unavailable venue criteria do not authorize invented ratings, and the absence of empirical ML experiments is not itself a weakness in this mathematical manuscript.

## Handoff

Blocking findings: **0**. Actionable minor findings: **0**. No manuscript correction is requested. The two pre-review superscript commas are already absent in the frozen source and were not mathematical changes. No issue from the previous proof review has reappeared through manuscript expansion.

The coordinator may proceed with the required final builds in two fresh directories and actual all-page visual QA on these reviewed source bytes. Those production gates, packaging, author/funding confirmation before any submission, separate source/target decisions, and any affected-only re-review after later source changes remain outside this completed review. Preserve the recorded source hashes; a changed mathematical input requires identifying the affected claims rather than silently extending this verdict to new bytes.
