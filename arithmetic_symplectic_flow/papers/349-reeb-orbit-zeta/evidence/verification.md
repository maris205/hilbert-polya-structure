# RCZ01 — verification, versions and preservation

**Audit ID:** `ANG-AUDIT-20260921-RCZ01`  
**Unchanged flow ID:** `ANG-20260921-RCF01`  
**Scientific status:**
`ORBIT ZETA ESTABLISHED; SCALAR IDENTIFICATION STOP; NATURALNESS OPEN`.

## 1. What the checks mean

Mathematical evidence consists of the explicit [paper](../paper.md),
unchanged348 owner proof and independent internal derivations. There was
NO scientific numerical experiment, finite orbit census, fitted zero datum
or claimed computer proof. Commands below check identity, formatting and
preservation; they cannot certify an infinite theorem or distributional
argument. No formal Route evaluation occurred.

The source identity and external-reference exposure are in the
[source record](source-record.md). The sole external analytic property
used is the standard classical zeta continuation, verified at official
DLMF25.2 after the own-flow definitions froze. Root's unnecessary zeros-
overview exposure is disclosed there, not hidden as a blinded analysis.

## 2. Exact frozen inputs and author surfaces

The original192-line349 card SHA-256 is
`7549da0db82ad6b260ce91dbebde484ce8d6045f92b7672f467900a5fdc9366e`.
Its final231-line version appends a mathematical disposition without
modifying that prefix. The full478-line checkpoint2 author proof hash is
`d6431109167315e5c3467c00739b00fe3f2696d255f7b15f1738a8074089d1fd`.
The final533-line paper preserves it, appending the singleton-1 terminology
clarification, explicit drift-kernel failure test and evidence navigation.

| Current author surface | EOF lines | SHA-256 |
| --- | --- | --- |
| candidate-card.md | 231 | `174a26d5abc313c61924e0869ad90ab16854343470bac7d30ee8c0a021fc4632` |
| paper.md | 533 | `dc33c69e4b2eeaa73b43551cca31e500ac58336ccebab3ba100fbb77a01b9c4c` |
| README.md | 51 | `b568d5858e1b766c9947181dbb0c32941af248b9c9c41ea3799d769910acff61` |
| claim-ledger.md | 56 | `e5d8d71af4096805e3b848c9b249391c56898ffe2f3e9d33e9ab670e1f322ecc` |

The card's original OPEN label and the paper's original pending-review
footer are historical frozen inputs, superseded explicitly by their
appended current status. They are not contradictory current outcomes.
The fixed scientific surfaces are not rewritten to hide earlier wording.

## 3. Independent work and actual access boundaries

The ARS scope checkpoint personally read only the original192-line card,
found it sufficiently specified and granted audit ENTRY, not mathematics.
Its149-line report hash is
`6e9572291e27a07a713cfdde4259a662076782b2ed9fe0bbad23a48384e88d72`.

MAIN's scalar derivation and the controls' derivations were assigned to
disjoint files and started from that frozen card without reading root's
new paper or each other's outputs. They retain shared earlier348 history
and the inherited model. This is not blind, cross-model or external review.
Root derived the author proof separately, then compared actual arguments.
Any later messages/exposure are recorded in the individual reports.

Root read the complete397-line control report through EOF, including its
explicit OPTIONAL NONCORE continuation supplement. Its frozen hash is
`8400d1b41466cf12bdc2cf013b110caf8f5c0348bc8960819ba6eafa93254e48`.
That extra calculation was already written when root requested scope
closure; it is not needed for MAIN or the core control verdict, and it
does not authorize further research. No auxiliary349 agent was spawned
by either independent derivation task.

Checkpoint2 reviews the original478-line author proof and192-line card,
not peer derivations. Checkpoint3 checks the final author-surface deltas,
not peer reports. Their final receipts and hashes are appended below after
completion and full root readback. Internal review is NOT_CALIBRATED;
human verification and externally independent errors are not attested.

## 4. Preservation of the unchanged flow and repository guidance

All11 files of348 were hashed before this work and checked unchanged.
The manifest encoding is sorted relative path + TAB + file SHA-256 + LF,
UTF-8, with paths relative to `papers/348-reeb-contact-refinement`.
The manifest SHA-256 is
`5255ca400be05283270cc95553d041004469a866853a26e260f25a3f0d9cc0d6`.
In particular its full219-line card and603-line proof remain the exact
dependencies locked in349. No old source or negative result was rewritten.

The only root overview edits prepend349 and demote the previous348 state
heading. Removing that new block and restoring ONLY the former heading
reconstructs the exact original files:

- readme.md: `a3c520153f7f334e60ca1f7b8cd5e242439d10ff77884469e7a2681408d6c9a9`.
- papers/README.md: `c281a47e8139c330d95abfda53ba32a6bc5d5ecd2c9d1e6288d9c62f82ed0345`.

The following read-only guidance/source anchors also match their opening
hashes. Existing user/worktree modifications are preserved, not reset.

| Path from stream root | Unchanged SHA-256 |
| --- | --- |
| AGENTS.md | `86b8d64302321ae0b1b4adc7ac8fc513e5c9c6bc8b1292dab11841188302438d` |
| plan.md | `9fa4aade2ca5e71077a70b3aa78b82378795d25fbb1007158f0d21297c1431a0` |
| docs/prior_work/README.md | `d2287008387388ac5968288ea4093d630ff0a913f6013547e43e769389a73cfd` |
| papers/paper-template.md | `ec6caabcd6acdda7d5e1c628b117b7084d266dcb4b0326bec1d25d4a1dfd5a3b` |

## 5. Reproducible read-only checks

Working directory is the arithmetic_symplectic_flow stream root. The
following Node command reproduces the byte locks and full package file
manifest without reading unrelated history or writing any file:

```bash
node <<'JS'
const fs=require('fs'), c=require('crypto');
const h=b=>c.createHash('sha256').update(b).digest('hex');
const walk=d=>fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>
  e.isDirectory()?walk(d+'/'+e.name):[d+'/'+e.name]);
const base='papers/349-reeb-orbit-zeta';
for(const [f,n,expected] of [
  ['candidate-card.md',192,'7549da0db82ad6b260ce91dbebde484ce8d6045f92b7672f467900a5fdc9366e'],
  ['paper.md',478,'d6431109167315e5c3467c00739b00fe3f2696d255f7b15f1738a8074089d1fd']
]) {
  const prefix=fs.readFileSync(base+'/'+f,'utf8').split('\n').slice(0,n).join('\n')+'\n';
  if(h(prefix)!==expected) throw Error('changed prefix: '+f);
  console.log('LOCK OK',f,n,h(prefix));
}
const old='papers/348-reeb-contact-refinement';
const manifest=walk(old).sort().map(f=>
  f.slice(old.length+1)+'\t'+h(fs.readFileSync(f))+'\n').join('');
if(h(manifest)!=='5255ca400be05283270cc95553d041004469a866853a26e260f25a3f0d9cc0d6')
  throw Error('changed348 bundle');
console.log('348 BUNDLE OK',h(manifest));
for(const f of walk(base).sort()) {
  const b=fs.readFileSync(f);
  console.log(f,b.toString().split('\n').length-1,h(b));
}
JS
```

Additional mechanical checks resolve all new package relative links and
any explicit heading anchors, balance fenced code blocks, compare Markdown
table widths, require EOF newlines and consistent audit/flow/status in
the four author surfaces. New overview blocks are checked separately;
unchanged historical text is covered by reconstruction hashes. The first
six-file pass checked17 local links and43 table lines with zero errors;
final expanded checks are reported below. No successful check is called
a theorem proof or formal Route gate.

Read-only Git commands were `git branch --show-current` and
`git status --short -- readme.md papers/README.md papers/349-reeb-orbit-zeta`.
They showed branch main, the two modified overview files and the untracked
new349 directory. No branch/reference creation, staging, commit, checkout,
push or external publication was performed. Output artifacts are Markdown
only; no LaTeX/PDF or publication artifact was generated.

EOF — verification base; final reviewer and mechanical delta receipts follow.

## 6. Completed derivation and analysis-review receipts

Root read the complete286-line independent scalar report through EOF.
Its frozen hash is
`f3a38bce008d433d1b0697ef047945e3ec8cfcccc52d67626a42299e71370e71`.
It derives the kernel, local/global pushforward, sharp initial domain,
non-trace-class status, product and mismatch independently of the author
manuscript. Its global continuation is explicitly conditional on the
classical property, not an invented personal source verification. The
parent's later agreement/DLMF-check message is disclosed in that report.

Root also read the complete351-line checkpoint2 report through EOF:
`6020fcc22e23b4872b677320af0eca96f5fcc42bdb20aa2fdb93d362734218b1`.
The verdict is PASS for bounded J1/J2/J3, with one minor source-basin
terminology correction. Its exact finding is retained: singleton(1) is
fixed, not terminal, even though both real-u components have no physical
period. The paper's final append resolves this without changing the frozen
478-line input or any analytic formula. The reviewer independently checked
official DLMF25.2; the unused general zero-product formula displayed on
that same page is disclosed, with no additional zeros-page/data use.

Checkpoint3 received only the final author deltas, full README/claim ledger
and the bounded new overview heads. It did not read peer reports or this
verification file. The initially reviewed51-line README hash was
`76bb1153533031e1080396c7d2a91fcc606dde5bcab21298cfa5e984052a02e2`.
Its line33 was then clarified from "no ... flat trace" to the explicit
"zero flat trace" for UNIT-HOLONOMY. That single-line clarification gives
the current hash in Section2; it is not a scientific result change or an
attempt to erase the original review input. The final delta receipt follows.

## 7. Full mechanical pass and scoped follow-up

The expanded read-only check at the ten-file package stage returned:

```text
files: 10
relative links checked, including both new overview heads: 36
Markdown table lines checked: 68
Markdown-only artifacts: true
frozen prefix checks: candidate192 / author478 / analysis-review351 PASS
348 bundle: 5255ca400be05283270cc95553d041004469a866853a26e260f25a3f0d9cc0d6
both historical overviews reconstructed: PASS
four author identity/status surfaces: PASS
errors: []
```

This pass preceded only the final review append, the explicit README
zero-trace wording and this receipt's additions. Subsequent checks are
limited to those changed inputs and the exact referenced surface hashes;
unchanged proofs and preserved old packages are not repeatedly re-audited.
The source-record78-line hash at that pass was
`8a875bff9a1c316c9c26904668009193c8bc6e3b67141d82dc1b0e0b7660b209`.

EOF — full checks and analysis integration recorded; final delta receipt pending.

## 8. Final checkpoint and handoff closure

Root read the complete new checkpoint3 append, lines352–470, retaining the
already read351-line analysis report. Its final470-line SHA-256 is
`c233f84b21842c6a77b6e54fdf53d1524f6bf8342ed130e088b4d3605801cb23`.
The original351-line prefix still has the Section6 hash. Checkpoint3 is
PASS: the actual M1 clarification is closed, the local mollifier argument
is valid at its specified scope, and final claims/naturalness/Route
boundaries agree. The final README line33 clarification was independently
read as a narrow delta and its current hash verified before review freeze.

All three ARS checkpoints have completed at their own scope. Independent
MAIN-scalar and control reports were read through their full EOFs and
compared with root's proofs. There is no unresolved mathematical-review
finding in this internal audit; this does NOT close strong naturalness,
establish formal correctness certification or supply external peer review.

The final mechanical delta check covers README, the completed review and
this receipt: relative links, tables, fenced blocks, whitespace and EOF;
it also compares the four final author hashes and the470/351 review locks.
No mathematical input changed after the checked author proof supplement.
No more scientific calculations, global package reruns or old-stream edits
are required by the changed inputs. Final output remains ten Markdown files
plus the two linked overview updates.

Handoff: study is RCZ01 on the SAME RCF01 flow. Ordinary orbit zeta and
actual scalar flat-determinant function are established; scalar equality
is false; strong naturalness remains OPEN. Same-object ledger intact.
Only owner-level T3 was evaluated; classical A0/A1/A2 NOT APPLICABLE;
formal UNASSIGNED; B NOT INVOKED. Portfolio **advance** those scoped
analytic objects and **stop** scalar identification. A different analytic
owner or naturalness study is a separate continuation choice, not performed.

EOF — completed internal audit and proportionate verification; no external release.
