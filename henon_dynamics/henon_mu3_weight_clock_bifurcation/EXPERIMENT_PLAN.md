# Reproducible experiment plan

## E1. Source cancellation

For \(n=2,3,4\), replay

\[
 Z_{p,n}=1+P_{2n-1}-\#S_n-\#Q_n+p\#X_n
\]

and verify

\[
 Z_{p,n}=p^{2n-1}-p^{n-1}-A_{p,n}-pB_{p,n},\qquad
 C_{p,n}=-2-\frac{2A_{p,n}}{p^{n-1}}
              -\frac{2B_{p,n}}{p^{n-2}}.
\]

Use exact integers and rationals only.  Reject any replay that changes the
ordered closing edge.

## E2. Rank identity

Compute

\[
 b^{\mathrm{prim}}_{2n-2}(S_n)=\frac{4^n+2}{3}
\]

from the cubic Jacobian ring, and extract
\([H^{2n-3}](1+H)^{2n}/((1+2H)(1+3H))\) to obtain

\[
 b_{2n-3}(X_n)=\frac{2(4^n-4)}{3}.
\]

The symbolic control may run through \(2\le n\le20\), but the released
Hénon application must remain restricted to the smooth rows \(n=2,3,4\).

## E3. Weight and center ledger

Construct \(E_n,O_n\), record their weights \(0,1\), and evaluate

\[
 s_{n,j}(w)=\frac{(w+1)/2-j}{n}
\]

for \(n=2,3,4\), \(w=0,1\), and several \(j\ge1\).  Require the exact
leading spectrum

\[
 \left\{-\frac14,-\frac16,-\frac18,0\right\}.
\]

The checker must reject a zero-based \(j\) convention unless it is
explicitly converted to the canonical \(j\ge1\) convention.

## E4. Logarithmic residual

Expand every standard local factor through degree two.  Subtract the
leading term forced by \(C_{p,n}\), and verify that the residual local
logarithm is \(O(p^{-2n\Re s-1})\).  This proves normal convergence and
nonvanishing of \(H_{n,S}\) on \(\Re s>0\).  No functional-equation field
is permitted for \(H_{n,S}\).

## E5. Twist and divisibility attacks

Check that a Tate twist \(k\) changes
\((w,j)\) to \((w-2k,j-k)\) and leaves \(s_{n,j}(w)\) fixed.  A formal
half twist must obey the same rule; holding \(u\) fixed is a forbidden
coefficient change.

For the direct source-native \(K\)-packet, verify

\[
 \frac23(23,40)=\left(\frac{46}{3},\frac{80}{3}\right),\qquad
 \frac12(87+168)=\frac{255}{2}.
\]

Record explicitly that restriction of scalars and Galois counterpackets
are outside this no-go statement.

## E6. Hodge ledger

Expand

\[
 Q_y(x)=\frac{x(1+ye^{-x})}{1-e^{-x}}
 =(1+y)+\frac{1-y}{2}x+\frac{1+y}{12}x^2
  -\frac{1+y}{720}x^4+O(x^6)
\]

and compute

\[
 \chi_y(X_4)=6[H^5]\,
 \frac{Q_y(H)^8}{(1+y)Q_y(2H)Q_y(3H)}
 =1-82y^2+82y^3-y^5.
\]

Compare with weak Lefschetz to recover
\(h^{4,1}=1\) and \(h^{3,2}=83\).

## E7. Fail-closed release checks

- Independent checker gates must replay semantic values, not merely hashes.
- Mutation tests must attack clock indexing, ranks, trace signs, weight
  labels, center values, and overclaim fields.
- Unknown schema keys and missing containers must fail.
- The paper may cite test counts only after code/results freeze.
- The final manifest must include root docs, both Route-A records, paper
  sources/PDF/report, code, and results.
