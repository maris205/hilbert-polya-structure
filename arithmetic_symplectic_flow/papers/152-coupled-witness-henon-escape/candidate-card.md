# Classical card — ASFS-20260915-CHE01

Version 1, 2026-09-15. Frozen before theorem/computation.
Initial P0 / operational A0--A2 OPEN.

For every integer n>=2 let K_n=max(1,floor(log_2(n-1))) and k be its cyclic
phase. Define the complete witness count by the fixed rule

\[
a(n)=\sum_{2\le d<n}1_{\{d\mid n\}}.
\]

The full count is evaluated as part of each update. It is not a supplied
primality flag, but it is not the local-batch schedule of 145/147/149.
For X=(x,y) and a=a(n) set

\[
V_a(x,y)=\frac{1-a}{2}\big((x+y)^2+y^2\big)
             +a\big(e^{x+y}+e^y\big).
\]

Freeze

\[
M=\coprod_{n,k}\mathbb R^4_{n,k},\quad
\omega=dQ_1\wedge dP_1+dQ_2\wedge dP_2,
\]
\[
F(n,k,Q,P)=(n,k^+,P,2P-Q+\nabla V_{a(n)}(P)),\quad \tau=1.
\]

| P0 field | Frozen scope |
| --- | --- |
| Lineage | Prime/composite divisor-exclusion constraint -> full finite witness count -> exact coupled nonlinear Hénon potential |
| Architecture | Four-dimensional generalized Hénon map; no auxiliary passive hyperbolic factor or cotangent construction |
| All data | All integers, elementary division, fixed quadratic/exponential functions; no selected-prime coefficients or log roof |
| Gain/interpolation | Integer witness count enters the displayed affine potential interpolation; its constraint-engineering nature must be explicit |
| Geometry | Full disconnected noncompact R4 components, all real coordinates; inverse and global symplecticity to check |
| Flow / measure | Unit-roof mapping torus, canonical volume; no finite invariant probability or later Hamiltonian owner |
| Coding | Intrinsic phase and witness observations, not a full source conjugacy |
| Full packet tests | Composite cycle-sum sign in the coupled force; prime full linear recurrence, all periods; full monodromy and multiplicity |
| Clock | Binary macrophase K_n; n-2 direct tests at each step, not one full scan spread across K_n steps |
| Analytic proposal | Ordinary unweighted complete Z if justified; transfer operator, domain and trace OPEN |
| Controls | a=0 all n; replace a by n-2; use count of d dividing n+1 over the original interval; full continuous-state audit |
| Stop | Failed source, full periodic classification or geometry -> decisive stop, no potential tuning |
| Generality | Other finite nonnegative integer witness predicates might work; no privileged Riemann naturalness inferred |
| Route | Owner-level results only; formal coordinates UNASSIGNED and Route B NOT INVOKED |

This is a new object with a new arithmetic update schedule and potential.
No source, packet, monodromy or zeta theorem transfers from 145/147/149.

## Version-1 audit adjudication — 2026-09-15

**Candidate:** ASFS-20260915-CHE01  
**Status:** ADVANCE — PRIME-ONLY NONDEGENERATE HÉNON PACKETS; ROUNDED CLOCK AND OPERATOR OPEN.

The frozen object above is unchanged. The [full audit](paper.md) establishes
its global inverse and symplecticity, excludes all periodic real states on
composite components, and proves that every prime component has exactly one
primitive phase cycle at zero. The exclusion is intrinsic to the full
periodic equation, not a centre-selection convention.

Writing \(C=\left(\begin{smallmatrix}1&1\\1&2\end{smallmatrix}\right)\) and
\(J=\left(\begin{smallmatrix}0&I\\-I&2I+C\end{smallmatrix}\right)\),
the primitive monodromy is \(J^{K_p}\), with hyperbolic nondegenerate
repetitions \(J^{rK_p}\). The same unit-roof flow has ordinary unweighted
\(Z(s)=\prod_p(1-e^{-sK_p})^{-1}\), whose logarithmic-series absolute
convergence abscissa is exactly \(\log2\).

The source executes \(n-2\) complete direct tests at every macrostep. Its
constraint-interpolation generality and the chosen rounded logarithmic
clock are retained as limitations; no exact \(\log p\), privileged Riemann
naturalness, operator/domain/trace, or continuation is established.

Decision: **advance** the bounded full-ledger/nondegeneracy result.
Any change of clock, potential or analytic owner beyond a construction for
this unchanged object requires its own stated scope/card as applicable.
Formal Route coordinates UNASSIGNED; Route B NOT INVOKED.
