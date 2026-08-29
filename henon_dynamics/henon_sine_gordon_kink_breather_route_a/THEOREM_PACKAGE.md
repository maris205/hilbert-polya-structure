# Theorem package

Consider
\[
 u_{tt}-u_{xx}+\sin u=0,
 \qquad {ℓ}(u,u_t)=\tfrac12(u_t^2+u_x^2)+1-\cos u,
\]
with finite relative energy and topological charge
$Q=(u(+\infty)-u(-\infty))/(2\pi)$ whenever the limits exist.

## Declared coherent-family theorem

1. Start with the unrestricted ansatz $u(x,t)=U(x-vt)$.  Its profile equation
   is $(v^2-1)U''+\sin U=0$.  Multiplication by $U'$ and the vacuum limits give
   $\tfrac12(v^2-1)(U')^2=\cos U-1$; a nonconstant heteroclinic therefore has
   $|v|<1$.  With $\xi=\gamma_v(x-vt-x_0)$, every finite-energy monotone
   heteroclinic is, up to translation,
   $U_{k,+}(\xi)=2\pi k+4\arctan e^\xi$ or
   $U_{k,-}(\xi)=2\pi k+4\arctan e^{-\xi}$, $k\in\mathbb Z$.
   The certificate rows use the canonical $k=0$ representatives.  Its energy and
   momentum are
   $E=8\gamma_v$, $P=8\gamma_vv$ under the locked sign convention, hence
   $E^2-P^2=64$ and $Q=\pm1$.
2. For $0<\Omega<1$, set $\eta=(1-\Omega^2)^{1/2}$.  The rest breather
   $u_B=4\arctan[\eta\sin(\Omega t)/(\Omega\cosh(\eta x))]$ is exact, has
   rest energy $16\eta$, zero rest momentum, charge $0$, and internal period
   $2\pi/\Omega$.  A boost with $\xi=\gamma_V(x-Vt)$ and
   $\tau=\gamma_V(t-Vx)$ gives $E=16\eta\gamma_V$ and
   $P=16\eta\gamma_VV$.  The period statement is in the comoving clock;
   no fixed-laboratory-point period is asserted for $V\ne0$.
3. At the rest kink, the Hessian
   $L_K=-\partial_x^2+1-2\operatorname{sech}^2x$ factors as
   $A^*A$ with $A=\partial_x+\tanh x$.  Its spectrum is
   $\{0\}\cup[1,\infty)$, the kernel is spanned by $2\operatorname{sech}x$,
   and there is no internal discrete mode.

The edge faces are $|v|\uparrow1$ (collapsing width and divergent energy),
$\Omega\uparrow1$ (zero-amplitude vacuum), $\Omega\downarrow0$
(infinite-period separatrix), $V=0$ (rest breather), and $V\ne0$ (boosted,
comoving period only).  The theorem is a declaration about these coherent
families, not a classification of every finite-energy solution; no nonlinear
stability rate is inferred.

The strict Route-A record is
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`overall=ROUTE_A_REJECTED`, `route_b_invocation_allowed=false`.  There is no
primitive periodic-orbit ledger and no arithmetic or Hilbert--Pólya operator.
