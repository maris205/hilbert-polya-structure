# HCS-C55 exact-code results

Status: `RELEASE_CANDIDATE`.

The producer and independent checker close the following finite controls:

- `R_(1,0)` has ambient dimension 156, relation rank 73, and quotient
  dimension 83; multiplication by `y` to `R_(2,-3)` has rank 83.
- The four frozen tangent lifts `[y p_i]` map to the four first-variation
  classes `[y^2 p_i]`.
- The ambient descent satisfies `D(Q)=rho^2 Q`, `D(z)=rho z`, and `D(F)=F`;
  all 24 split elements pass both defining-equation covariance tests.
- The four rational basis vectors use the canonical gauge `q0=e0`, followed
  by `q1=e1+e3`, `q2=(1+2rho)(e1-e3)`, and `q3=-rho e2`.
- Twenty direct reductions of `y^5(sum a_i p_i)^3` are interpolated exactly;
  the checker reconstructs them from the 20 unordered traces with the
  `1/3/6` mixed multinomial factors and compares the raw tensors up to one
  common nonzero `Q(rho)` gauge.
- The primitive 20-term rational cubic has coefficient gcd one and frozen
  coefficient hash
  `1c7065d5644c44bba80658dee5d0704c371e9f446c8c3c6ac29f9590d0831b9e`.
- Its homogeneous Jacobian quotient has length 16; hence its projective
  singular locus is empty.  Together with the exact factorization control,
  this certifies smoothness and geometric irreducibility of the cubic
  surface.
- The full infinitesimal ideal-stabilizer system has rank 73 in 74 unknowns,
  with unique kernel `lambda*(I8,2,3,0)` and projective nullity zero.

The checker reports 13/13 named semantic gates and the complete scalar
identity `1589 = 292 + 1296 + 1` (central + derived + chronology-only).
Nothing in this file promotes the finite controls to a relative VHS or a
motive; those implications remain written-proof obligations.
