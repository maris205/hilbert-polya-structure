"""Generate and independently reproduce every Paper-5 publication figure."""

from __future__ import annotations

import argparse
import hashlib
import json
import tempfile
from pathlib import Path

from data_loader import load_figure_data
from gen_fig1_additive_capacity import generate as generate_fig1
from gen_fig2_proof_flow import generate as generate_fig2
from gen_fig3_source_audit_matrix import generate as generate_fig3
from paper_plot_style import DPI, SVG_HASH_SALT


FIGURE_DIR = Path(__file__).resolve().parent
GENERATORS = (generate_fig1, generate_fig2, generate_fig3)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _generate(directory: Path) -> dict[str, Path]:
    outputs: dict[str, Path] = {}
    for generator in GENERATORS:
        for path in generator(directory).values():
            outputs[path.name] = path
    return dict(sorted(outputs.items()))


def generate_all(*, verify: bool = True) -> dict[str, str]:
    """Generate masters; optionally regenerate in isolation and compare bytes."""

    data = load_figure_data()
    primary = _generate(FIGURE_DIR)
    primary_hashes = {name: _sha256(path) for name, path in primary.items()}
    second_hashes: dict[str, str] | None = None
    if verify:
        with tempfile.TemporaryDirectory(prefix="paper5-figure-reproduction-") as raw:
            second = _generate(Path(raw))
            second_hashes = {name: _sha256(path) for name, path in second.items()}
        if primary_hashes != second_hashes:
            differences = sorted(
                name
                for name in set(primary_hashes).union(second_hashes)
                if primary_hashes.get(name) != second_hashes.get(name)
            )
            raise RuntimeError(f"figure reproduction mismatch: {differences}")

    report = {
        "schema": "PAPER5_FIGURE_REPRODUCIBILITY_V1",
        "candidate_id": data.candidate_id,
        "source_lock_sha256": data.source_lock_sha256,
        "reviewed_code_sha256": data.reviewed_code_sha256,
        "classification": data.classification,
        "registered_at_utc": data.registered_at_utc,
        "input_hashes": data.input_hashes,
        "style": {
            "dpi": DPI,
            "svg_hash_salt": SVG_HASH_SALT,
            "pdf_svg_vector_masters": True,
            "png_review_copy": True,
            "fixed_metadata_date": "2026-08-14",
        },
        "outputs": primary_hashes,
        "second_generation_hashes": second_hashes,
        "double_generation_match": second_hashes == primary_hashes if verify else None,
    }
    report_path = FIGURE_DIR / "figure_reproducibility.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return primary_hashes


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--no-verify",
        action="store_true",
        help="generate once without the isolated byte-for-byte reproduction check",
    )
    arguments = parser.parse_args()
    hashes = generate_all(verify=not arguments.no_verify)
    print(json.dumps(hashes, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
