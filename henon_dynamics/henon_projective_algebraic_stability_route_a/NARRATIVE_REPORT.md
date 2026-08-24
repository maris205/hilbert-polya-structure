# Narrative report — C121

## Motivation

Route-A orbit packages can certify individual cycles while leaving global
geometric structure unresolved.  C121 changes subtype: it studies the
birational projective geometry of a polynomial Hénon automorphism and obtains
an all-order algebraic invariant before returning to a small exact orbit
layer.

## Exact result

For \(H(x,y)=(x^2-4-y,x)\), the inverse is polynomial.  On the projective
plane, the forward indeterminacy point is \(I_+=[0:1:0]\), the inverse
indeterminacy point is \(I_-=[1:0:0]\), and the exceptional line at infinity
maps to the forward-fixed point \(I_-\).  A direct recurrence writes
\(H^n=(p_n,p_{n-1})\) with
\(p_n=p_{n-1}^2-4-p_{n-2}\).  Its unique leading term is
\(x^{2^n}\), so homogenization has no common factor and
\(\deg H^n=2^n\) at every order.  The algebraic dynamical degree is therefore
two.

The low-period layer finds the fixed coordinates \(q=1\pm\sqrt5\) and the
primitive cycle \((0,-2)\leftrightarrow(-2,0)\).  The tangent monodromy is
\(\begin{psmallmatrix}-1&4\\0&-1\end{psmallmatrix}\), with trace \(-2\),
determinant one, and determinant polynomial \((1+z)^2\).  In the family
\(H_c\), both proposed transitions have residual \(c+4\); hence \(c=-3\)
and \(c=-5\) are exact negative controls for this particular witness.

## Validation

The recurrence is stored as an exact expression DAG with sparse leading data
and exact integer probes through \(n=8\), where the projective degree is 256.
An independently written checker reconstructs the entire ledger.  A separate
SymPy program performs 97 exact checks, canonical replay fixes the bytes,
and sixteen hostile changes are all rejected.

## Interpretation and limit

The all-order degree theorem is stronger than a finite orbit sample, but it
does not classify periodic orbits.  The two fixed points and one primitive
cycle supply exact structural evidence, not a complete atlas or prime-like
target correspondence.  Algebraic dynamical degree is not asserted to equal
any entropy here.  Neither degree growth nor a tangent monodromy supplies a
weighted dynamical zeta, target divisor, transfer owner, functional equation,
counting law, continuation theorem, or analytic bridge.  The repository-native
verdict is therefore
`(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`, overall
`ROUTE_A_EXPLORATORY`, under `NO_BAD_EULER_OR_ROOT_NUMBER`.
