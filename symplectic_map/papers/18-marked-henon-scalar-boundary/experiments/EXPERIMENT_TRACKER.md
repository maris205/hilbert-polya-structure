# Experiment Tracker

**Paper:** *Marked Trace Coordinates and Scheme-Theoretic Ramification at the Polynomial Boundary of Generalized Hénon Maps*

**Date:** 2026-08-17

**Tracker type:** zero-science editorial validation; no experiment run is authorized or recorded

## Status

| Item | Status | Record |
|---|---|---|
| Scientific experiments | NOT APPLICABLE | Count 0; theorem proof only. |
| Computational experiments | NOT APPLICABLE | Count 0; no code or CAS. |
| Datasets and benchmarks | NOT APPLICABLE | Count 0. |
| Figures and empirical tables | NOT APPLICABLE | Count 0. |
| Theorem quantifier audit | COMPLETE | $d\ge2$; $d-1$ arbitrary-period, exact, disjoint, simple cycle markings; unique scalar component. |
| Fixed-$b$ guard audit | COMPLETE | General $b_0\in U\subset\mathbf G_m$; whole fiber dominant; at least one reduced component dominant and generically étale. |
| Fitting-scope audit | COMPLETE | Scheme equality only on the simple scalar locus; generic component multiplicities only. |
| Quotient audit | COMPLETE | Cyclic shifts removed by cycle marking; residual $\mu_{d-1}$ retained; coarse stabilizer warning present. |
| Primary-source role audit | COMPLETE | Gorbovickis and exact Stacks roles fixed; collision papers comparison-only. |
| Ten-file text audit | COMPLETE | Exactly 10 authorized Markdown files, 4 directories including the package root, 0 symlinks, identical A1--A20 ledgers, and no unsupported internal source date. |
| LF/final-newline audit | COMPLETE | All 10 files are LF-only and end in LF; no trailing whitespace. |
| SHA-256 and byte inventory | COMPLETE | Final values are reported in the author handoff; no eleventh manifest file was created. |

## Frozen theorem checkpoints

| Checkpoint | Frozen statement | Status |
|---|---|---|
| T1 | $\mathcal S_{\mathbf n}$ is nonempty and irreducible and lies in a unique component $\mathcal C_{\mathbf n}$; $\mathcal C_{\mathbf n}\to\mathcal B_d$ is étale/dominant and has scalar fiber exactly $\mathcal S_{\mathbf n}$ on the simple incidence. | COMPLETE |
| T2 | $\Psi=(-b,\rho_1,\ldots,\rho_{d-1})$ is étale at one scalar point, dominant, and generically étale; the traces are algebraically independent over $\mathbf C(b)$. | COMPLETE |
| T3 | For $b_0$ in a nonempty open of $\mathbf G_m$, the whole fiber map is dominant and at least one reduced irreducible component is dominant/generically étale; no fiber irreducibility. | COMPLETE |
| T4 | Every simple scalar completed local ring is $\mathbf C[[b,u]]$ and $\rho_i=\lambda_i+bG_i$. | COMPLETE |
| T5 | $\mathcal R_H\times_{\mathcal C}\mathcal S=\mathcal R_{\mathrm{poly}}$ scheme-theoretically on the simple locus and $J_H\bmod b=\pm J_{\mathrm{poly}}$; only generic component multiplicities follow. | COMPLETE |
| T6 | The full ordered-loop algebra is finite free of rank $d^n$, but the lemma proves neither irreducibility nor an exact-cycle count nor finiteness of the deleted open. | COMPLETE |

## Proof-dependency tracker

| Dependency | Exact role | Status |
|---|---|---|
| Orbit-equation Jacobian | Étaleness of the simple point-marked incidence. | COMPLETE |
| Free cyclic-shift quotient | Passage from point markings to cycle markings. | COMPLETE |
| Scalar iteration/derivative | Polynomial boundary identification, trace reduction, and simplicity. | COMPLETE |
| Gorbovickis, arXiv:1305.0867 | Theorem 1.6 and Lemma 2.1 support $d\ge2$ arbitrary-period full rank; Definition/Remark 1.4 and Lemma 1.5 support marked-space irreducibility. | COMPLETE |
| Regular-component argument | Unique total component through the full scalar locus. | COMPLETE |
| Open image of étale locus | Safe general fixed-$b$ statement without fiber irreducibility. | COMPLETE |
| Stacks Tags 02GH/0257 | Étale formal-local completion. | COMPLETE |
| Stacks Tag 07Z6/Lemma 15.8.4 and Tag 0C3I | Fitting base change and closed-subscheme restriction. | COMPLETE |
| Diagonal $\mu_{d-1}$ action | Global-injectivity obstruction and coarse-stabilizer warning. | COMPLETE |

## Collision-source tracker

| Source | Public-record role | Status |
|---|---|---|
| Gorbovickis, arXiv:1305.0867 | Imported theorem, with $d\ge2$ attributed to Theorem 1.6/Lemma 2.1 rather than Corollary 1.7. | VERIFIED |
| Gorbovickis--Taflin, arXiv:2411.12856 | Regular-endomorphism comparison only. | VERIFIED |
| Huguin, arXiv:2412.19335 | Complete unmarked low-period polynomial spectra comparison only. | VERIFIED |
| Cantat--Dujardin, arXiv:2603.09445 | v1 submitted 2026-03-10; full Hénon spectrum comparison only. | VERIFIED |
| Bianchi--He, arXiv:2606.29363 | v1 submitted 2026-06-28; thermodynamic full marked unstable spectrum comparison only. | VERIFIED |
| Friedland--Milnor, ETDS 9 (1989) | Normal-form and low-degree overlap. | VERIFIED |
| Stacks Project | Exact tags 07Z6, 0C3I, 02GH, and 0257 assigned only their verified algebraic roles. | VERIFIED |

## Frozen anti-claim ledger

The following A1--A20 ledger is frozen verbatim across all ten source-design files.

- **A1.** No irreducibility claim for the full marked Hénon incidence.
- **A2.** No irreducibility claim for any or every specialized fixed-$b$ fiber.
- **A3.** No local-coordinate claim for every nonzero $b$.
- **A4.** No conclusion at any prescribed nonzero fiber, including $b=-1$.
- **A5.** No global injectivity, birationality, or reconstruction claim on the monic-centered normal-form cover.
- **A6.** No claim that every irreducible component of a general fixed-$b$ fiber dominates or is generically étale.
- **A7.** No reducedness or smoothness claim for either critical/Fitting scheme.
- **A8.** No transversality or normal-crossings claim for the boundary intersection.
- **A9.** No global, nonsimple, or compactified Fitting-scheme equality beyond the simple scalar locus.
- **A10.** No closed-point numerical intersection multiplicity without a separately justified proper transverse slice; the theorem preserves generic multiplicities along boundary components.
- **A11.** No individual eigenvalue branch is a coordinate: $\det(DH_{b,p}^{n_i})=(-b)^{n_i}$, so trace records only the unordered eigenvalue pair once the determinant is known.
- **A12.** No interpretation of finite-free rank $d^n$ as an exact-cycle count.
- **A13.** The fiber $b=0$ is only the polynomial/proof boundary; $H_{0,p}$ is not a Hénon automorphism.
- **A14.** No positive-characteristic extension.
- **A15.** No extension to multi-factor or composed generalized Hénon maps.
- **A16.** Point-marked fibers contain cyclic-shift copies; passage to cycle markings removes only those shifts, not residual $\mu_{d-1}$ ambiguity.
- **A17.** No naive coarse $\mu_{d-1}$-quotient completed-local claim near stabilizers; stack or quotient-singularity analysis is required.
- **A18.** No claim that the simple exact open is finite or proper over all of $\mathcal B_d$, no uniform all-fiber degree, and no all-fiber reconstruction.
- **A19.** No absolute-priority or “first ever” claim.
- **A20.** No computational, CAS, numerical, empirical, or experimental evidence or result.

## Stopped candidates

| Candidate family | Status | Frozen replacement |
|---|---|---|
| Full-incidence or all-fiber irreducibility | STOPPED | Unique component through the full scalar locus; no specialized-fiber irreducibility. |
| Every-$b$, $b=-1$, or all-component coordinates | STOPPED | General $b\in U$ and at least one component of the reduced fiber dominant and generically étale. |
| Global injectivity, birationality, or reconstruction | STOPPED | Dominant/generically étale map with residual $\mu_{d-1}$ warning. |
| Global/nonsimple Fitting equality, reducedness, or transversality | STOPPED | Exact simple-boundary scheme restriction only. |
| Pointwise intersection number without slicing | STOPPED | Generic multiplicity along boundary components. |
| Individual eigenvalue coordinates | STOPPED | Trace plus known determinant gives an unordered pair. |
| Exact-cycle count from $d^n$ | STOPPED | Full ordered-loop scheme rank only. |
| Positive characteristic or multi-factor maps | STOPPED | Characteristic zero, one generalized Hénon factor. |
| Absolute priority or computational verification | STOPPED | Narrow comparative novelty and proof/source evidence only. |

## Architecture tracker

| Quantity | Frozen value | Status |
|---|---:|---|
| Acceptable pages | 22--24 | LOCKED |
| Target pages | 23 | LOCKED |
| Figures | 0 | LOCKED |
| Scientific experiments | 0 | LOCKED |
| Computational experiments | 0 | LOCKED |
| Numerical result tables | 0 | LOCKED |
| Novelty score | 8.0/10 against 7.5 | PASS |
| Standalone score | 7.7/10 against 7.5 | PASS |
| Proof-readiness score | 9.3/10 against 9.0 | PASS |

## Finalization rule

After the read-only inventory/LF/hash audit passes, update nothing outside the ten authorized source-design files and report **SOURCE DESIGN AUTHOR STOP**. This tracker records no scientific result.
