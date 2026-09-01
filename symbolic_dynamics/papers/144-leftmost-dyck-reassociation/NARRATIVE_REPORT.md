# Narrative report: leftmost reassociation of Dyck components

**Status:** round-2 internally accepted anonymous theorem record;
**OWNER-THIN / HOLD_EXTERNAL**.
No claim of priority, originality, posting readiness, or external clearance is
made.

## One-sentence technical story

For the literal selector that repeatedly takes the leftmost ground-level comb
cover, the all-time iterate and the target-indexed suffix-lift inverse form one
exact temporal/fibre conjunction; every underlying move, tree graft, clock
statistic, and component census is separately treated as prior or standard.

## Literal system

Let `D_n` be the Dyck paths of semilength `n >= 1`.  Every nonempty path has
a unique primitive factorisation

```text
P = C_1 C_2 ... C_k.
```

Write `C_1 = U A D`.  The map is

```text
Phi(P) = P,                                  if k = 1,
Phi(P) = U A C_2 D C_3 ... C_k,              if k >= 2.
```

Thus the closing down-step of the first primitive component moves across the
second primitive component.  The atomic move and the underlying Tamari order
are background inputs, not contribution claims.

Under the standard contour bijection to rooted ordered plane trees, the
factors `C_1,...,C_k` encode the subtrees at the root children
`T_1,...,T_k`.  The update is exactly

```text
(T_1,T_2,T_3,...,T_k)
  -> (T_1 with T_2 appended as its rightmost child,T_3,...,T_k).
```

Thus the clock is root degree minus one.  For a terminal tree whose root has
one child, a depth-`d` inverse lifts the last `d` children of that child to
become root-level siblings.  The contour bijection and this graft/lift
rewriting are zero-credit representation-level inputs.

## Claim package and proof status

**Status: PROVABLE AS STATED.**  The frozen theorem contract survives without
extra assumptions for every `n >= 1`.

### Claim A: exact factor clock

If `P=C_1...C_k` and `C_1=UAD`, then for `0 <= t <= k-1`,

```text
Phi^t(P) = U A C_2 ... C_(t+1) D C_(t+2) ... C_k,
```

where an empty block of factors is omitted.  The displayed first component is
primitive because its interior is a Dyck path.  Its remaining suffix consists
of the untouched primitive factors.  Hence every nonfixed update reduces the
number of primitive factors by exactly one and

```text
tau(P) = k(P) - 1.
```

Fixed and recurrent paths are precisely the primitive paths.  Removing their
outer `U,D` gives a bijection with `D_(n-1)`, so there are `Cat_(n-1)` fixed
paths.  Since every primitive factor has positive semilength, `k(P) <= n`;
equality forces every factor to be `UD`.  Therefore the maximum depth is
`n-1`, uniquely at `(UD)^n`.

### Claim B: complete temporal layers

Let `C(z)` be the Catalan series.  A primitive path is `U A D`, so its
semilength series is `z C(z)`.  Paths with exactly `k` primitive factors have
series `(z C(z))^k`.  Therefore their number is

```text
[z^(n-k)] C(z)^k
  = k/(2n-k) * binom(2n-k,n),       1 <= k <= n.
```

For completeness, put `W=C-1`, so `W=z(1+W)^2`.  Lagrange inversion gives,
for `m>=1`,

```text
[z^m](1+W)^k
 = (k/m)[w^(m-1)](1+w)^(2m+k-1)
 = k/(2m+k) * binom(2m+k,m).
```

The case `m=0` equals one directly.  Substituting `m=n-k` gives the layer
formula.  Catalan, ballot, first-return, and generic generating-function
extraction are assigned zero contribution credit.

### Claim C: complete terminal depth-fibre atlas

Every endpoint is primitive.  Fix a primitive target

```text
T = U Q D,
Q = Q_1 Q_2 ... Q_r
```

with the primitive factorisation of its interior.  For every `0 <= d <= r`,
define

```text
P_d = (U Q_1 ... Q_(r-d) D) Q_(r-d+1) ... Q_r.
```

The first parenthesised word is primitive, and `P_d` has exactly `d+1`
primitive factors.  The iterate formula sends it to `T` in exactly `d`
steps.

Conversely, suppose `P=B_1...B_(d+1)` has endpoint `T`, with `B_1=UAD`.
Then `Q=A B_2...B_(d+1)`.  Because `A` is a Dyck path, its endpoint is a
return of `Q`; because every later `B_i` is primitive, uniqueness of primitive
factorisation forces `B_2,...,B_(d+1)` to be the last `d` factors of `Q`.
Thus `P=P_d`.  This proves both existence and uniqueness at every depth:

```text
sum_(P: Phi^infinity(P)=T) u^tau(P) = 1 + u + ... + u^r.
```

The ordinary fibre size is `r+1 <= n`.  Equality requires `r=n-1`, which
forces every `Q_i=UD`; hence `U(UD)^(n-1)D` is the unique target with `n`
basin states.

## Dependency map

1. Unique primitive factorisation makes the literal update and iterate
   formula unambiguous.
2. The iterate formula implies the exact factor drop, pointwise clock,
   recurrent classification, and endpoint formula.
3. Positive component semilength proves the unique sharp clock witness.
4. The standard Catalan functional equation plus Lagrange inversion yields
   the exact layer census.
5. Unique primitive factorisation of a fixed target's interior proves the
   depth-refined inverse atlas and its extremum.
6. The ordered-plane-tree conjugacy rewrites the same proof as a root-child
   graft followed by a suffix lift; it is explanatory background, not an
   additional residual claim.

No theorem in this dependency map requires the finite computation.

## Exact evidence

`verify_p144.py` exhausts all 290,511 Dyck paths of semilength `1..12` and all
82,500 fixed targets in that range.  It checks the literal update, closure,
factor drop, every closed-form iterate, pointwise clock, fixed count, every
temporal layer, the unique deepest path, every target-depth source, every
depth-fibre polynomial, and the unique maximum fibre.  The frozen run makes
6,005,502 exact assertions and ends in `STATUS=PASS`.

The computation is falsification pressure only.  It does not establish an
all-parameter statement, priority, or owner clearance.

## Ownership boundary

- Huang and Tamari own the associativity/Tamari lattice background.
- Bousquet-Mélou, Fusy, and Préville-Ratelle give a path formulation of
  Tamari-type covers; the atomic reassociation is therefore zero credit.
- Pallo's 2003 arm-restricted rotations and Chapoton's 2020 comparison identify
  the comb covers with the Tamari covers whose moved subpath is at height zero.
  The entire comb/height-zero correspondence is zero credit; the literal map
  only selects the leftmost available ground cover.
- Pallo's 2006 leftmost left-rotation is a direct deterministic-scheduler
  precedent with a rooted rotation tree, grading, and distance.  It is a
  genuinely different map: after its terminal root is fixed it has one fixed
  state, whereas `Phi_n` has `Cat_(n-1)` fixed states and hence cannot be its
  mirror/reversal conjugate for `n>=3`.  The general leftmost-scheduler idea is
  nevertheless zero credit.
- Panayotopoulos and Sapounakis explicitly study primitive decomposition of
  Dyck words and enumerate paths by their number of components; that entire
  census is zero credit.
- Stanley supplies standard Catalan/Dyck/plane-tree background.  The contour
  model, root-child graft, suffix lift, and root-degree clock are assigned zero
  standalone credit.

After those deductions, the residual is limited to the conjunction, for this
specific literal selector, of the closed all-time orbit and the targetwise
statement that each feasible depth has one specified source.  Its polynomial
and extremal consequences are retained only as consequences of that
conjunction.  This is an owner-thin bookkeeping residual, not an ownership or
novelty decision.  External circulation remains on hold.

## Scope and limitations

The note treats only this deterministic selector.  It does not classify other
Tamari schedules, compare all maximal chains, or claim that the residual
package is absent from the literature.  A direct owner of the repeated
literal selector or of the retained temporal/target-fibre conjunction would
require reframing or withdrawal before external use.
