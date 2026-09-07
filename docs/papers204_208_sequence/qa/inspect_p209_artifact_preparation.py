#!/usr/bin/env python3
"""Root static/original closure only. No artifact/lifecycle/scientific invocation."""
import ast
from hashlib import sha256
import json
from pathlib import Path
import subprocess

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BASE=ROOT/'docs/papers204_208_sequence/qa/p209_terminal_artifact_preparation'
READS={}; ALIASES={}; USED={}; COMMANDS=[]
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}

def read(p):
    p=Path(p); assert p.is_file() and not p.is_symlink(),str(p)
    data=p.read_bytes(); value={'sha256':sha256(data).hexdigest(),'bytes':len(data)}
    assert str(p) not in READS or READS[str(p)]==value,str(p)
    READS[str(p)]=value
    return data

def j(p):return json.loads(read(p))

def pin(p,v):
    p=Path(p); wanted=v if isinstance(v,str) else v['sha256']
    chosen=ALIASES.get((str(p),wanted),p)
    data=read(chosen)
    assert sha256(data).hexdigest()==wanted,(str(p),str(chosen))
    if isinstance(v,dict) and 'bytes' in v:assert len(data)==v['bytes']
    if chosen!=p:USED[str(p)+' @ '+wanted]=str(chosen)
    return chosen

def rows(p):
    result={}
    for line in read(p).decode().splitlines():
        h,n=line.split('  ',1); r=Path(n)
        assert not r.is_absolute() and '..' not in r.parts and n not in result and len(h)==64
        result[n]=h
    return result

def command(argv,wanted):
    r=subprocess.run(argv,cwd=ROOT,env=ENV,capture_output=True)
    COMMANDS.append({'argv':argv,'cwd':str(ROOT),'env':ENV,'exit_code':r.returncode,
                     'stdout':r.stdout.decode(),'stderr':r.stderr.decode()})
    assert r.returncode==wanted and r.stderr==b'',COMMANDS[-1]
    return r.stdout

def main():
    pin(BASE/'SHA256SUMS','3250ea718e5b0f358a8a54ba2365a53732d637a2f9686c017e1767e4cdcc7e51')
    sealed=rows(BASE/'SHA256SUMS')
    assert len(sealed)==347
    assert set(sealed)=={str(p.relative_to(BASE)) for p in BASE.rglob('*') if p.is_file() and p!=BASE/'SHA256SUMS'}
    assert all(not p.is_symlink() for p in BASE.rglob('*'))
    for n,h in sealed.items():pin(BASE/n,h)
    originals=j(BASE/'ORIGINAL_INPUTS.json'); assert len(originals)==33
    live_drift=[]
    for name,v in originals.items():
        copy=BASE/v['copy']; pin(copy,v)
        live=read(name)
        if sha256(live).hexdigest()!=v['sha256']:
            assert name in [str(ROOT/'SYMBOLIC_DYNAMICS_STATE.md'),str(ROOT/'docs/papers204_208_sequence/PIPELINE_STATE.md')]
            live_drift.append(name)
            ALIASES[name,v['sha256']]=copy
        original=pin(name,v)
        command(['/usr/bin/cmp','--',str(original),str(copy)],0)
    draft1=j(BASE/'draft_history/unexecuted_01/ROLE.json')
    assert draft1['status']=='UNEXECUTED_STATIC_DRAFT' and draft1['auditor_executions']==0
    for name,v in draft1['files'].items():
        path=BASE/'draft_history/unexecuted_01'/name;pin(path,v)
        ALIASES[str(BASE/name),v['sha256']]=path
    earlier=j(BASE/'checks/final_static/INPUTS_BEFORE.json')
    for name in ('audit_p209.py','lifecycle_audit.py','p209_specific.py.fragment'):
        v=earlier[str(BASE/name)];path=BASE/'draft_history/unexecuted_02'/name;pin(path,v)
        ALIASES[str(BASE/name),v['sha256']]=path
    receipts=sorted((BASE/'checks').glob('*/RECEIPT.json'));assert len(receipts)==47
    historical_input_rows=0; diff_rows=[]
    for f in receipts:
        folder=f.parent; rec=j(f); attempt=j(folder/'ATTEMPT.json')
        before=j(folder/'INPUTS_BEFORE.json');after=j(folder/'INPUTS_AFTER.json')
        assert before==after and rec['inputs_unchanged'] and rec['actual_exit']==rec['expected_exit']
        assert rec['env']==ENV and rec['cwd']==str(ROOT)
        assert all(rec[k]==attempt[k] for k in ('argv','cwd','env','started_utc'))
        for name,v in before.items():pin(name,v);historical_input_rows+=1
        for stream in ('stdout','stderr'):pin(folder/stream,rec[stream])
        assert read(folder/'stderr')==b''
        argv=rec['argv']
        if argv[0]=='/usr/bin/cmp':
            assert argv[:2]==['/usr/bin/cmp','--'] and rec['actual_exit']==0 and read(folder/'stdout')==b''
            assert read(pin(argv[2],before[argv[2]]))==read(pin(argv[3],before[argv[3]]))
        elif argv[0]=='/usr/bin/diff':
            assert argv[:3]==['/usr/bin/diff','-u','--'] and rec['actual_exit']==1
            if folder.name.startswith('final_v2_'):
                assert command(argv,1)==read(folder/'stdout');diff_rows.append(folder.name)
        else:
            assert argv[:5]==['/usr/bin/python3.10','-I','-S','-B','-c'] and rec['actual_exit']==0
            ast.parse(argv[5]); assert j(folder/'stdout')['status'].startswith('PASS_')
    assert len(diff_rows)==6
    execution=j(BASE/'FINAL_CHECK_EXECUTIONS_v2.json')
    assert len(execution)==7
    full=[]
    for row in execution:
        found=[p for p in receipts if j(p)==row];assert len(found)==1
        if row['argv'][0]=='/usr/bin/diff':full.append(read(found[0].parent/'stdout'))
    assert b'\n'.join(full)==read(BASE/'ADAPTATION_FINAL.diff')
    sources={}
    for p in sorted(BASE.rglob('*.py')):
        data=read(p).decode();tree=ast.parse(data);compile(tree,str(p),'exec')
        sources[str(p.relative_to(BASE))]=(sha256(data.encode()).hexdigest(),{n.name:ast.get_source_segment(data,n) for n in tree.body if isinstance(n,ast.FunctionDef)})
    assert len(sources)==18
    final=j(BASE/'FINAL_STATIC_CHECK_v2.json');doc=j(BASE/'FINAL_DOCUMENT_CHECK.json')
    for name,h in doc['python_sources'].items():assert sources[name][0]==h
    for name in final['exact_unchanged_P208_helper_blocks']:
        assert sources['audit_p209.py'][1][name]==sources['original_snapshot/audit_p208.py'][1][name]
    for name in final['exact_shared_P209_lifecycle_blocks']:
        assert sources['audit_p209.py'][1][name]==sources['lifecycle_audit.py'][1][name]
    for rel in doc['readme_local_links']:assert (BASE/rel).exists()
    contract=j(BASE/'INPUT_CONTRACT.json');assert contract['status']=='PREPARED_ONLY_NOT_EXECUTED_OR_ACCEPTED'
    pres=j(BASE/'PRESEAL.json')
    assert pres['payloads_before_this_record']==346 and len(pres['input_pins_before_and_after'])==346
    for rel,v in pres['input_pins_before_and_after'].items():pin(BASE/rel,v)
    assert not (ROOT/contract['future_output_scope']).exists()
    consumed=dict(READS)
    for name,v in consumed.items():
        data=Path(name).read_bytes();assert {'sha256':sha256(data).hexdigest(),'bytes':len(data)}==v,name
    print(json.dumps({'status':'PASS_ROOT_P209_ARTIFACT_PREPARATION_ORIGINAL_STATIC_CLOSURE_NOT_EXECUTED',
      'preparation_payloads':347,'original_copies':33,'historical_commands':47,'historical_input_rows':historical_input_rows,
      'fresh_copy_comparisons':33,'fresh_full_raw_diff_comparisons':len(diff_rows),'python_sources_parsed_not_executed':18,
      'unchanged_P208_helpers':len(final['exact_unchanged_P208_helper_blocks']),
      'exact_lifecycle_shared_blocks':len(final['exact_shared_P209_lifecycle_blocks']),
      'current_original_control_drift':live_drift,'historical_exact_roles_used':USED,
      'all_current_paths_checked_twice':len(consumed),'all_current_paths':consumed,'actual_root_commands':COMMANDS,
      'artifact_lifecycle_math_build_view_executions':0,'owner':'OWNER_AMBER','external':'HOLD_EXTERNAL'},sort_keys=True,indent=2))

if __name__=='__main__':main()
