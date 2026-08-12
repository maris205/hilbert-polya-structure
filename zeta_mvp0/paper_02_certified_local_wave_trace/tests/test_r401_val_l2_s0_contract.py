from __future__ import annotations

import ast
import hashlib
import json
import re
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "validated/capd_r401_local_complement_mp.cpp"
PROTOCOL = (
    ROOT
    / "research/route_a_wave_trace/R401_VAL_L2_S0_LOCAL_COMPLEMENT_PROTOCOL.md"
)
FREEZE = ROOT / "research/route_a_wave_trace/R401_VAL_L2_S0_FREEZE.md"
RUNNER = ROOT / "scripts/run_r401_val_l2_s0_local_complement.py"
CHECKER = ROOT / "scripts/check_r401_val_l2_s0_local_complement_independent.py"
PLAN = ROOT / "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json"
DEPENDENCY = ROOT / "validated/CAPD_DEPENDENCY.md"

REPRESENTATIVE_SLABS = ("S000", "S025", "S050")
PRECISIONS = (128, 256)
MAX_DEPTH = 40
MAX_NODES = 20_000


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").split())


def literal_assignment(path: Path, name: str) -> object:
    module = ast.parse(path.read_text(encoding="utf-8"))
    for node in module.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
            return ast.literal_eval(node.value)
    raise AssertionError(f"missing literal assignment {name} in {path}")


def dict_values(path: Path, key: str) -> list[ast.expr]:
    module = ast.parse(path.read_text(encoding="utf-8"))
    values: list[ast.expr] = []
    for node in ast.walk(module):
        if not isinstance(node, ast.Dict):
            continue
        for candidate, value in zip(node.keys, node.values, strict=True):
            if isinstance(candidate, ast.Constant) and candidate.value == key:
                values.append(value)
    return values


def contains_constant(node: ast.AST, value: object) -> bool:
    return any(
        isinstance(candidate, ast.Constant) and candidate.value == value
        for candidate in ast.walk(node)
    )


def test_freeze_hash_table_binds_every_frozen_l2_s0_input() -> None:
    freeze_text = FREEZE.read_text(encoding="utf-8")
    rows = re.findall(
        r"^\| `([^`]+)` \| `([0-9a-f]{64})` \|$",
        freeze_text,
        flags=re.MULTILINE,
    )
    assert len(rows) == len({relative for relative, _ in rows})
    embedded = dict(rows)
    frozen_inputs = (SOURCE, PROTOCOL, RUNNER, CHECKER, PLAN, DEPENDENCY)
    expected_relatives = {str(path.relative_to(ROOT)) for path in frozen_inputs}
    assert expected_relatives <= embedded.keys()
    for path in frozen_inputs:
        relative = str(path.relative_to(ROOT))
        assert sha256(path) == embedded[relative]


def test_representative_matrix_and_resource_limits_are_exactly_consistent() -> None:
    assert literal_assignment(RUNNER, "REPRESENTATIVE_SLABS") == REPRESENTATIVE_SLABS
    assert literal_assignment(CHECKER, "REPRESENTATIVE_SLABS") == REPRESENTATIVE_SLABS

    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    selected = {
        record["slab_id"]: (record["epsilon_lower"], record["epsilon_upper"])
        for record in plan["slabs"]
        if record["slab_id"] in REPRESENTATIVE_SLABS
    }
    assert selected == {
        "S000": ("0.0000", "0.0021"),
        "S025": ("0.0499", "0.0521"),
        "S050": ("0.0994", "0.1010"),
    }

    runner = normalized(RUNNER)
    checker = normalized(CHECKER)
    protocol = normalized(PROTOCOL)
    freeze = normalized(FREEZE)
    assert 'parser.add_argument("--max-depth", type=int, default=40)' in runner
    assert 'parser.add_argument("--max-nodes", type=int, default=20_000)' in runner
    assert (
        'parser.add_argument("--precisions", type=int, nargs="+", '
        'choices=(128, 256), default=(128, 256))'
    ) in runner
    assert (
        'parser.add_argument("--slabs", nargs="+", '
        'choices=REPRESENTATIVE_SLABS, default=REPRESENTATIVE_SLABS)'
    ) in runner
    assert "set(requested_precisions) == {128, 256}" in runner
    assert "set(selected_ids) == set(REPRESENTATIVE_SLABS)" in runner
    assert "args.max_depth == 40" in runner
    assert "args.max_nodes == 20_000" in runner
    assert "for bits in (128, 256)" in checker
    assert "for slab in REPRESENTATIVE_SLABS" in checker

    for text in (protocol, freeze):
        assert all(slab in text for slab in REPRESENTATIVE_SLABS)
        assert "128" in text and "256" in text
        assert "depth 40" in text
        assert "20,000" in text
    assert "three representative parameter slabs" in protocol
    assert "at both 128 and 256 MPFR bits" in protocol
    assert "six trees in total" in freeze

    assert MAX_DEPTH == 40
    assert MAX_NODES == 20_000
    assert PRECISIONS == (128, 256)


def test_producer_cannot_promote_and_only_checker_assigns_smoke_milestone() -> None:
    runner_text = RUNNER.read_text(encoding="utf-8")
    checker_text = CHECKER.read_text(encoding="utf-8")
    source_text = SOURCE.read_text(encoding="utf-8")

    assert "PASS_S0_PRODUCER" in runner_text
    assert "PASS_IMPLEMENTATION_SMOKE" not in runner_text
    assert "PASS_IMPLEMENTATION_SMOKE" not in source_text
    assert checker_text.count('"PASS_IMPLEMENTATION_SMOKE"') == 1

    runner_milestones = dict_values(RUNNER, "milestone_status")
    assert len(runner_milestones) >= 2
    assert all(isinstance(value, ast.Constant) and value.value is None for value in runner_milestones)
    runner_finals = dict_values(RUNNER, "final_status")
    assert runner_finals
    assert all(isinstance(value, ast.Constant) and value.value is None for value in runner_finals)

    checker_milestones = dict_values(CHECKER, "milestone_status")
    promoters = [
        value
        for value in checker_milestones
        if contains_constant(value, "PASS_IMPLEMENTATION_SMOKE")
    ]
    assert len(promoters) == 1
    assert isinstance(promoters[0], ast.IfExp)
    assert isinstance(promoters[0].orelse, ast.Constant)
    assert promoters[0].orelse.value is None
    checker_finals = dict_values(CHECKER, "final_status")
    assert checker_finals
    assert all(isinstance(value, ast.Constant) and value.value is None for value in checker_finals)

    freeze = normalized(FREEZE)
    assert "The producer may emit only `PASS_S0_PRODUCER`." in freeze
    assert "Only a zero-failure run" in freeze
    assert "may assign `PASS_IMPLEMENTATION_SMOKE`" in freeze
    assert "`final_status` remains null" in freeze


def test_checker_requires_exactly_six_unique_tree_pairs() -> None:
    checker = normalized(CHECKER)
    assert (
        "expected_pairs = {(bits, slab) for bits in (128, 256) "
        "for slab in REPRESENTATIVE_SLABS}"
    ) in checker
    assert 'tree_paths = sorted((output / "trees").glob("*/*.json"))' in checker
    assert "pair_counts[pair] = pair_counts.get(pair, 0) + 1" in checker
    assert (
        "if len(tree_paths) != 6 or any(count != 1 for count in "
        "pair_counts.values()):"
    ) in checker
    assert "if actual_pairs != expected_pairs:" in checker
    assert (
        'if len(summary.get("tree_summaries", [])) != 6 or '
        "summary_pairs != expected_pairs:"
    ) in checker
    assert len({(bits, slab) for bits in PRECISIONS for slab in REPRESENTATIVE_SLABS}) == 6


def test_cpp_logical_margins_and_energy_newton_guards_are_pinned() -> None:
    cpp = SOURCE.read_text(encoding="utf-8")
    compact = " ".join(cpp.split())
    checker = normalized(CHECKER)

    margin_match = re.search(
        r'logical_margin\(bits == 128 \? "([^"]+)" : "([^"]+)"\)',
        cpp,
    )
    assert margin_match is not None
    margin_128, margin_256 = map(Decimal, margin_match.groups())
    assert margin_128 == 2 * Decimal("1e-30")
    assert margin_256 == 2 * Decimal("1e-60")
    assert 'MpInterval("-1e-40", "1e-40")' in cpp
    assert 'MpInterval("-1e-75", "1e-75")' in cpp
    assert "return value.rightBound() < -margin || value.leftBound() > margin;" in compact

    derivative_gate = "if (gradient_full[1].leftBound() <= MpFloat(0))"
    newton_formula = "const MpInterval newton_raw = midpoint_root[1] - midpoint_residual / gradient_full[1];"
    guarded_newton = "const MpInterval newton = newton_raw + newton_guard;"
    intersection_gate = "if (!intersection(qplus, newton, contracted))"
    assert compact.index(derivative_gate) < compact.index(newton_formula)
    assert compact.index(newton_formula) < compact.index(guarded_newton)
    assert compact.index(guarded_newton) < compact.index(intersection_gate)
    assert "for (; energy_iterations < 10; ++energy_iterations)" in compact
    assert "energy_exclusion_guard = gap > logical_margin;" in compact
    assert compact.index("if (!energy_exclusion_guard)") < compact.index(
        "if (!energy_has_candidate)"
    )
    for enclosure in ("F_direct[index]", "F_mean[index]", "F_preconditioned[index]"):
        assert f"omits_zero({enclosure}, logical_margin)" in compact
    assert compact.index("if (excluded && krawczyk_subset)") < compact.index(
        "if (excluded)"
    )

    assert (
        "expected_margin = Fraction(1, 10**30) if bits == 128 "
        "else Fraction(1, 10**60)"
    ) in checker
    assert (
        "expected_guard = Fraction(1, 10**40) if bits == 128 "
        "else Fraction(1, 10**75)"
    ) in checker
    protocol = normalized(PROTOCOL)
    freeze = normalized(FREEZE)
    assert "10^{-30}" in protocol and "10^{-60}" in protocol
    assert "10^{-40}" in protocol and "10^{-75}" in protocol
    assert "`2e-30`, `2e-60`" in freeze
    assert "`1e-40` and `1e-75`" in freeze
