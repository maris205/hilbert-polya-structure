# C210 exact theorem package

## Frozen owner

For \(a,b,\tau\geq0\), let \(x\) solve
\(x'=-ax-bx(t-\tau)\) from a continuous history on
\([-\tau,0]\).  For \(\tau>0\) the state is
\(x_t(\theta)=x(t+\theta)\) in \(X=C([-\tau,0];\mathbb C)\), and
\[
 A\phi=\phi',\qquad
 D(A)=\{\phi\in C^1:\phi'(0)=-a\phi(0)-b\phi(-\tau)\}.
\]
The clock is physical elapsed time; no fitted scale is introduced.

## Theorem 1 — characteristic roots and Lambert branches

The characteristic determinant is
\[
 \Delta(\lambda)=\lambda+a+b e^{-\lambda\tau}.
\]
For \(\tau>0,b>0\), every root, with algebraic multiplicity, is
\[
 \lambda_k=-a+\tau^{-1}W_k(-b\tau e^{a\tau}),\qquad k\in\mathbb Z.
\]
At the Lambert branch point the \(W_0,W_{-1}\) values coalesce.  Direct
 differentiation gives \(\Delta'=1-b\tau e^{-\lambda\tau}\).  A multiple
 root therefore satisfies
\[
 \lambda=-a-\tau^{-1},\qquad b\tau e^{a\tau}=e^{-1},
\]
and \(\Delta''\neq0\) when \(b>0\), so multiplicity is at most two.
The cases \(b=0\) and \(\tau=0\) reduce separately to the scalar ODE.

## Theorem 2 — exact method of steps and semigroup

With \(r(t)=0\) for \(t<0\) and \(r(0)=1\), the fundamental solution for
\(\tau>0\) is
\[
 r(t)=\sum_{n=0}^{\lfloor t/\tau\rfloor}
 \frac{(-b)^n}{n!}e^{-a(t-n\tau)}(t-n\tau)^n,\qquad t\geq0.
\]
It follows by Laplace expansion of
\(\Delta(s)^{-1}=(s+a)^{-1}\sum_{n\geq0}[-b e^{-s\tau}/(s+a)]^n\).
The history solution operators \(T(t)\) are a strongly continuous semigroup.
For \(t>\tau\), \(T(t)X\subset C^1\), hence Arzelà--Ascoli makes \(T(t)\)
compact.  Eventual compactness gives the nonzero spectral mapping
\[
\sigma(T(t))\setminus\{0\}=\exp(t\,\sigma(A)).
\]
At a nonzero semigroup eigenvalue \(\mu\), algebraic multiplicity is the sum
of characteristic-root multiplicities over all roots with
\(e^{t\lambda}=\mu\); exponential collisions are aggregated.

## Theorem 3 — complete nonnegative stability/Hopf atlas

If \(a\geq b\) and \((a,b)\ne(0,0)\), every finite delay is exponentially
stable.  If \(b>a\), put
\[
 \omega=\sqrt{b^2-a^2},\qquad
 \tau_c=\frac{\arccos(-a/b)}{\omega}.
\]
The semigroup is exponentially stable exactly for \(0\leq\tau<\tau_c\);
at \(\tau=\tau_c\) the only imaginary roots are the simple pair
\(\pm i\omega\), and for larger \(\tau\) a conjugate pair lies in the
right half-plane.  Differentiating \(\Delta(\lambda,\tau)=0\) at a crossing
gives
\[
 \frac{d\,\Re\lambda}{d\tau}
 =\frac{\omega^2}{(1+a\tau)^2+(\omega\tau)^2}>0.
\]
The equal-rate boundary \(a=b>0\) has no finite-delay imaginary root but its
spectral gap tends to zero as \(\tau\to\infty\).  At \(\tau=0\) the equation
is \(x'=-(a+b)x\), with fundamental solution \(r(0)=1\) and
\(r(t)=e^{-(a+b)t}\) for \(t>0\); at \(b=0\) there is no delayed feedback; and at
\(a=b=0\) histories become constant after one delay.  Hopf center solutions
are a two-dimensional linear family, not isolated primitive cycles.

## Boundary and scope

The displayed \(\Delta\) is a source characteristic determinant only.  No
Fredholm determinant, arithmetic divisor, prime clock, target spectrum or
Hilbert--Pólya operator is claimed.  Finite exact rows are regression
sentinels; the all-parameter assertions are proved by the identities above.
