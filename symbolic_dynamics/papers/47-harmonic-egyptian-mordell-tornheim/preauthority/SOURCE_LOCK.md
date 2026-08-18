# Source Lock — Harmonic/Egyptian Adjacency

## Candidate identity

- Candidate: SD-C49
- Paper position: Paper 47
- Portable namespace: papers/47-harmonic-egyptian-mordell-tornheim/preauthority
- Phase-2 parent seal:
  d035310ac046981abe7a37a033b1354e3d8da3f53f33d631786ed80f40b90181

## Frozen graph and symbolic source

Let \(G_{\rm E}\) be the undirected looped graph on \(\mathbb N\) with

$$
m\sim n\iff m+n\mid mn.
$$

Equivalently, the harmonic quotient \(k=mn/(m+n)\) must be a positive
integer. The symbolic source is the one-sided countable edge shift of this
graph with the left shift.

A primitive object is a least-period cyclic vertex word. One shift edge is
one unit of time, and \(z\) marks one edge. Ordered edge parameters
\((t,a,b)\) are derived coordinates, not temporal primitives.

## Frozen operator

On \(\ell^2(\mathbb N)\),

$$
E_s(m,n)=\mathbf 1_{\{m+n\mid mn\}}(mn)^{-s/2},
$$

using the real logarithm for complex powers. Loops are retained. The
operator is complex symmetric; it is Hermitian only when the parameter is
real.

## Unique edge coordinates

Writing \(g=(m,n)\), \(m=ga\), \(n=gb\), and \((a,b)=1\), the edge condition
forces \(a+b\mid g\). Thus \(g=t(a+b)\) and

$$
(m,n,k)=(t a(a+b),\,t b(a+b),\,t ab).
$$

Conversely, every such triple is legal. This is an ordered bijection.

## Determinant convention

- ordinary Fredholm determinant only for \(\Re s>1\);
- Hilbert–Carleman determinant \(\det_2(I-zE_s)\) for
  \(\Re s>1/2\);
- trace powers are asserted only in domains where the corresponding product
  is trace class;
- the first two trace formulas are same-object identities, not definitions
  of a different zeta operator.

## Allowed evidence

- exact divisibility, gcd, and divisor enumeration;
- exact coprime-scale parameterization;
- standard divisor-function estimates and trace ideals;
- primary Tornheim, Mordell, Bradley–Zhou, Tsumura, and
  Kalinin--Lupercio--Shkolnikov sources as ownership boundaries;
- exact finite enumerations as controls;
- the final sealed Phase-2 package.

## Forbidden moves

- deleting loops;
- replacing divisibility by an approximate harmonic condition;
- treating \((t,a,b)\) as a primitive orbit;
- claiming novelty for the parameterization or MT series;
- reusing P46's endpoint computation as Paper-47 evidence;
- changing to Pythagorean, Diophantine-tuple, or another conic support and
  counting it as a sequel;
- using finite cutoff spectra to prove endpoints;
- importing target zeros or fitted parameters.

## Exact claim boundary

The strongest authorized theorem is the unique edge parameterization, exact
\(0,1/2,1\) phase diagram, legal determinant, zeta first trace, the
\((s,s;2s)\) primitive Mordell–Tornheim second trace for this frozen harmonic
graph, and mixed-cycle realization for this single looped graph. Primitive
Mordell--Tornheim realization in general is prior-owned and is not claimed.
