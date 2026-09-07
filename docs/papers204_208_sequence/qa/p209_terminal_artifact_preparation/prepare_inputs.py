"""Documentary preparation helper only; never imports/invokes target auditors."""
import ast
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from datetime import datetime, timezone

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BASE=ROOT/'docs/papers204_208_sequence/qa/p209_terminal_artifact_preparation'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
INPUTS=[
 ('AGENTS.md','AGENTS.md'),
 ('SYMBOLIC_DYNAMICS_STATE.md','SYMBOLIC_DYNAMICS_STATE.md'),
 ('docs/papers204_208_sequence/PIPELINE_STATE.md','PIPELINE_STATE.md'),
 ('.agents/skills/symbolic-dynamics-research/SKILL.md','PROJECT_SKILL.md'),
 ('docs/research_state/WORKFLOW.md','WORKFLOW.md'),
 ('docs/papers204_208_sequence/ARTIFACT_CONTRACT.md','ARTIFACT_CONTRACT.md'),
 ('docs/papers197_201_sequence/HOSTILE_REVIEW_PROTOCOL.md','HOSTILE_REVIEW_PROTOCOL.md'),
 ('docs/papers204_208_sequence/qa/audit_p208.py','audit_p208.py'),
 ('docs/papers204_208_sequence/qa/p208_terminal_artifact/record_audit.py','record_p208_audit.py'),
 ('docs/papers204_208_sequence/qa/p208_terminal_artifact/lifecycle_audit.py','p208_lifecycle_audit.py'),
 ('docs/papers204_208_sequence/qa/p208_terminal_artifact/REPORT.md','P208_ARTIFACT_REPORT.md'),
 ('docs/papers204_208_sequence/qa/p208_terminal_artifact/LIFECYCLE_REPORT.md','P208_LIFECYCLE_REPORT.md'),
 ('docs/papers204_208_sequence/qa/p208_terminal_artifact/SHA256SUMS','P208_ARTIFACT_SHA256SUMS'),
 ('docs/papers204_208_sequence/qa/P208_TERMINAL_ROOT_INSPECTION.md','P208_TERMINAL_ROOT_INSPECTION.md'),
 ('docs/papers204_208_sequence/qa/P208_LIFECYCLE_ROOT_INSPECTION.md','P208_LIFECYCLE_ROOT_INSPECTION.md'),
 ('docs/papers204_208_sequence/qa/p209_terminal_preparation/README.md','TERMINAL_PREPARATION_README.md'),
 ('docs/papers204_208_sequence/qa/p209_terminal_preparation/GATE_CONTRACT.json','TERMINAL_GATE_CONTRACT.json'),
 ('docs/papers204_208_sequence/qa/p209_terminal_preparation/SHA256SUMS','TERMINAL_PREPARATION_SHA256SUMS'),
 ('docs/papers204_208_sequence/qa/p209_terminal_preparation/root_terminal_builds.py','root_terminal_builds.py'),
 ('docs/papers204_208_sequence/qa/p209_terminal_preparation/root_launch_terminal.py','root_launch_terminal.py'),
 ('docs/papers204_208_sequence/qa/p209_terminal_preparation/ADAPTATION_FINAL.diff','TERMINAL_ADAPTATION_FINAL.diff'),
 ('docs/papers204_208_sequence/qa/p209_terminal_preparation/SOURCE_PINS.json','TERMINAL_SOURCE_PINS.json'),
 ('docs/papers204_208_sequence/qa/p209_round2_preparation/ACCEPTANCE_INPUT_CONTRACT.json','ROUND2_ACCEPTANCE_INPUT_CONTRACT.json'),
 ('docs/papers204_208_sequence/qa/p209_round2_preparation/freeze_p209_round2.py','freeze_p209_round2.py'),
 ('docs/papers204_208_sequence/qa/P209_A_ROOT_DELTA_INSPECTION.actual.json','P209_A_ROOT_DELTA_INSPECTION.actual.json'),
 ('docs/papers204_208_sequence/qa/P209_B_ROOT_DELTA_INSPECTION.actual.json','P209_B_ROOT_DELTA_INSPECTION.actual.json'),
 ('docs/papers204_208_sequence/reviews/p209_a/CURRENT_FINDINGS.json','A_CURRENT_FINDINGS.json'),
 ('docs/papers204_208_sequence/reviews/p209_b/CURRENT_FINDINGS.json','B_CURRENT_FINDINGS.json'),
 ('docs/papers204_208_sequence/reviews/p209_b/SHA256SUMS','B_FINAL_REVIEW_SHA256SUMS'),
 ('docs/papers204_208_sequence/reviews/p209_b/delta_check_02/EXACT_HISTORY_ALIASES.json','B_EXACT_HISTORY_ALIASES.json'),
 ('docs/papers204_208_sequence/reviews/p209_a/delta_check_02/HISTORICAL_PIN_ROLE_MAP.json','A_HISTORICAL_PIN_ROLE_MAP.json'),
 ('papers/209-ordered-fibre-threading/AUTHOR_MANIFEST.sha256','AUTHOR_MANIFEST.sha256'),
 ('papers/209-ordered-fibre-threading/ROOT_ADOPTION.md','ROOT_ADOPTION.md')]


def info(path):
    p=Path(path);value=hashlib.sha256()
    with p.open('rb') as stream:
        for chunk in iter(lambda:stream.read(1024*1024),b''):value.update(chunk)
    return {'sha256':value.hexdigest(),'bytes':p.stat().st_size,'resolved':str(p.resolve()),
            'symlink':os.readlink(p) if p.is_symlink() else None}


def save(path,value):
    with Path(path).open('x') as stream:
        json.dump(value,stream,indent=2,sort_keys=True);stream.write('\n')


def command(label,argv,inputs,expected):
    folder=BASE/'checks'/label;folder.mkdir(parents=True)
    before={str(p):info(p) for p in inputs}
    save(folder/'INPUTS_BEFORE.json',before)
    attempted={'argv':argv,'cwd':str(ROOT),'env':ENV,'started_utc':datetime.now(timezone.utc).isoformat()}
    save(folder/'ATTEMPT.json',attempted)
    run=subprocess.run(argv,cwd=ROOT,env=ENV,capture_output=True,check=False)
    for name,raw in [('stdout',run.stdout),('stderr',run.stderr)]:
        with (folder/name).open('xb') as stream:stream.write(raw)
    after={str(p):info(p) for p in inputs};save(folder/'INPUTS_AFTER.json',after)
    result={**attempted,'actual_exit':run.returncode,'expected_exit':expected,
            'inputs_unchanged':before==after,'stdout':info(folder/'stdout'),'stderr':info(folder/'stderr'),
            'scope':'Actual documentary copy/diff/syntax command only; no target auditor/build/science/view invocation.'}
    save(folder/'RECEIPT.json',result)
    assert run.returncode==expected and before==after and not run.stderr,(label,result)
    return result,run.stdout


def intake():
    target=BASE/'original_snapshot';target.mkdir()
    before={str(ROOT/source):info(ROOT/source) for source,_ in INPUTS}
    commands=[];copies={}
    for index,(source,name) in enumerate(INPUTS,1):
        original=ROOT/source;copy=target/name
        shutil.copyfile(original,copy)
        row,_=command('copy_'+str(index).zfill(2),['/usr/bin/cmp','--',str(original),str(copy)],[original,copy],0)
        commands.append(row);copies[str(original)]={'copy':str(copy.relative_to(BASE)),**before[str(original)]}
    assert before=={str(ROOT/source):info(ROOT/source) for source,_ in INPUTS}
    save(BASE/'ORIGINAL_INPUTS.json',copies)
    save(BASE/'INTAKE_RESULT.json',{'status':'PASS_PHYSICAL_PREPARATION_INPUT_COPIES',
        'originals':len(copies),'actual_copy_comparisons':len(commands),'all_originals_unchanged':True,
        'target_auditor_build_view_executions':0,'commands':commands})
    print(json.dumps({'status':'PASS_PHYSICAL_PREPARATION_INPUT_COPIES','originals':len(copies),'comparisons':len(commands)}))


if __name__=='__main__':
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and sys.flags.optimize==0
    assert dict(os.environ)==ENV and Path.cwd()==ROOT
    assert sys.argv[1:]==['intake']
    intake()
