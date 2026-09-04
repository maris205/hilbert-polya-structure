#!/usr/bin/env python3
"""Deterministic release and manifest gate for HCS-C374."""
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
MANIFEST = ROOT / "C374_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c374_kummer_arboreal_evidence.json"
YML = ROOT / "evaluations/route_a/HCS-C374/2026-09-04.yaml"
BODY = ROOT / "paper/main_body.tex"
MAIN = ROOT / "paper/main.pdf"
ROUND_SOURCES = [ROOT / f"paper/main_round{r}.tex" for r in range(3)]
ROUND_PDFS = [ROOT / f"paper/main_round{r}.pdf" for r in range(3)]
SOURCE = "f58422d8f03235329863f946654981ecb5d4dc97"
EPOCH = 1788480000
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW = "1ffd05227ff84d1bcb2e86210f40bc64a4c9b770b3ba7fd00ad501895d55a455"
YAML_SEMANTIC = "da899423959140836240e0935670c66d9ab3a7b59592700a166f34ec70b5122e"
WARNING = re.compile(r"(?:LaTeX|Package).*Warning|Overfull|Underfull|badness|undefined", re.I)
ENGLISH_KEYWORDS = (
    ("kummer theory", "arboreal galois representations", "cyclotomic fields",
     "affine groups", "iterated preimages"),
    ("arboreal galois representations", "kummer extensions", "frobenius fixed points",
     "chebotarev density", "affine groups", "iterated preimages"),
    ("kummer dynamics", "arboreal galois representations", "2-adic affine groups",
     "frobenius permutations", "exact computation", "finite koopman operators",
     "route-a evaluation"),
)
CHINESE_KEYWORDS = (
    ("库默理论", "迭代原像树", "分圆域", "仿射群", "Galois作用"),
    ("算术动力学", "Frobenius不动点", "Chebotarev密度", "二次特征", "根数分布", "素数密度"),
    ("库默动力学", "二进仿射群", "Frobenius置换", "精确枚举", "有限Koopman算子", "路线A评估", "本原轨道障碍"),
)
EXPECTED_ROUTE = {
    "tuple": [
        "A0_STRUCTURAL_ARITHMETIC_RELATION", "A1_WEAK", "A2_FAIL",
        "A3_FAIL", "A4_FORMAL_HINT",
    ],
    "overall": "ROUTE_A_EXPLORATORY",
    "route_b_invocation_allowed": False,
    "a1_scope": "the proved affine action and fixed-root law are source-local and do not constitute a complete arithmetic primitive-orbit atlas",
    "a1_missing_requirements": [
        "no all-level primitive-cycle and repetition enumeration with completeness control",
        "no orbit orientation, phase, multiplicity-weight, or monodromy and stability atlas",
        "no intrinsic prime-to-orbit, prime-power, or log(p) period correspondence",
        "mandatory shuffled-period, random-weight, random-phase, same-density-length, neighboring-parameter, and simpler-parent controls are not completed at the A1 orbit layer",
    ],
}

EXPECTED = {
    "ASSUMPTIONS.md", "CLAIMS.md", "EXPERIMENT_PLAN.md", "LIMITATIONS.md",
    "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "PROJECT_README.md", "README.md", "REFERENCES.md", "RELEASE.md",
    "REPRODUCIBILITY.md", "RESEARCH_QUESTION.md", "SCOPE.md", "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md", "requirements.txt",
    "code/README.md", "code/c374_kummer_arboreal_checker.py",
    "code/c374_kummer_arboreal_mutation.py", "code/c374_kummer_arboreal_producer.py",
    "code/c374_kummer_arboreal_replay.py", "code/c374_kummer_arboreal_sympy_crosscheck.py",
    "code/c374_release_manifest.py",
    "evaluations/route_a/HCS-C374/2026-09-04.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_body.tex", "paper/main_round0.pdf", "paper/main_round0.tex",
    "paper/main_round1.pdf", "paper/main_round1.tex", "paper/main_round2.pdf",
    "paper/main_round2.tex", "proof/ANALYTIC_PROOF.md",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c374_kummer_arboreal_evidence.json",
    "review/CLAIM_REFERENCE_AUDIT.md", "review/FAILURE_MODE_AUDIT.md",
    "review/FINAL_INTEGRITY.md", "review/ROUND0_REVIEW.md", "review/ROUND1_REVIEW.md",
    "review/ROUND2_REVIEW.md", "tests/test_c374_smoke.py",
}


class Loader(yaml.SafeLoader):
    pass


Loader.yaml_implicit_resolvers = {
    key: [(tag, regex) for tag, regex in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def strict_mapping(loader, node, deep=False):
    out = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge keys are forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("duplicate or non-string YAML key")
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def strict_json(path: Path) -> dict:
    def unique(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate JSON key: {key}")
            out[key] = value
        return out

    value = json.loads(
        path.read_text(), object_pairs_hook=unique,
        parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)),
    )
    if type(value) is not dict:
        raise TypeError("JSON root must be mapping")
    return value


def strict_yaml(path: Path) -> dict:
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML aliases are forbidden")
    value = yaml.load(raw, Loader=Loader)
    if type(value) is not dict:
        raise TypeError("YAML root must be mapping")
    return value


def command(script: str, args=()) -> str:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    return subprocess.check_output(
        [sys.executable, "-B", str(ROOT / "code" / script), *args],
        cwd=ROOT, env=env, text=True, stderr=subprocess.STDOUT,
    ).strip()


def smoke_tests() -> str:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    proc = subprocess.run(
        [sys.executable, "-B", "-m", "unittest", "tests/test_c374_smoke.py"],
        cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
    )
    if proc.returncode != 0 or "OK" not in proc.stdout:
        raise AssertionError(f"smoke tests failed:\n{proc.stdout}")
    return "3/3 PASS"


def optimized_refusal(script: str) -> None:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    for flag in ("-O", "-OO"):
        cmd = [sys.executable, flag, "-B", str(ROOT / "code" / script)]
        if script == "c374_kummer_arboreal_producer.py":
            with tempfile.TemporaryDirectory(prefix="c374-opt-") as directory:
                proc = subprocess.run(
                    cmd + ["--output", str(Path(directory) / "evidence.json")],
                    cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                )
        else:
            proc = subprocess.run(cmd, cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if proc.returncode == 0 or "refuses optimized Python" not in proc.stdout:
            raise AssertionError(f"optimized execution not refused: {flag} {script}")


def fresh_pdf(round_number: int) -> tuple[bytes, str]:
    with tempfile.TemporaryDirectory(prefix=f"c374-pdf-{round_number}-") as directory:
        work = Path(directory)
        shutil.copy2(BODY, work / "main_body.tex")
        shutil.copy2(ROUND_SOURCES[round_number], work / f"main_round{round_number}.tex")
        env = dict(os.environ, SOURCE_DATE_EPOCH=str(EPOCH), FORCE_SOURCE_DATE="1", TZ="UTC")
        cmd = [
            "lualatex", "-interaction=nonstopmode", "-halt-on-error",
            "-jobname=artifact", f"main_round{round_number}.tex",
        ]
        for _ in range(2):
            subprocess.run(cmd, cwd=work, env=env, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log = (work / "artifact.log").read_text(errors="replace")
        hit = WARNING.search(log)
        if hit:
            raise AssertionError(f"paper warning round {round_number}: {hit.group(0)}")
        return (work / "artifact.pdf").read_bytes(), log


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
            raise AssertionError(f"font not embedded and subset: {row}")
    if not any("DroidSansFallback" in row for row in rows):
        raise AssertionError("embedded CJK font is missing")
    return len(rows)


def text_and_raster(path: Path, pages: int) -> tuple[str, list[int]]:
    raw = subprocess.check_output(["pdftotext", "-layout", str(path), "-"])
    if re.search(rb"[\x00-\x08\x0b\x0e-\x1f\x7f]", raw):
        raise AssertionError("control byte in extracted PDF text")
    text = " ".join(raw.decode().lower().split())
    for bad in ("??", "[verify]", "todo", "fixme", "__mutated"):
        if bad in text:
            raise AssertionError(f"PDF text garbage: {bad}")
    raster = []
    with tempfile.TemporaryDirectory(prefix="c374-raster-") as directory:
        for page in range(1, pages + 1):
            prefix = Path(directory) / f"p{page}"
            subprocess.run(
                ["pdftoppm", "-f", str(page), "-l", str(page), "-r", "72", "-png", str(path), str(prefix)],
                check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            )
            images = list(Path(directory).glob(f"p{page}-*.png"))
            if len(images) != 1 or images[0].stat().st_size < 1000:
                raise AssertionError("PDF raster failure")
            raster.append(images[0].stat().st_size)
    return text, raster


def pdf_receipts(write: bool) -> list[dict]:
    receipts = []
    tokens = ("round 0 advance", "round 1 advance", "round 2 advance")
    for round_number, path in enumerate(ROUND_PDFS):
        first, _ = fresh_pdf(round_number)
        second, _ = fresh_pdf(round_number)
        if first != second:
            raise AssertionError(f"nondeterministic PDF round {round_number}")
        if write:
            path.write_bytes(first)
        elif path.read_bytes() != first:
            raise AssertionError(f"stored PDF round {round_number} differs from fresh deterministic build")
        pages = page_count(path)
        text, raster = text_and_raster(path, pages)
        compact = text.replace(" ", "")
        if tokens[round_number] not in text:
            raise AssertionError(f"substantive round token missing: {round_number}")
        for header in ("abstract", "keywords:"):
            if header not in text:
                raise AssertionError(f"English abstract gate missing in round {round_number}: {header}")
        for header in ("中文摘要", "关键词："):
            if header not in compact:
                raise AssertionError(f"Chinese abstract gate missing in round {round_number}: {header}")
        if not 5 <= len(ENGLISH_KEYWORDS[round_number]) <= 7:
            raise AssertionError(f"English keyword count drift in round {round_number}")
        if not 5 <= len(CHINESE_KEYWORDS[round_number]) <= 7:
            raise AssertionError(f"Chinese keyword count drift in round {round_number}")
        if len(set(ENGLISH_KEYWORDS[round_number])) != len(ENGLISH_KEYWORDS[round_number]):
            raise AssertionError(f"duplicate English keyword in round {round_number}")
        if len(set(CHINESE_KEYWORDS[round_number])) != len(CHINESE_KEYWORDS[round_number]):
            raise AssertionError(f"duplicate Chinese keyword in round {round_number}")
        for keyword in ENGLISH_KEYWORDS[round_number]:
            if keyword not in text:
                raise AssertionError(f"English keyword missing in round {round_number}: {keyword}")
        for keyword in CHINESE_KEYWORDS[round_number]:
            if keyword.lower().replace(" ", "") not in compact:
                raise AssertionError(f"Chinese keyword missing in round {round_number}: {keyword}")
        forbidden_by_round = (
            (
                "complete fixed-root spectrum", "chebotarev root densities",
                "inverse limit and all-iterate frobenius cycles", "exact evidence and independent validation",
                "finite koopman realization and route-a boundary", "frobenius不动根", "完整计数",
                "逆极限", "有限层群枚举",
            ),
            (
                "inverse limit and all-iterate frobenius cycles", "exact evidence and independent validation",
                "finite koopman realization and route-a boundary", "逆极限", "有限层群枚举",
                "a1_weak", "路线a评估",
            ),
            (),
        )
        for forbidden in forbidden_by_round[round_number]:
            use_compact = any(ord(char) > 127 for char in forbidden)
            haystack = compact if use_compact else text
            needle = forbidden.lower().replace(" ", "") if use_compact else forbidden
            if needle in haystack:
                raise AssertionError(f"later-round leak in round {round_number}: {forbidden}")
        if round_number == 2:
            for sentinel in (
                "a1_weak", "route_a_exploratory", "empirical density alone receives no a0 credit",
                "a4_formal_hint", "no target euler product", "route b is not invoked",
            ):
                if sentinel not in text:
                    raise AssertionError(f"final paper sentinel missing: {sentinel}")
        receipts.append({
            "round": round_number,
            "source": str(ROUND_SOURCES[round_number].relative_to(ROOT)),
            "path": str(path.relative_to(ROOT)),
            "sha256": sha(path), "bytes": path.stat().st_size, "pages": pages,
            "font_rows": font_count(path), "raster_bytes": raster,
        })
    if len({row["sha256"] for row in receipts}) != 3:
        raise AssertionError("round PDFs are not distinct")
    if write:
        MAIN.write_bytes(ROUND_PDFS[2].read_bytes())
    elif MAIN.read_bytes() != ROUND_PDFS[2].read_bytes():
        raise AssertionError("main.pdf is not byte-identical to round 2")
    return receipts


def evidence_payload_hash() -> str:
    value = strict_json(EVIDENCE)
    claimed = value.pop("payload_sha256")
    got = hashlib.sha256(canonical(value)).hexdigest()
    if claimed != got:
        raise AssertionError("stale evidence payload hash")
    return claimed


def generated_reports(outputs: dict[str, str], pdfs: list[dict], smoke: str) -> dict[str, str]:
    checker = re.search(r"PASS \((\d+) assertions\)", outputs["checker"]).group(1)
    sympy = re.search(r"PASS \((\d+) exact checks\)", outputs["sympy"]).group(1)
    attacks = re.search(r"PASS \((\d+) attacks\)", outputs["mutation"]).group(1)
    evidence = strict_json(EVIDENCE)
    pair_count = sum(row["group_order"] for row in evidence["group_ledger"])
    parent_pair_count = evidence["arithmetic_controls"]["simpler_parent_full_affine"]["total_pairs"]
    cells = evidence["prime_regression"]["cell_count"]
    results = f"""# Results

The canonical evidence has SHA-256 `{sha(EVIDENCE)}` and self-excluding payload SHA-256 `{evidence_payload_hash()}`.

- analytic range: every `n>=3`;
- exact finite image: `H_n={{(a,b):(-1)^b=(2/a)}}`, order `2^(2n-2)`;
- adjacent restriction: surjective with kernel order four;
- nonzero fixed-root counts: `2`, `2^k` for `3<=k<n`, and `2^n`; never `1` or `4`;
- root-prime density: `7/24+1/(3*4^(n-1))`, limit `7/24`;
- finite receipts: {pair_count:,} group elements and {cells:,} prime--level cells.
- A0 controls: basepoint 3 has trivial intersection/full affine image; the
  {parent_pair_count:,}-pair full-affine ledger restores four fixed roots;
  five prime powers retain `Frob_p^r` repetition ownership while twenty
  mixed composites have no single-prime owner; empirical density earns no
  A0 credit.
- strict Route-A result: `A1_WEAK`, `A4_FORMAL_HINT`, overall
  `ROUTE_A_EXPLORATORY`.

The finite receipts validate implementations.  The proof in `proof/ANALYTIC_PROOF.md` establishes the all-level statements.
"""
    tests = f"""# Test report

All release lanes pass:

- producer: `{outputs['producer']}`;
- independent checker: {checker} assertions PASS;
- SymPy cross-check: {sympy} exact checks PASS;
- isolated byte replay: PASS;
- hostile repaired-hash suite: {attacks} attacks PASS;
- unittest smoke suite: {smoke};
- optimized-mode refusal under `-O` and `-OO`: PASS;
- strict JSON/YAML schema, A0 controls, weak-A1 lock, scope, source,
  membership, bilingual abstract/keyword layering, PDF, CJK font, text, and
  raster gates: PASS.
"""
    hostile = f"""# Hostile audit

The independent checker rejects {attacks} attacks covering stale and repaired payload hashes, candidate/source/basepoint substitution, intersection/image/density/restriction mutations, A0-control corruption, prime-stream and histogram corruption, DOI and ownership changes, Route-A escalation, forbidden claims, unknown or missing keys, duplicate JSON keys, and nonfinite JSON.

Every executable lane refuses optimized Python.  The checker contains no import of the producer, and the release gate locks all target-local, Euler-factor, root-number, automorphy, divisor, zero-match, Hilbert--Pólya, and Route-B flags to `false`.
"""
    additions = [
        "intersection, degree, exact finite image, and restriction theorem",
        "complete fixed-root spectrum and Chebotarev density theorem",
        "inverse limit, all-iterate dictionary, exact evidence, finite Koopman boundary, and Route-A closure",
    ]
    lines = [
        "# Compile report", "",
        "Each manuscript source was built twice in fresh directories with LuaLaTeX under `SOURCE_DATE_EPOCH=1788480000`; both builds matched byte for byte. Settled logs contain no warning, overfull/underfull box, badness, or undefined-reference sentinel. Every font is embedded and subset, extracted text is clean, and every page rasterizes.", "",
        "| round | source | pages | fonts | SHA-256 | theorem increment |",
        "|---|---|---:|---:|---|---|",
    ]
    for row, addition in zip(pdfs, additions):
        lines.append(f"| {row['round']} | `{row['source']}` | {row['pages']} | {row['font_rows']} | `{row['sha256']}` | {addition} |")
    lines += ["", "`paper/main.pdf` is byte-identical to round 2.", ""]
    paper_readme = """# Paper artifacts

`main_round0.tex`, `main_round1.tex`, and `main_round2.tex` are distinct wrappers around the auditable conditional source `main_body.tex`.  Each wrapper has its own deterministic trailer identifier and adds a substantive theorem layer.  Their PDFs are preserved beside them; `main.pdf` equals the final round byte for byte.

Every round contains an English abstract and an independently written Chinese abstract, each with 5--7 language-matched keywords.  The release gate rejects later-round conclusions or evidence in earlier artifacts and requires an embedded subset CJK font.

Run `python -B ../code/c374_release_manifest.py --write --build-pdfs` from this package directory to rebuild all paper artifacts and reports.
"""
    release = """# Release

The release object is closed by `C374_RELEASE_MANIFEST.json`, whose file ledger excludes only the manifest itself.  A release requires every analytic/source/scope lane, independent numerical lane, hostile mutation, smoke test, exact membership check, and deterministic PDF gate to pass.

Canonical command:

```bash
python -B code/c374_release_manifest.py --write --build-pdfs
python -B code/c374_release_manifest.py
```

No commit or push is performed by the package.
"""
    return {
        "results/RESULTS.md": results,
        "results/TEST_REPORT.md": tests,
        "results/HOSTILE_AUDIT.md": hostile,
        "paper/COMPILE_REPORT.md": "\n".join(lines),
        "paper/README.md": paper_readme,
        "RELEASE.md": release,
    }


def content_gates() -> dict:
    if sha(YML) != YAML_RAW:
        raise AssertionError("route YAML raw hash drift")
    route = strict_yaml(YML)
    if hashlib.sha256(canonical(route)).hexdigest() != YAML_SEMANTIC:
        raise AssertionError("route YAML semantic hash drift")
    if route["source_commit"] != SOURCE or route["scope_literal"] != SCOPE:
        raise AssertionError("route source or scope drift")
    if route["code_commit"] != SOURCE:
        raise AssertionError("route code-commit drift")
    if route["evaluator_authority_sha256"] != EVALUATOR:
        raise AssertionError("evaluator hash drift")
    if route["skill"] != "route-a-evaluator" or route["skill_version"] != "0.2.0":
        raise AssertionError("route evaluator schema drift")
    required_lock = {
        "object", "arithmetic_origin", "clock", "normalization",
        "determinant_convention", "cutoff", "precision", "allowed_data", "forbidden_data",
    }
    if set(route["source_lock"]) != required_lock:
        raise AssertionError("route source-lock drift")
    if route["tuple"] != EXPECTED_ROUTE["tuple"] or route["overall_verdict"] != EXPECTED_ROUTE["overall"]:
        raise AssertionError("route verdict drift")
    if route["route_b_invocation_allowed"] or any(route["scope_flags"].values()):
        raise AssertionError("forbidden route flag")
    a0_controls = route["a0"]["arithmetic_controls"]
    if len(a0_controls) < 3:
        raise AssertionError("A0 arithmetic controls missing")
    if [row["status"] for row in a0_controls] != [
        "ANALYTICALLY_PROVED", "EXECUTED_EXACT", "EXECUTED_EXACT",
    ]:
        raise AssertionError("A0 control status drift")
    composite_result = a0_controls[2]["result"]
    for token in ("5 prime powers", "Frob_p^r repetition controls", "20 mixed composites", "no one-prime Frobenius owner"):
        if token not in composite_result:
            raise AssertionError(f"route composite decomposition drift: {token}")
    if route["a1"]["verdict"] != "A1_WEAK" or route["a1"]["metrics"]["mandatory_a1_controls_completed"] != 0:
        raise AssertionError("strict A1 evaluator drift")
    if route["a4"]["verdict"] != "A4_FORMAL_HINT":
        raise AssertionError("strict A4 evaluator drift")
    if route["a4"]["metrics"]["canonical_time_reversal_for_family"]:
        raise AssertionError("unearned A4 time-reversal claim")
    if route["a4"]["metrics"]["nontrivial_phase_weight_preserved"]:
        raise AssertionError("unearned A4 phase-weight claim")
    for layer in ("a0", "a1", "a2", "a3", "a4"):
        if not route[layer].get("artifacts"):
            raise AssertionError(f"route artifact ledger missing: {layer}")
    for key in (
        "adversarial_controls", "claim_boundary", "blocking_conditions",
        "next_smallest_test", "round2_clues",
    ):
        if not route.get(key):
            raise AssertionError(f"route required field missing: {key}")
    if route["adversarial_controls"]["verdict"] != "PASS_SCOPE_LIMIT_RETAINED":
        raise AssertionError("proves-too-much control drift")

    evidence = strict_json(EVIDENCE)
    if evidence["source_commit"] != SOURCE or evidence["scope_literal"] != SCOPE:
        raise AssertionError("evidence source or scope drift")
    if evidence["route_a"] != EXPECTED_ROUTE:
        raise AssertionError("evidence route drift")
    if any(evidence["scope_flags"].values()):
        raise AssertionError("forbidden evidence flag")
    evidence_payload_hash()
    controls = evidence["arithmetic_controls"]
    neighbor = controls["neighboring_basepoint_3"]
    if neighbor["status"] != "PROVED_BY_VALUATION_AND_CAPELLI":
        raise AssertionError("basepoint-three control drift")
    if neighbor["shared_Q_sqrt_2_character_entanglement"]:
        raise AssertionError("basepoint-three entanglement drift")
    parent = controls["simpler_parent_full_affine"]
    if parent["total_pairs"] != 11184800 or not parent["restores_four_fixed_roots"]:
        raise AssertionError("full-affine parent control drift")
    for row in parent["level_ledger"]:
        if row["four_fixed_elements"] != 2 ** (2 * row["n"] - 5):
            raise AssertionError("four-root control formula drift")
    composite = controls["composite_label_decomposition"]
    if composite["odd_composite_count_below_100"] != 25:
        raise AssertionError("composite-control total drift")
    if composite["prime_power_count"] != 5 or composite["mixed_composite_count"] != 20:
        raise AssertionError("composite-control decomposition drift")
    if [row["value"] for row in composite["prime_power_labels"]] != [9, 25, 27, 49, 81]:
        raise AssertionError("prime-power label drift")
    if "Frob_p^r" not in composite["prime_power_owner"]:
        raise AssertionError("prime-power repetition owner drift")
    if composite["mixed_composite_has_single_prime_frobenius_owner"]:
        raise AssertionError("mixed-composite Frobenius-owner drift")
    if controls["empirical_density_earns_a0_credit"]:
        raise AssertionError("empirical density received A0 credit")
    quantization = evidence["quantization_boundary"]
    if quantization["route_a_verdict"] != "A4_FORMAL_HINT":
        raise AssertionError("evidence A4 verdict drift")
    if quantization["canonical_global_time_reversal_to_inverse"]:
        raise AssertionError("evidence claims a canonical global time reversal")
    if quantization["nontrivial_orbit_phase_or_weight_package"]:
        raise AssertionError("evidence claims an absent phase-weight package")
    if quantization["global_self_adjoint_hamiltonian_owner"]:
        raise AssertionError("evidence claims an absent Hamiltonian owner")

    checker = (ROOT / "code/c374_kummer_arboreal_checker.py").read_text()
    if re.search(r"(?:from|import)\s+[^\n]*c374_kummer_arboreal_producer", checker):
        raise AssertionError("checker imports producer")
    source = BODY.read_text()
    proof = (ROOT / "proof/ANALYTIC_PROOF.md").read_text()
    for token in (
        "Cyclotomic nonsquare", "Radical--cyclotomic intersection", "Exact image and restriction",
        "Fixed-root law", "Root-prime density", "Infinite arboreal image",
        "A1\\_WEAK", "A4\\_FORMAL\\_HINT", "ROUTE\\_A\\_EXPLORATORY", "中文摘要", "Keywords:", "关键词：",
        "no target Euler product", "not a Hilbert--P\\'olya operator", "Route B is not invoked",
    ):
        if token not in source:
            raise AssertionError(f"paper theorem token missing: {token}")
    for token in ("Capelli", "L intersect C=Q(sqrt(2))", "kernel four", "delta_n -> 7/24"):
        if token not in proof:
            raise AssertionError(f"proof token missing: {token}")
    for doi in (
        "10.5802/pmb.a-154", "10.1007/978-1-4613-0041-0",
        "10.1007/978-1-4612-1934-7", "10.1007/978-3-662-03983-0",
    ):
        if doi not in source or doi not in (ROOT / "SOURCE_AUDIT.md").read_text():
            raise AssertionError(f"source DOI missing: {doi}")
    if (ROOT / "paper/main.tex").read_text().strip() != r"\input{main_round2.tex}":
        raise AssertionError("main.tex does not select round 2")
    repeated_sentence = "has no odd prime divisor.  Its reduction is separable, and"
    if source.count(repeated_sentence) != 1:
        raise AssertionError("Chebotarev setup sentence missing or duplicated")
    mixed_owner_sentence = (
        "each with at least two distinct prime factors, are rejected as having no\n"
        "single-prime Frobenius owner."
    )
    if source.count(mixed_owner_sentence) != 1:
        raise AssertionError("mixed-composite ownership sentence missing, inverted, or duplicated")
    if "are rejected as having one\nsingle-prime Frobenius owner" in source:
        raise AssertionError("mixed-composite ownership sentence is semantically inverted")
    for index, wrapper in enumerate(ROUND_SOURCES):
        wrapper_text = wrapper.read_text()
        if wrapper_text.count(f"\\def\\CRevisionRound{{{index}}}") != 1:
            raise AssertionError(f"round wrapper number drift: {index}")
        if wrapper_text.count("\\input{main_body.tex}") != 1:
            raise AssertionError(f"round wrapper body drift: {index}")
    return route


def make_manifest(pdfs: list[dict]) -> dict:
    route = content_gates()
    files = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file() and path != MANIFEST}
    if set(files) != EXPECTED or len(files) != 48:
        raise AssertionError(f"file ledger mismatch missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}")
    return {
        "schema": "hcs-release-manifest-v1",
        "candidate_id": "HCS-C374", "obstruction_id": "HEN-O358",
        "source_commit": SOURCE, "fixed_epoch": EPOCH, "scope_literal": SCOPE,
        "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
        "evaluator_version": "0.2.0", "evaluator_authority_sha256": EVALUATOR,
        "evaluation_raw_sha256": YAML_RAW, "evaluation_semantic_sha256": YAML_SEMANTIC,
        "payload_file_count": 48, "physical_file_count": 49,
        "evidence_sha256": sha(EVIDENCE), "evidence_payload_sha256": evidence_payload_hash(),
        "analytic_theorem_range": "all n>=3",
        "finite_evidence": {
            "levels": "3..12", "group_pairs": 5592400,
            "full_affine_control_pairs": 11184800, "odd_prime_level_cells": 95910,
            "odd_composites_below_100": 25, "prime_power_repetition_controls": 5,
            "mixed_composites_without_single_prime_owner": 20,
        },
        "route_tuple": route["tuple"], "overall_verdict": route["overall_verdict"],
        "release_lanes": {
            "producer": "PASS", "independent_checker": "PASS", "sympy_crosscheck": "PASS",
            "isolated_byte_replay": "PASS", "hostile_mutation": "PASS", "unittest_smoke": "PASS",
            "optimized_mode_refusal": "PASS", "strict_json_yaml": "PASS",
            "source_and_scope_gate": "PASS", "deterministic_pdf_rebuild": "PASS",
            "embedded_subset_fonts": "PASS", "payload_membership": "PASS",
        },
        "pdf_rounds": pdfs, "main_pdf_sha256": sha(MAIN),
        "files": {name: sha(path) for name, path in sorted(files.items())},
    }


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C374 release refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--build-pdfs", action="store_true")
    args = parser.parse_args()
    if args.build_pdfs and not args.write:
        raise ValueError("--build-pdfs requires --write")
    if args.write:
        command("c374_kummer_arboreal_producer.py")

    content_gates()
    with tempfile.TemporaryDirectory(prefix="c374-release-producer-") as directory:
        producer_output = command(
            "c374_kummer_arboreal_producer.py",
            ("--output", str(Path(directory) / "evidence.json")),
        )
    outputs = {
        "producer": producer_output,
        "checker": command("c374_kummer_arboreal_checker.py"),
        "sympy": command("c374_kummer_arboreal_sympy_crosscheck.py"),
        "replay": command("c374_kummer_arboreal_replay.py"),
        "mutation": command("c374_kummer_arboreal_mutation.py"),
    }
    sentinels = {
        "producer": "C374_PRODUCER_PASS", "checker": "C374 independent checker: PASS",
        "sympy": "C374 SymPy cross-check: PASS", "replay": "C374 byte replay: PASS",
        "mutation": "C374 hostile mutation suite: PASS",
    }
    for key, token in sentinels.items():
        if token not in outputs[key]:
            raise AssertionError(f"lane did not pass: {key}")
    for script in (
        "c374_kummer_arboreal_producer.py", "c374_kummer_arboreal_checker.py",
        "c374_kummer_arboreal_sympy_crosscheck.py", "c374_kummer_arboreal_replay.py",
        "c374_kummer_arboreal_mutation.py",
    ):
        optimized_refusal(script)
    smoke = smoke_tests()

    pdfs = pdf_receipts(write=args.build_pdfs)
    reports = generated_reports(outputs, pdfs, smoke)
    for name, content in reports.items():
        path = ROOT / name
        if args.write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
        elif not path.exists() or path.read_text() != content:
            raise AssertionError(f"generated report drift: {name}")

    manifest = make_manifest(pdfs)
    if args.write:
        MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
    else:
        if strict_json(MANIFEST) != manifest:
            raise AssertionError("release manifest drift")
    print(
        "C374_RELEASE_PASS "
        f"evidence_sha256={sha(EVIDENCE)} main_pdf_sha256={sha(MAIN)} manifest_sha256={sha(MANIFEST)}"
    )


if __name__ == "__main__":
    main()
