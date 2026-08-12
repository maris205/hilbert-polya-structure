#!/usr/bin/env python3
"""Read-only audit of every accepted release provenance in this paper."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    releases = sorted((ROOT / "results").glob("*/RELEASE_PROVENANCE.json"))
    reports: list[dict[str, object]] = []
    total_failures = 0
    for release_path in releases:
        payload = json.loads(release_path.read_text(encoding="utf-8"))
        authority_path = release_path.with_name("AUTHORITATIVE_STATUS.json")
        authority = (
            json.loads(authority_path.read_text(encoding="utf-8"))
            if authority_path.is_file()
            else {}
        )
        if authority.get("may_be_cited_as_proof") is False:
            reports.append(
                {
                    "release": str(release_path.relative_to(ROOT)),
                    "release_status": payload.get("release_status"),
                    "authority": authority.get("authoritative_status"),
                    "files_checked": 0,
                    "failures": [],
                    "note": "excluded from authoritative audit",
                }
            )
            continue
        failures: list[str] = []
        for key, expected in payload.get("files", {}).items():
            path = ROOT / key
            if not path.is_file():
                failures.append(f"missing: {key}")
            elif sha256(path) != expected:
                failures.append(f"hash mismatch: {key}")
        total_failures += len(failures)
        reports.append(
            {
                "release": str(release_path.relative_to(ROOT)),
                "release_status": payload.get("release_status"),
                "final_status": payload.get("final_status"),
                "files_checked": len(payload.get("files", {})),
                "failures": failures,
            }
        )
    output = {
        "audit_status": "PASS" if releases and total_failures == 0 else "FAIL",
        "release_count": len(releases),
        "total_failures": total_failures,
        "reports": reports,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if output["audit_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
