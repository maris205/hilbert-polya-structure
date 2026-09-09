# R5 X2 second arithmetic scout — all-place polynomial reversibility

2026-09-09 UTC. Source/scout report only. This is not the C4 author proof,
an independent mathematical review, an admission, or a paper-count decision.
Only this file is written; the first R5 scout and earlier rounds are frozen.

## 1. Decision and current gate

Select **B, the original-field Hasse question for polynomial reversibility**,
as the sole full-question candidate for the coordinator's author/review gate.
The promising outcome is a negative answer by the four-factor construction
in §4, not a positive descent theorem. Reject formulation A for independent
paper substantiality: its cheap construction is a classical intersective
polynomial mechanism with an elementary real-orbit exclusion.

This recommendation changed during the bounded discriminator. Initially B
had an unresolved centralizer/component descent gap and no complete route.
Checking the supposed Kummer shortcut exposed the classical Wang exception,
and then a possible realization of that exception by an aperiodic Hénon word.
The coordinator has assigned C4 the full author attempt. The all-polynomial
exclusion below is an explicit outstanding obligation, not a theorem certified
by this scout. No completed or admitted contract is claimed here.

The substantive question is different from good-model patching, periodic
point existence, and congruence orbit separation: does a reversing symmetry
exist over the prescribed number field when one exists over every completion?
A complete negative answer would close that question without changing its
quantifiers. Nevertheless, the proposed example combines old normal forms
and old Wang arithmetic. A successful proof still requires an independent
judgment that this realization merits a separate source paper rather than
an auxiliary observation. Absence of a retrieved exact collision is not
that judgment.

## 2. The two formulations and internal subtraction

Only the following two subtype formulations were considered in this second
scout. The failed two-factor trial in §4 is a test within B, not a third
candidate.

| Formulation | Complete question | Scout disposition |
|---|---|---|
| A: local periodic existence | Can an everywhere regular-good integral Hénon map have a fixed point over every completion of $\mathbb Q$, integral at every finite place, but no rational point of any native period? | Short construction available; reject independent-paper substantiality. |
| B: arithmetic reversibility | For every number field and every nonempty finite Hénon word, does polynomial reversibility over every completion imply polynomial reversibility over the original field? | Sole selected full-question lead; explicit Wang-twisted counterexample proposed; all-polynomial proof and independent review pending. |

The internal comparison included the original LG4 interface and the B1
congruence-separation record, especially its virtual-centralizer theorem and
reverser falsifier:
[B1 report](../../lanes/b1_congruence_separation/REPORT.md).
That record already uses finite-by-cyclic centralizer structure. Its unsolved
problem asks whether two given integral points lying in the same orbit modulo
every modulus lie in the same integer-time orbit. It assumes an integral
reversor when testing one possible method; it does not solve field descent
of reversors. Neither A nor B repairs its missing all-modulus orbit-incidence
condition. Original LG4 remains unchanged and unclosed by this scout.

The C425 comparison was checked in its introduction and the earlier
[Fricke source audit](../../../research_c424_c428/continuation_round3/nonlinear_geometry/SOURCE_AUDIT.md).
It already credits residual periodicity on Markoff surfaces to Vishkautsan.
Thus neither residual periodicity nor the use of reversing symmetries is
presented as a newly discovered research theme.

The first R5 affine-good-model scout is a separate record, not an input that
establishes B. No GR5 extension, ideal square/product obstruction, finite-jet
control, local optimal-cycle tower, or measure statement is relabelled here.

## 3. Frozen full question B

Let $K$ range over all number fields and $\Omega_K$ over all of their places,
including every real, complex, and finite place. For every integer $r\ge1$,
every $f_i\in K[Y]$ of degree $d_i\ge2$, and every $a_i\in K^\times$, set

$$
H_i(x,y)=(y,f_i(y)-a_i x),\qquad
F=H_r\circ\cdots\circ H_1\in\operatorname{Aut}_K(\mathbb A^2).
$$

The question is whether the following implication holds for every such datum:

$$
\left[
\forall v\in\Omega_K\ \exists R_v\in
\operatorname{Aut}_{K_v}(\mathbb A^2):
R_v F R_v^{-1}=F^{-1}
\right]
\quad\Longrightarrow\quad
\left[
\exists R\in\operatorname{Aut}_K(\mathbb A^2):
R F R^{-1}=F^{-1}
\right].                                                    \tag{B}
$$

Here an automorphism means a polynomial map with a polynomial inverse.
There is no imposed degree bound, order bound, affine restriction, involution
restriction, common local formula, or common field of definition for the
different $R_v$. No place may be omitted. No extension of $K$ may replace
the demanded global reversor. Existence merely over algebraic closures,
finite residue fields, or almost all completions is insufficient.

The native clock is one application of the entire ordered word $F$.
The number $D=\prod_i d_i$ is its degree, not a substituted clock. Passing
to $F^m$ cannot replace (B). Cyclic reordering may be a labelled conjugacy
device, not an unannounced change of the dynamical object.

The observable is the existence of a polynomial reversor. The only
determinant used is the ordinary constant Jacobian determinant
$J(F)=\prod_i a_i$. The premise forces $J(F)^2=1$, since conjugacy preserves
this determinant and $J(F^{-1})=J(F)^{-1}$. This necessary condition does not
itself imply reversibility. There is no Fredholm determinant, target Euler
factor, root number, automorphy, or Hilbert–Pólya assertion.

Success is either a full proof of (B), or one explicit $K,F$ satisfying every
local clause together with a proof excluding **every** polynomial reversor
over $K$. A negative example need not classify all words, because it would
settle the universal implication negatively. Failure to find a reversor in
one affine ansatz, one bounded degree, or one source normal form is not success.

## 4. Cheap discriminator: the Wang-twisted four-factor lead

### 4.1 Proposed construction and verified arithmetic input

Write $H_{c,d}(x,y)=(y,c y^d-x)$. The specific proposed counterexample is

$$
K=\mathbb Q(\sqrt7),\qquad
F=H_{4,7}\circ H_{1/16,15}\circ H_{16,15}\circ H_{1/4,7}.      \tag{1}
$$

The coefficients of $F$ are already rational, but the base field for (B)
is exactly $K$. The word has four nonlinear factors and Jacobian one.
Its degree is $7\cdot15\cdot15\cdot7$; no expansion of this large
coordinate polynomial and no mathematical program is needed or performed.
There is no claim that (1) has an everywhere-good integral model: that is
not a hypothesis of B and is not this subtype's question.

The arithmetic fact is classical:

$$
16\in K_v^{\times8}\text{ for every }v\in\Omega_K,
\qquad 16\notin K^{\times8}.                                \tag{2}
$$

It is explicitly recorded in the primary sources listed in §6. A direct
check is also short. Over an odd $p$, at least one of $2,-2,-1$ is a square
modulo $p$, because the corresponding quadratic characters multiply as
$\chi(-2)=\chi(-1)\chi(2)$. Hensel lifting and

$$
X^8-16=(X^2-2)(X^2+2)(X^2-2X+2)(X^2+2X+2)
$$

give a root in $\mathbb Q_p$, hence in every $K_v$ over $p$.
The dyadic completion satisfies
$\mathbb Q_2(\sqrt7)=\mathbb Q_2(i)$: the quotient $-7$ is a square in
$\mathbb Q_2$ since $-7\equiv1\pmod8$. In it, $(1+i)^8=16$.
The real completions contain $\sqrt2$. Globally $K$ is real and its only
possible real eighth roots of $16$ are $\pm\sqrt2$, neither in
$\mathbb Q(\sqrt7)$. This checks every place and the global non-root.

This also refutes the shortcut that
$K^\times/K^{\times m}\to\prod_v K_v^\times/K_v^{\times m}$ is always
injective for arbitrary number fields and arbitrary $m$. The earlier
tentative shortcut was abandoned; (2), not injectivity, is the proposed
arithmetic mechanism.

### 4.2 Proposed dynamical realization, not an author-proof replacement

Choose $u\in\overline K$ and let

$$
F_0=H_{1,7}\circ H_{1,15}\circ H_{1,15}\circ H_{1,7},\qquad
u^8=4,\qquad A=\operatorname{diag}(u,u^{-1}).
$$

Alternating $A$ and $A^{-1}$ through the four factors gives
$F=A^{-1}F_0A$. The coordinate swap reverses $F_0$ because its ordered
factor sequence is a palindrome. The proposed local reversors of (1) are

$$
R_t(x,y)=(t^{-1}y,tx),\qquad t^8=16.                       \tag{3}
$$

The pure-diagonal symmetry calculation for $F_0$ gives
$S_\zeta=\operatorname{diag}(\zeta,\zeta^{-1})$ with $\zeta^8=1$:
the simultaneous degree-seven and degree-fifteen intertwining equations
force precisely these scalars. This calculation is not yet an exclusion
of nonlinear centralizers.

The decisive proposed bridge is

$$
C_{\operatorname{Aut}_{\overline K}(\mathbb A^2)}(F_0)
=\{S_\zeta F_0^n:\ \zeta^8=1,\ n\in\mathbb Z\}.            \tag{4}
$$

The polydegree cycle $(7,15,15,7)$ has no nonzero rotational period smaller
than four. The intended use of the actual normal-form conjugacy theorem
is to exclude a centralizing proper word-prefix, then remove affine
translations and determine the remaining diagonal group. The C4 author
must establish this exhaustively, including all polynomial conjugators.
The fact that a commuting subgroup exists does not establish (4).

If (4) is established, any polynomial reversor differs from the conjugated
swap by a member of this centralizer. Removing a native power of the
$K$-defined $F$ should then force a parameter $t\in K$ satisfying (3).
Combined with (2), that would exclude every global polynomial reversor,
not just the displayed affine ones. This implication is the precise
pending author/reviewer obligation.

For organizing that proof, the scout also supplied the single-family
interface, for any number field $K$ and any $b\in K^\times$,

$$
F_b=H_{b,7}\circ H_{b^{-2},15}\circ H_{b^2,15}\circ H_{b^{-1},7},
\qquad
F_b\text{ polynomially reversible over }K
\ \Longleftrightarrow\ b^2\in K^{\times8}.                 \tag{5}
$$

Equation (5) is a **proposed** strengthening of the same mechanism, not
a proved classification, extra candidate, or replacement of full question B.
The intended counterexample uses $b=4$.

### 4.3 Decisive failed control and the component issue

The two-factor analogue is not a counterexample. Writing
$X=y^7/4-x$, it is $(X,4X^7-y)$, the product of the two $K$-defined
involutions

$$
E_1(x,y)=(y^7/4-x,y),\qquad E_2(x,y)=(x,4x^7-y).
$$

Thus it already has a global polynomial reversor. Failure of the affine
swap ansatz would miss that elementary reversor. This cheap failure is
why the four-factor aperiodic word, and the full centralizer claim, are
essential rather than cosmetic coefficient choices.

For a general positive approach, even identifying a finite kernel with
$\mu_m$ would leave a component problem. Conditionally, if the geometric
centralizer has a suitable extension by $\mathbb Z$, choosing a geometric
generator can produce a boundary class $a$; a reversor component gives
a class $b$. Local triviality can then express
$b_v\in\langle a_v\rangle$ with different exponents at different places,
not $b_v=0$ in a single chosen component. This is a schematic obstruction
analysis, not a proved classification for all words. In addition, (2)
shows that even the single-component power kernel can be nonzero.

## 5. Rejected formulation A: exact hand check and novelty subtraction

Set

$$
g(Y)=(Y^3+Y+1)(Y^2+31),\quad f(Y)=2Y+g(Y),\quad
T(x,y)=(y,f(y)-x).
$$

Then $T$ and $T^{-1}(x,y)=(f(x)-y,x)$ have integral coefficients and
Jacobian one. The monic degree-five leading terms remain nonzero at every
prime; the forward and inverse indeterminacy points are the two distinct
coordinate points at infinity. Thus this is regular good reduction at
every finite prime in these coordinates.

The cubic $Y^3+Y+1$ is irreducible over $\mathbb Q$ by the rational-root
test and has discriminant $-31$. At odd unramified primes, its $S_3$
Frobenius either fixes a cubic root or is a three-cycle, in which case
the quadratic discriminant field splits. This gives a simple root of
one factor and hence a root of $g$ in $\mathbb Z_p$. At $31$, the cubic
has the simple root $3$ modulo $31$, with derivative $28$. At $2$,
$-31\equiv1\pmod8$ is a $2$-adic square. Therefore $T$ has a fixed point
$(z,z)\in\mathbb Z_p^2$ for every $p$.

Also

$$
g'(Y)=5Y^4+96Y^2+2Y+31
     =5Y^4+96(Y+1/96)^2+2975/96>0.
$$

So $g$ has one real root $\theta$, the irrational real root of its cubic
factor. For any real periodic coordinate cycle, the recurrence is
$f(z_j)=z_{j-1}+z_{j+1}$. At its maximum $M$, $g(M)\le0$; at its minimum
$m$, $g(m)\ge0$. Strict monotonicity implies
$M\le\theta\le m$, so every entry equals $\theta$. There are no rational
periodic points of any positive native period, while the real fixed point
and all finite-place fixed points exist.

Status of this displayed construction: hand-proved feasibility, no program,
not independently reviewed. It is **not recommended as a separate paper**.
The arithmetic factor-cover mechanism is classical, and the global orbit
exclusion is a short maximum/minimum argument. In particular, Vishkautsan's
primary §1.2 already records an affine-line polynomial with no rational
periodic points and fixed points modulo every prime, citing earlier work.
The Hénon realization and the stronger completion/integrality clauses do
not by themselves establish a substantial independent increment.

## 6. Primary-source comparison and actual access

The following are source boundaries, not worldwide novelty certificates.
Statements attributed to sources were read in the indicated passages;
search-result snippets alone were not used to certify a theorem.

1. **Gómez–Meiss, 2004.**
   [Author-hosted published PDF](https://amath.colorado.edu/faculty/jdm/papers/Reversors.pdf),
   *Reversors and symmetries for polynomial automorphisms of the complex
   plane*, Nonlinearity 17, 975–1000. Read §2.1 Theorem 3, §2.2 Theorem 4
   and its proof, §2.3 normalization, §3 Theorem 7/Proposition 8/Corollary 9
   with proofs, and §4 Lemma 10/Theorem 11 with proofs. Polynomial
   conjugacy, finite diagonal symmetries, and finite-order reversors are
   prior inputs. Theorem 1 states inclusion of a commuting subgroup;
   it must not be quoted as equality with the full centralizer. The
   complex normalizations do not automatically descend to $K$.

2. **Lamy, 2001.**
   [Original article](https://www.math.univ-toulouse.fr/~slamy/stock/lamy_algebra.pdf),
   *L'alternative de Tits pour Aut[$\mathbb C^2$]*, Journal of Algebra 239,
   413–437. Read the introductory dynamical-degree convention and all of
   Lemma 4.7/Proposition 4.8 with adjoining Remark 4.9. This supplies
   finite-cyclic-by-infinite-cyclic geometric centralizers, not a universal
   direct product or an arithmetic local-global theorem. The source is
   already deducted in the internal B1 report.

3. **Baake–Roberts.**
   [arXiv:math/0501151](https://arxiv.org/pdf/math/0501151), Proposition 6
   and Theorem 4 with proofs, and the field assumptions of Theorem 2 and
   Corollary 1 were read. The finite-even-order statement applies in
   characteristic zero. The especially simple symmetry-group conclusion
   assumes the only roots of unity are $\pm1$; that hypothesis cannot be
   applied to $\overline K$ or arbitrary completions. The related
   [*Reversing symmetry groups*](https://web.maths.unsw.edu.au/~jagr/BR06.pdf)
   was checked at Proposition 2, Theorem 2 and Example 5; these are
   conditional group-structure inputs, not a proof of (B).

4. **Roberts–Vivaldi, 2005.**
   [Primary PDF](https://web.maths.unsw.edu.au/~jagr/RV05p.pdf), §2.2 and
   Theorem 1 with the preceding construction were read. The map and a
   reflection-type involutory reversor are already defined over a number
   field; the result gives positive-density finite-field reductions with
   prescribed cycle consequences. This is neither arbitrary-polynomial
   reversibility at every completion nor a converse descent theorem.

5. **Cantat–Dujardin, 2024.**
   [Published article](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/blms.13164),
   *Holomorphically conjugate polynomial automorphisms of $\mathbb C^2$
   are polynomially conjugate*. The final example of §2 and its explanation
   were read. It gives Hénon maps conjugate after adjoining a scalar root
   but not over $\mathbb Q$. Thus field-of-conjugacy obstructions are
   already explicit prior work. It does not state the all-place reversal
   counterexample or remove the alternate-reversor obligation in §4.

6. **Wang arithmetic.**
   [Song Wang, arXiv:1401.0389v1](https://arxiv.org/pdf/1401.0389),
   §2.1 Proposition 2.1, the following special-case remark, and Theorems
   2.2–2.3 were read. The exact all-place example is also explicitly in
   [*Distribution of genus numbers of abelian number fields*, Example 3.9](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.12737),
   whose full example was read. These own (2); it is not new arithmetic.
   Direct attempts to access the original Shianghaw Wang 1948/1950 JSTOR
   articles did not yield readable proofs. The failed KCL PDF was not
   counted as access; the publisher's Example 3.9 was accessible.

7. **Intersective and residual-periodicity antecedents.**
   [Bubboloni–Sonn, arXiv:1507.08593](https://arxiv.org/pdf/1507.08593),
   introduction/Proposition 1.1 and the $S_3$ covering passage were read.
   They record the decomposition-group covering mechanism behind
   intersective products. [Vishkautsan, arXiv:1504.07099v2](https://arxiv.org/pdf/1504.07099),
   abstract and §§1.1–1.2 were read, including the earlier affine-line
   example just described. No unread later classification proof is used.

8. **A discarded arithmetic shortcut.**
   [Kowalski, *Some local-global applications of Kummer theory*](https://people.math.ethz.ch/~kowalski/kummer.pdf),
   introduction, the local-generation definition and Theorem 3.3 statement
   were checked. Membership in the subgroup generated by a fixed element
   after reduction is a different condition from the proposed component
   quotient or fixed eighth-power kernel. Its theorem was not imported to
   justify B; the scout does not claim to have read its full proof.

## 7. Bounded search ledger and retrieval limits

The actual queries included at least three formulations of each core
question. Representative literal query groups are recorded below; these
are queries actually issued, not searches inferred from paper titles.

**A / periodic existence:**

```text
Hénon maps strongly residually periodic intersective polynomial
polynomial automorphism no rational periodic points local fixed points Hasse principle
"Hénon" "strongly residually periodic"
"intersective" "Hénon"
"intersective" "x^3+x+1"
"Hénon" "local fixed points" "rational periodic"
"intersective polynomial" "periodic points" Henon site:arxiv.org
```

The last query was issued with a 184-day recency filter. A separate query
included `"Hénon" "intersective" 2024 2025 2026`.

**B / original-field reversibility and geometric obstruction:**

```text
"polynomial automorphisms" "reversibility" "number field"
"Hénon" "reversor" "Galois"
"polynomial automorphism" "reversibility" "local-global"
"reversor" "number field"
"Hénon" "centralizer" "Galois descent"
"Hénon" "centralizer" "cyclic" "finite"
"Lamy" "centralisateur" "automorphismes"
```

**B / Wang realization and competing descent mechanisms:**

```text
Wang counterexample Henon reversible locally all places
"Hénon" "Grunwald"
"Grunwald" "polynomial automorphisms"
"reversors" "Hasse"
"Hénon" "Kummer" "reversibility"
"polynomial reversibility" "Kummer"
```

The arithmetic locator queries included `"Grunwald" "sqrt{7}" "16"`,
`"16" "eighth power" "every completion"`, and
`Shianghaw Wang On Grunwald theorem 1950 pdf`. Encyclopedic/search summaries
were locators; the source claims in §6 rely on accessed primary articles
and the independent elementary check in §4.1.

**Recent/discoverability controls:**

```text
"Hénon" "reversibility" "local-global" site:arxiv.org
"polynomial automorphisms" "Galois descent" reversor after:2026-03-09 before:2026-09-10
"Hénon" "reversor" "local" site:arxiv.org after:2026-03-09 before:2026-09-10
"polynomial automorphism" "Wang" "Hasse" 2024 2025 2026
"Hénon" "reversibility" "number field" site:scholar.google.com OR site:semanticscholar.org
```

The first recent query also used a 184-day filter. These controls did not
retrieve an applicable exact theorem or exact four-factor Hasse-reversal
example. This is a bounded retrieval result only. Scholar/Semantic Scholar
were web-indexed discoverability queries, not an exhaustive database export;
no claim is made that every recent arXiv submission was searched. Unrelated
results, claimed Jacobian-conjecture examples, and time-series notions of
reversibility were not used as mathematical evidence.

## 8. Substantiality, handoff, and stopping rule

The potential increment in B is the realization of an everywhere-locally
soluble but globally empty reversor torsor **after all polynomial reversing
symmetries have been exhausted**, yielding a full negative answer to (B).
It is not the existence of a scalar root obstruction, Wang's exceptional
class, the centralizer normal form, or an affine reversor computation in
isolation. The failed two-factor control demonstrates the distinction.

This is a plausible intrinsic arithmetic source question under workflow §2,
with a concrete cheap route to a complete answer and a different mechanism
from the admitted local-inertia/quotient/measure work. It carries no target
Euler/root-number bridge. Whether the synthesis is important and substantial
enough for an independent paper remains a separate gate. If the complete
result amounts only to an immediate classical corollary at that gate,
retain it as auxiliary; do not enlarge its title or count it automatically.

C4 received the exact construction, failed two-factor control, proposed
uniform interface (5), and primary theorem locators directly. The coordinator
independently checked the elementary arithmetic and alternating-scale
identity but has not thereby certified (4). The present scout does not
duplicate C4's full proof, and messages are not substitutes for reading the
completed author artifact. An independent nonauthor review must verify
the full centralizer exclusion and every-place/no-global conclusion.

The local skills used were the Route-A batch workflow, idea-creator,
novelty-check, and proof-writer feasibility checklist. They caused explicit
source subtraction, rejection of A despite a working formula, preservation
of the unrestricted B quantifiers, and withholding of a proof/admission
label while (4) is pending. Defaults requiring external models or experiment
pilots were not executed under the coordinator's bounded source-only scope.

Resource record: no new, nested, or reused child agent in this second scout;
no mathematical execution or new program; no external-model API or upload;
no Git, shared-state, configuration, manuscript, evaluator, or PDF-output
write. Read-only source downloads were streamed to text extraction without
creating source PDF files. Only this report was created. C4's independent
assignment was made by the coordinator, not by this scout.

Final status: **B selected for full author/review; A rejected for independent
paper substantiality; zero newly certified complete or admitted contracts.**
