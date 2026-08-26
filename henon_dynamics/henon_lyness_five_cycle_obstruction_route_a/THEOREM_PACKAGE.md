# C173 theorem package

Let (X=(0,\infty)^2),

\[
F(x,y)=\left(y,\frac{1+y}{x}\right),\qquad
R(x,y)=(y,x),\qquad d\mu=\frac{dx\,dy}{xy}.
\]

All statements below are source-side results about this frozen system.

## Theorem 1: exact global period law

For every ((x,y)\in X),

\[
\begin{aligned}
F(x,y)&=\left(y,\frac{1+y}{x}\right),\\
F^2(x,y)&=\left(\frac{1+y}{x},\frac{1+x+y}{xy}\right),\\
F^3(x,y)&=\left(\frac{1+x+y}{xy},\frac{1+x}{y}\right),\\
F^4(x,y)&=\left(\frac{1+x}{y},x\right),\\
F^5(x,y)&=(x,y).
\end{aligned}
\]

The unique fixed point is ((\phi,\phi)), where
(\phi=(1+\sqrt5)/2).  Every other point has exact least period five.

### Proof

Direct substitution gives the five displayed rational maps; all
denominators are positive on (X), so the identity is global.  A fixed
point must satisfy (y=x) and (x^2=x+1).  Exactly one root of this
quadratic is positive, namely (\phi).  Since (F^5=I), every least period
divides the prime number five.  Removing the unique period-one point leaves
least period five.  ∎

## Corollary 2: Artin--Mazur obstruction

For positive integers (n),

\[
\operatorname{Fix}(F^n)=
\begin{cases}
\{(\phi,\phi)\},&5\nmid n,\\
X,&5\mid n.
\end{cases}
\]

Consequently the classical series

\[
\zeta_{\rm AM}(z)=\exp\!\left(\sum_{n\ge1}
\#\operatorname{Fix}(F^n)\frac{z^n}{n}\right)
\]

is not defined: its fifth fixed-point count is uncountable.  Likewise there
is no Euler product over a finite or countable family of isolated primitive
periodic orbits.  No regularization or Lefschetz substitute is asserted.

## Theorem 3: invariant geometry and reversal

The measure (\mu) is invariant, (R) is an involution, and
(RFR=F^{-1}), with

\[
F^{-1}(x,y)=\left(\frac{1+x}{y},x\right).
\]

### Proof

The Jacobian determinant is ((1+y)/x^2), while the product of the two
image coordinates is (y(1+y)/x).  Hence the pulled-back density is

\[
\frac{|\det DF(x,y)|}{F_1(x,y)F_2(x,y)}=\frac1{xy}.
\]

The inverse and reversor identities follow by direct substitution.  ∎

## Theorem 4: natural Koopman decomposition and operator obstruction

On (H=L^2(X,\mu)), define (Uf=f\circ F).  Then (U) is unitary and
(U^5=I).  With (\omega=e^{2\pi i/5}),

\[
P_j=\frac15\sum_{r=0}^4\omega^{-jr}U^r,
\qquad j=0,\ldots,4,
\]

are mutually orthogonal projections satisfying
(\operatorname{ran}P_j=\ker(U-\omega^jI)) and
(\sum_jP_j=I).  Every one of the five ranges is infinite-dimensional.
Therefore (U) is noncompact, belongs to no finite Schatten class, is not
trace class, has no ordinary trace-class Fredholm determinant
(\det(I-zU)), and is not self-adjoint.

### Proof

Measure invariance and invertibility make (U) unitary; (F^5=I) gives
(U^5=I).  Finite cyclic Fourier orthogonality proves the projection
identities and fixes the negative sign in (\omega^{-jr}).

Away from the single fixed point, the action is free.  Because (X) is
nonatomic and sigma-finite, one can choose countably many positive finite
measure sets (A_m) whose five translates are mutually disjoint, including
between different (m).  For nonzero (h_m\) supported on (A_m), the five
terms in (P_jh_m) have disjoint supports, so
(\|P_jh_m\|^2=\|h_m\|^2/5>0).  Different (m) give orthogonal vectors.
Thus each range is infinite-dimensional.

A compact operator cannot have a nonzero eigenvalue of infinite
multiplicity; hence (U) is not compact, and no finite Schatten membership
or ordinary trace-class determinant follows.  If a unitary (U) were
self-adjoint, then (U^2=I); together with (U^5=I) this would force
(U=I), contrary to the nontrivial composition action.  ∎

If (V_Rf=f\circ R) and (Kf=\bar f), the antiunitary
(\Theta=V_RK) satisfies (\Theta U\Theta^{-1}=U^{-1}).  This is a
natural reversal, not a self-adjoint Hamiltonian.

## Evidence boundary

The finite (10\times10) rational grid and (n\le50) ledger are regression
sentinels only.  The proofs above carry the global claims.  There is no
prime correspondence, target divisor, target functional equation or
counting law, arithmetic local datum, Euler factor, root number, automorphy,
Hilbert--Pólya operator, or Route-B authorization.
