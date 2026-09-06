# C403 citation and claim map for full internal manuscript review

The manuscript contains exactly four bibliography entries and eleven actual
`\cite{...}` occurrences. This map inventories all of them; it is an
author-side navigation aid, not the non-author review itself. Line locators
refer to the frozen initial TeX. The main bibliography metadata and access
limitations are in `BIBLIOGRAPHY_CHECK.md`.

## All bibliography entries and all citation contexts

| Key / rendered reference | Actual context and TeX locator | Claim supported and scope |
|---|---|---|
| `Hilberdink2017` / [2] | `sections/1_introduction.tex:76` | 2017 multiplicative Toeplitz work; following sentences distinguish Theorem 2.2/Corollary 2.3 for complete multiplicativity from Theorems 3.1/3.2 with extra hypotheses |
| `Hilberdink2017` / [2] | `sections/2_framework.tex:32` | Section 1.1 states global Potter bounds under the stated local upper and lower bounds |
| `Hilberdink2017` / [2] | `sections/3_gram_limit.tex:21` | Proposition 2.1 owns the elementary common-multiple Gram identity; the displayed specialization is directly derived |
| `Hilberdink2017` / [2] | `sections/7_scope.tex:18` | Its multiplicative settings remain different from the present pointwise nonmultiplicative coefficient class; no claim of wholesale containment |
| `HilberdinkPushnitski2023` / [3] | `sections/1_introduction.tex:89` | LCM family, spectral asymptotics, and power-coefficient Toeplitz link; the following comparison is explicitly bound to Theorem 2.1 of arXiv:2110.14323v1 (2021), not a current-open-problem assertion |
| `HilberdinkPushnitski2023` / [3] | `sections/2_framework.tex:72` | Exact specialization of source Theorem 1.1 to second parameter one; supplies positive, compact, injective `E_s` and positive-constant eigenvalue asymptotics; all-positive-q membership then follows by a p-series test |
| `HilberdinkPushnitski2023` / [3] | `sections/7_scope.tex:27` | Explicit ownership of the LCM asymptotics, their constant, and prime-factor analysis; repeats the accessed-version boundary |
| `BinghamGoldieTeugels1987` / [1] | `sections/1_introduction.tex:125` | Classical uniform convergence theorem and Potter bounds, not a novelty claim |
| `BinghamGoldieTeugels1987` / [1] | `sections/2_framework.tex:30` | Equations (2.2) and (2.3), with measurable positivity and local bounds; no invented monograph page/theorem locator |
| `Simon2005` / [4] | `sections/1_introduction.tex:126` | General classical compact-operator framework |
| `Simon2005` / [4] | `sections/2_framework.tex:91` | Singular-value approximation/min--max framework around equation (2.7); the sum inequality and linearity of every `S_q` are proved immediately afterward, rather than resting on an uninspected precise book locator |

Table 1 summarizes the same three coefficient settings as the adjacent
source discussion. Source names there are not additional `\cite` commands.
The bibliography deliberately uses verified print/edition years while
identifying the accessed 2021 preprint in the Hilberdink--Pushnitski entry.

## Key claims and complete proof locations

| Claim | Statement / input | Proof or boundary |
|---|---|---|
| Standing hypotheses and common Hilbert-space realization | `sections/1_introduction.tex:12`, equations (1.1)–(1.2) | Measurability, positivity, compact-interval upper/lower bounds, `sigma<1/2`, zero extension all explicit; `sections/2_framework.tex:4` retains them |
| Main single theorem, including exact negative range | `sections/1_introduction.tex:43`, Theorem 1.1 | Sections 3–5; final assembled proof at `sections/5_ideal_convergence.tex:4` |
| Classical LCM spectrum, not new | `sections/2_framework.tex:51`, Theorem 2.1, equations (2.4)–(2.6) | Attributed specialization of source Theorem 1.1; exact threshold derived from its asymptotic |
| All-positive-q singular-value sum/ideal linearity | `sections/2_framework.tex:94`, Lemma 2.2 | Proof at line 104, using finite-rank approximation and the elementary scalar power inequality |
| Exact nonmultiplicative Gram entry | `sections/3_gram_limit.tex:6`, equation (3.1) | Direct matrix multiplication and the common-multiple parametrization; no multiplicativity used |
| Uniform Potter majorization | `sections/3_gram_limit.tex:45`, Proposition 3.2 | Proof at line 56; all input arguments in `[1,N]`, alpha below one, all N powers cancel |
| Entrywise limit including the smallest indices | `sections/3_gram_limit.tex:87`, Proposition 3.3 | Proof at line 101; uniform convergence on `[delta,1]`, equation (3.9) bounds the complementary tail independently of N, then N followed by delta limits |
| Uniform positive congruence | `sections/4_uniform_tails.tex:6`, Proposition 4.1 | Proof at line 28; finite-dimensional construction, shifted bounded LCM kernel, bilinear bound, and only then positive-operator order |
| N-independent eigenvalue tails | `sections/4_uniform_tails.tex:74`, Corollary 4.2 | Min--max applied to the genuine diagonal operator majorant; only eta below rho asserted |
| Operator-norm convergence | `sections/4_uniform_tails.tex:94`, Proposition 4.3 | Uniform two-sided tails, compact limit tail, and fixed finite-head convergence; no inference from entries alone |
| Every real q with q rho greater than one | `sections/5_ideal_convergence.tex:4`, proof of Theorem 1.1 | eta strictly between 1/q and rho; odd/even singular-value grouping; scalar dominated convergence, valid also below q=1 |
| Nonmembership when q rho at most one | `sections/5_ideal_convergence.tex:44` | Classical nonmembership plus finite rank and ideal linearity; applies to every finite N |
| Cumulative normalization | `sections/6_consequences.tex:13`, Corollary 6.1 | Scalar c_N tends to one by Gram entry (1,1); bounded c_N, operator convergence, and the same tail argument cover q below one |
| Fixed-index singular values and moments | `sections/6_consequences.tex:51`, Corollary 6.2 | Eigenvalue Lipschitz bound; positive limit eigenvalues; dominated spectral moments; absolute uniform error explicitly distinguished from relative growing-index asymptotics |
| Admissible nonmultiplicative / nonconvergent L | `sections/6_consequences.tex:108`, Section 6.3 | Logarithmic family checked directly; beta=1 violates multiplicativity at 2,3; bounded oscillatory example checked for slow variation and no limit |
| Nonclaims | `sections/7_scope.tex:1`, Section 7 | No arbitrary-arithmetic-sequence theorem from energy growth alone, universal rate, uniform endpoint tail, joint relative asymptotic, global priority certificate, or target spectral identification |

The principal body locations in the initial 11-page PDF are: Theorem 1.1
on printed page 2; classical input on pages 3–4; Gram estimates on pages
4–6; positive congruence and operator convergence on pages 6–7; full ideal
proof on page 8; consequences on pages 8–10; scope on page 10; declarations
and the four-entry bibliography on page 11. These are navigation aids for
this actual initial PDF, not unverified source-paper page anchors.
