# Theorem package

Status: **PROVABLE AS STATED**.

## Convention

Put `u=x+i y`, `v=v_x+i v_y`, where

```text
v_x=p_x+c y/2,  v_y=p_y-c x/2,  v_z=p_z,
Delta=c^2-2 zeta^2.
```

Let

```text
C_Delta(t)=cos(sqrt(Delta)t/2),
S_Delta(t)=sin(sqrt(Delta)t/2)/(sqrt(Delta)/2),
```

continued by `C=1,S=t` at `Delta=0`, and by the corresponding
`cosh/sinh` expressions when `Delta<0`.

## Main theorem: exact flow and full atlas

For every real `c`, every `zeta>=0`, every real time `t`, and every initial
state, the physical radial variables satisfy

```text
u(t)=exp(-i c t/2)[(C+i c S/2)u(0)+S v(0)],
v(t)=exp(-i c t/2)[zeta^2 S u(0)/2+(C-i c S/2)v(0)].
```

The axial flow is the oscillator formula with its exact `zeta=0` free limit.
If `T_c(q,p)=(q,v)`, the canonical flow is `M_c=T_c^{-1}V_cT_c`; it obeys
`M_c(t)^T J M_c(t)=J`, `M_c(t+s)=M_c(t)M_c(s)`, `det M_c(t)=1`, and preserves
the displayed Hamiltonian.

The boundedness atlas is exhaustive:

- `zeta>0, Delta>0`: every orbit is bounded (bounded dimension 6).
- `zeta>0, Delta=0`: generic radial amplitude grows linearly; an orbit is
  bounded exactly when `v(0)=-i c u(0)/2` (bounded dimension 4).
- `zeta>0, Delta<0`: generic radial exponential rate is
  `sqrt(-Delta)/2`; the all-time bounded subspace is the axial plane
  (dimension 2), while the forward-bounded space has dimension 4 and radial
  stable plane `v(0)=-(sqrt(-Delta)/2+i c/2)u(0)`.
- `zeta=0,c!=0`: the radial motion is a cyclotron circle about a fixed guiding
  centre and the axial motion is free; all-time bounded initial states have
  dimension 5.
- `zeta=c=0`: three-dimensional free motion; the bounded subspace has
  dimension 3.

At `B=0` with `zeta>0`, `Delta<0`, so electrostatic axial confinement alone
is radially unstable.  The canonical involution
`R(x,y,z,p_x,p_y,p_z)=(x,-y,z,p_x,-p_y,p_z)` conjugates the flow at `c` to
the flow at `-c`.

## Stable signed-mode theorem

In `zeta>0, Delta>0`, put `r=sqrt(Delta)`, `sigma=sgn(c)`, and

```text
omega_+=(|c|+r)/2,  omega_-=(|c|-r)/2.
```

Then

```text
u=A_+ exp(-i sigma omega_+ t)+A_- exp(-i sigma omega_- t),
I_+=r|A_+|^2/2,  I_-=r|A_-|^2/2,
I_z=(v_z^2+zeta^2 z^2)/(2 zeta),
H=omega_+ I_+ - omega_- I_- + zeta I_z.
```

The Krein/energy signs are respectively positive modified-cyclotron, negative
magnetron, and positive axial.  The negative magnetron sign is a feature of
the Hamiltonian normal form, not an instability inside the stable chamber.

## Closed-orbit, minimal-period, and strobe theorem

A nonstationary stable-chamber orbit is closed if and only if its active
labeled modes in `(omega_+,omega_-,zeta)` are rationally commensurate.  If the active
frequencies are `n_j g` with positive integers of gcd one, its minimal period
is exactly `2 pi/g`.  No inactive frequency may enlarge that period.

For a stable strobe time `tau`, put `(f_1,f_2,f_3)=(omega_+,omega_-,zeta)`;
the indices retain their mode labels even when two frequencies coincide.  Then

```text
dim Fix M_c(tau)
 = 2 * #{j in {1,2,3}: f_j tau in 2 pi Z}.
```

On the critical face, the radial fixed dimension is two exactly when
`c tau/2` is in `2 pi Z`; the Jordan direction never fixes.  On
`zeta=0,c!=0`, the fixed dimension is three, plus two at a cyclotron return.

## Proof skeleton

1. Hamilton's equations give the two displayed second-order equations.
2. The rotation `u=exp(-ict/2)w` gives `w''+Delta w/4=0`; its entire
   fundamental pair proves the flow formula and all three parameter chambers.
3. The gauge map is linear and invertible.  Direct differentiation of the
   Hamiltonian flow gives `A^T J+JA=0`, hence `exp(tA)` is symplectic and
   energy preserving.
4. In the stable chamber the two radial exponentials are distinct.  Solving
   for their amplitudes and substituting into `H` cancels cross terms and
   yields the signed action form.
5. Bounded-subspace dimensions follow from the oscillatory, Jordan, hyperbolic,
   Landau/free decompositions.
6. A finite sum of distinct mode rotations returns exactly when every active
   phase returns; the gcd normalization proves minimality, and the same block
   decomposition gives every fixed-space dimension.

## Scope and nonclaims

The theorem concerns the ideal axially symmetric trap only.  No claim is made
for imperfections, damping, many-body coupling, experimental accuracy,
arithmetic local data, Euler factors, root numbers, automorphy, a target
counting law, a target divisor, or a Hilbert--Polya operator.
