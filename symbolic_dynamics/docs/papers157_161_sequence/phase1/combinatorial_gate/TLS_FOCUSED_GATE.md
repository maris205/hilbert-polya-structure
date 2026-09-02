# Focused gate for the cyclic Temperley--Lieb sweep

**Gate date:** 2026-09-02 UTC  
**Status:** `KILL_P130_P144_TRANSFER`  
**External state:** `HOLD_EXTERNAL`  
**Allocation:** no paper number and no manuscript

This note freezes the strongest exact theorem discovered in the replacement
scout and the reason that it still cannot enter the five-paper pool.  The
theorem is valid; the portfolio residual is not paper-sized.

## 1. Literal finite dynamical system

Let `NC_2(n)` be the noncrossing perfect matchings of the cyclically ordered
points `0,1,...,2n-1`.  For an index `i` read modulo `2n`, the
Temperley--Lieb generator `e_i` joins `i` to `i+1`.  If their old partners are
`a` and `b`, it also joins `a` to `b`; if `i` and `i+1` were already joined,
it fixes the matching.  Define the deterministic sweep

```text
F_n = e_(2n-1) o ... o e_1 o e_0,
```

where the rightmost map acts first.  Thus the program applies the generators
in the displayed time order `e_0,e_1,...,e_(2n-1)`.

Write `B_n` for the matchings containing the boundary arc `{0,2n-1}`.  The
strip map `s:B_n -> NC_2(n-1)` deletes that arc and subtracts one from every
remaining endpoint.  Let `rho` add one to every cyclic label.

## 2. Exact theorem contract

### Theorem TLS

For every `n>=1`:

1. `im(F_n)=B_n`.  Consequently `|im(F_n)|=Cat_(n-1)`, and every state has
   preperiod at most one.
2. For `n>=2` and `M in B_n`,

   ```text
   s(F_n(M)) = rho^(-2)(s(M)).
   ```

   Hence the restriction to the image is conjugate to rotation by two steps
   on `NC_2(n-1)`, and its complete cycle census is the corresponding
   rotation census.
3. Let `U in B_n`, set `V=rho(s(U))`, and let `r(V)` be the number of
   primitive factors of the Dyck word associated with `V`.  Then

   ```text
   |F_n^(-1)(U)| = r(V)+1.
   ```

   For `k=n-1>=1`, the number of targets of indegree `r+1` is

   ```text
   (r/k) binom(2k-r-1,k-1),       1<=r<=k.
   ```

   The maximum fibre is `n`, attained by a unique target.  At `n=1` the sole
   state has fibre one.

The exhaustive verifier checks the image, conjugacy, tail bound, targetwise
fibre identity, distribution, and extremum through `n=9` (4,862 source
states at the last rank).  Exhaustion is a falsifier, not the proof.

## 3. Short complete proof skeleton

For the image statement, the last generator `e_(2n-1)` joins `2n-1` to `0`,
so every output lies in `B_n`.  Start instead with a matching in `B_n` and
follow the unique exposed strand during `e_0,e_1,...,e_(2n-2)`.  At step `j`,
planarity forces that strand to be the boundary of the already swept interval;
the reconnection moves its interior endpoint two cyclic positions backwards
and preserves the relative nesting of all untouched arcs.  Induction on `j`
therefore gives

```text
s(F_n(M))=rho^(-2)(s(M)).
```

The last generator merely restores the outer arc.  Rotation is bijective, so
the displayed identity supplies a predecessor in `B_n` for every member of
`B_n`; this proves `im(F_n)=B_n`, the one-step tail bound, and the rotation
conjugacy.

For the inverse fibre, run the sweep backwards from `U`.  After stripping the
forced final arc and undoing the fixed label shift, encode the remaining
matching by the Dyck word `V=C_1...C_r` in its unique primitive
factorisation.  Inside a primitive factor, noncrossing leaves exactly one
possible continuation of the exposed strand.  A second continuation becomes
possible precisely at a return to height zero.  Choosing one of the `r-1`
internal cuts, either outside cut, reconstructs exactly one source; equivalently
there are the `r+1` cuts before, between, and after the primitive factors.
The forced-continuation argument also shows that these sources are exhaustive
and distinct.

Finally, a primitive Dyck word has generating function `z C(z)`.  A sequence
of exactly `r` primitive factors therefore has generating function
`(z C(z))^r`; Lagrange extraction gives

```text
[z^k](z C(z))^r = (r/k) binom(2k-r-1,k-1).
```

The largest possible component count is `k`, achieved only by `(UD)^k`, so
the maximum fibre is uniquely `k+1=n`.

## 4. Five-layer internal collision matrix

| layer | P130 comparison | P144 comparison | gate consequence |
|---|---|---|---|
| literal | different componentwise chord retraction | different leftmost Dyck reassociation | literal novelty alone does not save TLS |
| state | matchings mapped onto a noncrossing matching core | Dyck paths, bijective with noncrossing matchings | TLS uses P144's carrier after `s` |
| all iterates | one-step retraction to a finite core | terminating fixed core | TLS temporal residual is only classical rotation |
| fibre | target-local matching fibres and unique maximum | exactly `r+1`, with `r` primitive Dyck components | TLS has the same target coordinate and extremum as P144 |
| proof engine | targetwise inverse construction | cut the primitive-factor list; ballot extraction | the TLS reverse sweep mechanically becomes P144's cut inverse |

The decisive identity is not merely a shared Catalan number:

```text
TLS target fibre
  -- strip forced boundary arc and rotate once -->
number of cuts in a primitive-Dyck-factor list
  = P144 terminal fibre.
```

More explicitly, if `w(V)` is the Dyck word of a noncrossing matching, then

```text
Theta(U) = up · w(rho(s(U))) · down
```

is a primitive Dyck path of semilength `n`, hence a fixed target of P144.
This is a bijection from the TLS image `B_n` to the P144 fixed set.  Both the
TLS predecessors of `U` and the P144 basin sources ending at `Theta(U)` are
canonically indexed by the same cuts of the primitive-factor list of
`w(rho(s(U)))`.  Thus the target statistic and inverse coordinate migrate,
not just their final cardinalities.

P144 already proves the same `r+1` law, the same primitive-cut bijection, the
same ballot distribution, and the same unique maximum.  P130 additionally
occupies the matching-to-noncrossing retraction and target-fibre silhouette.
After those subtractions, TLS retains only a product of standard cyclic
Temperley--Lieb generators whose recurrent action is rotation.

## 5. Direct-owner chain

The bounded search found two positive adjacencies:

1. S. Ng, [*Link Patterns and the Catalan Tree*](https://arxiv.org/abs/1305.4877),
   directly uses preimages of a Temperley--Lieb generator on link patterns.
2. The FPL/link-pattern literature, for example
   [*Link patterns of quarter-turn symmetric FPL configurations*](https://dmtcs.episciences.org/3644/pdf),
   uses the same cyclic reconnection generators and circular rotation.

The search did not locate the precise ordered product `e_0...e_(2n-1)` under
a standard name.  That bounded non-hit is not a novelty claim and cannot
override the exact internal transfer above.

## 6. Verdict

```text
mathematical contract: PASS
external adjacency:    DIRECT INGREDIENT OWNERS
internal residual:     EMPTY AT PAPER SCALE
gate:                  KILL_P130_P144_TRANSFER
```

Do not allocate, draft, freeze, release, commit, or push this candidate.
