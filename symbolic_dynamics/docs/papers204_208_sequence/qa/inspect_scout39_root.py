"""Read-only original closure; historical science/source/audit not rerun."""
import ast
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BASE=ROOT/'docs/papers204_208_sequence/scouting/finite_systems_thirty_ninth'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
WATCH={}

def read(path):
    path=Path(path); assert path.is_file() and not path.is_symlink(),str(path)
    raw=path.read_bytes(); row={'sha256':sha256(raw).hexdigest(),'bytes':len(raw)}
    assert str(path) not in WATCH or WATCH[str(path)]==row,str(path)
    WATCH[str(path)]=row; return raw

def obj(path): return json.loads(read(path))

def pin(path,digest):
    raw=read(path); assert sha256(raw).hexdigest()==digest,str(path)
    return raw

def lines(raw): return re.findall(rb'[^\n]*\n|[^\n]+$',raw)

def main():
    started=datetime.now(timezone.utc).isoformat()
    for path in (Path(__file__),Path(sys.executable),Path('/usr/bin/cmp')): read(path)
    seal=read(BASE/'SHA256SUMS'); wanted='bb3658e1551e3d0be3e463ba77b9702d702f0732937be99378b4e9b622ef17e4'
    assert sha256(seal).hexdigest()==wanted
    payload={}
    for line in seal.decode().splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  (.+)',line); assert m
        digest,name=m.groups(); p=Path(name)
        assert name not in payload and name!='SHA256SUMS' and not p.is_absolute() and '..' not in p.parts
        payload[name]=digest; pin(BASE/name,digest)
    physical=list(BASE.rglob('*')); assert not any(p.is_symlink() for p in physical)
    assert {p.relative_to(BASE).as_posix() for p in physical if p.is_file()}==set(payload)|{'SHA256SUMS'} and len(payload)==130
    roles=obj(BASE/'CONTROL_ROLES.json'); assert len(roles)==2
    aliases={r['original_path']:r for r in roles}
    for r in roles: pin(r['copy_path'],r['sha256'])
    def historical(path,digest):
        if path in aliases:
            assert aliases[path]['sha256']==digest
            path=aliases[path]['copy_path']
        pin(path,digest); return path
    audit=BASE/'commands/09_documentary_audit'
    expected_inputs={str(BASE/name) for name in payload if not name.startswith('commands/09_documentary_audit/') and name!='CLOSURE.md'}
    paths=sorted((BASE/'commands').glob('*/receipt.json')); assert len(paths)==20
    records=[]; oldrows=[]; occurrences=0; identities=set(); sed_count=rg_count=0
    for path in paths:
        folder=path.parent; r=obj(path); before=obj(folder/'inputs_before.json')
        assert before==obj(folder/'inputs_after.json') and r['unchanged'] and len(before)==r['input_count']
        assert r['exit']==0 and r['cwd']==str(ROOT) and r['started_epoch']<=r['finished_epoch']
        for name,digest in before.items():
            resolved=historical(name,digest)
            if folder!=audit:
                expected_inputs.add(resolved); occurrences+=1; identities.add((name,digest))
        stdout=pin(folder/'stdout.raw',r['stdout_sha256']); stderr=pin(folder/'stderr.raw',r['stderr_sha256'])
        assert stderr==b''
        argv=r['argv']
        if argv[0]=='sed':
            selected=[tuple(map(int,p[:-1].split(','))) for p in argv[2].split(';')]
            source=[]
            for name in argv[3:]: source.extend(lines(read(historical(name,before[name]))))
            assert stdout==b''.join(line for n,line in enumerate(source,1) for lo,hi in selected if lo<=n<=hi)
            sed_count+=1
        elif argv[0]=='rg' and '--files' not in argv:
            if '--' in argv:
                split=argv.index('--'); selected=argv[split+1:]; pattern=argv[split-1]
            else: selected=argv[3:]; pattern=argv[2]
            expression=re.compile(pattern,re.I if '-i' in argv else 0); hits=[]
            for name in selected:
                for n,line in enumerate(read(name).decode().split('\n'),1):
                    if expression.search(line): hits.append((name+':' if len(selected)>1 else '')+str(n)+':'+line)
            assert Counter(stdout.decode().splitlines())==Counter(hits); rg_count+=1
        if folder!=audit:
            oldrows.append({'command':folder.name,'exit':0,'pins':len(before),'raw_sed_reexecution_byte_exact':argv[0]=='sed'})
        records.append({'command':folder.name,'inputs':len(before),'exit':0,'stdout_bytes':len(stdout)})
    assert len(expected_inputs)==238 and expected_inputs==set(obj(audit/'inputs_before.json'))
    assert occurrences==278 and len(identities)==130 and sed_count==6 and rg_count==4
    raw_rows=[json.loads(row) for row in read(audit/'stdout.raw').decode().splitlines()]
    assert raw_rows[:19]==oldrows and len(raw_rows)==22
    for name,pages,size in [('whirling',21,428547),('poset_whirling',26,578124)]:
        folder=BASE/'sources'/name; pdf=read(folder/'body.raw')
        assert pdf.startswith(b'%PDF-') and len(pdf)==size
        headers=read(folder/'headers.raw')
        assert re.findall(rb'^HTTP/[^ ]+ (\d{3})[^\r\n]*',headers,re.M)[-1]==b'200'
        info=read(BASE/'commands'/(name+'_pdfinfo')/'stdout.raw')
        assert re.search(rb'^Pages:\s+'+str(pages).encode()+rb'$',info,re.M)
        assert re.search(rb'^File size:\s+'+str(size).encode()+rb' bytes$',info,re.M)
        expected={'documentary_extraction_argv':['pdftotext','-layout',str(folder/'body.raw'),'-'],
            'exit':0,'byte_exact_to_recorded_layout_text':True,'actual_primary_pdf_pages':pages,'actual_primary_pdf_bytes':size}
        assert expected in raw_rows[19:21]
    assert raw_rows[-1]=={'checked_historical_pin_occurrences':278,'control_copy_aliases':2,'distinct_historical_identities':130,
        'failed_scheduler_proposals':1,'first_query_matches':346,'independent_mathematical_reviews':0,'inventory_paths':922,
        'new_valid_autonomous_maps':0,'pilots':0,'primary_layout_reextractions_byte_exact':2,'prior_commands':19,
        'raw_sed_reexecutions_byte_exact':6,'result':'PASS_DOCUMENTARY_ONLY','scientific_executions':0,
        'second_query_matches':1,'selected_original_notes':111}
    assert read(audit/'stdout.raw')==''.join(json.dumps(r,sort_keys=True)+'\n' for r in raw_rows).encode()
    scope=obj(BASE/'DISCOVERY_SCOPE.json'); inventory=sorted(set(read(BASE/'commands/03_filename_inventory/stdout.raw').decode().splitlines()))
    assert len(inventory)==scope['metadata_paths']==922 and len(scope['selected_paths'])==111
    assert set(scope['selected_paths'])<=set(inventory) and sum(scope['denied_counts'].values())+111==922
    for name in ('04_scoped_body_search','08_whirling_history'):
        argv=obj(BASE/'commands'/name/'receipt.json')['argv']
        assert argv[argv.index('--')+1:]==scope['selected_paths']
    for n in range(1,4):
        assert obj(BASE/f'search{n:02d}_input.json') and obj(BASE/f'search{n:02d}_output.json')
    for path in BASE.glob('*.py'): ast.parse(read(path))
    argv=['/usr/bin/cmp','--',str(audit/'inputs_before.json'),str(audit/'inputs_after.json')]
    run=subprocess.run(argv,cwd=ROOT,env=ENV,capture_output=True,check=False)
    assert run.returncode==0 and run.stdout==run.stderr==b''
    for path,row in WATCH.items():
        raw=Path(path).read_bytes(); assert row=={'sha256':sha256(raw).hexdigest(),'bytes':len(raw)},path
    print(json.dumps({'status':'PASS_ROOT_SCOUT39_ORIGINAL_DOCUMENTARY_CLOSURE_NO_PROMOTION','started_utc':started,
        'ended_utc':datetime.now(timezone.utc).isoformat(),'payloads':130,'seal_sha256':wanted,
        'current_paths_read_twice':len(WATCH),'read_map_sha256':sha256(json.dumps(WATCH,sort_keys=True).encode()).hexdigest(),
        'reconstructed_historical_audit_inputs':238,'old_pin_occurrences':278,'old_identities':130,
        'original_native_records':records,'LF_only_read_reconstructions':sed_count,'rg_raw_multiset_reconstructions':rg_count,
        'fresh_raw_comparison':{'argv':argv,'exit':0,'stdout':'','stderr':''},'original_audit_layout_reextractions_inspected':2,
        'root_new_source_acquisitions_or_scientific_or_old_audit_executions':0,'independent_mathematical_review':False,
        'external_status':'HOLD_EXTERNAL'},sort_keys=True,indent=2))

if __name__=='__main__':
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
    assert dict(os.environ)==ENV and Path.cwd()==ROOT
    main()
