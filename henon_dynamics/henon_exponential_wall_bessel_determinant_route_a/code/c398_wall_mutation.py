#!/usr/bin/env python3
"""Repaired-hash semantic mutations; standalone checker is the gate."""
if not __debug__:
    raise RuntimeError("c398 mutation refuses optimized Python")
import copy,hashlib,json,subprocess,sys,tempfile,shutil
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
EVAL=ROOT/"evaluations/route_a/HCS-C398/2026-09-05.yaml"
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def main():
    original=json.loads((ROOT/"results/c398_wall_evidence.json").read_text())
    changes=[
      ("candidate",lambda x:x.update(candidate_id="WRONG")),
      ("baseline",lambda x:x.update(source_commit="0"*40)),
      ("epoch bool",lambda x:x.update(fixed_epoch=True)),
      ("claim true",lambda x:x["scope_flags"].update(claims_target_zero_match=True)),
      ("claim integer zero",lambda x:x["scope_flags"].update(claims_target_zero_match=0)),
      ("route B true",lambda x:x["route_a"].update(route_b_invocation_allowed=True)),
      ("route B integer zero",lambda x:x["route_a"].update(route_b_invocation_allowed=0)),
      ("route upgrade",lambda x:x["route_a"]["tuple"].__setitem__(1,"A1_PASS_ANALYTIC")),
      ("overall upgrade",lambda x:x["route_a"].update(overall_verdict="ROUTE_A_PROMISING")),
      ("unknown field",lambda x:x.update(extra=1)),
      ("missing metadata",lambda x:x.pop("evidence_role")),

      ("series omission",lambda x:x["series"].pop()),
      ("series duplicate",lambda x:x["series"].append(x["series"][0])),
      ("numeric boolean",lambda x:x["series"][0].update(k=True)),
      ("numeric float",lambda x:x["series"][0].update(k=8.0)),
      ("noncanonical rational",lambda x:x["series"][0].update(a=[2,4])),
      ("imaginary sign",lambda x:x["series"][0]["terms"][1].__setitem__(1,[0,1])),
      ("term omission",lambda x:x["series"][0]["terms"].pop()),
      ("tail derivative",lambda x:x["tails"][0].update(series_derivative_bound=[0,1])),
      ("tail omission",lambda x:x["tails"].pop()),
      ("action sign",lambda x:x["actions"][0].update(action_constant=[1,1])),
      ("period factor",lambda x:x["actions"][0].update(period_log_coefficient=[1,1])),
      ("action omission",lambda x:x["actions"].pop()),
      ("determinant order",lambda x:x["controls"].update(energy_order=[1,1])),
      ("heat coefficient",lambda x:x["controls"].update(heat_log_coefficient_times_sqrt_pi=[1,2])),
      ("normalization",lambda x:x["controls"].update(forced_frequency_scale=[1,1])),
    ]
    source=yaml.safe_load(EVAL.read_text());source_text=yaml.safe_dump(source,sort_keys=False,allow_unicode=True)
    passed=0
    with tempfile.TemporaryDirectory(prefix="c398-hostile-") as tmp:
        ep=Path(tmp)/"evidence.json";yp=Path(tmp)/"evaluation.yaml"
        def reject(label,raw,ytext=source_text):
            nonlocal passed
            ep.write_text(raw);yp.write_text(ytext)
            p=subprocess.run([sys.executable,"-B",str(ROOT/"code/c398_wall_checker.py"),str(ep),"--evaluation",str(yp)],capture_output=True,text=True)
            assert p.returncode!=0,"survived "+label
            passed+=1
        for label,change in changes:
            x=copy.deepcopy(original);change(x);x.pop("payload_sha256")
            x["payload_sha256"]=hashlib.sha256(canonical(x)).hexdigest();reject(label,json.dumps(x))
        raw=json.dumps(original)
        reject("duplicate JSON",raw[:-1]+', "candidate_id":"HCS-C398"}')
        reject("NaN",raw[:-1]+', "extra":NaN}')
        reject("Infinity",raw[:-1]+', "extra":Infinity}')
        variants=[source_text+"\ncandidate_id: HCS-C398\n",source_text+"\nunknown: 1\n",
          source_text.replace("evaluation_date: '2026-09-05'","evaluation_date: 2026-09-05"),
          source_text+"\na: &v 1\nb: *v\n",source_text+"\n1: value\n",
          source_text.replace("route_b_invocation_allowed: false","route_b_invocation_allowed: 0"),
          source_text+"\n<<: {x: 1}\n",source_text+"\nnew: !!str abc\n",
          source_text.replace("claims_target_zero_match: false","claims_target_zero_match: true")]
        for i,v in enumerate(variants):
            assert v!=source_text
            reject("YAML "+str(i),raw,v)

    # Exercise the real release --write entry on a complete disposable package.
    # The independent evidence/evaluation gate runs before any manifest write.
    write_rejected=0
    with tempfile.TemporaryDirectory(prefix="C398-write-gate-") as tmp:
        repo=Path(tmp)/"repo";package=repo/"henon_dynamics"/ROOT.name
        shutil.copytree(ROOT,package)
        authority=repo/"flow_systems/skills/route-a-evaluator.md";authority.parent.mkdir(parents=True)
        shutil.copy2(ROOT.parents[1]/"flow_systems/skills/route-a-evaluator.md",authority)
        manifest=package/"C398_RELEASE_MANIFEST.json"
        sentinel=b"must not be overwritten\n"
        manifest.write_bytes(sentinel)
        local_e=package/"results/c398_wall_evidence.json"
        for mode in ("integer false flag","numeric boolean"):
            x=copy.deepcopy(original)
            if mode=="integer false flag":x["scope_flags"]["claims_target_zero_match"]=0
            else:x["fixed_epoch"]=True
            x.pop("payload_sha256");x["payload_sha256"]=hashlib.sha256(canonical(x)).hexdigest()
            local_e.write_text(json.dumps(x))
            p=subprocess.run([sys.executable,"-B",str(package/"code/c398_release_manifest.py"),"--write"],capture_output=True,text=True)
            assert p.returncode!=0 and manifest.read_bytes()==sentinel,"actual release write survived "+mode
            assert "checker.py" in p.stderr,"write failed before independent gate"
            write_rejected+=1
        local_e.write_text(json.dumps(original))
        cache=package/"code/__pycache__";cache.mkdir(exist_ok=True)
        rogue=cache/"unlisted.txt";rogue.write_text("unlisted physical payload")
        p=subprocess.run([sys.executable,"-B",str(package/"code/c398_release_manifest.py"),"--write"],capture_output=True,text=True)
        assert p.returncode and "physical ledger" in p.stderr and manifest.read_bytes()==sentinel
        write_rejected+=1;rogue.unlink()
        link=package/"payload-link";link.symlink_to(package/"README.md")
        p=subprocess.run([sys.executable,"-B",str(package/"code/c398_release_manifest.py"),"--write"],capture_output=True,text=True)
        assert p.returncode and "symlink payload refused" in p.stderr and manifest.read_bytes()==sentinel
        write_rejected+=1
    print(f"C398 actual release --write refusal PASS: {write_rejected}/4; sentinel unchanged; unlisted cache and symlink rejected")
    print(f"C398 hostile PASS: {len(changes)} repaired-hash + 3 JSON + 9 YAML = {passed}/{passed}")
if __name__=="__main__":main()
