#!/usr/bin/env python3
"""Hash-repaired semantic attacks plus actual write-mode locked-YAML attacks."""
if not __debug__:raise RuntimeError("c386 mutation refuses optimized Python")
import argparse, copy, hashlib, json, shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()
def main():
    argparse.ArgumentParser().parse_args()
    original=json.loads((ROOT/"results/c386_szego_evidence.json").read_text())
    attacks=[]
    for key in ("d","Q","M","energy","defect","d_dot","d_ddot","kappa_squared","compact_lower_bound"):
        def attack(x,key=key):x["generic_rows"][0][key][0]+=1
        attacks.append((key,attack))
    for key in ("alpha","b","c","p","velocity","d_star","native_determinant_coefficients","regime"):
        def attack(x,key=key):
            row=x["cascade_rows"][0]
            if key=="regime":row[key]="compact"
            elif key=="d_star":row[key]=[0,1]
            elif key=="velocity":row[key][0][0][0]+=1
            elif key=="native_determinant_coefficients":row[key][1]=[1,1]
            elif key=="alpha":row[key][0]+=1
            else:row[key][0][0]+=1
        attacks.append((key,attack))
    attacks.extend([
       ("rank-zero-threshold",lambda x:x["constant_rows"][0].update(cascade=True)),
       ("bool-to-zero",lambda x:x["constant_rows"][0].update(cascade=0)),
       ("count",lambda x:x["counts"].update(cascade=73)),
       ("drop-row",lambda x:x["inner_rows"].pop()),
       ("extra-row-field",lambda x:x["inner_rows"][0].update(unregistered=True)),
       ("scope",lambda x:x["scope_flags"].update(claims_root_number=True)),
       ("route",lambda x:x["route_a"].update(route_b_invocation_allowed=True)),
       ("same-det-control",lambda x:x["control_rows"][0]["bounded"].update(regime="cascade")),
       ("source-baseline",lambda x:x.update(source_commit="0"*40))])
    rejected=[]
    with tempfile.TemporaryDirectory(prefix="c386-hostile-") as directory:
        work=Path(directory)
        for name,mutate in attacks:
            data=copy.deepcopy(original);mutate(data);data.pop("payload_sha256")
            data["payload_sha256"]=hashlib.sha256(canon(data)).hexdigest()
            path=work/"attack.json";path.write_text(json.dumps(data))
            p=subprocess.run([sys.executable,"-B",str(ROOT/"code/c386_szego_checker.py"),str(path)],capture_output=True,text=True)
            assert p.returncode,(name,"accepted");rejected.append(name)
        for name,text in (("duplicate-json",'{"candidate_id":1,"candidate_id":2}'),
                          ("nonfinite-json",'{"x":NaN}')):
            path=work/"attack.json";path.write_text(text)
            p=subprocess.run([sys.executable,"-B",str(ROOT/"code/c386_szego_checker.py"),str(path)],capture_output=True,text=True)
            assert p.returncode;rejected.append(name)
    yaml_source=ROOT/"evaluations/route_a/HCS-C386/2026-09-05.yaml"
    for name,transform in (
        ("yaml-unknown-key",lambda s:s+"\nunknown_release_field: false\n"),
        ("yaml-false-to-zero",lambda s:s.replace("claims_root_number: false","claims_root_number: 0")),
        ("yaml-unquoted-date",lambda s:s.replace("evaluation_date: '2026-09-05'","evaluation_date: 2026-09-05"))):
        with tempfile.TemporaryDirectory(prefix="c386-yaml-write-") as directory:
            w=Path(directory);(w/"code").mkdir();(w/"evaluations/route_a/HCS-C386").mkdir(parents=True)
            for script in ("c386_release_manifest.py","c386_szego_checker.py"):
                shutil.copy2(ROOT/"code"/script,w/"code"/script)
            (w/"evaluations/route_a/HCS-C386/2026-09-05.yaml").write_text(transform(yaml_source.read_text()))
            p=subprocess.run([sys.executable,"-B",str(w/"code/c386_release_manifest.py"),"--write"],capture_output=True,text=True)
            assert p.returncode and "evaluation changed" in p.stdout+p.stderr
            assert not (w/"C386_RELEASE_MANIFEST.json").exists();rejected.append(name)
    print("C386 hostile PASS",json.dumps(dict(rejected=len(rejected),attempted=len(attacks)+5,attacks=rejected)))
if __name__=="__main__":main()
