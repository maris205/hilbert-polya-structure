# HCS-C47 exact computation

C47 realizes the C45 normalized logarithmic norm in an explicit graded
finite algebra at every split prime.  The positive trace is

\[
\tau_p(A_+\oplus A_-)=d_p^{-1}(\operatorname{Tr}A_++\operatorname{Tr}A_-),
\]

while the signed supertrace is

\[
\operatorname{str}_p(A)=\tau_p(\Gamma_pA).
\]

The code keeps these two functionals separate.  It verifies all exact block
dimensions through \(p=499\), reconstructs chronological moments through
order three at seven primes, and retains the rational—not rounded—third
moments.

For the global block \(X_s=\bigoplus_p p^{-s}W_p\), the positive trace gives

\[
\tau(|X_s|^q)=\sum_{p\equiv1\pmod3}\frac{8p+4}{3}p^{-q\Re s}.
\]

Thus \(X_s\in L^q(M,\tau)\) exactly when \(q\Re s>2\).  This is the
field-degree-normalized semifinite ideal, not the classical Schatten class of
the underlying Hilbert direct sum.  In the latter category,

\[
X_s\in S^q(\mathcal H)\quad\Longleftrightarrow\quad q\Re s>3,
\]

so classical trace class begins only at \(\Re s>3\) and does not encode the
normalized root.  The smallest fixed \(L^q(M,\tau)\) order covering
\(\Re s>1/2\) is four, producing the exact source-native semifinite
regularization

\[
\mathcal G(s)=e^{-\ell_1-\ell_2/2-\ell_3/3}
\det_{4,\tau,\mathrm{gr}}(I-X_s).
\]

This is a \(\tau\)-associated graded determinant, not a classical Fredholm
determinant.

The low-order \(\ell_n\) are sums of local supertraces.  The code does not
conflate them with a global semifinite trace of a non-\(L^1\) power.

These \(L^q\) spaces use \(\tau\), not the canonical Hilbert-space trace.
Under the latter, the same block satisfies \(X_s\in S^q\) only when
\(q\Re s>3\) and encodes the unnormalized Galois norm.

Run `./code/run_c47.sh` from the project directory.  The runner regenerates
artifacts, checks byte identity, runs 39 mutation tests, and verifies the
manifest.
