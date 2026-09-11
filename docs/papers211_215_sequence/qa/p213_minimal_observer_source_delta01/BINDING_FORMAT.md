# P213 finite-permission binding format V2 — documentary and disabled

This file supersedes the old exact-full-row *proposal* only within this new
source delta. No frozen predecessor is changed. BINDING.disabled.json is
not loaded by observe.py, and enabled=false/id=null/operation_authorized=false
do not constitute an enabled literal. The source keeps an unconditional
SystemExit and a separate BINDING=None gate. capture.sh exits before allocating
anything. Source pins, actual launch/module facts and all observed keys stay
null. A separately accepted enabled source, exact literal/capture/request and
one-probe grant are mandatory.

## Fields consumed only by a later independently accepted source

- id: a fixed reviewed identifier, unresolved here; not learned from a file.
- interpreter: the identical complete entry for the selected mandatory
  interpreter in files. lexical/final are chosen equal spellings; links=[].
- observer/cwd/env/bash/capture_mkdir: exact chosen absolute paths, not host
  observations. Only interpreter/observer/cwd are read by observer logic;
  the others constrain the separate capture review.
- launch_policy: CPython 3.10.12 final, cpython-310, Linux, exact argv/orig_argv,
  three exact sys.path strings, /usr prefixes, null pycache_prefix,
  dont_write_bytecode=true, 17 exact named flag requirements, UTF-8 encoding
  options and exact errors strings. All facts are compared to actual copies.
- flag_names: the complete 17-member ordered layout from the frozen proposal,
  duplicated verbatim from launch_policy.flag_names for the collector.
- module_names.early/helper/closing: exact finite allowed names, not predicted
  inventories. early has 23; helper and closing each have the same 62.
- required_module_names: exactly __main__, builtins, sys early; additionally
  os, hashlib, json after helpers. Earlier complete rows must remain present
  and unchanged. No removal/backfill is allowed.
- modules: one policy per allowed name. Each includes mechanism and file_roles;
  source/extension entries also include exact origin/file/cache/package_path,
  frozen entries an exact nominal_file, and direct_script its own file.
  observed_row remains null. provenance is documentary, never copied to an
  actual snapshot to fill missing values.
- loader_ids: a single exact tagged qualified class/instance permission for
  each mechanism, not a list of aliases or short class-name wildcard.
- special_maps: only empty, [heap], [stack], [vvar], [vdso], [vsyscall].
- files: exactly 69 distinct fixed candidates. Each entry has lexical,
  final=lexical, links=[], optional boolean, absence_required boolean,
  earliest_phase early/helper and a finite roles list. observed_presence and
  observed_key stay null. All present candidates must be regular and fully
  keyed; optional means only genuine no-link ENOENT is admissible.
- bounds: all positive integers, exactly the frozen proposal's limits.
  link_hops remains 1 for field compatibility but links must always be empty.

The documentary paths must be converted to one exact reviewed literal in an
enabled copy without loading JSON/config/source or inspecting unapproved
paths to fill it. id/source pins are not automatically supplied, and changing
the chosen observer/capture path is a new exact source/binding review.

## Immutable actual collection is unchanged

A module row is (name, present, builtin_membership, spec, module_loader,
file, cached, package_paths), all copied values, never module/spec objects.
The spec is missing/null or ("spec", origin, spec_loader, has_location,
search_locations). Scalars retain ("missing",), ("null",), ("value", value),
or ("sequence", tuple_of_tags). Qualified loaders retain class versus
instance and the tagged __module__/__qualname__. Both loader positions
must satisfy the selected permission separately.

The launch record still has seven parts: 18 named sys facts; all 17 named
flags; full str(sys.flags); every scalar/sequence implementation member;
stdout/stderr encoding/error tags; filesystem encoding; filesystem errors.
All were in the original collection design. Additional bounds now cover
implementation-member counts/names and untagged launch strings. The complete
immutable actual record is compared between early/second/helper/closing
using type-preserving same_tree. Other than the explicit chosen invariants,
ancillary scalars are observed, not given expected historical values.

## Five mechanisms; no mechanism widening

| Mechanism | Required actual observations | Explicit content candidates |
|---|---|---|
| builtin | Exact builtin-only allowed name; membership true; built-in origin; class-valued _frozen_importlib.BuiltinImporter in both loaders; has_location=false; null spec search; missing/null file/cache/package paths | None |
| frozen | One of three exact names; membership false; frozen origin; class-valued _frozen_importlib.FrozenImporter in both loaders; has_location=false; null spec search; cache/package paths missing/null; file missing/null or exact nominal label | None; nominal filenames are never read |
| source_file | Membership false; exact .py file=origin; SourceFileLoader instances in both loaders; has_location=true; exact selected .pyc cached field; exact package directory or nonpackage null/missing policy | Exact .py source_or_matching_source, required when row occurs; exact eligible_nonoptimized_cache, full key if present or genuine ENOENT |
| extension_file | Membership false; exact .so file=origin; ExtensionFileLoader instances in both loaders; has_location=true; cache/package missing/null and null spec search | Exact extension_origin full key required when row occurs; same file has mapped_file role |
| direct_script | __main__, membership false, null (not missing) spec, exact new observer file, SourceFileLoader instance, null cached and missing/null package path | New observer direct_script_source, mandatory |

Ordinary packages are only encodings, json and collections. Their spec and
module search sequences must both be the exact one-element directory list.
No namespace, zip, SourcelessFileLoader, extension spelling fallback, arbitrary
path alias or general builtin inclusion is allowed. os.path and posixpath
share exact source/cache candidates; when both occur their remaining seven
structural fields must agree.

SourceFileLoader can execute eligible .pyc while reporting a .py origin:
source_or_matching_source does not attest executed bytes. Under optimize=0,
cpython-310 and no cache prefix, each of the 29 source paths has one statically
selected nonoptimized __pycache__ candidate. No cache derivation helper runs.
The startup /usr/lib/python310.zip path is a required ENOENT candidate; if
present it is rejected after lstat and before any content open.

## Phase and file rules

Early names and launch facts are copied and validated before the first
explicit maps read; early maps are parsed/allowlisted before further explicit
access. The second complete early snapshot/launch must agree before imports.
Exactly os/hashlib/json are imported next under ordinary interpreter trust.
Their resulting full rows/launch are validated before helper maps and any
candidate file/proc access. Late unknowns cause HOLD before further explicit
access, not adaptive discovery. Implicit bootstrap/helper reads are not
instrumented, denied retroactively or presented as a syscall sandbox.

All 69 candidates are keyed once in a fixed preclosing pass. No content key
is acquired after closing_modules is sampled. An actual content or mapped-file
role requires a complete earlier key even if its entry was optional; a prior
absence can support only a non-content eligibility role. Mapped files require
device/inode agreement against full keys. Special maps require zero device
and inode, with all file-backed mappings checked, not just executable ones.

Full keys retain the original single-fd EOF/SHA-256, byte counts, ten exact
integer stat fields, path/fd/end-point comparisons, bounded sentinel accounting
and close-failure handling. Optional ENOENT and presence are checked again at
closing. No leaf symlink or unlisted final target is followed. Only ordinary
unscanned ancestor traversal is trusted. /proc/self/exe is followed by stat
only after its observed readlink target and both cwd strings are accepted.
No key proves continuous identity, mapped memory bytes, tool attestation or
the next scientific process's environment.

See COLLECTION_DELTA.md and CONTRACT.md for author remedies and remaining
independent gates. Original F01/F02 are not self-closed.
