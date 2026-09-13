# Final terminal-integrity review

## Review identity and disposition

I acted as the fresh, sole terminal-integrity reviewer for Paper20. I authored none of the Q67 predecessor universe and did not serve as its governance author, finalization reviewer, release-candidate/manifest author, or terminal-build evidence author. My authority was limited to a read-only independent audit, the exact cleanup authorized by the finalization lock after every gate passed, and this one review file.

The audit used the paper-compilation review workflow only for read-only prerequisite, log, bibliography, PDF, font, metadata, security, and rendering checks. I performed no build, source edit, PDF transformation, CAS or numerical experiment, network access, transport, upload, submission, repository push, public hosting, external message, or identity disclosure. The effect ceiling is, and remains, `LOCAL_ANONYMOUS_RELEASE_ONLY`.

No blocker was found. Cleanup was not started until every Q67, historical-residue, live-root, PDF, visual, scientific, citation, anonymity, governance, role-separation, and effect-firewall check below had passed.

## Q67 tree and cryptographic binding audit

The pre-cleanup project tree was exactly Q67: 67 regular files, four internal directories (`experiments`, `notes`, `paper`, and `refine-logs`), zero symlinks, and zero other entries. The project root and all four internal directories were real nonsymlink directories owned by uid/gid 0/0. `paper/reviews` and this review path were absent.

I captured a complete external snapshot containing the root/directory metadata and every Q67 file's path, mode, uid, gid, byte count, and SHA-256. It had 72 LF-terminated rows, 7,884 bytes, and SHA-256 `53f67faeae9fe5bf964896ed1640668dd9af71debd258182b945707d523ab07b`. The snapshot was byte-identical immediately before governed cleanup and immediately after cleanup. The external snapshot was then deleted with an exact no-follow unlink before this project write.

All ten JSON files decoded as strict UTF-8 and passed duplicate-key rejection, nonfinite-number rejection, BOM/CR/NUL rejection, recursive Unicode-codepoint key ordering, compact separators, exact decode/re-encode round trip, and exactly one terminal LF. The three self-excluded artifacts had null byte/hash self-fields and `terminal_lf_count: 1`; their actual independently measured identities were:

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `experiments/finalization_lock.json` | 34,833 | `3b1098c48b6d1b2a4a0f8cf0319aefb8fe6cf1ab4db16baf7fdd9bd345eae842` |
| `paper/FINAL_RELEASE_MANIFEST.json` | 24,086 | `422d278b72b606e4c3e0fb1463f1a6d24f78dc9dc5d449b05681ccb086bc4316` |
| `paper/TERMINAL_REBUILD_RECEIPT.json` | 36,799 | `3d9d5152f7cc970d27face326a87d9c17a0b34e6ccc8ecc95e82de643010c8e2` |

I independently re-enumerated and rehashed every binding, including bytes and LF counts:

- the finalization lock's exact F61 universe: 61 of 61 bindings passed;
- the release manifest's self-excluded 65-file binding contract: 65 of 65 passed, with a nonempty role for every path;
- the terminal receipt's self-excluded R66 precondition: 66 of 66 passed, and all 65 inherited manifest roles agreed exactly;
- manifest self-exclusion and terminal-receipt self-exclusion were exact, with no missing, additional, duplicated, unsafe, absolute, or parent-traversing project path.

The stage lineage and dependency DAG were exact: F61 -> G63 -> P64 -> R66 -> Q67 -> T68, with file counts 61, 63, 64, 66, 67, and 68. G63 adds the finalization scope and lock; P64 adds the independent finalization review; R66 adds the raw-copy candidate and self-excluded manifest; Q67 adds the self-excluded terminal receipt; T68 adds only `paper/reviews/final_integrity_review.md` and its necessary `paper/reviews` parent.

The authoritative governance terminals were present as the last nonempty lines of their bound files: `SOURCE_LOCK_PASS`, `PAPER_PLAN_PASS`, `PUBLICATION_STAGE_PASS`, both source page-fix passes, both build page-fix passes, `FINAL_MANUSCRIPT_INTEGRITY_PASS`, the metadata-correction author stop, the finalization-scope author stop, and `FINALIZATION_STAGE_PASS`. The bound finalization scope, lock, and independent finalization review rehashed to `52ea249aed4ae377cc8be5ebf6e056ae2d9bc3d3b16abe1e56e374412be3d151`, `3b1098c48b6d1b2a4a0f8cf0319aefb8fe6cf1ab4db16baf7fdd9bd345eae842`, and `a09e620e3fb2cf215702db929017c109b78c6ca1dfd0bac70cbe003ac0b278fe` respectively.

The two disclosed superseded governance pairs, the statement that independent finalization review had not started, and the `theorem_source_candidate_or_effect_changed: false` recovery fact were consistent across the scope, lock, review, manifest, and receipt. Historical R0 source identities inside the R0 metadata/receipt were correctly treated as predecessor records; the R1 source-revision chain supersedes them and binds the current source trio.

The metadata-correction chain also passed. The corrected publication review and the superseding correction note rehashed to `937612e3810c99eda8e9499abaa188b1d5b4d8421c7d8c260188d2d4b1481e02` and `e6791c117c48785e31eabe58f4349e59b0b8d270e662ab0281760b921e6d3404`. The disclosed historical source-lock title, authoritative display title, and short PDF metadata title were distinct only as documented; `substantive_change` and theorem/candidate-byte change were false. The authoritative public title is “Coupled Hamiltonian Shear Degree Matrices in A4: An Asymmetric g>=5 Family,” while the PDF metadata title is “Coupled Hamiltonian Shear Degree Matrices in A4.”

Every external-effect flag in the finalization lock, manifest, and terminal receipt was false. Their permission firewalls forbade external release, source edits, cleanup before this review, experiments, scientific execution, CAS, transport, upload, submission, and publication outside the local anonymous boundary.

## Candidate and historical PDF identities

`paper/main_release_candidate.pdf` is an exact raw-byte copy of `paper/main_round1.pdf`: 429,723 bytes, 2,338 LF bytes, 23 pages, and SHA-256 `07426e1892fbbb85876a6f79401318c16f9d3aee96ae7d6ae2b087a25ca98e40`. No compile, rendering, optimization, signing, transformation, metadata rewrite, or overwrite of a historical PDF occurred in candidate creation.

The current historical `paper/main.pdf` remained byte-identical to `paper/main_round0.pdf`, with 380,574 bytes, 2,049 LF bytes, 14 pages, and SHA-256 `ed58824860f77186210fee298b1631e7877868dc828b4b3a9cd048fcaa1545e9`. It is not the release candidate. The failed pre-page-fix PDF remained a distinct 22-page historical artifact, 424,691 bytes and SHA-256 `e40b4b44a3a8fa7e1102efdbc615476a9fa038cf146777838de6b9e0b5cb24f9`.

## Historical residue: complete locked snapshot

Before any deletion, I audited all seven finalization-lock-bound historical directories and all six bound top-level files directly under literal `/tmp`. Each parent resolved to real `/tmp`; every top target was the bound nonsymlink type; every direct leaf was a root-owned, nlink-1, regular nonsymlink file; and every name, mode, uid/gid, byte count, LF count, and SHA-256 matched the full lock snapshot. There were exactly 71 directory leaves plus six top-level files, hence 77 historical files and 13 historical top-level targets, with no additional child, subdirectory, symlink, or other entry.

The directory inventories were:

| Literal directory | Mode; uid/gid; stat bytes | Exact direct inventory | Leaves | Verified ledger SHA-256 |
|---|---|---|---:|---|
| `/tmp/p20-paper20-r1-pagefix-retry-A-ev483m` | 0700; 0/0; 4096 | standard 13-leaf build set | 13 | `abf98a75f4f09698844eee47c261991637f3ea5fd2903192b43370184f3f47ee` |
| `/tmp/p20-paper20-r1-pagefix-retry-B-s4iTTx` | 0700; 0/0; 4096 | standard 13-leaf build set | 13 | `68c97f0eeea1f8f4c8b8fe2d200a984a10d03ee00211f4aa035264a2bfb5cde9` |
| `/tmp/p20-paper20-r1-pagefix-A-JBuZF3` | 0700; 0/0; 185 | four command logs plus source trio | 7 | `4f2e1ca92965448f05683fe11d73e90ddba88ee2931504b1d308b8c93cfa4de3` |
| `/tmp/p20-paper20-r1-pagefix-B-w344h4` | 0700; 0/0; 185 | four command logs plus source trio | 7 | `0637e2219d05e3bad55dd5974c4cf92b001aed4f30292ab5208e0336cde96c92` |
| `/tmp/p20-paper20-r1-A-7GEBaI` | 0700; 0/0; 4096 | standard 13-leaf build set | 13 | `9b4a91dfc7e79bc71c533fc23df0b80c01610208c7c3a151ca248e67fa92d09c` |
| `/tmp/p20-paper20-r1-B-rx5cFc` | 0700; 0/0; 4096 | standard 13-leaf build set | 13 | `0db29a5d8692451764ba0e23ec938eb19d019a4ae8b3742999ac02b055ff2220` |
| `/tmp/p20-failed-r0-20260822` | 0755; 0/0; 110 | `main.aux`, `main.bbl`, `main.blg`, `main.log`, `main.out` | 5 | `1d3660ed88a5a781221652b8452ad220f90dc9b6a60ec579afce39b85d4d80c7` |

The standard 13-leaf build set was exactly `command-1.log` through `command-4.log`, `main.aux`, `main.bbl`, `main.blg`, `main.log`, `main.out`, `main.pdf`, `main.tex`, `math_commands.tex`, and `references.bib`. The source trio was exactly `main.tex`, `math_commands.tex`, and `references.bib`. The reviewer ledger digest over all 77 historical rows was `5dc25aab20bb953a06710bacd41a36fd9e1479967c9a571126817e3abbfc523b`.

The six individual top-level file identities were:

| Literal file | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `/tmp/p20-build-r0-command-1.log` | 12,943 | 368 | `8338909c7f6dd779890f5e53b7d24ae54b2818f50b57b949e8142168056d67bd` |
| `/tmp/p20-build-r0-command-2.log` | 158 | 4 | `7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9` |
| `/tmp/p20-build-r0-command-3.log` | 8,169 | 186 | `1d53b8542c228250a42dc08502677a5c274a0e4dbae526d80446ebbcd5b8767c` |
| `/tmp/p20-cites.txt` | 286 | 9 | `cd9474bf43d6567ff170f382db9eedc7a97d37618036c3caf2191ef718056210` |
| `/tmp/p20-labels.txt` | 1,513 | 67 | `2a0192a84106cd17ec30cd8bca2d3285b18fbf7e941b5d94372d39d397917678` |
| `/tmp/p20-main-text.txt` | 43,383 | 739 | `a690d5478e1a2da1817db1c11ec10a6fade9bf408993c0cfcc8ef13fd20b5a6e` |

## Live terminal roots and deterministic build evidence

I directly audited `/tmp/p20-paper20-terminal-A-MuAi0H` and `/tmp/p20-paper20-terminal-B-RE7KpW`. Each was a literal, real, root-owned uid/gid 0/0, mode-0700 nonsymlink directory whose real parent was `/tmp`. Each had exactly the same 13 regular, root-owned, mode-0644, nlink-1 nonsymlink direct children, with no subdirectory, symlink, or other entry. All 13 corresponding A/B files were byte-identical. The combined 26-row reviewer ledger digest was `f536f64e4a3c1e328a4666898733aa3d4fc285f3717e5c61b9b6354da245785a`.

The complete common leaf inventory was:

| Leaf in both A and B | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `command-1.log` | 14,846 | 456 | `8f824c515e693797908825336799895733a3fd36e359dda2d751d1b6296e2568` |
| `command-2.log` | 158 | 4 | `7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9` |
| `command-3.log` | 9,446 | 204 | `85ea55997be36d466b2e9d45dbbe8a86aaf7d4032448da4e17b5963e5dd0e5fb` |
| `command-4.log` | 8,071 | 142 | `bd5b14c904c7d25046ff81cd2d28235f75add86b56a930b87e62c4cbbd4724bb` |
| `main.aux` | 11,920 | 139 | `a96b8a6d534c04f897581590f431164f75f600ee0c85ce062cdc33ad617a8d16` |
| `main.bbl` | 2,282 | 56 | `15c4662bc3e3c6b65eef8a8b80d7f8210da9b8b3011a9ba5c5896504adff81f6` |
| `main.blg` | 900 | 46 | `3292543c220a005dc56db3fdaf1287cd9f142cc52b2d0db012f4da156ae66e15` |
| `main.log` | 28,899 | 734 | `34bf450186dfc29b4355ade433de214f48daf09efb724e0941a32456a6b5771f` |
| `main.out` | 5,653 | 25 | `9cfe3093cc76d9ea5da78ad4dc35e3701dcbd91e14031ba6052e937212f12fa2` |
| `main.pdf` | 429,723 | 2,338 | `07426e1892fbbb85876a6f79401318c16f9d3aee96ae7d6ae2b087a25ca98e40` |
| `main.tex` | 61,835 | 1,619 | `b891987e42396981b3859d2aaeb00b39b8281ccb559ef9d6383200a1e8682b90` |
| `math_commands.tex` | 702 | 20 | `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582` |
| `references.bib` | 2,335 | 73 | `529612c446e0a56919efb79dae7f80358f4f3fa1fc3424e6e15f7da2886c5eaf` |

The exact isolated environment was `FORCE_SOURCE_DATE=1`, `LANG=C`, `LC_ALL=C`, `PATH=/usr/bin:/bin`, `SOURCE_DATE_EPOCH=1787356800`, and `TZ=UTC`, with no HOME declaration/reset and no network access. Each root ran exactly:

1. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
2. `bibtex main`
3. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
4. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`

All eight exits were zero and all eight command-log identities matched the receipt. The independently recounted per-command diagnostics, equal in A and B, were:

| Pass | Warning lines | Undefined-citation lines | Undefined-reference lines | Underfull | Overfull | Fatal/emergency |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 86 | 15 | 65 | 3 | 0 | 0 |
| 2 (BibTeX) | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | 20 | 15 | 0 | 3 | 0 | 0 |
| 4, final | 5 | 0 | 0 | 3 | 0 | 0 |

The pass-1/pass-3 undefined counts include the corresponding “there were undefined ...” summary line, exactly as the receipt specifies. The final pass had zero unresolved citation/reference lines, zero overfull boxes, and zero fatal/emergency lines. Its eight actual nonblocking diagnostics were three underfull boxes with badness 1776, 1072, and 1565, four hyperref PDF-string warnings, and one label-rerun warning. BibTeX had zero warnings and zero errors.

Both terminal PDFs, `paper/main_round1.pdf`, and `paper/main_release_candidate.pdf` were a four-way byte match at SHA-256 `07426e1892fbbb85876a6f79401318c16f9d3aee96ae7d6ae2b087a25ca98e40`.

## Independent PDF, bibliography, anonymity, and visual audit

Independent `pdfinfo`, Poppler font/image/attachment tools, raw-token scans, and Ghostscript checks established:

- 23 pages, PDF 1.5, letter size 612 x 792 points, rotation zero, and no parser suspect;
- title `Coupled Hamiltonian Shear Degree Matrices in A4`, author `Anonymous Authors`, creator `LaTeX with hyperref`, and producer `pdfTeX-1.40.22`;
- deterministic raw creation and modification dates `D:20260822000000Z`;
- exactly 25 font records, with 25/25 embedded, 25/25 subset, and 25/25 Unicode;
- zero images and zero embedded files; no JavaScript, form, encryption, signature, launch action, open action, or active `/AA`, `/AcroForm`, `/EmbeddedFiles`, `/JS`, `/JavaScript`, `/Launch`, `/OpenAction`, `/Type /Sig`, or `/ByteRange` token;
- a clean Ghostscript null-page parse.

The source has exactly `\author{Anonymous Authors}`, no `\thanks`, affiliation/address/email command, acknowledgment heading, or email address. The first rendered page and PDF metadata both say `Anonymous Authors`. The source trio and extracted PDF text had zero hits for `[VERIFY]`, `[?]`, `??`, `TODO`, `FIXME`, `XXX`, `PLACEHOLDER`, or `DRAFT`, and no governance, terminal-build, or release-confirmation marker leaked into the rendered manuscript.

The source contained 14 citation occurrences over exactly seven unique keys: `DangFavre2021`, `Deserti2018`, `FavreJonsson2011`, `FriedlandMilnor1989`, `Fujioka2023`, `GuedjSibony2002`, and `HenonSurvey2024`. Those sets matched the seven `.bib` entries, seven `.aux` citation keys, and seven `.bbl` items exactly. The references were rendered and the final build had no undefined citation or reference.

Section 12, `Conclusion`, begins and ends on page 22. `References` starts later on page 22 and continues through page 23. Page 23 contains the final Guedj--Sibony entry and is not blank.

For visual inspection, I rendered all 23 pages into a reviewer-owned external `mktemp` directory, inspected four contact sheets covering every page, and then inspected high-resolution pages 1, 5, 6, 10, 12, 17, 18, 19, 21, 22, and 23. This covered the title/abstract, theorem and cone, complete-support table, block/symplectic calculation, phase-gap table and complete matrix, exact recurrence, Perron proof, closed form, anti-claims, conclusion/reference boundary, and last page. I found no clipping, corruption, unintended blank page, missing glyph, malformed formula, table collision, or citation-rendering problem. I precisely unlinked all 45 regular inspection files and removed the empty reviewer-owned inspection directory before project writing.

## Mathematical and claim-boundary audit

I checked the theorem line directly against the displayed potentials. Differentiating

\[
V=q_1^2q_2^2+q_1^g,\qquad W=p_1^2p_2^2+p_2^g
\]

gives the advertised support rows and coefficients. On the half-open cone

\[
\mathcal C_g=\{u>0:1\le u_2/u_1<(g-2)/2\},\qquad g\ge5,
\]

the strict first-phase and second-phase inequalities select

\[
A_g=\begin{pmatrix}g-1&0\\2&1\end{pmatrix},\qquad
B_g=\begin{pmatrix}1&2\\0&g-1\end{pmatrix},
\]

and multiplication gives exactly

\[
C_g=B_gA_g=\begin{pmatrix}g+3&2\\2(g-1)&g-1\end{pmatrix}.
\]

The intermediate ratio is `(2+r)/(g-1)`, the second selector has the strict margin required precisely for `g>4`, and the complete-step ratio map

\[
f_g(r)=\frac{(g-1)(2+r)}{g+3+2r}
\]

is increasing and returns the half-open cone strictly inside itself. The carried-coordinate gaps, old-term dominance, and positive characteristic-zero coefficients close the two-phase induction without cancellation. The explicit triangular inverses and symmetric Hessian blocks establish polynomial invertibility and preservation of the standard symplectic form; the determinant calculation is used only as a consistency check.

The exact recurrence and visible total-degree functional are consistent:

\[
u_{n+1}=C_gu_n,\qquad
\deg(F_g^n)=e_2^{\mathsf T}C_g^n(1,1)^{\mathsf T}\quad(n\ge1).
\]

Moreover,

\[
C_g-A_g=\begin{pmatrix}4&2\\2g-4&g-2\end{pmatrix}>0
\]

for `g>=5`, so the second q-coordinate sees the Perron class and dominates the final p-degrees. The trace is `2g+2`, the determinant is `(g-1)^2`, and the discriminant is `16g`, giving

\[
\lambda_\pm=g+1\pm2\sqrt g=(\sqrt g\pm1)^2.
\]

The Perron coefficient is positive, the scalar recurrence

\[
d_{n+2}=2(g+1)d_{n+1}-(g-1)^2d_n,\qquad d_0=1,\quad d_1=3(g-1)
\]

matches the closed form, and `(sqrt(g)+1)^2 < (g-1)^2` holds for every `g>=5`. At the endpoint audit `g=5`, the ledgers give `v_1=(4,3)`, `u_1=(10,12)`, `v_2=(40,32)`, `u_2=(104,128)`, and visible degrees `1,12,128`, exactly matching the displayed table and recurrence.

The claims remain deliberately narrow. The manuscript does not claim a universal Newton-fan theorem, a dimension-four classification, arbitrary-support or arbitrary-coefficient validity, positive-characteristic validity, universal non-conjugacy, a product-decomposition classification, an entropy equality, a periodic-point result, or proof/priority authority from contextual citations. Its “non-product” statement is explicitly limited to the displayed coordinate support and strict degree comparison. The seven revision hard stops on page 22 preserve the selector, phase, no-cancellation, Perron-visibility, mixed-support, and citation boundaries.

## Exact governed cleanup and final tree

Only after every preceding check passed, I revalidated all 103 cleanup-bound files as one read-only gate. I then used literal `/tmp` parents, `lstat`, `O_NOFOLLOW`, inode consistency checks, direct-child enumeration, and immediate byte/hash revalidation to unlink each individually named file. I used no `rm -rf`, recursion, glob, wildcard, unresolved shell variable, symlink traversal, broad target, or unbound object.

The exact cleanup result was:

- 77 historical files unlinked: 71 leaves from the seven bound historical directories plus six individually bound top-level files;
- 26 terminal files unlinked: 13 leaves from each of the two receipt-bound terminal roots;
- 103 governed files unlinked in total;
- nine exact, verified-empty directories removed with `rmdir`;
- all 13 historical top targets and both terminal roots confirmed absent;
- zero project file changed during cleanup; the complete Q67 snapshot remained byte-identical at SHA-256 `53f67faeae9fe5bf964896ed1640668dd9af71debd258182b945707d523ab07b`.

After cleanup, I created only the necessary `paper/reviews` parent and this sole regular file. The resulting project universe is T68: 68 regular files, five internal directories, zero symlinks, and zero other entries. Existing Q67 bytes remain unchanged. This confirmation has only local anonymous effect; all external-action flags remain false.

FINAL_INTEGRITY_PASS
RELEASE_CONFIRMED
