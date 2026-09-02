# Exact theorem and proof package — HCS-C284

## Claim

For `N>=3`, let `N` identical planar point vortices of circulation `Gamma>0`
occupy the vertices of a regular polygon of radius `R>0`.  With the Hamiltonian

`H=-(Gamma^2/(2*pi))*sum_{j<k} log|z_j-z_k|`

and the convention `Gamma*z_j'=J*grad_j H`,
`J=[[0,1],[-1,0]]`, the polygon rotates with

`Omega=Gamma*(N-1)/(4*pi*R^2)`.

In radial–tangential discrete Fourier coordinates, the rotating-frame
linearization has blocks

`L_m=c*[[0,q_m],[-sigma_m,0]]`,

where

`c=Gamma/(4*pi*R^2)`, `q_m=m*(N-m)`, and
`sigma_m=2*(N-1)-q_m`.

After fixing the center of vorticity and angular impulse and quotienting
rotation, the regular polygon is linearly elliptic for `3<=N<=6`; for `N=7`
only modes `m=3,4` are linearly degenerate; and every `N>=8` has a real
hyperbolic pair.  The `N=7` statement is only linear and makes no claim about
nonlinear stability.

## Status

`PROVABLE AS STATED`.

## Assumptions

- `N` is an integer with `N>=3`.
- All vortices have the same circulation `Gamma>0`.
- `R>0`, so no two polygon vertices collide.
- Stability means the spectrum of the linearized rotating-frame Hamiltonian
  system on the centered, fixed-angular-impulse rotational slice.
- No assertion is made about nonlinear stability at the degenerate heptagon.

## Notation and convention

Write `theta_j=2*pi*j/N` and

`a_j=R*(cos(theta_j),sin(theta_j))`.

The matrix `J` rotates a vector clockwise by `pi/2`; therefore
`-J` is the counterclockwise generator.  With this convention, a positive
circulation polygon rotates counterclockwise.  Let

`G=H+(Gamma*Omega/2)*sum_j |z_j|^2`

be the rotating-frame augmented Hamiltonian.  The linearization at the
polygon is

`L=J_N*Gamma^(-1)*D^2G(a)`.

The local radial and counterclockwise tangential basis at vertex `j` is the
rotation matrix `Q_j=[e_r,j,e_t,j]`.  The unitary DFT uses modes
`m=0,...,N-1`.

## Proof strategy and dependency map

1. Differentiate the source Hamiltonian to obtain the angular velocity and
   raw Cartesian pair Hessian.
2. Rotate every `2 by 2` Cartesian block into local radial–tangential bases.
3. Diagonalize the resulting block-circulant Hessian by the DFT.
4. Evaluate its only nontrivial trigonometric sum by root-of-unity
   orthogonality.
5. Square each `2 by 2` Hamiltonian block and classify its sign.
6. Remove, rather than misclassify, the rotation, scale, and translation
   directions.
7. Maximize `m*(N-m)` to prove the sharp `6/7/8` trichotomy.

## Proof

### Step 1: relative equilibrium and angular velocity

For `d_jk=z_j-z_k`, differentiation gives

`grad_j H=-(Gamma^2/(2*pi))*sum_{k!=j} d_jk/|d_jk|^2`.

At `j=0`, each summand has radial component

`R*(1-cos(theta_k))/(2*R^2*(1-cos(theta_k)))=1/(2R)`.

The tangential components cancel in the pair `k,N-k`.  Rotational covariance
therefore yields

`sum_{k!=j} (a_j-a_k)/|a_j-a_k|^2=((N-1)/(2R^2))*a_j`.

Consequently

`grad_j H(a)=-Gamma*Omega*a_j`,

with `Omega=Gamma*(N-1)/(4*pi*R^2)`.  Thus `grad G(a)=0`, and Hamilton's
equation gives rigid counterclockwise rotation at angular velocity `Omega`.

### Step 2: raw Cartesian Hessian

For a nonzero vector `d`, define

`A(d)=I/|d|^2-2*d*d^T/|d|^4`.

The pair contributions are

`D^2_jj H=-(Gamma^2/(2*pi))*A(d_jk)`,

`D^2_jk H=+(Gamma^2/(2*pi))*A(d_jk)`.

The augmented term adds `Gamma*Omega*I` to each diagonal block.  These
formulas specify the complete raw `2N by 2N` Hessian used by the independent
checker; no Fourier formula enters that construction.

### Step 3: local blocks

Set `theta=theta_k` and `d=a_0-a_k`.  Since

`|d|^2=4*R^2*sin(theta/2)^2`,

direct substitution gives

`A(d)=(1/(4*R^2*sin(theta/2)^2))*[[cos(theta),sin(theta)],[sin(theta),-cos(theta)]]`.

Multiplication on the right by `Q_k` turns the displayed matrix into
`diag(1,-1)`.  Hence the local off-diagonal block in the first block row is

`B_k=c/(1-cos(theta_k))*diag(1,-1)`, `k!=0`,

where `c=Gamma/(4*pi*R^2)`.  The diagonal block follows either from the raw
formula or from the translation-invariant Hessian row sum before augmentation.
Writing

`A_N=sum_{k=1}^{N-1} 1/(1-cos(theta_k))`,

one obtains

`B_0=c*diag(2*(N-1)-A_N,A_N)`.

The sine parts of every Fourier sum cancel between `k` and `N-k`.

### Step 4: the exact DFT block

Define

`S_m=sum_{k=1}^{N-1}(1-cos(m*theta_k))/(1-cos(theta_k))`.

Using the blocks from Step 3 gives

`Gamma^(-1)*D^2G_hat_m=c*diag(2*(N-1)-S_m,S_m)`.

It remains to evaluate `S_m`.  For `z=exp(i*theta)`,

`(1-cos(m*theta))/(1-cos(theta))=|1+z+...+z^(m-1)|^2`.

Let `zeta=exp(2*pi*i/N)`.  For `0<=m<=N-1`, root-of-unity orthogonality gives

`sum_{k=0}^{N-1}|sum_{r=0}^{m-1} zeta^(k*r)|^2=N*m`.

The `k=0` term equals `m^2`; hence

`S_m=N*m-m^2=m*(N-m)=q_m`.

This proves the claimed Hessian block with
`sigma_m=2*(N-1)-q_m`.

### Step 5: Hamiltonian block spectrum

Because the local basis preserves `J`,

`L_m=c*[[0,q_m],[-sigma_m,0]]`.

Therefore

`L_m^2=-c^2*q_m*sigma_m*I`.

For `m=1,...,N-1`, `q_m>0`.  Thus:

- `sigma_m>0` gives the semisimple pair
  `+/- i*c*sqrt(q_m*sigma_m)`;
- `sigma_m=0` gives a nonzero nilpotent block and a double zero eigenvalue;
- `sigma_m<0` gives the real pair
  `+/- c*sqrt(q_m*(-sigma_m))`.

For a non-self-conjugate Fourier label, the `m` and `N-m` complex blocks join
to one real four-dimensional isotypic component.  Thus at `N=7`, the conjugate
labels `3,4` give algebraic zero multiplicity four and geometric multiplicity
two on the real reduced space.  This multiplicity statement is still purely
linear.

### Step 6: symmetry and scale directions

For `m=0`, `q_0=0` and

`L_0=c*[[0,0],[-2*(N-1),0]]`.

Its kernel is uniform tangential displacement, namely rotation.  Uniform
radial displacement is its scale generalized vector.  Fixing angular impulse
and quotienting rotations removes this entire block.

The conjugate first harmonics `m=1,N-1` contain the physical translation
plane.  Indeed, if `xi_j,eta_j` are local coordinates and
`w_j=xi_j+i*eta_j`, then the center variation is

`sum_j exp(i*theta_j)*w_j`,

which selects one complex plane in the first-harmonic real isotypic component.
Fixing the center removes that plane.  Since `q_1=sigma_1=N-1`, the full
first-harmonic Hessian is the scalar `c*(N-1)*I`; its centered complementary
plane is invariant and elliptic with frequency `Omega=c*(N-1)`.  No symmetry
zero or Euclidean frequency is counted as a shape instability.

### Step 7: the sharp threshold

The maximum of `q_m=m*(N-m)` is `floor(N^2/4)`.  Hence the least stability
sign is

`sigma_min=2*(N-1)-floor(N^2/4)`.

Direct evaluation gives a positive value for `N=3,4,5,6`, zero for `N=7`,
and a negative value for `N=8`.  For even `N=2k>=8`,

`floor(N^2/4)-2*(N-1)=k^2-4k+2>0`.

For odd `N=2k+1>=9`, the difference is

`k*(k+1)-4k=k*(k-3)>0`.

At `N=7`, equality `m*(7-m)=12` holds only for `m=3,4`.  This proves:

- reduced linear ellipticity for `3<=N<=6`;
- exactly the two conjugate nilpotent modes `m=3,4` at `N=7`;
- at least one real hyperbolic pair for every `N>=8`.

The theorem is linear.  In particular, the nilpotent heptagon calculation
does not decide or claim nonlinear stability.  This completes the proof. ∎

## Boundary ledger

- `N<3`: outside the theorem; the centered two-vortex case has no reduced
  shape degree of freedom.
- `R=0`: a logarithmic collision singularity, so the Hamiltonian is undefined.
- `Gamma=0`: the weighted symplectic form degenerates; only the zero-velocity
  limit survives.
- `Gamma<0`: reverses time and leaves all stability signs unchanged.
- `R->infinity`: all frequencies tend to zero as `R^(-2)` without changing
  the sign atlas.
- `N=7`: linear degeneracy only; nonlinear stability remains outside the
  theorem claimed here.

## Evidence boundary

The receipt contains 2,077 exact mode rows for `N=3..64`, 62 polygon summaries,
64 exact `Gamma/R^2` scale cells, seven explicit symmetry-slice rows, and eight
named boundaries.  The independent checker rebuilds every raw Cartesian
`2N by 2N` Hessian, acts on explicit rotation, scale, translation, and centered
first-harmonic vectors, and passes 65,655 assertions.  SymPy proves 4,585 exact
identities, including coefficient-counted root sums and exact slice actions;
two fresh paths replay the evidence byte-for-byte; and 76/76 hostile mutations
are rejected.  Exact JSON schemas, types, row order, semantic uniqueness,
duplicate keys, and nonstandard constants are all enforced.  These finite
checks audit the implementation and conventions.  The all-`N` result is proved
by the root-sum identity and inequalities above, not by enumeration.

## Route-A result

The tuple is

`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`.

The regular polygons supply a natural family of relative periodic motions,
which is enough only for `A1_WEAK`.  Their periods vary continuously with
`Gamma/R^2`; there is no rational-prime carrier, logarithmic-prime clock,
isolated primitive-orbit census, target determinant, target divisor, target
functional equation, or same-clock quantum lift.  The overall verdict is
`ROUTE_A_REJECTED`, Route B is not authorized, and the locked scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## Originality and ownership boundary

The polygon and its stability question are classical.  Thomson, Havelock,
Cabral–Schmidt, and Celli–Lacomba–Pérez-Chavela are cited as source owners and
later authoritative context.  This package claims only a self-contained
proof reconstruction, complete boundary ledger, independent executable audit,
and a distinction from C1–C283 inside this repository.  It makes no claim of
invention or priority in the literature.
