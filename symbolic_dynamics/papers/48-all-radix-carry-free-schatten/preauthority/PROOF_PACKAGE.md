# Proof Package — All-Radix Carry-Free Operator

## Main theorem

For each \(b\ge2\), \(1\le q<\infty\), and
\(\sigma=\Re s\),

$$
B_{b,s}\in S_q
\iff
\sigma>\max\{1,\log_b\kappa_{b,q}\}.
$$

Moreover \(B_{b,s}\) is bounded and compact iff \(\sigma>1\);
\(B_{b,s}\in S_2\) iff \(\sigma>1\); and
\(B_{b,s}\in S_1\) iff \(\sigma>\alpha_b\), where
\(\alpha_b=\log_b\tau_b>1\).

## Status and assumptions

PROVABLE AS STATED. Here \(\mathbb N=\{1,2,\ldots\}\),
\(1\le q<\infty\), complex powers use the real logarithm, and every
Schatten assertion is about the completed operator on
\(\ell^2(\mathbb N)\). No assertion below adds the zero word as a vertex.

## Step 1: remove complex phases

For \(s=\sigma+it\), diagonal unitaries give

$$
B_{b,s}=U_tB_{b,\sigma}U_t,
\qquad U_te_n=n^{-it/2}e_n.
$$

Singular values depend only on \(\sigma\).

## Step 2: finite digit singular values

After conjugating \(C_bC_b^*\) by the row-reversal permutation, it is the
covariance matrix
\(K_b=(\min(i,j))_{1\le i,j\le b}\). Its inverse is tridiagonal, with
diagonal \(2,\ldots,2,1\) and adjacent entries \(-1\). Solving its sine
recurrence gives angles
\(\theta_j=(2j-1)\pi/(2b+1)\), and hence

$$
s_j(C_b)
=\left[
2\sin\frac{(2j-1)\pi}{4b+2}
\right]^{-1},
\qquad 1\le j\le b.
$$

Thus \(\kappa_{b,q}\) is explicit. Also

$$
\kappa_{b,2}^2=\frac{b(b+1)}2<b^2.
$$

Column reversal makes \(C_b\) triangular with unit diagonal, so the product
of all singular values is one. The arithmetic-geometric mean inequality
gives \(\tau_b\ge b\), with strict inequality because the displayed
singular values are not all one. Hence \(\alpha_b>1\).

## Step 3: exact unweighted shell blocks

Let

$$
I_k=\{b^k,\ldots,b^{k+1}-1\}.
$$

Write \(A_{k\ell}\) for the unweighted carry-free block from \(I_\ell\) to
\(I_k\), and set \(\kappa_{0,q}=0\). Zero rows and columns do not affect
nonzero singular values. For \(k>\ell\), permutation of digit coordinates
gives the exact nonzero-singular-value factorization

$$
A_{k\ell}\simeq
\mathbf 1_{(b-1)b^{k-\ell-1}}
\otimes C_{b-1}\otimes C_b^{\otimes\ell},
$$

where the first factor is a column vector of ones. Consequently,

$$
\|A_{k\ell}\|_{S_q}
=\bigl((b-1)b^{k-\ell-1}\bigr)^{1/2}
\kappa_{b-1,q}\kappa_{b,q}^{\ell}.
$$

The top nonzero digit and intervening free digits produce the repetition
vector, the leading digit of the shorter vertex produces \(C_{b-1}\), and
each lower digit produces \(C_b\). For \(k<\ell\), use transposition.

For \(k=\ell\), the same deletion and permutation give
\(A_{kk}\simeq C_{b-2}\otimes C_b^{\otimes k}\), and therefore

$$
\|A_{kk}\|_{S_q}
=\kappa_{b-2,q}\kappa_{b,q}^{k}.
$$

Here \(C_0\) denotes the zero block. Thus for \(b=2\) every same-shell
block is zero; this is the binary endpoint exception.

## Step 4: weighted block comparison

For \(\sigma>0\), write \(B_{k\ell}=D_kA_{k\ell}D_\ell\). Every diagonal
entry of \(D_k\) lies between \(b^{-(k+1)\sigma/2}\) and
\(b^{-k\sigma/2}\). Applying the ideal inequality also to the inverse
diagonal factors gives the explicit uniform comparison

$$
b^{-\sigma}b^{-(k+\ell)\sigma/2}\|A_{k\ell}\|_{S_q}
\le \|B_{k\ell}\|_{S_q}
\le
b^{-(k+\ell)\sigma/2}\|A_{k\ell}\|_{S_q}.
$$

This comparison preserves equality endpoints because the constants are
uniform in \(k,\ell\).

## Step 5: sufficiency

For \(k=\ell+h\), \(h\ge1\), the cross-block upper bound is a constant times

$$
b^{h(1-\sigma)/2}
\bigl(\kappa_{b,q}b^{-\sigma}\bigr)^\ell.
$$

The sum of these upper bounds over \(h,\ell\) converges under

$$
\sigma>1,\qquad \kappa_{b,q}b^{-\sigma}<1.
$$

The same-shell series has the second condition. The transposed half has the
same norm. Since \(q\ge1\), the triangle inequality in \(S_q\), followed by
completion of finite block truncations, shows that the full operator is in
\(S_q\).

## Step 6: the universal wall \(\sigma>1\)

The column indexed by \(n=1\) contains every \(m\) whose least significant
digit is at most \(b-2\). This set has positive density. Its squared
\(\ell^2\) norm contains a positive-density subseries of
\(\sum m^{-\sigma}\), which diverges for \(\sigma\le1\). Hence the operator
is unbounded there.

For \(\sigma>1\), Step 5 with \(q=2\) applies because
\(\log_b\kappa_{b,2}<1\). Thus the operator is Hilbert–Schmidt and therefore
compact and bounded. This proves the bounded/compact/\(S_2\) equivalence.

## Step 7: the digit-norm wall and equality

By Step 1 it suffices to work with the real, positive matrix
\(B_{b,\sigma}\). Assume \(\sigma>1\) but
\(\kappa_{b,q}b^{-\sigma}\ge1\).

For \(b\ge3\), pinch to the mutually orthogonal same-shell blocks. Their
weighted \(S_q\) norms are bounded below by a positive constant times

$$
\bigl(\kappa_{b,q}b^{-\sigma}\bigr)^k.
$$

The \(q\)th powers are not summable, including equality.

For \(b=2\), same-shell blocks vanish. In this radix
\(\kappa_{1,q}=1\), so the exact adjacent-shell formula is

$$
\|A_{2j+1,2j}\|_{S_q}=\kappa_{2,q}^{2j}.
$$

Pinch to the mutually
orthogonal two-shell spaces

$$
I_{2j}\oplus I_{2j+1}.
$$

Each compression has the form
\(\left(\begin{smallmatrix}0&X_j\\X_j^*&0\end{smallmatrix}\right)\), so its
nonzero singular values are those of \(X_j\), each twice. The adjacent-shell
formula and the uniform lower comparison give a lower bound proportional to

$$
\bigl(\kappa_{2,q}2^{-\sigma}\bigr)^{2j},
$$

again nonsummable at equality. Pinching is contractive for Schatten norms,
so \(B_{b,s}\notin S_q\). This completes the iff theorem.

## Step 8: trace class and trace

Taking \(q=1\) gives the exact trace-class wall

$$
\sigma>\alpha_b=\log_b\tau_b>1.
$$

In that domain the diagonal is absolutely summable. Let

$$
\mathcal D_b=
\{m\ge1:\text{ every base-}b\text{ digit of }m
\text{ is at most }\lfloor(b-1)/2\rfloor\}.
$$

Then

$$
\operatorname{Tr}(B_{b,s})
=\sum_{m\in\mathcal D_b}m^{-s}.
$$

For \(b=2\), \(\mathcal D_b\) is empty and the trace is identically zero.
For \(b>2\), this is a nonempty Dirichlet series and is positive on the real
half-line \(s=\sigma>\alpha_b\). No pointwise zero-free assertion is made
for nonreal \(s\).

## Step 9: determinant and least periods

For \(\sigma>1\), \(B_{b,s}\in S_2\). For every \(r\ge2\), finite-shell
compression followed by Schatten convergence gives

$$
\operatorname{Tr}(B_{b,s}^r)
=\sum_{\substack{n_1,\ldots,n_r\ge1\\
n_i+n_{i+1}\text{ carry-free}\ (i\bmod r)}}
\prod_{i=1}^r n_i^{-s}.
$$

This series is absolutely convergent: replacing \(s\) by \(\sigma\)
majorizes it and \(B_{b,\sigma}^r\in S_1\). Thus
\(\det_2(I-zB_{b,s})\) is entire in \(z\) and

$$
\log\det_2(I-zB_{b,s})
=-\sum_{r\ge2}\frac{z^r}{r}\operatorname{Tr}(B_{b,s}^r)
$$

for \(|z|\) sufficiently small. The ordinary trace and determinant are
asserted only for \(\sigma>\alpha_b\).

Distinct powers \(b^j\) form an infinite clique because their nonzero digits
occupy different positions. For \(b=2\) there are no loops. Alternating two
distinct powers realizes least period two, and a word of \(r\ge3\) distinct
powers realizes least period \(r\); hence the least-period set is exactly
\(\{r\ge2\}\). For \(b>2\), \(1\) has a loop, while distinct-power words
realize every \(r\ge2\), so the least-period set is every positive integer.
Shifting all chosen digit positions yields infinitely many witnesses.

Unweighted fixed-point counts are infinite for every allowed length (for
binary, every length at least two). Therefore no Artin–Mazur zeta is
claimed. Least periods are support statements and are not inferred from
possible cancellations in complex weighted traces.

## Ownership and scope

The finite tensor and singular-value controls are not claimed as new. The
theorem concerns the infinite positive-vertex Dirichlet-weighted shell sum,
all radices, every finite Schatten index, and strict equality endpoints.
