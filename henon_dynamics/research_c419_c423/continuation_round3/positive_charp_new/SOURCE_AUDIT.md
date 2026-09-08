# Source audit — round 3 positive-characteristic scout

Audit date: 2026-09-07. Scope: two frozen contracts only. Source absence is not proof of novelty. Search-result snippets and repository notes were used for routing; the mathematical decisions use the primary passages listed below and the explicit derivations in the proof package.

## Documented fresh queries

The following ten queries were actually issued in this round after the initial orientation scan. They alone exceed the five-query gate. A `183 days` flag describes the search request, not independently verified publication recency.

| # | Exact query | Recency |
|---|---|---|
| 1 | `"Rational functions with a unique critical point" Faber` | unrestricted |
| 2 | `finite adelic distortion Kummer matrix isogeny dynamical zeta nilpotent` | unrestricted |
| 3 | `"Dynamics of endomorphisms of algebraic groups and related systems" arxiv` | unrestricted |
| 4 | `"z^p" "1/z" "zeta"` | unrestricted |
| 5 | `"unicritical" "zeta" positive characteristic` | unrestricted |
| 6 | `"Artin-Mazur" "zeta" "rational functions" "finite fields" general transcendence` | unrestricted |
| 7 | `"z^p+1/z" dynamics` | unrestricted |
| 8 | `"dynamical zeta" "positive characteristic" 2026` | 183 days |
| 9 | `"Kummer" "matrix" "zeta" "dynamical" rationality` | unrestricted |
| 10 | `"Kummer" "dynamical zeta" 2026` | 183 days |

Queries 4, 5, and 7 returned largely irrelevant hits. These negative/poor results are recorded, not treated as evidence that no relevant theorem exists. The Kummer queries also returned unrelated Kummer-congruence papers; those were not used as quotient-variety owners.

## Primary sources actually read

### S1. Xander Faber — unicritical structural owner

- [arXiv:1102.1433v2, *Rational Functions with a Unique Critical Point*](https://arxiv.org/html/1102.1433v2).
- [Version metadata](https://arxiv.org/abs/1102.1433): original submission 2011-02-07; inspected version 2011-05-17. Do not replace these dates with a search crawler's freshness label.
- Actually read: Theorem 1.1 and its statement context; the complete §2 characterization proof, including Lemmas 2.1 and 2.3, Example 2.4, and the division-algorithm argument.
- Owns the continued-fraction characterization used to recognize PC3-A as $[z^p,z]$. It does not provide the desired periodic-count or zeta theorem. No claim that the complete paper's geometric sections were read is made.

### S2. Andrew Bridy — dynamically affine zeta boundary

- [arXiv:1306.5267v2](https://arxiv.org/html/1306.5267v2), *The Artin-Mazur Zeta Function of a Dynamically Affine Rational Map in Positive Characteristic*.
- Actual version date in the full text: 2014-02-24. [Publisher record](https://jtnb.centre-mersenne.org/articles/10.5802/jtnb.941/) identifies the 2016 journal volume, pages 301–324, DOI 10.5802/jtnb.941; its online publication date is 2017-01-02.
- Actually read: Theorems 1.2–1.3; Remark 1.5; Conjecture 1.6; Definitions 2.1–2.2; Lemma 2.4 and proof; descriptions of the five families and the opening Lattès setup in §5.
- The separable-map theorem is family-restricted. The general separable statement is explicitly conjectural. PC3-A's exclusion from those five families is derived in our proof package, not quoted as a statement of Bridy.

### S3. Byszewski–Cornelissen–Houben, with van der Meijden for Appendix B — quotient formula and scalar scope

- [arXiv:1904.04942v1](https://arxiv.org/html/1904.04942v1), *Dynamically affine maps in positive characteristic*; [metadata](https://arxiv.org/abs/1904.04942), submitted 2019-04-09. The preprint lists four authors and notes van der Meijden's Appendix B contribution; the inspected preprint attribution is retained.
- Actually read: full definition in §1.2; the coseparability definition and Theorem B; Lemma 3.1; (H1)–(H4); Theorems 3.5–3.6; Proposition 4.7 and caveat; Proposition 5.4 and the relevant discussion.
- Lemma 3.1 owns the geometric quotient count. Theorem B explicitly treats integer multiplication, not arbitrary integer matrices. The definition permits confined isogenies, including relevant degree-one cases. No assertion that general $A$ satisfies (H2) is used.

### S4. Byszewski–Cornelissen–Houben — abelian/FAD recurrence owner

- [arXiv:2209.00085v2](https://arxiv.org/html/2209.00085v2), *Dynamics of endomorphisms of algebraic groups*, with the subtitle on finite-adelically distorted systems.
- [Metadata](https://arxiv.org/abs/2209.00085): initial submission 2022-08-31; inspected revision 2024-04-19. This is the revised 176-page monograph, not a new 2026 paper. The older title containing “and related systems” is a retrieval alias, not the inspected title.
- Actually read: introductory setup and FAD definition; complete §5.3 (Theorem 5.3.1 and proof); complete §11.3 (Proposition 22, Theorems 11.3.2–11.3.4 and proofs/discussion); complete §14.1. The rest of the monograph was not claimed to have been read.
- The used implication is restricted to an actual abelian/FAD system: nontrivial distortion prevents recurrence. Our quotient is not simply declared to be FAD. The proof applies the theorem to $A^r$ on $E^g$ and subtracts the separately recurrent plus term. This is our short reduction from the cited results, not a purported verbatim theorem in the monograph.

### S5. Current primary calendar — date check only

- [CANARI 2025/2026 seminar page](https://canari.inria.fr/seminar/2025.html), actually read at its 2026-06-02 entry: Marc Houben, “Arithmetic dynamics of algebraic groups.”
- The event is within the six-month window. Its abstract is a current primary pointer to the algebraic-group theme, not a new proof of either frozen contract. A search label said the page was over a year old; the actual event date, not that label, supplies recency. No theorem is inferred from the seminar.

## Peripheral routing and exclusion

[Doyle–Faber, arXiv:2203.06205v3](https://arxiv.org/abs/2203.06205), revised 2022-12-19, was inspected at metadata and introduction level while considering source-first alternatives. Its uniform boundedness theme over function fields was not used as an exact geometric all-period count theorem and did not become a third deep-screen candidate.

The narrow local search used the corrected directories `continuation_round2/new_charp`, `positive_characteristic`, and `continuation_round2/elliptic_dynamics` under this batch. It tested the exact reciprocal form, integer-matrix/Kummer terms, and the two closest general-owner identifiers. No matching strings appeared there. The initial search with a missing `henon_dynamics/` prefix failed and was not counted as a successful check.

No Zotero/Obsidian result, unavailable full text, uninspected theorem, or secondary snippet was promoted to evidence. An attempted nonexistent v3 URL for the 2019 preprint was corrected to its actual v1 before using the source. Mathematics-bearing HTML was rendered from its MathML alt text in memory; no source PDF or downloaded cache was added to the repository.

## Gate conclusions

PC3-A: a direct dynamically affine collision is ruled out by the structural argument, but the full ordinary zeta claim is unproved and the search is not exhaustive. **HOLD, no novelty certification.**

PC3-B: the complete frozen count/rationality statement has a short derivation from known mechanisms. **REJECT as a short classical companion**, without pretending a literal arbitrary-matrix theorem was found or extending the result to stronger analytic properties.

These decisions were made by this current-team scout; they are not represented as an independent external review. Zero admissions, zero manuscripts, zero candidate computational experiments.
