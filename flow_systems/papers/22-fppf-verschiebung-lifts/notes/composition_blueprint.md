# Paper 22 Stage-2 composition blueprint

Status: **approved under the user's Stage-2 continuation and delegated-choice authority**  
Target: **5,000 body words; seven numbered sections; no figure required**

## Working title

**A Descent Obstruction to Verschiebung Lifts on fppf and Finite-Flat Sites**

## Section architecture

| Section | Target | Purpose and proof payload |
|---|---:|---|
| 1. Introduction and main results | 800 | Bind the source question, state the fppf and finite-flat theorems, state the extension corollary and `N=1` control, subtract the nearest different-owner work, and describe the explicit obstruction. |
| 2. Rational Witt sheaves and the extension | 650 | Define the reduced monoid algebra, `W_rat`, `omega`, `V_N`, the sites, `K_0`, `K`, and `e`; separate sheaf epimorphy from objectwise surjectivity. |
| 3. Detection and injectivity lemmas | 800 | Prove torsion-freeness, exact sheafification, the big-Witt detector, and the Dedekind domain-refinement injectivity lemmas for both sites. |
| 4. The all-index descent obstruction | 1,250 | Construct the root cover and forced local preimage, pass to the double overlap, specialize to truncated dual numbers, detect a nonzero kernel section, and record the `N=2` case. |
| 5. Extension-theoretic formulation | 550 | Prove the pushout/pullback criterion and torsor statement; derive `u_*e != V_N^*e`, nonsplitting, and nonvanishing without claiming Cech computes all `Ext^1`. |
| 6. Finite-flat site and the Dedekind-section assertion | 650 | Re-run the site-dependent argument, exhibit the non-global section, and identify the exact Corollary-4.6 sheaf-epi/sections gap in restrained language. |
| 7. Scope, controls, and conclusion | 300 | Record controls, positive comparator, limitations, nonclaims, and the negative answer. |
| **Total** | **5,000** | |

## Evidence map

| Section | External evidence | Internal proof evidence |
|---|---|---|
| 1 | Deninger p. 25; Deninger--Mellit Thm. 1.1 | Phase-3 main theorem |
| 2 | Deninger Thm. 3.4 and Prop. 4.3; Stacks `03CN` | exact sheafification ledger |
| 3 | Deninger Ex. 4.4 and Prop. 4.5; Stacks `00HS`, `0AUW` | domain-refinement proof |
| 4 | Deninger Ex. 4.4 as `N=2` control | root-cover product identity and nonzero overlap specialization |
| 5 | Stacks `010I`, `06XP` | extension morphism criterion and nonlift theorem |
| 6 | Deninger Props. 4.3, 4.5 and Cor. 4.6; Stacks `03CN` | finite-free counterexample |
| 7 | Deninger Cor. 4.7 | claim boundary and route crosswalk |

## Claim ledger

Identifier reconciliation (2026-08-24, before Phase 6b): an earlier ledger
revision reused P22-C4 for the derived nonvanishing corollary while the
pre-draft claim-intent manifest reserved P22-C4 for the source correction.
The table below restores the manifest identifiers; no claim text, evidence,
or negative constraint was changed.

| ID | Claim | Status | Wording firewall |
|---|---|---|---|
| `P22-C1` | no fppf additive lift for every `N>1` | to be proved in manuscript | universe-small absolute site in Deninger's sense; additive only |
| `P22-C2` | no finite-flat additive lift for every `N>1` | to be proved separately | do not infer it merely from fppf |
| `P22-C3` | no `u` gives `u_*e=V_N^*e` | formal corollary | state the extension category and convention |
| `P22-C3a` | `e` and `V_N^*e` are nonzero | derived under `P22-C3` | failed descent detects nonzero; no full Cech-Ext claim |
| `P22-C4` | Corollary 4.6's sectionwise assertion requires correction | explicit example | use "as stated/read in v1"; preserve Props. 4.3 and 4.5 |
| `P22-CTRL1` | `N=1` has the identity lift | control, not a new claim-intent ID | no nontrivial law package follows |

## Route-map crosswalk

The governing files are `skills/route-a-evaluator.md` and
`skills/route-b-evaluator.md`, both version `0.2.0`.

```text
ROUTE_A_EVALUATION=NOT_TESTABLE
A0_A1_A2_A3_A4_TUPLE=NOT_ASSIGNED
ROUTE_A_ADVANCEMENT=NONE

ROUTE_B_INVOCATION_ALLOWED=false
ROUTE_B_ENTRY_AUTHORIZED=false
ROUTE_B_STATUS=ROUTE_B_NOT_TESTABLE
B1_B2_B3_B4_B5_TUPLE=NOT_ASSIGNED
HILBERT_POLYA_CLAIM_ALLOWED=false

GATE_A=NOT_REACHED
GATE_B=NOT_REACHED
GATE_C=NOT_REACHED
GATE_D=NOT_REACHED
GATE_E=NOT_REACHED
```

Paper 22 has no phase space, dynamics, arithmetic clock, primitive-orbit
ledger, determinant convention, Hilbert space, operator domain, trace
formula, or completed-zeta divisor.  Its sheaf-theoretic use of the word
"lift" is unrelated to Route-A layer A4.  The theorem is a reusable proved
algebraic obstruction but contributes no Route coordinate or Gate A--E
credit.  The exact roadmap files audited at Stage 2.5 have SHA-256 values
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
for Route A and
`170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`
for Route B.

`criteria_binding_unavailable`
