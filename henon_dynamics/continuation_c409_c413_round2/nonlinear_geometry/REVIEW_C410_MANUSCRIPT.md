# C410 actual-manuscript review

Date: 2026-09-06 (UTC). Reviewer: `scout_nonlinear_return`, a current-team non-author of C410. Reviewed object: `papers/C410_wild_cubic/`, *Wild cubic inverse-image towers in characteristic three*.

## Decision and its exact scope

**PASS for the stated source-mathematics manuscript, with two optional precision edits below.** No blocking mathematical error, missing main proof, incompatible quantifier, or unsupported promotion of the classical group was found in this actual full draft. This is an independent manuscript assessment, not an external-journal acceptance, exhaustive priority certification, or a Route-A/A0 pass. No target Euler product, functional equation, root number, zero correspondence, or Hilbert–Pólya operator is supplied by the paper.

I read `main.tex`, `math_commands.tex`, every file `sections/0_abstract.tex` through `sections/8_conclusion.tex`, and all six entries of `references.bib`. I also read the author's citation audit, reverse outline and build report, but the mathematical conclusions below come from checking the actual proofs, not from adopting those reports or the earlier root-level proof review. I extracted the actual PDF text, including its complete bibliography, and inspected rendered pages 3, 5, 9, 10, 11 and 13. This is not a claim to have performed the root agent's separate all-page visual QA. No author source was edited, no old mathematical checker was rerun, and no new build was run for this review.

The `research-review` workflow was applied as a claim-by-claim non-author review using the current team, under the repository's current-agent review convention. No old external-MCP review session is asserted.

## 1. Claims actually proved

| Statement | Domain and claim | Manuscript proof | Assessment |
| --- | --- | --- | --- |
| Theorem 2.1 | Every field `k` of characteristic 3, including imperfect fields; every `a != 0`; transcendental `t`; all inverse-image heights `n >= 1`. Arithmetic and geometric tree groups equal the classical `E_n` in one compatible labeling; the function fields are regular over `k`. | Sections 3, 4, 5 and 6, especially the joint induction and Section 6.5 descent. | Supported. Neither a square root of `a` nor perfectness of `k` is assumed. |
| Theorem 2.2 | After algebraic closure of the constants, exactly the sibling square-class relations, global Artin–Schreier rank `3^n`, completely split quadratic step at infinity, and local additive rank exactly 1. | Proposition 5.2, Lemma 6.1, Propositions 6.2–6.3. | Supported. The global and local ranks have genuinely different proofs. |
| Theorem 2.3 | Geometric branch set exactly `{0, infinity}`, explicit ramification indices and different exponents, and genus at all heights. | Lemma 5.1, Proposition 6.3, Proposition 7.1 and Riemann–Hurwitz in Section 7. | Supported. All local residue-field assumptions are confined to geometric constants. |

This is a theorem paper, not an experimental claim: the displayed heights 1 and 2 are consequences of the induction. The proof contains no inference from bounded computation to arbitrary height.

## 2. Base field, normal form, and signature upper bound

### 2.1 The cubic and first height

The normal form retains the necessary coefficient:

`beta^2 = alpha/a^3`, `z^3-z = beta`, and the three roots are `a(z^2-1)`, `a(z^2+z)`, `a(z^2-z)`.

The identity `f(a(z^2-1)) = a^3(z^3-z)^2` is correct in characteristic 3. The difference of the third and second roots is `az`, so the full root field contains `z` and then `beta`; this proves equality with the radical field, not merely an upper bound. Also `beta != 0` implies `z` is not in `F_3`, which directly confirms that the three expressions are distinct. The discriminant `a^3 alpha` and root product `alpha` have the correct signs. Thus a Vandermonde divided by `a^3`, not by an implicitly adjoined square root of `a`, gives the quadratic radical.

Irreducibility of `f^{circ n}(X)-t` follows from the prime quotient `k[X,t]/(f^{circ n}(X)-t) = k[X]` and Gauss's lemma. The derivative `(-a)^n product_{j=0}^{n-1} f^{circ j}(X)` has no common zero with the generic polynomial because 0 is fixed. Both arguments work over any characteristic-3 field. At height 1 the rational parameter `t=a^3(z^3-z)^2` has degree 6 and exactly the six automorphisms `z -> +/-z+j`; it supplies both initial induction facts `G_1=S_3` and `e_infinity=6`, with a regular rational field.

### 2.2 Compatibility is actually proved

Proposition 4.1 does not confuse a single leaf permutation sign with the recursive local relation. It first imposes

`product_{w child of v} Delta_w = a^3 Delta_v`

on the actual infinite inverse-image tree. The squared identity follows from the discriminant and product formulas. An odd reordering one height lower changes the needed sign without changing previously fixed Vandermondes higher up. Distinct parents involve disjoint corrections. Applying a Galois element then yields the local identity `s_v = product s_w` at every vertex with two levels below it. This proves the upper bound in one labeling at every height over the original `k`.

The order recurrence `|E_{n+1}|=3|E_n|^3` and the independent bottom `A_3` actions are valid consequences of the defined group. The proof explicitly delays use of these bottom actions for the actual Galois group until the current-height equality is known.

## 3. Joint induction and the two radical ranks

### 3.1 Tame zero-place geometry is independent of next-height maximality

The only finite critical value of the root cover is 0. Over algebraically closed constants, taking local conjugates and a compositum introduces no ramification away from 0 and infinity. At 0, every root-cover ramification index is a power of 2 dividing `2^n`, with `2^n` attained at the zero root. The local extensions are tame, and their local Galois compositum therefore has least-common-multiple index `2^n`.

With normalized upstairs valuation, `v_P(t)=2^n`. Monicity gives integrality of every root. Exactly `2^n` roots reduce to 0 because that is the multiplicity of 0 in the reduced iterate. At a zero-reducing root the first nonzero local term of the iterate has degree `2^n`, so its valuation is exactly 1; all other roots are units. The reduced child equation `X^2(X+a)=0` gives exactly the stated parity patterns on sibling triples.

### 3.2 Exact Kummer relations, not just an upper bound

The parity vectors lie in the direct sum of the two-dimensional even spaces on sibling triples. A bottom three-cycle, available from the *current* induction hypothesis `G_n=E_n`, lets the proof subtract two conjugate parity vectors and isolate a nonzero even vector on one triple. Its cyclic translates span the whole even space there. Transitivity on bottom parents propagates this to every triple. Hence the parity span has dimension `2*3^{n-1}`.

Orthogonality forces every square-class relation into the span of disjoint sibling indicators. The converse is established inside the already available splitting field by

`product_{f(alpha)=eta} (alpha/a^3) = eta/a^9 = (beta_eta/a^3)^2`.

The parent radical `beta_eta` is already in the current field by its child Vandermonde; this also works for `n=1`, `eta=t`. Therefore the relations are exact. The relation code has no word of weight 1 or 2, proving that individual square classes are nonzero and pairwise distinct. The quadratic degree follows from the proved elementary radical-degree lemma.

### 3.3 Pole-one classes and global independence

The second current-height induction hypothesis `e_infinity=2*3^n` gives every depth-`n` root valuation `-2`: the monic leading term has uniquely smallest valuation. All quadratic radicands have even valuation and geometric units have square roots by Hensel's lemma. Therefore the entire quadratic extension splits at each infinity completion and every `beta_alpha` has valuation `-1` there. This proves that each global Artin–Schreier class is nonzero, since an Artin–Schreier image with a pole has pole order divisible by 3.

Individual nonvanishing alone would not prove independence. Proposition 6.2 supplies the missing argument: the exact Kummer relations give distinct nontrivial characters of the elementary abelian 2-group `H=Gal(Mbar_n/Lbar_n)`. The quotient by the Artin–Schreier image is an `F_3[H]`-module, and `|H|` is invertible in `F_3`. Each finite character projector isolates one of the nonzero classes. This is valid even though the ambient quotient may be infinite-dimensional. Thus all `3^n` classes are globally independent.

The reverse inclusion in the splitting-field identity is present: the child Vandermondes recover the quadratic radicals and differences of child roots recover `z_alpha`. The compositum is exactly `Lbar_{n+1}`, so the global additive degree is really `3^(3^n)`.

### 3.4 Local rank exactly one

At a fixed geometric completion the leading coefficients of two roots have ratio whose `3^n`-th power is 1. In characteristic 3 this forces residue ratio 1. Consequently two quadratic radicals have residue ratio `+1` or `-1`; since both have pole order one, their principal parts cancel after that sign change. Their difference is integral and hence an Artin–Schreier image by Hensel's lemma over the algebraically closed residue field. Every class is still nonzero, so the local span is exactly one-dimensional, not merely at most one-dimensional.

The resulting local additive extension has degree and ramification index 3. The quadratic step was split, yielding the next infinity index `2*3^{n+1}`. The argument does not incorrectly apply the global character projectors to one fixed completion: the manuscript explicitly notes that those automorphisms need not preserve that place.

### 3.5 No circularity

The actual dependency order is:

1. Current `G_n=E_n` gives the exact Kummer rank via zero-place geometry.
2. Current infinity index gives split quadratic completions and pole-one radicals.
3. Character projectors give the global additive degree; principal parts separately give the local additive degree.
4. The global degree ratio equals `|E_{n+1}|/|E_n|`, forcing the next group using the previously established upper bound; the local calculation supplies the next infinity index.

Neither next-height group maximality nor the different/genus formula is used to establish the ranks. The simultaneous induction is complete with the explicit first-height base case.

## 4. Descent, ramification, different, and genus

### 4.1 Arbitrary and imperfect constants

The geometric degree is `|E_n|` and cannot exceed the arithmetic degree. The original-field signature bound bounds the arithmetic degree by the same quantity. Equality therefore identifies the two tree actions in the same labeling. The natural finite-dimensional multiplication map

`L_n tensor_{k(t)} kbar(t) -> kbar L_n`

is surjective and the equal dimensions make it an isomorphism to a field. Together with separability of `L_n/k(t)`, this is the usual separably generated/linear-disjointness criterion for regularity over `k`. The proof does not identify “no extra separable constants” with regularity while overlooking purely inseparable constants: it has extended to the full algebraic closure and separately proved separability over `k(t)`. A finite purely inseparable constant extension in `L_n` would contradict that separability. The inverse-limit assertion respects restriction because the signature labeling was chosen once on the infinite tree.

### 4.2 Different normalization

At 0, tameness yields `d_0=2^n-1`. At infinity, in the single-root rational field put `u=1/X` and `h(u)=u^3/(1+au)`. Both `ord_u h=3` and `ord_u h'=3` are correct, with `h'=-au^3/(1+au)^2`. The chain rule gives the root-field different exponent

`3*(1+3+...+3^{n-1}) = 3(3^n-1)/2`.

Its root completion has degree `3^n` over the base, whereas the proved geometric Galois completion has degree `2*3^n`; residues are the same algebraically closed field. The relative degree is therefore 2 and tame, with different exponent 1. Transitivity must multiply the root-field different by 2, and the manuscript does so, obtaining `3^{n+1}-2`. This avoids confusing the root cover's different with that of the splitting cover.

### 4.3 Branch set and Riemann–Hurwitz

Both branch indices exceed 1 for `n>=1`, so the earlier support containment is upgraded to the exact set `{0,infinity}`. With `N=|E_n|`, the contribution is

`2g_n-2 = N[-2+(1-2^{-n})+(3/2-3^{-n})]`.

The signs, normalization and place counts agree with Theorem 2.3. At height 1 the formula gives genus 0; at height 2 the data `(N,e_0,d_0,e_infinity,d_infinity,g)=(648,4,3,18,25,46)` are consistent. These observations are arithmetic substitutions in a proved formula, not a replacement for the all-height proof. No assertion about arithmetic residue degrees over the original `k` is made.

## 5. Independent near-source and bibliography check

The comparison is to the cited versions, not to an asserted exhaustive literature search. I opened primary sources independently during this review on 2026-09-06:

- Benedetto–Faber–Hutz–Juul–Yasufuku: the publisher's full article explicitly gives the characteristic-zero realization for `-2X^3+3X^2` in Corollary 1.3, defines the ternary `E_n` in Section 2, and gives the identical order in Proposition 2.2. The draft's attribution of the group and order is correct. [Publisher full article](https://link.springer.com/article/10.1007/s40993-017-0092-8).
- Bouw–Ejder–Karemaker: the publisher's Theorem 2.3.1 identifies the appropriate normalized Belyi geometric groups with `E_n` over characteristic-zero constants. It is relevant classical context, not a theorem that already covers this wild characteristic-3 map. The publisher and university repository support volume 165, pages 1–34 and issue-year 2021; online appearance in 2020 is not a conflicting publication year. [Publisher article](https://link.springer.com/article/10.1007/s00229-020-01204-3), [Utrecht repository](https://dbc.library.uu.nl/handle/1874/410845).
- Ejder: Definitions 2.1–2.2 of the actual arXiv PDF give the product-sign map and recursive `E_n` used in the manuscript. The paper's number-field monodromy setting is also explicit. The author's university-hosted CV confirms the final volume 779, pages 91–102, AMS, 2022 metadata. The direct AMS chapter endpoint was unavailable in this session; it was not represented as read. [Author's paper](https://arxiv.org/pdf/2201.09005), [Author's publication record](https://cdn.ku.edu.tr/resume/OZEJDER.pdf).
- Adams–Hyde: the cited `2504.13028v1` abstract, introduction and Theorem 1.1 explicitly assume power-unicritical form and degree prime to the characteristic. The draft accurately describes this scope. [Specified v1 full text](https://arxiv.org/html/2504.13028v1).
- Hlushchanka–Lukina–Wardell: the cited `2507.05033v1` Theorem 1.5 is over number fields. Remark 1.6 describes an *expected* extension to characteristic prime to 2 and 3. The draft says “discusses extension,” not that this extension is proved; it correctly excludes characteristic 3 from the stated comparison. [Specified v1 full text](https://arxiv.org/html/2507.05033v1).
- Stichtenoth: the publisher confirms the second edition, 2009, GTM 254, and the chapter on extensions of algebraic function fields. The subscription chapter body was not obtained in this review. Accordingly, the audit verifies the broad classical attribution and metadata, not an unexamined precise theorem locator. The manuscript gives the radical-degree and elementary local proofs itself and explicitly states the different and Riemann–Hurwitz tools. [Publisher book record and contents](https://link.springer.com/book/10.1007/978-3-540-76878-4).

No cited source is used to manufacture a novel abstract group. The differentiating content actually established in the manuscript is the wild characteristic-3 realization, the arbitrary-constant-field conclusion and the simultaneous global/local radical and ramification analysis. Whether this exact family has another treatment outside these checked sources remains a priority-search question, not a proved mathematical conclusion here.

## 6. Narrative and boundary audit

The abstract states the all-height theorem and the two ranks; the introduction attributes the existing groups before claiming the new calculation; Section 2 fixes all base-field and valuation conventions; the proof order follows the stated dependency; Section 8 returns to the precise scope. There is a complete proof for each main theorem, not a result list with promised later arguments.

The following boundaries are stated in the manuscript itself, not merely in workflow notes:

- `n` is inverse-image depth, not ordinary forward period and not finite-field extension degree.
- `L_n` is the full generic splitting field; `t` is transcendental.
- No specialization `t=t_0` is asserted to have the full generic group.
- Geometric ramification and genus do not assert residue degree one over the original constants.
- The abstract group and its order are classical.
- Source arithmetic is not promoted to target Euler factors, a target functional equation/root number, an operator, or a correspondence with zeros.

These limitations are appropriate and do not contradict the main theorems. The present source-paper pass therefore leaves any strict target evaluation and A0 completeness to the separate formal evaluator and its evidence requirements.

## 7. Optional precision edits; no blocking requests

1. In Lemma 3.1's first proof paragraph (`sections/3_normal_form.tex`, around lines 30–33), “They are distinct because the polynomial is separable” is compressed: separability alone does not logically prevent listing one root twice. An optional stronger sentence is: “Since `beta != 0`, `z` is not in `F_3`; the pairwise differences are nonzero multiples of `z`, `z-1`, and `z+1`.” This is an immediate consequence of the existing hypotheses and does not alter the lemma or its proof mechanism.
2. In Section 6.5 (`sections/6_artin_schreier.tex`, final descent paragraph), an optional parenthetical could name the criterion as “`t` is a separating transcendence basis and the full algebraic constant extension preserves the degree.” The current tensor/separability argument is valid; this wording would make the imperfect-field conclusion easier to recognize for readers less familiar with regular extensions.

Neither point requires changing a theorem, a computed invariant, a cited source boundary, or the present decision. The reviewer made neither edit, respecting author-file ownership.

## 8. Artifact lock and handoff

The actual `main.pdf` is 13 pages, 407,977 bytes, with the anonymous title/author metadata. The viewed equation-rich pages show readable bars, exponent towers, class quotients, group projectors and different formulas; the bibliography is resolved. The whole actual PDF text contains all sections and references. The root agent remains responsible for its requested independent build/full-page release QA.

Reviewed SHA-256 values:

```text
9d16aa8a475bf2eca95ca95f768d62a8525b2f352afb868deea88c48114c745a  main.pdf
5928dfba0c047a381bba7f0b087d47dfa4fa34033351414a14f693bd31d40b23  main.tex
3513f0751777cae67f9100838dac3a0f674259e997a64d506dadc50604f2dccc  math_commands.tex
79a4656e2a9eca557a042b2183721317576841a8437fcd07bced38e70adf6c92  references.bib
2e5b0e98228c7d0779d3ed8b794da80635f8dc2a7ba7d78e2a744e6637a4d49a  sections/0_abstract.tex
c713b06250274959e3b15d198cdef6983eced066577986e9207a8345c0edaa4d  sections/1_introduction.tex
4e622589e2e8fbaab4d377488a7afda7826eac83a40bc3645bc412c875940b96  sections/2_statements.tex
874add6f86c5f8361e9524045657853befed70628d35bcf3b99c98201d3441c9  sections/3_normal_form.tex
339f2640e58a0427d11150ba37638a81da5ec92634c2a59e7d8ed8449b0f5a07  sections/4_signature.tex
9782d6b770002965eb1b181b50aaedacf57b22db44589a4a716c81c6da45fe36  sections/5_kummer.tex
010b3778f7fef5ccbcc11aed9b744e9f1f2661b7aa1f996b9d50fb64ee44e601  sections/6_artin_schreier.tex
138a23159a6b79fda5b2603a0f053f03f7a8ca8fa3f4c1331ae40a715213a4d3  sections/7_ramification.tex
cd756f172e50d075db5f70d8427604d075e70cd1ac74143af55530e679a0e38e  sections/8_conclusion.tex
```

Final manuscript disposition: the source theorem package is internally supported in the reviewed full draft. Preserve the classical attribution and all explicit clock/constant-field/target boundaries in any subsequent revision. No formal target metric is upgraded by this review.

## 9. Actual confirmation of the local precision revision

Confirmation timestamp from the session clock: 2026-09-06 16:03:48 UTC. After the author notified completion, I read only the affected first proof paragraph of `sections/3_normal_form.tex` (current lines 25–39) and its immediately adjoining context. This is a local revision confirmation, not another full review or a build/visual-QA pass.

The revised paragraph now explicitly uses `beta != 0` to deduce `z notin F_3` and lists the three nonzero differences. Writing the displayed roots in their existing order as `r_1,r_2,r_3`, the arithmetic is exactly

```text
r_2-r_1 = a(z+1),
r_3-r_1 = a(1-z),
r_3-r_2 = az                 (because -2 = 1 in characteristic 3).
```

Since `a != 0` and `z` is not any of `0,1,-1`, all three differences are nonzero. The three displayed expressions are therefore distinct roots; the following reverse-containment argument still recovers `z` from `r_3-r_2=az` and then recovers `beta`. The change is correct and resolves optional precision comment 1 in Section 7. Optional comment 2 was not required for the pass and was not included in this local check. The original source-mathematics disposition remains unchanged, with no new blocking finding.

The actual revised normal-form source SHA-256 is

```text
5f82f44d34e1994128be6237479642e85e98b24dee423b692d66c20fc4e2efe7  sections/3_normal_form.tex
```

The source/PDF hashes in Section 8 remain the historical lock for the initial full review. In particular, that listed PDF predates this local edit; this addendum does not certify a rebuilt PDF from the revised source. The root agent owns the fresh build and final PDF QA. I changed only this review addendum, did not edit any author file or C412 source, and did not rerun mathematical checkers or builds.
