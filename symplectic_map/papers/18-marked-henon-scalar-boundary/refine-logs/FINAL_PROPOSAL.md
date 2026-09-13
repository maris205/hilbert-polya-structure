# Final Proposal

**Working title:** *Marked Trace Coordinates and Scheme-Theoretic Ramification at the Polynomial Boundary of Generalized Hénon Maps*

**Date:** 2026-08-17

**Decision:** GO for a 22--24 page proof paper; target 23 pages, 0 figures, and 0 scientific or computational experiments.

## Final thesis

For a single generalized Hénon normal form
$$
H_{b,p}(x,y)=(p(x)+by,x),
$$
where $p$ is monic centered of degree $d\ge2$, choose $d-1$ pairwise-disjoint simple cycles of arbitrary prescribed positive periods. The trace functions of these marked cycles, together with $-b$, form a dominant generically étale coordinate map on the unique irreducible component through the full simple polynomial boundary. At that boundary, the completed trace germs reduce to the one-variable multipliers and the relative critical Fitting scheme restricts exactly, scheme-theoretically, to the polynomial multiplier critical scheme.

The contribution is not a new polynomial multiplier-independence theorem. It imports Gorbovickis's arbitrary-period result and proves the Hénon component construction, scalar lift, block differential, safe fixed-$b$ spreading, completed-local statement, and exact Fitting base change.

## Setup

Let
$$
\mathcal P_d^{\rm cm}
=\left\{p(z)=z^d+\sum_{k=0}^{d-2}a_kz^k\right\}
\simeq\mathbf A^{d-1}
$$
and
$$
\mathcal B_d=\mathbf A^1_b\times\mathcal P_d^{\rm cm}.
$$
Put $r=d-1$ and fix
$$
\mathbf n=(n_1,\ldots,n_r)\in\mathbf Z_{>0}^{r};
$$
period repetitions are allowed. Let $\widetilde{\mathcal X}_{\mathbf n}^{\circ}$ be the incidence of point-marked tuples $(b,p,z_1,\ldots,z_r)$ such that each $z_i$ has exact period $n_i$, all marked cycles are pairwise disjoint, and
$$
\det(D_{z_i}H_{b,p}^{n_i}-I)\ne0.
$$
The free cyclic-shift group
$$
G_{\mathbf n}=\prod_i\mathbf Z/n_i\mathbf Z
$$
acts on this exact locus. Define the cycle-marked incidence
$$
\mathcal X_{\mathbf n}^{\circ}
=\widetilde{\mathcal X}_{\mathbf n}^{\circ}/G_{\mathbf n},
$$
its scalar locus
$$
\mathcal S_{\mathbf n}=(\mathcal X_{\mathbf n}^{\circ})_{b=0},
$$
and the marked traces
$$
\rho_i=\operatorname{tr}(D_{z_i}H_{b,p}^{n_i}).
$$
The trace is cyclic-shift invariant. Let $\lambda_i$ be the corresponding one-variable polynomial multiplier on $\mathcal S_{\mathbf n}$.

## Exact theorem

### Theorem A: marked trace coordinates and scalar-boundary ramification

For every $d\ge2$ and every $\mathbf n\in\mathbf Z_{>0}^{d-1}$, the following assertions hold.

1. **Marked scalar component.** The scalar cycle-marked locus $\mathcal S_{\mathbf n}$ is nonempty and irreducible. It is contained in a unique irreducible component $\mathcal C_{\mathbf n}$ of $\mathcal X_{\mathbf n}^{\circ}$. The natural map
   $$
   \pi:\mathcal C_{\mathbf n}\longrightarrow\mathcal B_d
   $$
   is étale and dominant. Moreover,
   $$
   (\mathcal C_{\mathbf n})_{b=0}=\mathcal S_{\mathbf n}
   $$
   scheme-theoretically inside the simple exact disjoint incidence.

2. **Coordinate map.** The morphism
   $$
   \Psi=(-b,\rho_1,\ldots,\rho_r):\mathcal C_{\mathbf n}
   \longrightarrow\mathbf A^1\times\mathbf A^r
   $$
   is étale at some scalar point and hence is dominant and generically étale. Consequently,
   $$
   \rho_1,\ldots,\rho_r
   $$
   are algebraically independent over $\mathbf C(b)$ in $\mathbf C(\mathcal C_{\mathbf n})$.

3. **Safe fixed-$b$ specialization.** There is a nonempty Zariski-open set $U\subset\mathbf G_m$ such that, for every $b_0\in U$, the whole-fiber map
   $$
   \rho_{b_0}:
   (\mathcal C_{\mathbf n})_{b_0}\longrightarrow\mathbf A^r,
   \qquad
   x\longmapsto(\rho_1(x),\ldots,\rho_r(x)),
   $$
   is dominant. For each $b_0\in U$, at least one irreducible component of the reduced fiber $(\mathcal C_{\mathbf n})_{b_0,\mathrm{red}}$ maps dominantly and generically étale to $\mathbf A^r$. No irreducibility of the specialized fiber is asserted.

4. **Completed local form.** For every scalar point $s\in\mathcal S_{\mathbf n}$ and centered coefficient coordinates $u=(u_0,\ldots,u_{d-2})$ based at $\pi(s)$, there are compatible isomorphisms
   $$
   \widehat{\mathcal O}_{\mathcal C_{\mathbf n},s}
   \simeq\mathbf C[[b,u_0,\ldots,u_{d-2}]],
   \qquad
   \widehat{\mathcal O}_{\mathcal S_{\mathbf n},s}
   \simeq\mathbf C[[u_0,\ldots,u_{d-2}]],
   $$
   under which
   $$
   \rho_i(b,u)=\lambda_i(u)+bG_i(b,u)
   $$
   for a unique $G_i\in\mathbf C[[b,u]]$.

5. **Fitting-scheme restriction.** Define
   $$
   \mathcal R_H
   =V\!\left(\operatorname{Fitt}_0
   \Omega_{\mathcal C_{\mathbf n}/(\mathbf A^1\times\mathbf A^r)}\right)
   $$
   and
   $$
   \mathcal R_{\mathrm{poly}}
   =V\!\left(\operatorname{Fitt}_0
   \Omega_{\mathcal S_{\mathbf n}/\mathbf A^r}\right).
   $$
   Then
   $$
   \mathcal R_H\times_{\mathcal C_{\mathbf n}}\mathcal S_{\mathbf n}
   =\mathcal R_{\mathrm{poly}}
   $$
   as closed subschemes of $\mathcal S_{\mathbf n}$. In completed local coordinates, if $J_H$ and $J_{\mathrm{poly}}$ are local Jacobian determinants, then
   $$
   J_H\bmod b=\pm J_{\mathrm{poly}}.
   $$
   Hence scheme multiplicities agree along every irreducible component of the boundary ramification scheme. For $d>2$, no closed-point numerical intersection multiplicity is asserted without a proper transverse slice.

Here $\Psi$ uses the target coordinate $t=-b$. Also
$$
\det(DH_{b,p}^{n_i})=(-b)^{n_i};
$$
therefore a trace determines only the unordered eigenvalue pair after the determinant is fixed, not an individual eigenvalue branch.

## Auxiliary finite-free lemma

Let $R_d=\mathbf C[b,a_0,\ldots,a_{d-2}]$ and, for $n\ge1$, set
$$
A_n=R_d[x_0,\ldots,x_{n-1}]
\Big/
\left(p(x_j)+b x_{j-1}-x_{j+1}:j\in\mathbf Z/n\mathbf Z\right).
$$
For any graded monomial order in the $x$-variables, the normalized relations have leading monomials $x_j^d$. They are monic and pairwise coprime, so the monic Buchberger criterion over $R_d$ gives a Gröbner basis. Thus $A_n$ is finite free of rank $d^n$, with basis
$$
\left\{x_0^{e_0}\cdots x_{n-1}^{e_{n-1}}:0\le e_j<d\right\}.
$$
The argument includes the cyclic coincidences at $n=1$ and $n=2$. Cyclic first coordinates identify this scheme with the full $H^n$ fixed-point incidence. Products for the $r$ markings are finite free of rank $d^{\sum_i n_i}$.

This lemma is auxiliary. The full incidence includes lower periods, collisions, nonsimple points, and nonreduced fibers. The lemma does not imply full-incidence irreducibility, does not count exact cycles, and does not make the deleted simple exact open finite or proper over the entire base.

## Proof obligations and discharge

| Obligation | Discharge | Guard |
|---|---|---|
| Exact marked incidence | The orbit-equation Jacobian in each marking is $DH^{n_i}-I$; simplicity makes the point-marked incidence étale. Exactness and disjointness are open, and the cyclic-shift action is free. | Point markings and cycle markings remain distinct. |
| Scalar identification | $H_{0,p}^n(x,y)=(p^n(x),p^{n-1}(x))$ and $DH_{0,p}^n=\left[\begin{smallmatrix}\lambda&0\\ *&0\end{smallmatrix}\right]$. Hence simplicity is $1-\lambda\ne0$ and trace equals $\lambda$. | $b=0$ is a proof boundary, not an automorphism. |
| Scalar irreducibility and rank | Import Gorbovickis's marked-polynomial irreducibility and arbitrary-period full-rank theorem for $d\ge2$ and at most $d-1$ cycles. | Repeated periods are allowed; the cycles are distinct. |
| Unique total component | The simple incidence is regular because it is étale over smooth $\mathcal B_d$; distinct irreducible components are disjoint. The irreducible scalar locus therefore lies in one component. | No statement about other full-incidence components. |
| Total coordinate map | At the Gorbovickis point, $d\Psi$ is block triangular with first row $(-1,0,\ldots,0)$ and the polynomial multiplier Jacobian as the lower-right block. | Proves étale at one scalar point, then dominance and generic étaleness. |
| Fixed-$b$ fibers | Let $E$ be the étale locus of $\Psi$. Since $\Psi|_E$ is étale, it is open; $V=\Psi(E)$ is nonempty open. Shrink the open projection of $V$ to $U\subset\mathbf G_m$. Then each $V_{b_0}$ is nonempty open dense, so the whole fiber map is dominant; among finitely many reduced components, at least one is dominant and meets the base-changed étale locus. | Does not assume specialized fibers irreducible or all components good. |
| Completed local form | Étaleness of $\pi$ identifies the completed local rings with the completed base; scalar restriction has kernel $(b)$ and $\rho_i\bmod b=\lambda_i$. | Stacks Tags 02GH and 0257 support the formal-local step. |
| Fitting restriction | The scalar square is Cartesian on the simple component. Base change gives $\Omega_{\mathcal C/T}\otimes\mathcal O_{\mathcal S}\cong\Omega_{\mathcal S/\mathbf A^r}$; Fitting ideals commute with base change. The local block determinant gives $J_H\bmod b=\pm J_{\mathrm{poly}}$. | Stacks Tag 07Z6, Lemma 15.8.4, and scheme-level Tag 0C3I; no global nonsimple extension. |
| Multiplicity | Equality of closed subschemes preserves the generic lengths along irreducible components of the boundary ramification scheme. | A closed-point number for $d>2$ requires a separate proper transverse slice. |
| Residual quotient | Diagonal conjugacy by $\beta^{d-1}=1$ preserves $b$, the cycles, and all traces. | Rules out injectivity on the cover; coarse stabilizers need separate analysis. |

The full lemma-by-lemma proof is frozen in `../notes/PROOF_PACKAGE.md`.

## Primary-source roles and collision control

| Source | Exact role | Collision avoided |
|---|---|---|
| Gorbovickis, arXiv:1305.0867 | Theorem 1.6 gives arbitrary-period independence for degree $d\ge2$ and $k\le d-1$; Definition/Remark 1.4 and Lemma 1.5 give the irreducible marked space and marking independence; Lemma 2.1 supplies the test point. | Polynomial input is credited, not claimed as new. |
| Gorbovickis--Taflin, arXiv:2411.12856 | Comparison with multiplier coordinates for regular polynomial endomorphisms, principally periods at least $4$. | Their regular-endomorphism theorem is not imported as a Hénon theorem. |
| Huguin, arXiv:2412.19335 | Comparison with finite birational recovery from complete unmarked period-$1$ and period-$2$ polynomial spectra. | Complete unmarked small-period data are not arbitrary marked Hénon coordinates. |
| Cantat--Dujardin, arXiv:2603.09445, v1 submitted 2026-03-10 | Closest Hénon comparison: full-spectrum rigidity and finite low-period determination. | Full spectra do not prove arbitrary selected finite trace coordinates or boundary Fitting equality. |
| Bianchi--He, arXiv:2606.29363, v1 submitted 2026-06-28 | Comparison with the full marked unstable spectrum and thermodynamic path metrics on hyperbolic components. | Analytic full-spectrum variation does not imply the algebraic theorem here. |
| Friedland--Milnor, ETDS 9 (1989) | Foundational normal forms and the low-degree period-$1$ overlap. | The arbitrary-period and scheme-boundary scope remains distinct. |
| Stacks Project, Tags 07Z6 and 0C3I | Base change for Fitting ideals and the associated closed subschemes. | Used only on the proved Cartesian simple-boundary square. |
| Stacks Project, Tags 02GH and 0257 | Étale and completed/formal-local behavior. | No coarse-quotient completion is inferred. |

The literature stop date is 2026-08-17. No absolute-priority assertion is authorized.

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

- Full-incidence irreducibility: stopped; only the unique component through the scalar locus is proved.
- Every-$b$ or prescribed-$b$ coordinates: stopped; only a nonempty open $U\subset\mathbf G_m$ is proved.
- All specialized components generically étale: stopped; at least one component of the reduced fiber is dominant and generically étale.
- Global injectivity or birational reconstruction: stopped by the residual $\mu_{d-1}$ action.
- Global compactified Fitting equality, reducedness, and transversality: stopped beyond the simple scalar locus.
- Closed-point boundary multiplicities in dimension greater than two: stopped without a proper transverse slice.
- Eigenvalue-branch coordinates: stopped at the multiplier discriminant; trace plus determinant gives an unordered pair.
- Exact-cycle enumeration by $d^n$: stopped because the finite-free loop scheme includes lower periods and multiplicities.
- Positive characteristic and multi-factor compositions: stopped outside the hypotheses and proof.
- Absolute priority and computer verification: stopped.

## Paper architecture

| Section | Pages | Figures | Science experiments |
|---|---:|---:|---:|
| Abstract and introduction | 3.5 | 0 | 0 |
| Marked incidence and exact-cycle quotients | 3.0 | 0 | 0 |
| Universal cyclic-loop algebra | 2.0 | 0 | 0 |
| Scalar component and coordinate theorem | 4.0 | 0 | 0 |
| Completed local boundary | 3.0 | 0 | 0 |
| Fitting ramification and multiplicities | 3.5 | 0 | 0 |
| General nonzero fibers and finite quotients | 1.5 | 0 | 0 |
| Comparison, limitations, and outlook | 1.0 | 0 | 0 |
| Appendix algebra details | 1.0 | 0 | 0 |
| References | 0.5 | 0 | 0 |
| **Total** | **23.0** | **0** | **0** |

Acceptable manuscript range: 22--24 pages. No figure, computation, numerical table, code artifact, or empirical section is part of the design.

## Scores and final disposition

| Dimension | Score | Threshold | Result |
|---|---:|---:|---|
| Novelty | **8.0/10** | 7.5 | Pass |
| Standalone value | **7.7/10** | 7.5 | Pass |
| Proof readiness | **9.3/10** | 9.0 | Pass |

**Final disposition: GO FOR SOURCE DESIGN WITH CLAIM FREEZE.**
