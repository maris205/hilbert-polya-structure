"""Read-only bounded artifact audit; no map evaluation or independent review."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BASE=ROOT/'docs/papers204_208_sequence/scouting/finite_systems_twenty_ninth'
reads={}
aliases={}
counts={'manifest_payloads':0,'pin_rows':0,'snapshots':0,
        'command_receipts':0,'full_scope_searches':0,'raw_pairs':0}

def raw(path):
    path=path.absolute()
    value=path.read_bytes()
    h=hashlib.sha256(value).hexdigest()
    if path in reads:
        assert reads[path]==h, ('changed-during-read',str(path))
    reads[path]=h
    return value

def sha(path):
    return hashlib.sha256(raw(path)).hexdigest()

def jread(path):
    return json.loads(raw(path))

def alias(name,h,path):
    assert sha(path)==h, ('bad-alias',name,str(path))
    aliases[(name,h)]=path

initial={
 'SYMBOLIC_DYNAMICS_STATE.md':('initial_STATE.md','f4658260fc26911fba4df4f98675df842b73a179cf8af14823c91ac667444df0'),
 'docs/papers204_208_sequence/PIPELINE_STATE.md':('initial_PIPELINE.md','aeb4ca0405cf7ae25f56c2f0973bf2ee26aaba9e51e7555747bbd46743d422c1'),
 'docs/papers204_208_sequence/GIT_SYNC_RECEIPT.md':('initial_GIT_SYNC_RECEIPT.md','2f6998d2986831fa8776e31e9d336497e6ab37b114d1b13ef94879f3e2271c24')}
for name,(copy,h) in initial.items():
    alias(name,h,BASE/'history'/copy)
    counts['snapshots']+=1

for path in sorted((BASE/'history').glob('*.json')):
    value=jread(path)
    assert value['equal'] is True
    assert value['before']==value['after']
    assert len(value['copies'])==len(value['before'])
    assert [(r['path'],r['sha256']) for r in value['copies']]==[(r['path'],r['sha256']) for r in value['before']]
    for row in value['copies']:
        assert row['copy_sha256']==row['sha256']
        alias(row['path'],row['sha256'],BASE/row['copy'])
        counts['snapshots']+=1

old_capture=BASE/'history/capture_initial.py'
alias(str((BASE/'capture.py').relative_to(ROOT)),sha(old_capture),old_capture)
counts['snapshots']+=1

def pin(row):
    name,h=row['path'],row['sha256']
    assert isinstance(name,str) and re.fullmatch('[0-9a-f]{64}',h)
    # Explicit historical originals take precedence, without pretending that
    # their former mutable live names still have the old digest.
    target=aliases.get((name,h),ROOT/name)
    assert sha(target)==h, ('pin-failed',name,h,str(target))
    counts['pin_rows']+=1

def walk(value):
    if isinstance(value,list):
        for item in value:
            walk(item)
    elif isinstance(value,dict):
        if isinstance(value.get('path'),str) and isinstance(value.get('sha256'),str):
            pin(value)
        for item in value.values():
            if isinstance(item,(dict,list)):
                walk(item)

for path in sorted(BASE.rglob('*.json')):
    walk(jread(path))

selected=raw(BASE/'evidence/selected_paths.txt').decode().splitlines()
excluded=raw(BASE/'evidence/excluded_paths.txt').decode().splitlines()
discovered=raw(BASE/'evidence/discovery/stdout.bin').decode().splitlines()
selection=jread(BASE/'evidence/selection.json')
assert len(discovered)==selection['discovered_count']==34721
assert len(selected)==selection['count']==5341
assert selected==sorted(set(selected))
assert excluded==sorted(set(excluded))
assert not(set(selected)&set(excluded))
assert set(selected)|set(excluded)==set(discovered)

def choose(name):
    low=name.lower()
    current='docs/papers204_208_sequence/'
    return (low.endswith(('.md','.tex'))
        and not any(x in low for x in selection['excluded_path_substrings_casefolded'])
        and not any(x in Path(low).name for x in selection['excluded_basenames_containing_casefolded'])
        and (not low.startswith(current) or low.startswith(current+'scouting/')))

assert selected==sorted(n for n in discovered if choose(n))
for name in selected:
    low=name.lower()
    assert '/order_geometry_tenth/' not in low
    assert '/order_geometry_tenth_desk/' not in low
    assert '/finite_systems_tenth/' not in low
    assert '/finite_systems_nineteenth/' not in low
    assert '/finite_systems_twenty_eighth/' not in low
    assert '/208-' not in low and '/209-' not in low
    assert not any(x in Path(low).name for x in ('p208','p209','ofs','fth'))

discovery_pins=jread(BASE/'evidence/discovery_pins.json')
assert [r['path'] for r in discovery_pins]==selected

missing_initial={'history_focused','local_pdf_candidates','local_pdf_relevance'}
for path in sorted((BASE/'evidence').glob('*/receipt.json')):
    value=jread(path)
    before=jread(path.parent/'inputs_before.json')
    after=jread(path.parent/'inputs_after.json')
    assert before==after and value['inputs_equal'] is True
    assert len(before)==value['input_count']
    assert sha(path.parent/'stdout.bin')==value['stdout_sha256']
    assert sha(path.parent/'stderr.bin')==value['stderr_sha256']
    assert value['started_ns']<=value['finished_ns']
    assert value['cwd']==str(ROOT)
    assert value['exit']==0, ('nonzero-recorded-command',path,value['exit'])
    assert isinstance(value['argv'],list) and value['argv']
    if path.parent.name not in missing_initial:
        names={r['path'] for r in before}
        for arg in value['argv']:
            if (ROOT/arg).is_file():
                assert arg in names, ('argv-file-unpinned',path,arg)
    counts['command_receipts']+=1

for label in ('history_structure','history_cards','history_relational'):
    directory=BASE/'evidence'/label
    value=jread(directory/'receipt.json')
    assert value['argv'][:4]==['rg','-n','-i','--']
    assert value['argv'][5:]==selected
    pin_names={r['path'] for r in jread(directory/'inputs_before.json')}
    assert set(selected)<=pin_names
    assert len(pin_names)==len(selected)+1
    counts['full_scope_searches']+=1

for old,new,comparison in (
 ('history_focused','history_focused_v2','focused_v2_raw_cmp'),
 ('local_pdf_candidates','local_pdf_candidates_v2','pdf_candidates_v2_raw_cmp'),
 ('local_pdf_relevance','local_pdf_relevance_v2','pdf_relevance_v2_raw_cmp')):
    one=BASE/'evidence'/old/'stdout.bin'
    two=BASE/'evidence'/new/'stdout.bin'
    assert raw(one)==raw(two)
    oldreceipt=jread(BASE/'evidence'/old/'receipt.json')
    newreceipt=jread(BASE/'evidence'/new/'receipt.json')
    assert oldreceipt['argv']==newreceipt['argv']
    assert oldreceipt['input_count']==1 and newreceipt['input_count']==2
    comparison_receipt=jread(BASE/'evidence'/comparison/'receipt.json')
    assert comparison_receipt['argv']==['cmp',str(one.relative_to(ROOT)),str(two.relative_to(ROOT))]
    assert comparison_receipt['exit']==0
    assert raw(BASE/'evidence'/comparison/'stdout.bin')==b''
    assert raw(BASE/'evidence'/comparison/'stderr.bin')==b''
    counts['raw_pairs']+=1

preflight=jread(BASE/'evidence/local_169_preflight/stdout.bin')
assert preflight['verdict']=='UNAVAILABLE'
assert any('pypdf-not-installed' in warning for warning in preflight['warnings'])
assert sha(ROOT/preflight['file'])==preflight['sha256']
assert len(raw(BASE/'evidence/ji_html/stdout.bin'))==666780
assert b'2407.15889v3' in raw(BASE/'evidence/ji_html/stdout.bin')

allfiles=sorted(p for p in BASE.rglob('*') if p.is_file())
assert not any('__pycache__' in p.parts or p.name.startswith('pilot') for p in allfiles)
if '--manifest' in sys.argv:
    expected={}
    for line in raw(BASE/'SHA256SUMS').decode().splitlines():
        h,name=line.split('  ',1)
        assert name not in expected and name!='SHA256SUMS'
        assert not Path(name).is_absolute() and '..' not in Path(name).parts
        assert re.fullmatch('[0-9a-f]{64}',h)
        expected[name]=h
    actual={str(p.relative_to(BASE)) for p in allfiles if p!=BASE/'SHA256SUMS'}
    assert set(expected)==actual, ('manifest-coverage',len(expected),len(actual))
    for name,h in expected.items():
        assert sha(BASE/name)==h, ('manifest-pin',name)
    counts['manifest_payloads']=len(expected)

for path,h in list(reads.items()):
    assert hashlib.sha256(path.read_bytes()).hexdigest()==h, ('changed-after-read',str(path))
print(json.dumps({'status':'PASS_AUTHOR_READ_ONLY_ARTIFACT_AUDIT',
  'counts':counts,'unique_read_paths_rechecked':len(reads),
  'literal_definitions':1,'scientific_executions':0,'original_pilots':0,
  'initial_mixed_lifecycle_preserved':True,
  'initial_derived_filter_pin_defect_preserved_and_supplemented':True,
  'pdf_structural_preflight':'UNAVAILABLE',
  'no_independent_gate':True,'no_scientific_or_hermetic_replay':True},sort_keys=True))
