"""Root read-only closure of revision02, not a target-auditor execution."""
import ast
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BATCH=ROOT/'docs/papers204_208_sequence'
BASE=BATCH/'qa/p209_terminal_artifact_revision_02'
OLD=BATCH/'qa/p209_terminal_artifact_revision_01'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
WATCH={}

def read(p):
    p=Path(p); assert p.is_file(),str(p)
    if p.is_relative_to(ROOT): assert not p.is_symlink(),str(p)
    raw=p.read_bytes(); row={'sha256':sha256(raw).hexdigest(),'bytes':len(raw)}
    assert str(p) not in WATCH or WATCH[str(p)]==row,str(p)
    WATCH[str(p)]=row
    return raw

def j(p): return json.loads(read(p))

def pin(p,row):
    read(p); want={'sha256':row} if isinstance(row,str) else row
    for k in ('sha256','bytes'):
        if k in want: assert WATCH[str(p)][k]==want[k],(str(p),k)

def pins(rows):
    for p,row in rows.items(): pin(Path(p),row)

def manifest(base,count,digest):
    pin(base/'SHA256SUMS',digest); rows={}
    for line in read(base/'SHA256SUMS').decode().splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  (.+)',line); assert m
        h,rel=m.groups(); p=Path(rel)
        assert rel not in rows and rel!='SHA256SUMS' and not p.is_absolute() and '..' not in p.parts
        rows[rel]=h; pin(base/rel,h)
    files=set()
    for p in base.rglob('*'):
        assert not p.is_symlink()
        if p.is_file(): files.add(p.relative_to(base).as_posix())
    assert len(rows)==count and files==set(rows)|{'SHA256SUMS'}
    return rows

def fs(raw):
    tree=ast.parse(raw); compile(tree,'<source-only>','exec',dont_inherit=True,optimize=0)
    return {n.name:ast.get_source_segment(raw,n) for n in tree.body if isinstance(n,ast.FunctionDef)}

def main():
    began=datetime.now(timezone.utc).isoformat()
    read(Path(__file__)); read(Path(sys.executable)); read(Path('/usr/bin/diff'))
    manifest(BASE,79,'6e9c86fad5802ed82df5ffa78e3f7d7bc9c3bec00a04892c96e002db121ed6ed')
    final=j(BASE/'STATIC_RESULT.json')
    assert final['status']=='PASS_STATIC_PREPARATION_ONLY_NOT_ARTIFACT_GATE'
    before=final['original_inputs_before']; assert before==final['original_inputs_after'] and len(before)==2070
    pins(before); pins(final['central_controls_unchanged'])
    for name,row in final['second_complete_original_package_validation'].items():
        assert row['complete_nonself']; manifest(BATCH/'qa'/name,row['payloads'],row['sha256'])
    manifest(BASE/'unexecuted_draft_before_link_registration',7,'501f7f25cd3dc6756926d73ad089a5a297eb3fe75c70c45d709e468c821bda14')
    schema=j(BASE/'SCHEMA_PROJECTIONS.json'); added=j(BASE/'LINK_ADDITION_INTAKE.json')
    shapes=schema['json_shapes']; assert len(shapes)==schema['source_data_records']==1017
    for p in shapes: j(Path(p))
    original=j(BASE/'SCHEMA_INPUTS_BEFORE.json'); assert original==j(BASE/'SCHEMA_INPUTS_AFTER.json')
    pins(original); assert len(original)==1812
    assert added['inputs_before']==added['inputs_after']; pins(added['inputs_before'])
    copies=schema['physical_copies']+added['copies']; commands=schema['actual_cmp_commands']+added['actual_cmp_commands']
    assert len(copies)==len(commands)==34
    for copy,row in zip(copies,commands):
        pin(Path(copy['copy']),copy)
        if not Path(copy['original']).is_relative_to(BASE):
            pin(Path(copy['original']),copy); assert read(copy['original'])==read(copy['copy'])
        assert row['argv']==['/usr/bin/cmp','--',copy['original'],copy['copy']]
        assert row['cwd']==str(ROOT) and row['env']==ENV
        assert row['exit_code']==0 and row['stdout']==row['stderr']==''
    assert len([r for r in copies if not Path(r['original']).is_relative_to(BASE)])==27
    for name,value in schema['observations'].items():
        if isinstance(value,bool): assert value,name
        elif isinstance(value,dict) and 'equal' in value: assert value['equal'],name
        elif isinstance(value,list):
            for row in value:
                for key in ('embedded_equal','attempt_shared_fields_equal','map_union_equal','attempt_fields_equal'):
                    if key in row: assert row[key],(name,key)
    layout=j(BASE/'LINK_LAYOUT.json'); links=j(BASE/'LINK_ADDITIONS_RESULT.json')
    for data,a,b in [(layout,'original_inputs_before','original_inputs_after'),(links,'inputs_before','inputs_after')]:
        assert data[a]==data[b]; pins(data[a])
    assert len(layout['links'])==links['complete_line_scan_local_links_recomputed']==1528
    assert len(layout['missing'])==links['old_missing']==176 and links['remaining_missing']==[]
    assert links['resolved_by_exact_origin']=={'A01':9,'B01':10,'author_workspace':157}
    assert links['registered_origin_roles_by_group']=={'A01':9,'A02':9,'B01':2,'author_workspace':33}
    for row in links['origin_comparisons']:
        assert row['before'] in layout['links'] and row['after']['exists']
        assert Path(row['after']['destination']).exists()
    changes={'audit_p209.py':{'reviews','revision_originals_and_failure','pages_and_links'},'record_audit.py':{'main'},'lifecycle_audit.py':set()}
    recipes=j(BASE/'SOURCE_EDITS.json'); recorded=j(BASE/'SOURCE_FUNCTION_CHECKS.json'); unchanged={}; diffs=[]
    assert set(recipes)==set(changes)
    for name,edits in recipes.items():
        old=read(OLD/name).decode(); actual=read(BASE/name).decode(); built=old
        assert read(OLD/name)==read(BASE/'original_snapshot'/(OLD/name).relative_to(ROOT))
        for row in edits:
            assert built.count(row['old'])==row['required_old_occurrences']==1
            built=built.replace(row['old'],row['new'],1)
        assert built==actual
        first,second=fs(old),fs(actual); assert set(first)==set(second)
        different={k for k in first if first[k]!=second[k]}; assert different==changes[name]
        imports=lambda raw:[ast.dump(n) for n in ast.parse(raw).body if isinstance(n,(ast.Import,ast.ImportFrom))]
        assert imports(old)==imports(actual)
        unchanged[name]=len(first)-len(different)
        for key in first:
            assert recorded[name]['literal_function_source_comparisons'][key]=={'original_sha256':sha256(first[key].encode()).hexdigest(),'prepared_sha256':sha256(second[key].encode()).hexdigest(),'equal':first[key]==second[key]}
        pin(BASE/name,final['source_pins'][name])
    assert unchanged=={'audit_p209.py':32,'record_audit.py':3,'lifecycle_audit.py':36}
    for row,native in zip(j(BASE/'DIFF_COMMANDS.json'),final['fresh_final_actual_raw_diffs']):
        name=Path(row['argv'][-1]).name
        expected=['/usr/bin/diff','-u','--',str(BASE/'original_snapshot'/(OLD/name).relative_to(ROOT)),str(BASE/name)]
        assert row['argv']==native['argv']==expected
        assert row['cwd']==native['cwd']==str(ROOT) and row['env']==native['env']==ENV
        assert row['exit_code']==native['exit_code']==1
        for stream in ('stdout','stderr'):
            pin(BASE/row[stream+'_path'],row[stream+'_sha256']); pin(BASE/native[stream]['path'],native[stream])
            assert read(BASE/row[stream+'_path'])==read(BASE/native[stream]['path'])
        child=subprocess.run(expected,cwd=ROOT,env=ENV,capture_output=True,check=False)
        assert child.returncode==1 and child.stdout==read(BASE/row['stdout_path']) and child.stderr==b''
        diffs.append({'argv':expected,'cwd':str(ROOT),'environment':ENV,'exit_code':1,'stdout':child.stdout.decode(),'stderr':child.stderr.decode()})
    assert len(diffs)==3 and read(BASE/'ADAPTATION.diff')==''.join(r['stdout'] for r in diffs).encode()
    parsed=[]
    for p in sorted(BASE.rglob('*.py')):
        compile(ast.parse(read(p),filename=str(p)),str(p),'exec',dont_inherit=True,optimize=0); parsed.append(p.relative_to(BASE).as_posix())
    assert parsed==final['python_files_parsed_compiled_not_executed'] and len(parsed)==18
    for number,digest in [('01','6c070f981a6b6f6ae05363e32f8047efda4f2a0e8c458f22dd9152990ccfb7cf'),('02','87df565befc65ce9d96c25cf6e28f470521bea9207750c17ee1123ed6384c09b')]:
        attempt=BATCH/('qa/p209_terminal_artifact/initial_'+number)
        assert j(attempt/'COMMAND.json')['exit_code']==1
        assert j(attempt/'INPUTS_BEFORE.json')==j(attempt/'INPUTS_AFTER.json')
        assert read(attempt/'audit.stdout')==b''; pin(attempt/'audit.stderr',digest)
    assert not (BATCH/'qa/p209_terminal_artifact/initial_03').exists()
    for path,want in WATCH.items():
        raw=Path(path).read_bytes(); assert want=={'sha256':sha256(raw).hexdigest(),'bytes':len(raw)},path
    print(json.dumps({'status':'PASS_ROOT_REVISION02_COMPLETE_STATIC_ORIGINAL_PREFLIGHT_NOT_TARGET_EXECUTION','started_utc':began,'ended_utc':datetime.now(timezone.utc).isoformat(),'revision_payloads':79,'original_paths_checked_twice':2070,'all_current_read_paths_checked_twice':len(WATCH),'read_map_sha256':sha256(json.dumps(WATCH,sort_keys=True).encode()).hexdigest(),'original_physical_copies':27,'unexecuted_draft_copies':7,'archived_actual_cmp_commands':34,'old_packages_and_two_real_failures_unchanged':True,'source_replace_once_and_imports_unchanged':True,'literal_unchanged_functions':unchanged,'python_sources_static_only':len(parsed),'schema_records':1017,'static_local_links':1528,'static_missing_after_exact_origin_registration':0,'fresh_actual_raw_diffs':diffs,'target_science_build_view_lifecycle_executions':0,'owner':'OWNER_AMBER','external_status':'HOLD_EXTERNAL'},sort_keys=True,indent=2))

if __name__=='__main__':
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
    assert dict(os.environ)==ENV and Path.cwd()==ROOT
    main()
