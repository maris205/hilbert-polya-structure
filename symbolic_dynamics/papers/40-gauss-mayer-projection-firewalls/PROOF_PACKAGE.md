# Proof package

Status: `POST_CANONICAL_DEPENDENT_RENDERING`
Candidate: `SD-C42`
Source lock: `2269e06576dd20c513c5ca9482cb49d36678e07358aaf80f2f08b33806b87041`
Control result: `d0be9630e4f0710c1f602e14e517939f6eef21c582934d79f795a9871f45a30f`
Prototype result: `2fee7701a08ec4f7e019863c6e86bf6fb884bf0323e5593e4bf946ef35e7a995`

This is a post-canonical proof rendering.  It binds the mathematical claims
to the corrected source and exact outputs but carries no prospective status.

## Main theorem

Let `w` range over cyclic `RhoPrimitivePair` words, with ordered digit
monodromy

\[
M(w)=\prod_{i=1}^{2k}\begin{pmatrix}a_i&1\\1&0\end{pmatrix}.
\]

Let `t=tr M`, `Delta=t^2-4`,
`lambda=(t+sqrt(Delta))/2`, and `T=2 log lambda`.  On the exact Mayer space
and domain in `MAYER_SOURCE_BOUNDARY.md`, let `K_s=L_s^2` and
`D_42(s,u)=det(I-u^2K_s)`.  Then:

1. the pair return map, pair primitivity, monodromy, Gauss branch, derivative
   roof, digit marker, raw `K_s^k` summand, and determinant are one typed
   source construction;
2. `P_t=t`, `P_Delta=Delta`, and `P_N=lambda^2` are the complete frozen
   scalar-projection family;
3. no member of that family satisfies the full rational-prime reciprocal
   Euler-ledger conjunction on the full pair ledger;
4. no integer-valued member simultaneously preserves the exact clock and
   temporal powers;
5. the frozen untwisted operator schema declares no reducing owner for any
   rational-prime scalar postselection.

Consequently the six-code terminal tuple in `SOURCE_LOCK.md` follows.  The
theorem does not assert universal nonexistence over twists, objectwise
pair/geodesic equivalence, witness novelty or minimality, or a new Selberg or
Mayer identity.

## Lemma 1: typed return and splitting

Let `X=N^N` carry the digit shift `sigma`, let `X2=(N^2)^N` carry the pair
shift `rho`, and group adjacent digits by `iota`.  Then

\[
\rho\iota=\iota\sigma^2.
\]

If a `sigma` orbit has least period `n`, it splits under `sigma^2` into
`gcd(n,2)` cycles of length `n/gcd(n,2)`.  Hence

\[
N_{D^2}(k)=2N_D(2k)+\mathbf1_{k\text{ odd}}N_D(k).
\]

### Proof

Both compositions delete the first two digits before grouping, which proves
the conjugacy.  On a least-period-`n` orbit, label points by `Z/nZ`.  The map
`sigma^2` is addition by two.  Its subgroup has index `gcd(n,2)`, so there are
that many cycles, each of the stated length.  A pair cycle of length `k`
therefore arises twice from a digit cycle of length `2k`, or once from a digit
cycle of length `k` when `k` is odd.  Summing primitive orbit classes yields
the formula.  This also proves that the two trace-4 pair phases are distinct
`rho` cycles and that `((2,2))` can be pair-primitive while its flattening is
digit-imprimitive.  QED.

## Lemma 2: matrix, branch, and clock ownership

For every even stored word, `M(w)` lies in `SL_2(Z)`, has trace at least
three, and satisfies

\[
M(w^r)=M(w)^r,\qquad T(w^r)=rT(w).
\]

If `phi_a(z)=1/(a+z)`, its stored branch `Phi_w` satisfies

\[
-\log|\Phi'_w(x_w)|=2\log\lambda_+(M(w)).
\]

Moreover the stored summand of `K_s^k=L_s^{2k}` is obtained by globally
reversing the raw transfer indices.

### Proof

Every digit matrix has determinant `-1`; an even product has determinant one.
All entries are positive and the smallest one-pair product, `A(1)^2`, has
trace three, so positivity and monotonicity in the digits give `t>=3`.
Concatenation gives `M(w^r)=M(w)^r`; eigenvalues therefore become
`lambda_+^r` and `lambda_+^-r`, proving clock additivity.

Set `B(a)=[[0,1],[1,a]]` and `J=[[0,1],[1,0]]`.  Direct multiplication gives
`A(a)=JB(a)J`, hence

\[
M(w)=JB(a_1)\cdots B(a_{2k})J.
\]

Under the column-vector Möbius convention the middle product represents
`Phi_w=phi_a1 o ... o phi_a2k`.  For
`B_w=[[alpha,beta],[gamma,delta]]`, the fixed-point equation is

\[
\gamma x^2+(\delta-\alpha)x-\beta=0.
\]

At the attracting root, `gamma x+delta` is the expanding eigenvalue of the
conjugate matrix.  Since the even product has determinant one,
`|Phi'_w(x)|=(gamma x+delta)^-2=lambda_+^-2`, proving the clock identity on
the positive real branch.

Finally, direct nesting gives

\[
L_s(L_sf)(z)=\sum_{a,b}j_a(z)j_b(\phi_a z)
f(\phi_b\circ\phi_a z).
\]

Thus raw indices occur in the reverse of stored composition order.  Repeating
the calculation inductively for `2k` applications gives the global reversal
and the exact nested product of `(a+z)^(-2s)` factors on Mayer's fixed
holomorphic logarithm branch.  For an even word this is the corresponding
holomorphic branch of `(Phi'_w(z))^s`; only on the positive real branch may it
be written `|Phi'_w(z)|^s`.  The reversal is a dummy-index
bijection, so it neither removes words nor changes primitive necklace counts.
The direct exact fixture values `442/623`, `16/388129` versus the wrong-order
`146/697`, `16/485809` distinguish the two expansions.  QED.

## Lemma 2.1: intrinsic pair Fredholm regrouping

In Mayer's nuclear domain, coefficientwise as a formal series in `u^2` and
analytically for sufficiently small `|u|`, the determinant of `K_s=L_s^2`
owns the intrinsic `RhoPrimitivePair` ledger:

\[
-\log\det(I-u^2K_s)
=\sum_{[v]\ \mathrm{rho\mbox{-}primitive}}
 \sum_{r\ge1}\frac{u^{2k(v)r}d_v^{rs}}{r(1-d_v^r)}.
\]

Consequently

\[
\det(I-u^2K_s)^{-1}
=\prod_{[v]}\prod_{j\ge0}
(1-u^{2k(v)}d_v^{s+j})^{-1}.
\]

### Proof

Nuclear Fredholm theory gives, first coefficientwise/formally and
analytically for sufficiently small `|u|`,

\[
-\log\det(I-u^2K_s)
=\sum_{n\ge1}\frac{u^{2n}}n\operatorname{Tr}(K_s^n),
\]

for the local logarithm at `u=0`.  Lemma 2 shows that
raw-index reversal bijectively rewrites every summand in stored
pair-composition order and is compatible with cyclic classes and repetition.
For one stored pair word `w`, the one-dimensional holomorphic
weighted-composition trace formula is

\[
\frac{d_w^s}{1-d_w},
\]

where `d_w=|Phi'_w(x_w)|` is the positive real fixed-point multiplier; the
underlying complex weight uses the fixed holomorphic branch of Lemma 2.

Write a length-`n` word as `v^r`, where `v` is a primitive pair necklace of
length `k`.  Then `n=kr`, `d_(v^r)=d_v^r`, and `v` has exactly `k` cyclic
representatives in the word trace.  Its coefficient is therefore

\[
\frac{k}{kr}u^{2kr}\frac{d_v^{rs}}{1-d_v^r}
=\frac{u^{2kr}d_v^{rs}}{r(1-d_v^r)}.
\]

Summing proves the trace-to-primitive formula.  In the same local/formal
sense, expand `(1-d_v^r)^(-1)=sum_(j>=0)d_v^(jr)` and exponentiate the trace
series to obtain the product.  We do not continue a single-valued logarithm
through determinant zeros or assert convergence of this primitive product at
arbitrary `u`.  The `u=1` Selberg-zeta/Fredholm identity and its continuation
are invoked only through Mayer's separate sourced theorem.  This regrouping
uses no Selberg primitive class and no objectwise pair/geodesic bijection.
QED.

## Lemma 3: exact algebraic labels

For every source word,

\[
\Delta=(t-2)(t+2)
\]

is prime exactly when `t=3`; `P_N=lambda_+^2` is irrational; `P_N` and the
derivative multiplier `d=lambda_+^-2` are reciprocal roots of

\[
x^2-(t^2-2)x+1.
\]

### Proof

For `t>3`, both integer factors `t-2` and `t+2` exceed one, so `Delta` is
composite.  At `t=3`, it equals five.  The strict inequalities

\[
(t-1)^2=t^2-2t+1<t^2-4<t^2
\]

hold because `2t-5>0`.  Hence `Delta` lies strictly between consecutive
squares and is not square, so `lambda_+` is irrational.  Squaring
`lambda+lambda^-1=t` gives `lambda^2+lambda^-2=t^2-2`; the polynomial and
reciprocal root selectors follow.  Its discriminant is
`(t^2-2)^2-4=t^2 Delta`, which is nonsquare because `Delta` is nonsquare.
Therefore `lambda_+^2` is also irrational.  QED.

## Lemma 4: trace and order-discriminant fail clock and powers

Neither `P_t` nor `P_Delta` preserves temporal powers or the source clock on
all realized traces.  No constant rescales `log t` to `T` on all source
objects.

### Proof

Cayley--Hamilton gives `M^2-tM+I=0`.  Multiplying by `M^(r-2)` and taking
traces yields

\[
q_r=tq_{r-1}-q_{r-2},\qquad q_0=2,\quad q_1=t.
\]

Thus `q_2=t^2-2`, not `t^2`.  Further,

\[
\Delta(M^2)=q_2^2-4=t^2(t^2-4)=t^2\Delta(M),
\]

which differs from `Delta(M)^2` because `Delta=t^2-4`.

For `t>=3`, the difference
`t^2-4-(t-2)^2=4t-8` is positive.  Therefore

\[
\lambda=\frac{t+\sqrt{t^2-4}}2>t-1,
\qquad \lambda^2>(t-1)^2\ge t,
\]

and hence `T=log lambda^2>log t`.
Every integer `t>=3` occurs for

\[
w_t=((1,t-2)),\qquad
M(w_t)=\begin{pmatrix}t-1&1\\t-2&1\end{pmatrix}.
\]

As `t` tends to infinity, `lambda=t+O(t^-1)`, so
`log(lambda^2)/log(t)` tends to two.  Any global rescaling constant would
therefore be two.  But `lambda<t` for finite `t`, since
`lambda=(t+sqrt(t^2-4))/2<t`; hence `lambda^2<t^2`, contradicting equality
for that constant.  QED.

## Lemma 5: exact collision and full-ledger witnesses

Each frozen scalar projection has duplicate source species, and the full
trace ledger contains a composite species.

### Proof

Direct ordered multiplication gives:

| Pair word | Matrix | Pair length | Trace | Order discriminant |
|---|---|---:|---:|---:|
| `((1,2))` | `[[3,1],[2,1]]` | 1 | 4 | 12 |
| `((2,1))` | `[[3,2],[1,1]]` | 1 | 4 | 12 |
| `((1,4))` | `[[5,1],[4,1]]` | 1 | 6 | 32 |
| `((2,2))` | `[[5,2],[2,1]]` | 1 | 6 | 32 |
| `((2,4))` | `[[9,2],[4,1]]` | 1 | 10 | 96 |
| `((1,1),(1,2))` | `[[8,3],[5,2]]` | 2 | 10 | 96 |

One-pair words are pair-primitive.  The two-pair word has unequal pair
symbols and hence is not a proper pair power.  The trace-4 pair is
reversal-related but reversal is not quotiented; the trace-6 pair is not
reversal-related; the trace-10 pair is non-reversal and cross-length.
Because `P_Delta` and `P_N` are functions only of `t`, each pair collides
under all three projections.  The trace value four is composite and belongs
to the full ledger.  QED.

## Lemma 6: reciprocal-determinant amplitude mismatch

Even a formal assignment of a source word to `p=P_N(w)` does not identify its
Mayer reciprocal-determinant factor with a rational-prime Euler factor.

### Proof

By Lemma 2.1, for pair length `k` and derivative multiplier
`d=lambda^-2`, the source factor is

\[
\prod_{j\ge0}(1-u^{2k}d^{s+j})^{-1}.
\]

Expanding its logarithm and summing the geometric series over `j` gives the
repetition-`r` coefficient

\[
\frac{u^{2kr}d^{rs}}{r(1-d^r)}.
\]

The target factor `(1-u^(2k)p^-s)^-1` instead has coefficient
`u^(2kr)p^(-rs)/r`.  Setting `p=d^-1` matches the exponential base but leaves
the nonunit factor `(1-d^r)^-1`.  Hence source stability amplitude and Selberg
tower remain.  QED.

## Lemma 7: no declared scalar owner in the frozen schema

No projection among `P_t`, `P_Delta`, and `P_N` has a declared reducing
projector owning its selected trace in the frozen untwisted operator schema.

### Proof

The hash-bound schema declares `K_s=L_s^2`, the full pair ledger, and no
scalar-selection projector.  The executable ownership predicate separately
requires a matrix projector, idempotence, commutation, compatible dimension,
power traces, multiplicity, and marker support.  Its positive toy fixture
`K=diag(2,3)`, `P=diag(1,0)` passes all requirements; mutations of each field
fail.  The scalar inventory `{3,4}->{3}` has no declared projector and
therefore cannot pass the predicate.  This proves absence in the frozen
schema only.  QED.

## Proof of the main theorem

Lemmas 1, 2, and 2.1 establish a complete intrinsic pair ledger owned by the same
Mayer even iterate and marker, giving the two modular GO statements within
the stated source/domain boundary.  For `P_t`, Lemmas 4 and 5 show failures of
prime support, injectivity, clock, and powers.  For `P_Delta`, Lemmas 3--5 show
failures of prime support, injectivity, clock, and powers.  For `P_N`, Lemma 3
shows failure of rational-integer support while Lemmas 5 and 6 show
injectivity and amplitude failures; although it passes clock and powers, its
full conjunction is false.  Thus the disjunction of the three complete
`ProjectionGO` predicates is false.  Lemma 7 adds the frozen ownership STOP.

The integer/clock/power matrix has `P_t` and `P_Delta` in the integer column
but outside both clock and power columns, while `P_N` lies in both clock and
power columns but outside the integer column.  This proves the narrowly scoped
second STOP.  All six terminal codes follow.  QED.

## Machine-checked finite obligations

The canonical control has fourteen conjunctive gates and the independent
replay recomputes twenty-three checks with zero failures.  The exact prototype
contains six registered runs, 39,622 scientific rows, zero theorem failures,
and exact return-map, splitting, branch-order, and three-collision
certificates.  Its independent replay recomputes fourteen checks with zero
failures.  These bounded computations check fixtures, finite enumeration, and
schema integrity; universal claims above rest on the displayed algebraic
proofs rather than finite extrapolation.

## Remaining boundary

The Mayer identity is used only with its function-space and domain
qualification: the Fredholm identity is holomorphic for `Re(s)>1/2`, the
Euler-product interpretation begins in `Re(s)>1`, and meromorphic
continuation extends to the complex plane.  At `u=1` it is a function identity,
not an objectwise pair/geodesic bridge.  No corrected witness receives
novelty or priority credit.
