# Narrative report: folded-hypercube products and component-order inversion

**Status:** round-2 internally accepted anonymous theorem record /
`OWNER_REPAIRED / HOLD_EXTERNAL`
**Carrier:** one push orbit of orientations of a fixed finite simple graph
**Literal randomness:** choose one labelled vertex uniformly at each step

## Owner subtraction changes the story

A connected component of order `s` is not merely an unspecified abelian
quotient walk.  Choosing a pivot identifies

```text
F_2^s / <1>  ~=  F_2^(s-1),
[e_nonpivot] -> coordinate vector,
[e_pivot]    -> all-ones vector.
```

This is exactly the standard Cayley presentation of the folded hypercube
`FQ_(s-1)`.  Xu and Meng directly own that presentation and its character
spectrum.  Xu and Ma own the folded-hypercube bipartiteness boundary, while
Chen, Li, and Lin show that random walks on the same named graph family are an
established subject.  Vertex pushing, generic finite-abelian Fourier analysis,
and uniform stationarity were already zero-credit inputs.  Round 1 therefore
subtracts the folded-hypercube identification, all single-component spectral
facts, bipartiteness, and generic return-as-spectral-moment facts as well.

The residual is narrower:

1. expose the labelled disconnected chain as a degree-weighted random-scan
   product and write its multi-component multiplicity polynomial; and
2. recover the component-order multiset from that polynomial when the ambient
   order `n` is supplied, using a rigorous input-only algorithm.

No novelty or priority claim is made for either item.

## Exact product kernel and conventions

If the component orders are `s_1,...,s_c` and `m_1` are isolates, then

```text
P_G = sum_(i:s_i>=2) (s_i/n) (P_FQ_(s_i-1) tensor I_elsewhere)
      + (m_1/n) I.
```

This is a weighted tensor sum, not an unweighted simple-graph Cartesian
product.  Two low-dimensional cases are frozen explicitly:

- `s=1`: pushing the isolate is an identity move;
- `s=2`: the two labelled vertices induce the same nonzero quotient
  translation, so the unnormalised generator is doubled even though the
  normalised component kernel agrees with the usual two-state `FQ_1` walk.

Accordingly, “transition spectrum” always means the labelled-generator Markov
kernel, not a loop/parallel-edge-suppressed adjacency matrix.

The known single-factor spectrum combines over components as

```text
M_G(x) = product_i B_(s_i)(x),
B_s(x) = sum_(j even) binom(s,j) x^j.
```

The eigenvalue `(n-2k)/n` has multiplicity `[x^k]M_G(x)`.  Character
orthogonality gives the return law.  The global period is two precisely when
all component orders are even; an isolate is correctly an aperiodic loop.
These consequences remain proved, but single-factor spectrum, bipartiteness,
and generic walk machinery receive zero credit.

## Known-`n` inverse and executable algorithm

Knowing `n`, distinct eigenvalue labels recover `M_G`.  Compress it as

```text
M_G(x) = Q_G(x^2),
Q_G(y) = product_i E_(s_i)(y),
E_s(y) = sum_r binom(s,2r) y^r.
```

For `s>=2`,

```text
E_s(-t^2) = (1+t^2)^(s/2) cos(s arctan t).
```

All roots are simple and negative.  The root nearest zero is

```text
rho_s = -tan^2(pi/(2s)),
```

and moves strictly toward zero as `s` increases.  If `r<s` and
`E_r(rho_s)=0`, the cosine zero equation would force
`r/s=2j+1`, impossible because the left side is less than one.  This excludes
the nearest root of the larger factor; it deliberately does not claim that
all pairs `E_r,E_s` are coprime.

The revision turns that proof into an exact public-input algorithm:

```text
input: n, Q
R := Q
for s=n,n-1,...,2:
    while E_s divides R exactly in Z[y]:
        record s
        R := R/E_s
append n - sum(recorded orders) copies of 1
```

A false division by `E_s` into a product of smaller factors would force its
nearest root to occur in a smaller factor, contradicting the root lemma.
Therefore descending exact division recovers every non-isolated order and
its multiplicity.  Since `E_1=1`, the known total recovers isolates.

`verify_p145.py::recover_component_orders` takes only `(n,Q)`.  Across every
partition of every total through 30, the hidden partition is used only after
the routine returns, as the expected answer.  This replaces round 0's
known-factor divisions.

## Honest inverse boundary

Internal adjacency is invisible because the polynomial depends only on
component orders.  The verifier now constructs the actual edge sets and
labelled transition matrices for `P_4` and `K_4`; both exact characteristic
polynomials are `z^8-z^6`.

A starting orientation is not a marked input to a transition spectrum.  All
push orbits are affine cut-space cosets, and translation conjugates their
labelled kernels.  The paper states this as a category boundary rather than a
substantive reconstruction target.

Known `n` is essential in general: every positive-order edgeless graph has the
same one-state identity kernel and spectrum `{1}`.

## Exact evidence and limitations

The revised verifier uses integers and `fractions.Fraction` only.  It retains
complete graph controls through order five and return recurrences through time
six.  It adds 28,628 input-only recoveries, 624,834 exact candidate division
attempts, a real `P_4/K_4` adjacency witness, low-dimensional quotient checks,
and unknown-`n` edgeless witnesses.  It makes 155,901 exact assertions and
ends in `status=PASS`.

The former “strict root order” and “no-smaller collision” executable checks
were assertions of their hypotheses and have been deleted.  Code now claims
only exact squarefreeness checks through `s=30`; nearest-root ordering remains
an analytic proof obligation.  Finite controls are counterexample pressure,
not owner or novelty evidence.

No figure is needed.  External release, posting, submission, specialist
contact, and any novelty/priority decision remain unauthorized.
