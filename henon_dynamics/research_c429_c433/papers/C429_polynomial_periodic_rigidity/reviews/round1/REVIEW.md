# C429 — actual manuscript review, pass 1

Title: *Polynomial periodic-data rigidity for unicritical maps in finite characteristic*.

Current-team nonauthor mathematical reviewer: `/root/c429_e4_cover_review`. This is the first review of the actual manuscript, not a repetition of an earlier research-package review. The review was completed against the author baseline identified below; the actual clock checkpoint during completion was 2026-09-09 20:59 UTC.

## Recommendation and scope

**Minor revision. The central theorems and their complete typeset proofs pass this review. There are zero Critical findings, zero Major findings, and three Minor precision/locator repairs requested below.** No change to the all-prime, all-degree, all-parameter theorem or either finite bound is requested.

The manuscript proves that ordinary affine primitive-cycle sums for $f=x^d+c$ over $\overline{\mathbb F}_p$ characterize polynomial coboundaries, for every prime and every $d\ge2$. Its two-return theorem retains all three derivative regimes, constants and zero input, arbitrary algebraic coefficients, and native periods divisible by $p$. The main proof-bearing increment is present in the article: the full weighted carry bijection and the marked Hasse insertion argument, including source localization, wraparound control, deletion, and isolation of the new mark. No central step is replaced by a Markdown link, a sampled computation, or an unexplained finite-matrix assertion.

This is internal AI review, not human peer review, journal acceptance, a calibrated score, an exhaustive novelty search, or final release certification. Calibration status: `NOT_CALIBRATED`; no venue-specific criteria were selected. The coordinator supplied the abstract-cap concern and requested the preprint-locator check; both were independently checked here. The scalar omission was identified during this manuscript read. Nonauthor status does not imply blind review or independent error processes.

## 1. Exact read extent and frozen inputs

I read all ten active mathematical/BibTeX files: `main.tex` (49 lines), `math_commands.tex` (29), all seven included sections (171, 149, 175, 97, 254, 192, and 90), and `references.bib` (67): **1,273 lines in total**. I also read the complete 85-line `AUTHOR_RECORD.md`, all 23 entries of `BASELINE_FILES.sha256`, the applicable repository guidance and approved batch plan, and the four complete proof inputs listed below, totaling **1,770 proof-input lines**.

The actual 16-page `main.pdf` was checked with `pdfinfo`. A fresh read-only `pdftotext -layout main.pdf -` extraction hashes identically to the retained 823-line `build_attempts/02/main.txt`, which I read in full. Its SHA-256 is:

```text
29cdc6d87c6dee81ddb0693eb2d98840ff759a9dd9c55bb93a85c8bb68886133
```

All **23** snapshot members passed `sha256sum -c BASELINE_FILES.sha256`. The active mathematical files and PDF match the corresponding snapshot hashes. These checks establish byte identity, not theorem correctness. Mathematical conclusions below come from the full proof read and hand verification.

The review uses section, equation, and source-line anchors. I also inspected the retained rendered images named `page-01`, `page-02`, `page-10`, `page-13`, and `page-16`; this selected visual check is not a claim of an independent all-page visual release inspection. The algebraic-closure bars, three-regime table, adaptive-cut formulas, loss identity, and inspected references are legible. Reading the frozen final log found the already disclosed single underfull bibliography paragraph of badness 2173 and no further matching warning/error entries. No build was run.

## 2. Requested repairs

### W1 — declare the positive integer degree cap in the abstract

**Severity:** Minor. **Confidence:** high; direct abstract/body comparison.

**Evidence anchor:** absence: abstract, `main.tex` lines 32–35 — expected the positive integer domain of the logarithmic cap; checked the complete abstract and Section 1's definition and Theorem 1.2.

The abstract gives the logarithmic bounds under $\deg h\le M$ without saying $M\ge1$. A reader considering a constant observable could otherwise choose $M=0$, where the displayed logarithm is undefined. Section 1 explicitly fixes an integer cap $M\ge1$ and includes $h=0$, so this is not a defect in the finite theorem or its proof.

**Minimum repair:** replace the abstract clause with “for any integer $M\ge1$ and $\deg h\le M$”. Keep the zero-input convention and the existing bounds unchanged. No mathematical rerun or theorem weakening is needed.

### W2 — retain the scalar in the introductory description of the marked difference

**Severity:** Minor. **Confidence:** high; exact comparison with Proposition 6.1.

**Evidence anchor:** text: Section 1.1, `sections/01_introduction.tex` lines 151–154, “equal to the leading normal coefficient raised to a characteristic power”.

The actual identity is

$$C(n+1,s+1)-C(n,s)=\alpha a_D^P,$$

where $\alpha=(d-1)/P\bmod p\ne0$. It need not be one: $p=3$, $d=7$, $P=3$ gives $\alpha=2$. Equation (6.2), its derivation, and the later contradiction correctly retain this factor. Only the introductory description overstates the exact equality.

**Minimum repair:** say “equal to a nonzero scalar multiple of the leading normal coefficient raised to a characteristic power”, or state the exact $\alpha a_D^P$ formula. Do not alter the proposition or erase the coefficient Frobenius power.

### W3 — identify the actually inspected version in the residue locator

**Severity:** Minor. **Confidence:** high about the accessed version; no claim that published numbering is wrong.

**Evidence anchor:** text: Section 1.1, `sections/01_introduction.tex` lines 135–138, “global residues, and Jacobian traces”, with the Section 4 citation to `cattani1996residues`.

The displayed bibliography entry is the published chapter, whereas the actual full Section 4 inspected in the author record and this review is the accessible arXiv preprint. The publisher page supplied chapter metadata and an abstract, not that section's full text. The scientific comparison is supported; identical published section numbering has not been established by this access route.

**Minimum repair:** make the locator “Section 4 of the accessible preprint” while retaining the verified published reference and preprint link. This is an access/locator clarification, not a claim of a source mismatch or a mathematical dependency failure. The separate citation reviewer and coordinator may consolidate this item with their corresponding finding.

## 3. Substantive strengths

### S1 — the finite theorem states the original ordinary-data problem precisely

**Evidence anchor:** table: Table 1, all three rows, together with Theorem 1.2 and equation (1.5).

The tests are disjoint and exhaustive: $F_j\mid F_j'H_j$ for $p\nmid d(d-1)$, $F_j\mid H_j$ for $p\mid d$, and $F_j\mid D^{[P]}F_jH_j^P$ for $p\mid d-1$. Both adjacent returns are required, and the ordinary-root condition uses the whole return sum at every root, not only exact-period cycles. The period and iterate-degree statements are not presented as optimized runtime claims.

### S2 — the changing-length coefficient comparisons are complete proofs

**Evidence anchor:** equation: Propositions 3.1 and 6.1, equations (3.1)–(3.9) and (5.7)–(6.6).

The article supplies actual finite expansions, weight-preserving correspondences, and integer carry bounds. It checks all sources and all old marks, rather than proving only the existence of one attractive path. The new-mark contribution is derived by a nonnegative integer loss identity and an existence/uniqueness argument.

### S3 — multiplicity, characteristic two, and native time are addressed at the point of use

**Evidence anchor:** equation: Lemma 2.4, equation (2.1), Sections 4.2, 6.4, and the return formula in Section 7.1.

Ordinary-root vanishing is used only in its valid necessary direction into the full quotient. Integer exponents and repetition counts are kept distinct from field scalars. The smallest Hasse boundary $p=2,d=3,P=2$ is checked explicitly, and the skew-map interpretation preserves one application of the original map as a tick.

## 4. Detailed mathematical and transcription checks

### 4.1. Normalization, the full algebra, and leading detection

Lemma 2.1's elimination terminates because $\Delta_f x^t$ is monic of degree $dt$ and introduces only lower terms. A nonconstant coboundary has leading degree divisible by $d$, which proves trivial intersection with the specified normal space and uniqueness of $Q$ modulo constants. No invertibility of the integer $d$ is required.

In Lemma 2.2, elimination identifies the cyclic quotient with $k[x]/(F_n)$, of dimension $d^n$. The total-degree-lowering reductions span exactly $d^n$ legal digit monomials, proving their independence without squarefreeness. For Lemma 2.3, all terms remain inside a window of $m+1$ distinct sites, the unique no-constant branch has weight equal to the original exponent, and $e_0,e_m>0$ isolate the source when $n>2m$. The singleton case $m=0$ is included. Lower coefficients or characteristic cancellations cannot remove the isolated leading contribution.

Lemma 2.4 gives order at least $\max(e-E,0)+E\ge e$ at a root of multiplicity $e$. It does not require a bound on $e$ or nonzero Hasse coefficients. The manuscript correctly declines a one-level converse.

### 4.2. Ordinary carry stabilization and the first two regimes

In Section 3, the recurrence $t_s\le1+(r-1)/d^s$ reaches $\{0,1\}$ after $L=m+1$ steps. Normality gives $b_0\le d-2$, so the final carry at the source leaves a legal digit: no omitted second circuit remains. The source-localization proof uses the full target digit vector, and a drop at only the last step would make the target empty. Hence every contributing source is in the stated two blocks.

The insertion site $a=2m+2$ and its required successor are nonsources with zero outputs at sufficient distance from every allowed source. The two-output argument forces the weight-one $1\to1$ transition. The longer-level source blocks correspond exactly under relabeling, including exclusion of a source at the new site. Insertion and deletion are inverse on all contributing source/path pairs. Constants produce only the full-background monomial and have zero coefficient at the chosen short target.

Section 4 correctly extracts $d^nC_n=a_D=d^{n+1}C_{n+1}$. Stabilization and subtraction give $(1-d)a_D=0$, contradictory in the first regime. The derivative-zero branch instead uses $F_j'=-1$ and the leading detector directly. Constant normal parts are eliminated by the two adjacent integer scalars. The arguments have not silently required prime-to-$p$ return levels.

### 4.3. Hasse formula, adaptive cut, and localization

The coefficient-of-$z^P$ composition rule yields the stated marked backgrounds. It remains valid when $P=2$; no missing intermediate Taylor term is then introduced. The equality $\mathcal H_n(v)^P=\mathcal H_n(v^P)$ raises coefficients as well as monomial exponents, and $\gcd(P,d)=1$ preserves normal positive exponents.

The target digits are legal, and $d\nmid PD$ gives the indispensable first post-block digit at most $d-2$. For an adaptive nonsource cut, the distance condition ensures both the final carry bound and the predecessor bound in the suffix case. The final cut exponent is at most $d$. If it overflows, the extra unit carry leaves the cut with digit at most one, incompatible with the target $d-1\ge2$. In a contributing nonoverflow branch, adding the final carry does not change the original cut quotient, so the cyclic path weight is the genuine expansion weight.

The baseline identity is used only for indices below $n-1$, exactly where it holds. A nonpositive excess cannot become positive before the source; the selected interval reaches a zero target digit before encountering a source in both excluded source ranges. Constants are excluded by the same argument without a source. After localization, the common cut at zero has no overflow and gives $t_0=t_n=1$ with unchanged quotient and weight. Thus the later bijection uses one justified common path convention.

### 4.4. Pairing old marks and the unique new contribution

The source interval lies strictly beyond the insertion site and its neighbors. For every old mark, the inserted unmarked transition joins equal low baselines and has weight one. In the inverse direction, those baselines also agree when the mark is the predecessor or successor of the inserted site. No old mark, added source position, constant term, or zero-weight branch is omitted.

For the new mark, the forced incoming carry $P-1$ gives quotient zero and resets the carry. The first smaller target digit forces $i\le S$. Summing the exact conservation law with the specified integer weights yields

$$Pr=PDd^{S-i}+\sum_{u=i}^{N-1}\kappa_ud^{u-i+1}.$$

Here $r\le D$, $i\le S$, and every loss is nonnegative. Hence $i=S$, $r=D$, and all suffix losses are zero. The earlier baseline transitions are forced as well. The no-loss source recurrence gives the digits of $PD-1$, then carry one through the zero suffix; it exists, is unique, and has weight one. Including the derivative coefficient and observable coefficient gives exactly $\alpha a_D^P$, as correctly typeset in Proposition 6.1.

### 4.5. Constants, finite equivalence, bounds, and characteristic two

For a constant normal part in the Hasse regime, one selected return $j$ is prime to $p$. Each marked univariate term has degree $d^j-P$ and leading coefficient one; their sum has leading coefficient $j\alpha\ne0$. The displayed degree calculation is correct. The remaining divisibility therefore forces the constant to vanish. Zero input is handled separately, and no logarithm of its degree is taken in the theorem or proof.

In both mechanisms, coboundaries imply polynomial divisibility by telescoping; ordinary-root vanishing implies the applicable necessary derivative certificate; and the pair of certificates forces a zero normal part. This proves the stated three-way equivalence without asserting a false one-return converse. A failed ordinary-root test has value $(j/r)S_h(O)\ne0$, which implies a nonzero primitive sum without dividing in the field.

The exact choices give $n_J+1=3\lfloor\log_dM\rfloor+5$ and $n_H+1=7\lfloor\log_d(PM)\rfloor+23$, hence the claimed $d^5M^3$ and $d^{23}(PM)^7$ iterate-degree bounds. All uses of $P\ge3$ or $d-1\ge3$ from the earlier odd-characteristic wording have been replaced by the sufficient $P\ge2$ and $d-1>1$. Equal anchor/long-block digits at $p=2,d=3$ are harmless; the actual strict comparison is with an overflow digit at most one and with the smaller post-block digit. Even degrees in characteristic two use $F_j'=1$.

### 4.6. Consequences and excluded overclaims

The sign of the shear is correct: $\Phi_Q(x,y)=(x,y-Q(x))$ conjugates $T_h$ to $(f(x),y)$ exactly when $h=Q\circ f-Q$. Above a native base period $r$, the lifted period is $r$ or $pr$ according as the cycle sum is zero or nonzero; the argument remains valid when $p\mid r$. No inverse of the base or skew map is asserted.

Example 7.1 really passes every ordinary-Jacobian test for $c=0,h=x,d\equiv1\pmod p$, while the fixed point one has nonzero ordinary sum. It is correctly labeled a failed detector, not a counterexample to rigidity. The manuscript claims neither rational-observable rigidity nor a general-polynomial-base theorem, and it introduces no target Euler factors, root numbers, or spectral/arithmetic realization.

## 5. Accepted-input comparison and bounded source assessment

The R3 binary source/path argument, R4 general-digit proof and derivative-zero branch, R5 marked-background/adaptive-cut proof, and characteristic-two audit are all reproduced at their necessary proof-bearing extent in Sections 2–6. Changes of notation are consistent: the article uses $\Pi_n$ for the full background, $\mathcal H_n$ for its quotient class, and $H_n$ for the univariate return polynomial. The $P$th power on coefficients, source-digit correction, integer losses, two separate cut conventions, and exponents in both finite bounds have survived the transcription.

For the classical residue comparison, I freshly read the complete Section 4 of the [Cattani–Dickenstein–Sturmfels preprint](https://arxiv.org/pdf/alg-geom/9404011), including Lemma 4.2, Theorem 4.3, the Jacobian trace identity, Algorithm 4.8, and Theorem 4.9. These substantiate the normal-form/residue/trace antecedent. The [publisher chapter record](https://link.springer.com/chapter/10.1007/978-3-0348-9104-2_8) supplies metadata and an abstract, not a fresh full-chapter read. W3 preserves that distinction. The article proves its finite-characteristic algebra itself rather than importing complex contour formulas.

I also freshly read the relevant quadratic derivation in Section 4 of the [1998 author PDF](https://cns.gatech.edu/~predrag/papers/contourNonl.pdf), through equations (24)–(28) and the explicit attribution of the finite matrices to Levin–Sodin–Yuditskii. This supports the stated antecedent and attribution. I did not obtain or audit the 1994 original theorem/proof. The manuscript's explicit access limit and its statement that no unread theorem is invoked are therefore appropriate; deleting that disclosure would not be justified.

The remaining Livšic citations are contextual, not logical inputs to the proof. Their metadata and detailed source access are also assigned to a separate citation review; I do not certify a fresh full read of those papers here. This review neither reopens the entire prior novelty search nor asserts absence of a later or closer result.

## 6. Criterion-bound disposition

The applicable criteria come from the approved batch's C429 contract and full-proof/source-honesty requirements, interpreted for a proof-only mathematical article.

| Criterion | Judgment | Evidence and reason | Scope / decision bearing |
| --- | --- | --- | --- |
| Original theorem and parameter preservation | MEETS | Theorems 1.1–1.2; Sections 4 and 6 retain all primes, degrees, coefficients, and ordinary periods. | No new domain extension certified; supports mathematical pass. |
| Proof rigor and self-containedness | MEETS | Lemmas 2.1–2.4 and Propositions 3.1, 6.1 contain the complete algebra and path arguments. | Current-team hand review, not formal verification; supports mathematical pass. |
| Evidence sufficiency and argument coherence | MEETS | Integer carry bounds and bijections feed the exact two-level contradictions. | No empirical data or recomputable statistical claims; no experiment required. |
| Expository precision | PARTLY_MEETS | W1 and W2: the abstract cap and introductory scalar need limited correction. | Decision-bearing Minor repairs; core proofs unchanged. |
| Source applicability and disclosure | PARTLY_MEETS | Section 1.1 separates antecedents from proof inputs and discloses the unread 1994 text; W3 sharpens the inspected-version locator. | Bounded source check, separate citation audit outstanding; no priority certificate. |
| Consequence scope | MEETS | Section 7's shear, native periods, and blind-test example are proved with explicit limits. | No target-arithmetic or general-base implication; supports mathematical pass. |
| Venue fit, worldwide priority, final reproducibility | NOT_ASSESSED | No venue selected; no exhaustive search or final clean builds performed by this reviewer. | Cannot be inferred from this recommendation. |

## 7. Hash ledger

Paths in this first table are relative to the C429 manuscript directory. Each value was actually read from `sha256sum` and matches the assigned baseline.

| Input | SHA-256 |
| --- | --- |
| `main.pdf` | `118733318d139821d5cb29ab8deccc9d46fe577230563fbd38858df7ea431a02` |
| `BASELINE_FILES.sha256` | `225084568d2c0def64a3171248306d29fe688a24616fba55c3ee73f33c3f974d` |
| `AUTHOR_RECORD.md` | `4a1b11611b2b9ec2279e85ff023ce3601d178a1b87a27e72e6deed3dc785cfd6` |
| `main.tex` | `e8af703473b863355e39c809650f1a0d7da98432747ea8d5a1474775895b6b27` |
| `math_commands.tex` | `08d91e8041f21be8f5f08a273468daef71a75262e65efc0d6508b7b818b4e40d` |
| `references.bib` | `2572ac5a6b6be971085d89df647042ea43f62df451b8c65962f31466db22f04b` |
| `sections/01_introduction.tex` | `4261b94f9cdb2ee8f8344240657e61593066e916fd02bb56fca7de57acede495` |
| `sections/02_periodic_algebra.tex` | `5eda56a89a9d279180b42e0289ce5d57f315d0e87e374b9e148d4d54154fd1f2` |
| `sections/03_carry_stabilization.tex` | `0c10b30eac8d3cbf3b34b8d6f133a009cd27b9b1c3f9c6d8b0c70141006146e3` |
| `sections/04_jacobian_regimes.tex` | `3ebb7dd19724c1cedfa0d3e1c158ce65a7f8c4bc04268b85b90f0c4ff283367a` |
| `sections/05_hasse_paths.tex` | `8891ca9a50f08062be10d4ccc2d9cec62603f4ed144b4b89971a63d6469a2386` |
| `sections/06_marked_insertion.tex` | `8e041a4fce45ff486c4718409a065984ddb2c7c8ca7d0104ed3698a7eb9d8226` |
| `sections/07_consequences.tex` | `bb55c5c3603fb1ab1b942c1da7beb10816fcb9dfed7cdfa5eb4cd9ee8a37ce1b` |

The following paths are relative to `henon_dynamics/research_c429_c433/`. Each proof input was read in full, not merely sampled from a review summary.

| Accepted input | Lines | SHA-256 |
| --- | ---: | --- |
| `continuation_round3/a1_periodic_normal_form/PROOF_PACKAGE.md` | 444 | `06d0d06c1798b55d5a052b7ae3874bd176338ff31887a129b80041c5e1147450` |
| `continuation_round4/a2_unicritical_carry_extension/PROOF_PACKAGE.md` | 487 | `766f8d95f3297fdfe2b803965bc217ed28ccc7934090c07c68f42c9624f0cd01` |
| `continuation_round5/a2_excluded_congruence/PROOF_PACKAGE.md` | 517 | `b703fde520e5405b6ab28833a40dcce324925bebbbeaefea6b9ca22de57445e3` |
| `continuation_round5/a2_excluded_congruence/CHARACTERISTIC_TWO.md` | 322 | `0e7d600e2b35455aa5b93ffefef34c357d8a71e9fb3c20aa76dcf6f1be13d18a` |

## 8. Handoff boundary

The named auto-paper-improvement-loop skill was applied to this actual first review pass under the batch's current-team mathematical-review override. Proof-writer and the bounded ARS theoretical-review guidance supplied the full-proof, scoped-severity, and source-access checks. Their older external-model, ML-venue, numeric-score, and automatic-revision defaults were not executed. No complete ARS panel or calibration run is claimed.

Only this allocated review file was written. No source, bibliography, PDF, snapshot, author record, shared file, evaluator, Git state, or earlier proof/review was edited. No mathematical program, new agent, model/API upload, or build was run. The existing underfull bibliography paragraph is a readable, nonblocking typographic observation, not an additional mathematical finding.

There is no unresolved mathematical question for the author to answer in this pass beyond making the precise limited repairs above. The coordinator should adjudicate W1–W3 alongside the separate citation report, then authorize the actual revision. A later second manuscript review must inspect that real revised source/PDF and its response to these items in this same review thread; this report does not pre-certify a revision that has not occurred. Final deterministic builds and release checks remain separate gates. `NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.
