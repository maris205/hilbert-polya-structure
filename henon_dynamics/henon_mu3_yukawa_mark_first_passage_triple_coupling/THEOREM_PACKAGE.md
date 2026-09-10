# C101 theorem package

Let (T_i,T_j,T_k) be three C88 first-passage times and

\[
S_{ijk}(a,b,c)=\#\{\pi:T_i>a,\ T_j>b,\ T_k>c\}.
\]

Sorting the three thresholds gives a nested chain of supports
(A\subseteq B\subseteq C).  The closure-state dynamic program contracts
this chain against the C88 target inclusion matrix, while the boundary planes
are supplied by C88 and C90.  Three-dimensional finite differences recover

\[
N_{ijk}(a,b,c)=\Delta_a\Delta_b\Delta_c S_{ijk}(a,b,c).
\]

For every one of the 1,140 unordered triples, the resulting 17^3 array is a
nonnegative normalized permutation-count PMF.  Its coordinate permutations,
all 400 pair marginals, all 20 single marginals, 64 raw moments through order
three, covariance matrix, and third interaction cumulant are checked exactly.
These are finite identities only; no arithmetic or operator claim is made.
