# Independent bounded audit of the nonaffine-characteristic-p scout

Date: 2026-09-06. Reviewer: sibling arithmetic scout, independently of the author of the five audited files. This is an AI-team proof/source audit, not external human peer review or a complete review of the cited papers.

## Verdict

**The recommendation of zero retained contracts is supported.** No mathematical defect was found in the stated Witt or Markov short proofs. One substantive source-use caveat was found in candidate A: the literal odd-cycle factors in the accessed isogeny paper cannot be certified as correct. This does not undo that paper's ownership of the proposed framework, but it must accompany any claim of its exact theorem coverage. A small correction to an already-owned framework is not promoted here into a new paper contract.

| Audited target | Result | Boundary |
|---|---|---|
| B, Witt translation and all Frobenius-twisted iterates | Pass | Hidden commutative algebraic-group structure is explicit; the translation itself is not an identity-preserving endomorphism |
| C, Markov parabolic twist and all iterates | Pass | Odd characteristic, κ∉{0,4}, any integer k, every n≥1; all exceptional fibers included |
| A, isogeny source ownership | Pass with source caveat A1 | Definition/framework ownership is real; literal general odd-cycle formula has a reproducible sign error |
| Nine recorded Gröbner checks | Code/result scope inspected; not rerun | They remain finite checks, not independent all-period evidence |

## 1. Scope and inputs

Read all of [SCOUT_REPORT.md](../nonaffine_charp/SCOUT_REPORT.md), [PROOF_PACKAGE.md](../nonaffine_charp/PROOF_PACKAGE.md), [SOURCE_AUDIT.md](../nonaffine_charp/SOURCE_AUDIT.md), [exact_probe.py](../nonaffine_charp/exact_probe.py), and [exact_probe_results.json](../nonaffine_charp/exact_probe_results.json). Applied the targeted proof-writing/research-review disciplines: check quantifiers, hidden structure, all exceptional cases, and actual primary-source theorem context. No full ARS review pipeline, paid external model, old result rerun, evaluator, registry, CURRENT file, or Git mutation was used.

Initial reviewed SHA-256 values, before the requested source caveat is incorporated by the lane owner:

| File | SHA-256 |
|---|---|
| SCOUT_REPORT.md | `e426f81d37c7f7aa1d1a307067653f55ddd223c082b39a2547e510ef10a86f2d` |
| PROOF_PACKAGE.md | `196cbc83a8deea393dd612fae451f098288258b2966d19b44203604aa492c0ee` |
| SOURCE_AUDIT.md | `b666614c7c0da8e770c121e609da3ed6887ab861978fc611642ee09a5953f146` |
| exact_probe.py | `480b35734d22c6fb59690b686ff6fd1744753342f2213bfcb87e3ed224691a53` |
| exact_probe_results.json | `7181dc00a8995fc9f8353349fada9ac05a3364784b81055c0f41c6bf9c82649d` |

This reviewer wrote only the present file. The five audited files belong to the other lane.

## 2. Witt proof: hidden group and precise clock

The polynomial C_p is integral before reduction. The displayed addition law follows from the first two Witt ghost equations, and the cocycle identity makes associativity directly checkable. In particular, S_p is translation by e=(1,0) on W₂, and not a new non-group map merely because its second coordinate is nonlinear. The calculation p e=(0,1), p² e=0 gives exact order p², so ordinary finite geometric fixed-point counts already fail at that period.

For F=S_p^k Fr_q, commutation is valid because the group law and translation are defined over F_p. The two displayed fixed equations each have Q=qⁿ distinct roots in their respective variable. This proves Q² simple points for every n, even when p divides n or k is negative. The translation conjugacy has the correct sign: choosing Fr_q(b)−_W b=−_W(k e) gives τ_b⁻¹ F τ_b=Fr_q.

Independent primary context checked: Hazewinkel's addition/ghost construction and truncation discussion, §§5.9–5.14 and 7.1. It supports identification with W₂; the explicit finite counting argument does not require importing an endomorphism theorem for a translation. The scout correctly keeps those distinct. [Hazewinkel, *Witt vectors. Part 1*](https://arxiv.org/pdf/0804.3888)

## 3. Markov proof: all n and every exceptional fiber

The inverse of T and preservation of the cubic are correct. Writing Fⁿ=T^{kn} Fr_Q is legitimate for all k∈Z because T is defined over F_q. A fixed point has z=t∈F_Q, and A_t is invertible. The proof does not replace geometric fixed points by the finite permutation on X_κ(F_q).

The eigen-coordinate identity was checked directly: for λ²−tλ+1=0, u=x−λy satisfies u(TP)=λu(P), and uv=κ−t². On split smooth fibers the equation has Q−1 roots. On nonsplit smooth fibers Frobenius exchanges u and v, giving u^{Q+1}=λ^{kn}(κ−t²), with Q+1 roots. This works without a condition on p dividing kn.

The degenerate cases are correctly separate. For t²=κ, split intersecting lines contribute 2Q−1 and nonsplit lines contribute 1. For t=2 the branch character is χ_Q(κ−4); for t=−2 it is (−1)^{kn}χ_Q(κ−4). On any preserved branch the fixed equation has nonzero linear derivative. These fibers are disjoint under the standing κ assumptions.

The sum identity for χ_Q(t²−4), the number 1+χ_Q(κ) of roots of t²=κ, and χ_{qⁿ}(a)=χ_q(a)ⁿ give exactly the reported five power-sum terms. An independent summation reproduces the displayed N_n and its formal rational zeta.

Reducedness is not inferred from numerical agreement. The ambient fixed equations have Jacobian −I. For each of the Q values of t their leading x,y equations have the invertible coefficient matrix A_t^{kn}; hence there are no points at infinity in that two-variable leading system and the fixed scheme is finite. Its quotient cutting out X_κ is a quotient of a finite product of algebraically closed fields, so remains reduced.

The known complex conic decomposition and finite homological action support the background mechanism, not a finite-characteristic Lefschetz substitution. The author's normalization differs by κ=t+2, as the scout records. [Goldman–Neumann, Theorem 1 and §4](https://www.math.columbia.edu/~neumann/preprints/wmgwdn2.pdf) The separately cited hyperbolic longest-orbit problem is genuinely different from this parabolic Frobenius clock; no claim is made about the current status of its conjectures. [Cerbu–Gunther–Magee–Peilen, Theorem 1.5 and Conjecture 1.10](https://arxiv.org/pdf/1610.07077)

No extension to κ=0,4, characteristic 2, general hyperbolic words, or ordinary untwisted geometric periods is required or certified here. The proof being correct does not establish that its increment merits a paper.

## 4. Source caveat A1: odd-cycle determinant sign

Severity: **substantive source-use caveat; not a blocker to the zero-retained scout decision.** The accessed text really supplies the abstract-graph definitions and determinant/modular-curve framework. However, Lemma 4.11's asserted cycle factor for det(I+sP_k) is wrong for odd k>1. The issue occurs in both HTML and PDF text, not only in duplicated HTML fragments. Relevant original locators are Definition 3.1, Lemma 4.11 (printed pp.12–13), Theorem 4.12 (p.13), and Theorem 6.9 (p.25). [Lau–Morrison–Orvis–Scullard–Zobernig, primary PDF](https://arxiv.org/pdf/2509.15214), [accessed HTML](https://arxiv.org/html/2509.15214v1)

An elementary independent check suffices. Let P₃ be the permutation matrix of a three-cycle. Then

\[
\det(I+sP_3)=1+s^3,
\qquad
\det(I+sP_k)=1-(-s)^k.
\]

The paper's printed factor at k=3 instead has a minus sign. Here is also a counterexample within its abstract graph hypotheses, independent of any elliptic-curve realization. Take one vertex, three loop edges, J=(123), and L=id. Its degree is 3, so D commutes with L. With E the 3×3 all-ones matrix, the non-backtracking edge matrix is W=E−P₃. Consequently

\[
\zeta(u)=\det(I-uW)^{-1}
=\frac{1+u}{(1-2u)(1+u^3)}.
\]

The literal specialization of the printed Theorem 4.12 instead replaces 1+u³ by 1−u³. Already the coefficient of u³ in u(d/du)log ζ is 6 for the actual matrix and 12 for that printed specialization. A read-only SymPy 3×3 determinant calculation independently returned det(I+uP₃)=1+u³ and Tr(Wⁿ)=[3,3,6,15,33,66] for n=1,…,6. This diagnostic did not rerun any of the nine Markov Gröbner computations.

The determinant identity immediately before the source's cycle-factor expansion has the expected signs; the finding specifically concerns its expansion and formulas inheriting it. It does not establish that every arithmetic isogeny specialization fails: when all relevant cycles have the requisite even lengths, this particular sign objection may vanish. No claim is made that the three-loop abstract graph is realized by an actual supersingular isogeny graph.

Required reporting adjustment, sent to the lane owner and root: retain the framework-ownership rejection, but explicitly flag the literal-formula caveat and avoid citing the full displayed general identity as correctness-certified. This is not a request to extend the research batch or contact the authors.

Access/version qualification: the retrieved HTML has a September 2025 arXiv header and an August 24, 2026 body date; the separately retrieved PDF has a September 19, 2025 body date. Both show the relevant sign issue. The audit does not certify their complete version equivalence. Browser PDF text was inspected; a requested screenshot did not provide a usable image here, and no full-PDF visual review is claimed.

## 5. Handoff boundary

The scout's scientific selection remains **0 retained**, with B and C proved only at their actual scope. There is one requested source-report clarification (A1), no requested change to either short proof, and no request for a further numerical campaign. Discovery of a literal source error is not by itself a sufficient new-theorem or publication contract.

## 6. Remediation closure — 2026-09-06

**A1 reporting remediation: CLOSED.** After the lane owner reported the edits, this reviewer reread the revised report, source audit, and [CLAIM_INTENT.json](../nonaffine_charp/CLAIM_INTENT.json), and independently recomputed their hashes. This closes the local reporting issue; it does not claim the external paper was corrected.

The report's decision table and candidate-A section now use `REJECT_FRAMEWORK_OWNED_NO_NEW_ARITHMETIC_LEMMA`. They explicitly distinguish framework ownership from correctness certification of the printed odd-cycle formulas. The source audit preserves the correct permutation determinant, the admissible abstract three-loop counterexample, the HTML/PDF distinction, and the limitation that no actual supersingular realization or new full-family arithmetic theorem was established. Claim A in the JSON repeats the same boundary. No unconditional literal-theorem coverage remains in those reviewed locations.

| Revised file | Verified SHA-256 |
|---|---|
| SCOUT_REPORT.md | `5397df40144acf6e71eddd173e5d4a93e942f7f2845438939075f4876d692260` |
| SOURCE_AUDIT.md | `a98917d057fceff24176bccd0e7761dba89c70d3a09fab61d83e666875b06332` |
| CLAIM_INTENT.json | `7fab68cfde83711e635bb5deb074d79414bf2c02d5b3b2d5028fa8b44d3ac538` |

The hashes of PROOF_PACKAGE.md, exact_probe.py, and exact_probe_results.json still match the initial table. The nine checks were not rerun. This closure preserves the original finding and pre-remediation hashes above; the final recommendation remains zero retained contracts, with no unresolved local reporting adjustment from this audit.
