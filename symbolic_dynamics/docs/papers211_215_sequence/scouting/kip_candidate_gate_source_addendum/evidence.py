"""Bounded source-addendum evidence; no scientific code is imported or run."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import sys

BASE = Path(__file__).resolve().parent
GATE = BASE.parent / "kip_candidate_gate"
EXPECTED_GATE_SHA = "11cc87ac615849ae33718ff63edde8b43b6456343d046e4d2a19717e41eebeda"

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def pin(path):
    raw = path.read_bytes()
    return {"path": str(path), "bytes": len(raw), "sha256": sha(raw)}

def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")

def check_manifest(folder):
    manifest = folder / "SHA256SUMS"
    rows = [line.split("  ", 1) for line in manifest.read_text().splitlines()]
    assert len(rows) == len(set(rel for digest, rel in rows))
    for digest, rel in rows:
        assert rel and not Path(rel).is_absolute() and ".." not in Path(rel).parts
        assert sha((folder / rel).read_bytes()) == digest, rel
    actual = sorted(str(p.relative_to(folder)) for p in folder.rglob("*")
                    if p.is_file() and p != manifest)
    assert actual == sorted(rel for digest, rel in rows)
    return {"manifest": pin(manifest), "payload_files": len(rows),
            "payload_bytes": sum((folder / rel).stat().st_size for digest, rel in rows)}

def gate_check():
    result = check_manifest(GATE)
    assert result["manifest"]["sha256"] == EXPECTED_GATE_SHA
    assert result["payload_files"] == 78 and result["payload_bytes"] == 2017173
    return result

def native(label, argv):
    folder = BASE / "native"
    folder.mkdir(exist_ok=True)
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    proc = subprocess.run(argv, cwd=BASE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ended = datetime.datetime.now(datetime.timezone.utc).isoformat()
    out, err = folder / (label + ".stdout"), folder / (label + ".stderr")
    out.write_bytes(proc.stdout)
    err.write_bytes(proc.stderr)
    record = {"argv": argv, "cwd": str(BASE), "started_utc": started,
              "ended_utc": ended, "exit_code": proc.returncode,
              "stdout": pin(out), "stderr": pin(err),
              "scope": "source_documentation_only"}
    dump(folder / (label + ".json"), record)
    print(json.dumps({"native": label, "exit_code": proc.returncode,
                      "stdout_bytes": len(proc.stdout), "stderr_bytes": len(proc.stderr)}))
    return record

def capture():
    assert not (BASE / "SOURCE_PINS.json").exists(), "do not overwrite capture"
    before = gate_check()
    anchors = []
    for name in ["HANDOFF.md", "SHA256SUMS"]:
        source = GATE / name
        target = BASE / "historical" / ("gate_" + name)
        target.parent.mkdir(exist_ok=True)
        target.write_bytes(source.read_bytes())
        assert target.read_bytes() == source.read_bytes()
        anchors.append({"source": pin(source), "copy": pin(target), "raw_equal": True})
    sources = []
    for version in ["v1", "v3"]:
        url = "https://arxiv.org/html/2604.15497" + version
        target = BASE / "sources" / ("2604.15497" + version + ".html")
        target.parent.mkdir(exist_ok=True)
        record = native(version + "_html", ["curl", "--fail", "--location",
            "--max-time", "30", "--output", str(target), url])
        assert record["exit_code"] == 0, version
        sources.append({"version": version, "url": url, "body": pin(target),
                        "native_receipt": "native/" + version + "_html.json"})
    browser = []
    for file in sorted((BASE / "browser").glob("*.json")):
        record = json.loads(file.read_text())
        text = record["returned_text"]
        assert record["tool"] == "web.run" and isinstance(text, str)
        browser.append({"container": pin(file), "decoded_utf8_bytes": len(text.encode()),
                        "decoded_utf8_sha256": sha(text.encode())})
    assert len(browser) == 7
    after = gate_check()
    assert before == after
    dump(BASE / "SOURCE_PINS.json", {"gate_before": before, "gate_after": after,
        "historical_anchors": anchors, "sources": sources, "browser_records": browser,
        "scientific_invocations": 0})
    print(json.dumps({"capture": "PASS", "historical_raw_pairs": len(anchors),
                      "sources": len(sources), "browser_records": len(browser),
                      "gate_payload_files": after["payload_files"],
                      "scientific_invocations": 0}))

def audit():
    record = json.loads((BASE / "SOURCE_PINS.json").read_text())
    assert record["gate_before"] == record["gate_after"] == gate_check()
    for row in record["historical_anchors"]:
        source, copy = Path(row["source"]["path"]), Path(row["copy"]["path"])
        assert source.read_bytes() == copy.read_bytes()
        assert pin(source) == row["source"] and pin(copy) == row["copy"]
    for row in record["sources"]:
        assert pin(Path(row["body"]["path"])) == row["body"]
        receipt = json.loads((BASE / row["native_receipt"]).read_text())
        assert receipt["exit_code"] == 0 and row["url"] == receipt["argv"][-1]
        for stream in ["stdout", "stderr"]:
            assert pin(Path(receipt[stream]["path"])) == receipt[stream]
        assert receipt["argv"][-2] == row["body"]["path"]
    for row in record["browser_records"]:
        file = Path(row["container"]["path"])
        assert pin(file) == row["container"]
        text = json.loads(file.read_text())["returned_text"].encode()
        assert len(text) == row["decoded_utf8_bytes"]
        assert sha(text) == row["decoded_utf8_sha256"]
    assert record["scientific_invocations"] == 0
    result = {"audit": "PASS", "historical_raw_pairs": 2, "native_bindings": 2,
              "browser_records": 7, "source_body_hashes": 2,
              "original_gate_payload_files": 78, "scientific_invocations": 0}
    if (BASE / "SHA256SUMS").exists():
        result["addendum_manifest"] = check_manifest(BASE)
    print(json.dumps(result))

def seal():
    assert not (BASE / "SHA256SUMS").exists(), "immutable seal already exists"
    audit()
    files = sorted(p for p in BASE.rglob("*") if p.is_file())
    (BASE / "SHA256SUMS").write_text("".join(
        sha(p.read_bytes()) + "  " + str(p.relative_to(BASE)) + "\n" for p in files))
    print(json.dumps(check_manifest(BASE)))

if __name__ == "__main__":
    {"capture": capture, "audit": audit, "seal": seal}[sys.argv[1]]()

