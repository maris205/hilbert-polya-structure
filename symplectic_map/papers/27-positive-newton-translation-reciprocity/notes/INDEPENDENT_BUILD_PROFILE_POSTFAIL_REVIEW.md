# Independent review of the Paper 27 post-failure build profile

## 1. Authority, target, separation, and historical disposition

This is the sole mechanical aggregate authorized by
`B07-E0287-P27-POSTFAIL-PROFILE-FRESH-DUAL-REREVIEW-PASS-CONSUMPTION-AND-AGGREGATE-ARTIFACT-AUTHORIZATION`.
The aggregate-path no-follow presence preflight returned absent.  The E0287
authority ledger then had 1,446,658 bytes, 17,243 LF, mode 0644, link one,
SHA-256
`49aa7151c637276d86a9f040dff7a3faaedeb6078e56ebde3da5f6bfedaa41d0`,
and ended in
`BATCH07_P27_POSTFAIL_PROFILE_AGGREGATE_ARTIFACT_AUTHORIZED`.

Both fresh reviewers independently reviewed the E0286 opening ledger at
1,440,939 bytes, 17,186 LF, mode 0644, link one, SHA-256
`e45664dc9023f6530577d79251c0aa1f2ca12dbf58f04b27f16f430cbf46a312`,
ending in
`BATCH07_P27_POSTFAIL_PROFILE_FRESH_DUAL_ZERO_WRITE_REREVIEW_AUTHORIZED`.
Their common exact target was
`notes/BUILD_PROFILE_POSTFAIL.md`, 53,878 bytes, 963 LF, mode 0644, link
one, SHA-256
`f4829e21e4626b372a05e646f34d29f0ea306b653d23d6dd924d1fc54161687e`,
strict UTF-8/LF with no BOM, CR, or NUL, exactly one terminal LF, and terminal
`BATCH07_P27_BUILD_PROFILE_POSTFAIL_AUTHOR_STOP`.

Rereviewer C and Rereviewer D worked from separated contexts.  Neither read
the other report or any earlier reviewer report.  Neither wrote a file,
executed, imported, or compiled the validator, invoked a build/PDF tool, or
probed, listed, statted, or read any Paper 27 `build/*` entity.  Build-path
strings were inspected only as literals in authorized control files.  This
aggregate author adds no review conclusion; it records the two complete
substantive reports and their conjunction.

The first dual review remains immutable history: Reviewer A returned PASS
with Blocker=0, Major=0, Minor=0, Ambiguity=0, while Reviewer B returned FAIL
with Blocker=0, Major=0, Minor=0, Ambiguity=2.  E0285 froze the two findings:

1. a prospective `plain.bst` sentence could be read as reopening an already
   consumed dependency-read gate; and
2. an `It` antecedent could be read as letting the aggregate review artifact,
   rather than a later build-author ledger event, authorize bootstrap.

E0286 bound the exact two-hunk correction: +329 bytes and +6 LF, with the
profile terminal unchanged.  Neither the failed bytes nor the findings are
erased by the fresh PASS reports below.

## 2. Fresh Rereviewer C report

### 2.1 Direct identity and control evidence

Rereviewer C reproduced the E0286 ledger and corrected-profile identities
printed above.  It also reproduced all exact allowed frozen controls:

| Control | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `notes/BUILD_PROFILE_SUCCESSOR.md` | 45,627 | 816 | `2e608faaa05e3063352c193869b92d5a305cc3de956ad18624d457b303787bec` |
| `notes/DEPENDENCY_LOCK_SUCCESSOR.md` | 30,145 | 215 | `66c96cc6b40658370cc129e3bf828bcd08a7e69f7f2462ebea084cc77ce6ed17` |
| `notes/INDEPENDENT_DEPENDENCY_LOCK_SUCCESSOR_REVIEW.md` | 12,687 | 231 | `b37e361c1cb8e7340c7a2e4af5b207de40df935ced707043c63c1e0f7017df35` |
| `notes/INDEPENDENT_STATIC_SOURCE_SUCCESSOR_REVIEW.md` | 31,760 | 704 | `7745af4b80e4e5ff35134e9279b7d2493f9b063bac0110bab115199bae3114ae` |
| `notes/VALIDATOR_LOCK_SUCCESSOR.md` | 57,684 | 1,061 | `c770bdba165b60953253c50b0050537b00ea2c4bbd7322140cb372f319f37d65` |
| `notes/BUILD_VALIDATOR_SUCCESSOR.py` | 398,248 | 9,360 | `27c8f1e6535602f3cdc734eb8bf89ad28889493532d9628c31d9d95e78faffc1` |

Each is regular mode 0644 and link one.  The frozen source trio also matched
the profile and source review exactly:

| Source | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `paper/main.tex` | 55,063 | 1,681 | `d60ec6611683cafdf822b4cb493040258dc1dd29502363d493f52c3e2deeed3e` |
| `paper/math_commands.tex` | 601 | 17 | `34fdee026ed49adf9d7ad2d3b3c2d397549f29fd9f896fe5d54e046456e30957` |
| `paper/references.bib` | 6,610 | 217 | `a77d814de144852c760c9c6e894ad92ea567dd03be188e2786662aaf7cb521e5` |

The complete old/new profile diff showed no semantic drift in Sections 5,
7, 8, or 9.  Section 3 adds only the frozen E0280 launcher boundary; the tool
and environment tables are unchanged.  Section 6 changes only the reserved
build-evidence name.  Every other difference is classified as immutable
failure history, new namespace/control identity, consumed dependency state,
parser correction, or downstream gate closure.

The profile candidate fence and dependency lock each contain the same 87
ordered logical paths.  The lock has 86 distinct final regular targets and
two symlink rows; set difference, order difference, sorting error, and
identity error were all zero.  The `plain.bst` sentence is now explicit
consumed past history, binds the passed lock/review, and ends with the
unconditional statement that no new candidate or target read is opened.

The E0280 launcher and profile contain the same thirteen literal lines with
zero mismatch.  The frozen argv0 remains
`batch07-p27-successor-liveness-fd-scrub-launcher`; file descriptors 0/1/2
are proved live before every other decimal descriptor is closed; only soft
`RLIMIT_NOFILE` is lowered to 4096; `env -i` is assigned only environment
clearing; and the consumed audits and microtests are not reopened.

Static text inspection found 15 modes in both `MODE_ARITY` and
`VALIDATOR_RESULT_FIELDS`, 90 field occurrences, and 52 distinct field
names.  The predecessor invalid-only defect covers exactly `root`, `stage`,
`checkpoint`, `id`, `dependencies`, and `disposition`.  The corrected profile
requires total name dispatch for all six, exactly one accepting branch for
each field in all fifteen modes, fifteen canonical valid details, and invalid
mutations for each symbolic field while preserving decimal, ordinary hash,
warning-hex, recorder-hash, and cross-manifest predicates.

### 2.2 Complete scope conclusions

- E0282 failure preservation: PASS.  A000, the old controls, and all three old
  build namespaces are immutable history with no read, probe, retry, cleanup,
  reuse, retroactive PASS, or release.
- New namespace freshness: PASS.  The evidence, r0, r1, evidence/r0,
  evidence/r1, and evidence/cross-root paths are reserved and unprobed, not
  asserted absent.  Future presence is permanent STOP; no suffix or reuse.
- Source, dependency, tools, and environments: PASS.  The source trio, 87/86
  dependency closure, exact compiler/BibTeX/admin tools, and mutually
  exclusive PUBLICATION/ADMIN/VALIDATOR environments are preserved.
- Root lifecycle: PASS.  Each root has exactly
  `pdflatex -> bibtex -> pdflatex -> pdflatex`; there is no fifth pass, retry,
  repair, or cross-root copy, and root1 cannot be probed after root0 failure.
- Receipts and immutable evidence: PASS.  Receipt triples, snapshots, five raw
  manifests, exclusive creation, no-follow checks, and no overwrite remain.
- Publication acceptance: PASS.  The 20-key bibliography closure, 24--28
  proof pages, sentinel/reference equality, warning/error closure, PDF 1.5,
  portrait/metadata, Type1/font streams, raw-token and decoded-text checks,
  and anonymity constraints remain complete.
- Cross-root acceptance: PASS.  Raw product equality, three recorder
  root-prefix projections, five manifest pairs, and the sole in-memory
  `main.fls` raw-SHA projection remain exact; no raw evidence is rewritten.
- Namespace census: PASS.  Old build names occur only in immutable history;
  old dependency/source controls and launcher argv0 are intentional; there is
  no stale active build or control namespace.
- Finding A1: CLOSED.  The dependency statement is consumed past history and
  cannot authorize a new read.
- Finding A2: CLOSED.  Only an explicit later build-author ledger event, after
  profile aggregate PASS, new validator/lock independent review PASS, and a
  separately authorized runtime microtest PASS, may authorize bootstrap.
- Downstream closure: PASS.  Validator authoring/review, runtime microtest,
  build, evidence, build review, release-integrity, local release, and Paper
  28 remain serial and unopened by the profile itself.

Rereviewer C exact findings: none.

`Blocker=0; Major=0; Minor=0; Ambiguity=0`

`PASS`

`PROFILE_REREVIEW_C_PASS`

## 3. Fresh Rereviewer D report

### 3.1 Direct evidence and stale-namespace census

Rereviewer D independently reproduced the same E0286, corrected-profile, and
six frozen-control identities, strict encoding, and terminal constraints.  It
performed a sentence-level future-authority and stale-namespace census.

All `successor-d60ec6611683-*` profile occurrences are confined to the exact
immutable old-build block.  Permitted predecessor names are limited to the
read-only profile/validator/lock baseline, passed dependency/static-source
controls, historical recorder provenance, and the frozen E0280 argv0.  There
is no active old validator review, build evidence/review, evidence stage, or
certified-root namespace.  The active namespace is exactly the three new
direct children and three new stages.  All six are unprobed and carry no
absence claim; presence later is permanent STOP with no fallback, deletion,
rename, or reuse.

### 3.2 A1 and A2 adversarial rereview

Finding A1 is closed.  The `plain.bst` declaration is expressly positioned
before an already consumed dependency-lock derivation, uses past tense for
its then-unclaimed existence/type/chain/bytes, states that consumed events
froze it in the passed lock/review, and grants no new candidate or target
read.  Later chain prose is limited to consumed derivation rules and future
exact rebind of already locked paths.  The fence has 87 rows and the lock 86
unique final targets; prospective extras remain forbidden and unopened.

Finding A2 is closed.  The aggregate artifact can only bind the two complete
separated reports.  The sole authorization subject is the explicit phrase
`Only a later build-author ledger event`, and that subject is conditioned on
aggregate profile PASS, new validator/lock independent review PASS, and
separately authorized runtime microtest PASS.  Only that later event may
authorize evidence bootstrap, ordered root mutations, receipts, and the one
reserved build-evidence record.  `This profile` only reserves the path and
explicitly grants no authority to create it.  No remaining pronoun admits a
review artifact as a build authorizer.

### 3.3 Launcher and frozen validator predicate baseline

The thirteen launcher lines, argv0, standard-FD liveness guard, arbitrary
extra-FD scrub, soft-limit-only change, two absolute empty-environment
boundaries, positional row script, and consumed-test rule all match E0280.

The predecessor source proves the same six invalid-only parser structures.
It otherwise supplies the frozen baseline required by the corrected profile:
15 modes and 74 exact argv rows; no-follow identity pools; filesystem/text
ceilings; runtime image/import/environment/FD/RLIMIT/source-copy-lock holds;
87/86 dependency rebind; receipt guards and exact stage/evidence universes;
exclusive snapshots/manifests; recorder/BIB/LOGBIB/PDFINFO/PDFTEXT; PDFRAW
object graph, xref, semantic tokens, `/Contents`, resources and fonts; Type1
decoding and bounded concrete/abstract execution; SOURCEFINAL, STAGEINV,
CROSS, and EVIDENCE; terminal recomputation and post-emission checks; and the
external trust-boundary premises.  The corrected profile permits changes only
to the six parser branch structures and exact regime-specific namespace and
control identities.

### 3.4 Preservation and semantic-diff conclusions

The source trio, dependency closure, tools, environments, four publication
commands, receipts, snapshots, manifests, root0-before-root1 first-fail rule,
and cross stage after two local PASS results all remain unchanged.  Log,
bibliography, sentinel, page, PDF, font, anonymity, raw equality, recorder
projection, and manifest-projection rules show no regression.

The two-hunk correction footprint is exactly +329 bytes and +6 LF with the
terminal unchanged: A1 contributes +164 bytes/+2 LF and A2 contributes +165
bytes/+4 LF.  No correction diff touches scientific, source, dependency,
tool, environment, publication, PDF/Type1, cross-root, release, or external
effect semantics.

The downstream sequence remains profile aggregate, validator/lock authoring,
fresh validator review, separately authorized runtime microtest, later
build-author event, evidence author stop, fresh build review, separately
authored/reviewed release-integrity, then Paper 28.  Release remains local and
external effect remains none.

Rereviewer D exact findings: none.

`Blocker=0; Major=0; Minor=0; Ambiguity=0`

`PASS`

`PROFILE_REREVIEW_D_PASS`

## 4. Aggregate conjunction and scope

The two fresh reports bind the same exact E0286 status and corrected profile,
cover the complete E0286 rereview scopes, independently close both historical
ambiguities, and have no conflicting evidence or conclusion.

| Report | Blocker | Major | Minor | Ambiguity | Result |
|---|---:|---:|---:|---:|---|
| Rereviewer C | 0 | 0 | 0 | 0 | PASS |
| Rereviewer D | 0 | 0 | 0 | 0 | PASS |
| Conjunction | 0 | 0 | 0 | 0 | PASS |

This artifact certifies only the corrected post-failure build profile and its
frozen derivation controls.  It is not a validator source/lock review, runtime
test, build review, release-integrity review, build authorization, network
action, or external effect.  No validator source/lock or build path was
created, imported, compiled, executed, or probed during either review.

BATCH07_P27_BUILD_PROFILE_POSTFAIL_REVIEW_PASS
