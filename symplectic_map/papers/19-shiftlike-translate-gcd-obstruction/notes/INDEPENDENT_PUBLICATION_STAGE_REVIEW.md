# Independent Publication-Stage Review — Fourth Replacement

Date: 2026-08-20 UTC  
Role: fresh independent fourth replacement publication-stage reviewer  
Round: `FOURTH_REPLACEMENT_AFTER_CONSUMED_PACKAGE4C92_SAME_PASS_AUX_FAILURE`  
Decision scope: exact live v5 Paper 19 U21 only

## 1. Independence, authority, and read boundary

I authored none of the reviewed inputs, the v5 lock, the consumed package,
the incident evidence, or either stale third replacement review. I treated the
prior publication and source review files only as identity-bearing stale
inputs. Their earlier pass claims were not evidence for this decision.

The exact authorized U21 consists of twenty-one regular project files under
the four directories `experiments`, `notes`, `paper`, and `refine-logs`. I
read and rehashed that exact universe. I did not inspect any temporary or
shared-memory residue, transport, package, build root, dashboard, predecessor
project, or unrelated workspace object. I ran no TeX, BibTeX, CAS, scientific
code, enumeration, build, cleanup, persistence, or external action.

This review has one conditional write: replacement of this existing file.
It confers no authority over the manuscript, bibliography, lock, scope,
dashboard, source review, package, build, residue, finalization, release, or
external systems.

## 2. Exact activation identities

The live v5 lock authenticated before this write as:

- SHA-256 `9726e5bd3b570e74541578bac86d87544a8db5a0aec05f5ea8afa8eddb45d1c9`;
- 443271 bytes and exactly one LF;
- regular, non-symlink, mode `0644`, valid UTF-8, no BOM/CR/NUL, and one
  terminal LF.

Strict parsing independently rejected duplicate keys and non-finite numeric
constants. Recursive key ordering, compact separators, `ensure_ascii=False`,
`allow_nan=False`, semantic array order, and the terminal LF reproduced the
lock byte for byte.

Before this write, the exact live U21 independently rehashed to:

- aggregate SHA-256
  `51f2923ca000973a2ae3020fa0ffa40d970f40da41631fe1239fd3ebaa8bd450`;
- 863589 bytes and 7260 LF;
- twenty-one regular, non-symlink, mode-`0644`, terminal-LF files and four
  directories;
- no additional member in the authorized path universe.

The consumed stale review identities matched exactly:

- publication review:
  `19cf8034e092299ec5f50d0807d79330426e929930aa87ae5f555a483145e52e`,
  15460 bytes, 304 LF;
- source review:
  `c22fe658dd633f8503ec85c5e980cc72d2ff0288b26b08d3cd5fb9c6b64f9666`,
  24699 bytes, 239 LF.

The manuscript and bibliography remained exactly:

- `paper/main.tex`:
  `c8eb38dcc13a78bebb267d8021965315ab82f7e1ec5d7317f93a49e148b6d588`,
  68921 bytes, 1116 LF;
- `paper/references.bib`:
  `5da35a497c24e7f62d4f088da0de2cc3f409a0df23c352aec6aa5360068d050f`,
  7031 bytes, 227 LF.

These checks satisfy the activation boundary: the externally applied v5 lock
is live, the lock-repair author has stopped, and the current gate is this
fourth replacement publication review.

## 3. V5 incident reconstruction and containment

The lock contains a complete, internally consistent account of the consumed
package/run incident without requiring a live residue read.

The consumed package nonce is `4c92a7e16fd03b85`; the consumed run nonce is
`666f18106e0155e4`. The outer capture reconstructs canonically to SHA-256
`3af1d82f685c6d78d264e99ebdb2943251da96bdb22a04c8e0bfd2fa1ece7550`,
1015 bytes, one LF. It binds the exact child argv, project cwd, five-variable
environment, closed stdin, separate streams, child return code 86, empty
stdout, and the exact 92-byte diagnostic:

`R0_GATE_ERROR: SAME_PASS_INPUT_UNBOUND: root-local INPUT absent at pdflatex start: main.aux`

Only the first A-root `pdflatex` child started. It completed with return code
zero. No BibTeX child, later A pass, B child, comparison child, validator
child, replay, HOLD, approval token, persistent output, cleanup, or project
write followed. The child stdout identity is
`7df762276fb9d1a5395cd4b9e83c33b21a3b6863c2c2821a2f3ef7c9cd66ea04`;
stderr is empty.

The frozen pass-one recorder has SHA-256
`2e52128e7333f7069ddd69d06da892819610cf5df8cb5cdd6ebd30445fe26d14`,
29263 bytes, 462 LF. Its ordered anchors are coherent: PWD at line 1,
`OUTPUT main.aux` at line 301 / I/O ordinal 300, and `INPUT main.aux` at
line 438 / I/O ordinal 437. Counts are exactly one PWD, 458 INPUT, three
OUTPUT, and 461 I/O records. The prepass manifest has SHA-256
`7476d946249cb152897277b726277003cc3f369c260cc8bd32ba624b80195bac`,
3206 bytes, one LF, and binds `main.tex` and `references.bib` while correctly
recording that `main.aux` was absent at pass start.

The four consumed top partitions reconstruct exactly to nineteen regular
files, nine directories, 922810 bytes, and 11395 LF. Their combined file and
directory record streams independently reproduce
`66729d8f1abe7f038e6efaeb9583a450c71d7b04e3352ccaab3e3bfd1093a104`
and
`661254b590e6e5bb13dd845d2c5d3e6703155e55e16360eed2a8ff7240132d7d`.
Every partition record, canonical-record digest, stream byte count, mode,
terminal-LF field, and total is consistent. The consumed package manifest
and prepass manifest also reconstruct byte for byte from their embedded
canonical objects.

The failure is therefore a deterministic temporal-ledger policy defect in
the consumed package, not a manuscript, bibliography, TeX, or scientific
failure. Retrying unchanged cannot succeed. The package and run nonce are
consumed, non-authoritative, cleanup-only after a future successful gated
run, and forbidden for reuse, re-execution, or pass evidence.

## 4. Heterogeneous typed identity epochs and mandatory anti-claim

The v5 repair correctly narrows the evidence claim. Its coverage name is
“complete recorder-input-event coverage with heterogeneous typed identity
epochs,” not equivalence to the v4 uniform input-byte ledger.

Every raw FLS INPUT occurrence must be classified exactly once as one of:

1. root-local prepass;
2. root-local same-pass-generated stable available file; or
3. system explicit root.

The exact same-pass-generated allowlist contains only `$ROOT/main.aux`.
Expansion requires a new lock and static audit. Pass one starts with the file
absent. A later pass may bind a pre-output `main.aux` INPUT to its pass-start
preimage, but a post-output INPUT may use the generated class only after all
v5 guards pass. Each pass has the exact declared FLS topology and
cardinality; unknown, ambiguous, or unexplained occurrences block HOLD.

The in-process Linux inotify envelope is installed on the stable fresh build
root before each `pdflatex` spawn and remains active through child reap,
postimage capture, final drain, and deliberate teardown. It binds raw event
bytes, parsed event ledgers, watch/root identities, ordered masks, event
counts, child spawn/exit envelope, writer close, inferred reader epoch, and
the separately labeled verifier read. It rejects overflow, unexpected watch
loss, unknown events or names, malformed bytes, cookies, attribute/link
changes, later writes, multiple writers, moves, deletion, replacement,
symlinks, or inode discontinuity.

After a successful child, the postimage is opened with `O_NOFOLLOW` on one
file descriptor, required to be regular and link-count one, read completely,
checked for stable lstat/fstat identity, frozen with `O_EXCL` mode `0600`,
fsynced, closed, and read back before the next child. A/B retain their raw
root-specific evidence separately and compare the normalized topology,
occurrence mapping, counts, source classes, preimages where applicable,
postimages, evidence identities, identity unions, and unexplained count
exactly. Replay reparses the frozen raw FLS and inotify streams and rebuilds
every ledger and normalized view without treating final live roots as
identity authority.

The central anti-claim is explicit and mandatory: the `main.aux` digest and
byte count identify only the frozen post-child pass-final file. The monitored
envelope can establish unchanged availability during an inferred reader
epoch. It does not identify pass-start, open-time, or read-time bytes; bytes
or offsets consumed; completeness or EOF consumption; or PID/fd attribution.

Accordingly, all required booleans remain false: `bytes_consumed_proven`,
`read_time_bytes_proven`, `pass_start_identity_for_generated_occurrence`,
`consumed_offsets_proven`, `consumption_completeness_proven`,
`PID_attribution_proven`, and `fd_attribution_proven`. The consumption-byte
proof count is zero. Any future package that weakens, omits, or contradicts
these fields must be blocked.

## 5. Cleanup universe and future package fences

The known cleanup union is internally exact and disjoint:

- legacy component: 29 tops, 189 files, 51 directories, 4665893 bytes,
  55057 LF;
- post-lock invalid-package component: six tops, 26 files, six directories,
  606341 bytes, 8744 LF;
- consumed failure component: four tops, nineteen files, nine directories,
  922810 bytes, 11395 LF.

Their union has exactly 39 tops, 234 files, 66 directories, 6195044 bytes,
and 75196 LF. The independently rebuilt known-union streams match:

- files:
  `2b946c1ea7e3bfef6d4e000a9b9b31fdd715bbdd0a09827665e9342ad1bce482`;
- directories:
  `87324da73dccb0354b8a76a28e5f8e3a8a66c4f9f9a3e72838310c7dd514fb73`.

The exact future topology is 39 known tops plus four new literal tops: one
fresh immutable package and fresh A, B, and evidence roots under a single new
run nonce. The future successful receipt must freeze every actual record and
the exact union of 43 tops. Missing, extra, overlapping, symlinked, drifted,
or unidentified content blocks persistence and cleanup.

Cleanup is not authorized by this review. It remains after successful HOLD,
approved replay, persistence of PDF then receipt, strict readback, and a
separate all-before-any cleanup preflight. Deletion must use exact literal
leaf-to-root paths, no glob or recursion, and may never target `/tmp` itself.

Both replacement reviews must pass in order before a package author may be
separately invoked. Package construction is out of project, uses fresh
package/run nonces, binds the exact post-review U21, implements every typed
epoch and regression obligation, and ends at AUTHOR STOP. An independent
static package audit follows. Even its pass does not authorize a child: a
separate package-specific parent GO must bind the package, project state, and
fresh literal roots. Any failure consumes that package and run and requires
new governance.

## 6. Independent manuscript, proof, and citation audit

The source is a coherent proof-first pure-mathematics article with the exact
locked title. Its abstract is independently counted at 198 words, inside the
180–220 band. It presents the character-shadow/scalar-lift distinction,
Part A lift scheme, q-at-least-three obstruction, non-optimality fence, and
resonant q-equals-two boundary before technical development.

The source has exactly eleven numbered sections, zero appendices, zero
figures/images/diagrams, zero numerical-result tables, and no deferred proof
supplement. It contains exactly thirty-one numbered lemma/proposition/theorem/
corollary statements. The thirty new or internally proved results have
matching main-text proof environments; the remaining anchored dimension
theorem is explicitly delimited and cited as predecessor input. The article
uses no computation, CAS, finite enumeration, code, data, empirical result,
randomness, or scientific experiment as evidence.

The common map, inverse, recurrence orientation, exact equation/state ranges,
window varieties, survivor sets, and projection bijection agree. Part A uses
the actual collected support and correct nonzero hypotheses. It proves middle
collapse, a free saturated quotient, equality-subgroup rigidity, active
interval and activity count, exact scalar reconstruction, both open families,
normalization, all-root-tuple avoidance including the zero-dimensional case,
geometric component counts, multiple-root nilpotents, the fixed-support
finite-flat root scheme, relative lci and discriminant-complement smoothness,
completed fiber equations, and the qualified coefficientwise arithmetic
endpoint.

Part B keeps arbitrary character rank through exclusive labels, independent
component colors, cycle-integrable integer heights, and the colored Laurent
recurrence. Minimum-height persistence and the triangular zero set prove
q-squared extinction. Central coverage uses the required `t,h,j` construction
and inequalities; the delta block, both generating functions, coprime
semigroup guard, and first `1+T^q` collision are derived without enumeration.
Original residue counts and full ambient-coordinate coverage precede the
actual lattice conclusion. The seven-label proof treats both zero cases,
excludes `2L=q`, checks all indices, and permits the sole compatible
coincidence. Its scalar chain is in the locked order:
`bc^(d-1)=-1`, `a=-1`, then `2c=0`. The q-equals-two theorem proves both
directions, five active scalars, a primitive exponent vector, the actual
polynomial automorphism and inverse, and generic inactive-residue filling for
arbitrary gcd.

All eighteen scientific anti-claims are preserved in substance. In
particular, dimension is never assigned to `T_m`; Part A does not classify
lower-dimensional or inclusion-maximal translates; `E_m` is not promoted to
a Hilbert/Fano/fine-moduli object; fiber, squarefree, support, lci,
discriminant, and compatible-group qualifiers remain visible; Laurent is
qualitative only; and the q-at-least-three conclusion is not called exact,
optimal, shortest, minimal, or sharp.

Static citation extraction finds exactly 22 distinct TeX citation keys and
22 distinct BibTeX entry keys, with exact set equality and no duplicate
entry. Every entry is cited. All labels are unique, and every `ref`/`eqref`
target exists. The sole external proof input is Laurent at its qualitative
scope and only after recurrence geometry. Other external sources provide
context or bounded collision control. The three anonymous companion works
are used only for precisely delimited predecessor ownership. No metadata was
invented beyond the frozen citation ledger and verified predecessor
bindings, and no absolute-priority statement appears.

## 7. Page contract and public safety

The authoritative rendered contract is the v5 contract: 22 substantive
pages, references beginning exactly on page 23, two nonempty reference pages,
24 total pages, no appendix, blank page, padding, or source expansion. The
unchanged 29-page or 26–29-page statements in fourteen non-lock inputs are
explicitly exhaustive historical source-design estimates, not rendered-page
authority. They do not reactivate the old target. The unchanged source has
the required `clearpage` before its nonempty bibliography and no structural
padding device. The later deterministic two-root build must independently
re-prove the exact rendered page facts before persistence.

The public manuscript contains no author, affiliation, email, ORCID,
acknowledgment, funding field, local path, hash, reviewer identity, dashboard
state, lifecycle token, private machine identity, TODO/FIXME/XXX, or
`[VERIFY]` marker. Predecessor prose is neutral third person. The bounded
literature statement is dated and explicitly leaves unindexed, non-English,
unpublished, and private work unresolved.

## 8. Permission and temporal-coherence decision

The v5 lock separates its construction-time self-excluded application
manifest from its post-application gate. Thus the construction-era phrase
`v5 candidate static audit only` does not authorize or block a role after the
externally authenticated lock replacement and lock-repair AUTHOR STOP. The
more specific post-write fields agree: the current lifecycle names this fresh
fourth publication reviewer; `authorization.current_gate_after_write` names
the publication-review gate; and the role-exclusivity window allows only this
one-time review replacement. There is no live permission contradiction.

After this file is replaced and read back, the only next possible project
write is a separately invoked, fresh, independent fourth source review of the
resulting exact U21. This decision does not make the stale source review
authoritative and does not authorize package construction until that new
source review also passes. It authorizes no compilation, build child, HOLD,
replay, persistence, cleanup, manuscript change, bibliography change,
finalization, release, submission, upload, repository action, messaging, or
external effect.

## 9. Verdict

Every obligation of
`fourth_replacement_review_contract_v5.publication_stage_replacement` and
the independent publication-review contract passes on the exact authenticated
live v5 U21. The incident is completely bound and fail-closed; consumed
objects are non-authoritative; the typed-epoch amendment is precise and
retains its mandatory anti-claims; cleanup and future package gates are exact;
the scientific, proof, citation, page, ownership, zero-science, and
public-safety contracts remain coherent; and current permissions are
exclusive and fail-closed.

PUBLICATION_STAGE_PASS
