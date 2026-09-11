"""Root read-only closure of scout30 originals; no scientific execution."""
import json
from pathlib import Path
import re
import runpy
import subprocess

R = Path('/root/autodl-tmp/symbolic_dynamics')
Q = R / 'docs/papers204_208_sequence/qa'
B = Q.parent / 'scouting/finite_systems_thirtieth'
D = runpy.run_path(str(Q / 'inspect_p209_a_initial.py'))
pin, obj, manifest = (D[n] for n in ('pin', 'obj', 'manifest'))
pin(__file__)
seal = 'b15bebabdb0f5db86f3c8ee993510cd19da129e795675176c02909724d0cc2e2'
assert pin(B / 'SHA256SUMS')['sha256'] == seal
outer = manifest(B / 'SHA256SUMS', complete=True)
assert len(outer) == 170
report = obj(B / 'final_documentary_audit/REPORT.json')
assert report['status'] == 'PASS_DOCUMENTARY_ONLY' and report['checks'] == 154565
assert report['scientific_executions'] == 0
assert pin(B / 'final_audit.py')['sha256'] == report['audit_source_sha256']
assert str(Path(report['python_executable']).resolve()) == report['python_resolved']
assert pin(report['python_resolved'])['sha256'] == report['python_sha256']

CURRENT = 'docs/papers204_208_sequence/'
RECENT = tuple(CURRENT + 'scouting/finite_systems_' + n + '/' for n in
               ('twenty_sixth', 'twenty_seventh', 'twenty_eighth'))
def banned(path):
    p = Path(path)
    parts = [x.lower() for x in p.parts]
    return (bool(re.search('p208|p209|ofs|fth', p.name, re.I))
            or bool(set(parts) & {'order_geometry_tenth','order_geometry_tenth_desk',
                'finite_systems_nineteenth','ofs_gate','fth_gate'})
            or any(re.match(r'(?:papers)?(?:208|209)(?:\D|$)', x) for x in parts)
            or (path.startswith(CURRENT) and not any(path.startswith(a) and len(p.parts)==5 for a in RECENT)))

initial = obj(B / 'discovery_paths.json')
corrected = obj(B / 'corrected_discovery_paths.json')
strict = obj(B / 'final_documentary_audit/strict_discovery_paths.json')
assert len(initial) == 7946 and len(corrected) == 7719 and len(strict) == 7704
assert len(set(corrected)) == 7719 and all(not banned(p) for p in corrected)
assert set(strict) <= set(corrected) and all(not banned(p) for p in strict)
assert obj(B / 'final_documentary_audit/initial_extra_hashed_paths.json') == sorted(set(initial) - set(corrected))
assert len(set(initial)-set(corrected)) == 227
delta = obj(B / 'final_documentary_audit/strict_vs_content_paths.json')
assert delta == {'strict_only': [], 'content_only': sorted(set(corrected)-set(strict))}
assert len(delta['content_only']) == 15 and all('fifth' in p.lower() for p in delta['content_only'])
for path, rows in [(B/'discovery_pins.sha256',initial), (B/'corrected_discovery_pins.sha256',corrected),
                   (B/'final_documentary_audit/strict_discovery_pins.sha256',strict)]:
    assert list(manifest(path, base=R)) == rows

read_paths, searches, pin_rows = [], [], 0
commands = []
for folder in sorted((B / 'evidence').iterdir()):
    row = obj(folder / 'receipt.json')
    assert row['kind'] == 'documentary' and row['exit'] == 0 and row['cwd'] == str(R)
    for stream in ('stdout','stderr'):
        assert pin(folder / stream)['sha256'] == row[stream + '_sha256']
    if (folder / 'paths.json').exists():
        paths = obj(folder / 'paths.json')
        pre = manifest(folder / 'before.sha256', base=R)
        post = manifest(folder / 'after.sha256', base=R)
        assert pre == post and list(pre) == paths
        pin_rows += 2 * len(pre)
        assert all(not banned(p) for p in paths)
        if row['argv'][0] == 'rg':
            assert paths == corrected and row['argv'][:4] == ['rg','-n','-i','--'] and row['argv'][5:] == paths
            searches.append(folder.name)
        else:
            assert row['argv'] == ['sed','-n','1,$p',paths[0]] and len(paths) == 1
            assert pin(folder/'stdout')['sha256'] == pin(R/paths[0])['sha256']
            assert pin(B/'snapshots'/paths[0])['sha256'] == pin(R/paths[0])['sha256']
            read_paths.extend(paths)
    commands.append({'receipt_path':str(folder/'receipt.json'),'receipt_pin':pin(folder/'receipt.json'),
                     'argv_count':len(row['argv']),'exit':row['exit']})
assert len(commands) == report['receipts'] == 15
assert len(searches) == 5 and pin_rows == report['pin_rows'] == 77206
assert read_paths == report['explicit_original_reads'] and len(read_paths) == 8
failure = obj(B/'final_documentary_audit/initial_metadata_failure.json')
for name,total,bad_count in [('00_path_discovery',36292,21775),('01_path_discovery_corrected',36298,21781)]:
    names=(B/'evidence'/name/'stdout').read_text().splitlines()
    assert len(names)==total and sum(banned(p) for p in names)==bad_count
    assert failure[name] == {'total':total,'excluded_metadata_rows':bad_count}

audit_commands=[]
for path in sorted((B/'final_documentary_audit').glob('*/receipt.json')):
    row=obj(path); folder=path.parent
    assert row['kind']=='documentary' and row['exit']==0 and row['cwd']==str(R)
    for stream in ('stdout','stderr'):
        assert pin(folder/stream)['sha256']==row[stream+'_sha256']
    assert pin(folder/'stderr')['bytes']==0
    if row['argv'][0]=='cmp':
        assert row['argv'][1]=='-s' and len(row['argv'])==4
        assert pin(row['argv'][2])['sha256']==pin(row['argv'][3])['sha256']
        assert pin(folder/'stdout')['bytes']==0
    else:
        assert row['argv'][0]=='rg'
        assert all(not banned(p) for p in (folder/'stdout').read_text().splitlines())
    audit_commands.append({'receipt_path':str(path),'receipt_pin':pin(path),'argv':row['argv'],'exit':0})
assert len(audit_commands)==18
comparisons=[]
for local, row in report['controls'].items():
    original=B/'controls'/local; alias=R/row['exact_alias']
    assert pin(original)['sha256']==pin(alias)['sha256']==row['sha256']
    argv=['/usr/bin/cmp','--',str(original),str(alias)]
    proc=subprocess.run(argv,cwd=R,env=D['ENV'],capture_output=True)
    comparisons.append({'argv':argv,'exit':proc.returncode,'stdout':proc.stdout.decode(),'stderr':proc.stderr.decode()})
    assert proc.returncode==0
for path in list(D['READS']): pin(path,fresh=True)
assert manifest(B/'SHA256SUMS',complete=True)==outer
print(json.dumps({'status':'PASS_ROOT_SCOUT30_COMPLETE_ORIGINAL_CLOSURE','sealed_payloads':170,
    'seal_sha256':seal,'initial_hash_paths':7946,'corrected_content_paths':7719,'strict_discovery_paths':7704,
    'preserved_extra_initial_hashed_paths':227,'preserved_excluded_metadata_counts':[21775,21781],
    'original_pin_rows':pin_rows,'complete_content_searches':searches,'explicit_original_copies':read_paths,
    'original_documentary_commands':commands,'audit_documentary_commands':audit_commands,
    'actual_new_root_raw_comparisons':comparisons,'all_current_paths_twice':len(D['READS']),
    'scientific_executions':0,'boundary':'Root original/documentary closure, not a new science replay, blind review, owner clearance or promotion.'},indent=2,sort_keys=True))
