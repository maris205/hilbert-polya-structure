# Stage-1 hostile gate: cyclic sign Laplacian (`CSL`)

**Reviewer role:** process-separated hostile gate.  I did not use or import a
CSL author/scout verifier.  **External lifecycle:** `HOLD_EXTERNAL`.

## Decision

```text
CSL: KILL_EXACT_TCSD_FACTOR
severity: FATAL INTERNAL/SAME-BATCH COLLISION
promotion residual: NONE
```

The small-box dynamics are correct, but CSL is not merely close to TCSD.  On
the entire frozen ternary carrier it is exactly a shifted second iterate of
TCSD.  Its all-size clock, recurrent involution, and every-target fibre
problem are therefore inherited TCSD statements.  A separate paper slot or
theorem-spike recommendation is not defensible.

## 1. Frozen literal maps and orientation

Index by `Z/nZ`, let `sgn` take values in `{-1,0,1}`, and use the TCSD
orientation

```text
D(x)_i = sgn(x_(i+1)-x_i),
rho(x)_i = x_(i+1).
```

The proposed CSL update is

```text
C(x)_i = sgn(x_(i-1)+x_(i+1)-2x_i).                  (1)
```

All coordinates in (1) are read from the old state.  This gate covers the
ternary carrier only; enlarging the alphabet would be a different system and
would invalidate several advertised claims.

## 2. Exact factor identity

### Local three-chain lemma

For `u,v,w in {-1,0,1}`, put `a=v-u` and `b=w-v`.  Then

```text
sgn(b-a)=sgn(sgn(b)-sgn(a)).                          (2)
```

If `a,b` have different signs or one is zero, (2) follows directly from
their order.  If both are positive, then `u<v<w` in a three-element chain,
so necessarily `(u,v,w)=(-1,0,1)` and `a=b=1`.  If both are negative, the
only possibility is `(1,0,-1)` and `a=b=-1`.  These exhaust all cases.

Apply (2) with

```text
a=x_i-x_(i-1),       b=x_(i+1)-x_i.
```

The left side is (1), while the right side is

```text
sgn(D(x)_i-D(x)_(i-1))=D^2(x)_(i-1).
```

Therefore, with no exceptional cyclic length,

```text
C = rho^(-1) D^2.                                    (3)
```

Because `D` commutes with cyclic shifts,

```text
C^t = rho^(-t) D^(2t)                                (4)
```

for every `t>=0`.  Equation (3) is an exact literal factor/iterate identity,
not an analogy, a first-front projection, or a shared proof technique.

The ternary hypothesis is essential but does not rescue CSL.  On a longer
chain, adjacent positive increments can have unequal magnitudes and (2) can
fail.  The proposed carrier is exactly the one on which (3) holds.

## 3. All-size clock is mechanically transferred

Let

```text
K_n={x:D^4(x)=rho^2(x)}
```

be the TCSD recurrent core.  It is shift invariant.  From (4),

```text
C^t(x) in K_n  iff  D^(2t)(x) in K_n.
```

Hence the pointwise tails obey the exact identity

```text
tau_C(x)=ceil(tau_D(x)/2).                             (5)
```

Conversely, if a point is periodic for `C`, then (4), followed by a multiple
of `n`, makes it periodic for `D`; it therefore lies in `K_n`.  On `K_n`,
`D` and `rho` are bijections, so `C` is bijective.  Thus CSL and TCSD have
the same recurrent set.

The TCSD sharp maxima are `H_1=1`, `H_n=n-1` for even `n`, and `H_n=n-2`
for odd `n>=3`.  Equation (5) immediately gives

```text
max tau_C = 1                  (n=1),
            floor(n/2)         (n>=2).                (6)
```

Moreover, on `K_n`,

```text
C^2=rho^(-2)D^4=id,
```

so every recurrent CSL period is one or two.  CSL has only the zero fixed
point: if `x_i=1`, the expression in (1) is nonpositive and cannot have sign
`1`; if `x_i=-1`, it is nonnegative and cannot have sign `-1`.  Therefore a
fixed word has every coordinate zero.  These are sound theorems, but (3)--(6)
show that the temporal axis is a TCSD subsampling, not an independent
mechanism.

## 4. Fibre theorem is a two-step TCSD fibre

For every labelled target `y`, (3) gives the exact set equality

```text
C^(-1)(y) = D^(-2)(rho(y)),                            (7)
```

and more generally

```text
C^(-t)(y) = D^(-2t)(rho^t(y)).                         (8)
```

Thus any local transfer matrix for CSL is a presentation of a prescribed
two-step TCSD inverse problem.  A new matrix reduction may be useful
bookkeeping, but it cannot furnish an independent inverse axis after the
literal factor (3) is disclosed.

The independent exhaustive controls agree with the proposed maximum-fibre
surface:

| `n` | max one-step CSL fibre | number of maximizers | equality pattern |
|---:|---:|---:|---|
| 1 | 3 | 1 | `0` |
| 2 | 3 | 3 | `00` and the two alternating signs |
| 3 | 3 | 7 | `000` and the six one-defect sign words |
| 4 | 11 | 2 | the two alternating signs |
| 5 | 9 | 10 | cyclic sign words with one doubled sign |
| 6 | 39 | 2 | the two alternating signs |
| 7 | 31 | 14 | cyclic sign words with one doubled sign |
| 8 | 131 | 2 | the two alternating signs |
| 9 | 105 | 18 | cyclic sign words with one doubled sign |
| 10 | 443 | 2 | the two alternating signs |
| 11 | 355 | 22 | cyclic sign words with one doubled sign |

For odd length, “alternating target” must mean the displayed one-doubled-sign
cyclic pattern; strict cyclic alternation is impossible.  This boundary
language should be retained if the killed calculation is archived.  The
equality data do not weaken the kill: by (7), they are extrema of the
two-step TCSD target fibres.

## 5. Independent exact controls

A fresh inline enumerator, written from (1) and the TCSD definition rather
than imported code, exhausted every ternary word for `1<=n<=11`.  It made
**2,408,356** checks, including:

- (3) on every state;
- (4) for `t=0,1,2,3` on every state;
- equality of the CSL recurrent set with `K_n`;
- (5), the sharp boundary (6), `C^2=id` on `K_n`, and uniqueness of zero as
  fixed point;
- `C(x)=-x` for every nonzero recurrent state in these boxes; and
- every one-step target fibre and all maximizers in the table above.

No author verifier, canonical transcript, or precomputed transition table was
read to obtain these checks.

## 6. Collision subtraction

| prior surface | verdict |
|---|---|
| TCSD (`scouting/word_poset_lane`) | **Fatal exact hit:** CSL is `rho^-1 D^2`.  The sharp clock is `ceil(tau_D/2)` and CSL fibres are rotated two-step TCSD fibres. |
| P178 state-selected finite differences | Secondary vocabulary/proof-engine warning only.  P178 uses a state-selected translation difference on functions over `F_p`; it is not needed for the fatal decision. |
| P164 equality feedback and P196 cyclic Gödel implication | Local ternary/cyclic-CA and transfer-matrix language is already dense, but again the exact TCSD identity decides the gate before these softer comparisons matter. |

## 7. Required archival boundary

If CSL materials are kept as a killed spike, they must state (3) prominently,
attribute all temporal consequences to TCSD subsampling, describe (7) before
any fibre-matrix calculation, preserve the `n=1,2,3` and odd-maximizer
exceptions, and carry `KILL_EXACT_TCSD_FACTOR / HOLD_EXTERNAL`.  They must not
be counted in the breadth denominator as an independent survivor.

**Final disposition:** `KILL_EXACT_TCSD_FACTOR`.  No open mathematical
finding is needed to reach this decision; the system is mathematically clean
and promotion-ineligible for an exact internal reason.

