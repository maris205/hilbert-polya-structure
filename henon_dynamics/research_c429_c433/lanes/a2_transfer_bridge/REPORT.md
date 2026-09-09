# A2: ordinary periods to a finite algebraic transfer

2026-09-09 UTC. Initial question freeze preceded substantial proof writing;
hand feasibility analysis and local/primary-source inspection had begun.
This lane complements A1 on **one original PC424-L question**, not a second
paper candidate. No mathematical program is authorized or executed here.

## Exact unchanged question and decisive criterion

For every odd prime $p$, $k=\overline{\mathbb F}_p$, every $c\in k$ and
every $h\in k[x]$, set $K=k(x)$, $f=x^2+c$ and
$\sigma|_k=\mathrm{id}$, $\sigma(x)=f(x)$. Suppose

$$\sum_{a\in O}h(a)=0$$

for every ordinary geometric primitive $f$-orbit $O$, counting each
distinct point once, including periods divisible by $p$. Does this imply
that there is one finite field extension $E/K$ carrying an injective
extension of $\sigma$ and an element $u\in E$ with

$$\sigma(u)-u=h?$$

The native clock is one application of $f$ (or the triangular lift
$(x,y)\mapsto(f(x),y+h(x))$), never arithmetic Frobenius. Success means
constructing that single compatible algebraic object for all these
quantifiers. A counterexample must satisfy all primitive-orbit conditions
while admitting no such object. Failure of an Artin–Schreier construction
is not a counterexample to the full implication.

## Source subtraction and allocated attack

The complete R6 descent theorem in
[PROOF_AND_GAPS.md](../../../research_c424_c428/continuation_round6/positive_characteristic/PROOF_AND_GAPS.md),
Sections 1–7, is imported unchanged: any such algebraic $u$ for a
prime-to-$p$ polynomial base degree is already in $k[x]$. In particular
the present existence question is exactly PC424-L, not a relaxation.
R6's frozen question, complete proof, source audit and disposition were
read. The initial PC proof and R3 prime-contact proof were also read;
finite interpolation, quadratic normal form, rational-pole descent and
the new-prime multiplicity obstruction are old results and are not
claimed here. A1 owns the direct polynomial-quotient/multiplicity attack.

This lane tested finite étale covers and invariant Artin–Schreier torsors.
The precise certificate is a **global identity**
$b\circ f-b=h^p-h$, not independent pointwise roots of
$T^p-T-b(a)$. A proved geometric obstruction is that no nontrivial
connected finite étale cover of $\mathbb A^1_k$ admits a compatible
self-map over $f$. Its compactification/Riemann–Hurwitz proof and its
implication for the missing existence step are kept separate below.

The bounded-transfer sub-attack asks a discriminating algebraic question,
not for another interpolation census: can finite transfer graphs be put on
curves of uniformly bounded **total degree**, independent of field size?
A Bézout argument can convert such a bound into a periodic algebraic
curve. Bounding only degree in the transfer variable is vacuous, since
every interpolant $Q_r$ already satisfies $Y-Q_r(X)=0$.

## Result: original implication open; three exact interfaces obtained

**Original all-orbit implication: NOT CURRENTLY JUSTIFIED / OPEN.**
No original counterexample has been established. No independent paper
or admission is proposed. The complete author-level arguments are in
[PROOF_SUPPLEMENT.md](PROOF_SUPPLEMENT.md); they have not yet received
a nonauthor internal check.

| Interface | Exact proved output | What a consumer must still supply |
| --- | --- | --- |
| Finite étale obstruction, supplement Section 1 | For any connected finite étale $\pi:Y\to\mathbb A^1_k$, a self-map $g$ with $\pi g=f\pi$ forces $\deg\pi=1$. No Galois assumption is needed. | This does not construct a section or a transfer from orbit data. It rules out searching for a nontrivial connected étale intermediary. |
| Artin–Schreier certificate, supplement Section 2 | $\Delta b=h^p-h$ with $b\in k(x)$ exists iff $h=\Delta Q+\beta$, $Q\in k[x]$, $\beta\in\mathbb F_p$. A fixed-point orbit kills $\beta$. | One must derive the global identity from the ordinary sums; Artin–Schreier theory alone does not do so. |
| Bounded-graph extraction, supplement Sections 3–4 | If a transfer graph on a finite $f$-stable set $S$ lies on a nonzero curve equation of total degree at most $D$, then $|S|>2^D\max(2,\deg h)D^4$ forces $h=\Delta Q+\beta$, $\beta\in k$. Again a fixed-point orbit kills $\beta$. | A uniform bound on total algebraic degree for some finite transfer graphs. The bound may depend on $p,c,h$, but not on field size. |

For the first theorem, compactify $Y$ to $C$, write $m=\deg\pi$
and let $b\ge1$ count its points above infinity. The lifted map has
degree $2$ and is separable. The $m$ points above the finite critical
point $0$ contribute $m$ to its ramification, and total invariance of
the boundary contributes $b$. Riemann–Hurwitz gives
$2-2g(C)\ge m+b\ge2$, forcing $m=b=1$.

For the second, every Artin–Schreier cohomology class has a unique
polynomial representative with zero constant term and positive exponents
prime to $p$. Pullback by $f$ doubles its leading degree. Thus no nonzero
class has a finite pullback orbit. A compatible torsor must split; its
lift can still permute the split components by the constant $\beta$.

For the third, Bézout converts sufficiently many graph points into a
chain of dominant images between the finitely many curve components.
Each tick loses at most a factor of two in graph-point count. A repeated
component gives a periodic nonvertical algebraic curve, hence a finite
algebraic transfer for an iterate. R6 applies to that iterate, and a
commuting-difference calculation returns to the original one-step
equation up to a constant. This is a conditional extraction theorem,
not an interpolation experiment or an asserted uniform bound.

## Genuine obstruction examples and what they do not prove

Underlying geometric fiber splitting cannot detect the required global
cover: the nonzero Artin–Schreier class $[x]$ restricts to zero on every
finite reduced set of $k$-points, including every ordinary primitive
orbit. All those residue fields are algebraically closed. The additional
dynamical holonomy must not be erased by replacing it with this splitting
test.

The compatible disconnected cover $y^p-y=0$ with lift
$(x,y)\mapsto(f(x),y+1)$ permutes all $p$ components. It has no
one-step stable field component furnishing $\sigma(u)-u=1$.
This explicitly separates a finite étale **algebra** from the requested
stable extension **field**. The observable $h=1$ fails the original
fixed-point condition, so this is not a counterexample to PC424-L.

## Precise unresolved implication

With all original quantifiers retained, either of these would finish
the algebraic route:

1. Derive $\Delta b=h^p-h$ for one $b\in k(x)$ from all ordinary
   primitive-orbit sums.
2. For a finite field $\mathbb F_q$ containing the coefficients,
   derive a uniform total-degree bound $D$ for nonzero equations of
   some transfer graphs over $\mathbb F_{q^n}$ for arbitrarily large
   $n$.

The second condition allows the equations and transfer choices to vary
with $n$; no cross-field compatibility is assumed. Once such a bound is
provided, one sufficiently large finite graph yields a polynomial
transfer by the proved threshold theorem. Conversely a polynomial
transfer supplies that bound, via the equation $Y-Q(X)=0$.
This exact equivalence is the new bounded interface; the ordinary sums
have not been proved to supply its bound. Merely writing $Y-Q_n(X)=0$
for unrelated interpolants bounds only $\deg_Y$, which is not enough.

## Primary-source access and subtraction limits

Local sources were inspected first; no relevant local PDF was needed.
The root `papers/` belongs to a different stream and was not searched as
the mathematical corpus. Only the relevant Hénon proofs and source
records were used. Ordinary browsing was used, not a programmatic
resolver or an external-model service.

| Primary source actually opened | Actual read scope and use |
| --- | --- |
| [Stacks, Section 53.2, Curves and function fields](https://stacks.math.columbia.edu/tag/0BXX) | Lemmas 53.2.1–53.2.5 and Theorem 53.2.6 with their displayed proofs; compactification and extension of curve maps. |
| [Stacks, Section 53.12, Riemann–Hurwitz](https://stacks.math.columbia.edu/tag/0C1B) | Full displayed section through Lemma 53.12.4 and its proof; separability, the genus identity and different exponent at least $e-1$. |
| [Stacks, Section 59.63, Artin–Schreier sequence](https://stacks.math.columbia.edu/tag/0A3J) | Exact-sequence opening and affine-vanishing argument of Lemma 59.63.1; the explicit polynomial reduction is proved in the supplement. No finite-dimensionality claim for affine $H^1$ is imported. |
| [J. S. Milne, Algebraic Geometry](https://www.jmilne.org/math/CourseNotes/AG.pdf) | Author-hosted PDF, Section 6n, Theorem 6.37, displayed proof and Remark 6.38, browser-extracted lines 9037–9109; only the distinct-point Bézout upper bound is used. No local PDF or local page anchor was used. |

Eleven targeted browser search formulations covered Artin–Schreier
sequence/dynamics, finite-field periodic sums, algebraic cohomological
equations, invariant finite étale covers, Riemann–Hurwitz and Bézout.
Search-only hits on analytic Livšic theory, finite-field dynamics and
unrelated invariant-ring material were not promoted into proof inputs.
No inspected primary source supplied the missing period-to-algebraicity
implication. This bounded search is not a claim that no such theorem
exists, nor a global novelty certificate. Riemann–Hurwitz,
Artin–Schreier reduction, Bézout and R6 ownership are explicitly
subtracted from any future claim of an independent research increment.

## Execution, skill influence and handoff

Only this lane's `REPORT.md` and `PROOF_SUPPLEMENT.md` were written.
No old files, global indexes, Git state, formal evaluations, manuscripts,
PDFs, code, experiments, model/API calls or credentials were changed or
executed. Mathematical program count remains **0**; all new deductions
are hand proofs. No nested agent was launched.

The batch workflow kept A2 complementary to A1 and forbade counting these
auxiliaries as another paper. Proof-writer preserved the unchanged claim
and marked its exact gap. Research-lit kept classical primary inputs
separate from the new deductions. The ARS router was inspected, but no
ARS research/review pipeline or source-role workflow was run in this
mathematical lane, consistent with the scoped batch plan.

The coordinator received the exact finite-étale obstruction, AS
certificate and bounded-graph consumer conditions as they were obtained.
Potential consumers are A1 (uniform-complexity closure), X1 (interface
composition) and X2 (split-algebra/stable-field and geometric-point
splitting firewalls). They must check the stated compatibility conditions;
none follows merely by citing the interface. No target Euler factor,
root number, automorphy, zero correspondence or Hilbert–Pólya claim is
made.
