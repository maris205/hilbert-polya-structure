# Object, Marker, Operator, and Determinant Contract

## Typed objects

| Symbol | Type | Owner | Forbidden identification |
|---|---|---|---|
| $n$ | `PositiveIntegerVertex` | $G_2$ | rational-prime primitive |
| $2^a$ | `DyadicEdgeLabel` | support relation | temporal primitive orbit |
| $(n_1,\ldots,n_r)$ | `ClosedVertexWalk` | $X_{G_2}$ | unordered edge-label tuple |
| $\mathcal O$ | `LeastPeriodClosedOrbit` | unit edge clock | repeated traversal |
| $z$ | `OneEdgeTimeMarker` | trace/determinant ledger | arithmetic magnitude marker |
| $H_s$ | `DirichletWeightedAdjacency` | $\ell^2(\mathbb N)$ | self-adjoint HP operator for nonreal $s$ |
| $A_s$ | `OddValuationBlock` | odd vertices | finite cutoff |

## Primitive and repetition law

A primitive orbit is a cyclic vertex word with least shift period $r$.
Rotations represent the same orbit.  Its $j$-fold traversal has length $jr$
and is a repetition, not a new primitive.  Edge-label tuples are derived from
the vertex cycle and do not replace it as the primitive type.

## Weight ownership

For a closed walk $n_1,\ldots,n_r,n_{r+1}=n_1$, the operator product is

$$
\prod_{i=1}^r H_s(n_i,n_{i+1})
=\prod_{i=1}^r n_i^{-s}.
$$

Thus $\operatorname{Tr}(H_s^r)$, when legal, is the sum of this weight over
based closed walks of length $r$.  Division by $r$ in a determinant logarithm
accounts for cyclic base points; it does not convert a repeated orbit into a
new primitive.

## Valuation and marker ownership

The exact equality $v_2(n_i)=v_2(n_{i+1})$ holds along every edge.  A closed
walk therefore lies in a unique valuation block $2^k\mathbb N_{\rm odd}$.
The factor $2^{-krs}$ in an $r$-step trace is an arithmetic weight, while
$z^r$ is the time marker.  These two roles may not be interchanged.

## Legal determinant identities

For $\sigma>1/2$ and $r\ge2$,

$$
\operatorname{Tr}(H_s^r)
=\frac{\operatorname{Tr}(A_s^r)}{1-2^{-rs}},
$$

and

$$
\det_2(I-zH_s)
=\prod_{k\ge0}\det_2(I-z2^{-ks}A_s).
$$

The product is an identity of entire regularized determinants.  For
$\sigma>1$ the ordinary trace is

$$
\operatorname{Tr}(H_s)=\sum_{k\ge0}2^{-ks}=\frac1{1-2^{-s}}.
$$

## Firewall verdicts

| Proposed move | Verdict | Reason |
|---|---|---|
| remove the loop at $1$ | `OBJECT_CHANGE` | changes trace and the odd block |
| use $q_i=2^{a_i}$ as primitive objects | `TYPE_ERROR` | labels constrain vertex cycles |
| identify $2^a$ with all rational primes | `SUPPORT_ERROR` | only one explicit prime base occurs |
| claim ordinary determinant for $1/2<\sigma\le1$ | `IDEAL_ERROR` | only $\det_2$ is legal |
| call $H_s$ Hermitian for $\Im s\ne0$ | `OPERATOR_TYPE_ERROR` | complex symmetric is not Hermitian |
| infer endpoint membership from cutoff SVD | `LIMIT_ERROR` | endpoints require infinite lower bounds |

