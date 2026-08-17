# Independent Devil's-Advocate Report — Paper 41 portable preauthority seal

Review date: 2026-08-17 UTC

Portable review target:
`papers/41-knauf-rooted-clock-non-descent/preauthority`

This report is external to the reviewed package.  It authorizes no authority
directory, registry change, Route publication, manifest mutation, Git action,
push, or mirror action.

## Frozen seal reviewed

- package `SHA256SUMS.txt`:
  `55214e6af4457ba22ea41d406524d6e94f7fe99c7274c08644822fe7505d41bb`
- `RESEARCH_LOCK.json`:
  `010b1633369fd0a0e622bdf22224145b860d139ec70cc3f5f30fe2fe5a01025a`
- portable `SOURCE_HASHES.sha256`:
  `773671adbfed36050f837d73378baa07237a338c21cf118915dc10cd0d123129`
- `ROUTE_EXPECTATION.yaml`:
  `54e0ad184799de8c12a93e64e7fcba09b0938725afec5362b621f2b9be88ff51`

Only these replacement bytes receive this verdict.

## Exact package and text boundary

Independent enumeration verified:

- 16 regular package files in total;
- 15 C-sorted, unique, self-excluding package-manifest entries;
- package file set exactly equal to the 15 entries plus the manifest itself;
- 15/15 package hashes valid;
- 14 immutable lock mappings, exactly the package files other than the
  package manifest and the self-excluding research lock;
- 14/14 immutable mappings valid;
- zero symlinks;
- zero carriage returns and trailing spaces/tabs;
- every file has a final linefeed;
- zero host-absolute path tokens for the common Unix home and temporary-root
  namespaces.

The package namespace and its sealed prose do not depend on the staging
location.

## Portable source-ID resolver audit

The source manifest contains exactly 22 typed IDs:

- 20 `repo:` IDs resolved from the repository root containing `.git`;
- `dependency:P40_DA_REPORT`;
- `dependency:P40_DA_REPORT_SIDECAR`.

The identifiers are C-sorted and unique.  Every resolved regular file matched
its declared SHA-256, giving 22/22.  The Paper-40 DA sidecar also binds the
resolved report bytes exactly.

The independent resolver enforced all of the following:

- `repo:` payloads must be nonempty canonical POSIX-relative paths;
- absolute paths, `.` components, `..` components, and backslashes are
  forbidden;
- canonical resolution must remain inside the selected repository root;
- symlink escapes and non-files are rejected;
- the dependency map must contain exactly the two declared dependency IDs;
- unknown, missing, or injected dependency IDs are rejected;
- substituted dependency bytes are rejected by their frozen SHA-256;
- malformed, duplicate, or non-C-sorted source-manifest rows are rejected.

Negative controls directly exercised absolute-path injection, parent escape,
backslash injection, symlink root escape, unknown dependency, missing
dependency, extra dependency-map entry, dependency-byte substitution,
duplicate ID, reversed order, and malformed separator.  All 11 controls were
rejected.

The typed resolver, rather than direct path-oriented `sha256sum -c`, is the
correct verification procedure for this source manifest.

## Scientific projection recheck

The portability repair did not change the Route bytes.  Independent matrix
multiplication under the frozen convention again produced:

```text
h(epsilon)=1, h(0)=1, h(1)=2,
h(01)=3, h(10)=2, h(11)=3,
h(001)=4, h(010)=3.
```

Consequently the four exact attacks remain valid:

```text
h(01) != h(10),
h(11) != h(1)^2,
lambda(h(001)) != lambda(h(010)),
lambda(h(11)) != lambda(h(1))^2.
```

The theorem boundaries remain unchanged and defensible:

- T1 rules out only the canonical right append-one action on the specified
  trailing-zero quotient;
- T2 rules out cyclic and ordinary-power descent only for the frozen rooted
  `h` clock;
- T3 rules out the literal scalar Liouville observable and one-letter scalar
  characters, not arbitrary enlarged-state cocycles;
- T4 is a trace-class diagonal state-inventory determinant on
  `Re(s)>2`, entire in its marker, with trace-log expansion only for
  `|u|<1`; it receives no primitive-return ownership;
- the repair corollary is exhaustive only over its declared finite repair
  list.

Direct-limit words, necklaces, trace-word models, and the diagonal inventory
remain distinct types.  No source, clock, operator, or quantifier changed in
the portability reseal.

## Selection, chronology, and collision boundary

The literal retrospective six-card rule still has the unique survivor
`SD-C06`.  It does not use Paper 39 ranking, Paper 40 authorization, paper
number, or a hidden nontriviality predicate.

All six cards, their results, and the exact Paper-41 witnesses were known
before the final rule.  Only the corrected final input bytes were frozen
before independent DA.  The package claims no prospective selection,
outcome-independent evidence, preregistration, discovery priority, or
selector novelty.

Primary-source chaining still finds strong prior art for the Knauf partition
function, Farey trace models, generalized chains, transfer operators, and
trace-product counts, but no located primary source states the exact frozen
four-witness conjunction.  The defensible novelty boundary remains moderate
and source-specific; source/function novelty, general partition-trace
novelty, selector novelty, and broad-mechanism novelty remain zero.  This is a
bounded search result, not proof that no collision exists.

## Strict Route verdict

The independently defended tuple remains:

```text
(
  A0_ANALYTIC_ARITHMETIC_ORIGIN,
  A1_FAIL,
  A2_FAIL,
  A3_PARTIAL_ANALYTIC_STRUCTURE,
  A4_FAIL
)
```

The overall status is `ROUTE_A_REJECTED`, and Route B remains disallowed.
The valid diagonal determinant does not earn A2 because it owns state
inventory rather than binary primitive returns; the parameter-dependent
diagonal operator does not earn A4.

## Final verdict

`DA_ACCEPT_PREAUTHORITY`

The portable replacement seal is **CLEAN for root consideration as a
preauthority research package**.  The companion SHA-256 sidecar records this
report's exact bytes outside the reviewed package.  Any source-ID, resolver,
dependency-map, mathematical, chronology, or seal change reopens the review.

