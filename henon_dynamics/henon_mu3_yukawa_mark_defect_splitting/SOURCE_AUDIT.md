# C69 source audit

The producer verifies exact SHA-256 bindings before calculation:

| Source | Role |
|---|---|
| C64 evidence and manifest | frozen `16 x 16` mark matrix `M` |
| C65 evidence and manifest | saturation columns `u1,u2,u3` |
| C66 evidence and manifest | ambient cokernel order and Smith data |
| C68 evidence and manifest | actual embedded subgroup and quotient |

The C68 evidence hash is
`6d99afb5ec5e291f068f603060c79c72114e3fd2c26e0c9c21fdd5281add9ab9`;
the C68 manifest hash is
`aab32e57216e091c2eeedc2486a6651d83bfac713ad6f290d9c1bb9b45a947bc`.

Every source carries `NO_BAD_EULER_OR_ROOT_NUMBER`.  The new claim is confined
to the concrete finite extension on the frozen sixteen-type support.
