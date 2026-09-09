# C425 stable first-draft handoff

2026-09-09 UTC. **AUTHOR STOP-WRITE: ready for the two assigned
nonauthor manuscript review passes.** No manuscript review is counted
by this author receipt. The mathematical admission and approved outline
precede this draft; their frozen source files were not changed.

## Main deliverables

- [Complete article](main.pdf), 12 pages; [LaTeX entry](main.tex).
- [Genuine pre-review baseline](baseline.pdf) and `baseline_source/`.
- [Actual build/failure receipt](BUILD_REPORT.md).
- [Source access, ownership and citation audit](SOURCE_AUDIT.md).

PDF SHA-256:
`aa6c4ee4bbc6f55bcf2934caccc927bf36aef872bf230466541c0f3de7b2f207`.
The current PDF, baseline PDF and final first-draft build output are
byte-identical. All active source copies in `baseline_source/` preserve
this version; failed/intermediate build inputs and logs are retained.

## Full active input list and hashes

The 12 manuscript inputs are `main.tex`, `math_commands.tex`,
`references.bib` and the nine section files below. `build.sh` is the
13th reproducibility input. All TeX package/font dependencies are listed
by the actual recorder in `build_initial_04/main.fls`.

| File | SHA-256 |
| --- | --- |
| `main.tex` | `1d9df3c901777f5993ea4ac586be1b4aa29c4a8c3aa729bfef8d7caffbe4cc8a` |
| `math_commands.tex` | `40878d702da4e1cf18b3effb0a87ebd840790258fd64f9337304f481b926ce97` |
| `references.bib` | `9b35b94a205812d6b9e7ab43e2b6d162206fa94c34e07b7a84bce5b0bc69b7c0` |
| `sections/00_abstract.tex` | `89f057e8a1bdae42d21e6c1696112dc9a64bab18272d9117aec0878797a982e0` |
| `sections/01_introduction.tex` | `53a15a438a71f3ca6666be7ac4f90f425722df1b65cbdb048021bfe949c3313d` |
| `sections/02_phase_lift.tex` | `1ddc3f867112dbdb2aa8eb33bfb9724731f55c331e8b1a1b309ea91bc457bff8` |
| `sections/03_state_graph.tex` | `514d6b7d89c8ec63a588e6e5b2264f92320c66d8501e47972552fb5f5a798a65` |
| `sections/04_height_forcing.tex` | `21844ed7ccb5bd1956410386e9468ce19443e2db20e18304c0a88b2323a3cec5` |
| `sections/05_line_exhaustion.tex` | `8f9890ce3a66df0327be78c7e6987414f18337415e7fcf9e158718c52fb2b56b` |
| `sections/06_effective_classification.tex` | `2432ae11bd4f35d11be1c3785776354f6dfdcb397c677edb0e8848a183a74c02` |
| `sections/07_level_counts.tex` | `1c93670e56816f391123852f7b2b35642ec2cad96cb10447395d9c9006d2c38f` |
| `sections/08_scope.tex` | `795fd2f41be2d98f308292de8bf219e278d9dff6ff265eec144bfcffe392e194` |
| `build.sh` | `81a579a73fe5067a1924aaf6dc991dffc03bb7ec09bccfb1a7f087c45d8018ff` |

## Claim-to-proof map for manuscript review

| Approved scope | Included manuscript location |
| --- | --- |
| Every ordered integer coefficient triple, all integer points/levels, ordinary singular points retained | Theorem 1.1; §§1, 7 |
| Exact native word `T=s_z s_y s_x`, rightmost first; no changed clock | Equations (1.2)–(1.3), (2.1)–(2.4) |
| Scalar maximum equals maximum native-orbit coordinate height | Equation (2.6) and preceding construction |
| True global-maximum entry into 27 phase-labelled states | Lemma 2.1 and equation (2.7) |
| Complete Type I/II conditions and intermediate whole-line identities | Table 2 and Lemma 3.1 |
| All omitted-edge cases forced away above `100(H+1)`; 27 transitions | Lemma 4.1, including inequalities (4.2)–(4.4); Proposition 4.2 |
| Affine-return test, phase divisibility and whole periodic lines | Table 3 and Lemma 5.1 |
| Bijective inverse-image argument removes every graph tail | Equation (5.3), Lemma 5.2 and Proposition 5.3 |
| At most 27 phase-zero lines; native certified returns at most 54 | Proposition 5.3, separately from least-period claims |
| Exhaustive finite core with no empirical cutoff and correct exit semantics | Lemma 6.1 and exhaustive-union proof in §6.1 |
| Primitive integer parametrization, coincidences and all intersections | §6.2 |
| Generic least period and every exceptional parameter, via polynomial gcd/integer roots | Proposition 6.2 and disjointness convention |
| Complete terminating parameterwise output, not an executed census | Procedure 6.3 and its termination explanation |
| Monic quadratic level restriction; at most two points per line and `54+N_R` point bound | Equations (7.1)–(7.3), Corollary 7.1 |
| Ordinary native cycle counts and finite fibre zeta only | Equations (7.4)–(7.5) and following limitation |
| Explicit Shin independent-coefficient/height/low-coordinate subtraction, Cantat fixed-fibre input and C421 equal-forcing ownership | §1.1, Table 1 and six-entry bibliography |
| No sharpness, practical complexity, worldwide priority or target-arithmetic claim | Theorem 1.1 closing sentence, §§1.1, 6, 8 |

The new proof is wholly typeset in the article. No accepted mathematical
input was strengthened, no old proof/certificate was edited or rerun,
and no new theorem exploration was performed. This author reports zero
mathematical-program executions. The exact first-draft build history is
one failure and three successes on changed inputs, not four manuscript
review rounds or a final deterministic double-build test.

## Reviewer and coordinator boundary

The first draft is stable and the author has stopped writing pending
explicit review instructions. Reviewers should read the actual complete
article, proof package and source scopes, not only this map. The two
manuscript passes and final release gates are not yet claimed complete.
The coordinator owns shared files, evaluation, manifest/release work,
integration and Git. No file outside `papers/C425_fricke_return/` was
created or modified by this manuscript assignment.
