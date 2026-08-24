# Narrative report — C120

The quartic map `F(q,p)=(q^3-2q-p,q)` supplies a small but unusually complete
variational test object. Its determinant-one Jacobian, polynomial inverse,
coordinate-swap reversor, and type-1 generating function are all exact. This
makes it possible to connect a phase-space orbit certificate to an action
critical point without numerical shooting.

The central witness is the primitive cycle
`(0,-1) -> (1,0) -> (-1,1) -> (0,-1)`. Chronological multiplication is
important: `B(-1)B(1)B(0)` equals `[[-1,0],[-3,-1]]`. The determinant
polynomial `(1+z)^2` records a repeated multiplier at `-1`, but this is only
the tangent monodromy of one named cycle.

The coordinate word `(0,1,-1)` is stationary for the cyclic action generated
by `S(q,Q)=qQ-V(q)`. The action value is `1/2`; its Hessian has determinant
four and two negative eigenvalues. The nonzero determinant separates the
Morse statement from the parabolic tangent multiplier: the two calculations
use related variational data but certify different finite objects.

Three controls sharpen attribution. Changing `alpha=2` to `5/2`, deleting
the cubic term, or substituting the noncyclic word `(0,1,0)` breaks an exact
transition, with explicit residuals. The controls therefore prevent a
generic-map or arbitrary-word interpretation.

The exact calculations are proved structural evidence, but the evaluator-
native Route-A tuple is deliberately weak:
`(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`. There is no target prime
correspondence or completeness result, no source-owned dynamical
zeta/Fredholm object, and no target divisor or global analytic structure. The
action and reversibility provide only a formal liftability hint because no
quantum object, Hilbert space, or operator domain is defined. The package
remains `ROUTE_A_EXPLORATORY` under `NO_BAD_EULER_OR_ROOT_NUMBER`.
