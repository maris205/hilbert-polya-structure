# Frozen theorem contract — parallel odd-vertex pruning

External status: **HOLD_EXTERNAL**.  Candidate status:
**PASS_FOCUSED / UNNUMBERED**.

Fix an ambient label set `[n]`.  A state is a simple graph on an arbitrary
subset `S` of `[n]`, including the empty graph.  Let `F(G)` be the induced
graph left after simultaneously deleting every vertex having odd degree in
`G`.  An **even graph** here means a graph all of whose vertex degrees are
even; connectivity is not required.

For `0 <= s < m <= n`, put `d=m-s` and define the strict inverse transfer

```text
B_n(s,m) = binom(n-s,d) 2^[s(d-1)+binom(d-1,2)]   if d is positive and even,
           0                                      otherwise.
```

Let `e_0=e_1=1` and `e_s=2^binom(s-1,2)` for `s>=2`.

The manuscript must prove the following conjunction.

1. **Finite dynamics and sharp clock.**  Every nonfixed epoch deletes a
   positive even number of vertices.  The recurrent states are precisely the
   even graphs, all fixed.  Every orbit enters this locus in at most
   `floor(n/2)` steps, and the labelled path on `[n]` attains the bound.
2. **Strict inverse theorem.**  For every target graph `H` on a fixed
   `s`-set and every `m>s`, the number of rank-`m` strict predecessors is
   exactly `B_n(s,m)`, independent of every edge of `H`.  The proof must be
   an incidence-matrix rank calculation on the connected graph consisting of
   all edges incident with the deleted set, not an appeal to computation.
3. **Every-time, every-target fibres.**  Treat `B_n` as an `(n+1)`-square
   nilpotent matrix.  For a target `H` of rank `s`,

   ```text
   # (F^t)^(-1)(H), refined by source rank m
     = (B_n^t)(s,m)                         if H is not even,
     = (I+B_n+...+B_n^t)(s,m)               if H is even.
   ```

   Summing over `m` gives the full fibre.  Explain why a strict predecessor
   is automatically non-even, which is what makes matrix multiplication
   exact rather than an overcount.
4. **Exact image layers.**  At time `t=0` every state occurs.  For `t>=1`, a
   graph `H` on `s` labels lies in `im(F^t)` iff either `H` is even or
   `n-s>=2t`.
5. **Censuses.**  The total phase size, fixed count, and depth CDF are

   ```text
   |X_n| = sum_s binom(n,s) 2^binom(s,2),
   |Fix F| = sum_s binom(n,s) e_s,
   #{G: tau(G)<=t}
     = sum_s binom(n,s) e_s sum_m (I+B_n+...+B_n^t)(s,m).
   ```

   Exact shells are successive differences.  The time-`t` image count is the
   corresponding sum of all even graphs plus the non-even rank layers allowed
   by `n-s>=2t`.

The scope ceiling is this complete parity-transfer atlas.  The handshaking
lemma, binary incidence-matrix rank, cycle-space count, sequential parity
deletion games, and generic graph-pruning language receive zero contribution
credit.
