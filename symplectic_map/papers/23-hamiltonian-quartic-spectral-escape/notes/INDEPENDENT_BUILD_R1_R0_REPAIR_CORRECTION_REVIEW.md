# Paper 23 — Independent corrected-R0 Build R1 review

Review date: 2026-08-25 UTC

## 1. Decision, independence, and exact meaning of this PASS

I performed a wholly new corrected-R0 Build R1 audit from zero. I did not
author or build the source, the R0 artifacts, either immutable original JSON
record, the build-evidence correction, the overlay review, any lock, any
governance root, or any earlier Paper 23 review. I treated every builder,
author, prior reviewer, and parent statement as an unproved pointer to
evidence. Every acceptance finding below comes from my own reads, hashes,
parsers, algebra, log inspection, PDF inspection, and fresh visual render.

The recovered effective evidence conjunction and my direct audit support
accepting the existing corrected R0 outputs now. In particular, the frozen
source trio builds reproducibly in the two permitted roots, the retained
outputs are byte-identical and clean, the visible PDF is complete and
anonymous, and the headline mathematical claims agree with independent exact
calculation.

This is deliberately not a retrospective certification of the old build
contract. The immutable BUILD_RECEIPT_R0.json status BUILD_R0_REPAIR_PASS and
its original acceptance fields remain historical, suspended, and noncredited.
The two erroneous executable digests were not semantically validated before
persistence, so the old requirement that every hard conjunct pass before a
success path existed was not met. Neither this review nor the append-only
correction makes that historical timing statement true. This review accepts
the already retained outputs only under the prospective recovered conjunction:

1. the immutable original metadata and receipt, excluding their suspended
   semantic claims and reading their four executable-digest fields through
   the correction precedence map;
2. R0_BUILD_EVIDENCE_CORRECTION.md and the strict-canonical
   BUILD_EVIDENCE_CORRECTION_R0.json overlay;
3. INDEPENDENT_R0_BUILD_EVIDENCE_CORRECTION_REVIEW.md; and
4. this fresh direct audit of the source, build roots, executables, commands,
   logs, outputs, manuscript, proof, citations, PDF structure, fonts,
   security, anonymity, and all 23 rendered pages.

No compilation, retry, source edit, output replacement, cleanup, release,
Paper 24 work, submission, upload, contact, network action, or other external
effect was performed. The only project write authorized on a complete pass is
this review.

## 2. Live governance and access boundary

I read all three current governance roots completely through EOF and
reproduced these exact identities immediately before the write:

| Root | SHA-256 | Bytes | LF | Mode / owner / links |
|---|---|---:|---:|---|
| BATCH_06_STATUS.md | fa9675a79a01d61337a7f9bbbd45643c83c2881e084d8c0be6961277da7a4346 | 99,686 | 1,463 | 0644 / root:root / 1 |
| BATCH_06_IDEA_REPORT.md | 20851c6689a761a82a48985c30f536d197b63c44af9c720e5d545d72b9403eba | 162,519 | 3,052 | 0644 / root:root / 1 |
| BATCH_06_PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTION.md | 27615c425261aa72caa4c880b6bc7f54ecfa98c99399a2d7efc78ed19d8282c4 | 8,524 | 245 | 0644 / root:root / 1 |

The live gate is exactly PAPER23_CORRECTED_R0_BUILD_R1_REVIEW_OPEN and the
queue is exactly CORRECTED_R0_BUILD_R1_REVIEW_OPEN. The roots authorize only
this one independent review path after every conjunct passes. They keep source
revision, R1 authorization or build, finalization, release, Paper 24, and all
external effects closed.

I read all 44 opening project files completely. Text records were decoded and
read through EOF; the PDFs and other binary objects were read bytewise and
then inspected with independent structural and rendering paths. I read and
rehash-checked every file in the two permitted live roots:

- /tmp/paper23-r0-repair-correction-A.Er2f85
- /tmp/paper23-r0-repair-correction-B.tcCPcQ

I also audited the parent-resolved read-only validator base
/tmp/paper23-evidence-correction-author-stage.Wi0tmI. I did not access, list,
stat, glob through, or touch any excluded earlier build root. Names of
excluded roots encountered inside already authorized project or governance
records were treated only as text.

For independent parsing, algebra, structural checks, contact sheets, and
rendering, I created the project-external private scratch
/tmp/paper23-build-r1-independent.NGbqVj. It is a root-owned mode-0700
directory on device 149, inode 4833888855. No author render evidence was
reused.

## 3. Complete opening project universe

At opening and again at final read-only prewrite stability check, the project
contained exactly 44 ordinary regular files, four child directories, zero
symlinks, and zero other objects. The target review path was absent under an
lstat/no-follow check. The four child directories experiments, notes, paper,
and refine-logs were root-owned mode 0755 directories on device 2431. The
project root was device/inode 2431/5374559700; the child directory inodes were
5913543618, 6443323387, 3227277694, and 6980649940 respectively.

The complete opening regular-file manifest below is sorted by relative-path
UTF-8 bytes. Its fields are path, SHA-256, bytes, LF count, mode, owner,
device, inode, and link count. It is 6,117 bytes and 44 LF, has SHA-256
fb3ed0099966e8ecf9f413ad9c5ad705792f99a0d5505919692c8076abf7df03,
and binds 1,887,425 regular-file bytes.

    experiments/EXPERIMENT_PLAN.md	b37132e282cceeb04a36723d75f48c4af6f3361836067850496cf52b8ad603e8	6015	151	644	root:root	2431	5913543619	1
    experiments/EXPERIMENT_TRACKER.md	85724a53e161bfbbb45af305af66454a757771330157694ff5d7f85215ffcb31	2927	55	644	root:root	2431	5913543620	1
    experiments/publication_lock.json	6f1830f14413c49cad0945facc7b10c081be1a36d4884e5768205273fce200c4	51578	1	644	root:root	2431	5913543623	1
    experiments/source_lock.json	5956a7e6c2e12a9be287b2ead2922e135c4a64da738757a0b55884e16974b248	32889	1	644	root:root	2431	5913543616	1
    notes/BUILD_AUTHORIZATION_R0_REPAIR.md	d2af138c12d3abc59dce9d7950a7e53113e2b1f8c1b312a1d4803c3b5cc8d207	25966	428	644	root:root	2431	6443708207	1
    notes/BUILD_AUTHORIZATION_R0_REPAIR_CORRECTION.md	0bddcd479cb82406888de2ca837f7e5c39ba5b6b2acbd12b365971f50aa5e48e	31040	491	644	root:root	2431	6443704696	1
    notes/BUILD_R0_BLOCKER.md	8d395e7fdeb2103370b1b1700c1bd54301f0f1206c5a3eea4352298cdd1c5384	8900	180	644	root:root	2431	6443678303	1
    notes/BUILD_R0_REPAIR_BLOCKER.md	c05d9bb243bd28cd43dee4972f5ee829d01b165b73e7b9bef25a8c4f6940f472	11493	223	644	root:root	2431	6443708204	1
    notes/CITATION_VERIFICATION.md	fcf71a2364fe6b1624ac99189dd61a6655551928989a75bd2b338cea3d059da6	7269	90	644	root:root	2431	6443323389	1
    notes/CLAIMS_EVIDENCE_MATRIX.md	e3d6165b7429880cbe4407c6918ce25d6d8872ee05a48dfe457b5559f4df48c6	7107	123	644	root:root	2431	6443323390	1
    notes/INDEPENDENT_BUILD_AUTHORIZATION_R0_REPAIR_CORRECTION_REVIEW.md	b34e35c7877870b40354d66b59ec7f816010a2470bc863b34f730e548a01ba53	15505	235	644	root:root	2431	6443678300	1
    notes/INDEPENDENT_PAPER_PLAN_REVIEW.md	d491d6fa2fe3ca0d5b03195006f86021f65f6cf56529f592b46730086504b2d9	22954	651	644	root:root	2431	6443323789	1
    notes/INDEPENDENT_PAPER_SOURCE_R1_R0_REPAIR_REVIEW.md	b8c62343aa9d893d9dcc0bf73e24755d92833c294c4f4a790cd1238c886f2636	21240	465	644	root:root	2431	6443678298	1
    notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md	aad55320dc0645931be2c0019327cd4255aaa56d77f94cd48e1a3702b10fb9bb	30329	785	644	root:root	2431	6443658252	1
    notes/INDEPENDENT_PAPER_SOURCE_R2_R0_REPAIR_REVIEW.md	075b9b6e7cc271f8abec29b08d28509df5ce7c8b6e0951753051d14a6b36c653	21535	425	644	root:root	2431	6443678301	1
    notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md	0ecfdc71a2de08e37311cb4683e393e397bb8e87854b01eb021a7db7f4d46dec	23481	633	644	root:root	2431	6443323778	1
    notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md	8711ba1e5e6daaef5c008f773cd5a5a0751eb1794b8595befc4c8bd5e4df88fb	15589	483	644	root:root	2431	6443334570	1
    notes/INDEPENDENT_R0_BUILD_EVIDENCE_CORRECTION_REVIEW.md	489148a4246c04c4b1f3b403f6baa8ef7ad6639d803059858c4426f62847fa00	22861	407	644	root:root	2431	6443784811	1
    notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md	c6ae173c45d0e8fbe073395abf366a33e3f4b24bf97c1ab97ad39cdb245e356e	17851	441	644	root:root	2431	6443323385	1
    notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md	8828364af81e829ee13201e5e8c63b1b92cb33df462c598ec3b615057545ec8c	23668	586	644	root:root	2431	6443323386	1
    notes/NOVELTY_ASSESSMENT.md	3ba35e3a336360e22f054c4821801c9b55e61dd4e9bc50e6aa57150dbca59dca	6992	141	644	root:root	2431	6443323391	1
    notes/PROOF_PACKAGE.md	0d0ffb5a7d540c987d37a93ec38c7a7736ac8445f6a82c5096e471ebcc34c040	24560	1184	644	root:root	2431	6443323776	1
    notes/PUBLICATION_STAGE_SCOPE.md	fa0aef81669da75eacbe604614d86ae4a18610ef2ce70ba58391a47657f29b31	44575	1269	644	root:root	2431	6443323790	1
    notes/R0_BUILD_EVIDENCE_CORRECTION.md	89e56bf502a2d40ecb831991b4d5edd5e2672fcd3c1f9149d6edb2222a8f5b01	31005	426	644	root:root	2431	6443469984	1
    notes/R0_HYPERREF_SOURCE_REPAIR.md	a0fe52acf07aed30dc8571b86a48602e74dc7cd15105ea4d69cd701f2e80bbe4	15841	222	644	root:root	2431	6443678299	1
    notes/RESEARCH_QUESTION.md	3cd1e22973e443c47a1672a82431c14c3b86ceba685330234d19085e65acdb5c	5492	135	644	root:root	2431	6443323388	1
    notes/SOURCE_R1_ABSTRACT_INTEGER_REPAIR.md	f5bea1184027da2afe9c1cc6810c000b72fb058cc6cb527a30222866b521ef3b	8168	136	644	root:root	2431	6443457781	1
    paper/BUILD_EVIDENCE_CORRECTION_R0.json	257d37600e9c7498b3e801d08fce3391d6852c5ce34ba1d468c502e357de7bfd	41366	1	644	root:root	2431	3227387381	1
    paper/BUILD_METADATA_R0.json	599a8c3e1578e79fee6dff197d0cd8d3bcb3cb06ab13ebd4b8e1c975ec951362	70889	1	644	root:root	2431	3227322490	1
    paper/BUILD_RECEIPT_R0.json	70ad2b65c82201981488c5bcc4685f08f37529504082afb7e1778248c96cd590	71124	1	644	root:root	2431	3227322494	1
    paper/PAPER_PLAN.md	fa7e5a7ea6693b0d8ef10651da317d253f5a1ba199e3b026a3b92c8104b6c974	44881	799	644	root:root	2431	3227277695	1
    paper/main.aux	2748935c255778a4e40227c008adeb8c361a3933a9ff5f545407f04ae48c8eeb	14072	165	644	root:root	2431	3227322495	1
    paper/main.bbl	baa229dd7d35d96b27d7dfb18a844db73c98b752df3be4c008d748636f199cf9	2881	73	644	root:root	2431	3227332992	1
    paper/main.blg	be7e80a71c65ef8bbfcc2e43c3aadcc0b89cb8216e61a785ca24403ec6c04c34	900	46	644	root:root	2431	3227332993	1
    paper/main.log	ab451da731a6ef13c7f1f83e9de463b4b2d71b0cb255e10b2d831a235aaa13f6	27628	700	644	root:root	2431	3227332994	1
    paper/main.out	14be6d78b541eb75e29cec5bf18d1e9a26bfb0c128ddaa5f4c26ab00d315bb94	6226	28	644	root:root	2431	3227332995	1
    paper/main.pdf	ae37679ef3ee4fa0b86f41e073f374920499f4959a196e289829e654b3d12d37	492452	2724	644	root:root	2431	3227332996	1
    paper/main.tex	1ac57197ff87b2c1c6ec2cea7cf644021e629e519e4215d4b32e9e4420aa46b0	67408	1776	644	root:root	2431	3227298198	1
    paper/main_round0.pdf	ae37679ef3ee4fa0b86f41e073f374920499f4959a196e289829e654b3d12d37	492452	2724	644	root:root	2431	3227332997	1
    paper/math_commands.tex	a69565204428ce95abbcab5afb3833290004110e2718c074fbc805f7d1bdcb0d	420	13	644	root:root	2431	3227298196	1
    paper/references.bib	ba0156abd7eb399de532b9bc1eefa81b3bb1be7868eed6ee4b42f8cd3371c782	2812	99	644	root:root	2431	3227298197	1
    refine-logs/FINAL_PROPOSAL.md	aa1221ef198ed1fe8c21da2e24107efb5671cc0f4fb70a7cd657a21c73e1f47b	5531	185	644	root:root	2431	6980649942	1
    refine-logs/INITIAL_PROPOSAL.md	485fd5b98e69338aae9a681548ac906e698d98adcd3af8dbf9e42622df9471b4	5158	146	644	root:root	2431	6980649941	1
    refine-logs/REVIEW_SUMMARY.md	c02b85e92727134a2cd65789c4034bbef7c047811d3e03314c9e598e5a054bf3	4395	101	644	root:root	2431	6980649943	1

Every opening regular file was root-owned mode 0644 and link count one. The
complete manifest digest and all 44 rows reproduced unchanged at final
prewrite stability check.

## 4. Independent reconstruction of the corrected evidence

The three one-line JSON objects have these immutable identities:

| Object | SHA-256 | Bytes / LF | Integer tokens | Absolute value above 2^53 |
|---|---|---:|---:|---:|
| BUILD_METADATA_R0.json | 599a8c3e1578e79fee6dff197d0cd8d3bcb3cb06ab13ebd4b8e1c975ec951362 | 70,889 / 1 | 1,446 | 0 |
| BUILD_RECEIPT_R0.json | 70ad2b65c82201981488c5bcc4685f08f37529504082afb7e1778248c96cd590 | 71,124 / 1 | 1,451 | 0 |
| BUILD_EVIDENCE_CORRECTION_R0.json | 257d37600e9c7498b3e801d08fce3391d6852c5ce34ba1d468c502e357de7bfd | 41,366 / 1 | 519 | 42 |

I wrote two new validators in the private scratch. The Python path uses a
duplicate-aware object-pairs hook, integer-only hooks, arbitrary-precision
integers, Unicode-scalar validation, Unicode-code-point key order, and its own
recursive encoder. It byte-round-tripped all three objects, rejected 33
adversarial cases, and accepted four valid controls. The Node path is a
handwritten recursive-descent parser with explicit duplicate rejection,
BigInt integers, surrogate checks, Unicode-code-point ordering, and an
independent encoder. It also byte-round-tripped all three objects, rejected
32 adversarial cases, and accepted four controls. The cases collectively
cover duplicate and escape-equivalent keys, nested and astral key order,
fractions, exponents, nonfinite forms, leading zero, negative zero, BOM,
invalid UTF-8, CRLF, missing or extra LF, NUL and raw controls, trailing
whitespace and records, noncanonical escapes, malformed surrogates, and
trailing commas.

As a separate check, I read both retained author validators fully and ran
each on each of the three JSON objects. All six executions round-tripped the
input bytes exactly; every execution rejected all 22 author adversarial cases
and accepted its control. The five-file validator-base nine-field manifest is
659 bytes and five LF with SHA-256
21f25dcbdc32c8a6e42017b5a0286d0b9a67475e529cf473241d1586100b5825.
Author code is corroboration only, not the basis of my result.

I independently resolved every RFC 6901 pointer. There are exactly four
unique factual corrections and no other corrected pointer:

| Target | Pointer | Immutable erroneous value | Correct observed value |
|---|---|---|---|
| paper/BUILD_METADATA_R0.json | /build/executable_identities/bibtex/sha256 | c9ecb7182f287007d277d67a1537a721493f2d3b0c98d16006ba24493710618f | c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f |
| paper/BUILD_METADATA_R0.json | /build/executable_identities/pdflatex/sha256 | 01a7ab54dd9ca121cc8694f3bb656633682f2e2fd5fba6f9adcd8a9508336cf9 | 01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9 |
| paper/BUILD_RECEIPT_R0.json | /build/executable_identities/bibtex/sha256 | c9ecb7182f287007d277d67a1537a721493f2d3b0c98d16006ba24493710618f | c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f |
| paper/BUILD_RECEIPT_R0.json | /build/executable_identities/pdflatex/sha256 | 01a7ab54dd9ca121cc8694f3bb656633682f2e2fd5fba6f9adcd8a9508336cf9 | 01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9 |

The overlay states corrections.count = 4,
other_factual_pointers_corrected = 0, and
materialized_patched_json_pair = false; the value tree and the originals
agree with those statements. The original metadata and receipt value trees
differ only at /companion_candidate, /record_kind, and /status.

Exactly four semantic pointers in each immutable original are suspended,
for eight pointer/document pairs:

- /acceptance/all_hard_conjuncts_pass
- /acceptance/blocker
- /acceptance/chosen_outcome
- /checks/success_paths_absent_before_complete_validation

Exactly four validation statements in each original, again eight
pointer/document pairs, remain usable only in the narrow namespace
immutable_original_erroneous_candidate_syntax_canonical_bytes:

- /json_validation/candidate_hashes_recorded_before_persistence
- /json_validation/candidate_round_trips_exact
- /json_validation/two_value_trees_agree
- /json_validation/validation_completed_before_persistence

They prove syntax, canonicality, original candidate equality, and physical
history only. They do not prove the erroneous executable facts, semantic
acceptance, the later overlay, or any hypothetical patched JSON.

I independently applied only the four allowed replacements in memory and
re-encoded canonically. The unauthorized virtual metadata is 70,889 bytes,
SHA-256
9a1864be2795df47a3f82855f2b1aef2aa51424809c7550767c466a7fc9a4493.
The unauthorized four-pointer virtual receipt is 71,124 bytes, SHA-256
d675ef6aeca693c732f4f39601f5b68592f7dda2cab4ca7bf2bc956346397a15.
Changing its companion hash would be an unauthorized fifth pointer and gives
the distinct virtual receipt SHA-256
3b6b6343dd1d07aa6106f07e9c61ee451cc8c4e74f0ad918d1d086fb11e5b67c.
None was written or treated as evidence.

The original receipt PASS, original all-hard-conjunct fields, and
old-contract compliance therefore remain denied. The correction is an
append-only semantic precedence map, not a repaired historical candidate.

## 5. Exact executables and causal defect

I streamed both resolved executable objects independently through Python
SHA-256, GNU sha256sum, and OpenSSL dgst. All three routes agreed:

| Resolved executable | SHA-256 | Bytes / LF | Device / inode | Mode / owner / links |
|---|---|---:|---:|---|
| /usr/bin/pdftex | 01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9 | 1,802,504 / 4,629 | 149 / 3829692913 | 0755 / root:root / 1 |
| /usr/bin/bibtex.original | c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f | 117,128 / 393 | 149 / 3829692848 | 0755 / root:root / 1 |

/usr/bin/pdflatex resolves to /usr/bin/pdftex and /usr/bin/bibtex resolves to
/usr/bin/bibtex.original. Their full stat identities and nanosecond
timestamps match the overlay. Their births and ctimes are respectively
2026-07-30 02:12:41.969305619 UTC and
2026-07-30 02:12:41.961305260 UTC; both mtimes are
2026-01-27 17:36:46 UTC.

I read the retained A-root generator completely. Its physical lines 384 and
385 contain exactly the two obsolete digest literals. The common value tree
was then deep-copied into metadata and receipt and canonically serialized.
The validators checked grammar and round trips but did not hash the named
executables. This independently supports the narrow diagnosis: a static
literal transcription defect propagated faithfully; neither executable
replacement, compiler malfunction, JSON corruption, copy failure, nor a
filesystem swap is needed to explain the evidence.

## 6. Permitted A/B roots and the exact four-command build

The permitted roots remained private, root-owned directories:

| Root | Mode | Device / inode / links | Regular files / child dirs / symlinks / other | Regular bytes | Complete nine-field manifest |
|---|---|---|---|---:|---|
| /tmp/paper23-r0-repair-correction-A.Er2f85 | 0700 | 149 / 6443678302 / 3 | 43 / 1 / 0 / 0 | 8,637,740 | 5,655 bytes, 43 LF, SHA-256 415f5d1d47828a25154f2dea5423d8259cdd40b3085a3b4c4d2140607f237b38 |
| /tmp/paper23-r0-repair-correction-B.tcCPcQ | 0700 | 149 / 6981323841 / 2 | 13 / 0 / 0 / 0 | 648,698 | 1,515 bytes, 13 LF, SHA-256 1d0e5a4a101f148a449dac5bd5499c5bf87daccb995ea27b42cf84eb7129a067 |

Root A's sole validation-pages directory is mode 0700, root-owned, device
149, inode 10739810258, link count two. I read every source, log, output,
staged JSON, validation script, validation result, manifest, root stat,
command transcript, and A/B comparator in the permitted roots.

The source trio, four command logs, and six outputs form the 13 common A/B
pairs below. Every pair is byte-identical:

| Artifact | SHA-256 | Bytes / LF | A inode | B inode |
|---|---|---:|---:|---:|
| main.tex | 1ac57197ff87b2c1c6ec2cea7cf644021e629e519e4215d4b32e9e4420aa46b0 | 67,408 / 1,776 | 6443704693 | 6981323845 |
| math_commands.tex | a69565204428ce95abbcab5afb3833290004110e2718c074fbc805f7d1bdcb0d | 420 / 13 | 6443704694 | 6981323850 |
| references.bib | ba0156abd7eb399de532b9bc1eefa81b3bb1be7868eed6ee4b42f8cd3371c782 | 2,812 / 99 | 6443704695 | 6981323851 |
| command-1.log | 1fcbc0319012bbeb4fd526dad9eef6a0ca9e86474e9c092ae766a70a4ef466ce | 18,124 / 597 | 6443704697 | 6981323852 |
| command-2.log | 7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9 | 158 / 4 | 6443704702 | 6981323857 |
| command-3.log | cba30ead0e25a854366d5bf7e9156ffadfb713fd4de7097a43b6f284e1d2db72 | 8,363 / 158 | 6443708172 | 6981323860 |
| command-4.log | ad3eb1bf23dd06e82b1683ccb3e66c34b142303fa24685f56f268f58368612b0 | 7,254 / 112 | 6443708173 | 6981323864 |
| main.aux | 2748935c255778a4e40227c008adeb8c361a3933a9ff5f545407f04ae48c8eeb | 14,072 / 165 | 6443704699 | 6981323854 |
| main.bbl | baa229dd7d35d96b27d7dfb18a844db73c98b752df3be4c008d748636f199cf9 | 2,881 / 73 | 6443708171 | 6981323859 |
| main.blg | be7e80a71c65ef8bbfcc2e43c3aadcc0b89cb8216e61a785ca24403ec6c04c34 | 900 / 46 | 6443704703 | 6981323858 |
| main.log | ab451da731a6ef13c7f1f83e9de463b4b2d71b0cb255e10b2d831a235aaa13f6 | 27,628 / 700 | 6443704698 | 6981323853 |
| main.out | 14be6d78b541eb75e29cec5bf18d1e9a26bfb0c128ddaa5f4c26ab00d315bb94 | 6,226 / 28 | 6443704700 | 6981323855 |
| main.pdf | ae37679ef3ee4fa0b86f41e073f374920499f4959a196e289829e654b3d12d37 | 492,452 / 2,724 | 6443704701 | 6981323856 |

The project source trio is byte-identical to both roots. Project main.aux,
main.bbl, main.blg, main.log, main.out, main.pdf, main_round0.pdf,
BUILD_METADATA_R0.json, and BUILD_RECEIPT_R0.json are byte-identical to their
staged A-root counterparts; project main.pdf and main_round0.pdf are directly
byte-identical.

Both value trees prescribe the exact six-variable environment:

- PATH=/usr/bin:/bin
- SOURCE_DATE_EPOCH=1787616000
- FORCE_SOURCE_DATE=1
- TZ=UTC
- LC_ALL=C
- LANG=C

They prescribe, and both transcripts show exactly once per root, this exact
sequence:

1. pdflatex -interaction=nonstopmode -halt-on-error main.tex
2. bibtex main
3. pdflatex -interaction=nonstopmode -halt-on-error main.tex
4. pdflatex -interaction=nonstopmode -halt-on-error main.tex

Both exit vectors are [0,0,0,0]. There is no retry, fifth pass, intervening
edit, or network use, and no fifth command log. I did not rerun this build.

## 7. Logs, bibliography, labels, and semantic build closure

I read every command log, final log, AUX, BBL, BLG, and OUT file completely.
The diagnostic progression is internally coherent:

| Pass | LaTeX warnings | Package warnings | Meaning |
|---|---:|---:|---|
| command 1 | 118 | 11 | first-pass reference/citation/outline convergence |
| command 2 | 0 | 0 | BibTeX completed cleanly |
| command 3 | 0 | 11 | citation convergence before the final LaTeX pass |
| command 4 | 0 | 0 | fully converged |

The first pass has 116 individual undefined-reference warnings plus the two
standard undefined-reference/rerun summaries. Its package warnings are the
nine initially undefined citations, the natbib summary, and the expected
outline-rerun warning. The third pass package warnings are the nine citations
plus the natbib undefined/changed summaries before final convergence. No pass
contains a fatal line, compiler error, overfull or underfull box, or hyperref
warning.

The retained 700-line final main.log has zero fatal/error, LaTeX warning,
package warning, undefined citation, undefined reference, rerun request,
changed-label, multiply-defined-label, overfull box, underfull box, or
hyperref finding. main.blg reports nine entries and warning count zero.

The final AUX has nine citation commands, nine bibcite entries, 95 newlabel
entries, bibliography style plainnat, and database references. The BBL has
nine bibliography items. The OUT has exactly 28 repaired bookmark lines,
including one clean subsection.8.3 record and no raw math dollar sign or
texorpdfstring leakage.

Independent source closure found 95 unique labels and 116 references, all
defined; nine citation commands with nine distinct keys; exactly nine BibTeX
records, comprising eight article entries and one misc entry, with exact key
equality. It found nine sections, 19 subsections, three tables, 72 equation
environments, 16 aligned environments, no figure, no appendix, and no
placeholder. A detex-style count gives 6,647 manuscript words. The abstract
interior has exactly 197 words.

The nine citation keys are BlancVanSantenAffineTriangular,
ShaoSunDimensionFour, HenonOpenProblems, BergerTuraevHamiltonianMaps,
ForstnericComplexSymplectic, KochLomeliStraightLineFlows,
RangarajanPolynomialSymplectic, DesertiDegreeGrowthExamples, and
DangFavreSpectralInterpretations. Their metadata matches references.bib and
the bounded citation ledger. Related work uses them only for general
dynamical-degree, affine-triangular, Hénon, symplectic-shear, and Hamiltonian
context. The manuscript explicitly denies a proof transfer: its selectors,
six walls, two carries, survival, visibility, principal minors, and
finite-field factor exclusion are local. It also denies firstness, priority,
generality, and newness of Perron numbers as a class. I found no citation
scope overstatement.

## 8. Independent manuscript and mathematical audit

I read main.tex, math_commands.tex, references.bib, PAPER_PLAN.md,
PROOF_PACKAGE.md, CLAIMS_EVIDENCE_MATRIX.md, CITATION_VERIFICATION.md,
PUBLICATION_STAGE_SCOPE.md, both canonical locks, the full independent review
chain, and every limitation and anti-claim. The visible PDF follows the
source. The title is exactly Four-Mode Hamiltonian Product Shears Beyond Cubic
Collapse: Exact Degree Growth and Quartic Perron Subfamilies.

The fixed family is over an arbitrary characteristic-zero field K, with
integer g at least 10:

    V_g = q1^2 q2^2 q3^2 q4^2 + q1^g + q2^(g-1)
    W_g = p1^2 p2^2 p3^2 p4^2 + p3^(g-1) + p4^g
    S_g^+(q,p) = (q, p + grad V_g(q))
    T_g^+(q,p) = (q + grad W_g(p), p)
    F_g = T_g^+ composed with S_g^+.

The direct Hessian-block calculation proves both gradient shears and their
composition preserve the standard symplectic form. The subtraction shears
are explicit polynomial inverses.

The selected phase matrices and their product are exactly

    A_g = [ g-1   0    0    0 ]
          [  0   g-2   0    0 ]
          [  2    2    1    2 ]
          [  2    2    2    1 ]

    B_g = [ 1    2    2    2   ]
          [ 2    1    2    2   ]
          [ 0    0   g-2   0   ]
          [ 0    0    0   g-1  ]

    C_g = B_g A_g
        = [ g+7   2g+4    6      6   ]
          [ 2g+6  g+6     6      6   ]
          [ 2g-4  2g-4   g-2    2g-4 ]
          [ 2g-2  2g-2   2g-2   g-1  ].

My own exact integer-polynomial engine reproduced C_g = B_g A_g, the phase
seeds

    A_g 1 = (g-1, g-2, 7, 7)^T
    C_g 1 = (3g+23, 3g+24, 7g-14, 7g-7)^T,

and every downstream symbolic identity without a computer-algebra-system
oracle.

The sufficient ratio cone is exactly

    K_g = {u1(1,x,y,z)^T:
           u1>0,
           1 <= x <= a_g,
           1 <= y <= z <= a_g y,
           y+z < H_g},
    a_g = (g-1)/(g-2),    H_g = (g-5)/2.

The four phase-correct selector gaps are

    S1 = (g-2) - 2x - 2y - 2z
    S2 = (g-3)x - 2 - 2y - 2z
    T3 = -8 - 6x + (g-7)y + (2g-8)z
    T4 = -6 - 4x + (2g-6)y + (g-6)z.

The first two are strict from x <= a_g and y+z < H_g. The second-phase gaps
are correctly evaluated after the first phase at A_g u; using x <= a_g <=
9/8 and y,z >= 1 gives the displayed strict lower bounds. At g=10 the four
ordinary-seed margins are (2,1,1,8).

Writing C_g u/u1 = (D,N2,N3,N4)^T, I re-expanded all four numerators and
checked all six cone walls with the exact required weak or strict sign:

| Target wall | Exact certificate |
|---|---|
| X' >= 1 | N2-D = (g-1)-(g-2)x >= 0 |
| X' < a_g | (g-1)D-(g-2)N2 >= 2g+25 > 0 |
| Y' > 1 | N3-D >= 4g-29-8a_g >= 2 |
| Z' > Y' | N4-N3 >= 2+2x+((2g-3)/(g-2))y > 0 |
| Z' <= a_g Y' | (g-1)N3-(g-2)N4 = (g-1)(g-2)(z-y) >= 0 |
| Y'+Z' < H_g | E_H > 3g^2-31g+26 = 16+(g-10)(3g-1) > 0 |

Thus 1 lies in K_g and C_g K_g is contained in K_g. The weak faces are
correctly distinguished from the independently strict selector gaps.

The two temporal carries are also independent obligations. A_g 1 > 1 handles
the first base phase. Every entry of C_g-I is positive for g at least 10, so
(C_g-I)u>0 for positive u; applying nonnegative A_g with a positive entry in
every row propagates strict first-phase temporal domination. The positive
integer coefficients of the forward iterates prevent cancellation, and
characteristic zero keeps every selected positive coefficient nonzero.

I separately checked C_g-A_g entry by entry and all three fourth-row
differences. They prove strict q4 visibility against the other three
q-coordinates and all four p-coordinates after every positive iterate. The
identity case at n=0 is correctly treated as an eight-coordinate tie.
Consequently the actual degree vectors and total degree are

    u_n = C_g^n 1,
    v_n = A_g C_g^(n-1) 1 for n>=1,
    deg(F_g^n) = e4^T C_g^n 1 for every n>=0.

For the spectral theorem, I independently recomputed all ten nontrivial
principal minors:

    M12 = -3g^2-7g+18       M123 = -3g^3+23g^2-52g+36
    M13 =  g^2-7g+10        M124 = -3g^3+20g^2-35g+18
    M14 =  g^2-6g+5         M134 = -3g^3+12g^2-15g+6
    M23 =  g^2-8g+12        M234 = -3g^3+15g^2-24g+12
    M24 =  g^2-7g+6
    M34 = -3g^2+9g-6.

Their sums give

    e1(C_g) = 4g+10
    e2(C_g) = -2g^2-26g+45
    e3(C_g) = -12g^3+70g^2-126g+72.

Block determinants give

    det A_g = det B_g = -3(g-1)(g-2)
    det C_g = 9(g-1)^2(g-2)^2.

The characteristic polynomial is therefore exactly

    R_g(t) =
      t^4 -(4g+10)t^3 +(-2g^2-26g+45)t^2
      +(12g^3-70g^2+126g-72)t
      +9(g-1)^2(g-2)^2.

I also reproduced

    12g^3-70g^2+126g-72 = 2(g-3)(2g-3)(3g-4)
    R_g(1) = 3g(g-1)(3g^2-11g+4) > 0.

Cayley-Hamilton gives the exact annihilating recurrence

    d_(n+4) = (4g+10)d_(n+3)
            +(2g^2+26g-45)d_(n+2)
            -(12g^3-70g^2+126g-72)d_(n+1)
            -9(g-1)^2(g-2)^2 d_n,

with d_0=1 and d_1=7g-7. The manuscript correctly does not claim minimality
for every g.

For g congruent to 3 modulo 5, reduction is exactly

    f(t) = t^4 - 2t^3 - t^2 + 1

over the five-element field. Its values at 0,1,2,3,4 are (1,4,2,4,3), so
there is no linear factor. I exhaustively checked every monic quadratic
factor shape and all four constant pairs (1,1), (2,3), (3,2), (4,4);
none works. Thus R_g is irreducible over the rationals on
g=13,18,23,... . Positivity of C_g gives a primitive integer matrix, so
Perron-Frobenius and the positive e4/right and left/1 pairings yield

    lambda_1(F_g) = rho(C_g).

Irreducibility makes that spectral radius a degree-four Perron algebraic
integer on the stated progression. Comparing the t^3 coefficient makes the
values pairwise distinct.

The g=9 boundary is stated narrowly and correctly. The ordinary seed margins
are (1,0,-2,5) and y+z=H_9=2, so this strict selector/cone induction cannot
start. The text does not make a global smaller-parameter impossibility claim.

I also checked the publication-review kernel correction directly:

    ker(A_g+I) = span((0,0,1,-1)^T)
    ker(B_g+I) = span((1,-1,0,0)^T),

the two shifted kernels meet trivially, while

    ker(A_g) = ker(B_g) = {0}

because both determinants are nonzero. There is no remaining ordinary-kernel
misstatement in the manuscript. Together with R_g(1) nonzero, this matches
the bounded comparison with Paper 22's common shifted-kernel collapse
mechanism without claiming a classification or a sufficient quartic
criterion.

The theorem, tables, proof package, claims/evidence matrix, plan, abstract,
introduction, conclusion, and limitations agree. The exact theorem is bounded
to the displayed positive coefficients, supports and phase order in
characteristic zero; the cone is sufficient rather than necessary or
maximal; irreducibility is claimed only on one residue class; and no entropy,
integrability, conjugacy, genericity, periodic-point, minimal-dimension, or
optimal-sparsity consequence is asserted. I found no mathematical
contradiction, missing qualifier, theorem-table drift, or unsupported
headline claim.

## 9. PDF identity, metadata, structure, security, and fonts

The accepted PDF and main_round0.pdf are byte-identical:

- SHA-256:
  ae37679ef3ee4fa0b86f41e073f374920499f4959a196e289829e654b3d12d37
- 492,452 bytes
- PDF 1.5
- 23 pages
- US Letter, 612 by 792 points, zero rotation on every page
- unencrypted

Poppler reports the exact title, empty Subject, Keywords, Author, Creator,
and Producer fields, no custom metadata, no metadata stream, no form, no
JavaScript, no suspect flag, and no dates. The visible title agrees with the
source after whitespace normalization; the visible author is Anonymous
exactly once, while PDF metadata author remains empty.

I searched raw bytes, all decoded xref objects, all decoded streams, and
visible extracted text. CreationDate, ModDate, the deterministic epoch date,
and any alternative date marker are absent in every layer. There is no
encryption dictionary, metadata stream, AcroForm, XFA, JavaScript, launch
action, submit/import action, embedded file, attachment, filespec, RichMedia,
movie, sound, screen, 3D object, collection, or image object. pdfimages lists
zero images and pdfdetach lists zero embedded files. A Ghostscript
SAFER/nullpage structural pass exits successfully.

PyMuPDF 1.27.2.3 opened all pages and traversed xrefs 1 through 639 without
exception. The xref length is 640; the trailer has Index [0 640], Size 640,
Root 637, and Info 638. It contains 86 streams and no object/xref/trailer
inconsistency. The only action families are ordinary navigation: 164
/S /GoTo actions, one /S /URI action, outline Next links, and one catalog
OpenAction at xref 637 pointing to xref 114 with destination Fit. Page-level
enumeration finds 135 internal links and one external arXiv URI
https://arxiv.org/abs/2509.14584. There are no widgets, attachments, images,
or nonlink annotations.

There are exactly 28 outline/bookmark entries. Their hierarchy and page
destinations match the nine sections and 19 subsections, including the
repaired plain g=9 bookmark. All 23 pages have nonzero text and word counts;
there is no missing or duplicate page.

pdffonts reports 31 rows. Every row is embedded, subsetted, and Unicode
mapped. This includes all Latin Modern roman, bold, italic, sans, mono,
mathematical italic/symbol/extension rows and MSBM10. No font row fails any
of the three requirements.

The private-marker scan found no TODO, TBD, FIXME, BLOCKED, PASS, Paper 23,
Batch 06, gate, queue, private path, checksum, reviewer/agent/model, ORCID,
email, acknowledgment, funding, affiliation, or corresponding-author leak.
The ordinary verb verify occurs twice in legitimate prose and is not a
placeholder. The presentation remains anonymous.

## 10. Fresh rendering and page-by-page visual review

I independently rendered the accepted project PDF, without rebuilding it,
using /usr/bin/pdftoppm -png -r 200 into the private scratch. The renderer is
Poppler pdftoppm 22.02.0, SHA-256
f09bac4b4bc5e08ef9d44620fb5a4f1dd61574a8ed9fe49f48575d45e6966165.
The render produced exactly 23 root-owned mode-0644 RGB PNGs, each
1700 by 2200 pixels. Their seven-field manifest uses filename, SHA-256,
bytes, width, height, color mode, and file mode. It is 2,346 bytes and 23
LF, has SHA-256
2b2532390e4bc604393ecc5db355585650ffc035d234ed18fc3627014675cff6,
and binds 9,568,574 PNG bytes.

| Page | PNG SHA-256 | Bytes |
|---:|---|---:|
| 1 | 33801f3bf3d2cf21ff57d04c4b604d254893d7ae4efefad7dbd3cd1ac26c6d76 | 452,006 |
| 2 | 3d271c39af4e2b800687d6364bd898bb3680a0a7d89057de491089e77d3e7bdf | 525,172 |
| 3 | e3f4606402c9540b323cdc5e45fc5f27b8504d98347c171d08017d866596ea9b | 665,390 |
| 4 | 2c6c76cb631a3b99062c1d526b2c835772a81a4c34bc4241c0d3696429cbacaa | 334,954 |
| 5 | cf497d261948f398870a93ea68d7e9cad47b7fd796b99a5dbb2cb978a25383eb | 482,954 |
| 6 | 4ec32520c9464a4f723420b64b1b54ff8957d1bebadfcc9e314f6bf7f1e58d24 | 475,316 |
| 7 | c0253e1e0da879a9aad4fcbdbb3a882e9dd97d803d67e123fe68e204e7bb9ebc | 472,888 |
| 8 | 51420188e93e5ab362b75a861f82f116f5d53c0c1121db7fa842326615a3abd1 | 322,614 |
| 9 | 6e357859effd66580f2012b83eeb46c0b49ad7f5c6c6f355d329c7a3ebfb36d8 | 320,763 |
| 10 | 833b88d6e63554deb614c0c2d5bedf9a910534f31bf2e6c5cf21029e1b150bcb | 389,382 |
| 11 | 9d3c011b7253293951efd3531f50797f69e7da50de03e2985ae59dc10371f041 | 324,796 |
| 12 | 53d9e4499fae3baad49a3a31e30972bf83f27aa7b2a0f1a5a7f13606bfd2126b | 356,692 |
| 13 | 3c5d1cf4f73bed924515e6c9fae3ce1a561cf5b99e7b1bf4a85f5bc45fcb5db5 | 572,501 |
| 14 | 3b7766f05968ab910d9dbb8b52f1c3f4d79c3354abdb435e777c71e2e48d03e0 | 411,362 |
| 15 | 77e2a2b57282909613851e90ac892736797ac3d5774abb9a6dfc4c64711e6881 | 384,416 |
| 16 | 805d71251cdb9f2eb41bd79c6e350acaab00a870e89e4c7a578d470fa0af58b7 | 333,453 |
| 17 | 75ea3e26f7618e99717844a21e9cd28722c2506bc9c71d5baff60575b0b92d4c | 391,835 |
| 18 | 8216c9973bcc02afdd7bd79c74448f2c5036374244b54910348481e72c5f7c06 | 306,217 |
| 19 | 102e96afb8011378af6a9d1112f98022aaeed667a2ac009eaf5bf7f03125d2da | 511,631 |
| 20 | 3fe658a527b509cb1eb7602cc6574557f037e224979c8dd0489b2e83ff2ea3c6 | 283,583 |
| 21 | 9b0b0f4dc0b7f57570617ccec0623c1938ae3c3facf131795cbbc8d31abe5e23 | 426,397 |
| 22 | 35a8f1a148e4cda994794664cbbd6e0710de5a573d82d7149d55e871e3d0942e | 502,990 |
| 23 | d68cb9922f245cb1953450b2d9f06c2ca886fa2bc1d68ec01bcd892c62e8a578 | 321,262 |

I made four contact sheets for navigation, then inspected every one of the
23 page PNGs individually at the original 200-dpi review resolution. I
separately inspected the main-theorem displays, selectors and cone pages,
both carry and survival arguments, visibility displays, quartic and
recurrence pages, modulo-five proof, g=9 boundary, shifted-kernel correction,
limitations, and bibliography. Tables 1, 2, and 3 were inspected at page
detail: the complete support ledger on page 7, six ratio-cone walls on page
10, and ten principal minors on page 15 are fully legible and agree with the
source.

Across all pages I found no clipping, overlap, broken or missing glyph,
unreadably small material, margin overflow, bad display break, orphan
heading, bad page break, blank page, duplicate page, missing page, citation
artifact, broken visible link, or identity leak. Page 23's remaining white
space is the normal end of the nine-entry bibliography, not a layout defect.
The visual title, Anonymous line, abstract, section order, equations, tables,
citations, bibliography, and page sequence all agree with the source and
structural text extraction.

## 11. Final acceptance boundary

Every audit conjunct required by the corrected-R0 Build R1 gate passed:

- all 44 opening files and all three governance roots were read and remained
  stable;
- the corrected evidence conjunction was reconstructed without relying on an
  old PASS;
- both independently authored strict JSON implementations and the retained
  validators passed;
- the four and only four executable corrections, eight semantic
  suspensions, eight syntax-only scopes, and three negative virtual hashes
  were reproduced;
- the exact executables, permitted root manifests, source/log/output A/B
  equality, environment, command sequence, exit vectors, persistence
  identities, and converged diagnostics passed;
- the complete manuscript, proof chain, citation boundary, theorem
  qualifiers, matrices, selectors, six walls, carries, survival,
  visibility, quartic, recurrence, irreducibility, Perron statement, g=9
  boundary, and shifted kernels passed;
- PDF identity, metadata, dates, xref/trailer, actions, security, fonts,
  bookmarks, links, anonymity, and all 23 fresh page renders passed; and
- no prohibited root, build, source edit, cleanup, retry, network action, or
  external effect occurred.

The existing corrected R0 outputs are accepted prospectively under the
effective evidence conjunction. The immutable old receipt is not accepted
as written, historical old-contract compliance remains denied, and no
downstream lifecycle action is authorized by this review alone.

BUILD_R1_R0_REPAIR_CORRECTION_PASS
