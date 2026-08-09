# Narrative report — LOG-0001 lower-growth stage

## Frozen object

Keep the same exact-\(U_c\) polar matching-space determinant

\[
D_{\rm pol}(s)=\det_{\rm Fr}(I-\mathcal L_{s,B})
\]

and its signed based-word trace identity.  No finite matrix, reciprocal zeta,
or separately glued product replaces this determinant.

## Cancellation-safe derivative

Let

\[
\alpha_0=\frac{U_c^2}{4},\qquad
\tau_*=-\log\alpha_0,
\qquad
B_2=\frac{-\log(1-2\alpha_0^2)}{1-\alpha_0}.
\]

At the safe point \(s=2\), the signed trace logarithm converges absolutely.
For real \(\sigma\) in the zero-free half-plane, every exact denominator
\(1-\varepsilon_\omega e^{-T_\omega}\) is positive.  The complete trace sum
\(S(\sigma)\) is therefore positive, while
\(\log D_{\rm pol}(\sigma)=-S(\sigma)<0\).  Its derivative is

\[
\frac{d}{d\sigma}\log D_{\rm pol}(\sigma)
=\sum_{n\ge1}\frac1n
 \sum_{\omega\in\{L,R\}^n}
 \frac{T_\omega e^{-\sigma T_\omega}}
 {1-\varepsilon_\omega e^{-T_\omega}}>0.
\]

The absolute trace majorant gives
\(D_{\rm pol}(2)\ge e^{-B_2}\).  The pure-left length-one word has
\(T_L=\tau_*\), \(e^{-T_L}=\alpha_0\), and \(\varepsilon_L=1\).  Retaining
that positive term, without changing any other signed denominator, yields

\[
D_{\rm pol}'(2)\ge
e^{-B_2}\frac{\tau_*\alpha_0^2}{1-\alpha_0}
=0.0213084085497861\ldots>0.0213.
\]

## Maximum modulus and transcendence

For \(R>2\), the disk centered at \(2\) with radius \(R-2\) lies inside
\(|s|\le R\).  Cauchy's derivative estimate therefore gives

\[
M_D(R):=\max_{|s|\le R}|D_{\rm pol}(s)|
\ge (R-2)|D_{\rm pol}'(2)|
>0.0213(R-2).
\]

For \(R\ge4\), this implies \(M_D(R)>0.01065R\).

The same trace majorant tends to zero as \(\sigma\to+\infty\), so
\(D_{\rm pol}(\sigma)\to1\).  Since the derivative at \(2\) is nonzero, the
entire determinant is nonconstant; since a nonconstant polynomial cannot tend
to one on the positive real ray, it is transcendental entire.  Consequently,
for every fixed \(A>0\),

\[
\frac{M_D(R)}{R^A}\longrightarrow\infty.
\]

This last statement is qualitative: it follows from the existence of
arbitrarily high nonzero Taylor coefficients and gives no explicit
coefficient sequence or quantitative order.

## Claim boundary

The stage proves nonconstancy, a certified derivative lower bound, a linear
explicit maximum-modulus lower bound, and qualitative transcendental
super-polynomial growth.  It proves none of the following: positive order,
exact order, an exponential lower bound, a determinant-zero lower bound, a
sharp divisor asymptotic, a \(T\log T\) law, completed-xi structure,
quantization, Route B, Hilbert--Polya, or RH.
