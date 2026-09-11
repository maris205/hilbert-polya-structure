# P212 physical Round1 — SOURCE-only fixed-copy preparation

Status: SOURCE_ONLY / NOT_EXECUTED / FINAL_A_AND_A_PDF_ADOPTED / LIFECYCLE_DELTA_PROPOSED.
This package prepares one later Round1 freeze. It performs no copy, live
edit, build, scientific run, host observation, Git action or nested-agent
task. The argument guard is not a grant. Only this preparation directory
is written. Root has now accepted final A and adopted its PDF; the exact
three-file lifecycle proposal remains here for root's documentary reception
and application, not an extra manuscript-review or user-approval stage.

## Exact reuse and input boundary

Reuse the accepted P212 [Round0 recipe and plan](../p212_round0_freeze_source01/PLAN.md),
not a P213 layout or new observer. The actual
[Round0 receipt](../p212_round0_freeze_binding01/ROUND0_RECEPTION.md)
accepts operation 82d984 and root physical reception 2622bc. In this task,
the current frozen directory was also listed with hidden files included:
exactly its 25 payload names plus SHA256SUMS, no additional file. All 25
directory-relative hashes passed actual 2f3935. Its manifest hash remains
`c8cc4f28b808888060b57dd121ff52a7e06b98452d89adfeec32ef3468468234`.
This read-only integrity check is not another physical freeze.

[FILES.tsv](FILES.tsv) keeps all 25 destination roles and row order.
Only row 25 changes its source from the Round0 binding's FREEZE_SCOPE.md
to the separately prepared Round1 binding's FREEZE_SCOPE.md. The first
24 source spellings are unchanged; their accepted contents may differ at
the new milestone. [RECIPE.diff](RECIPE.diff) changes only the preparation,
binding and frozen destination paths and the final pending-reception
marker. [MAPPING.diff](MAPPING.diff) records the one mapping change.

The fixed payload inventory is:

- Eight TeX/Bib sources: main.tex, math_commands.tex, references.bib,
  sections/01_setup.tex, 02_returns.tex, 03_period_set.tex, 04_census.tex
  and 05_scope.tex.
- Six framing/proof documents: PROOF_PACKAGE.md, PAPER_PLAN.md,
  SOURCE_AUDIT.md, CLAIMS_EVIDENCE.md, NARRATIVE_REPORT.md and README.md.
- Five verifier/interface/output files: verify.py, PARAMETERS.json,
  OUTPUT_SCHEMA.md, OUTPUT_PLAN.md and the actual author CANONICAL.json.
- Four unchanged author receipts with the same original source spellings
  and evidence/ destinations as Round0.
- The root-adopted current main.pdf and root-authored FREEZE_SCOPE.md.

Total: 25 payload files plus a newly generated directory-relative nonself
SHA256SUMS. Only sections/ and evidence/ children are created. Do not copy
the whole live, Round0, A-review or QA tree; do not transplant A's verifier
or canonical into author roles. All old freezes, source-era seals, failed
evidence and original receipt bytes remain untouched.

## Actual changed dependencies and required documentary delta

The available [final same-A delta](../../reviews/p212_a/DELTA.md) accepts
only these two manuscript-source corrections:

| File | Received repaired SHA-256 | Change |
| --- | --- | --- |
| sections/01_setup.tex | 5f680c50155ce878b6b32e287af53ed962d2adf940c940393d62cc598e2929ad | Holroyd Eulerian-tour locator: Theorem 3.8 becomes Lemma 4.9 |
| references.bib | 45359fea915fdabe3c0fae561162b1da23188e2ef50264bf3698b55e58b6c895 | Add Lemma 4.9 to the note; retain Theorem 3.8 and Corollary 4.10 |

Root already received the source-stage correction at
[SOURCE_RECEPTION.md](../p212_a_source_root01/SOURCE_RECEPTION.md).
The final A report/delta/current finding census and the subsequent
[root final-A acceptance](../p212_a_source_root01/FINAL_A_ACCEPTANCE.md)
have been read. Actual e65ca8 receives that final review and exact delta;
this preparation does not repeat or issue the review. The final review uses FINDINGS_FINAL.json for its current
census; immutable initial FINDINGS.json and its source seal remain intact.

The new A PDF is already accepted as an artifact at
[the A artifact root receipt](../p212_a_build_artifact_root01/RECEPTION.md):
191,507 bytes, six pages, SHA-256
`096adcb6b24fd6ae1853cf8fecff4cd0acc1a6d4b9aab0e9470bdb3e66997c31`.
At this preparation's first comparison cutoff, live main.pdf still equalled
the historical Round0 PDF. Subsequently root's actual
[PDF adoption 4318bb](../p212_a_source_root01/PDF_ADOPTION_NATIVE.json)
preserved and raw-compared that original under MAIN_BEFORE_A.pdf, then
adopted and raw-compared the accepted new A PDF at live main.pdf. This
actual record was read; the earlier comparison is not rewritten as a
post-adoption observation. The old PDF and evidence remain available.

The read current README, CLAIMS_EVIDENCE and NARRATIVE_REPORT still equal
their Round0 originals. This package now preserves those exact texts under
originals/ and gives complete proposed/ replacements, with actual
[LIFECYCLE.diff](LIFECYCLE.diff). Their specific documentary changes are:

1. README: replace the opening Round0/A-pending current milestone; identify
   accepted physical Round0 and accepted A/exact delta, current adopted A
   PDF and the actual adoption receipt. Retain the old initial-build/PDF
   facts as historical facts, not the identity of current main.pdf. Record
   A's actual process and preserve the existing contributor exclusions;
   do not invent B, physical Round1 or terminal acceptance.
2. CLAIMS_EVIDENCE: update the opening and closing Round0-pending/no-A
   statements and distinguish accepted Review A from still-pending B and
   terminal gates. Keep every theorem row, author count and 5/6/5 limit.
3. NARRATIVE_REPORT: replace its final next-Round0/no-A current-status
   paragraph with the received A/delta/current-PDF milestone and pending
   Round1/B/terminal obligations. Keep its mathematical narrative intact.

SOURCE_AUDIT, PAPER_PLAN and OUTPUT_PLAN explicitly describe historical
source-preparation phases; they need no generic rewrite to present tense.
SOURCE_AUDIT's Holroyd row already includes both Theorem 3.8 and Lemma 4.9.
PROOF_PACKAGE, verifier, parameters, schema, author canonical, the six
other TeX sources and four original author receipts have no requested
change. Thus the expected Round0-to-Round1 delta is 2 repaired sources,
main.pdf, 3 lifecycle documents and FREEZE_SCOPE.md: seven changed payload
roles, with the other 18 full byte pairs unchanged. This is an exact
expected-delta boundary, not a claim that seven future writes occurred.
If the accepted actual delta differs, stop and receive that difference.
Root must compare the preserved original texts to live before applying
these exact three replacements, then compare each live result to proposed/
and record that documentary acceptance. No live file was changed here.

## Root's final freeze note and external binding

The final note is deliberately NOT manufactured in this package before
root's remaining lifecycle application. Root must prepare the actual
`docs/papers211_215_sequence/qa/p212_round1_binding01/FREEZE_SCOPE.md`
after its already completed final-A/delta receipt and live PDF adoption,
and after narrow lifecycle acceptance. It is the 25th copied payload, not a post-copy assertion of
success. It must state the following concrete facts with their actual
receipt paths/identities, rather than fill placeholder future hashes:

- the accepted physical Round0 and immutable old 25-input identity;
- final A report/delta/current-census provenance and root reception;
- exactly the two source corrections above, unchanged author science
  dependencies and the actual adopted A PDF/content/page-view linkage;
- the exact three-document lifecycle acceptance and its preserved old
  originals, without retroactively rewriting any frozen text;
- this complete 25-row source/destination map and original link bases;
- the remaining distinct nonauthor B/delta, Round2, two actual terminal
  builds, final views and full paper/batch gates; OWNER_AMBER/HOLD_EXTERNAL.

The four evidence receipts retain their exact original bytes. Their
original paths are specified by FILES.tsv, and links in every copied
source document are interpreted relative to that original source path,
not silently rebased to a deeper frozen directory. The final scope must
make this explicit. Linked A/raw/runtime/build archives stay at their
sealed workspace origins; the freeze is not a standalone clone of QA.
The root-authored final scope should use correct frozen-destination links
or explicit workspace-relative textual paths for its own references.

After those actions, root independently prepares the binding's
`INPUTS.sha256` with workspace-relative paths for all 25 actual source
files plus FILES.tsv and FREEZE.proposed.sh.txt: 27 exact inputs. Root's
separate grant must bind the whole external manifest and exact request;
the script's internal hash check does not authenticate an unreceived list.
Do not reuse the Round0 input-manifest hash or insert placeholder/future
lifecycle, live-PDF, scope, output-manifest or native-result hashes here.
[SOURCE_INPUTS.sha256](SOURCE_INPUTS.sha256) pins only the 20 already
existing source/reference documents used for THIS preparation; it is not
the future operation's INPUTS.sha256 and cannot authorize the freeze.

## Proposed request, operation and physical acceptance

Only after root source/delta/binding acceptance and a separate one-copy
grant, use this proposed request, with shell /bin/bash, login=false,
tty=false and cwd /root/autodl-tmp/symbolic_dynamics:

```text
/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /bin/bash --noprofile --norc /root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p212_round1_preparation01/FREEZE.proposed.sh.txt --execute-under-separate-root-grant
```

The guard, input checks, exclusive directory creation, fixed-row ordinary
copy/cmp loop, generated 25-row nonself SHA256SUMS and before/after input
checks are unchanged from the accepted Round0 recipe. Failure stops and
preserves its partial destination; no cleanup, overwrite, automatic retry,
format rebuild, scientific call or return-value invention is permitted.
This preparation has not queried the future binding, frozen_round1,
parent capacity or output-path absence.

Root must receive the actual complete command/result, separately compare
all 25 mapped source/destination byte pairs, verify the exact 26-file tree
membership and reproduce/check the complete nonself directory manifest.
Only a later root physical receipt establishes Round1. The pre-copy
FREEZE_SCOPE/lifecycle wording must not be edited retroactively afterward.
B starts from that received physical Round1, not this preparation package.
Ordinary filesystem trust is unchanged: no atomicity/fsync/chmod protection
or hostile-writer/ancestor attestation is claimed.

## Checks actually done here

The project skill/workflow, artifact contract, complete accepted Round0
recipe/map/receipt/scope, current lifecycle texts, relevant A root receipts
and final A report/delta/current census were read as text. No mathematical
verifier or operation recipe was imported, parsed by its runtime or run.
An actual 24-pair raw comparison against Round0 found only the two already
repaired citation sources different; the other 22 pairs, including the
historical live PDF and current lifecycle texts, were equal at that cutoff.
Expected cmp exit 1 on the two changed sources is not a failed freeze.
[DOCUMENTARY_NATIVE.json](DOCUMENTARY_NATIVE.json) retains those exact
requests/results, the actual prior membership and reference hashes.
The leading-index display was partly truncated; no missing historical
tail is used as proof or an accepted gate. No nested agents were created.
