# Independent source audit of the initial P212 pre-probe observer

Disposition: REVISION_REQUIRED_SOURCE_ONLY. One open source finding,
PSA-F1, prevents acceptance of the frozen 425-line observer. This is a
manual source/JSON review, not an observer run or a native-host attestation.
The input source SHA256 is
59f7e5060f338a224442ea3e38efffa9c4685e28ab52bf87750d25fb87dc57f5;
its author's nonself manifest SHA256 is
5741ce7f3dd3019b67d084d13dbd7672bd22e9a49ce575e18af96d6bbf8d3e29.

## Independence and exact scope

I did not author this new ctypes.Structure observer or its FRONTIER.
I previously authored the private-Git 202-line observer and contributed the
P212 execution-scope source amendment: the six literal source/path/hash
driver changes and accompanying frontier/source-graph/capsule prose.
Consequently this review does not independently accept that old code, nor
does it claim blind review or independent tooling. The new observer imports
only its stated ordinary Python facilities; it neither imports nor targets
my old private-Git observer. I have not authored a P212 mathematical proof.
The two old authorship handoffs are explicitly pinned and read here.

The root has explicitly accepted the ordinary trusted observer bootstrap
assumption. Reviewing it does not require a self-observer, bootstrap receipt
for its own imports, hostile-platform proof, or infinite recursive audit.
Existing accepted P212 source/boundary receipts are inputs reused in their
bounded scope, not new independent acceptance of every historical dependency.

## PSA-F1: resolved identity is checked only after content has been read

In observe.py lines 221-252, whole_file receives a path, byte limit and
capture flag but no expected resolved key. It opens that path (224), obtains
the same-fd native key (226), checks regular-file kind and size (227-228), and
starts os.read at 233. The caller obtains the resolved key first but does not
compare it to the fd key until lines 269-270, after whole_file has returned.

A finite deductive counterexample suffices: resolve records regular A;
opening the same approved spelling obtains a different, bounded regular B;
native(fd) identifies B; the loop reads B; only after those reads does the
caller reject A versus B. The proposed contract needs a detected wrong
identity to stop before content consumption. Eventual HOLD does not undo a
body read. This counterexample is source reasoning, not an executed race test.

Required minimal correction: pass the expected resolved key into whole_file,
perform the existing stable(expected, before) immediately after native(fd)
and before any os.read, and pass before['stat'] from observe_target. Retain
the current same-fd post-read comparison, complete byte-count check, and
caller's post-return comparison. No broad rewrite is required.
Root independently read the offending lines and agreed to author a new
sibling correction; this original report and author package remain frozen.
A later delta must receive a separate audit, not overwrite this finding.

## Other reviewed mechanisms and bounded conclusions

- Native representation: Stamp is 16 bytes and Statx has a declared 256-byte
  envelope with an uninterpreted 112-byte tail at offset 144. The source
  checks Linux/little-endian LP64 sizes and every used field offset before
  target calls. Signed seconds and bounded unsigned nanoseconds preserve
  integer nanoseconds. The source requests 0xFFF, requires all those returned
  bits, preserves rc/errno/mask/raw 256-byte buffer before decoding, and has
  no zero/ctime birthtime fallback. Device numbers use ordinary os.makedev.
  This matches the referenced Linux UAPI shape; no actual host support or
  ctypes layout has been tested.
- The fourteen decimal-string fields and stable comparison policy are
  explicit. Leaves exclude atime only; intermediate directories compare
  dev/ino/mode/uid/gid/rdev/birthtime identity and retain other fields without
  claiming stable unrelated directory contents. Missing mask or unsupported
  ABI fails rather than silently reducing the key.
- Apart from PSA-F1, whole-file reads use the same fd for before/after keys,
  complete SHA256 and observed byte count. Regular kind and literal limits
  precede reading; O_NOFOLLOW prevents following a terminal link at open;
  O_NONBLOCK does not provide a hard regular-file read timeout. Per-file,
  aggregate-read, capture and output ceilings are explicit, with a permitted
  one-byte read-growth sentinel. Failed partial body bytes are not promised
  to survive as complete captures.
- resolve separates lexical lstat, actual link text, component-chain rows
  and the final followed observation. It checks each next component against
  the literal permissions before a native call; unexpected link destinations
  are rejected before explicit traversal. ENOENT and the separately justified
  ENOTDIR case alone represent absence; other errors fail. This is bounded
  discrete path observation, not an atomic namespace or adversarial-race
  exclusion. In particular O_NOFOLLOW constrains only open's terminal
  component, not all ancestor lookups.
- Membership deliberately uses path-bracketed os.scandir and entry.name
  only, preserving name/ordinal events with a finite ceiling, exact expected
  names, and two-pass comparison. It does not call DirEntry.stat/is_dir,
  recurse, or consume member bodies. This is not a same-directory-fd
  attestation. The stated contract requires path brackets/two-pass names;
  therefore no separate source defect or mandatory same-fd directory
  upgrade is raised. A stronger future promise would need a new mechanism.
- The first target failure stops later targets and the next planned pass;
  closing controls are skipped on failure. Completed rows plus accumulated
  raw native/path events survive normal caught failures. Output overflow,
  failed transport or failed stdout cannot be interpreted as a complete
  success. The serialized 128-MiB check is not a peak-memory/time guarantee.
- Canonical external authorization is required before native initialization;
  fixed source/trust/frontier control paths are fully keyed at opening and,
  only after success, closing. The supplied control is disabled, all three
  pins are null, and no bootstrap-receipt-self-key is requested. A successful
  observation would still fix observer_bootstrap_attested=false,
  author_probe_executed=false and closure_certified=false.

The native shape/mask reasoning is supported by the actual complete tagged
[Linux stat.h](https://raw.githubusercontent.com/torvalds/linux/v6.8/include/uapi/linux/stat.h)
and flag definitions in
[Linux fcntl.h](https://raw.githubusercontent.com/torvalds/linux/v6.8/include/uapi/linux/fcntl.h).
Terminal O_NOFOLLOW and the regular-file O_NONBLOCK limitation follow
[Linux open(2)](https://man7.org/linux/man-pages/man2/open.2.html).
The bounded API distinction between descriptor reads and directory-name
iteration follows the retrieved portions of
[Python os documentation](https://docs.python.org/3.10/library/os.html).
These are upstream semantic references, not evidence of installed versions.

## Initial frontier is not dependency closure

The complete 2159-line FRONTIER was read in three contiguous segments and
parsed only as JSON data in the orchestration layer, with a recorded
ASCII-canonical round trip. It declares 164 targets and 204 components:
109 required files, 32 optional files, 11 optional directories, five
memberships, six metadata roles and one required absence. The five exact
name guards total 292 names (22/12/1/256/1); 120 targets request bounded raw
capture; 40 permitted components are ancestor/alias-only.

These are documentary properties, not current observations. The _ctypes ELF
and exact libffi dependency/alias frontier, full normal/error-path Python
imports and startup states, Node's six named builtins and lazy/native
dependencies, current configuration-driven paths, masks and actual fourteen
fields remain unresolved. No guessed libffi filename, wildcard scan, source
import, current configuration read or author probe is authorized by this
report. All author probes, driver, outer operational runs, P211 execution,
Git/SSH, build and external phases remain HOLD.

## Evidence and census

[READ_SCOPE.md](READ_SCOPE.md) distinguishes complete new-source reads from
background reuse and pin-only auxiliary files. [READS_NATIVE.json](READS_NATIVE.json)
holds 34 actual read/hash command returns, including unchanged before/after
pins for all 36 documentary inputs. The author's 17 payload hashes and 16
background pins passed their actual SHA256 checks. All 36 inputs have
1,719,272 bytes in the saved wc result; hash equality is documentary integrity,
not a current native runtime key. [JSON_PROJECTION.json](JSON_PROJECTION.json)
contains JSON-only counts and closure gaps. [PRIMARY_SOURCES.json](PRIMARY_SOURCES.json)
records the actual public requests and bounded read/use metadata.
[FINDINGS.json](FINDINGS.json) has exactly one OPEN source finding.

No Python/Node interpreter, import, AST, syntax test, observer, author probe,
driver, host dependency/configuration/proc/environment/credential query,
Git operation or build was performed. There is no execution receipt and no
source acceptance of the original 425-line body.
