# Focused-gate handoff: `BST` and `ORT`

**Decision:** advance exactly `BST` and `ORT`; no reserve.  No paper number is
assigned and external state is **HOLD_EXTERNAL**.

| finalist | selection-gate verdict | residual that may be tested as a contribution | immediate kill condition |
|---|---|---|---|
| `BST` | **`PASS_FOCUSED`** | complete four-stratum functional graph together with the nonuniform every-block source parametrization and codomain-wide `1/(N-2)/0` fibre law | an exact-map owner, or transfer of the same temporal-plus-fibre theorem from an occupied paper |
| `ORT` | **`PASS_FOCUSED_AMBER`** | anisotropic finite-field singular boundary, oriented right-angle depth split, sharp stable image, and codomain-wide fibre/image law | prior ownership of that singular/fibre package, or a focused finding that only the classical orthocentric identity remains |

All other fourteen breadth candidates have verdict **`KILL`**.  In
particular `CRE` is not a reserve.

## `BST` theorem contract

Let `V=F_2^r`, `r>=2`, `P=V\{0}`, and `N=2^r-1`.  Define

```text
x star y = x          if x=y,
             x+y      if x!=y,
S(a,b,c) = (b star c,c star a,a star b).
```

The focused theorem must prove all of the following as one package.

1. Diagonals and ordered distinct triples with `a+b+c=0` are fixed;
   exactly-two-equal triples have exact period three; every distinct triple
   with `a+b+c!=0` has depth one and lands at a fixed block.
2. Fixed points: `N^2`.  Strict three-cycles: `N(N-1)`.  Depth-one points:
   `N(N-1)(N-3)`.  Periodic/image size: `4N^2-3N`.  The stabilization height
   is zero for `r=2` and one for `r>=3`.
3. A target has fibre size one if diagonal or exactly-two-equal, `N-2` if an
   ordered block, and zero if a nonblock.  Consequently
   `zeta_S(z)=(1-z)^(-N^2)(1-z^3)^(-N(N-1))`.

### Proof skeleton to rederive

- Equality patterns are invariant except that a distinct nonblock becomes a
  distinct block.
- For distinct inputs the output is `(b+c,c+a,a+b)`, whose sum is zero.
- For a target block `(x,y,z)`, solve
  `b+c=x`, `c+a=y`, `a+b=z`.  Writing `a=t` gives
  `(a,b,c)=(t,t+z,t+y)`.  Exactly the three values `0,y,z` are forbidden, so
  the fibre has `(N+1)-3=N-2` elements.  This also proves the every-target
  statement independently of the orbit count.
- Count diagonals, ordered blocks, exactly-two-equal triples, and their
  complement.  Do not infer a proof from the enumerator.

### Owner/portfolio gate

Give zero credit to Steiner quasigroups, the `PG(r-1,2)` Steiner triple
system, and quasigroup cellular automata.  Re-search the exact ternary map and
all permuted-coordinate forms.  The closest internal systems are P153
(finite-plane shallow collapse) and P152 (triad language), but neither has
this literal update, fixed/three-cycle core, block-source parametrization, or
proof engine.  Current gate: **GREEN FOR FOCUSED AUDIT, NOT NOVELTY-CLEARED**.

## `ORT` theorem contract

Let `p=3 mod 4` be prime.  In `F_p^2` use the dot product `u dot v` and let
`X` be all ordered noncollinear triangles plus a sink `dagger`.  If `H` is the
orthocenter of `(A,B,C)`, define

```text
F(A,B,C) = (B,C,H)  if B,C,H are noncollinear,
             dagger otherwise,
F(dagger) = dagger.
```

Set

```text
T = p^2 (p^2-1)(p^2-p),
R = p^2 (p^2-1)(p-1),
Q = T-3R = p^2 (p^2-1)(p-1)(p-3).
```

The focused theorem must prove all of the following.

1. There are `R` triangles right-angled at each listed vertex, and the three
   classes are disjoint.  Nonright triangles have exact period four.
2. Right-at-first triangles have depth two.  Right-at-second and
   right-at-third triangles have depth one.  The sink is fixed.  Thus the
   stable image at time two has size `1+Q`, the maximum tail is sharply two,
   and `zeta_F(z)=(1-z)^(-1)(1-z^4)^(-Q/4)`.
3. The sink fibre has size `1+2R`.  A triangle right at its first or second
   listed vertex has fibre zero; one right at its third listed vertex or a
   nonright triangle has fibre one.  Hence `|F(X)|=1+T-2R`; the depth CDF at
   times `0,1,2` is `1+Q`, `1+T-R`, `1+T`.
4. The `p=3` boundary is explicit: `Q=0`, so the sink is the only recurrent
   state, while the height remains two.

### Proof skeleton to rederive

- `p=3 mod 4` makes `x^2+y^2` anisotropic.  This gives uniqueness of the
  altitude intersections, prevents two right angles in one noncollinear
  triangle, and makes a nonzero perpendicular vector linearly independent
  of the original vector.
- Choose the first vertex, a nonzero first side, and one of `p-1` nonzero
  perpendicular second sides to obtain `R`.
- For a nonright triangle, the four distinct points `A,B,C,H` are an
  orthocentric system; successive windows are
  `(A,B,C),(B,C,H),(C,H,A),(H,A,B)`.  For a right triangle, `H` is the
  right-angle vertex, which gives the oriented depths by direct substitution.
- A target `(A,B,C)` can only have predecessor
  `(H(A,B,C),A,B)`.  It is invalid exactly when the target is right at `A` or
  `B`.  It is valid for a nonright target and for a target right at `C`.
  This proves the fibre theorem without division by orbit counts.

### Owner/portfolio gate

The orthocentric four-point identity is classical and contributes nothing.
Wildberger already transports triangle geometry and orthocenters to finite
fields.  The only possible residual is the anisotropic singular boundary,
oriented depth split, and every-target fibre/image package.  P150 is the
closest internal threat because it also totalizes a finite-field rational map
and resolves its singular in-tree; the literal carrier, update, period, and
proof equations differ, but a focused collision review is mandatory.  Current
gate: **AMBER FOR FOCUSED AUDIT; KILL IF THE FINITE-FIELD SINGULAR PACKAGE IS
OWNER-COVERED**.

## Exact-control handoff

`verify_replacement.py` checks ranks `2,3,4` for `BST`, primes `3,7` for
`ORT`, fourteen killed controls, 40 boxes, and 575,833 assertions.  Two cold
runs must be byte-identical to `CANONICAL.txt`, with no bytecode cache.  These
checks are falsification pressure only.
