# R5 E5 — independent full-proof review of all-place reversibility

## 1. Verdict and exact review boundary

**PROVABLE AS STATED: the explicit counterexample is valid.**
The universal affirmative implication in the frozen question is false.
There are **zero unresolved mathematical or source-applicability must-fixes**
in the reviewed claims. No author revision was required by this review.

This is a current-team nonauthor mathematical review, not human peer review,
a novelty certificate, a formal Route-A evaluation, an admission decision,
or a completed-paper claim. The separate B1 source/substantiality review and
the coordinator's admission judgment are not replaced by this document.

I read the complete author proof and report, not just their outcomes, at
these exact byte identities:

| Artifact, relative to `continuation_round5/` | Lines | SHA256 |
| --- | ---: | --- |
| `c4_reversor_local_global/PROOF_PACKAGE.md` | 491 | `99bf7efa1486df5a685347aac3bfa6d2c79ab45f241dc1b94c6a5a69b181143e` |
| `c4_reversor_local_global/REPORT.md` | 184 | `2710692dc3c30c5a58a5d448c36ed900ba6aa93b0bc62bbaa8f5ffc958a019de` |

Author locators below refer to this frozen
[proof package](../../c4_reversor_local_global/PROOF_PACKAGE.md) and
[report](../../c4_reversor_local_global/REPORT.md).
I also read the relevant frozen-question, four-factor proposal, failed
two-factor control, and source-comparison passages of the
[X2 scout](../../x2_second_replacement/REPORT.md).
That scout is context and a control, not independent evidence for the
previously unproved centralizer equality.

The proof-writer skill governed exact-claim and implication checks;
research-review was implemented by this independently assigned current-team
review under the repository workflow, with no external reviewer/API;
research-lit governed actual primary-source access and source subtraction.
Only this exclusive review file was written.

## 2. Full question, object, and dependency audit

The frozen question quantifies over every number field $K$ and every finite
nonempty word of generalized Hénon automorphisms
$H_i(x,y)=(y,P_i(y)-a_i x)$, with $P_i\in K[y]$, $\deg P_i\ge2$,
and $a_i\ne0$. It asks whether

$$
\bigl[\forall v\in\Omega_K\ \exists R_v\in
\operatorname{Aut}_{K_v}(\mathbb A^2),\quad R_vFR_v^{-1}=F^{-1}\bigr]
\Longrightarrow
\bigl[\exists R\in\operatorname{Aut}_K(\mathbb A^2),\quad
RFR^{-1}=F^{-1}\bigr].
$$

The author preserves every place, including infinite places, the original
fields, arbitrary polynomial degrees and orders, and the original native
map $F$. Local witnesses may differ with $v$. There is no assumption that
a hypothetical global reversor is affine or involutory.

The negative witness is

$$
K=\mathbb Q(\sqrt7),\qquad H_{c,d}(x,y)=(y,c y^d-x),\qquad
F=H_{4,7}H_{1/16,15}H_{16,15}H_{1/4,7}.
$$

Composition is rightmost first. All four factors have polynomial inverses
$H_{c,d}^{-1}(x,y)=(c x^d-y,x)$ and determinant one. Thus the word is
within the original class. Its rational coefficients do not change the
specified base field from $K$ to $\mathbb Q$. No good-reduction or
integrality condition is needed or asserted.

The dependency chain actually proved is:

1. The full geometric centralizer of
   $F_0=H_{1,7}H_{1,15}H_{1,15}H_{1,7}$ is
   $\{S_\zeta F_0^j:\zeta^8=1,\ j\in\mathbb Z\}$, where
   $S_\zeta=\operatorname{diag}(\zeta,\zeta^{-1})$.
2. A known reversing swap and scalar conjugation give every geometric
   reversor of the family $F_a$, not just candidate reversors.
3. Removing a native power defined over the original number field reduces
   existence to $t^8=a^2$ in that same field.
4. For $a=4$, the classical class $16$ is an eighth power in every $K_v$
   and not in $K$; local reversors are constructed over those actual fields.

Each dependency is checked below. A single counterexample closes the
universal implication negatively; a classification of all words is not
needed and is not claimed.

## 3. Whole-group tree argument and native translation image

### 3.1 The imported group theorem has the required scope

The input is the Jung–van der Kulk equality
$G=\mathcal A*_{\mathcal B}\mathcal E$ for the **entire** polynomial
automorphism group over $\mathbb C$, with the author's triangular
$\mathcal E$ and $\mathcal B=\mathcal A\cap\mathcal E$.
It does not start with a tame subgroup assumed to equal a larger unknown
group: in dimension two the imported theorem gives the full group here.

The graph with vertices $G/\mathcal A$, $G/\mathcal E$ and edges
$G/\mathcal B$ is connected. A non-backtracking circuit would contradict
the nontriviality of an alternating reduced word. Thus the graph is a
tree; the left action preserves vertex types and has no edge inversions.
These are consequences of the stated group input, not an additional
unproved centralizer theorem.

### 3.2 Axis and minimal displacement

Write $H_d=H_{1,d}$. With $e_d=(-x+y^d,y)$ and $\tau=(y,x)$,
one has $H_d=\tau e_d$.
The eight-syllable word
$\tau e_7\tau e_{15}\tau e_{15}\tau e_7$ is reduced and cyclically
reduced: every $e_d$ is nonaffine and $\tau\notin\mathcal B$.
The prefix-edge path and all its native translates therefore concatenate
without backtracking. It gives an axis on which $F_0$ translates by eight
edge lengths, or four consecutive $\mathcal E$-vertices.

For a point off the axis, its branch and the image branch attach at two
distinct axis points. The displacement formula
$d(z,F_0z)=8+2d(z,\mathcal L)$ follows. Hence the axis is the full
minimal-displacement set. Every commuting polynomial automorphism
preserves it. A reflection of this line would invert a nonzero
translation, so a centralizer element acts by a translation. Its shift
has even edge length because vertex types are preserved.

### 3.3 The turn label is intrinsic, not a chosen-word invariant only

At an $\mathcal E$-vertex represented by $g\mathcal E$, write the two
incident axis edges as $g e_1\mathcal B$, $g e_2\mathcal B$. The label
$\deg(e_1^{-1}e_2)$ is well defined for this unordered pair of edges.
I checked all changes of representatives in proof equation (6):

- Replacing $g$ by $ge$ changes each $e_i$ to $e^{-1}e_i$ and does not
  change the relative product.
- Changing edge representatives gives left and right multiplication of
  $e_1^{-1}e_2$ by triangular affine maps. For a nonlinear elementary
  polynomial this only rescales the leading coefficient and substitutes
  an invertible affine expression into its nonlinear variable; the
  remaining added terms have degree at most one. Degree cannot cancel.
- Exchanging the edges takes an elementary inverse, which has the same
  degree. Left multiplication by any member of $G$ leaves the relative
  pair unchanged.

Distinct edges ensure that the relative element is not in $\mathcal B$,
so its degree is at least two. This proves invariance under **every**
polynomial automorphism acting on the tree, not just normalized Hénon maps.

### 3.4 No hidden shorter translation

The resulting periodic label sequence is $(7,15,15,7)$ repeated.
It has least shift period four: shifts one, two, and three each change an
entry. Consequently a commuting map's translation has length divisible
by eight. Since $F_0$ realizes eight, its native translation generates
the complete translation image.

Thus for every $h\in C_G(F_0)$ there is an integer $j$ for which
$hF_0^{-j}$ fixes the axis pointwise and still centralizes $F_0$.
This conclusion excludes all smaller-step centralizers and all possible
roots/twisted roots with smaller positive translation. No bound on the
degree of $h$ was used. This is the decisive exhaustive step missing from
an affine ansatz or a commuting-subgroup inclusion.

## 4. All axis fixers, translations, and reversor components

The two axis edges $\mathcal B$ and $\tau\mathcal B$ force the remaining
centralizer element into
$\mathcal B\cap\tau\mathcal B\tau^{-1}$, which consists exactly of
diagonal affine maps $(\alpha x+c,\beta y+e)$. Arbitrary translations
are retained at this point; they were not discarded by normalization.

Let $P_i=H_{d_1}\cdots H_{d_i}$ with $(d_1,d_2,d_3,d_4)=(7,15,15,7)$.
Both $P_i\mathcal B$ and $P_i\tau\mathcal B$ lie on the axis,
including the translated pair at $i=4$. Thus every
$h_i=P_i^{-1}h_0P_i$ is diagonal affine. The identity

$$
H_d^{-1}(\alpha x+c,\beta y+e)H_d
=\bigl((\alpha y+c)^d-\beta y^d+\beta x-e,\ \alpha y+c\bigr)
$$

is correct, including both translation signs. Vanishing of its nonlinear
$y^d$ coefficient gives $\beta=\alpha^d$. The next coefficient forces
$c=0$ in characteristic zero. Applying the next factor kills $e$ as
well. The actual degrees are seven and fifteen, so there is no low-degree
or characteristic exception in this example.

Successive conjugations then interchange the two diagonal scalars and
give exactly

$$
\beta=\alpha^7,\quad \alpha=\beta^{15},\quad
\beta=\alpha^{15},\quad \alpha=\beta^7.
$$

The first and third imply $\alpha^8=1$ and $\beta=\alpha^{-1}$.
Conversely these conditions satisfy all four equations, and each
$S_\zeta$ really commutes with the four-factor word: each individual
factor conjugates it to $S_{\zeta^{-1}}$. Hence the full equality is

$$
C_G(F_0)=\{S_\zeta F_0^j:\zeta^8=1,\ j\in\mathbb Z\}
\cong\mu_8\times\mathbb Z.
$$

The finite subgroup intersects the native cyclic subgroup trivially,
since nonzero powers of $F_0$ have nonzero axis translation. The direct
product is established for this word; a universal direct-product theorem
for arbitrary complex Hénon centralizers is not imported.

Finally $\tau H_d\tau=H_d^{-1}$, and the ordered degree word is a
palindrome. Therefore $\tau F_0\tau=F_0^{-1}$. If $R$ is any reversor,
$R\tau$ centralizes $F_0$, giving the complete coset

$$
\operatorname{Rev}_{\mathbb C}(F_0)
=\{S_\zeta F_0^j\tau:\zeta^8=1,\ j\in\mathbb Z\}.
$$

This does not assume that $R$ has finite order. Indeed the resulting
classification implies that the displayed reversors are involutions;
the order conclusion is derived, not imposed on the global search.

## 5. Twist, all eight roots, and original-field descent

For a number field $L$ and $a\in L^*$, embed $L$ into $\mathbb C$ only
for the geometric classification and choose $u^8=a$. With
$A_u=\operatorname{diag}(u,u^{-1})$, direct substitution verifies both
identities in proof equation (14). Alternating the two signs gives

$$
A_u^{-1}F_0A_u
=H_{a,7}H_{a^{-2},15}H_{a^2,15}H_{a^{-1},7}=F_a.
$$

In particular the coefficient order and both degree-fifteen coefficients
are correct. The conjugated swap is
$R_{u^2}$, where $R_t(x,y)=(t^{-1}y,tx)$.
The diagonal symmetries commute with $A_u$, and
$S_\zeta R_{u^2}=R_{\zeta^{-1}u^2}$. As $\zeta$ varies, these parameters
are exactly all eight roots of $t^8=a^2$, not only the roots of $t^4=a$.
This proves the full geometric equality

$$
\operatorname{Rev}_{\mathbb C}(F_a)
=\{F_a^jR_t:j\in\mathbb Z,\ t^8=a^2\}.
$$

If a reversor $R$ is defined over $L$, choose its representation in this
equality. For any sign of $j$, the map $F_a^{-j}$ is a polynomial
automorphism over $L$. Thus $F_a^{-j}R=R_t$ is defined over $L$.
Its second coordinate has coefficient $t$ on $x$, forcing $t\in L$.
This explicitly resolves every integer component, even if the original
reversor has very large degree. A cancellation among coefficients in
$F_a^jR_t$ cannot evade this removal of an $L$-defined native power.

Conversely such a root gives $R_t$. Therefore the number-field equality
in proof equation (18) and the equivalence with $a^2\in L^{\times8}$
are proved without adding an assumption.

The local construction does **not** require an embedding
$K_v\hookrightarrow\mathbb C$. In any characteristic-zero field
containing $a,t$ with $t^8=a^2$, adjoin $u$ temporarily in an algebraic
closure. The same explicit conjugation identities and finite diagonal
symmetries give the reversal identity for $R_t$. Both sides already have
coefficients in the original field, so the identity holds there.
Only this sufficiency, not a whole-group classification over a completion,
is used for the local premise.

## 6. Every original place and the global obstruction

The arithmetic of proof §4 is independently valid and covers all cases:

| Places of $K=\mathbb Q(\sqrt7)$ | Hand-checked root argument |
| --- | --- |
| Every place above an odd rational prime $p$ | At least one of $2,-2,-1$ is a nonzero square modulo $p$. Its root lifts to $\mathbb Q_p$. Roots of $\pm2$ have eighth power $16$; if $i^2=-1$, then $(1+i)^8=16$. Every $K_v$ over $p$ contains $\mathbb Q_p$. |
| The unique place above $2$ | The unit $7$ is not a square in $\mathbb Q_2$, whereas $-7$ is: for $X^2+7$ at $1$, the strong Hensel inequality is $3>2$. Thus $K_v=\mathbb Q_2(\sqrt7)=\mathbb Q_2(i)$ and $1+i$ is a root. |
| Both infinite places | $K$ is real quadratic, so each completion is $\mathbb R$ and contains $\sqrt2$. There are no complex places. |

No prime is excluded by the odd-prime argument: $2,-2,-1$ are nonzero
at every odd prime, including the ramified rational prime seven.
The dyadic field is the completion of the specified $K$, not a new
extension chosen to repair a missing root.

Globally, a real eighth root of $16$ is necessarily $\pm\sqrt2$.
If $(b+c\sqrt7)^2=2$ with $b,c\in\mathbb Q$, then $bc=0$; one would
need a rational square equal to $2$ or $2/7$. Both have odd $2$-adic
valuation. Thus neither root belongs to $K$.

Taking $a=4$ supplies a local involution $R_{t_v}$ over every actual
$K_v$. The exhaustive global criterion excludes every polynomial
reversor over $K$. This is an all-place counterexample, not merely an
almost-everywhere one, and it retains one application of the whole word
as the native clock throughout.

## 7. Failed two-factor control checked independently

For the two-factor analogue, set $X=y^7/4-x$. Its map is
$(X,4X^7-y)=E_2E_1$, with

$$
E_1=(y^7/4-x,y),\qquad E_2=(x,4x^7-y).
$$

Both are involutions defined over $K$, and
$E_1(E_2E_1)E_1=(E_2E_1)^{-1}$. Hence this map has a global
polynomial reversor, regardless of failure of a proposed affine swap.
The report states this control correctly.

Its repeated degree cycle does not impose the four-factor native
translation restriction proved above. This explains the logical role of
the aperiodic cycle and full centralizer computation; it is not enough
to repeat a failed affine equation with different coefficients.

## 8. Primary-source applicability and classical subtraction

The relevant sources were independently accessed through primary PDFs
or the publisher's article text. The following records distinguish
actual passages read from conclusions derived in this review.

- **Gómez–Meiss**, *Reversors and symmetries for polynomial automorphisms
  of the complex plane*, Nonlinearity 17 (2004), 975–1000:
  [author-hosted published PDF](https://amath.colorado.edu/faculty/jdm/papers/Reversors.pdf).
  I read §2.1 and Theorem 3, §2.2 Theorem 4 and its proof, and the
  relevant §3/Theorem 7 statement and surrounding subgroup wording.
  The full-group amalgam/reduced-word input matches the author's use
  over $\mathbb C$. The commuting-subgroup inclusion does not itself
  give the required full centralizer equality. Here that equality is
  independently established by §§1–2 of the author proof. General
  polynomial conjugacy, symmetry, and reversor normal forms are classical.

- **Baake–Roberts**, *Symmetries and reversing symmetries of polynomial
  automorphisms of the plane*, arXiv:math/0501151:
  [primary preprint](https://arxiv.org/pdf/math/0501151).
  I read §2 Facts 1–2, the relevant group definitions, and Proposition 1
  with its proof, and checked Theorem 2 and Corollary 1's field scope.
  The first group of results supplies the claimed amalgam and reduced
  words. The simpler later finite-symmetry/direct-product conclusions
  assume characteristic zero and only $\{\pm1\}$ as roots of unity;
  they cannot be applied over $\mathbb C$. The reviewed proof does not
  do so and directly computes its $\mu_8$ instead.

- **Cantat–Dujardin**, *Holomorphically conjugate polynomial
  automorphisms of $\mathbb C^2$ are polynomially conjugate*,
  Bull. London Math. Soc. 56 (2024), 3745–3751:
  [publisher article](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/blms.13164).
  I read the final example of §2.2 and its explanation, with the adjoining
  centralizer/field-of-definition discussion. The example already uses
  a scalar root and the full centralizer to exclude all alternative
  polynomial conjugacies over the original field. Applying its displayed
  centralizer argument with exponent eight and the Wang class gives an
  analogous all-place failure for two separately chosen maps; this last
  combination is an inference, not an all-place theorem stated there.
  Scalar twisting and exhaustive centralizer descent are therefore old
  mechanisms. The present mathematical distinction is the constrained
  inverse pair $(F,F^{-1})$ and exclusion of its alternative reversors.

- **Song Wang**, *Grunwald–Wang theorem, an effective version*,
  arXiv:1401.0389v1:
  [primary preprint](https://arxiv.org/pdf/1401.0389v1).
  I read §2.1 Proposition 2.1 and the following remark on printed p. 7.
  The remark explicitly identifies $\mathbb Q(\sqrt7)$, exponent eight,
  and the class $16$. Some exceptional-set notation is damaged in the
  PDF text extraction; the direct all-place proof checked in §6 above
  avoids reliance on that transcription. The power obstruction is
  classical and is not credited to the present construction. No false
  universal injectivity statement for the all-place power map is used.

These were targeted applicability/ownership checks, not full audits of
every proof in those papers or an exhaustive novelty search. No claim
about unread Frei et al. passages is inherited from the scout or author.
No configured Zotero/Obsidian tools were available, and the local relevant
PDF/script filename check returned no matching source or arXiv fetch
script in the checked paths; primary browsing supplied the needed texts.
No source PDF was saved into the repository.

## 9. Final findings and execution record

| Item | Final disposition |
| --- | --- |
| Entire polynomial group, intrinsic turn labels, primitive native translation image | Verified; no unproved centralizer equality imported. |
| All pointwise-axis centralizers, including translations | Verified; exactly $\mu_8$. |
| Every polynomial reversor and every integer component | Verified; no degree/order/involution restriction used. |
| Twisted family and exact root equation | Verified; all roots of $t^8=a^2$ retained. |
| Original-number-field descent and original completions | Verified; no completion embedding or enlargement required. |
| Odd, dyadic, and infinite local places; global non-root | Verified individually. |
| Two-factor failed control | Verified as globally reversible, not a counterexample. |
| Mathematical/source-applicability must-fixes | Zero unresolved; no requested author repair. |

The proof and report hashes were checked on the actual files. Their final
identities are the ones in §1; hash agreement establishes which bytes were
reviewed, not their mathematical correctness. The substantive verification
above consists of independent hand deductions and primary-source checks.

No mathematical program, old checker, new agent, external model/API call,
GPU run, Git action, author/shared/frozen-file edit, manuscript/PDF build,
formal evaluation, or admission write was performed by this reviewer.
The prior Fricke reviews were not reopened or rewritten.

The original all-place reversibility implication is negatively resolved by
this example. The one-family criterion belongs to the same mechanism.
No conclusion follows here about general reversor classification for all
words, good-model descent, LG4, SF2/FGT, target Euler factors, root numbers,
automorphy, or a Hilbert–Pólya realization. Whether this classical-mechanism
inverse-pair realization merits an independent paper remains the separate
source/substantiality and coordinator admission question.
