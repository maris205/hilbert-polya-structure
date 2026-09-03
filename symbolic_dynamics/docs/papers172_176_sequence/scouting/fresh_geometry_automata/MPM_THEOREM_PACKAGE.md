# Minimum-pivot Mobius feedback: theorem package

**Handle:** `D02_MPM`  
**Decision:** `PROVISIONAL_AMBER / HOLD_EXTERNAL`  
**Scope:** a proved candidate package, not a novelty or priority claim

## 1. Literal system

Let `p` be prime and order the projective line as

```text
0 < 1 < ... < p-1 < infinity.
```

For `2 <= k <= p`, let `X_(p,k)` be the `k`-subsets of
`P^1(F_p)`.  Every such subset has a finite point.  For `S in X_(p,k)`, put

```text
a(S) = min(S intersect F_p)
g_a(x) = 1/(x-a),
```

with `g_a(a)=infinity` and `g_a(infinity)=0`, and define
`M(S)=g_(a(S))(S)`.  The coordinate order and the prime-field model are part
of the literal rule; the map is not claimed to be projectively natural.

Write

```text
Z = {S : infinity in S},
Y = {S : 0,infinity in S}.
```

## 2. Complete functional graph theorem

For every prime `p` and `2 <= k <= p`:

1. `im(M)=Z` and `im(M^2)=Y`.
2. A state is recurrent if and only if it lies in `Y`.
3. On `Y`, `M` fixes `0,infinity` and sends every `x in F_p^*` to
   `x^-1`.  Hence every recurrent period is one or two and `M^4=M^2`.
4. The exact depth layers are

   ```text
   depth 0: C(p-1,k-2),
   depth 1: C(p-1,k-1),
   depth 2: C(p,k).
   ```

   Thus the maximum tail is sharply two throughout the stated range.
5. Put `r=k-2`.  If `p` is odd, the number of fixed states is

   ```text
   F_(p,k) = [u^r] (1+u)^2 (1+u^2)^((p-3)/2).
   ```

   The number of 2-cycles is

   ```text
   (C(p-1,k-2)-F_(p,k))/2.
   ```

   For `p=2,k=2`, there is one recurrent state and it is fixed.

### Proof

The pivot always maps to infinity, so `M(S)` lies in `Z`.  Conversely, if
`R in Z`, then `g_0^-1(R)` contains zero and has pivot zero, so it maps to
`R`.  This proves `im(M)=Z`.

The only point mapped to zero is infinity.  Consequently a state outside
`Z` maps to `Z\Y`, a state in `Z\Y` maps to `Y`, and a state in `Y` has
pivot zero and stays in `Y`.  On `Y`, `g_0` is the involution
`x -> x^-1`.  This proves the image tower, recurrence statement, and the
pointwise depth criterion.  The three layer counts follow by choosing the
remaining points after requiring neither, exactly infinity, or both of
`0,infinity`.  Since `k<=p`, a `k`-subset avoiding infinity exists, so depth
two is attained.

For odd `p`, inversion on `F_p^*` has two singleton orbits `{1}` and `{-1}`
and `(p-3)/2` two-element orbits.  An invariant `r`-subset is a union of
these orbits, giving the displayed coefficient.  All other recurrent states
pair into 2-cycles.  For `p=2`, inversion fixes the sole nonzero point.

## 3. Every-target inverse and pivot mark

For a target `R`, define

```text
b(R) = max { y^-1 represented in {1,...,p-1} :
             y in R intersect F_p^* },
```

with empty maximum zero, and put `h(R)=p-b(R)`.

Then

```text
|M^-1(R)| = 0                         if infinity notin R,
|M^-1(R)| = h(R)                      if infinity in R,
sum_(S:M(S)=R) z^(a(S))
             = 1+z+...+z^(h(R)-1)     if infinity in R.
```

This is an every-target formula, including zero fibres, and the polynomial
recovers more than the functional graph census: it identifies the complete
set of possible feedback pivots.

### Proof

Fix `R` containing infinity.  A parent whose pivot is `a` is forced to be

```text
S_a = g_a^-1(R).
```

Besides the forced point `a=g_a^-1(infinity)`, every nonzero finite
`y in R` contributes the finite point

```text
a + y^-1 (mod p).
```

The proposed pivot is valid precisely when all these representatives are at
least `a`.  For `b in {1,...,p-1}`,

```text
(a+b mod p) >= a  iff  a < p-b.
```

Thus `a` is valid exactly for `0 <= a < p-b(R)`.  These forced parents are
distinct because they have distinct least finite points.  This proves both
the cardinality and marked formulas.  If infinity is absent from `R`, there
is no parent because every image contains infinity.

## 4. Boundary audit

- The theorem deliberately starts at `k=2`, so the exceptional singleton
  `{infinity}` never lacks a finite pivot.
- The upper bound `k<=p` is exactly what makes the depth-two layer nonempty.
  At `k=p+1` the full projective line is a separate degenerate fixed state and
  is outside the family.
- At the smallest prime, `(p,k)=(2,2)`, the three states have depths
  `0,1,2`, respectively; the core consists only of `{0,infinity}`.  The
  verifier checks this box explicitly.

## 5. Exact verification boundary

`verify_breadth.py` exhausts every state for

```text
p in {2,3,5,7,11,13},
2 <= k <= p for p<=7, and 2<=k<=5 for p in {11,13}.
```

For every state it checks closure, tail and period, and for every target it
checks the zero/nonzero fibre formula and the exact pivot set.  It also checks
the fixed/2-cycle coefficient formula.  These tests support the proof but do
not replace it.

## 6. Value and owner gate

The closest internal neighbours are P168 (span of inverses of subspaces),
P96 (finite subsets under an induced fixed map), and the P166 `SCD` negative
control (projection followed by a duality involution).  The present literal
map does not take spans, is not induced by a fixed base map, and its inverse
uses an order-threshold on the state-selected translation pivot rather than
Gaussian, Singer, or lattice-Mobius enumeration.  Therefore no complete
internal proof transfer was found.

The P166 `AQN` hostile gate is a closer architectural warning and is
subtracted explicitly.  It already kills the generic package "select a group
element from the current state, choose a section of a group quotient, and
then expose a classical group action," even when that package has an exact
clock and marked fibres.  Consequently MPM receives **zero credit** for
adaptive normalisation, projective inversion, or projection-to-recurrence as
such.  AQN's cyclic-difference quotient has constant `q`-point translation
fibres; it does not yield MPM's nested image conditions
`infinity in S`, then `{0,infinity} subset S`, nor the target-dependent pivot
interval `0<=a<p-b(R)`.  That remaining literal inverse law prevents a direct
proof-engine kill, but the collision rules out green status.

The weakness is real: the clock is only two, the recurrent action is ordinary
field inversion, and the order-dependent pivot is artificial enough that a
specialist may regard the package as theorem-thin.  Primary literature on
fixed Mobius dynamics and `PGL(2,p)` actions on projective-line subsets is
subtracted in `OWNER_SEARCH_LOG.md`.  The bounded literal non-hit is not
novelty evidence.  Status remains the lane's **unique provisional amber**
recommendation and `HOLD_EXTERNAL`; any demonstration that the threshold
fibre is a routine corollary of an owned adaptive-section framework is an
immediate kill.
