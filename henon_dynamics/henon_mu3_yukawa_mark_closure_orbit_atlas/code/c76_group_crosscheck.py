#!/usr/bin/env python3
"""Independent GAP cross-check for the effective C76 label action.

C75's lifted group has order 11520, but its ambient C6 factor fixes every
label.  This script reconstructs the five nontrivial label permutations from
the locked C75 evidence and asks GAP to enumerate the effective action on all
16-label supports.
"""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess


PROJECT = Path(__file__).resolve().parents[1]
ROOT = PROJECT.parents[1]
C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift"
C76_EVIDENCE = PROJECT / "results/c76_closure_orbit_atlas_evidence.json"

FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
C76_EVIDENCE_SHA256 = "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94"
C75_HASHES = {
    "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
    "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
}
EFFECTIVE_GENERATOR_NAMES = (
    "zero_5_cycle",
    "zero_transposition",
    "fiber_F3_transposition",
    "fiber_F9_transposition",
    "ambient_s",
)
CARDINALITY_VECTOR = [
    1, 7, 27, 73, 151, 252, 352, 424, 450,
    424, 352, 252, 151, 73, 27, 7, 1,
]
ORBIT_SIZE_SPECTRUM = {
    1: 128, 2: 256, 4: 416, 5: 128, 8: 192, 10: 384,
    16: 16, 20: 672, 40: 608, 80: 208, 160: 16,
}


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def gap_list(values: list[int]) -> str:
    return "[" + ",".join(str(value) for value in values) + "]"


def parse_gap_output(stdout: str) -> dict[str, str]:
    rows: dict[str, str] = {}
    for line in stdout.splitlines():
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        rows[key.strip()] = value.strip()
    return rows


def main() -> None:
    c76_raw = C76_EVIDENCE.read_bytes()
    assert digest(c76_raw) == C76_EVIDENCE_SHA256
    c76 = json.loads(c76_raw)
    assert c76_raw == canonical(c76)
    assert c76["schema_id"] == "hcs-c76-finite-support-closure-orbit-atlas-prefreeze-v1"
    assert c76["status"] == "PREFREEZE_G3_PASS"
    assert c76["scope_literal"] == FIREWALL
    assert c76["authority"] == C75_HASHES

    source_paths = {
        "c75": C75 / "results/c75_closure_incidence_lift_evidence.json",
        "c75_manifest": C75 / "C75_PREFREEZE_MANIFEST.json",
    }
    assert {name: digest(path.read_bytes()) for name, path in source_paths.items()} == C75_HASHES
    c75 = json.loads(source_paths["c75"].read_text())
    assert c75["status"] == "PREFREEZE_G3_PASS"
    assert c75["scope_literal"] == FIREWALL
    assert c75["lifted_symmetry"]["lifted_group_order"] == 11520

    assert c76["source_model"]["c75_lifted_group_order"] == 11520
    assert c76["source_model"]["c75_ambient_c6_kernel_order"] == 6
    assert c76["source_model"]["effective_label_group_order"] == 1920
    assert c76["source_model"]["effective_label_group_candidate"] == "S5 x C2 x D8"
    assert tuple(c76["source_model"]["effective_generator_names"]) == EFFECTIVE_GENERATOR_NAMES
    assert c76["support_orbit_atlas"]["orbit_count"] == 3024
    assert c76["support_orbit_atlas"]["orbit_count_by_cardinality"] == CARDINALITY_VECTOR
    assert c76["support_orbit_atlas"]["orbit_size_spectrum"] == {
        str(size): count for size, count in ORBIT_SIZE_SPECTRUM.items()
    }

    c75_generators = {
        row["name"]: row for row in c75["lifted_symmetry"]["generators"]
    }
    label_permutations: list[list[int]] = []
    for name in EFFECTIVE_GENERATOR_NAMES:
        row = c75_generators[name]
        permutation = row["label_permutation"]
        assert sorted(permutation) == list(range(16))
        label_permutations.append([image + 1 for image in permutation])

    gap_lines = [
        "# Five generators of the faithful 16-label quotient of C75.",
        *[
            f"g{index}:=PermList({gap_list(permutation)});;"
            for index, permutation in enumerate(label_permutations)
        ],
        "G:=Group(g0,g1,g2,g3,g4);;",
        'Print("SIZE=",Size(G),"\\n");;',
        'Print("DESC=",StructureDescription(G),"\\n");;',
        "counts:=[];;",
        "spectrum:=List([1..160],value->0);;",
        "for k in [0..16] do",
        "  domains:=Combinations([1..16],k);;",
        "  orbitlist:=OrbitsDomain(G,domains,OnSets);;",
        "  Add(counts,Length(orbitlist));",
        "  for orbit in orbitlist do",
        "    spectrum[Length(orbit)]:=spectrum[Length(orbit)]+1;",
        "  od;",
        "od;",
        'Print("CARD=");;',
        "for k in [1..Length(counts)] do",
        '  if k>1 then Print(","); fi;',
        "  Print(counts[k]);",
        "od;",
        'Print("\\n");;',
        'Print("TOTAL=",Sum(counts),"\\n");;',
        'Print("SPECTRUM=");;',
        "first:=true;;",
        "for k in [1..Length(spectrum)] do",
        "  if spectrum[k]>0 then",
        '    if not first then Print(","); fi;',
        '    Print(k,":",spectrum[k]);',
        "    first:=false;",
        "  fi;",
        "od;",
        'Print("\\n");;',
        "QUIT;",
    ]
    run = subprocess.run(
        ["gap", "-q"],
        input="\n".join(gap_lines) + "\n",
        text=True,
        capture_output=True,
        check=True,
    )
    rows = parse_gap_output(run.stdout)
    assert rows["SIZE"] == "1920"
    # C76 writes the mathematically equivalent factor order S5 x C2 x D8.
    assert rows["DESC"] == "C2 x S5 x D8"
    cardinality_vector = [int(value) for value in rows["CARD"].split(",")]
    assert cardinality_vector == CARDINALITY_VECTOR
    assert int(rows["TOTAL"]) == 3024
    spectrum = {
        int(size): int(count)
        for size, count in (entry.split(":") for entry in rows["SPECTRUM"].split(","))
    }
    assert spectrum == ORBIT_SIZE_SPECTRUM

    print(json.dumps({
        "status": "GAP_CROSSCHECK_PASS",
        "c76_evidence_sha256": C76_EVIDENCE_SHA256,
        "effective_generator_names": list(EFFECTIVE_GENERATOR_NAMES),
        "gap_effective_group_order": 1920,
        "gap_structure": rows["DESC"],
        "gap_support_orbit_count": 3024,
        "gap_orbit_count_by_cardinality": cardinality_vector,
        "gap_orbit_size_spectrum": {str(size): count for size, count in spectrum.items()},
    }, sort_keys=True))


if __name__ == "__main__":
    main()
