# Proof spike: parallel Glaisher compression

Status: **PROVED / SEND TO INDEPENDENT OWNER-VALUE GATE / EXTERNAL HOLD**.

## 1. Literal system

Fix an integer base `b>=2`.  On the integer partitions of `n`, replace every
complete batch of `b` equal parts `j` by one part `bj`, for all part sizes
simultaneously.  In multiplicities,

```text
m'_j = (m_j mod b) + 1_[b|j] floor(m_(j/b)/b).
```

Weight is preserved.  Whenever the state changes, the number of parts drops
strictly, so every orbit reaches a fixed point and no nontrivial cycle exists.

Write every part uniquely as `q b^k`, with `b` not dividing `q`.  The dynamics
is a product of independent one-sided carry towers

```text
m'_0 = m_0 mod b,
m'_k = (m_k mod b) + floor(m_(k-1)/b),  k>=1.
```

The terminal base-`b` normalization and the equality between partitions with
multiplicities below `b` and partitions with no part divisible by `b` are the
classical Glaisher bijection.  They receive zero contribution credit.

## 2. Sharp global clock

After `t` rounds, the first `t` levels of every carry tower are permanently
stable and have multiplicity below `b`.  This follows by induction: level zero
is reduced modulo `b` in the first round and has no incoming edge; once levels
below `t` are stable, level `t` receives no later carry after its next modulo
reduction.

If a state is still nonfixed after `t` rounds, some unstable level has index at
least `t`.  Its `b` equal parts already carry weight at least `b^(t+1)` (and an
additional factor `q>=1`).  Therefore every partition of `n` has depth at most

```text
floor(log_b n).
```

This is sharp for every `n`.  Put `r=floor(log_b n)` and `s=n-b^r`.  For
`r>=1`, take `b+s` copies of `1` and `b-1` copies of each
`b,b^2,...,b^(r-1)`.  Its weight is `n`.  A carry wave reaches one new level
per round: before the wave arrives, the next level still contains `b-1`
parts, so the incoming carry makes it unstable.  Its depth is exactly `r`.
For `r=0`, every partition is already fixed.

## 3. Every one-step fibre

For one carry tower, let `y_k` be the target multiplicities.  Write a source
coordinate as `x_k=b c_k+epsilon_k`, with `0<=epsilon_k<b`.  The target
equations are

```text
y_0=epsilon_0,
y_k=epsilon_k+c_(k-1),  k>=1.
```

Thus a target has a preimage iff `y_0<b`.  Conditional on this, for each
`k>=1` choose `epsilon_k` independently from
`0,...,min(b-1,y_k)` and set `c_(k-1)=y_k-epsilon_k`.  This reconstructs one
finite-support source, and every source arises uniquely.  Multiplying across
towers gives

```text
|Phi^-1(lambda)| = 0,
  if some part q with b not dividing q has multiplicity at least b;

|Phi^-1(lambda)| = product_(b|j) min(b,m_j(lambda)+1),
  otherwise.
```

This is a pointwise formula, not merely an aggregate count.

## 4. All iterated images

For every `t>=1`,

```text
lambda in Im(Phi^t)
iff m_j(lambda)<b for every j not divisible by b^t.
```

Necessity is the stable-low-level lemma.  For sufficiency, reverse one carry
round tower by tower using the preceding remainder/carry equations while
requiring the first `t-1` source levels to be below `b`; the assumed first
`t` target levels make this possible, and the finite zero tail fixes the
boundary.  Induction on `t` completes the construction.

Consequently the exact image-size generating function is

```text
sum_(n>=0) |Im(Phi^t on P_n)| x^n
 = product_(b^t does not divide j) (1+x^j+...+x^((b-1)j))
   times product_(b^t divides j) 1/(1-x^j).
```

As `t` exceeds `log_b n`, this specializes coefficientwise to the classical
Glaisher fixed-point product.  The residual is the complete temporal image
tower, not the owned limiting identity.

## 5. Evidence and claim ceiling

The exact verifier exhausts partitions through the declared ranges, compares
literal fibres with the pointwise product, tests all iterated images, sharp
depth witnesses, coefficient products, and the Glaisher limit.  It is a
falsification control, not a proof or owner certificate.

A bounded exact-phrase and translated search located the classical sequential
merge/split Glaisher bijection and its general base form, but no source for the
literal synchronous self-map, its sharp per-`n` clock, pointwise fibres, or
complete image tower.  This is only a bounded non-hit.  No novelty, priority,
minimality, asymptotic, or external-release claim is permitted.
