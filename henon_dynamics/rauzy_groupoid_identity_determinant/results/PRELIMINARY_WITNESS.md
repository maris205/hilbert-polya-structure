# HCS-C29 preliminary exact witness

## Proof-level relation

Using the frozen C25 fixed-fibre matrices:

```text
C1 = 0t  1b  (0t)^-1  0b  3t  (0b)^-1
```

is a closed primitive cyclically non-backtracking word with holonomy `I_4`.
The state sequence is `0,1,1,0,3,3,0`; `g_0t=g_0b=I_4`; and
`g_1b=g_3t^-1`.

A second exact word is

```text
C2 = 4t  (6b)^-1  6t  5b  (6t)^-1  6b.
```

With `P=g_4t`, `Q=g_6b`, `R=g_5b`, exact integer multiplication gives
`Q R Q^-1 P=I_4`.  The two rotation classes are distinct, and each is distinct
from its inverse class.  Their six cyclic starting positions therefore prove
`N_6>=24` without a word search.

## C26 induced-branch relation

For the frozen C26 matrices `B=AHA`, `C=AKA` and `Y=H^-1 K H`,

```text
K Y K = Y K Y
```

with common matrix

```text
[-1  0  0 -1]
[ 2  1  0  0]
[ 0  0  1 -1]
[ 2  0  0  1].
```

The common matrix has fourth power `I_4`.  The braid relation expands to a
free and cyclically reduced length-24 identity word in the actual C26 branch
alphabet `A,B,C`; it is not a proper power and its inverse is not a cyclic
rotation.  It therefore supplies at least 48 marked contributions to the
twenty-fourth unit-weight moment of the C26 symmetric return rose.

## Exploratory census -- not yet a release certificate

A one-off exact replay on the 28-arrow symmetric C25 graph gave the based
oriented identity-holonomy counts

```text
n:    1  2  3  4  5  6  7  8   9
N_n:  0  0  0  0  0 24  0 32 144
```

This suggests an identity-holonomy systole of six and exact `N_6=24`, but the
bounded census is not a theorem artifact until Phase 2 supplies an independent
checker and mutation tests.  The nonconstant determinant conclusion uses only
the explicit proof-level lower bound.
