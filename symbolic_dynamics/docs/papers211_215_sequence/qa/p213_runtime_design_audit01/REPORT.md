# P213 minimal runtime design — independent bounded audit

Verdict: `DESIGN_ACCEPTABLE_FOR_MINIMAL_SOURCE_COMMISSIONING_ONLY`.
Concrete unresolved design defects found: **0**. This is not SOURCE_PASS,
PROBE_AUTHORIZATION, RUNTIME_PASS, scientific acceptance or a batch milestone.
2026-09-09 UTC. Auditor: /root/round211_finite_matching_scout.

## Exact reviewed object and evidence

The complete [design](../p213_runtime_preparation01/DESIGN.md), all 235 lines
and 14,497 bytes, has SHA-256
`6dcfb89b271cfa1904ee8129831ab89f0a09eb3d1551542ca521517ab5373d84`.
Its complete preparation packet is seven payloads/eight files, 76,936 bytes;
the directory-relative nonself seal is
`f0e254caa515275cbd95848ba9845909a94b94d681e7c3e58569f9a5c2e1fefa`.
The four declared paper interfaces total 11,751 bytes; all were read as
text, including the JSON parameters. No scientific source was parsed,
compiled, imported or executed in this design audit.

[CHECK_NATIVE.json](CHECK_NATIVE.json) records the actual successful
documentary check, reporting 415 checks across these 12 inputs/88,687 bytes.
All 12 full-file hashes, byte counts and ten non-atime integer metadata
fields agree before/after. The preparation seal covers exactly its seven
physical payloads. All four input pins and the three corresponding paper
manifest leaf entries match. Reading the paper's 29-entry source manifest
here is not a new 29-payload source acceptance; the previous source/parameter
audit and title delta remain separate frozen work.

Nine archived documentary outputs compare as raw UTF-8 bytes: four whole
interfaces (11,751 bytes), four hash lines, four strict input-OK lines, the
48-line design excerpt, and complete READ_SCOPE/HANDOFF. Two archived wc
tables match their actual named files' byte/newline counts. All eleven
author documentary native records are accounted for; none was rerun as a
scientific command. The author's primary-access record is byte-keyed and
its seven public request members structurally checked, not represented as
a complete physical upstream-source archive or substituted for my own
fresh public semantic checks.

The unsealed audit's first reread used a nonexistent PARAMETERS.md suffix;
its exit 2 and exact output remain in READS_NATIVE.json, followed by the
correct PARAMETERS.json and source-manifest read. The first documentary
checker required an unnecessary `./` prefix for the preparation's legitimate
basename-only seal. Its actual failure and exact source remain in
CHECK_FAILED_NATIVE.json and CHECK_INPUTS.cjs. The new-only
CHECK_INPUTS_BASENAME.cjs adapter fixes that exact local layout assumption,
without relaxing the known membership/digest requirements or editing any
input. These are auditor documentary failures, not P213 runtime failures.

## Why the design is adequate for the next source-only step

The proposal explicitly relies on ordinary trusted product, Bash, env,
CPython, kernel and filesystem bootstrap (design lines 17–23), and rejects
hermetic startup, full ELF/NSS/configuration closure, continuous immutability,
loaded-memory identity and P212's different historical requirements. That
is a disclosed premise, not an observed result. First access to already
initialized sys is part of that bootstrap; the fixed CPython initialization
example supports sys/encoding/stream availability before ordinary scripts,
not this machine's installed version. [CPython v3.11.13 initialization](https://raw.githubusercontent.com/python/cpython/v3.11.13/Python/pylifecycle.c).

The startup/observer boundary is substantive: immutable scalar module and
sys facts precede helper imports; raw bounded early maps and a second
pre-helper snapshot precede explicitly labelled helper/closing snapshots
(lines 66–100). This avoids a late shallow snapshot being called early
evidence. The registry's mutability and orig_argv's distinction from argv
are consistent with the [official sys contract](https://docs.python.org/3/library/sys.html).

The draft does not treat `-I -S -B` as an import-free runtime, infer cache
absence, or equate a nominal frozen filename with executed text (lines
48–52 and 144–151). Disabling bytecode writes does not rule out reads;
source/cache observations alone do not identify executed code.
[Command-line flags](https://docs.python.org/3/using/cmdline.html),
[import/cache contract](https://docs.python.org/3/reference/import.html#cached-bytecode-invalidation),
[fixed cache-reading implementation](https://raw.githubusercontent.com/python/cpython/v3.11.13/Lib/importlib/_bootstrap_external.py),
[fixed FrozenImporter implementation](https://raw.githubusercontent.com/python/cpython/v3.11.13/Lib/importlib/_bootstrap.py).

The finite frontier is also real: approved paths/classes/numeric bounds
must exist before a probe; observing a path grants no permission to read
it. Unknown/deleted/unsupported/late-unkeyed cases HOLD without recursive
acquisition (lines 112–142). Internal trusted imports are expressly outside
that preventive limit. Maps are finite current observations, not startup
history, an atomic whole-process state, or another process's dependencies;
the [kernel documents partial-read races](https://www.kernel.org/doc/html/latest/filesystems/proc.html).

Same-fd complete byte hashing, pointwise identity checks, true optional
existence results and preserved failures are appropriate to the limited
claim (lines 153–182). Absence remains an actual authorized-path result,
including for a zip candidate that can be listed without existing.
[Python path initialization](https://docs.python.org/3/library/sys_path_init.html).
None of these assertions supplies yet-unobserved paths, identities, caches,
limits or absence facts.

## Mandatory later source/acceptance obligations

These seven items are acceptance requirements already bounded by the
design, not seven completed tests or seven open design-defect findings.
They must be received in the separately commissioned exact source/binding.

1. **Early representation.** Preserve immutable scalar facts, explicit
   missing versus null values and actual qualified loader-class identity.
   A direct source-file launch has a known `__main__.__spec__ = None` case;
   it must be classified, not accidentally made an unknown-mechanism HOLD.
   Class-valued builtin/frozen loaders must not collapse to the generic
   label `type`. This follows from the [direct-script contract](https://docs.python.org/3/reference/import.html#main-spec)
   and [BuiltinImporter/FrozenImporter definitions](https://docs.python.org/3/library/importlib.html#importlib.machinery.BuiltinImporter).
   The small pre-helper operations and the helpers actually imported must
   match the reviewed source; no discovery import is implicitly approved.
2. **Concrete launch/trust binding.** Resolve exact env/interpreter/script/
   cwd paths, flags, actual implementation/version, encodings and other
   recorded launch facts before probe authorization. Keep the proposed
   literal child environment separate from an assertion about pre-env
   state. If implemented with os.environ, label it as the Python-level
   mapping captured on os import under the stated trust boundary; it is
   not a continuously refreshed C-environment attestation.
   [Official environment-mapping semantics](https://docs.python.org/3/library/os.html#os.environ).
   No extra environment inspection or reloading is authorized by this note.
3. **Mechanism/source/cache separation.** Receive the approved known
   builtin/frozen/direct-script/ordinary-file classifications and actual
   eligible source/cache roles. Keep nominal frozen paths and actual file
   roles distinct. Capture all helper additions separately; the closing
   snapshot cannot silently repair an earlier missing dependency key.
4. **Finite frontier.** Exact allowlisted lexical paths/symlink targets,
   supported classes/encodings and numeric module/maps/file/per-file/total
   bounds remain unresolved. File-backed maps include non-executable maps.
   Unexpected observation is evidence to HOLD, not permission to extend
   the frontier. Do not turn import-internal trust into a sandbox claim.
5. **Keys and absence.** Implement bounded regular-file opening without a
   surprise FIFO/device content-read block, full same-fd EOF hashing, exact
   non-atime integer metadata and lexical/final/map identity comparisons.
   Preserve actual ENOENT separately from dangling symlink, ENOTDIR,
   permission and other errors; check named optional roles at both points.
   Integer nanosecond fields are not a promise of filesystem nanosecond
   precision or creation time. [os.stat_result](https://docs.python.org/3/library/os.html#os.stat_result).
6. **Single actual capture and independent reception.** Separately review
   the exact capture source/settings, exclusive paths and complete separate
   stdout/stderr/native/session returns before authorizing the one probe.
   Bound/truncation/transport/nonzero failures remain failures; no automatic
   retry, synthetic completion or author self-audited runtime acceptance.
   There is no hard-deadline or hostile-cancellation guarantee to infer.
7. **Later science stays separate.** After actual independent runtime
   reception, each initial run, canonical adoption and strict replay pair
   needs its own authorization/receipt and agreed before/after refresh.
   Different processes with matching launch settings/point keys are not
   proved runtime-identical. The fixed scientific box cannot expand; build,
   page views, physical Round0 and manuscript reviews are still later gates.

The read-only child challenge independently found no commissioning blocker
and highlighted the direct-script null and class-valued-loader cases. I
checked both directly against primary documentation; this verdict is not
based solely on a subagent summary. No observer/runtime-design source or
P213 mathematical contribution was made by either audit participant here.

## Handoff boundary

Root may receive this exact design audit as support for separately
commissioning minimal observer source. This report grants no operation.
The concrete binding, source review, separately authorized actual probe and
independent complete runtime reception do not exist in this audit packet.
No old source, title delta, review, failed evidence or central index was
edited. `OWNER_AMBER / HOLD_EXTERNAL` remains unchanged.
