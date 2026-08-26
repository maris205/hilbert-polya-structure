# P22 Stage 4.5 E6 independent semantic audit

## Recorded result

**none detected by the recorded semantic review**

The schema-valid companion contains an empty ordered finding set. This is a model-mediated semantic-review result, not a deterministic no-drift certificate, a completeness claim, or an author disposition. The review started from the complete Revision-Evidence Bundle and did not inherit the conclusion of the earlier Stage 4 audit.

## Detector and protocol binding

| Field | Value |
|---|---|
| Detector kind | `model_mediated_semantic_review` |
| Detector ID | `codex-session-model/p22-stage4.5-e6-independent-20260825` |
| E6 protocol | `academic-pipeline/references/claim_verification_protocol.md` |
| E6 protocol SHA-256 | `f26d4e0b876f323db5fccc1bbc3120189e69282e45ec6b6cc0cee1e3b1e7a537` |
| Claim-strength ladder SHA-256 | `22f51a6fefb2525e685b6938cc446fa658bdfb6e43157b5d2e6d5051f2212dfe` |
| Token-conservation checker SHA-256 | `19908ee8469d25497796190ec9a731d510c9db8ad7484da24ac657971aa853fb` |
| Finding schema SHA-256 | `c0c58f2c39544929ef52c3c2d3046b50c92c290896ac26e1c891ddea08fdaf98` |
| Bundle validator SHA-256 | `5341358d489a550b56f0e7efde850c551b6d9df41106b0462e2f804ab4de9998` |

The companion `notes/stage4_5_claim_strength_drift_findings.json` binds the exact final draft SHA-256 `663ade71e41de81afd376db516ed8f548af3090cf342dd4db052eb212ce3c2d2` and exact bundle SHA-256 `763f9e3cc12a8115f02a0d315dc9c74415448676c341a20e80cc0d292006f0ff`.

## Fresh bundle replay

The first operation in this audit was:

```text
python3 ars/scripts/revision_roadmap.py validate-bundle \
  papers/22-fppf-verschiebung-lifts/notes/stage4_revision_evidence_bundle.json \
  --root papers/22-fppf-verschiebung-lifts
```

Raw validator output:

```text
revision evidence bundle ok
```

The validated bundle carries one continuous review-roadmap round:

| Bundle member | Bound SHA-256 |
|---|---|
| Chain-start / pre-round draft, `notes/stage3_revision_base.tex` | `32f7bea67f6c837a7e8b26b35aeb0297a13ec2c7f910abc09617dcb817c4a4a8` |
| Pre-round block manifest | `b21625abd194fc2f0cfdba0eb0193da5915bc81e4a7d26056a770c58f767cc91` |
| Chain-start integrity receipt | `1d63c9c707de60ed5475c7c0a37cae0025b5c99c42051e1e9229a4ea3bcd31ff` |
| Immutable roadmap | `634205f0cd71f97f1204740b422aea1d4336ae6a256272a928665690aebc8737` |
| Empty claim-surface manifest | `9307a9f2d6b5774e4e44a90d9f1d898789ffdcf8f43fe46887c07cefd0c15a15` |
| Author adjudication | `b7f8c047b1f3fadb0739a1ac4c11848b61af169b1d94e72bbe8f633691a41ddb` |
| Official round-1 patch | `e9c1debbb21a0b209847004de16fd76c9e1489844c4209417dd7fdb6b2ca5a6a` |
| Apply report | `95354037ded702bc6c73c61a0565b5529148b33cd341153f38e5eabbf1a1f45f` |
| Post-round / final anchored draft | `663ade71e41de81afd376db516ed8f548af3090cf342dd4db052eb212ce3c2d2` |

Independent patch replay against the exact pre/post bytes found all 13 old-hash preconditions and all applied replacement segments exact. B0091 is the sole deletion; B0103/B0104, B0105, and B0106 are only the mechanical continuation segments of B0022, B0023, and B0092. The other 89/89 base blocks are byte-identical. These mechanical facts establish the comparison population but do not supply the semantic conclusion.

## Authorization boundary

All six author-adjudication rows are `will_address`, and every op targets an operation expressly allowed by its cited roadmap item. Every patch-level `claim_strength_changes` array and every adjudication-level `claim_strength_authorizations` array is empty. The claim-surface manifest has zero registered surfaces. Accordingly, a generic permission to touch a block was not treated as permission to change claim strength: any actual rung or qualifier movement below had to be supported by the specific semantic instruction in the cited roadmap item.

## Thirteen-op rung and qualifier review

“Categorical/proved mathematical assertion” is used as the field-relative analogue of the ladder's categorical top rung; it does not recast these mathematical statements as causal empirical claims. “Outside ladder” means that the text is metadata, a definition, or project-administrative prose rather than an association/prediction/causation claim.

| Op | Block / roadmap | Claim surface and prior rung | Current rung | Hedge, null, limitation, or caveat movement | Specific authorization and E6 result |
|---:|---|---|---|---|---|
| 0 | B0016 / REV-005 | Claim-bearing site statement: categorical distinction between finite-flat and fppf; the covering convention itself was absent. | Same categorical site distinction, plus categorical definitional/subcanonicity statements outside the causal ladder. | No existing hedge or caveat is dropped. The added family convention does not claim the family has finite cardinality; the separate-site limitation remains. | REV-005 specifically requires the covering-family convention and the subcanonicity property. This is an authorized addition, not a silent rung move; no E6 row recorded. |
| 1 | B0019 / REV-004 | Claim-bearing formal setup: categorical exact-sequence/Ext statement, with topology suppressed. | Same categorical formal statement, now indexed in `Ab(C_tau)`. | No modality, null result, or caveat changes. The unindexed abbreviation is stated explicitly. | REV-004 specifically requires `tau`, `K_tau`, `e_tau`, and the category-indexed Ext group. Same rung; no E6 row recorded. |
| 2 | B0020 / REV-004 | Claim-bearing proved corollary: categorical `u_*e != V_N^*e`, `e != 0`, and `V_N^*e != 0`, for every `N>1` and every `u`. | Same categorical/proved rung with explicit `tau` and the matching category. | No universal quantifier, negation, null/non-null conclusion, or limitation is removed. | REV-004 specifically requires topology-indexed corollary wording. Same rung and exact mathematical range; no E6 row recorded. |
| 3 | B0022 / REV-001 | Claim-bearing literature positioning: categorical owner comparison plus a bounded negative search observation; explicit non-priority caveat. | Same owner-comparison rung and same bounded negative-observation rung, with a more reproducible surface/query record. | `bounded`, the owner restriction, and “not a claim of global priority” are preserved; “Within this declared scope” adds rather than drops a bound. The search date moves from 24 to 25 August 2026, but the claim remains date/surface bounded. | REV-001 specifically requires the updated indexes, query clusters, inclusion bounds, hit dispositions, proposition-level comparison, and non-priority wording. No rung or hedge drift detected; no E6 row recorded. |
| 4 | B0023 / REV-006 | Claim-bearing categorical summary of four features of the concrete proof. | Categorical conditional descent template under explicit hypotheses, followed by the concrete instantiation. | The new text adds a load-bearing caveat: failure of an unrelated target section is insufficient. It does not drop the uniqueness, overlap-nonzero, or every-`u` conditions. Abstracting the scope is not silently unconditional because every hypothesis is stated. | REV-006 specifically asks for this abstract template and separation from Witt/site inputs. The same categorical rung is retained; the authorized scope abstraction and added caveat produce no E6 row. |
| 5 | B0069 / REV-004 | Claim-bearing categorical transition: the extension criterion is formal in an abelian category. | Same categorical transition, instantiated in `Ab(C_tau)` for each topology. | No caveat or modality is removed; untouched Proposition 5.1 still states the general any-abelian-category criterion. | REV-004 specifically requires topology-indexed extension language. No rung movement; no E6 row recorded. |
| 6 | B0073 / REV-004 | Claim-bearing categorical proof: equality would produce a lift, contradicting one of the two nonlift theorems; every `u`. | Same categorical proof with the selected topology, matching theorem, `e_tau`, and `K_tau` made explicit. | No contradiction step, universal `u`, or theorem alternative is dropped. The B0074 continuation is explicitly bound to the fixed topology. | REV-004 specifically requires this proof-level indexing. Same rung and proof modality; no E6 row recorded. |
| 7 | B0091 / REV-002 | Project-administrative/scope prose outside the scientific ladder; it says Route/Gate credit is absent and “lift” is sheaf-theoretic. | Deleted. | The local scope sentence disappears, but the mathematical sheaf-lift limits remain byte-identical in B0090 and B0100; no scientific hedge, null result, or theorem caveat is lost from the manuscript. | REV-002 specifically orders deletion of the whole internal Route/Gate paragraph. The deletion is not an unregistered scientific-strength change; no E6 row recorded. |
| 8 | B0092 / REV-006 | Claim-bearing categorical conclusion: every nontrivial additive lift is ruled out on both sites and the pullback extension class is nonzero. It also presents four calculations as sufficient for reproducibility. | Same categorical theorem rung, now exactly `N>1`, each site, and `V_N^*e_tau != 0`; the four calculations are described as the computational core within a larger proof package. | The theorem hedge/range does not move. The proof-sufficiency recap moves downward by adding the Dedekind/sheaf/subcanonicity/detector/torsion-free qualification; no caveat is dropped. | REV-006 specifically requires separating the abstract template from precisely those arithmetic and site inputs. The downward qualification is specifically authorized rather than silent; no E6 row recorded. |
| 9 | B0005 / REV-003 | Authorship placeholder; no prior epistemic rung. | Confirmed declarative metadata outside the scientific ladder. | No scientific hedge/null/caveat is involved. The placeholder is replaced rather than reframed as a research result. | REV-003 specifically requires finalized human-approved byline metadata at B0005. This is a new metadata assertion, not a rung movement; no E6 row recorded. |
| 10 | B0096 / REV-003 | Contribution placeholder plus an approval condition; outside the scientific claim ladder. | Confirmed declarative contribution metadata. | The approval condition is removed only as the placeholder is finalized; no scientific-result limitation or null finding is removed. | REV-003 specifically requires finalized human-approved contribution text at B0096. No scientific-strength move; no E6 row recorded. |
| 11 | B0097 / REV-003 | Funding placeholder; no prior epistemic rung. | Confirmed negative funding declaration outside the scientific ladder. | A metadata null declaration is added. It is not a null study result and does not reframe evidence of absence/absence of evidence. | REV-003 specifically requires finalized funding information at B0097. No scientific-strength move; no E6 row recorded. |
| 12 | B0098 / REV-003 | Competing-interest placeholder; no prior epistemic rung. | Confirmed negative competing-interest declaration outside the scientific ladder. | A metadata null declaration is added. It is not a null study result or causal/evidential caveat. | REV-003 specifically requires finalized competing-interest information at B0098. No scientific-strength move; no E6 row recorded. |

## Token-conservation replay

The deterministic sibling was replayed against the exact round-1 patch and pre-round draft, with no optional protected terms because none is declared in the bundle:

```text
PYTHONPATH=<vendored-ars-root> python3 \
  ars/scripts/check_revision_token_conservation.py patch \
  --patch papers/22-fppf-verschiebung-lifts/notes/stage4_revision_patch_round1.json \
  --base papers/22-fppf-verschiebung-lifts/notes/stage3_revision_base.tex
```

The checker returned exit 0, top-level `conserved: false`, and four advisory rows:

| Token advisory | Exact deterministic delta | Semantic-review attribution (not an author disposition) |
|---|---|---|
| ADV-REV-1, op 3 B0022 / REV-001 | Numbers added: `1` x2, `4.3` x2, `4.5` x2, `21`, `23`, `4.7` x2, `03`, `010`, `06`, `25`, `7`, `2025`; no reported citation/protected-term delta. | Proposition/page/Stacks-tag locators and the bounded-search date/window added by the specific REV-001 instruction. The checker is multiset-based: the pre-round date's `24` is numerically offset by the new p. 24 locator, so E6 separately reviewed the 24-to-25 search-date change. |
| ADV-REV-2, op 4 B0023 / REV-006 | Numbers added: `0` x7 and `1` x1; no reported citation/protected-term delta. | Exact-sequence zeros, the `z_0` source-section notation, and the constant `1` in the selected Witt target `1-xT^N` in the specifically requested abstract template; not empirical quantities. |
| ADV-REV-3, op 8 B0092 / REV-006 | Number added: `1` x1; no reported citation/protected-term delta. | The explicit bound `N>1`, which preserves the old “nontrivial” theorem range in the specifically requested conclusion rewrite; not a changed empirical quantity. |
| ADV-REV-4, op 9 B0005 / REV-003 | Numbers added: `1` x2, `1037`, `430070`; no reported citation/protected-term delta. | Affiliation label, street number, and postal code in the specifically requested metadata replacement; not research-result quantities. |

Ops 0, 1, 2, 5, 6, 7, 10, 11, and 12 were token-conserved under the checker's declared grammar. `citations_delta` was empty for every op, but this grammar does not tokenize LaTeX `\cite{...}` commands; therefore that empty field is not promoted into a claim that LaTeX citations were mechanically conserved. Likewise, the empty protected-term deltas reflect the absence of an optional protected-term input, not a hedge-completeness result. The four token advisories are visible here and have not been converted into author dispositions.

## Comparison with the earlier Stage 4 audit

Only after the bundle replay, per-op rung review, and token replay were complete was `notes/stage4_e6_semantic_drift_audit.md` consulted as a comparison artifact (SHA-256 `7cf3329ae9a217040e68764f20ea0ea0fc7676f66eb451cbba52add13e34985d`). Its block-level outcome does not conflict with this fresh review, but it is not an input to the finding-set classification or a substitute for the bundle-bound audit above.

## Companion disposition boundary

The ordered `findings` array is empty, so there is no `ADV-E6-*` row for an author to restore, authorize with reason, or pause. No author choice was inferred or manufactured. If a later semantic review detects a row, this empty companion cannot dispose it; a new exact finding set and the protocol's raw-event-bound author-disposition workflow would be required.
