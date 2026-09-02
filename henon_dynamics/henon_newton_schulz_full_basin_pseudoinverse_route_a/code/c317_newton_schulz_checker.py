#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C317."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import sympy as sp
import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c317_newton_schulz_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C317/2026-09-03.yaml"
SOURCE = "1938bae19e5a92f9ce2411aafdc68323bd641bd0"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EXPECTED_EVALUATION_SHA256 = "d29ae6ce991fa179c563ea20e2b75077378f9f6a67e437fcf9900418cf8d6710"
EXPECTED_EVALUATION_SEMANTIC_SHA256 = "71ead48c862e8a5e55b5c4225a73cc3f7a696bbb342fba1873e81a22b4feacef"

SQUARE_SPECS = [
    ("nilpotent-j5", [("0", 5)]), ("nilpotent-mixed", [("0", 2), ("0", 4)]),
    ("scalar-half", [("1/2", 1)]), ("jordan-half-3", [("1/2", 3)]),
    ("jordan-minus-half-4", [("-1/2", 4)]),
    ("mixed-interior", [("1/3", 2), ("-1/2", 3)]),
    ("unit-one-semisimple", [("1", 1), ("1/2", 1)]),
    ("unit-minus-one-semisimple", [("-1", 1), ("1/3", 1)]),
    ("unit-i-semisimple", [("I", 1), ("1/2", 1)]),
    ("unit-jordan-3", [("1", 3)]), ("super-three-halves", [("3/2", 1)]),
    ("super-minus-two-j2", [("-2", 2)]),
    ("mixed-peripheral", [("1", 2), ("-1", 1), ("1/2", 2)]),
    ("zero-plus-half", [("0", 3), ("1/2", 2)]),
]
RECT_SPECS = [
    ("tall-3x2-r2", 3, 2, ["1", "3"], [("1/2", 2)]),
    ("wide-2x3-r2", 2, 3, ["1", "2"], [("1/2", 1), ("-1/3", 1)]),
    ("singular-square-4-r2", 4, 4, ["1", "2"], [("-1/2", 2)]),
    ("tall-5x3-r1", 5, 3, ["2"], [("0", 1)]),
    ("square-5-r3", 5, 5, ["1/2", "1", "4"], [("0", 2), ("1/2", 1)]),
    ("zero-3x5", 3, 5, [], []),
]
ALPHA_BASE = {"full-2": (2, 2, ["1", "2"]), "rank2-4x3": (4, 3, ["1", "3"]),
              "repeated-max-4": (4, 4, ["1", "2", "2"]), "zero-3x2": (3, 2, [])}
ALPHA_LABELS = ("zero", "safe-half", "safe-center", "sharp-boundary", "outside", "negative")
INCOMPATIBLE_SPECS = [
    ("tall-c", 3, 2, ["1", "3"], [("1/2", 2)], "C"),
    ("wide-d", 2, 3, ["1", "2"], [("1/2", 1), ("-1/3", 1)], "D"),
    ("square-c", 4, 4, ["1", "2"], [("-1/2", 2)], "C"),
    ("square-d", 4, 4, ["1", "2"], [("-1/2", 2)], "D"),
    ("square-e", 4, 4, ["1", "2"], [("-1/2", 2)], "E"),
    ("square-cde", 4, 4, ["1", "2"], [("-1/2", 2)], "CDE"),
]


def duplicate(items):
    out = {}
    for key, value in items:
        if key in out: raise ValueError(f"duplicate JSON key {key}")
        out[key] = value
    return out


def strict_json(path):
    value = json.loads(path.read_text(), object_pairs_hook=duplicate,
                       parse_constant=lambda x: (_ for _ in ()).throw(ValueError(f"nonfinite {x}")))
    if type(value) is not dict: raise TypeError("JSON root must be object")
    return value


class UniqueLoader(yaml.SafeLoader): pass
UniqueLoader.yaml_implicit_resolvers = {key: [(tag, regex) for tag, regex in values if tag != "tag:yaml.org,2002:timestamp"] for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()}


def unique_mapping(loader, node, deep=False):
    out = {}
    for knode, vnode in node.value:
        if knode.tag == "tag:yaml.org,2002:merge": raise ValueError("YAML merge forbidden")
        key = loader.construct_object(knode, deep=deep)
        if type(key) is not str or key in out: raise ValueError("duplicate/non-string YAML key")
        out[key] = loader.construct_object(vnode, deep=deep)
    return out


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)): raise ValueError("YAML anchors/aliases forbidden")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict: raise TypeError("YAML root must be mapping")
    return value


def digest(data):
    body = dict(data); body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def semantic_digest(data):
    """Canonical digest used to lock every parsed YAML value, independent of layout."""
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def sx(text): return sp.sympify(text, locals={"I": sp.I})
def ss(value): return sp.sstr(sp.simplify(value))


def matrix(rows, expected_rows=None, expected_cols=None):
    if type(rows) is not list or any(type(row) is not list for row in rows): raise TypeError("matrix schema")
    if expected_rows is not None and len(rows) != expected_rows: raise AssertionError("matrix row count")
    if rows:
        width = len(rows[0])
        if any(len(row) != width for row in rows): raise AssertionError("ragged matrix")
    else: width = expected_cols or 0
    if expected_cols is not None and width != expected_cols: raise AssertionError("matrix column count")
    return sp.Matrix([[sx(cell) for cell in row] for row in rows]) if rows else sp.zeros(expected_rows or 0, expected_cols or 0)


def canonical_jordan(blocks):
    built = []
    for text, size in blocks:
        block = sp.eye(size) * sx(text)
        for i in range(size-1): block[i, i+1] = 1
        built.append(block)
    return sp.diag(*built) if built else sp.zeros(0)


def canonical_similarity(n):
    transform = sp.eye(n)
    for i in range(n - 1): transform[i, i + 1] = i + 1
    if n > 2: transform[0, n - 1] = 1
    return transform


def expected_class(blocks):
    if not blocks: return sp.Integer(0), 0, "nilpotent", 1
    radii = [sp.sqrt(sp.simplify(sx(x)*sp.conjugate(sx(x)))) for x, _ in blocks]
    rho = max(radii, key=float)
    size = max(s for (_, s), r in zip(blocks, radii) if sp.simplify(r-rho)==0)
    if rho == 0: return rho, size, "finite-termination", max(s for _, s in blocks)
    if rho < 1: label = "convergent"
    elif rho == 1 and size == 1: label = "bounded-nonvanishing"
    elif rho == 1: label = "polynomially-unbounded"
    else: label = "double-exponential-divergence"
    return rho, size, label, None


def canonical_a(m, n, singulars):
    A = sp.zeros(m, n)
    for i, value in enumerate(singulars): A[i, i] = sx(value)
    return A


def projectors(m, n, rank):
    P, Q = sp.zeros(m), sp.zeros(n)
    for i in range(rank): P[i, i] = Q[i, i] = 1
    return P, Q


def compatible_x(m, n, singulars, blocks):
    rank=len(singulars); X=sp.zeros(n,m)
    if rank:
        sigma=sp.diag(*[sx(x) for x in singulars]); residual=canonical_jordan(blocks)
        X[:rank,:rank]=sp.simplify(sigma.inv()*(sp.eye(rank)-residual))
    return X


def leaf_count(value):
    if type(value) is dict: return sum(leaf_count(v) for v in value.values())
    if type(value) is list: return sum(leaf_count(v) for v in value)
    return 1


def main():
    if sys.flags.optimize: raise RuntimeError("C317 checker refuses optimized Python")
    parser = argparse.ArgumentParser(); parser.add_argument("--evidence", type=Path, default=DEFAULT); parser.add_argument("--evaluation", type=Path, default=EVALUATION); args = parser.parse_args()
    data = strict_json(args.evidence); evaluation = strict_yaml(args.evaluation); checks = 0
    if hashlib.sha256(args.evaluation.read_bytes()).hexdigest() != EXPECTED_EVALUATION_SHA256: raise AssertionError("evaluation byte contract mismatch")
    if semantic_digest(evaluation) != EXPECTED_EVALUATION_SEMANTIC_SHA256: raise AssertionError("evaluation semantic contract mismatch")
    if digest(data) != data.get("payload_sha256"): raise AssertionError("payload hash mismatch")
    checks += 1
    top = {"schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch", "source_commit", "scope_literal", "evaluator", "model", "theorem_contract", "square_cases", "compatible_rectangular_cases", "incompatible_rectangular_cases", "canonical_alpha_cases", "collision_boundary", "route_a", "scope_flags", "nonclaims", "references", "enumeration", "payload_sha256"}
    if set(data) != top: raise AssertionError("top-level schema")
    if (data["schema"], data["candidate_id"], data["obstruction_id"], data["evaluation_date"], data["fixed_epoch"], data["source_commit"], data["scope_literal"]) != ("hcs-c317-newton-schulz-full-basin-v1", "HCS-C317", "HEN-O301", "2026-09-03", 1788393600, SOURCE, SCOPE): raise AssertionError("identity/provenance")
    expected_model = {"dynamics": "X_{k+1}=X_k(2I-AX_k)", "square_residual": "R_k=I-AX_k", "singular_residual": "R_k=AA^dagger-AX_k on range(A)"}
    expected_theorem = {"square_basin": "X_k tends to A^{-1} iff rho(I-AX_0)<1", "jordan_rate": "Theta((2^k)^(s-1) rho^(2^k)) with finite nilpotent termination", "pseudoinverse_basin": "X_k tends to A^dagger iff X_0=QX_0P and the compressed residual has spectral radius below one", "canonical_corridor": "X_0=alpha A^* converges iff 0<alpha<2/sigma_max^2 for nonzero A", "boundary": "the sharp alpha endpoint deletes every maximal-singular-value direction; rank zero is separate"}
    if data["model"] != expected_model or data["theorem_contract"] != expected_theorem: raise AssertionError("model/theorem contract")
    expected_collision = {
        "C257": "scalar quadratic Newton--Cayley dynamics owns root basins and source zeta; C317 owns matrix inverse and Moore--Penrose basins",
        "C201": "heavy-ball owns second-order optimization recurrences; C317 owns residual powers and arbitrary nonnormal Jordan blocks",
        "C309": "matrix Riccati is a continuous symmetric flow; C317 is a discrete rectangular matrix iteration",
    }
    expected_nonclaims = [
        "Exact-arithmetic convergence is not a floating-point stability theorem.",
        "Residual squaring is source-local and is not an arithmetic primitive-orbit construction.",
        "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, zero match, or Hilbert--Polya operator is asserted.",
        "The package does not assert literature priority for Newton--Schulz or generalized-inverse iteration.",
    ]
    expected_references = [
        {"identifier": "10.1002/zamm.19330130111", "role": "original reciprocal-matrix iteration"},
        {"identifier": "10.1214/aoms/1177731489", "role": "Hotelling matrix-calculation lineage"},
        {"identifier": "10.1090/S0025-5718-1965-0179915-5", "role": "generalized-inverse iteration"},
    ]
    if data["evaluator"] != {"version": "0.2.0", "sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"} or data["collision_boundary"] != expected_collision or data["nonclaims"] != expected_nonclaims or data["references"] != expected_references: raise AssertionError("static evidence contract")
    checks += 15
    route = {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
    expected_flag_keys={"claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy","claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b"}
    if data["route_a"] != route or set(data["scope_flags"])!=expected_flag_keys or any(type(v) is not bool or v for v in data["scope_flags"].values()): raise AssertionError("scope/route")
    checks += 12
    eval_keys = {"schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256", "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters", "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention", "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed", "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens"}
    if set(evaluation) != eval_keys: raise AssertionError("evaluation schema")
    if (evaluation["schema"], evaluation["candidate_id"], evaluation["obstruction_id"], evaluation["source_commit"], evaluation["fixed_epoch"], evaluation["scope_literal"]) != ("route-a-evaluation-v0.2.0", "HCS-C317", "HEN-O301", SOURCE, 1788393600, SCOPE): raise AssertionError("evaluation provenance")
    if evaluation["tuple"] != route["tuple"] or evaluation["overall_verdict"] != "ROUTE_A_REJECTED" or evaluation["route_b_invocation_allowed"] is not False or evaluation["scope_flags"] != data["scope_flags"] or evaluation["theorem_status"] != "PROVABLE_AFTER_EXPLICIT_COMPATIBILITY_CONDITION": raise AssertionError("evaluation verdict/status")
    for key, verdict in zip(("a0","a1","a2","a3","a4"), route["tuple"]):
        if type(evaluation[key]) is not dict or evaluation[key].get("verdict") != verdict: raise AssertionError("evaluation branch")
    checks += 20
    if len(data["square_cases"]) != len(SQUARE_SPECS): raise AssertionError("square count")
    for row, (case_id, blocks) in zip(data["square_cases"], SQUARE_SPECS):
        keys = {"case_id", "dimension", "blocks", "a", "similarity", "initial_residual", "initial_x", "spectral_radius", "largest_peripheral_jordan_size", "regime", "nilpotency_index", "snapshots", "jordan_binomial_rows"}
        if set(row) != keys or row["case_id"] != case_id: raise AssertionError("square schema/id")
        n = sum(size for _, size in blocks)
        if row["dimension"] != n or row["blocks"] != [{"lambda": x, "size": s} for x,s in blocks]: raise AssertionError("square blocks")
        A = matrix(row["a"], n, n); T = matrix(row["similarity"], n, n); R0 = matrix(row["initial_residual"], n, n); X0 = matrix(row["initial_x"], n, n)
        expected_a=sp.diag(*range(1,n+1)); expected_t=canonical_similarity(n)
        if A != expected_a or T != expected_t or A.det() == 0 or T.det() == 0 or sp.simplify(T*canonical_jordan(blocks)*T.inv()-R0) != sp.zeros(n) or sp.simplify(sp.eye(n)-A*X0-R0) != sp.zeros(n): raise AssertionError("square construction")
        rho, size, label, nilindex = expected_class(blocks)
        if (sx(row["spectral_radius"]), row["largest_peripheral_jordan_size"], row["regime"], row["nilpotency_index"]) != (rho, size, label, nilindex): raise AssertionError("square classification")
        X = X0
        if len(row["snapshots"]) != 6: raise AssertionError("square snapshots")
        for k, snap in enumerate(row["snapshots"]):
            if set(snap) != {"k","dyadic_power","x","left_residual"} or (snap["k"],snap["dyadic_power"]) != (k,2**k): raise AssertionError("snapshot schema")
            gotx = matrix(snap["x"], n, n); gotr = matrix(snap["left_residual"], n, n)
            if gotx != X or sp.simplify(gotr-(sp.eye(n)-A*X)) != sp.zeros(n) or sp.simplify(gotr-R0**(2**k)) != sp.zeros(n) or sp.simplify(X-A.inv()*(sp.eye(n)-R0**(2**k))) != sp.zeros(n): raise AssertionError("square exact iterate")
            X = sp.simplify(X*(2*sp.eye(n)-A*X)); checks += 4*n*n
        expected_jrows = []
        for lam_text, block_size in blocks:
            lam = sx(lam_text)
            for k in range(6):
                power = 2**k
                expected_jrows.append({"lambda": lam_text, "size": block_size, "k": k, "power": power,
                    "coefficients": [ss(0 if j>power else sp.binomial(power,j)*lam**(power-j)) for j in range(block_size)]})
        if row["jordan_binomial_rows"] != expected_jrows: raise AssertionError("Jordan binomial ledger")
        checks += sum(len(x["coefficients"]) for x in expected_jrows) + 10
    if len(data["compatible_rectangular_cases"]) != len(RECT_SPECS): raise AssertionError("rect count")
    for row, (case_id,m,n,singulars,blocks) in zip(data["compatible_rectangular_cases"], RECT_SPECS):
        expected_rect_keys={"case_id","m","n","rank","singular_values","a","p_projector","q_projector","initial_x","compatibility_left","spectral_radius","largest_peripheral_jordan_size","regime","nilpotency_index","snapshots"}
        if set(row)!=expected_rect_keys: raise AssertionError("rect schema")
        if row["case_id"] != case_id or (row["m"],row["n"],row["rank"],row["singular_values"]) != (m,n,len(singulars),singulars): raise AssertionError("rect identity")
        rank=len(singulars); A=matrix(row["a"],m,n); P=matrix(row["p_projector"],m,m); Q=matrix(row["q_projector"],n,n); X0=matrix(row["initial_x"],n,m)
        eP,eQ=projectors(m,n,rank)
        if A != canonical_a(m,n,singulars) or P != eP or Q != eQ or sp.simplify(Q*X0*P-X0)!=sp.zeros(n,m) or matrix(row["compatibility_left"],n,m)!=sp.zeros(n,m): raise AssertionError("rect compatibility")
        expected_x=compatible_x(m,n,singulars,blocks)
        if X0 != expected_x: raise AssertionError("rect frozen initial condition")
        R0=sp.simplify(P-A*X0); X=X0; pinv=A.pinv()
        canonical_residual=sp.zeros(m)
        if rank: canonical_residual[:rank,:rank]=canonical_jordan(blocks)
        if R0 != canonical_residual: raise AssertionError("rect frozen residual")
        if len(row["snapshots"]) != 6: raise AssertionError("rect snapshot count")
        for k,snap in enumerate(row["snapshots"]):
            if set(snap)!={"k","dyadic_power","x","compressed_residual"} or (snap["k"],snap["dyadic_power"])!=(k,2**k): raise AssertionError("rect snapshot schema")
            gotx=matrix(snap["x"],n,m); gotr=matrix(snap["compressed_residual"],m,m)
            if gotx!=X or sp.simplify(gotr-(P-A*X))!=sp.zeros(m) or sp.simplify(gotr-R0**(2**k))!=sp.zeros(m) or sp.simplify(X-(pinv-pinv*R0**(2**k)))!=sp.zeros(n,m): raise AssertionError("rect exact iterate")
            X=sp.simplify(X*(2*sp.eye(m)-A*X)); checks += 3*m*m+n*m
        rho,size,label,nilindex=expected_class(blocks)
        if (sx(row["spectral_radius"]),row["largest_peripheral_jordan_size"],row["regime"],row["nilpotency_index"])!=(rho,size,label,nilindex): raise AssertionError("rect classification")
        checks += 12
    if len(data["incompatible_rectangular_cases"]) != len(INCOMPATIBLE_SPECS): raise AssertionError("incompatible count")
    for row,(case_id,m,n,singulars,blocks,kind) in zip(data["incompatible_rectangular_cases"],INCOMPATIBLE_SPECS):
        if set(row)!={"case_id","m","n","rank","off_support_kind","a","p_projector","q_projector","initial_x","compatibility_violation","snapshots","converges_to_moore_penrose"}: raise AssertionError("incompatible schema")
        rank=len(singulars)
        if (row["case_id"],row["m"],row["n"],row["rank"],row["off_support_kind"])!=(case_id,m,n,rank,kind): raise AssertionError("incompatible identity")
        A=matrix(row["a"],m,n);P=matrix(row["p_projector"],m,m);Q=matrix(row["q_projector"],n,n);X=matrix(row["initial_x"],n,m)
        eP,eQ=projectors(m,n,rank); expected_x=compatible_x(m,n,singulars,blocks)
        if "C" in kind: expected_x[0,rank]=1
        if "D" in kind: expected_x[rank,0]=1
        if "E" in kind: expected_x[rank,rank]=1
        if A!=canonical_a(m,n,singulars) or P!=eP or Q!=eQ or X!=expected_x: raise AssertionError("incompatible construction")
        violation=matrix(row["compatibility_violation"],n,m)
        if sp.simplify(violation-(Q*X*P-X))!=sp.zeros(n,m) or violation==sp.zeros(n,m) or row["converges_to_moore_penrose"] is not False: raise AssertionError("incompatible witness")
        if len(row["snapshots"]) != 5: raise AssertionError("incompatible snapshot count")
        for k,snap in enumerate(row["snapshots"]):
            if set(snap)!={"k","dyadic_power","x","compressed_residual"} or (snap["k"],snap["dyadic_power"])!=(k,2**k): raise AssertionError("incompatible snapshot schema")
            gotx=matrix(snap["x"],n,m); gotr=matrix(snap["compressed_residual"],m,m)
            if gotx!=X or sp.simplify(gotr-(P-A*X))!=sp.zeros(m): raise AssertionError("incompatible iterate")
            X=sp.simplify(X*(2*sp.eye(m)-A*X)); checks += m*m+n*m
        checks += 5
    expected_alpha_ids=[f"{base}-{label}" for base in ("full-2","rank2-4x3","repeated-max-4") for label in ALPHA_LABELS]+["zero-3x2-arbitrary-zero"]
    if [row.get("case_id") if type(row) is dict else None for row in data["canonical_alpha_cases"]] != expected_alpha_ids:
        raise AssertionError("canonical alpha frozen ledger")
    for row in data["canonical_alpha_cases"]:
        if set(row)!={"case_id","m","n","rank","singular_values","alpha","classification","initial_x","directions"}: raise AssertionError("alpha schema")
        # Resolve the four frozen base names without relying on substring accidents.
        found=None
        for candidate in ALPHA_BASE:
            prefix=candidate+"-"
            if row["case_id"].startswith(prefix): found=candidate; label=row["case_id"][len(prefix):]; break
        if found is None: raise AssertionError("alpha case id")
        m,n,singulars=ALPHA_BASE[found]; rank=len(singulars); alpha=sx(row["alpha"]); A=canonical_a(m,n,singulars)
        if rank == 0:
            expected_alpha=sp.Rational(7,3)
        else:
            smax=max(sx(x) for x in singulars); scale=smax**2
            expected_alpha={"zero":sp.Integer(0),"safe-half":sp.Rational(1,2)/scale,
                "safe-center":1/scale,"sharp-boundary":2/scale,
                "outside":3/scale,"negative":-1/scale}[label]
        if sp.simplify(alpha-expected_alpha)!=0: raise AssertionError("canonical alpha frozen value")
        if (row["m"],row["n"],row["rank"],row["singular_values"])!=(m,n,rank,singulars) or matrix(row["initial_x"],n,m)!=sp.simplify(alpha*A.conjugate().T): raise AssertionError("alpha construction")
        if len(row["directions"])!=rank: raise AssertionError("alpha directions")
        for cell,sigma_text in zip(row["directions"],singulars):
            if set(cell)!={"sigma","initial_residual","predicted_limit","iterate_coefficients"}: raise AssertionError("alpha direction schema")
            sigma=sx(sigma_text); residual=sp.simplify(1-alpha*sigma**2)
            expected_coeff=[ss((1-residual**(2**k))/sigma) for k in range(6)]
            if cell["sigma"]!=sigma_text or sx(cell["initial_residual"])!=residual or cell["iterate_coefficients"]!=expected_coeff: raise AssertionError("alpha scalar formula")
            if abs(float(residual))<1: expected_limit=ss(1/sigma)
            elif label=="sharp-boundary" and residual==-1: expected_limit="0"
            else: expected_limit=None
            if cell["predicted_limit"]!=expected_limit: raise AssertionError("alpha limit")
            checks += 10
        expected_label="rank-zero-canonical-zero" if rank==0 else "converges-pseudoinverse" if label in ("safe-half","safe-center") else "spectral-truncation-boundary" if label=="sharp-boundary" else "zero-fixed" if label=="zero" else "divergent"
        if row["classification"]!=expected_label: raise AssertionError("alpha classification")
        if label=="sharp-boundary":
            smax=max(sx(x) for x in singulars)
            for cell in row["directions"]:
                if sx(cell["sigma"])==smax and cell["predicted_limit"]!="0": raise AssertionError("maximal singular direction not deleted")
        checks += 7
    enum=data["enumeration"]
    if set(enum)!={"square_case_count","square_snapshot_count","jordan_binomial_row_count","compatible_rectangular_case_count","compatible_snapshot_count","incompatible_case_count","incompatible_snapshot_count","canonical_alpha_case_count","canonical_direction_count","audited_leaf_count"}: raise AssertionError("enumeration schema")
    if enum["square_case_count"]!=14 or enum["square_snapshot_count"]!=84 or enum["compatible_rectangular_case_count"]!=6 or enum["compatible_snapshot_count"]!=36 or enum["incompatible_case_count"]!=6 or enum["incompatible_snapshot_count"]!=30 or enum["canonical_alpha_case_count"]!=19: raise AssertionError("enumeration counts")
    if (enum["jordan_binomial_row_count"]!=sum(len(x["jordan_binomial_rows"]) for x in data["square_cases"])
        or enum["compatible_snapshot_count"]!=sum(len(x["snapshots"]) for x in data["compatible_rectangular_cases"])
        or enum["incompatible_snapshot_count"]!=sum(len(x["snapshots"]) for x in data["incompatible_rectangular_cases"])
        or enum["canonical_direction_count"]!=sum(len(x["directions"]) for x in data["canonical_alpha_cases"])): raise AssertionError("derived enumeration")
    body=dict(data);body.pop("payload_sha256")
    if enum["audited_leaf_count"]!=leaf_count(body): raise AssertionError("leaf count")
    checks += 12
    print(f"C317 independent checker: PASS ({checks} checks)")


if __name__ == "__main__": main()
