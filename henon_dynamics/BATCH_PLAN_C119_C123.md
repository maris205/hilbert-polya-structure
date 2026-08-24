# Route-A dynamics-variant batch plan: C119--C123

Status: **five complete paper packages; uniform release audit passed**.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

This round continues the roadmap's A branch and deliberately changes the
dynamical subtype from paper to paper.  The common contract is to freeze one
exact source model, construct only the orbit/operator object owned by that
model, and keep local, low-period, finite-prefix, and target-facing boundaries
explicit.  In particular, a tangent monodromy is not called a transfer
operator, algebraic degree growth is not called entropy, and an analytic
Fredholm determinant for a source-defined Fock owner is not claimed to match a
target divisor.

## Frozen sequence

1. **C119 -- trace-class bosonic-Fock contraction.**  Freeze the linear
   Hénon-type contraction
   \(\Phi(x,y)=(3x/4-y/4,x/2)\).  On the standard symmetric bosonic Fock
   space, the source-defined second-quantized owner \(\Gamma(A)\) is trace
   class and has an exact all-order trace law and Fredholm product.  The same
   contraction has only the origin as a periodic point, so this operator-first
   success intentionally records `A1_FAIL`; because the determinant is not
   primitive-orbit-owned and no target divisor is compared, strict A2 also
   fails.
2. **C120 -- quartic variational period three.**  Freeze the reversible,
   area-preserving map \(F(q,p)=(q^3-2q-p,q)\), certify one primitive
   three-cycle, and derive its exact discrete action, action Hessian, Morse
   index, tangent monodromy, and three rejecting controls.
3. **C121 -- projective algebraic stability.**  Extend
   \(H(x,y)=(x^2-4-y,x)\) to \(\mathbb P^2\), separate the forward and inverse
   indeterminacy points, and prove the all-order degree law
   \(\deg H^n=2^n\).  Fixed and primitive period-two witnesses are included,
   while the algebraic dynamical degree is not promoted to an entropy theorem.
4. **C122 -- adaptive-feedback Hénon automorphism.**  Promote the Hénon
   parameter to a third state coordinate in
   \(G(x,y,a)=(x^2+a-y,x,a/2+3x-1/2)\).  Certify the exact polynomial inverse,
   constant Jacobian determinant, two fixed points, a primitive two-cycle,
   its three-dimensional monodromy, and controls that isolate the feedback
   gain and offset.
5. **C123 -- additive-noise Hénon moments.**  Freeze an iid two-branch affine
   contraction, enumerate every rooted noise word through length six and its
   primitive necklaces, and construct the exact degree-four polynomial Markov
   operator together with stationary covariance and fourth-cumulant data.

## Uniform artifact contract

Every package contains a source audit, research question, theorem/boundary
package, experiment and paper plans, narrative report, deterministic producer,
independent checker, exact symbolic cross-check, canonical replay, hostile
mutation audit, LaTeX source, three preserved round PDFs, compile report,
canonical evidence receipt, and content-addressed manifest.  Release requires
a closed 26-file ledger, matching evidence/PDF hashes, two fixed-date isolated
builds, embedded fonts, a clean final warning/layout/reference scan, and a
rendered-page inspection.

## Paper and artifact ledger

| paper | dynamical subtype | PDF pages | hostile mutations | evidence SHA-256 | manifest SHA-256 | PDF SHA-256 |
|---|---|---:|---:|---|---|---|
| C119 | linear contraction with global bosonic-Fock owner | 2 | 12/12 | `26d0e4a5c01ed64555bbf984323c6965366fc3919bb9b71983af964bc1138100` | `e8be7af8517f746a61e338e408356ff0c534769cdc1ee44b192f73c7cd2548c4` | `77aa108f6ccad9b3dd9db6d69c89116dfac788cb50c3d6d251d3926c7cce40c2` |
| C120 | quartic reversible variational period three | 2 | 21/21 | `657e0be369890496a525122dddabe7d7ae9dd12f0b38f1c912917cd55d9c0ae0` | `b24c2f29c7063f3349b4b20459ee85fbc20f662d8e5da9f8b2376947b7d0ecc1` | `6ecb9ba1d6f2d5129949e16d029b0162e7495be5f041b581ddd2aa0f8817fdc4` |
| C121 | projective algebraically stable polynomial automorphism | 2 | 16/16 | `a3e24e9edb514bb3655367997990c8941cbebba0e2e116c6f683f6e7ef2f431b` | `f034b47c278d0e20d2bf7f7d52c1f29e435718e2a1996fe9dce9d46dca3ff469` | `fa46eca15628ef467fb7731123f400bb62c6f88c0fc2fcd58119040bc4b8fc7a` |
| C122 | three-dimensional adaptive-feedback automorphism | 2 | 16/16 | `ac79342ae63b56b3761f97d7d047f5dc68a63a5eefcf06ecb0ecab9a137b7f15` | `98b352579690f0545c7d5b3e17b2dd0633aa41236c8fe75b291dfb9a830cbe55` | `eb23aed0cd77147f1d24dae91e7023d2c85345580b3fb58f9a75200ca32d754b` |
| C123 | iid additive-noise affine Hénon moments | 2 | 19/19 | `07456f446a13e57ff5225c85974dc630d01a11ac0abc2eda09d473d5c6ba7434` | `2f176bf60235664e0f332b7974ac618b78c504c7e195eb8c92fe469382887d42` | `2ec52ecdc8829e5b131ec44e7c7f286fcb54df2e9fb45e5d1f1546c365225700` |

## Route-A boundary after C119--C123

| paper | A1 | A2 | A3 | A4 |
|---|---|---|---|---|
| C119 | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` |
| C120 | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` |
| C121 | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` |
| C122 | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` |
| C123 | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` |

C119 closes the requested source-space/action/trace-law subgate: its Fock
space, operator, trace class, trace powers, and Fredholm product are all
source-defined and exact.  This structural theorem is deliberately separated
from the canonical Route-A verdict: the owner is not built from primitive
orbits and no target-divisor comparison, missing/extra-zero count, or sealed
validation region exists, so `A2_FAIL` is mandatory.  Canonical labels are
used without package-local substitutes.

The strongest single-candidate tuple in this round is C120:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
```

Its exact three-cycle is natural but far short of a target orbit
correspondence, while the variational structure supplies only a formal lift
hint.  The other candidates must not be combined coordinatewise to manufacture
a stronger tuple.  Overall status is `ROUTE_A_EXPLORATORY`.  No package
establishes the joint bridge from a nontrivial primitive-orbit structure to a
source-native global analytic owner and then to a target-facing divisor
theorem.  Route B remains unauthorized.

## Reproduction

Run the package-specific commands in each linked README and regenerate its
content manifest.  The five compiled papers are:

- [C119 paper](henon_fock_nuclear_contraction_route_a/paper/main.pdf)
- [C120 paper](henon_quartic_variational_period3_route_a/paper/main.pdf)
- [C121 paper](henon_projective_algebraic_stability_route_a/paper/main.pdf)
- [C122 paper](henon_adaptive_feedback_route_a/paper/main.pdf)
- [C123 paper](henon_additive_noise_moment_route_a/paper/main.pdf)
