# HCS-C49 proof package

This file records the derivations that are easiest to get subtly wrong:
the radial multiplicities, the Fermat signs, the Fano odd-cohomology sign,
and the scope of the smoothness certificate.

## A. Radial multiplicities

For a nonzero representative \(v\),

\[
 \Phi(\lambda v)=\lambda^2(2\lambda\mathcal C(v)+\mathcal Q(v)).
\]

The four disjoint projective strata and their numbers of **nonzero** radial
solutions are

| stratum | nonzero radial roots |
|---|---:|
| \(\mathcal C\ne0,\mathcal Q\ne0\) | \(1\) |
| \(\mathcal C\ne0,\mathcal Q=0\) | \(0\) |
| \(\mathcal C=0,\mathcal Q\ne0\) | \(0\) |
| \(\mathcal C=\mathcal Q=0\) | \(p-1\) |

Adding the affine origin gives

\[
 Z=1+(\#\mathbf P^5-\#S-\#Q+\#X)+(p-1)\#X,
\]

which is equation (4) of the theorem package.

## B. Split-quadric count without a classification theorem

With \(e,o,M_\rho\) as in (5), \(e^tM_\rho o=0\).  If \(e=0\), there are
\(p^3\) choices of \(o\).  For each of the \(p^3-1\) nonzero \(e\), the
equation is one nonzero linear equation in \(o\), hence has \(p^2\)
solutions.  The affine cone therefore has \(p^5+p^3-p^2\) points, and

\[
 \frac{p^5+p^3-p^2-1}{p-1}=p^4+p^3+2p^2+p+1.
\]

## C. Fermat cubic character calculation

Fix a nontrivial additive character \(\psi\) and write

\[
 G=\sum_x\chi(x)\psi(x),\qquad
 \bar G=\sum_x\bar\chi(x)\psi(x).
\]

For \(t\ne0\), the number of cube roots of \(y\) is
\(1+\chi(y)+\bar\chi(y)\), including \(y=0\).  Consequently

\[
 \sum_x\psi(tx^3)=\bar\chi(t)G+\chi(t)\bar G.
\]

Additive orthogonality gives the number \(N_S^{\mathrm{aff}}\) of affine
zeros of \(\sum_{i=0}^5x_i^3\):

\[
 N_S^{\mathrm{aff}}
 =p^5+\frac1p\sum_{t\ne0}
       (\bar\chi(t)G+\chi(t)\bar G)^6.
\]

Only binomial indices \(0,3,6\) survive the sum over \(t\), so

\[
 N_S^{\mathrm{aff}}
 =p^5+\frac{p-1}{p}(G^6+20G^3\bar G^3+\bar G^6).       \tag{C.1}
\]

Because \(p\equiv1\pmod6\), \(\chi(-1)=1\) and \(G\bar G=p\).  If
\(\pi=J(\chi,\chi)\), then

\[
 \pi=\frac{G^2}{\bar G}=\frac{G^3}{p},
 \qquad G^3=p\pi,
\]

and similarly \(\bar G^3=p\bar\pi\).  Equation (C.1) becomes

\[
 N_S^{\mathrm{aff}}
 =p^5+p(p-1)(\pi^2+\bar\pi^2)+20p^2(p-1).
\]

Since \(N_S^{\mathrm{aff}}=1+(p-1)\#S\), division proves

\[
 \#S=(1+p+p^2+p^3+p^4)+pa_p+20p^2.
\]

This also fixes the sign: each of the twenty mixed primitive sectors has
Frobenius eigenvalue \(+p^2\), not \(-p^2\).

## D. Smoothness: theorem-level finite-exception proof

Both hypersurfaces \(S\) and \(Q_\rho\) are smooth in characteristic
different from \(3\), respectively \(2,3\).  If their intersection is
singular, their gradients are proportional.  With

\[
 q_0=x_1+\rho x_5, q_1=x_0+x_2, q_2=x_1+x_3,
\]
\[
 q_3=x_2+x_4, q_4=x_3+x_5, q_5=x_4+\rho x_0,
\]

the proportionality has \(q_i=\kappa x_i^2\) with \(\kappa\ne0\).
Projectively rescaling \(x\mapsto\kappa x\) reduces it to

\[
 q_i=x_i^2\qquad(0\le i\le5).                            \tag{D.1}
\]

Starting with \(x=x_0,y=x_1\), set recursively

\[
 x_2=y^2-x,\quad x_3=x_2^2-y,\quad
 x_4=x_3^2-x_2,\quad x_5=x_4^2-x_3,                     \tag{D.2}
\]

and define

\[
 f=y+\rho x_5-x^2,\qquad
 g=x_4+\rho x-x_5^2,\qquad
 h=\sum_{i=0}^5x_i^3.                                   \tag{D.3}
\]

The projective singular locus is the nonzero zero set of \(f,g,h\).
Exact lexicographic elimination over \(\mathbf Q(\rho)\) gives reduced
basis \(\{y,x\}\).  Therefore the characteristic-zero member is smooth.
Spreading out over \(\mathbf Z[\rho,1/6]\) and openness of the smooth locus
give a finite exceptional set \(\Sigma_{\mathrm{sm}}\).  This is the
unconditional smoothness input used by the analytic theorem.

## E. Candidate all-split certificate and exact replay data

This subsection records the stronger exact calculation.  It is a release
gate until two independent implementations reproduce the polynomial
identities; the main theorem does not depend on its promotion.

Assume \(x_0\ne0\), put \(t=x_0^3\) and \(u=x_1/x_0^2\), and define

\[
 A_2=tu^2-1,\quad B_3=A_2^2-u,\quad
 A_4=tB_3^2-A_2,\quad B_5=A_4^2-B_3,
\]

\[
 F=u+\rho B_5-1,\qquad
 G=A_4+\rho-tB_5^2,
\]

\[
 L=1+A_2^3+A_4^3+t(u^3+B_3^3+B_5^3).                  \tag{E.1}
\]

Thus \(F=G=L=0\) is exactly (D.1) plus \(h=0\) on \(x_0\ne0\).  With
lexicographic order \(u>t\), the boundary ideal \((F,G)\) has a monic
triangular basis \(u-U_\rho(t),R(t)\), where

\[
\begin{aligned}
R(t)={}&t^{21}-32t^{20}+432t^{19}-3200t^{18}+14192t^{17}
-38960t^{16}\\
&+68992t^{15}-93280t^{14}+128846t^{13}-167888t^{12}
+176266t^{11}\\
&-130240t^{10}+17436t^9-160t^8-31172t^7-5384t^6
-4090t^5\\
&-3640t^4-948t^3-96t^2-t-1.
\end{aligned}                                             \tag{E.2}
\]

Let \(H(t)\) be the unique degree-at-most-20 normal remainder of \(L\) in
this triangular quotient.  This definition, together with (E.1), fixes
every coefficient without a floating-point choice.  Exact rational
subresultants give

\[
 \boxed{\operatorname{Res}_t(R,H)=2^{21}3^{12}23^3.}      \tag{E.3}
\]

For a literal coefficient replay, put

\[
D_H=279120457625197909574647915374957709828779
\]

and write \(H=(2/D_H)\widetilde H\).  In descending order from \(t^{20}\)
to \(t^0\), the coefficients of the primitive integer polynomial
\(\widetilde H\) are

```text
-145703718178631335347220360120867024686272
4661621627370767144604796374178029740390040
-62914860378264924680387224058288372737725792
465850852912341040228649592911850402799054888
-2064782131154121039518642129245474075586073728
5662673110832763888691094375596214849508927114
-10012578031308468751424550008795016454979710640
13518153111230074404047331240689196360536155048
-18675246318538570340741709291221417666189160704
24332710732466401909973892445306875547645241013
-25510683268342422614780199514657030683736782968
18791793976603365518470373078374490339615195656
-2408254480046539911408547106092940172750841792
13315783568860964077537982156297694958567245
4509667199840392042860762933446160050690341084
807275697640248175371636276793663742605516944
596601679510299209195816160742317568708953968
523424587800883936267583272067364863644382706
135985127526255609704800607472185819916305952
13732724459598184161838717552260124522717626
137707195104673694663949192867180643480421
```

The resultant convention in (E.3) is the rational polynomial \(H\), not
the primitive integral polynomial.  The corresponding integral check is

\[
\begin{aligned}
|\operatorname{Res}(R,\widetilde H)|={}&
3^{96}23^3\cdot
(11\cdot17\cdot61\cdot139\cdot1777\cdot14243\\
&\qquad\cdot14431\cdot14503\cdot29303\cdot50119
\cdot279359053)^{21}.                                  \tag{E.3a}
\end{aligned}
\]

Equivalently, the prime factorization is

\[
3^{96}23^3\prod_{q\in\mathcal D}q^{21},
\quad
\mathcal D=\{11,17,61,139,1777,14243,14431,14503,
29303,50119,279359053\}.                                \tag{E.3b}
\]

The common leading-coefficient denominator of \(U_\rho\) is

\[
\begin{aligned}
\Delta={}&3^6\cdot11\cdot17\cdot61\cdot139\cdot1777
\cdot14243\cdot14431\cdot14503\\
&\cdot29303\cdot50119\cdot279359053,                    \tag{E.4}
\end{aligned}
\]

while \(H\) needs the same product with \(3^4\) in place of \(3^6\).
Away from \(2\cdot3\cdot23\cdot\Delta\), (E.3) rules out a common zero.

The split prime divisors of \(\Delta\) are exactly

\[
 61,139,1777,14431,14503,50119,279359053.                \tag{E.5}
\]

For each prime in (E.5), exact reduction of (D.3) for one order-three
root has reduced lex basis \(\{y,x\}\); the other root is covered by the
explicit isomorphism

\[
 x_0=\rho^2y_5,\quad x_1=y_0,\quad x_2=y_1,\quad
 x_3=y_2,\quad x_4=y_3,\quad x_5=y_4,                    \tag{E.6}
\]

which preserves \(\sum x_i^3\) and sends
\(\mathcal Q_\rho(x)\) to \(\mathcal Q_{\rho^2}(y)\).

For completeness, if \(x_0=0\), (D.1) gives

\[
 x_1=-\rho x_5,\quad x_2=\rho^2x_4,\quad
 x_4=-\rho^2x_3^2.
\]

The cubic equation becomes \(x_3^3(1-2x_3^3)=0\).  The first case gives
the zero vector.  In the second, the \(q_2=x_2^2\) and \(q_4=x_4^2\)
equations respectively give, for \(r=x_5/x_3\),

\[
 r=\rho^2-\rho/2,\qquad r=\rho/2-1,
\]

whose equality reduces to \(2\rho=0\), impossible in characteristic
different from two.

Consequently the only residual resultant characteristics are (2,3,23).
The first two are excluded from the model and \(23\equiv2\pmod3\) is
inert, so no residual characteristic is a split prime.  Promotion of the
all-split statement requires the checker to verify (E.2)--(E.5), not just
to scan small primes.

## F. Fano topology and Frobenius sign

Expanding the normal sequence gives

\[
 c(TX)=\frac{(1+H)^6}{(1+2H)(1+3H)}=1+H+4H^2-6H^3.
\]

Since \(\int_XH^3=6\), \(\chi(X)=-36\).  Weak Lefschetz and Poincare
duality leave only \(b_3\) unknown, so

\[
 -36=1+1-b_3+1+1=4-b_3,
\]

and \(b_3=40\).  The Grothendieck--Lefschetz trace formula has a minus
sign in odd degree:

\[
 \#X=1+p-B_p+p^2+p^3.
\]

This is the source of the term \(-pB_p\), rather than \(+pB_p\), in
\(Z_{p,3}\).

## G. Chevalley--Warning divisibility

For polynomials \(f_j\) over \(\mathbf F_p\), the common-zero count is

\[
 N\equiv\sum_{x\in\mathbf F_p^n}
       \prod_j(1-f_j(x)^{p-1})\pmod p.
\]

If \(\sum_j\deg f_j<n\), every nonconstant expansion term has total
degree \(<(p-1)n\), hence some variable exponent is \(<p-1\); summation in
that variable vanishes modulo \(p\).  The constant term also sums to
\(p^n\equiv0\).  Thus \(p\mid N\).

For the \((2,3)\) cone, \(2+3<6\), so

\[
 0\equiv N_{\mathrm{cone}}
 =1+(p-1)\#X\equiv1-\#X\pmod p.
\]

Therefore \(B_p=(1+p+p^2+p^3)-\#X\) is divisible by \(p\).

## H. Convergence at the new wall

For a compact subset of \(\Re s>1/4\), choose
\(\sigma_0>1/4\) below all real parts and \(P_0\) so that
\(4p^{-\sigma_0}\le1/2\) for \(p>P_0\).  Then

\[
 \sum_{p>P_0}\sum_{n\ge4}
 \frac{|c_{p,n}|}{n}p^{-n\sigma_0}
 \ll\sum_{p>P_0}p^{-4\sigma_0}<\infty.
\]

For the finitely many \(p\le P_0\), the local unitary-block estimate
\(|c_{p,n}|\le\tau_p(I)=(8p+4)/3\) makes the \(n\)-series geometric.
The explicit \(n=1,2,3\) estimates finish local normal convergence.
