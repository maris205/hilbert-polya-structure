# Paper 33 source lock — SD-C35

## Frozen inherited object

For every integer `n >= 2`, retain exactly the Paper 32 state space

$$
X_n=P^1(\mathbb Z/n\mathbb Z)
$$

and the projective actions

$$
S[a:b]=[-b:a],\qquad R[a:b]=[-b:a+b],
$$

with the same cusp `c_n=[1:0]`, the same bidirectional cusp edges between
`n` and `2n/3n`, the same within-block roof `log n`, the same cross-edge roof
`log(max endpoint)`, and the same one-edge free marker `z`.

The only new candidate operation is a functorial chain quotient or twist of
this object.  No state, edge, block, or roof may be changed after arithmetic
classification.

## Frozen chain quotient

Over `Q`, let `V_n=Q[X_n]` and

$$
W_n=\operatorname{im}(I+P_{S,n})+
    \operatorname{im}(I+P_{R,n}+P_{R,n}^2),
\qquad M_n=V_n/W_n.
$$

Thus the `S^2` and `R^3` presentation circuits are removed before any
prime/composite label is computed.  Treat each cross pair as one oriented
one-cell and attach the square

$$
n\to2n\to6n\leftarrow3n\leftarrow n
$$

for every `n>=2`.  This removes every source-visible cusp diamond at chain
level; the nonexistent `n=1` block and its square are not inserted.

For the homology proof only, the incidence-dessin edge labelled by `c_n` may
be subdivided once so that a cross cell attaches at its midpoint.  This is an
auxiliary CW realization: it does not split or alter an inherited dynamical
edge, roof, transition, or marker.

## Allowed inputs

- the inherited full-shift semiring operations and congruence source;
- the inherited `X_n`, `S`, `R`, cusps, cross edges, roofs, and marker;
- rational cellular chains, boundaries, homology, orbit partitions, and
  source-functorial relabelling;
- fixed characters or supercharacters of the presentation group `C2*C3`,
  chosen before controls and extended trivially over cross multipliers;
- exact integer/rational/finite-field verification and SHA-256 provenance;
- independent post-census prime, prime-power, and mixed-composite labels.

## Forbidden inputs

- `|X_n|=n+1`, field status, primality, factorization, an Euler table, or any
  accepted-support table inside the quotient/twist/operator;
- deletion of composite blocks or insertion of a completed block projector;
- another residue system, another terminal verifier, or another family of
  dynamics;
- target zeros, coefficient fitting, zero matching, or Route B;
- a post-control character, sign, roof, cell, or projection;
- induction/first return or a replacement marker;
- calling an orthogonal compression an induced quotient operator when the
  relation subspace is not invariant;
- calling a scalar block identity determinant the determinant of the original
  graph-step dynamics.

## Frozen audit parameters

```text
moduli:                    2,...,192
coefficient field audit:  F_1000003 (characteristic avoids 2 and 3)
random C2*C3 controls:    64
random seeds:             330000,...,330063
matched relabel seed:     1003003+n
cross multipliers:        2 and 3
honest 1D characters:     all 6 characters of C6; word/norm semantics split
zero-superdimension:      all 15 differences; word/norm semantics split
analytic comparison:      Re(s)>2
target-zero data:         none
```

## Stop rule

Stop and close the whole semiring-residue family if any one of the following
holds:

1. the relation quotient is nonzero on prime powers or mixed composites;
2. a universal cusp or presentation-action control survives;
3. cancellation is functorial for arbitrary `C2*C3` actions rather than
   arithmetic-specific;
4. exact composite suppression is equivalent to the forbidden static field
   projector;
5. the original graph-step operator does not descend to the quotient with its
   original marker.

Paper 33 realizes conditions 1, 2, 3, and 5.
