# C185 results

## All-size theorem

For every real symmetric simple-spectrum orthogonal orbit and every strictly
increasing diagonal `N`, the Brockett equation

`dH/dt=[H,[H,N]]`

is globally defined and isospectral.  Its height satisfies

`d Tr(HN)/dt=||[H,N]||_F^2`.

There are exactly `n!` diagonal permutation equilibria.  At permutation
`pi`, the `(i,j)` mode has rate

`(lambda_pi(i)-lambda_pi(j))*(nu_j-nu_i)`.

The unstable dimension of the ascent flow and the Morse index of the sorting
energy `-Tr(HN)` both equal `inv(pi)`.  Every trajectory converges to one
equilibrium; outside the lower-dimensional stable manifolds of nonsorted
equilibria, it converges to increasing alignment.  No nonconstant trajectory
is recurrent or periodic.

Repeated source or target spectra are excluded from the main theorem.  The
source sentinel distinguishes a zero ambient pair rate in a stabilizer
direction from a tangent mode on the smaller orbit; the target sentinel has a
genuine tangent zero mode and continuous Morse--Bott equilibrium family.  No
full boundary or Bruhat/Schubert closure classification is claimed.

## Exact evidence

- dimensions: all `n` by proof; finite regression `2<=n<=7`;
- permutation rows: 5,912;
- pair-mode rows: 118,004;
- exact rational matrix rows: 6;
- independent checker: 183,158 assertions;
- separate SymPy path: 253,765 checks;
- replay: 12,391,893 bytes, byte-identical;
- hostile mutations: 67 repaired-hash and one stale-hash rejection;
- evidence payload SHA-256:
  `8dc7236bd484977e6261feebcecb6212609675fc11d9ba518936b18ed736ab00`;
- evidence file SHA-256:
  `9a273ac5bb3d55b02e680ebe6ee801ada1390a5404ee8230cd754b90a104ec50`.

## Route-A verdict

`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`, overall
`ROUTE_A_REJECTED`; Route B false.

The arbitrary real spectra fail A0.  Strict Lyapunov monotonicity removes every
nonconstant primitive periodic carrier, so A1 fails.  There is no source-owned
dynamical determinant, target analytic structure, or Weil compression.  The
state-dependent skew Lax generator is only a formal orthogonal lift, not a
fixed quantum operator.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
