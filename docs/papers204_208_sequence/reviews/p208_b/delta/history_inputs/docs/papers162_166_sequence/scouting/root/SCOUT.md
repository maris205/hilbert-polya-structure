# Root exact scout — reciprocal windows and semilattice erosion

**Date:** 2026-09-02 UTC  
**Historical boundary:** P1--P161 plus all retained and killed systems in the
P152--P161 sequence records  
**External state:** `HOLD_EXTERNAL`

## Outcome

Three literal systems were pursued past the pencil stage.  Two survived exact
falsification and enter the independent candidate gate; one is killed by a
strong internal tree-dynamics collision.

| handle | literal system | strongest exact result | gate |
|---|---|---|---|
| `RFW` | on `F_p^2`, `(x,y) -> (y,xy inv0(x+y))` | reciprocal conjugacy to the Fibonacci matrix off one singular projective orbit; exact transient polynomial, sharp rank-of-apparition clock, all-time every-target fibres, and complete Mobius cycle inventory | **`SELECT_GREEN_PENDING_HOSTILE_GATE`** |
| `CNG` | cyclic divisor tuples, `x_i -> gcd(x_i,x_(i+1))` | sliding-window iterates; longest-minimum-gap depth; transfer-matrix depth CDF; every-time target fibres; one-step image criterion | **`SELECT_AMBER_PENDING_MORPHOLOGY_SUBTRACTION`** |
| `RLR` | rooted labelled trees; move every current nonroot leaf directly to the root | depth `height-1`, bounded-height EGF and an every-target surjection fibre formula | `KILL_INTERNAL_P114_P148_TREE_ENGINE` |

The exact programs are finite counterexample pressure, not proofs and not
novelty evidence.  `RFW` made 2,425,108 assertions across nineteen odd primes;
`CNG` made 36,435 assertions across fourteen single-prime exponent boxes and
one two-prime product box.  Both transcripts end in `STATUS PASS`.

## `RFW`: reciprocal Fibonacci window

For an odd prime `p`, put `inv0(0)=0`, `inv0(a)=a^(-1)` for `a!=0`, and

```text
H_p(x,y)=(y,xy inv0(x+y)).
```

Let `F_0=0,F_1=1`, let

```text
z(p)=min{k>=1:p divides F_k},
A=[[0,1],[1,1]],
```

and let `O_p` be the projective `A`-orbit of `[1:0]`.  Its size is `z(p)`.
On the nonsingular torus, reciprocal coordinates `(u,v)=(x^(-1),y^(-1))`
give

```text
(u,v) -> (v,u+v)=A(u,v).
```

The line `u+v=0` is the singular exit; it maps to a coordinate axis and then
to `(0,0)`.  This yields the following candidate theorem ceiling.

1. The recurrent set is `(0,0)` together with the torus points whose
   reciprocal projective line is outside `O_p`.  Hence its size is

   ```text
   p^2-z(p)(p-1).
   ```

2. The maximum transient depth is exactly `z(p)-1`.  The depth polynomial is

   ```text
   p^2-z(p)(p-1) +(p-1)u+2(p-1)u^2
     +(p-1) sum_(d=3)^(z(p)-1) u^d.
   ```

3. Every one-step fibre is explicit.  For target `(a,b)` its size is

   ```text
   p,  if (a,b)=(0,0);
   0,  if a=0,b!=0;
   2,  if a!=0,b=0;
   0,  if a=b!=0;
   1,  otherwise.
   ```

   Thus the one-step image has `p^2-2p+2` states.

4. For every `t`, the sink fibre has size

   ```text
   1                                  t=0,
   p                                  t=1,
   1+min(t+1,z(p))(p-1)               t>=2.
   ```

   Every recurrent nonsink target has one `t`-source.  Each transient target
   lies on one of the explicit projective chains; the vertical-axis targets
   have no positive-time sources, a horizontal-axis target has two one-step
   sources and one source for `2<=t<=z(p)-2`, and a torus target of depth `d`
   has one source precisely for `t<=z(p)-1-d`.  This is an all-time,
   every-target fibre atlas, not only an image-size statement.

5. Put `nu_p(k)=nullity(A^k-I)` over `F_p`.  The fixed-point count is

   ```text
   Fix(H_p^k)=p^nu_p(k)-1_{A^k=I} z(p)(p-1).
   ```

   Therefore the number of cycles of exact length `ell` is

   ```text
   (1/ell) sum_(d|ell) mu(ell/d) Fix(H_p^d).
   ```

The proof has two visibly different components: a singular birational
completion of a linear recurrence, and a complete analysis of the finite
in-tree created by totalization.  Fibonacci periods/ranks and generic finite
rational-map background receive zero credit.

## `CNG`: cyclic neighbour-GCD

Fix `N=prod_j p_j^(e_j)` and `m>=2`.  On cyclic `m`-tuples of divisors of
`N`, set

```text
T(x)_i=gcd(x_i,x_(i+1)).
```

In the `p^e` exponent coordinate this is `a_i -> min(a_i,a_(i+1))`.  Hence

```text
T^t(a)_i=min_{0<=r<=t} a_(i+r).
```

For an exponent word `a`, let `rho(a)` be the longest cyclic run of entries
strictly above `min_i a_i`.  The point depth is

```text
tau(x)=max_(p^e || N) rho(a^(p)),
```

so the height is `m-1` and the fixed states are the constant divisor tuples,
numbering `tau(N)`.

For `q>=1`, let `B_(q,t)` be the `(t+1)`-state weighted run automaton: every
state has one transition to state zero (a minimum marker), and state `r<t`
has a transition of weight `q` to `r+1`.  The number of exponent words in
`{0,...,e}^m` of depth at most `t` is

```text
A_(e,m)(t)=1+sum_(q=1)^e trace(B_(q,t)^m).
```

The complete divisor-tuple CDF is the product of these terms over the prime
powers of `N`; exact layers are consecutive differences.

For a one-step exponent target `beta`, define

```text
M_b(r,s)=1_{min(r,s)=b},  0<=r,s<=e.
```

Then its fibre has size `trace(prod_i M_(beta_i))`.  Multiplication over the
prime powers gives every divisor target.  More generally, replacing states by
length-`t` contexts gives a finite de Bruijn transfer whose trace is the exact
time-`t` fibre for every target.  At one step, an exponent target is in the
image exactly when it has no strict cyclic local minimum; a canonical source
is `a_i=max(beta_(i-1),beta_i)`.

The sliding-minimum operator is a standard lattice erosion and receives zero
credit.  The only residual candidate contribution is the conjunction of the
finite cyclic depth distribution, divisor-product assembly, target-resolved
transfer atlas and exact local-minimum image test.  This makes `CNG` amber
rather than green until hostile threshold review.

## Killed tree candidate

`RLR` preserves the labelled vertex set while moving every old leaf directly
to the root, whereas P114 deletes leaves and P148 contracts alternating tree
levels.  Nevertheless its point clock is again height, its bounded-depth count
is the same classical rooted-tree height EGF, and its inverse proof is another
leaf-allocation inclusion--exclusion.  The update is literally different but
its entire theorem engine transfers from the occupied tree lane.  It is
therefore killed, not held as a reserve.

## Replay

```bash
PYTHONDONTWRITEBYTECODE=1 python3 docs/papers162_166_sequence/scouting/root/verify_rfw.py
PYTHONDONTWRITEBYTECODE=1 python3 docs/papers162_166_sequence/scouting/root/verify_cng.py
```

Frozen transcript SHA-256 values are

```text
RFW_CANONICAL.txt  85fcacb94fe19297f430973dc92f14893c56b1efa9fd045b9563260a5bc08097
CNG_CANONICAL.txt  b2bceec36a29464cac571004468106d49e1d5e922781a3335d32f2d233946667
```

