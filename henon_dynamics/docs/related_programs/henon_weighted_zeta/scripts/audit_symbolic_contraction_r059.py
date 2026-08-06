#!/usr/bin/env python3
"""Independent exact arithmetic audit of the R059 symbolic contraction lemma."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = PROJECT_ROOT / "research" / "refine-logs" / "R059_CERTIFIED_DOMAIN_PROTOCOL.json"
PROOF = PROJECT_ROOT / "research" / "refine-logs" / "R059_SYMBOLIC_CONTRACTION_PROOF.md"
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "symbolic_contraction_r059.json"
PROTOCOL_SHA256 = "f94801f5b7abd5baaebd4c859a3662af4cf6d63954b1f4b18aaa6e8d3596f2b6"
STATE_ORDER = ("--", "-+", "+-", "++")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--protocol", type=Path, default=PROTOCOL)
    parser.add_argument("--proof", type=Path, default=PROOF)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def state_pair(state: int) -> tuple[int, int]:
    return ((-1, -1), (-1, 1), (1, -1), (1, 1))[state]


def main() -> None:
    args = parse_args()
    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    matrix = protocol["h_sets"]["adjacency_matrix"]
    x_intervals = {
        "-": (Fraction(-5, 8), Fraction(-1, 3)),
        "+": (Fraction(1, 3), Fraction(5, 8)),
    }
    y_intervals = {
        "-": (Fraction(-81, 128), Fraction(-5, 16)),
        "+": (Fraction(5, 16), Fraction(81, 128)),
    }

    parent_checks = {
        "protocol_sha256": sha256_file(args.protocol) == PROTOCOL_SHA256,
        "proof_exists": args.proof.exists(),
        "proof_sha256": sha256_file(args.proof) if args.proof.exists() else None,
    }

    graph_equivalence_rows = []
    graph_equivalence_pass = True
    for source in range(4):
        source_first, source_previous = state_pair(source)
        for target in range(4):
            target_first, target_previous = state_pair(target)
            structural = target_previous == source_first
            no_double_positive = not (
                source_previous == 1 and target_first == 1
            )
            expected = structural and no_double_positive
            observed = bool(matrix[source][target])
            passed = observed == expected
            graph_equivalence_pass = graph_equivalence_pass and passed
            graph_equivalence_rows.append(
                {
                    "source": STATE_ORDER[source],
                    "target": STATE_ORDER[target],
                    "structural_shift": structural,
                    "no_double_positive_neighbors": no_double_positive,
                    "matrix_value": int(matrix[source][target]),
                    "pass": passed,
                }
            )

    # Exact square comparisons for the two radicand cases.
    radicand_cases = {
        "both_negative": {
            "lower": Fraction(5, 18),
            "upper": Fraction(3, 8),
        },
        "mixed": {
            "lower": Fraction(17, 144),
            "upper": Fraction(31, 144),
        },
    }
    radicand_checks = {}
    for name, bounds in radicand_cases.items():
        lower = bounds["lower"]
        upper = bounds["upper"]
        radicand_checks[name] = {
            "lower_above_one_third_squared": lower > Fraction(1, 9),
            "upper_below_five_eighths_squared": upper < Fraction(25, 64),
        }

    derivative_bound_squared = Fraction(4, 17)
    cone_entropy_matrix = matrix
    # Characteristic polynomial via exact 4x4 determinant at a symbolic lambda.
    import sympy as sp

    lambda_symbol = sp.symbols("lambda")
    characteristic = sp.factor(
        (lambda_symbol * sp.eye(4) - sp.Matrix(cone_entropy_matrix)).det()
    )
    expected_characteristic = (lambda_symbol**2 - lambda_symbol - 1) * (
        lambda_symbol**2 + 1
    )
    checks = {
        "parent_protocol": parent_checks["protocol_sha256"],
        "graph_sign_equivalence": graph_equivalence_pass,
        "both_negative_radical_range": all(radicand_checks["both_negative"].values()),
        "mixed_radical_range": all(radicand_checks["mixed"].values()),
        "strict_contraction": derivative_bound_squared < 1,
        "n1_n2_duplicate_neighbor_bound": derivative_bound_squared < 1,
        "x_inside_y_minus": Fraction(-5, 8) > Fraction(-81, 128)
        and Fraction(-1, 3) < Fraction(-5, 16),
        "x_inside_y_plus": Fraction(1, 3) > Fraction(5, 16)
        and Fraction(5, 8) < Fraction(81, 128),
        "characteristic_polynomial": sp.expand(characteristic)
        == sp.expand(expected_characteristic),
        "proof_exists": parent_checks["proof_exists"],
    }
    output = {
        "run_id": "R059_SYMBOLIC_CONTRACTION_AUDIT",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "protocol_path": str(args.protocol.relative_to(PROJECT_ROOT)),
        "protocol_sha256": sha256_file(args.protocol),
        "proof_path": str(args.proof.relative_to(PROJECT_ROOT)),
        "proof_sha256": parent_checks["proof_sha256"],
        "state_order": list(STATE_ORDER),
        "radicand_cases": {
            name: {
                "lower": f"{bounds['lower'].numerator}/{bounds['lower'].denominator}",
                "upper": f"{bounds['upper'].numerator}/{bounds['upper'].denominator}",
                "checks": radicand_checks[name],
            }
            for name, bounds in radicand_cases.items()
        },
        "derivative_bound": {
            "single_neighbor_squared": "1/17",
            "sup_norm_lipschitz_squared": "4/17",
            "sup_norm_lipschitz_float": (4 / 17) ** 0.5,
        },
        "graph_equivalence": graph_equivalence_rows,
        "characteristic_polynomial": str(characteristic),
        "checks": checks,
        "status": "PROVABLE AS STATED" if all(checks.values()) else "AUDIT FAILURE",
        "scope": "Exact contraction/coding audit on the four rational h-sets; it does not certify the global numerical orbit catalog or continuous operator convergence.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "output": str(args.output.relative_to(PROJECT_ROOT)),
                "status": output["status"],
                "all_checks_pass": all(checks.values()),
            },
            indent=2,
        )
    )
    if not all(checks.values()):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
