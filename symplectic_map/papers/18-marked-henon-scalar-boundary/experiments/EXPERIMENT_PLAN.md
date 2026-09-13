# Experiment Plan

**Paper:** *Marked Trace Coordinates and Scheme-Theoretic Ramification at the Polynomial Boundary of Generalized Hénon Maps*

**Date:** 2026-08-17

**Mode:** zero-science source validation only

## Executive constraint

Paper18 is a proof paper. It has no scientific experiment, computational experiment, symbolic calculation, numerical example, dataset, benchmark, ablation, plot, or empirical result. No experiment can support any mathematical claim in this project.

This file adapts a claim-driven experiment plan into a source-design validation plan. Its only purpose is to check that the ten authorized Markdown files consistently state the same theorem, proof guards, citation roles, anti-claims, scores, and paper architecture. Validation is editorial and read-only except for corrections made to these authorized Markdown files by the source-design author.

## Frozen theorem under validation

For $d\ge2$, let $r=d-1$, choose arbitrary positive periods $n_1,\ldots,n_r$, and mark pairwise-disjoint simple exact cycles of
$$
H_{b,p}(x,y)=(p(x)+by,x)
$$
with monic centered $p$. On the cycle-marked incidence, the frozen theorem asserts exactly:

1. The scalar locus $\mathcal S_{\mathbf n}$ is nonempty and irreducible and is contained in a unique irreducible component $\mathcal C_{\mathbf n}$ of the simple exact disjoint incidence. The map $\mathcal C_{\mathbf n}\to\mathcal B_d$ is étale and dominant, and its scalar fiber is $\mathcal S_{\mathbf n}$ scheme-theoretically within that simple incidence.
2. $\Psi=(-b,\rho_1,\ldots,\rho_r)$ is étale at a scalar point, hence dominant and generically étale, and the traces are algebraically independent over $\mathbf C(b)$.
3. For every $b_0$ in an unspecified nonempty open $U\subset\mathbf G_m$, the whole specialized trace map is dominant and at least one irreducible component of the reduced fiber is dominant and generically étale. The fiber need not be irreducible, and no prescribed $b_0$ is covered.
4. At every simple scalar tuple,
   $$
   \widehat{\mathcal O}_{\mathcal C,s}\simeq\mathbf C[[b,u]],
   \qquad
   \rho_i=\lambda_i+bG_i.
   $$
5. On the simple scalar locus,
   $$
   \mathcal R_H\times_{\mathcal C}\mathcal S
   =\mathcal R_{\mathrm{poly}}
   $$
   scheme-theoretically and $J_H\bmod b=\pm J_{\mathrm{poly}}$. This preserves generic multiplicities along irreducible boundary components, not arbitrary closed-point numerical intersections when $d>2$.

The optional finite-free lemma says that the full ordered $n$-loop algebra is finite free of rank $d^n$. It is not evidence for irreducibility, exact-cycle counts, finiteness of the deleted simple open, or global reconstruction.

## Validation questions

| ID | Validation question | Acceptance criterion | Evidence class |
|---|---|---|---|
| V1 | Do all theorem-bearing files use the same degree, marking, component, and fixed-fiber quantifiers? | $d\ge2$; $r=d-1$; arbitrary positive periods; exact, disjoint, simple cycles; unique component through the full scalar locus; general nonzero fibers only; at least one good reduced component. | Editorial theorem comparison |
| V2 | Is every proof step discharged without CAS or experiments? | The proof dependency chain ends in direct algebraic arguments, Gorbovickis's precisely cited result, and exact Stacks lemmas. | Proof audit |
| V3 | Is the Fitting equality scoped correctly? | Equality is only on the Cartesian simple scalar locus; no reducedness, transversality, compactified equality, or unjustified point length is stated. | Scheme-scope audit |
| V4 | Are point markings, cycle markings, and residual normal-form symmetry separated? | Cyclic shifts are quotiented only on the exact locus; residual $\mu_{d-1}$ remains; coarse stabilizers carry a warning. | Definition audit |
| V5 | Are citation roles supported by primary sources? | Gorbovickis Theorem 1.6/Lemma 2.1 carry the $d\ge2$ claim; CD26 and BH26 use exact public v1 submission facts; Stacks tags match their stated role. | Source audit |
| V6 | Is the A1--A20 ledger identical in all ten files? | Each file contains exactly one complete canonical ledger with no changed wording or numbering. | Cross-file text audit |
| V7 | Is the manuscript envelope stable? | Every planning file records 22--24 pages, target 23, 0 figures, and 0 science experiments. | Architecture audit |
| V8 | Is the source-design inventory exact? | Exactly the ten authorized Markdown files exist under the Paper18 path; all have LF endings, final newlines, nonzero byte counts, and reported SHA-256 hashes. | Read-only filesystem audit |

## Claim-to-validation map

| Claim group | Validation | Failure condition |
|---|---|---|
| Marked component and scalar fiber | V1, V2, V4 | Any statement that the full incidence is irreducible or that unrelated components are controlled. |
| Dominant/generically étale trace coordinates | V1, V2 | Any missing block-differential step or any promotion from “general $b$” to “every/prescribed $b$.” |
| Fixed-$b$ specialization | V1, V2 | Any assumption that the specialized fiber is irreducible or every component is good. |
| Completed-local boundary | V2, V3, V4 | Any coarse-quotient assertion at a stabilizer or extension outside the simple normal-form cover. |
| Critical/Fitting restriction | V2, V3 | Any claim of radicality, transversality, global compactified equality, or automatic pointwise multiplicity. |
| Finite-free loop lemma | V1, V2 | Any conversion of rank into exact-cycle enumeration or full-incidence irreducibility. |
| Novelty positioning | V5 | Any implication imported from a neighboring work outside its verified scope or any absolute-priority language. |
| Whole source package | V6--V8 | Ledger mismatch, architecture drift, extra file, CRLF, missing final newline, or missing hash/byte record. |

## Proof-validation protocol

### PV1. Incidence and component audit

Read the definitions and Lemmas 2--5 in `../notes/PROOF_PACKAGE.md` continuously. Confirm that simplicity makes the orbit Jacobian invertible, exactness and disjointness are open, cyclic shifts act freely, the scalar polynomial marked locus is irreducible, and regular components are disjoint. Record no inference from the finite-free full loop scheme to irreducibility.

### PV2. Scalar differential audit

Confirm by the written direct induction, not by CAS, that
$$
H_{0,p}^n(x,y)=(p^n(x),p^{n-1}(x))
$$
and that the displayed derivative has trace $\lambda$ and determinant condition $1-\lambda$. Check that the differential of $\Psi$ has first row $(-1,0,\ldots,0)$ and lower-right multiplier Jacobian. The imported full-rank point must cite Gorbovickis Theorem 1.6 and Lemma 2.1 specifically; Corollary 1.7 is not the source of the $d=2$ case.

### PV3. Fixed-fiber audit

Let $E$ be the total étale locus. Verify that $\Psi|_E$ is étale and therefore open, so $V=\Psi(E)$ is a nonempty open subset of the target. After projecting and shrinking to $U\subset\mathbf G_m$, check that every $V_{b_0}$ is nonempty open dense. Dominance of the whole fiber follows. Since a finite-type reduced fiber has finitely many irreducible components, at least one has dense image; its meeting with the base-changed étale locus yields generic étaleness there. Do not infer all-component dominance.

### PV4. Formal and Fitting audit

Confirm that étaleness of $\mathcal C_{\mathbf n}\to\mathcal B_d$ gives the displayed completed local rings, scalar restriction has kernel $(b)$, and trace reduction gives $\rho_i=\lambda_i+bG_i$. On the Cartesian simple-boundary square, verify the base-change isomorphism for relative differentials and the Fitting ideal identity using Stacks Tag 07Z6/Lemma 15.8.4 and Tag 0C3I. The Jacobian congruence must be stated up to a unit sign. Translate scheme equality only into generic component multiplicities.

### PV5. Quotient audit

Confirm
$$
\det(DH_{b,p}^{n_i})=(-b)^{n_i}
$$
and the diagonal $\mu_{d-1}$ conjugacy. Check that “trace coordinate” never becomes “individual eigenvalue branch,” that cycle quotient removes only cyclic shifts, and that no coarse-quotient completed ring is asserted at a stabilizer.

## Citation-validation protocol

| Source | Required role | Forbidden inference |
|---|---|---|
| Gorbovickis, arXiv:1305.0867 | Theorem 1.6: $d\ge2$, $k\le d-1$, arbitrary periods; Definition/Remark 1.4 and Lemma 1.5: irreducible marked space; Lemma 2.1: full-rank test point. | Do not attribute the quadratic headline to Corollary 1.7, and do not claim the polynomial theorem as new. |
| Gorbovickis--Taflin, arXiv:2411.12856 | Neighboring regular-endomorphism multiplier coordinates. | Does not prove the Hénon theorem. |
| Huguin, arXiv:2412.19335 | Complete unmarked low-period polynomial spectra. | Does not yield arbitrary marked Hénon birationality. |
| Cantat--Dujardin, arXiv:2603.09445, v1 submitted 2026-03-10 | Full-spectrum Hénon rigidity and finite low-period determination. | Does not yield arbitrary selected coordinates or scalar-boundary Fitting equality. |
| Bianchi--He, arXiv:2606.29363, v1 submitted 2026-06-28 | Thermodynamic use of the full marked unstable spectrum. | Does not imply finite algebraic trace independence. |
| Friedland--Milnor, ETDS 9 (1989) | Normal forms and low-degree fixed-point overlap. | Does not subsume arbitrary periods or boundary ramification. |
| Stacks Tags 07Z6/0C3I and 02GH/0257 | Fitting base change and étale formal-local support, respectively. | Do not export either result beyond its established Cartesian/simple or normal-form hypotheses. |

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

## Stopped-candidate guard

The validation must fail if any source-design file revives full-incidence irreducibility, all-$b$ or prescribed-$b$ coordinates, all-component generic étaleness, global injectivity/birational reconstruction, a naive coarse-quotient completion, global nonsimple Fitting equality, reducedness, transversality, pointwise multiplicity without slicing, eigenvalue-branch coordinates, exact-cycle enumeration by $d^n$, positive characteristic, multi-factor composition, or absolute-priority language.

## Resource and evidence budget

| Resource | Authorized amount |
|---|---:|
| Scientific experiments | 0 |
| Computational experiments | 0 |
| CAS computations | 0 |
| Datasets | 0 |
| GPU/accelerator time | 0 |
| Figures | 0 |
| Numerical result tables | 0 |
| Target manuscript pages | 23 |
| Acceptable manuscript range | 22--24 |

## Completion rule

The source-validation plan is complete when V1--V8 pass, the exact ten-file inventory and read-only SHA-256/byte/LF checks are reported, the scores remain 8.0/7.7/9.3 against thresholds 7.5/7.5/9.0, and no result beyond the frozen theorem or A1--A20 ledger is introduced.
