# Open P166 finite-algebra scout

**Decision:** `KILL_ALL`  
**External status:** `HOLD_EXTERNAL`  
**Paper action:** none; no theorem contract is promoted.

This scout opened a Route-A lane disjoint from P158 and tested natural finite
systems on matrices, permutations, and extension-field codes.  Three maps
survived the desk screen.  Each has exact mathematics; none clears the combined
owner, portfolio-collision, and theorem-mass gate.

## 1. UTAS: upper-triangular Artin--Schreier dynamics

Let `B_n` be the algebra of upper triangular `n x n` matrices over `F_2`, and
let `J_n` be its strictly upper triangular radical.  The literal update is

```text
Phi(A) = A + A^2.                                      (1.1)
```

### 1.1 Exact reduction and clock

The diagonal of `A+A^2` is zero, so `Phi(B_n)` is contained in `J_n`.  For
`Y in J_n`, put

```text
g(Y) = Y + Y^2 + Y^4 + Y^8 + ... ,                    (1.2)
```

where the sum terminates by nilpotence.  Then `g(Y)+g(Y)^2=Y`.  Hence

```text
Phi(B_n)=J_n,
Phi|_(J_n) is a permutation with inverse g.             (1.3)
```

On one element `N in J_n`, all its powers commute.  If `t>=0`, the binomial
theorem and Lucas parity give the pointwise iterate

```text
Phi^t(N) = sum_(j subset_bits t) N^(2^j).               (1.4)
```

In particular,

```text
Phi^(2^s)(N) = N + N^(2^(2^s)).                         (1.5)
```

If `h(N)=min{m>=1:N^m=0}`, the exact period of `N` is the smallest `2^s`
such that

```text
2^(2^s) >= h(N).                                        (1.6)
```

The convention includes `h<=2`, for which the period is one.  Every element
of `J_n` is recurrent; every element of `B_n\J_n` has tail exactly one.  The
largest core period is therefore the smallest `2^s` with `2^(2^s)>=n`, and a
single nilpotent Jordan chain attains it.

This is a genuine double-logarithmic period anomaly, but not a nontrivial
transient theorem.

### 1.2 Every-target fibre: exact bijection, failed closed census

For `Y in J_n`, let

```text
E_Y = {E in B_n : E^2=E and EY=YE}.
```

There is an exact bijection

```text
Phi^(-1)(Y)  <-->  E_Y,
A             |->  A+g(Y),
g(Y)+E        <--|  E.                                  (1.7)
```

Indeed `Y` is a polynomial in `A`, so a source `A` commutes with `Y` and with
`g(Y)`; characteristic two then makes `A+g(Y)` idempotent.  Conversely a
commuting idempotent cancels from `(g+E)^2+(g+E)`.

Two sharp targets follow:

- at `Y=0`, every triangular idempotent is allowed, so

  ```text
  |Phi^(-1)(0)| = sum_(k=0)^n binom(n,k) 2^(k(n-k));     (1.8)
  ```

- for the regular nilpotent Jordan chain `J`, its centralizer is the local
  polynomial algebra `F_2[J]`, whose only idempotents are zero and one, so
  `|Phi^(-1)(J)|=2`.

Equation (1.7), however, is not a closed all-target count.  It transfers the
hard part to idempotents in an arbitrary triangular centralizer.  The exhaustive
fibre spectra already fragment rapidly:

```text
n=3: 2^2, 6^4, 10^1, 26^1
n=4: 2^12, 6^16, 10^16, 18^2, 26^12, 42^4, 66^1, 162^1
n=5: 16 different fibre sizes, from 2 through 1442.
```

Here `a^b` means `b` targets have fibre size `a`.

### 1.3 UTAS gate

The fixed points are precisely the square-zero strictly triangular matrices,
a separately studied enumeration.  Triangular idempotents are also directly
enumerated in the literature.  After subtracting those strata, the residual is
a tail-one entry into functional-calculus power dynamics, with (1.7) not an
evaluated every-target atlas.  It is also too close to P102's power core and to
the matrix-algebra territory already occupied by P103/P119.

**UTAS: `KILL_OWNER_DENSE_WEAK_INVERSE`.**

## 2. RTCD: reversal-twisted coboundary dynamics

Let `w=w_0` be the reversal involution in `S_n`, with
`r=floor(n/2)` transpositions.  Define

```text
Theta(pi)=w pi w,
T(pi)=pi^(-1) Theta(pi)=pi^(-1) w pi w.                 (2.1)
```

This was the strongest mathematical signal in the lane.

### 2.1 Exact image and first fibres

Set `H=C_(S_n)(w)`, so

```text
|H| = 2^r r!.                                           (2.2)
```

The first image is

```text
Omega_n={y in S_n : y w is conjugate to w}.             (2.3)
```

The equation `T(pi)=y` is equivalent to
`pi^(-1)w pi=yw`.  Thus every supported target has exactly `|H|` sources,
every unsupported target has none, and

```text
|Omega_n| = n!/(2^r r!).                                (2.4)
```

This is orbit--stabilizer, not a residual theorem by itself.

### 2.2 Collapse to the `-2` power map

Every `y in Omega_n` satisfies

```text
Theta(y)=y^(-1),
T(y)=y^(-2),
T^k(y)=y^((-2)^k).                                      (2.5)
```

Let `ord(y)=2^a m` with `m` odd.  Then a point already in `Omega_n` has
tail `a` and eventual period `ord_m(-2)`.  For an arbitrary `pi` outside
`Omega_n`, put `y=T(pi)`; its tail and period are

```text
depth(pi)=1+v_2(ord(y)),
period(pi)=ord_(oddpart(ord(y)))(-2).                   (2.6)
```

Inside `Omega_n`, remove the initial `1+` and use `pi` itself.  The recurrent
set consists exactly of the odd-order elements of `Omega_n`.

The maximum tail is

```text
D_n = 0                              (n=1),
D_n = 1+floor(log_2 floor(n/2))      (n>=2).             (2.7)
```

The upper bound follows because all even cycle lengths below are parts of a
partition of `r`.  A part equal to the largest power of two not exceeding `r`
gives equality; a non-Cartan source over that matching supplies the initial
level.

### 2.3 Matching partition census

Write

```text
z_lambda = product_i i^(m_i(lambda)) m_i(lambda)!,
W_r(lambda)=2^(r-ell(lambda)) r!/z_lambda.              (2.8)
```

If `n=2r`, the union of the fixed matching `w` and the matching `yw` is a
disjoint union of alternating cycles.  Their half-lengths form
`lambda partition r`; exactly `W_r(lambda)` targets have this type, and their
orders are `lcm(lambda)`.

If `n=2r+1`, the union also has one alternating path.  If that path uses `s`
fixed-matching edges, it contributes one `(2s+1)`-cycle to `y`; the remaining
half-lengths form `lambda partition r-s`.  For each pair `(s,lambda)`, again
exactly `W_r(lambda)` targets occur, now with order
`lcm(2s+1,lambda)`.

For `k>=1` put

```text
M_k=|(-2)^k-1|.                                         (2.9)
```

Every point fixed by `T^k` lies in `Omega_n`.  Therefore

```text
F_k(2r) = sum_[lambda partition r; each part divides M_k] W_r(lambda),

F_k(2r+1)
 = sum_[0<=s<=r; 2s+1 divides M_k]
     sum_[lambda partition r-s; each part divides M_k] W_r(lambda).   (2.10)
```

The number of cycles of exact length `k` is

```text
C_k=(1/k) sum_(d|k) mu(k/d) F_d.                        (2.11)
```

The verifier checks (2.3)--(2.11) over every permutation through `n=8` and
for `k=1,...,12`.  For example, at `n=7` the recurrent cycle inventory is

```text
15 fixed points, 6 cycles of length 4, 8 cycles of length 6.
```

### 2.4 RTCD gate

The fatal problem is structural, not computational.

1. The map `g -> g^(-1)Theta(g)`, its quotient by the fixed subgroup, and the
   condition `Theta(y)=y^(-1)` are the classical symmetric-space/Cartan
   embedding package.
2. The matching carrier is the standard `S_(2r)/H_r` perfect-matching Gelfand
   pair, and its orbitals are already indexed by the same partitions used in
   (2.8).
3. Most decisively, P102 already uses the full proof skeleton “involution map
   lands in an involution-defined locus; later iterates are a scalar power map;
   derive fixed counts, Mobius cycle counts, sharp depth, and recovery.”  RTCD
   changes commutative Fourier blocks to matching coset types and changes `+2`
   to `-2`, but does not supply an independent engine.
4. The only general positive-time target formula left after (2.3) is

   ```text
   |(T^t)^(-1)(z)|
    = |H| #{y in Omega_n : y^((-2)^(t-1))=z},           (2.12)
   ```

   which is an exact reduction, not a closed target-resolved atlas.

The P102 collision alone is fatal under the present hard intake rule.

**RTCD: `KILL_INTERNAL_P102_PROOF_ENGINE`.**

## 3. SCD: subfield-core duality on codes

Let `K=F_(q^2)`, `F=F_q`, and let the carrier be all `K`-linear codes
`C<=K^n`.  Define the Galois interior

```text
I(C)=span_K(C cap F^n)                                  (3.1)
```

and use the ordinary Euclidean dual over `K`:

```text
T(C)=I(C)^perp.                                         (3.2)
```

### 3.1 Complete dynamics

The image `I(C)` is Galois invariant.  Galois-stable codes are precisely scalar
extensions of `F`-codes, and their duals are stable.  Consequently

```text
T^2(C)=I(C),
T^3(C)=T(C).                                            (3.3)
```

The one-step image and the recurrent set are both the stable codes.  A stable
code lies in a duality cycle of length one or two; every nonstable code has
tail one.  The image size is the Grassmann number

```text
G_n(q)=sum_(k=0)^n [n choose k]_q.                      (3.4)
```

### 3.2 Closed every-target fibre

Define

```text
A_m(q)=sum_(j=0)^m (-1)^j q^(binom(j,2))
                    [m choose j]_q G_(m-j)(q^2).        (3.5)
```

This counts `K`-subspaces of `K^m` containing no nonzero `F`-rational point.
It is ordinary Mobius inversion on the `F`-subspace lattice.

For a stable target `D_K` of dimension `k`, quotienting a source by
`D_K^perp` gives exactly such a rational-point-free subspace of `K^k`.  Hence

```text
|T^(-1)(D_K)|=A_k(q);                                   (3.6)
```

all nonstable targets have fibre zero.  The mass identity is

```text
sum_(k=0)^n [n choose k]_q A_k(q)=G_n(q^2).             (3.7)
```

For `q=2`, the first values are `A_0,...,A_4=1,1,3,15,183`, exactly as found
by exhaustive enumeration of all `F_4` codes through length four.

### 3.3 SCD gate

This is the cleanest inverse formula of the lane, but the dynamics are exactly
a forbidden construction: an idempotent Galois-interior projection followed by
classical duality.  The relations `T^2=I` and `T^3=T` expose rather than cure
that defect.  Delsarte's trace/subfield duality, Galois invariance, and explicit
Galois closure/interior operators are direct background.  Formula (3.5) is a
subspace-lattice Mobius count attached to the one-step projection.

**SCD: `KILL_ONE_STEP_GALOIS_INTERIOR`.**

## 4. Verification and final decision

`verify_scout.py` is self-contained.  It checks:

- all `46,233` permutations through `S_8`, matching image/fibres, pointwise
  depth/period, partition weights, twelve fixed iterates, and Mobius cycles;
- all `33,866` binary upper triangular matrices through order five, all core
  iterates through time seven, every target's commuting-idempotent fibre, and
  both fibre extremes;
- all `582` `F_4`-linear codes through length four, literal Galois interior and
  orthogonal complement, every target, (3.3), (3.5), and (3.7).

The frozen run contains **270,398 exact assertions** and three deterministic
state-table fingerprints.  Two fresh executions were required to match the
canonical transcript byte for byte.

No candidate survives the hard gate.  In particular, the mathematically
strongest candidate is not retained as a reserve merely to fill P166.

**Final decision: `KILL_ALL`.  External circulation remains `HOLD_EXTERNAL`.**
