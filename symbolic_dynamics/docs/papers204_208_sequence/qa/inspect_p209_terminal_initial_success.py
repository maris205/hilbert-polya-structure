"""Root original closure for a genuinely successful terminal artifact attempt.
Read-only. Requires externally supplied, previously inspected preparation pins.
Does not run the auditor, mathematical producer, build, render or lifecycle.
"""
import argparse
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
BATCH=ROOT/'docs/papers204_208_sequence'
PAPER=ROOT/'papers/209-ordered-fibre-threading'
OUT=BATCH/'qa/p209_terminal_artifact'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
WATCH={}


def read(path):
    p=Path(path); assert p.is_file(), str(p)
    if p.is_relative_to(ROOT): assert not p.is_symlink(), str(p)
    raw=p.read_bytes()
    value={'sha256':sha256(raw).hexdigest(),'bytes':len(raw),'resolved':str(p.resolve())}
    if str(p) in WATCH: assert WATCH[str(p)]==value, str(p)
    WATCH[str(p)]=value
    return raw


def j(path): return json.loads(read(path))


def pin(path,value):
    read(path); expected={'sha256':value} if isinstance(value,str) else value
    for key in ('sha256','bytes','resolved'):
        if key in expected: assert WATCH[str(path)][key]==expected[key], (str(path),key)


def path_of(name): return Path(name) if Path(name).is_absolute() else ROOT/name


def manifest(base,name,digest,count=None,complete=True):
    pin(base/name,digest); rows={}
    for line in read(base/name).decode().splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  (.+)',line); assert m, str(base/name)
        h,rel=m.groups(); p=Path(rel)
        assert not p.is_absolute() and '..' not in p.parts and rel not in rows and rel!=name
        rows[rel]=h; pin(base/rel,h)
    if count is not None: assert len(rows)==count, (str(base),len(rows),count)
    if complete:
        files=set()
        for p in base.rglob('*'):
            assert not p.is_symlink(), str(p)
            if p.is_file(): files.add(p.relative_to(base).as_posix())
        assert files==set(rows)|{name}, str(base)
    return rows


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--attempt',required=True)
    parser.add_argument('--preparation',required=True)
    parser.add_argument('--preparation-sha256',required=True)
    parser.add_argument('--auditor-sha256',required=True)
    args=parser.parse_args()
    assert re.fullmatch(r'initial_\d+',args.attempt)
    assert re.fullmatch(r'p209_terminal_artifact_revision_\d+',args.preparation)
    assert all(re.fullmatch(r'[0-9a-f]{64}',v) for v in (args.preparation_sha256,args.auditor_sha256))
    began=datetime.now(timezone.utc).isoformat()
    read(Path(__file__).resolve()); read(Path(sys.executable).resolve()); read(Path('/usr/bin/cmp'))
    prep=BATCH/'qa'/args.preparation; attempt=OUT/args.attempt
    prep_rows=manifest(prep,'SHA256SUMS',args.preparation_sha256)
    pin(prep/'audit_p209.py',args.auditor_sha256)
    native_seal=sha256(read(attempt/'SHA256SUMS')).hexdigest()
    manifest(attempt,'SHA256SUMS',native_seal,8)
    assert read(attempt/'executed_auditor_snapshot.py')==read(prep/'audit_p209.py')
    assert read(attempt/'executed_recorder_snapshot.py')==read(prep/'record_audit.py')
    command=j(attempt/'COMMAND.json'); prespawn=j(attempt/'ATTEMPT.json')
    expected_argv=['/usr/bin/python3.10','-I','-S','-B','-X',
                  'pycache_prefix='+str(attempt/'unused_pycache'),str(prep/'audit_p209.py'),
                  'terminal-artifact-after-actual-views']
    assert command['argv']==expected_argv and command['cwd']==str(ROOT) and command['environment']==ENV
    assert command['exit_code']==0 and command['status']=='COMPLETED' and command['failure'] is None
    assert command['inputs_unchanged'] and command['unused_cache_absent'] and not (attempt/'unused_pycache').exists()
    assert prespawn['status']=='ATTEMPTED' and prespawn['exit_code'] is None
    assert all(prespawn[k]==command[k] for k in ('argv','cwd','environment','started_utc'))
    before=j(attempt/'INPUTS_BEFORE.json'); assert before==j(attempt/'INPUTS_AFTER.json')
    for name,value in before.items(): pin(path_of(name),value)
    for stream in ('stdout','stderr'): pin(attempt/('audit.'+stream),command[stream])
    assert read(attempt/'audit.stderr')==b''
    result=j(attempt/'audit.stdout')
    assert result['schema']=='p209-terminal-artifact-audit-v1' and result['paper']=='P209'
    assert result['status']=='PASS_P209_TERMINAL_ARTIFACT_GATE'
    assert result['auditor_sha256']==args.auditor_sha256
    assert result['checks']==sum(result['checks_by_section'].values()) and result['checks']>0
    assert result['fresh_mathematical_executions']==result['fresh_builds']==result['fresh_page_views']==0
    assert result['owner']=='OWNER_AMBER' and result['external_status']=='HOLD_EXTERNAL'
    consumed=result['all_consumed_inputs_rechecked']
    assert len(consumed)==result['all_consumed_input_count']
    for name,value in consumed.items(): pin(path_of(name),value)
    for name,resolved in result['host_path_resolutions_rechecked'].items():
        assert Path(name).resolve(strict=True)==Path(resolved)
    manifests=result['complete_manifests_validated']
    for row in manifests:
        manifest(path_of(row['base']),row['name'],row['sha256'],row['entries'],row['complete_nonself'])
    for key,physical in result['explicit_historical_aliases_used'].items():
        original,digest=key.rsplit(' @ ',1)
        assert Path(original).is_absolute() and re.fullmatch(r'[0-9a-f]{64}',digest)
        pin(Path(physical),digest)
    for row in result['all_local_links_checked']:
        assert path_of(row['document']).is_file()
        dest=path_of(row['resolved_target']); assert dest.exists()
        if 'sha256' in row: pin(dest,row['sha256'])
    links=result['link_summary']
    assert links['local_links']==len(result['all_local_links_checked'])
    runtime=[]
    for phase in ('before','after'):
        sample=result['actual_auditor_runtime_'+phase]
        assert sample['environment']==ENV and sample['executable']=='/usr/bin/python3.10'
        assert sample['pycache_prefix']==str(attempt/'unused_pycache')
        assert all(s in sample['flags'] for s in ('optimize=0','isolated=1','no_site=1','dont_write_bytecode=1'))
        for row in sample['modules'].values(): pin(Path(row['path']),row)
        for name,value in sample['mapped_files'].items(): pin(Path(name),value)
        runtime.append({'phase':phase,'modules':len(sample['modules']),'mapped_files':len(sample['mapped_files'])})
    assert result['whole_paper_manifest_entries']==8231
    frozen=result['frozen_and_author']; assert [frozen[k] for k in ('author_entries','round0_payloads','round1_payloads','round2_payloads')]==[1985,1989,2003,2021]
    for letter in ('a','b'):
        assert result['accepted_reviews'][letter]['current_open']=={'critical':0,'major':0,'minor':0}
    assert result['terminal_builds']['pages']==[4,4] and result['terminal_builds']['actual_commands']==32
    assert result['actual_root_views']['actually_attested_pages']==4 and result['actual_root_views']['auditor_views']==0
    assert 'ARTIFACT_GATE_PENDING' in read(PAPER/'ROOT_LIFECYCLE.md').decode()
    raw_comparisons=[]
    pairs=[(attempt/'executed_auditor_snapshot.py',prep/'audit_p209.py'),
           (attempt/'executed_recorder_snapshot.py',prep/'record_audit.py'),
           (PAPER/'qa_final/cold_build_1/main.pdf',PAPER/'qa_final/cold_build_2/main.pdf')]
    for left,right in pairs:
        read(left); read(right); argv=['/usr/bin/cmp','--',str(left),str(right)]
        child=subprocess.run(argv,cwd=ROOT,env=ENV,capture_output=True,check=False)
        assert child.returncode==0 and not child.stdout and not child.stderr
        raw_comparisons.append({'argv':argv,'cwd':str(ROOT),'environment':ENV,'exit_code':0,
                                'stdout':child.stdout.decode(),'stderr':child.stderr.decode()})
    for name,wanted in WATCH.items():
        p=Path(name); raw=p.read_bytes()
        assert wanted=={'sha256':sha256(raw).hexdigest(),'bytes':len(raw),'resolved':str(p.resolve())}
    print(json.dumps({'status':'PASS_ROOT_COMPLETE_SUCCESSFUL_TERMINAL_ATTEMPT_ORIGINAL_INSPECTION',
        'started_utc':began,'ended_utc':datetime.now(timezone.utc).isoformat(),
        'paper':'P209','attempt':str(attempt),'preparation':str(prep),
        'preparation_manifest_sha256':args.preparation_sha256,'preparation_payloads':len(prep_rows),
        'native_attempt_manifest_sha256':native_seal,'native_attempt_payloads':8,
        'native_child_exit':command['exit_code'],'native_recorder_inputs':len(before),
        'audit_stdout':{'path':str(attempt/'audit.stdout'),**{k:WATCH[str(attempt/'audit.stdout')][k] for k in ('sha256','bytes')}},
        'auditor_sha256':args.auditor_sha256,'auditor_checks':result['checks'],
        'all_consumed_input_count':len(consumed),'all_root_read_paths_rechecked':len(WATCH),
        'root_read_map_sha256':sha256(json.dumps(WATCH,sort_keys=True).encode()).hexdigest(),
        'complete_manifests_rechecked':len(manifests),'explicit_historical_aliases_checked':len(result['explicit_historical_aliases_used']),
        'links_rechecked':links,'runtime_original_samples_checked':runtime,
        'frozen_and_author':frozen,'accepted_reviews':result['accepted_reviews'],
        'reused_original_strict_pairs':result['root_strict_replays_reused'],
        'terminal_builds':result['terminal_builds'],'actual_views_attestation':result['actual_root_views'],
        'fresh_raw_comparisons':raw_comparisons,'new_scientific_build_or_view_executions':0,
        'lifecycle_acceptance':False,'owner':'OWNER_AMBER','external_status':'HOLD_EXTERNAL'},sort_keys=True,indent=2))


if __name__=='__main__':
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
    assert dict(os.environ)==ENV and Path.cwd()==ROOT
    main()
