criteria_binding_unavailable
contract_role: domain
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: warn
trigger: "bounded, repairable inaccuracies or omissions weaken domain precision or literature representation without invalidating a central conclusion"

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

The central domain claims are mathematically coherent within their stated finite boundary. The level-11 form and time change, cycle-owned Hecke relation, genus-one scalar control, degree/root/repetition separation, all-parameter quadratic-moment criterion, and exact rational-homology taxonomy agree with the supplied theorem records and audits. The only domain weakness found is a repairable gap in current-literature positioning; it does not alter the proofs or the finite verdicts.

No target venue or criteria authority was supplied. Accordingly, `criteria_binding_unavailable` applies, and this card makes no venue-alignment or submission-readiness claim.

### S1: The level-11 setup and period-owner laws are correctly scoped

**Evidence Anchor**: equation: manuscript.tex, Proposition \(\ref{prop:owner}\), the three identities for conjugacy, inversion, and traversal powers

**Confidence**: 5/5 — direct verification from the stated weight-two transformation law and one-form integration

**Rationale**: The normalization \(f=\eta(z)^2\eta(11z)^2\), \(a_1=1\), and the one-dimensional rational newspace are consistent with the cited official LMFDB record. Pulling \(\alpha_f=\operatorname{Re}(2\pi i f(z)\,dz)\) to the unit tangent bundle gives a bounded clock perturbation at the cusp, and the manuscript correctly derives conjugacy invariance, orientation sign change, and linear scaling under traversal repetition without identifying these operations with one another.

### S2: The Hecke eigenperiod law is correctly cycle-owned and explicitly non-discriminative

**Evidence Anchor**: equation: manuscript.tex, Theorem \(\ref{thm:hecke}\), \(\int_{T_{p,*}C}\omega_f=a_p\int_C\omega_f\)

**Confidence**: 5/5 — the normalization and branch-gluing proof can be checked line by line

**Rationale**: For the declared left-coset representatives, \(\sum_\beta\beta^*\omega_f\) gives the stated weight-two \(T_p\) normalization. Iterating \(\beta_jM=\gamma_j\beta_{\pi(j)}\) around a permutation cycle yields the closed owner \(\delta_O=\beta_jM^{d_O}\beta_j^{-1}\in\Gamma_0(11)\), so the left side is a sum of owned closed cycles rather than a one-orbit image. The genus-one control is also correct: \(H^1(X_0(11),\mathbb R)\) is spanned by the real and imaginary parts of the unique holomorphic differential, and real \(a_p\) acts by the same scalar on both. The manuscript therefore properly treats the linear law as non-discriminative evidence for a primitive Euler mechanism.

### S3: Branch degree, primitive-root exponent, and zeta repetition remain distinct

**Evidence Anchor**: text: manuscript.tex, subsection “Three indices that must remain distinct,” “Thus d_O>1 can coexist with a primitive output owner”

**Confidence**: 5/5 — the geometric length relation and finite root-certificate boundary are both explicit

**Rationale**: The branch-cycle degree \(d_O\) records return to a correspondence sheet and gives length \(d_O\ell(M)\); it is not a power relation inside \(\Gamma_0(11)\). The separate exact root search certifies exponent one for every registered output, while the logarithmic-product index \(r\) is introduced only after selecting a primitive owner. The manuscript also correctly retains output multiplicity because cross-instance conjugacy canonicalization has not been performed. Thus the object is a finite owner multiset, not a global primitive-conjugacy census.

### S4: The quadratic moment criterion follows from the all-parameter identity

**Evidence Anchor**: equation: manuscript.tex, Theorem \(\ref{thm:moment}\), \(Q_1(M,p)=\lambda_pI(M)^2\) and \(Q_d(M,p)=0\) for \(d>1\)

**Confidence**: 5/5 — the divisor-coefficient calculation and Möbius inversion are exact

**Rationale**: Writing \(q=e^{-sL(M)}\), the Ruelle output coefficient is \(n\sum_{d\mid n}Q_d/d\). Equality for every sufficiently large \(s\) fixes all power-series coefficients, and Möbius inversion gives exactly the displayed degree-one and nonunit-degree obligations. In the frozen-stability kernel the factor \((1-e^{-nL})^{-1}\) is common and nonzero for every divisor contribution at coefficient \(q^n\), so the same inversion applies. The manuscript correctly concludes that the signed linear Hecke sum cannot determine nonnegative degree-wise sums of squares.

### S5: Exact homology supports the stated instance and group taxonomies

**Evidence Anchor**: table: manuscript.tex, Table \(\ref{tab:instances}\), “All” row with 2 full kernels, 2 projection-only kernels, 134 true nonkernels, and 138 total instances

**Confidence**: 5/5 — the rational coordinate theorem, locked counts, and supplied replay audits agree

**Rationale**: The involution \(\tau(x,y,z)=(-x,y+z,-z)\) gives the exact real-period coordinate \(k=2y+z\), so kernel decisions and normalized quadratic moments use rational equalities rather than tolerance tests. The two compact-zero and two anti-invariant \(p=5\) instances are correctly distinguished. The manuscript also keeps the denominators separate: 138 correspondence components support the instance taxonomy, whereas 55 source/prime groups support each scalar-law verdict. Thus \(a_p\) and \(a_p^2\) each fail 51 of 55 groups, while \(a_p^2-p\) fails all 55, without promoting four kernel survivors into arithmetic validation.

### S6: The finite novelty and route boundaries are preserved

**Evidence Anchor**: text: manuscript.tex, Section “Limitations and open obligations,” “The taxonomy is complete only for the frozen output multiset.”

**Confidence**: 5/5 — the same boundary is repeated consistently across the manuscript and supplied theorem notes

**Rationale**: The claims remain confined to the frozen 138-instance/55-group multiset and do not assert global conjugacy deduplication, a complete primitive census, a global determinant, analytic continuation, prime-to-orbit matching, or a quantum realization. The required status is retained exactly as `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` with `ROUTE_A_EXPLORATORY`, and Route B remains unauthorized and absent.

### W1: The five-source frame omits a directly adjacent current geodesic-period literature strand

**Severity**: Minor

**Evidence Anchor**: absence: manuscript.tex Related work and references.bib — expected a verified nearest-neighbor comparison for modern closed-geodesic-period results and the claimed finite owner-obstruction contribution; checked the five cited entries, Related work, and supplied Stage-2/2.5 citation audits

**Confidence**: 4/5 — a bounded primary-source search found a directly adjacent 2025 paper, but the search was not systematic

**Rationale**: The five cited sources accurately support the level-11 record, modular-symbol/Hecke background, and primitive-orbit product conventions, and the manuscript appropriately avoids a broad priority claim. They do not, however, locate the work within modern research on periods over primitive closed geodesics. Constantinescu and Nordentoft, [“Non-vanishing of Geodesic Periods of Automorphic Forms”](https://doi.org/10.1007/s00039-025-00715-z) (2025), directly treats primitive oriented closed geodesics and includes holomorphic forms on finite-covolume Fuchsian groups with a cusp. That paper does not by itself anticipate the present Hecke-owner moment obstruction, but its omission leaves the bounded novelty comparison thinner than the underlying domain warrants. This is a literature-positioning defect, not an error in the finite theorem.

**Actionable Remedy**: Add a concise, source-verified nearest-neighbor paragraph that distinguishes geodesic-period nonvanishing/distribution results from the present level-11 cycle-pushforward, branch-degree, and exact finite moment-obstruction result. Use the 2025 paper as one verified entry point, follow its primary references for the weight-two closed-geodesic-period strand, and state the search boundary instead of claiming exhaustive novelty. Do not add any citation until its metadata and relevance have been checked.

**Search Limits**: Eight English-language queries were restricted to arXiv, DOI, Project Euclid, and primary publisher surfaces using combinations of “closed geodesic,” “period,” “holomorphic cusp form,” “Hecke,” “primitive,” and “dynamical zeta.” The search opened the 2025 primary article and one adjacent transfer-operator paper; it did not perform systematic citation chaining, subscription-database searching, cross-language searching, or full-text review of paywalled results.
