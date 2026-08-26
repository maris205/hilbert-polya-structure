# P22 Stage 4 E6 semantic-drift audit

## Verdict

**OVERALL PASS.** The official 13-operation apply is faithful to the immutable roadmap and the explicit author authority. All twelve replacements, the one deletion, and all four mechanically created fresh blocks were reviewed. No unauthorized claim-strength movement, lost theorem quantifier, topology conflation, proof-logic gap, literature-priority overstatement, metadata inference, or collateral change was found.

This is the required manual E6 review of unregistered claim surfaces. The claim-surface manifest contains no registered surfaces, so the mechanical apply receipt alone was not treated as a semantic verdict.

## Bound audit set

| Artifact | SHA-256 |
|---|---|
| `notes/stage3_revision_base.tex` | `32f7bea67f6c837a7e8b26b35aeb0297a13ec2c7f910abc09617dcb817c4a4a8` |
| `notes/stage3_revision_base.block-manifest.json` | `b21625abd194fc2f0cfdba0eb0193da5915bc81e4a7d26056a770c58f767cc91` |
| `notes/stage3_revision_roadmap.json` | `634205f0cd71f97f1204740b422aea1d4336ae6a256272a928665690aebc8737` |
| `notes/stage4_author_adjudication.json` | `b7f8c047b1f3fadb0739a1ac4c11848b61af169b1d94e72bbe8f633691a41ddb` |
| `notes/stage4_claim_surface_manifest.json` | `9307a9f2d6b5774e4e44a90d9f1d898789ffdcf8f43fe46887c07cefd0c15a15` |
| `notes/stage4_rev003_author_event_20260825.txt` | `eaac1940fcabccba6065beb59bef85566ecbd0ccf6bff3233e6abf517cd964f1` |
| `notes/stage4_rev003_contribution_event_20260825.txt` | `446f3fcac1358efc9db00541c8e6f625fc63a1a4b51ab8bd10bb2408c20c65bd` |
| `notes/stage4_rev003_author_metadata_input.json` | `a68802da320852f088a791a74c7dcf5ef96c843283b4897dd002682aae6ec595` |
| `notes/stage4_revision_patch_round1.json` | `e9c1debbb21a0b209847004de16fd76c9e1489844c4209417dd7fdb6b2ca5a6a` |
| `notes/stage4_revision_round1.tex` | `663ade71e41de81afd376db516ed8f548af3090cf342dd4db052eb212ce3c2d2` |
| `notes/stage4_revision_round1.tex.apply-report.json` | `95354037ded702bc6c73c61a0565b5529148b33cd341153f38e5eabbf1a1f45f` |
| `notes/stage4_nonliterature_independent_audit.md` | `6d1fb15e05f1b537957410132e3da3490988d6e1828ce3a03da23e210b613bb3` |
| `notes/stage4_rev001_research.md` | `d3ec672c3d793385546da0b60f1e5d967c20485047a4131c62c1151ec5154a3b` |

The patch's base, roadmap, adjudication, and claim-manifest bindings match these raw hashes. The apply report's base prefix, output prefix, and full patch digest match the files above. Both REV-003 event hashes in the confirmed metadata carrier match their raw event files exactly.

## Mechanical replay and collateral receipt

- All 13 `old_hash` preconditions match the corresponding blocks in the exact base.
- The twelve replacement payloads reproduce the applied block text exactly after the vendored fragment segmentation rule.
- B0091 is the only base block absent from the applied draft, exactly as authorized by REV-002.
- The only new block IDs are B0103, B0104, B0105, and B0106. They are, respectively, the second and third segments of B0022, the second segment of B0023, and the second segment of B0092; they contain no text outside the authorized replacement payloads.
- Of the 102 base blocks, 13 are touched and the other **89/89 are byte-identical** in the applied draft. There is no unexpected altered or missing base block, no additional fresh block, no heading edit, and no section-count change.

## Every touched and fresh block

| Block | REV | E6 verdict | Semantic finding |
|---|---|---|---|
| B0005 | REV-003 | **PASS** | Renders only the confirmed byline, affiliation/address, and contact email. `Contact:` and an affiliation superscript do not designate a corresponding author; there is no star, `thanks`, or corresponding-author label. |
| B0016 | REV-005 | **PASS** | Defines a finite-flat cover as a jointly surjective family whose members are finite and flat, without incorrectly requiring the family itself to be finite. The affine finite-locally-free translation and the subcanonicity use are accurate, and the fppf and finite-flat conclusions remain separate. |
| B0019 | REV-004 | **PASS** | Introduces \(\tau\in\{\fppf,\ff\}\), \(\mathcal K_\tau\), \(e_\tau\), and the Ext group in the same category \(\mathrm{Ab}(\mathscr C_\tau)\). Its unindexed-symbol convention is explicit. |
| B0020 | REV-004 | **PASS** | Preserves the complete range: each topology, every \(N>1\), and every endomorphism \(u\) in the matching sheaf category. Both \(e_\tau\ne0\) and \(V_N^*e_\tau\ne0\) remain stated. |
| B0022 | REV-001 | **PASS** | Supplies proposition-level owner comparison: Deninger v1 Propositions 4.3/4.5 and Corollary 4.7, Deninger--Mellit's different presentation owner, and the Stacks formalism are assigned distinct roles. No comparator is described as solving the present lifting problem. |
| B0103 | REV-001 | **PASS** | Records searched indexes, query clusters, the inclusion rule, and retained/excluded hit dispositions. The negative result is expressly bounded to the declared search and ends with “not a claim of global priority.” |
| B0104 | REV-001 | **PASS** | Keeps the contribution narrow: additive \(V_N\) lifting for the stated sheaf epimorphism, the all-index descent obstruction, and its formal extension consequence. Frobenius lifts, compatible Witt operations, and ring endomorphisms remain excluded. |
| B0023 | REV-006 | **PASS** | The abstract implication is logically complete: \(w=v(p(z_0))\), cover-local existence and uniqueness, and a nonzero overlap difference rule out a global preimage; a middle-object map inducing \((u,v)\) would send \(z_0\) to that forbidden preimage. Thus the pushout--pullback criterion yields the stated Ext inequality. It expressly rejects inference from an unrelated nonliftable target section. |
| B0105 | REV-006 | **PASS** | Instantiates every abstract datum with \(p=\omega\), \(z_0=(x)^\sharp\), \(v=V_N\), \(w=1-xT^N\), and the root cover, and separately names the uniqueness, site, detector, and torsion-free inputs. |
| B0069 | REV-004 | **PASS** | Binds the concrete obstruction to the topology-indexed \(e_\tau\) in the matching abelian category without changing the general proposition that follows. |
| B0073 | REV-004 | **PASS** | Fixes one \(\tau\), invokes the theorem for that same topology, and keeps “every \(u\).” Its final abbreviation sentence makes untouched B0074 a coherent continuation in the fixed category. |
| B0091 | REV-002 | **PASS** | Exact authorized deletion. No Route-A/Route-B, Route-coordinate, or Gate A--E language remains in the applied manuscript, and the B0090-to-B0092 transition is coherent. |
| B0092 | REV-006 | **PASS** | Restates the exact theorem range—an additive lift is ruled out for every \(N>1\) on each site—and the topology-indexed pullback nonvanishing. It does not generalize to \(N=1\), other sites, multiplicative lifts, or other owners. |
| B0106 | REV-006 | **PASS** | Distinguishes the reusable conditional mechanism from the example-specific proof package. The four finite calculations are described only as the computational core, not as an exhaustive proof, so the prior audit's proof-input omission is repaired. |
| B0096 | REV-003 | **PASS** | The contribution sentence is byte-for-byte the confirmed sentence in the metadata carrier: “Liang Wang conceived the study, developed and verified the proofs, conducted the literature review, and wrote and revised the manuscript.” |
| B0097 | REV-003 | **PASS** | Exactly renders the confirmed no-specific-funding statement. |
| B0098 | REV-003 | **PASS** | Exactly renders the confirmed no-competing-interests statement. |

## Per-REV conclusion

| Revision | Verdict | Roadmap and claim-strength conclusion |
|---|---|---|
| REV-001 | **PASS** | B0022/B0103/B0104 satisfy the reproducible bounded-positioning obligation. The base already made a bounded non-priority claim; the update adds audit detail and owner subtraction but does not promote it to novelty, completeness, or global priority. |
| REV-002 | **PASS** | Only the internal Route/Gate paragraph is deleted; no mathematical claim is removed or relocated. |
| REV-003 | **PASS** | All four authorized targets exactly implement human-confirmed authorship, contribution, funding, and conflict information. No corresponding author is inferred. |
| REV-004 | **PASS** | The topology-indexed notation is repaired consistently while the original modalities and universal quantifiers remain unchanged. |
| REV-005 | **PASS** | The finite-flat convention and the exact subcanonicity property used by the proof are made explicit; no result is transferred between topologies. |
| REV-006 | **PASS** | The abstract descent template is now sufficient, its arithmetic/site instantiation is separate, and the conclusion accurately carries all non-formal proof inputs. No theorem strengthening or weakening occurs. |

## Load-bearing invariant check

1. **Quantifiers:** The principal and extension conclusions still quantify over every integer \(N>1\); the untouched \(N=1\) identity control remains intact. No edited recap substitutes an ambiguous “nontrivial” range for \(N>1\).
2. **Topologies:** fppf and finite-flat remain distinct sites. Kernel sheaves, extension classes, and Ext groups are indexed by the selected topology, and the proof invokes the matching nonlift theorem rather than a change-of-site implication.
3. **Proof logic:** The local-to-global obstruction still requires the forced local preimage, its uniqueness on the root-cover source, and the nonzero double-overlap difference. The Ext conclusion is connected to the specific source section \((x)^\sharp\), not to an arbitrary target section.
4. **Literature strength:** The search statement is dated and surface-bounded, records owner exclusions, and explicitly denies a global-priority inference. The narrow contribution paragraph preserves the base manuscript's non-priority posture.
5. **Human metadata:** The raw author event establishes Liang Wang, the stated affiliation/address and email, no specific funding, and no competing interests. The separate raw confirmation event promotes exactly the recorded contribution sentence. Neither event designates a corresponding author, and the LaTeX does not create one.
6. **Untouched content:** The abstract, theorem statements, arithmetic proof, B0074 continuation, source correction, limitations, AI disclosure, bibliography commands, and all other unauthorized surfaces retain their exact base bytes.

## E6 disposition

**PASS — no semantic-drift correction is required before the next authorized gate.** This finding is limited to roadmap fidelity, authority fidelity, and semantic drift on the exact applied artifact; it is not a new global proof, literature-completeness, venue-readiness, or publication-integrity claim.
