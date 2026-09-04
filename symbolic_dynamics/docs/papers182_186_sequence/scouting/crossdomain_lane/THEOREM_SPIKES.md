# Rigorous theorem spikes

These are proof targets, not polished manuscript claims.  Every formula below
was derived before ranking and its finite instances are independently rebuilt
by `verify_crossdomain.py`.

## Spike A: RICS conflict deletion and order kernel

Let `D_n` be the loopless labelled digraphs on `[n]`.  For `A in D_n`, define
`C_v(A)` by replacing `A_{vu}` with `A_{uv}` for every `u != v`.  The Markov
kernel chooses `v` uniformly.  Define the conflict graph

`H(A)={{u,v}: A_uv != A_vu}`.

The target theorem package is:

1. **Conflict deletion.**
   `H(C_v A)=H(A)-{e: v in e}`.  Consequently the only recurrent states are
   symmetric digraphs, all of them fixed.
2. **Exact absorption polynomial.**  Let `S(t,r)` be a Stirling number of the
   second kind.  The number of length-`t` vertex words that absorb `A` is

   `sum_{M independent in H(A)} (n-|M|)! S(t,n-|M|)`.

   Indeed, after a word with support `S`, precisely `H(A)[[n]\S]` remains.
3. **Exact endpoint kernel.**  Fix a support `S` and the order `pi` in which its
   vertices first occur.  For a conflict edge with at least one endpoint in
   `S`, the endpoint appearing first in `pi` copies the opposite arc; this
   resolves the pair permanently.  An edge disjoint from `S` remains
   unresolved.  Exactly `S(t,|S|)` length-`t` words have a prescribed
   first-occurrence order.  Therefore

   `N_t(A,B)=sum_{(S,pi): E_{S,pi}(A)=B} S(t,|S|)`.

4. **One-step fibres.**  If `k(B)` is the number of isolated vertices of
   `H(B)`, then the number of labelled pairs `(A,v)` with `C_v(A)=B` is
   `k(B) 2^(n-1)`.  The number of distinct sources is zero when `k(B)=0`, and

   `1+k(B)(2^(n-1)-1)`

   otherwise.  Preimage families for distinct admissible vertices intersect
   only in `B`.

**Unmistakable spike.**  The absorption CDF is an evaluation of the independent
set inventory of the *initial conflict graph*, while the endpoint law needs
first-occurrence order.  These are simultaneous graph-enumerative and
noncommutative signals, not merely a coupon-collector estimate.

**Next proof task.**  Express survival and endpoint statistics for graph
families with tractable independence polynomials; determine whether the
endpoint multiplicity polynomial has a useful deletion recurrence.

### Deductive proof route for Spike A

1. Work one unordered pair `{u,v}` at a time.  Show directly from the two arc
   bits that `C_v` makes this pair equal exactly when `v` is selected, and that
   later selections cannot make an equal pair unequal.
2. Taking the product over unordered pairs proves conflict deletion and shows
   that a history leaves exactly the induced conflict graph on its missing
   vertex set.  This simultaneously proves the recurrent classification.
3. Partition histories by missing set `M`.  Absorption is equivalent to `M`
   being independent; histories whose exact support is `[n]\M` are surjections
   onto `n-|M|` labels, counted by `(n-|M|)!S(t,n-|M|)`.  The support classes
   are disjoint, so summation proves the CDF without inclusion--exclusion.
4. Refine a nonempty support by first-occurrence order.  Delete from a word all
   but the first occurrence markers; restricted-growth strings give a
   bijection with set partitions of `[t]` into `|S|` blocks, hence exactly
   `S(t,|S|)` words per prescribed order.  The two-bit calculation from step 1
   then proves the endpoint kernel.
5. Invert one update at a vertex `v`: it is possible precisely when `v` is
   isolated in `H(B)`, and its `n-1` overwritten outgoing bits are free.  This
   gives `2^(n-1)` labelled sources per admissible `v`.  Prove that source
   families for two different vertices intersect only at `B`; their union then
   gives the distinct-source formula.

## Spike B: CGT prime-power functional graph and fibre atlas

Fix a prime `p`, `a>=1`, `N=p^a`, and

`T(x)=x+N/gcd(x,N) mod N`, `0<=x<N`.

Put `v(0)=a` and `v(x)=v_p(x)` otherwise.

1. **Low strata.**  If `2v(x)<a`, the valuation is invariant, the state is
   recurrent, and its cycle length is `p^v(x)`.
2. **High strata.**  If `2v(x)>a`, one step enters valuation `a-v(x)` and the
   eventual period is `p^(a-v(x))`; the tail is exactly one.
3. **Middle conveyor.**  If `a=2h` and `x=p^h u` with `p` not dividing `u`, put
   `r=p-(u mod p)` and `s=v_p(u+r)` (allow `s=h` when `u+r=p^h`).  Then the tail
   is `r+1` and the period is `p^(h-s)`.
4. **Cycle census.**  For every `v` with `2v<a`, there are exactly
   `(p-1)p^(a-2v-1)` cycles of length `p^v`.  The recurrent population is
   `p^a-p^floor(a/2)`.
5. **Tail census.**  For `a=2h+1`, exactly `p^h` states have tail one.  For
   `a=2h`, exactly `p^(h-1)` states occur at each tail depth
   `1,2,...,p`; all other states are recurrent.
6. **Fibre census.**  Put `d=p^floor((a-1)/2)`.  Across all targets, exactly
   `d` fibres are empty, `d` have size two, and `p^a-2d` have size one.  Thus
   `|image(T)|=p^a-d`.
7. **Double-target atlas.**  Besides `y=1`, a target is double precisely when
   `v_p(y)=w<a/2` and

   `y/p^w = 1+p^(a-2w)u`

   for a unit `u` with `1<=u<p^w`.

**Unmistakable spike.**  Even exponents have a uniformly populated tail ladder
of length `p`, produced by consecutive unit increments in the unique middle
valuation layer.  Independently, every fibre is at most two and the image
defect has a closed prime-power form.

**Next proof task.**  Complete a bounded exact-title/formula owner search, then
write the valuation proof with all modular representatives explicit.  Only
after that should one test composite moduli via Chinese remaindering; composite
experiments are not part of the present claim.

### Deductive proof route for Spike B

1. Write every nonzero state uniquely as `x=p^v u`, with `u` a unit, and note
   that the added term is `p^(a-v)`.  The valuation of the sum is decided by
   comparing `v` and `a-v`, except at equality.
2. If `2v<a`, divide by `p^v`: one step adds `p^(a-2v)` to the unit coordinate
   modulo `p^(a-v)`.  This preserves the stratum and has additive order `p^v`,
   proving recurrence and period.
3. If `2v>a`, the added term has strictly smaller valuation, so the new
   valuation is `a-v<a/2`.  Step 2 supplies the eventual period and proves the
   one-step tail.  Treat `x=0` separately as `0->1`.
4. If `a=2h` and `v=h`, the unit coordinate advances by one.  It remains a unit
   for exactly `r-1` advances, becomes divisible by `p` on advance `r`, and one
   further high-to-low step invokes step 3.  The valuation `s` at the landing
   point gives low valuation `h-s` and period `p^(h-s)`.
5. Count elements of each low valuation stratum and divide by its period to get
   the cycle census.  Count high strata geometrically.  In the middle stratum,
   each residue of `u mod p` occurs `p^(h-1)` times, yielding the uniform tail
   ladder.
6. Solve `T(x)=y` separately on low, high, and (when present) middle strata.
   Low strata permute themselves; high strata inject into explicit low targets;
   the middle map is an injective consecutive-unit shift.  This bounds fibres
   by two and gives the displayed double-target equation.
7. Count high sources for odd `a`, and the missing middle congruence class for
   even `a`, to obtain `d=p^floor((a-1)/2)` empty targets.  Since the domain and
   codomain have equal size, the same number of double targets follows; the
   explicit atlas independently identifies them.

## Retired control: SSC formulas

For completeness, after a bit word `w` of length `t<=d`,

`A.w={suffix_{d-t}(x) concatenated with w: x in A}`.

For `t>=d`, the image is the singleton containing the last `d` input bits.  If
`ell(A)` is the longest common suffix length, the tail to the singleton class
is `d-ell(A)`, and

`#{A: tail(A)<=t}=2^(d-t)(2^(2^t)-1)` for `0<=t<=d`.

For fixed `t<=d`, an admissible target `B` has
`(2^(2^t)-1)^|B|` preimages under its unique compatible history.  These are
valid exact identities, but they explain why the system was killed: the whole
package is the transparent power-automaton action of a shift register.
