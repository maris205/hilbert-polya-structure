# Initial Proposal

**Historical status:** superseded by the repaired final proposal

**Date recorded:** 2026-08-17

**Initial title:** *Marked Multiplier Coordinates and Exact Scalar-Boundary Ramification for Generalized Hénon Maps*

## Initial thesis

Let $d\ge3$, let $\mathcal P_d^{\mathrm{cm}}$ be the monic centered degree-$d$ polynomials, and extend the generalized Hénon family to
$$
H_{b,p}(x,y)=(p(x)+by,x),
\qquad b\in\mathbf A^1.
$$
For arbitrary positive periods $n_1,\ldots,n_{d-1}$, choose pairwise-disjoint simple exact-period marked cycles and define
$$
\rho_i=\operatorname{tr}(DH_{b,p}^{n_i}),
\qquad
\Psi=(-b,\rho_1,\ldots,\rho_{d-1}).
$$
The initial proposal asserted that there is an irreducible marked component containing and dominating the scalar boundary such that $\Psi$ is dominant and generically étale. It further asserted algebraic independence of the $\rho_i$ over $\mathbf C(b)$, generic fixed-nonzero-$b$ local coordinates, completed-local trace expansions
$$
\rho_i=\lambda_i+bG_i,
$$
and an exact scheme-theoretic restriction of the Hénon critical scheme to the polynomial multiplier critical scheme at $b=0$.

## Initial mechanism

At the scalar boundary,
$$
H_{0,p}^n(x,y)=(p^n(x),p^{n-1}(x)),
$$
so a polynomial exact $n$-cycle lifts canonically to the plane. Along such a lifted point,
$$
DH_{0,p}^n=
\begin{pmatrix}
\lambda&0\\
*&0
\end{pmatrix},
$$
where $\lambda=(p^n)'$. Therefore
$$
\operatorname{tr}(DH_{0,p}^n)=\lambda,
\qquad
\det(DH_{0,p}^n-I)=1-\lambda.
$$
The intended proof imported Gorbovickis's arbitrary-period polynomial multiplier independence and used the block differential
$$
D\Psi|_{b=0}=
\begin{pmatrix}
-1&0\\
*&D\Lambda
\end{pmatrix}.
$$
For the critical scheme, the initial argument observed that the same block form gives
$$
J_H\bmod b=\pm J_{\mathrm{poly}}.
$$

## Initial contribution claims

1. A finite arbitrary selection of marked Hénon cycles of any prescribed periods gives generic local coordinates.
2. Polynomial multiplier independence transfers across the singular Hénon degeneration $b=0$.
3. The transfer retains the full critical scheme and its boundary multiplicities, not only the reduced critical set.
4. The result complements global full-spectrum Hénon rigidity with a minimal-dimensional marked local-coordinate theorem.

## Strengths identified at proposal time

- The parameter count is exact: $d-1$ polynomial coefficients plus $b$, matched by $d-1$ traces plus $-b$.
- Arbitrary periods, including repeated period values, are inherited from the strongest one-variable input.
- The scalar derivative computation is transparent.
- The Fitting formulation naturally excludes unsupported reducedness and transversality claims.
- The story is proof-theoretic; no numerical evidence is needed.

## Ambiguities and risks in the initial version

The initial proposal was not source-ready for the following reasons.

### 1. Marked points versus marked cycles

Gorbovickis's algebraic space is naturally point-marked, while the title and theorem said “marked cycles.” The finite cyclic quotient and its freeness on the exact locus were not defined.

### 2. The component quantifier

“An irreducible marked component containing/dominating the scalar boundary” did not say whether it contained one scalar test point, one boundary component, or the full simple scalar marked locus. It also risked sounding like irreducibility of the full Hénon incidence.

### 3. Exactness and collisions

Arbitrary period vectors can repeat. The theorem needed an explicit open condition removing lower-period solutions and all iterate collisions between labelled cycles.

### 4. Degree range

The initial $d\ge3$ range followed the wording of Gorbovickis's corollary, but his Theorem 1.6 already covers $d=2$, $k=1$.

### 5. Fixed-$b$ specialization

“Generic fixed nonzero $b$” needed to mean $b$ in a nonempty Zariski-open subset of $\mathbf G_m$. Total dominance does not establish every nonzero fiber or a prescribed fiber.

### 6. Reducible specialized fibers

Even if the total component is irreducible, a closed fiber can be reducible. The initial statement did not specify on which specialized component generic étaleness holds.

### 7. Fitting-scheme scope

The local calculation is exact on the simple scalar locus. The proposal did not explicitly bar a reader from interpreting it as a global compactified statement through nonsimple points.

### 8. Intersection multiplicity language

For $d>2$, the intersection of the two divisors has positive dimension. “Preserves boundary intersection multiplicities” needed to refer to generic multiplicities along irreducible components, not automatically to closed-point lengths.

### 9. Residual normal-form quotient

The $\mu_{d-1}$ diagonal conjugacy preserves every proposed coordinate. It rules out generic global injectivity on the monic-centered cover and complicates coarse-quotient completions at stabilizer points.

### 10. Novelty proximity

The proposal needed direct positioning against Gorbovickis--Taflin, Huguin, Cantat--Dujardin, Bianchi--He, and the low-degree Friedland--Milnor calculations.

## Initial anti-claims

Even the initial version intended to exclude:

- reducedness of the critical schemes;
- transversality of the boundary intersection;
- global injectivity.

The gate concluded that this list was insufficient and expanded it substantially in the final proposal.

The following final A1--A20 ledger is frozen verbatim across all ten source-design files, including this historical record.

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

## Initial page concept

The first concept was a short algebraic-dynamics note of approximately 18--20 pages. Review concluded that a correct standalone treatment needs 22--24 pages because the exact marked incidence, cycle quotient, specialized-fiber guard, Fitting base change, residual finite action, and collision matrix must be explicit.

Figures proposed: 0.

Scientific or computational experiments proposed: 0.

## Disposition

**REPAIR.** The mechanism was accepted, but the statement required a complete quantifier and scheme-scope rewrite. The current theorem is the one in `FINAL_PROPOSAL.md` and `../notes/PROOF_PACKAGE.md`; this file is retained only as an auditable history of the refinement.
