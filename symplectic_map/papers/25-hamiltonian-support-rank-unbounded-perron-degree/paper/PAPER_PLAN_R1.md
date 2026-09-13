# Paper Plan R1

## Frozen article identity

- **Exact title:** Sharp Support-Rank Bounds and Unbounded Perron Degree in Hamiltonian Product Shears
- **Article type:** standalone proof-first journal article
- **Evidence mode:** complete symbolic derivation; no empirical evidence
- **Base scope:** ordinary total degree over a characteristic-zero field, for the displayed positive Hamiltonian product-shear family
- **Literature cutoff:** the fixed, nonexhaustive eight-record primary-source screen through 2026-08-26 UTC
- **Content-page target:** 26.0 pages from Abstract through Conclusion, excluding references
- **Planned source count after later authorization:** exactly three manuscript-source files
- **Current lifecycle:** plan only; manuscript, bibliography, figures, computation, build, PDF, publication, and release remain unopened

### Reader promise

For every integer \(d\ge 2\), the article will construct an explicit positive
Hamiltonian product shear on \(2d\) affine coordinates whose ordinary iterate
degrees are exactly
\[
\deg(F^n)=e_1^{\mathsf T}C^n\mathbf 1,
\]
whose Perron dynamical degree has algebraic degree exactly \(d\), and whose
visible scalar degree sequence has minimal rational constant-coefficient
recurrence order exactly \(d\); an accompanying selected support-row rank
factorization bounds the nonunit characteristic degree, and this family
attains that bound in every constructed rank \(r=d\ge 2\).

This complete all-\(d\) conjunction is the headline. The abstract rank
factorization, any fixed-dimensional specialization, and each standard
spectral or finite-field ingredient are supporting components, not alternative
headlines.

### What, why, and so what

- **What:** prove a support-rank upper law and realize it sharply by one
  explicit positive Hamiltonian family in every nontrivial rank \(d\ge2\),
  with literal, fixed-coordinate ordinary-degree visibility.
- **Why:** a selected degree matrix gives only a candidate tropical recursion;
  it does not by itself prove strict face selection, survival against both
  temporal carries, noncancellation of leading forms, or minimality after
  scalar observation.
- **So what:** the construction produces unbounded Perron algebraic degree and
  unbounded exact scalar recurrence order inside a rigid Hamiltonian
  product-shear model, while identifying the selected support-row rank as a
  sharp structural ceiling on nonunit characteristic degree.

## Narrative and contribution order

The article tells one proof chain, not two loosely coupled stories.

1. **Headline all-\(d\) realization.** Announce the explicit family and the
   conjunction of exact visible degrees, Perron degree \(d\), scalar order
   \(d\), and support-rank attainment.
2. **Exact-degree mechanism.** Explain why the literal polynomial maps follow
   the matrix recursion: parameter order, symplectic gradients, broad and
   fine chambers, two half-step carries, positive-semiring survival, and
   fixed \(q_1\) visibility.
3. **Arithmetic-spectral closure.** Derive the characteristic polynomial,
   force an irreducible reduction \(t^d-c\), and pass from positivity and
   irreducibility to Perron degree and exact scalar minimality.
4. **Structural interpretation.** Prove the support-row factorization early,
   then return to it at the end to establish existential rank-\(d\)
   sharpness.

The Introduction may state the support-rank theorem before the construction
theorem for readability, but its contribution bullets and final paragraph
must make the all-\(d\) conjunction the paper's value proposition.

## Frozen theorem hierarchy

### Headline Theorem H: all-degree sharp Hamiltonian realization

For every \(d\ge2\), choose parameters in the exact order
\[
d\longrightarrow p,c\longrightarrow
a_1<\cdots<a_d\longrightarrow b,R_0
\]
with the locked congruence and strict inequalities. Define
\[
V(q)=\prod_{j=1}^d q_j^2+\sum_{i=1}^d q_i^{a_i+1},
\qquad
W(p)=\prod_{j=1}^d p_j^b,
\qquad
F=T_W\circ S_V,
\]
and
\[
D=\operatorname{diag}(a_1,\ldots,a_d),\qquad
B_0=bJ-I_d,\qquad
C=B_0D=b\mathbf1a^{\mathsf T}-D.
\]
Then:

1. \(F\) is a positive integer-coefficient polynomial symplectomorphism;
2. \(\deg(F^n)=e_1^{\mathsf T}C^n\mathbf1\) for every \(n\ge0\), with
   \(q_1\) uniquely degree-maximal only for \(n\ge1\);
3. \(\chi_C\) is irreducible over \(\mathbb Q\);
4. \(\lambda_1(F)=\rho(C)\), and \(\rho(C)\) has algebraic degree \(d\);
5. the visible scalar sequence has minimal rational
   constant-coefficient recurrence order \(d\), both from \(n=0\) and
   eventually; and
6. the selected stacked row rank is \(r=d\), so the structural bound below
   is attained.

Every conjunct must survive in the final theorem statement. No theorem
summary may replace it with only the matrix formula, a fixed \(d\), or a
Perron-degree existence sentence.

### Structural Theorem S: support-row factorization

For
\[
A=-I_N+\mathsf P\mathsf Q,\qquad
B=-I_N+\mathsf R\mathsf S,\qquad C=BA,
\qquad
r=\operatorname{rank}\begin{bmatrix}\mathsf Q\\\mathsf S\end{bmatrix},
\]
choose a full row basis \(T_0\) of the stacked row space and factor
\(\begin{bmatrix}\mathsf Q\\\mathsf S\end{bmatrix}=LT_0\). With the locked
matrix \(X\), prove
\[
\chi_C(t)=(t-1)^{N-r}
\det\bigl((t-1)I_r-T_0X\bigr).
\]
The reduced determinant is monic of degree \(r\). This proves only unit
algebraic multiplicity at least \(N-r\) and nonunit characteristic degree at
most \(r\). It does not exclude additional copies of \(t-1\).

### Corollary C: existential sharpness in every constructed rank

For the family in Theorem H, use
\[
D=-I_d+I_d(D+I_d),\qquad
B_0=-I_d+(b\mathbf1)\mathbf1^{\mathsf T}.
\]
Since \(D+I_d\) is invertible, the stacked selected row rank is \(d\).
Irreducibility of the degree-\(d\) characteristic polynomial excludes
\(t-1\), so the entire degree is nonunit. This attains Theorem S for each
constructed \(r=d\ge2\), existentially and not for every rank presentation.

## Complete lemma dependency map

| ID | Frozen proof unit | Inputs | Output | Used by | Main-text location |
|---|---|---|---|---|---|
| L1 | Full-row-basis factorization and rectangular Sylvester identity | \(A,B,C\), compatible dimensions, row basis \(T_0\) | Explicit factor \((t-1)^{N-r}\) and monic degree-\(r\) reduced determinant | L2, L15, Theorem S | §3.2 |
| L2 | Common-kernel sector and rank boundaries | L1 and \(\ker[\mathsf Q;\mathsf S]\) | Unit multiplicity lower bound only; \(r=0\), \(r=N\), and empty-determinant semantics | Theorem S, anti-claim control | §3.3 |
| L3 | Ordered residue lifts and simultaneous large-\(b\) choice | Fixed \(d\ge2\), Dirichlet, cyclicity of \(\mathbb F_p^\times\) | Parameters in order \(d\to p,c\to a_i\to b,R_0\), all strict inequalities | L4–L7, L12 | §4 |
| L4 | Literal gradients, inverses, symplecticity, and selected matrices | Locked \(V,W\), characteristic zero | Polynomial symplectomorphisms and literal \(D,B_0,C\) | L5–L11, L15 | §2.2 and recalled in §5.1 |
| L5 | Broad-cone strict spike selection | L3, literal \(V\)-rows, \(a_1+1>4d\), \(R_0^2<2\) | Pure spike wins strictly in every component on \(\mathcal K_{\rm ratio}\) | L6, L8, L10 | §5.2 |
| L6 | Strict broad-cone invariance and cross-block domination | L3, L5, positive \(C\) | \(C\mathcal K_{\rm ratio}\) lies in its interior and \((Cu)_i>\max_j a_ju_j\) | L8, L10 | §5.3 |
| L7 | Fine visibility-chamber invariance | L3, L4, weighted visibility inequalities | Seed admission; all chamber walls preserved; coordinate one strictly largest after one step | L10 | §5.4 |
| L8 | Both temporal carries | L5–L7, phase labels, \(a_i>1\) | Fresh \(V\)-terms beat carried momentum and fresh \(W\)-terms beat every carried \(q,p\) term | L9, L10 | §5.5 |
| L9 | Positive-semiring top-form survival | Positive integer coefficients, strict selectors, characteristic zero | No selected leading form cancels or vanishes | L10 | §5.6 |
| L10 | Exact ordinary-degree visibility | L4–L9 and \(u_0=\mathbf1\) | \(u_n=C^n\mathbf1\), exact degree formula, tied seed, unique \(q_1\) for \(n\ge1\) | L13, L14, Theorem H | §5.7 |
| L11 | Characteristic-polynomial formula | Locked rank-one form of \(C\) | \(\chi_C(t)=t^d+\sum_{k=1}^d(1-bk)e_k(a)t^{d-k}\) | L12, L13, L14 | §6.1 |
| L12 | Modular reduction and full binomial audit | L3, L11, roots-of-unity residue multiset, primitive \(c\) | \(\chi_C\bmod p=t^d-c\), irreducible over \(\mathbb F_p\) and \(\mathbb Q\) | L13–L15 | §6.2–§6.4 |
| L13 | Perron dynamical and algebraic degree | Positive \(C\), L10, L12 | \(\lambda_1(F)=\rho(C)\), Perron algebraic integer of degree \(d\) | Theorem H | §7.1–§7.2 |
| L14 | Reachability, observability, Hankel rank, and scalar order | L10, L12, L13, Cayley–Hamilton | Exact rational recurrence order \(d\), both from-start and eventual | Theorem H | §7.3–§7.5 |
| L15 | Rank-\(d\) sharpness | L1–L2, L4, L12, selected presentations | Existential attainment of the support-rank bound for every \(d\ge2\) | Corollary C, Theorem H | §8.1 |

### Dependency graph in prose

The structural branch is \(L1\to L2\), held open until \(L15\). The
construction branch begins with \(L3+L4\), passes through
\(L5+L6+L7+L8+L9\), and closes at exact visibility \(L10\). The arithmetic
branch is \(L3+L11\to L12\). Exact visibility and arithmetic irreducibility
meet at \(L13\) and \(L14\). Finally \(L1+L2+L4+L12\to L15\), which joins
the abstract rank law to the all-\(d\) family.

No citation replaces any arrow in this graph. Standard results may be cited
for provenance, but their hypotheses and the theorem-critical application
must be written in the article.

## Boundary-case map

| Boundary | Required treatment | Location | Failure to prevent |
|---|---|---|---|
| \(r=0\) | \(Y=0\), \(C=I_N\), and the empty determinant equals one | §3.3 | dimensionally meaningless reduced factor |
| \(r=N\) | forced unit exponent is zero; no unit factor is forced | §3.3 | false claim that a unit root always occurs |
| extra unit roots | reduced determinant may itself vanish at \(t=1\) | §3.3 and §8.3 | exact-unit-multiplicity overclaim |
| \(d=2\) | \(p\) is odd and primitive \(c\) is a nonsquare | §4.5 and §6.4 | missing smallest-degree irreducibility case |
| \(4\mid d\) | \(p\equiv1\pmod d\) implies \(p\equiv1\pmod4\) | §6.3–§6.4 | omission of the extra binomial criterion |
| tied seed | all \(2d\) coordinate degrees equal one at \(n=0\) | §5.4 and §5.7 | false unique-visibility claim at the identity |
| positive iterates | \(q_1\) is uniquely maximal for every \(n\ge1\) | §5.7 | changing visible coordinate or a merely eventual claim |
| characteristic zero | injectivity of \(\mathbb Z\to K\) preserves positive derivative coefficients | §2.1 and §5.6 | unsupported positive-characteristic extension |
| strict walls | every selector, ratio, weighted, carry, and block inequality remains strict | §5.2–§5.5 | a hidden tie in the tropical-to-polynomial upgrade |

## Claims-to-evidence matrix

The term evidence below means a complete internal symbolic derivation unless
the row is explicitly contextual. No experiment, computed example, or
literature citation is mathematical evidence for a headline claim.

| Claim | Exact evidence obligation | Frozen input anchor | Planned statement/proof | Status required in manuscript |
|---|---|---|---|---|
| H1: support-row factor | Reproduce the row-basis factorization and polynomial Sylvester identity with dimensions | PROOF_PACKAGE Step 1; C-01 | Theorem S, §3.2 | proved in full |
| H2: lower-bound-only unit sector | Kernel check, \(r=0,N\), and extra-\(t-1\) warning | PROOF_PACKAGE Step 1 and Boundary Cases; C-02 | §3.3 | proved and explicitly narrowed |
| H3: parameters for every \(d\) | Noncircular existence with finite simultaneous large-\(b\) choice | PROOF_PACKAGE Step 2; C-03 | Proposition, §4 | proved in full |
| H4: polynomial symplecticity | Direct Hessian pullback and subtraction inverses | PROOF_PACKAGE Step 3; C-04 | Lemma, §2.2 | proved directly |
| H5: literal selected matrices | Differentiate \(V,W\); derive \(D,B_0,C\) from actual monomials | PROOF_PACKAGE Step 3; C-04 | §2.2, §5.1 | proved directly |
| H6: broad selection and invariance | Strict spike comparison, denominator positivity, strict ratio inequality | PROOF_PACKAGE Steps 5; C-05 | §5.2–§5.3 | proved wall by wall |
| H7: fine visibility | Seed membership and every coordinate, ratio, weighted wall | PROOF_PACKAGE Step 6; C-06 | §5.4 | proved wall by wall |
| H8: two carries | Track both half-steps and all old-versus-new comparisons | PROOF_PACKAGE Step 7; C-07 | §5.5 | proved with phase labels |
| H9: no cancellation | Positive-semiring induction and integral-domain top forms in characteristic zero | PROOF_PACKAGE Step 7; C-08 | §5.6 | proved, not assumed generic |
| H10: exact ordinary degrees | Combine H5–H9 and fixed \(q_1\) visibility | PROOF_PACKAGE Step 7; C-09 | Theorem H component, §5.7 | exact equality for all \(n\ge0\) |
| H11: characteristic formula | Rank-one determinant lemma plus \(k\)-fold count | PROOF_PACKAGE Step 8; C-10 | §6.1 | derived coefficient by coefficient |
| H12: irreducibility | Roots-of-unity residues, full binomial criterion, Gauss lift | PROOF_PACKAGE Step 9; C-11 | §6.2–§6.4 | proved with \(d=2\) and \(4\mid d\) |
| H13: Perron degree | Positive Perron projection with positive visible coefficient and irreducible minimal polynomial | PROOF_PACKAGE Step 10; C-12 | §7.1–§7.2 | proved |
| H14: exact scalar order | Cayley–Hamilton upper bound; cyclic reachability/observability; Hankel and tail lower bounds | PROOF_PACKAGE Step 11; C-13 | §7.3–§7.5 | from-start and eventual versions proved |
| H15: rank sharpness | Selected presentation, invertible \(D+I_d\), irreducible nonunit factor | PROOF_PACKAGE Step 12; C-14 | §8.1 | existential for \(r=d\ge2\) |
| N1: public positioning | Use only the eight locked contextual records and the exact cutoff | CITATION_VERIFICATION; both independent PASS reviews | §1.2, §2.3, §8.2 | bounded and nonexhaustive |
| N2: portfolio separation | Subtract occupied local mechanisms without exposing internal governance as public scholarship | NOVELTY_ASSESSMENT; source lock collision rows | planning and §8.2 wording control | no public internal identifiers |

## Exact page budget

References are outside the 26.0-page content budget. All theorem-critical
proofs remain in the 26.0 pages; no appendix is required to carry a missing
dependency.

| Unit | Pages |
|---|---:|
| Abstract | 0.5 |
| §1 Introduction and theorem map | 2.5 |
| §2 Hamiltonian product shears, degree profiles, and context | 2.5 |
| §3 Support-row factorization | 2.5 |
| §4 Uniform parameter construction | 3.0 |
| §5 Two-level chambers and exact polynomial-degree induction | 6.0 |
| §6 Characteristic polynomial and irreducibility | 3.0 |
| §7 Perron degree and exact scalar recurrence | 3.0 |
| §8 Sharpness, positioning, limitations, and conclusion | 3.0 |
| **Total content pages** | **26.0** |

If space pressure appears, compress repeated algebraic rearrangements and
duplicate motivation first. Never compress away assumptions, phase labels,
strictness, boundary cases, the exact binomial hypotheses, scalar-minimality
arguments, or anti-claim language.

## Section-by-section writing plan

### Abstract — 0.5 page

- **Purpose:** state the all-\(d\) result before field-level background and
  make the complete conjunction intelligible without citations.
- **Inputs:** Theorem H, Theorem S, and Corollary C.
- **Outputs:** one compact reader promise; the explicit family class; exact
  degree identity; Perron algebraic degree \(d\); scalar order \(d\); and
  rank-\(d\) sharpness.
- **Proof dependencies:** none shown in detail, but every abstract clause must
  map to H1–H15.
- **Transition:** end by naming strict face control and arithmetic
  irreducibility as the two proof engines developed in the body.

Five-sentence content order:

1. State the explicit all-\(d\) construction and exact visible degree result.
2. Explain that matrix-degree propagation is difficult because literal
   polynomial iterates contain competing faces and carried coordinates.
3. State that two nested strict chambers and positive-semiring survival close
   the tropical-to-polynomial gap.
4. State the irreducible characteristic polynomial, Perron degree \(d\), and
   minimal scalar order \(d\).
5. State the support-row upper law and its attainment by the family, with no
   firstness or priority wording.

Do not open with a generic claim about dynamical systems or symplectic maps.
Do not cite in the Abstract. Do not mention a fixed \(d\).

### §1 Introduction and theorem map — 2.5 pages

- **Purpose:** make the What, Why, and So What explicit and position the
  all-\(d\) conjunction as the sole contribution unit.
- **Inputs:** reader promise, Research Question, Claims–Evidence Matrix,
  frozen context boundaries, and anti-claims.
- **Outputs:** formal problem anchor, contribution bullets, concise theorem
  statements, proof-roadmap table, and bounded positioning.
- **Dependencies:** no proof is discharged here; all claims point forward to
  §§2–8.
- **Transition:** the final paragraph moves from the announced theorem to the
  literal Hamiltonian supports whose gradients generate the matrices.

Subsection allocation:

#### §1.1 Problem anchor and obstruction — 0.55 page

Explain the distinction among a selected matrix upper recursion, literal
ordinary polynomial degrees, and scalar recurrence complexity. State why a
rank ceiling is meaningful only if a gradient-compatible family attains it
and the selected orbit is exact.

#### §1.2 Bounded context and gap — 0.55 page

Synthesize four contextual families rather than listing papers:

1. affine-triangular dynamical-degree realization;
2. spectral and algebraicity frameworks;
3. Hamiltonian position/momentum shear generation;
4. higher-dimensional degree-growth examples and finite-field arithmetic.

Use the eight-source cutoff and nonexhaustive qualifier. Do not make the
literature screen a theorem or a priority argument.

#### §1.3 Headline theorem and reader promise — 0.70 page

State Theorem H first as a compact conjunction. State Theorem S second as the
structural ceiling and Corollary C as the joining result. Preserve
the iterate-index condition \(n\ge0\), unique visibility only for \(n\ge1\),
characteristic zero, and existential sharpness.

#### §1.4 Contributions and non-contributions — 0.45 page

Use four falsifiable bullets:

1. exact all-\(d\) Hamiltonian degree visibility;
2. arithmetic Perron degree \(d\);
3. exact from-start and eventual scalar recurrence order \(d\);
4. support-rank upper law attained in every constructed \(r=d\ge2\).

Follow immediately with a one-paragraph limitation signal: the work is not
a general weak-Perron realization, classification, minimality, or priority
theorem.

#### §1.5 Proof map and organization — 0.25 page

Include one compact structural table mapping construction, exact-degree,
arithmetic-spectral, and sharpness branches. This table replaces a forced
hero figure and lets a skim reader see the dependency chain.

### §2 Hamiltonian product shears, degree profiles, and context — 2.5 pages

- **Purpose:** define the object exactly, prove symplecticity directly, and
  separate contextual citations from theorem evidence.
- **Inputs:** characteristic-zero field \(K\), ordinary total degree, the
  locked potentials, and standard symplectic form.
- **Outputs:** unambiguous notation; polynomial inverses; direct
  symplecticity; literal gradient competitors; selected matrices
  \(D,B_0,C\); and a contextual literature boundary.
- **Dependencies:** L4; named background sources only for context.
- **Transition:** the selected support presentations motivate the abstract
  row-rank theorem in §3.

Subsection allocation:

#### §2.1 Field, degree, and phase notation — 0.60 page

Define \(K\), \(q,p\), ordinary tuple degree, \(F^n\), leading homogeneous
form, position-degree vector \(u_n\), momentum half-step vector, and the
forward first dynamical degree. State characteristic zero at first use.

#### §2.2 Literal gradients and symplecticity — 1.15 pages

Differentiate both potentials, show the two \(V\)-competitor weights and the
unique \(W\)-row, give subtraction inverses, and perform the symmetric-Hessian
pullback argument. Derive
\[
D,\qquad B_0=bJ-I_d,\qquad C=B_0D=b\mathbf1a^{\mathsf T}-D
\]
from the supports rather than inserting matrices after the fact. Record
strict positivity of every entry of \(C\).

#### §2.3 Context without theorem transfer — 0.75 page

Use Berger–Turaev and Koch–Lomelí only to establish shear context; use
Blanc–van Santen, Shao–Sun, Dang–Favre, Déserti, and Abboud–Xie only for the
bounded dynamical-degree landscape. Explicitly state that invertibility,
symplecticity, exact degrees, and rank sharpness are proved internally.

### §3 Support-row factorization — 2.5 pages

- **Purpose:** prove the structural ceiling cleanly and delimit precisely
  what row rank does and does not determine.
- **Inputs:** compatible presentations
  \(A=-I+\mathsf P\mathsf Q\),
  \(B=-I+\mathsf R\mathsf S\).
- **Outputs:** Theorem S, common-kernel corollary, \(r=0,N\) audit, and the
  extra-unit-root warning.
- **Dependencies:** L1–L2; rectangular Sylvester identity with hypotheses
  stated.
- **Transition:** §4 constructs parameters for which this ceiling will later
  be attained without violating the Hamiltonian gradient constraints.

Subsection allocation:

#### §3.1 Dimensions and stacked row space — 0.35 page

Display the abstract ambient dimension \(N\) and the dimensions of
\(\mathsf P,\mathsf Q,\mathsf R,\mathsf S\). Define
\(Y=[\mathsf Q;\mathsf S]\), its rank \(r\), and a full row basis \(T_0\).

#### §3.2 Factorization and determinant identity — 1.10 pages

Multiply \(C-I_N\), factor it as \(UY\), write \(Y=LT_0\), and obtain
\(C=I_N+XT_0\). Apply Sylvester over \(K(t-1)\), then explicitly invoke
polynomial identity to include \(t=1\). Establish monicity and degree of the
reduced determinant.

#### §3.3 Kernel interpretation and boundary cases — 0.70 page

Identify
\(\ker T_0=\ker\mathsf Q\cap\ker\mathsf S\), show it is fixed by \(C\), and
state only a lower bound. Treat \(r=0\) with the empty determinant and
\(r=N\) with exponent zero. State that extra unit roots may occur.

#### §3.4 Structural meaning and limits — 0.35 page

Translate the factorization into an upper bound on nonunit characteristic
degree. Say explicitly that rank does not determine an exact unit profile,
unique presentation, or quotient degree.

### §4 Uniform parameter construction — 3.0 pages

- **Purpose:** show that all arithmetic, selector, and visibility conditions
  can be met for every \(d\ge2\) in a noncircular order.
- **Inputs:** fixed \(d\ge2\); exact congruence and inequalities from the
  source lock.
- **Outputs:** one parameter-existence proposition feeding every later
  chamber and irreducibility argument.
- **Dependencies:** L3; Dirichlet and finite-field cyclicity, with standard
  citations still pending verification.
- **Transition:** freeze all parameters before beginning the orbit proof in
  §5; no later iterate may influence their choice.

Subsection allocation:

#### §4.1 Locked quantifiers and target inequalities — 0.40 page

Display the full order
\(d\to p,c\to a_1<\cdots<a_d\to b,R_0\), define
\(S_a=\sum_i a_i\), \(M=a_d\), and list every locked congruence and strict
inequality once.

#### §4.2 Prime and primitive element — 0.60 page

Use \(p\equiv1\pmod d\), \(d\mid p-1\), and cyclicity to select a generator
\(c\) of exact order \(p-1\). Never weaken primitive to merely nonzero.

#### §4.3 Ordered positive lifts — 0.65 page

Take all \(d\)-th roots of unity modulo \(p\), choose sorted least positive
representatives, and add one common sufficiently large multiple of \(p\).
Prove order, residue-set preservation, positivity, and \(a_1+1>4d\).

#### §4.4 Congruence class and simultaneous large-\(b\) closure — 0.90 page

Use invertibility of \(d\bmod p\) to solve the congruence for \(b\).
Along that fixed class, prove \(R_0\downarrow1\), then satisfy \(b\ge2\),
\(R_0^2<2\), and all finitely many visibility inequalities with one choice.
Emphasize that the \(a_i\) were frozen first.

#### §4.5 Arithmetic boundaries — 0.45 page

Record why the construction includes \(d=2\) and why the later
\(4\mid d\) clause will follow from the same prime progression. Do not use
a numerical example as evidence.

### §5 Two-level chambers and exact polynomial-degree induction — 6.0 pages

- **Purpose:** carry the central burden of upgrading literal selected support
  weights to exact ordinary degrees of every polynomial iterate.
- **Inputs:** locked parameters, literal phase matrices, ordinary seed, and
  positive coefficients.
- **Outputs:** L5–L10 and the exact formula
  \(\deg(F^n)=e_1^{\mathsf T}C^n\mathbf1\).
- **Dependencies:** L3–L4; every subsection is theorem-critical.
- **Transition:** only after exact degree visibility is proved may §6 analyze
  the characteristic polynomial and §7 identify its Perron root with the
  dynamical degree.

Subsection allocation:

#### §5.1 Phase-labelled recursion target — 0.50 page

Define the start-of-step position vector, post-\(V\) momentum vector, and
post-\(W\) position vector. State the candidate update \(u_{n+1}=Cu_n\) as
an obligation, not yet a conclusion. List both carried blocks explicitly.

#### §5.2 Broad cone and strict spike selection — 0.80 page

Define
\[
\mathcal K_{\rm ratio}(R_0)
=\{u>0:\max_i u_i\le R_0\min_i u_i\}.
\]
Show seed membership and compare \(a_i u_i\) against
\(2\sum_j u_j-u_i\) using \(a_1+1>4d\) and \(R_0<\sqrt2\). Retain every
strict inequality.

#### §5.3 Strict broad-cone invariance and block domination — 1.00 page

For \(H=a^{\mathsf T}u\) and \(z_i=bH-a_iu_i\), prove positivity, denominator
positivity, and
\[
\frac{\max z_i}{\min z_i}
\le\frac1{1-MR_0/(bS_a)}<R_0.
\]
Separately derive
\[
(Cu)_i>\max_j a_ju_j>u_i.
\]
Do not conflate coordinatewise growth with the global cross-block
comparison.

#### §5.4 Fine visibility chamber — 1.00 page

Define
\[
\mathcal K_{\rm vis}(R_0)
=\{u>0:u_i\le u_1<R_0u_i,\ 
a_1u_1<a_iu_i\text{ for }i>1\}.
\]
Prove its inclusion in the broad cone, the tied seed's valid membership, and
all three output walls:
\[
w_i<w_1,\qquad w_1<R_0w_i,\qquad a_1w_1<a_iw_i.
\]
Keep the direction of the weighted inequality visible at each substitution.

#### §5.5 Both temporal carries — 1.00 page

At the first \(V\)-phase, compare \(a_i\) with the degree-one momentum seed.
At later \(V\)-phases, compare \(a_i u_{n,i}\) with
\(a_i u_{n-1,i}\). At every \(W\)-phase, compare \((Cu_n)_i\) with every
entry of \(Du_n\) and every carried position degree. Conclude exact phase
vectors only after all comparisons are strict.

#### §5.6 Positive-semiring leading-form survival — 0.75 page

Induct first in the nonnegative integer coefficient semiring. Explain why a
strictly larger source cannot cancel at addition, why products and powers of
nonzero top forms stay nonzero in a polynomial domain, and why
characteristic zero prevents positive derivative coefficients from
vanishing after base change. Do not invoke genericity.

#### §5.7 Exact fixed-\(q_1\) visibility — 0.95 page

Combine the chambers, carries, and top forms to prove
\[
u_n=C^n\mathbf1,\qquad
\deg(F^n)=e_1^{\mathsf T}u_n
\]
for every \(n\ge0\). State the tied identity seed and unique \(q_1\)
visibility only for positive iterates. End with a boxed exact ordinary-degree
identity and an explicit sentence that it is not merely a tropical upper
bound.

### §6 Characteristic polynomial and irreducibility — 3.0 pages

- **Purpose:** force degree-\(d\) rational irreducibility uniformly in \(d\).
- **Inputs:** locked rank-one form of \(C\), residue multiset, and congruence
  for \(b\).
- **Outputs:** L11–L12 and the exact minimal polynomial for the Perron root.
- **Dependencies:** L3 and L11; Heyman–Shparlinski supplies criterion
  provenance but not an unchecked conclusion.
- **Transition:** irreducibility and exact visibility are the two inputs that
  meet in §7.

Subsection allocation:

#### §6.1 Rank-one determinant and coefficient count — 0.80 page

Apply the matrix determinant lemma over \(\mathbb Q(t)\), then expand
\[
\prod_i(t+a_i)-b\sum_i a_i\prod_{j\ne i}(t+a_j).
\]
Count each \(k\)-fold squarefree product exactly \(k\) times and derive every
coefficient, including the constant term.

#### §6.2 Roots-of-unity reduction — 0.60 page

Compare coefficients of \(\prod_i(x-a_i)\equiv x^d-1\bmod p\). Derive the
vanishing intermediate elementary symmetric functions and the sign of
\(e_d(a)\), then use the locked \(b\)-congruence to obtain
\(\chi_C(t)\equiv t^d-c\).

#### §6.3 Full finite-field binomial criterion — 0.80 page

State all three conditions:

1. every prime divisor of \(d\) divides \(\operatorname{ord}(c)\);
2. the required quotient gcd is one; and
3. if \(4\mid d\), then \(p\equiv1\pmod4\).

Check them using \(\operatorname{ord}(c)=p-1\) and \(d\mid p-1\). A citation
to Heyman–Shparlinski Lemma 6 accompanies, but does not replace, these
checks.

#### §6.4 Boundary and rational lifting audit — 0.50 page

For \(d=2\), show a generator is a nonsquare. For \(4\mid d\), derive the
extra congruence. Use monicity, preservation of degree under reduction, and
Gauss's lemma to lift irreducibility to \(\mathbb Q\).

#### §6.5 Arithmetic output — 0.30 page

State clearly that \(\chi_C\) is the degree-\(d\) minimal polynomial of
every eigenvalue, including the Perron root. Do not claim novelty for the
binomial criterion.

### §7 Perron degree and exact scalar recurrence — 3.0 pages

- **Purpose:** distinguish and then connect matrix dimension, algebraic
  degree, dynamical degree, and scalar recurrence order.
- **Inputs:** exact degree identity, strict positivity of \(C\), and
  irreducibility of \(\chi_C\).
- **Outputs:** L13–L14 and the two exact complexity statements in Theorem H.
- **Dependencies:** L10–L12 plus standard Perron–Frobenius and
  Cayley–Hamilton results with hypotheses stated.
- **Transition:** §8 uses irreducibility once more to close rank sharpness,
  then states the precise scope of the complete result.

Subsection allocation:

#### §7.1 Perron projection and dynamical-degree limit — 0.75 page

Apply Perron–Frobenius to the strictly positive matrix. Display positive
left and right eigenvectors, strict spectral gap, and the positive visible
coefficient in
\[
e_1^{\mathsf T}C^n\mathbf1
=\gamma\rho(C)^n+O(\theta^n).
\]
Combine with §5, not with a citation alone, to prove
\(\lambda_1(F)=\rho(C)\).

#### §7.2 Exact Perron algebraic degree — 0.50 page

Use irreducibility of the monic degree-\(d\) characteristic polynomial to
identify the minimal polynomial of \(\rho(C)\). State the Perron algebraic
integer conclusion and degree exactly \(d\).

#### §7.3 Cayley–Hamilton upper bound — 0.35 page

Define rational constant-coefficient recurrence order precisely and derive
an order-at-most-\(d\) recurrence. Explicitly say this is not yet minimality.

#### §7.4 Reachability, observability, and Hankel rank — 0.85 page

Use Bézout with irreducible \(\chi_C\) to prove every nonzero state and
covector cyclic. Show both matrices are invertible and factor the
\(d\times d\) Hankel matrix as observability times reachability. Its rank
\(d\) excludes every smaller from-start recurrence.

#### §7.5 Eventual recurrence order — 0.45 page

Assume a lower-order tail recurrence, divide its Perron asymptotic by
\(\rho(C)^n\), and infer a polynomial of degree below \(d\) vanishes at
\(\rho(C)\), a contradiction. State both from-start and eventual order
exactly \(d\).

#### §7.6 Conceptual distinction — 0.10 page

One transition sentence records that size \(d\), algebraic degree \(d\), and
scalar order \(d\) are separately proved facts, not interchangeable
definitions.

### §8 Sharpness, positioning, limitations, and conclusion — 3.0 pages

- **Purpose:** join the two theorem branches, explain the bounded
  contribution boundary, and close without expansion.
- **Inputs:** Theorem S, irreducibility, selected presentations, citation
  map, and anti-claim ledger.
- **Outputs:** Corollary C, honest comparison, limitations, and concise
  conclusion.
- **Dependencies:** L15 and all context controls.
- **Transition:** none; the conclusion restates the all-\(d\) conjunction
  without introducing future claims.

Subsection allocation:

#### §8.1 Rank-\(d\) attainment — 0.90 page

Display the two \(-I+\) presentations, prove the stacked row rank is \(d\),
and use irreducibility to exclude a unit factor. State existential sharpness
for each constructed \(r=d\ge2\). Repeat that this does not cover rank zero,
rank one, every presentation, minimal dimension, or optimal sparsity.

#### §8.2 Positioning after subtraction — 0.75 page

Compare the complete conjunction with the eight public contextual records.
Internally ensure that fixed cubic, fixed quartic, isolated \(d=5\),
stationary selector-to-matrix grammar, common-kernel intuition, and
period-two selector mechanisms are not re-advertised. In public prose, omit
internal paper numbers, paths, review roles, scores, hashes, and governance.
Use only publication-safe references verified downstream.

#### §8.3 Limitations and open directions — 0.65 page

State the locked boundaries: positive displayed supports, characteristic
zero, forward ordinary degree, existential construction, and bounded
literature screen. Open directions may be phrased as questions about other
supports, inverse or higher dynamical degrees, or minimality, but the article
must say they are not established here.

#### §8.4 Conclusion — 0.70 page

Restate, in new wording, the exact visible all-\(d\) family, unbounded Perron
degree, exact scalar order, support-rank ceiling, and sharpness. End on the
structural lesson that literal support control and scalar observability are
both necessary. Add no new theorem, priority claim, or empirical promise.

## Citation-to-context plan

The source set is fixed at eight primary or authoritative records through
2026-08-26 UTC. No literature expansion occurs at the plan stage. Final
bibliographic fields and standard-theorem sources remain a downstream
pre-bibliography verification task.

| ID | Locked source | Permitted contextual role | Planned sections | Prohibited transfer |
|---|---|---|---|---|
| BvS | Jérémy Blanc and Immanuel van Santen, Dynamical degrees of affine-triangular automorphisms of affine spaces, arXiv:1912.01324, DOI 10.1017/etds.2021.90 | affine-triangular dynamical degrees, weak-Perron realization, matrix/valuation context | §1.2, §2.3, §8.2 | no claim that weak-Perron realization is new here; no theorem transfer |
| SS | Enbo Shao and Xiaosong Sun, Dynamical degrees of affine-triangular automorphisms in dimension four, arXiv:2509.14584 | dimension-four affine-triangular algebraic-degree context | §1.2, §8.2 | no arbitrary-\(d\) Hamiltonian conclusion |
| DF | Nguyen-Bac Dang and Charles Favre, Spectral interpretations of dynamical degrees and applications, Annals of Mathematics 194(1), 299–359 (2021), DOI 10.4007/annals.2021.194.1.5 | broad spectral and algebraicity context | §1.2, §2.3, §7 introduction | no replacement for exact visibility or the Perron limit proof |
| BT | Pierre Berger and Dmitry Turaev, arXiv:2210.14710 and DOI 10.1007/s11856-024-2709-7 | position/momentum shear generation and approximation context | §2.3 | no polynomial iterate-degree or rank-sharpness proof |
| KL | Hans Koch and Héctor E. Lomelí, On Hamiltonian flows whose orbits are straight lines, arXiv:1304.3377 | Hamiltonian shear and affine-integrable flow context | §2.3 | no cone, recurrence, or support-rank transfer |
| Des | Julie Déserti, Degree growth of polynomial automorphisms and birational maps: some examples, arXiv:1602.04642 | higher-dimensional degree-growth examples | §1.2, §8.2 | no exhaustive collision or absence inference |
| AX | Marc Abboud and Junyi Xie, Dynamical degrees of twisted rational maps, arXiv:2608.09275 | current twisted/relative rational-map context | §1.2, §8.2 | no statement about polynomial Hamiltonian product shears |
| HS | Randell Heyman and Igor E. Shparlinski, Counting irreducible binomials over finite fields, arXiv:1504.01172; Finite Fields and Their Applications 38, 1–12 (2016) | exact irreducible-binomial criterion, including the separate \(4\mid d\) clause | §6.3 | no novelty claim and no unchecked theorem-critical inference |

### Berger–Turaev title control

The arXiv metadata literally use **Generators of groups of Hamitonian maps**.
The authoritative version of record uses **Generators of Groups of
Hamiltonian Maps**. The later bibliography author must preserve this
source-specific distinction and must not silently normalize the arXiv title
into the journal title.

### Standard theorem citation queue

The manuscript will use the following named results, but no final source or
metadata is assigned at this gate:

- rectangular Sylvester determinant identity;
- matrix determinant lemma;
- Dirichlet's theorem on primes in arithmetic progressions;
- cyclicity of finite-field multiplicative groups;
- Gauss's lemma and the same-degree reduction criterion;
- Perron–Frobenius theorem for strictly positive matrices;
- Cayley–Hamilton theorem;
- standard reachability, observability, and Hankel-rank facts.

Before bibliography authoring, a separately authorized actor must verify a
reliable source and the exact hypotheses for every item. The article still
expands each theorem-critical application.

### Approved bounded noncollision wording

The only approved search conclusion is:

> No direct collision with the complete support-rank, sharp positive
> Hamiltonian, exact-visibility, and scalar-minimality package was found in
> the bounded primary-source screen through 2026-08-26 UTC.

Whenever used, it must be followed immediately by:

> The screen is bounded and nonexhaustive and does not establish firstness,
> uniqueness, or priority.

## Assumption ledger

| Assumption | First declaration | Exact proof use | Scope consequence |
|---|---|---|---|
| \(K\) is a field of characteristic zero | §2.1 and theorem statements | positive integer derivative coefficients remain nonzero; rational arithmetic and base change are valid | no positive-characteristic family theorem |
| \(d\ge2\) | Theorem H and §4.1 | nontrivial all-degree construction and binomial boundaries | no \(d=1\) construction claim |
| ordinary total degree | §2.1 | coordinate tuple maximum and exact visibility | no weighted-degree or higher-degree theorem |
| exact positive supports of \(V,W\) | §2.2 | selector comparisons and positive-semiring survival | no arbitrary sign/support/exponent extension |
| ordered positive \(a_1<\cdots<a_d\) | §4 | fine-chamber seed and visibility | ordering is not an order on \(\mathbb F_p\) |
| \(c\) has order exactly \(p-1\) | §4.2 | full binomial criterion | primitive never means merely nonzero |
| \(a_1+1>4d\) | §4.3 | broad-cone strict spike selection | required strict margin |
| \(b\) obeys the exact congruence | §4.4 | reduction to \(t^d-c\) | no arbitrary \(b\) claim |
| \(R_0=1+2M/(bS_a)\), \(R_0^2<2\) | §4.4 | broad invariance, denominator, carries, ratio walls | strict chamber is construction-specific |
| all visibility inequalities hold | §4.4 | fine weighted-wall invariance | one simultaneous large-\(b\) choice is essential |
| scalar recurrences have rational constant coefficients | §7.3 | Cayley–Hamilton and minimality | no variable-coefficient or nonlinear recurrence claim |

## Notation ledger

| Symbol | Meaning | Collision control |
|---|---|---|
| \(N\) | abstract ambient dimension in Theorem S | separate from construction parameter \(d\) and iterate index \(n\) |
| \(n\) | nonnegative iterate index in \(F^n\), \(u_n\), and \(s_n\) | never used for the abstract ambient dimension \(N\) |
| \(\alpha,\beta\) | factor widths in Theorem S | dimensions shown at first use |
| \(\mathsf P,\mathsf Q,\mathsf R,\mathsf S\) | abstract factor matrices | sans-serif; never reuse for scalar cone ratio |
| \(r\) | rank of the stacked selected row space | in Theorem H sharpness, specialize only to \(r=d\) |
| \(d\) | arbitrary construction degree and half-dimension | always quantified before \(p,c,a_i,b,R_0\) |
| \(p\) | prime congruent to one modulo \(d\) | never a momentum vector in arithmetic sections |
| \(c\) | generator of \(\mathbb F_p^\times\) | exact order \(p-1\) stated |
| \(a=(a_1,\ldots,a_d)^{\mathsf T}\) | ordered positive exponent vector | distinguish vector \(a\) from symmetric functions \(e_k(a)\) |
| \(S_a,M\) | \(\sum_i a_i\) and \(a_d\) | fixed before choosing \(b\) |
| \(R_0\) | scalar ratio \(1+2M/(bS_a)\) | this notation represents the lock's scalar \(R\) and avoids \(\mathsf R\) |
| \(J\) | \(\mathbf1\mathbf1^{\mathsf T}\) | define once |
| \(D,B_0,C\) | selected \(V\)-half-step, \(W\)-half-step, and complete-step matrices | \(B_0\) avoids collision with abstract \(B\) |
| \(u_n\) | position-degree vector at the start of the next \(V\)-phase | phase index fixed in §5.1 |
| \(s_n\) | \(e_1^{\mathsf T}C^n\mathbf1=\deg(F^n)\) | equality established only after §5.7 |
| \(\rho(C)\) | Perron spectral radius | identify with \(\lambda_1(F)\) only in §7.1 |
| \(\operatorname{LF}(G)\) | top-degree homogeneous form | used in positive-semiring proof |

## Anti-claim ledger

The public manuscript must not claim or imply:

1. exact unit-eigenvalue multiplicity \(N-r\), an exact rank-only spectral
   profile, or exclusion of extra \(t-1\) factors;
2. arbitrary signs, supports, exponent profiles, coefficients, added
   monomials, or shear words;
3. realization of every Perron algebraic integer or every weak-Perron number;
4. minimal ambient dimension, optimal sparsity, or a rank-zero or rank-one
   sharp Hamiltonian construction;
5. inverse-degree behavior, higher dynamical degrees, compactification,
   entropy equality, integrability, or arithmetic-orbit consequences;
6. selector periodicity, automata, genericity, classification, or
   nonconjugacy;
7. positive-characteristic validity of the Hamiltonian family theorem;
8. novelty from an isolated \(d=4\) or \(d=5\) case, the support-rank lemma
   alone, a fixed-dimensional example, or a standard theorem;
9. firstness, exclusivity, unprecedented status, exhaustiveness, or absolute
   priority;
10. a citation as proof of any factorization, selector, cone, carry,
    noncancellation, visibility, irreducibility, Perron-degree,
    scalar-minimality, or sharpness step;
11. numerical iteration, CAS, a parameter scan, a dataset, a plot, or a
    generated certificate as mathematical evidence; or
12. that rank sharpness holds for every presentation rather than
    existentially for the selected family.

## Proof-risk checklist

### Structural factorization

- [ ] All matrix dimensions are displayed and compatible.
- [ ] \(C-I_N\) is factored through the actual row span of
  \([\mathsf Q;\mathsf S]\).
- [ ] The Sylvester calculation is promoted to a polynomial identity before
  evaluating at \(t=1\).
- [ ] The reduced determinant is shown monic of degree \(r\).
- [ ] Unit multiplicity is phrased as at least \(N-r\).
- [ ] \(r=0\), \(r=N\), and extra unit roots are explicit.

### Parameters and literal maps

- [ ] Choices occur only in the order
  \(d\to p,c\to a_i\to b,R_0\).
- [ ] Primitive \(c\) means order \(p-1\).
- [ ] The residue multiset is exactly all \(d\)-th roots of unity.
- [ ] A common lift preserves strict ordering and achieves \(a_1+1>4d\).
- [ ] One \(b\) in one fixed congruence class satisfies all finite strict
  inequalities.
- [ ] Both potentials and their positive coefficients match the lock.
- [ ] Polynomial inverses and symplecticity are proved directly.
- [ ] \(D,B_0,C\) are derived from literal gradient monomials.

### Exact degree induction

- [ ] Broad and fine chambers are defined separately and nested correctly.
- [ ] The ordinary seed is permitted on coordinate-equality walls.
- [ ] Every spike beats the mixed \(V\)-competitor strictly.
- [ ] The broad cone maps into its strict interior.
- [ ] Every denominator is proved positive before multiplication.
- [ ] The global cross-block inequality is stronger than a componentwise
  growth statement.
- [ ] The fine chamber preserves coordinate, ratio, and weighted walls in the
  correct direction.
- [ ] The first \(V\)-carry and every later \(V\)-carry are both checked.
- [ ] Every \(W\)-phase checks old \(q\), current \(p\), and fresh \(q\)
  degrees.
- [ ] Positive-semiring survival is proved over characteristic zero without
  genericity.
- [ ] \(q_1\) visibility is unique only for \(n\ge1\).
- [ ] The conclusion is exact ordinary degree, not a tropical bound.

### Arithmetic and spectrum

- [ ] The factor \(k\) in each characteristic coefficient is counted.
- [ ] Signs in \(e_d(a)\) and the \(b\)-congruence are checked explicitly.
- [ ] Reduction keeps degree \(d\).
- [ ] All three binomial conditions are stated.
- [ ] \(d=2\) and \(4\mid d\) are audited separately.
- [ ] Gauss's lemma is applied only after monicity and degree preservation.
- [ ] Strict positivity, rather than nonnegativity alone, supports the Perron
  spectral gap.
- [ ] The visible Perron coefficient is shown positive.
- [ ] Matrix size, algebraic degree, and recurrence order are not conflated.
- [ ] Cayley–Hamilton is presented only as the upper bound.
- [ ] Reachability and observability are separately proved invertible.
- [ ] Hankel rank proves from-start minimality.
- [ ] Perron asymptotics prove eventual minimality.

### Sharpness, scope, and citations

- [ ] \(D+I_d\) is invertible and the stacked rank is exactly \(d\).
- [ ] Irreducibility excludes \(t-1\) for \(d\ge2\).
- [ ] Sharpness is existential and restricted to \(r=d\ge2\).
- [ ] All eight citations stay inside their contextual roles.
- [ ] Berger–Turaev's two title strings remain source-specific.
- [ ] Standard theorem sources are verified downstream rather than invented.
- [ ] The cutoff and nonexhaustive qualifier accompany any noncollision
  sentence.
- [ ] Public prose contains no internal project numbers, paths, hashes,
  review scores, agent roles, or governance vocabulary.
- [ ] Every anti-claim remains visible in theorem wording or limitations.

## Structural table and figure policy

This is a theory article with no empirical section.

| Item | Decision | Reason | Data source |
|---|---|---|---|
| Proof-map table in §1.5 | planned | materially clarifies four dependent proof branches for skim readers | manual theorem dependencies only |
| Compact notation table near §2.1 | conditional | include only if it prevents \(N/d/n\), \(B/B_0\), or \(\mathsf R/R_0\) collisions | manual definitions only |
| Related-context comparison table | conditional | prose is preferred; use a table only if contextual roles remain clearer without paper-by-paper listing | eight locked sources only |
| Hero figure | intentionally not planned | there is no empirical comparison, architecture, or geometric relation that a figure explains better than the proof map | none |
| Cone diagram | optional and default-off | add only after an independent source review finds the nesting hard to follow; it may illustrate definitions but never serve as proof | manual inequalities only |
| Plot, benchmark, ablation, dataset, or result figure | forbidden | no empirical claim or authorized computation exists | none |

Any later structural figure requires separate authorization and must be
vector-based, anonymous, accessible in grayscale, and self-contained. No
figure is necessary for the plan or proof.

## No-empirical-section declaration

The article contains no Experiments, Evaluation, Results, Ablation, Dataset,
Implementation, or Numerical Validation section. The source-design directory
name experiments refers only to adversarial symbolic proof checks and must
not leak into the public manuscript. A finite example, if a later reviewer
requests one, may only illustrate a theorem already proved for every \(d\);
it would require separate authorization and could not count as evidence.

## Expected anonymous public wording

### Headline wording

> For every integer \(d\ge2\), we construct an explicit positive Hamiltonian
> product shear whose ordinary iterate degrees are exactly visible through a
> positive \(d\times d\) matrix, whose Perron dynamical degree has algebraic
> degree \(d\), and whose scalar degree sequence has minimal rational
> recurrence order \(d\). A selected support-row rank factorization bounds
> the nonunit characteristic degree, and the construction attains that bound
> for every constructed rank \(d\ge2\).

### Structural-bound wording

> The factorization forces unit multiplicity at least \(N-r\), but the
> reduced factor may contain additional unit roots; rank alone does not
> determine the exact spectral profile.

### Literature wording

> The construction is positioned within affine-triangular dynamical-degree,
> spectral, Hamiltonian-shear, and higher-dimensional degree-growth
> literatures. The cited results provide context and standard tools; the
> selector, carry, visibility, and scalar-minimality arguments are proved
> directly here.

### Anonymous-submission controls

- Use no author names, affiliations, grant identifiers, acknowledgments,
  personal URLs, self-identifying repositories, or identity-bearing
  metadata.
- Do not mention Papers 20–24, the batch, local file paths, internal reviews,
  hashes, scores, source locks, gates, agents, or unpublished governance.
- Do not write “our earlier paper” unless a publication-safe reference is
  later verified and anonymization policy permits it.
- Use neutral forward references such as “Section 5 proves” and public
  citations only after bibliography verification.
- Keep local portfolio subtraction as an internal drafting constraint, not a
  public literature claim.

## Exact future manuscript-source architecture

If and only if later publication governance and source authoring are
separately opened, the intended manuscript source universe is exactly:

1. paper/main.tex
   - anonymous article front matter;
   - Abstract and §§1–8;
   - every theorem statement, proof, table, limitation, and conclusion;
   - no included section files and no generated content.
2. paper/math_commands.tex
   - notation macros only;
   - no prose, claims, bibliography data, or hidden proof text.
3. paper/references.bib
   - only independently verified bibliography records;
   - all eight locked contextual sources and later verified standard-theorem
     sources;
   - Berger–Turaev title fields kept source-specific.

These three files do not yet exist and are not authorized by this plan.
No section file, style file, figure file, code file, data file, build file,
or alternative bibliography is part of the intended source architecture.
Writing, bibliography, compilation, PDF, and release permissions remain
closed until separate parent-controlled transitions.

## Planned review checklist

The later independent plan reviewer should verify, without editing this plan:

- [ ] exact title and reader promise match the frozen lock;
- [ ] the all-\(d\) conjunction is the headline;
- [ ] page allocations sum exactly to 26.0;
- [ ] every section has purpose, inputs, outputs, dependencies, and a
  transition;
- [ ] all L1–L15 proof units have a main-text home;
- [ ] no theorem-critical proof is relegated to citation or appendix;
- [ ] support rank is lower-bound-only for unit multiplicity;
- [ ] parameter quantifiers are noncircular;
- [ ] symplecticity and literal supports are proved directly;
- [ ] broad and fine chambers retain distinct roles;
- [ ] both temporal carries and positive-semiring survival are explicit;
- [ ] exact \(q_1\) visibility includes the tied seed boundary;
- [ ] characteristic arithmetic includes the factor \(k\), \(d=2\), and
  \(4\mid d\);
- [ ] Perron degree and both scalar-order versions are separately proved;
- [ ] rank sharpness is existential for \(r=d\ge2\);
- [ ] \(r=0\), \(r=N\), extra unit roots, and characteristic zero are visible;
- [ ] all eight source roles and the 2026-08-26 cutoff are preserved;
- [ ] Berger–Turaev title strings are not conflated;
- [ ] standard theorem bibliography work remains pending;
- [ ] no empirical section, invented datum, benchmark, result, or forced
  figure appears;
- [ ] public wording is anonymous and omits internal governance;
- [ ] the only future source paths are the exact three-file architecture;
- [ ] no downstream permission is inferred from plan completeness.

The later manuscript reviewer should additionally verify:

- [ ] theorem statements, contribution bullets, Abstract, and Conclusion
  make the same conjunction;
- [ ] notation never drifts from the ledger;
- [ ] every strict inequality remains strict in source;
- [ ] every claim maps to an internal proof or bounded contextual citation;
- [ ] all citation metadata and theorem numbers were verified rather than
  generated from memory;
- [ ] no appendix contains a theorem-critical gap left out of the main text;
- [ ] no internal path, identity, review record, or governance term appears
  in public source;
- [ ] limitations match the anti-claim ledger;
- [ ] source universe, build, and release actions follow only their later
  explicit authorizations.

## Plan-stage completeness disposition

The plan closes the article narrative at 26.0 content pages, places every
frozen theorem and boundary in the main text, maps every claim to symbolic
evidence, confines all eight citations to context, and leaves the exact
future source trio unopened. It introduces no experiment, datum, fixed-case
headline, new theorem, bibliography record, source file, build action,
publication action, successor-paper action, or external effect.

PAPER PLAN R1 AUTHOR STOP
