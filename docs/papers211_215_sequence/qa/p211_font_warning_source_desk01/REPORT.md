# P211 terminal font-expansion warning: primary-source desk

Outcome: SOURCE_DOCUMENTATION_ONLY / ROOT_DISPOSITION_PENDING. The diagnostic
supports a late font-expansion setup interpretation, not a finding of lost
glyphs. It does not establish harmlessness or correct expansion either.
P211-COLD1-IO-D1 remains Minor / OPEN_PENDING_ROOT_DIAGNOSTIC_DISPOSITION.
No manuscript, build, terminal or paper PASS is issued.

## Exact diagnostic and source condition

The saved pass 3 log, line 608, actually says:

> pdfTeX warning (font expansion): font should be expanded before its first use

In the retrieved TeX Live upstream `pdftex.web`, `read_expand_font` emits
this warning after preceding identifier/base-link, normalized step/limit and
expansion-ratio checks, precisely when the stored expansion step is zero
and the font type is neither new nor virtual. In its four-state enumeration
that means real or substituted. The alternative nonzero-step branch instead
checks existing expansion parameters for consistency. The warning branch
then calls `set_expand_params`; it does not abort at this warning or test
glyph existence. Source comments associate new-to-real/virtual classification
with first character output, while substituted is a spacing-adjustment
state. Thus “late setup” is a useful interpretation; the exact criterion is
the stored state, not an independently logged first-use event.
[Upstream pdftex.web](https://raw.githubusercontent.com/TeX-Live/texlive-source/refs/heads/trunk/texk/web2c/pdftexdir/pdftex.web),
retrieved browser lines 15908–15920 and 16327–16387; complete returned
contexts in [retrieval 04](web/retrieval_04.json) and
[retrieval 08](web/retrieval_08.json).

The current official manual describes font expansion as horizontal glyph
scaling for justification, potentially affecting line breaks with
`pdfadjustspacing=2`; character-loss diagnostics are described separately
under `tracinglostchars`. These are different mechanisms.
[Official pdfTeX user manual](https://tug.ctan.org/systems/doc/pdftex/manual/pdftex-a.pdf),
sections 4.3.1–4.3.2 (printed pages 29–30), 4.23.2 (63–64);
[retrieval 07](web/retrieval_07.json). Neither the warning alone nor its
absence certifies rendered glyph coverage.

## Executed version is not the retrieved source version

The actual saved cold1 log banner and the saved version command stdout
both identify **pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)**,
with kpathsea 6.3.4/dev in the latter. The archived command receipt records
`/usr/bin/pdflatex --version`, exit 0, and its 555-byte stdout hash; this
desk only read that saved evidence, not the executable.
See [native 02](native/read_02.json), [04](native/read_04.json) and
[05](native/read_05.json).

The retrieved upstream file declares 1.40.29, and the official manual title
identifies 1.40.29 dated 2026-02-16 (revision 979 in section 1.1).
[Source](https://raw.githubusercontent.com/TeX-Live/texlive-source/refs/heads/trunk/texk/web2c/pdftexdir/pdftex.web),
[manual](https://tug.ctan.org/systems/doc/pdftex/manual/pdftex-a.pdf).
The exact warning spelling is present in both the archived log and current
upstream source. That does not prove an exact source/binary correspondence:
no Debian source-package revision, distribution patch set, complete engine
build source, immutable upstream commit, or binary/source attestation was
obtained. The branch explanation above is explicitly the inspected upstream
implementation, not a claim to have traced the executed binary.

Root requested at most one bounded historical-source lookup. One search of
the official TeX-Live GitHub source repository for 1.40.22/pdftex.web returned
no results; [retrieval 12](web/retrieval_12.json) preserves the actual empty
result. No additional historical query, host probe or compiler download was
attempted. Failure to find an indexed result is not proof of source absence.

A tempting contrary shortcut is out of scope. The microtype author's
current manual discusses this warning for tracking plus expansion with
pdfTeX **older than 1.40.4**, and calls that historical case ignorable.
That scoped statement does not establish the status of P211's 1.40.22
execution. [Microtype manual v3.2d, section 11, printed page 30](https://mirror.math.princeton.edu/pub/CTAN/macros/latex/contrib/microtype/microtype.pdf);
[actual retrieved context](web/retrieval_11.json). No general benignness
claim is imported from that paragraph.

## P211 evidence and remaining limits

The actual cold1 pass 2 and pass 3 diagnostic lines were reread at lines
624 and 608 respectively. Whole-file native hashes/sizes agree with the
ordered-I/O report: pass 2 is 26,096 bytes; pass 3 is 25,362 bytes.
The warning occurs while the log has `main.bbl` open, just before page 5
is reported. It contains no font identifier, character, source line or
macro call stack; its location does not identify the exact triggering
bibliography macro or font. No such attribution is made.

The saved main source loads microtype; the saved final log reports automatic
expansion enabled, level 2, stretch/shrink 20 and step 1. These observations
do not reveal the warning's internal font state. The two separate
microtype Info contexts for character 029 explicitly say that protrusion
settings are ignored; they are not silently recast as emitted glyph-loss
diagnostics. See [native 03](native/read_03.json) and
[06](native/read_06.json).

The saved measurement object has an empty warnings array. The saved
executed builder snippet matches capital “Warning” without an
ignore-case flag, explaining why it misses the lower-case engine warning.
[Native 10](native/read_10.json), [11](native/read_11.json).
The independent lane's complete 18-file census and its current finding
remain authoritative for that scope:
[ordered-I/O REPORT](../p211_terminal_cold_artifact_audit01/io_lane/REPORT.md).
This desk does not replace that full census or repeat its 5,132 checks.

Root's actual page-view reception reports all five pages viewed with no
visible clipping, collision or dropped glyph at the viewed resolution,
and explicitly does not establish intended internal font-expansion behavior.
[Root view reception](../p211_terminal_pair_pages_root01/RECEPTION.md);
[saved read](native/read_12.json). This desk performed zero page views,
and does not convert that limited visual observation into a warning waiver.

Accordingly, the warning alone proves neither missing glyphs nor their
absence; neither failed PDF production nor correct typography; neither the
causing font/macro nor a justified repair. The saved final log reports a
five-page, 301,007-byte PDF despite the warning. Root must separately
adjudicate the documented census omission and any residual concern.

## Evidence and scope

[INPUT_PINS.json](INPUT_PINS.json) binds the nine selected workspace evidence
files (99,636 bytes), with native whole-file hash and byte-count returns
preserved in native 13–14. Reading scope is explicit: selected source/log/
measurement snippets, complete version stdout/receipt and the two complete
audit/reception reports. Hashing a whole input is not claiming its whole
body was read. Initial skill/workflow/state/index/navigation reads were
performed but their original native envelopes were not persisted here;
an initial large state/discovery response and one combined display were
truncated. Later dedicated evidence results were retained without
reconstructing those earlier envelopes.

Twelve web request/result records preserve actual returned evidence,
including 403/502/unsafe-URL/redirect failures and unsuccessful text finds.
They are tool-returned representations, not raw HTTP response bodies,
complete downloaded PDFs, or a full upstream checkout. Browser line
numbers above are not claimed as raw-file physical line numbers.
`EVIDENCE_INDEX.json` maps every saved request to its packet member.
Successful source/manual retrievals do not erase failed retrievals.

The project symbolic-dynamics-research skill and WORKFLOW governed phase
separation and preservation. Only this new desk packet was written.
No submitted code, Python, TeX, build or host-dependency query was run;
no scientific claim, manuscript repair, source repair, Git operation,
external upload or specialist contact occurred. The shell calls here were
workspace reads and documentary integrity checks only. The final
directory-relative SHA256SUMS covers every payload and excludes itself.
OWNER_AMBER / HOLD_EXTERNAL remains unchanged.
