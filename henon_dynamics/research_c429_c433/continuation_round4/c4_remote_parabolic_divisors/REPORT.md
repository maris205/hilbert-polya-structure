# R4 C4: genuine higher-period branch divisors along the smooth fold

2026-09-09. Exclusive new lane. R3 is frozen; its partial claims passed
E5's final independent internal review with no unresolved must-fixes.
No mathematical execution is allocated in R4.

## 1. Frozen exact question

Keep the universal Fricke surface
$$
x^2+y^2+z^2-xyz-Ax-By-Cz=D
$$
over $B=\mathbb A^4_{\overline{\mathbb Q}}$, with native ordered map
$T=s_zs_ys_x$ (rightmost first). Let $P_n$ be the ordinary geometric
generic set of exact least native period $n$, and $L_n$ its splitting
field. Let $\mathscr F$ be the irreducible smooth-fold divisor from
the accepted cycle map
$$
\Phi(q,X,Y,Z)=(X-qYZ,Y-qXZ,Z-qXY,
q(XYZ-X^2-Y^2-Z^2)),
$$
whose critical hypersurface contains
$(q,X,Y,Z)=(2/3,3/2,3/2,3/2)$ over
$b_f=(0,0,0,-9/4)$.

**Unchanged SF2:** for every $n\ge3$, the normalization of $B$ in
$L_n$ is unramified at $\eta_{\mathscr F}$. Success must address all
ordinary higher-period point fields and their normal closures, not
just raw scheme lengths or the colliding two-cycles. An actual
$n\ge3$ whose normalized splitting cover ramifies along this same
divisor is a decisive counterexample. Failure of a candidate proof
mechanism is not such a counterexample.

## 2. Accepted reduction and proposed new mechanism

R3 proves that each $\operatorname{Fix}(T^n)$ is finite flat over
$B^{\rm sm}$ and that every period-two germ over
$\eta_{\mathscr F}$ is isolated from higher native layers. Over the
strict henselian DVR at that generic point, remove the open-and-closed
period-two part for even $n$, and remove nothing for odd $n$. The
remaining finite flat algebra is $\mathcal Z_n$; all its special points
have least native period at least three. SF2 is equivalent to étaleness
of the normalization of every such residual generic point algebra.
Those facts are read-only inputs, not an R4 increment.

**Status at freeze: NOT CURRENTLY JUSTIFIED.** The proposed new route
is a genuine noncontainment mechanism: either a parameter-transversality
theorem excluding persistent higher-period resonances on the marked
two-cycle fold, or an explicit point/family on the same divisor with
all genuine higher-period returns nonresonant. The latter may use a
different witness for each $n$, provided the quantifier is proved
uniformly and all sheets at that witness are controlled. Mere expected
codimension, unrestricted genericity, finite-period testing, or real
hyperbolicity outside the fold is insufficient.

The proof-writer and research-lit skills are in use. Primary sources
will be checked with their exact parameter and dynamical hypotheses.
The local-first library check found no relevant named local PDF or
configured Zotero/Obsidian tool; the arXiv-fetch script is absent, so
primary web/arXiv retrieval is the fallback. D2 owns the complementary
slice-character arithmetic; the coordinator owns admission/review,
shared records and Git.

## 3. Author-complete result

The [new proof package](PROOF_PACKAGE.md) keeps SF2
**NOT CURRENTLY JUSTIFIED** and provides two concrete local outputs.

First, the explicit candidate witness curve is generically in the
**cusp locus**, not the simple-fold locus, of the cycle map. For
$A=B=0,D=-C$, at $(q,X,Y,Z)=(1/C,0,0,C)$, put
$s=(X+Y)/2$, $a=(A+B)/2$ and $t=D+C$. After solving the other
coordinates,
$$
a=\frac{t}{C}s-\frac{C-3}{C^2}s^3+O(ts^3,s^5).
$$
For $C\notin\{0,3,4,-4/3\}$ the surface is smooth and this local
map has a versal cubic cusp. The three colliding cycle labels restrict
to an analytic axis label plus a square-root pair on $a=0$; the
three-label central collision is not an inertia 3-cycle. The sign
change $C\mapsto-C$ gives the $D=C$ statement. This strengthens the
already known three-label inventory with an exact local unfolding,
but gives no all-higher-period hyperbolicity witness (§1).

Second, a proposed parameter-transversality proof now has explicit
quantities to establish. On the generic marked two-cycle fold,
$$
\nu_f=dD-q(g-2v)^tJ^{-1}d(A,B,C),
$$
where $v=(X,Y,Z)^t$, $g=(YZ,XZ,XY)^t$, and $J$ is the derivative of
$(A,B,C)$ with respect to $(X,Y,Z)$ at fixed $q$. At a remote simple
period-$n$ fold, its unfolding covector is
$\alpha_n=\ell D_a(T_a^n-\mathrm{id})$, where $\ell$ is the left
cokernel of the surface return displacement derivative. The package
proves the local criterion $\alpha_n\wedge\nu_f\ne0$ and gives
$\alpha_n$ as an explicit sum of transported parameter variations
along the native orbit (§§2–3).

The all-period bridge remains conditional: one must establish this
independence for every potentially shared simple-fold component,
control lower-period root-of-unity resonance components, and exclude
untested higher-degeneracy strata. The tests must occur on the common
smooth locus of the global image divisors, with the marked branch
equal to the unique local germ of $\mathscr F$; distinct local germs
alone do not imply distinct global components. None of those global obligations
is removed by the local formula. No actual higher-period branch
component containing $\mathscr F$ was found either (§§4–5).

At a special witness in $\mathscr F\cap B^{\rm sm}$, the all-sheet criterion includes
every point in the finite closure of the generic higher-period
sheets, even if its special least period drops to one or two. R3's
lower-period isolation at generic $\mathscr F$ cannot be used to
discard such limits elsewhere on the divisor.

## 4. Primary-source subtraction and applicability

| Paper / inspected version | Venue or status | Relevant result | Exact boundary here | Source |
| --- | --- | --- | --- | --- |
| Rebelo–Roeder, *Dynamics of groups of automorphisms of character varieties and Fatou/Julia decomposition for Painlevé 6*, v4 (2024) | arXiv metadata says forthcoming in *Indiana University Mathematics Journal*; final publisher status not checked | Lemma 10.8: outside countably many real-algebraic hypersurfaces in the ambient four-parameter family, every fixed point of every hyperbolic even word is a saddle | Proves ambient exceptional sets proper, not relative noncontainment on the prescribed fold | [Primary PDF](https://arxiv.org/pdf/2104.09256v4), independently scouted by X1 and selected proof read here |
| Buzzard–Hruska–Ilyashenko (2005), author preprint (2003) | *Inventiones Mathematicae* 161, 45–89 | Theorems 1.1 and 1.4 give full-parameter-space Kupka–Smale genericity and generic rank-two stable/unstable multiplier variation | The family is all normalized polynomial automorphisms of $\mathbb C^2$ of fixed dynamical degree; no transfer to the constrained Fricke fold is proved | [Author PDF](https://www.math.purdue.edu/~buzzard/papers/ks29sep03.pdf), §1.1 read |
| Dujardin–Lyubich, *Stability and bifurcations for dissipative polynomial automorphisms of $\mathbb C^2$*, v2 (2014) | Inspected arXiv preprint | §3.1 and Theorem 3.2 give stability equivalences for substantial families | The definition explicitly excludes conservative families; $T^2$ preserves the two-form and has determinant one, so the hypothesis fails, in addition to the ambient-family mismatch | [Primary PDF](https://arxiv.org/pdf/1305.2898v2), §3.1–Theorem 3.2 read |
| Levin–Shen–van Strien, *Transversality in the setting of hyperbolic and parabolic maps*, v2 (2023) | *Journal d'Analyse Mathématique* 141 (2020), 247–284; updated primary preprint inspected | Main Theorem: one-dimensional local holomorphic families with a specified lifting property have a transversality-or-persistence alternative | No such one-dimensional reduction or lifting property is proved for Fricke returns; persistence is itself an allowed conclusion | [Primary PDF](https://arxiv.org/pdf/1901.09941v2), §§2.1–2.4 read |

The direct Fricke source is the closest one. Its no-escape input and
ambient nondegeneracy argument are classical source contributions,
not R4 discoveries. The translated even-word theorem can be applied
to $T^{2n}$ without changing the native clock. However, the marked
two-cycle already supplies multiplier one for these even powers, so
the whole fixed-point exceptional locus contains $\mathscr F$.
Discarding that locus discards the divisor being studied. This
conclusion is an inference from the accepted fold, not a quotation
of a relative theorem.

The other sources do not repair this restriction. A full-space
generic rank theorem need not retain its rank after restricting to
a prescribed parabolic divisor. The conservative relation also
prevents invoking the cited substantial-family result. The
one-dimensional lifting approach identifies a genuine transversality
mechanism, but supplying its analogue here would itself require a
new theorem; it is not available merely because both problems involve
periodic multipliers.

The explicit slice calculation independently tests the alternative
witness route. It identifies a cusp and its square-root pair; it does
not control the derivative of any remote higher-period orbit. A
large-parameter heuristic on this curve, or a finite period census,
would not establish the required all-sheet statement. Those avenues
were not promoted into an asserted hyperbolicity theorem or executed
as unapproved numerical tests.

X1's [separate direct-family source report](../x1_fricke_parabolic_sources/REPORT.md)
records its additional exact-source checks and bounded search. No
applicable all-higher-period theorem on $\mathscr F$ was located in
this combined pass. That is a bounded source-search result, not a
claim that SF2 is known to be open everywhere in the literature or a
no-go for proving it.

## 5. Handoff and workflow boundary

The cusp formula was sent to D2, together with the explicit smoothness
exclusions and the warning that a local marked squareclass is not the
full cycle-sign field. The conormal formula supplies a precise
parameter-transversality interface for a future proof attempt. No
actual higher-layer inertia parity, vanishing, or character exclusion
is exported as proved.

The proof-writer skill kept the original SF2 quantifier and enforced
separation of local proofs from the unverified global bridge. The
research-lit skill shaped the primary-source hypothesis checks and
the source-subtraction table. Only this lane's REPORT.md and
PROOF_PACKAGE.md were written. Mathematical executions: **zero**;
no child spawned by C4, no shared/frozen/evaluator/Git/manuscript/PDF
edit, and no extra API or private-proof upload. Nonauthor review of
the new local claims is pending coordinator allocation.
