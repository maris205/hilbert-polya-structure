# Binding format and unresolved selections

This is a source interface, not actual host data. All null fields in
BINDING.disabled.json remain unresolved. No guessed executable name, version,
module/cache inventory, alias target, metadata, hash or absence is supplied.
No external JSON is loaded by observe.py. A future source reviewer receives
the complete embedded literal BINDING and its exact new source pin.

The binding's top-level keys used by the observer are id, interpreter,
observer, cwd, launch_record, flag_names, module_names, modules, loader_ids,
special_maps, files and bounds. Additional documentary env/bash/capture_mkdir
and child_environment/interpreter_flags fields bind the capture request.
All selected paths must be literal absolute paths. The source's path grammar
is printable ASCII, no backslash, no duplicate slash or lexical dot segments.
Source-enabled bindings must be bounded, finite plain literal data; no
callable, file reader, comprehension/import or dynamic computation may be
inserted into the binding expression.

## Exact immutable data representation

Primitive values are ["value", value]; None is ["null"]; an absent attribute
is ["missing"]. Sequences are ["sequence", [tagged elements...]]. Tuple/list
differences are not runtime claims; the JSON representation is used for
exact scalar comparisons. Unsupported object-valued facts fail.

A module row has eight entries:

    [name, registry_present, builtin_membership, spec,
     module_loader, file, cached, package_paths]

A present spec is ["spec", origin, spec_loader, has_location, search_paths].
A loader is ["class" or "instance", tagged_module, tagged_qualname], or the
missing/null marker. For a class-valued builtin/frozen loader, the actual
class itself supplies the qualified name. The direct-script __main__ null
spec is known; a missing spec is not equivalent to it.

launch_record is the exact serialized launch_snapshot return: named sys
attributes; explicit named flags; full sys.flags string; all scalar
sys.implementation dictionary members; stdout/stderr encodings/errors;
filesystem encoding/error mode. flag_names must be the selected version's
complete applicable scalar flag field set, independently reviewed, not a
short list chosen to evade checks. Captured version_info is copied as a
tuple-derived scalar sequence, not retained as a mutable runtime object.

module_names maps early/helper/closing to exact sorted module-name lists.
modules maps every permitted name to {record, mechanism, file_roles}.
record is the entire expected eight-entry row, mechanism is one of builtin,
frozen, direct_script or ordinary_file. Namespace/unknown mechanisms are
not supported by this source. Every observed name must have a policy;
earlier modules cannot disappear/change even if a binding tries to omit
them from a later phase. Known additions remain explicitly late.

loader_ids maps each mechanism to a finite list of canonical JSON strings
for permitted qualified loader records. Both spec and module loader IDs
must match. The future binding reviewer must justify the exact concrete
CPython class identities from the selected version; generic type is not
an acceptable substitution. No observed class names are supplied here.

Each module file_roles member is {path, role, content_required}. Ordinary
__file__/origin and any eligible __cached__ path must be declared. The
ordinary/direct-script actual filename requires content_required=true.
Eligible cache or matching-source candidates can be optional and false;
they require a full key when present, or actual two-point absence when
legitimately absent. A frozen nominal filename must remain explicitly
nominal and cannot become executed-source evidence through this field.
The binding review owns exact source/cache eligibility for the chosen
loader/version, including any matching source for bytecode-origin cases.

special_maps lists exact supported anonymous/kernel-special path strings,
including the empty string if anonymous maps are approved. No names are
guessed here. File-backed paths are governed by files, not this list.

## Finite file entries

files is a unique lexical-path list of entries with exactly these roles:

    {lexical, final, links, optional, roles}

links is a finite ordered chain of {path, target, next}; target is the
literal readlink string and next is its already approved lexical resolution.
The final path is an ordinary file, not an implicit symlink resolution.
No links means final=lexical. Entries do not authorize reading ancestors.
interpreter is {lexical, final} matching its actual selected file entry.
The observer and interpreter entries are mandatory, nonoptional.

roles is a finite reviewed list of descriptive role labels. Every module
role must occur in its file entry. Every mapped-file entry must include
mapped_file; there is no executable-permission filter. Each file entry
must have a stated reason in the accepted binding; unused speculative
paths are not permission to scan. Optional entries are only selected
finite startup/eligibility candidates or preapproved closing candidates,
not a generic search frontier. verify.py is excluded from observer reads.

All files are acquired once before closing-module/map validation. A late
actual content dependency may use an already complete key; an absent
eligibility role is not complete content. The observer does not retry.

## Numeric bounds and capture

bounds needs positive integers for modules, maps_bytes, files, file_bytes,
total_bytes, scalar_chars, sequence_items, link_hops and stdout_bytes.
The future binding review must justify concrete small limits against the
selected finite inventory. No limit is a wall-time/deadline guarantee.
Map/file overflow detection admits one retained sentinel byte beyond its
successful-read bound. stdout_bytes must accommodate the entire intended
JSON, including three raw maps encodings and five module-snapshot records,
the separately exposed early/helper/closing facts, file keys and roles.
Setting a small number cannot turn a missing envelope into accepted data.

CAPTURE_REQUEST.disabled.json additionally needs exact Bash, env, mkdir,
new capture-source and observer-source paths, cwd, one new exclusive output
directory and its fixed stdout.bin/stderr.bin paths, exact native cmd and
all source/binding pins. Use login=false, tty=false and preserve every
actual continuation result. The capture source invokes env -i LANG=C
LC_ALL=C and the exact interpreter -I -S -B observer with no script args.
It does not open stdin. Its mkdir is nonrecursive and preexisting targets
fail. Capture/source review and a distinct one-probe grant precede creation.

An archive can suggest finite names/expected launch values; it supplies no
current metadata, presence, module inventory or startup identity. Current
accepted runtime evidence can arise only from the separately authorized
probe and independent full reception, never from filling this placeholder.
