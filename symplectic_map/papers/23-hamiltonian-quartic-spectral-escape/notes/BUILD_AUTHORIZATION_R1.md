# Paper 23 — Deterministic R1 No-Op Build Authorization

Date: 2026-08-25 UTC  
Stage: unchanged-source deterministic R1 build  
Disposition: exactly one later, distinct R1 builder invocation may be opened
only by the parent-consumption transition specified here

## 1. Authority, issuance provenance, and author stop

This note is a frozen build contract, not a build.  Its author is distinct
from the R1 no-op revision author and creates only this note.  This author
does not create a temporary root, execute TeX or BibTeX, render a page, edit a
source or existing artifact, consume the future build authority, perform a
review, or cause an external effect.

The following values are the exact authorization-author opening state.  They
are **issuance provenance only**.  The mandatory parent transition will
change the first two ledger identities, so no future builder may substitute
these issuance hashes for the actual post-consumption identities.

| Issuance artifact or field | Exact opening value |
|---|---|
| `BATCH_06_STATUS.md` | SHA-256 `2e47a8d5b707017354b75eb6097f190e3f42aaaf17c9344ec958b93a650492e2`; 104,067 bytes; 1,527 LF; mode 0644; root:root; link count one; device/inode 2431/12439253850 |
| issuance gate | `PAPER23_R1_BUILD_AUTHORIZATION_OPEN` |
| Paper 23 issuance queue | `R1_NO_OP_REVISION_PASS_PENDING_BUILD_AUTHORIZATION` |
| `BATCH_06_IDEA_REPORT.md` | SHA-256 `073aaf862fa5a66e46e345780c26c692e4ee8bb60b5bf697be6e6e58fd862254`; 170,049 bytes; 3,183 LF; mode 0644; root:root; link count one; device/inode 2431/12439253853 |
| `BATCH_06_PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTION.md` | SHA-256 `27615c425261aa72caa4c880b6bc7f54ecfa98c99399a2d7efc78ed19d8282c4`; 8,524 bytes; 245 LF; mode 0644; root:root; link count one; device/inode 2431/12439253857; terminal `PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTED_PASS` |

The Paper 23 project opened at exactly 47 ordinary regular files, four child
directories, zero symlinks, zero other objects, and 1,963,629 regular-file
bytes.  The project root and the four child directories `experiments`,
`notes`, `paper`, and `refine-logs` are ordinary root-owned mode-0755
directories, not symlinks.  At opening, all 47 files are ordinary root-owned
mode-0644 regular files with link count one.

No-follow preflight found all five downstream paths absent:

- `notes/BUILD_AUTHORIZATION_R1.md`;
- `paper/BUILD_METADATA_R1.json`;
- `paper/BUILD_RECEIPT_R1.json`;
- `paper/main_round1.pdf`;
- `notes/BUILD_R1_BLOCKER.md`.

The sole authorization-author write is the first path above, created with
exclusive-create, no-overwrite, and no symlink following.  It must be an
ordinary root-owned mode-0644 regular file with link count one and must end
with the exact unique final nonempty line `BUILD_AUTHORIZATION_R1`.  The
authorization-author successful stop is exactly 48 regular files, four child
directories, zero symlinks, and zero other objects.  The other four paths
remain absent.  This author performs no parent consumption and no build.

## 2. Complete 47-file issuance manifest

The complete opening manifest is sorted under `LC_ALL=C` by project-relative
path bytes.  Each LF-terminated row has nine TAB-separated fields:
`path`, `sha256`, `bytes`, `LF`, `mode`, `owner`, `device`, `inode`, and
`links`.  The exact stream is 6,570 bytes and 47 LF and has SHA-256
`47184ac421ca6941d795e3a2bf5250ee16f54ab2a63780215b9cbfea8affe336`.

```text
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
notes/INDEPENDENT_BUILD_R1_R0_REPAIR_CORRECTION_REVIEW.md	98e709908c44f6a62dc11520649134be2c6b2830e2aecf6bbf6743a9889e6089	39959	702	644	root:root	2431	6443730220	1
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
notes/R1_REVISION_WINDOW_NO_CHANGE.md	d632175aa1a9ab29d782e2b300b40c7f334021979e785def4deb4191c8de0e09	15558	205	644	root:root	2431	6443730221	1
notes/RESEARCH_QUESTION.md	3cd1e22973e443c47a1672a82431c14c3b86ceba685330234d19085e65acdb5c	5492	135	644	root:root	2431	6443323388	1
notes/SOURCE_R1_ABSTRACT_INTEGER_REPAIR.md	f5bea1184027da2afe9c1cc6810c000b72fb058cc6cb527a30222866b521ef3b	8168	136	644	root:root	2431	6443457781	1
paper/BUILD_EVIDENCE_CORRECTION_R0.json	257d37600e9c7498b3e801d08fce3391d6852c5ce34ba1d468c502e357de7bfd	41366	1	644	root:root	2431	3227387381	1
paper/BUILD_METADATA_R0.json	599a8c3e1578e79fee6dff197d0cd8d3bcb3cb06ab13ebd4b8e1c975ec951362	70889	1	644	root:root	2431	3227322490	1
paper/BUILD_RECEIPT_R0.json	70ad2b65c82201981488c5bcc4685f08f37529504082afb7e1778248c96cd590	71124	1	644	root:root	2431	3227322494	1
paper/PAPER_PLAN.md	fa7e5a7ea6693b0d8ef10651da317d253f5a1ba199e3b026a3b92c8104b6c974	44881	799	644	root:root	2431	3227277695	1
paper/SOURCE_REVISION_RECEIPT_R1.json	a0ee8c63436e5c8277b44b9df82c03f1c9c6c7b1b3eff53118bc75ed7eae3c7b	20687	1	644	root:root	2431	3227546572	1
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
```

Every row and the three issuance governance roots are immutable through this
authorization authorship.  At builder opening, the 47 rows remain unchanged
and are joined only by this authorization's final externally measured row.

## 3. Mandatory parent consumption and dynamic builder opening

This note does not itself permit root creation or compilation.  Before a
builder may act, a separate parent transition must:

1. read and externally bind this authorization's final project-relative
   path, SHA-256, byte count, LF count, mode, owner, device, inode, link
   count, and exact terminal line in both `BATCH_06_STATUS.md` and
   `BATCH_06_IDEA_REPORT.md`;
2. set the live gate exactly to
   `PAPER23_DETERMINISTIC_R1_BUILD_OPEN`;
3. set the Paper 23 queue exactly to `R1_BUILD_AUTHORIZED`; and
4. state that exactly one distinct no-op R1 build invocation is open, that
   authority is consumed at first fresh-root creation, and that there is no
   retry, replacement invocation, or builder self-review.

The later builder must not expect the issuance hashes in Section 1 to remain
current.  Before creating a root, it must read both post-consumption ledgers
through EOF, hash and stat their actual bytes, verify their exact gate/queue
and authorization binding, record their actual final identities and terminal
lines, and freeze those exact ledger bytes throughout its invocation.  It
must likewise reconstruct and bind the complete 48-file project universe:
the exact 47-file issuance manifest above plus this authorization's final
external identity.  That 48-file universe, every pre-existing project inode
and byte string, the publication-correction root, and both actual
post-consumption ledgers are read-only to the builder and must remain stable
through final persistence or failure disposition.

At builder opening the project must be exactly 48 regular files, four child
directories, zero symlinks, and zero other objects.  These four future paths
must all remain absent under no-follow checks:

- `paper/BUILD_METADATA_R1.json`;
- `paper/BUILD_RECEIPT_R1.json`;
- `paper/main_round1.pdf`;
- `notes/BUILD_R1_BLOCKER.md`.

A mismatch before first-root creation means zero root and zero project write.
It is reported to the parent for a new governance decision; the would-be
builder may not repair, reinterpret, or consume authority.  Authority is
consumed irrevocably when the builder creates the first of the two fresh R1
roots.

## 4. Frozen source and verified no-op revision evidence

The only build input is the following immutable source trio and no other
source, asset, generated file, bibliography, or cache:

| Project source | SHA-256 | Bytes | LF | Mode / owner / links |
|---|---|---:|---:|---|
| `paper/main.tex` | `1ac57197ff87b2c1c6ec2cea7cf644021e629e519e4215d4b32e9e4420aa46b0` | 67,408 | 1,776 | 0644 / root:root / 1 |
| `paper/math_commands.tex` | `a69565204428ce95abbcab5afb3833290004110e2718c074fbc805f7d1bdcb0d` | 420 | 13 | 0644 / root:root / 1 |
| `paper/references.bib` | `ba0156abd7eb399de532b9bc1eefa81b3bb1be7868eed6ee4b42f8cd3371c782` | 2,812 | 99 | 0644 / root:root / 1 |

The no-op revision evidence is independently frozen:

| Evidence | SHA-256 | Bytes / LF | Required exact status or terminal |
|---|---|---:|---|
| `notes/INDEPENDENT_BUILD_R1_R0_REPAIR_CORRECTION_REVIEW.md` | `98e709908c44f6a62dc11520649134be2c6b2830e2aecf6bbf6743a9889e6089` | 39,959 / 702 | terminal `BUILD_R1_R0_REPAIR_CORRECTION_PASS`; zero required and zero cosmetic findings |
| `notes/R1_REVISION_WINDOW_NO_CHANGE.md` | `d632175aa1a9ab29d782e2b300b40c7f334021979e785def4deb4191c8de0e09` | 15,558 / 205 | terminal `R1_REVISION_WINDOW_NO_CHANGE` |
| `paper/SOURCE_REVISION_RECEIPT_R1.json` | `a0ee8c63436e5c8277b44b9df82c03f1c9c6c7b1b3eff53118bc75ed7eae3c7b` | 20,687 / 1 | schema `PAPER23_SOURCE_REVISION_RECEIPT_R1_NO_OP_V1`; artifact id `paper23_r1_no_op_source_revision`; status `R1_NO_OP_REVISION_PASS`; null self bytes/hash |

The source receipt is strict-canonical one-line UTF-8 JSON.  It records one
total revision window, one consumed window, zero remaining windows, empty
changed-path and changed-hunk sets, zero added/removed/changed bytes, zero
source, theorem, proof, title, citation, anonymity, and anti-claim changes,
and identical before/after identities for the three source files.  Those
facts are hard builder preconditions.  There is no further revision window.

## 5. Recovered corrected-R0 evidence: exact namespaces and non-retroactivity

The accepted comparator is not the original receipt alone.  The builder must
represent the evidence in four noninterchangeable namespaces and preserve
their meanings verbatim:

1. `historical_original_bytes`: the immutable original metadata and receipt
   exactly as written, including their erroneous executable literals and
   physical-history facts.  Their semantic PASS claims are not credited.
2. `correction_overlay`: the append-only human correction, strict-canonical
   overlay, and independent overlay review.  This namespace supplies factual
   precedence only at the four listed executable-digest pointers and scopes
   or suspends the exact claims listed below.
3. `effective_corrected_r0`: the conjunction of the first two namespaces,
   the independent overlay PASS, and the fresh direct corrected-R0 R1 review.
   This conjunction prospectively accepts the retained outputs now while
   still denying historical old-contract compliance.
4. `r1_live_observation`: only facts freshly observed by the future builder
   from its new invocation.  No original, overlay, review, or comparator
   literal may be copied into a live-observation field as though measured.

The complete six-artifact recovered conjunction is:

| Namespace role and path | SHA-256 | Bytes / LF | Exact status or terminal and effect |
|---|---|---:|---|
| original bytes: `paper/BUILD_METADATA_R0.json` | `599a8c3e1578e79fee6dff197d0cd8d3bcb3cb06ab13ebd4b8e1c975ec951362` | 70,889 / 1 | `BUILD_METADATA_R0_REPAIR`, historical record label only |
| original bytes: `paper/BUILD_RECEIPT_R0.json` | `70ad2b65c82201981488c5bcc4685f08f37529504082afb7e1778248c96cd590` | 71,124 / 1 | historical builder claim `BUILD_R0_REPAIR_PASS`, suspended and noncredited |
| correction ledger: `notes/R0_BUILD_EVIDENCE_CORRECTION.md` | `89e56bf502a2d40ecb831991b4d5edd5e2672fcd3c1f9149d6edb2222a8f5b01` | 31,005 / 426 | terminal `R0_BUILD_EVIDENCE_CORRECTION_AUTHOR_STOP` |
| correction overlay: `paper/BUILD_EVIDENCE_CORRECTION_R0.json` | `257d37600e9c7498b3e801d08fce3391d6852c5ce34ba1d468c502e357de7bfd` | 41,366 / 1 | schema `PAPER23_R0_BUILD_EVIDENCE_CORRECTION_V1`; status `R0_BUILD_EVIDENCE_CORRECTION_FROZEN_PENDING_INDEPENDENT_REVIEW`; pending label resolved only by the next PASS |
| overlay review: `notes/INDEPENDENT_R0_BUILD_EVIDENCE_CORRECTION_REVIEW.md` | `489148a4246c04c4b1f3b403f6baa8ef7ad6639d803059858c4426f62847fa00` | 22,861 / 407 | terminal `R0_BUILD_EVIDENCE_CORRECTION_PASS` |
| direct corrected-R0 review: `notes/INDEPENDENT_BUILD_R1_R0_REPAIR_CORRECTION_REVIEW.md` | `98e709908c44f6a62dc11520649134be2c6b2830e2aecf6bbf6743a9889e6089` | 39,959 / 702 | terminal `BUILD_R1_R0_REPAIR_CORRECTION_PASS`; prospective acceptance only |

Exactly four and only four factual pointers receive overlay precedence:

| Immutable target | RFC 6901 pointer | Historical erroneous value | Corrected comparator value |
|---|---|---|---|
| `paper/BUILD_METADATA_R0.json` | `/build/executable_identities/bibtex/sha256` | `c9ecb7182f287007d277d67a1537a721493f2d3b0c98d16006ba24493710618f` | `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` |
| `paper/BUILD_METADATA_R0.json` | `/build/executable_identities/pdflatex/sha256` | `01a7ab54dd9ca121cc8694f3bb656633682f2e2fd5fba6f9adcd8a9508336cf9` | `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` |
| `paper/BUILD_RECEIPT_R0.json` | `/build/executable_identities/bibtex/sha256` | `c9ecb7182f287007d277d67a1537a721493f2d3b0c98d16006ba24493710618f` | `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` |
| `paper/BUILD_RECEIPT_R0.json` | `/build/executable_identities/pdflatex/sha256` | `01a7ab54dd9ca121cc8694f3bb656633682f2e2fd5fba6f9adcd8a9508336cf9` | `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` |

Exactly eight semantic pointer/document pairs remain suspended: the
Cartesian product of both original JSON paths and these four pointers:

- `/acceptance/all_hard_conjuncts_pass`;
- `/acceptance/blocker`;
- `/acceptance/chosen_outcome`;
- `/checks/success_paths_absent_before_complete_validation`.

Exactly eight validation pointer/document pairs retain only the scope
`immutable_original_erroneous_candidate_syntax_canonical_bytes`: the
Cartesian product of both original JSON paths and these four pointers:

- `/json_validation/candidate_hashes_recorded_before_persistence`;
- `/json_validation/candidate_round_trips_exact`;
- `/json_validation/two_value_trees_agree`;
- `/json_validation/validation_completed_before_persistence`.

Those eight syntax-only scopes prove only grammar, duplicate rejection,
canonical encoding, original candidate equality, and physical history.  They
do not prove executable identity truth, semantic acceptance, all hard
conjuncts, the later overlay, the R1 candidates, or a hypothetical patched
document.  Separately, the receipt's top-level `BUILD_R0_REPAIR_PASS` remains
a suspended historical builder claim, and the metadata status remains only a
record label.

The builder and both R1 JSONs must state all of the following explicitly:

- `original_receipt_as_written_pass=false`;
- `historical_old_contract_compliance=false`;
- `no_retroactive_cure=true`;
- `materialized_patched_json_pair=false`;
- `other_factual_pointers_corrected=0`;
- all companion, self, staged-copy, persistence, atomic-nine-path, and old
  inventory statements stay in the original-byte/physical-history namespace;
- the retained nine R0 paths are accepted now only through the prospective
  recovered conjunction, never by reviving the old receipt.

No four-pointer-patched JSON pair is defined or written.  For negative
control only, the unauthorized virtual metadata would hash to
`9a1864be2795df47a3f82855f2b1aef2aa51424809c7550767c466a7fc9a4493`,
the four-pointer virtual receipt with the old companion hash would hash to
`d675ef6aeca693c732f4f39601f5b68592f7dda2cab4ca7bf2bc956346397a15`,
and the forbidden fifth-companion-corrected virtual receipt would hash to
`3b6b6343dd1d07aa6106f07e9c61ee451cc8c4e74f0ad918d1d086fb11e5b67c`.
None is evidence or an allowed persistence object.

## 6. Accepted corrected-R0 roots and exact byte comparators

Only these two retained successful roots are permitted corrected-R0
comparators:

| Read-only comparator root | Mode / owner | Complete retained inventory | Nine-field manifest |
|---|---|---|---|
| `/tmp/paper23-r0-repair-correction-A.Er2f85` | 0700 / root:root | 43 regular files, one child directory, zero symlinks, zero other objects; 8,637,740 regular bytes | 5,655 bytes / 43 LF / SHA-256 `415f5d1d47828a25154f2dea5423d8259cdd40b3085a3b4c4d2140607f237b38` |
| `/tmp/paper23-r0-repair-correction-B.tcCPcQ` | 0700 / root:root | 13 regular files, zero child directories, zero symlinks, zero other objects; 648,698 regular bytes | 1,515 bytes / 13 LF / SHA-256 `1d0e5a4a101f148a449dac5bd5499c5bf87daccb995ea27b42cf84eb7129a067` |

They are never inputs, caches, templates, validator sources, clones, or
staging roots.  The future builder may perform only read-only direct
comparisons against them, and only after both new R1 roots have completed all
four commands.  Both comparator roots and every object beneath them must
remain unchanged.  Their scripts and prior validation outputs may not be
executed or copied into the R1 validation path.

The following four command logs are byte-identical between the two accepted
roots and are the direct no-op R1 comparators:

| Log | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `command-1.log` | `1fcbc0319012bbeb4fd526dad9eef6a0ca9e86474e9c092ae766a70a4ef466ce` | 18,124 | 597 |
| `command-2.log` | `7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9` | 158 | 4 |
| `command-3.log` | `cba30ead0e25a854366d5bf7e9156ffadfb713fd4de7097a43b6f284e1d2db72` | 8,363 | 158 |
| `command-4.log` | `ad3eb1bf23dd06e82b1683ccb3e66c34b142303fa24685f56f268f58368612b0` | 7,254 | 112 |

The six final outputs below are byte-identical between the accepted roots and
the current project.  The project copies are immutable throughout R1:

| Output | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `main.aux` | `2748935c255778a4e40227c008adeb8c361a3933a9ff5f545407f04ae48c8eeb` | 14,072 | 165 |
| `main.bbl` | `baa229dd7d35d96b27d7dfb18a844db73c98b752df3be4c008d748636f199cf9` | 2,881 | 73 |
| `main.blg` | `be7e80a71c65ef8bbfcc2e43c3aadcc0b89cb8216e61a785ca24403ec6c04c34` | 900 | 46 |
| `main.log` | `ab451da731a6ef13c7f1f83e9de463b4b2d71b0cb255e10b2d831a235aaa13f6` | 27,628 | 700 |
| `main.out` | `14be6d78b541eb75e29cec5bf18d1e9a26bfb0c128ddaa5f4c26ab00d315bb94` | 6,226 | 28 |
| `main.pdf` | `ae37679ef3ee4fa0b86f41e073f374920499f4959a196e289829e654b3d12d37` | 492,452 | 2,724 |

Project `paper/main.pdf` and `paper/main_round0.pdf` are directly
byte-identical with the displayed PDF identity.  Project
`paper/BUILD_METADATA_R0.json`, `paper/BUILD_RECEIPT_R0.json`, all six
outputs, and both existing PDF paths are read-only evidence; none may be
edited, replaced, recopied in place, relinked, removed, chmodded, or touched
by persistence.

The following four roots are absolutely excluded:

- `/tmp/paper23-r0-A.DyWKGR`;
- `/tmp/paper23-r0-B.dsQvTx`;
- `/tmp/paper23-r0-repair-A.BzlBNd`;
- `/tmp/paper23-r0-repair-B.TVRci7`.

The builder and every child process, validator, comparator, and diagnostic
must not access, enumerate, list, stat, glob through, read, write, copy from,
link to, rename, clean, or otherwise touch any excluded root.  A root name
appearing as inert text in an immutable governance or project record does not
authorize a filesystem operation.

## 7. Exactly two fresh private R1 roots and exact execution

After every pre-root conjunct passes, the single builder invocation creates
exactly two brand-new independently allocated private directories, called R1
root A and R1 root B.  Each canonical absolute path must not previously have
existed; each is an ordinary root-owned mode-0700 directory, not a symlink.
The roots must have distinct device/inode identities and may share no source,
log, output, validator, or other object by hard link or symlink.  Root B may
not be cloned from root A, and neither may be cloned from or populated by an
old root.

Before command 1, each root contains exactly three independently copied
ordinary mode-0644 link-count-one regular files and no other object:
`main.tex`, `math_commands.tex`, and `references.bib`.  Their bytes equal the
frozen project trio, while their inodes are distinct from the project and one
another.  Record root creation/freshness evidence, canonical paths, complete
initial inventories, modes, owners, devices, inodes, links, source
identities, and direct copy comparisons.

Each of the eight child build processes receives an empty inherited
environment populated with exactly these six variables and no others:

```text
PATH=/usr/bin:/bin
SOURCE_DATE_EPOCH=1787616000
FORCE_SOURCE_DATE=1
TZ=UTC
LC_ALL=C
LANG=C
```

With the corresponding root as the exact working directory, execute exactly
once and in this order in root A, and exactly once and in this order in root
B:

1. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
2. `bibtex main`
3. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
4. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`

Capture each command's merged stdout/stderr byte stream directly as
`command-1.log` through `command-4.log` in its own root without changing the
arguments, environment, working directory, output bytes, or exit status.
Both exit vectors must be exactly `[0,0,0,0]`.

There is no retry, fifth TeX pass, second BibTeX run, alternate command,
`latexmk`, engine or option substitution, shell escape, package installation,
source generation or edit, scientific computation, cache use, network use,
old-root use, cleanup build, third root, or replacement root pair.  Any false
conjunct after first-root creation consumes the authority and selects failure.

Only after both roots finish command 4 may root A acquire one explicitly
named mode-0700 child subtree, `r1-validation-staging`.  All fresh validators,
candidate JSONs, read-only PDF-analysis records, page renders, contact sheets,
and success-staging files must stay inside that subtree.  It is part of root
A, not a third build root, and it is not a build input.  Root B receives no
validation or candidate staging.  Both complete roots, including this
subtree, are retained privately and unchanged after the final checkpoint for
a separately authorized fresh R2 review.

## 8. Pinned-content, dynamically observed executable identity

Executable identity is a live acceptance fact, never a future hard-coded
field.  The invocation uses the PATH resolution of `pdflatex` and `bibtex`.
At pre-root preflight, immediately before and after every one of the eight
commands, at the start and end of validation, immediately before persistence,
and after persistence/readback or failure disposition, the builder must:

1. resolve and record the complete wrapper/symlink chain with no-follow
   `lstat` evidence and the final target with `stat` evidence;
2. stream each resolved target independently through (a) a fresh Python
   `hashlib.sha256` loop using fixed-size binary chunks, (b) GNU
   `sha256sum`, and (c) OpenSSL `dgst -sha256`;
3. require all three hash routes to agree in that observation; and
4. record observed resolved path, SHA-256, bytes, LF, mode, owner, link count,
   device, inode, and available nanosecond mtime, ctime, birth time, and atime.

The pinned-content comparator is:

| Invoked name and required resolved path | Historical corrected comparator SHA-256 | Bytes / LF | Mode / owner / links |
|---|---|---:|---|
| `/usr/bin/pdflatex` resolving to `/usr/bin/pdftex` | `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` | 1,802,504 / 4,629 | 0755 / root:root / 1 |
| `/usr/bin/bibtex` resolving to `/usr/bin/bibtex.original` | `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` | 117,128 / 393 | 0755 / root:root / 1 |

The live resolved path, three-way SHA-256, byte count, mode, owner, and link
count must equal the corresponding corrected-R0 comparator.  Device, inode,
mtime, ctime, and birth time are live dynamic values: they need not equal the
historical overlay's old stat values, but each must remain stable throughout
this invocation.  Atime is recorded at each observation but is expressly not
a stability conjunct because the required reads may update it.  The wrapper
chain, final target, and every other required field must remain stable.

The historical comparator strings above may appear in the R1 JSON only under
the recovered-R0 comparator namespace.  Every value in the R1 live
executable-observation namespace must be derived programmatically from the
builder's in-memory live-measurement object.  Literal assignment, copy/paste
from this note, copying an original or overlay field, or using a static common
value tree to populate a live path, digest, byte count, mode, owner, link,
device, inode, or timestamp field is forbidden.

Both independent semantic validators must reopen the executable paths,
repeat live resolution, `lstat`/`stat`, and three-way hashing, and
pointer-compare every executable-related JSON field against their own fresh
observation and against the candidate generator's recorded measurement
provenance.  Syntax-only round trips are insufficient.  The generator and
validators must record that no live executable field was assigned from a
literal comparator.  Any mismatch, drift, unproved provenance, or semantic
validator disagreement is failure; no candidate may be patched after it.

## 9. Conjunctive R1 acceptance contract

Success requires every clause in this note.  An aggregate judgment, clean
PDF, historical PASS token, or equality on most files cannot compensate for
one false, missing, ambiguous, drifting, or unrecorded conjunct.

### 9.1 Execution, immutability, and direct equality

1. Both exit vectors are exactly `[0,0,0,0]` and all executable observations
   satisfy Section 8.
2. Hash and stat the project source trio before copying, after both command
   sequences, after validation, and after persistence/failure.  Hash and stat
   each root source trio before command 1, after command 4, and at every final
   boundary.  Every source byte remains frozen and all copied inodes remain
   independent.
3. Each R1 root ends command 4 with readable, nonempty `main.aux`,
   `main.bbl`, `main.blg`, `main.log`, `main.out`, and `main.pdf`, stable
   through validation and final disposition.
4. The two R1 roots are directly byte-identical for the source trio, all four
   corresponding command logs, and all six corresponding final outputs.
5. Because the revision was a verified no-op, each R1 source, command log,
   and output is also directly byte-identical to the corresponding object in
   each accepted corrected-R0 comparator root, with exactly the hashes,
   bytes, and LF counts in Sections 4 and 6.
6. Both R1 PDFs are directly byte-identical to immutable project
   `paper/main.pdf` and `paper/main_round0.pdf`, SHA-256
   `ae37679ef3ee4fa0b86f41e073f374920499f4959a196e289829e654b3d12d37`,
   492,452 bytes.  All six existing project outputs and both existing project
   PDFs remain byte-identical to builder opening.
7. Record every comparison as a direct byte comparison plus independent
   hashes, not as equality inferred from matching filenames or a prior claim.

### 9.2 Logs, closure, labels, citations, bibliography, and bookmarks

Read all eight command logs and both final LOG/AUX/BBL/BLG/OUT sets through
EOF.  The exact diagnostic progression in each root is:

| Pass | LaTeX warnings | Package warnings | Required interpretation |
|---|---:|---:|---|
| command 1 | 118 | 11 | 116 individual undefined-reference warnings plus two summaries; nine undefined citations plus natbib summary and outline rerun warning |
| command 2 | 0 | 0 | clean BibTeX |
| command 3 | 0 | 11 | nine citation warnings plus natbib undefined/changed summaries before final convergence |
| command 4 | 0 | 0 | fully converged |

No pass may contain a fatal error, compiler error, overfull box, underfull
box, or hyperref warning.  Each final 700-line `main.log` and command-4 log
has zero fatal/error, LaTeX warning, package warning, undefined citation,
undefined reference, rerun request, changed label, multiply defined label,
overfull box, underfull box, or hyperref finding.  Each `main.blg` reports
nine entries and zero warning.

Final closure must reproduce all of these exact counts independently:

- nine AUX citation commands and nine AUX `bibcite` entries;
- 95 unique `newlabel` entries and 116 resolved source references;
- bibliography style `plainnat`, database `references`, and nine
  nonduplicate BBL items;
- exactly 28 syntactically readable OUT/bookmark records, including the
  repaired plain `g=9` bookmark and no raw math shift or private token;
- nine source sections, 19 subsections, three tables, 72 equation
  environments, 16 aligned environments, no figure, no appendix, and no
  placeholder.

The exact nine distinct citation keys are
`BlancVanSantenAffineTriangular`, `ShaoSunDimensionFour`,
`HenonOpenProblems`, `BergerTuraevHamiltonianMaps`,
`ForstnericComplexSymplectic`, `KochLomeliStraightLineFlows`,
`RangarajanPolynomialSymplectic`, `DesertiDegreeGrowthExamples`, and
`DangFavreSpectralInterpretations`.  Every key is defined, cited, and present
exactly once in the bibliography, and no tenth key exists.  Citations remain
bounded related-work context and are not evidence for the selectors, cone,
carries, visibility, principal minors, quartic, irreducibility, or theorem.

Source, logs, generated text files, extracted PDF text, metadata, outlines,
annotations, links, and object streams contain no unresolved marker, `??`,
TODO, TBD, FIXME, VERIFY placeholder, citation-needed marker, private path,
checksum, gate/queue, review history, PASS/BLOCKED token, permission ledger,
agent/model/tool identity, identity disclosure, or other private provenance.

### 9.3 PDF identity, date omission, safety, fonts, and visual review

Each R1 PDF must independently reproduce the accepted byte identity and these
fresh structural observations:

- PDF 1.5, exactly 23 physical nonblank US Letter pages of 612 by 792 points,
  rotation zero, readable page and text traversal, and no missing or duplicate
  page;
- xref length 640; trailer `Index [0 640]`, `Size 640`, `Root 637`, and
  `Info 638`; 86 streams; no object/xref/trailer inconsistency;
- unencrypted, with no encryption dictionary, JavaScript, Launch,
  SubmitForm, ImportData, embedded file, attachment, Filespec, AcroForm, XFA,
  signature, RichMedia, movie, sound, screen, 3D object, collection, image
  object, or other dangerous action;
- only ordinary navigation actions: the accepted GoTo/URI/OpenAction and
  link set, with no private or dangerous target;
- exactly 31 reported font rows, every row embedded, subsetted, and Unicode
  mapped; a zero-font or partially mapped result fails;
- exactly 28 decoded outline/bookmark entries with the accepted nine-section,
  19-subsection hierarchy and destinations.

The decoded and visible title is exactly “Four-Mode Hamiltonian Product
Shears Beyond Cubic Collapse: Exact Degree Growth and Quartic Perron
Subfamilies”.  Visible author is exactly `Anonymous`; decoded PDF `Author`,
`Creator`, and `Producer` are each empty.  There is no identity, affiliation,
email, ORCID, acknowledgement, funding, or corresponding-author disclosure.

The epoch `1787616000` is build-environment provenance only.  Date omission
is a hard conjunct: `CreationDate` and `ModDate` keys and values occur zero
times in `pdfinfo -rawdates`, decoded metadata, every nonzero xref object,
every trailer and `/Info` dictionary, every decoded stream, raw PDF bytes,
XMP or other metadata streams, annotations, outlines, visible text, and
extracted text.  Blank, alternate, duplicate, hidden, or differently spelled
date content is not absence.  The old raw value `D:20260825000000Z`, any
alternate build date, and any visible source date are absent.  No historical
rule requiring a raw date value is incorporated into R1.

After command 4 and before JSON finalization, render the accepted R1 root-A
PDF freshly at 200 dpi or higher into root A's
`r1-validation-staging` subtree.  Produce exactly 23 page images and inspect
every page individually at original review resolution.  Contact sheets may
aid navigation but never replace individual inspection.  Separately inspect
all theorem-critical displays, selector and cone pages, both carry and
survival arguments, visibility displays, quartic and recurrence pages,
modulo-five proof, `g=9` boundary, shifted-kernel comparison, limitations,
bibliography, and Tables 1--3.  Record zero clipping, crop, overlap, collision,
broken or missing glyph, unreadably small material, margin overflow, bad
display break, orphan heading, bad page break, blank/duplicate/missing page,
citation artifact, broken visible link, or anonymity leak.  Retain the
complete render manifest and images for R2.

Pagination and planning verdicts remain separate and must be recorded
truthfully, not normalized into one PASS:

- Abstract begins on page 1;
- the repaired boundary subsection and Section 9 begin on page 20;
- Conclusion is entirely on page 22;
- References begin and end on page 23; no appendix exists;
- the substantive span is pages 1--22;
- `hard_band_pass=true` for the 22--30 hard band;
- `preferred_band_pass=false` for the 24--28 preferred band; and
- `planning_target_pass=false` for the 26-page planning target, missed by
  four substantive pages under the accepted convention.

## 10. Strict R1 JSON syntax and independent semantic validation

All candidate scripts, records, parser code, semantic validators, and
validation results are created only after command 4 inside root A's
`r1-validation-staging` subtree and are retained there.  No candidate or
validator is staged in the project or a third root.

The exact required schema, artifact-id, and status triples are:

| Project artifact | `schema` | `artifact_id` | `status` |
|---|---|---|---|
| `paper/BUILD_METADATA_R1.json` | `PAPER23_BUILD_METADATA_R1_NO_OP_V1` | `paper23_build_metadata_r1_no_op` | `BUILD_METADATA_R1_NO_OP` |
| `paper/BUILD_RECEIPT_R1.json` | `PAPER23_BUILD_RECEIPT_R1_NO_OP_V1` | `paper23_build_receipt_r1_no_op` | `BUILD_R1_NO_OP_PASS` |

Each is compact strict-canonical UTF-8 JSON on exactly one physical line with
exactly one terminal LF.  Each has zero BOM, CR, NUL, invalid UTF-8,
insignificant whitespace, duplicate key at any depth, float, exponent,
nonfinite token, leading-zero integer, negative zero, unpaired surrogate,
noncanonical escape, trailing whitespace, trailing content, or second
record.  Numeric values are canonical decimal integers with arbitrary
precision.  Every object at every depth is ordered by increasing Unicode code
point; arrays retain semantic order; strings contain valid Unicode scalars
and use one canonical escape policy.  The exact candidate bytes, not an
abstract parsed tree, are the evidence object.

Each artifact's `self_identity` records its own exact project-relative path
and has `bytes:null` and `sha256:null`; no circular non-null self-hash is
allowed.  The receipt is generated only after the metadata candidate is
finalized and must bind the metadata's complete external candidate identity,
including path, SHA-256, byte count, LF, and canonical-round-trip result.

Together, without an unrecorded side ledger, the two JSON value trees must
contain named, unambiguous namespaces for and fully bind:

- this authorization's final external identity and terminal, its issuance
  provenance, both actual post-consumption governance identities and
  terminals, the exact build-open gate/queue, and the complete frozen
  48-file builder-opening manifest;
- the source trio, no-op ledger and receipt, window accounting, unchanged
  before/after identities, and every project/root source stability checkpoint;
- all four recovered-evidence namespaces, the complete six-artifact
  conjunction, four correction entries, eight suspended pointer/document
  pairs, eight syntax-only pointer/document pairs, three negative virtual
  hashes, no patched pair, and every explicit denial in Section 5;
- both permitted comparator roots and manifests, all four excluded-root
  denials, both new R1 roots and their creation/inventory/custody evidence,
  exact environment/commands/exits, all source/log/output identities, all
  A/B and cross-round comparisons, and the immutable project outputs;
- every live executable observation and its measurement provenance, wrapper
  chain, three-way hashes, stability decisions, historical comparator kept in
  its separate namespace, and independent semantic pointer comparisons;
- all log progression, closure, citation, label, reference, bibliography,
  bookmark, marker, PDF structure, security, date absence, font, page,
  pagination, render-manifest, page-by-page visual, and anonymity checks with
  exact observed counts and evidence;
- both strict syntax validators, both independent semantic validators, their
  code/runtime identities, adversarial suites, accepted controls, value-tree
  agreement, candidate hashes and round trips, and committed readback; and
- actual effective permissions, granted/denied authority, the logical
  persistence transaction, outcome, inventories, root retention, and zero
  network or external effects.

Before persistence, each exact JSON candidate must independently pass two
fresh syntax/parser-encoder implementations that share no parser, encoder, or
number-normalization code:

1. a duplicate-aware Python parser with integer-only hooks,
   arbitrary-precision integers, Unicode-scalar checks, and a separately
   written recursive Unicode-code-point canonical encoder; and
2. a handwritten Node recursive-descent parser with duplicate rejection at
   every depth, explicit BigInt integer semantics, surrogate/scalar checks,
   and its own recursive Unicode-code-point encoder.  Native `JSON.parse` or
   `JSON.stringify` alone is insufficient.

Each implementation must reproduce each candidate byte-for-byte, agree on
the complete value tree, and independently reject at least 33 adversarial
records.  The suite covers duplicate and escape-equivalent keys at multiple
depths, nested and astral key order, fractions, exponents, nonfinite forms,
integers beyond 2^53, leading zero, negative zero, BOM, invalid UTF-8, CR or
CRLF, missing/extra terminal LF, embedded LF, NUL/raw controls, insignificant
or trailing whitespace, trailing/multiple records, noncanonical escapes,
unpaired or malformed surrogates, truncated syntax, trailing comma, and
non-object top level.  Each also accepts a canonical nested non-ASCII control
containing positive and negative integers beyond 2^53 without precision loss.

Syntax validation is not semantic validation.  Two independently written
semantic validators, separate from the candidate generator and from each
other, must reopen all referenced project objects, post-consumption ledgers,
new roots, comparator objects, and executables; rehash/restat them; resolve
every required pointer; recompute inventories and comparisons; and prove that
the JSON observation fields equal live evidence.  Each independently checks
all four corrected values, eight suspensions, eight syntax scopes, all
namespace denials, and every live executable field.  Both validators must
pass before persistence and repeat on committed project bytes afterward.

## 11. Success-only logical transaction, failure, and retained custody

No success path may exist until both builds, every acceptance conjunct, both
JSON candidates, both syntax validators, and both semantic validators pass.
Stage the exact accepted PDF and finalized JSON candidates only inside root
A's validation subtree.  Immediately before persistence, repeat project,
governance, source, executable, comparator, and absence preflight.

Successful persistence is a **logical all-or-none** three-file transaction,
not a claim that an ordinary filesystem provides a crash-atomic multi-file
primitive.  Every creation uses exclusive-create/no-overwrite/no-follow and
must yield an ordinary root-owned mode-0644 regular file with link count one.
Commit in this order:

1. `paper/main_round1.pdf`, from the accepted staged R1 root-A PDF;
2. `paper/BUILD_METADATA_R1.json`, from the finalized validated metadata;
3. `paper/BUILD_RECEIPT_R1.json`, last, as the commit marker binding the
   finalized metadata external identity.

If any create, readback, identity, permission, or post-commit validator check
fails, remove only the partial paths created by this transaction before any
failure record.  That bounded rollback is part of the same one-shot
transaction; it is not a retry or permission to clean a build root or any
pre-existing object.  The receipt may never exist without the other two
validated members.  After all three creations, re-open and byte-compare every
member with its staged candidate, rerun both syntax and semantic validators,
and recheck the complete immutable boundary.

On success exactly those three paths and no blocker are added to the frozen
48-file opening universe.  The project is exactly 51 regular files, four
child directories, zero symlinks, and zero other objects.  The three PDFs
`paper/main.pdf`, `paper/main_round0.pdf`, and `paper/main_round1.pdf` are
directly byte-identical with SHA-256
`ae37679ef3ee4fa0b86f41e073f374920499f4959a196e289829e654b3d12d37`
and 492,452 bytes.  Every one of the 48 opening paths, all existing outputs,
all governance snapshots, and both comparator roots remains unchanged.

Any false, missing, ambiguous, drifting, or unrecorded conjunct after first
root creation is failure.  Failure leaves zero success paths.  The sole
optional project write is `notes/BUILD_R1_BLOCKER.md`, an ordinary root-owned
mode-0644 link-count-one regular file created with no-overwrite/no-follow and
ending exactly with the unique final nonempty line `R1_BUILD_BLOCKED`.  If
that optional factual blocker is persisted, the project inventory is exactly
49 regular files, four child directories, zero symlinks, and zero other
objects; if it cannot safely be persisted, the project remains the frozen
48-file opening universe and the builder reports the failure without another
write.  In every failure branch the three success paths are absent.

A pre-root mismatch creates zero root and zero project file and does not
exercise the authority.  A post-root failure consumes the authority whether
or not a blocker can be written.  There is no repair, source edit, candidate
patch, second root pair, resumed invocation, retry, cleanup of retained
evidence, replacement builder, or builder self-review.  Retain both fresh R1
roots privately and unchanged for a fresh, separately authorized R2 review.
Report complete root paths, manifests, executable observations, candidates,
validator identities/results, comparisons, disposition, project inventory,
and then stop.

## 12. Role separation and prohibited downstream effects

This authorization author, the no-op revision author, the corrected-R0 R1
reviewer, the parent consumer, the future R1 builder, and any later R2
reviewer are separate roles.  The builder cannot author its own review or
infer downstream authority from a clean output, an old PASS token, or this
authorization alone.

This note authorizes no manuscript or bibliography edit, further revision
window, theorem/proof/citation change, old-root access outside the two named
read-only comparators, excluded-root operation, R1 self-review, R2 review,
finalization, release, publication, submission, upload, public hosting,
repository action, messaging, identity disclosure, Paper 24 work, network
access, scientific experiment, or other external effect.

BUILD_AUTHORIZATION_R1
