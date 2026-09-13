# Paper28 single EC metric supplement

Status: prospective capture plan; no metric content captured yet.
The user confirmed the narrow supplement and requested instruction optimization first.
That audit is now complete; this is the previously confirmed next step.

The actual first LaTeX failure requests `ecrm1095.tfm` while loading T1 fontenc.
Two exact metadata-only candidate paths were checked: the file exists at
`/usr/share/texlive/texmf-dist/fonts/tfm/jknappen/ec/ecrm1095.tfm` as a root-owned
0644 regular file of 3584 bytes; the alternative `fonts/tfm/public/ec/` path
does not contain that named file. No live metric content was read by that check.

Capture only this one demonstrated dependency with a 4096-byte content budget,
well inside the unchanged original 2 GiB limit. No directory census, package
recapture, font generation, installation, library discovery or additional metric
is included. A new actual failure can establish another need; it is not assumed now.

Reviewed controller: `EC_SUPPLEMENT_CAPTURE_20260905.py`, run using configured
administrative Python with `-I -S -B` and an independently authored review JSON
whose exact SHA-256 is supplied. Review binds script/plan, manuscript trio,
exact target and budget. This trusted administrative capture is not falsely
called a hermetic publication child.

The only output root is the exclusively created
`notes/dependency-ec-supplement-20260905`. Before opening the host target,
record intent and attempted path. Traverse physical ancestors with no-follow
directory descriptors; verify regular type, fixed metadata and admitted byte
budget before content reads. Read exactly the admitted 3584 bytes from the
verified descriptor; compare pre/post identity and metadata. Preserve bytes,
hashes, LF count and metadata, rebind source/controls, then seal prior outputs
in outcome.json. Do not hash outcome into itself.

Failure preserves the new root and reports actual bytes read; it does not retry,
delete, repair or search for alternatives. There are no subprocesses, builds,
network actions, global configuration changes or source edits in this capture.
No old build root or first failed dependency capture is read or touched.

An independent recording-integrity review must verify the completed supplement.
The successor may then bind this file plus unchanged CAPTURE2 using a new
controller/plan and `build-capsule-ec-20260905`; all existing PDF/source/loader,
fixed-pass, isolation and acceptance predicates remain applicable. Capture PASS
alone is not a build or PDF PASS. Paper27 is already accepted and is not rerun.
