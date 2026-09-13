# Novelty Assessment

**Assessment date:** 2026-08-17

**Gate history:** initial verdict **REPAIR**; corrected theorem **GO for source design**

**Proposed title:** *Marked Trace Coordinates and Scheme-Theoretic Ramification at the Polynomial Boundary of Generalized Hénon Maps*

## Executive assessment

The candidate is novel as a focused algebraic-dynamical note, not as a new general multiplier-rigidity theory. Its defensible contribution is the exact bridge between two established but previously separate settings:

1. Gorbovickis's arbitrary-period multiplier coordinates on marked polynomial spaces; and
2. current Hénon multiplier-rigidity work based on full or complete low-period spectra.

The bridge has two parts that must remain coupled:

- any prescribed $d-1$ pairwise-disjoint simple exact marked cycles give generic trace coordinates, together with the Jacobian parameter, on the Hénon component issuing from $b=0$;
- the critical Fitting scheme of this coordinate map restricts scheme-theoretically, with multiplicity, to the polynomial multiplier critical scheme at the scalar boundary.

The first part alone is a concise deformation argument once Gorbovickis is imported. The second part, together with the exact incidence/component bookkeeping, raises the package to standalone-note level.

## Contribution decomposition

### N1. Arbitrary-selection marked trace coordinates for Hénon normal forms

For every positive period vector $\mathbf n=(n_1,\ldots,n_{d-1})$, the selected traces and $-b$ form a dominant generically étale map on the unique simple marked component containing the polynomial boundary.

What is new:

- the periods are arbitrary, including $1$, $2$, repetitions, and mixed periods;
- the cycles are an arbitrary labelled disjoint selection, not the complete spectrum at one or more periods;
- the theorem uses exactly $d-1$ marked traces plus the Jacobian parameter;
- algebraic independence is over $\mathbf C(b)$;
- the statement is attached to a rigorously identified marked component.

What is inherited:

- full-rank variation of the polynomial multipliers;
- irreducibility of the polynomial marked incidence.

### N2. Exact scalar-boundary ramification restriction

On the simple scalar locus,
$$
\mathcal R_H\times_{\mathcal C_{\mathbf n}}\mathcal S_{\mathbf n}
=\mathcal R_{\mathrm{poly}}
$$
as schemes. Equivalently,
$$
J_H\equiv\pm J_{\mathrm{poly}}\pmod b.
$$

What is new:

- the comparison is scheme-theoretic rather than set-theoretic;
- it retains multiplicities along boundary components;
- it is valid at every simple scalar marked tuple, not only the full-rank test point;
- it separates exactly what base change proves from reducedness, transversality, and isolated-intersection claims that it does not prove.

### N3. Finite-free cyclic-loop algebra

The full ordered $n$-loop algebra is finite free of rank $d^n$ over the extended parameter base, with an explicit standard-monomial basis. This is a useful structural lemma and makes the finiteness of the full marked fixed-point incidence transparent.

Novelty weight: supporting, not headline. The argument is elementary commutative algebra. It must not be advertised as an irreducibility theorem or as a count of exact cycles.

## Primary-source collision matrix

| Source | Strongest overlapping result | Direct collision? | Separation that must appear in the paper |
|---|---|---:|---|
| Gorbovickis, arXiv:1305.0867 | Arbitrary-period algebraic independence for up to $d-1$ marked polynomial cycles; irreducible marked polynomial space. | **Input-level collision** | Credit as the deep boundary input. New work starts with the extended Hénon incidence, the scalar lift, block trace differential, fixed-$b$ spreading, and Fitting restriction. |
| Gorbovickis--Taflin, arXiv:2411.12856 | Maximal collections of eigenvalue functions give local coordinates for regular polynomial endomorphisms; marked-incidence irreducibility. | No | Generalized Hénon maps are not regular projective endomorphisms; Paper18 allows arbitrary periods and studies the singular $b=0$ boundary and traces. |
| Huguin, arXiv:2412.19335 | Complete unmarked period-$1$ and period-$2$ polynomial spectra define a finite birational morphism. | No | Paper18 uses an arbitrary selected marked set at arbitrary periods and proves a local Hénon theorem, not global polynomial recovery. |
| Cantat--Dujardin, arXiv:2603.09445 | Full trace spectrum gives finite Hénon rigidity; finitely many complete trace multisets suffice; complete periods $1,2$ plus Jacobian give strong determination away from Jacobian $-1$. | **Closest Hénon neighbor** | Their data are full/complete spectra and their goal is global rigidity. Paper18 proves arbitrary-selection local coordinates and an exact degeneration/ramification theorem. |
| Bianchi--He, arXiv:2606.29363 | Full marked unstable multiplier spectrum controls a thermodynamic path metric on hyperbolic components. | No | Analytic full-spectrum covariance is distinct from finite algebraic coordinates and scheme-theoretic boundary base change. |
| Friedland--Milnor, ETDS 9 (1989) | Generalized Hénon normal forms and strong fixed-point trace control in the quadratic/cubic rigidity analysis. | Partial at $d=2,3$, all periods $1$ | Acknowledge the low-degree fixed-point overlap; Paper18's arbitrary periods, general degree, selected marked data, and boundary ramification remain separate. |

## Residual quotient and novelty restraint

The monic-centered normal form has a residual action
$$
p(z)\mapsto\beta^{-1}p(\beta z),
\qquad \beta^{d-1}=1.
$$
Diagonal conjugacy transports the marked cycles and leaves $b$ and every trace unchanged. Thus the coordinate map is generically étale but is not generically injective on the normal-form cover when $d>2$.

This is not a defect in N1: étale local coordinates permit a finite global deck ambiguity. It does rule out “generic reconstruction on the monic-centered cover” as a novelty claim. Any moduli-level birational statement would require a separate quotient and degree analysis.

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

## Stopped candidate claims

The following stronger candidates were considered and stopped before source design.

| Candidate | Stop reason | Frozen replacement |
|---|---|---|
| S1. The full marked Hénon incidence is irreducible. | The finite-free algebra can have several components; the scalar argument controls only one. | Unique component containing the full simple scalar locus. |
| S2. Every arbitrary nonzero $b$ has marked trace coordinates. | Total dominance only spreads outside a proper closed subset of the $b$-line. | Nonempty open $U\subset\mathbf G_m$. |
| S3. The theorem applies in particular at $b=-1$. | The exceptional set is not computed. | No prescribed-fiber conclusion. |
| S4. Every component of a general fixed-$b$ fiber is generically étale. | Specialized fibers may be reducible, and the proof forces only a dominating component. | Whole fiber dominant; at least one component of the reduced fiber dominant and generically étale. |
| S5. The marked trace map is generically injective or birational. | Residual $\mu_{d-1}$ orbits remain in fibers; point markings add cyclic shifts. | Dominant and generically étale only. |
| S6. The coarse moduli quotient has the same completed local rings everywhere. | Root-of-unity stabilizers can produce quotient singularities. | Work on the normal-form cover; mention a stack/stabilizer-free option. |
| S7. The global compactified critical scheme has exact polynomial restriction. | Nonsimple points can have singular, embedded, or component-multiplicity issues. | Exact equality on the simple scalar locus and its completions. |
| S8. The ramification divisors are reduced. | Fitting base change does not imply radicality. | Preserve the full possibly nonreduced scheme. |
| S9. The ramification divisors meet transversely. | The determinant congruence does not control first-order normal crossing. | No transversality claim. |
| S10. Every scalar point has a numerical boundary intersection multiplicity. | For $d>2$ the intersection generally has dimension $d-2$. | Multiplicity along generic points of components; optional transverse slices left outside the theorem. |
| S11. Individual two-dimensional multipliers are coordinates. | Eigenvalue branches meet at the discriminant. | Trace plus known determinant $(-b)^{n_i}$ determines the unordered pair. |
| S12. The finite-free rank $d^n$ counts exact cycles. | It counts the full $H^n$ fixed-point scheme, including lower periods. | Call it the full ordered-loop rank. |
| S13. Gorbovickis--Taflin already proves the Hénon theorem. | Their parameter spaces are regular endomorphisms, not Hénon automorphisms. | Use only as comparison. |
| S14. Cantat--Dujardin full rigidity implies the selected finite-coordinate theorem. | Full-spectrum finite rigidity does not identify arbitrary selected coordinate subfamilies. | Prove N1 from the scalar boundary. |
| S15. Huguin's birationality transfers to the Hénon family. | Complete unmarked small-period data and arbitrary marked data are different morphisms. | Use Huguin only in the collision discussion. |
| S16. Computation can verify the ramification equality globally. | No computation can replace missing scheme/component hypotheses, and this project authorizes zero science. | Direct local algebraic proof only. |

## Novelty risk analysis

### Risk 1: “This is immediate by openness.”

Response: the dominance implication is short, but the article's substance is the exact marked incidence, all-period/disjoint-cycle quantifiers, the full scalar component, the safe reducible-fiber specialization, and the scheme-theoretic Fitting restriction with multiplicities. These cannot be compressed to an unqualified openness sentence.

### Risk 2: proximity to Cantat--Dujardin

Response: state their theorem on page 2 and contrast the data structures precisely. Full unmarked spectra answer a global finite-rigidity question. A selected labelled set of exactly $d-1$ arbitrary cycles answers a local coordinate question. The scalar-boundary ramification theorem has no counterpart there.

### Risk 3: overreliance on Gorbovickis

Response: advertise Paper18 as a transfer-and-boundary theorem, not a new proof of polynomial independence. Include a self-contained statement of the imported theorem and verify every hypothesis. Do not reproduce Gorbovickis's long combinatorial construction.

### Risk 4: title overstates “exact ramification”

Response: use “scheme-theoretic ramification at the polynomial boundary,” which names the proved equality and localizes its scope. Put “on the simple marked locus” in the abstract theorem sentence.

## Standalone architecture test

The result supports a 22--24 page note if the page budget remains proof-driven:

- 3.5 pages for motivation and exact relation to the six primary neighboring works;
- 5 pages for marked incidences and the finite-free loop model;
- 4 pages for the scalar component and coordinate theorem;
- 6.5 pages for completed local rings, Fitting base change, and multiplicities;
- 2.5 pages for safe fixed-$b$ spreading, residual quotients, limitations, and references;
- 1.5 pages of appendix-level edge cases as needed.

Target: 23 pages, 0 figures, 0 computational experiments, 0 tables of numerical results.

## Scores

Scores apply to the frozen repaired theorem.

| Dimension | Score | Threshold | Decision rationale |
|---|---:|---:|---|
| Novelty | **8.0/10** | 7.5 | New arbitrary-selection Hénon coordinate transfer plus exact boundary ramification; close input and neighboring rigidity work keep the score below 9. |
| Standalone value | **7.7/10** | 7.5 | Passes only when N1 and N2 are both central and the component/fiber guards are fully proved. |
| Proof readiness | **9.3/10** | 9.0 | All obligations reduce to a verified imported theorem and direct algebraic geometry; no missing research lemma remains. |

## Final novelty verdict

**GO FOR SOURCE DESIGN, WITH CLAIM FREEZE.**

The manuscript must remain a precise local-coordinate and boundary-ramification paper. Any attempt to add global injectivity, all-$b$ specialization, full-incidence irreducibility, or nonsimple compactified ramification would reopen the gate and currently receive **STOP**.
