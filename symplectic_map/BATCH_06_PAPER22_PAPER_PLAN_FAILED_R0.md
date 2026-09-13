# Paper Plan

**Title**: Cubic Spectral Collapse for Endpoint-Spiked Hamiltonian Product Shears: Sharp Selector Thresholds in Arbitrary Mode Number  
**Author**: Anonymous  
**Type**: proof-first mathematics / algebraic dynamics  
**Intended format**: local proof-first mathematical article; not an ICLR, ICML, or NeurIPS submission  
**Date**: 2026-08-24  
**One-sentence contribution**: For the displayed endpoint-spiked Hamiltonian product shears in every mode number (r\ge4) and every (g\ge2r+1) over an arbitrary characteristic-zero field, we prove that the apparent (r)-dimensional degree system splits off an ((r-3))-dimensional unit eigenspace, so all nontrivial growth descends exactly to one explicit three-dimensional quotient governed by a cubic.  
**Page contract**: 26.5 substantive pages target; preferred band 24--28 and hard band 22--30, measured from the Abstract through the end of the Conclusion, with references excluded  
**Section count**: 8 numbered sections, with the Abstract planned separately as §0

## Narrative and Public-Article Contract

The article tells one proof story: literal gradient supports determine two
phase matrices; two strict selectors and one invariant cone turn those formal
matrices into the exact degree recurrence; a visible last coordinate turns the
recurrence into the ordinary degree; and middle-coordinate symmetry reduces
the entire nontrivial spectrum to three dimensions.

By the end of the Introduction, a reader must know:

- **What**: the exact degree formula, the ((r-3))-dimensional unit space, the
  explicit three-dimensional quotient, and its cubic characteristic factor;
- **Why**: a formal max-plus or matrix calculation is insufficient until both
  selectors, carried coordinates, leading-form survival, and degree
  visibility are proved;
- **So what**: increasing the number of Hamiltonian modes enlarges only a
  semisimple unit sector and does not enlarge the nontrivial spectral degree
  of this family.

The title, Abstract, and first two pages must carry that complete message.
There is intentionally no hero figure: the central object is an exact proof
chain, and a decorative schematic would be weaker than the displayed theorem,
the support-row ledger, and the three-dimensional quotient.

The public article must contain no local project names or numbers, filesystem
paths, hashes, PASS labels, agents, dashboards, source/publication locks,
collision matrices, permission history, or other governance provenance.
Internal predecessor records have no public citation role. Low-mode overlap
may be stated only as a mathematical specialization, and no citation to an
unpublished local object may be invented.

## Planning-Only Claims--Evidence Matrix

This matrix controls drafting but is not a table for the public article. Every
evidence item is a hand proof that must appear in the main body; no citation,
experiment, plot, numerical example, or computer certificate proves a row.

| ID | Locked claim | Main-body evidence | Planned location |
|---|---|---|---|
| C1 | The displayed (S), (T), and (F=T\circ S) are polynomial automorphisms preserving the standard symplectic form. | Explicit gradients, subtraction inverses, triangular Jacobians, and Hessian symmetry. | §2 |
| C2 | Literal gradient supports give (M=2\mathbf1\mathbf1^{\mathsf T}-I), the endpoint-modified phase matrices (A,B), and (C=BA), with exactly two competitive rows. | Complete hand-typeset support-row ledger and row-by-row matrix derivation. | §3 |
| C3 | The region (x_i\ge1), (sigma=\sum_{i=2}^r x_i<(h-1)/2) is an explicit sufficient invariant selector cone containing the ordinary-degree seed. | Both selector margins, seed check, every lower wall, the open height wall, and the least-parameter audit. | §§3--4 |
| C4 | Actual coordinate degrees obey (v_{n+1}=Au_n) and (u_{n+1}=Cu_n), and the chosen leading forms cannot cancel. | Phase-labelled carried-coordinate induction and the integral-domain highest-homogeneous-form argument. | §5 |
| C5 | The four-nonzero-coefficient extension holds only on the same fixed supports. | Nonzero derivative scalars in characteristic zero plus strict uniqueness of the selected leading form. | §5 |
| C6 | The last (q)-coordinate is strictly visible for (n\ge1), (deg(F^n)=e_r^{\mathsf T}C^n\mathbf1) for (n\ge0), and (lambda_1(F)=\rho(C)). | (C-A>0), last-row difference bounds, the tied (n=0) audit, and Perron--Frobenius visibility. | §6 |
| C7 | (C) is the identity on an ((r-3))-dimensional space and has the displayed three-dimensional equal-middle restriction (Q). | The direct invariant splitting (K^r=U\oplus E), exact actions of (A,B,C), and row computation in the declared coordinate convention. | §7 |
| C8 | (chi_C(t)=(t-1)^{r-3}P_{m,h}(t)), (P_{m,h}(1)\ne0), the unit eigenvalue has exact multiplicity (r-3), and the exact degree sequence has a cubic annihilator. | Trace, principal-minor sum, determinant, direct-sum factorization, evaluation at one, and Cayley--Hamilton on (E). | §7 |
| C9 | (g=2r) is sharp only for the ordinary seed and selected strict face, and the formal (r=3) substitution is only a low-mode consistency check. | Exact first-score difference (g-2r), cone-height equality, and literal (m=1) substitution. | §8 |

The proof dependency order is fixed:



[
 C1\longrightarrow C2\longrightarrow C3\longrightarrow(C4,C5)
 \longrightarrow C6\longrightarrow(C7,C8)\longrightarrow C9.
]

The manuscript may preview later conclusions, but it may not use a later
claim to prove an earlier one or treat a formal matrix as an already verified
degree recurrence.

## Frozen Theorem and Notation

Let (K) be an arbitrary field of characteristic zero, let (r\ge4), and
let (g\ge2r+1). Set

[
 V_{r,g}(q)=\prod_{i=1}^r q_i^2+q_1^g,qquad
 W_{r,g}(p)=\prod_{i=1}^r p_i^2+p_r^g,
]

[
 S(q,p)=(q,p+\nabla V_{r,g}(q)),qquad
 T(q,p)=(q+\nabla W_{r,g}(p),p),qquad F_{r,g}=T\circ S.
]

Put (h=g-1), (m=r-2), and

[
 M=2\mathbf1\mathbf1^{\mathsf T}-I_r.
]

The matrix (A) is (M) with its first row replaced by
(h e_1^{\mathsf T}), the matrix (B) is (M) with its last row replaced
by (h e_r^{\mathsf T}), and (C=BA). For (u>0), define only

[
 x_i=\frac{u_i}{u_1}\quad(2\le i\le r),qquad
 \sigma=\sum_{i=2}^r x_i.
]

The cone is always named the **explicit sufficient invariant selector cone**

[
 \mathcal K_{r,g}=
 \left\{u>0:x_i\ge1\ (2\le i\le r),\quad
 \sigma<\frac{h-1}{2}=\frac{g-2}{2}\right\}.
]

The word “sufficient” is mandatory. The article must never call this cone
maximal, necessary, unique, exact, or a classification.

The spectral notation is

[
 U=\left\{z\in K^r:z_1=z_r=0,\quad
 \sum_{i=2}^{r-1}z_i=0\right\},qquad
 E=\{(a,b,\ldots,b,c)^{\mathsf T}:a,b,c\in K\}.
]

In the fixed coordinate convention
((a,b,c)\mapsto(a,b,\ldots,b,c)), with exactly (m) common middle
coordinates, the restriction of (C) to (E) is

[
 Q_{m,h}=
 \begin{pmatrix}
 h+4m+4 & 2m(2m+1) & 2(2m+1)\\
 2h+4m+2 & 4m^2+1 & 4m\\
 2h & 2mh & h
 \end{pmatrix}.
]

The locked cubic is

[
 \begin{aligned}
 P_{m,h}(t)={}&t^3-(2h+4m^2+4m+5)t^2\\
 &+(h^2-8hm(m+1)+2h+4)t-h^2(2m+1)^2.
 \end{aligned}
]

## Structure

### §0 Abstract — 0.5 pages

- Open with the achieved theorem, not generic field background: the displayed
  family for (r\ge4), (g\ge2r+1), over any characteristic-zero field has
  an exact degree recurrence whose nontrivial spectrum is three-dimensional.
- Explain the obstacle in one sentence: exponent rows alone do not determine
  actual iterate degrees until strict selection, carried terms,
  noncancellation, and coordinate visibility are closed.
- State the mechanism in one sentence: an explicit sufficient invariant
  selector cone yields (v_{n+1}=Au_n), (u_{n+1}=Cu_n), while middle
  differences form an ((r-3))-dimensional identity space.
- State the memorable exact results:
  (deg(F^n)=e_r^{\mathsf T}C^n\mathbf1),
  (lambda_1(F)=\rho(C)), and
  (chi_C=(t-1)^{r-3}P_{m,h}).
- Include the sharp qualifier: (g=2r) is a tie only for the stated seed and
  selected face. Do not claim global optimality.
- Use no citation, priority language, acronym, experiment, or unexplained
  symbol in the Abstract. A reader should understand the contribution without
  opening the paper.

### §1 Introduction and bounded positioning — 3.0 pages

#### Purpose and order

1. Begin with the exact degree-growth question for the displayed shear word,
   not with generic claims about polynomial dynamics.
2. Explain why the problem is nontrivial: a winning support can change under
   iteration, old coordinates can tie a fresh gradient, and equal-degree
   leading forms can cancel.
3. Give the one-sentence contribution verbatim or in a mathematically
   equivalent form before the end of the first page.
4. State a compact main-theorem bundle with the parameter range, exact degree
   identity, unit-space dimension, quotient dimension, cubic factor, and
   seed/face threshold.
5. Position the result by mathematical question: broader affine-triangular
   degree constructions; higher-dimensional polynomial degree growth;
   spectral interpretations of dynamical degree; and neighboring polynomial
   symplectic or coupled-Hénon constructions. This synthesis may use only the
   six verified context sources S01--S06.
6. End with the proof roadmap in the same order as C1--C9.

#### Contribution bullets

The Introduction should use three specific, falsifiable bullets:

1. We derive both phase matrices from literal gradient supports and prove one
   explicit sufficient invariant selector cone, including both selectors,
   every cone wall, all carried coordinates, and leading-form survival.
2. We prove the exact degree and Perron formulas and show that the
   (r)-dimensional system decomposes into an ((r-3))-dimensional unit
   sector and the displayed three-dimensional equal-middle restriction.
3. We compute the characteristic factor and cubic degree recurrence, prove
   exact unit multiplicity, and isolate the precise (g=2r) seed/selected-
   face boundary together with the fixed-support coefficient corollary.

#### Front-loading and positioning checks

- The main theorem appears before detailed literature context.
- The Introduction distinguishes contextual comparison from proof; no source
  is credited with a theorem-critical identity.
- It makes no firstness, priority, exhaustive-search, or absolute novelty
  claim.
- It contains no internal predecessor title, project number, collision table,
  disclosure workflow, or unpublished citation. The formal low-mode
  specialization is deferred to §8 as mathematics only.
- No hero figure is planned. The theorem display and the three contribution
  bullets perform the skim-reader function.
- Every paragraph has one job: problem, obstacle, mechanism, theorem,
  context, or roadmap.

All theorem statements and proof intuition remain in the main body; no
Introduction content is delegated to an appendix.

### §2 The family, polynomial inverses, and symplectic geometry — 3.5 pages

#### Definitions and explicit calculations

- Fix (K), (r), (g), (h), (m), coordinates
  (q=(q_1,\ldots,q_r)), (p=(p_1,\ldots,p_r)), and
  (omega=\sum_i dq_i\wedge dp_i).
- Display (V_{r,g}), (W_{r,g}), (S), (T), and (F=T\circ S) in the
  exact phase order.
- Expand every gradient type:

  [
  \frac{\partial V}{\partial q_1}
  =2q_1\prod_{j=2}^r q_j^2+gq_1^{g-1},qquad
  \frac{\partial V}{\partial q_i}
  =2q_i\prod_{j\ne i}q_j^2,
  ]

  [
  \frac{\partial W}{\partial p_i}
  =2p_i\prod_{j\ne i}p_j^2,qquad
  \frac{\partial W}{\partial p_r}
  =2p_r\prod_{j=1}^{r-1}p_j^2+gp_r^{g-1},
  ]

  with the non-endpoint index ranges stated explicitly.
- Prove the subtraction inverses
  (S^{-1}(q,p)=(q,p-\nabla V(q))) and
  (T^{-1}(q,p)=(q-\nabla W(p),p)).
- Write

  [
  J_S=\begin{pmatrix}I&0\\H_V&I\end{pmatrix},qquad
  J_T=\begin{pmatrix}I&H_W\\0&I\end{pmatrix},
  ]

  and verify (J^{\mathsf T}\Omega J=\Omega) from Hessian symmetry.

#### Formal result and proof placement

State and prove a proposition that (S,T,F) are polynomial symplectic
automorphisms. The proof is short but theorem-critical and stays here in full.
Algebraic closedness must not be introduced; characteristic zero is the only
field assumption in the headline theorem.

The section ends by observing that symplecticity does not itself determine
degree growth. The next section therefore reads the exponent rows literally.

### §3 Gradient supports and the two strict selectors — 3.5 pages

#### Support-row ledger

- Explain that the mixed derivative in row (i) has exponent score
  (2\sum_j u_j-u_i), the (i)-th row of
  (M=2\mathbf1\mathbf1^{\mathsf T}-I).
- Include one compact, hand-typeset mathematical support-row table covering:
  the mixed and pure rows in (partial V/\partial q_1); the singleton mixed
  rows (2\le i\le r); the singleton mixed (W)-rows (1\le i<r); and the
  mixed and pure rows in (partial W/\partial p_r).
- Derive (A) and (B) from that table, then define (C=BA). Do not present
  the matrices as free combinatorial choices.
- State explicitly that there are exactly two competitive rows.

#### Normalization and first selector

- Define (x_i=u_i/u_1) only for (2\le i\le r) and write every time
  (sigma=\sum_{i=2}^r x_i), excluding (x_1).
- Introduce (mathcal K_{r,g}) by its mandatory name, **explicit sufficient
  invariant selector cone**.
- For (v=Au), prove the first pure-minus-mixed margin

  [
  hu_1-\left(u_1+2\sum_{i=2}^r u_i\right)
  =u_1(h-1-2\sigma)>0.
  ]

#### Second selector

- First display

  [
  \frac{v_1}{u_1}=h,qquad
  \frac{v_i}{u_1}=2+2\sigma-x_i\quad(2\le i\le r).
  ]

- Make clear that (B)'s last selector acts on (v=Au), never directly on
  (u).
- Derive the exact second pure-minus-mixed margin

  [
  \frac{\Delta_T}{u_1}
  =(2h-4m)\sigma-(h+1)x_r-4m-2.
  ]

- Use (x_r\le\sigma-m) and split according to the sign of
  (h-4m-1), obtaining respectively

  [
  \frac{\Delta_T}{u_1}>
  \frac{(h+1)(h-2m-3)}2>0
  ]

  and

  [
  \frac{\Delta_T}{u_1}\ge
  (2m+1)(h-2m-3)>0.
  ]

The open inequality must reverse correctly in the negative-coefficient case.
The section ends only after strictness at the least parameter
(h=2m+4) is explicit.

### §4 Seed containment and strict cone invariance — 4.0 pages

#### Exact complete-step rows

Multiply (C=BA) in the main text and record

[
\begin{aligned}
C_{11}&=h+4m+4,& C_{1j}&=4m+2 &&(2\le j\le r),\\
C_{i1}&=2h+4m+2,& C_{ij}&=4m+\mathbf1_{\{i=j\}}
&&(2\le i<r,\ 2\le j\le r),\\
C_{rj}&=2h &&(1\le j<r),& C_{rr}&=h.
\end{aligned}
]

Then display the three normalized row formulas

[
\frac{(Cu)_1}{u_1}=h+4m+4+(4m+2)\sigma,
]

[
\frac{(Cu)_i}{u_1}=2h+4m+2+4m\sigma+x_i
\quad(2\le i<r),
]

[
\frac{(Cu)_r}{u_1}=h(2+2\sigma-x_r).
]

#### Seed and every cone wall

1. Prove seed containment from
   (sigma(\mathbf1)=m+1<(h-1)/2).
2. For each middle lower face, prove

   [
   \frac{(Cu)_i-(Cu)_1}{u_1}
   =(h-1-2\sigma)+(x_i-1)>0.
   ]

3. For the last lower face, retain both sign cases and the exact positive
   lower bounds

   [
   \frac{(h+2)(h-2m-3)}2,qquad
   2(m+1)(h-2m-3).
   ]

4. For the open height face, define

   [
   H_2=(h-1)(Cu)_1-2\sum_{i=2}^r(Cu)_i
   ]

   and prove

   [
   \frac{H_2}{u_1}\ge
   (h-2m-3)(h+4m^2+4m+2)>0.
   ]

5. At (m=2) and (h=2m+4), state that every factor
   (h-2m-3) equals one; no threshold equality is hidden.

Include a compact hand-typeset selector/cone proof ledger with columns
“obligation,” “exact expression,” “inequality used,” and “strict lower
bound.” This is a public mathematical audit table, not an internal
claims-evidence or governance table.

The invariant-cone theorem and all wall calculations stay in the main body.
The section ends with (C\mathcal K_{r,g}\subset\mathcal K_{r,g}), which is
the input to the phase induction.

### §5 Carried coordinates, leading forms, and fixed-support coefficients — 3.5 pages

#### Phase-labelled induction

- Define (u_n) as the (q)-degree vector after (F^n) and (v_{n+1}) as
  the intermediate (p)-degree vector after the next (S)-phase.
- Prove (C-I) is entrywise positive, (A\mathbf1>\mathbf1), and every row
  of (A) is nonnegative and nonzero.
- Use these facts in the actual phase order:

  [
  Au_n>Au_{n-1}=v_n,qquad
  BAu_n-u_n=(C-I)u_n>0.
  ]

- Conclude only after both carried-coordinate checks that

  [
  v_{n+1}=Au_n,qquad u_{n+1}=Cu_n\qquad(n\ge0).
  ]

#### Leading-form survival

- State the polynomial-domain identities

  [
  \operatorname{LH}(fg)=\operatorname{LH}(f)\operatorname{LH}(g)\ne0,
  \qquad
  \deg f>\deg g\Rightarrow\operatorname{LH}(f+g)=\operatorname{LH}(f).
  ]

- Explain coordinate by coordinate why strict uniqueness supplies one
  highest-degree source and why its nonzero product leading form survives.
- Do not use a positive-coefficient semiring as the proof: arbitrary nonzero
  coefficient signs and phases are allowed in the corollary.

#### Coefficient corollary

State the extension only for

[
 \alpha\prod_i q_i^2+\beta q_1^g,qquad
 \gamma\prod_i p_i^2+\delta p_r^g,qquad
 \alpha,\beta,\gamma,\delta\in K^\times.
]

The proof must note that (2\alpha,g\beta,2\gamma,g\delta) are nonzero in
characteristic zero and that the supports and strict selectors are unchanged.
A vanished coefficient, added monomial, altered support, or positive-
characteristic specialization is expressly outside the corollary.

### §6 Last-coordinate visibility, exact degrees, and Perron growth — 2.5 pages

#### Visibility proof

- Compute (C-A) and prove it is entrywise positive, so each full-step
  (q_i)-degree exceeds the corresponding intermediate (p_i)-degree.
- Reuse the last-lower-wall calculation to show
  ((Cu)_r>(Cu)_1).
- For every (2\le i<r), derive the last-versus-middle difference and retain
  the two strict lower bounds

  [
  \frac{(h+2)(h-2m-3)}2,qquad
  (2m+1)(h-2m-3).
  ]

- State strict (q_r) visibility only for (n\ge1). At (n=0), all
  (2r) coordinate degrees tie at one.

#### Exact degree and first dynamical degree

Prove in the main text

[
 \deg(F_{r,g}^n)=e_r^{\mathsf T}C^n\mathbf1\qquad(n\ge0),
]

with the (n=0) case separated from strict visibility. Then use positivity
of (C), the positive seed, and the positive visible functional to prove

[
 \lambda_1(F_{r,g})=\rho(C).
]

The paragraph must distinguish this algebraic-degree limit from every
topological, metric, arithmetic, or measure-theoretic notion of entropy. No
such entropy equality is claimed.

### §7 Unit modes, the equal-middle quotient, and cubic recurrence — 4.0 pages

#### Invariant splitting

- Define (U) and (E) exactly as frozen above.
- Prove (dim U=r-3), (A|_U=B|_U=-I_U), and (C|_U=I_U).
- Prove (U\cap E=0) using the invertibility of the nonzero integer
  (m=r-2) in a characteristic-zero field, then conclude (K^r=U\oplus E).
- Fix the coordinate convention
  ((a,b,c)\mapsto(a,b,\ldots,b,c)) before displaying a matrix.

#### Three-dimensional algebra

For transcription control, display

[
 A_E=\begin{pmatrix}
 h&0&0\\2&2m-1&2\\2&2m&1
 \end{pmatrix},qquad
 B_E=\begin{pmatrix}
 1&2m&2\\2&2m-1&2\\0&0&h
 \end{pmatrix},
]

and multiply them to obtain the exact (Q_{m,h}) frozen above. Compute in
the main body

[
 \operatorname{tr}Q=2h+4m^2+4m+5,
]

[
 \sum\text{ principal }2\times2\text{ minors}
 =h^2-8hm(m+1)+2h+4,
]

[
 \det Q=h^2(2m+1)^2.
]

Use these invariants to derive, rather than merely announce,

[
 \chi_C(t)=(t-1)^{r-3}P_{m,h}(t).
]

Evaluate

[
 P_{m,h}(1)=-4m(m+1)(h+1)^2\ne0
]

and conclude that the eigenvalue (1) has algebraic and geometric
multiplicity exactly (r-3), with no quotient unit eigenvalue or hidden unit
Jordan block.

#### Exact scalar recurrence

Because (mathbf1\in E), apply Cayley--Hamilton to define

[
\begin{aligned}
T_0&=2h+4m^2+4m+5,\\
S_0&=h^2-8hm(m+1)+2h+4,\\
D_0&=h^2(2m+1)^2,
\end{aligned}
]

and prove for (d_n=e_r^{\mathsf T}C^n\mathbf1)

[
 d_{n+3}=T_0d_{n+2}-S_0d_{n+1}+D_0d_n,qquad n\ge0,
]

with (d_0=1) and (d_1=h(2m+3)). State that this cubic is an
annihilator. The article must not say that it is minimal or irreducible for
every parameter, or that (ho(C)) always has algebraic degree three.

No determinant, invariant-space, multiplicity, or recurrence proof is moved
to an appendix.

### §8 Sharp boundary, low-mode consistency, limitations, and conclusion — 2.0 pages

#### Boundary audit

- At the ordinary-degree seed, calculate the first pure-minus-mixed score

  [
  (g-1)-\bigl(1+2(r-1)\bigr)=g-2r.
  ]

- At (g=2r), state both facts: the first selector ties and
  (sigma(\mathbf1)=r-1=(g-2)/2) lies on the open cone-height boundary.
- At (g=2r+1), state the selector gap one and height slack one half.
- Phrase sharpness only for the ordinary seed and the chosen strict selected
  face. Do not infer the actual degree dynamics at or below the boundary.

#### Low-mode consistency

Formally set (r=3), (m=1), only after the (r\ge4) theorem is complete,
and record

[
 Q_{1,g-1}=
 \begin{pmatrix}
 g+7&6&6\\2g+4&5&4\\2(g-1)&2(g-1)&g-1
 \end{pmatrix},
]

[
 P_{1,g-1}(t)
 =t^3-(2g+11)t^2+(g^2-16g+19)t-9(g-1)^2.
]

This is a consistency calculation outside the public headline range, not a
new (r=3) theorem or a correction. If no stable public identifier exists
for the low-mode lineage, the article must not fabricate a citation or name
an internal record.

#### Limitations and conclusion

Give a compact limitations paragraph covering the sufficient-not-maximal
cone, fixed supports and shear word, characteristic-zero field, (n=0) tie,
seed/face-only sharpness, and nonminimal cubic possibility. Then conclude by
restating only:

- the exact degree and Perron identities for the fixed (r\ge4) family;
- the ((r-3))-dimensional unit space and three-dimensional quotient; and
- the cubic characteristic factor and annihilating recurrence.

The Conclusion contains no priority assertion, governance history, local
predecessor identity, submission language, or speculative extension presented
as achieved work.

## Page Budget and Feasibility

| Block | Pages | Non-negotiable content |
|---|---:|---|
| §0 Abstract | 0.5 | Exact contribution, assumptions, degree identity, quotient collapse, qualified boundary |
| §1 Introduction and bounded positioning | 3.0 | What/Why/So What, theorem bundle, three contributions, S01--S06 context |
| §2 Family and symplectic geometry | 3.5 | Potentials, gradients, inverses, Hessian-block proof |
| §3 Support rows and selectors | 3.5 | (M,A,B,C), support ledger, both exact selectors |
| §4 Strict cone invariance | 4.0 | Seed, all lower faces, open height face, least parameter |
| §5 Carry, leading forms, coefficient corollary | 3.5 | Both carried phases, domain noncancellation, four fixed-support coefficients |
| §6 Visibility, exact degree, Perron growth | 2.5 | (C-A>0), (n\ge1) visibility, (n=0) tie, PF |
| §7 Unit space, quotient, cubic, recurrence | 4.0 | (U\oplus E), (Q), invariants, (P(1)), exact multiplicity, recurrence |
| §8 Boundary, consistency, limitations, conclusion | 2.0 | (g=2r), formal (r=3), anti-claims, bounded conclusion |
| **Total** | **26.5** | References excluded |

The target lies inside both the preferred 24--28 band and the hard 22--30
band. Any draft outside 22--30 substantive pages returns to a fresh
completeness decision; page count may not be achieved with governance text,
duplicated proof, decorative assets, or discovery history.

## Visual and Mathematical-Table Plan

Generated figures, plots, diagrams, images, empirical tables, experiments,
datasets, and assets: **zero**.

The absence of a hero figure is intentional. Three hand-typeset mathematical
tables are permitted in the public article:

| Public table | Section | Mathematical function |
|---|---|---|
| Gradient support-row ledger | §3 | Enumerate all derivative-row types, their exponent rows, and the two competing endpoint supports. |
| Selector/cone proof ledger | §§3--4 | Pair each selector or cone wall with its exact expression and strict symbolic lower bound. |
| Three-dimensional invariant ledger | §7 | Record (operatorname{tr}Q), the principal-minor sum, (det Q), and their coefficients in (P_{m,h}). |

These tables are proofs or transcription controls. The internal
claims--evidence matrix, source screen, collision analysis, file inventory,
review history, and permission ledger must never be turned into public tables.

## Citation Plan: Exact Verified Pool S01--S06

No bibliography or BibTeX is created at the plan stage. A later independently
authorized bibliography may use only the following six verified records, and
only for the listed context roles. There is no seventh source in the pool, and
no theorem statement, selector inequality, matrix identity, recurrence, or
novelty/priority conclusion may be delegated to a citation.

| ID | Verified record | Planned context-only role | Forbidden use |
|---|---|---|---|
| S01 | Jérémy Blanc and Immanuel van Santen, “Dynamical degrees of affine-triangular automorphisms of affine spaces,” arXiv:1912.01324; DOI 10.1017/etds.2021.90 | §1: broader arbitrary-dimensional affine-triangular degree calculations and weak-Perron realization context | No transfer of the fixed gradient family, selector cone, quotient theorem, or first-realization claim |
| S02 | Enbo Shao and Xiaosong Sun, “Dynamical degrees of affine-triangular automorphisms in dimension four,” arXiv:2509.14584 | §1: current dimension-four affine-triangular algebraic-degree context | No identification with the displayed symplectic gradient family and no proof role |
| S03 | Julie Déserti, “Degree growth of polynomial automorphisms and birational maps: some examples,” arXiv:1602.04642 | §1: examples showing varied higher-dimensional polynomial-automorphism degree growth | No evidence for this exponential recurrence or cubic factor |
| S04 | Nguyen-Bac Dang and Charles Favre, “Spectral interpretations of dynamical degrees and applications,” *Annals of Mathematics* 194 (2021); DOI 10.4007/annals.2021.194.1.5 | §§1 and 6: general spectral context motivating an explicit visibility proof | No finite-support selector, family-specific identity, or shortcut to (lambda_1=\rho(C)) |
| S05 | G. Rangarajan, “Polynomial map symplectic algorithm,” arXiv:physics/0212098 | §1: neighboring polynomial symplectic-map construction methodology | No exact degree iteration, endpoint threshold, or spectral-collapse inference |
| S06 | Keisuke Fujioka, Ryota Kogawa, Jizhou Li, and Akira Shudo, “Coupled Hénon Map, Part I: Topological Horseshoes and Uniform Hyperbolicity,” arXiv:2303.05769 | §1: neighboring coupled symplectic Hénon setting concerned with hyperbolicity | No transfer to algebraic degree, the fixed potentials, or the quotient cubic |

The six references should be synthesized by question or method, not summarized
one by one. Their metadata must be copied only from the verified pool during a
later authorized bibliography stage; the plan does not generate citation keys
or BibTeX from memory.

## Hard Anti-Claims and Drafting STOP Rules

The public article does not claim:

1. that (mathcal K_{r,g}) is maximal, necessary, unique, exact, or a
   classification of selector regions;
2. any theorem for arbitrary supports, added monomials, arbitrary potentials,
   arbitrary Hamiltonian or polynomial maps, or arbitrary shear words;
3. positive-characteristic validity;
4. universal irreducibility or minimality of (P_{m,h}), or algebraic degree
   exactly three for every Perron root;
5. actual failure of degree dynamics at (g=2r), or global optimality of
   (g\ge2r+1);
6. a new low-mode theorem or correction from the (r=3) specialization;
7. entropy, periodic-point, trace, multiplier, torus, arithmetic-orbit,
   integrability, invariant-variety, or arithmetic-dynamics conclusions;
8. genericity, non-conjugacy, classification, universality, or realization of
   an arbitrary Perron or weak-Perron number;
9. absolute novelty, firstness, priority, uniqueness in the literature, or an
   exhaustive source screen;
10. any CAS, numerical spectrum, finite parameter scan, empirical table,
    experiment, dataset, or hidden computer certificate as evidence.

Drafting stops and returns to repair if any of these occurs:

- (sigma) includes (x_1), or any normalized index range changes;
- the second selector is applied to (u) rather than (v=Au);
- an input lower face or the open height face lacks its strict output proof;
- a carried coordinate can tie the fresh selected degree;
- leading-form survival is inferred from degree arithmetic without the domain
  argument;
- strict (e_r) visibility is claimed at (n=0);
- the coefficient corollary permits a zero coefficient or a changed support;
- the equal-middle coordinate convention, (Q), (P), or (P(1)) drifts;
- the cubic is promoted from an annihilator to a universal minimal or
  irreducible equation;
- the (g=2r) seed tie becomes a global impossibility statement;
- any citation is used as proof, or an unverified seventh reference appears;
- any theorem-critical proof is moved to an appendix.

## Main-Body and Appendix Policy

Every theorem-critical definition, selector, cone wall, carried-coordinate
comparison, leading-form argument, visibility bound, invariant splitting,
matrix computation, characteristic factor, (P(1)) evaluation, recurrence,
and boundary calculation appears in §§2--8. No theorem-critical appendix is
planned. If a later venue template mechanically permits an appendix, it may
contain only redundant notation or arithmetic already proved in the main
body, and it may not repair a missing argument.

## Draft-Readiness Checklist

- [ ] The exact title and Anonymous author status are unchanged.
- [ ] The headline range is (K) arbitrary characteristic zero,
  (r\ge4), and (g\ge2r+1).
- [ ] The phase order remains (F=T\circ S).
- [ ] The support rows literally determine (A), (B), and (C=BA).
- [ ] The cone is always an explicit sufficient invariant selector cone.
- [ ] (x_i) exists only for (2\le i\le r), and
  (sigma=\sum_{i=2}^r x_i).
- [ ] Both selectors, every cone wall, and the seed are proved before the
  phase recurrence.
- [ ] Both carry phases and the polynomial-domain noncancellation proof are
  explicit.
- [ ] The coefficient corollary has exactly four nonzero coefficients on the
  fixed supports.
- [ ] Strict last-coordinate visibility starts at (n=1), while the degree
  identity is stated for (n\ge0).
- [ ] (U), (E), the coordinate convention, (Q), (P), and (P(1)) are
  copied exactly.
- [ ] The eigenvalue one has exact algebraic and geometric multiplicity
  (r-3).
- [ ] The scalar cubic is called an annihilator, with no universal minimality
  or irreducibility claim.
- [ ] The (g=2r) statement is seed/selected-face sharpness only.
- [ ] The (r=3) calculation is consistency only and receives no fabricated
  local citation.
- [ ] Only S01--S06 are citation-eligible, all context-only.
- [ ] There are zero figures, plots, assets, experiments, empirical tables,
  numerical checks, and CAS certificates.
- [ ] No governance material enters the public article or Conclusion.
- [ ] The page allocation remains 26.5 and every critical proof remains in
  the main body.

## Independent Review Handoff and Exact Permissions

The plan author does not self-certify this artifact. At author stop, the exact
Paper 22 project inventory is 14 regular files, 4 directories, and 0
symlinks: the prior 13-file / 3-directory reviewed universe plus this one
`paper/PAPER_PLAN.md` file and its `paper/` directory.

After this plan-author stop, the only authorized possible write is by one
fresh independent reviewer at
`notes/INDEPENDENT_PAPER_PLAN_REVIEW.md`. If any conjunctive plan check fails,
the reviewer writes no PASS artifact. The sole passing terminal disposition
is `PAPER_PLAN_PASS`.

`PAPER_PLAN_PASS` makes only the independent scope-only stage at
`notes/PUBLICATION_STAGE_SCOPE.md` eligible. It does **not** directly
authorize a manuscript, publication lock, TeX, BibTeX, figures, code,
experiments, datasets, CAS, build, PDF, release, transport, submission,
upload, repository push, messaging, identity disclosure, Paper 23, or any
other external effect.

PAPER PLAN AUTHOR STOP
