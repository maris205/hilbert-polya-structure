# NFIT theorem spike — nonsingularity-feedback identity toggling

Let `q` be a power of two, let `M_n(q)` be the `n x n` matrices over
`GF(q)`, and define

`T(A) = A + I` if `A` is invertible, and `T(A)=A` otherwise.

Equivalently, `T(A)=A+det(A)^(q-1) I`.  External circulation remains
`HOLD_EXTERNAL`.

## Exact pair reduction

Because the characteristic is two, translation by `I` partitions the carrier
into unordered pairs `{A,A+I}`.  On such a pair there are only three cases:

1. both matrices are singular: both are fixed;
2. exactly one is invertible: the invertible member maps in one step to the
   singular fixed member; or
3. both are invertible: the two members form a strict two-cycle.

This proves at once that the maximum tail is one and the only periods are one
and two.  It also makes the inverse statement target-local rather than merely
enumerative:

`T^(-1)(B) = ({B} if B is singular) union ({B+I} if B+I is invertible)`.

## Frozen counting symbol

Write

- `N=q^(n^2)`,
- `G=|GL_n(q)|=product_(j=0)^(n-1)(q^n-q^j)`, and
- `D=D_n(q)=#{A: A and A+I are invertible}`.

Subspace Möbius inversion on the fixed space of an invertible matrix gives

`D=sum_(k=0)^n (-1)^k q^(binom(k,2)) [n choose k]_q
       q^(k(n-k)) |GL_(n-k)(q)|`.

Indeed, an invertible map fixing a prescribed `k`-space pointwise has
`q^(k(n-k)) |GL_(n-k)(q)|` choices, and the subspace-lattice Möbius value is
`(-1)^k q^(binom(k,2))`.  In characteristic two, `A+I` is invertible exactly
when `A` has zero fixed space.

## Proposed theorem package

- exactly `N-G` fixed states;
- exactly `D/2` strict two-cycles (`D` recurrent two-cycle states);
- exactly `G-D` tail-one states and the same number of nonimage targets;
- image and recurrent-set size `N-G+D`;
- for every `m>=1`,
  `|Fix(T^m)|=N-G` for odd `m`, and `N-G+D` for even `m`;
- indegree profile: `G-D` states of indegree zero, `G-D` of indegree two,
  and `N-2G+2D` of indegree one;
- the displayed every-target fibre formula, including all empty-fibre and
  mixed-pair boundary cases.

The pair dynamics is elementary and receives zero contribution credit.  The
candidate survives this scout only on the literal algebraic feedback together
with the linear-derangement census, full temporal atlas, and every-target
inverse geometry.  A direct owner of that conjunction kills it.
