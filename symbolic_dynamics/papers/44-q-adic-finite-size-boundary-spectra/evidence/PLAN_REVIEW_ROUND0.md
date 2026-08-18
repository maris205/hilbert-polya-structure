Overall, the plan is mathematically serious and unusually careful on ownership, but it is not yet ready. The core theorem arc is good; the main problems are evidence hierarchy, source disambiguation, and page pressure.

| Criterion | Score | Review |
|---|---:|---|
| Logical flow | 8/10 | The theorem-to-specialization-to-analytic-corollary arc works, but Section 2 interrupts the mathematical ramp before the reader has notation. |
| Claim-evidence alignment | 7/10 | C1 and C2 align well; C3 and C5 need sharper wording and more explicit bridge statements. |
| Missing mathematical or computational evidence | 6/10 | The issue is not missing experiments; it is missing reader-facing bridge lemmas/dictionaries for C3 and C5. |
| Source positioning and Ban--Hu--Lai caveat | 7/10 | The firewall is strong in intent, but the exact author-manuscript versus version-of-record separation still needs to be impossible to misread. |
| 11--14 main-body page feasibility | 6/10 | Feasible only if Section 6 is compressed hard and Section 2.3 is made very economical. |
| Title/abstract/introduction/Figure 1 strength for skim readers | 6/10 | The mathematics is strong; the current skim-facing packaging is too opaque and lets audit material compete with the theorem. |

No CRITICAL theorem-gap is visible from the plan itself, but the following weaknesses are blocking.

1. `MAJOR`  
Location: Abstract, bullet “Give the strongest exact quantitative value … and the retrospective finite replay count `548+32=580`”.  
Minimum concrete fix: Remove the replay count from the abstract. If you keep it at all, put it in the final sentence with the exact wording “implementation audit only; not evidence for C1--C3.”

2. `MAJOR`  
Location: Section 1, “Give four falsifiable contribution bullets corresponding to C1--C4”.  
Minimum concrete fix: Split these into “Theorems” for C1--C3 and “Verification audit” for C4. State in the C4 bullet that finite replay does not bear on the infinite claims.

3. `MAJOR`  
Location: Claims--evidence matrix, C3; Section 5 opening bullet.  
Minimum concrete fix: Replace “pole-type coefficients” with “nonzero radial leading coefficients” unless you prove a precise asymptotic with that terminology. Keep “natural boundary” as the only global analytic conclusion.

4. `MAJOR`  
Location: Section 2.3; Claim C5; citation-plan entry `ban2023boundary`.  
Minimum concrete fix: Identify the exact Ban--Hu--Lai author manuscript by full handle/version/date, then add this caveat verbatim or equivalent: “We checked only the author-manuscript version [identifier/version/date]. We did not line-check the version of record or any erratum, and make no claim about their displayed formulas.”

5. `MAJOR`  
Location: Section 2.3, “Reproduce the Ban--Hu--Lai author-manuscript … and reconcile it with the exact bounded remainder.”  
Minimum concrete fix: Add a compact notation dictionary mapping the manuscript symbols, normalization, and specialization to the present `A=J_d`, `Z(N)`, and `E(N)`. Without that, the “same-object correction” is asserted rather than shown.

6. `MAJOR`  
Location: Section architecture/page budget, especially Sections 2, 5, and 6.  
Minimum concrete fix: Move most mutation-family counts, chronology, and hash detail to Appendix B. Keep only one compact replay table and one short paragraph in the main text.

7. `MINOR`  
Location: Working title.  
Minimum concrete fix: Make the scope asymmetry visible in the title, with the general theorem first and the golden/binary specialization second.

8. `MINOR`  
Location: Section 2 before Section 3 definitions.  
Minimum concrete fix: Either add a short notation preview at the end of the introduction or move the technical part of the Ban--Hu--Lai reconciliation after Section 3.

9. `MINOR`  
Location: Section 3, first use of `\mathbb Z_q`; last bullet “`q` need not be prime.”  
Minimum concrete fix: Define `\mathbb Z_q := \varprojlim \mathbb Z/q^n\mathbb Z` explicitly at first use so composite `q` does not look like a prime-adic convention.

10. `MINOR`  
Location: Figure 1 plan and its introduction placement.  
Minimum concrete fix: Make the caption say in plain language that one cutoff step changes exactly one valuation level, and those levelwise changes assemble into the continuous boundary map.

11. `MINOR`  
Location: Claims--evidence matrix, C3 evidence line.  
Minimum concrete fix: Name the continuation-contradiction step explicitly. “Rational residue generating functions + dominated Abelian passage” is not yet enough, by itself, to signal why continuation across any arc is impossible.

Special checks: finite replay is mostly kept out of theorem proof, but the abstract and introduction still place it too close to C1--C3. Prior ownership is handled correctly at the plan level and does receive zero credit. Nonclaims, Route status, and retrospective boundaries are explicit enough once the abstract/introduction leak is fixed.

`PLAN_NOT_READY`