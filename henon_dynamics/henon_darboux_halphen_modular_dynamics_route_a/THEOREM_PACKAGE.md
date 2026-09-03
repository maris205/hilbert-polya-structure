# C320 theorem package

Let a prime denote `d/dtau` and freeze

`x1'=x2*x3-x1*(x2+x3)` cyclically.

For `Im(tau)>0`, put `Q=exp(pi*i*tau)` and

`(x1,x2,x3)=-2 d_tau(log theta2, log theta3, log theta4)`.

Then:

1. The theta triple solves the polynomial system.  Equivalently,
   `Xi=xi/(pi*i)` obeys `D Xi=Xj Xk-Xi(Xj+Xk)` for `D=Q d_Q`, with
   `X(0)=(-1/2,0,0)` and the three declared Jacobi series.
2. If `gamma=[[a,b],[c,d]]` has determinant one, then
   `x~_i(tau)=(c*tau+d)^(-2)x_i(gamma*tau)+c/(c*tau+d)` is again a
   solution wherever defined.  For theta seeds, `T` permutes `(2 3)` and
   `S` permutes `(1 3)` in the package's component numbering.
3. For `S=x1+x2+x3`,
   `S'''=-4*S*S''+6*(S')^2`.
4. For `Delta=(x1-x2)(x2-x3)(x3-x1)`,
   `Delta'=-2*S*Delta`; hence the pair-collision union is invariant.
5. On `x1=x2=a, x3=b`, for `c,C in C` and locally on `tau!=c`, every
   solution with `a` not identically zero is
   `a=1/(tau-c)`, `b=1/(tau-c)+C/(tau-c)^2`, including the diagonal
   at `C=0`.  The missing branch `a=0` is the equilibrium axis
   `(0,0,B)`, `B in C` arbitrary.  Indeed, one zero of `a` forces
   `a` to vanish identically by uniqueness.  The other strata follow cyclically, producing
   all three coordinate-axis equilibrium families; the axes meet at the
   origin.

The theta constants are holomorphic and nonzero on the upper half-plane.
The regular theta chart, cusp, modular poles, theta-zero poles possible only
after continuation outside that chart, collision union, reciprocal diagonal
layer, and coordinate-axis equilibria are all declared boundaries.
No exhaustive meromorphic classification is claimed.

The strict Route-A tuple is
`(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_PARTIAL_ANALYTIC_STRUCTURE,A4_FAIL)`;
overall `ROUTE_A_REJECTED`, with Route B locked.
