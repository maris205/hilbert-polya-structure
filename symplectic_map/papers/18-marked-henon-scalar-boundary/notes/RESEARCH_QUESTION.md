# Research Question

**Working title:** *Marked Trace Coordinates and Scheme-Theoretic Ramification at the Polynomial Boundary of Generalized Hénon Maps*

**Source-design status:** frozen after independent theorem and novelty gate

**Date:** 2026-08-17

## One-sentence question

For a monic centered degree-$d$ polynomial $p$ and the extended generalized Hénon family
$$
H_{b,p}(x,y)=(p(x)+by,x),
$$
does an arbitrary prescribed collection of $d-1$ pairwise-disjoint simple exact-period marked cycles give, together with the Jacobian parameter $-b$, generic algebraic local coordinates, and does the critical scheme of this coordinate map restrict exactly to the polynomial multiplier critical scheme at the degenerate boundary $b=0$?

## Parameter space and conventions

Work over $\mathbf C$. For $d\ge 2$, write
$$
\mathcal P_d^{\mathrm{cm}}
=\left\{p(z)=z^d+\sum_{j=0}^{d-2}a_jz^j\right\}
\simeq\mathbf A^{d-1}
$$
and
$$
\mathcal B_d=\mathbf A^1_b\times\mathcal P_d^{\mathrm{cm}}.
$$
The determinant of $DH_{b,p}$ is $-b$. Thus $b\ne0$ is the automorphism locus and $b=0$ is the polynomial, or scalar, boundary. The boundary map is not an automorphism; it is retained as an algebraic degeneration needed for the proof.

Fix
$$
r=d-1,
\qquad
\mathbf n=(n_1,\ldots,n_r)\in\mathbf Z_{>0}^{r}.
$$
A marked cycle is labelled by its index $i$, but no point on the cycle is preferred. The construction is made first on the point-marked cover and then divided by the free cyclic shift action $\prod_i\mathbf Z/n_i\mathbf Z$. The words *exact*, *disjoint*, and *simple* have the following fixed meanings:

- exact means minimal period exactly $n_i$;
- disjoint means the underlying finite orbits are pairwise disjoint, including when some $n_i$ coincide;
- simple means $\det(DH_{b,p}^{n_i}-I)\ne0$ at the marked point.

These are open conditions inside the full fixed-point incidence.

## Primary research questions

### RQ1. Exact marked component

Is the simple exact disjoint polynomial marked locus at $b=0$ irreducible, and is it contained in one unique irreducible component of the extended Hénon marked incidence?

The desired answer is yes. Irreducibility is imported precisely from Gorbovickis's arbitrary-period marked polynomial space. Uniqueness of the total component is a local consequence of the étaleness of the incidence over $\mathcal B_d$ at every simple tuple. No irreducibility of the unrelated full Hénon incidence is sought.

### RQ2. Arbitrary-period trace coordinates

For
$$
\rho_i=\operatorname{tr}(D H_{b,p}^{n_i}),
\qquad
\Psi=(-b,\rho_1,\ldots,\rho_r),
$$
is $\Psi$ dominant and generically étale on that component for every positive period vector $\mathbf n$?

The desired answer is yes. At $b=0$, the trace equals the one-variable polynomial multiplier. Gorbovickis supplies a scalar tuple where the polynomial multiplier Jacobian has full rank. The first row of $D\Psi$ is $(-1,0,\ldots,0)$, so the total differential is block triangular and has full rank at the same tuple.

### RQ3. Algebraic independence over the Jacobian field

Do the traces satisfy
$$
\operatorname{trdeg}_{\mathbf C(b)}
\mathbf C(b)(\rho_1,\ldots,\rho_r)=r?
$$

The desired answer is yes, as the function-field form of dominance of $\Psi$.

### RQ4. General fixed-$b$ fibers

What can be said after fixing a nonzero complex number $b_0$?

The safe target is:

- there is a nonempty Zariski-open $U\subset\mathbf G_m$ such that the trace map on the whole fiber over every $b_0\in U$ is dominant;
- for each such $b_0$, at least one irreducible component of the reduced fiber maps dominantly and generically étale to $\mathbf A^r$.

No irreducibility of the specialized fiber is assumed. No assertion is made for every $b_0\ne0$, or for a prescribed value such as $b_0=-1$.

### RQ5. Completed local boundary

At every simple scalar tuple, is the completed marked Hénon incidence just the completed parameter base, and do the trace germs have the form
$$
\rho_i(b,u)=\lambda_i(u)+bG_i(b,u),
$$
where $\lambda_i$ is the polynomial multiplier germ?

The desired answer is yes. It follows from formal étaleness of the marked incidence and the identity $\rho_i|_{b=0}=\lambda_i$.

### RQ6. Scheme-theoretic critical restriction

If the Hénon and polynomial critical schemes are defined by zeroth Fitting ideals of relative Kähler differentials, is
$$
\mathcal R_H\times_{\mathcal C_{\mathbf n}}\mathcal S_{\mathbf n}
=\mathcal R_{\mathrm{poly}}
$$
an equality of schemes on the simple scalar locus?

The desired answer is yes. The boundary square is Cartesian there, relative differentials commute with this base change, and Fitting ideals commute with base change. In local Jacobian coordinates this is the congruence
$$
J_H\equiv\pm J_{\mathrm{poly}}\pmod b.
$$
This preserves multiplicities along boundary components. When $d>2$, it does not create a pointwise numerical intersection multiplicity at an arbitrary closed point because the intersection is generally positive-dimensional.

## Auxiliary finite-free question

For one ordered $n$-cycle, introduce cyclic scalar coordinates $x_j$ with indices in $\mathbf Z/n\mathbf Z$ and equations
$$
x_{j+1}-p(x_j)-b x_{j-1}=0.
$$
Over
$$
R=\mathbf C[b,a_0,\ldots,a_{d-2}],
$$
the normalized equations have pairwise-coprime leading monomials $x_j^d$ for a graded monomial order in the $x$-variables. The universal ordered-loop algebra is therefore finite free over $R$, with basis
$$
\left\{\prod_{j=0}^{n-1}x_j^{e_j}:0\le e_j<d\right\}
$$
and rank $d^n$. This remains valid for $n=1$ and $n=2$, where cyclic indices coincide. Tensoring the algebras for the $r$ markings gives rank $d^{\sum_i n_i}$.

This lemma controls finiteness and fiber length of the **full** ordered fixed-point incidence. It is not an irreducibility theorem, does not separate exact from lower periods, does not remove collisions, and does not say that the simple exact open remains finite after points are deleted.

## Scope and anti-claims

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

The residual action
$$
p(z)\longmapsto\beta^{-1}p(\beta z),
\qquad \beta^{d-1}=1,
$$
comes from diagonal conjugacy and preserves $b$ and every trace. Generic global injectivity on the monic-centered normal-form cover is therefore impossible. Point markings would add the cyclic-shift ambiguity; cycle markings remove only that latter ambiguity.

## Degree range

The theorem should be stated for $d\ge2$. Gorbovickis's Theorem 1.6 applies to $k\le d-1$ for every $d\ge2$ and every positive period vector. The frequent $d\ge3$ formulation only highlights the nontrivial collection of $d-1$ multipliers. The quadratic case is a valid one-cycle specialization and should not be omitted without a reason.

## Planned article architecture

Target length: **23 pages**, acceptable range **22--24 pages**. Target number of figures: **0**. Target experimental or computational sections: **0**.

| Section | Target pages | Content |
|---|---:|---|
| Abstract and introduction | 3.5 | Result, mechanism, relation to rigidity literature, anti-claims |
| Marked incidence and exact-cycle quotients | 3.0 | Point markings, cycle quotient, simple/exact/disjoint opens |
| Universal cyclic-loop algebra | 2.0 | Finite-free lemma and its strict limitations |
| Scalar component and coordinate theorem | 4.0 | Boundary identification, Gorbovickis input, block differential |
| Completed local boundary | 3.0 | Formal coordinates and trace expansion |
| Fitting ramification and multiplicities | 3.5 | Cartesian base change, determinant congruence, component multiplicity |
| General nonzero fibers and finite quotients | 1.5 | Safe spreading statement, $\mu_{d-1}$ action |
| Comparison, limitations, and outlook | 1.0 | Exact novelty boundary; no stronger claims |
| Appendix-level algebra details | 1.0 | Monic Gröbner argument and edge cases $n=1,2$ |
| References | 0.5 | Primary sources only for collision-sensitive claims |
| **Total** | **23.0** | **0 figures; zero science** |

## Deliverable criterion

The source design is complete only if the exact theorem, every quantifier guard, the full proof dependency chain, the finite-free lemma's limitations, the primary-source collision matrix, and the zero-science architecture agree across all ten design files. No paper source, independent review, code, results, figures, or assets belongs to this stage.
