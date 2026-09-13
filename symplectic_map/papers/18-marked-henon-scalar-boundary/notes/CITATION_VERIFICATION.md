# Citation Verification

**Verification date:** 2026-08-17

**Policy:** collision-sensitive claims use primary papers or official foundational documentation. Search-result snippets, secondary surveys, and later paraphrases are not evidence. No source is cited for a theorem stronger than the exact role recorded below.

## V1. Gorbovickis: arbitrary-period polynomial multipliers

**Key:** `Gor13`

**Primary record:** Igors Gorbovickis, “Algebraic independence of multipliers of periodic orbits in the space of polynomial maps of one variable,” arXiv:1305.0867v1, 2013.

**URL:** https://arxiv.org/abs/1305.0867

**Verified internal locations:**

- Definition 1.3 and Remark 1.4 define the irreducible marked algebraic set $M^d_{\mathbf n}$.
- Lemma 1.5 states that this set is independent of the initial polynomial and marked periodic points.
- Theorem 1.6 is stated for polynomial degree $d\ge2$, any number $k\le d-1$ of marked cycles, every positive period vector, and every selected $k$-tuple of coefficient directions. The relevant multiplier Jacobian determinant is not identically zero, so a full-rank point exists; no nonemptiness of its zero scheme is imported.
- Lemma 2.1 constructs, for $p_0(z)=z^d$, periodic points of the prescribed periods at which the chosen multiplier minor is nonzero.
- The proof of Theorem 1.6 notes that nondegeneracy forces the selected points to lie on distinct periodic orbits.
- Corollary 1.7 is phrased for $d\ge3$ because it highlights $d-1$ algebraically independent multipliers; it does not negate the $d=2$, $k=1$ case of Theorem 1.6.

**Role in Paper18:** This is the only imported deep theorem in the proof. It supplies:

1. irreducibility of the arbitrary-period simple exact disjoint polynomial marked locus;
2. a scalar point at which the full $(d-1)\times(d-1)$ polynomial multiplier Jacobian is nonzero;
3. validity for repeated prescribed periods, provided the cycles themselves are distinct.

**Hypothesis check:** At a nonzero exact $n$-periodic point of $z^d$, the multiplier is $d^n\ne1$, so the test cycles are simple. The candidate uses $k=d-1$, which is within the theorem. All periods are positive and arbitrary.

**Does not support:** any Hénon statement for $b\ne0$, any global injectivity statement, or any Fitting-scheme identity. Those are proved directly.

**Verification status:** **VERIFIED**.

## V2. Gorbovickis--Taflin: several-variable comparison

**Key:** `GT24`

**Primary record:** Igors Gorbovickis and Johan Taflin, “Independence of multipliers in several variables complex dynamics,” arXiv:2411.12856v2, 2025 source version.

**URL:** https://arxiv.org/abs/2411.12856

**Verified internal locations:**

- Theorem 1.1 concerns regular polynomial endomorphisms of $\mathbf C^n$ and algebraic independence of the maximal number of eigenvalue functions attached to distinct cycles of periods at least $4$.
- Theorem 1.7 gives irreducibility of marked-periodic-point varieties over the regular polynomial endomorphism space for $n,d\ge2$.
- The introduction explicitly recalls that in one variable the period restriction is absent, citing Gorbovickis's earlier work.

**Role in Paper18:** nearest higher-dimensional local-coordinate and marked-incidence comparison.

**Does not support or subsume:** the family $H_{b,p}$. A generalized Hénon automorphism has indeterminacy in its projective extension and is not a regular polynomial endomorphism of $\mathbf P^2$. GT24 also does not study the singular degeneration $b=0$, Hénon trace functions, or boundary Fitting schemes.

**Required positioning:** acknowledge that “multipliers as local coordinates on marked higher-dimensional dynamical spaces” is not a new narrative; identify the arbitrary-period Hénon boundary-transfer and exact ramification base change as the new content.

**Verification status:** **VERIFIED**.

## V3. Huguin: complete small-cycle polynomial spectra

**Key:** `Hug24`

**Primary record:** Valentin Huguin, “Moduli spaces of polynomial maps and multipliers at small cycles,” arXiv:2412.19335v1, 2024.

**URL:** https://arxiv.org/abs/2412.19335

**Verified internal locations:**

- The Main Theorem states that the multiplier-spectrum morphism using all cycles of periods $1$ and $2$ is finite and birational onto its image on degree-$d$ polynomial moduli.
- For $d\in\{2,3\}$, the complete fixed-point multiplier morphism is an isomorphism onto its image.
- The morphisms are unmarked symmetric-spectrum morphisms on affine conjugacy classes.

**Role in Paper18:** global polynomial-spectrum comparison and an ingredient used by Cantat--Dujardin in their low-period Hénon argument.

**Does not support or subsume:** an arbitrary selected set of $d-1$ marked cycles, arbitrary prescribed periods, the Hénon automorphism parameter $b$, or the scalar-boundary ramification scheme.

**Verification status:** **VERIFIED**.

## V4. Cantat--Dujardin: Hénon multiplier rigidity

**Key:** `CD26`

**Primary record:** Serge Cantat and Romain Dujardin, “Multiplier rigidity for complex Hénon maps,” arXiv:2603.09445v1, submitted 2026-03-10.

**URL:** https://arxiv.org/abs/2603.09445

**Verified internal locations:**

- Theorem A states finite determination of a complex Hénon map by its full trace spectrum, and likewise by its unstable multiplier spectrum.
- Section 3.2 defines regular trace functions on periodic-point incidence spaces and packages complete period-$n$ trace multisets.
- Theorem 3.7 gives integers $P,N$ so that equality of all complete trace multisets through period $P$ leaves at most $N$ Hénon maps.
- Theorem 4.2 states finite determination, and generic uniqueness up to conjugacy, from the Jacobian and the complete period-$1$ and period-$2$ data when the Jacobian is not $-1$.
- Section 5.2 records the quotient of monic centered polynomials by the $(d-1)$st roots of unity.
- The discussion of Hénon normal forms records the residual diagonal root-of-unity ambiguity.

**Role in Paper18:** closest Hénon-spectrum collision; source for the state of global rigidity and for contextual definitions of trace spectrum.

**Does not support or subsume:** that any arbitrarily prescribed $d-1$ marked cycles give local coordinates; the exact-period component through $b=0$; algebraic independence over $\mathbf C(b)$ of the selected traces; or scheme-theoretic restriction of a critical Fitting scheme.

**Required positioning:** Paper18 is a finite *marked arbitrary-selection local-coordinate* theorem with an exact degeneration statement, not a stronger global rigidity theorem. It neither improves CD26's full-spectrum reconstruction nor identifies the exceptional fixed-$b$ set.

**Verification status:** **VERIFIED**.

## V5. Bianchi--He: marked unstable spectrum on hyperbolic components

**Key:** `BH26`

**Primary record:** Fabrizio Bianchi and Yan Mary He, “A thermodynamic path metric for complex Hénon maps,” arXiv:2606.29363v1, submitted 2026-06-28.

**URL:** https://arxiv.org/abs/2606.29363

**Verified scope:** The paper constructs a Hermitian covariance form on hyperbolic components from the full complex unstable derivative cocycle. It interprets the form through infinitesimal variation of the marked unstable multiplier spectrum and uses Cantat--Dujardin rigidity to prove a path metric.

**Role in Paper18:** current analytic comparison for “marked multipliers vary infinitesimally in Hénon parameter spaces.”

**Does not support or subsume:** algebraic independence of a finite arbitrary-period selected set, incidence-component irreducibility, degeneration to $b=0$, or critical-scheme base change.

**Verification status:** **VERIFIED**.

## V6. Friedland--Milnor: normal forms and low-degree overlap

**Key:** `FM89`

**Primary record:** Shmuel Friedland and John Milnor, “Dynamical properties of plane polynomial automorphisms,” *Ergodic Theory and Dynamical Systems* 9 (1989), 67--99.

**DOI:** https://doi.org/10.1017/S014338570000482X

**Verified internal locations:**

- The paper develops generalized Hénon normal forms for polynomial automorphisms.
- Theorem 7.1 treats analytic-conjugacy rigidity when there are two or three isolated fixed points counted with multiplicity.
- The proof computes, for a normalized Hénon map, that the determinant at a fixed point is the constant Jacobian and the trace is $p'(x)$; this yields particularly strong fixed-point control in degrees $2$ and $3$.

**Role in Paper18:** foundational normal-form citation and required acknowledgement of the $d=2,3$, period-$1$ special overlap.

**Does not support or subsume:** arbitrary periods, arbitrary selections in all degrees, the $b=0$ marked component, or scheme-theoretic ramification restriction.

**Verification status:** **VERIFIED**.

## V7. Stacks Project: Fitting base change

**Key:** `StacksFitt`

**Official records:**

- Tag 07Z6, Lemma 15.8.4: https://stacks.math.columbia.edu/tag/07Z6
- Tag 0C3I: https://stacks.math.columbia.edu/tag/0C3I

**Verified role:**

- Tag 07Z6 supports formation and base-change behavior of Fitting ideals for finitely presented modules.
- Tag 0C3I supports the associated scheme-level Fitting construction.

**Use in Paper18:** after the Cartesian identification of the scalar fiber and the base-change isomorphism for relative differentials, these tags justify
$$
\operatorname{Fitt}_0(\Omega_{\mathcal C/T})\mathcal O_{\mathcal S}
=\operatorname{Fitt}_0(\Omega_{\mathcal S/T_0}).
$$

**Guard:** the paper also gives the local determinant proof $J_H\bmod b=\pm J_{\mathrm{poly}}$, so no stronger global compactification claim is hidden in the citation.

**Verification status:** **VERIFIED**.

## V8. Stacks Project: étale formal-local behavior

**Key:** `StacksEtale`

**Official records:**

- Tag 02GH: https://stacks.math.columbia.edu/tag/02GH
- Tag 0257: https://stacks.math.columbia.edu/tag/0257

**Verified role:** formal-local and completed-local behavior of étale morphisms used to identify
$$
\widehat{\mathcal O}_{\mathcal C,s}
\simeq
\widehat{\mathcal O}_{\mathcal B,\pi(s)}
$$
when the residue fields are both $\mathbf C$.

**Guard:** these tags do not assert irreducibility of the incidence. Irreducibility comes from Gorbovickis on the scalar locus plus regular-component separation.

**Verification status:** **VERIFIED**.

## Citation-to-claim map

| Citation | Imported theorem used in proof? | Comparison only? | Paper18 claim IDs |
|---|---:|---:|---|
| Gor13 | Yes | Yes | C11, C12, C13, C17, C28 |
| GT24 | No | Yes | P2 |
| Hug24 | No | Yes | P3 |
| CD26 | No | Yes | P4, residual-quotient context |
| BH26 | No | Yes | P5 |
| FM89 | No | Yes/foundational | P6, low-degree context |
| StacksFitt | Foundational | No | C24--C26 |
| StacksEtale | Foundational | No | C22--C23 |

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

## Rejected citation inferences

The following inferences are explicitly disallowed:

1. GT24 regular-endomorphism independence $\Rightarrow$ Hénon independence.
2. CD26 full-spectrum rigidity $\Rightarrow$ arbitrary selected finite traces are coordinates.
3. Huguin's unmarked small-cycle birationality $\Rightarrow$ marked arbitrary-period Hénon birationality.
4. Bianchi--He path-metric nondegeneracy $\Rightarrow$ algebraic independence of a chosen finite trace set.
5. Finite normal-form ambiguity $\Rightarrow$ injectivity after quotient without stabilizer analysis.
6. Fitting base change on the simple Cartesian square $\Rightarrow$ a global equality on a nonsimple compactification.
7. Gorbovickis Corollary 1.7's $d\ge3$ wording $\Rightarrow$ failure of the $d=2$, $k=1$ case already covered by Theorem 1.6.

## Bibliographic stop rule

The collision search is bounded through 2026-08-17. The six dynamics papers above and the exact Stacks supports are sufficient for source design. No additional citation is to be added from a search snippet or secondary description. A later paper may be added only after its primary text is checked against a specific claim in the matrix.
