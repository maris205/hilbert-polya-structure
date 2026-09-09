# C3 report: rational Vieta arithmetic requires nonlinear strata

2026-09-09 UTC. **Complete proved obstruction; no new manuscript admitted.**
The frozen positive affine-atlas question is refuted. The substantive
increment is an exact positive-genus native-period locus, its all-prime
denominator law, and an explicit infinite denominator tower—not a new
rank theorem or a relabelled integer channel.

## Frozen question and result

Keep
$$
F_{n,a}(x_1,\ldots,x_n)
=(x_2,\ldots,x_n,x_2\cdots x_n+a-x_1),\quad
n\ge3,\ a\in\mathbb Z,
$$
on all $\mathbb Q^n$, at one native step per application. The
[frozen question](FROZEN_QUESTION.md) asks for a finite affine-linear
atlas of every rational periodic point, independent of the invariant
level, with exact least-period labels. It allows free rational
polyhedral parameters, not just integer generators with an automatically
bounded common denominator.

**Answer: no.** For $(n,a)=(5,-1)$, the entire exact native two-period
locus is
$$
\operatorname{Per}_2(F_{5,-1},\mathbb Q)
=\{(u,v,u,v,u):u^2v^2-u-v-1=0\}.
$$
There are infinitely many rational points, but the plane curve contains
no affine line. Hence every rational affine-polyhedral chart contained
in this exact-period locus is a singleton. No finite exact-period-labelled
affine atlas can cover it. More strongly, its elliptic completion admits
no nonconstant rational map from any affine space, ruling out finitely
many rational-function charts in free rational parameters as well.
Full details, including every valuation and exceptional point, are in
[PROOF_PACKAGE.md](PROOF_PACKAGE.md), Steps 1–7.

The explicit zero-free pair $(21,-2/9)$ has native least period two and
maximum coordinate $21>|a|+4=5$. Thus the integer nonzero-block bound
does not merely lack a rational proof: its literal extension is false.

## The reusable arithmetic interface

For every odd dimension $n=2m+1$, two-period words are exactly alternating
pairs satisfying
$$
u+v=(uv)^m+a,
$$
with $u\ne v$ for least period two. For nonzero $u,v$ and any prime
$p$ at which a denominator occurs, the valuations are exactly
$$
\{v_p(u),v_p(v)\}=\{-me,(m-1)e\},\qquad e\in\mathbb Z_{>0}.
$$
In particular denominators in the two coordinates have disjoint prime
supports and are perfect $m$th powers. Equivalently,
$$
u=\frac{D^{m-1}r}{B^m},\quad
v=\frac{B^{m-1}t}{D^m},\quad
(B,D)=1,\quad (rt,BD)=1,
$$
where $B,D>0$, $r,t\ne0$ are integers, and the exact residual equation is
$$
rD^{2m-1}+tB^{2m-1}=(rt)^m+a(BD)^m.
$$
Necessity and sufficiency are proved in Step 2. This is a usable
denominator-stratum constraint, not a claim of finitely many strata.

At $n=5$ the map $X=u,Y=u^2v$ identifies the plane curve with
$$
E_a:\quad Y^2-Y=X^3-aX^2
$$
minus $O$ and $(0,1)$; $u=0$ is handled by the regular inverse
$v=(X-a)/(Y-1)$. This is nonsingular for every integer $a$.
For $a=-1$, the seed $Q_0=(-3/4,-1/8)$ and classical tangent doubling
give
$$
X(2Q)=\frac{X^4-2X-1}{4X^3+4X^2+1}.
$$
If $v_2(X)=-2e$, the numerator and denominator have unique least
valuations $-8e$ and $2-6e$. Thus doubling raises $e$ by one, producing
zero-free native two-cycles with
$$
v_2(u_k)=-2(k+1),\qquad v_2(v_k)=k+1.
$$
The index $k$ labels different two-cycles; elliptic doubling is not
the native return map or a replacement clock.
This proves infinitude without a computation or a rank oracle. It also
proves that **no fixed rational affine coordinate change sends all
rational periodic points of this one map into $\mathbb Z_2^5$ or
$\mathbb Z^5$**: the inverse image of such a lattice has bounded
coordinate valuations, whereas this family does not.

The same reduction gives the polynomially isomorphic model
$$
w^2=(s^m+a)^2-4s,\qquad s=uv,\quad w=u-v.
$$
For integer $a$ and $m\ge2$, its polynomial is squarefree and its smooth
completion has genus $m-1$. A repeated root would force
$m^{2m}a^{2m-1}=(2m-1)^{2m-1}$, contradicted by any prime divisor of
$m$. Thus the arithmetic complexity already reaches genus one at
$n=5$ and genus at least two at all odd $n\ge7$; complete rational-point
sets on the latter curves are not computed or claimed.

## The invariant-level quantifier is preserved

On an odd-dimensional alternating pair, the original invariant is
$$
K=m s^{2m}+ma s^m-(2m+1)s,\qquad s=uv.
$$
For the explicit $n=5,a=-1$ tower,
$v_2(K)=1-4(k+1)$, so its levels are pairwise different. On each *fixed*
rational level the two-period stratum has at most eight states, because
$K=2s^4-2s^2-5s$ determines at most four values of $s$ and each determines
at most two ordered pairs. This finite-level fact plainly does not
exhaust the infinite levels or denominator strata. No all-period
finite-level finiteness claim is made.

## Actual source subtraction and transfer checks

| Source read | Exact ownership / compatibility conclusion |
| --- | --- |
| [C427 actual statement](../../../research_c424_c428/papers/C427_vieta_semilinear/sections/01_statement.tex), [nonzero blocks](../../../research_c424_c428/papers/C427_vieta_semilinear/sections/02_blocks.tex), [classical input](../../../research_c424_c428/papers/C427_vieta_semilinear/sections/03_classical.tex), [mixed-zero atlas](../../../research_c424_c428/papers/C427_vieta_semilinear/sections/04_atlas.tex), [completion](../../../research_c424_c428/papers/C427_vieta_semilinear/sections/05_completion.tex) | The complete integer atlas remains proved and is imported, not reopened. Its nonlinear reduction needs nonzero integer factors of magnitude at least one and an integer product of magnitude below two to be a sign. Both fail rationally. Its uniform period lemma applies to integral points, not arbitrary denominator strata. |
| [C421 actual theorem](../../../research_c419_c423/papers/C421_integral_return/sections/02_classification.tex) and [full cycle table](../../../research_c419_c423/papers/C421_integral_return/figures/TABLE_classification.tex) | Its complete $n=3$ integral classification and computational dependency remain inherited. The period-two hyperbola already gives an elementary rational nonaffinity obstruction. That easy observation is subtracted. The $n=5$ positive-genus obstruction cannot be rationally parameterized as that hyperbola can. |
| [C424 normalization](../../../research_c424_c428/papers/C424_integer_valued_quadratic/sections/2_normalization.tex) and [integrality proof](../../../research_c424_c428/papers/C424_integer_valued_quadratic/sections/3_integrality.tex) | A two-dimensional integer-valued quadratic Hénon family has a one-variable uniquely dominant square at a maximal denominator. Here products of different coordinates admit the signed valuation balance above. The hypotheses do not match; the explicit tower disproves a one-time affine-integral normalization for this Vieta map. |
| [C426 statement](../../../research_c424_c428/papers/C426_affine_good_models/sections/02_classification.tex) and [all-affine rigidity proof](../../../research_c424_c428/papers/C426_affine_good_models/sections/03_local_rigidity.tex) | Its object is a single two-dimensional generalized Hénon factor and degree-preserving good models with separated projective indeterminacy. Its top forms are powers of two independent linear forms. The five-dimensional Vieta product does not satisfy that input interface; integral map/inverse coefficients alone do not justify its unique square-disc conclusion. |

Paths in this table refer to read-only earlier packages. The new proof is
not merely the $n=3$ integer equation with rational parameters substituted.
Its strongest source-subtracted content is the odd-dimensional denominator
law, the positive-genus native-period geometry, and their concrete
normalization/atlas consequences. Admission should assess this integrated
content, not count its corollaries as separate papers.

## Bounded primary-source check

Local-first searches covered the relevant C421/C424/C426/C427 sources and
matching Vieta/denominator/elliptic phrases across Hénon Markdown/LaTeX
sources, excluding duplicate build snapshots. Targeted web searches used
Markoff–Hurwitz/Vieta with rational periodic points and elliptic curves,
plus the exact curve equation. No matching native five-dimensional
period-two obstruction was found in that bounded search; this is not a
worldwide novelty certificate.

- [Whang, *On periodic orbits of polynomial maps*, arXiv:2305.13529v3](https://arxiv.org/html/2305.13529v3): actual Theorems 1.1, 1.2, 1.4 and the §2.3 proof were checked. General individual-point periodicity decidability is classical and is not refuted or claimed anew here. Its finitely presented base ring may depend on the input point; no all-denominator affine atlas follows.
- [Hu–Tan–Zhang, *Polynomial automorphisms of $\mathbb C^n$ preserving the Markoff–Hurwitz polynomial*, arXiv:1501.06955v2](https://arxiv.org/html/1501.06955v2): abstract, polynomial, and introductory full-group definitions checked. Its unforced full-group action is not the forced single native return considered here; no whole-paper proof audit is claimed.
- [LMFDB curve 43.a1](https://www.lmfdb.org/EllipticCurve/Q/43/a/1) and [data provenance](https://www.lmfdb.org/EllipticCurve/Q/Source): the curve after $y=-Y$ is already recorded as $y^2+y=X^3+X^2$, with rank one and generator $(0,0)$. Those are established external arithmetic data, not this lane's discoveries. The proof does not depend on the tabulated rank, generator, conductor, or modular interpretation.
- [Stacks Project, Riemann–Hurwitz](https://stacks.math.columbia.edu/tag/0C1B): the characteristic-zero formula supports the classical genus and no-rational-map step. No new theorem of curve geometry is claimed.

One search-result snippet attached arXiv ID `1207.2091` to a purported
bielliptic-modular-curves paper; direct opening showed an unrelated
nonlinear-lattice paper. That identifier/source pairing was rejected and
is not used. No retraction/venue/author-conflict audit was performed;
source existence and scope checks are not journal acceptance or human
review. ARS verification guidance was used only for this bounded check.

## Disposition and missing work

**Frozen positive claim: REFUTED. Counterexample/proof: complete at
author-check level.** No missing lemma remains for the stated obstruction.
Independent internal proof/source/substantiality review is still required
before any manuscript admission. A complete nonlinear atlas of all
rational periods, rank computation uniformly in $a$, and complete
higher-genus rational-point determination remain outside what was proved.
Classical pointwise periodicity decidability must not be presented as that
missing all-point atlas.

The proof-writing skill required an exact negative theorem rather than
reusing the integral maximum argument; research-lit/ARS source discipline
identified the classical elliptic-curve ownership and the $n=3$ subtraction.
AI-assisted reasoning and source inspection were used. Mathematical runs:
**zero**. No old certificate, PDF build, shared file, Git operation,
formal evaluation, configuration edit, or external-model upload occurred.
No target Euler factor/root number/automorphy/zero correspondence or
Hilbert–Pólya claim is made; Route B remains closed.
