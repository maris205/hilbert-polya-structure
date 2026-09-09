# C424–C428 independent post-seal member verification

2026-09-09 UTC. **PASS — independent byte/member verification only.**
The actual single checker invocation completed at
`2026-09-09T11:05:15.384038+00:00`, exit **0**, using Python 3.12.3.
No staged-index, commit, push or publication result is claimed here.

## Authority, method and actual findings

The coordinator explicitly supplied the following literal ledger pin
after recording it in the outside [approval receipt](RELEASE_C424_C428.md)
and confirming actual check/seal/verify success. This checker freshly
read that receipt before execution. It did not derive a new trust pin
from the live ledger:

`0441eb689728c3ca06b4ba63ebaee62af0676d69c57a1c7f123c5df95caa4fc0`.

The approved root is
`/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c424_c428`.
The fixed producer's full 279-line source and member/metadata contract
were read during preparation; its SHA256 was
`529ad136f29879c5bb659171127b45e7edb8e5b3c05044b4e43e035114cd444f`.
The actual checker below **neither imports nor invokes that producer**.
It uses independently written standard-library `os.fwalk` traversal,
descriptor-relative nonfollowing reads, streaming SHA256 and its own
strict metadata validation and manifest reconstruction.

The scan covered every actual member, including ignored/hidden files,
historical build outputs and bytecode, without using Git's member list.
All six root/ancestor directory opens rejected symlink traversal.
Every payload and metadata file was regular and single-linked; no
symlink, special file or unrepresented empty directory was accepted.
Directory membership and file-read metadata stability checks passed.
The 162 subdirectories exactly equal the set of proper file ancestors.

The raw ledger matched the fixed external pin; JSON duplicate keys,
unknown keys, wrong types (including Boolean integers), nonfinite
numbers, unsafe paths, unsorted/duplicate entries, invalid totals and
noncanonical bytes are rejected by the executed checker. All measured
payload names, lengths and SHA256 values matched the entire ledger.
The manifest was reconstructed from the **measured actual payload**
plus the approved ledger pin, sorted canonically and byte-compared.
It includes the ledger and all payload files and excludes only itself.

| Independently measured object | Files / rows | Bytes |
| --- | ---: | ---: |
| Payload, excluding the two root metadata files | 1,157 files | 81,980,859 |
| Canonical ledger | 5,792 lines | 229,388 |
| Canonical manifest | 1,158 rows | 149,896 |
| Entire sealed root, including both metadata files | 1,159 files | 82,360,143 |

Actual manifest SHA256:
`bbaa5b44994c032c663155f6eb72789fb28d3d8f82ed14d24e33bbe78b648f3e`.

The five final PDF identities were fixed from the frozen build report
during preparation, before this ledger was available. For each paper,
the actual `main.pdf`, `main_round1.pdf`, `main_round2.pdf` and both
fresh final-build copies matched that independent length/digest anchor:
**five papers, 25 matched copies**. The final integration report also
matched the coordinator's literal
`53908c308400cd66a8f89bc6b8db648e5fc329cf16cb172c1bf4013a63665f7c`.
There were **zero failed checks or unresolved findings** in this execution.

## Scope and limits

Only this outside report was written, using apply_patch after the
successful scan. No package member was modified; C424 and C425 remain
frozen. Mathematical programs, PDF compilation/rendering, old release
tests, producer-verifier calls and Git writes during this check: zero.
Hashing the preserved bytecode did not execute or import it.

This is a separate implementation of local byte/member verification,
not authentication against replacement of the verifier and external
pin, a hostile-concurrency guarantee, a filesystem snapshot, a renewed
mathematical/source review or human peer review. It relies on the
coordinator's quiescent-tree boundary and checks ordinary read-time
changes. Earlier PDF page/quality conclusions are not relabelled as
fresh page inspection. Staged-index verification requires a later
explicit coordinator notification.

## Actual execution output

Command: the exact inline program in the next section was run once
with `python3 -B -` from
`/root/autodl-tmp/hilbert-polya-structure`, without creating a script or
temporary file in the payload. The measured elapsed time was
0.119 seconds. Actual terminal exit: **0**.

```json
{
  "all_file_bytes": 82360143,
  "all_regular_files": 1159,
  "completed_utc": "2026-09-09T11:05:15.384038+00:00",
  "elapsed_seconds": 0.119,
  "exact_members_lengths_digests_canonical_ledger_and_manifest": true,
  "five_preapproved_pdf_identities_and_25_copies": [
    {
      "bytes": 463423,
      "matched_copies": 5,
      "paper": "C424_integer_valued_quadratic",
      "sha256": "3a1eadac84dd7fe9b730cde464bbc31a80469963aa984ac3a7117936e7bdf98b"
    },
    {
      "bytes": 378223,
      "matched_copies": 5,
      "paper": "C425_fricke_return",
      "sha256": "e7330f65920c40c566b01ee0d864d9f5a023c70010954e8af633c325f92c1dcb"
    },
    {
      "bytes": 343725,
      "matched_copies": 5,
      "paper": "C426_affine_good_models",
      "sha256": "d0b4e14e8ed42002bf0ad454ee004c817403e9662ae92b25306a94adf4d582db"
    },
    {
      "bytes": 346694,
      "matched_copies": 5,
      "paper": "C427_vieta_semilinear",
      "sha256": "cae339b829dd8a4ca0c57accc75b3a9a3ced62173f49402e853e6d63c2d91bd1"
    },
    {
      "bytes": 389314,
      "matched_copies": 5,
      "paper": "C428_integer_period_spectrum",
      "sha256": "cf02bdd886584949847f2583904601bb2734010a5f9d9cafbcbe749ddb0553af"
    }
  ],
  "ledger_bytes": 229388,
  "ledger_lines": 5792,
  "ledger_sha256": "0441eb689728c3ca06b4ba63ebaee62af0676d69c57a1c7f123c5df95caa4fc0",
  "manifest_bytes": 149896,
  "manifest_rows": 1158,
  "manifest_sha256": "bbaa5b44994c032c663155f6eb72789fb28d3d8f82ed14d24e33bbe78b648f3e",
  "metadata_files": 2,
  "payload_bytes": 81980859,
  "payload_files": 1157,
  "python": "3.12.3",
  "root": "/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c424_c428",
  "root_and_ancestor_directories_checked": 6,
  "started_utc": "2026-09-09T11:05:15.264865+00:00",
  "status": "PASS",
  "subdirectories": 162,
  "symlinks_specials_multilink_files_empty_dirs_or_unstable_reads": 0
}
```

## Exact independent checker executed

This is the complete program used for the result above, not a call to
the producer or a proposed unexecuted check.

```python
import hashlib, json, os, re, stat, sys, time
from datetime import datetime, timezone

ROOT = "/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c424_c428"
PIN = "0441eb689728c3ca06b4ba63ebaee62af0676d69c57a1c7f123c5df95caa4fc0"
MANIFEST_PIN = "bbaa5b44994c032c663155f6eb72789fb28d3d8f82ed14d24e33bbe78b648f3e"
RESERVED = {"PAYLOAD_LEDGER.json", "MANIFEST.sha256"}
LIMIT = 16 * 1024 * 1024
started = datetime.now(timezone.utc).isoformat()
tick = time.monotonic()

def need(condition, message):
    if not condition:
        raise RuntimeError(message)

def safe(name):
    need(type(name) is str and bool(name), "invalid path type/empty path")
    need(all(p not in ("", ".", "..") and re.fullmatch(r"[A-Za-z0-9_.-]+", p)
             for p in name.split("/")), "unsafe path: " + repr(name))

def signature(info):
    return (info.st_dev, info.st_ino, info.st_mode, info.st_nlink,
            info.st_size, info.st_mtime_ns, info.st_ctime_ns)

def sha(data):
    return hashlib.sha256(data).hexdigest()

# Independent traversal: standard-library fwalk, not the producer's recursive scan.
flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
root_fd = os.open("/", flags)
ancestor_count = 1
for component in ROOT.split("/")[1:]:
    safe(component)
    before = os.stat(component, dir_fd=root_fd, follow_symlinks=False)
    need(stat.S_ISDIR(before.st_mode), "root ancestor is not a real directory")
    next_fd = os.open(component, flags, dir_fd=root_fd)
    need(signature(before) == signature(os.fstat(next_fd)), "root ancestor changed")
    os.close(root_fd)
    root_fd = next_fd
    ancestor_count += 1

files, metadata, expected_dirs, visited_dirs = {}, {}, {}, {}
expected_dirs[""] = signature(os.fstat(root_fd))

def traversal_error(exc):
    raise exc

try:
    for local, dirnames, filenames, directory_fd in os.fwalk(
            ".", topdown=True, onerror=traversal_error,
            follow_symlinks=False, dir_fd=root_fd):
        relative = "" if local == "." else local[2:]
        seen_stamp = signature(os.fstat(directory_fd))
        need(seen_stamp == expected_dirs[relative], "directory changed before visit: " + relative)
        visited_dirs[relative] = seen_stamp
        dirnames.sort()
        filenames.sort()
        for name in dirnames:
            entry = relative + "/" + name if relative else name
            safe(entry)
            info = os.stat(name, dir_fd=directory_fd, follow_symlinks=False)
            need(stat.S_ISDIR(info.st_mode), "symlink/non-directory entry: " + entry)
            need(entry not in expected_dirs, "duplicate directory")
            expected_dirs[entry] = signature(info)
        for name in filenames:
            entry = relative + "/" + name if relative else name
            safe(entry)
            observed = os.stat(name, dir_fd=directory_fd, follow_symlinks=False)
            need(stat.S_ISREG(observed.st_mode), "symlink/special file: " + entry)
            need(observed.st_nlink == 1, "hardlinked regular file: " + entry)
            need(entry not in files, "duplicate actual file")
            fd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK,
                         dir_fd=directory_fd)
            try:
                first = os.fstat(fd)
                need(signature(first) == signature(observed), "file changed while opening: " + entry)
                digest, length, saved = hashlib.sha256(), 0, []
                while True:
                    block = os.read(fd, 1048576)
                    if not block:
                        break
                    digest.update(block)
                    length += len(block)
                    if entry in RESERVED:
                        need(length <= LIMIT, "metadata exceeds 16 MiB")
                        saved.append(block)
                need(length == first.st_size, "short/long file read: " + entry)
                need(signature(first) == signature(os.fstat(fd)), "file changed while hashing: " + entry)
                files[entry] = (length, digest.hexdigest())
                if entry in RESERVED:
                    metadata[entry] = b"".join(saved)
            finally:
                os.close(fd)
    need(set(visited_dirs) == set(expected_dirs), "unvisited or unexpected directory")
    for directory, stamp in expected_dirs.items():
        current = os.stat(directory or ".", dir_fd=root_fd, follow_symlinks=False)
        need(stamp == signature(current), "directory changed during full scan: " + directory)
finally:
    os.close(root_fd)

ancestors = set()
for name in files:
    components = name.split("/")
    ancestors.update("/".join(components[:n]) for n in range(1, len(components)))
need(set(visited_dirs) - {""} == ancestors, "empty/unrepresented directory")
need(set(metadata) == RESERVED, "missing root metadata")
raw = metadata["PAYLOAD_LEDGER.json"]
need(re.fullmatch(r"[0-9a-f]{64}", PIN) is not None, "invalid literal pin")
need(sha(raw) == PIN, "ledger does not match external literal approval")

def unique_object(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, "duplicate JSON key")
        result[key] = value
    return result

def nonfinite(value):
    raise RuntimeError("nonfinite JSON: " + value)

ledger = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_object,
                    parse_constant=nonfinite)
need(type(ledger) is dict and set(ledger) ==
     {"schema", "payload_count", "payload_bytes", "files"}, "ledger shape")
need(ledger["schema"] == "c414-c418-exact-payload-v1", "ledger schema")
need(type(ledger["files"]) is list, "files must be list")
for key in ("payload_count", "payload_bytes"):
    need(type(ledger[key]) is int and ledger[key] >= 0, "invalid total type/value")
expected, previous = {}, None
for row in ledger["files"]:
    need(type(row) is dict and set(row) == {"path", "bytes", "sha256"}, "entry shape")
    safe(row["path"])
    need(row["path"] not in RESERVED, "reserved root metadata in ledger")
    need(previous is None or previous < row["path"], "unsorted/duplicate ledger paths")
    previous = row["path"]
    need(type(row["bytes"]) is int and row["bytes"] >= 0, "invalid file byte count")
    need(type(row["sha256"]) is str and
         re.fullmatch(r"[0-9a-f]{64}", row["sha256"]) is not None, "invalid digest")
    expected[row["path"]] = (row["bytes"], row["sha256"])
need(ledger["payload_count"] == len(expected), "ledger count")
need(ledger["payload_bytes"] == sum(x[0] for x in expected.values()), "ledger byte total")
canonical = (json.dumps(ledger, ensure_ascii=True, sort_keys=True, indent=2,
                        allow_nan=False) + "\n").encode("ascii")
need(raw == canonical, "noncanonical ledger bytes")
actual = {name: data for name, data in files.items() if name not in RESERVED}
need(set(actual) == set(expected), "exact payload set mismatch")
need(actual == expected, "payload length/digest mismatch")
need(set(files) == set(expected) | RESERVED, "extra/missing physical member")
need((len(actual), sum(x[0] for x in actual.values())) == (1157, 81980859),
     "approved payload totals mismatch")
manifest_hashes = {name: data[1] for name, data in actual.items()}
manifest_hashes["PAYLOAD_LEDGER.json"] = PIN
rebuilt = "".join(manifest_hashes[name] + "  " + name + "\n"
                  for name in sorted(manifest_hashes)).encode("ascii")
need(metadata["MANIFEST.sha256"] == rebuilt, "noncanonical/inexact manifest")
need(sha(rebuilt) == MANIFEST_PIN, "manifest receipt digest mismatch")
need(files["release/REVIEW_INTEGRATION.md"][1] ==
     "53908c308400cd66a8f89bc6b8db648e5fc329cf16cb172c1bf4013a63665f7c",
     "final integration report identity")

# Pre-ledger anchors read from the frozen final-build report during preparation.
papers = [
 ("C424_integer_valued_quadratic", 463423, "3a1eadac84dd7fe9b730cde464bbc31a80469963aa984ac3a7117936e7bdf98b", "build/final_frozen_"),
 ("C425_fricke_return", 378223, "e7330f65920c40c566b01ee0d864d9f5a023c70010954e8af633c325f92c1dcb", "build_final_"),
 ("C426_affine_good_models", 343725, "d0b4e14e8ed42002bf0ad454ee004c817403e9662ae92b25306a94adf4d582db", "builds/final_"),
 ("C427_vieta_semilinear", 346694, "cae339b829dd8a4ca0c57accc75b3a9a3ced62173f49402e853e6d63c2d91bd1", "builds/final_"),
 ("C428_integer_period_spectrum", 389314, "cf02bdd886584949847f2583904601bb2734010a5f9d9cafbcbe749ddb0553af", "builds/final_"),
]
pdf_results = []
for paper, size, digest, prefix in papers:
    names = ["main.pdf", "main_round1.pdf", "main_round2.pdf",
             prefix + "01/main.pdf", prefix + "02/main.pdf"]
    for name in names:
        need(files["papers/" + paper + "/" + name] == (size, digest),
             "frozen PDF identity mismatch: " + paper + "/" + name)
    pdf_results.append({"paper": paper, "bytes": size, "sha256": digest, "matched_copies": 5})

result = {
 "status": "PASS", "started_utc": started,
 "completed_utc": datetime.now(timezone.utc).isoformat(),
 "elapsed_seconds": round(time.monotonic() - tick, 3),
 "python": sys.version.split()[0], "root": ROOT,
 "root_and_ancestor_directories_checked": ancestor_count,
 "payload_files": len(actual), "payload_bytes": sum(x[0] for x in actual.values()),
 "all_regular_files": len(files), "all_file_bytes": sum(x[0] for x in files.values()),
 "subdirectories": len(ancestors), "metadata_files": 2,
 "ledger_bytes": len(raw), "ledger_lines": raw.count(b"\n"), "ledger_sha256": sha(raw),
 "manifest_bytes": len(rebuilt), "manifest_rows": rebuilt.count(b"\n"),
 "manifest_sha256": sha(rebuilt),
 "symlinks_specials_multilink_files_empty_dirs_or_unstable_reads": 0,
 "exact_members_lengths_digests_canonical_ledger_and_manifest": True,
 "five_preapproved_pdf_identities_and_25_copies": pdf_results,
}
print(json.dumps(result, ensure_ascii=True, sort_keys=True, indent=2))
```
