#!/usr/bin/env python3
"""Build and replay-check strict ARS Phase-E evidence rows for this package."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from urllib.parse import quote


def strict_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_builder(path: Path):
    spec = importlib.util.spec_from_file_location("ars_evidence_rows", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load ARS builder: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ars-builder", type=Path, required=True)
    parser.add_argument("--registry", type=Path, default=Path("claim_registry_round1.json"))
    parser.add_argument("--passages", type=Path, default=Path("evidence_source_passages_strict.json"))
    parser.add_argument("--rows", type=Path, default=Path("evidence_rows_round1.json"))
    parser.add_argument("--source-map", type=Path, default=Path("evidence_source_map_round1.json"))
    parser.add_argument("--manifest", type=Path, default=Path("evidence_source_manifest_round1.json"))
    parser.add_argument("--paper-id", default="P70")
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()

    ev = load_builder(args.ars_builder)
    registry = strict_json(args.registry)
    passage_doc = strict_json(args.passages)
    sources = passage_doc["sources"]
    selected = [c for c in registry["claims"] if c["selection_tier"] != "NOT-SELECTED"]
    required_slugs = []
    for claim in selected:
        for slug in claim["ref_slugs"]:
            if slug not in required_slugs:
                required_slugs.append(slug)
    if set(required_slugs) != set(sources):
        raise RuntimeError(
            f"source passage keys differ from selected registry slugs: required={required_slugs}, supplied={list(sources)}"
        )

    source_map = {slug: sources[slug]["source_text"] for slug in required_slugs}
    cached = {}
    if args.rows.exists():
        try:
            cached = {row["row_id"]: row for row in strict_json(args.rows)}
        except (OSError, ValueError, TypeError):
            cached = {}

    rows = []
    expected_tuples = []
    sequence = 0
    for claim in selected:
        refs = claim["ref_slugs"] or [None]
        for slug in refs:
            sequence += 1
            row_id = f"EVR-{args.paper_id}-STRICT-{sequence:04d}"
            if slug is None:
                anchor_kind = "none"
                anchor_value = ""
                display_label = None
                source_text = None
                detail = (
                    "Registry has no ref_slug for this selected paper-internal theorem/control claim; "
                    "this explicit anchorless row carries no external-source excerpt."
                )
            else:
                anchor_kind = "quote"
                anchor_value = sources[slug]["source_text"]
                display_label = sources[slug]["display_label"]
                source_text = source_map[slug]
                detail = (
                    f"Bounded primary/publisher source passage for {slug}; excerpt provenance is "
                    "separate from the unchanged Phase-E claim verdict."
                )
            locator = (
                f"{claim['paper_section']}; draft UTF-8 bytes "
                f"{claim['draft_span']['start_byte']}-{claim['draft_span']['end_byte']}"
            )
            template = {
                "schema_version": "evidence-row/1.0",
                "surface": "phase_e_claim_verification",
                "row_id": row_id,
                "claim": {
                    "claim_id": claim["claim_id"],
                    "text": claim["claim_text"],
                    "paper_locator": locator,
                    "selection_tier": claim["selection_tier"],
                },
                "source": {
                    "ref_slug": slug,
                    "display_label": display_label,
                    "source_artifact_sha256": None,
                },
                "anchor": {
                    "kind": anchor_kind,
                    "value_encoded": quote(anchor_value, safe=""),
                },
                "verdict": "VERIFIED",
                "detail": detail,
                "content_handling": {
                    "sharing_scope": "session_only",
                    "rights_basis": "not_assessed",
                },
            }
            row = ev.build(
                template,
                source_text,
                cached_row=cached.get(row_id),
            )
            rows.append(row)
            expected_tuples.append((claim["claim_id"], slug, anchor_kind, anchor_value))

    actual_tuples = [
        (
            row["claim"]["claim_id"],
            row["source"]["ref_slug"],
            row["anchor"]["kind"],
            row["anchor"]["value_decoded"],
        )
        for row in rows
    ]
    if actual_tuples != expected_tuples:
        raise RuntimeError("ordered evidence tuple expansion differs from the selected registry")
    ev.paginate(rows)
    for row in rows:
        ev.validate(row, source_map.get(row["source"]["ref_slug"]))

    manifest = {
        "schema_version": "ars-session-source-manifest/1.0",
        "ars_builder": str(args.ars_builder),
        "ars_builder_sha256": hashlib.sha256(args.ars_builder.read_bytes()).hexdigest(),
        "registry_path": str(args.registry),
        "registry_sha256": hashlib.sha256(args.registry.read_bytes()).hexdigest(),
        "passage_manifest_path": str(args.passages),
        "passage_manifest_sha256": hashlib.sha256(args.passages.read_bytes()).hexdigest(),
        "tuple_order": "selected registry claim order; exact ref_slugs array order; one anchorless tuple when ref_slugs is empty",
        "sources": [
            {
                "ref_slug": slug,
                "display_label": sources[slug]["display_label"],
                "direct_url": sources[slug]["direct_url"],
                "source_kind": sources[slug]["source_kind"],
                "source_content_sha256": sha256_text(source_map[slug]),
                "source_content_utf8_bytes": len(source_map[slug].encode("utf-8")),
                "source_word_count": len(source_map[slug].split()),
                "content_scope": "exact bounded passage held in this closure session",
                "human_read_attestation": False,
            }
            for slug in required_slugs
        ],
    }

    if not args.check_only:
        args.rows.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        args.source_map.write_text(json.dumps(source_map, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        args.manifest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    cited_rows = sum(row["source"]["ref_slug"] is not None for row in rows)
    anchorless_rows = len(rows) - cited_rows
    print(
        f"PASS: claims={len(selected)} tuples={len(rows)} cited={cited_rows} "
        f"anchorless={anchorless_rows} sources={len(source_map)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
