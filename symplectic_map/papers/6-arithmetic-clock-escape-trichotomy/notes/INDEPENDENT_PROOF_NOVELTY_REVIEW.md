# Independent Proof and Novelty Review

**Candidate:** `arithmetic_clock_escape_trichotomy_v1`  
**Review date / literature cutoff:** 2026-08-14  
**Reviewer role:** independent proof attack and external novelty collision search  
**Inputs examined:** `RESEARCH_QUESTION.md`, `PROOF_PACKAGE.md`,
`source_lock.json`, and `EXPERIMENT_PLAN.md` only. I did not inspect any other
unfinished agent output, did not modify the source lock or proof package, and
did not access prime tables or Riemann-zero data.

## Executive decision

**Verdict: REPAIR.**

The selector/union theorem currently written in `PROOF_PACKAGE.md` is correct
under the literal convention that a target is supplied by one L-, M-, or
A-component. Its proof survives the attacks below. However, the phrase
“architecture assembled from the three classes” naturally suggests that the
outputs may be combined. The present union proof does not address that reading,
and a selector-only union of three already established obstructions is too close
to a bookkeeping corollary to carry the strongest standalone positioning.

There is a clean repair that is both stronger and genuinely couples the three
mechanisms: prove the bound for an explicitly defined **additive architecture**.
For every realized prime, require a representation

\[
\log p=v+\log q+\alpha,
\qquad
v\in V,\qquad
q\in\overline{\mathbb Q}\cap\mathbb R_{>0},\qquad
\alpha\in\overline{\mathbb Q}\cap\mathbb R,
\]

where \(q^2\) is an \(S_{\mathbb Q}\)-unit. Under these hypotheses the same
bound

\[
\#\mathcal P_{\rm hit}
\leq \dim_{\mathbb Q}V+|S_{\mathbb Q}|
\]

is provable. The selector theorem is then an immediate special case. The full
proof is reconstructed below, including rational coefficients, negative powers,
field extensions, repeated representations, and the real-log convention.

**Novelty score: 5.5/10 (moderate synthesis/certificate novelty; low component
novelty).** No web-indexed primary source returned by the searches through the
stated cutoff and under the query families recorded below states this same
three-source additive capacity theorem. That negative search is evidence, not a
priority proof. The
finite-rank, good-reduction/S-unit, action-sum, and Hermite--Lindemann ingredients
are individually elementary or classical relative to their literatures. The
defensible contribution is the precise mixed-class certificate, its sharp
assumption ledger, and its machine-auditable escape map—not a new foundational
theorem in any one of symbolic dynamics, arithmetic dynamics, transcendence
theory, or symplectic geometry.

## A. Independent proof attack

### A.1 Mandatory normalization: what an additive architecture means

Fix a finite set \(S_{\mathbb Q}\) of rational primes and a finite-dimensional
\(\mathbb Q\)-vector space \(V\subset\mathbb R\).

Call an algebraic number \(x\neq0\) an
**\(S_{\mathbb Q}\)-unit** if, in one (equivalently every sufficiently large)
number field containing \(x\), its additive valuation is zero at every finite
place not lying over a prime in \(S_{\mathbb Q}\). This definition is stable
under finite field extension, multiplication, and inversion.

An in-scope additive readout for a periodic orbit must reduce to

\[
L=v+\log q+\alpha,                                      \tag{1}
\]

with:

1. \(v\in V\), where the same fixed \(V\) is used for the entire architecture;
2. \(q>0\) is algebraic and \(q^2\) is an
   \(S_{\mathbb Q}\)-unit;
3. \(\alpha\) is a real algebraic number; and
4. every coefficient, weight, normalization, and operation defining (1) is
   fixed independently of the target prime.

This normal form includes finite rational linear combinations and repetitions:

- rational combinations of L-lengths remain in \(V\);
- if \(q_j=|\lambda_j|>0\), \(q_j^2\) is an
  \(S_{\mathbb Q}\)-unit, and \(c_j\in\mathbb Q\), then
  \(\sum_jc_j\log q_j=\log q\) for the positive algebraic number
  \(q=\prod_jq_j^{c_j}\); after adjoining the required positive roots,
  \(q^2\) is still an \(S_{\mathbb Q}\)-unit;
- finite algebraic sums and allowed algebraic scalings of A-readouts remain
  algebraic.

Negative rational coefficients cause no problem: positive algebraic numbers
have positive algebraic rational powers, inverses of \(S\)-units are
\(S\)-units, and the real logarithm obeys
\(\log(q^c)=c\log q\). Integer repetitions are the special case
\(c\in\mathbb Z\).

This closure does **not** include an algebraic irrational coefficient multiplying
\(\log q\), an arbitrary nonlinear function of component outputs, an
orbit-indexed lookup table, or a logarithm applied after an A-action. None of
those operations is reduced to (1) by the present argument.

### A.2 Repaired theorem

**Theorem (additive finite arithmetic capacity).** Let \(V\subset\mathbb R\)
be finite-dimensional over \(\mathbb Q\), and let \(S_{\mathbb Q}\) be a fixed
finite set of rational primes. Suppose every prime \(p\) realized by the
architecture has at least one representation

\[
\log p=v_p+\log q_p+\alpha_p,                            \tag{2}
\]

where \(v_p\in V\), \(q_p\in\overline{\mathbb Q}\cap
\mathbb R_{>0}\), \(q_p^2\) is an \(S_{\mathbb Q}\)-unit, and
\(\alpha_p\in\overline{\mathbb Q}\cap\mathbb R\). Then

\[
\#\mathcal P_{\rm hit}
\leq \dim_{\mathbb Q}V+|S_{\mathbb Q}|.                \tag{3}
\]

**Status:** PROVABLE AS STATED under the normalized assumptions above.

### A.3 Proof of the repaired theorem

Let

\[
\mathcal P_0=\mathcal P_{\rm hit}\setminus S_{\mathbb Q}.
\]

For each \(p\in\mathcal P_0\), choose one representation (2). Multiple orbits
or multiple representations of the same prime do not create multiple set
elements; choosing one certificate per distinct prime is enough.

Take distinct primes \(p_1,\ldots,p_k\in\mathcal P_0\). Suppose that their
L-parts are rationally dependent:

\[
\sum_{i=1}^k c_i v_{p_i}=0,
\qquad c_i\in\mathbb Q.
\]

Clear denominators. There are integers \(m_i\), not all zero, such that

\[
\sum_{i=1}^k m_i v_{p_i}=0.                             \tag{4}
\]

Substitute (2) into (4). Because every \(q_{p_i}\) is positive and the real
logarithm is additive for positive factors, this gives

\[
\log R=\beta,                                           \tag{5}
\]

where

\[
R=\frac{\prod_i p_i^{m_i}}{\prod_i q_{p_i}^{m_i}}
   \in\overline{\mathbb Q}\cap\mathbb R_{>0},
\qquad
\beta=\sum_i m_i\alpha_{p_i}
   \in\overline{\mathbb Q}\cap\mathbb R.
\]

If \(\beta\neq0\), Hermite--Lindemann says that \(e^\beta\) is
transcendental, contradicting \(e^\beta=R\in\overline{\mathbb Q}\). Hence
\(\beta=0\), and (5) yields \(R=1\). Squaring eliminates every modulus square
root without making any choice of a complex logarithm:

\[
\prod_{i=1}^k p_i^{2m_i}
=\prod_{i=1}^k(q_{p_i}^2)^{m_i}.                         \tag{6}
\]

Put the finitely many algebraic numbers in (6) in one number field \(E\).
After finite extension, each \(q_{p_i}^2\) remains a unit at every finite place
not above \(S_{\mathbb Q}\). For a fixed \(i\), choose a finite place
\(w\) of \(E\) above \(p_i\). Since \(p_i\notin S_{\mathbb Q}\), the
right-hand side of (6) has \(w\)-valuation zero. The primes \(p_j\) are
distinct, so the left-hand side has valuation

\[
2m_i\,v_w(p_i).
\]

Here \(v_w(p_i)>0\), forcing \(m_i=0\). This holds for every \(i\),
contradicting the choice of a nonzero relation. Therefore

\[
\{v_p:p\in\mathcal P_0\}
\]

is linearly independent over \(\mathbb Q\). It has at most
\(\dim_{\mathbb Q}V\) elements. At most \(|S_{\mathbb Q}|\) further
distinct rational primes lie inside \(S_{\mathbb Q}\), proving (3). If the hit
set were infinite, any \(\dim V+1\) distinct primes outside \(S_{\mathbb Q}\)
would already contradict the finite-dimensional conclusion, so no separate
finiteness assumption on the hit set is used. \(\square\)

### A.4 Edge-case audit of the repaired theorem

- **\(q=0\):** excluded explicitly. A determinant-one return multiplier is
  nonzero, so its modulus is positive.
- **Negative algebraic inputs:** the theorem uses the positive real modulus
  \(q=|\lambda|\), never \(\log\lambda\). No logarithm of a negative number is
  taken.
- **\(q=1\):** allowed; it contributes zero.
- **Negative exponents:** allowed because \(q>0\) and the \(S\)-unit group is
  closed under inversion.
- **Rational exponents:** allowed after passing to a finite algebraic extension;
  zero valuations outside \(S_{\mathbb Q}\) remain zero. The paper should say
  this rather than informally “clearing denominators” inside a fixed field.
- **Square root/modulus:** no assertion \(\overline\lambda=\lambda^{-1}\) is
  made. One uses only \(q^2=\lambda\overline\lambda\) and stability of the
  unit property under Galois conjugation.
- **Representation choices:** one arbitrary valid representation is fixed for
  each distinct prime before testing a finite relation. The proof works for
  every such choice.
- **Repeated hits:** \(\mathcal P_{\rm hit}\) is a set, not a multiset. Repeated
  orbits realizing the same \(p\) do not affect (3).
- **Zero-dimensional \(V\):** the proof shows that no prime outside
  \(S_{\mathbb Q}\) can be hit; the bound remains valid.
- **Real-log convention:** positivity is essential. Complex logarithm branch
  changes would introduce multiples of \(2\pi i\) and are outside this theorem.

### A.5 Audit of the three source classes

#### Class L — PASS

Every closed-walk length is an integer combination of finitely many edge
lengths and hence lies in \(V\). A finite-memory locally constant function on a
finite-state shift can be passed to a higher-block presentation with finitely
many vertices and edges, so “finite memory” does not enlarge the rational span.
This passage must be stated explicitly. The bound uses only finite rational
rank; the edge multipliers need not be algebraic.

The family \(\{\log p\}\) is \(\mathbb Q\)-linearly independent by clearing
denominators, exponentiating a real equality, and applying unique factorization.
The rank bound is sharp only as an abstract capacity statement: inserting
\(\log p_j\) as edge data is target injection, not arithmetic emergence.

#### Class M — PASS, with exposition repairs required

The core argument is sound:

1. Expanding a periodic orbit of a composition into the individual Hénon
   factors gives a finite cyclic recurrence
   \(z_{j+1}+z_{j-1}=p_{i_j}(z_j)\).
2. Homogenize each recurrence equation to its own degree \(d_{i_j}\). At
   \(Z=0\), monicity leaves \(z_j^{d_{i_j}}=0\) for every \(j\), so the
   projective closure has no point at infinity. The manuscript should add the
   standard lemma that a positive-dimensional projective variety cannot be
   contained in an affine chart (a projective affine variety is
   zero-dimensional). This completes, rather than merely gestures at, the
   finiteness/algebraicity step.
3. At a nonarchimedean place of good reduction, choosing a coordinate of
   maximal norm \(R>1\) makes the monic leading term uniquely dominant:
   \(|p_i(z_j)|=R^{d_i}>R\), contradicting the recurrence bound. Thus every
   periodic coordinate is integral outside the fixed bad support.
4. Derivative factors lie in \(\mathrm{SL}_2\) over the integral closure. The
   monodromy and its inverse are integral, so both eigenvalues are units outside
   the bad places.
5. Put the orbit and multiplier in a common normal/Galois extension and enlarge
   the exceptional set to **all** places over the rational primes in
   \(S_{\mathbb Q}\). Then conjugation preserves the complement and
   \(q^2=\lambda\overline\lambda\) is an \(S_{\mathbb Q}\)-unit.

For the original selector target, \(\log|\lambda|=\log p\) is equivalent to
\(|\lambda|=p\) by injectivity of the real logarithm. For the repaired additive
theorem, rational products and powers of such moduli produce the canonical
\(q\) in (1). Neither statement claims that \(\log|\lambda|\) is algebraic.

#### Class A — PASS, with scope made explicit

At an algebraic periodic point where all rational functions are regular, every
term \(G(F^jP)\) is algebraic and a finite sum is algebraic. Algebraic scales,
averages, repetitions, real and imaginary parts, and modulus preserve
algebraicity. In particular, if \(a\in\overline{\mathbb Q}\), then
\(|a|^2=a\overline a\) is algebraic and the nonnegative square root \(|a|\)
is algebraic.

Hermite--Lindemann then excludes equality with \(\log p\). The exact-symplectic
identity legitimizes the quantity as an action, but algebraicity of the evaluated
sum is the operative obstruction. Algebraic gauge and endpoint terms remain
algebraic whether or not they telescope; compatibility is needed for canonical
gauge invariance, not for the algebraicity conclusion.

The positive boundary control should preferably use the identity map on
\(\mathbb A^2\), with its standard exact symplectic form and constant
\(G=\log2\), rather than relying on readers accepting a zero-dimensional point
as a symplectic phase space. It is still transparently forbidden transcendental
target injection.

#### Selector union — PASS as a corollary

The existing union bound is correct if “realized” means “realized by one
component.” It becomes a special case of the additive theorem by taking:

- L hit: \((v,q,\alpha)=(\ell_L,1,0)\);
- M hit: \((v,q,\alpha)=(0,|\lambda|,0)\);
- A hit: \((v,q,\alpha)=(0,1,\mathcal A)\).

The manuscript should not leave “assembled architecture” undefined and rely
only on this selector interpretation.

### A.6 Counterexample and boundary attacks

Each of the following defeats a broader, unstated version of the theorem and
therefore must remain outside the claim:

1. **Target-dependent or unbounded L data:** one prime-labelled loop of length
   \(\log p\) per target realizes all primes; the common space \(V\) then has
   infinite rank.
2. **Target-dependent or infinite bad support:** taking \(q=p\) places each
   target prime into the multiplier support; no finite \(S_{\mathbb Q}\) remains.
3. **Transcendental A normalization:** constant \(G=\log p\) realizes the target
   directly.
4. **Logarithmic postprocessing:** an algebraic action equal to \(2\), followed
   by \(L=\log|\mathcal A|\), realizes \(\log2\). This is not an A-readout.
5. **Arbitrary nonlinear assembly:** a fixed but infinite lookup
   \(h(n)=\log p_n\) applied to an orbit index contains the prime table in the
   observable. Such a readout is neither (1) nor intrinsic arithmetic
   provenance.
6. **Algebraic irrational scaling of multiplier logs:** a term
   \(c\log q\) with \(c\in\overline{\mathbb Q}\setminus\mathbb Q\) need not be
   a log of an algebraic \(S\)-unit by the elementary argument above. The
   repaired theorem must restrict these coefficients to \(\mathbb Q\), unless a
   separate transcendence theorem is introduced.
7. **Point-dependent Hölder roofs:** their periodic sums need not lie in one
   finite-dimensional rational space. Finite symbolic state alone does not
   imply the L-certificate for a general roof.
8. **Approximate matching:** no valuation or transcendence argument converts
   numerical closeness into exact equality.

No in-scope counterexample to the repaired additive theorem was found.

## B. Mandatory repairs before manuscript drafting

1. Replace the current main theorem by the additive theorem in A.2, or state it
   as the main theorem and retain the selector union as a corollary.
2. Define an additive architecture through the canonical representation (1).
   State exactly which rational sums, repetitions, and scalings are allowed and
   explicitly exclude arbitrary nonlinear mixing and algebraic irrational
   coefficients on multiplier logarithms.
3. Define \(S_{\mathbb Q}\)-unit uniformly across varying orbit fields and state
   extension invariance. Use one common field only after selecting the finite
   relation under examination.
4. Require \(q\in\overline{\mathbb Q}\cap\mathbb R_{>0}\), not merely an
   informal modulus symbol; state that \(q^2\), rather than necessarily \(q\),
   is the certified \(S\)-unit.
5. Include the full Hermite--Lindemann-plus-valuation proof in A.3. In
   particular, show why \(\beta=0\), square the algebraic identity, and take a
   place over each distinct outside prime.
6. In Class M, add the missing “projective and affine implies
   zero-dimensional” lemma, specify separate-degree homogenization, and perform
   conjugation only after passing to a normal extension and saturating the bad
   places above \(S_{\mathbb Q}\).
7. In Class L, state the higher-block recoding that absorbs fixed finite memory.
8. In Class A, distinguish algebraicity (which survives algebraic endpoint
   shifts) from canonical gauge invariance (which needs compatibility), and use
   a conventional positive-dimensional identity-map boundary example.
9. State that hits are distinct primes in a set, select one certificate per
   prime, and address \(q=1\), negative/rational powers, and real-log branches.
10. Recast the “escape gates” as necessary failures of the declared
    certificates. They are neither mutually exclusive, jointly exhaustive for
    all dynamics, nor sufficient for arithmetic correspondence.

## C. Novelty collision search

### C.1 Search protocol and limits

I searched web-indexed primary literature, journal/publisher pages, arXiv, and
open monographs through 2026-08-14. Query families included combinations of:

- `locally constant roof`, `finite rational rank`, `periodic orbit length`,
  `prime logarithm`, and `Ruelle zeta`;
- `generalized Hénon`, `periodic multiplier`, `good reduction`, `S-unit`, and
  `arithmetic dynamics`;
- `exact symplectic`, `generating function`, `periodic action`, `algebraic`, and
  `Hermite-Lindemann`;
- `finite arithmetic capacity`, `prime periodic orbit`, `length log p`,
  `Deninger`, `scaling site`, `adele class space`, `Berry--Keating`, and
  `Connes`;
- 2025--2026 searches for Hénon multiplier rigidity, symplectic periodic-orbit
  work, and prime-labelled dynamical systems.

I found no exact title/abstract/theorem collision for the mixed capacity bound.
This statement is deliberately limited: web search is not an exhaustive proof
over MathSciNet, zbMATH, books, unpublished manuscripts, or terminology not
captured by the queries. Historical priority must not be claimed from this
search.

### C.2 Closest literature by claim

| Claim area | Closest verified literature | Overlap | Difference from this candidate |
|---|---|---|---|
| Prime logarithms as desired classical periods | Berry--Keating (1999) argue that a conjectural “Riemann dynamics” should have periods that are multiples of prime logarithms. | Same motivating target. | It is a positive semiclassical analogy/speculation, not a finite-capacity obstruction or an arithmetic provenance theorem. |
| Symbolic suspensions and periodic-orbit roofs | Parry--Pollicott (1990) develop shifts of finite type, suspensions, Ruelle operators, and periodic-orbit zeta functions. | Standard setting behind finite locally constant roofs. | I did not locate the exact prime-log rank count, and certainly not its combination with Hénon units and algebraic actions. The L lemma itself is nevertheless elementary. |
| Infinite-dimensional arithmetic dynamics | Deninger constructs infinite-dimensional real dynamical systems whose compact packets of periodic orbits correspond to closed points and have length \(\log N x\). | An actual positive prime/prime-power length architecture. | It lies outside the finite-dimensional/finite-rank architecture and is a decisive boundary example, not support for a universal no-go. |
| Scaling site / adèle class space | Connes--Consani identify periodic orbits \(C_p\) of length \(\log p\); their 2024 work gives the mapping-torus/Frobenius interpretation. | Exact all-prime periodic lengths. | The arithmetic/adelic space carries prime places intrinsically and is not a finite L/M/A construction. It must be cited prominently to prevent overstatement. |
| Adelic trace-formula program | Connes (1999) gives a trace-formula and spectral interpretation on the adèle class space. | Prime/zero dynamical-spectral context. | No three-class capacity theorem; also no warrant here for a Riemann-zero or determinant claim. |
| Arithmetic Hénon dynamics | Ingram (2014) studies canonical heights, periodicity, and bad reduction; Hsia--Kawaguchi study height and periodic-parameter families. | Arithmetic control and finite bad-place themes for Hénon maps. | I did not find the exact return-modulus \(S\)-unit support statement or the mixed capacity theorem in these works. The candidate should not claim the broader arithmetic Hénon area as new. |
| Hénon multiplier spectra | Cantat--Dujardin (2026) prove multiplier rigidity for complex Hénon maps; Bianchi--He (2026) use the full complex unstable derivative cocycle in a thermodynamic metric. | Very recent multiplier-spectrum work. | Their focus is complex rigidity/thermodynamic geometry, not rational prime support at good reduction. These papers raise the bar for current related-work coverage. |
| Exact symplectic generating-function actions | Bialy--Tsodikovich (2023) study exact symplectic maps via action sums of a generating function. | Standard action-sum formalism. | No algebraic-evaluation/Hermite--Lindemann prime-log obstruction was located. The underlying action formalism is not novel here. |
| Transcendence step | Hermite--Lindemann: the exponential of a nonzero algebraic number is transcendental, equivalently a nonzero logarithm of an algebraic number is transcendental. | Exactly the A obstruction and the bridge in A.3. | Classical theorem; no novelty can be assigned to this ingredient. |

### C.3 Verified sources and links

The following links were checked against publisher, institutional, or author/arXiv
records:

1. M. V. Berry and J. P. Keating, *The Riemann Zeros and Eigenvalue
   Asymptotics*, SIAM Review 41 (1999), 236--266,
   [doi:10.1137/S0036144598347497](https://doi.org/10.1137/S0036144598347497).
2. W. Parry and M. Pollicott, *Zeta Functions and the Periodic Orbit Structure
   of Hyperbolic Dynamics*, Astérisque 187--188 (1990),
   [doi:10.24033/ast.28](https://doi.org/10.24033/ast.28).
3. C. Deninger, *Some Analogies between Number Theory and Dynamical Systems
   on Foliated Spaces* (ICM 1998),
   [doi:10.4171/DMS/1-1/2](https://doi.org/10.4171/DMS/1-1/2).
4. C. Deninger, *Dynamical Systems for Arithmetic Schemes*, Indagationes
   Mathematicae,
   [doi:10.1016/j.indag.2024.05.007](https://doi.org/10.1016/j.indag.2024.05.007),
   [arXiv:1807.06400](https://arxiv.org/abs/1807.06400). The paper explicitly
   constructs infinite-dimensional systems with periodic packets of length
   \(\log N x\).
5. A. Connes and C. Consani, *The Scaling Site*, Comptes Rendus Mathématique
   354 (2016), 1--6,
   [doi:10.1016/j.crma.2015.09.027](https://doi.org/10.1016/j.crma.2015.09.027).
6. A. Connes and C. Consani, *Knots, Primes and the Adele Class Space*,
   [arXiv:2401.08401](https://arxiv.org/abs/2401.08401). It states and develops
   the periodic orbits \(C_p\) of length \(\log p\).
7. A. Connes and C. Consani, *Knots, Primes and Class Field Theory*,
   [arXiv:2501.06560](https://arxiv.org/abs/2501.06560). This is relevant recent
   continuation of the prime-orbit/Frobenius program.
8. A. Connes, *Trace Formula in Noncommutative Geometry and the Zeros of the
   Riemann Zeta Function*, Selecta Mathematica 5 (1999), 29--106,
   [doi:10.1007/s000290050042](https://doi.org/10.1007/s000290050042),
   [arXiv:math/9811068](https://arxiv.org/abs/math/9811068).
9. P. Ingram, *Canonical Heights for Hénon Maps*, Proceedings of the London
   Mathematical Society 108 (2014), 780--808,
   [doi:10.1112/plms/pdt026](https://doi.org/10.1112/plms/pdt026).
10. L.-C. Hsia and S. Kawaguchi, *Heights and Periodic Points for
    One-Parameter Families of Hénon Maps*,
    [arXiv:1810.03841](https://arxiv.org/abs/1810.03841).
11. S. Cantat and R. Dujardin, *Multiplier Rigidity for Complex Hénon Maps*,
    [arXiv:2603.09445](https://arxiv.org/abs/2603.09445).
12. F. Bianchi and Y. M. He, *A Thermodynamic Path Metric for Complex Hénon
    Maps*, [arXiv:2606.29363](https://arxiv.org/abs/2606.29363).
13. M. Bialy and D. Tsodikovich, *Locally Maximising Orbits for the
    Non-standard Generating Function of Convex Billiards and Applications*,
    Nonlinearity 36 (2023), 2001--2019,
    [doi:10.1088/1361-6544/acbb50](https://doi.org/10.1088/1361-6544/acbb50).
14. *Lindemann theorem*, Encyclopedia of Mathematics,
    [verified theorem statement](https://encyclopediaofmath.org/wiki/Lindemann_theorem).

## D. Safe novelty assessment and positioning

### D.1 Core claims

1. **Selector bound \(|\mathcal P_L|\leq\dim V\): novelty LOW (2/10).** It is
   an elementary linear-algebra consequence of unique factorization.
2. **Good-reduction Hénon prime-support certificate: novelty MEDIUM (5/10 in
   this exact formulation).** Arithmetic Hénon and multiplier literatures are
   substantial; the precise rational-modulus support statement was not located
   in the search, but it follows from standard integrality/unit reasoning.
3. **Algebraic action versus \(\log p\): novelty LOW (3/10).** The application
   is neat, but the proof is a direct algebraic-evaluation plus
   Hermite--Lindemann argument.
4. **Additive mixed capacity theorem: novelty MEDIUM (6/10).** This is the most
   defensible mathematical delta. Hermite--Lindemann removes the algebraic
   additive contamination, then valuations remove the finite-support
   multiplier contamination, forcing the L-parts for outside primes to be
   independent.
5. **Assumption-to-escape certificate and machine-checkable ledger: novelty
   MEDIUM (6/10 as a research artifact).** Its value is clarity and falsifiability,
   not depth of any single lemma.

### D.2 Safe title

Recommended:

> **Finite Arithmetic Capacity under Additive Locally Constant,
> Good-Reduction Multiplier, and Algebraic-Action Readouts**

Shorter acceptable alternative:

> **A Finite Arithmetic-Capacity Certificate for Three Symplectic Clock
> Classes**

Avoid “escape trichotomy” in the title: the exits are not exhaustive or mutually
exclusive for arbitrary dynamics.

### D.3 Safe contribution statement

Use language of the following form:

> We formulate a fixed additive readout class that combines a finite-rank
> locally constant term, logarithms of algebraic moduli with fixed finite
> bad-prime support, and an algebraic action term. We prove that the number of
> exactly realized rational-prime logarithms is at most the rational rank plus
> the bad-prime count. The theorem is a scoped architecture certificate; it is
> not a no-go result for smooth symplectic dynamics.

Do not write “the first theorem,” “complete trichotomy,” “all finite-dimensional
symplectic maps fail,” or “prime clocks require infinite dimension.” Deninger
and Connes--Consani should be presented as positive arithmetic architectures
outside the declared finite class, not as confirmations of a universal
obstruction. Berry--Keating and Connes supply motivation and context, not a
claim that this candidate advances a Hilbert--Pólya construction.

## Final recommendation

**Proceed after mandatory repair.** The source-locked selector theorem is
mathematically correct but too easily read more broadly than proved. Promoting
the additive theorem to the main result resolves that ambiguity and supplies
the paper's strongest original delta. After the repairs in Section B, the
appropriate result label is `CAPACITY_BOUND_CERTIFIED`; without them, retain
`NARROW_OR_MERGE`.
