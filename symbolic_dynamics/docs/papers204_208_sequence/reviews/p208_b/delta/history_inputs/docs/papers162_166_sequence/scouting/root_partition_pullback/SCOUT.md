# Endpoint-duplicating pullback dynamics on set partitions

**Handle:** `EDP`  
**Final candidate decision:** `KILL_GENERIC_PULLBACK_RBELL_AND_P110_COLLISION`  
**External status:** `HOLD_EXTERNAL`

## Outcome first

Let `Pi_n` be the set of partitions of `[n]`, written as equivalence
relations.  Fix the endpoint-duplicating predecessor map

```text
p(1)=1,                    p(i)=i-1  (2<=i<=n),
```

and define the literal self-map

```text
x ~_(T pi) y    iff    p(x) ~_pi p(y).                       (1)
```

Thus `T` is the pullback of an equivalence relation along one fixed,
nonbijective transformation.  Unlike P110, no translate-meet or
translate-join is taken.  The early anomaly is that this nonmonotone map has
a completely rigid Bell staircase of images and a target-resolved inverse
polynomial although its source partition may gain and lose individual
relations.

The author verifier checks every partition through `n=8`, including every
time through stabilization and every coefficient of every target fibre:
`182,323` assertions, two byte-identical replays, `STATUS PASS`.

## 1. Closed iterate and Bell staircase

Put `p^t(i)=max(1,i-t)` and `h=min(t,n-1)`.  Functoriality of pullback gives

```text
x ~_(T^t pi) y    iff    p^t(x) ~_pi p^t(y).                 (2)
```

Consequently a target `eta` occurs at time `t` if and only if

```text
1 ~_eta 2 ~_eta ... ~_eta h+1.                              (3)
```

Deflating those `h+1` labels to a single first label is a bijection from the
time-`t` image to `Pi_(n-h)`.  Hence

```text
|im T^t| = Bell(n-h).                                       (4)
```

The only recurrent state is the indiscrete partition.  In particular the
Artin--Mazur zeta function of this finite map is `(1-u)^(-1)`.

## 2. Exact depth layers and sharp clock

For `pi` nonindiscrete, let `m(pi)` be the largest `m<n` for which
`1,...,m` lie in one block of `pi`.  Equation (2) gives the point depth

```text
D(pi)=n-m(pi),                                                (5)
```

while the indiscrete partition has depth zero.  Contracting the initial
block segment shows

```text
#{pi:D(pi)=0}=1,
#{pi:D(pi)=t}=Bell(t+1)-Bell(t)       (1<=t<=n-1).            (6)
```

Thus the maximum depth is sharply `n-1`; every layer is nonempty, and the
telescoping sum in (6) recovers all `Bell(n)` states.  This temporal law is
not inferred from the verifier.

## 3. Every-time, every-target two-variable fibres

Assume (3), put `b=#blocks(eta)`, and let

```text
a = |block_eta(1)|-h.
```

The quantity `a` is the size of the distinguished block after deflation.
Mark the number of source blocks by `z` and the size of the source block
containing `1` by `u`.  With

```text
B_j(z)=sum_(k=0)^j {j choose k}_2 z^k
```

the ordinary Bell polynomial (braces denote Stirling numbers of the second
kind), the complete source fibre is

```text
Phi_(t,eta)(z,u)
 = z^b u^a sum_(j=0)^h binom(h,j) B_j(z) (u+b-1)^(h-j).      (7)
```

If (3) fails, the polynomial is zero.  Formula (7) includes `t=0`, `n=1`,
the indiscrete target, all post-stabilization times, and every block/root-size
coefficient.

Indeed, the final `h` source labels are invisible to `p^h`.  Choose `j` of
them to form blocks disjoint from the retained prefix, partition those labels
(giving `B_j(z)`), and attach every remaining label either to the
distinguished old block (weight `u`) or to one of the other `b-1` old blocks.
This is a direct labelled construction, not a fitted identity.

At `z=u=1`, every supported target with `b` blocks has fibre

```text
sum_(j=0)^h binom(h,j) b^(h-j) Bell(j),                      (8)
```

the `b`-Bell number.  For `n>=2`, one-step indegree is `b+1` (for `n=1` it
is `1`), while the fully stabilized fibre of the sole terminal target is
`Bell(n)`.

## 4. Separation and claim ceiling

The three proof pieces are: composition of a noninjective predecessor,
initial-segment depth contraction, and an extension-of-a-fixed-partition
construction.  Classical pullback functoriality and Bell/r-Bell enumeration
receive no novelty credit.  The residual candidate package is only their
conjunction for the literal endpoint-duplicating self-map: the Bell image
staircase, exact depth layers, and the target-resolved `(blocks,root-size)`
fibre polynomial.

The closest internal paper is P110, but P110 repeatedly joins cyclic
translates on the same lattice, has a divisor-indexed fixed atlas and sharp
height `n-2`; EDP pulls back along a nonbijective rooted-chain map, has one
recurrent state, height `n-1`, and r-Bell extension fibres.  P143 acts on all
Boolean relations through row inclusion and preorder transposition, not on
partitions by pullback.  These distinctions must be rechecked independently;
same carrier alone is not being presented as novelty.

No claim is made to priority, freedom to operate, or external novelty.  A
bounded search found standard sources for inverse-image partitions and for
r-Stirling/r-Bell numbers, but no direct source for (1) together with
(2)--(8).  That is only a search non-hit.

## 5. Exact evidence and replay

Run

```bash
python3 docs/papers162_166_sequence/scouting/root_partition_pullback/verify_scout.py
```

The script constructs restricted-growth partitions independently, applies
the literal relation pullback, and checks the closed iterate, fixed locus,
sharp point depths, every image, the unweighted r-Bell count, and every
coefficient of (7).  Frozen receipts:

```text
verifier sha256  37efac83306f8172b4996ccfa4a9ec798b8b2a18928fe948b4ad0a3dc363d1ff
canonical sha256 5ad8c27c8da48598495491a8eb894af40e7c4917427ba96282d05878cbca185c
fresh replay 1   5ad8c27c8da48598495491a8eb894af40e7c4917427ba96282d05878cbca185c
fresh replay 2   5ad8c27c8da48598495491a8eb894af40e7c4917427ba96282d05878cbca185c
py_compile       PASS
```

## Final candidate gate

```text
EDP       KILL_GENERIC_PULLBACK_RBELL_AND_P110_COLLISION
MATH      PASS_AUTHOR_EXACT
EXTERNAL  HOLD_EXTERNAL
```

The independent gate found no mathematical failure in (1)--(8), apart from
the now-corrected `n=1` wording above.  It nevertheless showed that generic
equivalence-relation pullback plus marked r-Bell extension owns both main
engines; after subtraction, the remaining prefix-depth observation collides
too strongly with P110 on the same carrier.  EDP therefore receives no paper
slot.
