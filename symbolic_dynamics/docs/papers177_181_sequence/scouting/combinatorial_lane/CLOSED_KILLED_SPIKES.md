# Closed theorem spikes that fail the owner/collision gate

These results were proved and exhaustively checked before the decisive kill.
They are recorded to preserve mathematical progress, not to support a paper or
a novelty claim.

## Anchored minimum-cycle join (`MCJ`)

Let permutations act on `{0,...,n-1}`.  If the cycle containing 0 is not an
`n`-cycle, let `a` be the least label outside it and right-multiply by the star
transposition `(0 a)`; equivalently, swap the outgoing arrows at 0 and `a`.
An `n`-cycle is fixed.

### Exact theorem

1. Every nonfixed step merges exactly two cycles.  Hence
   `depth(pi)=number_of_cycles(pi)-1`; the recurrent set consists exactly of
   the fixed `n`-cycles.  The clock is sharply `n-1`, the identity is the unique
   deepest state, and the number of depth-`t` states is the unsigned Stirling
   number `c(n,t+1)`.
2. Write the 0-cycle of a target `q` as `(0,w_1,...,w_{m-1})`.  Let `r(q)` be
   the least label outside that cycle, with sentinel `n`, and let `ell(q)` be
   the number of left-to-right lower records among the `w_i` that are smaller
   than `r(q)`.  For every `t>=0`,

   ```text
   abs((T^t)^(-1)(q)) = binom(ell(q),t)                    if m<n,
                      = sum_{j=0}^{min(t,ell(q))} binom(ell(q),j) if m=n.
   ```

   Thus this is an all-time, every-target formula, including zero fibres.
3. The first image for `n>=2` is exactly the permutations in which 0 and 1
   lie in the same cycle, so it has size `n!/2`.  The one-step fibre is
   `ell(q)+1_{m=n}`.  Its unique maximum `n` occurs at
   `(0,n-1,n-2,...,1)`.
4. If `q` is a fixed `n`-cycle and `rho(q)` is the number of lower records in
   its tail, its complete terminal basin polynomial is `(1+u)^rho(q)`.
   Exactly `c(n-1,r)` endpoints have basin size `2^r`, and the basin masses
   sum to `n!`.

### Proof skeleton

Right multiplication by `(0 a)` swaps outgoing arrows at vertices in
different cycles, so it merges those cycles and changes no others.  Order the
nonanchor source cycles by increasing minima `a_1<...<a_s`, writing them as
`(a_i,B_i)` and the anchor cycle as `(0,A)`.  Direct arrow tracing gives the
terminal cycle

```text
(0, B_s, a_s, B_{s-1}, a_{s-1}, ..., B_1, a_1, A).
```

Reversing an update means cutting the target's 0-cycle after a lower record.
The cut label must be below the least untouched outside-cycle minimum.  Any
chosen set of `t` such cuts reconstructs exactly one source and is rejoined in
the forced increasing-minimum order.  For a nonfixed target exactly `t` cuts
are needed; for a fixed target any `j<=t` cuts are allowed because the
remaining iterates wait at the absorber.  This proves the fibre formulas.
The Stirling statements are the standard cycle/record distribution.

### Decisive kill

The proof itself exposes the collision.  Star-transposition merging is
classical, while the displayed normal form and inverse cuts are a Foata
cycle/record flattening.  P122 already spends the admissible-record-cut inverse
architecture; P105 and P155 occupy the neighbouring cycle/minimum and
cycle/extraction surfaces.  Once those pieces receive zero credit, no
independent paper-sized engine remains.  Status:
`KILL_FOATA_STAR_TRANSPOSITION_THIN`.

## First-descent follower to front (`FDF`)

For a nonidentity one-line permutation, take the entry immediately following
its first descent and move that entry to the front, preserving all other
relative order.  Fix `1,2,...,n`.

### Exact theorem

1. The identity is the unique recurrent state.  The maximum depth is
   `2^(n-1)-1`, attained uniquely by `(n,1,2,...,n-1)`.
2. For a target `q=(x,a_1,...,a_{n-1})`, let `a_1<...<a_r` be the longest
   increasing prefix of the tail.  Its complete one-step fibre size is

   ```text
   #{i<=r : a_i>x} + 1_{q=(1,2,...,n)}.
   ```

   The actual parents are obtained by inserting `x` immediately after each
   eligible `a_i`, plus the fixed self-parent at the identity.
3. For `1<=k<=n-2`, exactly `n!/(k+1)!` targets have positive fibre `k`;
   no target has fibre `n-1`; the identity is the unique target of fibre `n`.
   Consequently

   ```text
   abs(im T) = 1 + n! * sum_{j=2}^{n-1} 1/j!   (n>=2).
   ```

### Proof skeleton

Give label `j` the binary weight `2^(j-1)` and define

```text
B(pi)=sum_j 2^(j-1) * 1{some larger label occurs before j in pi}.
```

Suppose the first increasing prefix is `a_1<...<a_s` and the moved follower
is `x<a_s`.  Moving `x` to the front clears the bit of `x`.  The only bits it
can create are those of prefix entries smaller than `x`; every such entry was
a record before the move.  Hence

```text
B(T pi)-B(pi) = -2^(x-1) + sum_{a_i<x}2^(a_i-1) <= -1.
```

This proves absorption and the universal clock bound.  For
`(n,1,...,n-1)`, an induction splits the orbit into a copy on the ordered
alphabet `{1,...,n-2,n}`, the central move of `n-1`, and a copy on
`{1,...,n-1}` with `n` appended.  Its length therefore satisfies
`L_n=2L_{n-1}+1`, `L_1=0`.  Equality in every binary-potential drop forces the
original suffix successively to be `1,2,...,n-1`, proving uniqueness.

The target-fibre rule follows by reversing the move.  For the distribution,
rotate the target's first entry `x` back behind the lower entries of its
initial tail run.  Targets of fibre `k`, `1<=k<=n-2`, are thereby in bijection
with permutations whose first `k+1` positions increase, of which there are
`n!/(k+1)!`.  The identity supplies the exceptional fibre `n`.

### Decisive kill

Project Euler Problems 523 (**First Sort I**) and 524 (**First Sort II**) state
this exact scan-first-descent/move-the-smaller-entry-to-front algorithm and
explicitly study its step count `F`.  Literal ownership alone is fatal,
regardless of whether the fibre distribution above is separately written
there.  Status: `KILL_EXACT_EXTERNAL_OWNER_PROJECT_EULER_523_524`.

