# R5 E1 — Independent mathematical review of CGR5

## Verdict and exact reviewed bytes

**PROVABLE AS STATED. Zero mathematical or source-applicability must-fixes.**
The full local/global affine good-model classification in Theorem CGR5
survives the review without a hypothesis change. This is a current-team,
nonauthor mathematical review, not human peer review, a worldwide priority
certificate, an independent-substantiality decision, or paper admission.

The complete author proof and final companion report were read, including
all four examples and their scope limitations. This verdict binds:

| Author artifact | SHA-256 |
| --- | --- |
| [PROOF_PACKAGE.md](../../b3_composition_good_models/PROOF_PACKAGE.md), 618 lines | `3f810fa619ee61805ffd236514300844372d1dc5fca5215d8ff0049db31fcc4c` |
| [REPORT.md](../../b3_composition_good_models/REPORT.md), 259 lines | `9508495d93d76839777efb2ac028afbb1557588d98db0b18df91653586870b92` |

The final report includes its rendering-only punctuation repair. No change
to the mathematical reasoning was requested or made during this review.
Hashes identify the reviewed bytes; the arguments below, not those hashes,
are the basis of the mathematical verdict.

## 1. Frozen question and dependency boundary

The domain is every number field $K$, its full ring of integers
$R=\mathcal O_K$, and every nonempty finite ordered word
$$
F=H_r\circ\cdots\circ H_1,\qquad
H_i(x,y)=(y,f_i(y)-a_i x),\qquad \deg f_i=d_i\ge2,
$$
with arbitrary $a_i\in K^\times$ and $f_i\in K[y]$. Put
$D=\prod_i d_i$, $\delta=\prod_i a_i$, and let $b_i$ be the leading
coefficient of $f_i$. At a finite place, $v$ is normalized to have value
group $\mathbb Z$, $O_v=\mathcal O_{K_v}$, and $q_v$ is the size of
its residue field. A chart is any affine map over the original $K_v$
locally, or one affine map over the original $K$ globally. Both full maps
in the new coordinates must be integral, both reduced degrees must remain
$D$, and the reduced projective indeterminacy sets must be geometrically
disjoint. The native tick is one full application of $F$.

The proof does not assume factorwise good reduction, individual-unit
Jacobians, equal coordinate scales, tame residue characteristic, a PID,
a finite word-length bound, or potential good reduction after extension.
There is no infinite-place condition. These are the exact quantifiers I
checked; a weaker leading-coefficient or factorwise classification would
not discharge this question.

The dependency chain is complete:

1. Exact leading forms and integral primitive row directions give all
   possible affine linear parts, modulo integral affine right composition.
2. Two pure subleading coefficients give an exhaustive finite centre list;
   the full forward/inverse coefficient test decides each entry.
3. The native two-sided bounded set identifies the unique passing affine
   lattice and consequently all local charts.
4. Denominator-aware additive CRT patches centres. The determinant ideal
   is necessary, and an explicit two-ideal matrix proves sufficiency.

No scout assertion is used as an unproved mathematical input. The relevant
accepted GR5 mechanisms were checked against the actual earlier proof and
C426 manuscript sections; they are credited in §8 rather than counted anew.

## 2. Leading forms and arbitrary affine rigidity

The forward recursion $P_{i+1}=f_i(P_i)-a_iP_{i-1}$ has strictly increasing
new degrees. The subtracted old coordinate cannot cancel its leading term.
The inverse recursion runs in the opposite order with coefficient
$b_i/a_i$. It therefore gives exactly
$$
F_D=(0,By^D),\qquad (F^{-1})_D=(Cx^D,0),
$$
$$
B=\prod_i b_i^{\prod_{j>i}d_j},\qquad
C=\prod_i(b_i/a_i)^{\prod_{j<i}d_j}.
$$
In particular, $\deg F_1=D/d_r<D$ and $\deg(F^{-1})_2=D/d_1<D$.
The inverse exponents and the $r=1$ empty products are correct.

For a completely arbitrary good chart $T(z)=Az+c$, let $\ell_1,\ell_2$
be the row forms of $A$ and $e_1,e_2$ the standard column vectors.
The degree-$D$ parts are
$$
BA^{-1}e_2\ell_2^D,\qquad CA^{-1}e_1\ell_1^D.
$$
Write $\ell_1=su_1$, $\ell_2=tu_2$ with primitive integral row forms.
Each $u_i^D$ has a unit pure-power coefficient, including when the residue
characteristic divides $D$. Hence integrality forces both entries of
$Bt^DA^{-1}e_2$ and $Cs^DA^{-1}e_1$ integral, while degree preservation
forces each vector to have a unit entry. No cancellation between different
coordinates or nonunit binomial coefficients evades this conclusion.

The indeterminacy sets at infinity are precisely the zeros of $\bar u_2$
and $\bar u_1$. The last homogeneous coordinate is $Z^D$; a common factor
of the tuple could only be a power of $Z$, excluded by a surviving top
term. Reduction of the integral inverse identities also excludes affine
indeterminacy. Geometric separation of these two points is equivalent to
independence of the reduced row forms. Thus
$$
A=\operatorname{diag}(s,t)U,\qquad U\in\mathrm{GL}_2(O_v).
$$
This proves the rectangle reduction from arbitrary affine matrices; it
does not presume diagonal charts. Right-composition by $U^{-1}$ preserves
all good-reduction conditions, because integral affine conjugacy and its
reduction extend to projective linear automorphisms.

The diagonal-chart leading coefficients become $Bt^{D-1}$ and
$Cs^{D-1}$. Their required unit valuations force independently
$$
v(s)=-v(C)/(D-1),\qquad v(t)=-v(B)/(D-1).
$$
Both Jacobian determinants are integral constants, namely $\delta$ and
$\delta^{-1}$, so $v(\delta)=0$. No conclusion about an individual $a_i$
is justified or taken. Conversely, these scale conditions and integrality
of all coefficients supply unit top terms and the two distinct coordinate
points at infinity. The claimed full-coefficient sufficiency is valid.

## 3. Exhaustive centres, mixed terms, and the quadratic boundary

Write $S(X,Y)=(sX+c_x,tY+c_y)$. Let $\eta_y=[x^0y^{D-1}]F_2$ and
$\eta_x=[x^{D-1}y^0](F^{-1})_1$. Every monomial of $F_2$ other than
$By^D$ has total degree at most $D-1$. Thus no mixed term can have
$y$-degree $D-1$: a positive $x$-degree would violate that total-degree
bound. Terms with smaller $y$-degree cannot acquire a larger one by
diagonal translation. This proves the exact extracted coefficient
$$
[Y^{D-1}](S^{-1}FS)_2=t^{D-2}(DBc_y+\eta_y).
$$
The inverse argument gives $s^{D-2}(DCc_x+\eta_x)$. Neither expression
contains the other centre. The output-centre subtraction only changes
degree zero and therefore does not affect these formulas even at $D=2$.

Using the forced leading valuations, their integrality gives precisely
$$
c_x\in -\eta_x/(DC)+(s/D)O_v,\qquad
c_y\in -\eta_y/(DB)+(t/D)O_v.
$$
Integral right translations identify centres modulo $sO_v\times tO_v$.
Each remaining quotient is $O_v/DO_v$, so the candidate count
$q_v^{2v(D)}$ is finite and exhaustive over the original local field.
It is not advertised as an optimal bound. This handles all ramification
and primes dividing $D$ without treating $D$ as a unit.

The two centre restrictions are only necessary tests. Formula (20) then
checks every coefficient of all four full coordinate polynomials, including
constants, mixed terms and cancellations. Its output scales are correctly
$s$ for $F_1,V_1$ and $t$ for $F_2,V_2$. Ordinary binomial coefficients,
not division by factorials in the valuation ring, give the formula.

I specifically compared the $D=2$ case with old GR5. Write the single
quadratic as $f(Y)=bY^2+f_1Y+f_0$. GR5's reduced one-centre polynomial
is $q=f-aY$, so its linear coefficient is $f_1-a$.
CGR5 instead extracts pure coefficients from the full maps and correctly
uses $\eta_y=f_1$, $\eta_x=f_1/a$. This is not a missing $-a$ term.
For one quadratic factor the two base centres differ from GR5's by
$a/(2b)\in(s/2)O_v$, since $a$ and $bs$ are units. The full candidate
cosets therefore agree; the forward first and inverse second coordinates
enforce the remaining equality of centre classes. As a direct boundary
control, $H=(y,y^2+y-x)$ over $\mathbb Q_2$ has CGR5 base centre $-1/2$
and the valid candidate $0$ in each direction. No tame restriction is hidden.

## 4. Intrinsic filled rectangle and all local models

For an integral normalized $G,G^{-1}$ with unit top forms
$(0,uy^D)$ and $(wx^D,0)$, both preserve $O_v^2$. If
$M=\max(|x|,|y|)>1$ and $|y|=M$, the unique top monomial of $G_2$
has norm $M^D$, while all its other terms and every term of $G_1$ have
norm at most $M^{D-1}$. Therefore the next second coordinate is strictly
dominant and forward iterates grow through $M^{D^j}$. If the first
coordinate is maximal, the inverse gives the corresponding backward
escape. Equal initial norms are covered, not omitted.

Consequently the complete two-sided bounded set is exactly $O_v^2$.
Invertible affine maps preserve bounded sequences in both directions, so
every good rectangle chart maps $O_v^2$ to the intrinsic bounded set of
the native full $F$. This proves uniqueness without looking at the bounded
set of any factor. No local compactness or algebraic closure is needed.

The side ideals are already forced by the leading coefficients. Two such
rectangles agree exactly when their centres agree modulo those ideals.
Thus at most one tested centre pair passes. Combining this with the
primitive-row reduction proves that all local charts are exactly
$S\operatorname{Aff}_2(O_v)$. The term “left coset” is used correctly:
this is an orbit under right composition. Unit changes of $s,t$ and
changes of residue representatives do not create additional models.

## 5. Finiteness and global translation patching

The global rejections involve $\delta\in R^\times$ and the finitely
supported valuations of $B,C$. When the scale exponents are integral, set
$$
I_x=\prod_v\mathfrak p_v^{-v(C)/(D-1)},\qquad
I_y=\prod_v\mathfrak p_v^{-v(B)/(D-1)}.
$$
Here $\mathfrak p_v$ is the prime ideal belonging to $v$.
Afterward, only places at which $B,C$
are nonunits or a full forward/inverse coefficient has a denominator
need local search. Outside that set, the identity chart is already good.
A prime dividing $D$ need not be searched separately when this direct
certificate applies.

At a selected place a local scale may be chosen in $K^\times$ using an
element of $\mathfrak p\setminus\mathfrak p^2$. This does not assume
$\mathfrak p$ principal. Representatives for the finite quotient can be
chosen in $R$, so the finitely many passing local centres may be taken
in $K$ and set to zero elsewhere.

For either direction ideal $I$, the proof selects $h\in R\setminus\{0\}$
with $J=hI$ integral and all finitely many $hc_v\in R$. CRT is imposed
at every prime with $v(J)>0$, including primes introduced by clearing
denominators. At the other primes the desired congruence is automatic
from integrality. Thus $c=z/h$ satisfies $c-c_v\in IO_v$ everywhere.
Omitting those extra denominator primes would be a gap; this proof does
not omit them. Two solutions differ by $I$ by valuation intersection.
Applying the construction separately to the two directions establishes
the exact centre coset $c^*+(I_x\oplus I_y)$, with no translation
obstruction left over.

## 6. Product-ideal necessity, construction, and all global models

Let $L=I_x\oplus I_y$. Any global good chart has local image lattices
$AO_v^2=LO_v$ and centre difference in $LO_v$ at every finite place.
For $z\in L$, the vector $A^{-1}z$ is integral everywhere and hence lies
in $R^2$. Together with the reverse inclusion this proves $AR^2=L$.
Taking exterior squares gives the necessary equality
$$
(\det A)=I_xI_y.
$$
It applies to all mixed matrices, not only diagonal charts. Separate
principality of $I_x,I_y$ would be an unjustified stronger obstruction.

The constructive converse is also complete. The two-generator argument
for a fractional ideal uses module CRT at the finitely many primes where
one chosen generator has excess valuation; at every other prime that
generator is already minimal. Thus take $I_x=(\alpha,\beta)$ and
$u,v\in I_x^{-1}$ with $\alpha u+\beta v=1$. If
$I_xI_y=(\gamma)$, the displayed matrix
$$
A=\begin{pmatrix}\alpha&\beta\\-\gamma v&\gamma u\end{pmatrix}
$$
has determinant $\gamma$ and maps $R^2$ into $L$. For $x\in I_x$,
$y\in I_y$, its inverse gives
$$
A^{-1}(x,y)=(ux-\beta y/\gamma,\;vx+\alpha y/\gamma)\in R^2,
$$
proving surjectivity onto the actual embedded lattice, not merely an
abstract module isomorphism. This covers nonprincipal distinct ideals
and the case where a second ideal generator may be chosen zero.

For $T(z)=Az+c^*$, each $S_v^{-1}T$ has integral translation and linear
part in $\mathrm{GL}_2(O_v)$. Hence it is a good chart everywhere.
The same reasoning proves exactly the all-model formula (11):
$$
\{Az+c: AR^2=L,\quad c-c^*\in L\}.
$$
Its charts form one left coset of
$\operatorname{Aff}_2(R)$. A global affine reexpression multiplies the
determinant ideal by a principal ideal, so its class is coordinate-invariant.
The freeness/product-principality equivalence is not assumed from a
PID-only theorem; it is proved explicitly here.

## 7. Independent hand checks of the examples

**Order-three mixed repair.** For $\omega^2-\omega+6=0$,
$P=(2,\omega-1)$ and $\lambda=\omega+1$, the split-prime residues
and $N(\lambda)=8$ give $P^3=(\lambda)$. The norm form
$m^2+mn+6n^2$ has no value $2$, so $P$ is nonprincipal and its class
has exact order three. The two-factor map has $D=4$,
$B=\lambda^{-2}$, $C=\lambda^{-1}$, hence $I_x=P,I_y=P^2$.
For local generators $s,t$, both $t^2/(\lambda s)$ and $s^2/t$ are
units. The normalized map is explicitly a composition of two integral
unit-top Hénon factors, certifying the inverse as well as the map.

In the proposed global matrix, $u=-1$, $v=-\omega/2$ really satisfy
$2u+(\omega-1)v=1$ and $v\in P^{-1}$, since
$P(\omega/2)$ is generated by $\omega$ and $-3$. The matrix is
exactly the preceding constructive matrix, has determinant $\lambda$,
and has image $P\oplus P^2$. A diagonal chart would principalize both
ideals and is impossible. Finally, no nonzero output combination of the
degree-two and degree-four coordinates becomes nonconstant affine linear:
the degree-four term first forces its coefficient zero, then the degree-two
term forces the other zero. This invariant excludes affine conjugacy to
a single degree-four Hénon factor.

**Order-five obstruction.** For $\theta^2-\theta+12=0$,
$P=(2,\theta)$ and $\lambda=\theta+4$, the other prime above two
does not divide $\lambda$, while $N(\lambda)=32$. Thus
$P^5=(\lambda)$. The completed-square norm expression excludes norm
$2$, giving exact order five without a class-number assumption.
The quadratic/cubic word has $D=6$, $I_x=P,I_y=P^3$.
The local coefficients $t^2/(\lambda s)$ and $s^3/t$ are units,
so a good chart exists at every place, but $[P]^4\ne1$ obstructs every global
affine chart. Local solvability was proved, not inferred from the ideals.

**Nonunit factors.** Direct substitution in (29) yields
$H_i=T_iGT_{i-1}^{-1}$ with the displayed diagonal intermediate charts,
so the full product is $G^3$. It is everywhere good even though the
first and third factor Jacobians are $p$ and $p^{-1}$. A single such
factor cannot have a good affine chart at $p$ because its constant
Jacobian and inverse Jacobian cannot both be integral. This is a valid
counterexample to imposing factorwise goodness on the frozen question.

**Wild centres.** For $F=(y,y^2+y-x)^2$ over $\mathbb Q_2$,
both pure cubic coefficients are $2$, giving base centres $-1/2$.
The identity chart proves that the pair $(0,0)$ passes; it occurs at
$\alpha=\beta=2\bmod4$. Filled-set uniqueness excludes the other
classes. No execution of sixteen tests is claimed or required. The
single-factor specialization returns GR5's common scale, common centre
class, and ideal-square criterion, with a possibly less sharp candidate
count as the author explicitly states.

## 8. Antecedent subtraction and primary-source applicability

I read the relevant actual [GR5 proof](../../../../research_c424_c428/continuation_round5/arithmetic/PROOF_PACKAGE.md),
its [nonauthor review](../../../../research_c424_c428/continuation_round5/GR5_REVIEW/REVIEW.md),
the [coordinator source check](../../../../research_c424_c428/continuation_round5/GR5_COORDINATOR_SOURCE_CHECK.md),
and C426's final classification, local-rigidity, local-test and global
proof sections. GR5 already contains primitive-row reduction with two
initial scales; its single-factor coordinate relations then force them
equal. Integral affine invariance, filled-ball uniqueness, wild finite
translation tests, additive CRT, determinant/Steinitz reasoning and the
rank-two matrix construction are substantial antecedents, not new
mechanisms merely because they have been proved again for this word.

The proposed increment is the unrestricted composition classification
with independent directions and centres, the native filled rectangle,
and its unequal-ideal behavior. The examples establish a genuine
difference from the single-factor square rule. Whether this extension is
independently substantial enough for a separate paper is expressly outside
this mathematical audit and is not implied by that difference.

For source applicability I personally checked these primary passages:

| Primary source actually read | Applicable content and limit |
| --- | --- |
| [Kawaguchi, Definition 4.1 and Propositions 4.2–4.3, with proofs](https://msp.org/ant/2013/7-5/ant-v7-n5-p08-s.pdf), printed pp. 1240–1242 | The regular-good definition, homogeneous leading-ideal criterion and normalized good-reduction escape/norm mechanism are antecedents. The source works over an algebraically closed valued field. CGR5 instead proves its test over the original completion and checks geometric reduction explicitly; it does not deduce descent from the cited estimates. These passages are not the stated all-chart/two-ideal classification. |
| [Bruin–Molnar, Propositions 2.10 and 2.12, translated-coefficient formula, Algorithm 3.8 and its justification](https://arxiv.org/html/1204.4967) | Affine normalization and finite valuation/translation searches are established model techniques. Their objects are rational functions on the projective line and minimal resultants. Their affine matrix subgroup fixes infinity on that line; it is not the group of arbitrary affine automorphisms of the plane. No direct application supplies the full map/inverse rectangle theorem. |
| [Petsche–Stout, definitions, Theorem 1, Lemmas 5 and 7, Proposition 6 and the final global proof](https://arxiv.org/html/1303.5783v1) | Lattice intersections, integral stabilizers and local/global patching are antecedents. Their freeness and adelic factorization use a PID; their dynamical object is a projective morphism with a nonvanishing homogeneous lift. Neither condition holds automatically here. CGR5 supplies its separate Dedekind-domain product obstruction and does not misapply that theorem to a Hénon compactification with indeterminacy. |

These are bounded applicability checks, not an exhaustive subsequent-
literature search. I do not claim personal retrieval of the additional
sources attributed only to X2 in the author's report. The three checked
sources and accepted GR5 provide genuine ownership deductions; absence
of the exact displayed theorem in their checked passages is not a
worldwide no-collision conclusion.

## 9. Final disposition and work receipt

The original CGR5 question is answered by a complete necessary-and-sufficient
local test, a unique local affine lattice and all local charts, exact global
translation patching, and the necessary-and-sufficient ideal-product
obstruction with all global charts. All stated examples survive direct hand
verification. There is no required mathematical or source-applicability
repair in the bound author files.

Keep separate: correctness of this classification; bounded source ownership;
independent substantiality relative to GR5/C426; coordinator admission;
manuscript, evaluation and release gates. This review only closes the first
and its checked source-applicability obligations. It assigns no manuscript
number, extra contract count, evaluator grade or target-arithmetic inference.
It does not declare LG4 or WM6 solved. `NO_BAD_EULER_OR_ROOT_NUMBER` remains.

The repository batch workflow and the `research-review`/`proof-writer`
instructions guided exact-claim normalization, counterexample and boundary
checks, and a self-contained final verdict. The current-team/no-upload
instruction supersedes historical external-review examples; no external
MCP/model review is represented as having occurred. Only this assigned
review file was written. Mathematical programs, old certificate reruns,
new agents, external model/API uploads, Git changes, shared-index changes,
author-file changes and manuscript/PDF operations: **zero**.
