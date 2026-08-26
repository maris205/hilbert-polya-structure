# P22 Stage 4.5 Round 2 E6 independent semantic audit

Audit date: **2026-08-25 UTC**  
Mode: **fresh full-bundle model-mediated semantic review after authorized integrity correction**

## Recorded result

**none detected by the recorded semantic review**

The schema-valid companion has an empty ordered finding set. This is a
model-mediated review result, not a deterministic no-drift certificate, a
completeness claim, or an author disposition. The review began with the whole
two-round Revision-Evidence Bundle and did not inherit the conclusion of the
earlier Stage 4 or Stage 4.5 Round 1 audits.

## Exact bindings

| Field | Value |
|---|---|
| Final anchored draft | `notes/stage4_5_integrity_revision_round2.tex` |
| Final anchored draft SHA-256 | `a93b64f5ad41ede0ddaef8ad6fa46800092a9abd5d75fb099d357b54ea2058a2` |
| Public draft SHA-256 | `e90dd88109d4e53d1f789808286c15cc917003cd38b69f49ddaff8661b9158ed` |
| Revision-Evidence Bundle SHA-256 | `c665cee2e8c2288fb2c8e17a0e7e7e935b8062813a42d67cc8cea892ed6c10a9` |
| Finding companion SHA-256 | `9f3e7795831e2086686d6f527b51c117d6d73afbccd2453685e1df30b652e982` |
| Detector kind | `model_mediated_semantic_review` |
| Detector ID | `codex-session-model/p22-stage4.5-round2-e6-independent-20260825` |
| E6 protocol SHA-256 | `f26d4e0b876f323db5fccc1bbc3120189e69282e45ec6b6cc0cee1e3b1e7a537` |
| Claim-strength ladder SHA-256 | `22f51a6fefb2525e685b6938cc446fa658bdfb6e43157b5d2e6d5051f2212dfe` |
| Token checker SHA-256 | `19908ee8469d25497796190ec9a731d510c9db8ad7484da24ac657971aa853fb` |
| Finding schema SHA-256 | `c0c58f2c39544929ef52c3c2d3046b50c92c290896ac26e1c891ddea08fdaf98` |
| Bundle validator SHA-256 | `5341358d489a550b56f0e7efde850c551b6d9df41106b0462e2f804ab4de9998` |

Deleting only whole-line block-marker comments from the final anchored draft
reproduces the exact public draft. The finding companion therefore binds the
comparison authority while the public-draft hash binds the dissemination
surface.

## Fresh bundle replay

The first mechanical operation was a fresh `validate-bundle` replay against
the project root. It returned `revision evidence bundle ok`. The bundle is a
continuous two-round chain:

| Round | Kind | Pre-round SHA-256 | Post-round SHA-256 | Ops |
|---:|---|---|---|---:|
| 1 | `review_roadmap` | `32f7bea67f6c837a7e8b26b35aeb0297a13ec2c7f910abc09617dcb817c4a4a8` | `663ade71e41de81afd376db516ed8f548af3090cf342dd4db052eb212ce3c2d2` | 13 |
| 2 | `integrity_correction` | `663ade71e41de81afd376db516ed8f548af3090cf342dd4db052eb212ce3c2d2` | `a93b64f5ad41ede0ddaef8ad6fa46800092a9abd5d75fb099d357b54ea2058a2` | 2 |

Round 2 also replay-validates the exact issue list, author authorization,
patch SHA `421e969a54bcd5a783faeab1485605533e4465bd8b7e4289cdf522de0770ebc0`,
old-hash preconditions, two allowed targets, and the apply report. The apply
report records 103/105 blocks byte-preserved and no structural flag.

## Fifteen-op rung, hedge, null, limitation, and caveat review

For proved mathematical statements, “categorical/proved” is the
field-relative analogue of the ladder's top categorical rung. “Outside
scientific ladder” denotes metadata, definitions, or administrative prose.

| Round/op | Block / authority | Fresh semantic result |
|---|---|---|
| 1/0 | B0016 / REV-005 | Same site distinction; requested covering convention and subcanonicity added. No hedge or limitation removed. |
| 1/1 | B0019 / REV-004 | Same exact-sequence/Ext claim, now correctly topology-indexed. |
| 1/2 | B0020 / REV-004 | Same `N>1`, every-`u`, nonzero Ext consequences; only category/topology indexing changes. |
| 1/3 | B0022 / REV-001 | Bounded literature observation remains date/surface bounded and explicitly disclaims global priority. |
| 1/4 | B0023 / REV-006 | Requested abstract descent template states all load-bearing hypotheses and adds, rather than removes, a caveat about unrelated target sections. |
| 1/5 | B0069 / REV-004 | Same formal abelian-category transition, instantiated per topology. |
| 1/6 | B0073 / REV-004 | Same contradiction and every-`u` range; selected topology and theorem are made explicit. |
| 1/7 | B0091 / REV-002 | Internal Route/Gate administration deleted as authorized; the scientific scope limitations remain elsewhere unchanged. |
| 1/8 | B0092 / REV-006 | Theorem range remains `N>1` on both sites; proof-sufficiency wording is narrowed by listing the larger proof package. |
| 1/9 | B0005 / REV-003 | Author/byline placeholder finalized from explicit author metadata; outside scientific ladder. |
| 1/10 | B0096 / REV-003 | Contribution metadata finalized exactly as authorized; outside scientific ladder. |
| 1/11 | B0097 / REV-003 | Negative funding declaration finalized; administrative null, not a study-result null. |
| 1/12 | B0098 / REV-003 | Negative competing-interest declaration finalized; outside scientific ladder. |
| 2/0 | B0005 / IL-MINOR-1 | `24` to `25 August 2026` synchronizes metadata chronology. Exact-authorized and outside scientific ladder; no claim rung or caveat moves. |
| 2/1 | B0094 / IL-MINOR-2 | Deferred materials-status prose becomes an explicit author-owned “upon reasonable request” policy. Exact-authorized administrative declaration; it does not assert a public repository, redistribute third-party sources, or change a scientific claim. |

Every Round 1 patch-level `claim_strength_changes` array and every matching
adjudication authorization array is empty. Both Round 2 operations likewise
declare no claim-strength change and exactly match their authorized
integrity-correction targets. Fresh semantic inspection found no silent rung
increase, hedge deletion, limitation removal, null-result reframing, universal
quantifier expansion, or unauthorized caveat movement across any of the 15
operations.

## Round 2 token-conservation sibling

`notes/stage4_5_token_conservation_round2.json` reports one advisory:

| Row | Deterministic delta | Semantic attribution |
|---|---|---|
| `ADV-REV-1` | B0005 removes number `24` and adds `25`; citation and protected-term deltas are empty. | Exact date synchronization required by IL-MINOR-1; metadata only. |

B0094 is conserved under the checker's number/citation/protected-term grammar.
These token results are advisory and do not supply the semantic conclusion.
The empty protected-term delta is not promoted into a completeness claim.

## Operational boundary

The new availability statement is truthful only insofar as the author retains
and can lawfully share the author-owned proof ledger, locator audit, claim
manifest, and compilation materials when a reasonable request is received.
It does not authorize redistribution of third-party full text. This practical
obligation is not a scientific claim-strength finding and does not alter the
zero-finding E6 companion.
