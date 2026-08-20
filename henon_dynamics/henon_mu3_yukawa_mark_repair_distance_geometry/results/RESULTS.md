# C78 results

Canonical evidence (source-bound to the committed C73/C75/C76/C77 authorities):

```text
status: PREFREEZE_G3_PASS
evidence SHA-256: 728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae
C76 manifest SHA-256: 55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5
C77 manifest SHA-256: bcc3273b481123f89ed5bf10c216bcae7a2ac3ff77685edcba976ea959e84dbc
enumerated deletion sets: 65536
```

For a deletion set `D`, `A=L\\D` is retained and `rho(D)` is the minimum
number of deleted labels restored to make `A` generate `Q`.  The exact
structural formula is

```text
rho(D) = 1_{S9 in D} + max(0, t(D)-2),
```

where `t(D)` counts fully deleted blocks among
`[S1]`, `[S16]`, `[S7,S15]`, and `[S3,S4,S8,S11,S12]`.

## Distance marginal

| repair distance | number of deletion sets |
|---:|---:|
| 0 | 30400 |
| 1 | 32704 |
| 2 | 2368 |
| 3 | 64 |

Thus `rho <= 3`, and the counts sum to `65536`.

## Bivariate coefficient table

The polynomial is

```text
P(x,y) = sum_D x^|D| y^rho(D),
```

where `x` marks deleted labels.  Rows list coefficients of
`x^k y^0,...,x^k y^3`.

| deleted `k` | `y^0` | `y^1` | `y^2` | `y^3` | row total |
|---:|---:|---:|---:|---:|---:|
|0|1|0|0|0|1|
|1|15|1|0|0|16|
|2|105|15|0|0|120|
|3|455|105|0|0|560|
|4|1364|456|0|0|1820|
|5|2992|1375|1|0|4368|
|6|4950|3047|11|0|8008|
|7|6269|5116|55|0|11440|
|8|6095|6609|166|0|12870|
|9|4504|6595|341|0|11440|
|10|2461|5040|506|1|8008|
|11|940|2871|551|6|4368|
|12|224|1151|430|15|1820|
|13|25|289|226|20|560|
|14|0|34|71|15|120|
|15|0|0|10|6|16|
|16|0|0|0|1|1|

The row totals are `binomial(16,k)`, so `P(x,1)=(1+x)^16`.  Summing columns
gives `P(1,y)=30400+32704y+2368y^2+64y^3`.

## Closed form certificate

Let

```text
H(x,z) = product_{s in {1,1,2,5}}
          (sum_{d=0}^{s-1} binom(s,d)x^d + z*x^s).
```

After replacing `z^r` by `y^max(0,r-2)`,

```text
P(x,y) = (1+x)^6 (1+x*y) Transform(H).
```

The producer and SymPy checker agree coefficient-by-coefficient.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
