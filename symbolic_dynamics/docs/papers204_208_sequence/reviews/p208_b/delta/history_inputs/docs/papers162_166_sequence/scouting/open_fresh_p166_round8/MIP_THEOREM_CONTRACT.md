# Focused theorem contract — minimum inverse-position feedback (`MIP`)

**Candidate status:** `GREEN_OWNER_THIN / NEEDS_HOSTILE_GATE`  
**External status:** `HOLD_EXTERNAL`

## 1. Carrier and literal map

For `n>=1`, let `X_n=[n]^[n]` be the set of endofunctions, written with
labels `0,...,n-1`.  Define

```text
M(f)(i) = min {j : f(j)=i},   if i is in im(f),
          i,                  otherwise.
```

Thus the output coordinate indexed by a symbol records the first position of
that symbol in the source word, with the symbol itself as the missing-symbol
default.  No tie choice is hidden.

## 2. First image and component action

For every `g` in `im(M)`, the off-diagonal values

```text
{g(i) : g(i) != i}
```

are distinct.  Consequently each functional-digraph component of `g` is
either a directed cycle of length at least two, or a directed path ending in
a loop.  The condition is necessary but is not asserted sufficient; the
every-target formula below is the exact image test.

On a directed cycle, `M` reverses all arrows.  Write a loop-rooted path in
root-to-leaf order as

```text
(p_0,p_1,...,p_l),
g(p_0)=p_0,  g(p_j)=p_(j-1).
```

Then one update has the exact local form

```text
p_0 > p_1 : reverse the entire path;
p_0 < p_1 : split off p_0 as a fixed singleton and reverse the remaining path.
```

The map therefore acts componentwise after its first step.

## 3. Sharp clock and recurrent core

Every path either loses an endpoint within two steps or is already in a
two-cycle.  A nonsingleton path is recurrent precisely when

```text
p_0 > p_1   and   p_l > p_(l-1).
```

It is then exchanged with its reversal.  Cyclic components are exchanged
with their inverse orientations.  Hence every recurrent state has period one
or two.

A path on `s` labels needs at most `2s-2` steps to enter its recurrent form,
with equality only for a strictly decreasing root-to-leaf list.  Such a path
cannot use all `n` labels in a state of `im(M)`: every first-position vector
has some coordinate of value zero, while the full decreasing path has none.
It follows that an image state has tail at most `2n-3`, and an arbitrary state
has tail at most

```text
2n-2.
```

For `n>=2` the source

```text
(1,2,...,n-1,1)
```

maps to `(0,0,1,...,n-2)`, the increasing root-to-leaf path, and has depth
exactly `2n-2`.  For `n=1` the unique state is fixed and the height is zero.

## 4. Recurrent census, fixed census, and zeta

On a fixed `s`-label set, recurrent connected components number

```text
c_1 = 1,
c_2 = 1,
c_3 = (3-1)! + 2 = 4,
c_s = (s-1)! + s!/4,   s>=4.
```

The first term for `s>=2` is a directed cycle.  The path contribution is two
at size three; for `s>=4`, the two independent endpoint inequalities select
one quarter of all linear orders.  Therefore, if `R_n` is the number of
recurrent states,

```text
sum_(n>=0) R_n x^n/n!
 = 1/(1-x) * exp(x^3/3 + x^4/(4(1-x))).
```

The sequence begins

```text
R_0,...,R_7 = 1,1,2,8,38,220,1540,12460.
```

A state is fixed exactly when every component is a singleton or a directed
two-cycle.  Thus its fixed count `I_n` is the involution number,

```text
sum I_n x^n/n! = exp(x+x^2/2),
I_1,...,I_7 = 1,2,4,10,26,76,232.
```

For every positive iterate `k`,

```text
Fix(M^k) = I_n  if k is odd,
           R_n  if k is even.
```

Equivalently the dynamical zeta function is

```text
zeta_n(z)=(1-z)^(-I_n) (1-z^2)^(-(R_n-I_n)/2).
```

## 5. Every-target one-step fibre

Fix a target `g in X_n`.  Put

```text
U = {i : g(i) != i}.
```

If the values `g(i)`, `i in U`, are not distinct, the fibre is empty.  Assume
they are distinct, and let

```text
F = {i : g(i)=i and i notin g(U)}.
```

For `A subseteq F`, define the set of symbols declared present by
`P_A=U union A`, and their proposed first positions by

```text
r_A(i)=g(i) for i in U,
r_A(i)=i    for i in A.
```

Write `R_A={r_A(i):i in P_A}`.  Then the exact fibre is

```text
|M^(-1)(g)|
 = sum_(A subseteq F)
     product_(0<=j<n, j notin R_A)
       #{i in P_A : r_A(i)<j}.
```

An empty choice factor makes that summand zero.  This formula also decides
the exact first image: `g` is supported iff the displayed sum is positive.

Proof route: `i in U` must occur first at `g(i)`; a fixed coordinate either
occurs first at its own position or is absent.  Once those first occurrences
are chosen, every unforced word position may contain exactly one of the
symbols already opened.  Multiplication gives the summand and summing over
the fixed-symbol choices gives the fibre.

For a fixed kernel partition of a source, the target forces all block labels,
so at most one source per set partition can lie over a target.  Hence every
fibre is at most the Bell number `B_n`.  Equality holds over the identity:
label each block by its least element.  The maximum fibres through `n=7` are

```text
1,2,5,15,52,203,877.
```

## 6. Required hostile gates

Before any manuscript:

1. independently prove the `2n-3` image-tail bound, including the equality
   characterization used above;
2. rederive the path census at sizes `1,2,3` and the endpoint-independence
   step for `s>=4`;
3. attack the fibre formula on unsupported targets and all missing/present
   fixed-coordinate collisions;
4. search canonical generalized inverses, ordered transversals, first-
   occurrence transforms, and finite transformation semigroup dynamics for
   the exact literal iteration; and
5. attack the internal relation
   `KRR(f)(j)=M(f)(f(j))` and the P143/DFJ/P105/P115 neighbourhood.

Promotion ceiling is `GREEN_OWNER_THIN`, never a public novelty claim.

