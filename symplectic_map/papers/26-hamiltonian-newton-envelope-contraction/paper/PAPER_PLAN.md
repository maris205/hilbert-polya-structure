# Paper 26 Proof-First Paper Plan

## Frozen identity and planning status

**Exact title:** Newton-Envelope Contraction for Planar Hamiltonian Product Shears: Selector Rigidity and Bidirectional Degree Growth

**Candidate identifier:** planar_newton_envelope_bidirectional_degree_v1

**Article type:** anonymous, proof-first theory article.

**Future visible author:** Anonymous.

**Future visible date:** empty.

**Future PDF metadata:** the PDF Title must equal the exact title; Author, Creator, Producer, Subject, and Keywords must all be empty. No affiliation, acknowledgment, grant identifier, identity-bearing link, private path, review role, hash, gate, or local-project datum may enter source comments, rendered text, bookmarks, metadata, attachments, or bibliography fields.

**Venue status:** no venue is selected by this plan. Venue-specific formatting and submission statements remain unresolved and cannot change the theorem or page architecture.

**Page contract:** 22--30 mathematical content pages from front matter through the end of Section 9, excluding references. The center budget is exactly 26.0 pages. There is no appendix, hidden supplement, empirical section, or theorem-critical material outside the numbered body.

**Evidence status:** every promoted mathematical claim is supported by the frozen symbolic proof package and its independent reviews. The two fixtures are exact hand calculations, not numerical or CAS evidence. Global novelty and final primary-record citation verification remain unresolved.

**Current authority boundary:** this file is a manuscript plan only. It does not authorize LaTeX, bibliography authoring, figures, code, data, computation, compilation, a PDF, a build root, release, submission, external messaging, or a successor gate.

## Reader promise and narrative spine

### One-sentence contribution

For planar Hamiltonian product shears with arbitrary finite collected support in \(\mathbf Z_{\ge2}^{2}\) and a separated pure-power momentum Hamiltonian, the article proves coefficient-uniform full-face cancellation control, exact forward and inverse ordinary-degree transport, a shifted vector bridge, and global Newton-envelope log contraction, which together force interior stationarity or wall-convergent selector alternation and a uniform quadratic arithmetic bound, with an integer first dynamical degree on walls.

### What, why, and so what

- **What:** establish one cancellation-safe theorem for every finite nonempty collected \(E\subset\mathbf Z_{\ge2}^{2}\), every nonzero coefficient choice over a characteristic-zero field, and every separated momentum potential with derivative exponents \(e,f\ge2\).
- **Why it is hard:** a max-plus envelope is only an upper bound until top-form cancellation is excluded on every multi-point exposed face; forward and inverse maps use opposite phase orders; a decreasing piecewise projective map may alternate selector labels indefinitely even while its numerical orbit converges.
- **So what:** the arbitrary finite Newton support collapses projectively to one fixed ray, selector tails admit a complete interior/wall classification, forward and inverse exponential rates agree by an exact vector identity, and the first dynamical degree never has algebraic degree above two in this family.

### Contribution order

The Introduction must present the contributions in this order:

1. a coefficient-uniform exposed-face Hessian certificate and full-face algebraic-independence argument;
2. explicit cancellation-free forward and inverse half-step carries, visible degree blocks, and the shifted vector bridge;
3. a support-uniform logarithmic contraction patched across all Newton walls;
4. the interior/wall selector classification and its arithmetic consequences;
5. separately proved forward and inverse scalar recurrence upper bounds.

The recurrence laws, two-step monodromy, and fixtures are consequences. They must not displace the first four items in the title, abstract, opening paragraphs, or contribution bullets.

## Claims--evidence backbone

This prose matrix replaces a manuscript planning table. The future manuscript has exactly one structural table, specified later.

### CE-1: symplectic structure and inverse order

- **Frozen claims:** C01--C02.
- **Manuscript location:** Section 2.
- **Evidence:** direct block multiplication with the standard symplectic matrix; explicit subtraction shears; \(F^{-1}=S^{-1}\circ T^{-1}\), so \(T^{-1}\) acts first.
- **Status:** proved.
- **Kill condition:** any surviving skew-Hessian block, sign error, or use of the forward phase order for the inverse.

### CE-2: full-face cancellation certificate

- **Frozen claims:** C03--C08.
- **Manuscript location:** Section 3.
- **Evidence:** unique minimal-first-coordinate face point; isolated coefficient in the face-Hessian determinant; characteristic-zero Jacobian criterion; injective substitution; invariance under nonzero scalars, signs, and separated pure powers.
- **Status:** proved for one-point and arbitrary multi-point positive exposed faces and for all nonzero collected coefficients.
- **Kill condition:** a distinct exponent pair contributes to the witness coefficient, the coefficient can vanish in scope, a tied face is replaced by one monomial, or a leading pair is assumed independent without proof.

### CE-3: exact degree states, visibility, and bridge

- **Frozen claims:** C09--C14.
- **Manuscript location:** Section 4.
- **Evidence:** all four carry inequalities, including the cross-coordinate inequalities corresponding to frozen equations (6.3)--(6.4); explicit forward and reverse half-step inductions; positive homogeneity and the ordinary seed.
- **Status:** proved.
- **Kill condition:** a fresh block does not dominate every carried block, the inverse signs or order are suppressed, the bridge loses its shift or diagonal factor, or vector/rate comparison is promoted to scalar termwise equality.

### CE-4: projective contraction and inverse conjugacy

- **Frozen claims:** C15--C18 and C20.
- **Manuscript location:** Section 5.
- **Evidence:** exact \(\Phi,\phi,\psi\) formulas; negative chamber derivative; strict logarithmic denominator gap; endpoint decay; finite-support maximum \(q<1\); continuous wall patching; \(L\circ\psi=\phi\circ L\).
- **Status:** proved.
- **Kill condition:** only pointwise slope control is shown, the branch supremum reaches one, wall patching is omitted, or inverse selectors are evaluated at \(s\) instead of the Newton coordinate \(\kappa s\).

### CE-5: selector and spectral rigidity

- **Frozen claims:** C19 and C21--C23.
- **Manuscript location:** Section 6.
- **Evidence:** decreasing injective contraction; no delayed landing; two adjacent extreme exponents off a multiple tie and the full face on it; positive integral chamber matrices; primitive rational wall ray and common multiplier.
- **Status:** proved.
- **Kill condition:** an in-scope selector tail is not classified, selector alternation is called a numerical two-cycle, or an in-scope wall multiplier is not integral.

### CE-6: scalar recurrence consequences

- **Frozen claim:** C24.
- **Manuscript location:** Section 7.
- **Evidence:** forward matrices \(C_\xi\); separately derived inverse matrices \(D_\xi=A_\xi B=B^{-1}C_\xi B\); stable visible coordinates; the \(s_\star=1\) ordinary-seed case; fixed-wall and strict-wall cases; both \(M_\pm\) and \(N_\pm\); common trace and determinant.
- **Status:** proved as eventual upper bounds.
- **Kill condition:** the bridge is used as the inverse scalar proof, matrix order or selector coordinate is wrong, a visible maximum is not stabilized on each parity, or minimality is asserted.

### CE-7: exact fixtures and boundaries

- **Frozen evidence:** F01--F03 and B01--B04, together with the complete anti-claim register.
- **Manuscript location:** Section 8.
- **Evidence:** exact integer and rational arithmetic from the proof package; explicit failure mechanisms for axes, exponent one, mixed \(W\), positive characteristic, uncollected support, and altered seed or phase order.
- **Status:** cross-checked or boundary-frozen.
- **Kill condition:** a fixture is presented as computational evidence, an integer differs, or an excluded regime is described as covered.

## Precise main theorem contract

The formal Main Theorem must appear at the end of Section 3, after the exposed-face Hessian and cancellation proposition has been stated and proved. The Abstract and Section 1 may preview its consequences in prose, but no exact degree recursion may be derived before the full-face certificate.

### Hypotheses

Let \(K\) have characteristic zero. Let \(E\subset\mathbf Z_{\ge2}^{2}\) be finite, nonempty, and collected, and let every \(c_{x,y}\) for \((x,y)\in E\) be nonzero, with no positivity or common-sign assumption. Define
\[
V(q_1,q_2)=\sum_{(x,y)\in E}c_{x,y}q_1^xq_2^y
\]
and
\[
W(p_1,p_2)=\alpha p_1^{e+1}+\beta p_2^{f+1},
\qquad e,f\ge2,\quad\alpha\beta\ne0.
\]
With
\[
S(q,p)=(q,p+\nabla V(q)),\qquad
T(q,p)=(q+\nabla W(p),p),
\]
fix \(F=T\circ S\). Degrees are ordinary total degrees in the four initial coordinates. The forward and inverse degree seeds are both \(\mathbf1=(1,1)^\top\).

For \(u>0\), define
\[
H(u)=\max_{(x,y)\in E}(xu_1+yu_2),\qquad
\mathcal A(u)=\bigl(H(u)-u_1,H(u)-u_2\bigr)^\top,
\qquad
B=\operatorname{diag}(e,f).
\]

### Dependency-ordered conclusions

The theorem statement must list its conclusions in the following order.

1. **Structure and cancellation.** \(F\) is a polynomial symplectomorphism, \(F^{-1}=S^{-1}\circ T^{-1}\), and full exposed-face leading pairs survive every forward and inverse half-step, including subtraction phases and multiple ties.
2. **Exact vector transports and visible ordinary degrees.** For
   \[
   u_0^+=v_0^-=\mathbf1,
   \]
   \[
   u_{n+1}^+=B\mathcal A(u_n^+),\qquad
   v_{n+1}^-=\mathcal A(Bv_n^-),
   \]
   and
   \[
   \deg(F^n)=\|u_n^+\|_\infty,\qquad
   \deg(F^{-n})=\|v_n^-\|_\infty.
   \]
3. **Shifted vector bridge.** With \(c_\star=H(\mathbf1)-1\),
   \[
   u_{n+1}^+=c_\star Bv_n^-\qquad(n\ge0).
   \]
   Consequently the forward and inverse degree sequences are comparable up to fixed positive constants and one index shift, and
   \[
   \lambda_1(F)=\lambda_1(F^{-1}).
   \]
   This clause must explicitly deny termwise scalar equality and scalar-recurrence transfer.
4. **Uniform projective contraction.** The forward ratio map is globally contractive in logarithmic distance, the inverse ratio map is its scaling conjugate, and each has one fixed ray and no nontrivial numerical periodic orbit.
5. **Selector and arithmetic classification.** An interior fixed ray gives an eventually stationary selector; a wall fixed ray gives the full tied face on the fixed orbit and adjacent-selector alternation on every strict orbit while the ratios converge to the wall. Interior values have algebraic degree at most two; wall values are positive integers. Thus
   \[
   [\mathbf Q(\lambda_1(F)):\mathbf Q]\le2.
   \]
6. **Scalar recurrence consequences.** Forward and inverse interior degree tails have order at most two, strict wall-alternating tails have order at most four, and fixed-ray tails are geometric. The inverse claims are proved independently from \(D_\xi\), the selector coordinate \(\kappa s\), the \(s_\star=1\) and \(s_\star\ne1\) cases, and both parity products.

The main theorem must not include global priority, genericity, recurrence minimality, higher dynamical degrees, entropy, compactification, integrability, orbit arithmetic, or a classification of polynomial symplectomorphisms.

## Forward-only theorem dependency DAG

The manuscript must state this dependency chain as a compact numbered list, not as a second table or a figure.

1. Symmetric Hessian blocks imply symplecticity; reverse subtraction phases fix the inverse order.
2. A positive exposed face has a unique minimal-\(x\) support point.
3. That point isolates a nonzero coefficient in the full face-Hessian determinant.
4. The Jacobian criterion gives algebraic independence of the face-gradient pair.
5. Injective substitution, nonzero scalars, signs, and separated powers preserve the leading pair.
6. The carry inequalities identify the exact fresh vectors and visible coordinate blocks in both time directions.
7. Positive homogeneity and the ordinary seed give the shifted bridge and rate equality.
8. Exact forward transport yields the projective envelope map.
9. The branch derivative, positive gap, endpoint limits, finite support, and wall splitting give one global log-contraction constant.
10. The fixed ray gives the selector dichotomy.
11. Interior chamber matrices and the common primitive wall ray give the quadratic/integer spectral dichotomy.
12. Cayley--Hamilton, separately for forward and inverse states and both wall parities, gives scalar recurrence upper bounds.
13. The two fixtures check both terminal regimes with exact arithmetic.

No later node may be cited to prove an earlier node. In particular, the fixtures do not establish the theorem, the bridge does not establish inverse scalar recurrences, and a two-step monodromy does not establish the contraction.

## Exact page ledger

The content allocation is immutable at the plan stage:

1. Front matter and Abstract: **0.75 page**.
2. Section 1, Introduction, local related work, and contributions: **2.25 pages**.
3. Section 2, setting, symplecticity, and inverse phases: **1.50 pages**.
4. Section 3, full exposed-face Hessian and cancellation: **3.00 pages**.
5. Section 4, exact forward/inverse transports and bridge: **4.25 pages**.
6. Section 5, uniform logarithmic contraction: **3.75 pages**.
7. Section 6, selector and spectral rigidity: **3.50 pages**.
8. Section 7, forward and inverse scalar recurrences: **4.00 pages**.
9. Section 8, exact fixtures, scope, and collision subtraction: **2.50 pages**.
10. Section 9, conclusion: **0.50 page**.

The arithmetic is
\[
0.75+2.25+1.50+3.00+4.25+3.75+3.50+4.00+2.50+0.50=26.00.
\]
The four technical core sections satisfy
\[
\S4+\S5+\S6+\S7=4.25+3.75+3.50+4.00=15.50.
\]
References begin only after Section 9 and are outside the 26.0-page content count.

## Section-by-section manuscript architecture

### Front matter and Abstract -- 0.75 page

**Purpose:** let a reader identify the exact family, obstacle, proof mechanism, and arithmetic conclusion before reaching the technical sections.

**Planned mass:**

- title and anonymous/empty-date front matter: 0.10 page;
- Abstract: 0.65 page.

**Abstract sequence:**

1. name the planar product-shear family and exact support restrictions;
2. explain that Newton-envelope degrees are only predictions until full-face cancellation is excluded;
3. state the face-Hessian certificate, exact bidirectional transports, and shifted bridge;
4. state global log contraction and the interior/wall selector classification;
5. close with equal forward/inverse exponential rates, the quadratic cap, and wall integrality.

The Abstract contains no citation, no global novelty adjective, no period-two construction claim, no recurrence-minimality language, and no reference to experiments.

**Output:** a self-contained theoretical reader promise.

**Transition:** the Introduction explains why the conjunction, rather than any one standard tool, is needed.

### Section 1 -- Introduction, local related work, and contributions -- 2.25 pages

**Purpose:** establish the What/Why/So What, synthesize the locally verified context, and state bounded contribution bullets without a global novelty claim.

**Subsection and page allocation:**

- **1.1 Degree growth as an exact polynomial problem -- 0.45 page.** Motivate ordinary degree growth and the first dynamical degree, then isolate the difference between a tropical upper bound and an exact polynomial result.
- **1.2 The three coupled obstacles -- 0.45 page.** Explain tied-face cancellation, opposite forward/inverse phase order, and persistent selector switching.
- **1.3 Local related-work synthesis -- 0.70 page.** Organize by degree/dynamical-degree context, tropical/symplectic recurrences, and structured polynomial symplectomorphisms; state that every comparison is contextual and requires later primary-record rechecking.
- **1.4 Contributions and proof roadmap -- 0.65 page.** Give five contribution bullets in the frozen order and one compact dependency roadmap. Recurrences and fixtures appear only after the main mechanisms.

**Inputs:** exact title, safe local novelty wording, citation ledger, and Paper 24/Paper 25 collision map.

**Outputs:** one story centered on arbitrary-face exactness plus contraction, not a list of matrix consequences.

**Citation placement:** only the locally complete planning slots listed in the citation section below. Citations support context, never theorem steps.

**Anti-claim placement:** the final paragraph states that global novelty, final metadata, genericity, arbitrary Hamiltonian shears, and higher-dimensional classification are not claimed.

**Transition:** Section 2 freezes the literal map, phase order, ordinary degree, and theorem hypotheses.

### Section 2 -- Setting, symplecticity, and inverse phases -- 1.50 pages

**Purpose:** eliminate ambiguity about the polynomial map and the order in which inverse phases act.

**Subsection and page allocation:**

- **2.1 Map class, collected support, and ordinary degree -- 0.45 page.** Define \(K,E,V,W,S,T,F\), the coordinate order, the nonzero-coefficient rule, and the ordinary seed.
- **2.2 Symplectic block calculation -- 0.35 page.** State and prove Proposition 2.1 using the symmetric Hessian blocks and the standard symplectic matrix.
- **2.3 Subtraction inverses and phase chronology -- 0.30 page.** Display \(S^{-1},T^{-1}\), record \(F^{-1}=S^{-1}\circ T^{-1}\), and say explicitly that \(T^{-1}\) acts first.
- **2.4 Support function and theorem staging -- 0.40 page.** Define \(H,\mathcal A,B\), ordinary total degrees, and the seed. Preview the theorem conclusions without deriving a degree recursion. Explain that the precise Main Theorem is delayed until the full-face cancellation proposition at the end of Section 3.

**Formal statement placement:** Proposition 2.1, Symplecticity and inverse order.

**Inputs:** CE-1 and the theorem hypotheses.

**Outputs:** literal maps, inverses, and phase chronology needed by both half-step inductions.

**Proof dependency:** this section uses no degree-growth conclusion.

**Transition:** the Newton envelope can be trusted only after Section 3 proves that every exposed face survives.

### Section 3 -- Full exposed-face Hessian and cancellation -- 3.00 pages

**Purpose:** turn the Newton-envelope prediction into a coefficient-uniform polynomial theorem before any recurrence is used.

**Subsection and page allocation:**

- **3.1 Positive exposed support and full face polynomial -- 0.30 page.** Define \(E_u\) and \(P_u\); state that every tied term is retained.
- **3.2 Unique minimal first coordinate -- 0.35 page.** State and prove Lemma 3.1 from positivity of the exposing weight.
- **3.3 The isolated face-Hessian coefficient -- 0.75 page.** State and prove Lemma 3.2. Track both Hessian products and rule out every distinct support pair at \(X^{2x_0-2}Y^{2y_0-2}\).
- **3.4 Jacobian independence -- 0.40 page.** State Lemma 3.3 and give the characteristic-zero differential proof needed for the face-gradient pair.
- **3.5 Injective substitution and pure-power survival -- 0.65 page.** State Lemmas 3.4--3.5 and Proposition 3.6. Cover nonzero scalars, signs, separated powers, arbitrary multi-point ties, and the forward and inverse subtraction phases.
- **3.6 Dependency-ordered Main Theorem -- 0.55 page.** State the precise theorem under all frozen hypotheses, with cancellation before exact transports, bridge, contraction, classification, spectrum, and recurrence consequences.

**Formal statement placement:**

- Lemma 3.1, Unique minimal-\(x\) point.
- Lemma 3.2, Nonzero full-face Hessian determinant.
- Lemma 3.3, Characteristic-zero Jacobian criterion in the required two-variable form.
- Lemma 3.4, Injective substitution.
- Lemma 3.5, Separated powers, scalars, and signs preserve independence.
- Proposition 3.6, Full-face leading-pair survival.
- Theorem 3.7, Main Theorem.

**Inputs:** map and support hypotheses from Section 2.

**Outputs:** an exact noncancellation certificate usable at every forward and inverse half-step.

**Required proof details:**

- coefficient nonvanishing uses collected \(c_{x_0,y_0}\ne0\), \(x_0,y_0\ge2\), and characteristic zero separately;
- coefficient positivity is never assumed;
- a multiple tie is treated by the whole \(P_u\);
- generic coefficients are neither required nor permitted as a replacement.

**Citation rule:** no research citation is a proof dependency. If no separately verified authoritative standard reference is available later, the short Jacobian-criterion proof remains in the body.

**Transition:** with top forms now certified, Section 4 may derive exact degree states and visible ordinary degrees.

### Section 4 -- Exact forward/inverse transports and bridge -- 4.25 pages

**Purpose:** prove every half-step carry, identify the visible block of the four-coordinate map, and separate the shifted vector bridge from scalar recurrence claims.

**Subsection and page allocation:**

- **4.1 Weighted gradient transform -- 0.45 page.** Derive the exact degrees \(H(u)-u_1,H(u)-u_2\) and their full-face leading forms.
- **4.2 Lower carry inequalities -- 0.35 page.** Prove
  \[
  H(u)-u_1\ge u_1+2u_2,\qquad
  H(u)-u_2\ge2u_1+u_2.
  \]
- **4.3 Cross-coordinate upper carry -- 0.40 page.** With \(A=\mathcal A(u)\), reproduce
  \[
  2A_1-A_2=H-2u_1+u_2\ge3u_2>0,
  \]
  \[
  2A_2-A_1=H+u_1-2u_2\ge3u_1>0,
  \]
  and only then use \(e,f\ge2\) to prove that both components of \(BA\) dominate both components of \(A\).
- **4.4 Forward half-step induction -- 0.75 page.** Track the old position and momentum blocks, the fresh momentum vector, pure-power position vector, algebraic independence, and final visible position block.
- **4.5 Inverse half-step induction -- 0.85 page.** Track \(T^{-1}\) first, then \(S^{-1}\); keep subtraction signs; prove the fresh position and final momentum carries independently; name the visible block.
- **4.6 Exact vector states and total degrees -- 0.45 page.** State Propositions 4.2--4.3:
  \[
  u_{n+1}^+=B\mathcal A(u_n^+),\qquad
  v_{n+1}^-=\mathcal A(Bv_n^-),
  \]
  together with the two maximum formulas.
- **4.7 Shifted bridge induction -- 0.55 page.** Prove the \(n=0\) base case from \(\mathcal A(\mathbf1)=c_\star\mathbf1\), then the homogeneous induction
  \[
  u_{n+1}^+=c_\star Bv_n^-.
  \]
- **4.8 Norm comparison and exact boundary -- 0.45 page.** Deduce the two-sided constant-factor comparison and equality of exponential rates. State in the proposition and surrounding prose that the bridge gives neither termwise scalar equality nor the inverse scalar recurrence.

**Formal statement placement:**

- Lemma 4.1, Exact gradient degrees and four carry inequalities.
- Proposition 4.2, Forward top forms, transport, and position visibility.
- Proposition 4.3, Inverse top forms, transport, and momentum visibility.
- Proposition 4.4, Shifted forward--inverse vector bridge.
- Corollary 4.5, Equality of first dynamical degrees.

**Inputs:** Proposition 3.6 and all Section 2 phase conventions.

**Outputs:** exact polynomial degree states and the only permitted forward--inverse bridge statement.

**Notation introduced here:** \(w_{n+1}^+\) for the forward intermediate momentum-degree vector, \(u_n^+\) for the full forward position state, \(z_{n+1}^-\) for the inverse intermediate position vector, \(v_n^-\) for the full inverse momentum state, and \(d_n^\pm\) for scalar ordinary degrees.

**Anti-claim placement:** the bridge boundary is stated once in Proposition 4.4, once in Corollary 4.5, and once in the Section 4 transition; it is not left only to limitations.

**Transition:** exact forward transport can now be projectivized without a hidden cancellation assumption.

### Section 5 -- Uniform logarithmic contraction -- 3.75 pages

**Purpose:** upgrade chamberwise monotonicity to one global contraction on all positive rays and transfer it correctly to inverse selector coordinates.

**Subsection and page allocation:**

- **5.1 Projective support function and ratio map -- 0.45 page.** Introduce
  \[
  \Phi(r)=\max_E(xr+y),\qquad
  \kappa=e/f,\qquad
  \phi(r)=\kappa\frac{\Phi(r)-r}{\Phi(r)-1}.
  \]
- **5.2 Chamber derivative and monotonicity -- 0.45 page.** Derive the fractional-linear branch and its strictly negative derivative.
- **5.3 Logarithmic derivative and positive gap -- 0.65 page.** Introduce \(t=\log r\), \(h(t)=\log\phi(e^t)\), and
  \[
  \eta_{x,y}(r)
  =\frac{r(x+y-1)}
  {((x-1)r+y)(xr+y-1)}.
  \]
  Expand the denominator gap exactly and prove it positive.
- **5.4 Endpoint compactification for one branch -- 0.55 page.** Prove \(\eta_{x,y}(r)\to0\) at both endpoints and that its branch maximum is strictly below one.
- **5.5 Finite-support uniformity -- 0.35 page.** Take the maximum of finitely many branch constants to obtain one \(q<1\).
- **5.6 Wall patching -- 0.55 page.** Partition any log interval at the finitely many walls, integrate branch bounds, and reassemble by continuity. A pointwise derivative statement alone is insufficient.
- **5.7 Inverse map and scaled selector -- 0.40 page.** Define
  \[
  \psi(s)=\frac{\Phi(\kappa s)-\kappa s}{\Phi(\kappa s)-1},
  \qquad L(s)=\kappa s,
  \]
  prove \(L\circ\psi=\phi\circ L\), and state that inverse chamber selection uses \(\kappa s\).
- **5.8 Fixed point and numerical-cycle exclusion -- 0.35 page.** Apply completeness of log space to obtain one fixed ray and rule out every nontrivial numerical periodic orbit.

**Formal statement placement:**

- Proposition 5.1, Exact forward and inverse projective formulas and conjugacy.
- Lemma 5.2, Chamber logarithmic derivative and positive gap.
- Theorem 5.3, Finite-envelope uniform log contraction across walls.
- Corollary 5.4, Unique fixed ray, global convergence, and no nontrivial numerical cycle.

**Inputs:** exact transport from Section 4.

**Outputs:** one fixed forward ray \(r_\star\), inverse fixed ratio \(s_\star=r_\star/\kappa\), and global convergence.

**Anti-claim placement:** explicitly say that the proof uses finite \(E\), a one-dimensional projective chart, and diagonal \(B\); it does not cover infinite support, mixed \(W\), or dimension at least three.

**Transition:** the location of the unique fixed ray now classifies selectors and determines the arithmetic tail.

### Section 6 -- Selector and spectral rigidity -- 3.50 pages

**Purpose:** turn contraction into an exhaustive selector classification and then into the quadratic/interior versus integral/wall spectral dichotomy.

**Subsection and page allocation:**

- **6.1 Interior fixed ray -- 0.45 page.** Use positive distance from the wall set to prove eventual selector stationarity.
- **6.2 Wall fixed and strict trajectories -- 0.85 page.** Separate the fixed trajectory from strict trajectories; prove side swapping, adjacent-chamber alternation, convergence, no delayed landing, and the full-face/multiple-tie rule.
- **6.3 Selector alternation is not a numerical two-cycle -- 0.30 page.** State the distinction as a proposition consequence, not only as terminology.
- **6.4 Interior selector matrix and spectrum -- 0.55 page.** Define
  \[
  A_\xi=\begin{pmatrix}x-1&y\\x&y-1\end{pmatrix},
  \qquad C_\xi=BA_\xi,
  \]
  identify the positive fixed ray as the Perron ray, and obtain algebraic degree at most two.
- **6.5 Primitive wall ray and common multiplier -- 0.75 page.** Use a primitive positive integral direction \(\boldsymbol\omega\) to prove that every tied exponent gives the same \(A_\xi\boldsymbol\omega\) and hence
  \[
  C_-\boldsymbol\omega=C_+\boldsymbol\omega=\mu\boldsymbol\omega.
  \]
- **6.6 Integrality and per-step growth -- 0.40 page.** Prove \(\mu\in\mathbf Z_{>0}\), identify two-step Perron root \(\mu^2\), and conclude the uniform quadratic cap.
- **6.7 Structural Table 1 -- 0.20 page.** Place the sole manuscript table and use it to summarize mechanisms and boundaries without numerical results.

**Formal statement placement:**

- Proposition 6.1, Interior/wall selector dichotomy, including multiple ties.
- Proposition 6.2, Interior Perron spectrum.
- Proposition 6.3, Common primitive wall ray and integral multiplier.
- Corollary 6.4, Uniform algebraic-degree bound.

**Inputs:** unique fixed ray and convergence from Section 5.

**Outputs:** stationary or adjacent-alternating selectors, no numerical cycle, interior quadratic-at-most spectrum, and positive integer wall spectrum.

**Exact Table 1 contract:** the table is hand-typeset and has exactly three columns:

- Mechanism;
- Consequence;
- Boundary that breaks or limits it.

It has five concise, nonnumeric rows:

1. full-face Hessian certificate; cancellation-safe leading pair; axes, zero/uncollected coefficients, or positive characteristic;
2. strict carries plus separated powers; visible exact forward/inverse degrees; exponent one or mixed \(W\);
3. finite-envelope log contraction; unique ray and selector dichotomy; infinite support, mixed \(W\), or higher projective dimension;
4. interior matrix/common primitive wall ray; quadratic-at-most versus integral spectrum; no extension to all Hamiltonian shears or higher dynamical degrees;
5. stable visible coordinate plus Cayley--Hamilton; recurrence upper bounds; no minimality and no scalar transfer from the bridge.

There are exactly zero figures and no second table.

**Transition:** Section 7 extracts scalar recurrences from the classified matrix tails, treating inverse maxima independently.

### Section 7 -- Forward and inverse scalar recurrences -- 4.00 pages

**Purpose:** prove every scalar degree-tail law with the correct state matrix, selector coordinate, visible maximum, parity, and index threshold.

**Subsection and page allocation:**

- **7.1 State-matrix and visibility notation -- 0.45 page.** Freeze \(A_\xi,C_\xi,D_\xi\), \(d_n^\pm\), \(r_n\), \(s_n\), \(r_\star\), \(s_\star\), and the rule that inverse selectors use \(\kappa s_n\).
- **7.2 Forward interior tail -- 0.55 page.** Apply Cayley--Hamilton to \(C_\xi\); separate \(r_\star\ne1\), where one maximum coordinate stabilizes, from \(r_\star=1\), where the ordinary seed is fixed and the scalar sequence is geometric.
- **7.3 Forward fixed-wall and strict-wall tails -- 0.55 page.** Treat the fixed-wall seed geometrically; for a strict tail define both
  \[
  M_+=C_+C_-,\qquad M_-=C_-C_+,
  \]
  in selector-word order and derive the stride-two coordinate laws.
- **7.4 Inverse chamber matrices -- 0.65 page.** Derive directly from the inverse state
  \[
  D_\xi=A_\xi B=B^{-1}C_\xi B,\qquad
  v_{n+1}^-=D_\xi v_n^-,
  \]
  only when \(\kappa s_n\) lies in the \(\xi\)-chamber. Similarity alone is not the recurrence proof.
- **7.5 Inverse interior cases -- 0.45 page.** If \(s_\star\ne1\), prove eventual stable visibility before promoting the coordinate recurrence to \(d_n^-\). If \(s_\star=1\), prove that the ordinary inverse seed is fixed from time zero and the scalar sequence is geometric.
- **7.6 Inverse fixed-wall and strict-wall cases -- 0.65 page.** State the fixed-wall condition as \(\kappa s_\star=r_\star\) on the Newton wall and keep \(Bv_n^-\) on the tied ray. Prove that a strict ordinary inverse orbit has \(s_\star\ne1\), then define
  \[
  N_+=D_+D_-,\qquad N_-=D_-D_+,
  \]
  with
  \[
  N_\pm=B^{-1}M_\pm B.
  \]
- **7.7 Common coefficients, parity visibility, and indices -- 0.50 page.** Prove common
  \[
  \tau=\operatorname{tr}(M_\pm)=\operatorname{tr}(N_\pm),
  \qquad
  \Delta=\det(M_\pm)=\det(N_\pm),
  \]
  stabilize the same visible coordinate on each parity beyond an explicit threshold, and derive separately
  \[
  d_{n+4}^\pm=\tau d_{n+2}^\pm-\Delta d_n^\pm
  \]
  for all sufficiently large admissible \(n\).
- **7.8 Consequence and boundary -- 0.20 page.** Summarize order at most two, order at most four, and geometric special cases; deny minimality and deny derivation from the bridge.

**Formal statement placement:**

- Proposition 7.1, Forward interior and wall scalar tails.
- Proposition 7.2, Inverse interior scalar tails from \(D_\xi\).
- Proposition 7.3, Inverse fixed-wall and strict-wall parity tails.
- Corollary 7.4, Bidirectional recurrence upper bounds.

**Inputs:** exact state visibility from Section 4 and selector classification from Section 6.

**Outputs:** separately proved forward and inverse scalar recurrence laws.

**Required index discipline:**

- \(n\) is reserved for the iterate index;
- thresholds use \(n_{\mathrm{int}},n_{\mathrm{wall}}\), or \(n_0\), never a symbol already assigned to a support, ray, or matrix;
- the displayed order-four law is eventual and must say “for all sufficiently large \(n\)”;
- each parity product must match the actual selector step order;
- \(\tau,\Delta\) are shared coefficients, not claims that the state matrices are equal.

**Transition:** Section 8 checks both terminal regimes exactly and exposes every boundary before the conclusion.

### Section 8 -- Exact fixtures, scope, and collision subtraction -- 2.50 pages

**Purpose:** give two hand-checkable fixtures, show exactly where assumptions enter, and prevent overlap with the nearest local predecessors.

**Subsection and page allocation:**

- **8.1 Fixture I: genuinely quadratic interior value -- 0.65 page.** Use
  \[
  E=\{(2,2)\},\qquad B=\operatorname{diag}(3,2),
  \qquad C=\begin{pmatrix}3&6\\4&2\end{pmatrix}.
  \]
  Derive \(t^2-5t-18\), \((5+\sqrt{97})/2\), and the exact bridge check
  \[
  u_1^+=(9,6),\quad v_1^-=(7,8),\quad
  u_2^+=(63,48)=3Bv_1^-.
  \]
- **8.2 Fixture II: transient to a fixed wall -- 0.90 page.** Use
  \[
  E=\{(2,8),(4,5),(5,3)\},\qquad
  B=\operatorname{diag}(24,11).
  \]
  Derive walls \(3/2,2\), the exact ratios
  \[
  r_1=24/11,\quad r_2=1548/781,\quad
  r_3=51294/25619,
  \]
  prove the middle/high interval images, compute common wall direction \((2,1)^\top\), multiplier \(132\), and monodromy trace \(17648\), determinant \(3902976\), and eigenvalues \(17424,224\). Call this selector alternation converging to \(r=2\), never a numerical two-cycle.
- **8.3 Failure modes tied to assumptions -- 0.40 page.** Cover axes, exponent one, zero or uncollected coefficients, mixed \(W\), positive characteristic, altered seed or phase order, and dimension at least three. Each item names the exact broken lemma.
- **8.4 Local collision subtraction -- 0.30 page.** Record the Paper 24 and Paper 25 boundaries below. Public prose must describe mechanism/assumption differences without citing unpublished local project identifiers.
- **8.5 Remaining anti-claims -- 0.25 page.** State no higher dynamical degrees, entropy, compactification, integrability, point-orbit arithmetic, genericity, classification, nonconjugacy, support optimality, recurrence minimality, or global priority.

**Example status:** Examples 8.1 and 8.2 are exact proof fixtures. They do not create an experiment section, result table, plot, data source, CAS certificate, or numerical validation claim.

**Paper 24 subtraction:** Paper 24 owns a special two-term wall criterion, forced selector period two, two-step monodromy/parity mechanics, and the corresponding interleaved recurrence framing. Paper 26 must not claim novelty for those pieces. Its distinct center is arbitrary finite planar support, full tied-face cancellation, one global log contraction, no nontrivial numerical cycle, exact inverse transport, and a common-wall-ray integer multiplier. Two-step products appear only after Theorem 5.3 and Proposition 6.1.

**Paper 25 subtraction:** Paper 25 owns support-rank bounds, stationary sharp constructions, unbounded higher-dimensional Perron degree, and scalar minimality. Paper 26 proves rigidity for a narrower two-dimensional separated family. It must not present the quadratic cap as contradicting Paper 25, must not claim support-rank novelty, and must not claim scalar minimality.

**Inputs:** all theorem conclusions and the frozen local collision assessment.

**Outputs:** exact sharpness witness for the quadratic cap, exact wall witness, and visible limits on every conclusion.

**Transition:** the Conclusion states the closed theorem and the two unresolved publication checks without reopening extensions.

### Section 9 -- Conclusion -- 0.50 page

**Purpose:** restate the single mechanism chain and preserve the publication boundary.

**Subsection and page allocation:**

- **9.1 The theorem in one chain -- 0.35 page.** Rephrase full-face exactness, bidirectional transport, contraction, selector/spectral rigidity, and recurrence consequences without copying the Introduction.
- **9.2 Open verification, not new mathematics -- 0.15 page.** State that final primary-record citation verification and a global claim-level novelty search remain required. Do not list conjectural higher-dimensional or mixed-\(W\) extensions as results.

**Inputs:** Sections 3--8.

**Outputs:** a bounded conclusion with no new claim, citation, example, table, or figure.

## Notation and equation introduction order

The manuscript source author must follow this order and may not reuse a symbol for an incompatible role.

1. **Coordinates and maps:** \(K,q,p,V,W,S,T,F,J\), followed by \(S^{-1},T^{-1},F^{-1}\).
2. **Support geometry:** \(E,u,H,\mathcal A,B\), then \(E_u,P_u,(x_0,y_0)\). The face coefficient is written \(c_{x_0,y_0}\); do not abbreviate it by \(c_0\), because \(c_\star\) is reserved for the bridge.
3. **Degree states:** \(w_{n+1}^+,u_n^+,z_{n+1}^-,v_n^-\), then \(d_n^+=\deg(F^n)\) and \(d_n^-=\deg(F^{-n})\).
4. **Bridge:** \(c_\star=H(\mathbf1)-1\) only after both exact transports and visible degrees are proved.
5. **Projective dynamics:** \(r,\Phi,\kappa,\phi,t,h,\eta,q\), then inverse ratio \(s,\psi,L\). The letter \(q\) here denotes only the contraction constant after position coordinates are no longer denoted individually in that section.
6. **Selector matrices:** \(\xi=(x,y),A_\xi,C_\xi\). Use \(\boldsymbol\omega\), not \(w\), for the primitive wall direction so that it cannot be confused with \(w_n^+\).
7. **Inverse recurrence matrices:** \(D_\xi,s_n,s_\star,M_\pm,N_\pm,\tau,\Delta\). Define each product in actual time order before using cyclic trace.
8. **Fixtures:** introduce low, middle, and high labels only inside Example 8.2.

Equation introduction is also forward-only:

1. map and inverse formulas;
2. support function and full face;
3. Hessian witness coefficient;
4. Jacobian and substitution consequences;
5. carry inequalities;
6. exact degree states and visible maxima;
7. shifted bridge and norm comparison;
8. projective maps, derivative, logarithmic slope, gap, and \(q\);
9. selector matrices and spectral multipliers;
10. forward and inverse recurrence matrices and laws;
11. fixture arithmetic.

No equation may be cited before it is defined, and no later fixture equation may replace a general proof.

## Citation-slot map and bibliography admission

The plan uses only locally frozen, complete planning slots from the citation ledger. They remain contextual and require primary-record rechecking before a bibliography is authored.

### Eligible local planning slots

- **CTX-DEG-1:** Marc P. Bellon and Claude-Michel Viallet, “Algebraic entropy,” DOI 10.1007/s002200050652. Place at the end of the broad degree-growth motivation in Section 1.1.
- **CTX-DEG-2:** Nguyen-Bac Dang and Charles Favre, “Spectral interpretations of dynamical degrees and applications,” DOI 10.4007/annals.2021.194.1.5. Use only for general spectral context in Section 1.1 or the opening sentence of Section 6.
- **CTX-TROP-1:** Allan P. Fordy and Andrew N. W. Hone, “Symplectic maps from cluster algebras,” DOI 10.3842/SIGMA.2011.091. Use in Section 1.3 for structured symplectic/tropical recurrences.
- **CTX-TROP-2:** Allan P. Fordy and Andrew N. W. Hone, “Discrete integrable systems and Poisson algebras from cluster maps,” DOI 10.1007/s00220-013-1867-y. Use only as Poisson/symplectic recurrence context; the manuscript must explicitly avoid an integrability inference.
- **CTX-TROP-3:** Tsukasa Ishibashi and Shunsuke Kano, “Algebraic entropy of sign-stable mutation loops,” DOI 10.1007/s10711-021-00606-1. Use only for conceptual comparison with stable tropical sign data.
- **CTX-SYMP-1:** Stanisław Janeczko and Zbigniew Jelonek, “Polynomial symplectomorphisms,” DOI 10.1112/blms/bdm112. Use for family-level background, not classification or an exact degree formula.
- **CTX-SYMP-2:** Pierre Berger and Dmitry Turaev, “Generators of groups of Hamiltonian maps,” arXiv:2210.14710. Use only after the title form and current publication metadata are rechecked against the primary record.
- **CTX-AFF-1:** Jérémy Blanc and Immanuel van Santen, “Dynamical degrees of affine-triangular automorphisms of affine spaces,” DOI 10.1017/etds.2021.90, arXiv:1912.01324. Use only as an adjacent structured-automorphism comparison; do not place the present family inside that class without proof.

### Barred or unresolved slots

- The Koch--Lomelí record associated locally with arXiv:1304.3377 is barred from manuscript citation and from references.bib because its exact title, venue, author diacritics, and claim-level relevance are not fully frozen.
- No source inherited from Papers 20--25 is admitted merely because it appeared in a neighboring bibliography.
- No citation for the Jacobian criterion, Banach contraction, Perron--Frobenius, Cayley--Hamilton, rational algebraic integers, or cyclic trace may be invented. The body contains the needed theorem statement or proof; an authoritative standard citation may be added only after separate primary verification.
- No public citation is used to perform the private Paper 24/Paper 25 subtraction.

### Section-level placement

- **Abstract:** no citations.
- **Section 1.1:** CTX-DEG-1 and, if primary recheck passes, CTX-DEG-2.
- **Section 1.3:** a synthesized paragraph using the minimum sufficient subset of CTX-TROP-1, CTX-TROP-2, CTX-TROP-3, CTX-SYMP-1, CTX-SYMP-2, and CTX-AFF-1.
- **Section 2:** at most one family-context citation already introduced in Section 1; none is a proof dependency.
- **Sections 3--7:** no contextual citation inside a proof step. Any standard source is placed after the self-contained statement, never instead of the argument.
- **Section 8:** no citation for fixtures; no unpublished local-paper citation.
- **Section 9:** no priority or exhaustive-search citation.

### Admission test

Before any entry enters references.bib:

1. authors, title, year, venue, pagination or article number, and persistent identifier are checked against a primary record;
2. the exact cited sentence respects the source hypotheses;
3. the citation supplies context only and is cited somewhere in the body;
4. no bibliography field contains a local path, review datum, speculative title, or identity;
5. the comparison contains no “first,” “only,” “new globally,” “unprecedented,” or exhaustive noncollision wording.

If primary verification is not complete, references.bib authoring must stop rather than fill a field from memory.

## Anti-claim placement ledger

Every boundary must appear near the theorem step it limits and again, compactly, in Section 8.

- **Axes and exponent one:** state after Lemma 4.1 and in Section 8.3; these can break face-gradient independence or strict carries.
- **Zero or uncollected coefficients:** state with the definition of \(E\) and in Section 8.3; the theorem always uses actual collected support.
- **Positive characteristic:** state after Lemma 3.2 and in Section 8.3; derivative and Hessian coefficients can vanish.
- **Mixed \(W\):** state after Proposition 5.1 and in Section 8.3; diagonal scaling and decreasing projective dynamics can fail.
- **Dimension at least three:** state after Theorem 5.3 and in Section 8.3; the proof uses a one-dimensional ordered projective chart.
- **Changed phase order or seed:** state with Proposition 4.4 and in Section 8.3; the bridge base case and shift change.
- **No numerical two-cycle:** state in the Abstract, Proposition 6.1, Example 8.2, and Section 8.5; selector labels alternate while ratios converge.
- **No termwise forward/inverse equality and no scalar transfer:** state in Proposition 4.4, Section 7 opening, and Section 8.5.
- **No recurrence minimality:** state in every recurrence proposition and Section 8.5.
- **No global quadratic claim for all Hamiltonian shears:** state with Corollary 6.4 and Section 8.5.
- **No higher dynamical degrees, entropy, compactification, integrability, or point-orbit arithmetic:** state in Section 8.5.
- **No genericity substitute, support optimality, classification, nonconjugacy, or global priority:** state in Sections 1.4, 3.5, 8.5, and 9.2.

## Figure, table, and asset policy

- The manuscript contains **exactly zero figures**.
- No figure directory, raster image, vector image, diagram asset, data file, plot, contact sheet, or generated visual is planned or permitted.
- The manuscript contains **exactly one table**, the hand-typeset structural Table 1 in Section 6.7.
- Table 1 is qualitative and maps mechanism to consequence to boundary. It has no experimental values, benchmark, score, or numerical comparison.
- No page-budget table, claims matrix, fixture table, literature table, or notation table appears in the manuscript. Those planning functions remain prose lists in this file.
- Every fixture is typeset as equations and explanatory prose.

## Proof-mass and page-risk controls

The 26.0-page allocation is a design target, not a claim about an unbuilt PDF. Actual rendered pagination must be checked only at a later authorized build stage.

### Under-length defense

If a later authorized draft is below 22 content pages, it may expand only theorem-critical exposition, in this order:

1. Section 3 cross-pair exclusion, Jacobian argument, multi-point ties, and substitution chain;
2. Section 4 all old/fresh block comparisons, (6.3)--(6.4), and the full inverse induction;
3. Section 5 endpoint compactification, finite-support maximum, and interval wall patching;
4. Section 6 multiple ties, no delayed landing, primitive-ray integrality, and per-step versus two-step growth;
5. Section 7 inverse selector scaling, \(s_\star\) cases, product order, parity visibility, and admissible indices;
6. Section 8 exact interval images and hand arithmetic.

It may not expand the Introduction or Related Work first, repeat Paper 24 monodromy material, add a third example, add a figure or table, insert filler, force page breaks, enlarge displays, or change font, line spacing, margins, or paragraph spacing.

### Over-length defense

If a later authorized draft exceeds 30 content pages, compress repeated motivation in Section 1, repeated definitions, and duplicated fixture arithmetic first. Do not remove the full-face coefficient proof, either half-step induction, wall patching, wall integrality, or the separate inverse scalar recurrence proof. No theorem-critical argument may be moved to an appendix.

### Collision-driven mass control

- Paper 24-style parity and monodromy mechanics remain inside Sections 7 and 8 and cannot become the opening or the largest proof block.
- Paper 25-style matrix recurrence and Perron tools remain consequences; support rank, unbounded algebraic degree, and minimality do not enter the paper.
- Sections 4--7 retain exactly 15.5 pages so that the article cannot collapse into a short special-example note.

## Future exact source-trio architecture

A later parent gate may jointly authorize exactly these three source files and no others:

1. **paper/main.tex**
   - exact title, Anonymous, empty visible date, and empty PDF fields for Author, Creator, Producer, Subject, and Keywords;
   - Abstract and exactly Sections 1--9 in the order above;
   - all theorem statements and proofs;
   - the sole hand-typeset Table 1;
   - the bibliography call and References heading;
   - no appendix, figure, external input, local path, code, generated source, hidden metadata, or identity.
2. **paper/math_commands.tex**
   - notation and formatting macros only;
   - no prose, theorem, citation, file I/O, executable behavior, identity, or hidden source.
3. **paper/references.bib**
   - only primary-verified and actually cited entries admitted under the citation rules above;
   - no incomplete Koch--Lomelí entry, speculative metadata, local path, internal predecessor, review record, or unused entry.

No section files, style files, figure files, data, code, notebooks, scripts, generated tables, auxiliary sources, or alternate bibliography databases belong to the future source universe.

This plan does not authorize creation of any member of the trio.

## Future source-author acceptance checklist

A future source author may stop successfully only if every item below is satisfied.

### Identity, anonymity, and structure

- [ ] Exact title reproduced everywhere it is visible or stored.
- [ ] Visible author is Anonymous; visible date is empty.
- [ ] PDF Author, Creator, Producer, Subject, and Keywords are all empty; no identity appears in comments, metadata, bookmarks, links, filenames, or bibliography.
- [ ] Abstract plus exactly Sections 1--9; no appendix or supplement.
- [ ] Content plan totals 26.0 pages; references are excluded.
- [ ] Sections 4--7 retain 15.5 pages.
- [ ] Exactly zero figures/assets and exactly one structural table.

### Theorem order and proof completeness

- [ ] Full-face Hessian coefficient and algebraic independence appear before any degree recurrence derivation.
- [ ] Main Theorem includes every frozen hypothesis and conclusion in dependency order.
- [ ] Both forward half-steps and both inverse half-steps are explicit.
- [ ] Carry equations corresponding to (6.1)--(6.4) are present and used for block visibility.
- [ ] Inverse phase order and subtraction signs are correct.
- [ ] Degree states and four-coordinate visible maxima are distinguished.
- [ ] Bridge includes \(c_\star\), \(B\), the one-step shift, and ordinary seed.
- [ ] Bridge is never used as a scalar recurrence proof.
- [ ] Log contraction contains branch derivative, \(\eta\), positive gap, endpoint limits, finite maximum, and wall patching.
- [ ] Inverse selector uses \(\kappa s\).
- [ ] Wall fixed and strict trajectories, multiple ties, no delayed landing, and no numerical cycle are all explicit.
- [ ] Interior Perron and wall primitive-ray integer proofs are complete.
- [ ] Forward and inverse recurrences are separate; \(D_\xi\), \(s_\star=1\) and \(s_\star\ne1\), fixed and strict walls, \(M_\pm,N_\pm\), parity visibility, indices, and upper-bound wording are all present.
- [ ] Both fixtures reproduce every frozen rational and integer exactly.

### Claims, citations, and scope

- [ ] Every promoted claim maps to a proved proposition or corollary and a named kill condition.
- [ ] Citation slots are drawn only from the eligible local list and are admitted only after primary recheck.
- [ ] Koch--Lomelí-like incomplete metadata is absent.
- [ ] Citations provide context only; all theorem-critical proofs are internal.
- [ ] No global novelty, firstness, exhaustiveness, genericity, classification, recurrence minimality, entropy, integrability, compactification, or higher-dynamical-degree claim appears.
- [ ] Paper 24 wall-selector/monodromy ownership and Paper 25 support-rank/unbounded-degree/minimality ownership remain subtracted.
- [ ] Selector alternation is always described as convergence to one wall ray.

### Source-universe and no-drift checks

- [ ] The only future source files are main.tex, math_commands.tex, and references.bib.
- [ ] No theorem-critical proof is hidden in comments, an appendix, a supplement, or an uncited external source.
- [ ] No empirical, numerical, CAS, benchmark, dataset, ablation, or experiment language appears.
- [ ] No extra table, figure, asset, code, data, or generated source is introduced.
- [ ] No page-control or formatting trick substitutes for mathematical content.

## Kill criteria and forbidden drift

Any one of the following requires the future source stage to stop without a partial source trio or an invented repair:

1. an in-scope exposed face has zero Hessian determinant;
2. a tied wall leading form cancels or is replaced by one selected monomial;
3. algebraic independence is assumed or made generic rather than proved;
4. one of the forward or inverse visible-block comparisons fails;
5. the exact bridge base case, phase order, shift, scalar, or diagonal factor changes;
6. no single \(q<1\) is proved across all support branches and walls;
7. an in-scope selector tail lies outside interior stationarity, fixed-wall behavior, or adjacent-wall alternation;
8. selector alternation is promoted to a nontrivial numerical two-cycle;
9. a wall multiplier fails to be a positive integer or an in-scope value has algebraic degree above two;
10. the inverse scalar recurrence is inferred from the bridge, uses \(C_\xi\) instead of \(D_\xi\), selects by \(s\) instead of \(\kappa s\), omits a seed case, reverses a parity product, or lacks visible-coordinate stabilization;
11. a recurrence order is claimed minimal;
12. either fixture fails exact hand reconstruction;
13. an incomplete or unverified bibliographic record is required for a public comparison;
14. a primary source proves the same complete arbitrary-support, wall-safe, bidirectional contraction theorem and the novelty center is not narrowed;
15. a Paper 24 or Paper 25 headline is repackaged as the Paper 26 contribution;
16. the draft needs an appendix, second table, figure, computation, or formatting manipulation to meet the page target;
17. anonymity, empty-date, empty-PDF-metadata, or public-firewall requirements cannot be met.

Forbidden drift includes axis or exponent-one support, zero or uncollected coefficients, mixed \(W\), positive characteristic, dimension at least three, a changed phase order or arbitrary bridge seed, termwise forward/inverse equality, numerical cycles, global quadratic sharpness for all Hamiltonian shears, higher dynamical degrees, entropy, compactification, integrability or nonintegrability, periodic or arithmetic point-orbit conclusions, genericity, support optimality, classification, nonconjugacy, global priority, and external effects.

## Plan-review checklist

The later independent paper-plan reviewer must treat this plan as unproved and verify:

1. exact identity, unique terminal, sole L13-to-L14 delta, four-directory/fourteen-file inventory, and predecessor stability;
2. the exact 26.0-page and 15.5-page arithmetic, including every subsection subtotal;
3. full theorem hypotheses, conclusions, dependency order, notation order, and equation order;
4. complete placement of all cancellation, carry, contraction, selector, spectrum, recurrence, fixture, and boundary obligations;
5. separate inverse scalar-recurrence logic and the bridge boundary;
6. exactly zero figures/assets and exactly one structural table;
7. citation-slot eligibility, the Koch--Lomelí bar, unresolved primary verification, and absence of global-priority wording;
8. Paper 24 and Paper 25 subtraction;
9. anonymous/empty-date/empty-PDF-metadata intent and the exact future source trio;
10. kill criteria, forbidden drift, and the fact that this file grants no successor authority.

A finding in any class requires zero review write. A valid plan-review verdict, if separately authorized, cannot itself authorize manuscript source, bibliography verification, computation, compilation, build, release, submission, or an external effect.

## Final authority statement

This plan organizes the frozen Paper 26 source design without changing a theorem, hypothesis, example, citation boundary, novelty status, anti-claim, or permission. It plans a 26.0-page proof-first body, zero figures, one structural table, and a possible future exact three-file source universe. It creates no manuscript source and opens no successor action.

PAPER26_PAPER_PLAN_REPAIR_AUTHOR_STOP_R1
