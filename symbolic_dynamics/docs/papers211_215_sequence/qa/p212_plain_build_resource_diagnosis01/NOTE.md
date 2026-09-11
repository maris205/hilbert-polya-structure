# P212 plain-profile resource diagnosis — archived DATA only

2026-09-11 UTC. This is a bounded author-side resource comparison, not a
manuscript review, source-policy adoption, dependency-completeness verdict,
host observation or build grant. It uses the project research workflow's
changed-dependency rule. Only this note is written; author proposals,
accepted P213 evidence and historical failed branches are not edited.

## Bound inputs and result

The final manuscript examined here is the eight-file
[proposal02 source set](../p212_plain_build_source_proposal02/PROPOSED_SOURCE_ONLY.sha256),
20,165 bytes. Its manifest SHA-256 is
`fe4abe8535901fbb1e6dd8c63038e0ecef03c9ea5a5d05619559d452494a8288`.
All eight listed source hashes passed the actual workspace-only check
`14750c`. Relative to proposal01, seven complete raw `cmp` calls returned
zero; actual diff `05b633` shows the only further source change is table
`\centering\small` becoming `\centering`. The new table source hash is
`df023982b7fb6020e74cc8220da7cabd1ae9a79309f064a8820192152b6389c2`.
The eight source bodies were read completely, including all bibliography
fields. A later recipe-only proposal can use this diagnosis only while
these exact eight input bytes remain unchanged.

The comparison baseline is P213's accepted
[223-row manifest](../p213_round2_terminal_preparation01/RUNTIME_INPUTS.sha256),
SHA-256 `35e6d5ac4cb0fb3933dc2d4ceb201d5afbf11315bdbcdcf74308a184c1586530`,
its archived [runtime source/query records](../p213_initial_build_runtime_resolution01/RUNTIME_NATIVE.json),
and the actual terminal
[source tree and final-pass FLS](../../../../papers/213-receiver-limited-cyclic-transfer/qa_final/cold_build_1/source_only/main.fls).
The runtime-record file hash is
`d590b09facca16393f910d22b1c942a144fc933f02686a1447c125eeaa59af69`;
the FLS hash is
`9b398f2fe2128cdb3949c078fc68390863a157e8d6afb2bf29e0489084a31900`.
No path printed inside those archived records was followed on the host.

Result: removing the small-table selection eliminates the one concrete
new conditional size branch found in proposal01. Proposal02 exposes no
additional explicit font-family selector or demonstrated new font basename.
There is substantial finite common coverage, but **223 remains a selected
candidate set, not a theorem that every P212 resource is included**. New
configuration/cwd binding, affected bibliography/layout outputs and actual
P212 build acceptance remain necessary. P213 completion is not reopened.

## Actual font consumers, not keyword possibilities

| P212 source consumer | Archived comparison and precise boundary |
| --- | --- |
| `main.tex` lines 1–7: article 11pt, amsmath/amssymb/amsthm, five kernel lengths | These seven lines exactly match the P213 declaration profile. The manifest names article.cls, size11.clo, the AMS dependency files, l3backend-pdftex.def, existing pdflatex.fmt and plain.bst. This is shared selected content, not a claim that package names alone determine consumed files. |
| `math_commands.tex` line 5; table lines 23/25; census line 38: `\ind=\mathbf{1}` | All three uses put the bold digit at ordinary formula level, not inside another subscript, fraction numerator or reduced-size matrix. P213's `\one=\mathbf 1` is used at ordinary text/display level, including its subscripted indicator in the inverse theorem. Its final FLS actually names cmbx10/cmbx8/cmbx6 metrics and cmbx10/cmbx12 font programs. |
| `math_commands.tex` line 1: `\N=\mathbb{N}` | The macro is defined but never called. P213 actually uses its blackboard macro `\Zge`; its FLS contains the msbm metrics and msbm10.pfb. An unused definition is not a new glyph consumer, while AMS's own font initialization must still be allowed. |
| `\mathsf`, `\mathcal`, other custom math alphabets | None occurs in these eight P212 inputs. The manifest contains ot1cmss.fd but no cmss TFM/PFB. That fact is only a conditional risk if a later source adds sans-serif selection; it is not a present P212 missing dependency. |
| Three `\emph` calls, theorem bodies, title and author | The three emphases are in an ordinary proof, with no nested bold-italic text. There is no explicit boldmath/boldsymbol/mathversion, textsc/textsl/texttt or fontfamily selection. Archived ot1cmr.fd supports ordinary roman, italic and bold-extended shapes; the relevant cmr/cmti/cmbx candidates are present. P212's nonempty `Anonymous` author differs from P213's empty author, but cmr12 TFM/PFB is already selected even though that PFB is absent from the chosen P213 final FLS. |
| Abstract, sub/superscripts, fractions, cases and long displays | There is no explicit size command left, footnote/thanks, matrix/smallmatrix, scriptstyle or scriptscriptstyle command. Class-provided abstract/title sizes still exist. P212 has ordinary scripts, tfrac/frac/binom, cases, align and delimiters; P213 already has a mathematical abstract, cases, array, fractions, nested substack/text and indexed formulas. Similar consumers support the candidate comparison, not equal output or identical every-style initialization. |

The 223 rows contain exactly 43 TFM and 43 PFB entries with matching
basenames. Their finite font candidate groups are:

- cmr: 5, 6, 7, 8, 9, 10, 12, 17;
- cmmi: 5, 6, 7, 8, 9, 10, 12; cmsy: 5, 6, 7, 8, 9, 10;
- cmbx: 6, 8, 10, 12; cmti: 7, 8, 9, 10, 12; cmtt: 10;
- cmex: 7, 8, 9, 10; msam and msbm: 5, 7, 10 each;
- cmmib10 and cmbsy10.

The complete selected final FLS has 253 lines, including 249 INPUT events,
64 distinct absolute INPUT paths, 28 distinct TFM paths and 17 distinct PFB
paths. All 64 absolute input names occur in the 223-row manifest. This is
an in-memory comparison of archived path strings, not a fresh host hash
check, an all-pass census, or evidence of P212 consumption. In particular,
loaded metrics and actually embedded font programs are different sets.

The archived native outputs `dfdd09` (ot1cmr.fd), `f856e1` (omlcmm.fd),
`ee26bc` (omscmsy.fd), `ddd6b6` (omxcmex.fd), `aa4f42` (umsa.fd) and
`b577c3` (umsb.fd) were read as DATA. They supply the displayed shape/size
families and AMS 5/7/10 ranges. The archived record collection does not
supply the full installed size11/fontmath/NFSS selection implementation;
their manifest hashes alone are not a source-level proof of that code.
The ordinary installed-format boundary, not a new exhaustive source audit,
is the proposed basis for using shared class/format semantics. If a
consumer needs an additional explicit size derivation, supplement only the
relevant size11/fontmath/alphabet selection definitions for the actual
source uses, under a separate finite read authorization.

Historical proposal01 risk: its small table contained `\mathbf{1}`.
The archived OT1 bold-extended declaration maps the 5–9 size range to
corresponding cmbx metrics; the candidate manifest has no cmbx5 or cmbx7.
Thus a 10/7/5 math-size selection would have required additional prospective
metric coverage, even if some initialized faces were never embedded.
This was a conditional source diagnosis, not an observed failed build or
proof those host files were absent. Proposal02 removes that explicit
small-table trigger. It does not convert the old risk into a PASS or claim
that scripts disappear. No font or mathematical expression was replaced.

## Five bibliography entries and characters

Both bibliographies and all eight P212 inputs are ASCII byte streams.
P212's five actually cited keys are manna1987, loginov2007, berdine2006,
pham2015 and holroyd2008, all in setup lines 14–26; there is no nocite.
The 1,927-byte Bib file's sole backslash-bearing line is line 29, containing
`M{\'e}sz{\'a}ros`. The ASCII apostrophe in O'Hearn is not an accent macro.
There is no font-family, encoding, url or href macro in that file.

P213's 1,181-byte Bib has `Fuk{\'s}`. Its actual 764-byte
[BBL](../../../../papers/213-receiver-limited-cyclic-transfer/qa_final/cold_build_1/source_only/main.bbl)
retains that accent and ordinary italic journal text; its hash is
`631bb1b5c767e31d7f398f795531bcc43c2b6028338d6d60e79c3a42388013f6`.
The P212 acute/base pairs e and a differ from the old s pair. They introduce
no explicit new family, but an old accent control sequence is not a glyph
or resource acceptance for a new PDF. P212 also changes three article
entries into two inproceedings, one incollection and two misc entries,
with additional booktitle/series/note/howpublished fields. The selected
plain.bst is common; neither the old three BBL entries nor old event/page
counts can stand in for five new entries. The raw underscore inside one
URL is not currently an input command; if a different style begins emitting
URL fields, that is a changed consumer requiring review.

The finite supplement is P212's actual AUX-before-BibTeX, complete BLG/BBL,
exact five-key reconciliation, relevant warnings, embedded-font/text
inspection and all-page views after a separately granted build. If an
advance source argument for the new entry types is required, read only
plain.bst's relevant handlers as fixed DATA; do not invent a generated BBL.

## Configuration and the new cold cwd

The [P213 runtime scope](../p213_initial_build_runtime_resolution01/RUNTIME_SCOPE.json)
and [original handoff](../p213_initial_build_runtime_resolution01/HANDOFF.md)
already distinguish selected resources from complete consumed closure.
The proposed P212 and accepted P213 requests use the same 13 controlled
environment assignments, fixed Bash/no-profile/no-rc, engine/program names
and four-pass order. HOME/XDG values are not supplied; the old eight-field
P212 epoch is not silently retained. The inherited existing format is
pinned, not rebuilt. Current latex source/pdftexconfig files do not prove
that format's historical generation.

The archived configuration output `dc9d15` has the following relevant
source lines: 87/90/93 name the three user trees; 167 sets TEXMFDOTDIR to
`.`; 197/215 define latex/pdflatex inputs; 315 formats; 332/333 VF/TFM;
355 font maps; 358/359 Bib/BST; 391/419 Type1/encoding paths; 566 the three
absolute TEXMFCNF directories. Actual archived effective-variable records
in the scope file give:

- TEXMFCNF: `/etc/texmf/web2c:/usr/local/share/texmf/web2c:/usr/share/texlive/texmf-dist/web2c`;
- TEXMFDOTDIR: `.`;
- TEXMFHOME: `./texmf`;
- TEXMFCONFIG: `./.texlive2021/texmf-config`;
- TEXMFVAR: `./.texlive2021/texmf-var`.

The three actual config names in the selected terminal FLS, the existing
format, selected databases and both font maps are already named in the
223 candidates. Under the expressly shared ordinary installed namespace
and unchanged received content keys, the new cwd-dependent difference is
the local `.` search position and those three relative user trees. This
does not require observing every parent, rebuilding the format, scanning
system font/cache trees or executing kpsewhich. The previous cwd's absence
facts are not observations of the future P212 directory.

The examined proposal02 recipe uses exclusive nonrecursive mkdir of a new
output/cold tree, creates only its sections child, copies exactly the
eight ordinary non-link sources and checks each raw copy and source hash.
All tools remain in the cold cwd for the passes. This supplies a finite
construction argument under ordinary filesystem trust, but the directory
does not exist merely because source code describes it. The practical
S6 supplement, authorized for a subsequent source proposal but **not
implemented or executed by this note**, is:

1. After actual copy/hash and before the first TeX pass, capture the actual
   `pwd -P` and bind it to the accepted literal cold cwd.
2. Enumerate only that directory and its sections child, including dot
   entries other than `.` and `..`. Require exactly main.tex,
   math_commands.tex, references.bib and the sections directory at top
   level, and exactly the five declared section files below it; require
   ordinary non-link types. Record the complete names and successful
   assertions outside the cold tree, alongside the eight content pins.
3. Explicitly assert texmf and .texlive2021 absent, including dangling
   links. The exact two-level inventory already rules out local class,
   format, bibliography-style, map and other source-shadow files before
   pass 1. Do not scan their unneeded descendants or any parent/system
   directories. Existing fixed product-absence checks remain useful.

This is a bounded actual-workspace check, implementable using already
trusted Bash builtins; it is not a new observer or hostile-writer/ancestor
attestation. Root still has to receive its exact source/request and actual
successful record. Later generated AUX/BBL and other products must be
classified from their real before/after chronology, not rejected merely
because they were absent before the first pass. All fixed global runtime
content checks and the ordinary rendering/Fontconfig/cache trust limits
remain as stated in the accepted P213 handoff; this note does not turn them
into exhaustive syscall or private-cache closure.

## Remaining finite handoff

Receive and adopt the exact replacement policy/source proposal separately;
prepare P212's own finite manifest from the common candidates and any
specifically justified supplement; bind the actual request, source keys,
parent and fresh-cwd checks before any separately granted build. There is
currently no demonstrated additional font basename for proposal02, but no
P212 runtime/format/glyph/layout PASS is issued here. Preserve the initial
P213 omitted texfonts.map prepin history and the unused P212 B/S failures.
Any later unknown consumed FLS input stops acceptance and does not grant
permission to read that path, install a resource or retry a failed build.

The final acceptance must use complete P212 logs and ordered FLS records,
BibTeX inputs/outputs, all fresh page artifacts and actual views. It must
not copy P213's 64-path final-pass statistic, three entries, 17 embedded
fonts, seven pages or previous canonical/review conclusions as P212
expectations. Source/format changes affect build evidence; no scientific
verifier or manuscript review was run for this note.

Read limitations and retained failures: early displays of the large runtime
JSON were truncated; a first in-memory parse of a 6,000-line prefix failed.
A subsequent complete cat read parsed all 285 archived records, and only
the cited source outputs were selected for interpretation. Two guessed
document basenames did not exist; the correct source manifest and actual
raw source diff were subsequently read. These are navigation/DATA failures,
not source or build findings, and no missing output is invented. No TeX,
BibTeX, kpsewhich, PDF utility, science program or new host-path observation
was executed; no paper, central index, Git or external action was changed.
