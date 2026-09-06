# Independent cross-review: critical arithmetic Gram forms

Date: 2026-09-06. Reviewer: the current Hénon-arithmetic team agent, not the author of the reviewed arithmetic-forms package. This is a targeted internal mathematical and source-ownership review, not external human peer review or a formal Route-A evaluation.

## Verdict

**Mathematics: 0 blocking defects, 0 required theorem corrections.** The two alternatives, the explicit pure-singularity statement, and the arbitrary-positive-approximant resolvent lemma are correct under the written assumptions.

**Source positioning: one non-mathematical amendment recommended.** Name Simon's classical regular/singular decomposition when locating the largest-closable-minorant and variational machinery. The newly accessed original source and exact limits of that comparison are recorded below. This does not overturn the arithmetic theorem or identify a source already proving its complete nonmultiplicative dichotomy.

**Admission recommendation: retain as one compact research-note candidate, with modest significance language.** The explicit arithmetic prime-tail witness closes a genuinely different endpoint question from C403. It is not merely the already known unboundedness of a GCD matrix. However, the general form-theoretic relaxation and variational consequences are short classical machinery, and the square-summable branch is supporting closure theory. They should not be counted as separate innovations or separate papers. Global priority remains unverified.

## Materials and exact binding

Read completely:

- [PROOF_PACKAGE.md](../arithmetic_forms/PROOF_PACKAGE.md), 282 lines: SHA-256 `7bc0c91daeca890bab3520b814c456e65ed1ba6ec2a71eb8459745991c03f14c`.
- [SOURCE_AUDIT.md](../arithmetic_forms/SOURCE_AUDIT.md), 91 lines: SHA-256 `3666d4c1682cafa58ad5ad9d63af29f2b89a1707c66ec61b4258456fcebd9b5a`.
- [C403 proof package](../../continuation_c399_c403_round2/spectral_regular_variation/PROOF_PACKAGE.md): SHA-256 `0f8e436657de4207087137502236b2d48f69dae947f368b5d586039b7a282fee`.

The hashes bind the reviewed version; a subsequent author source amendment should be recorded as such. The reviewer did not edit those files, run their numerical code, rerun a sealed experiment, or change state/registry/evaluation files. Only this cross-review file was written in the assigned lane.

## 1. Pure singularity is proved in the declared sense

Proof lines 94–125 have the needed stronger property, not just one nonclosability sequence. For every finite $f$, primes outside its finite prime support give disjoint Hilbert-space shifts, whereas the form correlations factor as stated. Expanding the double sum gives

$$
q_r[h_E]=q_r[f]\left(1+s_E^{-2}\sum_{p\in E}r_p^2(1-r_p^2)\right),
\qquad \|h_E\|^2=s_E^{-1}\|f\|^2.
$$

Thus $h_E\to0$ in $\ell^2$ but $h_E\to f$ in the form seminorm. If $0\le b\le q_r$ is closable on $c_{00}$, then $(h_E)$ is $b$-Cauchy and tends to zero in Hilbert norm; closability forces $b[h_E]\to0$. The second approximation forces $b[f]=0$. This holds for every finite $f$, so **every** such minorant vanishes.

A closed nonnegative extension agreeing on $c_{00}$ would restrict to a nonzero closable minorant, contradicting this result. No assertion about indefinite extensions, a changed Hilbert space, or all possible renormalizations is needed or justified. In particular, “purely singular” is not being confused with singular spectral measure of a self-adjoint operator that has already been constructed.

The converse supporting argument is also sound: if $\sum r_p^2<\infty$, the factors for primes dividing a fixed column index are finite geometric tails, and the other factors give a convergent product. Every column is in $\ell^2$, yielding a densely defined nonnegative symmetric operator on $c_{00}$ and hence a closable quadratic form. The $r_p=0$ convention causes no exception.

## 2. The arbitrary-positive-approximant claim survives the quantifier test

Proof lines 142–174 require that each $B_N$ is bounded, self-adjoint and nonnegative; they do not assume uniform boundedness, monotonicity, or entrywise nonnegativity. The distinction matters.

For each fixed finite $v$, matrix-entry convergence gives convergence of its energy. The proof first constructs, independently of $N$, finite vectors $v_j\to g$ with $q_r[v_j]\to0$, and only then chooses an increasing $N_j$ so that the energy comparison holds **for all** $N\ge N_j$. The slowly increasing diagonal $j(N)$ is legitimate. It does not infer convergence on a moving support from entrywise convergence alone.

With $g=\lambda^{-1}f$, the recovery vector bounds the minimum of

$$
\langle x,B_Nx\rangle+\lambda\|x-\lambda^{-1}f\|^2.
$$

Positivity then forces the unique minimizer $(B_N+\lambda I)^{-1}f$ to converge in norm to $\lambda^{-1}f$. This is strong resolvent convergence to zero, not strong operator convergence of $B_N$. The norm-divergence argument is also fully quantified: an unbounded finite-core form supplies, for each $M$, one fixed unit vector whose limiting energy exceeds $2M$, forcing $\|B_N\|>M$ eventually.

Conceptually this is a direct zero-relaxation/variational argument. The proof is useful and complete, but its general functional-analytic mechanism should not be promoted as an independent new theory of resolvents.

## 3. All stated slowly varying weights are covered

Proof lines 176–207 correctly use measurable, positive slow variation and its uniform convergence theorem. For each fixed $A>1$, the moving multiplicative block contributes asymptotically $L(N)^2\log A$. Letting $A$ grow only **after** taking the large-$N$ lower limit establishes $L(N)^2=o(F(N))$; no uniform-in-$A$ assertion is required.

For each fixed $c\ge1$, the omitted block between $N/c$ and $N$ is $O_c(L(N)^2)$, giving $F(N/c)/F(N)\to1$. In the Gram identity, the two coefficient arguments are fixed multiples of $k$, so the summand ratio tends to one. Since $F$ diverges, a fixed initial segment is negligible. No multiplicativity, monotonicity of $L$, convergence of $L$ itself, or positive regular-variation index has been smuggled into this step.

At $r_p=p^{-1/2}$, prime reciprocal divergence supplies the exact tail condition. The identity $A_N(1,1)=1$ is consistent with resolvent collapse and inconsistent only with the stronger, unclaimed assertion of strong operator convergence to zero.

## 4. The finite-$F_\infty$ branch uses the correct maximal domain

Proof lines 209–254 define the maximal rowwise convolution operator explicitly. Every row is a continuous finite functional. Coordinatewise passage in a convergent graph sequence proves closedness on that domain, while square summability of each column ensures that $c_{00}$ lies in the domain and is Hilbert-space dense.

The proof does **not** assume that $c_{00}$ or coordinate truncations form a graph core. This avoids a real possible error. For a weakly convergent subsequence, retaining a fixed finite number of rows gives the energy lower bound; then increasing the retained row count supplies the full closed form, including the value $+\infty$ off the maximal domain. The comparison at the fixed limiting minimizer gives convergence of minimum values. Completing the square provides strong convergence.

The limiting operator is nonzero because its associated closed form has value one on $e_1$; this argument does not incorrectly assume $e_1\in D(C^*C)$ merely from $e_1\in D(C)$. The normalization tending to a positive finite constant is handled correctly. The logarithmic example with threshold $\beta=1/2$ supplies both branches within the same critical power.

## 5. Independent primary-source checks and one amendment

The reviewer freshly accessed the following specific primary contexts:

| Source and actual locator | What the comparison establishes |
|---|---|
| Aistleitner–Berkes–Seip, [arXiv:1210.0741v3, §3, Lemma 1 and its surrounding equations](https://arxiv.org/html/1210.0741v3); introduction's discussion of $\sum p_j^{-2\alpha}$ | The general finite product kernel, Poisson representation, positivity and the significance of the prime-square threshold are prior-owned. These are not new objects in this package. The inspected passage does not state the pure-singularity/minorant conclusion. |
| Yafaev, [arXiv:1603.06229v1, Theorem 1.3, §2.1 and Proposition 3.1](https://arxiv.org/html/1603.06229v1) | Confirms the classical form/closed-operator facts and the one-circle Toeplitz closability theorem. Its one-variable absolutely-continuous-measure criterion cannot simply be transferred to the infinite-prime analytic space. The submitted proof makes no such unsupported transfer. |
| Hilberdink–Pushnitski, [arXiv:2110.14323v1, §2.2–2.3, Theorem 2.1](https://arxiv.org/html/2110.14323v1) | The relevant rescaled-Gram convergence is explicitly subcritical, $\sigma<1/2$. It does not itself state the present critical singular-form dichotomy. The older power-coefficient norm/LCM framework remains acknowledged. |
| Simon, [original author-hosted article, §§2–3](https://math.caltech.edu/SimonPapers/81.pdf) | Theorems 2.1–2.2, printed pp. 379–380, characterize the largest closable minorant; p. 381 explicitly discusses a purely singular form. Theorems 3.1–3.2, pp. 382–383, are monotone form-convergence theorems. They own foundational machinery but do not directly state this arbitrary-entrywise approximation lemma. |

**Recommended source amendment S1:** add Barry Simon, *A canonical decomposition for quadratic forms with applications to monotone convergence theorems*, Journal of Functional Analysis **28** (1978), no. 3, 377–385, DOI [10.1016/0022-1236(78)90094-0](https://doi.org/10.1016/0022-1236(78)90094-0). Explain that the explicit arithmetic witness is being placed within this classical regular/singular framework, while the direct argument avoids requiring a monotone approximating family.

The original nine-page article was found through item 81 of the [author bibliography](https://math.caltech.edu/simon/biblio.html) and read in the browser, including the actual theorem statements above. The first `www` host retrieval timed out / failed certificate verification, and the publisher full-text open returned 403; the non-`www` author host succeeded. No inaccessible publisher full-text reading or local PDF download is claimed. OCR renders some symbols and one header page number poorly; the cited printed section/theorem identifiers and correct 377–385 metadata are supported by the original and official record.

The parent audit's other literature rows were read as supplied, but are not promoted here to an independent full-text attestation of every source. A fresh Hilberdink PDF browser open encountered the university anti-bot page; its proof claim is not accepted merely from that failed access. The Gram identity was independently derived above, and the directly accessed 2021 source supplies the needed subcritical comparison. Book-length regular-variation theory was not reread; the exact classical UCT version used is explicit in the proof.

Targeted searches for GCD/closability, multiplicative Toeplitz/singular forms, GCD/resolvent, and positive-form regular parts did not reveal the complete arithmetic dichotomy. Irrelevant polynomial-gcd, stochastic-Dirichlet-form and aggregation-site hits were not used as evidence. This is not an exhaustive novelty search or a venue-integrity certificate.

## 6. Substantive delta and release boundary

C403 proves compact Schatten convergence for $\sigma<1/2$ and arbitrary admissible slowly varying coefficients. The new problem at $\sigma=1/2$ does not admit a compact operator limit on the declared core. More importantly, the current proof determines what happens **instead**: the divergent normalization gives a nonzero entrywise form with zero closable part and zero strong-resolvent limit, while square-summable critical weights give a genuine nonzero maximal-convolution operator. This changes the type of limiting object, not just a constant or parameter range in the old conclusion.

After subtracting all classical ownership, the strongest candidate-level content is the explicit prime-tail construction and its deployment in this nonmultiplicative critical dichotomy. Its proof is short and its likely significance is that of a focused operator-theoretic arithmetic note, not a general spectral breakthrough. That modest assessment is compatible with retaining it as one candidate; it does not warrant splitting supporting lemmas or guaranteeing acceptance.

No numerical check can certify the divergent prime tail, the all-weight quantifiers, the maximal operator domain, or strong convergence for every vector. Therefore this review appropriately used proof and exact source scopes and did not request an artificial finite-matrix quota. The research-review and proof-writer checks were used within the current team and assigned write scope; old external-model calls, ML grading templates and root-memory mutations were not invoked.

There is no target Euler-factor construction, root-number evidence, target zero matching, or exclusion of all alternative Hilbert-space representations. The fixed-space source obstruction must retain that scope in any later manuscript or formal evaluation.

## 7. S1 attribution amendment closed

The author accepted recommendation S1 and added a Simon row to the source audit, an explicit classical-ownership paragraph to the proof's input section, and a short amendment note. On 2026-09-06 the reviewer reread **only those new attribution passages**. They correctly distinguish Simon's largest-closable-minorant theory and monotone-limit theorems from the direct arbitrary-entrywise recovery-vector argument. The author's actual reading scope is stated rather than overstated.

**S1 is resolved.** No mathematical statement was changed or rerun, and no second full proof review is claimed. The original version binding above remains the audit trail; the current amended bindings are:

- `arithmetic_forms/PROOF_PACKAGE.md`: SHA-256 `eacbacec1c5a37506a32563b7c774f634557825bde9dde130368b39e6a78ac14`.
- `arithmetic_forms/SOURCE_AUDIT.md`: SHA-256 `a861bbeba6e14775123276d6b9eade326b32520f3d6b3da54b4aadb82b998cf7`.

The mathematical verdict remains 0 blocking defects and 0 required theorem corrections; there is now no outstanding source amendment from this review.
