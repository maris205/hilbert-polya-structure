#!/usr/bin/env python3
"""Read-only check of package SHA256SUMS against committed Git object bytes.

This checks archival presence/integrity only, not mathematical acceptance,
manifest coverage policy, root-relative review input pins or paper completion.
"""
import argparse
import hashlib
import json
from pathlib import PurePosixPath
import subprocess


def git(repo, *args):
    return subprocess.check_output(["git", "-C", repo, *args])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("repository")
    parser.add_argument("ref")
    parser.add_argument("paths", nargs="+")
    args = parser.parse_args()
    ref = git(args.repository, "rev-parse", args.ref).decode().strip()
    paths = git(args.repository, "ls-tree", "-r", "--name-only", ref,
                "--", *args.paths).decode().splitlines()
    manifests = [p for p in paths if PurePosixPath(p).name == "SHA256SUMS"]
    checked = 0
    failures = []
    for manifest in manifests:
        body = git(args.repository, "show", f"{ref}:{manifest}").decode()
        for line in body.splitlines():
            if not line.strip():
                continue
            digest, relative = line.split(maxsplit=1)
            relative = relative.removeprefix("*")
            path = str(PurePosixPath(manifest).parent / relative)
            if len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
                raise ValueError(f"Invalid digest in {manifest}: {line}")
            try:
                actual = hashlib.sha256(git(args.repository, "show", f"{ref}:{path}")).hexdigest()
            except subprocess.CalledProcessError:
                failures.append({"manifest": manifest, "path": path, "error": "missing_git_object"})
                continue
            checked += 1
            if actual != digest:
                failures.append({"manifest": manifest, "path": path, "error": "sha256_mismatch"})
    print(json.dumps({"status": "PASS_GIT_OBJECT_PINS" if not failures else "FAIL",
                      "ref": ref, "manifests": len(manifests),
                      "checked_entries": checked, "failures": failures},
                     indent=2, sort_keys=True))
    raise SystemExit(bool(failures))


if __name__ == "__main__":
    main()
