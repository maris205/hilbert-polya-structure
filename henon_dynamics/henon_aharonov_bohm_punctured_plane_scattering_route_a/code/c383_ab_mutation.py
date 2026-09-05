#!/usr/bin/env python3
"""Hash-repaired hostile payload mutations must fail independent semantics."""
if not __debug__:raise RuntimeError("c383 mutation refuses optimized Python")
import argparse
import copy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
ROOT=Path(__file__).resolve().parents[1]
def main():
    argparse.ArgumentParser().parse_args();original=json.loads((ROOT/"results/c383_ab_evidence.json").read_text())
    changes=[("phase",lambda d:d["channels"][70].update(phase_over_pi=[1,2])),("order",lambda d:d["channels"][70].update(nu=[9,1])),("boundary",lambda d:d["channels"][32].update(limit_circle=False)),("gauge",lambda d:d["gauge_rows"][10].update(shifted_m=99)),("time_reversal",lambda d:d["time_reversal_rows"][1].update(position_preserving_TR=True)),("cutoff",lambda d:d["cutoff_rows"][70].update(shifted_phase_over_pi=[1,7])),("heat",lambda d:d["heat_rows"][0].update(radial_heat_kernel="1.25")),("cross_section",lambda d:d["cross_section_rows"][0].update(cross_section="2.5")),("scope",lambda d:d["scope_flags"].update(claims_target_zero_match=True)),("route_b",lambda d:d["route_a"].update(route_b_invocation_allowed=True)),("source",lambda d:d.update(source_commit="0"*40)),("yaml",lambda d:d["route_a_yaml"].update(raw_sha256="0"*64)),("missing_row",lambda d:d["channels"].pop()),("extra_key",lambda d:d.update(invented=True))]
    with tempfile.TemporaryDirectory(prefix="c383-hostile-") as directory:
        work=Path(directory)
        for label,change in changes:
            d=copy.deepcopy(original);change(d);d.pop("payload_sha256")
            d["payload_sha256"]=hashlib.sha256(json.dumps(d,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
            path=work/f"{label}.json";path.write_text(json.dumps(d))
            p=subprocess.run([sys.executable,"-B",str(ROOT/"code/c383_ab_checker.py"),str(path)],capture_output=True,text=True)
            assert p.returncode!=0,f"accepted hostile mutation {label}"
        for label,raw in (("duplicate",'{"x":1,"x":2}'),("nonfinite",'{"x":NaN}')):
            path=work/f"{label}.json";path.write_text(raw)
            p=subprocess.run([sys.executable,"-B",str(ROOT/"code/c383_ab_checker.py"),str(path)],capture_output=True,text=True)
            assert p.returncode!=0,label
        # Attack the actual --write entry point, with the manifest absent.
        # It must reject at the hard YAML gate before any artifact generation.
        original_yaml=(ROOT/"evaluations/route_a/HCS-C383/2026-09-05.yaml").read_text()
        yaml_attacks=(
            ("unknown_key",original_yaml+"unexpected_field: 1\n"),
            ("false_to_zero",original_yaml.replace("claims_target_zero_match: false","claims_target_zero_match: 0",1)),
            ("unquoted_date",original_yaml.replace("evaluation_date: '2026-09-05'","evaluation_date: 2026-09-05",1)),
        )
        for label,raw in yaml_attacks:
            case=work/("yaml_"+label);(case/"code").mkdir(parents=True)
            target=case/"evaluations/route_a/HCS-C383/2026-09-05.yaml";target.parent.mkdir(parents=True);target.write_text(raw)
            for script in ("c383_ab_checker.py","c383_release_manifest.py"):
                shutil.copy2(ROOT/"code"/script,case/"code"/script)
            p=subprocess.run([sys.executable,"-B",str(case/"code/c383_release_manifest.py"),"--write"],capture_output=True,text=True)
            assert p.returncode!=0 and "evaluation changed" in p.stdout+p.stderr,label
            assert not (case/"C383_RELEASE_MANIFEST.json").exists(),label
    print(f"C383 hostile mutation PASS: rejected={len(changes)+5}/{len(changes)+5}; repaired_hash_semantic={len(changes)}; actual_write_yaml_attacks=3")
if __name__=="__main__":main()
