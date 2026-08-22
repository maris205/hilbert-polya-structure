# Theorem package (finite exact version)

**Proposition 1 (exact symplectic map).** For the frozen potential `U`,
`F(q,p)=(grad U(q)-p,q)` has Jacobian
\[
J(q)=\begin{pmatrix}H(q)&-I_3\\I_3&0\end{pmatrix},
\quad H(q)=\operatorname{diag}(7-2q_i)-(1/5)L.
\]
Thus `J^T Omega J=Omega` and `det J=1` over `Q`. The involution
`R(q,p)=(p,q)` satisfies `R F R=F^{-1}`. With `lambda=q dot dp`,
`F^*lambda-lambda=d(U(q)-p dot q)`.

**Proposition 2 (certified witnesses).** The synchronous states
`(0,0,0;0,0,0)` and `(5,5,5;5,5,5)` are fixed. The two states
`(3,3,3;6,6,6)` and `(6,6,6;3,3,3)` form a primitive period-two orbit.

**Proposition 3 (mode factorisation).** The Laplacian eigenvalues are
`0,3,3`. Along the period-two orbit the scalar mode Hessians are `(1,-5)`
in the longitudinal mode and `(2/5,-28/5)` in each transverse mode. The
corresponding two-step traces are `-7,-106/25,-106/25`, and therefore
\[
\det(I-zM)=(1+7z+z^2)(1+\tfrac{106}{25}z+z^2)^2.
\]
Expanded coefficients are recorded in the evidence ledger.

These propositions are finite exact statements. They do not imply a global
primitive-orbit atlas, a Fredholm determinant, or analytic continuation.
