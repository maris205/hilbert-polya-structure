# GPT54_XHIGH_ROUND1_HOSTILE_REVIEW

## Provenance

- Model: `gpt-5.4`
- Reasoning effort: `xhigh`
- Role: mandatory independent hostile mathematical reviewer
- Scope: Stage-2 paper P69 only, Round 1 only
- Review date: 2026-08-25 UTC
- Artifacts inspected: `main.tex`; `math_commands.tex`; all substantive section files `sections/0_abstract.tex` through `sections/8_conclusion.tex`; `PROOF_PACKAGE.md`; `CLAIMS_EVIDENCE.md`; `CITATION_AUDIT.md`; `references.bib`; `main.bbl`; `RUDIN_SHAPIRO_OWNER_MEMO.md`; `BUILD.md`; `FINAL_QA.md`; `main.log`; `code/verify_surface_flat_sft.py`; `code/verify_surface_flat_sft.out`; `qa/final_text.txt`; extracted text from `main.pdf`; `pdfinfo`/`pdffonts` on `main.pdf`
- Independent rerun performed: `python3 papers/69-orientation-sensitive-surface-flat-sft/code/verify_surface_flat_sft.py`

## Overall verdict

`Conditional PASS on the core mathematics after reconstruction; NOT release-ready.`

I independently re-derived the rooted gauge factor, the cover-topology exponents, the orientable and nonorientable fixed-point laws, the finite-moment inversion scheme, and the `D_8/Q_8` separation formulas. I did not find a critical algebraic collapse. I did find one central proof-writeup defect, one material regression-coverage gap, and a few terminology/ownership-presentation issues. External release remains an explicit `HOLD`.

## Theorem-by-theorem audit

- `sections/2_background.tex`, Proposition 2.1: accepted as a cited classical input, not as new work. The normalization used here is consistent with the stated Klug reference and with the displayed exponents.
- `sections/3_flat_shift.tex`, Proposition 3.2: PASS. The local rule reads six coordinates in a fixed finite support, so the SFT claim is closed.
- `sections/3_flat_shift.tex`, Proposition 3.3: PASS. The count reconstructs as
  `|Fix_H(X_K)| = |K|^(V-1) * |Hom(H,K)|`
  with `V=[Lambda:H]`, by unique rooted gauge fixing to tree-trivial connections and identification of tree-trivial flat holonomy with `Hom(H,K)`.
- `sections/4_subgroup_counts.tex`, Lemma 4.1: PASS on substance. I re-derived:
  `[\Lambda:H_n]=n`, `H_n` nonorientable because `x_3 in H_n` but `omega(x_3)=1`, genus `n+2` from `chi=-n`;
  `[\Lambda:L_m]=2m`, `L_m <= ker omega`, orientable genus `m+1` from `chi=-2m`.
- `sections/4_subgroup_counts.tex`, Theorem 4.2: PASS. I re-derived
  orientable exponent `4m = (2m-1)+(2m+1)` and nonorientable exponent `2n = (n-1)+(n+1)`, with the nonorientable power `nu^(n+2)` and degree exponent `d^(-n)`.
- `sections/5_moment_recovery.tex`, Lemma 5.1: PASS as stated for sequences indexed by `m>=1`.
- `sections/5_moment_recovery.tex`, Theorem 5.2: PASS in substance, but Step 4 needs correction. The current text overstates what the Vandermonde step directly recovers and invokes `R_0` even though the lemma is formulated for `m>=1`.
- `sections/5_moment_recovery.tex`, Corollary 5.3: PASS once Theorem 5.2 Step 4 wording is repaired.
- `sections/6_dihedral_quaternion.tex`: PASS. I re-derived `nu_{chi_D}=+1` and `nu_{chi_Q}=-1` directly from square counts, and the displayed `O`, `N` formulas match both the mathematics and the rerun control output.

## CRITICAL issues

- None found in Round 1 after independent proof reconstruction.
- This is not external-release clearance.

## MAJOR issues

1. The central inverse proof is not written with the precision its own lemma requires.

- Source: `sections/5_moment_recovery.tex:102-111`
- Problem: Step 4 defines
  `R_m = sum_d ((c_d^+ - c_d^-)/d) (d^-2)^m`.
  The Vandermonde system therefore recovers the coefficients `(c_d^+ - c_d^-)/d`, not `delta_d` directly. In the same paragraph, the manuscript invokes `R_0,R_1,...` even though Lemma 5.1 is formulated for sequences indexed by `m>=1`.
- Why this matters: this is the heart of the recovery theorem. A hostile reader should not have to silently repair the indexing and the coefficient normalization in the main inverse step.
- Required Round-1 fix: either restate Lemma 5.1 so that the known-base part explicitly allows moments starting at `m=0`, or invoke `R_1,...,R_r` instead. In either case, explicitly say that the recovered coefficients are `(c_d^+ - c_d^-)/d` and only then multiply by the known degree `d` to obtain `delta_d`.

2. The regression harness never tests the `nu=0` branch, so one of the paper's central trichotomy claims is unexercised by the finite controls.

- Source: `sections/7_scope_controls.tex:45-65`, `code/verify_surface_flat_sft.py:148-190`
- Problem: the controls use `D_8`, `Q_8`, and an orientable `S_3` check. These cover indicator patterns `+1` and `-1` only. No tested group contributes a non-self-dual irreducible with Frobenius--Schur indicator `0`.
- Why this matters: Theorem 5.2 claims recovery of `c_d^+`, `c_d^-`, and `c_d^0`. The control layer never exercises the vanishing of non-self-dual contributions in the nonorientable moments and never tests the reconstruction of `c_d^0`.
- Required Round-1 fix: add at least one exact control with `nu=0` characters and verify both the nonorientable vanishing and the reconstruction logic. A small odd cyclic group or another group with non-real one-dimensional characters would be enough.

## MINOR issues

1. The all-positive-modulus families are not chains in the standard inclusion-order sense.

- Source: `sections/1_introduction.tex:45-54`, `sections/4_subgroup_counts.tex:7-10`
- `H_2` and `H_3` are incomparable, and likewise `L_2` and `L_3`. The manuscript does insert a local convention that "chain" means a divisibility-directed family, so this is not a theorem error. But the abstract and introduction use "chains" before that caveat is established, and many readers will read "chain" in the standard total-order sense.
- Required Round-1 fix: rename these objects to "families" or "directed systems", or front-load the divisibility convention at first use in the abstract/introduction.

2. The classical ownership subtraction is clear in the prose, but the bibliography still routes the key historical formulas only through Klug.

- Source: `sections/1_introduction.tex:31-34`, `sections/2_background.tex:47-75`, `sections/7_scope_controls.tex:13-19`, `CITATION_AUDIT.md:11-18`, `CITATION_AUDIT.md:40-47`, `references.bib`
- I do not regard this as a priority or ownership breach. The manuscript repeatedly says the surface homomorphism formulas are classical and not owned here. Still, for any external-facing version, direct historical citations or a sentence explicitly justifying use of a modern secondary source would reduce avoidable ambiguity.

## Source and ownership audit

- The classical surface homomorphism formulas are clearly owner-subtracted in the manuscript text. The introduction, background, and scope section all say that these formulas belong to prior literature and are used here via Klug's modern normalization/account.
- The rejected Rudin--Shapiro candidate is cleanly segregated, explicitly marked as non-manuscript content, and not smuggled into the present claim set.
- Paper mass survives subtraction. After removing the classical surface-count formulas themselves, the residual contribution is still nontrivial:
  the specific flat-connection SFT realization over `pi_1(N_3)`,
  the rooted gauge factorization,
  the two explicit finite-index probe families,
  the joint degree/indicator recovery argument by finite moments,
  and the `D_8/Q_8` orientation separation.
- My conclusion on ownership is therefore: subtraction is substantially honest, and the remaining mathematical mass is sufficient for a short note if the proof presentation is tightened.

## Reproducibility audit

- I reran `python3 papers/69-orientation-sensitive-surface-flat-sft/code/verify_surface_flat_sft.py` and obtained terminal status `ALL CHECKS PASS`.
- The rerun matches the frozen output file hash reported by the package:
  `73b89972f0bb810b4f85c1fbfd64d34405ef68c3f1880513402c1d79964429de`.
- `pdfinfo` on `main.pdf` reports a 10-page A4 PDF with suppressed author/date metadata and no encryption.
- `pdffonts` reports embedded/subset fonts only.
- `pdftotext` on `main.pdf`, together with `qa/final_text.txt`, shows no surviving comma-in-exponent corruption in the main displayed formulas. I did not detect a remaining compiled-PDF semantic typesetting error.
- `main.log` shows no undefined citation/reference or box-warning problem in the searched categories.
- Limits of the reproducibility layer:
  it checks selected classical count substitutions and parity behavior;
  it does not directly enumerate the manuscript's SFT on finite quotient cellulations;
  it does not test the `nu=0` branch;
  it does not prove Proposition 3.3 or Theorem 5.2. The manuscript mostly admits these limits, but they remain limits.

## Required Round-1 fixes

1. Repair Step 4 of Theorem 5.2 exactly: indexing and coefficient recovery must be stated correctly.
2. Add an exact finite control that exercises `nu=0` irreducibles and reports the nonorientable vanishing behavior.
3. Replace or explicitly front-load the nonstandard use of "chain".
4. For any external-facing version, strengthen the direct ownership citation line around the classical surface formulas.

## External-release status

- `HOLD`
- Reason: core formulas reconstruct, but the manuscript still has a central proof-writeup defect and an untested `nu=0` branch in its finite controls. Independent specialist literature review is also still mandatory by the package's own standards.

## Summary to coordinator

Core mathematics survives hostile reconstruction: the rooted gauge factor, the cover-topology exponents, the orientable/nonorientable fixed-point laws, the moment-recovery mechanism, and the `D_8/Q_8` separation all check out. I found no critical theorem failure, but I require one central proof repair, one additional `nu=0` control, and a terminology cleanup before this package should move past internal `HOLD`.
