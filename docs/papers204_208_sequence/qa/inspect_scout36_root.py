"""Root documentary original closure of sealed scout36; zero scientific runs."""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BASE=ROOT/'docs/papers204_208_sequence/scouting/finite_systems_thirty_sixth'
READS={}

def read(p):
    p=Path(p); assert p.is_file() and not p.is_symlink(),str(p)
    raw=p.read_bytes(); value={'sha256':sha256(raw).hexdigest(),'bytes':len(raw)}
    assert str(p) not in READS or READS[str(p)]==value,str(p)
    READS[str(p)]=value
    return raw

def j(p): return json.loads(read(p))

def pin(p,h):
    read(p); assert READS[str(p)]['sha256']==h,str(p)

def main():
    began=datetime.now(timezone.utc).isoformat(); read(Path(__file__).resolve())
    pin(BASE/'SHA256SUMS','d9e559921f2ba7af8b8ab5e919842e49a55297e86ed7ef781c8017347fe7a84a')
    manifest={}
    for line in read(BASE/'SHA256SUMS').decode().splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  (.+)',line); assert m
        h,rel=m.groups(); p=Path(rel)
        assert rel not in manifest and rel!='SHA256SUMS' and not p.is_absolute() and '..' not in p.parts
        manifest[rel]=h; pin(BASE/rel,h)
    physical=set()
    for p in BASE.rglob('*'):
        assert not p.is_symlink()
        if p.is_file(): physical.add(p.relative_to(BASE).as_posix())
    assert len(manifest)==152 and physical==set(manifest)|{'SHA256SUMS'}
    aliases={}
    for row in j(BASE/'CONTROL_ROLES.json'):
        p,q=Path(row['original_path']),Path(row['copy_path'])
        assert q==BASE/'controls'/p.name and row['role']=='physical_copy_before_body_read'
        pin(q,row['sha256']); aliases[(str(p),row['sha256'])]=q
        # Current controls are separately observed, never substituted for old pins.
        read(p)
    assert len(aliases)==3
    native=[]; originals={}; before_pins=0; sed_reads=[]; outer_count=None
    for recpath in sorted((BASE/'commands').glob('*/receipt.json')):
        folder=recpath.parent; rec=j(recpath)
        before=j(folder/'inputs_before.json'); assert before==j(folder/'inputs_after.json')
        assert sorted(before)==j(folder/'pathset.json') and len(before)==rec['input_count']
        assert rec['exit']==0 and rec['unchanged'] and rec['started_epoch']<=rec['finished_epoch']
        for name,h in before.items():
            pin(aliases.get((name,h),Path(name)),h)
            if folder.name!='11_documentary_audit':
                originals[name]=h; before_pins+=1
        for stream in ('stdout','stderr'): pin(folder/(stream+'.raw'),rec[stream+'_sha256'])
        argv=rec['argv']; assert isinstance(argv,list) and argv and rec['cwd']==str(ROOT)
        if argv[0]=='sed':
            assert argv[1]=='-n' and all(p in before for p in argv[3:])
            raw=b''.join(read(aliases.get((p,before[p]),Path(p))) for p in argv[3:])
            lines=re.findall(rb'[^\n]*\n|[^\n]+$',raw)
            ranges=[]
            for term in argv[2].split(';'):
                m=re.fullmatch(r'(\d+),(\d+)p',term); assert m
                start,stop=map(int,m.groups()); assert 1<=start<=stop
                ranges.append((start,stop))
            expected=b''.join(line for i,line in enumerate(lines,1) for start,stop in ranges if start<=i<=stop)
            assert read(folder/'stdout.raw')==expected and read(folder/'stderr.raw')==b''
            sed_reads.append({'receipt':folder.name,'argv':argv,'bytes':len(expected),'raw_reconstructed_from_exact_inputs':True})
        if folder.name=='11_documentary_audit': outer_count=len(before)
        native.append({'folder':folder.name,'argv':argv,'exit':rec['exit'],'input_count':len(before)})
    assert len(native)==20 and outer_count==250
    assert len(originals)==126 and before_pins==163 and len(sed_reads)==9
    result=j(BASE/'commands/11_documentary_audit/stdout.raw')
    assert result['status']=='PASS_DOCUMENTARY_ONLY' and result['historical_receipts']==19
    assert result['pin_occurrences_checked']==163 and result['distinct_original_pin_identities']==126
    assert result['scientific_executions']==result['candidate_pilots']==result['independent_reviews']==0
    reported=result['textual_command_reexecutions']
    assert len(reported)==9
    for row in reported:
        own=next(r for r in sed_reads if r['receipt']==row['receipt'])
        assert own['argv']==row['argv'] and own['bytes']==row['bytes'] and row['exit']==0 and row['raw_byte_equal']
    scope=j(BASE/'DISCOVERY_SCOPE.json'); assert len(scope['body_paths_selected'])==109 and scope['filenames_seen']==892
    search=read(BASE/'commands/06_scoped_body_search/stdout.raw'); assert len(search.splitlines())==15
    for name in scope['body_paths_selected']: assert name in originals
    for name,pages in [('register',12),('carlitz',13)]:
        assert read(BASE/'sources'/name/'body.raw').startswith(b'%PDF-')
        text=read(BASE/'commands'/(name+'_pdfinfo')/'stdout.raw').decode()
        assert re.search(r'^Pages:\s+'+str(pages)+r'\s*$',text,re.M)
    assert '13 pages' in read(BASE/'CLOSURE_AND_CORRECTION.md').decode()
    assert not (BASE/'CANONICAL.json').exists() and not (BASE/'__pycache__').exists()
    for p,want in READS.items():
        raw=Path(p).read_bytes(); assert want=={'sha256':sha256(raw).hexdigest(),'bytes':len(raw)},p
    print(json.dumps({'status':'ROOT_SCOUT36_COMPLETE_ORIGINAL_DOCUMENTARY_CLOSURE_NO_PROMOTION','started_utc':began,'ended_utc':datetime.now(timezone.utc).isoformat(),'complete_nonself_payloads':152,'native_documentary_records':20,'old_receipts':19,'outer_actual_input_pins':250,'old_pin_occurrences':163,'distinct_old_pin_identities':126,'actual_original_sed_reexecutions_checked':9,'root_sed_byte_reconstructions':sed_reads,'all_current_read_paths_checked_twice':len(READS),'read_map_sha256':sha256(json.dumps(READS,sort_keys=True).encode()).hexdigest(),'new_literal_systems':1,'original_scientific_pilots':0,'root_scientific_source_build_view_or_old_helper_executions':0,'admitted_candidates':0,'owner':'OWNER_AMBER','external_status':'HOLD_EXTERNAL'},sort_keys=True,indent=2))

if __name__=='__main__': main()
