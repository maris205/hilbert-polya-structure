#!/usr/bin/env python3
"""Read-only adapter for explicitly named directory-relative Git manifests.

Does not treat root-relative input pins as package manifests, does not
check mathematics, and does not claim an exact package path-set closure.
"""
import argparse
from hashlib import sha256
import json
from pathlib import PurePosixPath
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository")
    parser.add_argument("ref")
    parser.add_argument("manifests", nargs="+")
    args = parser.parse_args()
    def git(*cmd):
        return subprocess.check_output(["git", "-C", args.repository, *cmd])
    ref = git("rev-parse", args.ref).decode().strip()
    failures, checked = [], 0
    for manifest in args.manifests:
        location = PurePosixPath(manifest)
        if location.is_absolute() or ".." in location.parts:
            raise ValueError("manifest must be an explicit repository path")
        for line in git("show", f"{ref}:{manifest}").decode().splitlines():
            if not line.strip():
                continue
            wanted, rel = line.split(maxsplit=1)
            rel = PurePosixPath(rel.removeprefix("*"))
            if rel.is_absolute() or ".." in rel.parts:
                raise ValueError("only directory-relative package manifests are accepted")
            if len(wanted) != 64 or any(c not in "0123456789abcdef" for c in wanted):
                raise ValueError("invalid sha256 field")
            path = str(location.parent / rel)
            try:
                actual = sha256(git("show", f"{ref}:{path}")).hexdigest()
                checked += 1
                if actual != wanted:
                    failures.append({"path": path, "error": "sha256_mismatch"})
            except subprocess.CalledProcessError:
                failures.append({"path": path, "error": "missing_git_object"})
    print(json.dumps({"status": "PASS_GIT_OBJECT_PINS" if not failures else "FAIL",
                      "ref": ref, "manifests": args.manifests, "checked_entries": checked,
                      "failures": failures,
                      "scope": "Explicit directory-relative package manifests; not root-relative input pins, coverage policy or mathematics"},
                     indent=2, sort_keys=True))
    raise SystemExit(bool(failures))


if __name__ == "__main__":
    main()
