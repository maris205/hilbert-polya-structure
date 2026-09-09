# R5 X2 — Arithmetic replacement scout: affine good models of Hénon words

2026-09-09 UTC. Bounded candidate/source scout, not an author proof,
independent mathematical review, admission, or paper-count decision.
Only the present report is written. Earlier rounds remain frozen.

## 1. Decision and exact status

Of the two formulations considered, retain **B, the complete all-affine
local/global model problem for arbitrary finite Hénon compositions**, for
one author proof and subsequent independent substantiality review. Do not
retain A, the polynomial-versus-affine single-factor formulation, as an
additional candidate.

B is a viable full-question proof candidate, not yet a demonstrated new
independent paper. Its prospective increment is the classification for the
whole composition, with two potentially different canonical coordinate
scales and a product-ideal obstruction. The primitive-row argument, finite
valuation tests, unit-ball description, additive approximation, and
Steinitz obstruction machinery already have owners and must be subtracted.
In particular, a successful proof is not itself a decision that this is
substantial enough to be separate from C426/GR5.

The coordinator has assigned B3 the full author proof. The formulas in §4
are the X2 feasibility interface sent before that assignment and are
**proposed statements requiring proof**, not mathematical premises supplied
by this report. B3 reports independent derivations and is writing them;
this report neither anticipates its final proof status nor substitutes for
the independent review.

The bounded primary-source search found no checked theorem that directly
gives B's complete classification. This is not a worldwide priority
certificate or a claim that the question is known to be open.

## 2. Local-first collision and obstruction boundary

The starting records were the original LG4, GR5, and WM6 frozen contracts,
the relevant B1/B2/B3 and X2 first-wave obstruction records, and GR5's
actual proof package. The latter's local rigidity, wild-centre search,
global approximation, explicit free-basis construction, and examples were
read. Its contract and proof expressly exclude general compositions.

The following deductions are already unavailable as new candidates:

- LG4's all-modulus orbit compatibility is not established by profinite
  completion, a bounded-degree statement, or finite-place Green data.
  The B2 height-compatibility obligation remains unproved.
- The WM6 multiplier blind region is not repaired by merely renaming a
  fixed finite jet. The B3/X2 marked-cycle constructions already separate
  finite return-jet data from the global good-model obstruction.
- GR5 already classifies every affine good chart for every single factor
  over every number field. Its canonical local disc square and exact
  ideal-square obstruction are imported in full.
- Applying a classical integral-cycle period bound after selecting a
  local good chart does not detect a global ideal class. The C2 composition
  period-boundedness source collision also remains deducted.

B changes the model family explicitly; it does not relabel a weak partial
answer to LG4 or WM6 as their completion. None of those frozen questions
is changed. It is also separate in object and arithmetic from the admitted
polynomial Livšic and uniform local periodic-field contracts and the
optimal-cycle measure problem.

## 3. The two formulations; B's frozen full question

### A — Not selected

For every number field K and single-factor map
F(x,y)=(y,f(y)-ax), a nonzero and deg(f) at least two: if some polynomial
K-conjugacy takes F to a regular everywhere-good polynomial automorphism,
must an affine K-conjugacy do the same?

The arbitrary-field amalgamated-product conjugacy theorem makes this very
close to classical. Baake–Roberts, §2 and Proposition 2(3), supplies the
arbitrary-K group statement. Writing F=t e, with t the coordinate swap
and e elementary, its cyclically reduced word has length two. If the
regular target is affine-K-conjugate to a cyclically reduced representative,
the only cyclic arrangements are te and et; they differ by conjugacy by t,
and the remaining basic-group conjugacy is affine. This implication is
our deduction from that source, not a quoted theorem.
[Baake–Roberts, primary text, pp. 3–7](https://arxiv.org/pdf/math/0501151).

The remaining field-preserving bridge was not source-certified here.
Dujardin–Favre §1.2 says regular maps become Hénon compositions after a
linear change, but the standing field in §§1–4 is algebraically closed
(the number-field exceptions are §§1.6–1.7). It cannot be cited without
qualification to settle the K-rational bridge. A is rejected as an
unpromising independent increment, **not** declared proved, false, or
source-closed over every number field.
[Dujardin–Favre, §1 opening and §1.2, primary text](https://arxiv.org/pdf/1405.1377).

### B — Frozen question for the prospective author task

**Objects and all parameters.** Let K be any number field and
R=O_K. For every r at least one and every ordered word

$$
F=H_r\circ\cdots\circ H_1,\qquad
H_i(x,y)=(y,f_i(y)-a_i x),
$$

allow arbitrary f_i in K[Y] of degrees d_i at least two and arbitrary
a_i in K^×. Write b_i for the nonzero leading coefficient of f_i and
D=\prod_{i=1}^r d_i. No monicity, centring, coefficient integrality,
individual unit-Jacobian, class-number, or residue-characteristic
restriction is imposed. Factors are not assumed individually good in
any chosen coordinates.

**Domain and clock.** The domain is the full affine plane over K and
each K_v. One native step is the whole F, not one factor and not D
steps. D is its algebraic degree, not a period or clock conversion.

**All allowed charts.** Locally T_v(z)=A_v z+c_v with
A_v in GL_2(K_v), c_v in K_v²; globally T(z)=Az+c with
A in GL_2(K), c in K². Arbitrary mixing, unequal scales, and both
translations are in scope. No extension of K_v or K, nonlinear
polynomial conjugacy, or birational change is allowed in B.

**Good reduction convention.** For G=T_v^{-1}FT_v require, at every
finite place under consideration:

1. All coefficients of both G and G^{-1} belong to O_v.
2. Both reduced degrees are D.
3. The indeterminacy sets of their projective extensions are disjoint
   over the algebraic closure of the residue field.

The first item means an automorphism over O_v, not just an integral
forward map. The last two are essential. This is the regular-good
definition in Kawaguchi, Definition 4.1; the original text is over an
algebraically closed valued field, while the coefficient and projective
conditions here are tested over K_v and its residue-field closure.
[Kawaguchi, Definition 4.1](https://msp.org/ant/2013/7-5/ant-v7-n5-p08-s.pdf).

**Complete question.** For all the above inputs:

- Give a necessary and sufficient, terminating finite test for local
  existence, including all wild translation branches, and describe
  every good affine chart.
- Determine whether the underlying affine O_v-lattice is unique and
  make the resulting invariant independent of chart choices.
- If every finite place has a good affine chart, give the exact
  necessary and sufficient condition for a single global affine chart;
  describe all such global charts and construct one when it exists.
- Handle every ideal class and every affine direction. A diagonal-only
  criterion, a class-number-one theorem, or a sufficient factorwise
  criterion does not close this question.

The observable is the actual finite-place model/lattice classification.
The arithmetic carriers are coefficient valuations, fractional ideals,
and their ordinary determinant ideal. No Fredholm determinant, Euler
factor, root number, or target-spectral identification is asserted.

## 4. Proposed cheap proof interface, not a proof certificate

The following identities and implications were sent to the coordinator
and B3 as the bounded feasibility route. B3 must prove them under §3's
full quantifiers, repair any false intermediate statement without silently
shrinking the question, and supply its own complete argument.

Put empty products equal to one and define

$$
B=\prod_{i=1}^r b_i^{\prod_{j=i+1}^r d_j},\qquad
C=\prod_{i=1}^r (b_i/a_i)^{\prod_{j=1}^{i-1}d_j}.
$$

The expected highest homogeneous parts are

$$
F_D=(0,BY^D),\qquad (F^{-1})_D=(CX^D,0).
$$

For an arbitrary affine-good T=Az+c, adapt GR5's primitive-row and
opposite-indeterminacy argument to force

$$
A=\operatorname{diag}(s,t)U,\quad U\in\mathrm{GL}_2(O_v),
\qquad
v(s)=-\frac{v(C)}{D-1},\quad
v(t)=-\frac{v(B)}{D-1}.                       \tag{4.1}
$$

These are two scales, not a presumed common scale. The necessary
Jacobian condition is v(\prod_i a_i)=0; replacing it by v(a_i)=0
for every i would change the question.

For diagonal/translated T(x,y)=(sx+u,ty+w), put

$$
\gamma_y=[Y^{D-1}]F_2,\qquad
\gamma_x=[X^{D-1}](F^{-1})_1,
\quad
w_0=-\frac{\gamma_y}{DB},\quad
u_0=-\frac{\gamma_x}{DC}.
$$

The proposed necessary centre containers are

$$
u\in u_0+(s/D)O_v,\qquad
w\in w_0+(t/D)O_v.                          \tag{4.2}
$$

Modulo sO_v and tO_v, these give at most
|k_v|^{2v(D)} pairs. Test **every coefficient** of the resulting G
and G^{-1}, not only the two coefficients used to bound the centres.
Finite residue fields make this a finite test; at tame places v(D)=0
there is one candidate pair. The degree-two case, arbitrary lower terms,
and mixed monomials in the composition require explicit checks.

The proposed uniqueness discriminator is the two-sided filled set.
For a diagonal-good form, if a point has norm greater than one, a
coordinate of maximal norm should force escape under forward or backward
iteration through the corresponding pure unit top term. Thus the set of
points with bounded full F-orbit should be precisely O_v² in that chart.
This would identify every good image as one and the same rectangle in
the original coordinates. The general filled-set idea is old; its use
cannot be separately counted as a result.

If every local test passes, (4.1) proposes canonical fractional ideals

$$
I_x=\prod_v\mathfrak p_v^{-v(C)/(D-1)},\qquad
I_y=\prod_v\mathfrak p_v^{-v(B)/(D-1)}.
$$

After separately patching the two centre coordinates, the expected
global obstruction is

$$
I_x\oplus I_y\text{ is free over }R
\quad\Longleftrightarrow\quad [I_x I_y]=1.    \tag{4.3}
$$

The right side is a **product class**, not a declaration that each ideal
is principal and not an unexamined copy of GR5's square class. CRT
patching, determinant necessity, and rank-two Steinitz sufficiency are
classical machinery. The claim that these particular canonical ideals
classify every composition chart is the new obligation.

### Author-reported discriminator, pending actual-file review

B3 reports the following r=2 example over K=Q(√−23), with
ω=(1+√−23)/2, P=(2,ω−1), and A=ω+1, so P³=(A):

$$
H_1=(y,y^2/A-x),\qquad H_2=(y,y^2-x).
$$

Its proposed canonical ideals are I_x=P and I_y=P². Each is
nonprincipal but the product is principal. B3 supplies the candidate
basis matrix

$$
M=\begin{pmatrix}2&\omega-1\\\omega-3&-\omega-1\end{pmatrix},
\qquad \det M=A,
\qquad MR^2=P\oplus P^2.
$$

The arithmetic P³=(A) and nonprincipality are already in GR5, not new
number-field discoveries. The intended new contrast is that different
nonprincipal directions can cancel: neither a global diagonal chart nor
the single-factor same-ideal square captures this example. The full
local coefficient checks and the basis equality belong to B3's proof and
independent review; this report does not certify them from a message.

## 5. Primary-source subtraction actually checked

The main scout opened the primary texts below and read the identified
passages. Statements about their scope refer to those passages, not an
assertion that every unexamined page lacks another theorem.

| Source and actual passages | Already owned; boundary for B |
| --- | --- |
| Kawaguchi, ANT 7 (2013), Definition 4.1 and Propositions 4.2–4.3 with proofs, pp. 1240–1242 | Regular-good definition, top-form ideal criterion, and exact good-reduction Green/norm relation. These are background, not an all-affine coefficient/ideal classification. [Primary PDF](https://msp.org/ant/2013/7-5/ant-v7-n5-p08-s.pdf). |
| Bruin–Molnar, LMS J. Comput. Math. 15 (2012), Propositions 2.10/2.12, §3 centre/valuation search including Algorithm 3.8, Proposition 6.3 and Example 6.4 | One-dimensional rational-map minimal resultant, affine/full-projective distinctions, finite translation search, and nonprincipal-ideal obstructions. Their Aff₂ notation is not Aff(A²). The displayed family is on P¹, not a Hénon word with an inverse and two indeterminacy points. [Primary author text](https://arxiv.org/pdf/1204.4967). |
| Petsche–Stout, author version arXiv:1303.5783, definitions, Theorem 1/Corollary 2, Proposition 6/Lemma 7 and final model-patching proof | PID lattice factorization and global minimal models for projective morphisms. Their nonvanishing homogeneous lift is essential. A Hénon compactification has indeterminacy, and arbitrary O_K need not be a PID. The gluing idea is nevertheless fully deducted. [Primary text](https://arxiv.org/pdf/1303.5783). |
| Allen–DeMark–Petsche, arXiv:1610.04271v3, §1.1 standing assumptions and §3.4 Theorem 11 with proof | For their normalized quadratic map over complete locally compact fields of odd residue characteristic, the unit-ball regime is completely described. This is an antecedent for filled-set rigidity, not the full arbitrary-word/all-affine/global criterion. [Primary text](https://arxiv.org/html/1610.04271v3). |
| Lee–Silverman, arXiv:1907.13247v1, Definition 1.1, Theorem 1.2 and its degree-at-least-three proof | GIT stability of rational-map parameter points over algebraically closed characteristic-zero fields, not integral regular-good model existence. For example (y,y^d−x), d≥3, is regular-good at finite places although GIT-unstable in this source's sense. [Primary text](https://arxiv.org/html/1907.13247v1). |
| *Hénon maps: a list of open problems*, published 13 August 2024, §11 through its end | The number-field discussion uses a selected single-factor coordinate model with S-integral coefficients and unit leading/Jacobian parameters, then asks periodic/divisibility questions. That passage does not supply B's all-affine composition classification. It is not an open-status certificate for B. [Primary journal text](https://amj.math.stonybrook.edu/html-articles/Files-2015-2024/23-70/index.html). |
| Lamy, *Tame polynomial automorphisms*, arXiv:2609.05655v1, submitted 4 September 2026; introduction and §§4.1–4.2 definitions/statements | Valuation-complex and stabilizer language is adjacent, but these valuations vanish on nonzero coefficient-field constants and encode weighted degrees. They are not finite-place valuations extending a nontrivial valuation on K. The checked statements do not give (4.1)–(4.3). [Primary text](https://arxiv.org/html/2609.05655v1), [version record](https://arxiv.org/abs/2609.05655). |

The closest internal source is GR5 itself, not a remote paper. Its proof
already uses exactly the pure-row/top-form mechanism to reduce an
arbitrary affine matrix to two diagonal scales. The additional linear
coordinates of a **single factor** then identify those scales and centres.
That second identification is unavailable for a general word. B must
replace it by a complete rectangular classification, not claim that the
shared first part has been newly invented.

## 6. Bounded query ledger and retrieval limitations

Actual search formulations included the following three groups. They
target the same B question, not three additional candidate questions.

```text
Local all-affine classification:
"Hénon" "affine" "good reduction" composition classification
"regular polynomial automorphism" "potentially good reduction"
"Henon" "minimal model" "number field"
"polynomial automorphisms" "integral models" local global

Global compatibility / ideal obstruction:
"Hénon" "good reduction" "class group"
"Henon" "good reduction" "Steinitz"
"polynomial automorphism" "good reduction" "Dedekind"
"regular polynomial automorphism" "affine conjugacy" reduction models

Canonical lattice / composition interface:
"Hénon" "good reduction" "composition" affine
"polynomial automorphism" "good reduction" "lattice"
"Henon" "good reduction" "lattice" site:scholar.google.com OR site:semanticscholar.org
```

Additional source-locator queries used the titles/authors of
Bruin–Molnar and Petsche–Stout. A's bounded searches targeted polynomial
versus affine Hénon conjugacy and led to Baake–Roberts and
Dujardin–Favre; it was not expanded into a third formulation.

Recent screening actually included:

```text
"Hénon" "good reduction" "model" 2024 2025 2026
  [arxiv.org domain filter]
"Henon" "good reduction" "conjugacy"
  [arxiv.org domain filter; 184-day recency]
"regular polynomial automorphisms" "good reduction"
  after:2026-03-09 before:2026-09-10
```

These provider filters are not a complete arXiv submission census;
publication and crawl dates can differ. Lamy's actual version record,
not a search-result date, verifies the recent September submission.
The Scholar/Semantic Scholar discoverability query did not produce a
usable direct exact-theorem record; no authenticated or exhaustive
database search is claimed. Many broad queries returned unrelated
minimal-model, algebraic-group, or numerical Hénon work. Those snippets
are not used as theorem evidence. The endpoint-opened primary texts in
§5 are the evidence used.

## 7. Substantiality test and decisive caveats

Under batch Workflow §2, B is a coherent source-classification question:
it asks whether local integral realizability of the *whole native map*
patches globally and, if not, identifies the exact obstruction. It does
not manufacture a target-arithmetic bridge from an ideal label.

There are two distinct gates:

1. **Mathematical closure.** Prove all of §3, including arbitrary affine
   directions, both inverses/degrees, finite residue fields, every wild
   centre, uniqueness, product-class necessity and sufficiency, and all
   chart choices. The coordinator has assigned the author proof to B3;
   independent review remains required.
2. **Independent substantiality after subtraction.** Decide whether the
   surviving arbitrary-word classification and different arithmetic
   behavior are large enough beyond GR5 to warrant a separate contract.
   This source scout supports taking the bounded proof attempt but does
   not grant that decision. If the completed work is only a mechanical
   generalization of GR5 with classical lattice bookkeeping, retain it
   as an extension/auxiliary result, not another paper.

Particularly important review controls are:

- Check D as degree throughout; do not infer native period changes.
- Do not assume the separate factors preserve the same local lattice,
  or that each a_i is a unit because their product must be a local unit.
- Do not infer regular good reduction solely from a unit Jacobian or
  forward coefficient integrality.
- Do not replace all affine charts by diagonal charts before proving
  the opposite-indeterminacy rigidity.
- Check the centre container with D=2 and v(D)>0 and prove that changing
  representatives modulo the proposed lattice preserves the whole test.
- Prove the underlying rectangle is unique before treating its class
  as a canonical obstruction. Global translations must be patched too.
- Distinguish [I_x I_y]=1 from either individual principality or an
  imported square condition. Verify a genuinely different composition
  example on the actual author file.
- Preserve original LG4/WM6 and the target-Arithmetic Route-A gates.
  A source good-model theorem alone supplies no target Euler factors
  or root numbers: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## 8. Execution, delegation, and handoff

The idea-creation and novelty-check workflows were used for the two-way
pruning and explicit source ownership; the proof-writing checklist was
used to freeze quantifiers and distinguish a proposed interface from a
proved result. Their broad experimental/external-review defaults were
not invoked: the coordinator authorized this bounded pure-proof/source
scout, not mathematical programs, external model uploads, or GPU pilots.

With the coordinator's express approval, the already existing
`lsy_primary_access` child was reused only for A's read-only source check.
It was instructed not to spawn or reuse a nested agent, write files, or
run mathematical programs; no new agent was started for this R5 scout.
The main scout independently read the decisive Baake–Roberts and
Dujardin–Favre passages reported in §3. B3 is the coordinator's separate
author assignment, not an additional X2 delegation or proof outsourced
under a source-check label.

No mathematical program execution, old certificate rerun, formal
evaluation, external model/API review, Git operation, manuscript/PDF
write, or shared-file edit was performed. Text inspection, primary web
retrieval, report writing, and its integrity/readback checks are the only
execution categories here.

**Handoff:** one selected full-question candidate B; A rejected with its
exact near-classical field caveat; B3's complete proof and independent
mathematical/substantiality judgments remain the next gates. No current
paper count or admission status is changed by this report.
