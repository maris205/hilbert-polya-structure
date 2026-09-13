# Batch 07 Paper 28 V2 pre-review manifest and action-history recovery review

review_outcome: PASS
review_role: fresh independent Batch07 Paper28 pre-V2 manifest/action-history recovery reviewer
review_basis: B07-E0164-P28-V2-PRE-REVIEW-MANIFEST-ACTION-HISTORY-DISPOSITION
consumed_authority_for_this_review: BATCH07_PAPER28_V2_PRE_REVIEW_MANIFEST_ACTION_HISTORY_REVIEW_AUTHORIZED
candidate_id: primitive_selector_cycle_monodromy_v1
candidate_version_reviewed: V2, quarantined before formal review
paper_number_consumed: false
project_path: absent
external_effect: none

## Independence and exact read boundary

I did not participate in Paper 27, Paper 28 candidate design, either V1 formal
review, or the parent recomputation.  I read only the 47 literal existing paths
authorized for this audit: `BATCH_07_STATUS.md` and the 46 self-excluding
source/control paths reproduced in the manifest table below.  Every access was
a direct exact-path open after a no-follow `lstat` of that same literal path.
I performed no directory listing, path search, glob or wildcard expansion,
recursion, symlink traversal, absent/future-path test, or Paper 28 project/build
probe.  In particular, I did not repeat either historical ENOENT attempt.  I
used only administrative `PYTHONDONTWRITEBYTECODE=1` Python for byte, LF,
mode, link-count, encoding, framing, and SHA-256 checks.  There was no web,
compiler, CAS/scientific execution, cache creation, cleanup, source mutation,
external message, release, or other external effect.  This report is my sole
write and was created only after the all-zero prospective census below.

## E0164 parent, ledger, and candidate binding

The bytes physically preceding E0164, excluding the single inter-event
separator LF, are exactly 520,378 bytes with SHA-256
`02723acf5ac430b1717a2ecd6da817080138b73386ab6a1192ec20cbce236e97`.
They therefore match E0164's `parent_ledger_bytes` and
`parent_ledger_sha256`.  The current controlled ledger is a regular
non-symlink mode-`0644`, link-one file of 526,700 bytes and 9,298 LF with
SHA-256
`4b3b85b5f09bb8db0bae6fa46927ad867aff6ae258451429c4f949d23ba79bfd`.
It is strict UTF-8, contains no CR or NUL, has exactly one terminal LF, and
ends in the exact complete line
`BATCH07_PAPER28_V2_PRE_REVIEW_MANIFEST_ACTION_HISTORY_REVIEW_AUTHORIZED`.
That marker is one exact terminal line; its other token occurrence is the
machine `terminal_marker` field.

E0164 is sequence 161, names this report as its only allowed creation, keeps
formal V2 reviews unauthorized, reports no scientific execution or external
effect, and records Paper 28 as unconsumed with its project absent.  Its
candidate binding also recomputes exactly: `BATCH_07_IDEA_REPORT.md` is 43,462
bytes, 1,094 LF, regular mode `0644`, link one, and SHA-256
`b22de69f2aa70f1bee748cee56b3ad9472ef0622ec4d40a2ce97acb08b1d3f6a`.
It is strict UTF-8 with no CR or NUL and exactly one terminal LF.  The exact
complete line `BATCH07_PAPER28_CANDIDATE_V2_AUTHOR_STOP` occurs once and is the
physical terminal line.

## Reproducible live source/control manifest

For each row below I directly measured the regular-file byte count, LF count,
physical mode, link count, and SHA-256.  All 46 files are regular non-symlinks,
strict UTF-8, mode `0644`, link one, contain no CR or NUL, and have exactly one
terminal LF.  `BATCH_07_STATUS.md` is intentionally excluded.  The literal
rows are bytewise sorted and use exactly
`path<TAB>bytes<TAB>LF<TAB>644<TAB>1<TAB>sha256<LF>`:

```text
BATCH_05_FINAL_AUDIT.md	17937	325	644	1	3e583ac5a989a689b93da3a6a6a74ac42e37f2caaa2b6601c7ca14e37d46de3e
BATCH_05_IDEA_REPORT.md	54677	1067	644	1	e697b0b5e252a42b08363548316ffdea620dec57f7970d106b06e7f6b54cfa46
BATCH_05_STATUS.md	63905	925	644	1	296cbbbde7df633de5f995285b3878477487f5ac8ac1032077cac1aa35bf4e1e
BATCH_06_FINAL_AUDIT.md	25301	436	644	1	8f28253a94918a6ab0c6934ce167c3d6129deadc50e7f41d46136dce8b19c1f3
BATCH_06_IDEA_REPORT.md	675259	12068	644	1	2e097d928bbe695866653c47aace6215358e0187326044e8eb548fddd3cd1ef3
BATCH_06_STATUS.md	616461	9095	644	1	5c95ac0f195ae7de935b0c2cc902ebcf6df15f0cb7292835d1c51ea208d45609
BATCH_07_CHARTER_REVIEW.md	20209	364	644	1	4ced8ab1e1b48d89ec088be40206bf3bbff3e23c77471c45672442883b322f73
BATCH_07_IDEA_REPORT.md	43462	1094	644	1	b22de69f2aa70f1bee748cee56b3ad9472ef0622ec4d40a2ce97acb08b1d3f6a
BATCH_07_PAPER27_CANDIDATE_V5_REVIEW_R1.md	18431	377	644	1	0ec08ac6a8cfc25548f213a132855aec58618c3c488a459083e5059a59da32ff
BATCH_07_PAPER27_CANDIDATE_V5_REVIEW_R2.md	13329	304	644	1	59cbcbd71b634534f4a84ede34a46a447bab31041ad4e71e87c7c847b9295f2f
BATCH_07_PAPER27_CANDIDATE_V5_REVIEW_R2_CORRECTION.md	16395	374	644	1	da719d459bb9fbcc925ef3c38adf5021af9a8961db82516cc416843ecd885106
BATCH_07_PAPER28_PRE_DISCOVERY_ACTION_REVIEW.md	3908	86	644	1	6e505a543e56b6657c14bb037a2aedd44144b62a6530883339f55652dcf845bc
README.md	9594	41	644	1	415bc57e4d2e87bcf078b969c7edf0c769f436d1ff41cfca1619f37540222cda
docs/candidate_registry.md	17936	41	644	1	27f43be37659125f6a9ed2183772325da83acea1239aed22fe71d9494a54b77b
papers/27-positive-newton-translation-reciprocity/PAPER_PLAN.md	18412	249	644	1	61be9c2849d37ba6def1e3dc43a96fcd895d0d9b36500166ff08bfe164d79ca4
papers/27-positive-newton-translation-reciprocity/experiments/EXPERIMENT_PLAN.md	4928	108	644	1	1b9628e18703fd2332c90799c71abaaa42467b7080cb35a59ab3617b1c4c9a9d
papers/27-positive-newton-translation-reciprocity/experiments/EXPERIMENT_TRACKER.md	3116	52	644	1	bbd8ec0ebdd866fb09174b65dd87075623fae78eba48e96aaccc4625deb45e8e
papers/27-positive-newton-translation-reciprocity/notes/BUILD_PROFILE.md	6124	117	644	1	8fba2cbb84a02078094fbced92cf2b6286e86b6be4360bdbc0a893bd55b32c6e
papers/27-positive-newton-translation-reciprocity/notes/BUILD_PROFILE_REVISION.md	5238	109	644	1	1c01ec583391c3f60996018debd85f860c4b9709f3913da49c7e6c686e032f63
papers/27-positive-newton-translation-reciprocity/notes/CITATION_VERIFICATION.md	9366	61	644	1	1a54b62d83cd6861679f851ec509854d6ed83eb046d5b6db7343b6e96aa9c26b
papers/27-positive-newton-translation-reciprocity/notes/CLAIMS_EVIDENCE_MATRIX.md	6022	43	644	1	b0415cf8118b6e33352d513e170f5c2ad854e54a3ba854d683faca3eb6425b14
papers/27-positive-newton-translation-reciprocity/notes/INDEPENDENT_BUILD_PROFILE_REVIEW.md	3496	38	644	1	e9e6a1918136092795aa3263a78ff8245e4cd91615ef04115cacc88a0954286e
papers/27-positive-newton-translation-reciprocity/notes/INDEPENDENT_BUILD_PROFILE_REVISION_REVIEW.md	9161	69	644	1	815f4940302b832f5315c4f2695bcacd21f8bba0ec22d274a78f1573b2f8254c
papers/27-positive-newton-translation-reciprocity/notes/INDEPENDENT_BUILD_REVISION_REVIEW.md	11434	181	644	1	549082029f4a1b0ed8b153d86fea858ef7e16173fae981db070a957080bd7781
papers/27-positive-newton-translation-reciprocity/notes/INDEPENDENT_PAPER_PLAN_REVIEW.md	14763	216	644	1	812e2f41982ef7379337d4bf5d5288ef5067594ceed5df6ffa30daf405554b25
papers/27-positive-newton-translation-reciprocity/notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md	13363	239	644	1	e097d63b9142a4db6827886e4f660db3f9cff343d5f82e6af1b94309cca1a0c0
papers/27-positive-newton-translation-reciprocity/notes/INDEPENDENT_PUBLICATION_SCOPE_REVIEW.md	13024	224	644	1	da409ec539a51ca29e2fcfc99d07789ef2dddcd9aef00476672026d16ccb4055
papers/27-positive-newton-translation-reciprocity/notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md	11229	231	644	1	4fdf61878bc78315f42d07b4a4d565d9fe154910c3fa50e49a4c234867b0dbed
papers/27-positive-newton-translation-reciprocity/notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md	17638	329	644	1	25a11a57b6852bae6b9d94fc5ca59fafe8e7033e026a4f6ef678ebdfe282f86f
papers/27-positive-newton-translation-reciprocity/notes/INDEPENDENT_SOURCE_LOCK_REVISION_REVIEW.md	5903	113	644	1	c909eaac0776eeebeef03fc2b8deca2f041a6cda3004da2d113470fa056ecfe5
papers/27-positive-newton-translation-reciprocity/notes/INDEPENDENT_SOURCE_REVIEW.md	8527	149	644	1	81b13099cd239306d1b3d1e197d44e01e4b1c49f5f5b1b3bf29c3f59e489335f
papers/27-positive-newton-translation-reciprocity/notes/INDEPENDENT_SOURCE_REVISION_REVIEW.md	5858	112	644	1	769c21cf8d6c9b42b044cd3546020ad1ea07b1e9fdcdb1e20bc2215f62f98309
papers/27-positive-newton-translation-reciprocity/notes/INDEPENDENT_TERMINAL_BLOCKER_REVIEW_R3.md	3940	76	644	1	20a81ab28c51c1acef5e563ef1beafdb37ac7c1bc4328c804cb910ce2c1679b0
papers/27-positive-newton-translation-reciprocity/notes/NOVELTY_ASSESSMENT.md	6040	81	644	1	16b97ac1e7df048e1eb2d05f69980064f8201cf56a878bbd496831d20eec647c
papers/27-positive-newton-translation-reciprocity/notes/PROOF_PACKAGE.md	19921	527	644	1	c583d2cedcd97bef8410172bed967dfe99bcaf9caa69595c305bbf36ccd51fd1
papers/27-positive-newton-translation-reciprocity/notes/PUBLICATION_LOCK.md	7996	148	644	1	7eb6ad779a00c4f56f4b5bea5fc56f22ebe55ee9b80af9924d18c70d4ff834aa
papers/27-positive-newton-translation-reciprocity/notes/PUBLICATION_SCOPE.md	7055	137	644	1	2651dd8df815872300c020f3c243a94115c9c38c80e9d1d00fc0052ec9f23a40
papers/27-positive-newton-translation-reciprocity/notes/RESEARCH_QUESTION.md	4908	126	644	1	73b094e1905f4a5af49c82f3b3bfa7a242125e56ff724dcf00c1c8bb1a0ea4cc
papers/27-positive-newton-translation-reciprocity/notes/SOURCE_LOCK.md	9328	177	644	1	ab63ffebbc62149daa0db70f4378cd59604c4c24c201b70036e96f831b9560c6
papers/27-positive-newton-translation-reciprocity/notes/SOURCE_LOCK_REVISION.md	3387	68	644	1	8afd2516173ab949a65bfab7e232c1040c10b897bcce9681e7418c04d0d93445
papers/27-positive-newton-translation-reciprocity/paper/main.tex	33811	829	644	1	ba9879a7084821b18c3e76166706d90d99bc4cb8e0bb1cb09d04a23f3a007f18
papers/27-positive-newton-translation-reciprocity/paper/math_commands.tex	601	17	644	1	34fdee026ed49adf9d7ad2d3b3c2d397549f29fd9f896fe5d54e046456e30957
papers/27-positive-newton-translation-reciprocity/paper/references.bib	6610	217	644	1	a77d814de144852c760c9c6e894ad92ea567dd03be188e2786662aaf7cb521e5
papers/27-positive-newton-translation-reciprocity/refine-logs/FINAL_PROPOSAL.md	5446	131	644	1	d2bd1a47959907efa35364e408ede645353059a47cb3641226f5d022605a71ae
papers/27-positive-newton-translation-reciprocity/refine-logs/INITIAL_PROPOSAL.md	3525	75	644	1	af290d3d3587d6824cbe1c892d3b11c8551113d63c5fe03c1f641967af75e3e6
papers/27-positive-newton-translation-reciprocity/refine-logs/REVIEW_SUMMARY.md	4064	76	644	1	3805351516268043f6a3a91c35dc6568428849ad8fbdde33fc9872eef06e7836
```

The first 44 rows are exactly the 12 inherited top-level source/control files
and the 32 closed-Paper27 source/control files.  Their canonical framing is
6,525 bytes and 44 LF, with SHA-256
`79a69e258fa14af3675ff1c9e41f07178d8c8ad9d4fd27efd53445589a426536`.
Adding only `BATCH_07_PAPER28_PRE_DISCOVERY_ACTION_REVIEW.md` produces 45
rows, 6,652 bytes, 45 LF, and SHA-256
`2410c7ecc1d6c5102afc3fe57d87baca71631d8ca7fecf33b4704d5c3e8df026`.
Adding only the current `BATCH_07_IDEA_REPORT.md` to that universe produces 46
rows, 6,758 bytes, 46 LF, and SHA-256
`a7a79b7f31171d1d2cac64b1f042d995ee9cff9442916919304a9d15db12e41d`.
All three recomputations exactly match E0164.

## Literal manifest discontinuity

E0114 records the then-current 35-row aggregate as 4,996 bytes.  E0115 records
the created `BUILD_PROFILE.md` as 6,122 bytes, 117 LF, mode `644`, link one,
and SHA-256
`704c2ddab2ae5b0628f96cecf43c9f96ca4b4238c61b30b23d1070d9c0299037`.
Under the declared framing, that exact row is 153 bytes.  The correct additive
framing is therefore `4996 + 153 = 5149`, whereas E0115 records 5,150.  This is
the first visible framing divergence.

The bad identity propagates.  E0155 records a 44-row closed-Paper27 manifest as
6,526 bytes with SHA-256
`9d3e117b737689320bd54d9d156e2186ad784d00b31d5ec68963e775cfa310d7`;
the exact live 44-row identity is instead 6,525 bytes with SHA-256
`79a69e258fa14af3675ff1c9e41f07178d8c8ad9d4fd27efd53445589a426536`.
E0156 through E0158 carry the noncanonical identity.  E0159 still names it as
its `pre_manifest_sha256`, so E0159 is not retrospectively valid.  Its post,
however, is the exact independently recomputed 45-row live universe: 6,652
bytes and
`2410c7ecc1d6c5102afc3fe57d87baca71631d8ca7fecf33b4704d5c3e8df026`.
That exact post is a restoration of present byte identity, not a cure for the
invalid preimage.

E0162 later duplicated a substring in its `post_manifest_sha256`; E0163 names
that exact malformed literal, records that no action was taken under it, and
supplies the canonical 64-hex V1 manifest identity.  That narrow field
correction is disclosed.  It does not cure or validate the earlier E0115--E0159
manifest/preimage discontinuity.

## Historical path actions and their effects

E0156/E0157 disclose the literal command `test ! -e papers/28-*`.  It was a
prohibited future-path glob test and remains one immutable historical
action-history Blocker.  The shell pattern matched no path.  The recorded
effect is no file opened, created, read, modified, deleted, or linked; no Paper
28 number or project authority consumed; and no source, build, release, or
external effect.  I did not repeat the test.

E0164 also discloses two exact closed-Paper27 `read_bytes` attempts, at
`papers/27-positive-newton-translation-reciprocity/PUBLICATION_SCOPE.md` and
`papers/27-positive-newton-translation-reciprocity/notes/INDEPENDENT_TERMINAL_BLOCKER_REVIEW.md`.
Each literal historical spelling returned ENOENT before any descriptor or data
was obtained.  Neither string is a future Paper28 path.  The recorded effect is
no successful open, read, write, creation, modification, deletion, or link and
no paper-number, project, build, release, or external effect.  I did not touch,
stat, hash, open, or otherwise probe either spelling.

These three incidents remain carried history.  Their no-open/no-write effects
do not consume Paper 28 and do not by themselves forbid a fresh prospective
transition under the exact-path firewall; they cannot be erased or described
as a clean history.

## V1 failure, V2 append-only identity, and quarantine

The controlled ledger records two fresh V1 formal verdicts, both
`FAIL_WRITE_NOTHING`.  R1 recorded one Major, one Minor, and one Ambiguity; R2
recorded one Major and one Minor.  Both `r1_artifact_created` and
`r2_artifact_created` are false, E0163 records `dual_artifacts_created: false`,
and neither failed review consumed Paper 28 or created a project.

The first 32,149 bytes and 852 LF of the current idea report independently
recompute to SHA-256
`89c1544ebf78c1e55348e4e5f685a78e5fef712324e0e42a7e7508336ec947c5`
and end in the exact V1 corrected author-stop line.  Thus the V1 report is
byte-for-byte preserved and the V2 packet is a physical append.  The current
43,462-byte identity and unique V2 terminal marker match E0164.  E0164
explicitly sets `v2_formal_reviews_authorized: false`; no V2 review artifact,
Paper28 project, source, build, release, scientific execution, or external
effect is recorded.  The V2 packet is present but remains quarantined.

## Immutable history and strictly prospective recovery

The charter requires physical EOF appends bound to the parent hash and byte
offset, keeps historical events immutable, and says an invalid manifest opens
no transition authority.  It also permits an explicit append-only disposition
and a fresh distinct retry, and requires exact errors and canonical
replacements to be named before malformed fields become historical and
non-authoritative.  Therefore this review does not declare E0115--E0159 valid,
does not backfill the one-byte framing error, and does not use E0159's exact
post to validate its bad preimage.  Downstream descriptions of actual bytes
and actions may be retained as evidence, but they cannot bootstrap authority
from the malformed chain.

A bounded recovery is nevertheless permissible prospectively.  E0164 freezes
the defects, exact current 46-row universe, no-effect actions, unconsumed
number, absent project, and quarantined V2 packet, and authorizes only this
fresh review.  A new physical-EOF event may adopt that exact present state plus
this report as a new, review-backed starting boundary.  Such an event validates
only future authority from its own correct parent and manifest bindings.  It
does not pronounce the earlier actions authorized when taken and does not
repair, erase, or reclassify the malformed or prohibited history.

## Historical carried findings and current census

The following are historical/action findings carried without erasure:

1. the E0115-through-E0159 manifest/preimage discontinuity;
2. the E0156 prohibited future-glob probe, historically classified Blocker;
3. the first disclosed closed-Paper27 ENOENT open attempt; and
4. the second disclosed closed-Paper27 ENOENT open attempt.

Under the prospective conditions stated in this review, the independent
current census is:

| Current category | Count |
|---|---:|
| New Blocker | 0 |
| New Major | 0 |
| New Minor | 0 |
| New Ambiguity | 0 |
| Unresolved live-manifest mismatch | 0 |
| Unresolved disclosure or action-effect mismatch | 0 |
| New future/project/build-path touch | 0 |
| Paper28 number/project consumption | 0 |
| New filesystem or external effect outside this report | 0 |

The all-zero current census is conditional on immutable historical disclosure
and the exact next boundary below.  It is not an all-clean-history claim.

## Decisive disposition and exact next gate

PASS: every live identity and framing recomputes exactly, E0164's parent and
candidate bindings are exact, the disclosed incidents caused no successful
file read or write and consumed no Paper28 authority, V1 failed without review
artifacts, and V2 remains append-only and quarantined.  The charter permits a
new bounded prospective recovery but forbids retroactive validation.

The next action must be exactly one new physical-EOF ledger event.  It must:

1. consume this review by its exact verified bytes, LF, mode, link count,
   SHA-256, and terminal marker;
2. bind the canonical 47-row source/control universe consisting of the exact
   46 rows above plus this review's row, with `BATCH_07_STATUS.md` self-excluded;
3. preserve E0115--E0159, E0156, and both ENOENT attempts as immutable,
   non-authoritative/carried history and state explicitly that no retroactive
   validation is made;
4. authorize only two new, fresh, mutually blind V2 formal reviewers, neither
   reused from V1, with exact PASS-only artifact paths
   `BATCH_07_PAPER28_CANDIDATE_V2_REVIEW_R1.md` and
   `BATCH_07_PAPER28_CANDIDATE_V2_REVIEW_R2.md`; and
5. keep the Paper28 number unconsumed and its project absent, and authorize no
   project, source, build, release, scientific execution, external effect, or
   other write.

No V2 formal-review authority exists before that exact consumption event.

BATCH07_PAPER28_V2_PRE_REVIEW_MANIFEST_ACTION_HISTORY_REVIEW_PASS
