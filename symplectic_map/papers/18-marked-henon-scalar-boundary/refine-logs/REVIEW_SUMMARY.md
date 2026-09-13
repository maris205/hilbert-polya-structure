# Review Summary

**Paper:** *Marked Trace Coordinates and Scheme-Theoretic Ramification at the Polynomial Boundary of Generalized Hénon Maps*

**Date:** 2026-08-17

**Document role:** source-design refinement record. This is not an independent review, a manuscript review, or a publication decision.

## Outcome first

The initial candidate received **REPAIR** because its component, specialized-fiber, and ramification quantifiers were too strong. After the repairs below, it received **GO FOR SOURCE DESIGN WITH CLAIM FREEZE**.

The final scores are:

| Dimension | Score | Required threshold | Outcome |
|---|---:|---:|---|
| Novelty | **8.0/10** | 7.5 | Pass |
| Standalone value | **7.7/10** | 7.5 | Pass |
| Proof readiness | **9.3/10** | 9.0 | Pass |

## Frozen theorem

Let $d\ge2$, $r=d-1$, $\mathbf n=(n_1,\ldots,n_r)\in\mathbf Z_{>0}^r$, and
$$
H_{b,p}(x,y)=(p(x)+by,x),
\qquad
p(z)=z^d+\sum_{k=0}^{d-2}a_kz^k.
$$
Periods may repeat, but the marked cycles are exact, pairwise disjoint, and simple. Work first with point markings, then quotient by the free product of cyclic shifts to obtain the cycle-marked incidence $\mathcal X_{\mathbf n}^{\circ}$. Let $\mathcal S_{\mathbf n}$ be its $b=0$ fiber, $\mathcal C_{\mathbf n}$ the unique component containing that full scalar locus, and $\rho_i=\operatorname{tr}(DH^{n_i})$.

The exact result is:

1. $\mathcal S_{\mathbf n}$ is nonempty and irreducible, lies in a unique irreducible component $\mathcal C_{\mathbf n}$, and $\mathcal C_{\mathbf n}\to\mathcal B_d$ is étale and dominant. Inside the simple exact disjoint incidence,
   $$
   (\mathcal C_{\mathbf n})_{b=0}=\mathcal S_{\mathbf n}
   $$
   scheme-theoretically.

2. The map
   $$
   \Psi=(-b,\rho_1,\ldots,\rho_r):
   \mathcal C_{\mathbf n}\longrightarrow\mathbf A^1\times\mathbf A^r
   $$
   is étale at a scalar point, dominant, and generically étale. Thus $\rho_1,\ldots,\rho_r$ are algebraically independent over $\mathbf C(b)$.

3. There is a nonempty open $U\subset\mathbf G_m$ such that, for every $b_0\in U$, the whole-fiber trace map $(\mathcal C_{\mathbf n})_{b_0}\to\mathbf A^r$ is dominant. At least one irreducible component of the reduced specialized fiber maps dominantly and generically étale. Specialized-fiber irreducibility is not asserted.

4. At every $s\in\mathcal S_{\mathbf n}$,
   $$
   \widehat{\mathcal O}_{\mathcal C_{\mathbf n},s}
   \simeq\mathbf C[[b,u_0,\ldots,u_{d-2}]],
   \qquad
   \widehat{\mathcal O}_{\mathcal S_{\mathbf n},s}
   \simeq\mathbf C[[u_0,\ldots,u_{d-2}]],
   $$
   and
   $$
   \rho_i(b,u)=\lambda_i(u)+bG_i(b,u).
   $$

5. If
   $$
   \mathcal R_H=V(\operatorname{Fitt}_0\Omega_{\mathcal C_{\mathbf n}/(\mathbf A^1\times\mathbf A^r)})
   $$
   and
   $$
   \mathcal R_{\mathrm{poly}}=V(\operatorname{Fitt}_0\Omega_{\mathcal S_{\mathbf n}/\mathbf A^r}),
   $$
   then
   $$
   \mathcal R_H\times_{\mathcal C_{\mathbf n}}\mathcal S_{\mathbf n}
   =\mathcal R_{\mathrm{poly}}
   $$
   as closed subschemes on the simple scalar locus, and locally
   $$
   J_H\bmod b=\pm J_{\mathrm{poly}}.
   $$
   Multiplicities agree along irreducible components of the boundary ramification scheme. For $d>2$, no closed-point numerical intersection multiplicity is asserted without a proper transverse slice.

## Decisive repairs

| Initial issue | Repair adopted | Why the repair closes the issue |
|---|---|---|
| “An irreducible marked component” was not quantified carefully. | Define the simple exact disjoint incidence and prove there is a unique component containing the entire irreducible scalar locus. | Regularity of an étale scheme makes distinct components disjoint; it does not imply the full incidence is irreducible. |
| Point markings and cycle markings were conflated. | Build the point-marked incidence, prove cyclic-shift freeness on the exact locus, then take the finite étale cycle quotient. | Traces descend, and cyclic multiplicities are accounted for explicitly. |
| Arbitrary periods might have been read as distinct periods. | Allow arbitrary positive $n_i$, including repetitions, while requiring the cycles themselves to be distinct. | This matches the imported arbitrary-period theorem. |
| The headline began at $d\ge3$. | State $d\ge2$ and $r=d-1$. | Gorbovickis Theorem 1.6 and Lemma 2.1, not headline Corollary 1.7, cover the $d=2$, one-cycle case. |
| Total dominance was converted too quickly into a statement for every nonzero $b$. | Use the open image of the total étale locus and obtain an unspecified nonempty $U\subset\mathbf G_m$. | This proves only a general-fiber result and leaves prescribed fibers, including $b=-1$, open. |
| Specialized fibers were treated as if irreducible. | State dominance for the whole fiber and existence of at least one dominant generically étale irreducible component of the reduced fiber. | A finite union of component-image closures covers the target, while no all-component conclusion follows. |
| Fitting base change was phrased globally. | Restrict to the Cartesian simple scalar square and use base change of differentials and Fitting ideals there. | Stacks Tags 07Z6 and 0C3I support the exact scheme restriction, not a nonsimple compactification. |
| “Intersection multiplicity” was pointwise. | Preserve generic multiplicities along irreducible boundary components. | For $d>2$ the boundary intersection is generally positive-dimensional; a point number needs a proper transverse slice. |
| “Multipliers” could mean selected eigenvalue branches. | Use traces and record $\det(DH^{n_i})=(-b)^{n_i}$. | Trace plus determinant gives the unordered eigenvalue pair; it does not choose a regular branch. |
| Global reconstruction was suggested. | Record the residual $\mu_{d-1}$ diagonal conjugacy. | The normal-form trace map is generically noninjective for $d>2$; stabilizers also complicate coarse quotients. |
| The optional loop model risked doing too much. | Prove finite freeness of the full ordered-loop algebra but bar any irreducibility or exact-cycle-count inference. | Monic standard monomials prove rank, not geometry of the deleted exact open. |

## Proof audit

The proof is complete after one imported deep input.

- Direct algebra identifies the scalar fiber and gives
  $$
  DH_{0,p}^n=\begin{bmatrix}\lambda&0\\ *&0\end{bmatrix},
  \qquad
  \det(DH_{0,p}^n-I)=1-\lambda.
  $$
- Gorbovickis supplies irreducibility of the relevant marked-polynomial space and a full-rank arbitrary-period multiplier point.
- The orbit-equation Jacobian proves étaleness of the simple incidence.
- The scalar differential of $\Psi$ is block triangular, so one full-rank point proves total dominance and generic étaleness.
- The étale locus maps openly; its nonempty open image yields the guarded fixed-$b$ statement without assuming fiber irreducibility.
- Formal étaleness gives the completed rings and $\rho_i=\lambda_i+bG_i$; Stacks Tags 02GH and 0257 record the formal-local input.
- The Cartesian scalar square, base change for differentials, and Stacks Tag 07Z6/Lemma 15.8.4 plus scheme-level Tag 0C3I give the exact Fitting restriction.

No unresolved theorem obligation remains inside the frozen scope.

## Collision matrix summary

| Neighbor | Neighbor's scope | Paper18's noncolliding scope |
|---|---|---|
| Gorbovickis, arXiv:1305.0867 | Arbitrary-period polynomial multiplier independence and marked-space irreducibility. | Imported boundary input; Paper18 proves the Hénon transfer and ramification theorem. |
| Gorbovickis--Taflin, arXiv:2411.12856 | Regular polynomial endomorphisms, with principal period restrictions at least $4$. | Nonregular Hénon normal forms, arbitrary positive periods, and a scalar boundary. |
| Huguin, arXiv:2412.19335 | Complete unmarked period-$1$ and period-$2$ polynomial spectra and finite birational recovery. | Selected marked arbitrary-period Hénon traces and local scheme ramification. |
| Cantat--Dujardin, arXiv:2603.09445, v1 submitted 2026-03-10 | Full Hénon multiplier-spectrum rigidity and finite low-period determination. | Exactly $d-1$ selected marked traces and boundary Fitting restriction. |
| Bianchi--He, arXiv:2606.29363, v1 submitted 2026-06-28 | Full marked unstable spectrum, pressure, and path metrics on hyperbolic components. | Finite algebraic trace coordinates and scheme-theoretic degeneration. |
| Friedland--Milnor, ETDS 9 (1989) | Normal forms and a low-degree fixed-point overlap. | Arbitrary periods, all $d\ge2$, and exact boundary ramification. |

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

The review stopped full-incidence irreducibility, every-$b$ coordinates, the prescribed $b=-1$ case, all-component generic étaleness, global injectivity or birationality, naive coarse-quotient completions, global nonsimple Fitting equality, reducedness, transversality, pointwise multiplicity without slicing, eigenvalue-branch coordinates, exact-cycle enumeration by finite-free rank, positive characteristic, multi-factor compositions, and absolute-priority language.

## Manuscript envelope

The final source design authorizes a 23-page paper within a 22--24 page range:

| Material | Pages |
|---|---:|
| Abstract and introduction | 3.5 |
| Marked incidence and cycle quotient | 3.0 |
| Universal loop algebra | 2.0 |
| Scalar component and coordinates | 4.0 |
| Completed local boundary | 3.0 |
| Fitting ramification and multiplicity | 3.5 |
| Fixed-$b$ fibers and quotients | 1.5 |
| Comparison and limitations | 1.0 |
| Appendix details | 1.0 |
| References | 0.5 |
| **Total** | **23.0** |

Figures: **0**. Scientific experiments: **0**. Computational experiments: **0**. Numerical results: **0**.

## Final disposition

**GO FOR SOURCE DESIGN WITH CLAIM FREEZE.** Any expansion to an anti-claim in A1--A20 reopens the theorem and novelty gates.
