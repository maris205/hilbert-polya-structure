# C405 independent manuscript review

Date: 2026-09-06. Reviewer: the current Hénon-arithmetic team agent, who did
not author the C405 manuscript. This is a review of the actual stable
TeX/BibTeX body, not a repetition of the earlier proof-package verdict or
an inference from the abstract. It is current-team internal review, not
external human peer review, an external-model assessment, or a Route-A
evaluation.

## Verdict

**0 mathematical blockers, 0 required theorem corrections, and 0 required
citation/claim-boundary corrections.** The manuscript faithfully converts
the admitted critical summability dichotomy into a complete mathematical
article. Its full proof retains the arbitrary-positive-approximant
quantifiers, the fixed-space notion of pure singularity, and the maximal
rowwise operator domain in the square-summable branch.

The earlier Simon attribution amendment remains correctly incorporated.
The source positioning is appropriately modest: the finite product
kernel, Gram identity, classical form theory, and subcritical Schatten
results are acknowledged. The paper presents one arithmetic endpoint
dichotomy, not a new general theory of form relaxation or several separate
innovations. Global priority and publication significance are not certified.

This manuscript-review gate may be closed for the input versions below.
Final fresh-directory compilation, all-page visual QA, actual evaluations,
and any release actions remain separate coordinator responsibilities.

## 1. Materials actually read and version binding

The reviewer read all **909 lines** of the eleven current author-controlled
TeX/BibTeX files: main entry point, macros, bibliography, abstract, and all
seven numbered body sections. Also read were the frozen proof package,
source audit, finite receipts, previous independent proof review with its
Simon-amendment closure, and the writer's current bibliography/claim and
initial-compilation records.

The command below was run before and after the mathematical/claim check,
with the same result:

~~~sh
sha256sum main.tex math_commands.tex references.bib sections/*.tex | sha256sum
~~~

Ordered source-list digest:

~~~text
94360d34b9ee40525e9a20a95713a737d6b3d29968c93d769d5ee4dd252e66a1
~~~

This is a hash of the ordered textual hash listing, not a tar archive.
The individual stable source hashes, relative to arithmetic_forms/paper/,
are:

| Input | SHA-256 |
|---|---|
| main.tex | 53a73373cf85ecc654fe7a1ee1a0dd129400db45f1c3bf2c7c6faff643cb967e |
| math_commands.tex | f6da7cc997c448634577ec39b6a2ffd54aae4cd3f99746ddf896b670a0d5e29a |
| references.bib | b974b2e2f28020263b1b06c34c4ff6bf7321218215d7dcb77ee32e41933755b7 |
| sections/0_abstract.tex | 3fb7e9b05f2eab62329fea7a9129ceb46434ef2d661a9f306c42e2023d873a39 |
| sections/1_introduction.tex | 52e407fd196c74277d0854a1374deae95fa532ca6687214b5bf072fb8804a1ba |
| sections/2_product_forms.tex | 7066bf7a990be52c23b15a084007c40f7de5c3be48c36ca7ea810a9bea367354 |
| sections/3_variational.tex | 00afb318f3dc3c954d4684951aa267e7368003f9395c91e00fd2751dbde16ab5 |
| sections/4_critical.tex | 4ed718e09f38bbbe6f13df2f703a7b8fc51e5e8114e67d802ca14a07435931e0 |
| sections/5_summable.tex | c2ef5d4e0c7df624dc02d7f02e9848b63a4af4ff18fb66ff644bcb6f84a4e725 |
| sections/6_examples.tex | 9148d7e3a328a1745a24e45f832a5af152ef54b712f9d4b62234c5acc496c15b |
| sections/7_conclusion.tex | 5f865ee21522f56726705f0143e67c8ae308b56a19900aeac4a9d290c4bdae8c |

The actual initial PDF hash is
9b6801db5237ef523fded18797ec7508a06762bd79fd1c32f0074ddbfa9290c3.
It has 10 pages and 355317 bytes. The task message initially supplied
a mistyped PDF hash suffix; the coordinator confirmed the actual disk
hash above. This was a transcription error in the handoff message,
not a change to the manuscript or PDF.

Other inspected evidence, relative to arithmetic_forms/:

| Evidence | SHA-256 |
|---|---|
| PROOF_PACKAGE.md | eacbacec1c5a37506a32563b7c774f634557825bde9dde130368b39e6a78ac14 |
| SOURCE_AUDIT.md | a861bbeba6e14775123276d6b9eade326b32520f3d6b3da54b4aadb82b998cf7 |
| BOUNDED_RECEIPTS.md | b6de665b9c36d0bdd185fb4e2136a246df0ab45e5ab9c711f69a54502f2c9bc3 |
| paper/INITIAL_COMPILE_RECEIPT.md | 548e8338b96dcb12949ee73bc140e3577ab240d67cf0f859042f84695f573a51 |
| paper/BIBLIOGRAPHY_AND_CLAIM_CHECK.md | 9e154d3a6300372a9e61ac0fb91a57b74f6e712733bbe97a049698741b1e439d |

No author input, finite result, evaluation, registry, or Git state was
edited. The only file written by this review is the present report.

## 2. Quantified mathematical checks

### 2.1 The main statement fixes the objects before taking limits

The introduction defines one Hilbert space, one truncation parameter,
positive measurable slow variation with the stated local bounds, the
normalization F(N), and finite operators extended by zero. Since all
sampled coefficients are positive, F(N) is positive for every N. The two
alternatives exhaust the possibilities for this increasing positive sum.
The strong-resolvent assertions quantify over every positive lambda and
every Hilbert-space vector; there is no hidden uniform-in-N norm bound.
The definition of pure singularity concerns nonnegative closable
minorants on c00, not the spectral type of an operator already assumed
to exist.

### 2.2 Prime shifts and pure singularity

Lemma 2.2 explicitly requires tail primes to be absent from the prime
support of f. This makes the shifts pairwise disjoint in Hilbert norm
and gives the three distinct form correlations. The proof uses prime
factorization for both obligations; it does not confuse an isometry
with form orthogonality.

In Proposition 2.3, the diagonal and off-diagonal terms of q_r[h_E]
give exactly the displayed residual. The finite excluded prime set
does not affect divergence of the square sum. Crucially, the argument
begins with arbitrary finite f and arbitrary nonnegative closable
b below q_r. The constructed h_E is b-Cauchy, converges to zero in
Hilbert norm, and approximates f in b-seminorm. These facts force
b[f]=0. Thus the proof gives pure singularity, not merely a single
nonclosability witness.

The converse allows zero parameters and all parameters strictly below
one. Its fixed-column square sum is a nonnegative factorization limit;
the finitely many primes dividing the column index have finite
geometric-tail factors, while the remaining product converges under
the square-sum assumption. The resulting positive symmetric operator
on c00 has a closable quadratic form. The conclusion does not claim
the stronger and unnecessary assertion that the operator is bounded
or essentially self-adjoint.

A nonnegative closed extension agreeing with the divergent form would
have a nonzero closable restriction, contradicting the proved minorant
statement. The fixed-space and nonnegative qualifications are retained.

### 2.3 Recovery diagonalization and arbitrary positive approximants

Proposition 3.1 first passes from entrywise convergence to the energy
limit for each fixed finite vector. It then chooses finite v_j
approaching an arbitrary target, with limiting-form energy tending to
zero, before selecting increasing N_j. The comparison is imposed for
all N at least N_j, and the explicitly defined j(N) tends to infinity.
This order correctly handles moving supports; there is no unsupported
uniform entrywise convergence claim.

For the target lambda^{-1}f, minimality of the resolvent vector and
nonnegativity bound its squared distance by the recovery functional.
Every B_N is bounded, positive and self-adjoint, but no monotonicity
or common bound is needed. The last paragraph excludes extension to
arbitrary signed approximants.

Norm divergence is also correctly quantified. For each M, one fixed
finite unit vector with sufficiently large limiting energy works for
all sufficiently large N. This proves divergence of the full sequence
of norms, rather than just an unbounded subsequence.

### 2.4 Critical slow variation and entrywise limits

Lemma 4.1 uses the uniform convergence theorem on a fixed multiplicative
block. The parameter A is enlarged only after taking the lower limit
in N. This proves L(N)^2=o(F(N)) without needing uniformity for growing
blocks, monotonicity of L, or a limit of L itself. The omitted fixed-ratio
block is then negligible, with floor endpoints handled explicitly.

The Gram identity in Lemma 4.2 sums exactly the common-multiple rows.
The two coefficient arguments are fixed multiples of k, so ordinary
slow variation gives the summand ratio. Divergence makes the fixed
initial segment negligible. This gives the stated GCD kernel without
multiplicativity. Prime reciprocal divergence then supplies precisely
the hypothesis of the singularity and collapse propositions.

The identity A_N(1,1)=1 is retained and correctly used to rule out
strong operator convergence to zero, not strong-resolvent convergence.

### 2.5 The maximal-domain summable branch

Lemma 5.1 proves closedness by continuity of each finite row in a
converging graph sequence. Square summability of each column proves
that c00 is in the domain and is Hilbert-space dense. The manuscript
does not identify this maximal operator with the graph closure of a
finite-core operator.

Lemma 5.2 retains finitely many rows before passing to the weak limit,
then increases the row cutoff. It yields the full extended-valued
closed form, including infinity outside the domain. The normalization
converges to a strictly positive finite value.

In the resolvent proof, recovery is at the actual limiting minimizer,
which lies in D(C). The bounded sequence has weakly convergent
subsequences; the lower bound and fixed-competitor upper bound identify
every weak cluster point and the minimum values. The displayed
strong-convexity identity then proves norm convergence. None of these
steps needs a graph-core assertion.

Finally q_infinity[e_1]=1 proves nonzeroness of the closed form and
therefore of its associated operator. The manuscript explicitly avoids
deducing e_1 in D(C*C) from e_1 in D(C).

## 3. Examples and finite evidence

The logarithmic example is correct for every real beta. Its integrand
is eventually decreasing even for negative beta, and the transformed
integral has threshold beta=1/2 with divergence at equality. The
2,3,6 comparison proves nonmultiplicativity for every nonzero beta,
not merely for one selected value.

The two exact numerical values printed in the body match the frozen
receipt. They were also checked algebraically in this review, without
running the exact script or starting a new numerical census:

- The stated vector has q_K[f]=11/4. For E={5,7,11},
  s_E=167/385 and the residual formula gives 148819/27889.
- For the same vector and L=1, cancellation in the pairwise expression
  at N=12 leaves 1+(7/4)H_4/H_12, equal to 374167/172042.

The invalid tail overlaps the support primes and produces an actual
collision at 6. Its failure is clearly distinguished from the earlier
ineffective control. The large finite residual is expressly described
as an identity check rather than evidence of convergence. The
manuscript does not claim a resolvent computation, an empirical UCT,
or a finite certificate for prime-tail divergence.

The summable column of Table 1 refers to form entries
<Ce_m,Ce_n>/F_infinity. Its caption explicitly avoids an operator-domain
claim for the coordinate vectors. Polarization of the fixed-vector form
limit justifies that entrywise description.

## 4. All actual citation contexts

The six bibliography entries occur in eleven citation commands. The
table below covers every command, with locations relative to paper/.
This pass checked the actual manuscript statements against the supplied
source scopes and the previous independent primary-source review.
It did not repeat the whole literature search or claim a fresh reading
of an inaccessible book.

| Source | Actual context(s) | Assessment |
|---|---|---|
| Aistleitner–Berkes–Seip | sections/1_introduction.tex:100; sections/2_product_forms.tex:36 | Correct ownership of finite Poisson positivity, product kernels and finite GCD norm context. The exact preprint §3 Lemma 1 locator is version-marked in the bibliography. |
| Bingham–Goldie–Teugels | sections/4_critical.tex:7 | The exact measurable UCT statement is displayed; no uninspected page number, Potter estimate or stronger regularity theorem is claimed. The writer transparently reused checked C403 metadata, not a fresh full-book reading. |
| Hilberdink | sections/1_introduction.tex:104; sections/4_critical.tex:72 | Proposition 2.1 is credited for arbitrary-coefficient finite Gram algebra. The specialization is rederived. Accepted-manuscript access is recorded in the frozen author source audit; this review does not turn its own earlier anti-bot failure into a fresh full-text attestation. |
| Hilberdink–Pushnitski | sections/1_introduction.tex:109 | Compact/Schatten comparison stays within the source's stated subcritical range. The text does not silently drop the even-exponent qualification or claim endpoint coverage. The 2023 English-edition metadata is distinguished from the 2021 consulted preprint. |
| Simon | sections/1_introduction.tex:119; sections/2_product_forms.tex:155; sections/3_variational.tex:75 | The largest closable minorant and canonical decomposition are correctly prior-owned. Section 3's monotone theorems are explicitly not asserted to be an arbitrary-entrywise theorem. This closes the earlier source amendment at manuscript level. |
| Yafaev | sections/1_introduction.tex:124; sections/2_product_forms.tex:147 | The form/closed-operator distinction and positive-symmetric-operator closability fact are correctly used. The one-circle criterion is not transferred without proof to an infinite-prime space. |

The bibliography's exact identifiers and access scopes agree with the
writer's citation record. The older independent source checks of
Aistleitner–Berkes–Seip, Hilberdink–Pushnitski, Simon and Yafaev remain
documented in the proof cross-review; they are not falsely presented as
newly repeated browser sessions here. No unresolved citation issue
required a new external search during this bounded conversion review.

A fresh source scan found all six keys used, no uncited entry, no
missing key, no missing reference label, and no duplicate label.
No TODO/FIXME/XXX/VERIFY/PLACEHOLDER text was found in the TeX/Bib tree.

## 5. Independent reverse outline and scope assessment

The actual text follows one coherent dependency sequence:

| Part | Role in the complete argument |
|---|---|
| Abstract and §1 | State the fixed-space summability dichotomy, define closability, and subtract known source ownership |
| §2 | Establish finite positivity, exact prime-shift identities and the closability boundary with explicit singular witnesses |
| §3 | Convert those witnesses to low-energy recovery for all positive entrywise approximants and prove the resolvent/norm conclusions |
| §4 | Identify the critical arithmetic entrywise kernel under the full written slow-variation hypotheses |
| §5 | Prove the different square-summable limit directly on the maximal rowwise domain |
| §6 | Realize both branches, check finite identities and a missing-hypothesis control, and delimit the fixed-space result |
| §7 | Summarize the single endpoint question and honestly disclose reproducibility and internal AI assistance |

All quantified proofs appear in the body. The article does not use a
proof-only appendix to hide domain or convergence obligations. The
abstract's strong-resolvent claim is consistent with the body, and the
nonzero entrywise limit is never mislabeled as a limiting bounded
operator in the divergent branch.

The conclusion does not promote the fixed unweighted-l2 obstruction
to an exclusion of other Hilbert spaces, normalizations, indefinite
models, or unrelated spectral constructions. It supplies no target
Euler factors, root numbers, zero correspondence or Hilbert–Pólya
realization. These are proper limitations, not unproved negative
classification theorems.

## 6. Compilation evidence and handoff boundary

Read-only checks confirmed the initial PDF's ten pages and byte size,
and no Warning/Overfull/Underfull/undefined/TeX-error match in the
current final main.log and main.blg. The preparer's receipt correctly
distinguishes the first pipeline's missing pipefail from the later
successful pipefail-enabled build, and records the actual small
overfull-box repair. No fresh compilation was performed in this review.

This reviewer did not conduct all-page image inspection and makes no
such claim. The preparer's three-page visual spot check is not upgraded
to final QA. The current verdict binds the author source digest and
initial PDF above; any later source change requires an affected-text
review and updated binding.

The research-review discipline was used for explicit hypotheses,
claim/evidence matching, source ownership, and adversarial domain and
quantifier checks. The pure-mathematics assignment excludes old-template
external-model calls, ML experimental quotas and conference scoring.
No code was rerun and no evaluation or release artifact was edited.
