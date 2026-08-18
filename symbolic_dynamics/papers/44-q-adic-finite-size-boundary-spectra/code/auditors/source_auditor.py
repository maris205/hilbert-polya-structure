#!/usr/bin/env python3
"""Independent frozen-source, ownership, and correction-boundary auditor."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


LITERATURE_SHA256 = "1de200d9757fab8107bc5d11791c7a903034e97307d27f060a1b6b07b04130f0"
SOURCE_LOCK_SHA256 = "a49bbc392e21a25e7f36ab8c0c5426bbec510aa30bc6d2d6943b0e81c5347984"
CORRECTION_EXCERPT_SHA256 = "b7c4aaf6c75e5a1790fc17f311242a8c56d6d23fd153657baed7dd93421c022f"


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def get(root: Path, name: str) -> Path:
    if not root.is_absolute() or not root.is_dir() or root.is_symlink():
        raise ValueError("unsafe root")
    base = root / "preauthority"
    path = base / name
    if base.is_symlink() or path.is_symlink():
        raise ValueError("symlink")
    resolved = path.resolve(strict=True)
    if resolved != root.resolve(strict=True) / "preauthority" / name:
        raise ValueError("containment")
    return resolved


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root")
    parser.add_argument("--mutation")
    arguments = parser.parse_args()
    if arguments.mutation:
        if arguments.mutation != "MUT-OWNER/leading_results_new":
            raise ValueError("not designated")
        sys.stdout.buffer.write(canonical({
            "payload": {
                "code": "PRIOR_OWNERSHIP_TRANSFER",
                "consumer": "L",
                "instance_id": arguments.mutation,
                "witness": "chain product, entropy, and leading dimensions are zero-credit primary-owned components",
            },
            "schema": "paper44-mutation-rejection-v1",
            "status": "REJECT",
        }))
        return 2
    if not arguments.root:
        raise ValueError("root required")
    root = Path(arguments.root)
    literature = get(root, "LITERATURE_NOVELTY_AUDIT.md").read_bytes()
    source_lock = get(root, "SOURCE_LOCK.md").read_bytes()
    if hashlib.sha256(literature).hexdigest() != LITERATURE_SHA256 \
            or hashlib.sha256(source_lock).hexdigest() != SOURCE_LOCK_SHA256:
        raise ValueError("source bytes drift")
    start = b"The journal metadata were verified at DOI 10.1063/5.0118652."
    end = b"after all of Ban--Hu--Lai's valid leading/boundary ownership is subtracted."
    first = literature.index(start)
    last = literature.index(end, first) + len(end)
    excerpt = literature[first:last]
    if hashlib.sha256(excerpt).hexdigest() != CORRECTION_EXCERPT_SHA256:
        raise ValueError("Ban--Hu--Lai correction boundary changed")
    text = excerpt.decode("utf-8")
    required = [
        "checked only in the author manuscript arXiv:2210.09115v1",
        "cannot hold under the stated quantifiers",
        "same-object statement\nrequiring correction, not as novelty ownership and not as an exact duplicate",
        "version-of-record theorem text and any publisher erratum or correction\nnotice have not been checked line by line",
    ]
    if any(token not in text for token in required):
        raise ValueError("correction semantics changed")
    lock_text = source_lock.decode("utf-8")
    for token in ["Ban--Hu--Lin's direct admissible-chain pattern-count framework",
                  "Zero novelty credit is assigned to:",
                  "writing to authority, Git, mirrors, registries, or repository manifests"]:
        if token not in lock_text:
            raise ValueError("source ownership boundary")
    sys.stdout.buffer.write(canonical({
        "payload": {
            "ban_hu_lai_author_manuscript_correction_excerpt_sha256": CORRECTION_EXCERPT_SHA256,
            "ban_hu_lai_version_of_record_line_checked": False,
            "leading_results_novelty_credit": 0,
            "literature_sha256": LITERATURE_SHA256,
            "same_object_statement_disposition": "CORRECTION_NOT_NOVELTY_NOT_EXACT_DUPLICATE",
            "source_lock_sha256": SOURCE_LOCK_SHA256,
            "stop_duplicate_owner": "external_literature_and_publication_review",
        },
        "schema": "paper44-source-audit-v1",
        "status": "PASS",
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
