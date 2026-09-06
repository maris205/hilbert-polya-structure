# Independent internal review: regular-variation Gram limit

Date: 2026-09-05. Current-team mathematical review, not human peer review.
Calibration: `NOT_CALIBRATED`; no venue-fit assessment or external model call.
The author proof was read completely and not modified. No numerical rerun.

Input: `../spectral_regular_variation/PROOF_PACKAGE.md`, 260 lines.
SHA256, identical before and after review:
`0f8e436657de4207087137502236b2d48f69dae947f368b5d586039b7a282fee`.

## Verdict

**No blocking mathematical defect found. Retain as one substantive,
modestly scoped nonmultiplicative universality theorem.** The proof establishes
the stated full sharp Schatten range, including $q<1$, under its explicit
local-boundedness assumptions on $L$. This is not a new spectral law for the
limiting LCM operator. Paper admission should rest on the combined
nonmultiplicative family and sharp ideal convergence, not on an old conjectural
remark or separate papers for different exponents.

## Blocking findings

None. The following are the actual checked risk surfaces, not a test quota.

| Surface | Evidence anchor | Independent check |
|---|---|---|
| Global Potter bound | equation: RV1, lines 67–77 | Eventual Potter extends globally using the stated positive compact upper/lower bounds. All arguments used in the Gram sum are at least one. |
| Entry majorization | equation: (1)–(2), lines 83–108 | With $\alpha=2\sigma+2\epsilon<1$, the power sum supplies $N^{1-\alpha}\ell^{\alpha-1}$; the prefactor cancels the $N$ power and leaves exactly $(mn)^{\sigma+\epsilon}/\ell$. Negative $\alpha$ causes no failure. |
| Small indices | equation: (3), lines 126–137 | Writing $h=\ell/N$, the tail is bounded by $C h^{1-\alpha}(\delta/h)^{1-\alpha}=C\delta^{\rho-2\epsilon}$. The empty-tail case is handled. On the remaining interval the two UCT arguments range in fixed compact subsets of $(0,\infty)$. |
| Positive congruence | equation: (6), lines 147–168 | $B_N$ is a finite positive congruence; there is no unbounded inverse-diagonal domain problem. Entry domination is used only for the bilinear operator-norm estimate against bounded $E_s$. Then $0\le B_N\le MI$ yields the genuine operator inequality $A_N\le MD_\eta^2$. |
| Uniform spectral and spatial tails | equation: (7)–(9), lines 170–197 | Min–max gives $\lambda_j(A_N)\le Mj^{-\eta}$; finite-support form convergence gives the corresponding bound for $E_\sigma$. The two-sided coordinate tail follows from the factorization, not from entrywise convergence alone. |
| All $q>0$ | equation: line 208 and line 215 | The singular-value sum inequality controls odd indices, monotonicity controls even ones, and $\eta q>1$ gives a summable dominating sequence. Operator-norm convergence kills each fixed singular value. No Banach interpolation or triangle inequality at $q<1$ is used. |
| Sharp exclusion | text: §7 “by the linearity of the ideal” | Finite rank belongs to every $S_q$, and these are linear ideals even for $q<1$. Membership of the difference would contradict the classical exact membership threshold of $E_\sigma$. |

The $F(N)$ normalization, fixed-index eigenvalue limits and moment convergence
in §8 also follow. The zero-extended uniform eigenvalue statement is correctly
an absolute-error statement, not a relative asymptotic for growing indices.

## Minor findings

### M1. Preserve the actual scope of “arbitrary measurable”

Severity: Minor. Evidence anchor: text: §1 “bounded above and away from zero on every compact interval”.
Confidence: 5 — direct comparison of hypothesis and Potter usage.

The theorem is correct as written, but an abstract or handoff must not omit
this extra hypothesis while calling the family arbitrary positive measurable
slowly varying functions. Minimal remedy: retain that qualifier. Alternatively,
the author may explicitly replace global RV1 by integer-grid Potter: finitely
many small positive integer values admit finite upper/lower bounds, and all
sampled arguments are integers. This would permit deleting the unnecessary
real-compact assumption, but is an optional theorem extension, not a repair
needed for this input.

## Source ownership and substantive increment

[Hilberdink–Pushnitski v1](https://arxiv.org/html/2110.14323v1), Theorem 1.1,
supplies the positive compact LCM operator, spectral asymptotics and exact
Schatten membership. Theorem 2.1 gives the power-coefficient convergence for
even $q$; the following remark is not evidence that it remains unresolved.

Hilberdink's 2017 accepted manuscript, *Singular values of multiplicative
Toeplitz matrices*, was inspected in the supplied extracted text: Theorem
2.2/Corollary 2.3 require complete multiplicativity; Theorems 3.1/3.2 require
multiplicativity and additional correlation hypotheses. It already uses
regular variation and Potter bounds. Thus “regular variation enters this
subject for the first time” would be false. Its stated theorems do not directly
cover the present nonmultiplicative pointwise family.

Original PDF SHA256 checked:
`d040bf0f3df4da2d72b1f7728b80c6e3fed3d1214ed1e3a895e8dde81f71b518`.
Source: [official accepted manuscript](https://centaur.reading.ac.uk/66059/1/finitetoeplitz.pdf).
Theorem locators, not unaudited PDF page anchors, are used here.

The strongest objection is that much of the proof uses classical tools and
the $L=1$ parity extension alone is short. Nevertheless, removing arithmetic
multiplicativity for a complete oscillatory slowly varying family, while
obtaining every admissible ideal exponent and exact failure outside it,
answers a coherent full-family question. I recommend retaining this as one
paper-level theorem, subject to the coordinator's separate current-source
collision audit. This review does not certify global novelty or target
arithmetic progress. The research-review fallback and ARS read-only,
evidence-anchored discipline were used within the assigned single-review scope.
