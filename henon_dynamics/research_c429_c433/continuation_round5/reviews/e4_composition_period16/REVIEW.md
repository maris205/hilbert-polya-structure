# R5 E4 — Independent mathematical review of C2 class reduction and period-16 exclusion

## 1. Verdict and exact reviewed artifacts

**PASS / PROVABLE AS STATED** for the finite-cycle class-reduction lemma and the universal native period-16 exclusion, including its stronger $\mathbb Z_2^2$ conclusion. **Zero mathematical must-fix issues identified.** The exact universal integer spectrum is still **NOT CURRENTLY JUSTIFIED**: $9,12,18,24$ remain unresolved. This is an auxiliary-result review, not an independent-paper admission.

The reviewer read the complete actual files, not only the author's summary:

| Artifact | Complete read | SHA-256 |
| --- | --- | --- |
| `continuation_round5/c2_composition_exact_spectrum/PROOF_SUPPLEMENT.md` | All 338 lines, Sections 1–8 | `16ed4ea2b81d7a6b6c029b2c6fcd463716a0af9bd925bfb54d4747ee1ea35edb` |
| `continuation_round5/c2_composition_exact_spectrum/REPORT.md` | All 341 lines, including the complete diagnostic source and recorded output | `1e3d2e82de52341e686ebbf2bd48ee5c4b854c0b451dbbd7422495ee05308a0c` |

This is a separate current-team, nonauthor mathematical check. It is not human peer review, a cross-model review, a formal proof-assistant verification, or a calibrated reviewer-performance claim. `NOT_CALIBRATED`; `criteria_binding_unavailable`. No venue-alignment judgment is made. The proof-writer and research-review disciplines were applied within the batch's current-team, bounded, read-only contract; no external-model workflow or full ARS panel was run.

## 2. Claims, assumptions, and dependency map

The object is the semigroup $\mathcal H$ of all nonempty finite words in

$$
H_{p,\varepsilon}(x,y)=(y,p(y)-\varepsilon x),
\qquad p\in\mathbb Z[t],\quad \deg p\ge2,
\quad\varepsilon\in\{1,-1\}.
$$

There is no bound on word length, degree, height, or sign pattern. One complete chosen word is one native tick throughout.

The reviewed conclusions are:

1. The integer finite-cycle spectrum of $\mathcal H$ equals that of the integral tame subgroup $\operatorname{TA}_2(\mathbb Z)$. More precisely, each chosen finite tame cycle is preserved pointwise as a native permutation by some allowed nonlinear word.
2. No $F\in\mathcal H$ has a point of native least period $16$ in $\mathbb Z_2^2$, hence none in $\mathbb Z^2$.

The two proofs are independent. Class reduction uses elementary integral affine/triangular generation, finite intermediate supports, and vanishing-polynomial padding. The exclusion uses the derivative-sign character, the constant-Jacobian local four-cycle lemma, and a hypothetical cycle's residue period. The exclusion proof does not require the class reduction, the finite diagnostic, Pezda's upper spectrum, or Pezda's local eight-cycle lemma.

## 3. Class-reduction audit

### 3.1 Unrestricted factor generation

At proof lines 44–64, the unrestricted factors correctly give the swap $S(x,y)=(y,x)$ and quarter-turn $J(x,y)=(y,-x)$. Direct composition gives

$$
S\circ H_{p,-1}=U_p=(x+p(y),y),
\qquad H_{p,-1}\circ S=V_p=(x,y+p(x)).
$$

The products $S\circ J$ and $J\circ S$ give the two coordinate sign changes. Constant shears provide translations, integer linear shears together with swaps/sign changes generate $\operatorname{GL}_2(\mathbb Z)$ by the Euclidean algorithm, and triangular generators have the stated decompositions. Inverses introduce no coefficient-ring problem: the required negative shears and sign changes are already among these generators. An empty identity expression is correctly replaced by $S\circ S$.

Conversely, $H_{p,-1}=S\circ U_p$ and $H_{p,1}=H_{p,-1}\circ(-x,y)$ are integral tame. This proves the easy inclusion without claiming all integral polynomial automorphisms are tame.

### 3.2 Padding every intermediate support

At lines 66–109, each $E_i$ is the complete finite, nonempty second-coordinate support at stage $i$ of the original factor word, taken over every state of the selected native cycle. For each factor of degree at most one,

$$
\widetilde p_i(t)=p_i(t)+t^{\max(0,2-|E_i|)}\prod_{e\in E_i}(t-e)
$$

is integral, has degree at least two with no leading cancellation, and agrees with $p_i$ on all of $E_i$. The singleton-support case, the zero polynomial, and $0\in E_i$ are all covered.

The induction establishes equality of all intermediate states on every original cycle point, so the final word agrees with the original map on the entire cycle. Iterating that word therefore visits the same $n$ distinct states in the same order. Least period, rather than merely a return time or factor-step period, is preserved. Word length and degrees are correctly allowed to depend on the selected cycle; global conjugacy and exact interpolation of an arbitrary point permutation are not inferred.

## 4. Derivative-sign character audit

At lines 125–170, $\operatorname{GL}_2(\mathbb F_2)$ acts faithfully on the three nonzero vectors and has order six. Its ordinary permutation-sign homomorphism $\sigma$ has even-sign elements precisely the identity and the two order-three elements. An order-three element satisfies $A^2+A+I=0$.

For an integral polynomial automorphism with integral inverse, reduction is a permutation of the four base points and its derivative is invertible at every point. Thus

$$
\chi(T)=\prod_{q\in\mathbb F_2^2}\sigma(D\overline T(q))
$$

is multiplicative: the chain rule separates the two products, and $\overline U$ reindexes all four base points in the first product. This reindexing is essential and is valid for the maps under consideration.

For each Hénon factor the derivative modulo two is

$$
\begin{pmatrix}0&1\\1&\overline{p'}(y)\end{pmatrix}.
$$

For either value of $y$, its sign occurs twice, once for each $x$. Hence $\chi(H_{p,\varepsilon})=1$, and multiplicativity gives $\chi(F)=1$ for every finite allowed word. Both choices of $\varepsilon$ are included. The argument uses reduction of the formal derivative, not a derivative assigned to a finite set-map or an assumption that equal residue values imply equal derivatives.

## 5. Complete local four-cycle audit

The lemma at lines 176–282 applies to any integral polynomial map over $\mathbb Z_2$ with constant unit Jacobian determinant. It does not need a globally invertible polynomial map. Its conclusion is that a least four-cycle contained in one residue class has odd derivative sign.

### 5.1 Normalization and coefficient integrality

An integral polynomial map is congruence preserving. Applied cyclically to successive differences, this gives four successive valuation inequalities returning to the first value, so all finite valuations are equal to some $d\ge1$. Every cycle point differs from $z_0$ by a sum of such differences and lies in $z_0+2^d\mathbb Z_2^2$.

The substitution

$$
\widetilde g(X)=\frac{g(z_0+2^{d-1}X)-z_0}{2^{d-1}}
$$

has integral constant coefficient because $g(z_0)-z_0$ has valuation $d$. Every coefficient of positive total degree $k$ has a factor $2^{(d-1)(k-1)}$ after division. Translation by $z_0\in\mathbb Z_2^2$ uses integral binomial expansions. This also covers $d=1$, when no nontrivial scaling occurs.

The transformed four-cycle is even, begins at zero, and its first image $v$ satisfies $\nu(v)=1$. The scalar factors cancel in the derivative, preserving both the constant determinant and $Dg(z_0)$ at the new origin. The injective affine substitution preserves distinctness and least period. No unsupported inverse-map or isometry premise is used.

### 5.2 Even sign with order-three derivative

Write $A=Dg(0)$. At every even cycle point, the nonlinear Taylor terms lie in $4\mathbb Z_2^2$, giving $g(z)\equiv v+Az\pmod4$. Four iterations yield

$$
0\equiv(I+A+A^2+A^3)v\pmod4.
$$

For $u=(v/2)\bmod2\ne0$, division by two is legitimate and gives $(I+\overline A+\overline A^2+\overline A^3)u=0$. If $\overline A$ has order three, the parenthesized sum is $I$, contradicting $u\ne0$. This checks the normalization-dependent nonvanishing required by the Taylor argument.

### 5.3 Even sign with identity derivative

At proof lines 232–253, the displayed linear coefficients of the Jacobian determinant are correctly computed. With $a,h$ odd and $b,f$ even, their reductions are respectively the mixed quadratic coefficients $j$ and $d$. Higher-degree terms contribute no linear determinant coefficient. Constancy of the determinant therefore forces both $d$ and $j$ even.

Consequently $Dg(z)\equiv A\pmod4$ for every even $z$: pure quadratic derivatives have an explicit factor two, mixed quadratic derivatives now have even coefficients, and derivatives of higher-degree monomials have degree at least two in even coordinates. This is the substantive use of the constant-Jacobian hypothesis, not merely invertibility of $A$.

For $h_0=g^2$ and $w=h_0(0)$, the chain rule and $A=I+2B$ give

$$
Dh_0(0)=Dg(v)A\equiv A^2\equiv I\pmod4,
\qquad w\equiv(I+A)v\equiv0\pmod4.
$$

If $w=0$, the supposed four-cycle already has period dividing two. Otherwise $e_0=\nu(w)\ge2$ is finite. The equality $h_0(w)=0$ then becomes

$$
0=2w+4Cw+R(w),\qquad R(w)\in2^{2e_0}\mathbb Z_2^2.
$$

The last two terms have valuation at least $e_0+2$, whereas at least one coordinate of $2w$ has exact valuation $e_0+1$. They cannot cancel it. Both the zero-displacement and nonzero-displacement cases are complete. The two even-sign derivative possibilities are exhausted, proving the local lemma as stated.

## 6. Universal native-period contradiction and remaining spectrum

At lines 284–322, a hypothetical native least period $16$ reduces to a period $m$ dividing $16$ in a permutation of four points, so $m\in\{1,2,4\}$. The map $G=F^4$ has an actual least four-cycle on $P,F^4P,F^8P,F^{12}P$, all in one residue class. Its determinant is the constant $1$, since every factor determinant is $\varepsilon_i$.

The derivative sign of $G$ is the product of the four derivative signs of $F$ along the residue orbit. If $m=1$ or $m=2$, it is respectively a fourth power or a square. If $m=4$, these points exhaust all four residue points, and the product is $\chi(F)=1$. Every possible residue case therefore gives even sign, contrary to the local lemma. No residue period, sign pattern, coefficient, degree, or finite word length has been discarded.

The $\mathbb Z_2^2$ exclusion implies the integer exclusion by the natural embedding. The use of $F^4$ is an internal contradiction device and does not replace the native clock. Combined with the accepted imported attainments and upper theorem, the permitted partial statement is

$$
\{1,2,3,4,6,8\}\subseteq\mathcal S
\subseteq\{1,2,3,4,6,8,9,12,18,24\}.
$$

Composition closure makes the spectrum divisor closed: a witness for $18$ or $24$ produces one for $9$ or $12$ using an iterate as a new selected full word. Conversely, exclusion of $9$ or $12$ would exclude $18$ or $24$. Attainment of the smaller lengths alone does not settle the larger lengths. The report and proof retain this asymmetry and explicitly leave all four lengths unresolved.

## 7. Source ownership and evidence limits

The reviewer freshly read Pezda's primary article introduction/definitions, Theorem 2.1, and Proposition 3.3 with its normalization proof through a read-only PDF-to-text stream. Theorem 2.1 gives the displayed eleven-length union for general integral polynomial maps, not the Hénon-word attainability problem. Proposition 3.3 supplies the already classical translate-and-scale normalization of a congruent cycle. The new argument's constant-Jacobian preservation and subsequent parity/valuation reasoning were checked directly above. [Pezda, primary article](https://dml.cz/bitstream/handle/10338.dmlcz/120574/ActaOstrav_10-2002-1_10.pdf).

Browser access to the article and its landing page timed out; the subsequent bounded read-only stream succeeded. This review does not claim a fresh full proof audit of Pezda's upper theorem or local eight-cycle theorem, and it does not rely on the latter. Source locators here use theorem/proposition labels, not locally certified PDF-page anchors. No new PDF was written or compiled.

The reviewer also read the actual frozen C428 theorem/source section at `research_c424_c428/papers/C428_integer_period_spectrum/sections/01_theorem_sources.tex`. Its two single-factor unions have combined spectrum $\{1,2,3,4,6,8\}$ and exclude integer period nine for the single factor in the report's residue example. These are imported accepted results; the earlier computer-assisted exclusion certificates were not rerun or freshly re-audited.

The report's other bounded literature searches and access limitations are author source records, not searches freshly repeated by this reviewer. This audit makes no exhaustive-priority claim for the character or the 16-exclusion. Correctness of the auxiliary proof is separate from worldwide novelty, standalone substantiality, and the coordinator's admission decision.

## 8. Diagnostic and finite-residue controls — static review only

The complete code at report lines 78–239 matches the stated bounded question: $300$ factors, $90{,}000$ ordered two-factor words, and native plus intermediate states in the $81$-state box. The coefficient order, Horner evaluation, index conversion, partial-map composition, cycle extraction, canonical rotation, and per-word completion counter were checked statically. The traversal counts each directed cycle once for each selected word and imposes no period cutoff. Timeout/error outputs are explicitly partial and have nonzero exit statuses.

The marked-source extraction was rehashed read-only and matched `a2b9349d48fcfc97ea57d4d396abd0e06598e68d79402eacc4f1a4a807a5dca4`. This is byte binding, not a rerun or independent certification of the recorded counts. The stored receipt reports completion, $40{,}098$ word-cycle occurrences, six lengths, and no missing-length witnesses. The code and receipt jointly support the author's interpretation of its finite-window result; this reviewer did not reproduce the execution. No-hit is correctly kept separate from the universal exclusion.

The nine modulo-four transitions at report lines 309–319 were checked directly by substitution, including the outputs $40,39,42,17$ before reduction. The residue states are distinct. This is a valid native residue nine-cycle, not an integer or $\mathbb Z_2$ nine-cycle. Its failure to settle integer attainment is expressly stated. There is no newly emitted witness requiring another run.

## 9. Coverage receipt, corrections, and handoff

The empty must-fix list follows the completed checks below; no finding quota or favorable author status was used as evidence.

| Review dimension | Completed check and basis for no required correction |
| --- | --- |
| Quantifiers and clock | All finite allowed words, both signs, unbounded coefficients/degrees, and the whole-word native clock are retained. |
| Class reduction | Generator identities, integral coefficient ring, nonempty supports, padding edge cases, and equality of the full native permutation all check. |
| Derivative parity | Formal derivative reduction, chain-rule multiplicativity, four-base-point reindexing, and factorwise repeated signs all check. |
| Local lemma | Scaling integrality, derivative preservation, order-three contradiction, mixed-coefficient parity, derivative congruence, and both second-displacement cases all check. |
| Global contradiction | Residue periods $1,2,4$, constant determinant, actual four-cycle for $F^4$, and all derivative-sign cases are covered. |
| Evidence and scope | Finite diagnostic is not universal evidence; inherited results and non-fresh source checks are labeled; the exact spectrum and admission remain open. |

No author edit is required by this review. The author artifacts should remain bound to the hashes in Section 1; any mathematical change requires its affected reasoning to be checked again. No score, target-arithmetic promotion, or full-classification certificate is produced.

Only this assigned review file was written. No mathematical program, old checker, new/nested agent, author/shared-file edit, Git operation, manuscript/PDF build, formal evaluation, or external-model upload was performed. Exact diagnostic counts and timing remain the author's recorded execution evidence, not newly reproduced measurements.

## 10. Directed post-freeze addendum: all integral dyadic polynomial automorphisms

The coordinator subsequently read and accepted the original 179-line review and frozen proof as auxiliary mathematics, without a new admission. At the coordinator's explicit request, this addendum reviews only the newly appended report Sections 9–10 and their ambient-class deduction. It does not reopen the original complete proof or rerun any mathematical computation.

### 10.1 Historical and final byte bindings

The original 179 lines above remain unchanged. Their historical review SHA-256 is `0e866dbba4d2431fcb621c406195570aa4b8139d3614c91f44822b75d43e6572`; it identifies that pre-addendum review, not this subsequently enlarged file.

The initially assigned 367-line post-append report had SHA-256 `94df868a7664d7b5562d3e71ad66391d48b73dede026ce604955ab89518ccd05`. The reviewer read its new lines 342–367, requested only narrower ambient-class wording, and checked the author's resulting Section 9 revision, including its explicit constant-unit Jacobian clarification. The final 367-line report reviewed by this addendum has SHA-256 **`0b61d292915d2ab54c6047fea37a4908df9ffbdf07598a8766d5c6c530764e36`**.

Read-only extraction of the report's first 341 lines still gives `1e3d2e82de52341e686ebbf2bd48ee5c4b854c0b451dbbd7422495ee05308a0c`. The unchanged proof remains bound to `16ed4ea2b81d7a6b6c029b2c6fcd463716a0af9bd925bfb54d4747ee1ea35edb`. Report Section 10 correctly labels the earlier report/review hashes and earlier pending-review statements as historical. The new deduction was not retroactively included in the old review binding.

### 10.2 Ambient-class corollary: PASS / PROVABLE AS STATED

Let $T\in\operatorname{Aut}_{\mathbb Z_2}(\mathbb A^2_{\mathbb Z_2})$, meaning that $T$ and its polynomial inverse both have coefficients in $\mathbb Z_2$. Then $T$ has no point in $\mathbb Z_2^2$ of native least period $16$. This is the exact new claim; it is not a statement about arbitrary polynomial automorphisms over $\mathbb Q_2$ without an integral polynomial inverse.

The new interface checks are as follows:

1. **Reduction and field factorization.** The identities for the polynomial inverse reduce to inverse identities over $\mathbb F_2$, so $\overline T$ is a polynomial automorphism, not merely a permutation polynomial on four points. Jung–van der Kulk applies over every field, hence over $\mathbb F_2$, giving a factorization into affine and elementary maps there. No factorization over $\mathbb Z_2$ is asserted or needed.
2. **The character on generators.** The previously checked multiplicativity argument defines $\chi$ directly on $\operatorname{GA}_2(\mathbb F_2)$. For an affine map with linear part $A$, its character is $\sigma(A)^4=1$. For an elementary shear $(x+f(y),y)$, each derivative matrix occurs for both values of $x$, and the two signs square to one; the other shear orientation has the same repeated-coordinate argument. Triangular maps are covered by affine and elementary generators. Therefore $\chi(\overline T)=1$, with formal derivatives retained throughout.
3. **Constant unit Jacobian.** If $U=T^{-1}$, the polynomial identity $DU(T(X))DT(X)=I$ shows that $\det DT$ is a unit of $\mathbb Z_2[x,y]$. Because the coefficient ring is a domain, its polynomial-ring units are constant, so $\det DT=\delta\in\mathbb Z_2^\times$. Thus $\det D(T^4)=\delta^4$ is a constant unit. It need not equal $1$; the already proved local lemma assumes only a constant unit and therefore applies without alteration.
4. **Native contradiction.** A native $16$-cycle for $T$ would give a least four-cycle for $T^4$ contained in one residue class. Its original residue period is $1,2$, or $4$. The same fourth-power, square, or full-character product respectively gives even derivative sign, contradicting the accepted local four-cycle lemma. This uses the original native clock and covers every allowed $T$ and every point of $\mathbb Z_2^2$.

No new local lemma or proper-containment theorem is missing. The revised phrase “broader ambient-class” avoids making strictness or integral wildness an extra premise. The ambient class contains the original integral Hénon-word class, but this argument neither identifies all integral automorphisms with integral tame automorphisms nor requires proof of a strict inclusion between those integral groups. The wording request was a scope clarification, not a mathematical counterexample or a weakening of the new corollary.

### 10.3 Focused primary-source readback

**Bell–Ghioca–Tucker.** The reviewer freshly read Theorem 1.1 and Proposition 2.1 with its complete near-identity congruence proof from the linked author PDF, and checked the version record. For the orbit of a $\mathbb Z_2$ point, the smooth-point hypothesis of Theorem 1.1 is satisfied by that point's section. With $p=2$, $e=1$, and dimension $g=2$, its integer $r$ is $1$, not $0$, because the inequality is strict. The displayed bound is therefore $2^{1+1}\cdot6\cdot4=96$. This bound does not exclude $16$, and the inspected congruence argument does not supply the specific mixed-quadratic coefficient obstruction. This is a bounded source comparison, not a claim to have audited every result in that article. [Author PDF](https://personal.math.ubc.ca/~dghioca/papers/burnside_revision.pdf), [version record](https://arxiv.org/abs/1310.5775v2).

**Maubach–Willems.** The reviewer freshly read the versioned preprint's introduction, generator definitions, and Theorem 2.1. The stated field-factorization theorem covers $\mathbb F_2$. Its introduction's parity discussion is about induced permutations of finite-field points, so the distinction between $\mathbb F_4$ and $\mathbb Z/4\mathbb Z$ is correct. The factorization is a classical imported input; the derivative-character application and dyadic corollary are deductions here, not statements attributed verbatim to that source. The original Jung/van der Kulk proofs and published 2011 article were not freshly audited. [Versioned preprint](https://arxiv.org/html/0912.3387v1).

**Allen–DeMark–Petsche.** The reviewer also checked the linked v3 abstract/version record: its stated setting has odd residue characteristic. That accessed statement does not supply a dyadic period-$16$ theorem; no full-text audit is claimed. [Primary v3 record](https://arxiv.org/abs/1610.04271v3).

These checks support the two substantive source-scope paragraphs and the third abstract-level exclusion in report Section 9. They do not reproduce the author's entire negative search or certify priority of the present exclusion. Historical failed-access descriptions remain the author's provenance records, not new successful reads inferred by this reviewer.

### 10.4 Directed disposition

**PASS**, with zero open mathematical or source-applicability must-fixes for this ambient-class corollary and the checked appended source/status scope. The one wording clarification was implemented by C2 only within the new report Section 9 and read back here. The original proof and original report prefix are unchanged. The universal integer spectrum, the four lengths $9,12,18,24$, worldwide source priority, and any independent-paper admission remain unresolved/separate. New investigation assignments recorded in Section 10 are not treated as accomplished mathematical results or as authorization for this reviewer to join those investigations.

This directed follow-up added only this review section. It used read-only source access and byte checks, with no mathematical program, old proof rerun, author/shared-file write, additional agent, Git action, manuscript/PDF build, or external-model upload.
