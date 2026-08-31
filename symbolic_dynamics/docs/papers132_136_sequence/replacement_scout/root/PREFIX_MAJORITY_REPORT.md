# Synchronous prefix-majority dynamics on binary words

**Stage:** replacement proof spike after two independent hostile repairs.
**Disposition:** post-repair internal Stage-2 lead.  **External status:**
`HOLD_EXTERNAL`.

## 1. Literal map

For a binary word `w=w_1...w_n`, define `P_n(w)=y` by

```text
y_i = 1  iff  w_1+...+w_i >= i/2.                     (1.1)
```

Thus every position simultaneously reports the weak majority of its own
prefix.  With `x_i=2w_i-1` and `S_i=sum_(j<=i)x_j`, this is the sign trace
`y_i=1[S_i>=0]` of a simple walk.  The map is length-preserving and is neither
a local cellular automaton nor a sorting, deletion, transport, rotation, or
closure rule.

## 2. Fixed points and a sharp global clock

A word is fixed exactly when it belongs to one of the two families

```text
(01)^r 0^(n-2r),       0<=r<=floor(n/2),
(01)^r 1^(n-2r),       0<=r<=floor((n-1)/2).           (2.1)
```

These families are disjoint and give exactly `n+1` fixed words.  To see (2.1),
write the balance before the next letter as `h`.  At `h>=1` a fixed word is
forced to keep writing ones; at `h<=-2` it is forced to keep writing zeros;
at heights zero and minus one it may either traverse another `01` pair or
lock into one of the constant tails.

Every orbit reaches (2.1), and the worst exact tail is

```text
max_w depth(w) = ceil(log_2 n).                         (2.2)
```

The proof is a fixed-prefix amplification lemma.  Prefix compatibility says
that the maximal prefix on which a nonfixed word agrees with its image is
itself a fixed word.  Write it uniquely as `(01)^r b^ell`, with alternating
core length `c=2r` and `ell>=1`.

- If `b=1`, the balance after the fixed prefix is `ell`.  Even an all-zero
  continuation remains nonnegative for the next `ell` positions.  Applying
  `P_n` therefore preserves the core and produces a fixed prefix containing
  `(01)^r 1^(2ell)`.
- If `b=0`, maximality forces `ell>=2`: after a lone zero at balance minus
  one, either possible next input would still agree with (1.1).  The balance
  after the prefix is `-ell`, so even an all-one continuation remains
  negative for the next `ell-1` positions.  Applying `P_n` preserves the
  core and produces a fixed prefix containing `(01)^r 0^(2ell-1)`.

The same core is preserved at later steps: a locked one cannot restart the
alternation, and the negative branch contains at least two consecutive
zeros.  Hence after `t` steps

```text
positive branch: ell_t >= 2^t ell_0,
negative branch: ell_t-1 >= 2^t(ell_0-1).               (2.3)
```

Thus `2^t>=n` forces the whole word to be fixed.  For sharpness, put
`W_a=1^a0^(n-a)`.  Directly from its prefix balances,

```text
P_n(W_a)=W_min(2a,n).                                    (2.4)
```

Starting from `W_1=10^(n-1)` proves equality in (2.2), including `n=1`.
Hence all recurrent points are fixed, the functional graph has no nontrivial
cycles, and its finite zeta function is `(1-z)^(-(n+1))`.

## 3. Complete one-step inverse geometry

Let a target word have sign runs

```text
b_1^(l_1) b_2^(l_2) ... b_s^(l_s),       b_j != b_(j+1).
```

Write

```text
C_m = binom(2m,m)/(m+1),       M_m=binom(m,floor(m/2)).
```

Here `C_m` counts Dyck excursions and `M_m` nonnegative meanders.  If `s=1`,
then

```text
|P_n^(-1)(1^n)|=M_n,       |P_n^(-1)(0^n)|=M_(n-1).    (3.1)
```

For `s>=2`, the fibre is empty unless

```text
l_1 is even when b_1=1 and odd when b_1=0,
l_2,...,l_(s-1) are all odd.                            (3.2)
```

When (3.2) holds, every target has the exact product fibre

```text
|P_n^(-1)(y)| = A(b_1,l_1)
                product_(j=2)^(s-1) C_((l_j-1)/2)
                M_(l_s-1),                              (3.3)

A(1,l)=C_(l/2),        A(0,l)=C_((l-1)/2).              (3.4)
```

At every sign change the underlying walk must cross the edge between minus
one and zero.  Cutting at those crossings gives exactly the independent Dyck
excursions and the final meander in (3.3); concatenation is the inverse.
Thus this is a literal bijection, not only a generating-function count.

The run criterion (3.2) also gives

```text
|im P_n| = F_(n+2),                                    (3.5)
```

where `F_1=F_2=1`.  Equivalently, summing the admissible run series gives

```text
sum_(n>=1) |im P_n| z^n = (2z+z^2)/(1-z-z^2).
```

For strict extremality, send the partial-sum walk `S` of a source in the
fibre of `y` to `R_i=|S_i|`.  This is a nonnegative simple-walk meander, and
the map is injective on that fixed fibre because `y_i` recovers the sign of
`S_i`.  If `y` is nonconstant, a sign change forces `R` to return to zero at
a positive time, so the all-up meander `R_i=i` is missing and the injection
is strict.  If `y=0^n`, (3.1) gives `M_(n-1)<M_n` for `n>=2`; for `y=1^n`,
absolute value is a bijection onto all `M_n` meanders.  Therefore

```text
max_y |P_n^(-1)(y)| = binom(n,floor(n/2)),              (3.6)
```

attained uniquely by `1^n` for `n>=2` (both targets tie when `n=1`).  The
excursion product, Fibonacci image, zeta expression, and extremal fibre are
complete system-classification corollaries; the residual lead is the fixed
language and sharp clock in Section 2.

## 4. Exact audit

[`verify_prefix_majority.py`](verify_prefix_majority.py) exhausts every word
for `1<=n<=19`: 1,048,574 states and 5,894,725 integer assertions.  It checks
the literal map, (2.1), the fixed-prefix amplification lemma, every exact
tail, (2.2), every target fibre in (3.1)--(3.4), the Fibonacci image count,
and the unique maximal fibre.  No counterexample occurs.

Reproduce with

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_prefix_majority.py > /tmp/pm.txt
cmp -s /tmp/pm.txt PREFIX_MAJORITY_CANONICAL.txt
```

Finite enumeration is falsification evidence only.  The proof routes are the
balance automaton/fixed-prefix amplification and the independent random-walk
excursion factorization.

## 5. Owner and collision boundary

Husfeldt and Rauhe, [*New Lower Bound Techniques for Dynamic Partial Sums and
Related Problems*](https://doi.org/10.1137/S0097539701391592), study the
dynamic query asking whether the first `i` bits have sum at least
`ceil(i/2)`.  This is exactly the coordinate predicate in (1.1), so both the
predicate and its batched one-step evaluation receive zero originality credit.
Their data-structure problem does not replace the bit string by the complete
answer vector and repeat that full-vector update.

Bounded exact searches for “iterated prefix majority”, “running/cumulative
majority”, “sign of partial sums transform”, and the conjunction of the sharp
clock with the inverse atlas did not locate a literal dynamics owner.  This
non-hit is not novelty or priority evidence.

Michael Wallner's dissertation, *Combinatorics of lattice paths and tree-like
structures* ([DOI 10.34726/hss.2016.38100](https://doi.org/10.34726/hss.2016.38100)),
already gives the alternating positive/negative excursion plus terminal
meander architecture.  Sparre Andersen's fluctuation theorem
([DOI 10.7146/math.scand.a-10407](https://doi.org/10.7146/math.scand.a-10407))
and Erdos--Hunt's sign-change analysis
([primary article](https://msp.org/pjm/1953/3-4/pjm-v3-n4-p01-p.pdf))
own the classical persistence/sign background.  General majority-network
language is also zero credit; a representative primary source is
Goles--Montealegre--Salo--Torma
([DOI 10.1016/j.tcs.2015.09.014](https://doi.org/10.1016/j.tcs.2015.09.014)).
Accordingly no draft may advertise a new Catalan factorisation, Fibonacci
model, random-walk reflection method, or general majority theorem.

The internal firewall is equally explicit:

- P80 already occupies synchronous majority functional graphs; only the
  nested-prefix amplifier is residual here.
- P108 owns Fibonacci dynamics rhetoric, so (3.5) is a corollary only.
- P111 owns binary inversion/lattice-path enumeration, while the present map
  uses a partial-sum sign trace and claims no area polynomial.
- P117, P122, and P126 own run, sharp-clock, and binary-refinement
  silhouettes; no run reversal, record cut, or part splitting occurs here.
- P130 shows that a product fibre and unique maximum do not alone carry a
  paper.

After these deductions, the admissible residual is exactly the repeated
full-vector feedback system, its fixed language, and its sharp
`ceil(log_2 n)` convergence theorem.  The run atlas remains because it
completes the literal system, but all of its classical machinery is credited.
The second independent gate's direct one-step-owner repair is now satisfied;
the internal verdict is `POST_REPAIR_ELIGIBLE`, while external status remains
`HOLD_EXTERNAL`.
