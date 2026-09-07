#!/usr/bin/env python3
"""Exact, externally pinned payload inventory and no-overwrite release seal.

This checks bytes and members, not mathematical validity or authenticity.
Run with -B, from outside the release root, on a quiescent local tree.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import secrets
import stat
import sys

LEDGER = "PAYLOAD_LEDGER.json"
MANIFEST = "MANIFEST.sha256"
SCHEMA = "c414-c418-exact-payload-v1"
RESERVED = frozenset((LEDGER, MANIFEST))
HEX = re.compile(r"[0-9a-f]{64}\Z")
COMPONENT = re.compile(r"[A-Za-z0-9_.-]+\Z")
META_LIMIT = 16 * 1024 * 1024


class InvalidRelease(ValueError):
    """The release does not meet the explicit contract."""


def require(condition, message):
    if not condition:
        raise InvalidRelease(message)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def valid_path(path):
    require(type(path) is str and bool(path), "empty/non-string payload path")
    parts = path.split("/")
    require(all(p not in ("", ".", "..") and COMPONENT.fullmatch(p)
                for p in parts), f"unsafe payload path: {path!r}")
    return parts


def canonical(value):
    return (json.dumps(value, ensure_ascii=True, sort_keys=True, indent=2,
                       allow_nan=False) + "\n").encode("ascii")


def stamp(info):
    return (info.st_dev, info.st_ino, info.st_mode, info.st_nlink,
            info.st_size, info.st_mtime_ns, info.st_ctime_ns)


def open_root(root):
    """Open each root component without following links, including ancestors."""
    require(".." not in Path(root).parts, "root may not contain '..'")
    absolute = Path(os.path.abspath(root))
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        for component in absolute.parts[1:]:
            following = os.open(component, os.O_RDONLY | os.O_DIRECTORY |
                                os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = following
        return fd
    except BaseException:
        os.close(fd)
        raise


def scan(root):
    """Hash every regular file, including ignored/hidden files; reject aliases."""
    files, metadata, directories = {}, {}, set()

    def visit(directory_fd, prefix):
        before = os.fstat(directory_fd)
        with os.scandir(directory_fd) as entries:
            names = sorted(entry.name for entry in entries)
        for name in names:
            path = f"{prefix}/{name}" if prefix else name
            valid_path(path)
            observed = os.stat(name, dir_fd=directory_fd, follow_symlinks=False)
            if stat.S_ISDIR(observed.st_mode):
                child_fd = os.open(name, os.O_RDONLY | os.O_DIRECTORY |
                                   os.O_NOFOLLOW, dir_fd=directory_fd)
                try:
                    require(stamp(observed) == stamp(os.fstat(child_fd)),
                            f"directory changed while opening: {path}")
                    directories.add(path)
                    visit(child_fd, path)
                finally:
                    os.close(child_fd)
            else:
                require(stat.S_ISREG(observed.st_mode),
                        f"symlink or special file rejected: {path}")
                require(observed.st_nlink == 1, f"hard-linked file rejected: {path}")
                fd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK,
                             dir_fd=directory_fd)
                try:
                    first = os.fstat(fd)
                    require(stamp(first) == stamp(observed),
                            f"file changed while opening: {path}")
                    digest, count, chunks = hashlib.sha256(), 0, []
                    while True:
                        chunk = os.read(fd, 1024 * 1024)
                        if not chunk:
                            break
                        count += len(chunk)
                        digest.update(chunk)
                        if path in RESERVED:
                            require(count <= META_LIMIT, f"oversize metadata: {path}")
                            chunks.append(chunk)
                    require(count == first.st_size and stamp(first) == stamp(os.fstat(fd)),
                            f"file changed while hashing: {path}")
                    files[path] = {"path": path, "bytes": count,
                                   "sha256": digest.hexdigest()}
                    if path in RESERVED:
                        metadata[path] = b"".join(chunks)
                finally:
                    os.close(fd)
        require(stamp(before) == stamp(os.fstat(directory_fd)),
                f"directory changed while scanning: {prefix or '.'}")

    root_fd = open_root(root)
    try:
        visit(root_fd, "")
    finally:
        os.close(root_fd)
    ancestors = set()
    for path in files:
        parts = path.split("/")
        ancestors.update("/".join(parts[:i]) for i in range(1, len(parts)))
    require(directories == ancestors,
            f"empty/unrepresented directories rejected: {sorted(directories - ancestors)}")
    return files, metadata


def inventory(root):
    files, _ = scan(root)
    entries = [files[path] for path in sorted(files) if path not in RESERVED]
    return canonical({"schema": SCHEMA, "payload_count": len(entries),
                      "payload_bytes": sum(entry["bytes"] for entry in entries),
                      "files": entries})


def reject_duplicates(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def parse_ledger(raw, trusted_sha256):
    require(type(trusted_sha256) is str and HEX.fullmatch(trusted_sha256),
            "trusted ledger SHA-256 must be exactly 64 lowercase hex digits")
    require(sha256(raw) == trusted_sha256, "ledger differs from externally approved SHA-256")
    try:
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=reject_duplicates,
                           parse_constant=lambda value: (_ for _ in ()).throw(
                               InvalidRelease(f"nonfinite JSON value: {value}")))
    except (UnicodeError, json.JSONDecodeError, RecursionError) as exc:
        raise InvalidRelease(f"malformed ledger: {exc}") from exc
    require(type(value) is dict and set(value) ==
            {"schema", "payload_count", "payload_bytes", "files"}, "invalid ledger shape")
    require(value["schema"] == SCHEMA, "unsupported ledger schema")
    require(type(value["files"]) is list, "ledger files must be a list")
    for key in ("payload_count", "payload_bytes"):
        require(type(value[key]) is int and value[key] >= 0, f"invalid {key}")
    previous = None
    for entry in value["files"]:
        require(type(entry) is dict and set(entry) == {"path", "bytes", "sha256"},
                "invalid file entry shape")
        valid_path(entry["path"])
        require(entry["path"] not in RESERVED, "ledger cannot contain itself or manifest")
        require(previous is None or previous < entry["path"],
                "ledger paths must be strictly sorted and unique")
        previous = entry["path"]
        require(type(entry["bytes"]) is int and entry["bytes"] >= 0, "invalid byte length")
        require(type(entry["sha256"]) is str and HEX.fullmatch(entry["sha256"]),
                "invalid file SHA-256")
    require(value["payload_count"] == len(value["files"]), "payload count mismatch")
    require(value["payload_bytes"] == sum(e["bytes"] for e in value["files"]),
            "payload byte total mismatch")
    require(raw == canonical(value), "ledger is not canonical JSON")
    return value


def expected_manifest(ledger, trusted_sha256):
    hashes = {entry["path"]: entry["sha256"] for entry in ledger["files"]}
    hashes[LEDGER] = trusted_sha256
    return "".join(f"{hashes[path]}  {path}\n" for path in sorted(hashes)).encode("ascii")


def preflight(root, trusted_sha256, sealed=False):
    files, metadata = scan(root)
    require(LEDGER in metadata, f"missing {LEDGER}")
    ledger = parse_ledger(metadata[LEDGER], trusted_sha256)
    expected = {entry["path"]: entry for entry in ledger["files"]}
    actual = {path: entry for path, entry in files.items() if path not in RESERVED}
    require(set(actual) == set(expected),
            f"payload member mismatch; missing={sorted(set(expected) - set(actual))}; "
            f"unexpected={sorted(set(actual) - set(expected))}")
    for path in sorted(expected):
        require(actual[path] == expected[path], f"payload bytes/digest mismatch: {path}")
    manifest = expected_manifest(ledger, trusted_sha256)
    if sealed:
        require(MANIFEST in metadata, f"missing {MANIFEST}")
        require(metadata[MANIFEST] == manifest, "manifest is not the exact canonical inventory")
    else:
        require(MANIFEST not in files, "seal/check requires an absent manifest; never overwrites")
    return ledger, manifest


def publish_manifest(root, contents):
    """Only called after complete validation; never replaces an existing member."""
    root_fd = open_root(root)
    temporary = f".manifest-publish-{secrets.token_hex(16)}.tmp"
    created = False
    try:
        fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                     0o644, dir_fd=root_fd)
        created = True
        try:
            with os.fdopen(fd, "wb") as output:
                output.write(contents)
                output.flush()
                os.fsync(output.fileno())
            # Atomic no-replace publication. Unlink only our newly created temp.
            os.link(temporary, MANIFEST, src_dir_fd=root_fd, dst_dir_fd=root_fd,
                    follow_symlinks=False)
        finally:
            if created:
                os.unlink(temporary, dir_fd=root_fd)
                created = False
        os.fsync(root_fd)
    finally:
        os.close(root_fd)


def seal(root, trusted_sha256):
    # No files/temp files have been written before BOTH complete preflights pass.
    first = preflight(root, trusted_sha256, sealed=False)
    second = preflight(root, trusted_sha256, sealed=False)
    require(first == second, "release changed between preflight scans")
    publish_manifest(root, second[1])
    return second[0]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("inventory", "check", "seal", "verify"))
    parser.add_argument("root", type=Path)
    parser.add_argument("--ledger-sha256", help="independently approved ledger hash, not a live rehash")
    args = parser.parse_args(argv)
    try:
        if args.action == "inventory":
            require(args.ledger_sha256 is None, "inventory does not accept a trust pin")
            sys.stdout.buffer.write(inventory(args.root))
            return 0
        require(args.ledger_sha256 is not None, "this action requires --ledger-sha256")
        if args.action == "seal":
            ledger = seal(args.root, args.ledger_sha256)
        else:
            ledger, _ = preflight(args.root, args.ledger_sha256, sealed=args.action == "verify")
        print(f"PASS {args.action}: {ledger['payload_count']} payload files, "
              f"{ledger['payload_bytes']} payload bytes; ledger SHA-256 {args.ledger_sha256}")
        return 0
    except (InvalidRelease, OSError, ValueError) as exc:
        print(f"FAIL {args.action}: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
