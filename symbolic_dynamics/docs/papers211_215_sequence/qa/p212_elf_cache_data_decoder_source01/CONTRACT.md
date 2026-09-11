# P212 ELF/cache literal DATA decoder — source proposal

SOURCE_ONLY / HOLD_OPERATIONAL / HOLD_EXTERNAL. No actual body decoded.
The only proposed code is decode.proposed.mjs.txt, exporting
decodeCapturedBodies(buffers, manifestRaw, trustedManifestPin). It imports
only ordinary node:crypto and uses in-memory Buffer/BigInt/JSON operations.
There is no filesystem/process import, operational callback, module loading
from DATA, pointer invocation, path following, live selector or observation.

## Authenticated input, not a new observer

The first argument is exactly seven complete Buffers in this fixed order:
BASH, ENV, KPSEWHICH, LOADER_CANDIDATE, LIBC_CANDIDATE, TINFO_CANDIDATE,
LOADER_CACHE. The accepted envelope/body extractor supplies these existing
bytes; this decoder does not import that extractor or reopen any file.
Six images retain the16MiB/body limits; cache retains1MiB. The separately
authenticated manifest binds exact id/path/role, whole body length/hash,
received full-key receipt reference and root body-reception reference.
The existing SYSTEM_PRELOAD absence has its own actual received reference;
there is no absent body to parse or invented repeated absence observation.

Root must verify each referenced complete body key and its role against
the already accepted DATA reception before authenticating this manifest.
The outside trustedManifestPin must NOT come from that manifest itself.
The decoder recomputes every whole-body SHA256. References are typed DATA,
not self-authenticating receipts or instructions to read a path. Ordinary
trusted Node/crypto/parser/bootstrap is explicit, not recursively measured.
The current request has no invented body pins, external receipts or invocation.

## Finite literal interpretation

The supported ELF subset is ELF64, little endian, EM_X86_64, ET_EXEC/ET_DYN,
current ident/header version, SystemV/GNU ABI with ABI-version0, normal
64byte header/56byte program entries and nonextended program count. This
is a source support declaration, NOT a claim about any captured body.
Other formats/indirections receive a precise named HOLD and retained partial
literal table. All64bit addresses/values are BigInt until a checked file
offset conversion; no integer truncation is used.

Each image records class/endian/machine/header fields, all program headers,
PT_INTERP, every dynamic descriptor through DT_NULL and the entire required
zero-only tail. Full table/segment bounds and unique file-backed PT_LOAD
translations are checked. Duplicate singleton tags, ambiguous mappings,
unterminated strings and nonzero hidden dynamic tails stop that image.
Strings are unnormalized printable ASCII; other name encodings are HOLD.
Exact spans include containing body id/pin, byte offset/length and fresh
span SHA256. The pinned body retains original bytes for every span.

NEEDED order and all SONAME/RPATH/RUNPATH/AUDIT/DEPAUDIT/CONFIG/AUXILIARY/
FILTER strings are retained. RPATH/RUNPATH/audit colon components remain
literal names; no token, relative path, empty component or alias is expanded.
Each INIT/FINI descriptor and every PREINIT/INIT/FINI array slot is retained,
including zero values. Raw slot values are explicitly UNRELOCATED DATA;
resolved_code_role stays null, with the exact slot/table marked for matching
relocation/source-role evidence. An address is not a code-behavior proof.
No relocation application, dynsym/IFUNC resolution, symbol/version/note
interpretation or machine-code disassembly is silently performed. Ordinary
relocation/symbol/version tags are retained as uninterpreted descriptors;
this is not a claim those mechanisms are absent. Unknown dynamic/program
tags and nonzero loader flags remain named source/loader-rule obligations.

The cache subset is standalone glibc new1.1 format with explicit little/
big-endian flag, bounded24byte rows/string table and extension directory.
Legacy/compat cache, unknown endian flag, malformed offsets or unsupported
extension layout are named HOLD, not guessed using this host's byte order.
All cache rows and their terminated key/path strings are checked; only
rows whose names equal a finitely decoded load name are emitted. Every
same-name row is retained WITHOUT architecture/OS/hwcap eligibility filtering.
New hwcaps index/ISA metadata, extension index span and subdirectory literal
are included when present; old nonzero hwcap masks are preserved as raw DATA.
Unknown sections are not hidden, and malformed structures are not skipped.

This is a complete scan for the FINITELY DECODED names only, NOT proof that
those names are a complete installed graph when an ELF has a HOLD. Cache
rows are labelled UNFILTERED_SAME_NAME_CACHE_CANDIDATE_NOT_SELECTED.
Default/RPATH/RUNPATH/environment/hwcaps alternatives and actual eligibility
still need matched loader rules and selector facts or a complete finite
conservative set. No default directories, `$ORIGIN` expansion, exact selected
image, alias target, installed version or loaded map is invented.

The existing ceilings remain32image nodes,96distinct named states and64
init/fini entries globally. This exact invocation has only six image bodies;
it does not enlarge to32or follow newly found names automatically. Named
states include the original seven body paths and preload absence, then
literal dynamic components and relevant candidate paths. Repeated literal
names share a census entry while their individual source spans remain in
the image/cache tables. Bound failure preserves the partial table with
the exact rejected span; it never enlarges the limit or starts another probe.
Array size and cache/table extents are bounded by actual captured bytes;
these are finite parsers, not hard CPU/memory/storage guarantees.

## What the result authorizes

Nothing operational. It is a literal B1/B2 input table plus precise HOLD
rows for a later finite named follow-up. Each needed literal can be joined
to all emitted same-name cache rows without asserting loader selection.
Actual package/build/source roles, selected/candidate whole keys, alias text,
ENV8=C.UTF-8, relevant B3/B4branches and remaining B/S/tool/paper gates stay
open at their existing scope. No generic whole-libc/no-writer theorem or
new bootstrap observer is required by this decoder. The old scientific pair
is untouched. Source reception must precede any actual body interpretation.

## Actual preparation

Read the full next-step NOTE and complete DEPENDENCY_GATE. Narrow searches
and their limits are in SOURCE_AND_REUSE.md. Read primary format/loader
documentation only for source semantics. Source was authored with apply_patch;
no import, syntax/AST test, synthetic case, actual body parse, ldd/readelf/
kpsewhich, host/proc/private query, grant, child, science/build, central or Git
action occurred. No independent review/PASS is claimed. One arithmetic
constant was corrected during unexecuted author drafting to use the exact
upstream unsigned32 conversion; there is no failed decoder execution.
