# HCS-C28 results

## Outcome

The raw all-prime finite-Weil assembly fails, but a sharply delimited
prime-graded repair exists.  The result is theorem-level and uses no enlarged
prime scan.

## 1. Large-prime character limit

For fixed \(h\in\operatorname{Sp}(J_0,\mathbb Z)\), put
\(r(h)=\operatorname{rank}_{\mathbb Q}(h-I)\).  Outside finitely many
primes, Thomas's formula and rank stability give

\[
\frac{|\Theta_p(h)|}{p^2}=p^{-r(h)/2}.
\]

Thus \(p^{-2}\Theta_p(h)\to\mathbf1_{h=I}\).  This is the regular character
limit for the discrete integral cocycle group.

## 2. Sharp Schatten phase diagram

Compression by constants and interior evaluation, followed by a normalized
trace test against one inverse branch matrix, gives the lower bound
\(\|\mathcal L_{s,p}\|_{S_q}\gtrsim p^{2/q}\).  C26 branch summability gives
the reverse inequality.  Hence

\[
\|\mathcal L_{s,p}\|_{S_q}\asymp p^{2/q},
\qquad
\bigoplus_p c_p\mathcal L_{s,p}\in S_q
\Longleftrightarrow
\sum_p p^2|c_p|^q<\infty.
\]

For \(c_p=p^{-z}\), membership is equivalent to
\(q\operatorname{Re}z>3\).  The boundary is genuinely divergent.  Examples:

| Weight | Exact conclusion |
|---|---|
| \(z=0\) | not compact; no finite-order regularized determinant |
| \(z=1\) | first available regularized determinant is \(\det_4\) |
| \(z=2\) | \(S_2\setminus S_1\); \(\det_2\) deletes the first trace |
| \(\operatorname{Re}z=3\) | not trace class; prime-harmonic boundary |
| \(\operatorname{Re}z>3\) | ordinary trace-class Fredholm determinant |

## 3. Positive global determinant

On \(\operatorname{Re}s>-\sigma_0\), \(\operatorname{Re}z>3\),

\[
\mathfrak D(s,z,u)
=\det(I-u\mathfrak L_{s,z})
=\prod_{p\ {\rm odd}}D_p(s,u p^{-z})
\]

converges locally normally, is independent of prime enumeration, and is
jointly holomorphic in \((s,z,u)\).  Its word trace uses the exact
chronological matrix \(g_w\).  The added prime weight is a second Dirichlet
clock and is not source-derived.

For regular words \(D_w=\det(I-g_w)\ne0\), the inner odd-prime sum is an
orbit-dependent quadratic prime Dirichlet series plus finitely many
singular-prime corrections:

\[
P_{\chi_w}^{\rm odd}(q)
=\sum_{k\ge1}\frac{\mu(k)}{k}\log L(kq,\chi_w^k)
 -\chi_w(2)2^{-q},
\qquad \operatorname{Re}q>1.
\]

The logarithm is the Euler-product branch, and \(\chi_w^k\) is the pointwise
power (possibly imprimitive).  Fixed-space words use the singular
Gauss/prime-power law instead.  The character and conductor vary with
\(w\); no single global quadratic \(L\)-function is obtained.

## 4. Canonicality trilemma

1. Counting trace: the undamped direct sum is noncompact.
2. Normalized trace: the limit exists, but freeness of the positive return
   monoid makes every positive moment zero and the determinant germ one.
3. Prime damping: the determinant is nontrivial and rigorous for
   \(\operatorname{Re}z>3\), but \(z\log p\) is external to the AGY roof.

This trilemma is the central obstruction to calling C28 an intrinsic
one-clock Hilbert--Pólya construction.

## 5. Exact full-Rauzy fixed-plane obstruction

The frozen C24 ledger contains

\[
g_{073}=
\begin{pmatrix}
1&8&4&4\\
1&13&6&6\\
1&6&4&3\\
1&2&1&2
\end{pmatrix},
\qquad
\chi_{073}(x)=(x-1)^2(x^2-18x+1).
\]

All \(3\times3\) minors of \(g_{073}-I\) vanish and the gcd of its
\(2\times2\) minors is one, so its fixed-space dimension is exactly two over
every finite field.  The exact Thomas quotient has determinant \(-4\), and
for every odd prime

\[
\Theta_p(g_{073})
=\left(\frac{-4}{p}\right)
 \left(\frac{-1}{p}\right)p=p.
\]

Therefore
\(\sum_{p\ {\rm odd}}p^{-2}\Theta_p(g_{073})
=\sum_{p\ {\rm odd}}1/p\) diverges.  The exact
146-cycle census is

```text
fixed dimension 0: 125
fixed dimension 1:  20
fixed dimension 2:   1  (C24-P073)
```

This proves failure for a dimension-normalized marked assembly on the full
C24 Rauzy ledger.  It does not prove that P073 occurs in the selected C26
induced language; that all-word gate remains open.

## Route-A conclusion

The result supports an analytic determinant but not a Riemann determinant:

```text
(A1_WEAK, A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)
```

Overall: `ROUTE_A_EXPLORATORY`.  Route B is not authorized.
