# Theorem package

For (epsilon>0), let
\[
 u_t=u_{xx}+\epsilon^{-2}(u-u^3),\qquad
 W(u)=\tfrac14(1-u^2)^2.
\]
Every (C^2) monotone solution of
(U''+cU'+\epsilon^{-2}(U-U^3)=0) with (U(-\infty)=-1) and
(U(+\infty)=1) has (c=0) and is
(U_\epsilon(\xi-\xi_0)=\tanh((\xi-\xi_0)/(\sqrt2\epsilon))).
For (c=0), ((U')^2/2=\epsilon^{-2}W(U)), and
\[
 \int_\mathbb R\left(\tfrac12U'^2+\epsilon^{-2}W(U)\right)d\xi
 =\frac{2\sqrt2}{3\epsilon}.
\]

The gradient-flow energy satisfies (dE_\epsilon/dt=-\int u_t^2dx\) for smooth
finite-relative-energy solutions.  With (y=\xi/(\sqrt2\epsilon)),
\[
 L_\epsilon=\partial_\xi^2+\epsilon^{-2}(1-3U_\epsilon^2)
 =\frac1{2\epsilon^2}(\partial_y^2-4+6\operatorname{sech}^2y).
\]
The factorization
(-\partial_y^2+4-6\operatorname{sech}^2y=B^*B), (B=\partial_y+2\tanh y),
gives the simple kernel (U_\epsilon').  The second bound state is
(\operatorname{sech}y\tanh y) with eigenvalue (-3/(2\epsilon^2)), and
(\sigma_{\rm ess}(L_\epsilon)=(-\infty,-2/\epsilon^2]).

The theorem is one-dimensional and equal-well.  It does not assert a
multidimensional transverse stability rate, a global attractor, a nonzero-speed
front, or any arithmetic/Hilbert--Pólya correspondence.
