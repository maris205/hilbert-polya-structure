# Object, Marker, Operator, and Trace Contract

## Typed objects

| Symbol | Type | Owner | Forbidden identification |
|---|---|---|---|
| \(m,n\) | PositiveIntegerVertex | \(G_{\rm E}\) | rational-prime primitive |
| \(k=mn/(m+n)\) | IntegralHarmonicQuotient | an edge | time or orbit length |
| \((t,a,b)\) | OrderedCoprimeEdgeCoordinate | edge bijection | primitive cycle |
| \((n_1,\ldots,n_r)\) | BasedClosedVertexWalk | edge shift | unordered Diophantine tuple |
| \(\mathcal O\) | LeastPeriodClosedOrbit | unit edge clock | repeated traversal |
| \(z\) | OneEdgeTimeMarker | determinant ledger | harmonic quotient |
| \(E_s\) | DirichletWeightedAdjacency | \(\ell^2(\mathbb N)\) | positive or Hilbert–Pólya operator |

## Primitive and repetition law

Rotations of a least-period closed vertex word represent one primitive orbit.
Its \(j\)-fold traversal is a repetition of length \(jr\). Edge coordinates
and harmonic quotients are reconstructed from consecutive vertices and never
replace the temporal object.

## Weight law

For a based closed walk \(n_{r+1}=n_1\),

$$
\prod_{i=1}^r E_s(n_i,n_{i+1})
=\prod_{i=1}^r n_i^{-s}.
$$

Therefore legal trace powers sum the vertex Dirichlet weight over based
closed walks. Division by \(r\) in a determinant logarithm removes the base
point convention; it does not create arithmetic primes.

## Loop ownership

A loop occurs exactly when \(2m\mid m^2\), hence exactly when \(m\) is even.
Deleting loops changes:

- the source graph;
- the trace \(2^{-s}\zeta(s)\);
- the trace-class endpoint lower bound;
- the primitive period-one ledger.

Loop deletion is an object change, not a harmless graph convention.

## Mordell–Tornheim ownership

The second trace uses ordered edges:

$$
\operatorname{Tr}(E_s^2)
=\sum_{m\sim n}(mn)^{-s}.
$$

The edge bijection turns this into a scale sum times the coprime
\((s,s;2s)\) Mordell–Tornheim series. Classical MT identities and other
primitive-MT realizations remain externally owned; the graph owns only this
exact exponent-pattern realization as its trace.

## Determinant domains

| Object | Legal domain |
|---|---|
| \(E_s\) bounded/compact | \(\Re s>0\) |
| \(E_s\in S_2\), \(\det_2(I-zE_s)\) | \(\Re s>1/2\) |
| \(E_s\in S_1\), \(\operatorname{Tr}E_s\), \(\det(I-zE_s)\) | \(\Re s>1\) |

## Firewall verdicts

| Proposed move | Verdict |
|---|---|
| delete all even loops | OBJECT_CHANGE |
| call \(t,a,b\) primitive orbits | TYPE_ERROR |
| count \(k\) as elapsed time | CLOCK_ERROR |
| claim MT-series novelty | OWNERSHIP_ERROR |
| infer trace class from Hilbert–Schmidt membership | IDEAL_ERROR |
| call the real-\(s\) symmetric matrix positive semidefinite | OPERATOR_SIGN_ERROR |
| use ordinary determinant in the \(S_2\)-only strip | DETERMINANT_DOMAIN_ERROR |
