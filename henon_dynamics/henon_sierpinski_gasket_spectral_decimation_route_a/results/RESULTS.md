# C184 exact results

For every \(m\ge1\), the standard unnormalized finite-gasket Dirichlet
Laplacian has the complete classical 2/5/6 spectral-decimation genealogy
under \(R(t)=t(5-t)\).  The 2-series is born once at level one; 5-series
birth multiplicity is \((3^{j-1}+3)/2\); 6-series birth multiplicity is
\((3^j-3)/2\), and continued 6-series take the unique admissible first step
\(6\mapsto3\).  The weighted population closes exactly to
\(N_m=(3^{m+1}-3)/2\).

The same ledger proves

\[
\chi_m(t)=(-1)^{N_{m-1}}(t-5)^{a_m}(t-6)^{b_m}
\frac{\chi_{m-1}(t(5-t))}{(t-2)^{b_{m-1}}}
\]

and

\[
\det L_m=2^{(3^m-1)/2}
3^{(3^{m+1}-6m-3)/4}5^{(3^m+6m-1)/4}.
\]

It also gives exact finite heat and spectral-zeta identities, including
\(H_m(0)=\zeta_m(0)=N_m\), \(-H'_m(0)=4N_m\), and
\(\exp[-\zeta'_m(0)]=\det L_m\).

Released evidence contains 5 level rows, 103 lineage rows, 542 exact
characteristic-coefficient cells, and 537 graph-eigenvalue regression
cells.  The independent checker passes 3,041 assertions.  The separate
SymPy reconstruction passes 33,177 checks.  Replay is byte exact, and all
71 hostile mutations are rejected.

The inverse-branch tree is graph refinement, not physical time.  Hence the
strict tuple is `(A0_FAIL, A1_FAIL, A2_FAIL,
A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)`, overall rejected, with
Route B false.
