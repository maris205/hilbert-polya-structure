# Complementary power--GCD divisor dynamics

**Stage:** replacement proof spike.  **Disposition:** conditional reserve,
pending an independent owner/value gate.  **External status:**
`HOLD_EXTERNAL`.

## 1. Literal system and separation

Fix an integer `k>=2` and

```text
n = product_i p_i^(e_i),       e_i>=1.
```

On the complete divisor lattice of `n`, iterate

```text
T_(n,k)(d) = n / gcd(n,d^k).                              (1.1)
```

This is not ordinary power iteration: valuation factorization sends a divisor
with exponent vector `a=(a_i)` to the coordinatewise reflected truncation

```text
f_(e,k)(a) = max(e-ka,0).                                 (1.2)
```

The closest current-batch system is `A02`, but the mechanisms are different.
`A02` is squarefree and graph-coupled through prime divisibilities; (1.1) is
prime-power and completely local, with expanding affine transients around a
rational centre.  That distinction does not by itself justify using two
divisor-lattice papers in one batch, so this candidate remains a reserve until
the portfolio gate compares the final replacement pool.

## 2. Scalar theorem package

For `0<=a<=e`, put `c=e/(k+1)`.  The recurrent set of (1.2) is exactly

```text
{0,e} union ({c} if c is integral).
```

The endpoints form a two-cycle, and the optional centre is fixed.  There are
no other cycles.  Indeed `f` is order-reversing, and solving `f^2(a)=a` in
the truncated and untruncated regions gives only `a=0,e,c`.

For a nonrecurrent state, its exact entrance time `tau_(e,k)(a)` into the
endpoint cycle has a parity-sensitive logarithmic formula.  If `(k+1)a>e`,
it is the least odd `t>=1` such that

```text
k^t ((k+1)a-e) >= e.                                     (2.1)
```

If `0<a<c`, it is the least even `t>=2` such that

```text
k^t (e-(k+1)a) >= e.                                     (2.2)
```

The recurrent states have depth zero.  Before the entrance time, the full
iterate is

```text
f^t(a) = [e+(-k)^t((k+1)a-e)]/(k+1),       0<=t<tau.      (2.3)
```

At time `tau` the truncation reaches zero, after which the endpoint phase
alternates.  Thus (2.1)--(2.3) determine every iterate, not merely an upper
bound on the tail.

There is also a closed cumulative depth count.  Let `N_(e,k)(t)` be the
number of scalar states with depth at most `t`, and set

```text
R = 2 + [(k+1) divides e].
```

For `t>=1`, let `o(t)` be the largest odd integer at most `t`; for `t>=2`,
let `v(t)` be the largest even integer at most `t`.  Then

```text
N_(e,k)(t) = R
 + [t>=1] max(0, e-ceil((e+ceil(e/k^o(t)))/(k+1)))
 + [t>=2] max(0, floor((e-ceil(e/k^v(t)))/(k+1))).        (2.4)
```

Finally, every one-step scalar target has an exact fibre:

```text
|f^(-1)(b)| = e-ceil(e/k)+1,  b=0;
             1,              b>0 and k divides e-b;
             0,              otherwise.                 (2.5)
```

## 3. Product atlas on all divisors

Put `delta_i=[(k+1)|e_i]`.  Coordinate factorization yields immediately:

- the complete recurrent set has size `product_i(2+delta_i)`;
- the fixed set has size `product_i delta_i` (zero or one);
- the exact number of two-cycles is
  `(product_i(2+delta_i)-product_i delta_i)/2`;
- the tail of exponent vector `a` is `max_i tau_(e_i,k)(a_i)`;
- the number of divisors with tail at most `t` is
  `product_i N_(e_i,k)(t)`, so consecutive differences give every exact
  depth layer; and
- the one-step fibre of every target divisor is the product of (2.5).

This gives a complete temporal and inverse-geometry atlas for every `n` and
every `k>=2`, including all fixed points, cycles, basins, exact depth layers,
and target fibres.

## 4. Exact falsification audit

[`verify_complementary_power_gcd.py`](verify_complementary_power_gcd.py)
checks the literal integer map against valuation coordinates and audits all
claims above on 1,600 parameter boxes: ranks one through four, `2<=k<=7`,
and exponents as large as 80.  The frozen run covers 215,855 states and
3,111,459 exact assertions.  It uses Python integers only.  The largest
observed tail is eight; no counterexample occurs.

Reproduce with

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_complementary_power_gcd.py > /tmp/cpg.txt
cmp -s /tmp/cpg.txt CANONICAL.txt
```

Finite enumeration is falsification evidence, not a proof.  The proof is the
valuation reduction, the two-region solution of `f^2(a)=a`, the affine
recurrence (2.3), and coordinate factorization.

## 5. Owner and value boundary

Exact searches for the displayed divisor map and its valuation recurrence did
not locate a literal iteration owner in the bounded pass.  A non-hit is not a
novelty or priority certificate.  R. M. Dacic, *Properties of monotone
mappings in partially ordered sets*, Publ. Inst. Math. 30(44) (1981), 33--39,
is treated as background for monotone/antitone fixed-point structure.  Generic
divisor-lattice factorization, order reversal, and the fact that an antitone
chain map has periods at most two receive zero contribution credit.

The residual is only the conjunction tied to the literal arithmetic map:
the parity-sensitive exact transient formula, every depth layer, the complete
product recurrence census, and every-target multiplicative fibre.  A separate
hostile reviewer must still decide whether that residual is sufficiently far
from P100's valuation erosion and whether the batch may contain it together
with `A02`.
