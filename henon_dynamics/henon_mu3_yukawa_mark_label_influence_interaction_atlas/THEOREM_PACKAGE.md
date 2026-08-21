# C87 theorem package

## Frozen predicate

Let `L={S1,...,S16}`.  Define `F(A)=1` exactly when `A` contains `S9` and
meets at least two of

```text
B1={S1}, B2={S16}, B3={S7,S15}, B4={S3,S4,S8,S11,S12}.
```

The labels `S2,S5,S6,S10,S13,S14` are dummy coordinates.  Equivalently,
`F(A)=1` exactly when `A` contains one of the 25 C73 minimal generating
triples.  Exactly 30400 of the 65536 supports satisfy `F=1`.

## First-order atlas

For `i notin A`, set

```text
Delta_i F(A)=F(A union {i})-F(A),
c_i(k)=sum_{A subset L\{i}, |A|=k} Delta_i F(A).
```

The raw swing count is `sum_k c_i(k)`, the uniform Banzhaf influence is that
count divided by `2^15`, and the Shapley--Shubik value is

```text
sum_{k=0}^{15} c_i(k) k!(15-k)!/16!.
```

The nonzero coalition-size vectors are

```text
S1,S16: [0,0,8,59,196,390,521,494,339,166,55,11,1,0,0,0]
S7,S15: [0,0,7,52,175,355,486,473,332,165,55,11,1,0,0,0]
S3,S4,S8,S11,S12:
         [0,0,4,25,66,95,80,39,10,1,0,0,0,0,0,0]
S9:     [0,0,25,224,940,2461,4504,6095,6269,4950,2992,1364,455,105,15,1].
```

Thus `S9` has `(30400,475/512,271/360)`; `S1,S16` have
`(2240,35/512,61/1260)`; `S7,S15` have `(2112,33/512,2/45)`;
the five small-direction labels have `(320,5/512,31/2520)`; and all six
dummies have zero.  The triples list `(raw swing, Banzhaf, Shapley)`.
The total raw swing count is 40704, the Banzhaf sum is `159/128`, and the
Shapley sum is exactly one.

## Second-order atlas

For distinct `i,j` and `A subset L\{i,j}`, set

```text
Delta_ij F(A)=F(A union {i,j})-F(A union {i})-F(A union {j})+F(A).
```

Let `p_ij(k)` and `n_ij(k)` count `+1` and `-1` values among size-`k`
coalitions, and put `d_ij(k)=p_ij(k)-n_ij(k)`.  C87 uses

```text
B_ij = 2^-14 sum_k d_ij(k),
I_ij = sum_{k=0}^{14} d_ij(k) k!(14-k)!/15!.
```

All 120 pair rows occur in ten exact numerical classes:

| pairs | representative | positive | negative | `B_ij` | `I_ij` |
|---:|---|---:|---:|---:|---:|
| 75 | S1,S2 | 0 | 0 | 0 | 0 |
| 10 | S1,S3 | 64 | 256 | -3/256 | 0 |
| 4 | S1,S7 | 64 | 2048 | -31/256 | -5/84 |
| 2 | S1,S9 | 2240 | 0 | 35/256 | 31/168 |
| 1 | S1,S16 | 64 | 2176 | -33/256 | -11/168 |
| 10 | S3,S4 | 0 | 320 | -5/256 | -1/56 |
| 10 | S3,S7 | 64 | 128 | -1/256 | 1/168 |
| 5 | S3,S9 | 320 | 0 | 5/256 | 5/84 |
| 2 | S7,S9 | 2112 | 0 | 33/256 | 1/6 |
| 1 | S7,S15 | 0 | 2112 | -33/256 | -13/168 |

The canonical JSON retains the complete positive, negative, signed, and zero
counts by coalition size for every pair; the table is only the ten-class
projection.

## Faithful orbit theorem

The effective C76 label group has order 1920.  Its seven label orbits are

```text
{S1,S16}; {S2}; {S3,S4,S11,S12}; {S5,S6,S10,S13,S14};
{S7,S15}; {S8}; {S9}.
```

It has 27 orbits on unordered pairs, with orbit-size spectrum

```text
{1:5, 2:7, 4:7, 5:3, 8:1, 10:3, 20:1}.
```

Every first- and second-order row is constant on its corresponding faithful
orbit.  Equal numerical rows need not be in the same faithful orbit: for
example, `S8` has the same first-order values as `S3`, but lies in a separate
label orbit.  Likewise, 27 pair orbits compress to only ten numerical classes.

## Exact identities

The first-order Shapley values satisfy efficiency,

```text
sum_i phi_i = F(L)-F(empty)=1.
```

The pair Shapley index satisfies, for every label,

```text
sum_{j != i} I_ij = Delta_i F(L\{i})-Delta_i F(empty).
```

Only `S9` has endpoint contrast one; all other labels have zero.  Therefore
the sum over unordered pairs is `1/2`.  The unordered-pair Banzhaf sum is
`-119/256`; no Banzhaf efficiency statement is inferred from it.

The C82 distance-one ordered autocorrelation and the C87 monotone boundary
partition the sixteen outgoing cube edges from every true support.  Hence

```text
total_swing_count + C82_autocorrelation_by_distance[1]
= 40704 + 445696 = 16 * 30400 = 486400.
```

## Scope

These are exact finite Boolean-game and faithful permutation-action results.
They assert no arithmetic/local data, Euler factor, root number, automorphy,
full Burnside ring/table of marks, or Hilbert--Polya operator.  The scope
literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.
