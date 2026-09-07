"""Root read-only original closure; no old audit, science, build or view run."""
from datetime import datetime, timezone
from hashlib import sha256
import ast
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BATCH=ROOT/'docs/papers204_208_sequence'
S=BATCH/'scouting/finite_systems_forty_first'
Q=BATCH/'qa/scout41_documentary_audit'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
WATCH={}

def read(path):
    p=Path(path); assert p.is_file(), str(p)
    if p.is_relative_to(ROOT): assert not p.is_symlink(), str(p)
    raw=p.read_bytes(); value={'sha256':sha256(raw).hexdigest(),'bytes':len(raw),'resolved':str(p.resolve())}
    if str(p) in WATCH: assert WATCH[str(p)]==value, str(p)
    WATCH[str(p)]=value; return raw

def j(path): return json.loads(read(path))

def pin(path,value):
    read(path); expected={'sha256':value} if isinstance(value,str) else value
    for key in ('sha256','bytes','resolved'):
        if key in expected: assert WATCH[str(path)][key]==expected[key], (str(path),key)

def seal(base,digest,count):
    pin(base/'SHA256SUMS',digest); rows={}
    for line in read(base/'SHA256SUMS').decode().splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  (.+)',line); assert m
        d,rel=m.groups(); p=Path(rel)
        assert not p.is_absolute() and '..' not in p.parts and rel not in rows and rel!='SHA256SUMS'
        rows[rel]=d; pin(base/rel,d)
    assert len(rows)==count
    assert not any(p.is_symlink() for p in base.rglob('*'))
    assert {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()}==set(rows)|{'SHA256SUMS'}
    return rows

def main():
    began=datetime.now(timezone.utc).isoformat()
    read(Path(__file__).resolve()); read(Path(sys.executable).resolve()); read(Path('/usr/bin/cmp'))
    sr=seal(S,'3d71f6f995f6b1b6f8cdd56c5e385613743c0b6be9bb752f0c1a454e9bd5053d',196)
    qr=seal(Q,'ae86e2901299fb700d3adc759f2ca994ffcdf89d262f89531dcc1250ad2904e7',96)
    aliases={r['original_path']:r for r in j(S/'CONTROL_ROLES.json')}
    assert len(aliases)==2
    for original,row in aliases.items():
        assert row['copy_path']==str(S/'controls'/Path(original).name)
        assert row['role']=='physical_copy_before_packaged_control_read_after_initial_navigation'
        pin(row['copy_path'],row['sha256'])
    def historical(original,digest):
        p=Path(original)
        if original in aliases:
            assert aliases[original]['sha256']==digest
            p=Path(aliases[original]['copy_path'])
        pin(p,digest); return p
    original_rows=[]; prior_inputs=set(); identities=set(); occurrences=0
    receipt_paths=sorted((S/'commands').glob('*/receipt.json'))
    assert len(receipt_paths)==31
    for rp in receipt_paths:
        base=rp.parent; command=j(rp); before=j(base/'inputs_before.json')
        assert before==j(base/'inputs_after.json') and command['unchanged'] and len(before)==command['input_count']
        assert command['cwd']==str(ROOT) and command['started_epoch']<=command['finished_epoch']
        assert command['exit']==(35 if base.name=='synchronism_download' else 0)
        assert command['role']=='native_documentary_not_scientific_execution'
        pins=[]; streams={}
        for name,digest in before.items():
            p=historical(name,digest); pins.append({'historical_path':name,'sha256':digest,'resolved_path':str(p)})
            if base.name!='08_documentary_audit':
                prior_inputs.add(p); identities.add((name,digest)); occurrences+=1
        for stream in ('stdout','stderr'):
            p=base/(stream+'.raw'); pin(p,command[stream+'_sha256'])
            streams[stream]={'path':str(p),'bytes':WATCH[str(p)]['bytes'],'sha256':WATCH[str(p)]['sha256']}
        original_rows.append({'command':base.name,'receipt_path':str(rp),'receipt':command,'pins':pins,'streams':streams})
    assert occurrences==199 and len(identities)==134
    outer=j(S/'commands/08_documentary_audit/inputs_before.json')
    expected_outer={S/name for name in sr if not name.startswith('commands/08_documentary_audit/') and name!='CLOSURE.md'}|prior_inputs
    assert len(expected_outer)==len(outer)==303 and set(outer)==set(map(str,expected_outer))
    detail=j(Q/'DETAIL.actual.json'); assert detail['historical_commands']==original_rows
    assert detail['outer_303_path_reconstruction']==sorted(map(str,expected_outer))
    native=detail['native_commands']; assert len(native)==43
    for row in native:
        assert row['exit']==0 and row['started_epoch']<=row['finished_epoch']
        assert row['cwd'] in (str(ROOT),str(S))
        for stream in ('stdout','stderr'):
            value=row['streams'][stream]; p=Path(value['path'])
            assert p.parent==Q; pin(p,value)
        if row['argv'][0]=='cmp':
            assert row['argv'][1]=='--' and len(row['argv'])==4
            assert read(row['argv'][2])==read(row['argv'][3])
            assert read(row['streams']['stdout']['path'])==read(row['streams']['stderr']['path'])==b''
    assert sum(row['argv'][0]=='cmp' for row in native)==28
    assert sum(row['argv'][0]=='sed' for row in native)==10
    assert sum(row['argv'][0]=='pdftotext' for row in native)==4
    original_qa=j(Q/'receipt.actual.json'); before=j(Q/'input_pins_before.json')
    assert before==j(Q/'input_pins_after.json') and len(before)==326
    assert original_qa['input_count']==326 and original_qa['exit']==0 and original_qa['unchanged']
    assert original_qa['argv']==['/root/miniconda3/bin/python','-B',str(Q/'check.py')]
    assert original_qa['invocation']==['/root/miniconda3/bin/python','-B',str(Q/'capture.py'),'run']
    assert original_qa['cwd']==str(ROOT)
    for p,digest in before.items(): pin(p,digest)
    for stream in ('stdout','stderr'): pin(Q/('audit.'+stream+'.raw'),original_qa[stream+'_sha256'])
    assert read(Q/'audit.stderr.raw')==b''
    expected=[{'fresh_native':native[0]}]
    for row in original_rows:
        expected.append({'historical_command':row['command'],'argv':row['receipt']['argv'],'exit':row['receipt']['exit'],
                         'checked_pins':len(row['pins']),'streams':row['streams']})
    expected.extend({'fresh_native':row} for row in native[1:]); expected.append(detail['summary'])
    assert read(Q/'audit.stdout.raw')==''.join(json.dumps(row,sort_keys=True)+'\n' for row in expected).encode()
    assert detail['summary']['result']=='PASS_DOCUMENTARY_ONLY'
    assert not (S/'sources/synchronism/body.raw').exists()
    assert read(S/'commands/synchronism_download/stderr.raw')==b'curl: (35) Recv failure: Connection reset by peer\n'
    j(Q/'PREFLIGHT_FAILURE.json')
    source_names=[S/n for n in ('audit.py','record.py','primary.py','discover.py')]+[Q/'check.py',Q/'capture.py']
    for path in source_names: ast.parse(read(path).decode(),filename=str(path))
    pairs=[(Path(r['copy_path']),Path(r['original_path'])) for r in aliases.values()]
    pairs.extend((Q/('pdf_layout_'+name+'.stdout.raw'),S/'sources'/name/'body.txt')
                 for name in ('schuele','synchronism_arxiv','fuks_sequences','powley'))
    fresh=[]
    for left,right in pairs:
        read(left); read(right); argv=['/usr/bin/cmp','--',str(left),str(right)]
        child=subprocess.run(argv,cwd=ROOT,env=ENV,capture_output=True,check=False)
        assert child.returncode==0 and child.stdout==child.stderr==b''
        fresh.append({'argv':argv,'cwd':str(ROOT),'environment':ENV,'exit_code':0,'stdout':'','stderr':''})
    for name,value in WATCH.items():
        p=Path(name); raw=p.read_bytes()
        assert value=={'sha256':sha256(raw).hexdigest(),'bytes':len(raw),'resolved':str(p.resolve())}
    print(json.dumps({'status':'PASS_ROOT_SCOUT41_ORIGINAL_DOCUMENTARY_CLOSURE','started_utc':began,
        'ended_utc':datetime.now(timezone.utc).isoformat(),'target_payloads':len(sr),'independent_qa_payloads':len(qr),
        'original_native_commands':31,'prior_commands':30,'prior_pin_occurrences':occurrences,'prior_identities':len(identities),
        'original_outer_inputset_reconstructed':len(expected_outer),'qa_inputs_checked':len(before),
        'qa_full_stdout_bytes_reconstructed':len(read(Q/'audit.stdout.raw')),'archived_fresh_qa_commands':len(native),
        'all_root_paths_rechecked_twice':len(WATCH),'root_read_map_sha256':sha256(json.dumps(WATCH,sort_keys=True).encode()).hexdigest(),
        'full_original_sources_read_and_parsed':len(source_names),'root_fresh_raw_comparisons':fresh,
        'new_scientific_build_render_or_view_executions':0,'new_admission_or_independent_math_review':False,
        'disposition':'NO_PROMOTION','owner':'OWNER_AMBER','external_status':'HOLD_EXTERNAL'},sort_keys=True,indent=2))

if __name__=='__main__':
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
    assert dict(os.environ)==ENV and Path.cwd()==ROOT
    main()
