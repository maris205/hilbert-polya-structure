# P191 Review A — proof rederivation

## Status and conventions

**The mathematical claims are proved as stated.**  A state is a positive
composition `a=(a_1,...,a_k)` of `N`.  The internal boundary after part
`a_i` has old endpoint `s_i=sum_{j<=i} a_j`, and it is retained iff
`a_i | s_i`.  All decisions use the pre-update composition and are applied
simultaneously.  The terminal endpoint `N` is not an internal boundary and is
never tested.

## 1. Direct merge form, fixedness, and recurrence

Scan the old parts left to right while accumulating a pending block.  At each
internal index `i`, flush the block precisely when `a_i | s_i`; always flush
at the final part.  This direct composition-tuple description is equivalent
to retaining exactly the prescribed cut set and proves closure without using
a cut-mask encoding.

Every output boundary was already an input boundary, so the boundary set is
monotone decreasing.  Equality holds exactly when every nonfinal part divides
its endpoint.  Any nonfixed update strictly decreases the finite boundary
set, ruling out nontrivial recurrence; the recurrent states are exactly the
fixed states.

Let `A(0)=1`, and let `A(v)` count admissible internal-boundary histories
ending at `v`.  If their predecessor is `u`, the entering part `v-u` must
divide `v`, whence

\[
A(v)=\sum_{0\le u<v,\;v-u\mid v}A(u).
\]

A fixed composition of total `N` either has no internal cut (`v=0`) or has a
unique last internal cut `v<N`; the last part `N-v` is unrestricted.  Thus

\[
|\operatorname{Fix}(F_N)|=\sum_{v=0}^{N-1}A(v).
\]

## 2. Sharp height and uniqueness

Whenever an internal first cut exists, its part and endpoint are both `a_1`,
so that cut survives.  A length-`k` nonfixed composition consequently has at
most `k-2` deletable cuts.  The only length-`N` composition is all ones and is
fixed; hence a nonfixed state has `k<=N-1` and tail at most `N-3`.  Directly:

- `N=1`: only `(1)`;
- `N=2`: `(2)` and `(1,1)`;
- `N=3`: `(3)`, `(1,2)`, `(2,1)`, `(1,1,1)`.

Every listed state is fixed, so the small-total height is zero.

For `N>=4`, put `omega_N=(1,2,1^(N-3))`.  If

\[
F_N^t(\omega_N)=(1,2+t,1^{N-3-t}),
\]

then the middle part ends at `3+t`.  It cannot divide that endpoint because
it would then divide their difference one.  The following cut alone fails,
so induction gives the formula through `t=N-3`, where `(1,N-1)` is fixed.
This attains tail `N-3`.

Equality in the two upper bounds forces `N-1` initial parts and exactly one
deletion in each nonfixed epoch.  Such a positive composition has one part
two and all other parts one.  Placement of the two first or last is fixed.
If `r>=1` ones precede an internal two, at most `N-r-2` cuts lie to its right
and can be swallowed by its growing block.  Tail `N-3` therefore forces
`r=1`, proving that `omega_N` is the unique extremizer.

## 3. Global inverse characterization

Fix a target boundary set `T`.  A source boundary path
`0=x_0<...<x_l=N` maps to that target exactly when:

1. no edge skips a mandatory target boundary;
2. at every nonfinal source endpoint `v`, the incoming step `v-u` divides
   `v` iff `v` belongs to `T`; and
3. the final step into `N` is unrestricted.

Necessity follows from target boundaries being retained source boundaries and
the literal rule.  Conversely these conditions make precisely the target
vertices survive and every extra vertex disappear, so the resulting cut set
is exactly `T`.  This is a bijection, and last-edge decomposition gives the
paper's global recurrence and positivity image test.

The reviewer control obtains the same global fibres without implementing
that path recurrence: it recursively generates every source composition,
applies the direct merge transition, and bins it by the resulting target.

## 4. Independent interval factorization

For consecutive target endpoints `p<q`, an extra source endpoint `v` in the
open interval must be deleted, so its entering step does not divide `v`.
Let `h_p(p)=1` and

\[
h_p(v)=\sum_{p\le u<v,\;v-u\nmid v}h_p(u),\qquad p<v<q.
\]

At an internal target endpoint `q<N`, its last entering step must divide `q`:

\[
K(p,q)=\sum_{p\le u<q,\;q-u\mid q}h_p(u).
\]

At the terminal endpoint no condition is imposed:

\[
K_*(p,N)=\sum_{p\le u<N}h_p(u).
\]

Mandatory target endpoints split a source path uniquely into such intervals,
and concatenation reverses the split.  Therefore the fibre is the product of
the internal `K` factors and the last `K_*` factor.  The one-part target has
no internal factor; its empty product is one.

The final condition is essential.  The target `(1,N-1)` is fixed for every
`N>=3`, although its last part need not divide `N`.  A recurrence that treats
`N` as an internal retained cut undercounts its fibre; the reviewer verifier
constructs and separates this wrong control in every `N=3,...,18` box.

The reviewer interval implementation uses memoized backward recursion.  It is
also compared with brute enumeration of every positive refinement of every
interval `0<=p<q<=18`, for both internal and terminal endpoint semantics: 342
exact interval boxes.

## 5. Image and mass

The global inverse characterization and the interval split are bijections,
so a target is in the image iff its global count is positive iff every factor
in its nonnegative product is positive.  Finally, determinism sends every
source to exactly one labelled target; hence the fibres partition the
`2^(N-1)` recursively generated compositions:

\[
\sum_{b\in\mathcal C_N}|F_N^{-1}(b)|=2^{N-1}.
\]

Every target, including zero-fibre targets, is compared pointwise before this
mass identity is checked.  Thus mass cannot conceal a redistributed error.

No mathematical repair is required.  The source-ledger metadata correction in
`DELTA.md` has been accepted; no Review A finding remains open.
