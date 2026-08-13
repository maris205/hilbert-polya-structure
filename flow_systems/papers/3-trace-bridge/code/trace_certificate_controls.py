#!/usr/bin/env python3
"""Deterministic controls for the Stage-3 same-object trace certificate.

The controls use only Python's standard library.  They consume no Riemann-zero
data, perform no parameter fit, and make no claim to prove a trace formula.
The universal mathematical statements are proved in notes/proof_audit.md.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Mapping


PAPER_DIR = Path(__file__).resolve().parents[1]
RESEARCH_DATE = "2026-08-13"

REQUIRED_CERTIFICATE_FIELDS = (
    "classical_phase_object",
    "flow",
    "clock",
    "primitive_and_repetition_ledger",
    "analytic_object",
    "hilbert_or_cohomology_space",
    "operator_or_action",
    "domain_or_topology",
    "trace_or_regularization",
    "test_function_class",
    "spectral_or_resonance_ledger",
    "global_identity_or_local_statement",
    "orbit_coefficients",
    "non_orbit_terms",
    "error_or_distributional_convergence",
    "normalization",
    "arithmetic_map",
)


@dataclass(frozen=True)
class QuadraticElement:
    """An exact element a + b*sqrt(D), with rational a and b."""

    a: Fraction
    b: Fraction
    discriminant: int

    def __post_init__(self) -> None:
        if self.discriminant <= 0:
            raise ValueError("the discriminant must be positive")

    def __mul__(self, other: "QuadraticElement") -> "QuadraticElement":
        if self.discriminant != other.discriminant:
            raise ValueError("quadratic elements must have the same discriminant")
        d = self.discriminant
        return QuadraticElement(
            self.a * other.a + self.b * other.b * d,
            self.a * other.b + self.b * other.a,
            d,
        )

    def __pow__(self, exponent: int) -> "QuadraticElement":
        if exponent < 0:
            return self.inverse() ** (-exponent)
        result = QuadraticElement(Fraction(1), Fraction(0), self.discriminant)
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power >>= 1
        return result

    def conjugate(self) -> "QuadraticElement":
        return QuadraticElement(self.a, -self.b, self.discriminant)

    def norm(self) -> Fraction:
        return self.a * self.a - self.b * self.b * self.discriminant

    def inverse(self) -> "QuadraticElement":
        norm = self.norm()
        if norm == 0:
            raise ZeroDivisionError("zero quadratic element")
        return QuadraticElement(
            self.a / norm,
            -self.b / norm,
            self.discriminant,
        )

    def is_rational(self) -> bool:
        return self.b == 0

    def decimal_residuals(self, precision: int = 100) -> tuple[Decimal, Decimal]:
        """Return direct decimal norm and conjugate-versus-inverse residuals."""

        with localcontext() as context:
            context.prec = precision
            root = Decimal(self.discriminant).sqrt()
            a = Decimal(self.a.numerator) / Decimal(self.a.denominator)
            b = Decimal(self.b.numerator) / Decimal(self.b.denominator)
            value = a + b * root
            conjugate = a - b * root
            norm_residual = abs(value * conjugate - Decimal(1))
            galois_inverse_residual = abs(conjugate - Decimal(1) / value)
        return norm_residual, galois_inverse_residual


def is_square(integer: int) -> bool:
    if integer < 0:
        return False
    root = math.isqrt(integer)
    return root * root == integer


def hyperbolic_norm(trace_abs: int) -> QuadraticElement:
    """Return N_gamma=lambda^2 from an absolute integral hyperbolic trace."""

    if trace_abs <= 2:
        raise ValueError("a hyperbolic PSL(2,Z) trace must have absolute value > 2")
    discriminant = trace_abs * trace_abs - 4
    if is_square(discriminant):
        raise AssertionError("m^2-4 must be nonsquare for integral m>2")
    return QuadraticElement(
        Fraction(trace_abs * trace_abs - 2, 2),
        Fraction(trace_abs, 2),
        discriminant,
    )


def enumerate_hyperbolic_norms(
    trace_min: int = 3,
    trace_max: int = 20,
    repetition_max: int = 6,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Enumerate exact finite controls for the quadratic norm theorem."""

    if trace_min <= 2 or trace_max < trace_min or repetition_max < 1:
        raise ValueError("invalid enumeration bounds")

    rows: list[dict[str, Any]] = []
    max_norm_residual = Decimal(0)
    max_galois_residual = Decimal(0)

    for trace_abs in range(trace_min, trace_max + 1):
        base = hyperbolic_norm(trace_abs)
        if base.norm() != 1:
            raise AssertionError("base algebraic norm is not one")
        for repetition in range(1, repetition_max + 1):
            powered = base**repetition
            exact_norm = powered.norm()
            galois_equals_inverse = powered.conjugate() == powered.inverse()
            if exact_norm != 1:
                raise AssertionError("algebraic norm failed under repetition")
            if powered.is_rational():
                raise AssertionError("positive power unexpectedly became rational")
            if not galois_equals_inverse:
                raise AssertionError("Galois conjugate did not equal the inverse")

            norm_residual, galois_residual = powered.decimal_residuals()
            max_norm_residual = max(max_norm_residual, norm_residual)
            max_galois_residual = max(max_galois_residual, galois_residual)
            rows.append(
                {
                    "trace_abs": trace_abs,
                    "repetition": repetition,
                    "discriminant": powered.discriminant,
                    "rational_coefficient_a": str(powered.a),
                    "irrational_coefficient_b": str(powered.b),
                    "exact_field_norm": str(exact_norm),
                    "galois_equals_inverse_exact": galois_equals_inverse,
                    "irrational_coefficient_nonzero": not powered.is_rational(),
                    "decimal_norm_residual": f"{norm_residual:.8E}",
                    "decimal_galois_inverse_residual": f"{galois_residual:.8E}",
                }
            )

    summary = {
        "trace_range_inclusive": [trace_min, trace_max],
        "repetition_range_inclusive": [1, repetition_max],
        "rows": len(rows),
        "all_discriminants_nonsquare": all(
            not is_square(int(row["discriminant"])) for row in rows
        ),
        "all_exact_field_norms_one": all(
            row["exact_field_norm"] == "1" for row in rows
        ),
        "all_galois_conjugates_equal_inverse": all(
            bool(row["galois_equals_inverse_exact"]) for row in rows
        ),
        "all_tested_positive_powers_irrational": all(
            bool(row["irrational_coefficient_nonzero"]) for row in rows
        ),
        "maximum_decimal_norm_residual": f"{max_norm_residual:.8E}",
        "maximum_decimal_galois_inverse_residual": f"{max_galois_residual:.8E}",
        "interpretation": (
            "finite exact/decimal control only; the all-trace, all-repetition "
            "statement is Theorem B1 in notes/proof_audit.md"
        ),
    }
    return rows, summary


def compact_bump(x: float, center: float, half_width: float) -> float:
    """A C-infinity bump supported on [center-half_width, center+half_width]."""

    scaled = (x - center) / half_width
    if abs(scaled) >= 1.0:
        return 0.0
    return math.exp(1.0 - 1.0 / (1.0 - scaled * scaled))


def sampled_germ_control() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Illustrate exact sampled equality near a period and global inequality."""

    period = 1.0
    audited_radius = 0.2
    bump_center = 2.5
    bump_half_width = 0.4
    bump_amplitude = 0.75
    regularization = 0.03
    x_start = -1.0
    x_step = 0.01
    sample_count = 501

    audited_interval = (period - audited_radius, period + audited_radius)
    bump_support = (bump_center - bump_half_width, bump_center + bump_half_width)
    support_disjoint = (
        bump_support[1] < audited_interval[0]
        or bump_support[0] > audited_interval[1]
    )
    if not support_disjoint:
        raise AssertionError("bump support overlaps the audited neighborhood")

    rows: list[dict[str, Any]] = []
    local_differences: list[float] = []
    global_differences: list[float] = []
    period_index = round((period - x_start) / x_step)
    audited_steps = round(audited_radius / x_step)
    for index in range(sample_count):
        x = x_start + index * x_step
        # This is only a regularized plotting proxy for a singular trace germ.
        baseline = 1.0 / math.sqrt((x - period) ** 2 + regularization**2)
        bump = bump_amplitude * compact_bump(x, bump_center, bump_half_width)
        shifted = baseline + bump
        difference = shifted - baseline
        audited = abs(index - period_index) <= audited_steps
        if audited:
            local_differences.append(abs(difference))
        global_differences.append(abs(difference))
        rows.append(
            {
                "x": f"{x:.17g}",
                "baseline_proxy": f"{baseline:.17g}",
                "smooth_bump": f"{bump:.17g}",
                "shifted_proxy": f"{shifted:.17g}",
                "absolute_difference": f"{abs(difference):.17g}",
                "inside_audited_neighborhood": audited,
            }
        )

    local_max = max(local_differences)
    global_max = max(global_differences)
    if local_max != 0.0:
        raise AssertionError("sampled germ changed inside the audited neighborhood")
    if global_max <= 0.0:
        raise AssertionError("smooth shift did not change the global sample")

    summary = {
        "period": period,
        "audited_interval_closed": list(audited_interval),
        "bump_support_closed": list(bump_support),
        "support_disjoint": support_disjoint,
        "sample_count": sample_count,
        "audited_sample_count": len(local_differences),
        "maximum_local_absolute_difference": local_max,
        "maximum_global_absolute_difference": global_max,
        "interpretation": (
            "sampled illustration of Proposition A1; the distributional "
            "statement is proved analytically and is not inferred from this grid"
        ),
    }
    return rows, summary


@dataclass(frozen=True, order=True)
class Provenance:
    candidate_id: str
    source_lock: str

    def label(self) -> str:
        return f"{self.candidate_id}@{self.source_lock}"


@dataclass(frozen=True)
class FieldDatum:
    provenance: Provenance
    value: str
    evidence_state: str


@dataclass(frozen=True)
class TraceCertificate:
    declared_provenance: Provenance
    fields: Mapping[str, FieldDatum | None]

    def validate_t0(self) -> dict[str, Any]:
        unknown_fields = sorted(set(self.fields) - set(REQUIRED_CERTIFICATE_FIELDS))
        populated = {
            field: datum
            for field, datum in self.fields.items()
            if datum is not None
        }
        observed = sorted({datum.provenance for datum in populated.values()})
        mismatched = sorted(
            field
            for field, datum in populated.items()
            if datum.provenance != self.declared_provenance
        )
        missing = sorted(
            field
            for field in REQUIRED_CERTIFICATE_FIELDS
            if self.fields.get(field) is None
        )
        passes = not unknown_fields and not mismatched
        return {
            "declared_provenance": self.declared_provenance.label(),
            "observed_provenances": [item.label() for item in observed],
            "populated_field_count": len(populated),
            "missing_fields": missing,
            "unknown_fields": unknown_fields,
            "mismatched_fields": mismatched,
            "t0_passes": passes,
            "all_required_fields_populated": not missing and not unknown_fields,
            "interpretation": (
                "T0 checks provenance identity only; it does not certify "
                "completeness or gates T1--T7"
            ),
        }


def datum(
    provenance: Provenance,
    value: str,
    evidence_state: str = "PROVED",
) -> FieldDatum:
    return FieldDatum(provenance, value, evidence_state)


def candidate_certificates() -> tuple[TraceCertificate, TraceCertificate]:
    den = Provenance("DEN-WITT-Z-FIN", "deninger-v4-E_f-clock-t")
    mod = Provenance("MOD-GEO", "psl2z-unit-speed-cofinite")

    den_fields: dict[str, FieldDatum | None] = {
        field: None for field in REQUIRED_CERTIFICATE_FIELDS
    }
    den_fields.update(
        {
            "classical_phase_object": datum(den, "rational-Witt topological R-flow"),
            "flow": datum(den, "phi^t[P,u]=[P,exp(t)u]"),
            "clock": datum(den, "additive t; packet period log(p)"),
            "primitive_and_repetition_ledger": datum(
                den, "uncountable packet Gamma_p; repetitions k*log(p)"
            ),
            "arithmetic_map": datum(
                den,
                "closed point (p) gives packet support log(p); trace weight absent",
                "NOT_TESTABLE",
            ),
        }
    )

    mod_fields: dict[str, FieldDatum | None] = {
        "classical_phase_object": datum(mod, "unit tangent bundle of modular quotient"),
        "flow": datum(mod, "unit-speed geodesic flow"),
        "clock": datum(mod, "hyperbolic arc length"),
        "primitive_and_repetition_ledger": datum(
            mod, "primitive hyperbolic classes and repeated lengths"
        ),
        "analytic_object": datum(mod, "automorphic Laplace spectral decomposition"),
        "hilbert_or_cohomology_space": datum(mod, "L2 modular quotient"),
        "operator_or_action": datum(mod, "self-adjoint Laplace-Beltrami realization"),
        "domain_or_topology": datum(mod, "standard automorphic spectral domain"),
        "trace_or_regularization": datum(mod, "cofinite Selberg regularized trace"),
        "test_function_class": datum(
            mod,
            "exact convention awaits acquired full-source transcription",
            "OPEN",
        ),
        "spectral_or_resonance_ledger": datum(
            mod, "discrete plus continuous/scattering spectral data"
        ),
        "global_identity_or_local_statement": datum(
            mod, "exact complete tested cofinite identity"
        ),
        "orbit_coefficients": datum(mod, "same-quotient hyperbolic coefficients"),
        "non_orbit_terms": datum(
            mod, "identity, elliptic, parabolic/cusp, continuous/scattering"
        ),
        "error_or_distributional_convergence": datum(
            mod, "defined by the frozen test/regularization convention"
        ),
        "normalization": datum(
            mod, "unit-speed clock; exact Fourier convention pending transcription", "OPEN"
        ),
        "arithmetic_map": datum(
            mod, "rational-prime repeated support is disjoint", "REFUTED"
        ),
    }
    return TraceCertificate(den, den_fields), TraceCertificate(mod, mod_fields)


def coordinatewise_splice(
    left: TraceCertificate,
    right: TraceCertificate,
    fields_from_left: Iterable[str],
    declared_provenance: Provenance,
) -> TraceCertificate:
    """Select fields without erasing their original provenance."""

    left_fields = set(fields_from_left)
    unknown = left_fields - set(REQUIRED_CERTIFICATE_FIELDS)
    if unknown:
        raise ValueError(f"unknown fields in splice: {sorted(unknown)}")
    fields: dict[str, FieldDatum | None] = {}
    for field in REQUIRED_CERTIFICATE_FIELDS:
        source = left if field in left_fields else right
        fields[field] = source.fields.get(field)
    return TraceCertificate(declared_provenance, fields)


def certificate_t0_control() -> dict[str, Any]:
    den, mod = candidate_certificates()
    den_owned_fields = {
        "classical_phase_object",
        "flow",
        "clock",
        "primitive_and_repetition_ledger",
        "arithmetic_map",
    }
    hybrid = coordinatewise_splice(
        den,
        mod,
        fields_from_left=den_owned_fields,
        declared_provenance=den.declared_provenance,
    )

    alternate_lock = Provenance("MOD-GEO", "psl2z-posthoc-rescaled-clock")
    lock_mixed_fields = dict(mod.fields)
    lock_mixed_fields["clock"] = datum(alternate_lock, "post-hoc rescaled clock")
    lock_mixed = TraceCertificate(mod.declared_provenance, lock_mixed_fields)

    den_audit = den.validate_t0()
    mod_audit = mod.validate_t0()
    hybrid_audit = hybrid.validate_t0()
    lock_mixed_audit = lock_mixed.validate_t0()
    if not den_audit["t0_passes"] or not mod_audit["t0_passes"]:
        raise AssertionError("a same-source record failed T0")
    if hybrid_audit["t0_passes"]:
        raise AssertionError("a coordinatewise splice passed T0")
    if lock_mixed_audit["t0_passes"]:
        raise AssertionError("a source-lock mismatch passed T0")

    return {
        "den_same_source_record": den_audit,
        "mod_same_source_record": mod_audit,
        "coordinatewise_den_mod_splice": hybrid_audit,
        "same_candidate_different_clock_lock": lock_mixed_audit,
        "bridge_morphism_supplied": False,
        "route_b_invocation_allowed": False,
        "interpretation": (
            "same-source provenance can pass T0 even when fields are missing; "
            "borrowing populated coordinates from another source fails T0"
        ),
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        raise ValueError("cannot write an empty CSV")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def display_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(PAPER_DIR).as_posix()
    except ValueError:
        return resolved.as_posix()


def write_manifest(manifest_path: Path, artifacts: Iterable[Path]) -> None:
    entries = sorted((display_path(path), sha256(path)) for path in artifacts)
    manifest_path.write_text(
        "".join(f"{digest}  {name}\n" for name, digest in entries),
        encoding="utf-8",
    )


def verify_manifest(manifest_path: Path) -> dict[str, Any]:
    failures: list[str] = []
    checked = 0
    for line_number, raw_line in enumerate(
        manifest_path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not raw_line.strip():
            continue
        try:
            expected, name = raw_line.split("  ", 1)
        except ValueError:
            failures.append(f"line {line_number}: malformed")
            continue
        path = Path(name)
        if not path.is_absolute():
            path = PAPER_DIR / path
        if not path.is_file():
            failures.append(f"{name}: missing")
            continue
        checked += 1
        observed = sha256(path)
        if observed != expected:
            failures.append(f"{name}: expected {expected}, observed {observed}")
    return {
        "manifest": display_path(manifest_path),
        "files_checked": checked,
        "failures": failures,
        "verified": not failures,
    }


def run_all(output_dir: Path) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)

    hyperbolic_rows, hyperbolic_summary = enumerate_hyperbolic_norms()
    smooth_rows, smooth_summary = sampled_germ_control()
    certificate_summary = certificate_t0_control()

    hyperbolic_path = output_dir / "hyperbolic_norm_audit.csv"
    smooth_path = output_dir / "smooth_germ_control.csv"
    certificate_path = output_dir / "certificate_t0_audit.json"
    summary_path = output_dir / "run_summary.json"
    manifest_path = output_dir / "manifest.sha256"

    write_csv(hyperbolic_path, hyperbolic_rows)
    write_csv(smooth_path, smooth_rows)
    write_json(certificate_path, certificate_summary)

    run_summary = {
        "research_date": RESEARCH_DATE,
        "control_scope": "Stage-3 same-object trace certificate Phase 2",
        "data_policy": {
            "riemann_zero_inputs": 0,
            "fitted_parameters": 0,
            "network_inputs": 0,
            "random_seeds": None,
            "cofinite_selberg_formula_transcribed": False,
        },
        "theorem_status": {
            "local_germ_ambiguity": "PROVED",
            "clock_support_disjointness": "PROVED",
            "coordinatewise_splice_t0_failure": "PROVED",
            "proof_artifact": "notes/proof_audit.md",
        },
        "hyperbolic_norm_control": hyperbolic_summary,
        "smooth_germ_control": smooth_summary,
        "certificate_t0_control": {
            "den_t0_passes": certificate_summary["den_same_source_record"]["t0_passes"],
            "den_all_required_fields_populated": certificate_summary[
                "den_same_source_record"
            ]["all_required_fields_populated"],
            "mod_t0_passes": certificate_summary["mod_same_source_record"]["t0_passes"],
            "hybrid_t0_passes": certificate_summary[
                "coordinatewise_den_mod_splice"
            ]["t0_passes"],
            "clock_lock_mix_t0_passes": certificate_summary[
                "same_candidate_different_clock_lock"
            ]["t0_passes"],
        },
        "route_b_invocation_allowed": False,
    }
    write_json(summary_path, run_summary)

    manifest_inputs = [
        PAPER_DIR / "notes" / "proof_audit.md",
        PAPER_DIR / "code" / "trace_certificate_controls.py",
        PAPER_DIR / "code" / "test_trace_certificate_controls.py",
        PAPER_DIR / "experiments" / "reproduce.sh",
        hyperbolic_path,
        smooth_path,
        certificate_path,
        summary_path,
    ]
    missing_inputs = [path for path in manifest_inputs if not path.is_file()]
    if missing_inputs:
        raise FileNotFoundError(
            "manifest inputs are missing: " + ", ".join(map(str, missing_inputs))
        )
    write_manifest(manifest_path, manifest_inputs)
    verification = verify_manifest(manifest_path)
    if not verification["verified"]:
        raise AssertionError(f"newly written manifest failed: {verification}")
    return {"summary": run_summary, "manifest_verification": verification}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=PAPER_DIR / "results",
        help="directory for deterministic result artifacts",
    )
    parser.add_argument(
        "--verify-manifest",
        type=Path,
        help="verify an existing manifest instead of regenerating results",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.verify_manifest is not None:
        verification = verify_manifest(args.verify_manifest.resolve())
        print(json.dumps(verification, indent=2, sort_keys=True))
        return 0 if verification["verified"] else 1

    result = run_all(args.output_dir.resolve())
    compact = {
        "hyperbolic_rows": result["summary"]["hyperbolic_norm_control"]["rows"],
        "local_bump_difference": result["summary"]["smooth_germ_control"][
            "maximum_local_absolute_difference"
        ],
        "global_bump_difference": result["summary"]["smooth_germ_control"][
            "maximum_global_absolute_difference"
        ],
        "hybrid_t0_passes": result["summary"]["certificate_t0_control"][
            "hybrid_t0_passes"
        ],
        "manifest_verified": result["manifest_verification"]["verified"],
    }
    print(json.dumps(compact, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
