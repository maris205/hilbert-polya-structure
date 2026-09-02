# Verification plan — HCS-C302

1. Freeze HCS-C302, HEN-O286, source commit
   `83c058259c02707d004fca2d6b1a4ebaf5036094`, epoch `1788307200`, evaluator
   digest, and scope `NO_BAD_EULER_OR_ROOT_NUMBER`.
2. Generate exact rational PGF coefficients through `n=12`; verify positivity,
   normalization, support, permutation counts, and the `n=0,1` base cases.
3. Independently enumerate every permutation through `n=9`, then use a
   separate integer-count convolution through `n=12`.
4. Recover the first three raw moments from coefficients and compare the mean
   and variance with their harmonic closed forms.
5. Archive every exact `n+1`-centered pivot coefficient and toll through
   `n=32`, including zero average toll and the branch-square average.
6. Use an independent SymPy lane for unsimplified mean/variance recurrences,
   beta derivatives, the `2/3` contraction coefficient, and
   `m_3=16*zeta(3)-19`.
7. Keep the limit analytic: close the mixed-subproblem convergence by a
   uniform-`L2` cutoff/limsup argument, then license cubing by an `L3`
   binary-tree toll series and conditional Rosenthal inequality.
8. Replay evidence twice and kill mutations of endpoints, comparison cost,
   centering, `n` versus `n+1`, moments, route/scope, and strict parsers.
9. Retain three substantively different deterministic PDF rounds and close
   exactly 27 payloads plus one self-excluded manifest.
