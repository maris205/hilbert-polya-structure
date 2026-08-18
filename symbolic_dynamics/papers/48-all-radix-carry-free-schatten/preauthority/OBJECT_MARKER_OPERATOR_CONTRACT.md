# Object, Digit, Marker, and Operator Contract

## Types

| Object | Type | Owner | Forbidden identification |
|---|---|---|---|
| \(m,n\) | PositiveIntegerVertex | carry-free graph | zero-completed digit word |
| base-\(b\) digits | PositionalCoordinates | support predicate | temporal symbols |
| \(C_b\) | FiniteDigitCompatibilityMatrix | one digit | infinite operator |
| \(I_k=[b^k,b^{k+1})\) | PositiveVertexShell | magnitude partition | orbit period |
| closed vertex word | TemporalCycle | edge shift | binomial coefficient |
| \(z\) | OneEdgeMarker | determinant ledger | radix digit |
| \(B_{b,s}\) | DirichletWeightedAdjacency | \(\ell^2(\mathbb N)\) | finite Boolean graph |

## Clock and weight

For a based closed walk \(n_{r+1}=n_1\),

$$
\prod_{i=1}^r B_{b,s}(n_i,n_{i+1})
=\prod_{i=1}^r n_i^{-s}.
$$

The marker \(z^r\) counts edges. Shell weights and digit singular values are
arithmetic/operator data, not time.

## Zero boundary

The matrix \(C_b^{\otimes L}\) naturally indexes all length-\(L\) digit
words, including the zero word. It is a finite control. The infinite graph
uses positive integers only. Any trace or least-period statement must delete
zero before interpreting a temporal orbit.

## Trace boundary

A loop at \(m\) exists exactly when every base-\(b\) digit \(d\) of \(m\)
satisfies \(2d<b\). Hence:

- for \(b=2\), the positive graph has no loops and its trace Dirichlet
  series is identically zero;
- for \(b>2\), the trace sums over digits
  \(0\le d\le\lfloor(b-1)/2\rfloor\).

For \(b>2\) the trace is positive on the real trace-class half-line. No
zero-free claim is made for complex \(s\).

## Determinant domains

| Object | Legal domain |
|---|---|
| bounded, compact, \(S_2\), \(\det_2\) | \(\Re s>1\) |
| \(S_1\), ordinary trace and determinant | \(\Re s>\alpha_b\) |
| general \(S_q\), \(1\le q<\infty\) | \(\Re s>\max(1,\log_b\kappa_{b,q})\) |

## Firewall

| Mutation | Verdict |
|---|---|
| add zero as an infinite vertex | OBJECT_CHANGE |
| call \(C_b^{\otimes L}\) the source operator | FINITE_CONTROL_TYPE_ERROR |
| use Kummer for composite radix | SOURCE_SCOPE_ERROR |
| include equality at the critical surface | ENDPOINT_ERROR |
| use same-shell binary pinching | ZERO_BLOCK_ERROR |
| call digit positions temporal periods | CLOCK_ERROR |
| infer AM zeta from infinite fixed counts | DIVERGENT_LEDGER_ERROR |
| infer support periods from a complex trace value | CANCELLATION_ERROR |
