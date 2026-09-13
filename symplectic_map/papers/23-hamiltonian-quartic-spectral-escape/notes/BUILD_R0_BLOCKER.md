# Paper 23 Deterministic R0 Build Blocker

Build date: 2026-08-25 UTC

## Disposition

The one-shot deterministic R0 build is blocked.  Both independent build roots
completed the prescribed four-command sequence with zero exit codes and
byte-identical outputs, but the final LaTeX log in each root contains one
prohibited hyperref PDF-string warning.  Because acceptance is conjunctive,
this warning prevents R0 PASS.  No retry, source edit, warning waiver, fifth
pass, alternate engine, or successful-build persistence is authorized.

This blocker is the sole project write of the build invocation.  None of the
nine success-only paths has been created in the project.

## Bound opening authority

The current root-governance and review records were stable at preflight and
again immediately before this blocker write:

| Record | SHA-256 | Bytes | LF | Mode |
|---|---|---:|---:|---:|
| BATCH_06_STATUS.md | 4224835420a29d808ff83c5a9f8f2c42e5ac0061f2c1d45c8b75c9bad15a8cc0 | 72,566 | 1,078 | 0644 |
| BATCH_06_IDEA_REPORT.md | 099db6be6a2a2d7a7a82dc863ab57995e632e1dcc5b09d0d3a4efd713f15f22c | 112,986 | 2,195 | 0644 |
| BATCH_06_PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTION.md | 27615c425261aa72caa4c880b6bc7f54ecfa98c99399a2d7efc78ed19d8282c4 | 8,524 | 245 | 0644 |
| notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md | aad55320dc0645931be2c0019327cd4255aaa56d77f94cd48e1a3702b10fb9bb | 30,329 | 785 | 0644 |
| notes/SOURCE_R1_ABSTRACT_INTEGER_REPAIR.md | f5bea1184027da2afe9c1cc6810c000b72fb058cc6cb527a30222866b521ef3b | 8,168 | 136 | 0644 |

The source review ends exactly PAPER_SOURCE_R1_PASS, and the repair receipt
ends exactly SOURCE_R1_ABSTRACT_INTEGER_REPAIR_FROZEN.  At opening, the
project contained exactly 24 regular files in exactly four child directories,
with zero symbolic links and zero other filesystem objects.  Every existing
regular file was mode 0644 with link count one.  All nine success paths and
this blocker path were absent, and no compiled artifact existed.

## Frozen source and independent-copy custody

| Source | SHA-256 | Bytes | LF | Mode | Project inode | Root A inode | Root B inode |
|---|---|---:|---:|---:|---:|---:|---:|
| paper/main.tex | ec7c4be7195b7e0875a56e873a936629713bc5326e01ed5d5f4f6acf8a6d759c | 67,386 | 1,776 | 0644 | 3227298198 | 10422237 | 538009131 |
| paper/math_commands.tex | a69565204428ce95abbcab5afb3833290004110e2718c074fbc805f7d1bdcb0d | 420 | 13 | 0644 | 3227298196 | 10422240 | 538025635 |
| paper/references.bib | ba0156abd7eb399de532b9bc1eefa81b3bb1be7868eed6ee4b42f8cd3371c782 | 2,812 | 99 | 0644 | 3227298197 | 11091734 | 538025636 |

The project sources and all six copies were regular non-symlinks with link
count one.  Every listed inode is distinct from its project source and from
the corresponding copy in the other root.  The copies retained their exact
hashes, sizes, LF counts, and modes after all eight build commands.

The two brand-new private build roots are:

| Root | Canonical absolute path | Mode | Directory inode |
|---|---|---:|---:|
| A | /tmp/paper23-r0-A.DyWKGR | 0700 | 10422234 |
| B | /tmp/paper23-r0-B.dsQvTx | 0700 | 538009127 |

The roots are distinct, contain no symbolic links or special objects, and
received only independent copies of the three frozen source files before
compilation.  Each root now has exactly thirteen regular direct children:
the three sources, four command logs, and six final build outputs.  Both
roots are retained unchanged as local diagnostic evidence.

## Executables, environment, commands, and exits

Within the prescribed PATH, pdflatex resolved through /usr/bin/pdflatex to
/usr/bin/pdftex, a mode-0755 regular executable of 1,802,504 bytes with
SHA-256
01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9.
BibTeX resolved through /usr/bin/bibtex to /usr/bin/bibtex.original, a
mode-0755 regular executable of 117,128 bytes with SHA-256
c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f.

Every build child received an empty inherited environment populated with
exactly these six entries:

    PATH=/usr/bin:/bin
    SOURCE_DATE_EPOCH=1787616000
    FORCE_SOURCE_DATE=1
    TZ=UTC
    LC_ALL=C
    LANG=C

In each root, exactly once and in order, merged stdout and stderr were
captured as follows:

1. pdflatex -interaction=nonstopmode -halt-on-error main.tex
   to command-1.log;
2. bibtex main to command-2.log;
3. pdflatex -interaction=nonstopmode -halt-on-error main.tex
   to command-3.log;
4. pdflatex -interaction=nonstopmode -halt-on-error main.tex
   to command-4.log.

The exit vector is (0,0,0,0) in root A and (0,0,0,0) in root B.  There was
no retry, fifth pass, latexmk call, alternate engine, shell escape, package
installation, source generation, source edit, or build cleanup.

## Cross-root identity evidence

Every required final output and every corresponding command log was readable,
nonempty, and byte-identical across roots:

| Relative file | SHA-256 in both roots | Bytes | LF |
|---|---|---:|---:|
| main.aux | 888b09e906d5784d4517a6541e066e321348b2db8860edf073ec3cc8f270fadc | 14,049 | 165 |
| main.bbl | baa229dd7d35d96b27d7dfb18a844db73c98b752df3be4c008d748636f199cf9 | 2,881 | 73 |
| main.blg | be7e80a71c65ef8bbfcc2e43c3aadcc0b89cb8216e61a785ca24403ec6c04c34 | 900 | 46 |
| main.log | ae161baf177ac232b2fa313b6e2d3db7a38acee58dca30dd8005de2091c1976d | 27,769 | 705 |
| main.out | 14be6d78b541eb75e29cec5bf18d1e9a26bfb0c128ddaa5f4c26ab00d315bb94 | 6,226 | 28 |
| main.pdf | ae37679ef3ee4fa0b86f41e073f374920499f4959a196e289829e654b3d12d37 | 492,452 | 2,724 |
| command-1.log | 6d916d3f68e6a8ef6d1de37b39eea69859300a298efce6b8767713315c792112 | 18,265 | 601 |
| command-2.log | 7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9 | 158 | 4 |
| command-3.log | 2078f53209c7485ec4b3b417562a7ef7df6e2a2444ccc4109b1eca2e759a428a | 8,504 | 162 |
| command-4.log | 2c4df138d84bd55c6966f941398793ac05722cfd837ee096f285c6149ac20873 | 7,395 | 117 |

The final AUX contains exactly nine bibcite records, and the final BBL
contains exactly nine bibitem records with the same frozen keys:
BergerTuraevHamiltonianMaps, BlancVanSantenAffineTriangular,
DangFavreSpectralInterpretations, DesertiDegreeGrowthExamples,
ForstnericComplexSymplectic, HenonOpenProblems,
KochLomeliStraightLineFlows, RangarajanPolynomialSymplectic, and
ShaoSunDimensionFour.  The BLG summary reports warning count zero.  The
final log contains no fatal error, LaTeX error, undefined citation or
reference, multiply-defined label, changed-label instruction, overfull box,
or underfull box.  Its sole package warning is the blocker below.

Read-only pdfinfo on the unpersisted root PDF reported the exact title, empty
Author, Creator, and Producer fields, 23 pages, Letter geometry, and no
encryption.  Creation and modification dates were absent.  These partial
facts do not convert the blocked build into a candidate artifact.  Because
the mandatory diagnostic conjunct had already failed, the downstream
font/action/security, page-boundary, full-text, and every-page visual
acceptance audits were not used to claim PASS.

## Exact blocking conjunct

The final main.log and command-4.log in each root contain exactly this
hyperref warning:

    Package hyperref Warning: Token not allowed in a PDF string (Unicode):
    (hyperref)                removing 'math shift' on input line 1560.

The referenced frozen source line is:

    \subsection{The restricted boundary at \(g=9\)}

The warning appears once in each byte-identical final log and once in each
byte-identical fourth-command log.  The R0 acceptance contract requires zero
hyperref PDF-string warning.  This is therefore a hard blocker even though
the exit vectors and cross-root byte comparisons pass.  The build role has
no authority to add a texorpdfstring fallback, edit the heading, waive the
warning, or rebuild.

## Failure-atomic persistence and final custody

Immediately before this write, the project remained exactly 24 regular
files, four child directories, zero links, and zero other objects.  The
three project sources, all three root-governance records, the source review,
and the repair receipt retained the identities bound above.  No project
source, root ledger, lock, review, receipt, or earlier artifact was modified.

The following nine success-only project paths remain absent:

- paper/BUILD_METADATA_R0.json;
- paper/BUILD_RECEIPT_R0.json;
- paper/main.aux;
- paper/main.bbl;
- paper/main.blg;
- paper/main.log;
- paper/main.out;
- paper/main.pdf; and
- paper/main_round0.pdf.

No compiled output was copied from either root.  Creation of this blocker
makes the project exactly 25 regular files in the same four child
directories, with zero links and zero other objects.  There was no network
lookup, upload, submission, public release, repository push, transport,
messaging, identity disclosure, Paper 24 action, or other external effect.

R0_BLOCKED
