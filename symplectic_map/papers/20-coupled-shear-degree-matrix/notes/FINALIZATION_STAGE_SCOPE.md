# Paper 20 Finalization Stage Scope

Date: 2026-08-22 UTC

Project: `papers/20-coupled-shear-degree-matrix`

Public title: **Coupled Hamiltonian Shear Degree Matrices in A4: An Asymmetric g>=5 Family**

## 1. Authority and exact present state

The page-fixed source and its independent R1/R2 source and build reviews are
stable. The retained final-manuscript review ends
`FINAL_MANUSCRIPT_INTEGRITY_PASS`; its two incorrect publication-review
size fields are superseded by
`notes/FINAL_MANUSCRIPT_INTEGRITY_R1_METADATA_CORRECTION.md`, which ends
`FINAL_MANUSCRIPT_INTEGRITY_METADATA_CORRECTION_AUTHOR_STOP`. The correct
publication-review identity is
`937612e3810c99eda8e9499abaa188b1d5b4d8421c7d8c260188d2d4b1481e02`,
8,742 bytes and 161 LF.

This scope freezes the exact corrected after-R2 universe and defines a
local-only finalization protocol. The governance author may write exactly this
scope and then `experiments/finalization_lock.json`, in that order, validate
them read-only, and stop. This role may not edit source, bibliography, any PDF,
receipt, earlier lock or review; copy a candidate; compile; clean temporary
residue; perform scientific execution; access the network; or cause submission,
upload, public hosting, repository push, external messaging, or identity
disclosure.

## 2. Exact frozen input universe F61

Immediately before this scope was created, `F61` was the complete project
universe: 61 regular non-symlink files, exactly four project-internal
directories (`experiments`, `notes`, `paper`, and `refine-logs`), zero
symlinks, and zero other entry types. The following safe project-relative paths
are unique and in lexicographic byte order. LF is the count of byte `0a`,
including for binary PDFs.

| Path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `experiments/EXPERIMENT_PLAN.md` | `a0ea0eb5b5ffae47cccac4ddc15f060b2fbeb695cd60930ce516718fc010ecba` | 2146 | 47 |
| `experiments/EXPERIMENT_TRACKER.md` | `562db5acb674e269cad5e3d17dfb8ff8673601f8411347817276c60e585f5a3f` | 1232 | 32 |
| `experiments/publication_lock.json` | `4559e4947613b70eda65523f83d5c1f369199c77852af3cc1940afa7ecbf0eff` | 12382 | 1 |
| `experiments/source_lock.json` | `57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581` | 11847 | 1 |
| `notes/BUILD_AUTHORIZATION_R1.md` | `7922b4102675762d2950bba76681dd5aaf3d42d6b0fa7efeef9af254628691ff` | 1698 | 25 |
| `notes/BUILD_AUTHORIZATION_R1_PAGEFIX.md` | `283136a59f6768321148ae52315e4f37906c8752c7977001ef4c55413837fd77` | 2792 | 54 |
| `notes/BUILD_AUTHORIZATION_R1_PAGEFIX_RETRY.md` | `6994e72d95239c5110abd5f032712e0ef2f5bfcb5e651ca6267d286e5272fd87` | 954 | 19 |
| `notes/BUILD_HARNESS_FAILURE_PAGEFIX.md` | `7c51ebb42ab6433f1e0985dc6f1dec894e2342dbaacd6f93d65b60b7c15e78f5` | 922 | 23 |
| `notes/CITATION_VERIFICATION.md` | `bb075a0d7918603062795be88a1adcae932e4d550d0b544e46030f51207fe832` | 5723 | 48 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `7275171195b4aa2d95df1b4d701b6ae43a5e17778b7f3ce6b94027172e7d4f92` | 5607 | 48 |
| `notes/FINAL_MANUSCRIPT_INTEGRITY_R1.md` | `181159fa04aa03fa1c8ba4dd92f08061e6d112b6b1555faf30e5d54e04f8eaf1` | 8635 | 152 |
| `notes/FINAL_MANUSCRIPT_INTEGRITY_R1_METADATA_CORRECTION.md` | `e6791c117c48785e31eabe58f4349e59b0b8d270e662ab0281760b921e6d3404` | 3915 | 83 |
| `notes/INDEPENDENT_BUILD_R1_PAGEFIX_REVIEW.md` | `4bdd207d13572bd8a85aeafc32443c6a33555185e1a6ad0dddf96b7a3155da1e` | 8220 | 152 |
| `notes/INDEPENDENT_BUILD_R1_REVIEW.md` | `5668d444588ac942e5d84e1e278948986a9d42777088273c45e706d10e213b1f` | 4404 | 83 |
| `notes/INDEPENDENT_BUILD_R2_PAGEFIX_REVIEW.md` | `adbf7a25b252706a6a02deec6fc517fd21b46504c606bb391932981f332b9da3` | 8447 | 167 |
| `notes/INDEPENDENT_BUILD_R2_REVIEW.md` | `c999c54bb0faf551303a7367393f42999b13deec7b890df2ed372acff1100228` | 4295 | 89 |
| `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | `436fe8c2159dbcdde3dbdb6865746d0bfcb19627c68301ad98cf43cd86c50c91` | 6852 | 188 |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_BIB_REVIEW.md` | `3f28c58a33b82337b560d18f0eddb6bad80f53027f8a223460a34b40da938f68` | 6311 | 131 |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_EXPANDED_REVIEW.md` | `072f52c74c5131b47cb65e096063a04e785749e3801945209d9b8e31cf6596d6` | 3885 | 75 |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_FINAL_BIB_REVIEW.md` | `daff23ef415450f9547a57f944e4a03d6659936b20434d9c76f163abfe5745d2` | 6099 | 124 |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_FINAL_EXPANDED_REVIEW.md` | `0eb9a4c6ccb5072e0f22c415624708ad98f9831a693e0bddce12ec9615d33795` | 4205 | 77 |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_PAGEFIX_REVIEW.md` | `e83053d521542773696a59478944d8974b46b97b5b854cb7c775cc257cb2ee30` | 9340 | 181 |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md` | `8deca3d4b885d867efe8b866d7d59f5fe4cdc66af5d9ae8f9dda3e06a7c7a7d6` | 7569 | 149 |
| `notes/INDEPENDENT_PAPER_SOURCE_R2_BIBFIX_CORRECTION.md` | `16f24243c6dbd933f75bd0e7a2848578b2c939a764d9be2c9532355ae7aeff47` | 2373 | 54 |
| `notes/INDEPENDENT_PAPER_SOURCE_R2_BIBFIX_REVIEW.md` | `eb09c1f8f2a53fa0e9e9c38c4201ded1ec401053a5fc71bc942764cec09c81fe` | 3780 | 74 |
| `notes/INDEPENDENT_PAPER_SOURCE_R2_EXPANDED_REVIEW.md` | `c8577478750944d742c67fe2652c8f978f848e0f4e938818ffdd31c11619bbf6` | 6190 | 117 |
| `notes/INDEPENDENT_PAPER_SOURCE_R2_FINAL_EXPANDED_REVIEW.md` | `bcbf13754e6be43e6943be96d97eb8ab9d92c8703ae9cfae224cc6cba9aca077` | 7238 | 122 |
| `notes/INDEPENDENT_PAPER_SOURCE_R2_FINAL_REVIEW.md` | `c333970193257d598035342a375cdbbc773ee2ee5cdca955f3b5791fdd423a58` | 3242 | 68 |
| `notes/INDEPENDENT_PAPER_SOURCE_R2_PAGEFIX_REVIEW.md` | `e81e148cc8e9d4b220a62146a6bebb906df0cdb4fb5e555eca423e8ef2a8eaa5` | 9803 | 177 |
| `notes/INDEPENDENT_PAPER_SOURCE_R2_REVIEW.md` | `1ad8aecb522928da9047bf872cd89b191c448b37a74733ef5ce2c10c390a7cf3` | 6596 | 137 |
| `notes/INDEPENDENT_PAPER_SOURCE_R2_REVIEW_REPAIRED.md` | `2096d3ab58975f283b09ca445a5030d59ecb8ace9dc488db91b91620f0f576f5` | 5977 | 117 |
| `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | `937612e3810c99eda8e9499abaa188b1d5b4d8421c7d8c260188d2d4b1481e02` | 8742 | 161 |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | `c4f456c8d9aee5ac9364abf91dc140e9a0261b09cf1922491a773e8c7d87f2c5` | 9484 | 213 |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | `b6ba83186b7e8c5db548376c5478260bb6d1b3e3d84d8ff0944f641c185a513a` | 6513 | 158 |
| `notes/NOVELTY_ASSESSMENT.md` | `762bd9352641feffe6db5b9426d4a7b657509d7fb6bb9b065b32e7be391d9a2b` | 5840 | 102 |
| `notes/PROOF_PACKAGE.md` | `c111c75a11714c7b401583fdc459549ab4c0f783a1064112b495794e2e7e4baa` | 9407 | 269 |
| `notes/PUBLICATION_STAGE_SCOPE.md` | `875c615b00aa98ffc3a290548582762fc321907d19ed338741de58456b2133e2` | 14472 | 299 |
| `notes/RESEARCH_QUESTION.md` | `eee1350eeefb818f240328493a16d3036df7bdb028a86016594bb8e26d956b86` | 5150 | 88 |
| `notes/SOURCE_PAGEFIX_AUTHORIZATION_R1.md` | `2043428f4a18dc1a980d122bb98273fa7d6fd89410f8e7eb68d1eeb5b51d20a8` | 1095 | 22 |
| `notes/SOURCE_REPAIR_RECEIPT_R1_LEDGER.md` | `7e8e73fd994c43fc35f7021669e4e744ab7f137a4977e240cac2925f7f535c2e` | 1334 | 25 |
| `paper/BUILD_METADATA_R0.json` | `75e94cc9da7dd738fd287db32994fb98863d65c00350201ac6c77e48d017cc9c` | 3588 | 1 |
| `paper/BUILD_METADATA_R1.json` | `b891b8bb81d6383fc4b49fb81f41c346ecafbbd9663a25b44e7eb6bb8badf8dd` | 5549 | 1 |
| `paper/BUILD_RECEIPT_R0.json` | `3e7da7d9b66c02f68864d04c177ff12317e52d87b3c38c7fc8748f95ca9e4d62` | 4259 | 1 |
| `paper/BUILD_RECEIPT_R1.json` | `0c0ce98b3ee4349d269aaebacf78d89ad237aec4f36595a02d268c2fdf78cc31` | 11325 | 1 |
| `paper/PAPER_PLAN.md` | `4dfcf82f8dae85502fced2f7b1d73d80e35ee242eee609dd74b5f59ca793adf3` | 22064 | 397 |
| `paper/SOURCE_REVISION_RECEIPT_R1.json` | `d8600e8d50efcda1b694e332a5b4282beb8b6c9ad9b5f302199f6f1aba728d3a` | 6206 | 1 |
| `paper/main.aux` | `8091490a70a1be36670f587819f590f2c68411f9efc31ad01a70b06d896c2c76` | 8199 | 104 |
| `paper/main.bbl` | `15c4662bc3e3c6b65eef8a8b80d7f8210da9b8b3011a9ba5c5896504adff81f6` | 2282 | 56 |
| `paper/main.blg` | `3292543c220a005dc56db3fdaf1287cd9f142cc52b2d0db012f4da156ae66e15` | 900 | 46 |
| `paper/main.log` | `56fade7e27ce973b59d4c63b6da8b46d97001aa78240e261a75cdf4f3fc2f9a4` | 28801 | 734 |
| `paper/main.out` | `d4b7a073fb0241e34f3579b979b531378ac3b0b0118415a7e101d06178d91793` | 4875 | 23 |
| `paper/main.pdf` | `ed58824860f77186210fee298b1631e7877868dc828b4b3a9cd048fcaa1545e9` | 380574 | 2049 |
| `paper/main.tex` | `b891987e42396981b3859d2aaeb00b39b8281ccb559ef9d6383200a1e8682b90` | 61835 | 1619 |
| `paper/main_round0.pdf` | `ed58824860f77186210fee298b1631e7877868dc828b4b3a9cd048fcaa1545e9` | 380574 | 2049 |
| `paper/main_round1.pdf` | `07426e1892fbbb85876a6f79401318c16f9d3aee96ae7d6ae2b087a25ca98e40` | 429723 | 2338 |
| `paper/main_round1_failed_pre_pagefix.pdf` | `e40b4b44a3a8fa7e1102efdbc615476a9fa038cf146777838de6b9e0b5cb24f9` | 424691 | 2329 |
| `paper/math_commands.tex` | `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582` | 702 | 20 |
| `paper/references.bib` | `529612c446e0a56919efb79dae7f80358f4f3fa1fc3424e6e15f7da2886c5eaf` | 2335 | 73 |
| `refine-logs/FINAL_PROPOSAL.md` | `186036967ecda1f8ba82f61c6b5d3ea086b010693a54476391512dba482a8ee5` | 4156 | 100 |
| `refine-logs/INITIAL_PROPOSAL.md` | `48bec53019c21662033e9e3dbef6f180d60e6868d1f5169dbf2643604bc0fb2e` | 3447 | 88 |
| `refine-logs/REVIEW_SUMMARY.md` | `838bf872a4902fbd193d3045972a518fda55d059c0892f1080e6e352ccb1f1fa` | 2708 | 51 |

## 3. Authoritative source, candidate, and historical artifacts

The frozen source trio is exactly:

- `paper/main.tex`: `b891987e42396981b3859d2aaeb00b39b8281ccb559ef9d6383200a1e8682b90`,
  61,835 bytes / 1,619 LF;
- `paper/math_commands.tex`:
  `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582`,
  702 bytes / 20 LF;
- `paper/references.bib`:
  `529612c446e0a56919efb79dae7f80358f4f3fa1fc3424e6e15f7da2886c5eaf`,
  2,335 bytes / 73 LF.

Title lineage is disclosed rather than normalized silently. The retained
strict-canonical source lock's historical top-level governance string is
exactly `Coupled Hamiltonian Shear Degree Matrices in A^4: An asymmetric
g>=5 family`. Its lowercase `asymmetric` / `family` is a frozen early label,
not the rendered display title. The later TeX source, build metadata, reviewed
PDF, this scope, and every future release object use the authoritative display
title `Coupled Hamiltonian Shear Degree Matrices in A4: An Asymmetric g>=5
Family` (with mathematical `A^4` and `g\geq 5` in TeX). The historical lock
byte remains unchanged and fully bound; the capitalization difference changes
no theorem or candidate byte.

The only candidate input is `paper/main_round1.pdf`, SHA-256
`07426e1892fbbb85876a6f79401318c16f9d3aee96ae7d6ae2b087a25ca98e40`,
429,723 bytes / 2,338 LF / 23 pages. The future
`paper/main_release_candidate.pdf` must be an exclusive raw byte copy of this
file with no compile, transform, metadata rewrite, optimization, signing, or
rendering.

`paper/main.pdf` and `paper/main_round0.pdf` are retained historical
14-page R0 artifacts at `ed58824860f77186210fee298b1631e7877868dc828b4b3a9cd048fcaa1545e9`.
`paper/main_round1_failed_pre_pagefix.pdf` is a retained historical failed
22-page artifact at `e40b4b44a3a8fa7e1102efdbc615476a9fa038cf146777838de6b9e0b5cb24f9`.
None is a final candidate; no later object may claim equality between them and
the release candidate.

## 4. Monotone project universes

Each role must enumerate and rehash its complete predecessor universe:

- `F61`: the 61 frozen inputs above;
- `G63 = F61 + {notes/FINALIZATION_STAGE_SCOPE.md,
  experiments/finalization_lock.json}`;
- `P64 = G63 + {notes/INDEPENDENT_FINALIZATION_STAGE_REVIEW.md}`;
- `R66 = P64 + {paper/main_release_candidate.pdf,
  paper/FINAL_RELEASE_MANIFEST.json}`;
- `Q67 = R66 + {paper/TERMINAL_REBUILD_RECEIPT.json}`;
- `T68 = Q67 + {paper/reviews/final_integrity_review.md}`.

The only expected new project directory is `paper/reviews`, created by the
sole terminal reviewer after every check and cleanup pass. No future path may
be pre-created, no earlier byte may change, and no symlink may be followed.

## 5. Closed temporal roles

1. **Finalization-governance author.** Reads F61; writes only this scope and
   the strict-canonical finalization lock; validates; stops.
2. **Independent finalization reviewer.** Distinct from the governance author
   and author of none of G63; reads and rehashes exact G63 and the bound live
   temporary-residue snapshot. On success writes only
   `notes/INDEPENDENT_FINALIZATION_STAGE_REVIEW.md`, ending exactly
   `FINALIZATION_STAGE_PASS`; on any blocker writes nothing.
3. **Release-candidate author.** Distinct from the first two roles; reads exact
   P64; exclusively creates the raw-copy candidate from `main_round1.pdf`,
   then writes only strict-canonical `paper/FINAL_RELEASE_MANIFEST.json`;
   stops. Every external-effect field remains false.
4. **Terminal-build evidence author.** Distinct from prior roles; reads exact
   R66; creates two fresh root-owned mode-0700 directories matching
   `/tmp/p20-paper20-terminal-A-XXXXXX` and
   `/tmp/p20-paper20-terminal-B-XXXXXX`; records their empty initial state;
   copies only the frozen source trio; executes exactly
   `pdflatex -interaction=nonstopmode -halt-on-error main.tex`,
   `bibtex main`, and the same pdflatex command twice more, under
   `SOURCE_DATE_EPOCH=1787356800`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`,
   `LC_ALL=C`, `LANG=C`, and `PATH=/usr/bin:/bin`. It writes only the
   strict-canonical terminal receipt and leaves both roots live.
5. **Sole terminal-integrity reviewer.** Fresh and distinct from all four
   roles; authored none of Q67. It independently rehashes Q67, both fresh
   roots, and every historical residue target bound below; audits diagnostics,
   PDF security/metadata/fonts/text/rendering, theorem spine, citations,
   anonymity, and all role/effect fences. Only after every check passes may it
   no-follow unlink the exact validated files and rmdir exact emptied
   directories, then create `paper/reviews` and write only
   `paper/reviews/final_integrity_review.md`, whose final two nonempty lines
   are exactly `FINAL_INTEGRITY_PASS` and `RELEASE_CONFIRMED`.

## 6. Exact historical residue targets

The lock must bind the complete live snapshot of these seven literal
directories and six literal files; the two future terminal roots join this
closed cleanup set after the terminal build.

| Existing directory target | Mode | Direct regular children |
|---|---:|---:|
| `/tmp/p20-paper20-r1-pagefix-retry-A-ev483m` | 0700 | 13 |
| `/tmp/p20-paper20-r1-pagefix-retry-B-s4iTTx` | 0700 | 13 |
| `/tmp/p20-paper20-r1-pagefix-A-JBuZF3` | 0700 | 7 |
| `/tmp/p20-paper20-r1-pagefix-B-w344h4` | 0700 | 7 |
| `/tmp/p20-paper20-r1-A-7GEBaI` | 0700 | 13 |
| `/tmp/p20-paper20-r1-B-rx5cFc` | 0700 | 13 |
| `/tmp/p20-failed-r0-20260822` | 0755 | 5 |

The six existing literal regular-file targets are:

- `/tmp/p20-build-r0-command-1.log`;
- `/tmp/p20-build-r0-command-2.log`;
- `/tmp/p20-build-r0-command-3.log`;
- `/tmp/p20-cites.txt`;
- `/tmp/p20-labels.txt`;
- `/tmp/p20-main-text.txt`.

At governance freeze all 77 residue files are root-owned, non-symlink regular
files; all seven directories are literal children of real `/tmp`, root-owned,
non-symlink directories, with no subdirectories, symlink children, or other
entry types. Their exact names, modes, sizes, LF counts, and digests are bound
in the finalization lock.

Cleanup is forbidden until the sole terminal review. That reviewer must first
revalidate literal path, real parent `/tmp`, entry type, owner, mode, exact
child set, bytes/LF/digest, absence of symlinks and subdirectories, and
project-tree immutability. It then unlinks each individually named non-symlink
file and uses `rmdir` only on an empty exact directory. Recursive deletion,
globs, wildcards, unresolved variables, broad targets, symlink traversal, and
cleanup of any unbound path are forbidden.

## 7. Manifest, terminal receipt, and terminal checks

The release manifest binds every non-self file in exact R66, declares its own
path with hash/byte self-exclusion, records the raw-copy provenance and full
dependency chain, distinguishes all three historical PDFs from the candidate,
and keeps every external effect false.

The terminal receipt binds exact R66, both literal root paths, their empty
initial states and complete postbuild snapshots, all eight command exits and
command-stream identities, A/B correspondence, and exactly four-way equality
`root A PDF = root B PDF = paper/main_round1.pdf =
paper/main_release_candidate.pdf`. It must explicitly record inequality from
the historical R0 and failed pre-pagefix PDFs. Expected final PDF facts are 23
pages; conclusion through page 22 with References beginning on page 22; zero
fatal errors, undefined citations/references, BibTeX warnings, overfull boxes,
or unresolved markers; the retained nonfatal warning/underfull counts must be
measured rather than assumed. All fonts must be embedded, subsetted, and
Unicode-mapped. The receipt status before sole review is exactly
`TERMINAL_REBUILD_PASS_PENDING_INDEPENDENT_ROOT_AUDIT`.

The sole reviewer must additionally check no encryption, JavaScript,
attachments, forms, raster-image surprise, private path/hash/agent/lifecycle
leak, or public identity beyond `Anonymous Authors`; inspect all 23 rendered
pages for clipping, corruption, blank-page surprise, illegible formulas, and
citation/reference defects; and verify the theorem's characteristic-zero,
integer `g>=5`, matrix, Perron-root, degree, and anti-claim boundaries against
the frozen source and reviews.

## 8. Canonical JSON and terminal effect

The lock, manifest, and receipt use UTF-8 strict canonical JSON: recursive
Unicode code-point key order, compact `,:` separators, no BOM/CR/NUL,
duplicate keys, or nonfinite numbers, and exactly one terminal LF. Each
self-referential artifact declares a safe project-relative own path and
excludes its own hash and byte count.

The only possible terminal effect after sole-review PASS is
`LOCAL_ANONYMOUS_RELEASE_ONLY`. Submission, upload, public hosting,
repository push, external messaging, identity disclosure, network access, and
all scientific execution remain false and unauthorized.

## 9. Pre-review title-lineage governance recovery

A zero-write read-only preflight completed before any independent finalization
review began. It confirmed all F61 bytes and residue snapshots but required the
source-lock capitalization lineage to be stated explicitly. The governance
author therefore amended only this scope and rebound only the self-excluded
lock before opening the review gate. The first scope was
`597d351ca37dc31dd250bc7cf49e8a1b869b4084b71f009eadaf70dd8a7ba0f4`
(17,490 bytes / 261 LF), and its first lock was
`38636e0fc5938782cd6e799486a864eea86b533a7c6418fc88d3ae365725154e`
(33,714 bytes / one LF). The first amended scope was
`efee7e79593a9d21ee5756f775476395f0563cfc6e1b577a95b773e94e244cbd`
(18,203 bytes / 271 LF), and its rebound lock was
`48889009db039417b171569bb7fceb4cc226cbe5a539fdf3fa92662077c761b4`
(34,143 bytes / one LF). These transient identities are process history only;
they grant no authority and are superseded by the live pair. No F61 byte,
residue byte, source, PDF, theorem, stage count, role, cleanup rule, or effect
field changed.

FINALIZATION GOVERNANCE SCOPE AUTHOR STOP
