# Route-A dynamics-variant batch plan: C114--C118

Status: **five complete paper packages; uniform prefreeze audit passed**.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

This round follows the roadmap's A branch and deliberately changes the
dynamical subtype from paper to paper.  The common contract is conservative:
freeze one exact rational model, construct the smallest source-owned finite
object justified by that model, and state explicitly where A1/A2 stop.  A
local jet, low-period monodromy, symbolic prefix, or tangent-moment operator is
not promoted to a global transfer/Fredholm theorem, arithmetic data, or Route
B.

## Frozen sequence

1. **C114 -- local jet Koopman quotient.**  For
   \(F(u,v)=(u^2+3u/2-v/2,u)\), construct the pullback on
   \(\mathbb Q[u,v]/(u,v)^5\).  The exact 15-dimensional operator, its five
   graded blocks, determinant, characteristic data, and trace-power prefix
   give an operator-first local A2 certificate.
2. **C115 -- rational reversible McMillan/QRT map.**  Freeze
   \(M(x,y)=(-4x/(1+x^2)-y,x)\), verify the quartic first integral, inverse,
   reversor, fixed points, and the real primitive two-cycle
   \((1,-1)\leftrightarrow(-1,1)\).  Clearing-denominator roots at the forward
   poles \(x=\pm i\) are excluded rather than counted as cycles.
3. **C116 -- nonsmooth Lozi map.**  Freeze
   \(L(x,y)=(1-2|x|+y/2,x)\), exclude the border \(x=0\), and perform exact
   branch-domain pruning for every binary word through length eight.  The
   resulting 37 primitive necklaces own a finite 240-state cycle-atlas prefix.
4. **C117 -- Markov-switching H\'enon cocycle.**  Couple two rational H\'enon
   maps with transition matrix
   \(P=\left(\begin{smallmatrix}2/3&1/3\\1/4&3/4\end{smallmatrix}\right)\).
   Source-owned conditional first- and symmetric second-tangent-moment
   operators have dimensions 4 and 6; their exact determinant polynomials and
   a stationary-averaging control are certified.
5. **C118 -- conformally symplectic damped H\'enon dimer.**  Freeze a two-site
   variational map with damping \(\gamma=1/2\) and coupling \(\kappa=1/4\).
   Exact conformal symplecticity, inverse, fixed states, a synchronous
   primitive two-cycle, and longitudinal/transverse monodromy factors are
   checked over \(\mathbb Q\).

## Uniform artifact contract

Every package contains a source audit, research question, theorem/boundary
package, experiment and paper plans, narrative report, deterministic producer,
independent checker, exact symbolic cross-check, canonical replay, hostile
mutation audit, LaTeX source, three preserved round PDFs, compile report,
exact evidence receipt, and content-addressed manifest.  Release requires a
closed 26-file ledger, matching evidence/PDF hashes, two fixed-date isolated
builds, embedded fonts, and a clean final warning/layout/reference scan.

## Paper and artifact ledger

| paper | dynamical subtype | PDF pages | hostile mutations | evidence SHA-256 | manifest SHA-256 | PDF SHA-256 |
|---|---|---:|---:|---|---|---|
| C114 | local polynomial jet Koopman quotient | 2 | 13/13 | `5e957b0fb9825f8c736d0e6c4cda69132c6606cabf11d93819e5201dd937fbaa` | `81b7a2d89d03522809f9299121ff3b53c50ef8f136103abbbb6a013defba9db6` | `54db259d2f73c1eeaa967714aad50c5bafa96c2e635a1a2666689add70425def` |
| C115 | rational reversible McMillan/QRT | 2 | 12/12 | `1013fe8163eda456f453f9bd63560bcfb8e34a27f5b38eed33ec8b23380fa2e3` | `dd61b9b422705718f179fece9da85b7e3f330524b29bc6a0ea36273e9666101f` | `f5b9845be4f68f315f5ea312ea3bc090b07463a73dca0dd71fa5afea5f31037f` |
| C116 | nonsmooth Lozi sign itinerary | 2 | 12/12 | `e7347a90b6833846ee5ca6f007597ec2676d28d4c26110f3b63de43a63e3ab1f` | `dcf086b9610ebb109d78253b057ea2cd9e71d13de8fd7040e5301638ac09a839` | `a66073cf8185b528869e22be0527ed8bf80caba9b2568505eeddbab74796b6dd` |
| C117 | Markov-switching tangent moments | 2 | 12/12 | `e1a71257180704c36696dffc811766de49a04c58f554d520ab54e43eae544e00` | `9ca62aca1aeb93741e33817ce40295888706db1773d1ca54428f0731b4fdcd3a` | `415b3adca4549d3e9c8bbdbbcc72539171e11a69063af0614b1bcbf049ace83e` |
| C118 | conformally symplectic damped dimer | 2 | 12/12 | `54d83d5087c6f20103924d2580e26f8f2513092273ae7401530ec08eafe88a2f` | `1a8ed2e8d354ee8bb3aff4361717ca98bf906dc75b4d32f844b5f57a0b5cdc46` | `c36c3371fe5aa608dc1e55f50ab5573dc51bb9d21bf49809720013c41f28b74a` |

## Route-A boundary after C114--C118

| paper | A1 | A2 | A3 | A4 |
|---|---|---|---|---|
| C114 | `A1_PARTIAL_CERTIFIED` | `A2_CERTIFIED_PREFIX` | `A3_NOT_ADDRESSED` | `A4_FAIL` |
| C115 | `A1_PARTIAL_CERTIFIED` | `A2_FAIL` | `A3_NOT_ADDRESSED` | `A4_FAIL` |
| C116 | `A1_PARTIAL_CERTIFIED` | `A2_CERTIFIED_PREFIX` | `A3_NOT_ADDRESSED` | `A4_FAIL` |
| C117 | `A1_WEAK` | `A2_CERTIFIED_PREFIX` | `A3_NOT_ADDRESSED` | `A4_FAIL` |
| C118 | `A1_WEAK` | `A2_FAIL` | `A3_NOT_ADDRESSED` | `A4_FAIL` |

The global evaluator tuple remains

```text
(A0_NOT_ADDRESSED, A1_WEAK, A2_CERTIFIED_PREFIX,
 A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)
```

with overall status `ROUTE_A_EXPLORATORY`.  C114 and C116 strengthen finite
operator/cycle prefixes, but none of the five establishes a complete
primitive-orbit atlas, a source-native compact or nuclear global owner,
arithmetic prime data, a root-number law, or a Hilbert--P\'olya operator.
Route B remains unauthorized.

## Reproduction

Run the package-specific commands in each linked README and regenerate its
manifest.  The five compiled papers are:

- [C114 paper](henon_local_jet_koopman_route_a/paper/main.pdf)
- [C115 paper](henon_mcmillan_rational_route_a/paper/main.pdf)
- [C116 paper](henon_lozi_nonsmooth_route_a/paper/main.pdf)
- [C117 paper](henon_markov_switching_moment_route_a/paper/main.pdf)
- [C118 paper](henon_conformally_symplectic_dimer_route_a/paper/main.pdf)
