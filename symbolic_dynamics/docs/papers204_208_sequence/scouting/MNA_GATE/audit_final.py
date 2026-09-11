#!/usr/bin/env python3
"""Read-only scientific/evidence closure; emits actual full audit JSON."""
import hashlib
import json
from pathlib import Path
import re

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
GATE=ROOT/'docs/papers204_208_sequence/scouting/MNA_GATE'
checks=0

def check(ok,detail):
    global checks
    checks+=1
    if not ok:
        raise AssertionError(detail)

def pin(path):
    raw=Path(path).read_bytes()
    return {'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}

def read(path):
    return json.loads(Path(path).read_text())

roles=read(GATE/'INPUT_ROLES.json')['roles']
for row in roles:
    copied=Path(row['copy'])
    check(pin(copied)=={'sha256':row['sha256'],'bytes':row['bytes']},('physical_copy',row))
    # Current live metadata is explicitly NOT a reuse alias for a historical control.
    if row['role']!='orientation_snapshot_not_current_live_alias':
        check(Path(row['original']).read_bytes()==copied.read_bytes(),('actual_raw_origin_copy',row))
for line in (GATE/'INPUT_PINS.sha256').read_text().splitlines():
    sha,rel=line.split('  ',1)
    check(pin(ROOT/rel)['sha256']==sha,('input_pin',rel))
author=GATE/'inputs/author_lane40'
manifest=author/'SHA256SUMS'
check(pin(manifest)['sha256']=='807914fee97a2fa9380074688ad1ab803a601215e10011869f6a713075a9a55a','assigned_author_seal')
manifest_rows=manifest.read_text().splitlines()
check(len(manifest_rows)==155,'author_155_payloads')
names=[]
for line in manifest_rows:
    sha,rel=line.split('  ',1)
    names.append(rel)
    check(pin(author/rel)['sha256']==sha,('author_nested_seal',rel))
check(sorted(names)==sorted(str(p.relative_to(author)) for p in author.rglob('*') if p.is_file() and p!=manifest),'complete_author_nested_coverage')

# Validate six original pilot pins using explicit archival roles. Root clock's
# exact full native-read stdout is the author's documented physical origin role.
historical=read(author/'commands/17_one_mna_pilot/inputs_before.json')
clock_original=str(ROOT/'docs/papers204_208_sequence/scouting/MNA_ROOT_CLOCK_ATTEMPT/PROOF_PACKAGE.md')
pilot_resolution={}
for original,record in historical.items():
    if original==clock_original:
        resolved=author/'commands/16_root_clock_proof_read/stdout.raw'
    elif original.startswith(str(ROOT/'docs/papers204_208_sequence/scouting/finite_systems_fortieth')+'/'):
        resolved=author/Path(original).name
    else:
        resolved=Path(original)
    check(pin(resolved)==record,('original_pilot_exact_role',original,str(resolved)))
    pilot_resolution[original]={'resolved':str(resolved),'pin':record}

canonical=GATE/'CANONICAL.json'
data=read(canonical)
check(data['status']=='PASS' and data['state_count']==4095 and data['N_max']==12,'canonical_contract')
check(sum(data['checks'].values())==data['check_count']==115680,'named_assertion_census')
check(sum(len(b['states']) for b in data['boxes'])==4095,'all_state_rows')
check(sum(len(b['triangular_preimages']) for b in data['boxes'])==265,'all_bijection_rows')
pair=GATE/'evidence/pair03'
result=read(pair/'RESULT.json')
check(result['status']=='PASS' and result['known_inputs_unchanged']==997,'accepted_pair')
before=read(pair/'inputs_before.json')
after=read(pair/'inputs_after.json')
check(before==after,'accepted_before_after_key')
for path,record in before.items():
    check(pin(path)==record,('current_reuse_key',path))
for run in ('runtime01.json','runtime02.json'):
    runtime=read(pair/run)
    for path,record in runtime['files'].items():
        if path.startswith('/proc/'):
            continue
        check(path in before and before[path]==record,('observed_reusable_key',run,path))
    check(runtime['environment']=={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'},('actual_env',run))

native_receipts=[]
for lane in ('pair01','pair02','pair03'):
    for receipt in sorted((GATE/'evidence'/lane).glob('*/receipt.json')):
        row=read(receipt)
        for stream in ('stdout','stderr'):
            check(pin(receipt.parent/(stream+'.raw'))==row[stream],('native_stream',str(receipt),stream))
        check(row['exit']==0,('native_child_exit',str(receipt)))
        if receipt.parent.name in ('01_verify','02_verify'):
            check((receipt.parent/'stdout.raw').read_bytes()==canonical.read_bytes(),('actual_verifier_raw_bytes',str(receipt)))
        native_receipts.append(str(receipt.relative_to(GATE)))
for lane,exit_code in [('outer_pair_v2',1),('outer_pair_v3',0),('outer_compare_author',0)]:
    receipt=GATE/'evidence'/lane/'receipt.json'
    row=read(receipt)
    check(row['exit']==exit_code,('actual_outer_exit',lane))
    for stream in ('stdout','stderr'):
        check(pin(receipt.parent/(stream+'.raw'))==row[stream],('outer_native_stream',lane,stream))
    check(pin(row['argv'][-1])['sha256']==row['script_sha256'],('preserved_executed_outer_source',lane))
    native_receipts.append(str(receipt.relative_to(GATE)))
check(not (GATE/'evidence/pair01/RESULT.json').exists(),'no_fabricated_pair01_pass')
check(not (GATE/'evidence/pair02/RESULT.json').exists(),'no_fabricated_pair02_pass')
comparison=read(GATE/'evidence/author_comparison/RESULT.json')
check(comparison['status']=='PASS' and comparison['checks']==40969 and comparison['exit']==0,'full_author_comparison')
for rel,record in comparison['projection_pins'].items():
    check(pin(GATE/'evidence/author_comparison'/rel)==record,('full_projection_pin',rel))
check((GATE/'evidence/author_comparison/AUTHOR_PROJECTION.json').read_bytes()==(GATE/'evidence/author_comparison/INDEPENDENT_PROJECTION.json').read_bytes(),'full_projection_raw_bytes')
findings=read(GATE/'FINDINGS.json')
check(findings['open_count']==sum(f['state']=='open' for f in findings['findings'])==0,'zero_open_findings')
check(findings['resolved_count']==2,'resolved_finding_census')

links=[]
for name in ('CANDIDATE_GATE.md','SOURCE_AND_PROOF.md','REPLAY_LOG.md'):
    path=GATE/name
    for target in re.findall(r'\]\(([^)]+)\)',path.read_text()):
        if target.startswith(('http://','https://')):
            continue
        resolved=(path.parent/target).resolve()
        check(resolved.exists(),('local_report_link',name,target))
        links.append({'file':name,'target':target})
source_return_count=0
query_count=0
for path in sorted((GATE/'evidence').glob('mna_web*.actual.json')):
    web=read(path)
    check('args' in web and 'result' in web,('actual_web_record_schema',path.name))
    source_return_count+=1
    query_count+=len(web['args'].get('search_query',[]))
check(source_return_count==7 and query_count==13,'bounded_web_census')
summary={'status':'PASS','role':'actual_candidate_science_evidence_closure_before_final_nonself_seal',
         'checks':checks,'author_payloads':155,'input_roles':len(roles),
         'accepted_pair_known_inputs':len(before),'actual_native_receipts':native_receipts,
         'historical_pilot_exact_roles':pilot_resolution,'canonical':pin(canonical),
         'source_returns':source_return_count,'queries':query_count,'report_links':links,
         'not_claimed':['new_scientific_execution','OS_syscall_trace','manuscript_review',
                        'admission','global_novelty','central_lifecycle_update']}
print(json.dumps(summary,sort_keys=True,indent=2))
