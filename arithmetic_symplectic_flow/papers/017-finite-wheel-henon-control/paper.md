# A finite sieve wheel can force a symplectic Hénon closed orbit, but it fails endogenous A0

**Paper ID:** `017-finite-wheel-henon-control`  
**Candidate ID:** `ASFS-20260913-WHEEL01`  
**Date / status:** `2026-09-13; P0 CONTROL / A0 NEGATIVE`  
**Route state:** `A0 scoped FAIL; A1 local positive control only; A2 NOT EVALUATED; Route B NOT INVOKED`

## Abstract

This candidate realizes a finite sieve wheel in one exact symplectic object,
including an explicit primitive closed orbit. It therefore isolates the issue
that the prior sequential lifts lacked: periodicity. The price is fatal for A0:
the 30-wheel is supplied as a finite arithmetic table/factorization. The same
construction works with any externally selected squarefree wheel. It is a
positive geometry-and-orbit control and a negative arithmetic candidate.

## 1. Same-object construction

Let `B` be a nonnegative smooth bump on `(-1/60,1/60)` with `B(0)=1`, extended
periodically to `S^1=R/Z`. Put `B_j(theta)=B(theta-j/30)` and
`w_j=1_{gcd(j,30)=1}`. Their supports are disjoint, so
`a(theta)=sum_j w_j B_j(theta)` is a fixed smooth function. On
`Q=S^1 x R^2`, define

```text
g(theta,x,y)=(theta+1/30, y, -x+a(theta)y^2).
```

For every theta the fibre map has Jacobian determinant one and explicit inverse
`(theta',x',y') -> (theta'-1/30, -y'+a(theta'-1/30)x'^2, x')`. Hence `g` is a
diffeomorphism. Set `M=T*Q`, `F=T*g`, and roof `tau=1`. This is a single frozen
base map and roof; the cotangent lift preserves the canonical symplectic form.

The lineage retained is finite sieve-word coding -> periodic sequential driver
-> Hénon-type conservative map -> cotangent symplectic realization. It is a
finite, deliberately controlled deformation, not the full prime process.

## 2. Closed-orbit calculation

For every theta, `g(theta,0,0)=(theta+1/30,0,0)`. Therefore

```text
z_theta=(theta,0,0; 0,0,0) in T*Q
```

has `F^30(z_theta)=z_theta`; no smaller positive iterate returns its theta
coordinate. Each is a point on one primitive period-30 orbit (the phases are
cyclic representatives). In the unit-roof suspension, its primitive length is
`T=30`, and its repetitions have `T_r=30r`. This supplies only a local A1
control: it does not enumerate every periodic orbit or define a zeta.

## 3. A0 adversarial controls

The purported arithmetic mechanism is not endogenous.

- The value `P=30` and the values of `w_j` were fixed from the prime factors
  2, 3, and 5 before the map was written.
- Replacing 30 by any externally selected squarefree `P` and using the same
  `gcd(j,P)=1` rule creates the same smooth symplectic construction and a
  primitive orbit of length `P`.
- A shuffled wheel word can likewise be substituted into the bump coefficients
  while retaining the same clock and closed orbit.

Thus the construction recognizes only information already inserted in `P`; it
does not generate a varying-prime mechanism or a logarithmic prime clock. Its
period is the manually selected wheel modulus, not `log p`.

## 4. Gate decision

| Gate | Evidence for this exact candidate | Status | Decision |
| --- | --- | --- | --- |
| P0 | complete same-object card | frozen | retained as control |
| A0 | finite wheel/factorization is exogenous and control-insensitive | scoped FAIL | stop arithmetic advancement |
| A1 | one exact primitive orbit and repetition law | local positive control | no global A1 promotion after A0 failure |
| A2 | no orbit-complete zeta/determinant | NOT EVALUATED | unassigned |
| Route B | no Route-A-ready candidate | NOT INVOKED | prohibited |

The next fork may not inherit this orbit as prime evidence. It must obtain a
recurrent driver without inserting a finite wheel or prime-factor table.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Phase-I prior-work index](../../docs/prior_work/README.md)
