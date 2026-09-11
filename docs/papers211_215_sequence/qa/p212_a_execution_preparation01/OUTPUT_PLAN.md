# P212 A ordinary capture — source preparation only

The whole guard is guard.js. It has NOT been executed, imported or syntax-
parsed during preparation. No interpreter probe, scientific run, canonical
adoption or build is authorized by these files. REQUEST.initial.proposed.json
is a command proposal, expressly not a root execution grant.

After complete root source review and a separate fresh root one-run grant,
the exact initial capture command (cwd /root/autodl-tmp/symbolic_dynamics) is:

    node docs/papers211_215_sequence/qa/p212_a_execution_preparation01/guard.js initial01

The guard directly invokes /usr/bin/python3.10 with the three flags -I -S -B
and the absolute independent verify.py path, no script arguments, workspace
cwd, exactly LANG=C and LC_ALL=C, and stdin /dev/null. stdout/stderr are
exclusive regular file descriptors, not buffered child pipes; there is no
1 MB or other raw-output byte cap. The proposed timeout is 600000 ms with
SIGKILL on timeout. A timeout is failed retained evidence, never canonical.

## Exact root grant shape

The guard reads only ROOT/GRANT.<run_id>.json, where ROOT is
docs/papers211_215_sequence/qa/p212_a_source_root01. Root creates this later.
Its object must contain schema=P212_A_ONE_RUN_GRANT_V1, authority=root,
action=execute_once, run_id, exact absolute run_directory, guard_sha256,
preparation_manifest_sha256, source_manifest_sha256 and command. The last
object must equal scientific_command in REQUEST.initial.proposed.json,
including its displayed key order (the guard deliberately uses exact JSON
object-order comparison). The source manifest hash is fixed in the guard;
guard/preparation hashes must be the complete actually accepted current bytes.
The grant is evidence of ordinary root authority, not a cryptographic signer
or hostile-process authentication mechanism. No grant template is populated.

Run IDs match (initial|strict)[0-9]{2}. The run root is the fixed batch-local
qa/p212_a_runs directory. A specific run directory is created with exclusive
mkdir, never adopted/reused/overwritten. Even a failed preflight consumes that
directory; retry needs a fresh root grant and unused ID. There is no automatic
retry, canonical write, deletion, repair or dependency discovery.

## Inputs and trust

PREPARATION_INPUTS.sha256 pins exactly guard.js, this plan and the proposed
request, not itself. Its whole hash is bound by the future grant. Five fixed
document hashes bind root's complete runtime policy, current 19-role runtime
record, source reception, the exact 16-input review-source seal and the exact
25-input frozen seal. The guard parses both seals only after checking their
hashes and retains all full content keys. Duplicate identical pins merge;
conflicting pins fail. Source/parameter bytes remain separately pinned even
though the scientific producer itself reads no data files. The old paper
canonical is a frozen documentary input, never the new independent canonical.

For every selected present input, fresh open/fstat/read/fstat/path-stat checks
record full SHA256, byte size and dev/ino/mode/size/mtimeNs/ctimeNs metadata;
changes during a read fail. All 18 runtime file records must equal root's
expected path/kind/bytes/SHA256. Historical metadata drift is explicitly
retained in runtime_baseline_metadata_changes, not itself a rejection; root's
follow-up ordinary policy distinguishes historical metadata from current
pre/post stability. The startup zip must yield
actual lstat ENOENT (an existing dangling symlink fails). All source/frozen/
grant/preparation inputs must match their accepted hashes and their fresh
pre/post metadata. Runtime and input snapshots are repeated after exit and
compared completely. Snapshot read/mismatch errors are accumulated and saved
before failure, including postflight failures after a child exit. Atime is
deliberately excluded because reads alter it.

Node, its fs/crypto/child_process facilities, Python/bootstrap/standard-runtime
roles, ordinary path traversal and storage are trusted exactly as root policy
allows. This is selected-input pre/post evidence, not dynamic closure or
continuous race-proof monitoring. No ELF, package, recursive observer,
network or scientific imports are added. Root should submit the exact capture
command once per grant and retain the tool's native request/result as well.

## Retained output

Each exclusively new run contains REQUEST.json (actual bound grant/key/command),
PRE.json (full selected keys), stdout.raw and stderr.raw (unfiltered complete
bytes), EXIT.json (actual status/signal/error/pid), POST.json (full selected
keys), and RECEIPT.json (pre/post equality and full raw-output metadata/hash).
EXIT.json is saved before the postflight so an input-change failure does not
erase the actual child exit. GUARD_FAILURE.json preserves the failure reason
and whether science was submitted whenever the run directory exists. An
early setup/fatal I/O error can leave incomplete artifacts; such evidence
must be preserved as failure, never promoted. Run-path collision errors cannot
write into the old directory. Guard stdout/stderr and native exit must also
be captured by root's execution tool; they are not the scientific raw output.

A zero exit and unchanged selected inputs mean only capture completion.
Full independent-output schema/semantic reception is still required. Only
the actual accepted complete initial stdout may later be adopted by root as
canonical. Strict runs use fresh IDs/grants and the same fixed producer;
root separately performs complete raw-byte comparisons against the adopted
canonical and each other. This guard neither reads that canonical nor
mistakes matching hashes alone for those required raw comparisons.

No runtime file has been freshly probed by this preparation. The source
contains the proposed future checks; root's RUNTIME_INPUTS.json is preserved
input evidence with its stated historical/current scope. Ordinary runtime
acceptance, full semantic reception, strict pair and final review/build gates
remain separate and cannot be inferred from this source package.
