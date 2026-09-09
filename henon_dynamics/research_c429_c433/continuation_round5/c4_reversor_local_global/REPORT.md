# R5 C4 — polynomial reversibility over all original completions

## 1. Outcome and review status

**Author result: PROVABLE AS STATED, as a negative answer to the frozen
universal implication.** The complete hand proof is in
[PROOF_PACKAGE.md](PROOF_PACKAGE.md). No mathematical gap remains
identified by the author; independent mathematical review and separate
substantiality/admission review remain pending.

There is an explicit Hénon word over $K=\mathbf Q(\sqrt7)$ with a
polynomial reversor over **every original completion** $K_v$ and none
over $K$. The exclusion covers every polynomial degree and order.
The local witnesses happen to be affine involutions; that is a property
of this example, not a restriction imposed on the global search.

This result does not resolve or replace SF2, good-model descent,
congruence orbit separation, or any target arithmetic bridge.
It is not automatically a fourth admitted contract or a completed paper.

## 2. Frozen original question

For every number field $K$, let $F=H_r\circ\cdots\circ H_1$, $r\ge1$,
where $H_i(x,y)=(y,P_i(y)-a_i x)$, $P_i\in K[y]$,
$\deg P_i\ge2$, and $a_i\in K^*$. The exact question is whether

$$
\big[\forall v\in\Omega_K\ \exists R_v\in
\operatorname{Aut}_{K_v}(\mathbf A^2):
R_v F R_v^{-1}=F^{-1}\big]
\ \Longrightarrow\
\big[\exists R\in\operatorname{Aut}_K(\mathbf A^2):
R F R^{-1}=F^{-1}\big].                                   \tag{B}
$$

Here $\Omega_K$ includes all finite and infinite places. An automorphism
is polynomial with polynomial inverse. No place is omitted; no local
field is enlarged; no degree, order, affine, or involution bound is
allowed for $R$ or $R_v$. One application of the whole ordered $F$
is the native tick. Passing to an iterate is not a substitute.

The original freeze recorded a promising counterexample but not a
proof. The package now supplies the previously missing all-polynomial
exclusion, without changing (B). A single such example is enough to
disprove the universally quantified implication.

## 3. Exact counterexample and exhaustive criterion

Write $H_{c,d}(x,y)=(y,c y^d-x)$. Set

$$
K=\mathbf Q(\sqrt7),\qquad
F=H_{4,7}\circ H_{1/16,15}\circ H_{16,15}\circ H_{1/4,7}.    \tag{1}
$$

All four factors satisfy the frozen Hénon hypotheses, with coefficient
of $-x$ equal to one. No integral-good-model assertion is needed.
For every place choose $t_v\in K_v$ satisfying $t_v^8=16$ and put

$$
R_v(x,y)=(t_v^{-1}y,t_vx).                                  \tag{2}
$$

The package proves these roots exist at every place and verifies
$R_vFR_v^{-1}=F^{-1}$. It also proves the following one-family
criterion, which is an internal interface for the same counterexample:
for every number field $L$ and $a\in L^*$, let

$$
F_a=H_{a,7}H_{a^{-2},15}H_{a^2,15}H_{a^{-1},7}.
$$

Then the **entire set** of polynomial reversors is

$$
\operatorname{Rev}_L(F_a)=
\{F_a^jR_t:j\in\mathbf Z,\ t\in L^*,\ t^8=a^2\}.             \tag{3}
$$

Taking $a=4$ in (3), any hypothetical global reversor would force
$t^8=16$ in $K$. Since $K$ is real and does not contain $\sqrt2$,
this is impossible. Equation (3) accounts for every native-power
component; it is not merely an affine ansatz.

## 4. Proof obligations now discharged

| Obligation | Exact resolution | Package locator |
|---|---|---|
| Entire geometric centralizer, not subgroup inclusion | On the Jung–van der Kulk tree, the cycle $(7,15,15,7)$ has least label period four; every commuting translation is a native power. | §1 |
| Every possible pointwise-axis symmetry | Successive diagonal-affine conjugations kill translations and force exactly $\operatorname{diag}(\zeta,\zeta^{-1})$, $\zeta^8=1$. | §2 |
| All polynomial reversors, with unbounded degree | A known reversing swap and the full centralizer give every reversor as its centralizer coset. | §2 |
| Correct root equation after twisting | Alternating scalar conjugation gives $F_a=A_u^{-1}F_0A_u$, $u^8=a$, and all affine coset representatives have $t^8=a^2$, not the stronger $t^4=a$. | §3 |
| Original-field descent in every integer component | If $F_a^jR_t$ is defined over $L$, removing the $L$-defined $F_a^j$ leaves $R_t$, hence $t\in L$. | §3 |
| All original completions | Odd primes use a square root of one of $2,-2,-1$ in $\mathbf Q_p$; the dyadic completion contains $i$; both real completions contain $\sqrt2$. | §4 |
| No global polynomial reversor | $16\notin\mathbf Q(\sqrt7)^{\times8}$ combined with the exhaustive criterion. | §5 |

The aperiodic four-factor choice matters. The two-factor control in
the [X2 scout](../x2_second_replacement/REPORT.md), despite a failed
affine-swap equation, is a product of two globally defined elementary
involutions and is globally reversible. The present proof does not
repeat that false inference. It also does not claim unrestricted
Kummer local-global injectivity: the arithmetic counterexample refutes
that shortcut.

## 5. Primary sources and subtraction

The author read the passages indicated here. The full X2 scout was
also read, but passages read only by X2 are not relabelled as this
author's direct source access.

| Paper | Version / venue | Method and result used or subtracted | Relevance and actual access |
|---|---|---|---|
| Gómez–Meiss, *Reversors and symmetries for polynomial automorphisms of the complex plane* | Nonlinearity 17 (2004), 975–1000 | Amalgam and normalized conjugacy structure; its commuting-subgroup inclusion alone is insufficient for our equality. | Primary author-hosted PDF; §2.1, Theorem 3, §2.2, Theorem 4 and proof read; Theorem 7/Corollary 9 scope checked. [Source](https://amath.colorado.edu/faculty/jdm/papers/Reversors.pdf) |
| Baake–Roberts, *Symmetries and reversing symmetries of polynomial automorphisms of the plane* | arXiv:math/0501151v1 (2005 preprint) | General-field amalgam/reduced words, not the restricted symmetry conclusion. | Primary §2 Facts 1–2 and Proposition 1 read; Theorem 2/Corollary 1 explicitly require only $\{\pm1\}$ as roots of unity and are not used over $\mathbf C$. [Source](https://arxiv.org/pdf/math/0501151) |
| Cantat–Dujardin, *Holomorphically conjugate polynomial automorphisms of $\mathbf C^2$ are polynomially conjugate* | Bull. London Math. Soc. 56 (2024), 3745–3751 | Closest prior scalar-root/full-centralizer descent mechanism. | Primary final example of §2.2 and explanation read fully. [Source](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/blms.13164) |
| Song Wang, *Grunwald–Wang theorem, an effective version* | arXiv:1401.0389v1 (2014 preprint) | Classical exceptional power class for the precise field and exponent here. | Primary §2.1 Proposition 2.1 and p. 7 following remark read. Section 4 of our package independently checks all places. [Source](https://arxiv.org/pdf/1401.0389v1) |

The first source family supplies the classical polynomial group
structure. The labelled-tree proof and the explicit scalar equations
specialize that framework; they do not constitute a new centralizer
theory. The field restrictions in the simpler symmetry classifications
cannot be bypassed by silently changing the base field.

The closest prior mechanism already uses a scalar root and the full
centralizer to exclude every alternative polynomial conjugacy.
Combining it with Wang gives analogous all-place conjugacy failures.
Our distinction is the constrained inverse pair $(F,F^{-1})$, not
general twisting or field descent.

The arithmetic obstruction is entirely old. The proof includes the
dyadic and real checks to preserve the exact quantifiers and to avoid
mistaking almost-everywhere local solubility for the required premise.
The publisher's Frei et al. Example 3.9 was fully read by X2, but this
author's repeated fetch attempts did not return its text; it is not
counted as an independently read input here.

The potential increment is therefore narrowly identified: a single
native inverse-pair realization, plus complete exclusion of hidden
polynomial reversors. Whether that synthesis is substantial enough
for a separate paper remains an independent admission question.
Neither the source table nor the absence of an exact retrieved
collision certifies novelty or paper value.

## 6. Bounded retrieval record

No configured Zotero/Obsidian tools were present. The local PDF
filename filter found no relevant Hénon/reversor/Wang source in
the project's paper library. No arXiv fetch script was present in
the checked skill paths, so the literature skill used its web
fallback. No PDF was downloaded to the repository.

Actual author-side queries included:

- "Hénon" "reversibility" "local-global";
- "polynomial automorphisms" "Wang" "reversor";
- "Hénon" "reversor" "Hasse" site:arxiv.org;
- "polynomial automorphisms" "local-global" reversibility with
  the 2024-09-09 through 2026-09-10 date window;
- "Hénon" "reversibility" "number field" site:arxiv.org with
  a 184-day recency control;
- "Hénon" "Wang" "reversibility" in web-indexed Scholar/Semantic Scholar.

These searches retrieved no applicable exact all-place reversibility
result. Irrelevant time-series and unrelated algebra results were
not used as mathematical evidence. The separately owned X2 report
records the wider scout searches and the precise older-source
comparisons. This is a bounded search record, not an exhaustive
literature claim.

## 7. Execution, ownership, and handoff

Only this REPORT and PROOF_PACKAGE in the exclusive C4 R5 directory
were written. No mathematical program, new/nested agent, GPU/API
run, shared-file edit, Git action, manuscript, or upload was performed.
Earlier first-pass and continuation bytes remain untouched.

The proof-writing skill shaped the explicit assumptions, dependency
map, full-quantifier proof and review-risk list. The literature-review
skill shaped the source table, direct-access boundaries and classical
subtraction. Neither skill authorizes an admission or publication.
Root should obtain bounded non-author verification of §§1–5 and
independently decide substantiality after the closest-source
subtraction. Until then this is an author-complete negative answer,
not an accepted paper or a changed batch count.
