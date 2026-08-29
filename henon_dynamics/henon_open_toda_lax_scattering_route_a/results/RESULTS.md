# Results

The canonical receipt contains six rational parameter rows (three \(N=2\),
three \(N=3\)), 30 finite Lax states, 15 exact \(N=2\) sech/tanh comparisons,
six \(T=8\) endpoint sorting diagnostics, and nine \(N=3\) norming-coordinate
rows.  The RK4 invariant and spectral drifts remain below the checker bound
\(2\times10^{-7}\); all finite edges remain positive.  The largest exact
formula comparison is recorded rather than rounded away.

The norming ledger independently confirms
\(\rho_k(t)\propto\rho_k(0)e^{2\lambda_kt}\) at three times per \(N=3\) row.
The \(T=8\) values are explicitly finite-endpoint diagnostics: weak-link rows
need not be visually close to their limiting sorted values at that finite
time.

The repeated-root boundary is the decoupled matrix
\(\operatorname{diag}(0,0,1)\), with polynomial \(x^2(x-1)\).  It is not
included in the regular positive Jacobi chart.  All route and scope flags are
closed by the independent checker.

