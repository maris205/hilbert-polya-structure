# Source-first record and historical formula audit

Date: 2026-09-06 UTC. Author: `/root/twentieth_algebra_scout`.
This is a bounded author-side search, **not global novelty clearance**.
Exactly three formalized desk attempts are in INTAKE.md. The comparison
groups below add no candidates or executed systems. No external API review,
specialist contact or manuscript upload occurred.

## Public primary-source passages actually inspected

The four files under source_extractions/ preserve actual browser extraction
outputs, not downloaded original HTML/PDF bytes. Their hashes bind those
extractions only. They may include surrounding text beyond the claim scope.
The line references below are browser extraction locators, **not PDF page
anchors**. No claim is made to have read an entire paper from its landing
page, to have verified its cited bibliography, or to have obtained an
independent external assessment.

| ID | Primary source and metadata | Actual read scope and relevance |
|---|---|---|
| S1 | Yangjiang Wei, Guangwu Xu and Yi Ming Zou, *Dynamics of Linear Systems over Finite Commutative Rings*, [arXiv:1709.08579v1](https://arxiv.org/html/1709.08579v1), 25 September 2017 | Abstract and introduction, including the invariant-summand/lcm cycle discussion, elementary-divisor formula, finite-ring Fitting reduction and the statement of Lemma 2.1; extracted lines 24–92. This owns generic finite-linear cycle machinery. It does not state D1's map or prove a global conjugacy of D1 to one fixed linear system. D1's exact scalar adapter is proved locally. Saved: `source_extractions/linear_v1.txt`. |
| S2 | Li Guo, Yan Jiang, Yunhe Sheng and You Wang, *Rota-Baxter operators on braces, post-braces and the Yang-Baxter equation*, [arXiv:2512.16116v1](https://arxiv.org/html/2512.16116v1), 18 December 2025 | Abstract, Introduction 1.1–1.3 and Definitions 2.1/2.3/2.6 and neighboring propositions in the displayed extract. The definition of a set-theoretic Yang–Baxter solution explicitly requires a bijection. The body distinguishes group laws, actions and factorization constructions. No general theorem in this paper is asserted to identify D2; its Heisenberg examples were only encountered through a targeted search fragment, not fully read. Saved introduction extract: `source_extractions/braces_v1.txt`. |
| S3 | Jon McCammond and Giovanni Paolini, *Factoring isometries of quadratic spaces into reflections*, [arXiv:2103.02507v1](https://arxiv.org/html/2103.02507v1) | Abstract and Section 1 through the reflection formula (1), including quadratic/polar-form conventions and the nonsingular-normal condition, plus neighboring fixed/moved-space definitions and displayed Wall-parametrization arguments. The decisive locator is lines 75–78. This supplies the classical reflection primitive, not D3's simultaneous sum-axis scheduler or its isotropic completion. Saved: `source_extractions/reflection_v1.txt`. The requested v1 page displayed the arXiv header 3 March 2021 but an internal rendered `Date: August 24, 2026`; the latter is not silently substituted as a publication date or claimed to be a verified version history. |
| S4 | B. A. Omirov, U. A. Rozikov and M. V. Velasco, *A class of nilpotent evolution algebras*, [arXiv:1711.05030v1](https://arxiv.org/html/1711.05030v1), 14 November 2017 | Introduction, Section 2's natural-basis multiplication, nilpotency/upper-annihilator definitions and triangular structure statement, then the displayed construction (3.1), Proposition 1 and its initial basis calculation. These are structures built from quadratic forms and scalar shift chains, not a newly discovered finite autonomous rule. We do not claim its construction classifies every nilpotent evolution algebra; its abstract expressly limits that. Saved: `source_extractions/evolution_v1.txt`. |
| S5 | Yangjiang Wei and Yi Ming Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, [arXiv:2310.12368v1](https://arxiv.org/html/2310.12368v1), 18 October 2023 | Actual HTML introduction and Section 2 through Theorem 2.1/proof, including natural-basis structure matrices, the monomial change-of-basis action and Burnside enumeration. These are isomorphism-class orbits, not time orbits of squaring a state. A separate dynamical result is not inferred from the word “orbit”. No extraction snapshot of this earlier open is in the package; the exact URL and scope are retained here. |

For these mathematical sources the relevant evidence is the displayed
definition/proof and its exact assumptions. They are primary author
preprints; their existence/title/author fields were directly shown on
arXiv. No journal peer-review certification, author-credential audit,
retraction database audit or COI clearance was performed. The ARS empirical
evidence pyramid is not used to pretend a mathematical proof is a clinical
study. Fitness here is **primary but passage-bounded**, with the above
unverified publication/coverage limitations explicit.

Other search results included the publisher page *Permutation
Representations and Automorphisms of Evolution Algebras* (2025), whose
search extract displayed Definition 2.1. Its subsequent open returned a
page reference without an additional body passage in that response. It is
not counted as a sixth full-body audit. ResearchGate, secondary overviews,
generic Householder teaching pages, “Lang maps” of general-type varieties,
Frobenius-**norm** physics papers and unrelated Kerr/quantum papers were
search noise or metadata leads, not proof authorities. In particular a
Frobenius norm is not the finite-field Frobenius automorphism of D1.

## Actual failed access and discovery checks

- `https://arxiv.org/html/2103.02507v2` returned **Internal Error** and a
  one-line result, not a readable paper. The subsequent explicit v1 HTML
  retrieval succeeded and supplied only the scopes stated under S3.
- The guessed local paths `scouting/algebra/INTAKE.md` and
  `scouting/algebra_second/INTAKE.md` within this batch did not exist; their
  attempted reads returned “No such file or directory”. Discovery then
  located the actual report/gate paths. Nothing is cited from the missing
  files.
- The guessed `scouting/finite_systems_sixteenth/D2LC_PROOF.md` did not
  exist. The actual `PROOF_AND_DISPOSITION.md` was subsequently read through
  its local-machine value discussion. This was a path lookup correction,
  not a repaired mathematical execution.
- Several combined exploratory search/read tool outputs were truncated.
  The targeted original passages and scoped reads below, not completeness
  of those broad outputs, support the comparisons. No failure was turned
  into a source PASS or concealed scientific run.

## Six named comparison groups — not six candidates

| Group | Exact old literal or source construction | Relation to the three attempts; deduction actually used |
|---|---|---|
| C1: state diagonal / scalar action | P175: $A\mapsto[D(A),A]$ on all matrices; NL13: $(a,b)\mapsto(a,ab)$; CS endpoint normal form $rw$ with free coordinates | D1 changes the carrier and retains a Frobenius-updated diagonal. It is not equal or claimed conjugate to P175/CS. Its own equations (1)–(5) give a complete product-scalar template that consumes both axes. |
| C2: Gram / Lang / canonical matrix operations | Old field-Gram $A\mapsto AA^{\mathsf T}$; old MLG $A\mapsto A^{-1}\bar A$ on $\mathrm{GL}_2(\mathbb F_4)$; old Schur/pivot, cofactor and Hessian operations | These already-named operations were excluded, not formalized as additional new rows. No quotient of D3 by its Gram projection is confused with the literal **Gram update** $A\mapsto AA^{\mathsf T}$. No external Lang theorem was newly verified here. |
| C3: evolution-algebra squaring | S4's natural basis has cross-products zero; its displayed high-dimensional construction yields form values followed by scalar-coordinate multiplication | Directly applying this named multiplication as “a dynamical step” is only a preliminary comparison. No new literal carrier/feedback beyond D1–D3 was admitted. Classification orbits in S5 are not functional-graph orbits. |
| C4: Rota–Baxter / brace refactorization | S2 starts from compatible group laws, actions and bijective Yang–Baxter solutions | The named factorization construction was not recast as a fresh row. Neither bijectivity nor singleton inverses can supply the required independent second axis. No claimed source identity with D2. |
| C5: three-product word pattern | Old S04: $(a,b,c)\mapsto(ab,bc,ca)$ on a rectangular band; NL09: $(u,v,w)\mapsto(uv,vw,wu)$ on truncated free words | D2 is a carrier change, not a newly invented word pattern. No full-carrier equality/conjugacy to those semigroups is asserted. The exact **all-group** source-set square-root adapter (6)–(7), not the old pilots, decides the inverse boundary. |
| C6: reflection recurrence / formed-space quotient | Old REF: $(u,v)\mapsto(v,2B(u,v)v-u)$ on a unit anisotropic conic; old B2B-07 companion action with invariant symplectic scalar; P125/V02 finite formed-space quotients | D3 is not the old two-vector conic recurrence. Equation (9) is a factor, not an evaluated quotient clock, a conjugacy or proof of simultaneous bijectivity. The old reflection and formed-space primitives are spent; D3's global temporal/inverse gaps remain genuinely open rather than labelled an exact collision. |

## Historical originals and actual read extents

HISTORICAL_SHA256SUMS is workspace-root-relative and pins the **entire**
eighteen files below. A whole-file hash is not a whole-file-read claim or a
new replay of its old numerical evidence. These are deduction/source inputs,
not imports of a mathematical kernel.

| Pin | Original path (relative to workspace root) | Read scope |
|---|---|---|
| H1–H4 | `docs/papers204_208_sequence/scouting/finite_systems_seventeenth/{INTAKE,PROOF_BOUNDARIES,SOURCE_AND_COLLISION,SCOUT_REPORT}.md` | All four files completely. Exact derivative/permanent/Hessian/Viète exclusions and distinctions were retained; none of those formulas was reintroduced. |
| H5–H7 | `docs/papers204_208_sequence/scouting/finite_algebra_ninth/{INTAKE,PROOF_AND_ADAPTER_NOTES,SOURCE_AND_COLLISION}.md` | Entire intake and proof notes; source record through the displayed search/collision scope. QEF's complete fifth-degree elimination and unclosed scalar-quadratic diagonal were read, not merely its summary verdict. No QEF pilot was rerun. |
| H8 | `papers/175-diagonal-feedback-commutator/main.tex` | Lines 1–240: literal, coordinate equation, source framing, full fibre and extremum proofs, and clock theorem statement. No claim of reading later bibliography/build material. |
| H9 | `docs/papers204_208_sequence/scouting/algebra/CS_GATE/CANDIDATE_GATE.md` | Sections 1–5 and the displayed start of the execution discussion; especially the complete triangular scalar endpoint adapter and its not-a-conjugacy boundary. |
| H10 | `docs/papers162_166_sequence/scouting/replacement_nonlinear_algebra/SCOUT.md` | Lines 1–110, including the complete 24-row literal ledger, NL09/NL13/NL17/NL18 and the initial NL07 deduction. No historical execution adopted. |
| H11 | `docs/papers127_131_sequence/scouting/algebraic/SCOUT.md` | Targeted original R/S/X table passages, lines 80–109, including rectangular-band S04 and its exact multiplication. |
| H12 | `docs/papers157_161_sequence/scouting/replacement_geometry_mechanism/SCOUT.md` | Lines 130–177, especially complete REF and QIV literal/convention paragraphs. |
| H13 | `docs/papers204_208_sequence/scouting/graph_algebra_fifth/INTAKE.md` | Whole file: all six exact literals and existing group/derivative/Hessian/cross-product exclusions. |
| H14 | `docs/papers204_208_sequence/scouting/finite_systems_sixteenth/PROOF_AND_DISPOSITION.md` | Lines 1–230: CNL deductions, D2LC pointwise clock and fibre maximum, and the finite four-vertex passive-boundary adapter. Its sharp constants are not automatically new axes. |
| H15 | `docs/papers182_186_sequence/scouting/algebra_lane/SCOUT_AND_KILL_LEDGER.md` | Complete file, including A04 projective Hessian, A11 Lang and A13 symmetric elimination literals. |
| H16 | `docs/papers204_208_sequence/scouting/discrete_geometry_seventh/INTAKE.md` | Whole file; exact new-vs-old geometric update and reflection-family desk boundaries. |
| H17–H18 | `docs/papers172_176_sequence/scouting/fresh_nonlinear_algebra/{COLLISION_FIREWALL,SCOUT_AND_KILL_LEDGER}.md` | Complete files. P175's state-diagonal mechanism; full V02 small formed-space rejection; actual Gram, group-word and rational map literals. |

The eighteenth-lane PROOF_AND_ADAPTERS.md was also read as recovery/context
for what a zero-execution closure means, not used as a premise of D1–D3;
it is not included in the scientific-historical pin set. Central lifecycle
files can change under root ownership and are not claimed immutable merely
because they were required recovery reads.

## Executed public query formulations

Nineteen query formulations were issued in six search calls. Three of the
last queries used a 183-day recency filter as explicitly shown below. Dates
in snippets were never substituted for the sources' publication/version
metadata. Broad results were noisy; these queries are not exhaustive
coverage of arXiv, Scholar, Semantic Scholar or the literature.

1. `finite field nonassociative evolution algebra squaring dynamics nilpotent algebra`
2. `Rota Baxter operator finite algebra discrete dynamical systems factorization`
3. `finite field matrix Gram iteration A transpose A dynamics`
4. `site.arxiv.org "Rota-Baxter" "factorization" algebra finite`
5. `site.arxiv.org "evolution algebras" "finite fields" dynamics`
6. `site.arxiv.org "Lang map" "finite" fibres`
7. `site.arxiv.org "Gram" "finite fields" matrix`
8. `finite field reflection dynamical system quadratic form simultaneous reflection vectors`
9. `simultaneous reflections triangle vectors sum other vectors dynamics Householder`
10. `"finite fields" "reflection" "dynamics" 2025 2026` (183-day filter)
11. `"diagonal" "commutator" "Frobenius" "dynamics"`
12. `"finite field" "diagonal feedback" matrix`
13. `"semilinear" "scalar" "functional graph" finite field 2025 2026`
14. `"cyclic product" "Heisenberg" dynamics`
15. `"triple" "word map" "square roots" finite group`
16. `"noncommutative" "product" "dynamical" "finite groups" 2025 2026` (183-day filter)
17. `"simultaneous" "reflection" "finite field"`
18. `"reflection dynamics" "Gram"`
19. `"quadratic space" "dynamical system" "reflection" 2025 2026` (183-day filter)

This is a recorded bounded query list, not a claim that the package contains
all raw search-response bytes. Only the four actual selected extraction
outputs are archived. Direct primary HTML browsing was used in place of
external bibliographic Python/API clients, under the project/ARS routing
boundary. No novelty score or global owner-absence conclusion follows.

## Disposition

The D1 and D2 deductions already remove their plausible contribution
without relying on a web non-hit. D3 has source-neighbor and proof gaps;
neither the named reflection primitive nor an unevaluated Gram factor
settles its all-parameter dynamics. Therefore the desk closes
**NO_FRESH_SLATE / NO_PROMOTION**, preserving exactly three attempted
descriptions and six separately counted comparison groups. AI assistance
was used for this author-side search, proof triage and documentation; it is
not independent expert validation. HOLD_EXTERNAL remains unchanged.
