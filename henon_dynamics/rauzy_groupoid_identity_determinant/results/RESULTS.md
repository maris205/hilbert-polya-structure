# HCS-C29 Phase-2 results

## Executive result

The proposed escape from the C28 normalized-trace collapse splits into one
negative and one positive theorem.

- **Negative:** the genuine two-sided natural extension keeps the original
  positive periodic cocycle products, so its regular-group trace-log germ is
  still exactly one.
- **Positive:** a newly declared symmetric non-backtracking Rauzy path
  groupoid has nontrivial reduced kernel cycles.  Its dimension-normalized
  finite-Weil determinant converges on a common small disc to a nonconstant
  group-trace determinant germ.

The positive object is a changed dynamics.  It is not renamed as the AGY
natural extension.

## 1. Exact C25 cycles

The certificate reconstructs all fourteen positive arrows and their fourteen
formal inverses from the locked C25 graph.  It keeps the formal inverse of an
edge distinct from any antiparallel positive Rauzy arrow.  For example,
`0b^-1` retains positive-edge ID `0b` and is not the positive arrow `3b`.

Two primitive length-six identity-holonomy cycles are certified:

```text
C1 = 0t  1b  0t^-1  0b  3t  0b^-1
C2 = 4t  6b^-1  6t  5b  6t^-1  6b
```

Both are closed, cyclically non-backtracking, primitive, and distinct from
their inverse rotation classes.  They belong to distinct dihedral classes.
Their rotations and inverse rotations prove `N_6 >= 24`.

The independent exhaustive census through length nine sharpens this to

| Length `n` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| All marked identities `N_n` | 0 | 0 | 0 | 0 | 0 | 24 | 0 | 32 | 144 |
| Primitive marked identities | 0 | 0 | 0 | 0 | 0 | 24 | 0 | 32 | 144 |
| Primitive rotation classes | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 4 | 16 |
| Primitive dihedral classes | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 8 |

All and primitive counts are deliberately kept separate.  Their equality in
this small window is accidental: the exact repetition `C1^2` is a
nonprimitive length-twelve identity cycle and must enter the determinant
moment even though it does not enter the primitive census.

## 2. Exact C26 return relation

For the source-locked C26 matrices,

```text
B = A H A
C = A K A
Y = H^-1 K H
```

and exact rank-one algebra gives

```text
K Y K = Y K Y = Delta.
```

The common matrix is

```text
[-1  0  0 -1]
[ 2  1  0  0]
[ 0  0  1 -1]
[ 2  0  0  1]
```

with `Delta != I`, `Delta^2 != I`, and `Delta^4 = I`.

The producer forms the braid word, substitutes
`H=A^-1 B A^-1` and `K=A^-1 C A^-1`, and freely reduces.  The resulting word
in `A,B,C` has length 24, is primitive and cyclically reduced, evaluates to
the identity in both written-order and later-on-the-left path-order replays,
and is distinct from its inverse rotation class.  Thus

```text
N_24(C26 symmetric rose) >= 48.
```

This is a certified lower bound.  No total length-24 enumeration is claimed.
It proves that the full C26 branch subgroup is not free even though the
positive monoid remains free.

## 3. Determinant limit

For odd prime `p`, let `B_p` be the finite non-backtracking edge operator
twisted by the full `p^2`-dimensional finite Weil representation.  On the
zero-free norm disc define

```text
D_p^norm(u) = exp[p^(-2) Log_0 det(I-u B_p)].
```

At fixed path length, the normalized character tends to the identity-holonomy
indicator.  Since the C25 and C26 Hashimoto degrees are respectively 3 and 5,
the path traces have a prime-independent geometric majorant.  Therefore

```text
D_p^norm(u) -> exp[-sum_(n>=1) N_n u^n/n]
```

locally uniformly on `|u|<1/3` for C25 and `|u|<1/5` for C26.  On the common
disc `|u|<1/5`, both limits are nonconstant.  In particular,

```text
[u^6] log D_infinity,C25 = -4
[u^24] log D_infinity,C26 <= -2.
```

These are analytic germ statements.  The project does not claim an ordinary
infinite-dimensional Fredholm determinant, a positive Fuglede--Kadison
determinant, a global primitive Euler product, or continuation beyond the
stated discs.

## 4. Natural-extension control

The regular group trace extracts only identity cocycle products.  Every
nonempty positive C25/AGY word has nonidentity holonomy by the locked positive
monoid theorem.  Hence every positive regular trace moment vanishes and the
associated trace-log germ is exactly one.

A genuine natural extension changes one-sided coordinates into past-and-future
coordinates; it does not replace the forward cocycle with freely chosen
inverse letters.  The symmetric inverse-edge model is therefore a new finite
path dynamics, not a natural-extension theorem.

## 5. Arithmetic and Hilbert--Pólya assessment

What survived:

- exact primitive and repeated orbit bookkeeping;
- nontrivial identity-holonomy kernel at the C25 and C26 return levels;
- a canonical fixed-prime finite-Weil twist;
- an exact locally uniform normalized determinant limit;
- chronology and gauge invariance.

What did not appear:

- a prime-orbit correspondence or intrinsic `log p` clock;
- a von-Mangoldt amplitude law;
- a continuation or functional equation;
- a Riemann--von Mangoldt zero count;
- a xi divisor;
- an intrinsic positive reversible AGY roof;
- a two-sided nuclear/flat-trace operator theorem;
- a self-adjoint Hilbert--Pólya operator.

Accordingly, Phase 2 is a real algebraic/determinant advance but remains
`ROUTE_A_EXPLORATORY`; Route B is not authorized.

## 6. Reproducibility summary

- certificate SHA-256:
  `412840c37d2e474462b39ce7072614323023ac8e3f968bc16a9219cc3a0c0cca`;
- canonical payload SHA-256:
  `d3bde8d574b64fc146a9a65e1215654ee3516a20b3c07a4cb1f0a76ff0f2ab35`;
- independent report SHA-256:
  `f87ab0efb191be7ac68936c5eb25e95ba2dbfa2719614750c99f1934e918b215`;
- independent gates: `14/14 PASS`;
- tests: `38/38 PASS`;
- exact integer-inverse fuzz: `250/250 PASS`.

See `THEOREM_PACKAGE.md` for exact hypotheses, formulas, proofs and scope.
