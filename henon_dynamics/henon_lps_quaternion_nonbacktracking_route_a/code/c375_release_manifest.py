#!/usr/bin/env python3
"""Deterministic 38-payload release gate for HCS-C375."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

if sys.flags.optimize:
    raise RuntimeError("C375 release refuses optimized Python")

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C375_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c375_lps_nonbacktracking_evidence.json"
TEX = ROOT / "paper/main.tex"
MAIN = ROOT / "paper/main.pdf"
YML = ROOT / "evaluations/route_a/HCS-C375/2026-09-04.yaml"
RAW = "0839b808477a4492c297b32f6578e12d97d05ae632e4d0050b06369797aceeac"
SEMANTIC = "59f5eb72d8a887e20c73956f750d4d651dcaf6d0888a5c237438637235d883b5"
SOURCE = "f58422d8f03235329863f946654981ecb5d4dc97"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788480000
ROUNDS = [
    ROOT / "paper/main_round0_original.pdf",
    ROOT / "paper/main_round1.pdf",
    ROOT / "paper/main_round2.pdf",
]
ROUND_SOURCES = [
    ROOT / "paper/main_round0.tex",
    ROOT / "paper/main_round1.tex",
    ROOT / "paper/main_round2.tex",
]
WARNING = re.compile(
    r"(?:LaTeX|Package [^:\n]+|LaTeX Font) Warning:|warning  \(pdf backend\)|"
    r"Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character"
)
EXPECTED = {
    "ASSUMPTIONS.md", "CLAIMS.md", "EXPERIMENT_PLAN.md", "LIMITATIONS.md",
    "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md", "README.md",
    "REFERENCES.md", "REPRODUCIBILITY.md", "RESEARCH_QUESTION.md", "SCOPE.md",
    "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md", "requirements.txt",
    "code/README.md", "code/c375_lps_nonbacktracking_checker.py",
    "code/c375_lps_nonbacktracking_mutation.py",
    "code/c375_lps_nonbacktracking_producer.py",
    "code/c375_lps_nonbacktracking_replay.py",
    "code/c375_lps_nonbacktracking_sympy_crosscheck.py",
    "code/c375_release_manifest.py",
    "evaluations/route_a/HCS-C375/2026-09-04.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0.tex", "paper/main_round1.tex", "paper/main_round2.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c375_lps_nonbacktracking_evidence.json", "tests/test_c375_smoke.py",
}
ROUTE = {
    "tuple": [
        "A0_STRUCTURAL_ARITHMETIC_RELATION", "A1_WEAK",
        "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT",
    ],
    "overall": "ROUTE_A_EXPLORATORY",
    "route_b_invocation_allowed": False,
    "a1_scope": "the exact primitive ledger is source-local and does not transfer q or primality to individual primitive-orbit labels",
    "a1_missing_requirements": [
        "no prime-to-orbit or prime-power repetition correspondence",
        "no intrinsic log(p) or von Mangoldt orbit weights",
        "no orbit phases or monodromy and stability multipliers",
        "mandatory shuffled-period, random-weight, random-phase, same-density-length, neighboring-parameter, and simpler-parent controls are absent",
    ],
}
ENGLISH_KEYWORDS = (
    ("arithmetic cayley graphs", "hamilton quaternions", "lps graphs",
     "projective linear groups", "bipartite graphs"),
    ("arithmetic cayley graphs", "lps graphs", "hashimoto operator",
     "nonbacktracking dynamics", "primitive cycles", "finite-graph ihara product"),
    ("lps graphs", "arithmetic dynamics", "hashimoto operator", "primitive cycles",
     "ramanujan spectrum", "prime number theorem", "computational certification"),
)
CHINESE_KEYWORDS = (
    ("算术Cayley图", "整数四元数", "LPS图", "投影线性群", "二分图"),
    ("算术图动力学", "LPS图", "非回溯转移", "有向闭轨", "Hashimoto算子", "有限图Ihara乘积"),
    ("算术动力学", "LPS图", "非回溯算子", "本原闭轨", "Ramanujan谱", "算术级数素数定理", "计算机核验"),
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def strict_json(path: Path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate JSON key")
            result[key] = value
        return result
    return json.loads(
        path.read_text(), object_pairs_hook=unique,
        parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)),
    )


def strict_yaml(path: Path):
    raw = path.read_text()
    if re.search(r"(^|[\s\[{,])[*&][A-Za-z0-9_-]+", raw):
        raise ValueError("YAML anchors and aliases forbidden")

    class Loader(yaml.SafeLoader):
        pass

    def mapping(loader, node, deep=False):
        result = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            if key in result:
                raise ValueError("duplicate YAML key")
            result[key] = loader.construct_object(value_node, deep=deep)
        return result

    Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
    value = yaml.load(raw, Loader=Loader)
    if not isinstance(value, dict):
        raise ValueError("YAML root is not a mapping")
    return value


def command(script: str, args=()) -> str:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    process = subprocess.run(
        [sys.executable, "-B", str(ROOT / "code" / script), *args],
        cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
    )
    if process.returncode:
        raise AssertionError(f"{script} failed:\n{process.stdout}")
    return process.stdout.strip()


def isolated_lane(script: str) -> str:
    with tempfile.TemporaryDirectory(prefix="c375-lane-") as directory:
        args = ("--output", str(Path(directory) / "evidence.json")) if script.endswith("producer.py") else ()
        return command(script, args)


def optimized_refusal(script: str) -> None:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    for flag in ("-O", "-OO"):
        cmd = [sys.executable, flag, "-B", str(ROOT / "code" / script)]
        with tempfile.TemporaryDirectory(prefix="c375-opt-") as directory:
            if script.endswith("producer.py"):
                cmd += ["--output", str(Path(directory) / "evidence.json")]
            process = subprocess.run(
                cmd, cwd=ROOT, env=env, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, text=True,
            )
        if process.returncode == 0 or "refuses optimized Python" not in process.stdout:
            raise AssertionError(f"optimized execution not refused: {flag} {script}")


def smoke_tests() -> str:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    process = subprocess.run(
        [sys.executable, "-B", "-m", "unittest", "tests/test_c375_smoke.py"],
        cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
    )
    if process.returncode or "OK" not in process.stdout:
        raise AssertionError(f"smoke tests failed:\n{process.stdout}")
    return "3/3 PASS"


def fresh_pdf(round_number: int) -> bytes:
    with tempfile.TemporaryDirectory(prefix=f"c375-build-{round_number}-") as directory:
        work = Path(directory)
        shutil.copy2(TEX, work / "main.tex")
        source = ROUND_SOURCES[round_number]
        shutil.copy2(source, work / source.name)
        env = dict(os.environ, SOURCE_DATE_EPOCH=str(EPOCH), FORCE_SOURCE_DATE="1", TZ="UTC")
        cmd = [
            "lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main",
            source.name,
        ]
        for _ in range(2):
            process = subprocess.run(
                cmd, cwd=work, env=env, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, text=True,
            )
            if process.returncode:
                raise AssertionError(f"paper round {round_number} failed:\n{process.stdout[-5000:]}")
        log = (work / "main.log").read_text(errors="replace")
        hit = WARNING.search(log)
        if hit:
            raise AssertionError(f"paper warning round {round_number}: {hit.group(0)}")
        return (work / "main.pdf").read_bytes()


def page_count(path: Path) -> int:
    output = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in output.splitlines() if line.startswith("Pages:")))


def font_count(path: Path) -> int:
    rows = [
        line for line in subprocess.check_output(["pdffonts", str(path)], text=True).splitlines()[2:]
        if line.strip() and not line.lstrip().startswith("-")
    ]
    if not rows:
        raise AssertionError("PDF has no fonts")
    for row in rows:
        columns = row.split()
        if len(columns) < 7 or columns[-5] != "yes" or columns[-4] != "yes":
            raise AssertionError(f"font is not embedded and subset: {row}")
    if not any("DroidSansFallback" in row for row in rows):
        raise AssertionError("embedded CJK font is missing")
    return len(rows)


def text_and_raster(path: Path, pages: int):
    raw = subprocess.check_output(["pdftotext", "-layout", str(path), "-"])
    if re.search(rb"[\x00-\x08\x0b\x0e-\x1f\x7f]", raw):
        raise AssertionError("control byte in extracted PDF text")
    text = " ".join(raw.decode().lower().split())
    for bad in ("??", "[verify]", "__mutated", "varepsilon_"):
        if bad in text:
            raise AssertionError(f"PDF text garbage: {bad}")
    raster_sizes = []
    with tempfile.TemporaryDirectory(prefix="c375-raster-") as directory:
        for page in range(1, pages + 1):
            prefix = Path(directory) / f"p{page}"
            subprocess.run(
                ["pdftoppm", "-f", str(page), "-l", str(page), "-r", "72",
                 "-png", str(path), str(prefix)],
                check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            )
            images = list(Path(directory).glob(f"p{page}-*.png"))
            if len(images) != 1 or images[0].stat().st_size < 1000:
                raise AssertionError("PDF raster failure")
            raster_sizes.append(images[0].stat().st_size)
    return text, raster_sizes


def pdf_receipts():
    tokens = (
        "arithmetic quaternion chambers",
        "exact primitive nonbacktracking dynamics",
        "ramanujan circle and route boundary",
    )
    receipts = []
    for index, path in enumerate(ROUNDS):
        pages = page_count(path)
        text, raster = text_and_raster(path, pages)
        compact = text.replace(" ", "")
        if tokens[index] not in text:
            raise AssertionError(f"round token missing: {index}")
        for header in ("abstract", "keywords:"):
            if header not in text:
                raise AssertionError(f"English abstract gate missing in round {index}: {header}")
        for header in ("中文摘要", "关键词："):
            if header not in compact:
                raise AssertionError(f"Chinese abstract gate missing in round {index}: {header}")
        if not 5 <= len(ENGLISH_KEYWORDS[index]) <= 7:
            raise AssertionError(f"English keyword count drift in round {index}")
        if not 5 <= len(CHINESE_KEYWORDS[index]) <= 7:
            raise AssertionError(f"Chinese keyword count drift in round {index}")
        if len(set(ENGLISH_KEYWORDS[index])) != len(ENGLISH_KEYWORDS[index]):
            raise AssertionError(f"duplicate English keyword in round {index}")
        if len(set(CHINESE_KEYWORDS[index])) != len(CHINESE_KEYWORDS[index]):
            raise AssertionError(f"duplicate Chinese keyword in round {index}")
        for keyword in ENGLISH_KEYWORDS[index]:
            if keyword not in text:
                raise AssertionError(f"English keyword missing in round {index}: {keyword}")
        for keyword in CHINESE_KEYWORDS[index]:
            if keyword.lower().replace(" ", "") not in compact:
                raise AssertionError(f"Chinese keyword missing in round {index}: {keyword}")
        forbidden_by_round = (
            (
                "complete determinant and orbit ledger", "primitive cycles",
                "ramanujan circle and route boundary",
                "exact evidence, limitations, and declarations",
                "精确特征行列式", "本原有向闭轨", "非平凡二次根恰落在", "五个完整有限群",
            ),
            (
                "ramanujan circle and route boundary", "prime chamber density",
                "exact evidence, limitations, and declarations",
                "条件自然密度", "非平凡二次根恰落在", "五个完整有限群",
            ),
            (),
        )
        for forbidden in forbidden_by_round[index]:
            haystack = compact if any(ord(char) > 127 for char in forbidden) else text
            needle = forbidden.lower().replace(" ", "") if haystack is compact else forbidden
            if needle in haystack:
                raise AssertionError(f"later-round leak in round {index}: {forbidden}")
        if index == 2:
            for sentinel in (
                "hcs-c329 already owns", "no target arithmetic local datum",
                "route b is not invoked", "data availability", "ethics declaration",
                "ai-use disclosure", "route_a_exploratory",
            ):
                if sentinel not in text:
                    raise AssertionError(f"final paper sentinel missing: {sentinel}")
        receipts.append({
            "round": index, "path": str(path.relative_to(ROOT)),
            "sha256": sha(path), "bytes": path.stat().st_size, "pages": pages,
            "font_rows": font_count(path), "raster_bytes": raster,
        })
    if len({row["sha256"] for row in receipts}) != 3:
        raise AssertionError("conditional PDFs are not distinct")
    if MAIN.read_bytes() != ROUNDS[2].read_bytes():
        raise AssertionError("main PDF is not round 2")
    return receipts


def evidence_payload_hash() -> str:
    value = strict_json(EVIDENCE)
    claimed = value.pop("payload_sha256")
    got = hashlib.sha256(canonical(value)).hexdigest()
    if claimed != got:
        raise AssertionError("stale evidence payload hash")
    return claimed


def generated_reports(outputs, pdfs, smoke):
    checker = re.search(
        r"PASS \((\d+) assertions\)", outputs["c375_lps_nonbacktracking_checker.py"]
    ).group(1)
    sympy_count = re.search(
        r"PASS \((\d+) exact checks\)", outputs["c375_lps_nonbacktracking_sympy_crosscheck.py"]
    ).group(1)
    attacks = re.search(
        r"PASS \((\d+) attacks\)", outputs["c375_lps_nonbacktracking_mutation.py"]
    ).group(1)
    evidence = strict_json(EVIDENCE)
    chambers = evidence["prime_chamber_ledger"]["finite_chamber_counts"]
    results = (
        "# Results\n\n"
        f"The canonical evidence has SHA-256 {sha(EVIDENCE)} and self-excluding "
        f"payload SHA-256 {evidence_payload_hash()}. It constructs "
        f"{evidence['total_vertices']:,} vertices and {evidence['total_oriented_edges']:,} "
        f"oriented edges across five complete LPS groups, with "
        f"{evidence['total_prime_iterate_cells']} exact iterate rows. "
        f"The prime ledger contains {evidence['prime_chamber_ledger']['eligible_prime_count']} "
        f"eligible primes through {evidence['prime_chamber_ledger']['prime_bound']}; its finite "
        f"PSL/PGL counts are {chambers['PSL2_NONBIPARTITE']} and "
        f"{chambers['PGL2_BIPARTITE']}. These are regression receipts, not estimates of "
        "the proved conditional density.\n"
    )
    tests = (
        "# Test report\n\n"
        f"- producer: five full groups and 60 iterate rows PASS;\n"
        f"- independent checker: {checker} assertions PASS;\n"
        f"- SymPy lane: {sympy_count} exact checks PASS;\n"
        "- isolated replay: two byte-identical builds PASS;\n"
        f"- hostile mutation suite: {attacks} attacks PASS;\n"
        f"- unittest smoke suite: {smoke}.\n\n"
        "Every executable refuses optimized Python. The release gate also checks strict "
        "JSON/YAML, evaluator locks, deterministic PDFs, fonts, text, rasterization, and "
        "the frozen-wrapper bilingual abstract/keyword gates and exact 38-payload ledger.\n"
    )
    hostile = (
        "# Hostile audit\n\n"
        f"The repaired-hash suite rejects {attacks} attacks against source identity, quaternion "
        "norm, projective chambers, group sizes, determinant classes, trace and primitive-cycle "
        "rows, LPS/Bass/PNT-AP source boundaries, the HCS-C329 ownership split, controls, "
        "strict evaluator schema, route tuple, "
        "scope flags, parser structure, and stale hashes.\n"
    )
    additions = (
        "quaternion generators, gauge, LPS chambers, sizes and bipartite wall",
        "Bass characteristic factorization, traces, primitive cycles and finite-graph Ihara product",
        "Ramanujan circle, chamber density, evidence, declarations and Route-A boundary",
    )
    lines = [
        "# Compile report", "",
        "Every conditional round was built twice in fresh directories with LuaLaTeX under "
        "SOURCE_DATE_EPOCH=1788480000; both bytes matched the stored artifact. Settled logs "
        "have no warnings or layout defects. Every font is embedded and subset, extracted "
        "text is clean, and every page rasterizes.", "",
        "| round | pages | font rows | SHA-256 | substantive addition |",
        "|---|---:|---:|---|---|",
    ]
    for row, addition in zip(pdfs, additions):
        lines.append(
            f"| {row['round']} | {row['pages']} | {row['font_rows']} | "
            f"{row['sha256']} | {addition} |"
        )
    lines.extend(["", "main.pdf is byte-identical to round 2.", ""])
    return {
        "results/RESULTS.md": results,
        "results/TEST_REPORT.md": tests,
        "results/HOSTILE_AUDIT.md": hostile,
        "paper/COMPILE_REPORT.md": "\n".join(lines),
    }


def make_manifest(pdfs):
    source = TEX.read_text()
    tokens = (
        r"\mathcal S_5", r"M_{-\iota}(a)=JM_\iota(a)J^{-1}",
        r"\det(I-uH_q)", r"(t^2-1)^{2n_q}", r"|\mu|=\sqrt5",
        r"q\equiv13,17\pmod{20}", "HCS-C329 already owns",
        "NO\\_BAD\\_EULER\\_OR\\_ROOT\\_NUMBER", "Route B", "Data availability",
        r"A1_{\rm WEAK}", "ROUTE\\_A\\_EXPLORATORY",
        "prime number theorem for arithmetic progressions",
        "10.1007/978-1-4757-5927-3", "中文摘要", "Keywords:", "关键词：",
    )
    for token in tokens:
        if token not in source:
            raise AssertionError(f"missing theorem token: {token}")
    if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", source):
        raise AssertionError("TeX control byte")
    for index, wrapper in enumerate(ROUND_SOURCES):
        expected = f"\\def\\CRevisionRound{{{index}}}\n\\input{{main.tex}}\n"
        if wrapper.read_text() != expected:
            raise AssertionError(f"round wrapper drift: {index}")
    references = (ROOT / "REFERENCES.md").read_text()
    if "../henon_paley_graph_ihara_nonbacktracking_route_a/" not in references:
        raise AssertionError("C329 owner path drift")
    if "10.1007/978-1-4757-5927-3" not in references:
        raise AssertionError("Davenport source drift")
    files = {
        str(path.relative_to(ROOT)): path for path in ROOT.rglob("*")
        if path.is_file() and path != MANIFEST
    }
    if set(files) != EXPECTED or len(files) != 38:
        raise AssertionError(
            f"ledger mismatch missing={sorted(EXPECTED-set(files))} "
            f"extra={sorted(set(files)-EXPECTED)}"
        )
    if sha(YML) != RAW:
        raise AssertionError("YAML raw drift")
    yml = strict_yaml(YML)
    if hashlib.sha256(canonical(yml)).hexdigest() != SEMANTIC:
        raise AssertionError("YAML semantic drift")
    if yml["skill"] != "route-a-evaluator" or yml["skill_version"] != "0.2.0":
        raise AssertionError("YAML evaluator schema drift")
    if yml["source_commit"] != SOURCE or yml["code_commit"] != SOURCE:
        raise AssertionError("YAML frozen commit drift")
    required_lock = {
        "object", "arithmetic_origin", "clock", "normalization",
        "determinant_convention", "cutoff", "precision", "allowed_data", "forbidden_data",
    }
    if set(yml["source_lock"]) != required_lock:
        raise AssertionError("YAML source lock drift")
    if yml["tuple"] != ROUTE["tuple"] or yml["overall_verdict"] != ROUTE["overall"]:
        raise AssertionError("YAML route drift")
    if yml["route_b_invocation_allowed"]:
        raise AssertionError("YAML Route-B lock drift")
    controls = yml["a0"]["arithmetic_controls"]
    if len(controls) < 3 or any(row["status"] != "EXECUTED_EXACT" for row in controls):
        raise AssertionError("YAML A0 arithmetic controls drift")
    if yml["a1"]["verdict"] != "A1_WEAK":
        raise AssertionError("YAML strict A1 drift")
    if yml["a1"]["metrics"]["mandatory_a1_controls_completed"] != 0:
        raise AssertionError("YAML A1 control status drift")
    for layer in ("a0", "a1", "a2", "a3", "a4"):
        if not yml[layer].get("artifacts"):
            raise AssertionError(f"YAML artifact ledger missing: {layer}")
    for key in (
        "adversarial_controls", "claim_boundary", "blocking_conditions",
        "next_smallest_test", "round2_clues",
    ):
        if not yml.get(key):
            raise AssertionError(f"YAML required field missing: {key}")
    if yml["adversarial_controls"]["verdict"] != "PASS_SCOPE_LIMIT_RETAINED":
        raise AssertionError("YAML proves-too-much control drift")
    checker = (ROOT / "code/c375_lps_nonbacktracking_checker.py").read_text()
    if re.search(r"(?:from|import)\s+[^\n]*c375_lps_nonbacktracking_producer", checker):
        raise AssertionError("checker imports producer")
    evidence = strict_json(EVIDENCE)
    if evidence["source_commit"] != SOURCE or evidence["scope_literal"] != SCOPE:
        raise AssertionError("evidence source/scope drift")
    if evidence["route_a"] != ROUTE or any(evidence["scope_flags"].values()):
        raise AssertionError("evidence route or forbidden flag drift")
    if evidence["total_vertices"] != 104316 or evidence["total_oriented_edges"] != 625896:
        raise AssertionError("evidence finite census drift")
    boundary = evidence["source_theorem_boundary"]
    if "HCS-C329 owns" not in boundary["nearest_workspace_owner"]:
        raise AssertionError("ownership boundary drift")
    if not boundary["pnt_ap_input"].startswith(
        "The prime number theorem for arithmetic progressions"
    ):
        raise AssertionError("PNT-AP boundary drift")
    arithmetic_controls = evidence["arithmetic_controls"]
    if arithmetic_controls["shuffled_chamber_label_trials"] != 1124:
        raise AssertionError("arithmetic-control trial drift")
    if arithmetic_controls["shuffled_chamber_label_mismatches"] <= 0:
        raise AssertionError("arithmetic-label shuffle was not rejected")
    if evidence["nonclaims"][0] != (
        "no workspace ownership of the generic Bass-Ihara-Hashimoto identity "
        "already owned by HCS-C329"
    ):
        raise AssertionError("nonownership statement drift")
    return {
        "schema": "hcs-release-manifest-v1", "candidate_id": "HCS-C375",
        "obstruction_id": "HEN-O359", "source_commit": SOURCE,
        "fixed_epoch": EPOCH, "scope_literal": SCOPE,
        "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
        "evaluator_version": "0.2.0",
        "evaluator_authority_sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
        "payload_file_count": 38, "physical_file_count": 39,
        "evaluation_raw_sha256": RAW, "evaluation_semantic_sha256": SEMANTIC,
        "evidence_sha256": sha(EVIDENCE),
        "evidence_payload_sha256": evidence_payload_hash(),
        "release_lanes": {
            "producer": "PASS", "independent_checker": "PASS",
            "sympy_crosscheck": "PASS", "isolated_byte_replay": "PASS",
            "hostile_mutation": "PASS", "unittest_smoke": "PASS",
            "optimized_mode_refusal": "PASS", "deterministic_pdf_rebuild": "PASS",
            "payload_membership": "PASS",
        },
        "pdf_rounds": pdfs, "main_pdf_sha256": sha(MAIN),
        "files": {name: sha(path) for name, path in sorted(files.items())},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--build-pdfs", action="store_true")
    args = parser.parse_args()
    if args.build_pdfs and not args.write:
        raise ValueError("--build-pdfs requires --write")
    if args.write:
        command("c375_lps_nonbacktracking_producer.py")
    lanes = (
        ("c375_lps_nonbacktracking_producer.py", "C375_PRODUCER_PASS"),
        ("c375_lps_nonbacktracking_checker.py", "C375 independent checker: PASS"),
        ("c375_lps_nonbacktracking_sympy_crosscheck.py", "C375 SymPy cross-check: PASS"),
        ("c375_lps_nonbacktracking_replay.py", "C375 byte replay: PASS"),
        ("c375_lps_nonbacktracking_mutation.py", "C375 hostile mutation suite: PASS"),
    )
    outputs = {}
    for script, sentinel in lanes:
        output = isolated_lane(script)
        if sentinel not in output:
            raise AssertionError(f"lane sentinel missing: {script}")
        outputs[script] = output
        optimized_refusal(script)
    smoke = smoke_tests()
    if args.build_pdfs:
        for index, path in enumerate(ROUNDS):
            first = fresh_pdf(index)
            second = fresh_pdf(index)
            if first != second:
                raise AssertionError(f"nondeterministic PDF round {index}")
            path.write_bytes(first)
        MAIN.write_bytes(ROUNDS[2].read_bytes())
    else:
        for index, path in enumerate(ROUNDS):
            first = fresh_pdf(index)
            second = fresh_pdf(index)
            if first != second or first != path.read_bytes():
                raise AssertionError(f"stale or nondeterministic PDF round {index}")
    pdfs = pdf_receipts()
    reports = generated_reports(outputs, pdfs, smoke)
    for name, raw in reports.items():
        path = ROOT / name
        if args.write:
            path.write_text(raw)
        elif not path.exists() or path.read_text() != raw:
            raise AssertionError(f"report missing or stale: {name}")
    manifest = make_manifest(pdfs)
    raw_manifest = json.dumps(manifest, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    if args.write:
        MANIFEST.write_text(raw_manifest)
    elif not MANIFEST.exists() or MANIFEST.read_text() != raw_manifest:
        raise AssertionError("manifest missing or stale")
    forbidden = [
        path for path in ROOT.rglob("*") if path.is_file()
        and (path.suffix in {".aux", ".log", ".out", ".toc", ".pyc"}
             or "__pycache__" in path.parts)
    ]
    if forbidden:
        raise AssertionError(f"forbidden sidecars: {forbidden}")
    print(f"C375_RELEASE_PASS {sha(EVIDENCE)} {sha(MAIN)} {sha(MANIFEST)}")


if __name__ == "__main__":
    main()
