# P22 Stage 4 progress checkpoint

> **Historical pre-apply snapshot.** This file is preserved for chronology
> and is superseded by `stage4_completion_report.md`.  Its hold, frozen-paper,
> and “next steps” statements are no longer current after the author's separate
> contribution confirmation and the successful official Round-1 apply.

Date: **2026-08-25**

Status: **IN PROGRESS — FIVE ITEMS PREFLIGHT PASS; REV-003 CONTRIBUTION HOLD**

## Outcome to date

The scholar's exact event approving all six Stage-3 roadmap items and starting
Stage 4 has been stored and bound into a complete
`author-adjudication/1.0`.  All six decisions are `will_address`; authorized
targets are exact subsets of the immutable reviewer proposals; claim-strength
and collateral authorizations are empty.

The current stage has produced evidence-bounded content for five items and a
writer-emitted nine-op candidate that deliberately excludes `REV-003`.  A
temporary full-authority apply preview, token-conservation audit, and complete
LuaLaTeX/BibTeX build pass.  No official patch has been applied because doing
so before the human metadata arrives would break the intended one-round
continuous evidence chain.

| Item | Current result | Gate |
|---|---|---|
| `REV-001` | Bounded exact-owner search rerun through 2026-08-25; B0022 candidate adds proposition-level comparison, query surfaces/clusters, inclusion bounds, nearest-hit dispositions, and non-priority wording using only the three existing verified bibliography keys. | Candidate preflight PASS. |
| `REV-002` | Exact deletion of public-manuscript block B0091; surrounding scope and conclusion remain intact. | Candidate preflight PASS. |
| `REV-003` | Liang Wang, the HUST affiliation/address, contact email, no-funding status, and no-competing-interests status were explicitly supplied on 2026-08-25.  The contribution statement is still not explicit. | **HOLD — contribution must not be inferred from single authorship.** |
| `REV-004` | `e_\tau`, `\mathcal K_\tau`, and topology-specific Ext categories are consistent across B0019/B0020/B0069/B0073; untouched proof continuation remains coherent. | Independent semantic PASS and candidate preflight PASS. |
| `REV-005` | B0016 now defines jointly-surjective finite-flat covering families and the subcanonical convention; wording matches Deninger v1. | Independent semantic PASS and candidate preflight PASS. |
| `REV-006` | B0023 states the complete source-section/middle-map condition; B0092 separates the reusable template, complete proof inputs, and four-step computational core with explicit `N>1`. | Two audit repairs incorporated; candidate preflight PASS. |

## Contract and build receipts

```text
AUTHOR_ADJUDICATION=PASS
AUTHOR_DECISIONS=6/6 will_address
CHAIN_START_INTEGRITY=PASS
REGISTERED_CLAIM_SURFACES=0
UNREGISTERED_CLAIM_DRIFT_REVIEW_REQUIRED=true

FIVE_ITEM_CANDIDATE_SCHEMA=PASS
FIVE_ITEM_CANDIDATE_AUTHORIZATION=PASS
OPS_APPLIED_IN_TEMP_PREVIEW=9
PRESERVED_BLOCKS=93/102
PRESERVED_RATIO=0.9118
STRUCTURAL_FLAGS=false
TOKEN_ADVISORIES=3 (all roadmap-attributed and explained)
TEMPORARY_FULL_BUILD=PASS
TEMPORARY_PDF_PAGES=13
UNDEFINED_CITATIONS=0
UNDEFINED_REFERENCES=0
OVERFULL_BOXES=0
MISSING_GLYPHS=0
FATAL_ERRORS=0
```

The candidate patch SHA-256 is
`47da386e9fb3939fce60dcbf57f5d9be03851e53f036de2cde0254f2009856d3`.
It is explicitly named `stage4_revision_patch_candidate_no_rev003.json` and
is not a final or bundle-eligible patch.

## Route-roadmap correspondence

The user-designated evaluator files remain byte-identical to the frozen
receipts:

- Route A: `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`;
- Route B: `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.

Deleting B0091 is public-paper cleanup only.  The topology notation,
finite-flat convention, and descent template are pure-algebra exposition and
supply none of the dynamics, operator, trace, determinant, or completed-zeta
inputs required by the two route evaluators.

```text
ROUTE_A_EVALUATION=NOT_TESTABLE
A0_A1_A2_A3_A4_TUPLE=NOT_ASSIGNED
ROUTE_A_ADVANCEMENT=NONE
ROUTE_B_ENTRY_AUTHORIZED=false
ROUTE_B_STATUS=ROUTE_B_NOT_TESTABLE
B1_B2_B3_B4_B5_TUPLE=NOT_ASSIGNED
GATE_A=NOT_REACHED
GATE_B=NOT_REACHED
GATE_C=NOT_REACHED
GATE_D=NOT_REACHED
GATE_E=NOT_REACHED
```

## Frozen official artifacts

No official manuscript or PDF write occurred in this checkpoint:

- `paper/manuscript.tex` SHA-256:
  `5976642a43907a3e01abdb586e9188c697d4a07e7137330a8f285538caaa02fc`;
- `paper/paper.pdf` SHA-256:
  `b106aa48ca5b3906a47691d035c29ed640aca378ed24adb51f29f83264daec3d`.

## Exact information needed to close REV-003

The author has now explicitly supplied the byline, affiliation/address,
contact email, funding, and competing-interest facts.  Only the contribution
statement remains.  The proposed exact text awaiting confirmation is:

```text
Liang Wang conceived the study, developed and verified the proofs, conducted
the literature review, and wrote and revised the manuscript.
```

The supplied email will be displayed as a contact email; the event did not
explicitly designate a corresponding author.  ORCID remains outside this
round unless the scholar later supplies one.

## REV-003 author-event receipts

The partial metadata event has been preserved without promoting the pending
contribution sentence into an author-confirmed fact:

- raw author event SHA-256:
  `eaac1940fcabccba6065beb59bef85566ecbd0ccf6bff3233e6abf517cd964f1`;
- normalized metadata input SHA-256:
  `4fecb2b01f639b8db4467c68c0b2238e0642dee6c7bb3a42fbbaffd3aaf67ba6`;
- independent metadata validation SHA-256:
  `4f1b0506c42ac2b3d831b523af22e8fa640e9550e53ad6660cb6d88dcbd870a5`;
- safe partial LaTeX draft SHA-256:
  `84719f1ad7e0fc1b8b074daa02d03965cec15454ce8583a91a38fa787d85fc1c`.

The earlier `stage4_rev003_metadata_audit.md` remains an immutable pre-input
snapshot.  Its “not established” findings for byline, funding, and competing
interests were superseded by the later author event above; its contribution
finding remains current.

## Next deterministic steps after the facts arrive

1. The writer re-emits one complete 13-op round-1 patch, adding B0005 and
   B0096--B0098 without altering the nine preflighted operations.
2. The orchestrator validates and applies that exact patch once to a new
   anchored Stage-4 draft.
3. Run token conservation and independent E6 semantic drift review, then
   mechanically materialize and fully compile the revised LaTeX/PDF.
4. Complete all six Schema 8 response items and the revision log from the
   apply report.
5. Build and validate `revision-evidence-bundle/1.0`, then stop at the Stage 4
   mandatory checkpoint.

Stage 3-prime re-review, submission, release, external contact, Git action,
and Route advancement do not start automatically.
