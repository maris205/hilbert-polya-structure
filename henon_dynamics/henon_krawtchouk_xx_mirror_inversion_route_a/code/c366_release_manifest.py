#!/usr/bin/env python3
"""Release gate and self-excluding manifest for HCS-C366."""
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

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C366_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c366_krawtchouk_xx_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C366/2026-09-04.yaml"
TEX = ROOT / "paper/main.tex"
MAIN_PDF = ROOT / "paper/main.pdf"
SOURCE = "323ea43f6970544467f8a89f0ed9be0c7c39f896"
EPOCH = 1788480000
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVAL_RAW = "acc72ba628087e67f52927031ca66ee1798cc8073907133cf7049df49f04cc59"
EVAL_SEMANTIC = "a2ab8e3e0d4256ea4058300f66fecac5f6fec5283f9ad80432b21e28b0648ef5"
ROUND_PDFS = [ROOT / "paper/main_round0_original.pdf",
              ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md", "code/README.md",
    "code/c366_krawtchouk_xx_checker.py", "code/c366_krawtchouk_xx_mutation.py",
    "code/c366_krawtchouk_xx_producer.py", "code/c366_krawtchouk_xx_replay.py",
    "code/c366_krawtchouk_xx_sympy_crosscheck.py", "code/c366_release_manifest.py",
    "evaluations/route_a/HCS-C366/2026-09-04.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c366_krawtchouk_xx_evidence.json",
}
WARNING = re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|warning  \(pdf backend\)|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def strict_json(path: Path) -> dict:
    def unique(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate JSON key {key}")
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=unique,
                      parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))


class StrictLoader(yaml.SafeLoader):
    pass


StrictLoader.yaml_implicit_resolvers = {
    key: [(tag, regex) for tag, regex in values
          if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def strict_mapping(loader, node, deep=False):
    output = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge key forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in output:
            raise ValueError("duplicate or non-string YAML key")
        output[key] = loader.construct_object(value_node, deep=deep)
    return output


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def strict_yaml() -> tuple[dict, str]:
    raw = EVALUATION.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise AssertionError("YAML anchors and aliases are forbidden")
    data = yaml.load(raw, Loader=StrictLoader)
    if type(data) is not dict:
        raise AssertionError("YAML top-level mapping invalid")
    required = {"schema", "candidate_id", "title", "evaluation_date", "source_commit",
                "fixed_epoch", "scope_literal", "evaluator_authority", "evaluator_version",
                "evaluator_authority_sha256", "obstruction_id", "candidate_definition",
                "family", "phase_space", "dynamics", "parameters", "parameter_provenance",
                "arithmetic_origin", "clock", "normalization", "determinant_convention",
                "orbit_cutoff", "precision", "training_data", "forbidden_data",
                "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple",
                "overall_verdict", "route_b_invocation_allowed", "route_b_lock_reason",
                "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens"}
    if set(data) != required:
        raise AssertionError("evaluation field set changed")
    semantic = hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":"),
                                           ensure_ascii=False).encode()).hexdigest()
    return data, semantic


def run_lane(name: str) -> str:
    command = [sys.executable, "-B", str(ROOT / "code" / name)]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c366-lane-") as directory:
        if name == "c366_krawtchouk_xx_producer.py":
            generated = Path(directory) / "evidence.json"
            command += ["--output", str(generated)]
            output = subprocess.check_output(command, env=env, text=True)
            if generated.read_bytes() != EVIDENCE.read_bytes():
                raise AssertionError("producer bytes differ from checked evidence")
            return output
        return subprocess.check_output(command, env=env, text=True)


def optimized_refusal(name: str) -> None:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    for flag in ("-O", "-OO"):
        command = [sys.executable, flag, "-B", str(ROOT / "code" / name)]
        with tempfile.TemporaryDirectory(prefix="c366-opt-") as directory:
            if name == "c366_krawtchouk_xx_producer.py":
                command += ["--output", str(Path(directory) / "evidence.json")]
            proc = subprocess.run(command, env=env, stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT, text=True)
        if proc.returncode == 0 or "refuses optimized Python" not in proc.stdout:
            raise AssertionError(f"optimized refusal absent: {flag} {name}")


def fresh_build(round_number: int) -> bytes:
    with tempfile.TemporaryDirectory(prefix=f"c366-build-{round_number}-") as directory:
        work = Path(directory)
        shutil.copy2(TEX, work / "main.tex")
        env = dict(os.environ, SOURCE_DATE_EPOCH=str(EPOCH), FORCE_SOURCE_DATE="1", TZ="UTC")
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{main.tex}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error",
                   "-jobname=main", source]
        for _ in range(2):
            subprocess.run(command, cwd=work, env=env, check=True,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log = (work / "main.log").read_text(errors="replace")
        match = WARNING.search(log)
        if match:
            raise AssertionError(f"paper warning round {round_number}: {match.group(0)}")
        return (work / "main.pdf").read_bytes()


def build_pdfs() -> None:
    blobs = []
    for round_number, target in enumerate(ROUND_PDFS):
        first, second = fresh_build(round_number), fresh_build(round_number)
        if first != second:
            raise AssertionError(f"nondeterministic PDF round {round_number}")
        target.write_bytes(first); blobs.append(first)
    MAIN_PDF.write_bytes(blobs[2])


def pages(path: Path) -> int:
    info = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in info.splitlines()
                    if line.startswith("Pages:")))


def fonts(path: Path) -> int:
    info = subprocess.check_output(["pdffonts", str(path)], text=True)
    rows = [line for line in info.splitlines()[2:]
            if line.strip() and not line.lstrip().startswith("-")]
    if not rows:
        raise AssertionError("no PDF fonts")
    for row in rows:
        columns = row.split()
        if len(columns) < 7 or columns[-5] != "yes" or columns[-4] != "yes":
            raise AssertionError(f"font not embedded/subset: {row}")
    return len(rows)


def pdf_text(path: Path) -> str:
    raw = subprocess.check_output(["pdftotext", "-layout", str(path), "-"])
    # Poppler maps several newtx radical/delimiter glyphs to bounded control
    # bytes.  Normalize precisely those known glyph markers before the clean
    # text audit; every other control byte remains fatal.
    normalized = raw.translate(None, b"\x01\x12\x13\x14\x15")
    if re.search(rb"[\x00-\x08\x0b\x0e-\x1f\x7f]", normalized):
        raise AssertionError("PDF text control byte")
    output = normalized.decode("utf-8").lower()
    for token in ("qquad", "??", "[verify]", "todo", "fixme", "missing glyph", "__mutated"):
        if token in output:
            raise AssertionError(f"PDF garbage token {token}")
    return " ".join(output.split())


def raster(path: Path, count: int) -> list[int]:
    sizes = []
    with tempfile.TemporaryDirectory(prefix="c366-raster-") as directory:
        work = Path(directory)
        for page in range(1, count + 1):
            prefix = work / f"p-{page}"
            subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "72",
                            "-png", str(path), str(prefix)], check=True,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            images = list(work.glob(f"p-{page}-*.png"))
            if len(images) != 1 or images[0].stat().st_size < 1000:
                raise AssertionError("PDF raster failure")
            sizes.append(images[0].stat().st_size)
    return sizes


def build_manifest() -> dict:
    files = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*")
             if path.is_file() and path != MANIFEST}
    if set(files) != EXPECTED or len(files) != 27:
        raise AssertionError(f"ledger mismatch missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}")
    for name, path in files.items():
        if path.suffix != ".pdf" and re.search(rb"[\x00-\x09\x0b-\x1f\x7f]", path.read_bytes()):
            raise AssertionError(f"source control byte: {name}")
    evidence = strict_json(EVIDENCE)
    claimed = evidence.pop("payload_sha256")
    computed = hashlib.sha256(json.dumps(evidence, sort_keys=True, separators=(",", ":"),
                                         ensure_ascii=False).encode()).hexdigest()
    if claimed != computed:
        raise AssertionError("stale evidence payload hash")
    if evidence["route_a_yaml"] != {
        "relative_path": "evaluations/route_a/HCS-C366/2026-09-04.yaml",
        "raw_sha256": EVAL_RAW,
        "semantic_sha256": EVAL_SEMANTIC,
    }:
        raise AssertionError("evidence evaluation lock mismatch")
    if evidence["evaluator"] != {
        "authority": "flow_systems/skills/route-a-evaluator.md",
        "version": "0.2.0",
        "sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
    }:
        raise AssertionError("evidence evaluator lock mismatch")
    evaluation, semantic = strict_yaml()
    if sha(EVALUATION) != EVAL_RAW or semantic != EVAL_SEMANTIC:
        raise AssertionError("evaluation raw/semantic lock mismatch")
    if evaluation["tuple"] != ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL",
                               "A4_NATURAL_QUANTIZATION"]:
        raise AssertionError("evaluation tuple changed")
    if evaluation["overall_verdict"] != "ROUTE_A_REJECTED" or evaluation["route_b_invocation_allowed"] is not False:
        raise AssertionError("Route-A/Route-B lock changed")
    if any(evaluation["scope_flags"].values()):
        raise AssertionError("forbidden scope flag")
    checker = (ROOT / "code/c366_krawtchouk_xx_checker.py").read_text()
    if "c366_krawtchouk_xx_" + "producer" in checker:
        raise AssertionError("checker names producer")
    theorem = (ROOT / "THEOREM_PACKAGE.md").read_text()
    for token in ("PROVABLE AS STATED", "exterior power", "fermion parity", "Gaussian polynomial"):
        if token not in theorem:
            raise AssertionError(f"theorem sentinel absent: {token}")
    source = (ROOT / "SOURCE_AUDIT.md").read_text()
    for token in ("10.1103/PhysRevLett.92.187902", "10.1103/PhysRevLett.93.230502", "lineage"):
        if token not in source:
            raise AssertionError(f"source sentinel absent: {token}")
    report = (ROOT / "paper/COMPILE_REPORT.md").read_text()
    sentinels = ("single-particle propagator owner", "many-body phase owner",
                 "revival-boundary owner")
    pdf_rows = []
    for round_number, path in enumerate(ROUND_PDFS):
        count, font_rows, text = pages(path), fonts(path), pdf_text(path)
        if sentinels[round_number] not in text:
            raise AssertionError(f"revision sentinel absent round {round_number}")
        if round_number == 2:
            for token in ("route a is rejected", "route b is false", "not automatically",
                          "no rational-prime", "no_bad_euler_or_root_number",
                          "gaussian-polynomial rows", "2b/|ω| + n"):
                if token not in text:
                    raise AssertionError(f"final paper sentinel absent: {token}")
        digest = sha(path)
        if digest not in report or f"| {round_number} | {count} | {font_rows} |" not in report:
            raise AssertionError(f"compile report stale round {round_number}")
        pdf_rows.append({"round": round_number, "path": str(path.relative_to(ROOT)),
                         "sha256": digest, "bytes": path.stat().st_size,
                         "pages": count, "font_rows": font_rows,
                         "raster_bytes": raster(path, count)})
    if len({row["sha256"] for row in pdf_rows}) != 3 or MAIN_PDF.read_bytes() != ROUND_PDFS[2].read_bytes():
        raise AssertionError("PDF revision identity")
    return {
        "schema": "hcs-release-manifest-v1", "candidate_id": "HCS-C366",
        "obstruction_id": "HEN-O350", "source_commit": SOURCE, "fixed_epoch": EPOCH,
        "scope_literal": SCOPE, "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
        "evaluator_version": "0.2.0",
        "evaluator_authority_sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
        "evaluation_raw_sha256": EVAL_RAW, "evaluation_semantic_sha256": EVAL_SEMANTIC,
        "payload_file_count": 27, "physical_file_count": 28,
        "evidence_sha256": sha(EVIDENCE), "evidence_payload_sha256": claimed,
        "main_pdf_sha256": sha(MAIN_PDF),
        "release_lanes": {"producer": "PASS", "independent_checker": "PASS",
                          "sympy_crosscheck": "PASS", "isolated_byte_replay": "PASS",
                          "hostile_mutation": "PASS", "optimized_mode_refusal": "PASS",
                          "deterministic_pdf_rebuild": "PASS", "payload_membership": "PASS"},
        "pdf_rounds": pdf_rows,
        "files": {name: sha(path) for name, path in sorted(files.items())},
    }


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C366 release refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--build-pdfs", action="store_true")
    args = parser.parse_args()
    if args.build_pdfs:
        build_pdfs()
        print("C366_PDF_BUILD_PASS")
        return
    lanes = [
        ("c366_krawtchouk_xx_producer.py", "C366_PRODUCER_PASS"),
        ("c366_krawtchouk_xx_checker.py", "C366 independent Krawtchouk-XX checker: PASS"),
        ("c366_krawtchouk_xx_sympy_crosscheck.py", "C366 SymPy cross-check: PASS"),
        ("c366_krawtchouk_xx_replay.py", "C366 byte replay: PASS"),
        ("c366_krawtchouk_xx_mutation.py", "C366 hostile mutation suite: PASS"),
    ]
    outputs = {}
    for name, sentinel in lanes:
        outputs[name] = run_lane(name).strip()
        if sentinel not in outputs[name]:
            raise AssertionError(f"lane sentinel absent: {name}")
        optimized_refusal(name)
    optimized_refusal("c366_release_manifest.py")
    for round_number, checked in enumerate(ROUND_PDFS):
        first, second = fresh_build(round_number), fresh_build(round_number)
        if first != second or first != checked.read_bytes():
            raise AssertionError(f"stale or nondeterministic PDF round {round_number}")
    manifest = build_manifest()
    canonical = json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.write:
        MANIFEST.write_text(canonical)
    elif not MANIFEST.exists() or MANIFEST.read_text() != canonical:
        raise AssertionError("checked-in manifest stale")
    print("C366_RELEASE_PASS " + json.dumps({
        "checker": outputs["c366_krawtchouk_xx_checker.py"],
        "sympy": outputs["c366_krawtchouk_xx_sympy_crosscheck.py"],
        "mutation": outputs["c366_krawtchouk_xx_mutation.py"],
        "evidence_sha256": manifest["evidence_sha256"],
        "pdf_sha256": manifest["pdf_rounds"][2]["sha256"],
        "pages": manifest["pdf_rounds"][2]["pages"],
        "manifest_sha256": hashlib.sha256(canonical.encode()).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
