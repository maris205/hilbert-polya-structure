# C84 theorem package

Let `D` be a deletion set and `A=L\D`.  The pivot is `p=S9`.  The direction
blocks have sizes `(1,1,2,5)`:

```text
B1={S1}, B2={S16}, B3={S7,S15}, B4={S3,S4,S8,S11,S12}.
```

Write `I(D)={i:Bi subset D}`, `t(D)=|I(D)|`, and
`r(D)=max(0,t(D)-2)`.

## Theorem A: minimum-repair matroid

On ground set `D`, let `E_D` be the deleted labels outside the pivot and the
fully deleted blocks.  Define

```text
M_D = U_{0,E_D}
      direct-sum U_{1,{S9}} when S9 is deleted
      direct-sum Tr_{r(D)}(direct-sum_{i in I(D)} U_{1,Bi}).
```

Then the bases of `M_D` are exactly the minimum restoration witnesses for
`D`.  Consequently every minimum-witness family satisfies basis exchange.

**Proof.**  A full repair must restore `S9` when it is absent.  The retained
set already meets `4-t(D)` direction blocks, so it must restore one label from
each of exactly `r(D)` distinct fully deleted blocks.  Two labels from one
block do not create a second direction, hence cannot occur in a minimum
repair.  Conversely every such choice reaches two met directions and the
pivot.  These choices are precisely the bases of the displayed direct sum.

## Theorem B: ten templates and five graphs

With exchange adjacency `R~R'` when `|R triangle R'|=2`, the ten exact cells
are:

| `(rho,W)` | deletion sets | graph |
|---|---:|---|
| `(0,1)` | 30400 | `K1` |
| `(1,1)` | 30400 | `K1` |
| `(1,4)` | 1984 | `K4` |
| `(1,7)` | 192 | `K7` |
| `(1,8)` | 128 | `K8` |
| `(2,4)` | 1984 | `K4` |
| `(2,7)` | 192 | `K7` |
| `(2,8)` | 128 | `K8` |
| `(2,25)` | 64 | `L(K_{1,1,2,5})` |
| `(3,25)` | 64 | `L(K_{1,1,2,5})` |

Thus the aggregate support counts are `60800,3968,384,256,128` for
`K1,K4,K7,K8,L(K_{1,1,2,5})`, respectively.

**Proof.**  If `t<=2`, the direction rank is zero and there is one base.  If
`t=3`, the direction rank is one, so any two bases differ by exchanging their
unique direction label: the graph is complete on `W=4,7,8` vertices.  If
`t=4`, rank-two bases are pairs from distinct parts, hence are the edges of
`K_{1,1,2,5}`; single-element basis exchange is incidence in that graph, so
the exchange graph is its line graph.  The support counts follow from the six
dummy bits, the pivot bit, and the non-full block weights `2^s-1`.

## Theorem C: all-deleted extremal case

For `D=L`, every base is `{S9,x,y}` with `x,y` in two distinct direction
blocks.  There are

```text
1*1 + 1*2 + 1*5 + 1*2 + 1*5 + 2*5 = 25
```

such bases.  They equal, mask for mask, the 25 full-core-minimal triples
obtained by expanding C76's seven effective-label orbits.

The exchange graph `L(K_{1,1,2,5})` has 25 vertices, 128 edges, radius and
diameter 2, unordered distance spectrum `{1:128,2:172}`, and degree spectrum
`{9:10,10:10,13:4,14:1}`.

## Verification boundary

The independent checker reconstructs closure and verifies all 65536 basis
families plus 198912 ordered basis-exchange obligations.  The result is finite
and combinatorial.  It asserts no arithmetic/local data, Euler factors, root
numbers, automorphy, full Burnside ring/table of marks, or Hilbert--Polya
operator.  Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
