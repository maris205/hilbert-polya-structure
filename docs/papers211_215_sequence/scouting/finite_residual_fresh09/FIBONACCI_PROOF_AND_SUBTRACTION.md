# Finite-field Fibonacci update: exact fibres, unresolved time data

Author: `/root/round211_finite_matching_scout/p213_title_record_check`.
The propositions below are PROVABLE AS STATED; a complete, materially new
two-axis theorem contract is NOT CURRENTLY JUSTIFIED.
NO_NOMINATION / HOLD_EXTERNAL. No pilot or manuscript review.

## Literal and carrier

For every prime power q>=2 let
$$
 T_q:\mathbb F_q^2\longrightarrow\mathbb F_q^2,
 \qquad T_q(x,y)=(y,xy+1).
$$
Use the entire affine plane, including zeros, with simultaneous old-state
coordinates. No torus restriction, field extension chosen by an experiment,
quotient, scheduler or clock register is implicit. Dependencies below are
field division and elementary finite functional-graph structure.

## 1. Complete target fibres, image and sharp extremum

For every target (u,v),
$$
 T_q^{-1}(u,v)=
 \begin{cases}
 \{((v-1)/u,u)\},&u\ne0,\\
 \{(x,0):x\in\mathbb F_q\},&(u,v)=(0,1),\\
 \varnothing,&u=0, v\ne1.
 \end{cases} \tag{1}
$$
Indeed the first output equation forces y=u, and the second is xu+1=v.
For u nonzero it has exactly the one displayed solution; for u=0 it is
consistent exactly when v=1, independently of x. Conversely every displayed
source satisfies both equations. The branches are disjoint.

Thus the image has q(q-1)+1=q^2-q+1 elements, exactly q-1 targets have no
sources, and e=(0,1) is the unique target with the sharp maximal fibre q.
All other image vertices have indegree one.

## 2. Precisely what the functional-graph skeleton determines

Proposition. The vertex e lies on a directed cycle. Its component consists
of that cycle and exactly q-1 pairwise disjoint unbranched incoming chains,
each nonempty and ending at e. Their initial vertices are exactly the
q-1 leaves (0,v) with v!=1. Every other component is a pure directed cycle.

Proof. Any forward orbit eventually enters a cycle by finiteness.
If e were not on a cycle, let z be the first cycle vertex reached from e.
The predecessor of z on that tail differs from its cycle predecessor, so
z would have indegree at least two. By (1) this forces z=e, contradicting
the assumption that e was off-cycle. Thus e is cyclic.

For any off-cycle vertex, its first cycle entry has both a tail and a cycle
predecessor, so the same argument forces the entry to be e. Therefore
there are no tails on any other cycle and no off-cycle branch point.
Exactly one predecessor of e is its cycle predecessor; the other q-1
predecessors lie off-cycle. Follow each backwards. At every off-cycle
vertex there is at most one predecessor, and the backward chain cannot
repeat or it would contain a cycle whose forward orbit leaves that cycle.
Finiteness therefore ends each at an indegree-zero leaf. Different chains
cannot meet before e, since such a meeting would be another vertex of
indegree at least two. Conversely every off-cycle vertex belongs to one
of these chains, because its forward orbit enters e. Formula (1) identifies
all q-1 leaves and proves the asserted completeness.

This describes the graph's *shape*, not the lengths or census. In
particular, writing the height as the maximum of these unevaluated chain
lengths is not a sharp all-q clock theorem. Starting at e uses only 0,1,
addition and multiplication, so its orbit remains in the prime subfield;
its length is independent of the extension degree at fixed characteristic.
That fact does not evaluate the length as a function of the characteristic.

## 3. Exact external and internal adapters

Let S(x,y)=(y,x). The primary body of El Abdalaoui–Bonnot–Messaoudi–Sester,
[On the Fibonacci complex dynamical systems](https://arxiv.org/pdf/1304.4864v1),
Introduction, p. 2, defines H_c(x,y)=(xy+c,x) over the complex plane.
Polynomial substitution proves
$$
 T_q=S\circ H_1\circ S
$$
when this same integral polynomial is interpreted over the finite field.
This is an actual coordinate-swap conjugacy of the polynomial maps on
the chosen finite-field carrier, not a claim that the source's complex
Julia-set results classify finite-field cycles.

For the old multiplicative Fibonacci mechanism
M(x,y)=(y,xy), put V(u,v)=(u,v+1). Then
$$
 T_q=V\circ M,\qquad T_q^{-1}(z)=M^{-1}(V^{-1}z). \tag{2}
$$
Output translation transports the entire inverse/image/fibre extremum,
so (1) has no independent residual mechanism beyond scalar multiplication.
M also equals S H_0 S. Its exact recurrence is already the squared-norm
factor in the current closed
[nonlinear residual proof](../finite_nonlinear_residual_desk01/PROOF_PACKAGE.md),
Section 3, for old XPF. A factor of a six-coordinate vector map is not
asserted to be a conjugacy with that full vector map.

Equation (2) is NOT a conjugacy assertion between T_q and M. For example,
over F_2, M has two fixed states (0,0),(1,1), whereas T_q has none:
a fixed state requires x=y=a and a^2-a+1=0, whose value is 1 at both
field elements. This is a two-value symbolic check, not an executed pilot.
It rules out a bijective conjugacy between those two q=2 systems.

[P121](../../../../papers/121-random-product-plus-one-coalescence/main.tex)
has the scalar local operation (x,y)->xy+1 but chooses an adjacent pair
randomly and merges it in a positive-integer word. It is not a finite-field
plane map, and its random coalescence/history theorems are not credited as
a full-carrier conjugacy or as a temporal solution here.
The fully read fresh08 Lyness boundary concerns a rationalized inverse
update; neither its P150 conjugacy nor a local inverse product supplies
the missing recurrence theorem for T_q.

## 4. Missing result and stopping decision

No all-q evaluated classification of the special-cycle length, all other
cycles, q-1 chain lengths, recurrent-state count or sharp entrance height
has been proved here. Generic finiteness, the prime-subfield observation,
polynomial iteration or a full-carrier search would not fill this gap.
The known polynomial-family source and the transported inverse leave no
justified two-axis residual. This is a bounded negative, not a theorem
that finite-field Fibonacci dynamics can never have useful new results.
No no-hit global novelty assertion, third literal or numerical expansion.
