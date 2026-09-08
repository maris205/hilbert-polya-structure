# Fifth-pass checkpoint: documentation and static-link review

Date: 2026-09-08 UTC. Verdict: **PASS_DOCUMENTATION_ONLY**, after one
summary-domain omission was corrected by the coordinator and reread.
No unresolved mandatory documentation defect was found in the stated scope.
This is not a mathematical verification, formal evaluation, admission,
paper-completion certificate, repository seal, or human peer review.

## 1. Actual scope and division of work

The documentation auditor read all 21 Markdown files recursively present
under this fifth-pass directory before this report was created. The two
batch documents were read completely; the current-state comparison was
limited to its active prefix, lines 1–121, before the historical C414–C418
heading at line 122. The scoped static checker applied that same prefix
cutoff before counting content or links.

| Input group | Complete Markdown files read |
| --- | ---: |
| Fifth-pass root: README, COORDINATOR_REVIEW, SCOUT_PLAN | 3 |
| `lyness_closure/`: freeze, proof, scout, strata review | 4 |
| `lyness_sources/`: auxiliary freeze, proof, source audit, period-bound review | 4 |
| `arithmetic_frontier/`: freeze, proof, source audit, scout, helper review | 5 |
| `charp_frontier/`: freeze, proof, source audit, scout, helper review | 5 |
| [Batch README](../README.md) and [admission decisions](../ADMISSION_DECISIONS.md) | 2 |

Thus the input snapshot comprises **23 complete files and one prefix**,
or 24 document ranges. This report itself was not an input to that scan.
Links to earlier research were checked for path existence only; their
historical target contents were not added to the review scope. Historical
sections within the two expressly requested batch documents were read as
historical dispositions, not reopened as research tasks.

The auditor previously authored the four arithmetic scout documents; this
is therefore not described as a non-author mathematical review of that
lane. A separate read-only helper independently performed the scoped
link/whitespace/conflict/hash checks while the auditor compared the prose.
Neither performed new mathematical derivations, imported a research
program, reopened web sources, or ran old proof/census/build checks for
this documentation assignment.

## 2. Status, counts and theorem-boundary consistency

The [checkpoint](README.md), [coordinator adjudication](COORDINATOR_REVIEW.md),
batch entry, admission decisions and active
[current-state prefix](../../CURRENT_RESEARCH_STATE.md) consistently retain
M1/AS2/IR1 at **3/5 admitted contracts, two missing, zero new manuscripts,
PDFs or formal evaluations**. No fourth admission, C-number or A2 promotion
is asserted. Completion of the bounded fifth pass is not described as
completion of the five-paper objective.

The seven entries are LY4's old full-question continuation, three arithmetic
mechanisms and three characteristic-p mechanisms. The five deep attempts
are LY4, AF5-G, AF5-C, CF1 and CF3. AF5-D and CF2 remain shallow. The
coordinator's rational-period helper is neither an eighth entry nor a
second Lyness contract. Source-covered full statements need not be deep
attempts, so CF2's coverage is consistent with its shallow status.

The substantive summary boundaries match their frozen/proof/review texts:

- LY4 retains the complete small-period and $a=1$ strata and the exclusion
  of genuine period eight outside $a=1$. The integer exhaustion E and the
  full atlas remain unproved. The separate $N\le48$ theorem is about
  ordinary rational cycles avoiding $0,-1$, not an integer-height bound;
  its all-fiber language includes singular/reducible/nonreduced fibers
  within that domain. Special integer strata are not deleted from LY4.
- AF5-G has a period-four maximal-centralizer counterexample, not an
  all-period replacement Galois classification. AF5-C has source-dependent
  finiteness, not effective period/conductor exhaustion. AF5-D has no
  effective last-hit algorithm.
- CF1's complete all-prime/all-polynomial ordinary count and the
  every-positive-integer-power meromorphic natural boundary are retained
  as proved, but rejected as a short classical/owned reconstruction.
  CF2 is direct source coverage on its frozen local-field region.
  CF3 has only the nonreduced-return helper; its full ordinary-zeta
  classification is not passed by the helper review.

The four separate mathematical review artifacts preserve their respective
auxiliary/full scopes. Author-handoff wording about a then-pending review
is not used to override the later completed reviews and coordinator
adjudication. The present audit checks this documentary chronology, not
the correctness of those reviews' mathematical reasoning.

The three source ledgers contain 15, 33 and 31 listed formulations,
respectively, giving **79**. This was a count/cross-document check of the
ledgers, not a fresh replay of search history, verification of every
external access, or global novelty clearance. Direct opens are not
recounted as queries. The examined execution receipts consistently state
**zero fifth-pass mathematical program runs**; earlier passes' nonzero
counts remain explicitly historical. This audit itself ran no mathematics.

## 3. Finding D1 and its closed correction

Initially the fifth-pass LY4 row in `ADMISSION_DECISIONS.md` referred to
an all-fiber rational $N\le48$ bound without its no-$0,-1$ condition.
The auxiliary freeze/proof and coordinator review stated that hypothesis
explicitly. The omission was reported as a summary-scope precision defect,
not as a mathematical counterexample or proof failure.

The coordinator corrected three summary locations with `apply_patch`:
the admission table at line 22, fifth-pass README table at line 16, and
batch README opening at line 8. The auditor directly reread all three;
each now says ordinary rational cycles avoiding $0,-1$. The static helper
also rechecked exactly those three changed documents. **D1 is CLOSED.**
No proof or reviewed freeze was changed, and no mathematical rerun was
needed. The auditor did not edit these coordinator-owned documents.

## 4. Actual local-link and whitespace results

| Scoped input | Genuine local link occurrences |
| --- | ---: |
| The 21 fifth-pass Markdown inputs | 64 |
| Complete batch README | 36 |
| Complete admission decisions | 26 |
| Current-state lines 1–121 | 19 |
| Total | **145** |

All 145 occurrences resolve to existing paths, covering **68 unique local
targets**. The simple parser also recognized 59 external-link occurrences,
which were not opened or verified in this audit. It found no reference
definitions or fragment-only links within its supported syntax.

The raw regular expression yielded 146 candidates and 69 targets. Its
one apparent missing target, `z`, was inspected at
`charp_frontier/PROOF_PACKAGE.md:92`: it is part of the displayed TeX
operator equation, not a Markdown link. Removing that false positive
produces the genuine counts above; no real broken link was suppressed.

Explicit checks found **zero trailing-whitespace lines and zero conflict
markers** across all 24 ranges, including the 23 untracked full files.
`git diff --check` passed, but covered the tracked current-state change,
not these untracked inputs; it is not substituted for their explicit scan.

The post-correction check of the three index documents found 36, 26 and
16 local links respectively, all existing, with no whitespace/conflict
issue. These are overlapping targeted checks, not 78 extra unique links
or a second full audit. Current-byte receipts at that check were:

| Document | SHA-256 |
| --- | --- |
| Batch README | `38568d53ebea90d7478766fd89da1ccd2c528c68f20bca807f56ab9ecf1a5aeb` |
| Admission decisions | `05265e9d40d2ff6b7c3a4f7d2eb621ffb57f4c0c7d050b6227fb7d3757a74f6e` |
| Fifth-pass README | `857752b8c9576049a47c4af8172668f80952d1525be0645073d5f524d1b23c7d` |

Initial hashes of these index files were not captured, so this is not
presented as a pre/post byte comparison. Later addition of links to this
new report will change those hashes and requires only its own narrowly
scoped link check, not an implied mathematical revalidation.

## 5. Reviewed-input byte receipts

All seven distinct reviewed inputs match the applicable review receipts:

| Input relative to this directory | Current SHA-256 |
| --- | --- |
| `lyness_closure/PROOF_PACKAGE.md` | `f6f00908b8ade99a08806ebe37744ed89acc3fc02bb1ab92733361d3c64aab10` |
| `lyness_sources/FROZEN_AUXILIARY_SCOPE.md` | `362e46165c48e067a7f73d6d5ce2ab2a9ee3955f0dbffda90676a0bb5c1ff010` |
| `lyness_sources/PROOF_PACKAGE.md` | `828353a22d498568601fb645c8029c0d50300d3b83805f6de72592b0b2a0bc9a` |
| `arithmetic_frontier/FROZEN_CONTRACTS.md` | `c04925022c3c0887927930865513d57a9d4a8feec5fbf2c8e849430da35150ab` |
| `arithmetic_frontier/PROOF_PACKAGE.md` | `cd7d24ecaa0ec6b8b84eacde2184acc683ea47b6bb21fd64a500a3130a0456bb` |
| `charp_frontier/FROZEN_CONTRACTS.md` | `ede179b5dd93d61d901eab676d28c79a92ca7641cafb847c8060d8121ed29e2b` |
| `charp_frontier/PROOF_PACKAGE.md` | `e6a5a8f374daebc1546170b04a4941d474be0eeb535c1278a94c229b6eb240f0` |

The arithmetic review's initial proof hash, `117e4876...aadda953b`, remains
an explicitly earlier full-read snapshot. Its subsequent citation-target
correction records the current `cd7d24ec...a0456bb` hash. The later receipt,
not the initial table, is the applicable one. This audit checked receipt
consistency, not an automated reconstruction of the full historical diff.
Hashes identify bytes and confer no mathematical truth or seal.

## 6. Commands, parser limits and final boundary

All shell work used `/root/autodl-tmp/hilbert-polya-structure`. Actual
read-only commands included `rg --files ... -g '*.md'`, `wc -l`, contiguous
`sed -n` reads, targeted `rg -n`, scoped `git status --short`, `sha256sum`
on the seven explicit inputs above, and
`git diff --check -- henon_dynamics/CURRENT_RESEARCH_STATE.md`.
Truncated combined output was completed by smaller consecutive reads.
The exact current-prefix display used:

```bash
awk '/^## C414–C418 五篇完成状态（历史批次）/{exit} {print}' henon_dynamics/CURRENT_RESEARCH_STATE.md
```

The helper ran two read-only inline standard-library checks, each invoked
as `PYTHONDONTWRITEBYTECODE=1 python -` with a quoted `PY` here-document:
first all 24 input ranges, then exactly the three changed index documents.
The first body used `pathlib`, `re`, `json`, `subprocess` and
`urllib.parse`; its subprocess was scoped `git ls-files -z` solely to
distinguish tracked and untracked inputs. The second used `hashlib` for
the three current-byte receipts. Neither imported workspace code, wrote
a script/cache/output file, or executed a mathematical program.

The link recognizer used this actual expression, with code spans/fences
excluded in the main pass, URL parsing and percent-decoding for targets:

```text
!?\[[^\]\n]*\]\(\s*(?:<([^>\n]+)>|([^\s()]+))(?:\s+[\"\'][^\"\'\n]*[\"\'])?\s*\)
```

The checker is not a complete CommonMark parser or renderer. It does not
validate heading fragments, reference-style destinations, arbitrary nested
brackets/parentheses, external URL availability, mathematical formatting,
or the content of linked historical files. The TeX false positive was
handled by a targeted text read, not by editing the proof. These limitations
are part of the PASS scope.

Only this new review file was written by the documentation auditor, using
`apply_patch`. No roots, proofs, other lanes, manuscript, evaluator or Git
history were edited; no mathematical code compilation was needed for this
pure-Markdown task. No fresh fetch/push or remote-state guarantee is made.
The remaining research gaps and the 3/5 checkpoint are unchanged.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.
