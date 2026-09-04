# Exact results

The canonical evidence file has SHA-256
`d0c9544a450a22ecf89280bd7c8d92dd8cb12256ed8bc8fe531243fe5e769c9f`
and internal canonical payload SHA-256
`3e0bd7ddc06baeae57c248cd22146d7cb45879b91363c6aae2252dd89b4a3ff5`.

It records:

- 16 matrix-dimension/normalization rows;
- 1,040 exact level-multiplicity rows for $N\leq16$ and degree $\leq64$;
- 16,602 exact partition, strict-Slater-index, eigenvalue, and norm rows for
  $N\leq8$ and degree $\leq24$;
- 12 high-precision killed-determinant/Doob-kernel rows at $N=2,3,4$;
- detailed-balance residuals below $10^{-75}$ in every kernel row;
- four independently hashed data sections and one canonical payload hash.

The finite rows agree with the all-$N$ analytic theorem. They are not used to
infer completeness or boundary nonattainment by sampling.
