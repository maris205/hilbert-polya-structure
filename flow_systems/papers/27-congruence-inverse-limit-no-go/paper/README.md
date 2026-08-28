# P27 paper status

**ARS Stage 2 draft complete; Stage 2.5 is awaiting explicit user confirmation.** Stage 2.5 has not been passed.

## Manuscript deliverables

- [manuscript source](manuscript.tex)
- [bibliography](references.bib)
- [compiled paper](paper.pdf) — 12 pages
- [Stage 2 manuscript audit](stage2_manuscript_audit.md)
- reproducible LaTeX/BibTeX intermediates in `build/`

Title: **Renormalization Obstructions in Congruence and Homology Towers of Geodesic Flows**.

The paper gives a complete comparative account of the frozen Round 2–8 program. For a descending normal residual tower with one physical clock it proves inverse-limit aperiodicity, divisibility and divergence of fixed-owner quotient orders, and coefficientwise escape of every fixed finite owner panel. It specializes the theorem to `Gamma(3n!)`, includes a closed genus-two residual/homology control, and keeps finite whole-loop diagnostics distinct from primitive-period claims.

The separately registered pure homology-cover calibrator proves that a primitive content-one owner has cover degree `N^4`, deck order `N`, `N^3` primitive lift components, and physical period `N ell(g)`. The four-quadrant theorem shows that clock rescaling or multiplicity normalization alone fails; their simultaneous use recovers the base finite-panel factor exactly. This is a generic fixed-panel calibration, not a global arithmetic determinant.

The original residual candidate retains

```text
(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)
```

and the calibrator retains

```text
(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FAIL)
```

Both remain `ROUTE_A_REJECTED`; Route B remains unauthorized.

Verification completed on 2026-08-28:

- all historical unit tests: **58/58 PASS**;
- Round-8 verify-only reproducer: **12/12 PASS**, 96 quadrant rows, 1,248 coefficient rows, core SHA-256 `a1b588724dacb2ab2986326a7a5e1c6aec654c61538c1465e26564357b568b33`;
- LuaLaTeX + BibTeX build: **PASS**, no undefined citations/references and no box overflow;
- citation ledger: **5/5 cited entries**, no missing keys and no orphans;
- no `__pycache__/` or `.pyc` residue.

Research-history anchors remain available in the [Stage-1 spine](stage1_research_spine.md), [Round-6 contribution lock](round6_contribution_lock.md), [Round-7 spine](round7_research_spine.md), and [Round-8 spine](round8_research_spine.md).
