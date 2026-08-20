# C78 research question

Given the sixteen frozen named coordinates in
\(Q=\mathbb Z/9\oplus\mathbb Z/3\oplus\mathbb Z/2\), how many deleted labels
must be restored for every retained support to generate the full core, and
what is the exact joint distribution of deletion count and repair distance?

For each deletion set \(D\subseteq L\), put \(A=L\setminus D\) and define

\[
 \rho(D)=\min\{|R|:R\subseteq D,
                    \Phi((L\setminus D)\cup R)=Q\}.
\]

The experiment must:

1. bind the C75 coordinates and C76 subgroup/closure convention byte-for-byte;
2. enumerate every support, rather than sample Bernoulli supports;
3. compute \(\rho(D)\) by an exact minimum over restoration subsets of \(D\);
4. publish \(\mathcal P(x,y)=\sum_D x^{|D|}y^{\rho(D)}\), with both marginals;
5. independently rederive the distance distribution and reject semantic
   mutations of the receipt.

The variable \(x\) marks deleted labels and \(y\) marks labels restored by a
minimum repair.  It is important not to conflate deletion count \(|D|\) with
repair distance \(\rho(D)\).  The expected exact distance counts are

\[
N_0=30400,\qquad N_1=32704,\qquad N_2=2368,\qquad N_3=64,
\]
so \(\rho\leq3\) on the complete support space.

Boundary: this finite calculation concerns only the named presentation and
its inherited source convention.  It makes no arithmetic/local,
Euler-factor, root-number, automorphy, full Burnside-ring, or Hilbert--Polya
claim.  Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
