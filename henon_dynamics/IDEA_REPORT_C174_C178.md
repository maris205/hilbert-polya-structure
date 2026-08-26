# Route-A idea report: C174--C178

Date: 2026-08-26

Source commit: `100e5f601a0196710d53784bdeef40d2bff89fa8`.

Evaluator: `flow_systems/skills/route-a-evaluator.md`, v0.2.0, SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Design objective

The round deliberately increases theorem size and changes dynamical subtype in every paper. A candidate survives only if it supports an all-parameter classification or a sharp stopping theorem that is materially stronger than replacing symbols in a previous fixed-count formula. The five selected systems span non-Archimedean dynamics, a cellular automaton, an interacting stabilization system on graphs, a smooth expanding endomorphism, and a continuous Hamiltonian flow with a natural quantum lift.

“Bold hypothesis” is implemented as a falsifiable theorem program: each source receives its strongest plausible exact statement, while unsupported target or novelty claims remain forbidden.

## Pivots before freezing

- **Finite-field Frobenius:** killed before paper production. Existing finite-field and arithmetic-flow packages already own the nearby orbit mechanisms; another Frobenius ledger would not be a new subtype.
- **Logistic/tent conjugacy:** killed as structurally duplicative of existing full-shift and finite symbolic lines.
- **Gauss/Farey transfer dynamics:** not frozen in this round because modular and continued-fraction near-neighbors make ownership and collision boundaries less clean than the selected expanding-circle theorem.
- **Rotor-router unicycles:** retained as a valid future alternative, but not run beside sandpile because both would share the same spanning-tree backbone in one five-paper batch.
- **Elliptic multiplication/Lattès quotient:** retained as a future algebraic-dynamical alternative; its classical ownership requires a separate source audit and was unnecessary after five lower-collision subtypes survived.
- **Morse--Smale circle flow:** retained as a future dissipative-flow alternative if the oscillator package had failed its same-clock quantization theorem.

This is a local collision and theorem-ownership report, not a literature novelty certification.

## Frozen candidates and required increments

### C174 -- odd-affine 2-adic parity renewal

Freeze every odd integer pair \((a,b)\) on \(\mathbb Z_2\):
\[
T_{a,b}(x)=\begin{cases}x/2,&x\equiv0\pmod2,\\(ax+b)/2,&x\equiv1\pmod2.\end{cases}
\]
The classical parity conjugacy is background, not the claimed increment. The new package must distinguish three clocks: the original binary endomorphism, the accelerated first-return map on odd units, and the original-clock roof renewal. It must prove countably many accelerated fixed points and failure of the accelerated ordinary zeta, recover \((1-z)/(1-2z)\) from roof words, restore \((1-2z)^{-1}\) after the all-zero orbit, and prove the stability-weighted parameter blindness \((1-z)^{-1}\). The \((3,1)\) positive-integer Collatz boundary must remain explicit.

### C175 -- cyclic Rule 184 traffic dynamics

Freeze every particle sector \(X_{N,k}\) of the synchronous cyclic traffic rule. Prove finite attraction to the periodic core by a defect/gap Lyapunov argument; classify the low-density no-`11` and high-density no-`00` cores; identify right/left rotation; derive all-\(n\) fixed counts from cyclic hard-core words; and close exact periods and zeta by Möbius inversion. The full transient map must not be relabeled as the unitary rotation on its recurrent core.

### C176 -- Abelian sandpile recurrent translation

Freeze a finite connected undirected loopless multigraph with sink and an addition vector. Prove the bridge from recurrent stable configurations to the critical-group torsor, then resolve the translation order both from Smith normal form and from \(\operatorname{adj}(\Delta)b\). Every recurrent orbit must have the same exact length \(L\), giving the fixed ledger, zeta, finite Koopman determinant, character spectrum, inversion reversor, and the self-adjoint boundary \(L\le2\). The theorem is restricted to the recurrent set; transient stable configurations remain separate.

### C177 -- integer expanding circle endomorphism

Freeze \(T_b(x)=bx\pmod1\) for every integer \(b\ge2\). Beyond the fixed grid and rational zeta, prove the complete Haar--Koopman Wold decomposition, Perron backward filter, spectrum and operator-ideal boundary. The additional quantitative increment is the sharp mean-zero homogeneous-Sobolev correlation law with factor \(b^{-ns}\). Prime and composite degrees are mandatory negative controls.

### C178 -- harmonic-oscillator stroboscopic quantization

Freeze the planar oscillator strobe \(R_\theta\) for all angles. Separate irrational angles, with one fixed point for every positive iterate and zeta \((1-z)^{-1}\), from rational angles, where some iterates have a continuum of fixed points and ordinary zeta fails. Resolve the Gaussian Koopman operator in the Laguerre--angular basis, including infinite radial multiplicity and reversor. Then prove a natural same-clock quantum lift on Hermite space with exact Egorov, spectrum, conjugation reversal, and the noncompact/non-Schatten/determinant boundary. Heat/Wick evolution is a different clock and cannot be substituted.

## Frozen evaluation expectation

| paper | A0 | A1 | A2 | A3 | A4 | expected overall |
|---|---|---|---|---|---|---|
| C174 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C175 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C176 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_REJECTED` |
| C177 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C178 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_REJECTED` |

The coordinates remain candidate-local and cannot be merged. A4 never compensates for A0--A3. Route B remains unauthorized for all five.
