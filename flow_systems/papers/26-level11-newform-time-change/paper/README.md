# P26 paper status

**ARS Stage 2 draft complete; Stage 2.5 is awaiting explicit user confirmation.** Stage 2.5 has not been passed.

## Manuscript deliverables

- [manuscript source](manuscript.tex)
- [bibliography](references.bib)
- [compiled paper](paper.pdf) — 12 pages
- [Stage 2 manuscript audit](stage2_manuscript_audit.md)
- reproducible LaTeX/BibTeX intermediates in `build/`

Title: **Exact Newform-Period Taxonomy for a Level-11 Time Change of the Modular Geodesic Flow**.

The paper gives a relatively complete theorem/obstruction account of the frozen Round 2–8 program. It proves the level-11 time-change period laws, identifies Hecke output as a sum of explicitly owned branch-cycle geodesics, derives the all-parameter quadratic degree-moment criterion, and closes the frozen finite taxonomy by exact rational Schreier homology. Of 138 output instances, 2 are full complex-period kernels, 2 are real-projection-only kernels, and 134 are true nonkernels. The predeclared laws `a_p` and `a_p^2` each fail exactly 51/55 groups; the control `a_p^2-p` fails 55/55.

The manuscript retains the strict claim boundary. It does not assert a complete primitive `Gamma_0(11)` conjugacy census, a global dynamical determinant, a prime–orbit map, a zero fit, a functional equation, or a Hilbert–Pólya operator. Its formal Route-A tuple remains

```text
(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
```

with overall status `ROUTE_A_EXPLORATORY`; Route B remains unauthorized.

Verification completed on 2026-08-28:

- all historical unit tests: **74/74 PASS**;
- Round-8 verify-only reproducer: **18/18 PASS**, tree SHA-256 `cc36c1f952c9ce89050996f4bb4c9905571f9ef09a0d7115be8a985e02a5621d`;
- LuaLaTeX + BibTeX build: **PASS**, no undefined citations/references and no box overflow;
- citation ledger: **5/5 cited entries**, no missing keys and no orphans;
- no `__pycache__/` or `.pyc` residue.

Research-history anchors remain available in the [Round-8 spine](round8_research_spine.md), [Round-7 spine](round7_research_spine.md), [Round-6 spine](round6_research_spine.md), [Round-5 spine](round5_research_spine.md), and [Round-4 spine](round4_research_spine.md).
