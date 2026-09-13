# Paper Plan

## Internal drafting receipt

This is an internal planning artifact, not manuscript prose. The first-stage
gate was checked before any manuscript input was read:

- canonical verdict: `RESULT_AWARE_HANDOFF_PASS`;
- handoff-review SHA-256:
  `3df02be2a4a629d9eeab89b9fe3cd30dc47892729603205d308ab6b9f5320e98`;
- result-aware scope SHA-256:
  `265fd1539d4957a78422c641c9508a432d769389fe7f78fb3cc5fdbf7c8b0307`;
- manuscript-lock SHA-256:
  `488c257f377de1cbc94855041c3e7930cbab3fdf1d390a310684a8fc9b0344cd`.

These receipts must not appear in the public article.

## Article identity and narrative lock

- **Safe title:** *Normalized Primitive-Cycle Covers in a Degenerating Hénon
  Family*
- **Type:** anonymous, proof-first specialist mathematics article
- **Audience:** algebraic and arithmetic dynamics readers comfortable with
  finite covers, normalization, dynatomic curves, and geometric monodromy
- **Venue:** no venue criteria are bound; use a format-neutral article design
- **Length:** 24--25 pages of mathematical content, including Appendices A--C
  and excluding references; working total 24.5 pages
- **Structure:** eight numbered sections plus Appendices A--C
- **Drafting order:** Sections 2--6 and Appendices A--C; then Section 7; then
  the Abstract, Section 1, and Section 8
- **Hierarchy:** PC1 is the theorem spine and carries most of the residual
  contribution; PC2 is a deliberately narrower second layer after the direct
  Morton comparison
- **Visuals:** zero experimental figures, zero result plots, and zero result
  tables. The default article is figure-free. At most one optional
  definition-and-theorem architecture diagram may be added under a later,
  separately reviewed expansion lock and must be labeled non-evidence.

**One-sentence contribution.** For fixed integers \(d,n\geq2\), we construct
the finite-locally-free geometrically integral normalization of the generic
actual-period block for
\(H_{a,c}(x,y)=(ay+x^d+c,x)\), identify its exact affine scalar fiber and
full symmetric cycle monodromy, and then show, as a narrower second layer,
that the orbit sum and pointwise derivative-return trace separately generate
the generic cycle field.

**What / Why / So What.**

- **What:** a normalized two-parameter primitive-point cover and its cycle
  quotient, with exact scheme-theoretic scalar degeneration, full \(S_r\)
  cycle monodromy, and two separately primitive cycle coordinates.
- **Why:** actual period is naturally isolated only inside the generic
  finite-etale algebra, while normalization need not commute with the
  specialization \(a=0\); the argument must also preserve the correct
  special-to-global monodromy direction and distinguish two meanings of
  trace.
- **So what:** the theorem gives a coherent integral model connecting scalar
  dynatomic geometry to this normalized Hénon family and packages the generic
  cycle field by two natural integral characteristic polynomials, without
  relabeling scalar or low-period precedents as contributions.

## Claims--evidence matrix and proof firewall

The sole theorem authority is the locked source proof conjoined with the
independent `SOURCE_LOCK_PASS`. Imported theorems have only the roles listed
below. The sealed audit and `RESULT_PASS` have no theorem authority.

| Article claim | Atomic claims | Mathematical evidence | Imported input and exact role | Main locus | R100 role |
|---|---:|---|---|---|---|
| **PC1-A: fixed algebra and actual-period field.** \(B_n\) is \(A\)-free of rank \(d^n\); \(E_n\) is one degree-\(\nu\) field. | C1--C5 | Bridges 1--3: monic coefficient-ring reduction, generic etaleness and the actual-period idempotent, then the Henselian connected lift. | Gao--Ou supply scalar geometric integrality and normality needed at the scalar input. | Sections 2--3; Appendix A | None |
| **PC1-B: normalized point cover and exact scalar fiber.** \(S\) is geometrically integral and finite locally free of rank \(\nu\), with \(S/aS\simeq D_n\). | C6--C10 | Bridges 4--8: finite normalization, Cohen--Macaulayness and miracle flatness, multiplicity-one \(a\)-adic divisor, \(R_0+S_1\) nilpotent exclusion, finite birational normality, and constants. | Gao--Ou supply normality/geometric integrality of \(D_n\); standard algebra sources supply only their named local results. | Section 4; Appendix A | None |
| **PC1-C: quotient and monodromy.** \(S_0\) is finite locally free of rank \(r\), has fiber \(D_n^{C_n}\), and has geometric cycle monodromy \(S_r\). | C11--C14 | Bridges 9--10: Reynolds splitting and arbitrary base change, followed by the correctly directed fundamental-group map and centralizer bound. | Morton (1998) supplies scalar \(C_n\wr S_r\); Fakhruddin supplies the characteristic-zero/geometric form; Gao (2016) is a cross-check. | Section 5; Appendix B | None |
| **PC2-A: separate non-base observables.** \(\tau,\rho\in S_0\), and each lies outside \(K\) when \(r>1\). | C15--C17 | Bridges 11--13: cyclic invariance, infinity branches, the word-sum comparison for \(\tau\), and the independently derived inverse-word-product comparison for \(\rho\). | Morton (1996) already gives scalar \(\rho\)-generation for all \(d,n\) and scalar \(\tau\)-generation for \(d=2\); this is direct prior art. | Sections 6.1--6.3; Appendix B | None |
| **PC2-B: field generation and integral polynomials.** \(K(\tau)=F=K(\rho)\), with basis-free monic characteristic polynomials over \(A\) irreducible of degree \(r\) over \(K\). | C18--C19 | Bridges 14--15: maximality of \(S_{r-1}<S_r\) applied separately, then the determinant line, top wedge, Vandermonde, and generic discriminant. | Morton remains credited for the scalar generators; no citation bypasses the two-parameter stabilizer proof. | Sections 6.4--6.5; Appendix C | None |
| **Rank-one boundary.** For \((d,n)=(2,2)\), \(\nu=2\), \(r=1\), \(\tau=a-1\), \(z_0z_1=(a-1)^2+c\), and \(\rho=4a^2-6a+4+4c\). | C20 | Bridge 16: direct cyclic-equation and matrix-product derivation; both multiplication polynomials are linear. | No imported theorem. | Section 6.6; Appendix C | None |

### Proof/R100 firewall

1. Theorems, lemmas, equations, proofs, contribution bullets, captions, and
   conclusions use only mathematical derivations and the assigned imported
   sources.
2. `RESULT_PASS` means bounded implementation consistency for one
   preregistered, seedless, sealed audit. It is not proof, theorem validation,
   scientific truth, novelty evidence, or priority evidence.
3. No runtime value, route output, hash, finite \((d,n)\) ledger, numerical
   root, parameter scan, prime/modulus check, or machine certificate may
   enter a theorem premise, equation justification, proof step, abstract,
   contribution bullet, figure, table, or positioning argument.
4. Machine disagreement could have challenged bounded implementation
   consistency; machine agreement cannot establish PC1, PC2, or any proof
   bridge.
5. The following exact public-facing paragraph is mandatory and appears
   exactly once in Section 8:

   > Separately from the proof, a preregistered, seedless exact audit compared
   > two independently implemented bounded routes in a single sealed run. An
   > independent integrity review returned `RESULT_PASS` only for bounded
   > implementation consistency. This computation is neither a proof nor a
   > validation of the theorems, which rest on the mathematical argument and
   > its independent source review. All available reviews used one model
   > family, so correlated-error risk remains and no cross-model validation is
   > claimed.

## Notation and formal statement lock

Fix \(d,n\geq2\) and put

\[
A=\mathbb Q[a,c],\qquad K=\mathbb Q(a,c),\qquad
H_{a,c}(x,y)=(ay+x^d+c,x).
\]

With cyclic indices modulo \(n\), define

\[
g_i=z_i^d+az_{i-1}+c-z_{i+1},\qquad
B_n=A[z_0,\ldots,z_{n-1}]/(g_0,\ldots,g_{n-1}),
\]

\[
\nu=\sum_{e\mid n}\mu(n/e)d^e,\qquad r=\nu/n.
\]

The four objects must never be conflated:

- \(B_n\): full cyclic fixed algebra, including lower periods;
- \(E_n\): generic clopen actual-exact-period block inside
  \(B_n\otimes_AK\), proved to be one field;
- \(S\): integral closure of \(A\) in \(E_n\);
- \(S_0=S^{C_n}\): cycle quotient, with
  \(F=\operatorname{Frac}(S_0)\).

On \(a=0\), set

\[
D_n=\mathbb Q[c,z]/(\Phi_{d,n}).
\]

Only affine quotient language is used. Define

\[
\tau=\sum_{i=0}^{n-1}z_i,\qquad
M_i=\begin{pmatrix}d z_i^{d-1}&a\\1&0\end{pmatrix},\qquad
\rho=\operatorname{tr}(M_{n-1}\cdots M_0).
\]

Here \(\rho\) is the pointwise matrix trace of the derivative return map,
neither a field trace nor the determinant \((-a)^n\).

### Main theorem architecture

**Theorem A (normalized primitive-cycle cover; PC1).** State one theorem with
six numbered clauses:

1. \(B_n\) is \(A\)-free of rank \(d^n\), with basis
   \(\prod_i z_i^{e_i}\), \(0\leq e_i<d\).
2. \(E_n\) is one degree-\(\nu\) field over \(K\).
3. \(S\) is geometrically integral and finite locally free of rank \(\nu\).
4. The exact scheme-theoretic scalar fiber is
   \(S/aS\simeq D_n\).
5. \(S_0\) is finite locally free of rank \(r\), invariants commute with
   arbitrary base change, and
   \(S_0/aS_0\simeq D_n^{C_n}\).
6. On a common dense finite-etale open, geometric monodromy on the \(r\)
   cycles is \(S_r\); when \(r=1\), this is explicitly the trivial group
   \(S_1\).

**Theorem B (two primitive cycle coordinates; PC2).** With
\(F=\operatorname{Frac}(S_0)\), state

\[
K(\tau)=F=K(\rho).
\]

For each \(s\in\{\tau,\rho\}\), define the multiplication characteristic
polynomial canonically on \(\bigwedge_A^rS_0\). State that it lies in \(A[T]\)
and is irreducible of degree \(r\) over \(K\). Refer to two separate non-base
propositions; do not package the observables as one calculation.

**Proposition C (complete rank-one boundary).** For \((d,n)=(2,2)\), state
and derive

\[
\nu=2,\qquad r=1,\qquad \tau=a-1,
\]

\[
z_0z_1=(a-1)^2+c,\qquad
\rho=4a^2-6a+4+4c.
\]

State immediately that both multiplication polynomials are linear and that
this case provides neither a non-base assertion nor nontrivial monodromy
evidence.

## Page budget

The budget includes the abstract and appendices and excludes references.

| Component | Pages | Running total |
|---|---:|---:|
| Abstract | 0.50 | 0.50 |
| Section 1. Introduction | 1.75 | 2.25 |
| Section 2. Family, objects, and theorem statements | 2.25 | 4.50 |
| Section 3. Fixed algebra and the generic actual-period field | 2.75 | 7.25 |
| Section 4. Relative normalization and the exact scalar fiber | 3.75 | 11.00 |
| Section 5. Cyclic quotient and geometric monodromy | 2.75 | 13.75 |
| Section 6. Two primitive cycle coordinates | 3.25 | 17.00 |
| Section 7. Prior work and precise positioning | 1.50 | 18.50 |
| Section 8. Limitations and conclusion | 0.75 | 19.25 |
| Appendix A. Local algebra of the normalization and scalar divisor | 2.25 | 21.50 |
| Appendix B. Scalar restriction and infinity-branch lemmas | 1.75 | 23.25 |
| Appendix C. Determinant lines and the rank-one calculation | 1.25 | 24.50 |

## Section-by-section plan

### Abstract (180--220 words; 0.50 page)

Use a five-sentence proof-centered abstract:

1. Open with the exact family and normalized actual-period construction.
2. State the difficult PC1 conclusion: finite local freeness across \(a=0\)
   and the exact reduced fiber \(S/aS\simeq D_n\), rather than assumed
   commutation of normalization and base change.
3. Name the proof mechanism compactly: generic idempotent, Henselian lift,
   multiplicity-one scalar divisor, finite-birational comparison, and
   Reynolds quotient.
4. State full \(S_r\) cycle monodromy.
5. Present PC2 as the narrower final result: \(\tau\) and the pointwise
   derivative-return trace \(\rho\) separately generate \(F\), with
   basis-free integral characteristic polynomials and the explicit linear
   \((2,2)\) boundary.

The abstract contains no citations, priority language, audit statement,
experiment language, internal status term, or claim outside PC1/PC2.

### Section 1. Introduction (1.75 pages)

**Opening.** Begin with the degeneration
\(H_{a,c}|_{a=0}=(x^d+c,x)\) and the problem of carrying scalar actual-period
geometry into an integral two-parameter model. Distinguish the generic
actual-period block from the full fixed algebra in the first paragraph.

**Three obstacles.**

- Actual period is clopen only on the generic finite-etale locus; it cannot
  be declared an everywhere embedded family.
- Normalization does not automatically commute with \(a=0\); hidden
  multiplicity and nilpotents must be excluded.
- Scalar monodromy supplies a lower bound on global monodromy only through
  the correctly directed restriction map.

**Approach.** Preview

\[
B_n\longrightarrow E_n\longrightarrow S\longrightarrow S_0
\longrightarrow(\tau,\rho),
\]

while stating that the arrows abbreviate different constructions, not one
everywhere exact-period subscheme.

**Exactly three contribution bullets.**

1. The finite-flat normalized primitive-point cover and exact scalar fiber.
2. The finite-flat cycle quotient and full \(S_r\) geometric monodromy.
3. The narrower two-coordinate theorem, with separate \(\tau\) and \(\rho\)
   arguments and the explicit \((2,2)\) exception.

State early that scalar dynatomic geometry and wreath monodromy are imported,
that Morton already proves scalar \(\rho\)-generation in every degree and
scalar \(\tau\)-generation in degree two, and that PC1 carries most residual
weight. By the end, a skim reader must know the family, four distinct
objects, exact fiber, monodromy group, narrow PC2 status, and non-computational
proof authority.

### Section 2. Family, objects, and theorem statements (2.25 pages)

#### 2.1 Orbit coordinates and full fixed algebra

Fix the cyclic convention and define \(g_i\), \(B_n\), \(\nu\), \(r\), and
the shift \(\sigma\). State that \(B_n\) includes lower periods.

#### 2.2 Generic actual-period block and relative models

Define \(E_n\) only after passage to \(B_n\otimes_AK\). Define \(S\), \(S_0\),
and \(F\). Define the scalar affine algebras \(D_n\) and \(D_n^{C_n}\), with
no projective-compactification implication.

#### 2.3 Observables

Define \(\tau\), the ordered matrices \(M_i\), and
\(\rho=\operatorname{tr}(M_{n-1}\cdots M_0)\). Include the sign/order check

\[
\operatorname{tr}(M_1M_0)=u_0u_1+2a.
\]

#### 2.4 Main results

State Theorems A and B and Proposition C in the locked forms. Follow each
statement with a proof-architecture paragraph so the main text never leaves
bare theorems whose logic exists only in appendices.

### Section 3. Fixed algebra and generic actual-period field (2.75 pages)

#### 3.1 Monic cyclic Groebner basis — Bridge 1

Choose a graded order, record
\(\operatorname{LM}(g_i)=z_i^d\), use the monic product criterion over the
coefficient ring, and prove existence and uniqueness of coefficient-ring
remainders. Display the standard-monomial basis and rank \(d^n\). This is an
integral statement, not a generic point count.

#### 3.2 Generic etaleness and actual-period idempotent — Bridge 2

Use the scalar generic fiber to locate an etale fiber of the discriminant.
Isolate the Galois-stable clopen actual-period subset only in the generic
finite-etale algebra and derive
\(\nu=\sum_{e\mid n}\mu(n/e)d^e\) by Mobius inversion. Defer the one-field
conclusion.

#### 3.3 Henselian connected lift — Bridge 3

Pass to the henselization of the \(a\)-adic DVR, lift the scalar exact-factor
idempotent, prove connectedness from its field residue algebra, and identify
the lift with the generic actual-period block by excluding specialization of
lower-period closed loci. Use faithful flatness to exclude a product
decomposition of \(E_n\). Appendix A gives the line-by-line finite-etale
details.

### Section 4. Relative normalization and exact scalar fiber (3.75 pages)

This is the center of PC1 and receives the largest proof budget.

#### 4.1 Finite normalization — Bridge 4

Use finite type over \(\mathbb Q\), excellence, the Nagata property, and
finite normalization to prove \(S\) finite over \(A\).

#### 4.2 Cohen--Macaulayness and miracle flatness — Bridge 5

Record that the normal two-dimensional domain \(S\) is Cohen--Macaulay.
Establish local dimension equality over the regular base and
zero-dimensional fibers before miracle flatness. Conclude finite local
freeness of rank \(\nu\), with no every-fiber smoothness or etaleness claim.

#### 4.3 Scalar divisor and nilpotent exclusion — Bridge 6

Extract the unique height-one prime above \((a)\), ramification index \(e=1\),
residue degree \(\nu\), and
\(\operatorname{div}_S(a)=P\) with multiplicity one. Prove that \(S/aS\) is
\(S_1\) by Cohen--Macaulayness and \(R_0\) at its unique minimal prime;
deduce reducedness and exclude nilpotents supported at closed points. Retain
the flat-rank argument only as a redundant check.

#### 4.4 Exact scalar fiber — Bridge 7

Construct the finite map \(D_n\to S/aS\), identify the common fraction field,
and use normality of \(D_n\) to conclude

\[
S/aS\simeq D_n.
\]

Say explicitly that the divisor, reducedness, and finite-birational
normality chain proves this equality; normalization/base-change compatibility
was not assumed.

#### 4.5 Constants and geometric integrality — Bridge 8

Inject algebraic constants of \(E_n\) into \(\operatorname{Frac}(D_n)\), use
geometric integrality of \(D_n\) to show that \(\mathbb Q\) is algebraically
closed in \(E_n\), and combine this with characteristic-zero geometric
reducedness to prove geometric integrality of \(S\). Appendix A expands the
valuation descent, \(R_0+S_1\) argument, and constants lemma.

### Section 5. Cyclic quotient and geometric monodromy (2.75 pages)

#### 5.1 Reynolds invariants and base change — Bridge 9

Extend the faithful generic shift to \(S\) and apply

\[
\mathcal R=\frac1n\sum_{j=0}^{n-1}\sigma^j.
\]

Show that its image is \(S_0\), images of this idempotent commute with
arbitrary tensor base change, and \(S_0\) is finite locally free of rank
\(r\). Deduce

\[
S_0/aS_0\simeq D_n^{C_n}.
\]

Do not infer a free action or smooth quotient on every fiber.

#### 5.2 Special-line to global monodromy — Bridge 10

Choose a common dense finite-etale open \(U\) and scalar good locus \(U_0\).
Display the direction

\[
\pi_1\bigl((U_0)_{\overline{\mathbb Q}}\bigr)
\longrightarrow
\pi_1\bigl(U_{\overline{\mathbb Q}}\bigr)
\longrightarrow S_r.
\]

State that the scalar image is a subgroup of the global image. The
Morton--Fakhruddin scalar image is already \(S_r\) on cycles, while the
global cycle action is contained in \(S_r\), hence equality follows. At
point level, the time-shift centralizer supplies the upper bound
\(C_n\wr S_r\), but this is auxiliary rather than an advertised additional
claim. State \(S_1\) as trivial when \(r=1\). Appendix B records the source
extraction and base-point compatibility.

### Section 6. Two primitive cycle coordinates (3.25 pages)

Introduce PC2 as a narrower consequence of PC1, not as a new scalar
coordinate theory.

#### 6.1 Cyclic invariance — Bridge 11

Put \(\tau\) and \(\rho\) in \(S_0\). For \(\rho\), use cyclic rotation of
the ordered derivative product and matrix-trace cyclicity. Repeat its
pointwise trace category and the \(n=2\) order/sign check.

#### 6.2 Scalar infinity branches — Bridge 12

On \(a=0\), use

\[
c=-q^{-d},\qquad z_i=q^{-1}v_i,\qquad
\epsilon=q^{d-1},\qquad v_i^d=1+\epsilon v_{i+1}.
\]

For primitive root-of-unity words, derive independently

\[
\tau=q^{-1}\left(\sum_i\omega_i+O(\epsilon)\right)
\]

and

\[
\rho=d^nq^{-n(d-1)}
\left(\prod_i\omega_i^{-1}+O(\epsilon)\right).
\]

The word sum and inverse product must remain visibly different invariants.

#### 6.3 Separate non-base propositions — Bridge 13

Write one proposition for each observable.

- For \(d\geq3\), compare
  \((1,\ldots,1,\zeta)\) and
  \((1,\ldots,1,\zeta^2)\). Use only sums for \(\tau\), only inverse
  products for \(\rho\).
- For \(d=2,n\geq3\), compare a word with one minus sign and a word with two
  adjacent minus signs. Again keep the sum and product deductions separate.
- State the integrality intersection \(S_0\cap K=A\) used to pass from
  distinct scalar branches to \(\tau,\rho\notin K\).
- Exclude \(r=1\) before either non-base assertion.

#### 6.4 Full-symmetric stabilizer step — Bridge 14

Only after both non-base propositions, pass to a Galois closure with group
\(S_r\). A selected cycle has stabilizer \(S_{r-1}\); maximality of
\(S_{r-1}<S_r\) makes each observable stabilizer exactly \(S_{r-1}\).
Derive the two generation equalities separately, then combine them as
\(K(\tau)=F=K(\rho)\). State that non-base behavior alone is insufficient.

#### 6.5 Determinant line and irreducibility — Bridge 15

For \(s\in\{\tau,\rho\}\), define

\[
\chi_s(T)=\det(T\operatorname{id}-m_s)
\]

through \(\bigwedge_A^rS_0\). Over \(K\), use
\(1\wedge s\wedge\cdots\wedge s^{r-1}\ne0\) to identify the characteristic
and minimal polynomials. Record the Vandermonde and nonzero discriminant only
as generic separability; make no fiberwise promotion.

#### 6.6 Complete \((2,2)\) boundary — Bridge 16

Subtract the cyclic equations to obtain
\((z_0-z_1)(z_0+z_1-(a-1))=0\), restrict to the generic actual two-cycle
block, and derive

\[
\nu=2,\quad r=1,\quad \tau=a-1,\quad
z_0z_1=(a-1)^2+c,
\]

\[
\rho=4z_0z_1+2a=4a^2-6a+4+4c.
\]

End with the linear characteristic polynomials and the statement that this
boundary is not nontrivial monodromy evidence.

### Section 7. Prior work and precise positioning (1.50 pages)

Organize by mathematical role, not as a paper-by-paper list.

#### 7.1 Scalar geometry and monodromy

Synthesize Gao--Ou, Morton (1998), Fakhruddin, Gao (2016), Hutz, and
Doyle--Poonen. Attribute scalar smoothness/geometric irreducibility and the
full scalar wreath theorem exactly. Position PC1 as the combined relative
normalization, exact two-parameter degeneration, affine quotient, and correct
special-to-global transfer, not any scalar ingredient alone.

#### 7.2 Scalar generators and trace-spectrum adjacency

Give Morton (1996) the direct collision: scalar \(\rho\) generates for all
\(d,n\), while scalar \(\tau\) generates for \(d=2\). Cite the 2011
corrigendum with its limited finite-characteristic scope. Contrast this with
the residual PC2 content: two-parameter lift, uniform \(d\geq3\) \(\tau\)
argument, and basis-free integral polynomials.

Distinguish Cantat--Dujardin's formal-period trace multisets over finitely
many periods and finite-ambiguity parameter reconstruction from one fixed
actual-period cycle field and one cycle value. Neither theorem implies the
other.

#### 7.3 Low-period carriers and neighboring Hénon work

Use Endler--Gallas (2002, 2004) and Zhang (2014) to disclaim invention of
orbit-sum carriers, stability carriers, and cyclic-polynomial elimination.
Use Friedland--Milnor to delimit the ambient Hénon category. Arai and
Ji--Xie may appear only if their symbolic-monodromy and current
dynatomic-geometry distinctions remain useful. End with bounded positioning:
the article proves the exact conjunction and makes no priority inference from
a no-hit search.

### Section 8. Limitations and conclusion (0.75 page)

Use three short paragraphs:

1. Restate PC1 as the dominant theorem and PC2 as the narrower coordinate
   layer, without copying the Introduction bullets.
2. State the boundaries: fixed normalized family, generic actual-period
   block, affine quotient, dense finite-etale open, no every-fiber
   regularity, and no specialized irreducibility claim.
3. Insert the exact audit paragraph from the firewall here, exactly once in
   the article. It must not appear in the abstract, claims, proofs, figures,
   tables, or novelty positioning. End with one restrained direction:
   compactifications or broader Hénon families need new arguments and are
   not consequences of the theorem.

## Appendix contracts

### Appendix A. Local algebra of the normalization and scalar divisor (2.25 pages)

- Expand Henselian finite-etale lifting and identification with \(E_n\).
- Give the excellence/Nagata/finite-normalization chain.
- Prove local dimension equality and miracle flatness.
- Give valuation descent, \(ef=\nu\), the unique height-one prime, and
  coefficient-one divisor.
- Prove \(R_0+S_1\) reducedness, including closed-point nilpotent exclusion.
- Complete finite birational normality and the constants argument.

Appendix A expands Bridges 3--8; it does not hide them from Sections 3--4.

### Appendix B. Scalar restriction and infinity-branch lemmas (1.75 pages)

- State the exact-period factor of scalar \(C_n\wr S_r\) and Fakhruddin's
  geometric constant-field role.
- Fix compatible base points and prove
  \(\pi_1(U_0)\to\pi_1(U)\).
- Construct formal infinity branches indexed by primitive words.
- Prove word primitivity for the \(d\geq3\) and binary comparison pairs.
- Derive the \(\tau\) word sum and \(\rho\) inverse product independently.
- Record why \((2,2)\) is the only \(r=1\) case.

Appendix B expands Bridges 10 and 12--13 and contains no computational data.

### Appendix C. Determinant lines and rank-one calculation (1.25 pages)

- Give the basis-free determinant construction on
  \(\bigwedge_A^rS_0\), nonzero power wedge, Vandermonde, and discriminant.
- State the Gauss-lemma passage from monic coefficients in \(A\) and generic
  irreducibility in \(K[T]\).
- Reproduce the ordered \(n=2\) matrix multiplication.
- Give the complete direct \((2,2)\) sum, product, and \(\rho\) calculation,
  followed by the linear-polynomial and trivial-monodromy boundary.

Appendix C expands Bridges 15--16 and makes no fiberwise claim.

## Sixteen-bridge visibility ledger

| Order | Bridge | Main location | Expansion | Noncollapse check |
|---:|---|---|---|---|
| 1 | Monic cyclic Groebner basis | 3.1 | -- | coefficient-ring division and rank \(d^n\) explicit |
| 2 | Generic etaleness and actual-period idempotent | 3.2 | -- | generic clopen block only; Mobius degree shown |
| 3 | Henselian connected lift | 3.3 | Appendix A | identify the lift before concluding field |
| 4 | Finite normalization | 4.1 | Appendix A | excellence and Nagata chain named |
| 5 | Cohen--Macaulayness and miracle flatness | 4.2 | Appendix A | local dimensions and local freeness shown |
| 6 | \(a\)-adic divisor and nilpotent exclusion | 4.3 | Appendix A | unique prime, \(e=1\), multiplicity one, \(R_0+S_1\) |
| 7 | Exact scalar fiber | 4.4 | Appendix A | finite birational normality after Bridge 6 |
| 8 | Constants and geometric integrality | 4.5 | Appendix A | constants inject into scalar function field |
| 9 | Cyclic invariants and base change | 5.1 | -- | Reynolds projector and arbitrary base change |
| 10 | Special-line to global monodromy | 5.2 | Appendix B | subgroup direction and centralizer upper bound |
| 11 | Cyclic invariance of observables | 6.1 | Appendix C for \(n=2\) | ordered product and trace category fixed |
| 12 | Scalar infinity branches | 6.2 | Appendix B | sum and inverse product derived independently |
| 13 | Separate non-base proofs | 6.3 | Appendix B | degree cases and observables remain separate |
| 14 | Full-symmetric stabilizer step | 6.4 | -- | only after both non-base results |
| 15 | Determinant line and irreducibility | 6.5 | Appendix C | wedge, Vandermonde, generic discriminant |
| 16 | Degree-one boundary | 6.6 | Appendix C | exact formulas, linear polynomials, non-evidence |

## Figure and table policy

### Current inventory

- Experimental figures: **0**
- Numerical or empirical tables: **0**
- Machine-certificate displays: **0**
- Architecture diagrams in this stage: **0**

The article is logically complete without a figure. No visual asset is
created under the present authorization.

### Optional single diagram after separate authorization

If a later expansion lock authorizes one visual, it may be a single
grayscale vector diagram after Section 2.4 with this exact contract:

- **Purpose:** definitions and theorem architecture only; no data, empirical
  agreement, proof-completion badge, or evidentiary encoding.
- **Layout:** two columns, “marked points” and “cycles”; three rows,
  “generic,” “integral model,” and “scalar fiber.”
- **Marked-point nodes:** \(B_n\otimes_AK\supset E_n\);
  \(S=\overline A^{\,E_n}\); \(S/aS\simeq D_n\).
- **Cycle nodes:** \(F=E_n^{C_n}\); \(S_0=S^{C_n}\);
  \(S_0/aS_0\simeq D_n^{C_n}\).
- **Connectors:** horizontal labels “\(C_n\)-fixed subring”; vertical labels
  “integral model” and “modulo \(a\).” The extraction
  \(B_n\otimes_AK\supset E_n\) is labeled “generic clopen idempotent,”
  preventing an everywhere embedded-family suggestion.
- **Monodromy annotation:** “geometric monodromy \(S_r\) on a common dense
  finite-etale open,” with “\(S_1\) trivial” beneath.
- **Style:** black, dark gray, and one colorblind-safe blue accent; no
  gradient, icon, decorative title, numeric result, or internal identifier;
  vector output and grayscale legibility.
- **Exact public caption:**

  > **Figure 1. Definition-and-theorem architecture of the normalized
  > primitive-cycle cover.** The generic actual-period field \(E_n\) is cut
  > out only after passing to the generic finite-etale algebra
  > \(B_n\otimes_AK\); \(S\) is the integral closure of \(A\) in \(E_n\), and
  > \(S_0=S^{C_n}\). The theorem identifies the scalar fibers as
  > \(S/aS\simeq D_n\) and \(S_0/aS_0\simeq D_n^{C_n}\) and gives geometric
  > cycle monodromy \(S_r\) on a common dense finite-etale open. The diagram
  > records definitions and theorem organization only; it is not evidence
  > for any claim.

No second diagram is permitted. If the contract cannot be met exactly, keep
the article figure-free.

## Bibliography key plan

Bibliographic data must come only from the locked citation audit, never from
memory. Prefer the recorded published version to a preprint.

| Key | Exact article role | Planned locus |
|---|---|---|
| `gao-ou-2014-dynatomic` | scalar smoothness, geometric irreducibility, normality | Sections 1, 4, 7; Appendix A |
| `morton-1998-periodic-galois` | primary all-degree scalar wreath theorem | Sections 1, 5, 7; Appendix B |
| `fakhruddin-2014-generic-endomorphisms` | characteristic-zero/geometric form | Sections 5, 7; Appendix B |
| `gao-2016-preperiodic-dynatomic` | later all-degree cross-check, not primary proof | Section 7 |
| `morton-1996-algebraic-curves` | direct scalar \(\rho\)-generator for all \(d,n\), scalar \(\tau\)-generator for \(d=2\) | Sections 1, 6, 7 |
| `morton-2011-corrigendum` | bounded correction accompanying Morton (1996) | Section 7 |
| `schleicher-2017-internal-addresses` | optional quadratic historical context | Section 7 |
| `doyle-poonen-2020-gonality` | scalar quotient/modular-curve context | Section 7 |
| `hutz-2010-dynatomic-cycles` | formal-versus-actual warning | Sections 1, 3, 7 |
| `friedland-milnor-1989-plane-automorphisms` | ambient Hénon category | Sections 1, 7 |
| `cantat-dujardin-2026-multiplier-rigidity` | formal-period trace-spectrum parameter reconstruction | Sections 1, 7 |
| `endler-gallas-2002-arithmetical-signatures` | period-four orbit-sum precedent | Section 7 |
| `endler-gallas-2004-ghost-orbits` | period-six carrier/stability precedent | Section 7 |
| `zhang-2014-cycles-logistic-map` | bounded-period cyclic-polynomial precedent | Section 7 |
| `arai-2016-henon-monodromy` | optional symbolic-monodromy distinction | Section 7 if used |
| `ji-xie-2026-genus-gonality` | optional current dynatomic adjacency | Section 7 if used |
| `stacks-07qw`, `stacks-07qv`, `stacks-035s` | excellence, Nagata property, finite normalization | Section 4; Appendix A |
| `stacks-033p`, `stacks-00r4` | normal surfaces, \(R_0+S_1\), miracle flatness | Section 4; Appendix A |
| `stacks-0d49`, `stacks-09e4`, `stacks-09e8` | Henselian lifting and DVR ledger | Sections 3--4; Appendix A |
| `stacks-0309`, `stacks-037p`, `stacks-0322`, `stacks-0fwf` | finite-birational equality and geometric constants | Section 4; Appendix A |

Citation rules:

1. Distinguish Morton (1996) and Morton (1998) by year, title context, and
   theorem role whenever ambiguity is possible.
2. Pair Morton (1996) with the 2011 corrigendum when discussing corrected
   scope.
3. Attribute the wreath theorem primarily to Morton (1998), use Fakhruddin
   for geometric constants, and label Gao (2016) corroboration.
4. Cite Gao--Ou only for scalar geometry.
5. Describe Cantat--Dujardin with formal-period multisets, finitely many
   periods, finite ambiguity, and parameter reconstruction.
6. Give Endler--Gallas and Zhang explicit collision credit.
7. State Lau--Schleicher/Bousch history only through the checked source chain
   unless separately authorized bibliographic records are supplied.

## Anonymous and deterministic style

### Anonymity

- Use an anonymous author placeholder only. Include no name, affiliation,
  email, ORCID, acknowledgment, funding identifier, repository URL, personal
  homepage, institution-specific phrase, or identifying PDF metadata.
- Include no acknowledgments section in the anonymous draft.
- Public prose contains no internal directory, filename, hash, workflow row,
  batch identifier, model name, or private review logistics. The single
  bounded-audit paragraph is the maximum provenance disclosure.

### Deterministic mathematical prose

- Keep one symbol per object: \(B_n,E_n,S,S_0,F,D_n,\tau,\rho\).
- Reserve “actual exact period” for the generic clopen block; use “formal
  period” for the dynatomic special-fiber warning.
- Reserve \(\rho\)'s “trace” for matrix trace of the pointwise derivative
  return; spell out “field trace” for the other operation.
- Use “finite etale” only on an explicitly named dense open.
- Number theorem environments by section and use stable semantic equation
  labels. State each lemma before the theorem step that consumes it.
- Begin proof paragraphs with their purpose and end on the mathematical
  conclusion. Prefer “define,” “prove,” “identify,” and “deduce.”
- Preserve proof order 1--16 even when details move to appendices.
- Use no colored theorem boxes, confidence labels, or manuscript version
  dates.

## Forbidden overclaims

These restrictions apply to title, abstract, theorems, proofs, captions,
related work, conclusion, appendices, and any later supplementary prose.

1. Do not identify formal dynatomic period with actual exact period on every
   special fiber.
2. Do not describe an everywhere embedded primitive subscheme of
   \(\operatorname{Spec}B_n\).
3. Do not say normalization commutes with \(a=0\) without the same-rank,
   divisor, and nilpotent-exclusion proof.
4. Do not claim every-fiber smoothness, reducedness, etaleness, or a free
   cyclic torsor for \(S\) or \(S_0\).
5. Do not call the affine scalar quotient a projective compactification.
6. Do not reverse the monodromy lower-bound direction: the scalar image is a
   subgroup of the global image.
7. Do not infer primitivity from non-base behavior without full \(S_r\) and
   maximality of \(S_{r-1}\).
8. Do not call \(\rho\) a field trace or identify it with \((-a)^n\).
9. Do not assert \(\tau\notin K\), \(\rho\notin K\), or nontrivial monodromy
   when \(r=1\).
10. Do not extend PC1/PC2 to arbitrary generalized Hénon maps or polynomial
    automorphisms.
11. Do not treat a finite case table, root ledger, parameter scan,
    prime/modulus check, or machine certificate as proof.
12. Do not claim scalar \(\rho\)-primitivity, scalar quadratic
    \(\tau\)-primitivity, or formal trace-spectrum rigidity as contributions.
13. Do not claim invention of dynatomic curves, wreath monodromy, orbit-sum
    carriers, stability carriers, cyclic-polynomial elimination,
    normalization, Reynolds averaging, determinant lines, or
    primitive-element methods.
14. Do not use priority or universal-absence phrases such as “first,”
    “previously unknown,” “no prior work,” “method novelty,” or “we introduce
    the trace/orbit-sum carrier.”
15. Do not imply that novelty dissent, same-family correlated-error risk, or
    unavailable venue criteria have been resolved.
16. Do not promote generic irreducibility or a nonzero generic discriminant
    to every specialized characteristic polynomial.
17. Do not describe `RESULT_PASS` as machine proof, theorem validation,
    scientific validation, or novelty evidence.

## Author-side acceptance checks

A later draft passes the structural check only if:

- the title is exact and the author block anonymous;
- the abstract and three Introduction bullets map to the claims matrix;
- PC1 remains dominant and PC2 explicitly narrowed after Morton;
- \(B_n,E_n,S,S_0\) remain distinct;
- all sixteen bridges occur in order, with Bridges 6--7 and 10 visible in the
  main text;
- both non-base proofs stay separate until the common stabilizer step;
- the monodromy map is displayed in the correct direction;
- the complete \((2,2)\) boundary appears in Section 6 and Appendix C;
- no experimental figure, result table, or machine-evidence display exists;
- any optional diagram obeys the exact contract and has prior authorization;
- the bounded-audit paragraph appears exactly once in Section 8 and nowhere
  in the abstract, claims, proofs, figures, tables, or novelty positioning;
- citations follow the fixed keys and collision roles;
- public prose contains no local path, hash, workflow row, internal status,
  identity clue, or unresolved drafting marker;
- content remains within 24--25 pages excluding references;
- every forbidden-overclaim check passes.

## Required gates after this plan

No further publication artifact is produced in this stage. Subsequent actions
must occur in this order:

1. **Independent plan review.** A fresh role-separated reviewer binds this
   plan's exact SHA-256 and checks the claims matrix, page arithmetic,
   eight-section plus three-appendix structure, all sixteen bridges, PC1/PC2
   hierarchy, exact \((2,2)\) boundary, citation collisions, proof/R100
   firewall, visual policy, anonymity, and overclaim prohibitions. The
   reviewer performs no scientific recomputation and does not rewrite the
   plan it judges.
2. **Separate publication-expansion lock.** After a passing plan review, a
   new explicit lock enumerates every additional manuscript read and write,
   binds the reviewed plan hash, preserves theorem and machine firewalls, and
   states separately whether article source, bibliography, diagram assets,
   build products, and PDF compilation are authorized.
3. **Draft expansion.** Only after that independently reviewed lock may the
   article source and bibliography be drafted. The figure stays omitted
   unless the new lock expressly authorizes the one contracted diagram.
4. **Later finalization.** Compilation, final PDF production, identity
   release, submission, and supplementary artifacts require explicit
   downstream authority; none is inferred from this plan.
