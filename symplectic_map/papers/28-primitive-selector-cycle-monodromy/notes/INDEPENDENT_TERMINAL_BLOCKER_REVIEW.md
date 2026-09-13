# Independent review of the Paper 28 terminal build-profile blocker

## Verdict and review identity

Review verdict: **PASS**  
Finding census: `Blocker=0; Major=0; Minor=0; Ambiguity=0`  
Reviewer role: `fresh-independent-batch07-p28-terminal-blocker-reviewer`  
Controlling event: `B07-E0215-P28-TERMINAL-BLOCKER-REVIEW-AUTHORIZATION`  
Controlling sequence: 212  
Consumed marker: `BATCH07_PAPER28_TERMINAL_BLOCKER_REVIEW_AUTHORIZED`  
Candidate: `primitive_selector_cycle_monodromy_v1`  
Paper number: 28, consumed  
Project: `papers/28-primitive-selector-cycle-monodromy`  
Reviewed status: `TERMINAL_BUILD_PROFILE_FIREWALL_BLOCKED`  
Reviewed effect: `LOCAL_EVIDENCE_ONLY_NO_RELEASE`

I am a wholly fresh reviewer with no earlier Batch 07 author or reviewer role.
I did not participate in Paper 27; Paper 28 recovery, candidate, design, lock,
scope, plan, bibliography, publication-lock, source, build-profile, or
terminal-blocker work; or any prior terminal decision.  I independently
reviewed the terminal record from the authority and immutable bytes opened by
E0215.  The result is an unconditional all-zero PASS.

This review validates a terminal local-evidence-only disposition.  It is not
a build-profile PASS, source mutation, build authorization, PDF result,
release decision, retry token, replacement-candidate gate, or external-effect
authorization.  A later append-only ledger event must consume this review
before the terminal status becomes the active Paper 28 disposition.

## Restricted procedure and sole-write compliance

I read `BATCH_07_STATUS.md` and exactly the twelve other paths in E0215's
`opening_paths`.  I did not list a directory, use a glob or wildcard, recurse
or search outside those exact files, inspect a future or absent path, probe a
build parent or root, read system TeX content, run TeX, BibTeX, kpathsea, a PDF
tool, a scientific program, or a network operation, create a cache, or cause
an external effect.  Read-only byte, stat, hash, UTF-8, LF, marker, fixed-token,
and ledger-prefix checks used only the authorized files and administrative
stdin execution with bytecode disabled.

I did not test whether this review path existed before creation.  After all
review predicates were zero, I created only this exact E0215-authorized path.
I did not modify the ledger, terminal record, source trio, profile, plan,
charter, locks, prior reviews, or any other file.

## Authorization, parent chain, and physical identities

E0215 is the unique active review authorization.  Its immediate ledger parent
is exactly 751,131 bytes with SHA-256
`18c63e2debda36b960987a2174c86cb8d9de42380f3e41b1cacfdc231ac444c0`.
Independent prefix hashing of the live append-only ledger reproduces that
value exactly.  The complete E0215-opening ledger is 755,464 bytes and 12,092
LF with SHA-256
`990ca28560098bd4e6581d40d88c465890fe1fd374940b357c9f733e3bc2973f`.
It is regular mode 0644, link count one, strict UTF-8 and LF-only, with no CR
or NUL byte and exactly one terminal LF.  The controlling authorization marker
occurs exactly once as a complete line.

The parent chain around the terminal artifact is also exact.  E0213's
743,090-byte prefix hashes to
`4cbd21c6400a8ad71e2ce6784084ad0bcd74842f9369b8627e5a99aafed80b3c`,
and E0214's 747,307-byte prefix hashes to
`cb60b58518daeeba5a96ce126a43b5638b1a193c72b8f47007411ab72475a943`.
Thus the terminal record correctly binds the parent of its authorizing E0213,
E0214 correctly records the created artifact, and E0215 correctly consumes
the E0214 author-stop marker.  No ledger byte was rewritten or backfilled.

E0215 freezes the same 75-row source/control manifest before and after review
authorization: 11,150 framing bytes, 75 LF, SHA-256
`1783e5633b885260164c5f016c02d51f6f574a0226c032fa5613646b00842a68`,
using
`path<TAB>bytes<TAB>LF<TAB>644<TAB>1<TAB>sha256<LF>`.
The ledger is self-excluded and every build subtree remains excluded.

Every authorized non-ledger input was independently read and rehashed.  Each
is a regular, non-symlink mode-0644 file with link count one, strict UTF-8,
zero CR, zero NUL, and exactly one terminal LF:

| Path | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `BATCH_07_CHARTER_REVIEW.md` | 20209 | 364 | `4ced8ab1e1b48d89ec088be40206bf3bbff3e23c77471c45672442883b322f73` |
| `papers/28-primitive-selector-cycle-monodromy/PAPER_PLAN.md` | 49891 | 1063 | `ce5c2f61ab3ee9e5bdd12a53e0cfdc938a5d417b094ac8a3a335e1d4bc2d01a3` |
| `papers/28-primitive-selector-cycle-monodromy/notes/BUILD_PROFILE.md` | 62808 | 1033 | `6f4c2b81e0d2372776724429150d0d1a86726bd5784d61a4259f6516063c5f36` |
| `papers/28-primitive-selector-cycle-monodromy/notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md` | 30918 | 465 | `1ea0dc0c4cbdc98372fafa4bdc41b489df7f09ca9e8f539b71f8ed1d1bf1644b` |
| `papers/28-primitive-selector-cycle-monodromy/notes/INDEPENDENT_SOURCE_REVIEW.md` | 25100 | 531 | `bfa264202de33ae63c0910eeafe4c90968f85515179456ab44b10fcf91dfe750` |
| `papers/28-primitive-selector-cycle-monodromy/notes/PUBLICATION_LOCK.md` | 37163 | 578 | `a838a1315d82b650af402d90e3207a65f7ccd172d24b423a99e76f148271b005` |
| `papers/28-primitive-selector-cycle-monodromy/notes/PUBLICATION_SCOPE.md` | 19578 | 359 | `e8e34ac6c99cc4c27c81e0211002fe7ceecba47a5bcbd57168944b6437094a1a` |
| `papers/28-primitive-selector-cycle-monodromy/notes/SOURCE_LOCK.md` | 18591 | 593 | `6a45cd18cafe7c6f3b35aa30ffc39242f64e7a43e25476fc6bbad76260be009b` |
| `papers/28-primitive-selector-cycle-monodromy/notes/TERMINAL_BLOCKER.md` | 18046 | 333 | `90359406c4ddeb6d0a0fb3338e318bbf69c83f21bbd0c64399158ddc3056adfa` |
| `papers/28-primitive-selector-cycle-monodromy/paper/main.tex` | 73733 | 1605 | `bdc7a1edc06b3f8cfc75c6b47a8c24180883d24eef878c70d857588d19f1762e` |
| `papers/28-primitive-selector-cycle-monodromy/paper/math_commands.tex` | 444 | 14 | `16b1e55f52f21b63811a0d34eb64eba955533334f8e5f58005841d6da0a85ce5` |
| `papers/28-primitive-selector-cycle-monodromy/paper/references.bib` | 6104 | 204 | `e6a6bdb24a7db3a75b481c8363aa7733cb3dd4c1e8a121d9d9526eb83228882e` |

The terminal record's identity is exactly the one frozen at E0214 and E0215.
Its marker `BATCH07_PAPER28_TERMINAL_BLOCKER_FROZEN` occurs once as a complete
line and is the exact final line.  The required terminal status and effect are
both present and unqualified.

## Independent reconstruction of the R2 failure

E0212 records `FAIL_WRITE_NOTHING` with the fixed census

```text
Blocker=1; Major=5; Minor=0; Ambiguity=1
```

and records that the build-profile reviewer created no PASS artifact under
the PASS-only rule.  The terminal record preserves that census without
reclassification or attempted repair.  Direct review of the frozen revised
profile independently confirms the substance of every finding.

### Blocker — first dependency content read is not exactly predeclared

Profile lines 363--380 explicitly propose a sole “prefix-limited read
exception.”  Discovery TeX and BibTeX would be allowed to open not-yet-known
system files through kpathsea under four directory prefixes:

```text
/usr/share/texlive/texmf-dist/
/usr/share/texmf/
/var/lib/texmf/
/etc/texmf/
```

The commands D020, D030, D040, and D050 run before D061 extracts the exact
external path union from D012 and the D024/D044/D054 recorder snapshots, and
before D062 seals that union.  The later discovery STOP expressly occurs only
after those reads.  A lexical directory prefix denotes an open-ended set, not
a finite exact-file allowlist.  Non-release purpose, administrative no-read
language, recorder capture, and a later STOP cannot authorize the already
completed first content read retroactively.

The Batch 07 firewall is permanent: future paths must be exact and authorized
before observation or opening.  Therefore the discovery stage cannot lawfully
start, the transitive dependency universe cannot be established by this
profile, and neither certified root can be opened.  This is exactly the R2
Blocker and is independently sufficient to deny build-profile PASS.

### The five independent Major findings

1. **Bootstrap and seal lifecycle.**  BOOT-000 and BOOT-001 precede the
   evidence root but the universal capsule has no literal pre-root receipt
   destination for their console and status bytes.  The profile instead asks
   a later ledger event to serve as their sole durable receipt.  Its stage
   seal simultaneously must enumerate all stage-local evidence, is itself a
   stage-local artifact, and is followed by its own command status.  The
   required complete seal therefore depends on evidence not available when
   that seal is created.
2. **Symlink target bytes.**  The binding stage authorizes no-follow `lstat`
   and says that operation supplies literal link bytes.  `lstat` supplies
   metadata, not a symlink's target string.  The profile freezes neither a
   `readlink`/`os.readlink` operation nor authority for it, and in fact lists
   `readlink` among forbidden executables.  The hop-by-hop target chain is not
   executable as written.
3. **Validator acceptance set.**  The profile defers the exact validator stdin
   and its hash to a future build authorization.  Its PDF parser description
   does not freeze a complete token/value grammar and state transition set.
   Distinct future implementations can therefore have distinct acceptance
   sets while claiming to implement the prose.
4. **Tool-version and Python inputs.**  Frozen version labels do not include
   literal version-command arguments and the complete expected stdout/stderr
   bytes.  The claimed restricted Python import set does not bind all possible
   runtime module-file inputs or prove them embedded.  Execution would still
   infer unbound tool inputs.
5. **Contradictory fixed stage order.**  The exhaustive creation order at
   profile lines 235--264 places `cross-root`/C000 before `final`/F000.  The
   later mandatory lifecycle at lines 935--942 requires F000--F002 to finish
   before C000.  Both are presented as fixed; no literal run can satisfy both.

### The independent Ambiguity

The profile permits one root-prefix replacement for `main.fls`, yet also
requires root evidence, time-indexed snapshots, and semantic/evidence censuses
to agree exactly.  It does not state whether all three root-bearing `.fls`
snapshots are compared raw or after that normalization.  Raw equality is
root-dependent; applying normalization beyond the specifically described
comparison expands the unstated scope.  The acceptance rule is ambiguous.

The terminal record reproduces all seven findings faithfully.  It also keeps
the R2 otherwise-passing static census in its proper role: those source and
proposed acceptance properties do not cure any conjunctive finding and do not
show that a compiler, dependency universe, build root, page count, or PDF ever
existed.

## Passed local evidence is not executable authority

The preserved records support exactly the distinction made by the terminal
document:

- the source lock and paper plan freeze the family-wise theorem, proof spine,
  limits, anonymous article structure, and proof-only page-mass plan;
- the publication scope and publication lock freeze the qualified claim
  ceiling, bounded-search limitations, eighteen-key bibliography, exact
  three-source architecture, anonymity rules, three tables, no figures or
  appendix/supplement, and inclusive 22--30 intended content-page gate;
- the independent publication-lock review is an all-zero `NO_COLLISION` PASS
  under its frozen cutoff and explicitly grants no compiler, build, PDF,
  release, upload, submission, or message authority; and
- the independent source review is an all-zero R2 PASS on the corrected source
  trio and explicitly grants no executable binding, compilation, build root,
  PDF, finalization, release, upload, submission, or message authority.

The live bytes match every frozen identity.  As limited static corroboration,
`main.tex` contains eight sections, thirty-two subsections, exactly three
table environments, zero figure environments, seventeen package declarations,
one `\clearpage`, and anonymous author metadata; `math_commands.tex` contains
fourteen macro definitions; and the bibliography contains eighteen entries.
The corrected scalar `\sigma_0` and phase-matrix `C_0` remain type-distinct.

None of those observations is a compilation.  The 26.5-page plan and credible
source mass are not a physical page count; portability and deterministic-build
intent are not a build; and static source review is not a reproducibility or
release result.  The independently failed profile gate remains controlling.

## Revision exhaustion and terminal necessity

The ledger gives the build-profile lifecycle exactly one bounded revision.
R1 failed at E0208; E0209 authorized that one revision; E0210 froze the revised
profile; E0211 opened a wholly fresh R2 review; and E0212 recorded the all-
conjunctive failure.  That sole revision is consumed.  There is no authority
for a second revision, alternate profile, dependency-discovery exception,
builder substitution, guessed dependency list, receipt backfill, compiler
experiment, workaround, or candidate replacement.

The charter states that once a paper number is consumed, a terminal blocker
closes the numbered project and forbids retry, replacement, alternate project,
or relabeling under the same number.  Paper 28 is consumed.  The profile cannot
enter its first dependency-reading step without violating the permanent
firewall, and the remaining five Majors and one Ambiguity independently defeat
literal execution.  With the sole revision exhausted, terminalization is not
premature and does not suppress an authorized repair path; no such path
exists.

The exact necessary disposition is therefore
`TERMINAL_BUILD_PROFILE_FIREWALL_BLOCKED`.  Its exact effect is
`LOCAL_EVIDENCE_ONLY_NO_RELEASE`.  This preserves the immutable theorem,
publication, and source evidence while denying every unpassed downstream
claim and action.

## Negative authority audit

The terminal record contains no hidden or conditional authority to:

- reopen the failed profile, use an alternate or standard profile, revise it
  again, weaken the firewall, or learn exact dependency paths after a first
  unauthorized read;
- probe or create a build parent, evidence root, discovery root, certified
  root, cache, auxiliary file, PDF, candidate copy, or release object;
- run TeX, BibTeX, kpathsea discovery, a PDF inspector, a compiler, scientific
  code, package installation, or a network operation;
- relabel or replace Paper 28, reuse its consumed number, open an alternate
  project, or convert the terminal record into a fallback gate; or
- finalize, release, copy for release, host, upload, submit, externally
  message, identify, or otherwise transmit any artifact.

The record makes no claim of a compiled, measured, reproducible,
submission-ready, finalized, released, uploaded, submitted, hosted, accepted,
or published PDF.  Its statement that only explicit user authority could
alter the batch's external-effect ceiling in general is not a retry token: the
same sentence denies retrospective PASS or authority, and the terminal record
separately closes the consumed Paper 28 project.  Future exact read authority
for local auditing likewise does not imply mutation, compilation, reuse, or
release authority.

The absence of a build-profile PASS artifact is established only by E0212's
`FAIL_WRITE_NOTHING` report and the PASS-only creation rule.  Neither the
terminal author nor this reviewer tested an absent or future pathname to infer
that fact.

## All-zero finding census

| Review predicate | Findings |
|---|---:|
| E0215 authority, freshness, parent prefix, role, and sole-write boundary | 0 |
| Thirteen authorized opening-path identities and encoding/line-ending rules | 0 |
| Terminal-record identity, marker multiplicity, and exact final line | 0 |
| E0213--E0215 append-only parent chain and manifest binding | 0 |
| Fixed R2 `1 / 5 / 0 / 1` census fidelity | 0 |
| Permanent exact-predeclared-path firewall conflict | 0 |
| Bootstrap/seal lifecycle finding fidelity | 0 |
| Symlink-target operation and authority finding fidelity | 0 |
| Validator acceptance-set finding fidelity | 0 |
| Tool-version and Python-input finding fidelity | 0 |
| Contradictory stage-order finding fidelity | 0 |
| Raw-versus-normalized recorder ambiguity fidelity | 0 |
| Exactly one consumed build-profile revision | 0 |
| Passed local evidence versus failed executable authority distinction | 0 |
| Absence of build, PDF, page-count, reproducibility, or release claims | 0 |
| Terminal necessity for the consumed Paper 28 number | 0 |
| Exact `TERMINAL_BUILD_PROFILE_FIREWALL_BLOCKED` status | 0 |
| Exact `LOCAL_EVIDENCE_ONLY_NO_RELEASE` effect | 0 |
| Hidden retry, alternate profile, workaround, relabel, or replacement | 0 |
| Compiler, build-root, cache, scientific, or external effect | 0 |
| **Blocker** | **0** |
| **Major** | **0** |
| **Minor** | **0** |
| **Ambiguity** | **0** |

## Conclusion

The terminal record is byte-exact, factually faithful, nonexpansive, and
necessary.  It preserves valid theorem, publication, and static-source work
only as immutable local evidence; it accurately carries the unrepaired R2
build-profile failure; and it opens no retry, replacement, build, PDF,
release, or external-effect path.  The terminal status and effect are exact.

The next gate is a separately authorized terminal-review consumption event.
Only a later validated physical EOF ledger append may consume this PASS and
activate the terminal disposition.  Even after that consumption, Paper 28
remains local evidence only with no release.

BATCH07_PAPER28_TERMINAL_BLOCKER_PASS
