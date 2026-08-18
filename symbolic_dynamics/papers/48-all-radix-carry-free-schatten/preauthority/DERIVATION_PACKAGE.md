# Derivation Package — Radix Shells and Schatten Walls

## 1. Target

Classify, for every radix \(b\ge2\) and every finite Schatten index
\(1\le q<\infty\), the Dirichlet-weighted positive-vertex no-carry
operator

$$
B_{b,s}(m,n)=
\mathbf 1_{\{m+n\ {\rm is\ carry\!-\!free\ in\ base}\ b\}}(mn)^{-s/2}.
$$

The target includes the two strict endpoints, the binary zero-block
exception, the trace and regularized determinant domains, and the symbolic
least-period ledger.

## 2. Derivation status

The main classification is an exact theorem. The finite-control identities
are exact propositions. Numerical finite sections are validation devices
only and are not part of the derivation. No approximation is used in the
proof.

## 3. Invariant object

The invariant object is the operator on \(\ell^2(\mathbb N)\) with
\(\mathbb N=\{1,2,\ldots\}\). The graph relation is coordinatewise digit
compatibility. Digit tensors that contain the all-zero word are finite
controls, not finite restrictions of a source containing zero.

## 4. Assumptions and conventions

- \(b\) is an integer at least two.
- \(s=\sigma+it\), and \(n^{-s}\) uses the real logarithm.
- \(1\le q<\infty\); boundedness is treated separately from \(S_q\).
- \(C_d=(\mathbf 1_{\{a+c<d\}})_{0\le a,c<d}\) for \(d\ge1\);
  \(C_0\) is the zero block.
- \(\kappa_{d,q}=\|C_d\|_{S_q}\),
  \(\tau_b=\kappa_{b,1}\), and
  \(\alpha_b=\log_b\tau_b\).

## 5. Strategy

First remove the imaginary phase by two diagonal unitaries. Then partition
positive integers into radix shells and factor every unweighted shell block
into a repetition vector and digit matrices. Uniform diagonal comparison
transfers the exact finite norms to weighted bounds. Summation proves
sufficiency. A positive-density column supplies the universal wall
\(\sigma>1\), while orthogonal pinching supplies the digit-norm wall,
with adjacent paired shells replacing the zero same-shell block at \(b=2\).
Finally, diagonal and closed-walk expansions determine trace, determinant,
and period domains.

## 6. Dependency map

$$
\text{digit covariance}
\Longrightarrow s_j(C_b)
\Longrightarrow \kappa_{b,q}
\Longrightarrow \text{shell norms}
\Longrightarrow \text{weighted geometric series}
\Longrightarrow S_q\text{ classification}.
$$

The trace and least-period conclusions use the frozen positive-vertex
convention independently of finite zero-completed controls.

## 7. Exact digit singular values

After conjugating \(C_bC_b^*\) by the row-reversal permutation, it becomes

$$
K_b=(\min(i,j))_{1\le i,j\le b}.
$$

The inverse \(K_b^{-1}\) has adjacent entries \(-1\), diagonal entries
\(2\) except for final entry \(1\), and zero elsewhere. The eigenvector
recurrence is solved by \(\sin(i\theta)\); the final boundary condition
gives

$$
\theta_j=\frac{(2j-1)\pi}{2b+1},\qquad 1\le j\le b.
$$

Consequently

$$
s_j(C_b)=
\left(2\sin\frac{(2j-1)\pi}{4b+2}\right)^{-1}.
$$

There are \(b(b+1)/2\) ones, so
\(\kappa_{b,2}^2=b(b+1)/2<b^2\). Column reversal also shows
\(|\det C_b|=1\). Hence the product of the singular values is one, while
they are not all one (their squared sum is \(b(b+1)/2>b\)), and strict
arithmetic-geometric mean gives

$$
\tau_b=\sum_j s_j(C_b)>b,\qquad \alpha_b>1.
$$

## 8. Exact unweighted shell blocks

Let \(I_k=[b^k,b^{k+1})\cap\mathbb N\), and let \(A_{k\ell}\) be the
unweighted adjacency block. For \(k>\ell\), digit permutation and deletion
of zero rows give the nonzero singular-value equivalence

$$
A_{k\ell}\simeq
\mathbf 1_{(b-1)b^{k-\ell-1}}
\otimes C_{b-1}\otimes C_b^{\otimes\ell}.
$$

Therefore

$$
\|A_{k\ell}\|_{S_q}
=\bigl((b-1)b^{k-\ell-1}\bigr)^{1/2}
\kappa_{b-1,q}\kappa_{b,q}^{\ell}.
$$

For \(k=\ell\),

$$
A_{kk}\simeq C_{b-2}\otimes C_b^{\otimes k},
\qquad
\|A_{kk}\|_{S_q}
=\kappa_{b-2,q}\kappa_{b,q}^k.
$$

The first formula for \(k<\ell\) follows by transposition. At \(b=2\),
\(C_0=0\), so the diagonal-shell formula is exactly zero, not merely
asymptotically small. Also \(C_1=(1)\), and hence

$$
\|A_{2j+1,2j}\|_{S_q}=\kappa_{2,q}^{2j}.
$$

For reference, the binary singular values give
\(\tau_2=\sqrt5\) and \(\alpha_2=\log_2\sqrt5\).

## 9. Weighted transfer

For real \(\sigma>0\), write
\(B_{k\ell}=D_kA_{k\ell}D_\ell\). On \(I_k\),

$$
b^{-(k+1)\sigma/2}I\le D_k\le b^{-k\sigma/2}I.
$$

The ideal inequality applied forward and to the inverse diagonal factors
gives, uniformly in \(k,\ell\),

$$
b^{-\sigma}b^{-(k+\ell)\sigma/2}\|A_{k\ell}\|_{S_q}
\le \|B_{k\ell}\|_{S_q}
\le b^{-(k+\ell)\sigma/2}\|A_{k\ell}\|_{S_q}.
$$

For \(s=\sigma+it\),

$$
B_{b,s}=U_tB_{b,\sigma}U_t,\qquad
U_te_n=n^{-it/2}e_n,
$$

so the singular values depend only on \(\sigma\).

## 10. Sufficiency

Put \(k=\ell+h\), \(h\ge1\). Apart from a constant independent of
\(h,\ell\), the cross-shell upper bound is

$$
b^{h(1-\sigma)/2}
\bigl(\kappa_{b,q}b^{-\sigma}\bigr)^\ell.
$$

The double sum of block norms converges if and only if both geometric ratios
are less than one:

$$
\sigma>1,\qquad
\sigma>\log_b\kappa_{b,q}.
$$

The same-shell upper series requires the second inequality. Summing finite
block truncations in the Banach ideal \(S_q\) proves

$$
\sigma>\max\{1,\log_b\kappa_{b,q}\}
\Longrightarrow B_{b,s}\in S_q.
$$

## 11. Necessity and both equalities

The \(n=1\) column contains every \(m\) whose units digit is at most
\(b-2\), a positive-density set. Its squared norm majorizes a
positive-density subseries of \(\sum m^{-\sigma}\). Thus
\(\sigma\le1\) does not even define a bounded operator.

Now suppose \(\sigma>1\). For \(b\ge3\), pinch to the mutually orthogonal
same-shell blocks. The lower weighted comparison gives a positive constant
times

$$
\bigl(\kappa_{b,q}b^{-\sigma}\bigr)^k.
$$

The \(q\)-powers are nonsummable when the ratio is at least one, including
equality. For \(b=2\), pinch instead to
\(I_{2j}\oplus I_{2j+1}\). Each real compression is

$$
\begin{pmatrix}0&X_j\\X_j^*&0\end{pmatrix},
$$

whose singular values are those of \(X_j\), each twice. The exact
adjacent-shell formula gives a lower bound proportional to
\((\kappa_{2,q}2^{-\sigma})^{2j}\), again nonsummable at equality.
Contractivity of orthogonal pinching completes necessity.

## 12. Main conclusion

For every \(b\ge2\) and \(1\le q<\infty\),

$$
B_{b,s}\in S_q
\quad\Longleftrightarrow\quad
\sigma>\max\{1,\log_b\kappa_{b,q}\}.
$$

Because \(\kappa_{b,2}<b\), Hilbert-Schmidt membership starts exactly at
\(\sigma>1\). It follows that boundedness, compactness, and \(S_2\)
membership are equivalent to \(\sigma>1\). Taking \(q=1\) and using
\(\tau_b>b\) gives trace class exactly for \(\sigma>\alpha_b\).

## 13. Trace, powers, and determinant

A positive vertex \(m\) has a loop exactly when each digit \(d\) obeys
\(2d<b\). Thus, for \(\sigma>\alpha_b\),

$$
\operatorname{Tr}B_{b,s}
=\sum_{\substack{m\ge1\\
\text{all digits }d\le\lfloor(b-1)/2\rfloor}}m^{-s}.
$$

This series is identically zero at \(b=2\). For \(b>2\), it is positive for
real \(s=\sigma>\alpha_b\); complex zero-freeness is not asserted.

For \(\sigma>1\) and \(r\ge2\), \(B_{b,s}^r\in S_1\). Finite-shell
compression and absolute majorization by the real-\(\sigma\) operator yield

$$
\operatorname{Tr}(B_{b,s}^r)
=\sum_{\text{based carry-free closed }r\text{-walks}}
\prod_{i=1}^r n_i^{-s}.
$$

Therefore \(\det_2(I-zB_{b,s})\) is entire in \(z\), and its usual
trace-power logarithm is valid near \(z=0\). Ordinary trace and determinant
remain restricted to \(\sigma>\alpha_b\).

## 14. Least periods

Distinct powers of \(b\) are pairwise carry-free. At \(b=2\), no positive
vertex has a loop; two distinct powers give least period two, and \(r\)
distinct powers give least period \(r\) for every \(r\ge3\). At \(b>2\),
the vertex \(1\) has a loop and the same distinct-power construction gives
all \(r\ge2\). Hence

$$
\operatorname{LPS}(b=2)=\{2,3,\ldots\},\qquad
\operatorname{LPS}(b>2)=\{1,2,\ldots\}.
$$

These are support statements. They are not inferred from complex weighted
trace values.

## 15. Boundaries and open risks

- Kummer is used only as a prime-radix corollary.
- Finite digit tensors, singular values, Lucas counts, and Boolean or
  disjointness spectra receive zero novelty credit.
- The unweighted fixed-point sets are infinite, so no Artin–Mazur zeta is
  defined.
- Priority is not established by a bounded search. The literature audit
  records only that no exact infinite weighted theorem was found.
- The proof depends on \(q\ge1\); no quasi-Schatten claim for \(q<1\) is
  made.
