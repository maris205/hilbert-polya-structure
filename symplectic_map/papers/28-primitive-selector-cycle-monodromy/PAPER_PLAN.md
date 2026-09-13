# Proof-only anonymous article blueprint

## Publication-facing identity

Public-safe title: *Primitive Newton-Selector Cycles in
Permutation-Twisted Hamiltonian Shears: Normal-Fan Classification and Exact
Monodromy*

One-sentence public claim: For every rooted primitive selector-pair word of
length \(\ell\ge3\), one explicit autonomous polynomial symplectomorphism on
\(2(\ell+1)\) affine coordinates realizes that word as its strict endogenous
actual weighted-degree selector cycle for every nonzero coefficient tuple and
every positive momentum seed in the exact first-carry chamber, admits a
rational-polyhedral necessary-and-sufficient selector criterion, has separate
least selector and quotient periods \(\ell\), and has a marked period
monodromy that recovers the rooted support-vector word, with literal labels
requiring the labelled support dictionary.

The manuscript must say near the first occurrence of the claim that this is
one map per rooted word, with dimension growing with \(\ell\).  It is not one
universal map, one map per length, or a fixed-dimensional realization for
unbounded word length.

## Immutable writing contract

The article is an anonymous proof paper.  Its mathematical universe is a
field \(\Bbbk\) of characteristic zero, a rooted primitive pair word

\[
 \mathsf w=((a_0,b_0),\ldots,(a_{\ell-1},b_{\ell-1})),
 \qquad \ell\ge3,
\]

the dimension parameter \(r=\ell+1\), the moving \(\ell\)-cycle together
with one fixed star coordinate, integers \(H\ge2\), \(\rho\ge2\), and
\(K\ge1\), positive weighted-degree seeds, support exponents with every
coordinate at least two, and nonzero displayed coefficients.  Repeated
labels and a singleton V or W alphabet are allowed; the pair word itself
must be primitive.  Every theorem-critical argument, boundary, and
counterexample is in the main body.  There is no proof appendix, empirical
section, computation supplement, or generated figure.

Internal traceability labels T1--T8, C01--C18, P1--P13, P28-X01--P28-X12,
and F1--F6 are used in this plan only.  They must not appear in the public
article.  The public source uses ordinary theorem numbering and the semantic
labels frozen below.

## Notation table for the manuscript

The following is Table 1 of the article.  It must occur in Section 2.1 and
must distinguish the input word \(\mathsf w\) from the polynomial \(W\), and
the momentum weight \(m_n\) from every word symbol.

| Symbol | Exact meaning and domain |
|---|---|
| \(\Bbbk\) | characteristic-zero coefficient field |
| \(\mathsf w=((a_j,b_j))_{j=0}^{\ell-1}\) | rooted primitive selector-pair word, \(\ell\ge3\) |
| \(r\) | \(\ell+1\) symplectic coordinate pairs; ambient dimension \(2r\) |
| \(I_{\mathrm{mov}}\), \(\star\), \(I\) | \(\{0,\ldots,\ell-1\}\), the separate fixed coordinate, and \(I_{\mathrm{mov}}\sqcup\{\star\}\) |
| \(P\) | permutation with \(Pe_j=e_{j+1\pmod\ell}\), \(Pe_\star=e_\star\), \(P^\ell=I\), and \(P\mathbf1=\mathbf1\) |
| \(H,\rho,K\) | integers satisfying \(H\ge2\), \(\rho\ge2\), \(K\ge1\) |
| \(u_0,m_0\) | positive initial position and momentum weight vectors; \(u_0=\mathbf1+(H-1)e_0\) |
| \(S_a,T_b\) | occurrence sets \(\{j:a_j=a\}\) and \(\{j:b_j=b\}\) for used labels |
| \(\alpha_a,\beta_b\) | collected V and W support exponents defined by the incidence construction |
| \(D\) | common exponent total \(D=\rho r+K\ell\) |
| \(V_{\mathsf w},W_{\mathsf w}\) | collected-support Hamiltonians with arbitrary coefficients \(\xi_a,\zeta_b\in\Bbbk^*\) |
| \(S_V,T_W,\Pi_P,F_{\mathsf w}\) | the two gradient shears, simultaneous permutation, and their frozen ordered composition |
| \(A_\alpha,B_\beta\) | selected gradient degree matrices \(\mathbf1\alpha^{\mathsf T}-I\) and \(\mathbf1\beta^{\mathsf T}-I\) |
| \(c_{a,b},\lambda,C_{a,b}\) | \((D-1)\alpha_a-\beta_b\), \((D-1)^2\), and \(P+\mathbf1c_{a,b}^{\mathsf T}\) |
| \(x_n,t_n\) | residual and diagonal parts in \(u_n=x_n+t_n\mathbf1\), with \(x_n=P^nu_0\) |
| \(C_0,g,\mu\) | base incidence score, competitor gap, and constant scalar forcing |
| \(Q_s,R_s,M_{\mathsf w}\) | ordered prefix product, its rank-one row, and the \(\ell\)-step monodromy |
| \(q_n,d_n\) | position maximum and complete-state maximum, respectively |
| \(y_n^{(i)},z_m^{(i,s)}\) | individual position coordinate and its phase-\(s\) subsequence; the star formula is separate |
| \(\mathcal N_V^+(\alpha),\mathcal N_W^-(\beta),\mathcal C_{\mathsf w}\) | strict V-max fan, strict W-min fan, and pulled-back selector cone |

The notation table is descriptive only.  Definitions carrying a hypothesis
or a quantifier must be repeated in the theorem or lemma that uses them.

## Exact article architecture and page mass

References are excluded from every count.  The page allocations below are
hard targets, not ranges.  Subsection entries sum to their section entry;
the six mathematical-core sections sum to 22.0 pages and the three
peripheral entries sum to 4.5 pages.

| Article unit | Subsection allocation | Class | Pages |
|---|---|---|---:|
| Abstract | single unnumbered abstract | peripheral | 0.50 |
| 1. Introduction and bounded positioning | 1.1 Question and contribution 0.55; 1.2 Main theorem 1.05; 1.3 Established neighbors and roadmap 0.90 | peripheral | 2.50 |
| 2. Symplectic family and exact weighted-degree transport | 2.1 Inputs, supports, and notation 0.75; 2.2 Symplectic shears and inverse 1.10; 2.3 Selected gradient matrices 0.85; 2.4 Formal-versus-actual degree boundary 0.30 | core | 3.00 |
| 3. Normal-fan iff | 3.1 Equal-total residual reduction 1.00; 3.2 Pulled-back V-max/W-min criterion 1.45; 3.3 Rationality, walls, and singleton supports 0.85; 3.4 Selector/carry separation 0.70 | core | 4.00 |
| 4. Incidence realization of primitive words | 4.1 Moving cycle, fixed star, and supports 1.10; 4.2 Exact score table 1.30; 4.3 Endogenous every-word realization 0.90; 4.4 Hand-derived audit fixture and sharp incidence boundaries 0.70 | core | 4.00 |
| 5. Strict carries and leading forms | 5.1 Strict growth in \(r\ge2\) 0.75; 5.2 Exact first-carry chamber and induction 1.05; 5.3 Coefficient-uniform survival 1.05; 5.4 Cancellation and support-boundary counterexamples 0.65 | core | 3.50 |
| 6. Ordered monodromy and decoding | 6.1 Constant scalar forcing 0.55; 6.2 Ordered prefixes and period monodromy 1.30; 6.3 Digit bounds and pair injectivity 0.85; 6.4 Three-level decoder 0.85; 6.5 Missing-data boundary 0.45 | core | 4.00 |
| 7. Least periods, scalar boundaries, and counterexamples | 7.1 Two least periods 0.75; 7.2 Position maximum 0.55; 7.3 Moving, star, and phase subsequences 0.70; 7.4 Complete-state start index and residual 0.85; 7.5 Remaining structural boundaries and planar obstruction 0.65 | core | 3.50 |
| 8. Limitations and conclusion | 8.1 Scope and anti-claims 0.65; 8.2 Conjunctive contribution 0.55; 8.3 Proof-only evidence statement 0.30 | peripheral | 1.50 |
| **Mathematical core** | Sections 2--7 |  | **22.00** |
| **Peripheral** | Abstract, Section 1, Section 8 |  | **4.50** |
| **Anonymous content total** | references excluded |  | **26.50** |

The proof package's historical 21.5-page approximate grouping is not used in
the manuscript budget and is not added to 4.5.  The only controlling mass is
\(22.0+4.5=26.5\).

## Section-by-section writing contract

### Abstract — 0.50 page

Use one compact paragraph with five moves: the family-wise input quantifier;
the explicit autonomous symplectic construction; the general normal-fan iff
and exact carry chamber; the endogenous realization, two least periods, and
rank-one monodromy decoder; and the decoder side-information boundary.  Say
“weighted degree,” never “ordinary degree.”  State that coefficients are
arbitrary nonzero elements of a characteristic-zero field.  Do not cite
literature, mention a search, report a score, or imply one universal map.

### 1. Introduction and bounded positioning — 2.50 pages

#### 1.1 Question and contribution — 0.55 page

Pose the question in publication-facing language: can any rooted primitive
pair word be made an endogenous strict support-selector cycle of one fixed
polynomial symplectomorphism, with a complete chamber criterion and an exact
period product that retains the word?  Immediately separate selector words
from polynomial-state cycles, max-plus state cycles, external schedules, and
reduced automorphism words.  Give the one-sentence claim exactly once.

#### 1.2 Main theorem — 1.05 pages

State Theorem A with the complete input quantifier and all eight clauses:

1. polynomial symplecticity and the explicit inverse (T1);
2. the general equal-total strict-selector iff, explicitly for position
   weights only (T2);
3. incidence realization of every rooted primitive pair word, including
   repeated labels and singleton sides (T3);
4. the coordinatewise first-carry chamber and coefficient-uniform actual
   weighted-degree lift (T4);
5. the ordered prefix and period-monodromy formulas (T5);
6. the three-level, marked decoder with its missing-information losses (T6);
7. separate least selector and diagonal-quotient periods (T7); and
8. the exact scalar annihilators with literal domains and start indices (T8).

The theorem statement must include \(r=\ell+1\), ambient dimension
\(2(\ell+1)\), characteristic zero, exponent coordinates at least two,
nonzero coefficients, strict positive seeds, and the exact gate
\(0<m_0<A_{\alpha_{a_0}}u_0\).  It must say that a singleton side has
vacuous uniqueness and no finite competitor gap.  It must not suggest that
the selector iff alone proves the actual polynomial lift.

#### 1.3 Established neighbors and roadmap — 0.90 page

Use Table 2, “Established ingredients and the separation used here,” with no
more than six grouped rows: polynomial symplectomorphisms and automorphism
words; weighted degrees and chamber geometry; monomial degree recurrences;
max-plus state cycles and external schedules; cluster/sign itineraries and
ordered tropical products; and entropy/degree-growth context.  Each row has
one established ingredient and one explicit noncollision sentence.  End
with the bounded-search wording through 29 August 2026 for the exact
six-property conjunction, never “first,” “only,” or “unprecedented.”  The
last paragraph gives the section roadmap and says all proofs are in the main
body.

### 2. Symplectic family and exact weighted-degree transport — 3.00 pages

#### 2.1 Inputs, supports, and notation — 0.75 page

Define \(\mathsf w\), \(r\), \(I_{\mathrm{mov}}\), \(\star\), \(P\),
\(u_0\), the occurrence sets, exponents, common total \(D\), and the two
polynomials.  State that only labels that occur are used, every occurrence
set is nonempty, a component alphabet may be a singleton, and all displayed
coefficients lie in \(\Bbbk^*\).  Place Table 1 here.

#### 2.2 Symplectic shears and inverse — 1.10 pages

Proposition 2.1 proves P1/C01/T1.  Display the Jacobians with their symmetric
Hessian blocks, check preservation of the standard symplectic matrix, and
check that the same permutation acts on q and p.  Freeze the map order
\(F_{\mathsf w}=\Pi_P\circ T_W\circ S_V\), then display and verify the
polynomial inverse in the literal reverse order.  Do not invoke a degree
matrix as evidence of symplecticity.  Mention as an adjacent boundary that
different q and p permutations need not preserve the standard form.

#### 2.3 Selected gradient matrices — 0.85 page

Lemma 2.2 proves P2/C02--C03.  Derive each row degree
\(\alpha^{\mathsf T}u-u_i\), record why the derivative scalar is nonzero,
and obtain \(A_\alpha\), \(B_\beta\), their equal-total rank-one product,
and \(c^{\mathsf T}\mathbf1=\lambda-1\).  For the general support class use
V-total A and W-total B before specializing to \(A=B=D\).  The displayed
incidence matrix is then \(C_{a,b}=P+\mathbf1c_{a,b}^{\mathsf T}\).

#### 2.4 Formal-versus-actual degree boundary — 0.30 page

End the section with an explicit firewall: Sections 2--4 classify formal
strict selectors on position weights; only Section 5 proves that the chosen
matrices are the actual polynomial weighted-degree transport.  No ordinary-
total-degree, algebraic-degree, or dynamical-degree statement follows.

### 3. Normal-fan iff — 4.00 pages

#### 3.1 Equal-total residual reduction — 1.00 page

Begin P6/C04/T2 without using the later constant-forcing formula.  For a
selected matrix \(C_n=P+\mathbf1c_n^{\mathsf T}\), write
\(u_n=x_n+t_n\mathbf1\) and prove that the residual updates by
\(x_{n+1}=Px_n\).  Equal V totals cancel the diagonal component.  After V
selection, calculate the W score difference and prove its sign reverses, so
the actual W maximization is a minimization on the residual position weight.

#### 3.2 Pulled-back V-max/W-min criterion — 1.45 pages

Theorem 3.1 states and proves the exact iff

\[
 \mathcal C_{\mathsf w}=\mathbb R_{>0}^{r}\cap
 \bigcap_{j=0}^{\ell-1}P^{-j}
 \bigl(\mathcal N_V^+(\alpha_j)\cap
       \mathcal N_W^-(\beta_j)\bigr).
\]

Prove necessity and sufficiency separately and preserve the strict V-max/W-
min signs.  Corollary 3.2 records that the cone is rational, homogeneous,
open, and polyhedral and that a nonempty cone contains a positive rational
point, hence a positive integer seed after scaling.  This is a selector
classification, not an actual-lift iff.

#### 3.3 Rationality, walls, and singleton supports — 0.85 page

Counterexample 3.3 places F3/P28-X12 beside strictness: an equality in any
competitor inequality produces a tie, and the theorem supplies no tie-
breaking rule.  Remark 3.4 gives the singleton convention exactly: the
competitor family is empty, the intersection is the full positive weight
space, uniqueness is vacuous, and no finite gap is assigned.  Explain that
unequal totals restore diagonal drift and therefore invalidate this frozen
fan reduction.

#### 3.4 Selector/carry separation — 0.70 page

Use a boxed logical statement, not a merged theorem:

\[
 \text{strict selector word}
 \Longleftrightarrow u_0\in\mathcal C_{\mathsf w},
 \qquad
 \text{actual polynomial lift additionally requires the Section 5 gate.}
\]

This box is the only summary arrow.  It must not put the momentum condition
inside the fan iff or claim that cone membership is sufficient for leading-
form survival.

### 4. Incidence realization of primitive words — 4.00 pages

#### 4.1 Moving cycle, fixed star, and supports — 1.10 pages

Begin P7/C05--C06/T3.  Define the moving cycle, fixed star, spike seed,
occurrence sets, and both exponent families.  Verify coordinatewise
positivity and the common total \(D=\rho r+K\ell\).  State why distinct used
labels have distinct nonempty occurrence sets, while repeated occurrences of
the same label are collected into one support vector.

#### 4.2 Exact score table — 1.30 pages

At \(x_j=P^ju_0\), derive both score identities term by term.  State the
selected V score as \(C_0+g\), the selected W score as \(C_0\), and the
corresponding competitor score on the correct side.  The gap statement is
only “exactly \(g=K(H-1)\) against every competitor that exists.”  Repeat in
one sentence that a singleton side has no competitor and therefore no finite
gap.

#### 4.3 Endogenous every-word realization — 0.90 page

Theorem 4.1 concludes the formal incidence realization for every rooted
primitive pair word, including repeated labels and singleton component
alphabets.  It must say the supports and coefficients are fixed once and for
all before iteration; no phase-dependent Hamiltonian, external switch, or
schedule supplies the itinerary.  Use the canonical \(m_0=\mathbf1\) only
as a preview of the Section 5 chamber, and defer the actual-degree conclusion
until Theorem 5.2 and Proposition 5.3 are proved.

#### 4.4 Hand-derived audit fixture and sharp incidence boundaries — 0.70 page

Example 4.2 uses only the hand-derived word
\(((A,X),(B,X),(A,Y))\) with
\((\ell,r,\rho,K,H)=(3,4,2,1,2)\).  Display its four support vectors, common
total \(D=11\), \(C_0=13\), \(g=1\), and \(\lambda=100\).  State explicitly
that this checks notation and illustrates repeated labels but proves no
universal claim.  Immediately follow it with the \(H=1\) boundary: the
spike gap vanishes, incidence scores tie, and the quotient geometry
collapses.

### 5. Strict carries and leading forms — 3.50 pages

#### 5.1 Strict growth in \(r\ge2\) — 0.75 page

Lemma 5.1 proves P3.  Display the coordinate identity

\[
 (A_\alpha u)_i-u_i=(\alpha_i-2)u_i+
 \sum_{k\ne i}\alpha_ku_k>0
\]

for \(u>0\), \(r\ge2\), and
\(\alpha\in\mathbb Z_{\ge2}^{r}\), and state the identical B argument.
Keep the general \(r\ge2\) lemma distinct from the headline specialization
\(r=\ell+1\ge4\).

#### 5.2 Exact first-carry chamber and induction — 1.05 pages

Theorem 5.2 proves P4/C07/T4.  State the phase-zero coordinatewise gate

\[
 0<m_0<A_{\alpha_{a_0}}u_0
\]

as the exact strict source-carry chamber used by the lift.  Show the first V
gradient dominates carried momentum, the W gradient dominates carried
position, and then \(u_1>m_1\).  Inductively derive

\[
 m_{n+1}=PA_{\alpha_n}u_n,
 \qquad
 u_{n+1}=PB_{\beta_n}A_{\alpha_n}u_n.
\]

State next to the gate that \(0<m_0\le u_0\) is sufficient but not
necessary.  Do not claim anything about positive seeds outside the strict
gate.

#### 5.3 Coefficient-uniform survival — 1.05 pages

Proposition 5.3 proves P5/C08 and closes the two proof branches from Sections
3--4 and 5.  At every phase use: unique selected support exponent; exponent
coordinates at least two; nonzero derivative scalars in characteristic
zero; nonzero products of leading forms in a polynomial domain; and strict
carry over the coordinate term.  Conclude actual polynomial weighted-degree
transport for every coefficient tuple in
\((\Bbbk^*)^{|E_V|+|E_W|}\), with no genericity or sign hypothesis.  Only
here may Theorem 4.1 be upgraded from formal selection to the advertised
endogenous actual weighted-degree realization.

#### 5.4 Cancellation and support-boundary counterexamples — 0.65 page

Counterexample 5.4 is F1: over \(\mathbb Q\), take
\(V(q)=q^2\), \(W(p)=-p^2/4\), and calculate the next q-coordinate as
\(-p/2\); the formal one-dimensional matrices do not prevent cancellation.
In the same subsection place the three local failure statements next to the
hypotheses they justify: a zero exponent coordinate can delete a gradient
monomial, positive characteristic can annihilate a derivative scalar, and a
zero displayed coefficient changes the collected support.

### 6. Ordered monodromy and decoding — 4.00 pages

#### 6.1 Constant scalar forcing — 0.55 page

Lemma 6.1 proves P8/C09.  Use the incidence score table, not an empirical
pattern, to derive

\[
 \mu=(D-1)(C_0+g)-C_0>0,
 \qquad
 u_n=P^nu_0+t_n\mathbf1,
 \qquad
 t_{n+1}=\lambda t_n+\mu,
\]

and display \(t_n=\mu(\lambda^n-1)/(\lambda-1)\).  State that constant
scalar forcing is deliberate and carries no word information.

#### 6.2 Ordered prefixes and period monodromy — 1.30 pages

Theorem 6.2 proves P9/C10/T5.  Fix the order
\(Q_s=C_{s-1}\cdots C_0\), prove the prefix formula by induction, and retain
every rotation and \(\lambda\)-power.  Specialize \(P^\ell=I\) to obtain
the period monodromy, characteristic polynomial, nonnegative powers, and the
phase-prefix formula.  No asymptotic spectral, reciprocity, entropy, or
integrability claim may be attached.

#### 6.3 Digit bounds and pair injectivity — 0.85 page

Lemma 6.3 proves P10/C11--C12.  Derive both strict inequalities
\(0<(c_{a,b})_i<\lambda\) uniformly.  For injectivity, use a moving
coordinate in the symmetric difference of two distinct V occurrence sets:
the left difference has magnitude \(K(D-1)\) whereas the right difference
has magnitude at most \(K\).  Once V agrees, use distinct W occurrence sets
to force W agreement.  Reuse the hand fixture only to list its three digit
vectors and illustrate the strict interval; do not use it as proof.

#### 6.4 Three-level decoder — 0.85 page

Theorem 6.4 proves P11/C13/T6.  Read \(R_\ell^{\mathsf T}\) from any row of
\(M_{\mathsf w}-I\), perform coordinatewise base-\(\lambda\) expansion,
and undo the known rotations with \(P^{-j}\).  Table 3 must have exactly the
following information ladder:

| Available data | Exact recoverable object |
|---|---|
| \(M_{\mathsf w},P,\lambda,\ell\), marked phase zero | rooted ordered digit-vector word \((c_0,\ldots,c_{\ell-1})\) |
| preceding data plus the unlabelled support dictionary | rooted ordered exponent-support pairs |
| preceding data plus the labelled support dictionary | literal rooted label-pair word |

Add below the table: without literal names, labels are determined only up to
independent renaming of the V and W alphabets; without marked phase zero,
only the cyclic rotation class is intrinsic.

#### 6.5 Missing-data boundary — 0.45 page

Counterexample/Boundary 6.5 is F6/P28-X09: monodromy alone cannot invent a
support dictionary, an unmarked product has no intrinsic phase-zero label,
and many different words share the same scalar forcing.  Therefore no scalar
word decoder or unqualified literal-label decoder is claimed.  Do not claim
that distinct rooted words necessarily have unequal unmarked monodromy
matrices.

### 7. Least periods, scalar boundaries, and counterexamples — 3.50 pages

#### 7.1 Two least periods — 0.75 page

Theorem 7.1 proves P12/C14/T7 in two separately numbered clauses.  Word
primitivity gives least selector period \(\ell\).  For the quotient orbit,
assume \(P^du_0-u_0=c\mathbf1\) with \(0<d<\ell\); the fixed star
coordinate forces \(c=0\), while the moved unique H-spike contradicts
equality.  Place the two failure boundaries immediately afterward: a
nonprimitive pair word has a smaller selector period, and a permutation with
a shorter quotient orbit can shorten the quotient period.  Say explicitly
that neither least-period result is a periodic-polynomial-state theorem.

#### 7.2 Position maximum — 0.55 page

Begin P13/C15--C16/T8 with
\(q_n=\max_i(u_n)_i=H+t_n\).  Display its order-two recurrence and its
length-\(\ell\) annihilator, each with \(n\ge0\).  Call both relations
annihilators and make no minimality claim.

#### 7.3 Moving, star, and phase subsequences — 0.70 page

State the moving formula only for \(i\in I_{\mathrm{mov}}\), state
\(y_n^{(\star)}=1+t_n\) separately, and never write a congruence involving
\(\star\).  Display the coordinate annihilator from \(n\ge0\).  Then define
\(z_m^{(i,s)}=y_{s+m\ell}^{(i)}\) for \(i\in I\) and
\(s\in I_{\mathrm{mov}}\), and display its order-two recurrence from
\(m\ge0\).

#### 7.4 Complete-state start index and residual — 0.85 page

Define
\(d_n=\max\{\max_i(u_n)_i,\max_i(m_n)_i\}\).  Use the Section 5 strict
carry to prove \(d_n=q_n\) only for \(n\ge1\); therefore the
length-\(\ell\) complete-state annihilator begins at \(n\ge1\).  Display
the removed \(n=0\) residual exactly as

\[
 d_{\ell+1}-\lambda d_\ell-d_1+\lambda d_0
 =\lambda(d_0-q_0).
\]

State that it vanishes iff \(d_0=q_0\), equivalently
\(\max_i(m_0)_i\le\max_i(u_0)_i\).  Counterexample 7.3 uses the manual
fixture \((\ell,r,\rho,K,H)=(3,4,2,1,2)\),
\(u_0=(2,1,1,1)\), \(m_0=(10,10,10,10)\): the strict first gate still
holds, but \(q_0=2\), \(d_0=10\), \(\lambda=100\), and the forbidden
initial residual is 800.

#### 7.5 Remaining structural boundaries and planar obstruction — 0.65 page

Collect only boundaries not already proved next to their hypotheses:
unequal totals restore diagonal drift; \(H=1\) removes the spike; a missing
root/dictionary weakens decoder output; and scalar relations do not identify
the word.  Give the planar decreasing-projective-map calculation in a short
remark: on a chamber

\[
 g(r)=\kappa\frac{(a-1)r+b}{ar+b-1},
 \qquad
 g'(r)=\kappa\frac{1-a-b}{(ar+b-1)^2}<0,
\]

so its square is increasing and there is no least period greater than two.
Label this as explanatory motivation for the higher-dimensional finite-order
residual twist, not as a priority or classification theorem.

### 8. Limitations and conclusion — 1.50 pages

#### 8.1 Scope and anti-claims — 0.65 page

Give one compact limitations paragraph containing every locked exclusion:
no universal map or fixed dimension for unbounded length; no ordinary-total-
degree realization or free-standing exact-, algebraic-, or dynamical-degree
theorem beyond the stated chambered weighted-degree transport; no scalar
word decoder, scalar separation of words, or minimal recurrence; no literal-
label recovery without a labelled dictionary and no rooted recovery without
a marked phase; no periodic polynomial state; no entropy equality,
topological entropy, integrability, generic nonconjugacy, inverse
reciprocity, or cohomological spectrum; no positive-characteristic or zero-
coordinate extension; and no absolute priority statement.

#### 8.2 Conjunctive contribution — 0.55 page

Conclude only with the proved conjunction: every-word autonomous
realization, exact strict-selector fan criterion, coefficient-uniform actual
weighted-degree survival in the exact gate, two distinct least periods, and
marked monodromy recovery with declared side information.  Established
ingredients are not claimed as new individually.  The conclusion may state
that the proof is complete in the main body; it must not state the internal
page count.

#### 8.3 Proof-only evidence statement — 0.30 page

State in scientific language that every result is derived symbolically and
that the displayed finite examples are hand-derived sanity checks,
counterexamples, or boundary illustrations rather than evidence for a
universal claim.  Do not mention an experiment tracker, hardware, runtime,
workflow, or internal review.

## Formal result and counterexample inventory

The later source must use this numbering order and these semantic labels.
The exact final theorem numbers may shift only mechanically if the class
numbers sections differently; the order and labels may not change.

| Public result | Semantic label | Internal ownership | Main-body location |
|---|---|---|---|
| Theorem A, full family-wise theorem | `thm:main` | T1--T8 | Section 1.2; proof assembled from Sections 2--7 |
| Proposition 2.1, symplecticity and inverse | `prop:symplectic-inverse` | P1, C01, T1 | Section 2.2 |
| Lemma 2.2, selected gradient matrices | `lem:selected-matrices` | P2, C02--C03 | Section 2.3 |
| Theorem 3.1, strict normal-fan iff | `thm:selector-fan` | P6, C04, T2 | Sections 3.1--3.2 |
| Corollary 3.2, rational/integer seeds | `cor:rational-seed` | P6 | Section 3.2 |
| Counterexample 3.3, equality wall | `cex:fan-wall` | F3, X12 | Section 3.3 |
| Theorem 4.1, incidence realization | `thm:incidence-realization` | P7, C05--C06, T3 | Sections 4.1--4.3 |
| Example 4.2, repeated-label manual fixture | `ex:ell-three-fixture` | X03--X04 sanity fixture | Section 4.4 |
| Lemma 5.1, strict matrix growth | `lem:strict-growth` | P3 | Section 5.1 |
| Theorem 5.2, exact carry lift | `thm:carry-lift` | P4, C07, T4 | Section 5.2 |
| Proposition 5.3, coefficient-uniform survival | `prop:leading-survival` | P5, C08, T4 | Section 5.3 |
| Counterexample 5.4, dimension-one cancellation | `cex:dimension-one` | F1 | Section 5.4 |
| Lemma 6.1, constant scalar forcing | `lem:scalar-forcing` | P8, C09 | Section 6.1 |
| Theorem 6.2, ordered monodromy | `thm:ordered-monodromy` | P9, C10, T5 | Section 6.2 |
| Lemma 6.3, digit bounds and injectivity | `lem:digit-code` | P10, C11--C12 | Section 6.3 |
| Theorem 6.4, decoder ladder | `thm:decoder` | P11, C13, T6 | Section 6.4 |
| Boundary 6.5, missing decoder data | `rem:decoder-boundary` | F6, X09 | Section 6.5 |
| Theorem 7.1, two least periods | `thm:least-periods` | P12, C14, T7 | Section 7.1 |
| Proposition 7.2, scalar and coordinate annihilators | `prop:recurrences` | P13, C15--C16, T8 | Sections 7.2--7.4 |
| Counterexample 7.3, initial complete-state residual | `cex:initial-residual` | F2, X11 | Section 7.4 |
| Remark 7.4, planar obstruction | `rem:planar-obstruction` | retained exact obstruction | Section 7.5 |

F4 is split beside the claims it limits: \(H=1\) is in Section 4.4, while a
shorter quotient permutation and a nonprimitive word are in Section 7.1.
F5 is split beside the relevant hypotheses: unequal totals in Section 3.3,
and zero exponent, positive characteristic, and zero coefficient in Section
5.4.  Every failure fixture is therefore adjacent to its hypothesis rather
than isolated in an appendix.

## Complete T/C/P/X traceability

### Theorem and public-claim placement

| Obligation | Exact main-body placement and disposition |
|---|---|
| T1 / C01 | Theorem A(1) and Proposition 2.1, Section 2.2; P1 gives the Hessian proof and inverse. |
| C02--C03 | Lemma 2.2, Section 2.3; P2 gives rowwise differentiation and rank-one multiplication. |
| T2 / C04 | Theorem A(2) and Theorem 3.1, Sections 3.1--3.4; P6 proves the V-max/W-min selector iff and its separation from carry. |
| T3 / C05--C06 | Theorem A(3) and Theorem 4.1, Sections 4.1--4.3; P7 proves every-word incidence realization, exact existing-competitor gap, and singleton convention. |
| T4 / C07 | Theorem A(4), Lemma 5.1, and Theorem 5.2, Sections 5.1--5.2; P3--P4 prove the exact coordinatewise gate and induction. |
| T4 / C08 | Theorem A(4) and Proposition 5.3, Section 5.3; P5 proves survival for every nonzero coefficient tuple. |
| C09 | Lemma 6.1, Section 6.1; P8 proves constant scalar forcing. |
| T5 / C10 | Theorem A(5) and Theorem 6.2, Section 6.2; P9 proves the ordered prefixes and monodromy. |
| T6 / C11--C12 | Theorem A(6) and Lemma 6.3, Section 6.3; P10 proves digit bounds and pair injectivity. |
| T6 / C13 | Theorem A(6) and Theorem 6.4, Sections 6.4--6.5; P11 proves the decoder and exact information losses. |
| T7 / C14 | Theorem A(7) and Theorem 7.1, Section 7.1; P12 proves two distinct least periods. |
| T8 / C15--C16 | Theorem A(8) and Proposition 7.2, Sections 7.2--7.4; P13 proves every recurrence, index domain, residual, and anti-minimality statement. |
| C17 | Section 1.3 and Table 2; the bounded literature comparison is independent of the mathematical proof and supports no absence theorem. |
| C18 | Physically realized by the complete Abstract and Sections 1--8 main-body allocation above: 22.0 core plus 4.5 peripheral equals 26.5 pages.  This is a plan-level mass audit and is not typeset as a scientific claim. |

### Adversarial-check placement

| Check | Main-body proof or falsifier |
|---|---|
| P28-X01 | Proposition 2.1 / P1, Section 2.2 |
| P28-X02 | Lemma 2.2 / P2, Section 2.3 |
| P28-X03 | Theorem 4.1 / P7, Sections 4.1--4.2 |
| P28-X04 | Remark 3.4 and Theorem 4.1 / P6--P7, Sections 3.3 and 4.2--4.3 |
| P28-X05 | Theorem 5.2 / P3--P4, Sections 5.1--5.2 |
| P28-X06 | Lemma 5.1 through Proposition 5.3 / P3--P5, Sections 5.1--5.3 |
| P28-X07 | Theorem 6.2 / P9, Section 6.2 |
| P28-X08 | Lemma 6.3 / P10, Section 6.3 |
| P28-X09 | Theorem 6.4 and Boundary 6.5 / P11, Sections 6.4--6.5 |
| P28-X10 | Theorem 7.1 / P12, Section 7.1 |
| P28-X11 | Proposition 7.2 and Counterexample 7.3 / P13, Sections 7.2--7.4 |
| P28-X12 | Equality wall 3.3, spike boundary 4.4, cancellation/support boundaries 5.4, decoder boundary 6.5, and period/recurrence boundaries 7.1--7.5 |

No T, C, P, X, or F obligation is deferred to supplementary material.

## Dependency and forward-reference order

The proof dependency is frozen as follows:

\[
 \mathrm{P1}
 \quad\text{is an independent map-level branch},
\]

\[
 \mathrm{P2}\longrightarrow
 \begin{cases}
   \mathrm{P3}\longrightarrow\mathrm{P4}\longrightarrow\mathrm{P5},\\
   \mathrm{P6}\longrightarrow\mathrm{P7}.
 \end{cases}
\]

The two weighted-degree branches rejoin only when Proposition 5.3 upgrades
the Section 4 selector realization to actual polynomial weighted degrees.
After that join,

\[
 (\mathrm{P6},\mathrm{P7})\to\mathrm{P8},
 \qquad
 (\mathrm{P2},\mathrm{P8})\to\mathrm{P9},
 \qquad
 \mathrm{P7}\to\mathrm{P10},
 \qquad
 (\mathrm{P9},\mathrm{P10})\to\mathrm{P11},
\]

\[
 (\mathrm{P6},\text{spike geometry},\text{primitivity})\to\mathrm{P12},
 \qquad
 (\mathrm{P8},\mathrm{P4})\to\mathrm{P13}.
\]

P1 does not feed P2.  C17 is an independent positioning branch, and C18 is
the final mass audit.  No arrow originates in a literature search miss,
finite fixture, computation, or machine certificate.

Forward references are permitted only in four controlled places:

1. Theorem A announces the clauses proved later.
2. Section 2.4 points forward to Section 5 for actual weighted-degree
   survival.
3. Theorem 4.1 points forward to Theorem 5.2 and Proposition 5.3 before using
   the phrase “actual polynomial weighted degree.”
4. Section 6.1 points forward to Section 7 only for scalar consequences.

Every other result must cite only earlier propositions or prove the needed
identity locally.  In particular, Section 3 may use residual-diagonal
decomposition but may not assume the explicit constant \(\mu\), and Section
4 may not use coefficient-uniform survival before Section 5.

## Exact display-equation register

The later `main.tex` must display, not bury inline, every equation in this
register.  Semantic labels are fixed for cross-reference.

### Construction and map

1. `eq:word`: the rooted primitive word and \(\ell\ge3\).
2. `eq:permutation`: \(Pe_j=e_{j+1\pmod\ell}\),
   \(Pe_\star=e_\star\), \(P^\ell=I\), \(P\mathbf1=\mathbf1\).
3. `eq:spike`: \(u_0=\mathbf1+(H-1)e_0\).
4. `eq:incidence-exponents`:

   \[
    \alpha_a=\rho\mathbf1+K\sum_{j\in S_a}e_j
      +K(\ell-|S_a|)e_\star,
    \qquad
    \beta_b=\rho\mathbf1+K\sum_{j\notin T_b}e_j
      +K|T_b|e_\star.
   \]

5. `eq:common-total`: \(D=\rho r+K\ell\).
6. `eq:hamiltonians`: the two collected-support sums with
   \(\xi_a,\zeta_b\in\Bbbk^*\).
7. `eq:shears` and `eq:map-order`: the two shears, simultaneous permutation,
   and \(F_{\mathsf w}=\Pi_P\circ T_W\circ S_V\).
8. `eq:inverse`: with \(\bar q=P^{-1}Q\),
   \(\bar p=P^{-1}\mathsf P\),

   \[
    F_{\mathsf w}^{-1}(Q,\mathsf P)=
    \left(\bar q-\nabla W(\bar p),
    \bar p-\nabla V(\bar q-\nabla W(\bar p))\right).
   \]

### Selected matrices, fans, and incidence

9. `eq:selected-matrices`:
   \(A_\alpha=\mathbf1\alpha^{\mathsf T}-I\) and
   \(B_\beta=\mathbf1\beta^{\mathsf T}-I\).
10. `eq:rank-one-product`, first generally and then at common total D:

    \[
     B_\beta A_\alpha
     =I+\mathbf1((B-1)\alpha-\beta)^{\mathsf T},
     \qquad
     C_{a,b}=P+\mathbf1c_{a,b}^{\mathsf T}.
    \]

11. `eq:digit-definition`:
    \(c_{a,b}=(D-1)\alpha_a-\beta_b\),
    \(\lambda=(D-1)^2\), and
    \(c_{a,b}^{\mathsf T}\mathbf1=\lambda-1\).
12. `eq:normal-fans`: both definitions of
    \(\mathcal N_V^+\) and \(\mathcal N_W^-\), with every strict
    competitor inequality.
13. `eq:selector-cone`: the complete pulled-back intersection
    \(\mathcal C_{\mathsf w}\).
14. `eq:residual-step`:

    \[
     C_n(x_n+t_n\mathbf1)=Px_n+
     (c_n^{\mathsf T}x_n+\lambda t_n)\mathbf1.
    \]

15. `eq:w-sign-reversal`: the equal-total W difference after the V shear,
    with its leading minus sign.
16. `eq:score-constants`:
    \(C_0=\rho(H+\ell)+K\ell\) and \(g=K(H-1)>0\).
17. `eq:score-table`:

    \[
     \alpha_a^{\mathsf T}x_j=C_0+g\mathbf1_{\{j\in S_a\}},
     \qquad
     \beta_b^{\mathsf T}x_j=C_0+g\mathbf1_{\{j\notin T_b\}}.
    \]

### Carry and actual weighted degrees

18. `eq:strict-growth`: the coordinate identity in Lemma 5.1.
19. `eq:first-carry-gate`: \(0<m_0<A_{\alpha_{a_0}}u_0\), explicitly
    coordinatewise.
20. `eq:weight-transport`:

    \[
     m_{n+1}=PA_{\alpha_n}u_n,
     \qquad
     u_{n+1}=PB_{\beta_n}A_{\alpha_n}u_n.
    \]

21. `eq:coefficient-domain`:
    \((\xi,\zeta)\in(\Bbbk^*)^{|E_V|+|E_W|}\).

### Scalar forcing, monodromy, and decoder

22. `eq:scalar-forcing`:

    \[
     \mu=(D-1)(C_0+g)-C_0>0,
     \qquad
     u_n=P^nu_0+t_n\mathbf1,
     \quad t_0=0,
     \quad t_{n+1}=\lambda t_n+\mu.
    \]

23. `eq:t-closed`: \(t_n=\mu(\lambda^n-1)/(\lambda-1)\).
24. `eq:prefix-definition`: \(Q_s=C_{s-1}\cdots C_0\).
25. `eq:prefix-rank-one`:

    \[
     Q_s=P^s+\mathbf1R_s^{\mathsf T},
     \qquad
     R_s^{\mathsf T}=\sum_{j=0}^{s-1}
       \lambda^{s-1-j}c_j^{\mathsf T}P^j,
     \qquad
     R_s^{\mathsf T}\mathbf1=\lambda^s-1.
    \]

26. `eq:monodromy`: \(M_{\mathsf w}=Q_\ell=I+\mathbf1R_\ell^{\mathsf T}\).
27. `eq:monodromy-spectrum`:

    \[
     \chi_{M_{\mathsf w}}(z)=(z-1)^{r-1}(z-\lambda^\ell),
     \qquad
     M_{\mathsf w}^k=I+
     \frac{\lambda^{k\ell}-1}{\lambda^\ell-1}
     \mathbf1R_\ell^{\mathsf T}\quad(k\ge0).
    \]

28. `eq:phase-prefix`:

    \[
     Q_sM_{\mathsf w}^ku_0=P^su_0+
     \left[R_s^{\mathsf T}u_0+
     \lambda^s\frac{\lambda^{k\ell}-1}{\lambda^\ell-1}
     R_\ell^{\mathsf T}u_0\right]\mathbf1,
     \quad 0\le s<\ell.
    \]

29. `eq:digit-bounds`: \(0<(c_{a,b})_i<\lambda\) for every coordinate.
30. `eq:pair-injectivity`:
    \((a,b)\mapsto c_{a,b}\) is injective on the map-specific support
    dictionary.
31. `eq:decoder-expansion`: restate
    \(R_\ell^{\mathsf T}=\sum_{j=0}^{\ell-1}
    \lambda^{\ell-1-j}c_j^{\mathsf T}P^j\) immediately before decoding.

### Periods and recurrences

32. `eq:quotient-obstruction`:
    \(P^du_0-u_0=c\mathbf1\), followed by the star-coordinate deduction
    \(c=0\) for \(0<d<\ell\).
33. `eq:q-order-two`:

    \[
     q_{n+2}-(1+\lambda)q_{n+1}+\lambda q_n=0,
     \qquad n\ge0.
    \]

34. `eq:q-length-ell`:

    \[
     q_{n+\ell+1}-\lambda q_{n+\ell}-q_{n+1}+\lambda q_n=0,
     \qquad n\ge0.
    \]

35. `eq:moving-coordinate` and `eq:star-coordinate`:

    \[
     y_n^{(i)}=1+(H-1)\mathbf1_{\{n\equiv i\pmod\ell\}}+t_n
     \quad(i\in I_{\mathrm{mov}}),
     \qquad
     y_n^{(\star)}=1+t_n.
    \]

36. `eq:y-annihilator`:

    \[
     y_{n+\ell+1}^{(i)}-\lambda y_{n+\ell}^{(i)}
     -y_{n+1}^{(i)}+\lambda y_n^{(i)}=0,
     \qquad i\in I,\ n\ge0.
    \]

37. `eq:phase-subsequence` and `eq:z-annihilator`:

    \[
     z_m^{(i,s)}=y_{s+m\ell}^{(i)},
     \qquad
     z_{m+2}^{(i,s)}-(1+\lambda^\ell)z_{m+1}^{(i,s)}
       +\lambda^\ell z_m^{(i,s)}=0,
    \]

    with \(i\in I\), \(s\in I_{\mathrm{mov}}\), and \(m\ge0\).
38. `eq:complete-maximum`:
    \(d_n=\max\{\max_i(u_n)_i,\max_i(m_n)_i\}\) and \(d_n=q_n\) only
    for \(n\ge1\).
39. `eq:d-annihilator`:

    \[
     d_{n+\ell+1}-\lambda d_{n+\ell}-d_{n+1}+\lambda d_n=0,
     \qquad n\ge1.
    \]

40. `eq:initial-residual`:

    \[
     d_{\ell+1}-\lambda d_\ell-d_1+\lambda d_0
     =\lambda(d_0-q_0),
    \]

    together with the iff
    \(d_0=q_0\Longleftrightarrow
    \max_i(m_0)_i\le\max_i(u_0)_i\).

### Failure displays

41. `eq:dimension-one-cancellation`: for
    \(V(q)=q^2\), \(W(p)=-p^2/4\), display
    \(q-(p+2q)/2=-p/2\).
42. `eq:residual-800`: display
    \(d_4-100d_3-d_1+100d_0=100(10-2)=800\).
43. `eq:planar-obstruction`: display the projective map and its strictly
    negative derivative from Section 7.5.

No equation in this register may be supported only by the hand fixture.

## Citation ownership and exact placement

External citations own background and adjacency only.  P1--P13 own every
new theorem.  Proof paragraphs must not end with a citation that could be
read as transferring proof ownership.

| Manuscript location | Sources to cite | Exact permitted use |
|---|---|---|
| Section 1.3, polynomial automorphisms | Janeczko--Jelonek (2008); Friedland--Milnor (1989) | Polynomial symplectomorphisms and automorphism-word/degree theory are established subjects; neither proves this construction. |
| Sections 1.3, 2.4, and 3.1, weighted degrees | Blanc--van Santen (2022); Meunier preliminary manuscript, n.d.; Shao--Sun arXiv preprint (2025) | Weighted degrees, leading forms, valuations, and inequality regions are established; no two-fan every-word theorem is attributed. |
| Sections 1.3 and 7.2, monomial recurrences | Hasselblatt--Propp (2007) together with its corrigendum; Bedford--Kim (2008) | Monomial degree chambers and recurrence behavior are context only.  Any precise Hasselblatt--Propp use cites the corrigendum in the same sentence. |
| Section 1.3, state cycles | Gunawardena (2003); Akian--Gaubert--Lemmens--Nussbaum (2006); Ohmori--Yamazaki (2024) | Long state cycles and nonlinear/max-plus periodic behavior are established, but state period is not selector period. |
| Sections 1.3 and 4.3, switched schedules | Zorzenon--Komenda--Raisch (2024) | Their schedule is external; the present selector word is endogenous to one fixed map. |
| Sections 1.3 and 6.2, cluster/tropical products | Fordy--Hone (2011); Fordy--Hone (2014); Ishibashi--Kano (2021); Kim (2026) | Structured symplectic/Poisson cluster maps, sign itineraries, and ordered tropical matrices are adjacent; conjectural general statements are not called theorems. |
| Sections 1.3 and 8.1, entropy context | Bellon--Viallet (1999); Hone--Ragnisco--Zullo (2016) | Degree-growth and algebraic-entropy literature is context for an explicit nonclaim; no entropy conclusion is drawn. |

Bibliographic status is fixed as follows: versions of record anchor published
entries; Shao--Sun is labelled a preprint; Meunier is an author-hosted
preliminary manuscript with no invented year, venue, DOI, pagination, or
peer-review status; Ohmori--Yamazaki uses article number 082705; Kim uses
article 7; Fordy--Hone (2011) uses article 091; Hone--Ragnisco--Zullo uses
article 02LT01 and VOR year 2016; and the Hasselblatt--Propp corrigendum DOI
is retained.  The bounded-search sentence must be refreshed at publication
lock before source freeze, but a search miss may never support an absolute
priority claim.

Planned citation keys for the later bibliography are:
`JaneczkoJelonek2008`, `FriedlandMilnor1989`,
`BlancVanSanten2022`, `MeunierPreliminary`, `ShaoSun2025`,
`HasselblattPropp2007`, `HasselblattProppCorrigendum2007`,
`BedfordKim2008`, `Gunawardena2003`,
`AkianGaubertLemmensNussbaum2006`, `OhmoriYamazaki2024`,
`ZorzenonKomendaRaisch2024`, `FordyHone2011`, `FordyHone2014`,
`IshibashiKano2021`, `Kim2026`, `BellonViallet1999`, and
`HoneRagniscoZullo2016`.

## Tables, examples, and figure policy

The final article has exactly three hand-typeset tables:

1. the notation table in Section 2.1;
2. the grouped established-neighbor table in Section 1.3; and
3. the decoder side-information ladder in Section 6.4.

There are no empirical tables, sampled outcomes, data plots, generated
figures, architecture diagrams, or supplementary graphics.  The dependency
order is prose plus displayed arrows, not a figure.  The \(\ell=3\) fixture
is a hand-typeset example distributed only where it audits notation, digits,
and the initial recurrence boundary; it is never called validation of the
general theorem.

## Anonymity, zero-execution, and anti-claim firewall

The public article and all three later source files must contain none of the
following: paper or batch numbers, candidate identifiers, filesystem paths,
hashes, lifecycle markers, gate names, reviewer roles or identities,
governance chronology, internal novelty/proof scores, release history,
author identity, acknowledgments that reveal identity, repository links,
machine hostnames, or internal evidence vocabulary.

The manuscript may say only that the proofs are symbolic and the examples
are hand-derived.  It must not report scripts, notebooks, CAS, solvers,
CPU/GPU runs, parameter sweeps, random tests, datasets, generated artifacts,
sample counts, success rates, runtimes, or machine certificates, because no
such evidence supports the theorem.  No empirical or computational claim is
introduced during writing.

The following phrases or implications are forbidden throughout title,
abstract, body, captions, and bibliography annotations:

- “first,” “only,” “unprecedented,” “no previous work,” or an exhaustive
  priority claim;
- one map for all words, one map per length, or fixed dimension for
  unbounded length;
- ordinary total degree where weighted degree is meant;
- an exact-degree, algebraic-degree, dynamical-degree, entropy,
  integrability, generic-nonconjugacy, inverse-reciprocity, or
  cohomological-spectrum theorem;
- a periodic polynomial state;
- scalar word decoding, scalar separation of words, or a minimal recurrence;
- literal labels without the labelled support dictionary, or a rooted word
  without marked phase zero;
- positive-characteristic validity, zero-coordinate support survival, or a
  cancellation classification outside the frozen hypotheses; and
- a finite fixture, search miss, citation, or computation as proof of a
  universal clause.

## Exact source-trio handoff contract

This plan creates no manuscript source.  Only after separate downstream
authorization may an author create the exact trio
`paper/main.tex`, `paper/math_commands.tex`, and `paper/references.bib`.
Those three files, and no fourth scientific source file, receive the
following handoff.

### `paper/main.tex`

- Use the public-safe title and anonymous author metadata.
- Follow Sections 0--8, subsection order, result order, semantic labels, and
  exact page allocation in this plan.
- State Theorem A once in Section 1.2 and prove all clauses in Sections 2--7.
  No theorem-critical proof, hypothesis, decoder boundary, recurrence index,
  or failure fixture may be moved to an appendix, supplement, footnote, or
  external source.
- Include exactly the 43 registered display groups, allowing aligned lines
  within a group but no change in order, sign, transpose, domain, or start
  index.
- Include exactly three hand-typeset tables and no figure environment.
- Cite only with the planned keys and only for the ownership described above.
- Keep the selector iff and actual carry lift as separate results.  Keep
  singleton vacuity, the decoder ladder, the two least periods, the moving
  versus star formulas, and the \(q/d/y/z\) start indices literal.
- End the scientific text with the limitations and proof-only evidence
  language, not with governance, code availability, or an unsupported data
  statement.

### `paper/math_commands.tex`

- Contain semantic notation macros only; it must not contain theorem text,
  proof steps, bibliography data, author metadata, or hidden claims.
- Provide one unambiguous macro each for the field, input word, all-ones
  vector, moving index set, fan cones, selector cone, map, prefix product,
  monodromy, and the four scalar families.  Suggested stable names are
  `\field`, `\word`, `\onevec`, `\Imov`, `\NVplus`, `\NWminus`,
  `\selectorcone`, `\Fword`, `\prefixQ`, `\monodromy`, `\qmax`,
  `\dmax`, `\ycoord`, and `\zphase`.
- Do not overload \(W\) for the word, \(m\) for a phase index, or \(r\) for
  a projective coordinate in the main theorem.  Local use of \(r\) in the
  planar-obstruction remark must be explicitly scoped or renamed there.
- Preserve transpose notation, bold/all-ones notation, strict inequalities,
  and characteristic-zero field notation consistently.

### `paper/references.bib`

- Include only entries actually cited in `main.tex`, drawn from the eighteen
  planned keys above; do not add secondary summaries to support a theorem.
- Use VOR metadata and DOI for published claims, retain arXiv only as an
  access aid where appropriate, and keep all article numbers as article
  numbers rather than fabricated page ranges.
- Encode Meunier as an author-hosted preliminary manuscript with `n.d.` or no
  invented year, no venue or DOI, and a publication-lock access date.
- Include the Hasselblatt--Propp corrigendum whenever the original is used
  precisely; do not merge the two records.
- Label Shao--Sun as a preprint and distinguish proved results from
  conjectural statements in the cluster-map references.
- Refresh DOI/status and the bounded post-cutoff conjunction search at the
  publication-lock gate before freezing bytes.  Any new close source changes
  positioning, never the already proved internal mathematics without a new
  scientific authorization.

Cross-file compilation must fail loudly on an undefined semantic macro,
undefined theorem reference, or missing citation key.  The trio must not
load data, code, figures, generated tables, external URLs at build time, or
any file beyond the later authorized source/build profile.

## Final author-stop checklist

Before a later source author declares stop, verify all of the following
against the frozen source trio:

- The title and one-sentence claim are public-safe and family-wise.
- Theorem A contains T1--T8 with every frozen hypothesis and information
  boundary.
- C01--C17 have their assigned public locations, while C18 is physically
  realized by the exact 26.5-page main-body mass and is not printed as an
  internal planning claim.
- P1--P13 and F1--F6 are complete in the main body; X01--X12 each have the
  assigned proof or falsifier.
- The exact map order, inverse, V-max/W-min sign, strict carry chamber,
  ordered product, digit rotations, and decoder ladder are unchanged.
- Singleton supports have full cones, vacuous uniqueness, and no fictitious
  competitor gap.
- \(q_n\), \(y_n^{(i)}\), and their stated annihilators start at \(n=0\);
  \(z_m^{(i,s)}\) starts at \(m=0\); \(d_n\)'s annihilator starts at
  \(n=1\); and the removed initial residual is exactly
  \(\lambda(d_0-q_0)\).
- The two least-period claims remain distinct and no periodic polynomial
  state is inferred.
- Every citation owns background only, all mutable metadata has been
  refreshed, and no absolute priority language appears.
- There are exactly three hand-typeset tables, no figures, no empirical
  section, no proof appendix, no generated asset, and no scientific
  execution claim.
- The public anonymity firewall and every locked anti-claim hold in all
  three files.
- The anonymous content mass is exactly 22.0 core plus 4.5 peripheral equals
  26.5 pages, with references excluded.

BATCH07_PAPER28_PAPER_PLAN_FROZEN
