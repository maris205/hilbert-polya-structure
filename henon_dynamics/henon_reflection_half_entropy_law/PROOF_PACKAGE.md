# Proof package

## 1. Reversal identity

Let

\[
A=\begin{pmatrix}
1&0&1&0\\1&0&0&0\\0&1&0&1\\0&1&0&0
\end{pmatrix},
\qquad \rho=(0)(1\ 2)(3),
\]

and let `P` be the permutation matrix of `rho`.  Direct multiplication gives

\[
A=P A^{\mathsf T}P.
\]

For a cyclic word `w` of length `n`, define

\[
(R_k w)_j=\rho(w_{-j-k}).
\]

## 2. Closed and fixed words

The characteristic polynomial is

\[
(z^2+1)(z^2-z-1),
\]

so, with Fibonacci `F_m` and Lucas `L_m`,

\[
\operatorname{tr}(A^n)=L_n+2\cos(\pi n/2).
\]

For odd `n=2m+1`, every reflection is conjugate and

\[
\#\operatorname{Fix}(R_k)=F_{m+2}.
\]

For even `n=2m`, the even-index (edge--edge) class has

\[
G_m=L_m,
\]

whereas the odd-index (vertex--vertex) class has

\[
H_m=F_m+\frac25L_m-\frac45\cos(\pi m/2)
-\frac25\sin(\pi m/2).
\]

Each identity follows by choosing the two boundary symbol sets on a half-word
and summing the corresponding entries of `A^m` or `A^(m-1)`.

## 3. Primitive inversion

Let `C_n` be the number of primitive cyclic necklaces.  Then

\[
C_n=\frac1n\sum_{d\mid n}\mu(n/d)\operatorname{tr}(A^d).
\]

For odd `n`, the primitive reversible count is

\[
R_n=\sum_{d\mid n}\mu(n/d)F_{(d+3)/2}.
\]

For even `n`, define `Fix_E(d)` and `Fix_V(d)` to equal the odd formula when
`d` is odd and to equal `G_{d/2}` or `H_{d/2}` when `d` is even.  Then

\[
R_n^E=\frac12\sum_{d\mid n}\mu(n/d)\operatorname{Fix}_E(d),
\qquad
R_n^V=\frac12\sum_{d\mid n}\mu(n/d)\operatorname{Fix}_V(d).
\]

The factor `1/2` is forced: for a fixed even reflection, a compatible
primitive necklace has two rotated representatives fixed by it.  For odd
period, multiplication by two is invertible modulo `n`, so there is one.

## 4. Half entropy

Let `phi=(1+sqrt(5))/2`.  The dominant terms give

\[
C_n\sim\frac{\phi^n}{n},\qquad
R_n=\Theta(\phi^{n/2}).
\]

Proper-divisor terms are exponentially smaller.  Therefore

\[
\lim_{n\to\infty}\frac1n\log C_n=\log\phi,
\qquad
\lim_{n\to\infty}\frac1n\log R_n=\frac12\log\phi,
\]

and `R_n/C_n=O(n phi^(-n/2))`.

## 5. Boundary

The theorem counts physical symbolic necklaces.  It does not count roots of
the algebraic closure polynomials or embeddings of their trace fields.  That
distinction is exactly the P58 interface.
