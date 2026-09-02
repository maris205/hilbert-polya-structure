# Proof package — P152

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## 1. Literal quotient

Let `x_i` be the imbalance bit of page `i` and `K=sum_i x_i`.  A private
edge belongs to one page, so flipping either private edge of the chosen active
page sends `x_i=1` to zero and preserves every other bit.  The common spine
belongs to all pages, so its flip complements the entire bit vector.  Thus,
from every full sign state with `K=k>0`,

```text
k -> k-1  with mass 2/3,
k -> r-k  with mass 1/3.
```

The probabilities depend only on `k`, proving strong lumpability.  If the
targets coincide, their masses add.

## 2. Absorption before transforms

Pre-generate the private/spine type of each future edge choice.  Every type is
private with probability `2/3`, independently of the current state.  On the
event that the next `r` types are private, each active update lowers `K` by
one, so absorption occurs within the block.  Therefore, uniformly over all
states at a block boundary,

```text
P(no absorption during next r epochs) <= 1-(2/3)^r.
```

The Markov property gives

```text
P_k(T>nr) <= [1-(2/3)^r]^n.
```

This proves almost-sure absorption and finiteness of every moment needed in
the paper.

## 3. Joint transform elimination

For `F_k=E_k[z^T u^J]`, first-step conditioning gives

```text
3F_k/z = 2F_{k-1}+uF_{r-k}.                 (1)
```

For `1<=k<r`, use (1) at `k`, at `r-k`, and at `k+1`.  The first and reflected
equations yield

```text
uF_{r-k}=3F_k/z-2F_{k-1},
F_{r-k-1}=3F_{r-k}/(2z)-(u/2)F_k.
```

Substitution into the `k+1` equation, without dividing by `u`, gives

```text
F_{k+1}=2 xi F_k-F_{k-1},
xi=[9+z^2(4-u^2)]/(12z).
```

With `F_0=1`, the solution is

```text
F_k=U_{k-1}(xi)F_1-U_{k-2}(xi),  U_{-1}=0.
```

At the terminal count,

```text
F_r=(2z/3)F_{r-1}+zu/3.
```

Substitution gives the frozen numerator and denominator for `F_1`.  The
argument is an identity in the rational-function field; probability-transform
values at removable points come from the Bellman system.

## 4. Small and singular boundaries

- `r=1`: every first update absorbs, so `F_1=z(2+u)/3`.
- `r=2`: at count one, a spine flip is a self-loop, hence
  `F_1=2z/(3-zu)`.  In the raw Chebyshev ratio, the numerator is `3+zu` and
  `6xi-2z=(3-zu)(3+zu)/(2z)`; cancellation must precede evaluation.
- `z=0`: `xi` is undefined, while Bellman gives `F_0=1` and `F_k=0` for
  `k>0`.
- If `k-1=r-k`, the two update types are distinct but their quotient arrows
  have the same target, so the probabilities add.

## 5. Mean and extrema

The mean Bellman system is

```text
m_0=0,
m_k=1+(2/3)m_{k-1}+(1/3)m_{r-k}.
```

Using the equations at `k`, `r-k`, and `k+1` eliminates the reflected term:

```text
m_{k+1}-2m_k+m_{k-1}=-1.
```

Together with `m_r=1+(2/3)m_{r-1}`, this has the unique solution

```text
m_k=k(r+2-k)/2.
```

The quadratic is strictly concave.  On `1<=k<=r`, its endpoint comparison
gives the unique minimum `k=1` for `r>1`; its vertex at `(r+2)/2` gives the
even and odd maximizing sets in the theorem.  The `r=1` domain has one point.

## 6. Parity and exact inverse

Let `h_k=E_k[(-1)^J]`.  A private update preserves the sign, while a spine
update reverses it:

```text
h_0=1,
h_k=(2/3)h_{k-1}-(1/3)h_{r-k}.
```

The affine candidate

```text
h_k=(r+2-2k)/(r+2)
```

satisfies every equation.  The absorption certificate lets the bounded
first-step identity be iterated to the stopping time, proving that it is the
desired expectation.  Hence

```text
q=P_k(J odd)=k/(r+2).
```

Put `R=r+2`.  Then

```text
m=k(R-k)/2,
q(1-q)=k(R-k)/R^2,
2m/[q(1-q)]=R^2.
```

Every genuine nonabsorbing observation therefore has `m>0` and `0<q<1`.
For an arbitrary exact real candidate pair, failure of either domain condition
means immediate infeasibility; in particular, no real square root is taken
from a nonpositive scale. Necessity of the remaining integer conditions
follows.  Conversely, if the positive
square root `R` is an integer at least three and `k=qR` is an integer in
`[1,R-2]`, then `r=R-2` is a valid book and its formulas reproduce `(m,q)`.
This proves exact feasibility and uniqueness.  The central case `q=1/2` is
regular.  Parity alone collides at `(r,k)=(1,1),(4,2)`; mean alone collides at
`(2,2),(3,1)`.

## 7. Evidence boundary

The symbolic derivations above prove the all-parameter statements.
`verify_p152.py` supplies finite exact falsification only.  Round 1 added
bounded exact rejection pressure for the inverse iff, literal assertions for
both one-statistic collisions, and Fraction checks of private-block mass and
finite tail instances; none replaces the symbolic converse or Markov
iteration.  Primary-source subtraction is maintained separately in
`SOURCE_VERIFICATION.md`; no bounded search non-hit is used as a mathematical
or ownership proof.
