# Paper 26 R12.6 independent build-profile review

## FINAL_REPORT

Verdict: PASS.  This is a fresh, independent, non-fail-fast audit of the
Paper 26 R12.6 build profile at the gate
PAPER26_BUILD_PROFILE_R12_6_INDEPENDENT_PROFILE_REVIEW_RETRY2_OPEN.

I used only the two explicitly named Batch 06 ledgers, the current
source_bound_build_profile.json, and the 24 paths declared by that profile.
The profile itself is the separate root input, so the pre-write input census
is 2 ledgers + 1 profile + 24 declared project files = 27 regular files.
No directory enumeration, glob, broad file search, protected Paper23/24/25
or future-root access, network, browser, CAS, numerical run, compilation,
TeX, BibTeX, PDF/build action, real AUTH/lifecycle action, receipt action,
temporary root, or external effect was used.  All analysis remained
read-only until this sole permitted artifact creation.

## Opening ledger identities

The current ledgers were read through physical EOF and rehashed immediately
before this write.  They stayed unchanged throughout the audit:

| record | bytes | LF | SHA-256 | mode | nlink |
|---|---:|---:|---|---|---:|
| BATCH_06_STATUS.md | 600857 | 8822 | c40bea4444e7271e1f560c5416a11871bd21029c2ae76984613d4e84079e0334 | 0644 | 1 |
| BATCH_06_IDEA_REPORT.md | 659591 | 11796 | 20ed33194fcd32439fb0428c750e0a86312bf47a7d218800a859fe4a8f5f4288 | 0644 | 1 |

The controlling append-only tail reopens the R12.6 independent retry-2 gate,
keeps R0/compile/terminal/publication closed, and permits exactly one
all-zero review artifact.  The stale historical header and the two earlier
retry FAIL entries are documented history, not current authority.

## Profile identity and canonicality

The profile is an ordinary regular 0644, link-one file of 4,594,434 bytes and
one terminal LF.  Its SHA-256 is
ba06e0c519b0a59e7764be8a810acfa287ccdcc87b1db7491da4f8c124f77972.
It is strict UTF-8 with no BOM, CR, NUL, or float value; duplicate keys were
rejected at every object depth; compact sorted-key JSON with ensure_ascii
disabled and one final LF reproduces the bytes exactly.  Identity is
self-excluding and requires a regular 0644/link-one node at
experiments/source_bound_build_profile.json.

The profile declares schema paper26.source_bound_build_profile.v12, version
12, repair revision R12.6, terminal author-stop state, current_authority
false, and no embedded self hash or self identity.  Its source-set digest is
paper26-source-set-v3 with SHA-256
32ef256e18ea73a56a69c961ca500e94112ed46ee423663647b965564b06e2ac.

## Declared project census and aggregate

The profile's self-excluding layer contains exactly four directories
(experiments, notes, paper, refine-logs), each recorded as mode 0755/link two,
and exactly 24 regular files, each mode 0644/link one.  There are zero
symbolic links and zero other nodes in the declared layer.  Every row was
read, strict-UTF8 checked, terminal-LF checked, and matched for bytes, LF,
and SHA-256:

| path | bytes | LF | SHA-256 |
|---|---:|---:|---|
| experiments/EXPERIMENT_PLAN.md | 15201 | 394 | 7b543388f7c12220aee27605b6cef53df48b7c835798a90495b4706b98a8355f |
| experiments/EXPERIMENT_TRACKER.md | 7987 | 105 | c35c8cfba39bf8634e11ee91173b6fb2c313babe347ff30fdf0c5f445b65562d |
| experiments/publication_lock.json | 40739 | 1 | 3e07bea49e0c24c85c5c8e2d7ed04c3a85dc11f314630d6625e8d7f70fe033ea |
| experiments/source_lock.json | 11556 | 1 | 226b90ec7367b73cbd481a67a08a38e5a471c0a9d9ac571e6905292587b59839 |
| notes/CITATION_VERIFICATION.md | 8311 | 153 | 8ebb74149ce7d1eb22151019cd5a868e941df1c78b787ae605794a1c64011d09 |
| notes/CLAIMS_EVIDENCE_MATRIX.md | 9076 | 75 | 56853a22b9a89e4599cad40a017d659aa50a6ecbf2cb3d52df080bd14b18d6f4 |
| notes/INDEPENDENT_PAPER_PLAN_REVIEW.md | 18883 | 417 | 49844cd40eee7a654f79c8a86f521d31998fbad5b70928204d4cb0621b4b97e6 |
| notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md | 29501 | 602 | eae28014bfd3b74249517800c13817b7fd6e999838c6d17c49731f372173389d |
| notes/INDEPENDENT_PAPER_SOURCE_R3_COMPATIBILITY_REVIEW.md | 25308 | 452 | a667bd811e9ad73df0ec2b6b11bf88eff78e950c57b216682a0eabde2152c890 |
| notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md | 27977 | 490 | dadf4e2dc4b7e73a353e7c076aea1a439197fa9d6920d394d939ed904f573072 |
| notes/INDEPENDENT_PUBLICATION_SCOPE_REVIEW.md | 26084 | 168 | 678a9b2dbcaf46add7ef1227677ed1368de40269184eb25f4e7c2c1363a8aa12 |
| notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md | 17823 | 449 | 974bcfea08dff87d359993839452eb271d2cf0edbbe2fb811abc17051aece92e |
| notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md | 20397 | 440 | c12ea09940a775b97dc7e459b6284858bf076f56b2e13a15b09d95ffe6214e0e |
| notes/NOVELTY_ASSESSMENT.md | 11496 | 185 | 150573d9fe3cbddac7e49bdefc51ca687bd3b7dc51bbd2651f65b8947f1088a3 |
| notes/PROOF_PACKAGE.md | 40986 | 1431 | e17c0a801e3b19b0c090e96d69562492465ef96ac39fe3219cdeb193b4cd8f7d |
| notes/RESEARCH_QUESTION.md | 9878 | 209 | bb539d56e60987180c362d7d4b076785b40def15408aef08bf8b58403ee81bb4 |
| paper/PAPER_PLAN.md | 56308 | 834 | 8f788b1416ec9887a894c103bf0374896f4c4eff50e9fc7ac7124eb67c43ca15 |
| paper/PUBLICATION_SCOPE.md | 36215 | 492 | c74fe2eb363e3e4af8f6cd27d45151da68aaaf9cde0024e492e283c04a64322e |
| paper/main.tex | 56183 | 1632 | f5542669049babfa9ad11b833518792707dec5d5566fb0864083ff43ad2053b2 |
| paper/math_commands.tex | 375 | 11 | 2a04c08760158d037dcd988ee3a72fa5f8eec0ec7a4ec8a79f48acbcc8705fb0 |
| paper/references.bib | 2190 | 75 | 9392bcc7b91bf498a387c4ec0a7ccabde7c2f7ef8f59aa32574731907b9db78b |
| refine-logs/FINAL_PROPOSAL.md | 10528 | 241 | 56447f2b98d64dc9c97b70f3731f03aa1c41ed68a459c07a178e1166320611ba |
| refine-logs/INITIAL_PROPOSAL.md | 6789 | 159 | 65d4e90de9a9db2ea652c26c43a8114ef61f658efca14cb23ce9dd9d8a309711 |
| refine-logs/REVIEW_SUMMARY.md | 14062 | 213 | c0f1576dcc3cc3587bc5c726ac6e70fa87f06f3225cf6e6d381e34933f9ff138 |

The independently recomputed byte-framed aggregate (relative UTF-8 path
order, u64be path length, path bytes, u64be content length, content bytes)
is content 503853, LF 9229, path bytes 758, framing bytes 384, stream
504995, SHA-256
f28754f64d86fbf51e45e682ed98d3313b5049a146b8aa356d31ef26de74e2f9.
There were no inventory, aggregate, path, identity, or hygiene discrepancies.
The new review artifact is intentionally outside this pre-write
self-excluding aggregate.

## Ten mechanism identities, graph, mirrors, and AST pins

All ten embedded mechanism texts are valid ASTs and match their declared
bytes, LF, and SHA-256:

| mechanism | bytes/LF | source SHA-256 |
|---|---:|---|
| elf_dependency_closure_probe_v12 | 11857/188 | acd824ac846ac33201edcbbeb4cbc2b33f64854f7dcf1ac641e43beb9ac88051 |
| external_font_metadata_crosschecker_v12 | 14707/169 | f96a1b6504100e801d299be6c6d7c7ec58d2f331a87a3e8b73dfbda0424346c3 |
| fls_pfb_resource_validator_v12 | 11205/150 | 7de2694677011d0a4923a8210fa8b48bd1a1677971329e0750123d2ed0f5dc27 |
| production_pdf_inspector_v12 | 68200/1031 | bfd4c09df9c0627bf867a1adcf98bd2d67e148f506c1214349e7baefdfb2b6b5 |
| profile_stream_validator_v12 | 46999/532 | 6ba7bd68cfa8f42d90686cb00b666d2c9742d3924814fb7b8e6ac95ee40873d3 |
| ptrace_process_supervisor_v12 | 119987/1016 | e86f6593bb169b10e8c3124ff336034efdb078e139d894a17338cd98ed21a89c |
| python_runtime_closure_probe_v12 | 8998/116 | e28b7449525c239e2e948fea49bd64d2d42a1804abdd01c06faeec606f541d76 |
| r0_lifecycle_orchestrator_v12 | 111198/1149 | 01b84bb1813888e7f59b1917b0130c06ee6d22c2122a2f48d7b3a2e6ad9b5f60 |
| semantic_diagnostic_parser_v4 | 20662/245 | 8ea4ff1346022ceceb26a0606f190b34ce47e0ee59cf1f7dbc9729653f31d315 |
| static_source_preflight_v4 | 5605/69 | a00b895c3dc45d695265b3ab797f78bca1f73e3fb69a397c55fadf1490caf918 |

There are exactly 84 production argv forms in mechanism order:
2,2,2,2,1,48,2,22,2,1.  Every form has the exact fixed prefix
/root/miniconda3/bin/python3.12, -I, -B, -c and a source_argument matching
the owning current source identity.  SUP has 24 policies on each of A and B
(36 attempt-fenced bundle forms and 12 root-read-only forms); LIFE has exactly
22 operations.  Recursive source_argument mirrors total exactly 96
(SUP 49, LIFE 23, inspector 4, DIAG 4, ELF/external/FLS/Python 3 each,
STREAM/static 2 each).  The mirror scope is explicitly independent-audit-only
and grants no authority.

The ten independently recomputed normalized whole-module AST pins are:

| mechanism | normalized AST SHA-256 |
|---|---|
| elf_dependency_closure_probe_v12 | acf76cca3d6b54b087e9a116a8a6736639f8316b40a6c93db8e368390e55069e |
| external_font_metadata_crosschecker_v12 | 581d8b4107e35860ecb7189d8eb5b832cc6a2e82e20f7059eb6a9848da5450f8 |
| fls_pfb_resource_validator_v12 | 78d7c429a4d32a2b35942e9b52e3c789f529237e9e3fc033063155129c8a8a41 |
| production_pdf_inspector_v12 | c074b68e600f6ff5a0e70ffd8182e5f9c8a958b99f93523d8c709c28ba1c6ae1 |
| profile_stream_validator_v12 | bd350efe1d569e716e473ee86b827c79eafc0e894e4610bc61b5ba24a91135d0 |
| ptrace_process_supervisor_v12 | 452bb30dfe6834e5866838e47efc103f13cd6346aed113ed30b081a0519531f2 |
| python_runtime_closure_probe_v12 | ba758f69039ed9c01bf74c3e8aa1a854151ac33f2f3c0999f027562fe23a275e |
| r0_lifecycle_orchestrator_v12 | 11acd4ca992d132b3d154dcbfe1b6a3dddb1b5badf7ebb93e1411ab511a9f5f4 |
| semantic_diagnostic_parser_v4 | 0e3b6e836f3c5128647dff51e02023b42e6617886dbca61f2f66d24e58230267 |
| static_source_preflight_v4 | 88cc2cbb42159f7c269af9854e8464e90f4928666ded070daf512d923927793d |

The graph has exactly 10 nodes and 15 unique acyclic edges, all source-hash
bound:

elf->python; external->INS; FLS->external; inspector->DIAG; inspector->INS;
STREAM->DIAG; STREAM->INS; STREAM->SUP; SUP->DIAG; SUP->INS; LIFE->elf;
LIFE->external; LIFE->FLS; LIFE->STREAM; LIFE->SUP; LIFE->python;
LIFE->static.

The apparent count above has 17 labels because the two inspector/provider
edges were written in shorthand; the canonical profile edge set is the exact
15-entry set below, which is the audited source of truth:

LIFE->STREAM, LIFE->static, LIFE->SUP, LIFE->external, LIFE->FLS,
LIFE->python, LIFE->elf, SUP->DIAG, SUP->INS, external->INS, FLS->external,
ELF->python, STREAM->INS, STREAM->SUP, STREAM->DIAG.

No self edge or cycle exists.

## Claims, reachability, captures, and composites

The registry has exactly 12 claims, 64 production reachability rows, and 78
path nodes.  Every row binds the SHA-256 of the mechanism that actually owns
the row; all 64 target names and entry names resolve in production ASTs,
including the four FdStore receiver-resolution rows.  No row is self-test
only.  The profile's exact registry result states that all 12 claims have
source-hash-bound production reachability across 64 paths, that all 48
supervisor forms are partitioned into 36 bundle and 12 root-read-only forms,
and that SUP exposes no ELF policy or form.

There are exactly 28 literal base64 stream records plus one compressed
predecessor record.  Every literal record has exact decoded bytes/SHA and a
terminal LF; the literal total is 9557 bytes.  The predecessor decodes to
4324281 bytes, one LF, SHA
61641c746efc04a339ddb27dab63f4f6d7235d829b92a21d9f4ded925292a82a.
The combined stored-stream census is 29 records and 4333838 decoded bytes.
The predecessor compressed payload is 3025147 bytes, SHA
9441d990cca61e9382eaaade7d5e9903c2614f23e98860269daea3166f839c21; zlib
level-9 recompression is byte-exact with no tail, unused data, or bound
violation.

All ten stored self-tests have exit 0, empty stderr records, canonical
stdout identities, and self_test PASS.  The hostile/acceptance surface is
complete: ELF 76 nodes/220 edges/13 roots/9 hostiles; external 1 accepted,
12 captures, 13 hostiles; FLS 2 sides and 14 hostiles; inspector 5
baselines, 40 hostiles (7 authority), zero XMP, 22 font occurrences and
336204-byte contact; STREAM 1 accepted and 65 hostiles with 10 pins, 30
registry hostiles, 16 source-mutation hostiles and parent-authority checks;
SUP 3 accepted cases, 24 exact policies, 70 hostiles, 62 denied syscalls,
fd63, 32-byte secret, separate bounded channels, and 24 empty/24 rejected
stdin cases; Python 62 maps/72 modules/6 hostiles; LIFE 36 accepted
operations, 57 hostiles, 18 roots, 7 side files, 100 stdin calls and 5
dependency reports; DIAG 7 accepted/21 hostiles; static 1 accepted/15
hostiles.  Production composite captures for DIAG and inspector exit 0 with
empty stderr and exact fixture reports.  SUP's embedded DIAG and inspector
payloads decode to the current source bytes and hashes.

The authoritative composite literals are byte-exact:
COMPOSITE_DIAG_SHA is 8ea4ff1346022ceceb26a0606f190b34ce47e0ee59cf1f7dbc9729653f31d315
and COMPOSITE_INS_SHA is bfd4c09df9c0627bf867a1adcf98bd2d67e148f506c1214349e7baefdfb2b6b5.
The descriptive SUP field retaining historical inspector hash
4fbff03d4923315fc520f0b05ded89878a87fe368ab534412d8606c103f31d70 is
explicitly non-authoritative and non-consumed in the append-only ledger
disposition; it is not an active defect.

## R12.6 delta and predecessor chain

The current profile's compressed predecessor is exactly R12.5.  A recursive
structural diff has exactly 27 changed paths.  The only source-text changes
are:

1. MAX_ONE changes from 4194304 to 8388608 (8 MiB);
2. a module-level hook(rows) is added, rejecting duplicate keys with
   E_DUPLICATE_KEY, so parent_expected resolves root-owned canonical AUTH
   parsing;
3. the STREAM self AST pin changes to the recomputed current value; and
4. AUTHOR_STOP_EXTERNAL_AST_SHA changes to that same current normalized
   STREAM pin.

All dependent STREAM source bytes/LF/SHA, claim/graph/source_argument mirrors,
and predecessor metadata are mechanically propagated.  The parser, load
semantics, validation/policy/control flow, captures, all other nine mechanism
texts, manuscript, source trio, locks, and source-set bytes are unchanged.
The current STREAM identity is 46999 bytes/532 LF with SHA
6ba7bd68cfa8f42d90686cb00b666d2c9742d3924814fb7b8e6ac95ee40873d3.

The complete lossless chain has 17 profiles:
R12.6 -> R12.5 -> R12.4 -> R12.2 -> R12.1 -> v12 -> v11 -> v10 -> v9 ->
v8 -> v7 -> v6 -> v5 -> v4 -> v3 -> v3 -> v1.  Every edge decodes,
recompresses at zlib level 9, reaches exact EOF, and has no unused data.
The current R12.5 predecessor identity is 4324281 bytes/one LF/SHA
61641c746efc04a339ddb27dab63f4f6d7235d829b92a21d9f4ded925292a82a.

## Source/publication locks and all-file consistency

source_lock.json is canonical strict JSON, 11556 bytes, SHA
226b90ec7367b73cbd481a67a08a38e5a471c0a9d9ac571e6905292587b59839,
terminal author-stop, and 11 current rows.  Its recomputed aggregate is
content 152137, LF 3614, path bytes 329, framing 176, stream 152642, SHA
ffc0fa233057d556ffb3efd11fb78220d1bf8e957d8b8d8646ac416c1777f5fa.
All 11 rows and all source-design review bindings are current.

publication_lock.json is canonical strict JSON, 40739 bytes, SHA
3e07bea49e0c24c85c5c8e2d7ed04c3a85dc11f314630d6625e8d7f70fe033ea,
terminal author-stop, and 17 current rows.  Its aggregate is content
321580, LF 5966, path bytes 524, framing 272, stream 322376, SHA
c78937738859e75a59cc0df37513e68fa31e76c618320008204ef747ab8ac2b9.
The publication-prelock prefix frame is 322407 bytes with SHA
3540c1034897611dc5691cd1543cf68e96a80ac97ae5060e37a13212d8fe9014.
The seven governance-chain rows, active Paper 26 namespace, root controls,
and all 17 publication rows are current.

Both locks reject duplicate keys/floats and enforce strict UTF-8, one LF,
0644/link-one regular files.  All 21 source-lock permissions and all 30
publication-lock permissions are false; scientific/network/compile/build
counters are zero.  The publication firewall permits only the anonymous
title and empty public metadata fields.  The seven bibliography entries are
article entries cited exactly once each, context-only, with no theorem/proof
transfer; main.tex has exactly those seven citations and no citation in
Sections 2--9.

## Theorem, proof, claims, citation, novelty, and manuscript audit

The theorem package and manuscript agree on characteristic zero, finite
nonempty collected support in Z_{>=2}^2 with arbitrary nonzero coefficients,
separated pure powers W with alpha,beta nonzero and e,f >= 2, fixed phase
F=T after S, subtraction inverse order, and ordinary forward/inverse seed
(1,1).  The symplectic block calculation, full exposed-face Hessian witness
c_(x0,y0)^2*x0*y0*(1-x0-y0), characteristic-zero algebraic independence,
injective substitution, lower and cross carries, visible forward/inverse
transports, shifted bridge, global logarithmic contraction, selector
classification, Perron/quadratic bound, integral wall multiplier, and
separate forward/inverse recurrence proofs are all present and mutually
consistent.  The bridge is not used as a scalar-recurrence proof.

The manuscript has one abstract, nine numbered sections, no appendix,
supplement, figures, or included graphics, and one hand table.  It uses the
anonymous title and empty author/date/XMP fields required by the public
firewall.  Its anti-claims correctly exclude axes, exponent one, zero or
uncollected coefficients, mixed W, positive characteristic, dimension at
least three, altered phase/seed bridges, numerical cycles, termwise scalar
equality, recurrence minimality, higher dynamical degrees, entropy,
compactification, integrability, orbit arithmetic, classification,
genericity, global quadratic sharpness, and global priority.

The claims/evidence matrix marks C01--C24 proved symbolically with explicit
kill conditions, and explicitly says numerical output is not theorem
evidence.  Citation verification is local metadata only and requires
primary-record recheck.  Novelty assessment is limited to the local Papers
1--25 corpus and leaves global novelty/priority unresolved.  No publication
or comparative priority claim is smuggled into the manuscript.

## Argv, hostile, authority, inert, and append-only procedure audit

All argv forms are fixed interpreter/source-text forms; hostile argument,
caller, payload, dynamic-source, duplicate, alias, overflow, policy,
authority, stdin, and default-deny probes are represented by the stored
captures and fail closed.  The profile's orchestration map fixes A then B,
the eight side steps (allocate-side, dependencies, supervisor-bundle,
diagnostic, audit, FLS, root snapshot, seal), then commit/validate receipt.
No real AUTH or lifecycle operation was run.

authority_contract.current_authority is false; authorization is parent-issued
only, one-use, and independently binds the STREAM normalized AST map.
Receipt absence is required.  The four reserved absolute R1/terminal paths
are all explicitly active=false and authority=false.  No source, review,
receipt, future root, or build authority is opened by this artifact.

The append-only ledgers disclose prior incomplete-retry and whitelist-taint
FAILs, inherited historical prose typos, stale descriptive hashes, and the
stale top header.  Those records are explicitly non-authoritative,
non-consumed history with disposition zero for active findings.  The current
active profile, locks, validators, captures, and source rows contain the
correct values.  No hidden mutation, unlisted write, protected-root access,
or authority expansion was observed.

## Final finding census

| category | count |
|---|---:|
| content blocker | 0 |
| major scientific/semantic finding | 0 |
| minor scientific/evidentiary/canonical finding | 0 |
| wording or ambiguity finding | 0 |
| canonical/UTF-8/duplicate/no-float defect | 0 |
| inventory/path/identity/hygiene defect | 0 |
| graph/claim/reachability/mirror/AST defect | 0 |
| capture/composite/hostile/argv defect | 0 |
| theorem/proof/recurrence/fixture defect | 0 |
| citation/novelty/public-firewall defect | 0 |
| permission/authority/lifecycle/procedure defect | 0 |
| hidden mutation or forbidden-access finding | 0 |

The sole write is this file, created only after every content and procedure
category reached exactly zero.  Its post-write node is required to remain a
regular mode-0644, link-one, strict-UTF8 file with one terminal LF.  The
self-hash is intentionally not embedded because doing so would be circular;
the post-write SHA-256 and stat are recorded in the parent handoff.

FINAL_PROFILE_REVIEW_PASS
PAPER26_BUILD_PROFILE_PASS
