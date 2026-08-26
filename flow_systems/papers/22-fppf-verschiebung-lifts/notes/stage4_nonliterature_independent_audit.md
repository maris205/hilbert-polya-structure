# P22 Stage 4 non-literature independent audit

## Verdict

**REVISE (two local semantic repairs; no scope or theorem change).**

The draft respects the immutable authorization boundary and is mathematically sound on the finite-flat convention, topology-indexed extension classes, and deletion of the internal Route/Gate paragraph. Two phrases need repair before conversion into a patch:

1. B0023 does not state the extra data that make failure of one section to lift imply nonexistence of every middle-object lift of \(v\).
2. B0092 says that the example-specific verification “consists of” four finite-algebra calculations, although the draft itself correctly records additional injectivity, sheaf, subcanonicity, detector, and torsion-freeness inputs.

These are local repairs inside already authorized replace_block targets. They do not authorize a new finding, new block, changed quantifier, or changed theorem strength.

## Audit basis and integrity receipt

- Draft audited: notes/stage4_nonliterature_draft.md, SHA-256 59d2300e264d2ff05e1306edc86cbabc43598ffe7226808a62d0b08fcda04956.
- Anchored base: notes/stage3_revision_base.tex, SHA-256 32f7bea67f6c837a7e8b26b35aeb0297a13ec2c7f910abc09617dcb817c4a4a8.
- Immutable roadmap: notes/stage3_revision_roadmap.json, SHA-256 634205f0cd71f97f1204740b422aea1d4336ae6a256272a928665690aebc8737.
- Authority checked against notes/stage4_author_adjudication.json; the claim-surface manifest is empty and supplies no claim-strength authorization.
- The eight declared old_hash values agree with notes/stage3_revision_base.block-manifest.json.
- No manuscript, draft, patch, roadmap, adjudication, or provenance artifact was modified in this audit.

## Deninger v1 primary-source check

**PASS.** The official v1 text, §4 immediately before Corollary 4.6, says that the fp site has “coverings \(\{X_i\to X\}\) by finite flat morphisms which are jointly surjective.” See [Deninger, arXiv:2508.05329v1, §4](https://arxiv.org/html/2508.05329v1). The same wording is present on PDF p. 23 of the locally verified v1 PDF, SHA-256 19870cbdddbde82526939eb801c2ce14707dc7b48e54a7bc81f4a84400505002.

Consequently B0016 correctly treats a cover as a jointly surjective **family** whose members are finite and flat. It does not incorrectly impose finiteness on the cardinality of the family. On the noetherian affine owner, the corresponding ring maps are finite locally free. The subcanonicity statement is also correct: these are fpqc covering families, so representable presheaves satisfy descent; the structure presheaf is represented on this category by the affine line.

## Block-by-block findings

| Block | Result | Independent audit |
|---|---|---|
| B0016 | **PASS** | Matches Deninger v1's jointly-surjective-family convention. “Finite locally free” is valid on the noetherian affine base, and the stated subcanonicity consequence is exactly the property used later. The fppf and finite-flat conclusions remain separate. |
| B0019 | **PASS** | Quantifies \(\tau\in\{\fppf,\ff\}\), defines \(\Ksh_\tau\) and \(e_\tau\) in \(\mathrm{Ab}(\mathscr C_\tau)\), and places the class in the topology-specific Ext group. It does not identify the two extension objects. The contextual use of unindexed \(\Zsh,\Wsh\) is consistent with the existing manuscript convention. |
| B0020 | **PASS** | Preserves every original quantifier: each topology, every \(N>1\), and every kernel endomorphism. Both consequences \(e_\tau\ne0\) and \(V_N^*e_\tau\ne0\) are retained in the correct category. |
| B0023 | **REVISE** | The local-descent implication through “no global preimage” is correct. The following Ext sentence is under-specified: an arbitrary nonliftable \(w\in W(U)\) does not by itself rule out a middle-object lift of an arbitrary \(v\). The template must state a source section \(\xi\in Z(U)\) with \(w=v(p(\xi))\); then any \(\widetilde v\) satisfying \(p\widetilde v=vp\) supplies the forbidden global preimage \(\widetilde v_U(\xi)\). |
| B0069 | **PASS** | Correctly binds the concrete failure and \(e_\tau\) to the same fixed category \(\mathrm{Ab}(\mathscr C_\tau)\). No new assertion is added to the abstract proposition that follows. |
| B0073 | **PASS** | Fixes one \(\tau\), invokes the matching theorem, and obtains the inequality for every \(u:\Ksh_\tau\to\Ksh_\tau\). Its last sentence makes the unindexed \(e\) in untouched B0074 refer to the fixed \(e_\tau\). B0074's \(Z,K,W\) are the generic variables of Proposition 5.1, now interpreted in that fixed category, so the continuation and its proof-closing command remain coherent. |
| B0091 | **PASS** | Exact authorized deletion. B0090 already supplies the public scope limits; B0092 begins with the mathematical conclusion. Their new adjacency leaves no dangling reference, label, or environment. |
| B0092 | **REVISE** | The two-site nonlift and nonzero \(V_N^*e_\tau\) conclusions do not drift in strength. However, “verification consists of four finite algebra calculations” wrongly sounds exhaustive and conflicts with the additional inputs correctly listed in B0023. The theorem's \(N>1\) quantifier should also be written explicitly instead of relying on “nontrivial.” |

## Exact minimum repairs

### B0023

Replace the sentences beginning “Whenever a proposed middle-object lift” with the following conditional bridge:

    If, in addition, \(v\colon W\to W\) and \(\xi\in Z(U)\) satisfy
    \(w=v(p(\xi))\), then any middle-object morphism
    \(\widetilde v\colon Z\to Z\) with \(p\widetilde v=vp\) would make
    \(\widetilde v_U(\xi)\) a global preimage of \(w\).  Hence no such
    middle-object morphism exists.  For a short exact sequence with class
    \(e\), Proposition~\ref{prop:extcriterion} then gives
    \(u_*e\ne v^*e\) for every \(u\colon\ker(p)\to\ker(p)\).

In the instantiation paragraph, add the already-used data \(\,v=V_N\,\) and \(\,\xi=(x)^\sh\,\). This makes the abstract implication complete and exactly reproduces the proof in B0065, without generalizing it.

### B0092

Use an explicit theorem quantifier and a non-exhaustive dependency statement. A sufficient minimal replacement is:

    That single explicit descent failure rules out an additive lift of \(V_N\)
    for every \(N>1\) on each of the two sites and, for each
    \(\tau\in\{\fppf,\ff\}\), gives \(V_N^*e_\tau\ne0\).

    The example-specific verification combines four explicit finite-algebra
    steps---a root cover, a roots-of-unity product, one tensor-product overlap,
    and one truncated-polynomial specialization---with the stated Dedekind
    injectivity, rational-Witt sheaf, subcanonicity, big-Witt detector, and
    torsion-freeness inputs.

The remaining B0092 recap may stay unchanged. This correction preserves the original all-index/two-site conclusion while accurately separating the formal template from all inputs needed to instantiate it.

## Cross-block and authority conclusion

The indexed chain B0019 → B0020 → B0069 → B0073 is internally consistent. Untouched body occurrences such as B0074, B0075, and B0077 remain readable topology-by-topology under B0019's abbreviation convention; the English and Chinese abstracts retain their pre-existing unindexed shorthand, which is outside the roadmap's authorized targets. Expanding the edit to those blocks would be unauthorized and is not required for the two repairs above.

No proposed text changes the theorem's modality, the universal range \(N>1\), the two-site scope, or the nonvanishing conclusions. After the two repairs, the non-literature draft is suitable for patch construction within REV-002/004/005/006 only.
