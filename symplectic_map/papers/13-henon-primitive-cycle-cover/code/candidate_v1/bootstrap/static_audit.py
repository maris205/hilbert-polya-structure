"""Science-free source, AST, schema, and tree controls."""

import ast
from pathlib import Path
import re

from .canonical import canonical_bytes, read_regular_bytes, sha256_bytes, strict_load_bytes
from .constants import (
    CODE_RELATIVE,
    DEFINITIONS_RELATIVE,
    Q_ENGINE_RELATIVE,
    Q_FIXTURE_RELATIVE,
    R_ENGINE_RELATIVE,
    R_FIXTURE_RELATIVE,
    SOURCE_LOCK_RELATIVE,
    SOURCE_LOCK_SHA256,
    SOURCE_REVIEW_RELATIVE,
    SOURCE_REVIEW_SHA256,
)


ENGINE_FORBIDDEN_NAMES = frozenset(
    {
        "__import__",
        "breakpoint",
        "compile",
        "eval",
        "exec",
        "getattr",
        "globals",
        "input",
        "locals",
        "open",
        "print",
        "setattr",
        "vars",
    }
)
ENGINE_FORBIDDEN_MODULE_NAMES = frozenset(
    {
        "ctypes",
        "importlib",
        "os",
        "pathlib",
        "random",
        "requests",
        "secrets",
        "socket",
        "subprocess",
        "sys",
        "urllib",
    }
)
SCAN_LOOP_TARGETS = frozenset(
    {"d", "n", "degree", "period", "prime", "modulus", "parameter", "seed"}
)
EXPECTED_DEFINITIONS_SHA256 = (
    "3c77fd28005786c03bf6dbbffc28cc5fcbc01aa1d8134a19b2ba593a622aef2c"
)
EXPECTED_DEFINITIONS = {
    "base_ring": "Q[a,c]",
    "candidate_id": "henon_primitive_cycle_cover_v1",
    "control_identifier_type": "one of N1,N2,N3,N4,N5,N6,N7,N8",
    "cyclic_coordinate_convention": "(z_i,z_(i-1)) maps to (z_(i+1),z_i), indices modulo n",
    "cyclic_equation_convention": "z_i^d+a*z_(i-1)+c-z_(i+1)",
    "derivative_matrix_convention": "M_i=[[d*z_i^(d-1),a],[1,0]], return product ordered M_(n-1)...M_0",
    "fixed_integer_type": "d and n are exact integers at least 2",
    "fraction_field": "Q(a,c)",
    "normalized_family": "H_(a,c)(x,y)=(a*y+x^d+c,x)",
    "observable_names": {
        "rho": "pointwise derivative-return matrix trace",
        "tau": "cyclic coordinate sum",
    },
    "proof_contract_identifier_type": "one of P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12",
    "rational_wire_type": "object with exact integer numerator and positive integer denominator",
    "schema": "P13_DEFINITIONS_AND_TYPES_V1",
    "scope": "normalized affine two-parameter family only",
    "sparse_polynomial_wire_type": "sorted list of [monomial-exponent-vector,rational-coefficient] pairs",
}
EXPECTED_PRIVATE_SCHEMAS = (
    Path("code/candidate_v1/track_q/certificate.schema.json"),
    Path("code/candidate_v1/track_q/private_fixture.schema.json"),
    Path("code/candidate_v1/track_r/certificate.schema.json"),
    Path("code/candidate_v1/track_r/private_fixture.schema.json"),
)
EXPECTED_REVIEWED_SCHEMA_SHA256 = {
    "code/candidate_v1/shared/capability.schema.json": "d6423836ceb6b9d13ba165c4ff44253f5c43c75b7f5fd6d2f7064fe719716ba6",
    "code/candidate_v1/shared/durable_claim.schema.json": "91ade69993b9789e025ac864148205502e35e35b3bbc7f6fd1a789ca2abfea9b",
    "code/candidate_v1/shared/execution_stage.schema.json": "9fdac75f5e97599f402e528356f48730f6caa6cde25652384fff7593229c4a52",
    "code/candidate_v1/shared/raw_result.schema.json": "bfcf309a5566e15b6817c490bcd166e74cae9d83a13e8ffc50260f7014362d99",
    "code/candidate_v1/shared/result_manifest.schema.json": "35d188c119563190ab10e6c894b57664f343c0ac6cb8e94e815996bdd5570921",
    "code/candidate_v1/shared/terminal.schema.json": "b622a2c1625798b10f8c0b9fe139f5aac118bee9500a08e1402d9e500a470535",
    "code/candidate_v1/shared/track_envelope.schema.json": "0273ce2ecb097d9681db16a4e9df69e1612b285d8f54609ec7883def13bbc5cb",
    "code/candidate_v1/track_q/certificate.schema.json": "0411041406ec1a619b01bc7b2184efe974d0c85fe58f7a9ad89a6666d7cbb6b3",
    "code/candidate_v1/track_q/private_fixture.schema.json": "8386365d5c6ad4cbeb86afc536d8476ab76b5b55c71b14fcf2320d3a37f8f7c2",
    "code/candidate_v1/track_r/certificate.schema.json": "060fcf4938836649d83b694034f29691a543985e9cde126b8e2a63b2effca4d1",
    "code/candidate_v1/track_r/private_fixture.schema.json": "6f5958bc7b282b70d07537f5745a73978bd94105ccb189cf4ae5a4e1ee99daaf",
}
EXPECTED_SHARED_FILES = frozenset(
    {
        "capability.schema.json",
        "definitions.json",
        "durable_claim.schema.json",
        "execution_stage.schema.json",
        "raw_result.schema.json",
        "result_manifest.schema.json",
        "terminal.schema.json",
        "track_envelope.schema.json",
    }
)
EXPECTED_TRACK_FILES = frozenset(
    {
        "certificate.schema.json",
        "engine.py",
        "private_fixture.json",
        "private_fixture.schema.json",
        "runner.py",
    }
)
EXPECTED_CODE_DIRECTORIES = frozenset(
    {
        "candidate_v1",
        "candidate_v1/adjudicator",
        "candidate_v1/bootstrap",
        "candidate_v1/orchestrator",
        "candidate_v1/shared",
        "candidate_v1/track_q",
        "candidate_v1/track_r",
        "scripts",
        "tests",
    }
)
EXPECTED_CODE_FILES = frozenset(
    {
        "README.md",
        "candidate_v1/__init__.py",
        "candidate_v1/adjudicator/acceptance_ledger.json",
        "candidate_v1/adjudicator/adjudicate.py",
        "candidate_v1/bootstrap/__init__.py",
        "candidate_v1/bootstrap/boundary.py",
        "candidate_v1/bootstrap/canonical.py",
        "candidate_v1/bootstrap/constants.py",
        "candidate_v1/bootstrap/launcher.py",
        "candidate_v1/bootstrap/lifecycle.py",
        "candidate_v1/bootstrap/manifest.py",
        "candidate_v1/bootstrap/preflight.py",
        "candidate_v1/bootstrap/static_audit.py",
        "candidate_v1/orchestrator/__init__.py",
        "candidate_v1/orchestrator/registered.py",
        "candidate_v1/shared/capability.schema.json",
        "candidate_v1/shared/definitions.json",
        "candidate_v1/shared/durable_claim.schema.json",
        "candidate_v1/shared/execution_stage.schema.json",
        "candidate_v1/shared/raw_result.schema.json",
        "candidate_v1/shared/result_manifest.schema.json",
        "candidate_v1/shared/terminal.schema.json",
        "candidate_v1/shared/track_envelope.schema.json",
        "candidate_v1/track_q/certificate.schema.json",
        "candidate_v1/track_q/engine.py",
        "candidate_v1/track_q/private_fixture.json",
        "candidate_v1/track_q/private_fixture.schema.json",
        "candidate_v1/track_q/runner.py",
        "candidate_v1/track_r/certificate.schema.json",
        "candidate_v1/track_r/engine.py",
        "candidate_v1/track_r/private_fixture.json",
        "candidate_v1/track_r/private_fixture.schema.json",
        "candidate_v1/track_r/runner.py",
        "scripts/freeze_code_manifest.py",
        "scripts/run_registered_once.py",
        "scripts/run_safe_preflight.py",
        "tests/__init__.py",
        "tests/conftest.py",
        "tests/test_adjudicator_mutations.py",
        "tests/test_canonical_security.py",
        "tests/test_lifecycle.py",
        "tests/test_manifest_junit.py",
        "tests/test_mutation_security.py",
        "tests/test_q_helpers.py",
        "tests/test_r_helpers.py",
        "tests/test_registered_orchestrator.py",
        "tests/test_runtime_isolation.py",
    }
)
EXPECTED_CRITICAL_PYTHON_FINGERPRINTS = {
    "scripts/run_registered_once.py": {
        "ast_sha256": "c49f77cd5d79c87cb5a0ea928581c2beaed94992af95df82b45b5dbf1281c0ab",
        "functions": ["main"],
        "source_sha256": "ad5b85e1268d80fd17e382e3264cddf5fa7cad2824733e8287b1816b7a25cae2",
    },
    "candidate_v1/orchestrator/registered.py": {
        "ast_sha256": "6047aa20cfd29db62212c5eedb2f15b3483c9cbbe22f6cc32e4d10f9b1f22d60",
        "functions": ["_exact", "_exact_keys", "_read_bound_canonical", "_validate_code_manifest_live", "_validate_deployment_review", "_validate_prelaunch_inputs", "_capture_inbound_snapshot", "_verify_inbound_snapshot", "_consume_final_inbound_guard", "create_registered_claim_from_frozen", "_validate_access_counter_evidence", "_count_forbidden_authority_fields", "_anti_claim_counter_evidence", "_collect_registered_counters", "_embedded_fields", "_registered_operation", "_validate_registered_api_inputs", "execute_registered_once", "run_registered_transaction"],
        "source_sha256": "61df9b111013aad85af352326a0a130ba847a7b74942af7227801c3929bcedbc",
    },
    "candidate_v1/bootstrap/canonical.py": {
        "ast_sha256": "96b950cdf097f86b308d9b3adbca96d30848301f5b4187976bf9b6a674c1afc1",
        "functions": ["_reject_constant", "_reject_float", "_pairs_no_duplicates", "strict_load_bytes", "canonical_bytes", "strict_canonical_load", "sha256_bytes", "sha256_file", "read_regular_bytes", "fsync_directory", "write_bytes_exclusive", "_ensure_directory_chain", "_assert_no_symlink_ancestor", "write_json_exclusive"],
        "source_sha256": "e32dd81f7efbd1c3f7ca567e27b75b1f08e5fa8b52262dd3ea6f1ef4cf3fcd3e",
    },
    "candidate_v1/bootstrap/launcher.py": {
        "ast_sha256": "1b8270471b365eb6eb29da1976a52b14151524381738e038aab3369f2cf28345",
        "functions": ["_descriptor_snapshot", "_restore_descriptor_three", "_safe_close_descriptor", "_safe_close_stream", "_safe_close_process_stream", "_safe_poll", "_leader_exited_without_reap", "_kill_isolated_process_group", "_live_process_group_members", "_quiesce_isolated_process_group", "_add_cleanup_error", "_run_child", "_is_sha256", "_safe_token", "_validate_safe_response", "launch_safe_probe", "_registered_nonce", "_registered_token", "launch_registered_track"],
        "source_sha256": "66eddcdcebdfd7553c2f069f8f9e07f2338c1c55cca5d496d0b26bdaa1d21f6a",
    },
    "candidate_v1/bootstrap/lifecycle.py": {
        "ast_sha256": "e78de478f13a824dec88aa6cb6ee505d26317b7ae711b289a52f3798d282ad2b",
        "functions": ["_commit_terminal_once", "_json_exact", "_stream_diagnostic", "bounded_child_diagnostic", "_is_sha256", "_registered_capability_nonce", "_validate_stream_diagnostic", "validate_child_diagnostic", "build_claim", "_validate_claim_object", "_claim_receipt", "create_claim", "load_claim_receipt", "validate_claim_file", "terminalize_failure", "_validate_terminal_object", "_decode_embedded_record", "_validate_registered_capability", "_validate_registered_envelope", "_validate_registered_payload", "_seal_success", "_validate_result_manifest", "_validate_preterminal_runtime_tree", "_execution_stage_object", "run_after_claim"],
        "source_sha256": "1478df58426bd941882d88b5f57048155519df6ea43adcfac81c650f23040f01",
    },
    "candidate_v1/bootstrap/manifest.py": {
        "ast_sha256": "8f28d3e8bbda6c41386fc4d5cb56beed26dbf3629ba70e260f5a174dc44e15aa",
        "functions": ["_code_files", "code_tree_sha256", "_declared_count", "_suite_record", "_junit_record", "_validate_preflight_shape", "_preflight_record", "build_code_manifest", "validate_manifest_object"],
        "source_sha256": "190db5a56cc81493340caa396dc894b7a5e8b122ef016163cbda1cd6a4cd70d6",
    },
    "candidate_v1/bootstrap/preflight.py": {
        "ast_sha256": "25a0b226407edbe65e968d52ba06d4f5b9da540211442301f19797e2006f6c85",
        "functions": ["collect_preflight"],
        "source_sha256": "6c2f5bc128854852c9c782b1e9d488c75caace7380a04395e2378728694849f7",
    },
    "candidate_v1/adjudicator/adjudicate.py": {
        "ast_sha256": "8ac091f8713f94713171181776d2820c2b5699a60291e40faea4641a931bcd97",
        "functions": ["_keys", "_exact", "_q_rational", "_q_base_polynomial", "_r_base_polynomial", "_zero_rational", "_matrix_is_zero", "_normalized_q", "_normalized_r", "_track_route_q", "_track_route_r", "_attack_records_q", "_attack_records_r", "_contract_presence", "_validate_governance", "_validate_private_routes_and_attacks", "adjudicate"],
        "source_sha256": "a94fc8830b98ecf64fb93e7693eec2e5d1b612e1025cb6160d09fea6b26012aa",
    },
    "candidate_v1/track_q/runner.py": {
        "ast_sha256": "167f34ba9703d4ae4b965caa68d828525dffb47f93f3bb899664ec6a1e51b3ca",
        "functions": ["_pairs", "_reject_constant", "_reject_float", "_strict_load", "_canonical", "_sha", "_is_hex", "_read_capability", "_read_regular", "_install_guard", "_expect_denied", "_probe_write_open", "_probe_scandir", "_probe_rename", "_probe_unlink", "_run_safe_probes", "_build_science_builtins", "_exact_keys", "_validate_rational_wire", "_validate_poly_wire", "_validate_rejection_list", "_validate_certificate", "_registered_science", "main"],
        "source_sha256": "2ea9f7a110530a22f25b1a7b298736c5c51f0280eca753c9c0e4cb5e7533f9ca",
    },
    "candidate_v1/track_r/runner.py": {
        "ast_sha256": "33c94b4326601f223aa7eec181dc238ebf9c84569a26a3d2af5fb01e9adf3caf",
        "functions": ["_rj_pairs", "_rj_reject_constant", "_rj_reject_float", "_rj_load", "_rj_canonical", "_rj_sha", "_rj_is_hex", "_rj_read_capability", "_rj_read_regular", "_rj_install_guard", "_rj_expect_denied", "_rj_probe_write", "_rj_probe_scandir", "_rj_probe_rename", "_rj_probe_unlink", "_rj_safe_probes", "_rj_build_science_builtins", "_rj_keys", "_rj_rational", "_rj_poly", "_rj_matrix2", "_rj_rejections", "_rj_validate_certificate", "_rj_registered", "main"],
        "source_sha256": "37345fedca7552c147333bdd42ca3095b836bdd91afbf7bb09468075c720965e",
    },
}
SCHEMA_KEYWORDS = frozenset(
    {
        "$defs",
        "$ref",
        "$schema",
        "additionalProperties",
        "allOf",
        "const",
        "else",
        "enum",
        "if",
        "items",
        "maxItems",
        "maxLength",
        "maximum",
        "minItems",
        "minLength",
        "minimum",
        "oneOf",
        "pattern",
        "prefixItems",
        "properties",
        "required",
        "then",
        "title",
        "type",
        "uniqueItems",
    }
)
DUNDER_ESCAPE_TOKENS = frozenset(
    {
        "__bases__",
        "__builtins__",
        "__class__",
        "__closure__",
        "__code__",
        "__dict__",
        "__func__",
        "__globals__",
        "__mro__",
        "__self__",
        "__subclasses__",
    }
)
ENGINE_ATTRIBUTE_ALLOWLISTS = {
    "Q": frozenset(
        {"add", "append", "denominator", "extend", "get", "items", "keys", "numerator", "pop", "setdefault", "values"}
    ),
    "R": frozenset(
        {"add", "append", "denominator", "extend", "get", "items", "keys", "numerator", "pop", "remove", "setdefault", "values"}
    ),
}
ENGINE_LOOP_FINGERPRINTS = {
    "Q": {
        "counts": {"DictComp": 8, "For": 15, "GeneratorExp": 21, "ListComp": 7, "SetComp": 0, "While": 7},
        "sha256": "e0fc6a60ad47e5ef587c8ebd01182a651bafc9abd4403e794e8c1c81d6bdec4a",
    },
    "R": {
        "counts": {"DictComp": 2, "For": 19, "GeneratorExp": 21, "ListComp": 10, "SetComp": 0, "While": 7},
        "sha256": "03c6839492c1a8dcd6f7593a2c5e4ae847cb1736c8722f86691d05595a9198f8",
    },
}
ENGINE_MOD_FINGERPRINTS = {
    "Q": {"count": 0, "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},
    "R": {"count": 3, "sha256": "eee117526f5e658fda2f09abe04f2817c4604ad6953c247f3ad991653e1278ef"},
}
ENGINE_EXACT_FINGERPRINTS = {
    "Q": {
        "ast_sha256": "a4834525bb78c077b4c36d005373a98c6fe87ba8bfeb183ee10d706d1fb3f3fd",
        "function_count": 41,
        "source_sha256": "159fb635809ec33aff2979ac7b386066f6b1ac2abacb26653fd51821542bfabd",
    },
    "R": {
        "ast_sha256": "485b1d5bb2829fdd507c8bfa7b9cc9b26eded051196ce7fad7476553a4559c6c",
        "function_count": 36,
        "source_sha256": "a3b42cbd0f48ef18aa9e4c0953b36343e2151e058920c163f72b0ed8d813dc6d",
    },
}


def _loop_target_names(target):
    if isinstance(target, ast.Name):
        return {target.id}
    if isinstance(target, (ast.Tuple, ast.List)):
        output = set()
        for element in target.elts:
            output.update(_loop_target_names(element))
        return output
    return set()


def _constant_string_expression(node):
    if isinstance(node, ast.Constant) and type(node.value) is str:
        return node.value
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left = _constant_string_expression(node.left)
        right = _constant_string_expression(node.right)
        if left is not None and right is not None:
            return left + right
    return None


def _protected_engine_string(value, other_track_token):
    lowered = value.lower()
    return (
        other_track_token in lowered
        or "acceptance_ledger" in lowered
        or "proof_package" in lowered
        or "independent_source" in lowered
        or "experiments/" in lowered
        or "refine-logs" in lowered
        or "__" in value
        or any(token in value for token in DUNDER_ESCAPE_TOKENS)
    )


def _audit_engine(path: Path, track: str, enforce_live_fingerprints=False):
    source = read_regular_bytes(path).decode("utf-8")
    tree = ast.parse(source, filename=path.as_posix())
    imports = []
    helper_names = []
    forbidden_name_hits = []
    forbidden_module_hits = []
    float_literal_count = 0
    scan_loop_hits = []
    dangerous_string_hits = []
    attribute_names = set()
    identifier_names = set()
    call_target_names = set()
    loop_counts = {
        "DictComp": 0,
        "For": 0,
        "GeneratorExp": 0,
        "ListComp": 0,
        "SetComp": 0,
        "While": 0,
    }
    loop_records = []
    modulus_records = []
    other_track_token = "track_r" if track == "Q" else "track_q"
    module_nodes = list(tree.body)
    if (
        len(module_nodes) < 3
        or not isinstance(module_nodes[0], ast.Expr)
        or not isinstance(module_nodes[0].value, ast.Constant)
        or type(module_nodes[0].value.value) is not str
        or not isinstance(module_nodes[1], ast.ImportFrom)
        or module_nodes[1].level != 0
        or module_nodes[1].module != "fractions"
        or [(alias.name, alias.asname) for alias in module_nodes[1].names] != [("Fraction", None)]
        or any(not isinstance(node, ast.FunctionDef) for node in module_nodes[2:])
    ):
        raise RuntimeError(track + " engine exact module skeleton drift")
    for index, node in enumerate(module_nodes):
        allowed_docstring = (
            index == 0
            and isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Constant)
            and type(node.value.value) is str
        )
        allowed_import = (
            isinstance(node, ast.ImportFrom)
            and node.level == 0
            and node.module == "fractions"
            and [(alias.name, alias.asname) for alias in node.names] == [("Fraction", None)]
        )
        if not allowed_docstring and not allowed_import and not isinstance(node, ast.FunctionDef):
            raise RuntimeError(track + " engine has executable module-level node")
        if isinstance(node, ast.FunctionDef):
            arguments = node.args
            annotated_arguments = [
                argument
                for argument in (
                    *arguments.posonlyargs,
                    *arguments.args,
                    *arguments.kwonlyargs,
                )
                if argument.annotation is not None
            ]
            if arguments.vararg is not None and arguments.vararg.annotation is not None:
                annotated_arguments.append(arguments.vararg)
            if arguments.kwarg is not None and arguments.kwarg.annotation is not None:
                annotated_arguments.append(arguments.kwarg)
            if (
                node.decorator_list
                or node.returns is not None
                or node.type_comment is not None
                or arguments.defaults
                or any(default is not None for default in arguments.kw_defaults)
                or annotated_arguments
                or getattr(node, "type_params", ())
            ):
                raise RuntimeError(track + " engine executable definition metadata")
    for node in ast.walk(tree):
        # Several pattern/definition identifiers are stored as raw strings rather
        # than Name/Attribute nodes (notably MatchClass.kwd_attrs).  Scan every
        # AST field so no dunder object-graph handle can hide there.
        for field_name, field_value in ast.iter_fields(node):
            raw_identifiers = []
            if type(field_value) is str and field_name != "value":
                raw_identifiers = [field_value]
            elif type(field_value) is list and all(type(item) is str for item in field_value):
                raw_identifiers = field_value
            for identifier in raw_identifiers:
                if identifier.startswith("__") or identifier in DUNDER_ESCAPE_TOKENS:
                    forbidden_name_hits.append(identifier)
        type_alias_node = getattr(ast, "TypeAlias", ())
        if isinstance(node, (ast.ClassDef, ast.AsyncFunctionDef, ast.Lambda)) or (
            type_alias_node and isinstance(node, type_alias_node)
        ):
            raise RuntimeError(track + " engine nested executable definition form")
        if isinstance(node, ast.FunctionDef) and node not in module_nodes:
            raise RuntimeError(track + " engine nested function definition")
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append((node.module, tuple(alias.name for alias in node.names)))
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            helper_names.append(node.name)
            arguments = node.args
            annotated_arguments = [
                argument
                for argument in (
                    *arguments.posonlyargs,
                    *arguments.args,
                    *arguments.kwonlyargs,
                )
                if argument.annotation is not None
            ]
            if arguments.vararg is not None and arguments.vararg.annotation is not None:
                annotated_arguments.append(arguments.vararg)
            if arguments.kwarg is not None and arguments.kwarg.annotation is not None:
                annotated_arguments.append(arguments.kwarg)
            if (
                node.decorator_list
                or node.returns is not None
                or node.type_comment is not None
                or arguments.defaults
                or any(default is not None for default in arguments.kw_defaults)
                or annotated_arguments
                or getattr(node, "type_params", ())
            ):
                raise RuntimeError(track + " engine executable nested definition metadata")
        elif isinstance(node, ast.Name):
            identifier_names.add(node.id)
            if node.id in ENGINE_FORBIDDEN_NAMES:
                forbidden_name_hits.append(node.id)
            if node.id in ENGINE_FORBIDDEN_MODULE_NAMES:
                forbidden_module_hits.append(node.id)
            if node.id.startswith("__") or node.id in DUNDER_ESCAPE_TOKENS:
                forbidden_name_hits.append(node.id)
        elif isinstance(node, ast.Attribute):
            attribute_names.add(node.attr)
            if node.attr not in ENGINE_ATTRIBUTE_ALLOWLISTS[track]:
                forbidden_name_hits.append(node.attr)
            if node.attr.startswith("__") or node.attr in DUNDER_ESCAPE_TOKENS:
                forbidden_name_hits.append(node.attr)
        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            forbidden_name_hits.append("division-operator")
        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Pow):
            forbidden_name_hits.append("power-operator")
        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod):
            modulus_records.append(ast.dump(node, include_attributes=False) + "\n")
        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            folded = _constant_string_expression(node)
            if folded is not None and _protected_engine_string(folded, other_track_token):
                dangerous_string_hits.append(folded)
        elif isinstance(node, ast.Constant):
            if type(node.value) is float or type(node.value) is complex:
                float_literal_count += 1
            if type(node.value) is bytes:
                forbidden_name_hits.append("bytes-literal")
            if type(node.value) is str:
                if _protected_engine_string(node.value, other_track_token):
                    dangerous_string_hits.append(node.value)
        elif isinstance(node, (ast.JoinedStr, ast.FormattedValue)):
            dangerous_string_hits.append("dynamic-formatted-string")
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "str":
            dangerous_string_hits.append("dynamic-str-wrapper")
        elif isinstance(node, (ast.For, ast.AsyncFor)):
            targets = _loop_target_names(node.target)
            overlap = targets & SCAN_LOOP_TARGETS
            if overlap:
                scan_loop_hits.extend(sorted(overlap))
        if isinstance(node, (ast.For, ast.While, ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
            kind = type(node).__name__
            loop_counts[kind] += 1
            loop_records.append(kind + "\0" + ast.dump(node, include_attributes=False) + "\n")
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                call_target_names.add(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                call_target_names.add(node.func.attr)
    expected_import = [("fractions", ("Fraction",))]
    if imports != expected_import:
        raise RuntimeError(track + " engine import surface drift")
    if forbidden_name_hits or forbidden_module_hits:
        raise RuntimeError(track + " engine dangerous name")
    if float_literal_count:
        raise RuntimeError(track + " engine floating literal")
    if scan_loop_hits:
        raise RuntimeError(track + " engine scan-loop target")
    if dangerous_string_hits:
        raise RuntimeError(track + " engine protected-path/string reference")
    loop_fingerprint = sha256_bytes("".join(sorted(loop_records)).encode("utf-8"))
    zero_loop_counts = {key: 0 for key in loop_counts}
    if loop_counts == zero_loop_counts and not enforce_live_fingerprints:
        pass
    elif (
        loop_counts != ENGINE_LOOP_FINGERPRINTS[track]["counts"]
        or loop_fingerprint != ENGINE_LOOP_FINGERPRINTS[track]["sha256"]
    ):
        raise RuntimeError(track + " engine loop/comprehension fingerprint drift")
    modulus_fingerprint = sha256_bytes("".join(sorted(modulus_records)).encode("utf-8"))
    if not modulus_records and not enforce_live_fingerprints:
        pass
    elif (
        len(modulus_records) != ENGINE_MOD_FINGERPRINTS[track]["count"]
        or modulus_fingerprint != ENGINE_MOD_FINGERPRINTS[track]["sha256"]
    ):
        raise RuntimeError(track + " engine modulus-operator fingerprint drift")
    module_function_names = [node.name for node in tree.body if isinstance(node, ast.FunctionDef)]
    if len(module_function_names) != len(set(module_function_names)):
        raise RuntimeError(track + " duplicate top-level function name")
    if module_function_names.count("run_science") != 1:
        raise RuntimeError(track + " top-level science entry count")
    source_sha256 = sha256_bytes(source.encode("utf-8"))
    ast_sha256 = sha256_bytes(ast.dump(tree, include_attributes=False).encode("utf-8"))
    if enforce_live_fingerprints and (
        source_sha256 != ENGINE_EXACT_FINGERPRINTS[track]["source_sha256"]
        or ast_sha256 != ENGINE_EXACT_FINGERPRINTS[track]["ast_sha256"]
        or len(module_function_names) != ENGINE_EXACT_FINGERPRINTS[track]["function_count"]
    ):
        raise RuntimeError(track + " exact independently reviewed engine fingerprint drift")
    return {
        "ast_sha256": ast_sha256,
        "ast_node_count": sum(1 for _node in ast.walk(tree)),
        "attribute_surface": sorted(attribute_names),
        "call_target_surface": sorted(call_target_names),
        "float_literal_count": float_literal_count,
        "function_count": len(helper_names),
        "helper_count_excluding_entry": len([name for name in helper_names if name != "run_science"]),
        "import_surface": ["fractions.Fraction"],
        "identifier_surface": sorted(identifier_names),
        "loop_form_counts": loop_counts,
        "loop_form_fingerprint_sha256": loop_fingerprint,
        "modulus_operator_count": len(modulus_records),
        "modulus_operator_fingerprint_sha256": modulus_fingerprint,
        "scan_loop_target_count": len(scan_loop_hits),
        "source_sha256": source_sha256,
        "track": track,
    }


def _schema_json_type(value):
    if value is None:
        return "null"
    if type(value) is bool:
        return "boolean"
    if type(value) is int:
        return "integer"
    if type(value) is str:
        return "string"
    if type(value) is list:
        return "array"
    if type(value) is dict:
        return "object"
    return None


def _schema_branch_types(branch):
    if type(branch) is not dict:
        return set()
    declared = branch.get("type")
    if type(declared) is str:
        return {declared}
    if type(declared) is list and all(type(item) is str for item in declared):
        return set(declared)
    if "const" in branch:
        inferred = _schema_json_type(branch["const"])
        return {inferred} if inferred is not None else set()
    return set()


def _schema_constraints_disjoint(left, right):
    left_types = _schema_branch_types(left)
    right_types = _schema_branch_types(right)
    if left_types and right_types and left_types.isdisjoint(right_types):
        return True
    if type(left) is dict and type(right) is dict:
        left_properties = left.get("properties")
        right_properties = right.get("properties")
        if type(left_properties) is dict and type(right_properties) is dict:
            for key in set(left_properties) & set(right_properties):
                if _schema_constraints_disjoint(left_properties[key], right_properties[key]):
                    return True
    return False


def _walk_schema(
    node,
    location,
    errors,
    definitions,
    references,
    metrics,
    overlay_allowed=False,
):
    metrics["schema_node_count"] += 1
    if type(node) is not dict:
        errors.append(location + ": schema node is not an object")
        return
    if not node:
        errors.append(location + ": empty schema node")
        return
    unknown = set(node) - SCHEMA_KEYWORDS
    if unknown:
        errors.append(location + ": unknown schema keywords " + ",".join(sorted(unknown)))
    if "$ref" in node:
        reference = node["$ref"]
        if (
            type(reference) is not str
            or not reference.startswith("#/$defs/")
            or reference.count("/") != 2
            or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", reference.split("/")[-1])
        ):
            errors.append(location + ": nonlocal or malformed $ref")
        else:
            references.add(reference.split("/")[-1])
    node_type = node.get("type")
    if type(node_type) is list:
        if (
            not node_type
            or any(type(item) is not str for item in node_type)
            or len(node_type) != len(set(node_type))
        ):
            errors.append(location + ": invalid type union")
        type_values = set(node_type)
    elif node_type is None or type(node_type) is str:
        type_values = {node_type}
    else:
        errors.append(location + ": invalid type declaration")
        type_values = {None}
    valid_types = {None, "array", "boolean", "integer", "null", "object", "string"}
    if not type_values <= valid_types:
        errors.append(location + ": invalid type declaration")
    if "$schema" in node and node["$schema"] != "https://json-schema.org/draft/2020-12/schema":
        errors.append(location + ": invalid metaschema identifier")
    if "const" in node and node_type is not None:
        const_type = _schema_json_type(node["const"])
        if const_type not in type_values:
            errors.append(location + ": const/type mismatch")
    if "const" in node and "enum" in node and type(node["enum"]) is list:
        if canonical_bytes(node["const"]) not in {
            canonical_bytes(item) for item in node["enum"]
        }:
            errors.append(location + ": const is excluded by enum")
    if type(node.get("const")) is int:
        if type(node.get("minimum")) is int and node["const"] < node["minimum"]:
            errors.append(location + ": integer const is below minimum")
        if type(node.get("maximum")) is int and node["const"] > node["maximum"]:
            errors.append(location + ": integer const exceeds maximum")
    if type(node.get("const")) is str:
        if type(node.get("minLength")) is int and len(node["const"]) < node["minLength"]:
            errors.append(location + ": string const is shorter than minLength")
        if type(node.get("maxLength")) is int and len(node["const"]) > node["maxLength"]:
            errors.append(location + ": string const exceeds maxLength")
        if type(node.get("pattern")) is str:
            try:
                if re.search(node["pattern"], node["const"]) is None:
                    errors.append(location + ": string const does not match pattern")
            except re.error:
                pass
    if "enum" in node and node_type is not None:
        if type(node["enum"]) is list and any(
            _schema_json_type(item) not in type_values for item in node["enum"]
        ):
            errors.append(location + ": enum/type mismatch")
    if "title" in node and (type(node["title"]) is not str or not node["title"]):
        errors.append(location + ": invalid title")
    if "additionalProperties" in node and node["additionalProperties"] is not False:
        errors.append(location + ": additionalProperties must be false")
    object_keywords = {"additionalProperties", "properties", "required"}
    if set(node) & object_keywords and "object" not in type_values and not overlay_allowed:
        errors.append(location + ": object keywords require type object")
    array_keywords = {"items", "maxItems", "minItems", "prefixItems", "uniqueItems"}
    if set(node) & array_keywords and "array" not in type_values:
        errors.append(location + ": array keywords require type array")
    string_keywords = {"maxLength", "minLength", "pattern"}
    if set(node) & string_keywords and "string" not in type_values:
        errors.append(location + ": string keywords require type string")
    numeric_keywords = {"maximum", "minimum"}
    if set(node) & numeric_keywords and "integer" not in type_values:
        errors.append(location + ": numeric keywords require type integer")
    if "object" in type_values:
        if node.get("additionalProperties") is not False:
            errors.append(location + ": open object")
            metrics["recursive_open_node_count"] += 1
        if "properties" not in node or "required" not in node:
            errors.append(location + ": object lacks properties/required")
        else:
            required = node["required"]
            properties = node["properties"]
            if (
                type(required) is not list
                or any(type(item) is not str for item in required)
                or len(required) != len(set(required))
            ):
                errors.append(location + ": required is not unique strings")
            elif type(properties) is not dict or not properties or set(required) != set(properties):
                errors.append(location + ": required/properties mismatch")
    if "required" in node:
        required = node["required"]
        if (
            type(required) is not list
            or any(type(item) is not str for item in required)
            or len(required) != len(set(required))
        ):
            errors.append(location + ": required is not unique strings")
    if "array" in type_values:
        if "items" not in node and "prefixItems" not in node:
            errors.append(location + ": open array items")
            metrics["recursive_open_node_count"] += 1
        if "items" in node and node["items"] is not False and (
            type(node["items"]) is not dict or not node["items"]
        ):
            errors.append(location + ": items must be a nonempty schema object")
        minimum = node.get("minItems")
        maximum = node.get("maxItems")
        if minimum is not None and (type(minimum) is not int or minimum < 0):
            errors.append(location + ": invalid minItems")
        if maximum is not None and (type(maximum) is not int or maximum < 0):
            errors.append(location + ": invalid maxItems")
        if type(minimum) is int and type(maximum) is int and minimum > maximum:
            errors.append(location + ": minItems exceeds maxItems")
        if "uniqueItems" in node and node["uniqueItems"] is not True:
            errors.append(location + ": uniqueItems must be true")
    if "minimum" in node and type(node["minimum"]) is not int:
        errors.append(location + ": nonintegral minimum")
    if "maximum" in node and type(node["maximum"]) is not int:
        errors.append(location + ": nonintegral maximum")
    if type(node.get("minimum")) is int and type(node.get("maximum")) is int and node["minimum"] > node["maximum"]:
        errors.append(location + ": minimum exceeds maximum")
    if "minLength" in node and (type(node["minLength"]) is not int or node["minLength"] < 0):
        errors.append(location + ": invalid minLength")
    if "maxLength" in node and (type(node["maxLength"]) is not int or node["maxLength"] < 0):
        errors.append(location + ": invalid maxLength")
    if type(node.get("minLength")) is int and type(node.get("maxLength")) is int and node["minLength"] > node["maxLength"]:
        errors.append(location + ": minLength exceeds maxLength")
    if "pattern" in node:
        if type(node["pattern"]) is not str:
            errors.append(location + ": pattern is not a string")
        else:
            try:
                re.compile(node["pattern"])
            except re.error:
                errors.append(location + ": invalid regular expression")
    if "enum" in node:
        if type(node["enum"]) is not list or not node["enum"]:
            errors.append(location + ": enum is not a nonempty list")
        elif len({canonical_bytes(item) for item in node["enum"]}) != len(node["enum"]):
            errors.append(location + ": duplicate enum entry")
    for composition in ("allOf", "oneOf", "prefixItems"):
        if composition in node and (
            type(node[composition]) is not list
            or not node[composition]
            or any(type(item) is not dict for item in node[composition])
        ):
            errors.append(location + ": malformed " + composition)
        elif composition in node:
            encoded = [canonical_bytes(item) for item in node[composition]]
            if len(encoded) != len(set(encoded)):
                errors.append(location + ": duplicate " + composition + " branch")
            if composition == "oneOf":
                for left_index in range(len(node[composition])):
                    for right_index in range(left_index + 1, len(node[composition])):
                        if not _schema_constraints_disjoint(
                            node[composition][left_index], node[composition][right_index]
                        ):
                            errors.append(location + ": oneOf branches are not demonstrably disjoint")
    if "if" in node and "then" not in node and "else" not in node:
        errors.append(location + ": conditional lacks then/else")
    if "if" in node and type(node["if"]) is dict and "properties" in node["if"]:
        properties = node["if"].get("properties")
        required = node["if"].get("required")
        if type(properties) is dict and (
            type(required) is not list or set(required) != set(properties)
        ):
            errors.append(location + ": conditional property test is absence-vacuous")
    if ("then" in node or "else" in node) and "if" not in node:
        errors.append(location + ": orphan conditional branch")
    for conditional in ("if", "then", "else"):
        if conditional in node and (
            type(node[conditional]) is not dict or not node[conditional]
        ):
            errors.append(location + ": malformed " + conditional)
    if "$defs" in node:
        if type(node["$defs"]) is not dict or not node["$defs"]:
            errors.append(location + ": malformed $defs")
        elif any(
            type(key) is not str or re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", key) is None
            for key in node["$defs"]
        ):
            errors.append(location + ": malformed $defs key")
    if "properties" in node and type(node["properties"]) is not dict:
        errors.append(location + ": malformed properties")
    if "prefixItems" in node and node.get("items") is not False:
        errors.append(location + ": prefixItems tuple is not closed by items:false")
    if "prefixItems" in node and type(node["prefixItems"]) is list:
        tuple_length = len(node["prefixItems"])
        if node.get("minItems") != tuple_length or node.get("maxItems") != tuple_length:
            errors.append(location + ": prefixItems tuple length is not exact")
    for container_key in ("properties", "$defs"):
        container = node.get(container_key)
        if type(container) is dict:
            for child_key, child in container.items():
                _walk_schema(
                    child,
                    location + "/" + container_key + "/" + child_key,
                    errors,
                    definitions,
                    references,
                    metrics,
                    False,
                )
    for child_key in ("items", "if", "then", "else"):
        child = node.get(child_key)
        if child_key in node:
            if child_key == "items" and child is False:
                continue
            _walk_schema(
                child,
                location + "/" + child_key,
                errors,
                definitions,
                references,
                metrics,
                child_key in {"if", "then", "else"},
            )
    for list_key in ("allOf", "oneOf", "prefixItems"):
        children = node.get(list_key)
        if type(children) is list:
            for index, child in enumerate(children):
                if type(child) is dict:
                    _walk_schema(
                        child,
                        location + "/" + list_key + "/" + str(index),
                        errors,
                        definitions,
                        references,
                        metrics,
                        list_key in {"allOf", "oneOf"},
                    )


def _audit_schema(path: Path, project_root=None):
    value = strict_load_bytes(read_regular_bytes(path))
    if type(value) is not dict or not value:
        raise RuntimeError(path.name + ": schema root must be a nonempty object")
    if value.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise RuntimeError(path.name + ": exact draft-2020-12 metaschema required")
    recorded_path = (
        path.relative_to(project_root).as_posix()
        if project_root is not None
        else path.name
    )
    canonical_sha256 = sha256_bytes(canonical_bytes(value))
    reviewed_live_schema = False
    if project_root is not None:
        expected_sha256 = EXPECTED_REVIEWED_SCHEMA_SHA256.get(recorded_path)
        if expected_sha256 is None or canonical_sha256 != expected_sha256:
            raise RuntimeError(path.name + ": exact reviewed schema contract drift")
        reviewed_live_schema = True
    errors = []
    definitions = value.get("$defs", {})
    if type(definitions) is not dict:
        errors.append(path.name + ": $defs not an object")
        definitions = {}
    references = set()
    metrics = {"recursive_open_node_count": 0, "schema_node_count": 0}
    _walk_schema(value, path.name, errors, definitions, references, metrics)
    dangling = references - set(definitions)
    if dangling:
        errors.append(path.name + ": dangling refs " + ",".join(sorted(dangling)))
    graph = {}
    for definition_name, definition in definitions.items():
        targets = set()
        pending = [definition]
        while pending:
            item = pending.pop()
            if type(item) is dict:
                reference = item.get("$ref")
                if type(reference) is str and reference.startswith("#/$defs/") and reference.count("/") == 2:
                    targets.add(reference.split("/")[-1])
                pending.extend(item.values())
            elif type(item) is list:
                pending.extend(item)
        graph[definition_name] = targets
    for start in graph:
        pending = [(start, ())]
        while pending:
            current, ancestors = pending.pop()
            if current in ancestors:
                errors.append(path.name + ": cyclic local $ref at " + current)
                break
            pending.extend((target, ancestors + (current,)) for target in graph.get(current, ()))
    if errors:
        raise RuntimeError("; ".join(errors))
    if not reviewed_live_schema:
        pending = [(value, True)]
        while pending:
            item, is_root = pending.pop()
            if type(item) is dict:
                if set(item) & {"allOf", "if", "then", "else", "oneOf"}:
                    raise RuntimeError(path.name + ": unreviewed schema composition forbidden")
                if "$ref" in item:
                    permitted = {"$ref"}
                    if is_root:
                        permitted |= {"$schema", "$defs", "title"}
                    if not set(item) <= permitted:
                        raise RuntimeError(path.name + ": unreviewed $ref sibling forbidden")
                pending.extend((child, False) for child in item.values())
            elif type(item) is list:
                pending.extend((child, False) for child in item)
    return {
        "canonical_sha256": canonical_sha256,
        "exact_reviewed": reviewed_live_schema,
        "path": recorded_path,
        "recursive_open_node_count": metrics["recursive_open_node_count"],
        "schema_node_count": metrics["schema_node_count"],
    }


def _audit_fixture(value, label):
    pending = [value]
    forbidden_key_tokens = (
        "acceptance",
        "answer",
        "expected",
        "output",
        "result",
        "review",
        "source",
    )
    while pending:
        item = pending.pop()
        if type(item) is dict:
            for key, child in item.items():
                if type(key) is not str:
                    raise RuntimeError(label + " fixture non-string key")
                lowered = key.lower()
                if any(token in lowered for token in forbidden_key_tokens):
                    raise RuntimeError(label + " fixture contains authority/output key")
                pending.append(child)
        elif type(item) is list:
            pending.extend(item)
        elif type(item) not in (str, int, bool, type(None)):
            raise RuntimeError(label + " fixture contains nonexact JSON type")


def _json_field_inventory(value, prefix="$"):
    records = []
    if type(value) is dict:
        for key in sorted(value):
            child = value[key]
            path = prefix + "." + key
            records.append(path + ":" + _schema_json_type(child))
            records.extend(_json_field_inventory(child, path))
    elif type(value) is list:
        for index, child in enumerate(value):
            path = prefix + "[" + str(index) + "]"
            records.append(path + ":" + _schema_json_type(child))
            records.extend(_json_field_inventory(child, path))
    return records


def _tree_inventory(code_root: Path):
    if code_root.is_symlink() or not code_root.is_dir():
        raise RuntimeError("code root must be a regular directory")
    files = []
    directories = []
    for path in sorted(code_root.rglob("*"), key=lambda item: item.as_posix()):
        if path.is_symlink():
            raise RuntimeError("symlink in code tree")
        relative = path.relative_to(code_root).as_posix()
        if path.is_dir():
            directories.append(relative)
        elif path.is_file():
            if "__pycache__" in path.parts or path.suffix == ".pyc" or ".pytest_cache" in path.parts:
                raise RuntimeError("cache artifact in code tree")
            files.append(relative)
        else:
            raise RuntimeError("nonregular code-tree entry")
    return files, directories


def collect_static_audit(project_root: Path):
    source_lock_bytes = read_regular_bytes(project_root / SOURCE_LOCK_RELATIVE)
    source_review_bytes = read_regular_bytes(project_root / SOURCE_REVIEW_RELATIVE)
    if sha256_bytes(source_lock_bytes) != SOURCE_LOCK_SHA256:
        raise RuntimeError("source-lock binding drift")
    if sha256_bytes(source_review_bytes) != SOURCE_REVIEW_SHA256:
        raise RuntimeError("source-review binding drift")
    definitions_bytes = read_regular_bytes(project_root / DEFINITIONS_RELATIVE)
    definitions = strict_load_bytes(definitions_bytes)
    if (
        definitions_bytes != canonical_bytes(EXPECTED_DEFINITIONS)
        or sha256_bytes(definitions_bytes) != EXPECTED_DEFINITIONS_SHA256
    ):
        raise RuntimeError("shared definitions exact reviewed contract drift")
    if any(
        token in read_regular_bytes(project_root / DEFINITIONS_RELATIVE).decode("utf-8").lower()
        for token in ("expected", "acceptance", "proof_package", "source_lock", "review")
    ):
        raise RuntimeError("shared definitions contain forbidden scientific authority")
    q_fixture = strict_load_bytes(read_regular_bytes(project_root / Q_FIXTURE_RELATIVE))
    r_fixture = strict_load_bytes(read_regular_bytes(project_root / R_FIXTURE_RELATIVE))
    if q_fixture.get("track") != "Q" or r_fixture.get("track_identity") != "R":
        raise RuntimeError("private fixture identity")
    _audit_fixture(q_fixture, "Q")
    _audit_fixture(r_fixture, "R")
    q_fixture_schema = strict_load_bytes(
        read_regular_bytes(project_root / "code/candidate_v1/track_q/private_fixture.schema.json")
    )
    r_fixture_schema = strict_load_bytes(
        read_regular_bytes(project_root / "code/candidate_v1/track_r/private_fixture.schema.json")
    )
    if set(q_fixture_schema) != {"$schema", "const", "title"} or set(r_fixture_schema) != {"$schema", "const", "title"}:
        raise RuntimeError("private fixture schema exact metadata/root shape")
    if (
        canonical_bytes(q_fixture_schema["const"]) != canonical_bytes(q_fixture)
        or canonical_bytes(r_fixture_schema["const"]) != canonical_bytes(r_fixture)
    ):
        raise RuntimeError("private fixture exact-const schema drift")
    files, directories = _tree_inventory(project_root / CODE_RELATIVE)
    if set(files) != EXPECTED_CODE_FILES or set(directories) != EXPECTED_CODE_DIRECTORIES:
        raise RuntimeError("entire code package exact path inventory drift")
    engine_paths = sorted(path for path in files if path.endswith("/engine.py"))
    if engine_paths != [
        "candidate_v1/track_q/engine.py",
        "candidate_v1/track_r/engine.py",
    ]:
        raise RuntimeError("exact two-engine package inventory drift")
    entry_path = project_root / CODE_RELATIVE / "scripts/run_registered_once.py"
    entry_tree = ast.parse(
        read_regular_bytes(entry_path).decode("utf-8"),
        filename=entry_path.as_posix(),
    )
    entry_main_count = sum(
        1
        for node in entry_tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "main"
    )
    transaction_path = project_root / CODE_RELATIVE / "candidate_v1/orchestrator/registered.py"
    transaction_tree = ast.parse(
        read_regular_bytes(transaction_path).decode("utf-8"),
        filename=transaction_path.as_posix(),
    )
    transaction_function_count = sum(
        1
        for node in transaction_tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name == "run_registered_transaction"
    )
    if entry_main_count != 1 or transaction_function_count != 1:
        raise RuntimeError("unique registered entry/function inventory drift")
    critical_python_fingerprints = {}
    for relative, expected in EXPECTED_CRITICAL_PYTHON_FINGERPRINTS.items():
        path = project_root / CODE_RELATIVE / relative
        source_bytes = read_regular_bytes(path)
        tree = ast.parse(source_bytes.decode("utf-8"), filename=path.as_posix())
        observed = {
            "ast_sha256": sha256_bytes(
                ast.dump(tree, include_attributes=False).encode("utf-8")
            ),
            "functions": [
                node.name
                for node in tree.body
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            ],
            "source_sha256": sha256_bytes(source_bytes),
        }
        if canonical_bytes(observed) != canonical_bytes(expected):
            raise RuntimeError("exact critical Python fingerprint drift: " + relative)
        critical_python_fingerprints[relative] = observed
    shared_root = project_root / "code/candidate_v1/shared"
    if any(path.is_dir() or path.is_symlink() for path in shared_root.iterdir()):
        raise RuntimeError("shared directory must be a flat regular-file allowlist")
    shared_files = {
        path.name
        for path in shared_root.iterdir()
        if path.is_file() and not path.is_symlink()
    }
    if shared_files != EXPECTED_SHARED_FILES:
        raise RuntimeError("shared definitions/types inventory drift")
    if any(path.suffix == ".py" for path in shared_root.iterdir() if path.is_file()):
        raise RuntimeError("shared executable helper forbidden")
    for track_name in ("track_q", "track_r"):
        track_root = project_root / "code/candidate_v1" / track_name
        if track_root.is_symlink() or not track_root.is_dir():
            raise RuntimeError(track_name + " directory identity")
        if any(path.is_dir() or path.is_symlink() for path in track_root.iterdir()):
            raise RuntimeError(track_name + " directory must be a flat regular-file allowlist")
        observed_track_files = {
            path.name for path in track_root.iterdir() if path.is_file() and not path.is_symlink()
        }
        if observed_track_files != EXPECTED_TRACK_FILES:
            raise RuntimeError(track_name + " exact file inventory drift")
    schema_paths = sorted(
        (project_root / "code/candidate_v1/shared").glob("*.schema.json"),
        key=lambda item: item.as_posix(),
    ) + [project_root / path for path in EXPECTED_PRIVATE_SCHEMAS]
    schema_records = [_audit_schema(path, project_root) for path in schema_paths]
    expected_schema_paths = sorted(
        [
            "code/candidate_v1/shared/" + name
            for name in EXPECTED_SHARED_FILES
            if name.endswith(".schema.json")
        ]
        + [path.as_posix() for path in EXPECTED_PRIVATE_SCHEMAS]
    )
    if [record["path"] for record in schema_records] != expected_schema_paths:
        raise RuntimeError("exact recursive schema inventory drift")
    if (
        len(schema_records) != len(EXPECTED_REVIEWED_SCHEMA_SHA256)
        or any(not record["exact_reviewed"] for record in schema_records)
    ):
        raise RuntimeError("exact reviewed schema hash inventory drift")
    q_audit = _audit_engine(project_root / Q_ENGINE_RELATIVE, "Q", True)
    r_audit = _audit_engine(project_root / R_ENGINE_RELATIVE, "R", True)
    if set(q_audit["attribute_surface"]) != ENGINE_ATTRIBUTE_ALLOWLISTS["Q"]:
        raise RuntimeError("Q live engine exact attribute surface drift")
    if set(r_audit["attribute_surface"]) != ENGINE_ATTRIBUTE_ALLOWLISTS["R"]:
        raise RuntimeError("R live engine exact attribute surface drift")
    reviewed_identifiers = set(q_audit["identifier_surface"]) | set(
        r_audit["identifier_surface"]
    )
    reviewed_calls = set(q_audit["call_target_surface"]) | set(
        r_audit["call_target_surface"]
    )
    reviewed_surface = reviewed_identifiers | reviewed_calls
    closed_world_operation_counts = {
        "d_n_grid_scan_count": sum(
            audit["scan_loop_target_count"] for audit in (q_audit, r_audit)
        ),
        "interpolation_count": len(
            reviewed_surface & {"interpolate", "interpolation", "lagrange_interpolate"}
        ),
        "modulus_scan_count": len(
            reviewed_surface & {"modulus_scan", "scan_moduli", "scan_modulus"}
        ),
        "neighbor_d_n_evaluation_count": len(
            reviewed_surface & {"neighbor_degree", "neighbor_period", "neighbor_d_n"}
        ),
        "numerical_root_solve_count": len(
            reviewed_surface & {"nroots", "numerical_roots", "solve_numeric"}
        ),
        "parameter_scan_count": len(
            reviewed_surface & {"parameter_scan", "scan_parameters", "scan_parameter"}
        ),
        "post_result_retune_count": len(
            reviewed_surface & {"post_result_retune", "retune", "tune_after_result"}
        ),
        "prime_scan_count": len(
            reviewed_surface & {"prime_scan", "scan_primes", "scan_prime"}
        ),
        "random_seed_count": len(
            reviewed_surface & {"randint", "random", "seed", "secrets", "urandom"}
        ),
        "stored_exploratory_value_count": len(
            reviewed_surface & {"dump", "open", "save", "store", "write"}
        ),
    }
    if any(type(value) is not int or value != 0 for value in closed_world_operation_counts.values()):
        raise RuntimeError("exact reviewed engine closed-world operation drift")
    return {
        "cache_artifact_count": 0,
        "code_directory_count": len(directories),
        "code_file_count": len(files),
        "code_files": files,
        "closed_world_operation_counts": closed_world_operation_counts,
        "critical_python_fingerprints": critical_python_fingerprints,
        "definitions_only_shared_schema_count": 1,
        "definitions_contract_sha256": EXPECTED_DEFINITIONS_SHA256,
        "definitions_field_inventory": _json_field_inventory(definitions),
        "engine_audits": {"Q": q_audit, "R": r_audit},
        "exact_engine_count": 2,
        "registered_entry_file_count": 1,
        "registered_transaction_function_count": transaction_function_count,
        "private_fixture_count": 2,
        "private_fixture_contracts": {
            "Q": {
                "schema_mode": "EXACT_CONST_SCHEMA_PLUS_ENGINE_VALIDATOR_AND_HASH_BINDING",
                "validator": "_q_validate_inputs",
            },
            "R": {
                "schema_mode": "EXACT_CONST_SCHEMA_PLUS_ENGINE_VALIDATOR_AND_HASH_BINDING",
                "validator": "_r_validate_inputs",
            },
        },
        "recursive_schema_audits": schema_records,
        "exact_reviewed_schema_hash_count": len(schema_records),
        "schema_file_count": len(schema_records),
        "shared_arithmetic_helper_count": len(
            [path for path in shared_root.iterdir() if path.suffix == ".py"]
        ),
        "shared_schema_scientific_field_count": 0,
        "shared_scientific_implementation_count": len(
            [path for path in shared_root.iterdir() if path.suffix == ".py"]
        ),
        "source_lock_sha256": SOURCE_LOCK_SHA256,
        "source_review_sha256": SOURCE_REVIEW_SHA256,
        "symlink_count": 0,
        "third_engine_count": len(engine_paths) - 2,
    }
