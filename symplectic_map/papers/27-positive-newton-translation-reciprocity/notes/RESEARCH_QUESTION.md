# Research question and exact scope

## Question

For two separated polynomial Hamiltonian shears built from finite positive
mixed Newton supports, which weighted-degree statements are forced by the
support geometry, and which apparent reciprocity or stability statements
fail at the boundary?  The object is a certified weighted-degree orbit and
its leading forms, not a global dynamical-degree classification.

## Family and hypotheses

Let \(K\) be a characteristic-zero coefficient field and \(r\ge 3\).  Let
\[
 E_V,E_W\subset\mathbb Z_{\ge 2}^{\,r}
\]
be finite, nonempty, collected supports with coefficients in \(K^\times\):
\[
 V(q)=\sum_{\alpha\in E_V}c_\alpha q^\alpha,\qquad
 W(p)=\sum_{\beta\in E_W}d_\beta p^\beta .
\]
Define
\[
 S_V(q,p)=(q,p+\nabla V(q)),\qquad
 T_W(q,p)=(q+\nabla W(p),p),\qquad F=T_W\circ S_V .
\]
Degree vectors live in an ordered real space and are independent of \(K\).
A weighted seed has positive integer vectors \(u_0,w_0\) and disjoint
algebraically independent leading tuples.  Only unique exposed maximizers and
strict positive carries are in the headline theorem.

## One-sentence contribution

For separated Hamiltonian shears with nonempty finite collected supports
\(E_V,E_W\subset\mathbb Z_{\ge2}^{\,r}\), \(r\ge3\), every strict weighted-
degree orbit has an exact all-ones translation, at most
\(d_V+d_W-2\) selector changes, and a stationary affine
\((\lambda,\mu)\) tail; reflected inverse phase reciprocity is characterized
edgewise on observable seed spans, while the lower-ideal result is only a
one-edge, one-step statement.

## Headline theorem (target wording)

For a strict edge with unique exposed \(\alpha\in E_V\) and
\(\beta\in E_W\), define
\[
 A_\alpha=\mathbf1\alpha^{\mathsf T}-I,\qquad
 B_\beta=\mathbf1\beta^{\mathsf T}-I .
\]
If \((u,w)\) satisfies the declared selector, carry, target, and reflected
inequalities, then all forward and reflected-inverse leading forms survive and
\[
 (u,w)\longmapsto (B_\beta A_\alpha u,A_\alpha u).
\]
Writing
\[
 h_V(u)=\max_{\alpha\in E_V}\alpha\cdot u,\qquad
 h_W(v)=\max_{\beta\in E_W}\beta\cdot v,
\]
the two half-steps obey
\[
 v=h_V(u)\mathbf1-u,\qquad
 u'=h_W(v)\mathbf1-v=u+\delta\mathbf1,\qquad
 \delta=h_W(v)-h_V(u)>0 .
\]
Thus \(u_n=u_0+t_n\mathbf1\), \(t_0=0\).  If
\[
 d_V=\bigl|\{|\alpha|:\alpha\in E_V\}\bigr|,\qquad
 d_W=\bigl|\{|\beta|:\beta\in E_W\}\bigr|,
\]
then every infinite strict branch has
\[
 \#\{\text{selector changes}\}\le d_V+d_W-2 .
\]
After the last change, a stationary pair satisfies
\[
 t_{n+1}=\lambda t_n+\mu,\qquad
 \lambda=(|\alpha|-1)(|\beta|-1)>1,\qquad
 \mu=((|\beta|-1)\alpha-\beta)\cdot u_0 .
\]

Let \(R\) reverse coordinates and let
\(R_{\rm state}(u,w)=(Rw,Ru)\).  Reflected inverse reciprocity is an
edgewise statement on
\[
 U_e=\operatorname{span}_{\mathbb R}\{u:(u,w)\in C_e^{\mathbb Z}\},\qquad
 V_e=\operatorname{span}_{\mathbb R}\{A_\alpha u:(u,w)\in C_e^{\mathbb Z}\},
\]
where \(C_e^{\mathbb Z}\) is the positive-integer part of the declared pair
cell.  The required actions are
\[
 B_{R\alpha}R=RA_\alpha,\qquad A_{R\beta}R=RB_\beta .
\]
Literal full-matrix identities are asserted only when the relevant spans are
\(\mathbb R^r\).  The lower-ideal corollary uses four normalized compact
projections and preserves one forward and one reflected inverse leading step.

## Equality cases and failure boundaries

Equal-total-degree support differences are invariant along the translated
ray.  A persistent exposed tie is a wall boundary, not a strict selector.
A nonpositive carry \(\delta\le0\), an empty lattice cell, or a missing
target/reflected certificate terminates the certified branch.  A proper
\(U_e\) or \(V_e\) span supports only the induced restriction; it cannot be
promoted to a full matrix identity.  Same-seed reciprocity is meaningful only
for an \(R_{\rm state}\)-fixed pair.

The positive-support Hessian result is an auxiliary wall certificate; it does
not select a tied vertex.  The theorem excludes empty or uncollected
supports, zero coefficients, support coordinates 0 or 1, positive
characteristic, mixed-\(W\) extensions, and \(r=2\).  It does not claim a
map-level reversor, global conjugacy or classification, entropy, higher
dynamical degrees, a minimal scalar recurrence, a Perron algebraic degree,
global perturbation stability, or priority.

## Motivation and falsifiability

The two individual shears have simple gradient degree maps, but their
composition appears to create a high-dimensional selector automaton.  The
positive-support assumptions collapse both phases onto an all-ones
translation, making a sharp wall count and a phase-resolved inverse criterion
possible while still allowing a genuinely transient \(r=3\) path.  The exact
fixture and the cancellation/reflection boundaries make the statement
falsifiable rather than an appeal to generic coefficients.

BATCH07_PAPER27_RESEARCH_QUESTION_FROZEN
