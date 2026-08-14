# HCS-C49 derivation package

## Frozen chain

\[
\text{six ordered Hénon kernel steps}
\longrightarrow \Phi_{p,3}^{-1}(0)
\longrightarrow (S,Q_\rho,X_\rho)
\longrightarrow (A_p,B_p)
\longrightarrow c_{p,3}.
\]

No chronological edge is averaged or reordered.

## Exact substitutions

Let \(\Pi_m(p)=1+p+\cdots+p^m\).  The three projective counts are

\[
 \#S=\Pi_4+ A_p,
 \quad A_p=20p^2+pa_p,
\]

\[
 \#Q_\rho=1+p+2p^2+p^3+p^4,
\]

\[
 \#X_\rho=1+p+p^2+p^3-B_p.
\]

Therefore

\[
\begin{aligned}
Z_{p,3}
&=1+\Pi_5-(\Pi_4+A_p)
 -(1+p+2p^2+p^3+p^4)\\
&\qquad+p(1+p+p^2+p^3-B_p)\\
&=p^5-p^2-A_p-pB_p.
\end{aligned}
\]

The normalization now gives

\[
\begin{aligned}
C_{p,3}
 &=2p^{-2}Z_{p,3}-2p^3\\
 &=-2-2A_p/p^2-2B_p/p.
\end{aligned}
\]

With \(b_p=B_p/p\) and \(d_p=(p-1)/2\),

\[
C_{p,3}=-42-2b_p-2a_p/p,
\]

\[
c_{p,3}=\frac{2C_{p,3}}{p-1}
=-\frac4{p-1}(21+b_p+a_p/p).
\]

## Weight ledger

| piece | rank | weight | trace size | contribution to \(c_{p,3}\) |
|---|---:|---:|---:|---:|
| Fermat mixed primitive sectors | 20 | 4 | \(20p^2\) exactly | \(O(p^{-1})\) |
| Fermat pure Jacobi sectors | 2 | 4 | \(pa_p=O(p^2)\) | \(O(p^{-1})\) |
| Fano middle cohomology | 40 | 3 | \(B_p=O(p^{3/2})\) | \(O(p^{-1/2})\) |

The Fano term is dominant but still gains a square root after the real
cyclotomic degree normalization.

## Analytic threshold ledger

| moment | coefficient input | prime-series condition |
|---:|---|---|
| 1 | \(O(p^{-1})\) | \(\sigma>0\) |
| 2 | \(O(p^{-1/2})\) | \(2\sigma+1/2>1\) |
| 3 | \(O(p^{-1/2})\) | \(3\sigma+1/2>1\) |
| \(n\ge4\) | \(O(4^n)\) | \(4\sigma>1\) for the first tail term |

Thus moments two and the uniform tail meet at \(\sigma=1/4\); moment three
is no longer a wall.

## What remains empirical

The finite ledger suggests unexpectedly structured integers \(b_p\), but
this package proves only \(b_p\in\mathbf Z\) and
\(|b_p|\le40\sqrt p\).  It does not assert Sato--Tate behavior, an
intermediate-Jacobian factorization over \(\mathbf F_p\), or a compatible
global \(L\)-function.
