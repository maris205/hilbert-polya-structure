# Claims--Evidence Matrix

**Paper:** *Marked Trace Coordinates and Scheme-Theoretic Ramification at the Polynomial Boundary of Generalized Hénon Maps*

**Date:** 2026-08-17

**Evidence mode:** theorem proof and primary-source verification only; no numerical, symbolic, experimental, or computer-assisted evidence

## Claim policy

Every positive claim in the article must have one of three evidence types:

- **D:** proved directly in the paper;
- **I:** imported from a cited theorem with hypotheses checked explicitly;
- **C:** a formal corollary of established claims, with the implication written out.

No claim may be supported by computational examples, plots, benchmark results, or unverified folklore. The planned article has zero figures and zero science experiments.

## Core claim matrix

| ID | Exact claim allowed in the paper | Type | Evidence and dependency | Scope guard | Status |
|---|---|---:|---|---|---|
| C1 | The universal ordered $n$-loop algebra is finite free of rank $d^n$ over $\mathbf C[b,a_0,\ldots,a_{d-2}]$. | D | Monic Gröbner basis with leading monomials $x_j^d$; standard monomial basis. | Full ordered loop incidence only; includes lower periods and multiplicities. | Proved in Proof Package, Lemma 1. |
| C2 | For $r$ independent point markings, the full product incidence is finite free of rank $d^{\sum_i n_i}$. | C | Tensor product of the bases in C1. | Does not impose exactness, disjointness, or simplicity. | Proved. |
| C3 | The cyclic-loop algebra represents the scheme of points fixed by $H^n$. | D | Functorial inverse maps $x_\bullet\mapsto(x_0,x_{n-1})$ and fixed point $\mapsto$ its first-coordinate loop. | Ordered point marking, not a cycle quotient. | Proved. |
| C4 | The simple point-marked incidence is étale over $\mathcal B_d$. | D | Relative Jacobian in orbit variables is block diagonal with blocks $DH^{n_i}-I$. | Only where all marked points are simple. | Proved. |
| C5 | Exactness and pairwise cycle-disjointness define open conditions. | D | Remove lower-period equations and finitely many iterate-collision equations. | Periods are fixed in advance. | Proved. |
| C6 | The cyclic shift group acts freely on the exact point-marked locus, and the cycle quotient is finite étale. | D | A nontrivial shift fixing a point would lower its exact period; characteristic zero. | Freeness need not hold on the full lower-period closure. | Proved. |
| C7 | At $b=0$, $H_{0,p}^n(x,y)=(p^n(x),p^{n-1}(x))$. | D | Direct induction. | Valid for every $n\ge1$. | Proved. |
| C8 | The scalar exact marked incidence is scheme-identical to the polynomial marked incidence under $x\mapsto(x,p^{n-1}(x))$. | D | Scalar fixed equations and their inverse projection. | Stated inside the simple exact disjoint locus. | Proved. |
| C9 | Scalar Hénon simplicity is equivalent to polynomial simplicity. | D | $DH_{0,p}^n=\bigl[\begin{smallmatrix}\lambda&0\\ *&0\end{smallmatrix}\bigr]$ and $\det(DH^n-I)=1-\lambda$. | The multiplier is that of the exact marked cycle. | Proved. |
| C10 | On the scalar boundary, the Hénon trace is exactly the polynomial multiplier. | D | Trace of the matrix in C9. | No individual two-dimensional eigenvalue branch is chosen. | Proved. |
| C11 | The arbitrary-period simple exact disjoint polynomial point-marked locus is irreducible. | I | Gorbovickis, Definition/Remark 1.4 and Lemma 1.5; take the nonempty simple exact disjoint open. | Use degree $d\ge2$ and at most $d-1$ markings. | Verified primary source. |
| C12 | For every period vector and $d-1$ distinct cycles, the polynomial multiplier differential has full rank somewhere. | I | Gorbovickis, Theorem 1.6 and Lemma 2.1, using all $d-1$ coefficient directions. | Arbitrary positive periods; test cycles are distinct and simple. | Verified primary source. |
| C13 | The scalar cycle-marked locus $\mathcal S_{\mathbf n}$ is irreducible. | C | C11 plus the finite cyclic quotient. | Quotient is taken only on the exact free locus. | Proved. |
| C14 | A unique irreducible component $\mathcal C_{\mathbf n}$ of the simple Hénon incidence contains the full scalar locus. | D | The simple incidence is regular; its distinct irreducible components are disjoint; apply irreducibility of C13. | This is not irreducibility of the full Hénon incidence. | Proved. |
| C15 | $\mathcal C_{\mathbf n}\to\mathcal B_d$ is étale and dominant. | D | Restriction of C4; étale maps are open and the base is irreducible. | Image need only be dense open, not all of $\mathcal B_d$. | Proved. |
| C16 | The scalar fiber of $\mathcal C_{\mathbf n}$ is exactly $\mathcal S_{\mathbf n}$ scheme-theoretically. | D | Every scalar simple tuple lies in C14; no other regular component meets it; étale fiber is reduced. | Only inside the simple exact disjoint incidence. | Proved. |
| C17 | $\Psi=(-b,\rho_1,\ldots,\rho_{d-1})$ is étale at a scalar point. | D+I | C10 and C12; block-triangular differential with first row $(-1,0,\ldots,0)$. | Point supplied by Gorbovickis on $p(z)=z^d$. | Proved. |
| C18 | $\Psi$ is dominant and generically étale. | C | Same source and target dimension; full rank at one point; openness of the étale locus. | On $\mathcal C_{\mathbf n}$ only. | Proved. |
| C19 | The traces are algebraically independent over $\mathbf C(b)$. | C | Injectivity of the target function field from C18; clear denominators in a hypothetical relation. | Functions live on the marked component's function field. | Proved. |
| C20 | For general fixed $b_0\ne0$, the whole fiber trace map is dominant. | D | Spread an open $V\subset\Psi(E)$ from the total étale locus and shrink the $b$-line. | “General” means $b_0$ lies in an unspecified nonempty Zariski-open $U\subset\mathbf G_m$. | Proved. |
| C21 | For each $b_0\in U$, at least one irreducible component of the reduced fiber maps dominantly and generically étale. | D | Finite union of component-image closures covers $\mathbf A^{d-1}$; base change the total étale locus. | No assertion for every component or fiber irreducibility. | Proved. |
| C22 | At every simple scalar tuple, the completed local ring of $\mathcal C_{\mathbf n}$ is $\mathbf C[[b,u_0,\ldots,u_{d-2}]]$. | D | Étale completed-local property; Stacks Tags 02GH and 0257. | Normal-form cover; residue field $\mathbf C$. | Proved. |
| C23 | The trace germs satisfy $\rho_i=\lambda_i+bG_i$. | D | C10 and C22; kernel of scalar restriction is the principal ideal $(b)$. | $\lambda_i$ is the chosen formal polynomial continuation. | Proved. |
| C24 | The Hénon critical Fitting scheme restricts exactly to the polynomial critical Fitting scheme. | D | Cartesian boundary square; base change of differentials and Fitting ideals, Stacks Tags 07Z6 and 0C3I. | On the simple scalar locus only. | Proved. |
| C25 | Local Jacobians satisfy $J_H\bmod b=\pm J_{\mathrm{poly}}$. | D | Block determinant and C23. | Sign depends on ordering of coordinates and is a unit. | Proved. |
| C26 | Multiplicities along irreducible components of the boundary ramification scheme agree. | C | Length of the local quotient by $(b,J_H)$ equals length after reduction to $(J_{\mathrm{poly}})$. | Generic component multiplicity; not an arbitrary closed-point number when $d>2$. | Proved. |
| C27 | The normal-form trace map is generically noninjective for $d>2$. | D | Residual $\mu_{d-1}$ diagonal conjugacy preserves $b$ and every trace and is generically free. | A lower-bound obstruction, not an exact generic degree computation. | Proved. |
| C28 | The main theorem also holds for $d=2$. | I+C | Gorbovickis Theorem 1.6 begins at degree $2$ for $k\le d-1$; all direct arguments allow $d=2$. | There is one marked cycle and $\mu_1$ is trivial. | Verified and proved. |

## Collision-sensitive positioning claims

| ID | Positioning claim | Evidence | Required wording |
|---|---|---|---|
| P1 | Gorbovickis already proves the arbitrary-period polynomial multiplier theorem and marked polynomial irreducibility. | arXiv:1305.0867, Theorem 1.6, Definition/Remark 1.4, Lemma 1.5. | “Our polynomial-boundary input is Gorbovickis's theorem,” never “we first prove arbitrary-period polynomial independence.” |
| P2 | Gorbovickis--Taflin's several-variable result does not subsume Hénon automorphisms. | arXiv:2411.12856 treats regular polynomial endomorphisms of $\mathbf C^n$ and $\mathbf P^n$; main period condition is at least $4$. | Emphasize the nonregular Hénon geometry and the $b=0$ boundary, while acknowledging the nearby local-coordinate narrative. |
| P3 | Huguin proves finite birational recovery from complete unmarked period-$1$ and period-$2$ polynomial spectra. | arXiv:2412.19335, Main Theorem. | Contrast complete unmarked small-period spectra with arbitrary selected marked cycles and local ramification. |
| P4 | Cantat--Dujardin prove full-spectrum Hénon rigidity and finite low-period determination results. | arXiv:2603.09445, Theorem A, Theorem 3.7, Theorem 4.2. | Present this as the closest Hénon-spectrum work; do not suggest it proves arbitrary selected marked coordinate systems. |
| P5 | Bianchi--He use the full marked unstable spectrum on hyperbolic components for a path metric. | arXiv:2606.29363. | Distinguish analytic/thermodynamic full-spectrum variation from finite algebraic trace coordinates and boundary Fitting schemes. |
| P6 | Friedland--Milnor give a low-degree fixed-point rigidity overlap. | ETDS 9 (1989), Theorem 7.1 and its fixed-point trace computation. | Acknowledge the $d=2,3$, period-$1$ special case; retain the arbitrary-period and scheme-boundary distinction. |

## Forbidden claim matrix

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

The permitted replacements are exactly the positive statements C1--C28: the unique scalar component rather than the full incidence; a nonempty open of nonzero fibers and at least one good component rather than all fibers or all components; dominant and generically étale rather than injective; the simple-locus Fitting restriction and generic component multiplicities rather than global, reduced, transverse, or pointwise assertions; and proof/source verification rather than computational evidence.

## Evidence-to-section map for a 23-page paper

| Paper section | Claims carried | Pages | Figures | Science experiments |
|---|---|---:|---:|---:|
| Introduction | C17--C28; P1--P6 at summary level | 3.5 | 0 | 0 |
| Marked incidence | C4--C6 | 3.0 | 0 | 0 |
| Universal loop algebra | C1--C3 and A11 guard | 2.0 | 0 | 0 |
| Scalar component and coordinates | C7--C19 | 4.0 | 0 | 0 |
| Completed local boundary | C22--C23 | 3.0 | 0 | 0 |
| Fitting ramification | C24--C26 | 3.5 | 0 | 0 |
| Fixed-$b$ fibers and quotients | C20--C21, C27 | 1.5 | 0 | 0 |
| Comparison and limitations | P1--P6, A1--A20 | 1.0 | 0 | 0 |
| Appendix algebra | edge cases supporting C1--C3 | 1.0 | 0 | 0 |
| References | primary records | 0.5 | 0 | 0 |

## Final evidence audit

- Primary mathematical claim count: 2 — generic arbitrary-period marked trace coordinates, and exact scalar-boundary ramification restriction.
- Supporting structural claim: finite-free full loop incidence.
- Imported deep result count: 1 — Gorbovickis's arbitrary-period polynomial theorem and irreducibility package.
- Empirical claims: 0.
- Experimental claims: 0.
- Figures required: 0.
- Claims depending on unverified future work: 0.
