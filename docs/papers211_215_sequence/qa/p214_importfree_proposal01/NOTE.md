# P214 json-dependency removal and two scope clarifications — proposal only

2026-09-11 UTC. `SOURCE_ONLY / NOT_ADOPTED / NOT_EXECUTED / HOLD_RUNTIME`.
No file in the sealed live P214 directory is changed by this proposal.
The directory's historical importfree name means a builtin-only JSON encoder;
the refined root instruction explicitly **retains import sys**.

## Exact requested delta

The complete five touched originals are under `originals/`; their complete
proposed replacements are under `proposed/`. [EXACT_DIFF.patch](EXACT_DIFF.patch)
is the actual unified diff for those five pairs, not a hand-written summary.

1. `verify.py`: remove only `import json`, add the small `wire_string` and
   `wire` helpers, and replace the `json.dumps(...)` argument with
   `wire(record)`. Keep sys, the original two stdout.write calls, the exact
   newline write, buffering behavior, argv rejection, failure handlers,
   exit codes, record/check counters and every scientific statement unchanged.
2. `OUTPUT_PLAN.md`: describe the removed json dependency and the proved
   output domain while retaining the future runtime-binding requirement.
3. `verification/SOURCE_STATUS.md`: update only the current import/codec
   description. Initial source handoff history remains untouched.
4. `sections/0_abstract.tex`: explicitly bound the cumulative-depth sentence
   by 0<=h<=2m-2.
5. `sections/2_clock.tex`: explicitly bound the exact positive-depth sentence
   by 1<=h<=2m-2. The admitted formula/proof already has this domain; this
   resolves two root-noted wording ambiguities, not a theorem change.

The full [proposed verifier](proposed/verify.py) uses no codec import,
introspection, lazy import, monkeypatch or launcher argument substitution.
The initial idea of removing sys would have broken the existing argv guard;
root explicitly rejected that control change before any proposal was written.

## Serializer scope and unchanged metadata

[SERIALIZER_PROOF.md](SERIALIZER_PROOF.md) proves exact spelling on all
P214-emitted builtin values: None, booleans, integers, arbitrary Python
strings, finite lists/tuples and string-keyed dictionaries, with acyclic
container references. It covers success records, mismatch payloads, CLI
rejection and caught runtime-error metadata. Printable ASCII, all controls,
DEL, BMP/non-BMP characters and lone surrogates are handled explicitly.

This is not a general replacement for every json.dumps input. Floats,
nonstring dictionary keys and custom scalar/container subclasses are outside
the proved source domain and rejected. The frozen program constructs none
of them. JSON output schema/version, field names, record order, check names,
parameters, mathematical comparisons and the planned 5271/10646 coverage
remain unchanged. No future CANONICAL.json is present; its eventual role
remains the complete JSONL stream, not one JSON object.

The original live SOURCE_HANDOFF.md and SOURCE_PREPARED.sha256 remain an
unchanged historical preparation package. They are not rewritten to pretend
the initial source lacked json. If root adopts the proposal, it must record
the exact five-file amendment and the new current input pins separately.
The JSONL schema itself needs no field or version change because the spelling
contract is unchanged on its complete reachable domain.

## Source reading and checks actually performed

The main author used proof-writer's exact-domain and induction discipline;
no additional agent or reviewer was spawned. The root independently reads
this proposal next; no source or review PASS is claimed here.

The live 28-payload source seal was checked before preparation. All five
original copies were then compared byte-for-byte with the live originals by
actual cmp and agreed. The first cmp commands had one too many parent-path
components and failed to locate live targets; absolute-path comparisons
corrected that navigation error. Both failed and successful native records
are retained in [SOURCE_RECORDS.json](SOURCE_RECORDS.json).

Each actual diff exits 1 because a proposed change exists. A document-only
reverse replacement restores the complete original verifier text exactly:
all bytes outside the import/helper/serialization delta are unchanged.
No Python parser, import, serializer test, scientific calculation, compiler,
host dependency discovery, build, canonical or benchmark was run.

Primary reference reads were the Python json documentation and the CPython
3.10 reference encoder source's string/container spelling branches. They are
semantic references, not a pin of the as-yet-unbound executing interpreter.
Actual saved web responses are included in SOURCE_RECORDS.json; the selected
read scope is stated in SERIALIZER_PROOF.md. No undocumented runtime identity
or reuse of the earlier 19-role key is certified by this proposal.

`INPUT_PINS.sha256` uses paths relative to the workspace root and pins the
unchanged live source inputs. The proposal's `SHA256SUMS` uses paths relative
to this directory, lists all 15 payload files and does not list itself.
Links inside the copied complete replacement documents retain their intended
live-P214-relative meaning; `proposed/` is a five-file amendment, not a second
complete paper tree.

## Requested next decision

Root may accept or reject this optional source simplification after reading
the complete originals, replacements, exact diff and domain proof. Adoption,
current runtime binding, any fresh checks and actual execution require
separate authority. The two wording changes are separately visible and do
not depend on adopting the serializer. No public/external action is requested.
