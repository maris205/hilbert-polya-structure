# Finite runtime and artifact plan — not execution authority

Status: SOURCE_PLAN_ONLY / RUNTIME_IDENTITIES_UNRESOLVED.
This file was written before running or scientifically parsing verify.py.
It does not certify interpreter availability, installed versions, executable
paths, native library hashes, environment state or operational closure.

## Source reception before any scientific operation

The root-reviewed first gate must receive the exact verify.py bytes,
VERIFICATION_PARAMETERS.json, OUTPUT_SCHEMA.md and SCIENTIFIC_DEPENDENCIES.md,
plus the proof and complete source seal. An import, py_compile, compile(),
AST parse, smoke test or “syntax-only” interpreter pass counts as a later
scientific operation and is forbidden in this source milestone.

The sole scientific script uses Python 3 builtins with fixed parameters.
A possible later isolated invocation would use one resolved Python 3
interpreter, flags -I -S -B and the exact pinned verify.py path, with no
arguments after the script. This is a proposal only, not a runnable
authorization, resolved command or guarantee that all startup imports vanish.

## Runtime roles to resolve independently

The later finite gate must specify, within its authorized observation scope:

- The exact interpreter path/identity and relevant actual startup/native
  support under its declared trust boundary. No path or hash is invented.
- Whether encodings, I/O and startup support are supplied by frozen code,
  ordinary files, shared libraries or other actual mechanisms; the gate
  records what its finite contract actually promises.
- A controlled launch directory and the exact isolation/startup flags;
  no reliance on an unexamined environment or prior paper's closure claim.
- Complete native capture of stdout, stderr and exit status, with a
  transport limit high enough for all word-level records, and no silent
  truncation. The source buffers output but has no wall-time/memory guard.
- Explicit failure preservation and the boundary for any ordinary observer
  bootstrap. This plan does not require an unbounded chain of self-observers.

This author performs no host/configuration/proc/environment/credential
inspection to fill those roles. Any additional observer, wrapper or launcher
source must be separately received and authorized; it is not silently part
of verify.py or covered by the “no imports” statement.

## Initial run, canonical and strict author pair

After both source/parameter and runtime acceptance, the initial bounded
run may be commissioned. Preserve its exact command and full actual native
result, including failures. Only a complete accepted result matching
OUTPUT_SCHEMA may supply canonical_stdout.txt. The canonical is adopted
byte-for-byte from actual accepted stdout, never from hand-filled tables,
old candidate/gate data, reconstruction of a truncated result or a merely
matching count.

A separate strict author replay pair then uses exact pinned source,
parameters, runtime contract and canonical. Each replay must finish
successfully with complete receipts and exact byte equality; acceptance
of the initial run is not either replay. Failed evidence is retained and
cannot be relabelled or overwritten by a later success. No result from a
new/enlarged box is allowed under the present parameters.

## Manuscript and review artifacts after the scientific gate

The current minimal LaTeX source imports article.cls, amsmath, amssymb
(and its amsfonts dependency), amsthm, local math_commands.tex and the six
declared section files; it uses the standard plain bibliography style and
references.bib. The actual TeX/BibTeX executables, format, class/package,
font and style paths and runtime identities are unresolved. This source
manifest is not a claim of their operational closure.

An exact source-only initial build and actual view of every produced page
must precede physical Round0. Nothing has been built or viewed here.
No generated .aux/.bbl/.pdf is prefilled. Root fixes reviewer identities
and artifact interfaces before creating review packages; see
REVIEW_INTERFACES.md. A/accepted-delta/physical-Round1 and
B/accepted-delta/physical-Round2 remain separate. Two terminal physical
source-only builds and all-final-page views remain mandatory.

No external manuscript upload, specialist contact, public release, host
shortcut, private query or Git operation follows from this plan.
OWNER_AMBER / HOLD_EXTERNAL.

