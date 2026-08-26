# P22 Stage 4 — REV-003 local metadata audit

Date: 2026-08-25 (UTC)  
Scope: local, read-only fact audit for `REV-003` only  
Write boundary: this audit file only; no manuscript, roadmap, author-adjudication, patch, or apply artifact was modified

## Audit question and evidence rule

This audit asks whether the local P22 record establishes four facts with an explicit,
traceable human confirmation:

1. the manuscript byline;
2. CRediT / author contributions;
3. funding; and
4. competing interests.

A value counts only when a local record explicitly states the value and binds it to a
human confirmation. A placeholder, workflow authorization, project-contact role,
bibliographic author field, AI/agent execution record, file author, or inferred division
of labor does not establish manuscript metadata.

Search scope:

- every text-readable file under `papers/22-fppf-verschiebung-lifts/`;
- the current manuscript source, the Stage-3 revision base, configuration and audit
  notes, the Stage-4 human event and author-adjudication input, bibliography, README
  files, and compiled-PDF metadata;
- the two user-designated roadmap records:
  `skills/route-a-evaluator.md` and `skills/route-b-evaluator.md`.

Search families included `byline`, `author`, `co-author`, `corresponding author`,
`affiliation`, `ORCID`, `CRediT`, the 14 CRediT role names, `contribution`, `funding`,
`funder`, `grant`, `competing interests`, `conflict of interest`, `declaration of
interest`, and confirmation/approval terms.

## Overall result

| REV-003 field | Result | Safe conclusion |
|---|---|---|
| Manuscript byline | **NOT ESTABLISHED** | No human-confirmed author name, author order, affiliation, or corresponding-author identity is present. |
| CRediT / author contributions | **NOT ESTABLISHED** | No named human is assigned any CRediT role, and no final contribution statement is human-approved. |
| Funding | **NOT ESTABLISHED** | Neither a no-specific-funding declaration nor a funded declaration with funder/grant data is confirmed. |
| Competing interests | **NOT ESTABLISHED** | Neither a no-competing-interests declaration nor an affirmative disclosure is confirmed. |

`REV-003` has human-authorized write scope, but its replacement values are absent.
Therefore the metadata-content gate is:

```text
REV-003_METADATA_CONTENT=BLOCKED_PENDING_HUMAN_VALUES
```

## Human authorization receipt: authority exists, values do not

The Stage-4 event is genuine and hash-bound:

- Evidence: `papers/22-fppf-verschiebung-lifts/notes/stage4_author_event_20260825.txt:1`

  > 批准全部六项路线图，开始 Stage 4

- Raw SHA-256:
  `48b7e54cdd244c8ad985aa602f1042aae2c2846475c21a03374dd8351f89fa78`.
- Evidence: `papers/22-fppf-verschiebung-lifts/notes/stage4_author_choices.json:5-8`

  > `"source": "explicit_session_user_message"`  
  > `"actor_role": "author"`  
  > `"input_sha256": "48b7e54cdd244c8ad985aa602f1042aae2c2846475c21a03374dd8351f89fa78"`

For `REV-003`, the event authorizes `replace_block` on `B0005`, `B0096`,
`B0097`, and `B0098`:

- Evidence: `papers/22-fppf-verschiebung-lifts/notes/stage4_author_choices.json:49-68`

  > `"item_id": "REV-003"`  
  > `"author_triage": "will_address"`  
  > `"block_id": "B0005"`  
  > `"block_id": "B0096"`  
  > `"block_id": "B0097"`  
  > `"block_id": "B0098"`

The event text contains no author name, contribution role, funding value, or
competing-interest declaration. It authorizes addressing the item; it does not
provide or confirm the facts needed to fill the four blocks.

## 1. Manuscript byline — NOT ESTABLISHED

### Local evidence

- Evidence: `papers/22-fppf-verschiebung-lifts/paper/manuscript.tex:47-50`

  > `\title{\textbf{A Descent Obstruction to Verschiebung Lifts\\`  
  > `on fppf and Finite-Flat Sites}}`  
  > `\author{AUTHOR TO CONFIRM}`

- Evidence: `papers/22-fppf-verschiebung-lifts/notes/stage3_revision_base.tex:51-55`

  > `<!--block:B0005-->`  
  > `\author{AUTHOR TO CONFIRM}`

- Evidence: `papers/22-fppf-verschiebung-lifts/notes/stage2_paper_configuration.md:24-25`

  > `| **Co-Authors** | \`AUTHOR TO CONFIRM\` |`  
  > `| **Funding** | \`AUTHOR TO CONFIRM\` |`

- Evidence: `papers/22-fppf-verschiebung-lifts/paper/README.md:28-31`

  > Author identity, contributions, funding, and competing-interest fields must  
  > be confirmed by the human author.

- Read-only compiled-PDF check: `papers/22-fppf-verschiebung-lifts/paper/paper.pdf`
  reports an empty `Author:` metadata field via `pdfinfo`.

### Finding

No ordered human name, affiliation mapping, or corresponding-author identity is
locally confirmed. `AUTHOR TO CONFIRM` is an explicit unresolved placeholder,
not a pseudonym and not permission to infer a name.

### Minimum user-supplied fields

1. Ordered author name(s), exactly as they should appear in the manuscript.
2. Affiliation(s), mapped to each named author.
3. Corresponding author name and email, or an explicit statement that none is to
   be designated in the manuscript.
4. Confirmation that every named author approves the byline and final manuscript
   responsibility.

ORCID is optional for this local replacement unless the intended venue requires it;
it must not be invented.

## 2. CRediT / author contributions — NOT ESTABLISHED

### Local evidence

- Evidence: `papers/22-fppf-verschiebung-lifts/paper/manuscript.tex:950-952`

  > `\paragraph{Author contributions.}`  
  > `AUTHOR TO CONFIRM.  Named authors must approve the mathematical content and`  
  > `the final contribution statement before submission or public release.`

- Evidence: `papers/22-fppf-verschiebung-lifts/notes/stage3_revision_base.tex:1045-1048`

  > `<!--block:B0096-->`  
  > `\paragraph{Author contributions.}`  
  > `AUTHOR TO CONFIRM.  Named authors must approve the mathematical content and`  
  > `the final contribution statement before submission or public release.`

- Evidence: `papers/22-fppf-verschiebung-lifts/notes/phase4_writer_contract_report.md:35-39`

  > Required data availability, ethics, author contributions, funding,
  > competing-interests, AI-use, and limitations statements are present.  
  > Identity, funding, and competing-interest content remain openly marked  
  > AUTHOR TO CONFIRM, rather than being invented.

- Evidence: `papers/22-fppf-verschiebung-lifts/paper/manuscript.tex:960-964`

  > AI-assisted tools were used during literature triage, proof-audit support,  
  > and drafting. Every mathematical claim, reference, attribution, and  
  > wording choice requires final verification and responsibility by the named  
  > human author before dissemination. No AI system is listed as an author.

### Finding

No local record assigns any named human a CRediT role. The recorded use of AI or
the presence of agent-generated artifacts cannot be converted into an author or
contributor assignment. The work visible in repository files also cannot be used
to infer which human performed Conceptualization, Formal analysis, Methodology,
Writing, Validation, or any other role.

### Minimum user-supplied fields

1. For each confirmed author, the applicable CRediT role(s) from the closed
   14-role taxonomy; use `Lead` / `Supporting` only if the authors want those
   degrees recorded.
2. Explicit confirmation that all named authors approve the role allocation and
   the final contribution statement.
3. If this is a single-author paper, explicit confirmation of single authorship
   and the roles the sole author accepts; do not silently assign all roles.

## 3. Funding — NOT ESTABLISHED

### Local evidence

- Evidence: `papers/22-fppf-verschiebung-lifts/paper/manuscript.tex:954-955`

  > `\paragraph{Funding.}`  
  > `AUTHOR TO CONFIRM.`

- Evidence: `papers/22-fppf-verschiebung-lifts/notes/stage3_revision_base.tex:1050-1052`

  > `<!--block:B0097-->`  
  > `\paragraph{Funding.}`  
  > `AUTHOR TO CONFIRM.`

- Evidence: `papers/22-fppf-verschiebung-lifts/notes/stage2_paper_configuration.md:25`

  > `| **Funding** | \`AUTHOR TO CONFIRM\` |`

### Finding

The audited scope contains no human-confirmed statement that the work received no
specific funding, and no confirmed funder, grant type, grant/award number, recipient,
or funder-role declaration. Absence of a grant record cannot be promoted into a
no-funding statement.

### Minimum user-supplied fields

Choose exactly one branch:

- **No specific funding:** explicitly confirm that the research received no
  specific grant from public, commercial, or not-for-profit sectors; or
- **Funded:** for every source, provide the official funder name and grant/award
  number (or explicitly state that no number exists). Also provide any mandatory
  funder wording and whether the funder had a role in study design, analysis,
  publication decision, or manuscript preparation.

Funding and competing interests must be answered separately.

## 4. Competing interests — NOT ESTABLISHED

### Local evidence

- Evidence: `papers/22-fppf-verschiebung-lifts/paper/manuscript.tex:957-958`

  > `\paragraph{Competing interests.}`  
  > `AUTHOR TO CONFIRM.`

- Evidence: `papers/22-fppf-verschiebung-lifts/notes/stage3_revision_base.tex:1054-1056`

  > `<!--block:B0098-->`  
  > `\paragraph{Competing interests.}`  
  > `AUTHOR TO CONFIRM.`

### Finding

The audited scope contains neither a human-confirmed no-competing-interests
declaration nor an affirmative disclosure. A lack of visible relationships in the
repository is not evidence that no relationship exists.

### Minimum user-supplied fields

Choose exactly one branch and have every named author approve it:

- **None:** explicitly confirm that the authors have no known competing financial
  interests or personal relationships that could have appeared to influence the
  reported work; or
- **Exists:** identify the author, relationship type, organization/person involved,
  and the relationship needed for a complete disclosure. State whether the remaining
  authors declare no competing interests.

## Exclusion ledger

| Local candidate | Evidence | Why it cannot establish P22 authorship or declarations |
|---|---|---|
| Professor Christopher Deninger | `notes/author_contact_draft.md:11`: “Dear Professor Deninger,” | He is the source/preprint author and proposed contact recipient, not a confirmed P22 manuscript author. |
| Deninger, Mellit, and The Stacks Project Authors | `paper/references.bib:2,16,28` contains bibliography `author` fields | These are authors of cited works, not P22 byline evidence. |
| Contact-draft signatory | `notes/author_contact_draft.md:66-68`: “With best regards, `[Author name(s)]`” | The signatory remains an unresolved placeholder. The file is explicitly `UNSENT`. |
| Stage-4 `actor_role: author` | `notes/stage4_author_choices.json:5-8` | This proves the authority class and event binding, not the person's publication name, affiliations, contributions, funding, or COI. |
| AI-assisted tools / agents | `paper/manuscript.tex:960-964`: “No AI system is listed as an author.” | AI execution or generated files cannot be converted into authorship or CRediT roles. |
| File or Git authorship | Not used as an evidence source | File provenance does not prove manuscript authorship or declaration approval. |

The contact draft additionally states at `notes/author_contact_draft.md:3-5`:

> **Status: UNSENT.** This is an internal drafting artifact only. No external  
> contact has been authorized or made. Verify the final manuscript, author  
> names, and attachment set before any future use.

## Two roadmap-record search receipt

`papers/22-fppf-verschiebung-lifts/notes/stage2_5_integrity_report.md:120-125`
identifies the exact user-designated roadmap records by digest. The current local
digests match:

| Record | SHA-256 | Metadata-specific search result |
|---|---|---|
| `skills/route-a-evaluator.md` | `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c` | No word-bounded match for byline/authorship, CRediT/contributions, funding/grants, competing/conflict declarations, ORCID, or affiliation. |
| `skills/route-b-evaluator.md` | `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595` | No word-bounded match for the same metadata families. |

Their own headers identify them as evaluator instructions, not P22 fact records:

- `skills/route-a-evaluator.md:2-3`: `name: route-a-evaluator`; “Evaluate whether
  a proposed classical dynamical system ... is a credible Route-A candidate”.
- `skills/route-b-evaluator.md:2-3`: `name: route-b-evaluator`; “Evaluate whether
  a strong Route-A candidate can be promoted to a rigorous Hilbert-Pólya
  realization”.

No metadata value can be imported from either record.

## Minimal user reply template

The following is the smallest fact payload that can close this local audit without
inference:

```text
BYLINE
- Authors in publication order:
- Affiliation(s), mapped to each author:
- Corresponding author + email, or “none designated”:
- All named authors approve the byline and final responsibility: YES / NO

CREDIT
- [Exact author name]: [CRediT role(s)]
- All named authors approve the contribution allocation: YES / NO

FUNDING — choose one
- NONE: confirm no specific public, commercial, or not-for-profit grant; OR
- FUNDED: [official funder]; [grant/award number or explicitly none];
  [mandatory wording, if any]; [funder role or no-role confirmation]

COMPETING INTERESTS — choose one
- NONE: all named authors confirm no known competing financial interests or
  personal relationships; OR
- EXISTS: [author]; [relationship type]; [organization/person];
  [remaining-author declaration]
```

Until these values are supplied and explicitly confirmed, `B0005` and
`B0096`--`B0098` must retain a fail-visible unresolved state. This audit does not
authorize fabricated defaults such as single authorship, “all CRediT roles,”
“no funding,” or “no competing interests.”
