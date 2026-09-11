# Transport / network / nonlinear artifact audit

Date: 2026-09-08 UTC.
Outcome: ARTIFACT_INTEGRITY_PASS_WITH_DISCLOSED_LIMITS.
Root reception and scientific/source acceptance remain pending.

All three named archives pass the complete current payload and pin checks.
The nonlinear archive does not have the same provenance strength as the other
two: its missing browser requests and decoded-combined-output limits remain
explicit and are not repaired retrospectively.

## Actual result

| Named desk | Complete current nonself payload | Original pins / copies | Native evidence checked |
|---|---:|---|---|
| circular_interval_transport_desk | 40 files; 322,468 bytes | Seven original pins and seven byte-identical physical copies | Ten exact argv/cwd/environment records, all separated raw streams, seven exact excerpt reconstructions, seven browser request/return records |
| finite_network_rewrite_desk | 11 files; 243,501 bytes | Three original pins; four collector-input bindings, including two initial-draft mappings | Four exact argv/cwd/environment records and separated streams; three raw excerpt reconstructions; six browser request/return records |
| finite_nonlinear_feedback_fresh_desk | Four files; 208,324 bytes | Eight closing original pins, plus one earlier unpinned original checked at its current bytes | 22 cmd-string/tool-result records; 15 current text-slice comparisons, four current PDF-output comparisons, two closing hash-output comparisons and one preserved failed path read |

The three directories contain 58 actual regular files including their three
controlling seals, totalling 783,386 bytes. Their 55 nonself payload files
total 774,293 bytes. The network first MANIFEST.json remains a preserved
eight-payload historical seal and is included in the controlling V2 payload.
No extra payload, pin mismatch or byte-comparison failure was found.

The successful auditor performed 836 assertions. Its six actual subprocesses
were documentary only: the existing circular verify mode, the existing
network V2 verify mode, and four local pdftotext extractions from the two
already-pinned historical manuscripts. All six exited zero with empty
stderr. No science program was imported or executed, and no network request
or new primary research occurred.

[AUDIT_RESULT.json](AUDIT_RESULT.json) is the exact successful auditor stdout,
including full input pins, all check summaries, source-return shapes, the 22
nonlinear command records and six new processes' lossless separated streams.
[EXECUTION.json](EXECUTION.json) records the actual capture request, inner
argv/cwd/environment, exit code and raw-output binding. The result file has
135,044 bytes and SHA-256
1f6ee7fe6b916ba82e82f331a2d531ed9611db36fd37670f9f2fa4459f5bd4b9.

## Complete declared input key

Before and after the successful execution, the key was identical:

67ca0e4dd8e11727cf5c5781e5561f566735d8a65ab5b1aa09af10ba2cf80d12

Its 138 file entries comprise:

- All 58 files in the three actual desk directories, including their seals.
- Nineteen explicitly referenced originals: 18 existing pinned inputs and
  the earlier unpinned algebra SCOUT_REPORT.md used by an archived excerpt.
- The three root pending-intake files, this auditor entry file, and five
  documentary executable files.
- All 52 Python module files observed as loaded by the auditor.

The key also records fixed subprocess environment, Python version/flags,
entry argv, explicit scope and the current existence status of the recorded
wrong-path original. Canonical JSON and hash definitions are inside the
result. No entire workspace search or protected P211 input access was used.
This is complete declared artifact/entry-point provenance, not a hermetic
operating-system/shared-library lock or a historical runtime certificate.

## Limits and failures retained

1. Network metadata errata and first-seal history. Both author citation-title
   errors, their corrections, initial source versions and the old eight-file
   seal remain unchanged. The original capture.py verify is not appropriate
   for the enlarged directory and was not run. The additive capture_v2.py
   verify is controlling.

2. Nonlinear native shape. The archive supplies exact command strings,
   requested cwd and decoded combined tool output; it does not supply
   original native argv arrays, separated raw stdout/stderr, complete
   executable/environment bindings or an earlier-discovery hash bracket.
   The auditor labels shlex-derived argv as interpretations, not observed
   historical process argv.

3. Nonlinear browser request omission. All three browser rows contain only
   label, tool and returned text. Actual request objects, including complete
   search-query objects, are absent. They were not reconstructed from source
   result snippets. Circular's seven and network's six request objects are
   present and retain nonempty returned strings.

4. Other nonlinear failures. The wrong-path exit 2, successful pp. 1–5 and
   failed pp. 6–7 source-pipeline chunks, aggregate failure exit 1,
   curl-reported 56, empty-extractor error and transcribed TextEncoder
   assembly failure remain in the original archive. Per-member process
   exits and a raw assembly traceback are not claimed.

   Those two source-pipeline entries retain launch command strings and paired
   launch/completion result chunks, not launch cwd/environment, actual process
   argv arrays, or completion polling request objects. Their pairing is the
   archived association, not an independently recovered session transcript.

Comparisons involving nonlinear old output mean exact equality between
current raw bytes and the UTF-8 encoding of the archived tool-decoded
string. They are not a claim that the missing historical raw separated
streams have been recovered. The two closing hash strings equal INPUTPINS
byte-for-byte; their old before/after bracket still covers only the eight
closing excerpts.

All 16 browser returns are archived source-return strings, not raw HTTP,
complete PDFs, or visual-read certificates. This audit verifies archive
shape and identity, not the truth of every source claim or actual reading
of every returned passage.

## Preserved failure in this audit

The first new auditor execution exited 1 in setup: its module guard included
the auditor's own main entry among unexpected workspace imports. It launched
zero documentary subprocesses. The exact initial source survives at
[failed_setup01/audit.py](failed_setup01/audit.py), SHA-256
aa50e39561376d9cb2e3cdbb3b377b3c75e175564586734d1d2cbc2aa425b53f.
The actual failed execution and traceback are retained in
[failed_setup01/EXECUTION.json](failed_setup01/EXECUTION.json).

The only correction skips that same main entry in the imported-module list,
because it is already keyed separately as auditor_entry. The corrected audit
then completed successfully. No desk input or existing checker was modified;
the failed result is not overwritten or relabelled PASS.

A later inline seal diagnostic had an extra closing brace and failed during
command parsing. That command and its native return are retained in
[SEAL_CHECK_FAILURE.json](SEAL_CHECK_FAILURE.json), together with the then-current
six-payload seal. This did not execute the auditor or change its result. The
diagnostic was corrected without changing any scientific or audit predicate.

## Authorship and reuse disclosure

Auditor: /root/round211_rational_scout/relation_primary_sources.

I did not author the three packages or their existing capture checkers.
The nonlinear package author is my parent agent,
/root/round211_rational_scout; circular and network are authored by
/root/round211_queue_scout. I had previously read the nonlinear HANDOFF.md
during another bounded subtraction task. This is therefore not described as
blind research review or independent certification of any author's science.

I fully read circular capture.py and both network capture.py/capture_v2.py
before executing the two controlling verify modes. Their reuse is deliberate
and visible in the native process records. The new auditor additionally
checks exact circular argv and binding shape and handles the nonlinear
decoded-output archive separately; it never imports these checkers or a
scientific module.

No P211 A package or P211 mathematics was accessed in this task. No child
agent, central-index edit, Git operation, manuscript change, source upload or
specialist contact occurred. Writes are confined to this new QA directory.
The P211 B candidate contribution boundary remains unchanged.

## Replay

From /root/autodl-tmp/symbolic_dynamics run:

    /usr/bin/python3.10 -I -S -B docs/papers211_215_sequence/qa/transport_network_nonlinear_artifact_audit/audit.py

[audit.py](audit.py) is executable and read-only: it prints JSON and exits
zero for archive integrity with the stated limits, or nonzero for a new
integrity/check failure. It uses only the six explicit documentary command
bindings and does not write or execute a shell. A later change to any keyed
input appropriately changes the key; a successful archive audit alone does
not grant scientific acceptance or root reception.

MANIFEST.sha256 covers every regular payload in this QA directory except
itself. Root retains reception authority.
