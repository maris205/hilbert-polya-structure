# R5 B3 — All-affine good models for arbitrary Hénon compositions

2026-09-09 UTC. Author investigation, not admission. This report and
`PROOF_PACKAGE.md` are the only assigned write targets. Every preceding
batch, scout, proof and review remains read-only. Mathematical programs:
zero; no program allocation requested.

## Frozen complete question

For every number field $K$, $R=\mathcal O_K$, every integer $r\ge1$, and
every ordered word
$$
F=H_r\circ\cdots\circ H_1,\qquad
H_i(x,y)=(y,f_i(y)-a_i x),
$$
where $a_i\in K^\times$, $f_i\in K[Y]$, and $d_i=\deg f_i\ge2$,
classify all affine coordinate maps over each original completion $K_v$
that give regular good reduction, then classify all affine coordinate
maps over $K$ that are good simultaneously at every finite place.

Regular good reduction means that the conjugated full map and its full
inverse both have integral coefficients, both reductions retain degree
$D=\prod_i d_i$, and the degree-$D$ homogenizations have disjoint
geometric indeterminacy sets after reduction. All affine matrices and
translations are allowed. No extension of $K_v$ or $K$, no nonaffine
conjugacy, and no change of compactification is allowed. No factorwise
goodness, no common factor model, and no condition that each $a_i$ be a
unit is assumed. One application of the complete $F$ is the native tick.

The required outcome is a necessary-and-sufficient finite local test,
the complete set of local models and their possible nonuniqueness, and
the precise global obstruction with a construction and all-model formula
when it vanishes. A two-factor or tame-only answer is not completion.

## Initial status and decisive proof checks

At assignment: **NOT CURRENTLY JUSTIFIED**. X2's proposed pure leading
forms, rectangle radii, finite centre candidates, bounded-set uniqueness
and ideal-product obstruction were scout conjectures, not accepted inputs.
They were independently proved in `PROOF_PACKAGE.md`; none is retained
as an unproved scout input.

The bounded discriminator is a pure proof audit, with no executable test:

1. Prove leading forms for both full compositions without cancellation.
2. Starting with an arbitrary affine matrix, derive integral independent
   row directions from geometric separation at infinity.
3. Derive radii and centre restrictions, especially possible mixed-term
   contamination at total degree $D-1$ and wild primes dividing $D$.
4. Prove uniqueness by the two-sided bounded orbit set of the full map;
   do not substitute a factor clock or presume a scalar square.
5. Patch both centre coordinates and prove sufficiency of the exact
   determinant-ideal obstruction for possibly distinct nonprincipal ideals.
6. Exhibit a truly rectangular arithmetic example and explicitly show
   why individual factor-Jacobian conditions cannot replace the full test.

If any step fails, preserve the full question and state the missing lemma
or exact counterexample. No computation or source analogy can silently
replace one of these proof obligations.

## Provenance and source ownership to subtract

The original GR5 full contract, proof, independent review, coordinator
source check and C426 first manuscript review were read before the new
proof. GR5 is imported as a completed theorem only on its stated
single-factor domain; its internal mechanisms are explicitly credited
when generalized. The repository batch workflow and the `proof-writer`
and `research-lit` skills were read in full for this task. Current
continuous authorization overrides the older workflow's stop-after-five
wording, without changing this lane's assignment or admission authority.

Classical regular-good-reduction definitions, local escape/filled-set
estimates, affine integral-conjugacy invariance, additive approximation,
Dedekind ideal arithmetic and the rank-two determinant/Steinitz criterion
are not claimed as new mechanisms. X2 is assigned an independent
source-only comparison; its report is not a mathematical review or
automatic novelty/admission certificate.

## Completed author result

**Author proof status: PROVABLE AS STATED.** The frozen full question
survives unchanged. The theorem and its complete proof are in
[PROOF_PACKAGE.md](PROOF_PACKAGE.md), Theorem CGR5 and §§1–6.

Write $b_i$ for the leading coefficient of $f_i$, and put
$$
\delta=\prod_i a_i,\qquad
B=\prod_{i=1}^r b_i^{\prod_{j=i+1}^r d_j},\qquad
C=\prod_{i=1}^r(b_i/a_i)^{\prod_{j=1}^{i-1}d_j}.
$$
The full leading forms are $(0,By^D)$ and $(Cx^D,0)$ for $F$ and
$F^{-1}$, respectively. No highest-degree cancellation is possible in
the factor recursion. The inverse formula includes every $a_i$ in its
correct nested exponent.

The complete local prescription is as follows.

1. Reject unless
   $$
   v(\delta)=0,\qquad
   k_x=-v(C)/(D-1)\in\mathbb Z,\qquad
   k_y=-v(B)/(D-1)\in\mathbb Z.
   $$
   Choose scales $v(s)=k_x$, $v(t)=k_y$.
2. Let $\eta_x$ be the coefficient of $x^{D-1}$ in $(F^{-1})_1$,
   and $\eta_y$ that of $y^{D-1}$ in $F_2$, with the other variable
   to exponent zero. Set $c_x^0=-\eta_x/(DC)$ and
   $c_y^0=-\eta_y/(DB)$. Test all pairs
   $$
   c_x=c_x^0+(s/D)\alpha,\qquad
   c_y=c_y^0+(t/D)\beta,
   \qquad \alpha,\beta\in O_v/DO_v.
   $$
   This means a choice of representatives and exactly
   $q_v^{2v(D)}$ pairs, including all wild cases. Test every coefficient
   of $S^{-1}FS$ and $S^{-1}F^{-1}S$, where
   $S(x,y)=(sx+c_x,ty+c_y)$.
3. At most one pair passes modulo $sO_v\times tO_v$. If it passes,
   all good affine maps, including arbitrary mixed matrices, are
   exactly $S\operatorname{Aff}_2(O_v)$. Their common image is the
   intrinsic two-sided bounded-orbit set of the full $F$.

The proof derives $A=\operatorname{diag}(s,t)U$ with
$U\in\mathrm{GL}_2(O_v)$ from an arbitrary good affine matrix, using
primitive row forms and disjoint reduced indeterminacy points. It does
not impose the rectangle at the outset. The two centre formulas are
proved by excluding mixed monomials of the relevant variable degree;
the remaining lower terms are all tested, not discarded. The escape
argument uses the native full map and its inverse, covers equal input
norms, and yields uniqueness even at wild places.

Globally only finitely many coefficient or leading-form denominator
places need testing. If every place passes, set
$$
I_x=\prod_v\mathfrak p_v^{-v(C)/(D-1)},\qquad
I_y=\prod_v\mathfrak p_v^{-v(B)/(D-1)}.
$$
Separate additive CRT arguments patch the two centre coordinates to
$c^*\in K^2$; no translation obstruction remains. A global affine
model exists exactly when $I_xI_y$ is principal. All models are
$$
\{Az+c: AR^2=I_x\oplus I_y,\quad c-c^*\in I_x\oplus I_y\},
$$
one left coset of $\operatorname{Aff}_2(R)$ when nonempty. The class
$[I_xI_y]$ is independent of all chart choices and global affine
reexpression.

Sufficiency is constructive: if $I_x=(\alpha,\beta)$,
$\alpha u+\beta v=1$ with $u,v\in I_x^{-1}$, and
$I_xI_y=(\gamma)$, use
$$
A=\begin{pmatrix}\alpha&\beta\\-\gamma v&\gamma u\end{pmatrix}.
$$
The proof verifies both $\det A=\gamma$ and $AR^2=I_x\oplus I_y$
by writing the inverse on an arbitrary vector of that lattice. This
does not assume either direction ideal principal.

## Decisive arithmetic and boundary checks

All four checks below are exact proof examples in `PROOF_PACKAGE.md`
§7, not claimed program executions.

| Check | Actual conclusion |
| --- | --- |
| $K=\mathbb Q(\sqrt{-23})$, $P=(2,\omega-1)$, $P^3=(\omega+1)$; quadratic $H_1=(y,y^2/(\omega+1)-x)$ followed by $H_2=(y,y^2-x)$ | $I_x=P$, $I_y=P^2$, both nonprincipal but product principal. The displayed matrix $\left(\begin{smallmatrix}2&\omega-1\\\omega-3&-\omega-1\end{smallmatrix}\right)$ gives a global good model; no diagonal global good model exists. |
| $K=\mathbb Q(\sqrt{-47})$, $P=(2,\theta)$, $P^5=(\theta+4)$; quadratic denominator factor followed by a monic cubic | Every local test passes, but $I_x=P$, $I_y=P^3$ and $[I_xI_y]=[P]^4\ne1$. Thus no global affine good model exists. |
| Three explicit factors with $a_1=p$, $a_2=1$, $a_3=p^{-1}$ | Their full composition is $(y,y^2-x)^3$, already everywhere good. Individual nonunit Jacobians cannot be rejected factor by factor. |
| Over $\mathbb Q_2$, $F=(y,y^2+y-x)^2$ | $D=4$ and both base centres are $-1/2$, while the unique passing centre pair is $(0,0)$ modulo $\mathbb Z_2^2$. The wild candidate list is essential. |

The first example is not affinely conjugate to a single-factor map of
degree four: its coordinate degrees are two and four, and no nonzero
affine output combination is a nonconstant affine-linear polynomial.
This property is incompatible with the first coordinate of a single
Hénon factor under affine conjugacy. The second example verifies the
nonprincipal class directly from the norm form and $P^5=(\theta+4)$,
without assuming the entire class-number computation. When $r=1$,
the theorem reduces to GR5's common-scale square and ideal-square
criterion; the larger two-centre candidate bound is not claimed sharper.

## Primary-source comparison and subtraction

The author personally retrieved and read the passages in the following
table on 2026-09-09. The comparison is restricted to the actual checked
statements and proofs. Source antecedents are deducted even when a
self-contained proof is supplied here.

| Source and passages actually read | Owned mechanism and exact scope boundary |
| --- | --- |
| Shu Kawaguchi, *Local and global canonical height functions for affine space regular automorphisms*, Algebra & Number Theory 7 (2013); Definition 4.1 and Propositions 4.2–4.3 with their proofs, printed pp. 1240–1242. [Publisher primary PDF](https://msp.org/ant/2013/7-5/ant-v7-n5-p08-s.pdf). | The regular-good definition, leading-ideal separation criterion, and good-reduction Green/norm estimates are classical. The normalized unit-ball mechanism is deducted. These passages do not classify all affine charts by the displayed coefficient tests and two ideal classes. The source's valued field is algebraically closed; the present coefficient test stays over the original $K_v$ and checks geometric reduction separately. |
| Nils Bruin and Alexander Molnar, *Minimal models for rational functions in a dynamical setting*, LMS Journal of Computation and Mathematics 15 (2012), 400–417; Propositions 2.10 and 2.12 with proofs, §3's translated-coefficient formula and Algorithm 3.8 with termination/correctness argument. [Primary author text](https://arxiv.org/html/1204.4967). | Affine/projective model reduction and finite valuation/translation searches are established techniques. Their objects are rational functions on $\mathbb P^1$ and minimal resultants; their $\mathrm{Aff}_2$ fixes infinity on that line. It is not the group of all affine maps of $\mathbb A^2$. The checked results do not supply the full-map/inverse rectangle classification. |
| Clayton Petsche and Brian Stout, *Global minimal models for endomorphisms of projective space*, author version arXiv:1303.5783v1 (2013); definitions, Theorem 1, Corollary 2, Lemmas 5 and 7, Proposition 6, and final global-model proof. [Primary author text](https://arxiv.org/html/1303.5783v1). | Lattice intersections, adelic integral stabilizers, and global model patching are antecedents, not new ideas here. Their ring is a PID and their projective morphism has a nonvanishing homogeneous lift. A Hénon compactification has indeterminacy; arbitrary $\mathcal O_K$ need not be a PID. Thus their checked theorem cannot simply be applied as CGR5, although its gluing mechanism must be subtracted. |

The author also read the entire current
[X2 source-only report](../x2_arithmetic_replacement/REPORT.md). X2
records additional primary checks, including normalized quadratic
filled sets, GIT stability, the 2024 open-problems discussion and recent
valuation-complex work. Those are X2's separately attributed retrievals,
not a claim that this author personally reread all those sources. Its
bounded search found no checked theorem giving the complete new
classification. Neither that outcome nor the present table proves
worldwide novelty or independent substantiality.

The author's own bounded queries included:

```text
"Hénon" "composition" "good reduction" affine
"regular polynomial automorphisms" "good reduction" conjugate lattice
"Hénon" "good reduction" "affine" composition lattice
"Hénon" "minimal models" number field
"polynomial automorphism" "good reduction" "Steinitz"
```

These yielded no directly checked collision theorem. Broad unrelated
search snippets were not treated as evidence. There was no exhaustive
database or authenticated Scholar search, and no worldwide-priority
certificate is asserted.

The strongest subtraction is the internal accepted **GR5 theorem**.
Its primitive-row reduction already produces two scales; its special
linear coordinate equations then force them equal. That argument is
not a new CGR5 invention. The new full question removes the linear
coordinate relation by permitting every finite word, so the proof must
classify independent scales and centres and retain the correct product
ideal. Classical CRT, the determinant/Steinitz obstruction and the
rank-two matrix construction are likewise deducted. The result is not
presented as a new general theorem about Dedekind modules.

After subtraction, the author proposes only the complete unrestricted
composition classification and its genuinely rectangular arithmetic
behavior as the surviving mathematical increment. Whether that is
independently substantial enough for a separate contract, rather than
an extension of GR5, is expressly a nonauthor/coordinator decision.
The examples establish different arithmetic behavior; they do not by
themselves establish paper-level substance.

## Verification and handoff

The author reread the complete theorem and proof after drafting and
checked the hypothesis/quantifier match, both leading-form recursions,
primitive-row integrality in small residue characteristic, total-degree
exclusion of mixed-centre contamination, the $D=2$ boundary, norm ties
in two-sided escape, finite bad-place support, denominator-aware CRT,
and the constructive two-ideal matrix and examples. No intentionally
unproved lemma remains in the author package. Independent checking
of this assertion remains required.

The proof-writing skill required an exact status, dependency map and
edge-case audit; the literature skill required direct source attribution
and separation of antecedents from the proposed increment. They did not
authorize experiments, external-model review or additional write targets.
Only this report and `PROOF_PACKAGE.md` were written. Mathematical
programs, old certificate reruns, external model/API reviews, Git
operations, manuscript/PDF writes and shared-file edits: **zero**.

The files are ready for independent mathematical/source review. No
manuscript number, fourth contract count, formal evaluator grade, PDF
or release is claimed. LG4 and WM6 are not redefined or declared solved;
this is an explicitly different full composition-model question.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.
