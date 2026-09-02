# QNC all-time theorem contract — independently corrected

**Gate date:** 2026-09-03 UTC  
**Mathematical status:** proved below and exact-tested  
**Selection status:** `KILL`  
**External status:** `HOLD_EXTERNAL`

This file records the strongest correct theorem.  It is **not** a paper
contract: the owner subtraction in `OWNER_AUDIT.md` leaves only one narrow
specialized axis, so no P166 drafting is authorized.

## 1. Literal system and conventions

Let `p` be an odd prime, `e>=2`, and

```text
X_{p,e}=p Z / p^e Z,
F(x)=x(x+p) mod p^e.
```

The carrier and codomain both have `p^(e-1)` elements.  Divisibility and
quotients below are statements about residue classes; for example, if
`p^(t+1)|y`, then `y/p^(t+1)` is well-defined modulo `p^(e-t-1)`.  Put
`v_p(0)=e` when a valuation is used modulo `p^e`.

## 2. Exact iterates and target transport

For `x=pu`, direct substitution gives, for every `t>=1`,

```text
F^t(pu)=p^(t+1) P_t(u) mod p^e,                         (2.1)
P_1(u)=u(u+1),
P_{s+1}(u)=P_s(u)+p^s P_s(u)^2.                         (2.2)
```

For `1<=t<=e-1`, put `k=e-t-1`.  On `Z/p^k Z` define

```text
phi_s(a)=a+p^s a^2,
B_1=id,
B_t=phi_{t-1} o ... o phi_1.                            (2.3)
```

Then `P_t=B_t o P_1`.  Every `phi_s` is a permutation, since

```text
phi_s(a)-phi_s(c)=(a-c)(1+p^s(a+c))
```

and the second factor is a unit.  Hence `B_t` is a permutation.

For a target `y in X_{p,e}`:

* if `p^(t+1)` does not divide `y`, then `(F^t)^(-1)(y)` is empty;
* otherwise let

  ```text
  b=y/p^(t+1) mod p^k,
  a=B_t^(-1)(b),
  rho_{p^k}(d)=#{z mod p^k:z^2=d mod p^k}.
  ```

  Then

  ```text
  |(F^t)^(-1)(y)|=p^t rho_{p^k}(1+4a).                  (2.4)
  ```

Indeed, the target equation is `u(u+1)=a mod p^k`.  Completing the
square gives `(2u+1)^2=1+4a`; each solution modulo `p^k` has exactly `p^t`
lifts modulo `p^(k+t)=p^(e-1)`.

## 3. Complete fibre spectrum and image

For `1<=t<=e-1` and `k=e-t-1`:

* if `k=0` (equivalently `t=e-1`), the sole image target is zero and its
  fibre is the whole carrier, of size `p^t=p^(e-1)`;
* if `k>=1`, one target, characterized by
  `1+4B_t^(-1)(y/p^(t+1))=0 mod p^k`, has fibre

  ```text
  p^(t+floor(k/2));                                      (3.1)
  ```

* for every `0<=r<=floor((k-1)/2)`, exactly

  ```text
  (p-1)p^(k-2r-1)/2                                     (3.2)
  ```

  targets have fibre `2p^(t+r)`.

Thus, for `k>=1`,

```text
|Im(F^t)|=1+(p-1)/2 sum_{r=0}^{floor((k-1)/2)} p^(k-2r-1),   (3.3)
```

and the number of zero-fibre targets in the **whole codomain** is
`p^(e-1)-|Im(F^t)|`.  This complement includes both targets not divisible by
`p^(t+1)` and divisible targets whose transported discriminant is a
nonsquare; the two causes must not be conflated.

The proof is the standard odd-prime square census.  The congruence
`z^2=d mod p^k` has `p^floor(k/2)` roots for `d=0`; if
`v_p(d)=2r<k`, it has `2p^r` roots precisely when its unit part is a square,
and otherwise none.  There are `(p-1)p^(k-2r-1)/2` nonzero square residues
of valuation `2r`.

## 4. Time boundaries

The following are separate branches, not notational continuations of (2.4).

* `t=0`: `F^0` is the identity, so every target has fibre one.
* `t=e-1`: this is exactly the `k=0` branch above.
* `t>=e-1`: `F^t` is constant zero.  The zero fibre has size `p^(e-1)`
  and every other fibre is empty.  In particular, writing its size as `p^t`
  after `t=e-1` would be false.
* `e=2`: the only positive-time branch is already the constant map at
  `t=1`; the inner ball below is the singleton `{0}`.

For context, the older temporal axis is also correct: zero is the unique
cycle and the sharp absorption height is `e-1`.  If `v_p(x)>=2`, one
valuation digit is gained at every step.  The first step from the outer
shell has the single cancellation statistic `v_p((x/p)(x/p+1))`.  This axis
is historical zero-credit material for the present re-entry gate.

## 5. Finite Koenigs chart on the inner ball

Let `I_{p,e}=p^2 Z/p^e Z`.  For `x in I_{p,e}`, define

```text
H_e(x)=x product_{j>=0}(1+F^j(x)/p) mod p^e.             (5.1)
```

The product is finite at precision `p^e`: `v_p(F^j(x))>=j+2`, so all
sufficiently late factors are one modulo the precision relevant after
multiplication by `x`.  It is independent of representatives.  Factoring
`F(x)=px(1+x/p)` and shifting the product proves

```text
H_e(F(x))=p H_e(x).                                      (5.2)
```

Moreover, `H_e` is an isometric permutation of `I_{p,e}`.  To see this,
write `H_e(x)=xG(x)`.  Each `G(x)` is a unit and, for `x,y in I_{p,e}`,

```text
v_p(F^j(x)-F^j(y))=v_p(x-y)+j,
v_p(G(x)-G(y))>=v_p(x-y)-1.
```

In

```text
H_e(x)-H_e(y)=(x-y)G(x)+y(G(x)-G(y)),
```

the first term has valuation `v_p(x-y)` and the second has valuation at
least one larger.  Hence equality of distances follows, and finiteness gives
bijectivity.

Consequently, for every `t>=0`,

```text
Im(F^t|I_{p,e})=p^min(e,t+2) Z/p^e Z,
```

where the right side is `{0}` when the exponent is `e`.  Every target in
this image has exactly

```text
p^min(t,e-2)                                             (5.3)
```

inner-ball sources, and every other target has none.  The ball `p^2` is also
the natural sharp full-conjugacy ball: the other root `-p` lies on its
boundary `v_p=1`.

## 6. Owner-subtracted ceiling

All formulas in Sections 2--5 are true.  They do not, however, supply two
independent creditable axes after subtraction:

1. the positive spectrum in Section 3 is exactly the already owned one-step
   QNC spectrum at precision `p^(k+2)`, with every source repeated
   `p^(t-1)` times and targets relabelled by `B_t`; that one-step spectrum is
   the desJardins--Zieve critical-residue-class theorem (together with its
   nonsingular-class branch);
2. the inner-ball conjugacy is the attracting hyperbolic linearization
   theorem of Lindahl--Zieve specialized to `f(x)=px+x^2`; their iterative
   logarithm description gives (5.1) immediately from
   `F^n(x)/p^n=x product_{j<n}(1+F^j(x)/p)`.

The explicit target permutation `B_t^(-1)` is a clean finite specialization
not located verbatim in the bounded search.  Alone, it is below the batch's
two-axis paper threshold.  Verdict: **`KILL`**; retain only as an internal
exact lemma package under `HOLD_EXTERNAL`.
