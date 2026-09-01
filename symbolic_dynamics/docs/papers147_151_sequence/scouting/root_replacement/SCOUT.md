# ARC replacement scout: adjacent-run consolidation of compositions

**Stage:** P147--P151 replacement discovery.  **Status:** `HOLD_EXTERNAL`.

This note records a literal finite self-map, its theorem contract, exact
falsification pressure, and its ownership boundary.  It is not a novelty
certificate and does not by itself allocate a paper number.

## 1. Literal system and first signal

Let `Comp(n)` be the positive integer compositions of `n`.  For every maximal
run

`(...,s,s,...,s,...) = (...,s^r,...)`,

replace the whole run simultaneously by its sum `rs`.  Write the resulting
self-map as `A_n`.  For example,

`(1,1,2,4) -> (2,2,4) -> (4,4) -> (8)`.

The first exhaustive boxes did not merely show termination.  They showed a
sharp logarithmic clock for every carrier size, together with a divisor-path
description of every one-step fibre.  These are independent temporal and
inverse axes.

## 2. Proposed theorem contract

For every `n>=1`:

1. `A_n` preserves total weight and strictly decreases the number of parts
   away from a fixed point.  Its fixed points are exactly the Carlitz
   compositions: adjacent parts are unequal.
2. Every orbit is absorbed and

   `max_{alpha in Comp(n)} tau(alpha) = floor(log_2 n)`.

   This equality holds for every `n`, not only for powers of two.
3. Put `t=floor(log_2 n)`, `r=n-2^t`, and

   `C_t=(1,1,2,4,...,2^(t-1))`.

   If `r=0`, use `C_t`; if `r=2^(t-1)`, use `(r,C_t)`; otherwise use
   `(C_t,r)`.  This gives an explicit depth-`t` witness (with the evident
   singleton convention at `n=1`).
4. If the target is `beta=(b_1,...,b_k)`, define

   `Phi_beta(u) = sum u^(sum_i b_i/s_i)`,

   where the sum is over `s_i|b_i` with `s_i != s_(i+1)` for every adjacent
   pair.  Then `[u^ell]Phi_beta(u)` is exactly the number of one-step
   predecessors of `beta` having `ell` parts.  Thus `Phi_beta(1)` is the full
   one-step fibre, and `beta` belongs to the image exactly when this
   divisor-path polynomial is nonzero.

The fixed-point ordinary generating function is

`1 / (1 - sum_{j>=1} x^j/(1+x^j))`.

That fixed census is classical Carlitz-composition input and receives zero
credit.  It is kept in the contract only so the complete finite functional
graph has an auditable recurrent census.

## 3. Proof spine

### Termination and the upper clock

Every nonfixed step replaces at least one run of length at least two, so the
number of parts strictly falls.  To see the stronger clock, follow a part
created at the last nontrivial round backward.  A run present for the first
time at round `j` must contain a part whose value changed at round `j-1`;
otherwise the same adjacent equal run already existed and would have been
collapsed one round earlier.  When a value created at generation `j-1`
participates in a new run, an equal companion contributes at least the same
weight.  Induction therefore forces a part created after `j` dependent rounds
to have weight at least `2^j`.  A depth-`t` orbit consequently requires
`n>=2^t`.

The displayed cascade attains the bound.  At each round its left binary
prefix consolidates to the next power of two and meets the following equal
part.  The remainder is placed on the side that avoids a premature boundary
merge; direct induction gives exactly `t` rounds.

### Every-target inverse

Consider a one-step predecessor of `beta`.  The run that maps to `b_i` has a
unique common value `s_i|b_i` and length `b_i/s_i`.  Adjacent runs must have
different common values, or they would be one maximal run.  Conversely, every
adjacent-unequal divisor choice expands uniquely to a predecessor.  The input
length is `sum_i b_i/s_i`, proving the polynomial formula and image test.

The polynomial can be evaluated by a path dynamic program whose state is the
last chosen divisor.  This is an exact atlas, not an enumeration recipe over
all `2^(n-1)` source compositions.

### Fixed census

If `F_j(x)` counts nonempty fixed compositions ending in `j`, and `F(x)` also
includes the empty composition, then

`F_j=x^j(F-F_j)`.

Hence `F_j=x^j F/(1+x^j)` and summing over `j` gives the displayed Carlitz
generating function.  This derivation is included for self-containment but is
not claimed as new.

## 4. Exact falsifier

[`verify_arc_scout.py`](verify_arc_scout.py) exhausts every positive
composition through total `18`, hence `262,143` states.  In a fresh process it
checks:

- carrier and fixed-point counts;
- strict descent, total preservation, absence of cycles, and every endpoint;
- the pointwise logarithmic upper bound and an explicit sharp witness for
  every `n`;
- the complete depth census in every box; and
- the length-refined divisor-path fibre polynomial for every possible target,
  including empty fibres.

The run performs `2,690,869` exact assertions.  Its byte-for-byte expected
stdout is [`CANONICAL.txt`](CANONICAL.txt).

## 5. Collision boundary

The closest occupied carrier is P126, but its literal update refines balanced
composition blocks and its inverse is a suffix/codeword decoder.  ARC instead
coarsens maximal equal *adjacent runs*, has a logarithmic weight-doubling
ancestry clock, and its inverse is a constrained divisor path.  No theorem or
proof engine transfers between them.  P144 works on primitive Dyck
components with a leftmost reassociation and likewise has neither the same
carrier nor the divisor inverse.

Ordinary run-length encoding emits a value/count pair and changes the weight;
ARC emits their product and stays inside `Comp(n)`.  Conway-type descriptive
iteration is therefore not a conjugate system.

## 6. Intake recommendation

The sharp every-`n` clock plus the complete length-refined fibre atlas clears
the internal two-axis value gate.  Subject to the focused owner audit, ARC is
a **replacement finalist**.  Classical Carlitz fixed-point enumeration and
static run statistics must remain explicitly zero credit.

External action remains `HOLD_EXTERNAL`.
