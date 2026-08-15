# Results

## Exact theorem

The primitive/repetition product admits

    log Z_orb(t,1)=sum_{m>=1}c_m Phi(t^m),
    c_m=(1/m)product_{p|m,p odd}(1-p).

After the unique P71 m=1 counterterm,

    log C_rel(t)=H_rel(1-sqrt(2)t)-sum_{m>=2}c_m Phi(t^m).

Every c_m is nonzero, and at rho_m=2^(-1/(2m)),

    log C_rel(t)
      = -c_m/[sqrt(2)m(1-t/rho_m)] + holomorphic.

Thus C_rel has an essential singularity at every rho_m, m>=2, with rho_m
increasing to one.

## Verification

- 48 exact formal coefficient comparisons in the primary certificate.
- 100 comparisons in unit tests.
- 64 independently reconstructed Euler channels.
- 16/16 tests across normal and optimized modes.
- 25/25 claim mutations rejected.

## Boundary

The theorem refutes a unit-disk meromorphic/Fredholm determinant for this
specific relative germ. Punctured-domain operator models remain open.
Arithmetic advance is NO and Route B is not authorized.
