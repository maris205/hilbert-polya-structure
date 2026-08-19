# C73 theorem package

## Theorem 1: multipartite generation geometry

`S9` is the unique nonzero `Z/2` coordinate.  The active odd coordinates
fall into four projective direction blocks

```text
{S1}, {S16}, {S7,S15}, {S3,S4,S8,S11,S12}.
```

The dummy coordinates are `S2,S5,S6,S10,S13,S14`; `S2` is nonzero but lies
in the Frattini subgroup.  A support generates `8C` iff it contains `S9` and
meets at least two direction blocks.  Hence the non-isolated part of the
16-label minimal-generation hypergraph is the cone over `K_{1,1,2,5}` and has
25 edges; its six dummy labels are isolated vertices.

## Theorem 2: blocker geometry and deletion spectrum

There are exactly five minimal destructive deletion sets:

```text
{S9}
{S1,S7,S15,S16}
{S1,S3,S4,S8,S11,S12,S16}
{S1,S3,S4,S7,S8,S11,S12,S15}
{S3,S4,S7,S8,S11,S12,S15,S16}
```

Their polynomial is `b(x)=x+x^4+x^7+2x^8`.  There are 35136 destructive
and 30400 surviving deletion sets; the evidence records all size masses.

## Theorem 3: exact reliability

For independent equal deletion probability `q`,

```text
R(q)=(1-q)(1-q^4-q^7-2q^8+3q^9).
```

For heterogeneous deletions, let `Q_j` be the product of deletion
probabilities in direction block `j`.  Then

```text
R=(1-q9)(1-sum_j product_{k!=j} Q_k+3 product_j Q_j).
```

Dummy probabilities cancel exactly.

## Proposition: three robustness parameters

```text
unprotected worst-case tolerance:       0
worst-case tolerance with S9 protected: 3
maximum deletions with some survivor:   13 (25 supports)
```

The abstract hypergraph automorphism order is `345600`, but this is neither a
core-group automorphism claim nor a label-preserving symmetry claim.
