"""Root reception of the actual final B delta and all original keys.

Uses documentary patterns from the fully read root A/B receivers, without
importing or rerunning any of them. The historical B pre-decision absence
gate is not rerun after acceptance. No science, build or page view occurs.
"""
from pathlib import Path
from hashlib import sha256
import difflib
import json
import os
import re
import shlex

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT/'docs/papers211_215_sequence'
B = BASE/'reviews/p211_b'
RR = BASE/'qa/p211_b_report_root'
PAPER = ROOT/'papers/211-kernel-image-projection-feedback'
OUT = Path(__file__).resolve().parent
KEYS = {}
checks = 0


def need(ok, label):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(label)


def read(path, expected=None):
    p = Path(path)
    data = p.read_bytes()
    key = {'bytes':len(data), 'sha256':sha256(data).hexdigest(),
           'resolved':str(p.resolve(strict=True)),
           'symlink':os.readlink(p) if p.is_symlink() else None}
    need(str(p) not in KEYS or KEYS[str(p)] == key, ('stable full key',str(p)))
    if expected is not None:
        need(all(key[k] == v for k,v in expected.items()), ('all expected fields',str(p)))
    KEYS[str(p)] = key
    return data


def unique(rows):
    out = {}
    for k,v in rows:
        need(k not in out, ('duplicate JSON key',k))
        out[k] = v
    return out


def parse(body):
    return json.loads(body, object_pairs_hook=unique)


def doc(path):
    return parse(read(path))


def manifest(path, count, exact=False, absolute=False):
    path = Path(path)
    rows = {}
    for line in read(path).decode().splitlines():
        m = re.fullmatch(r'([a-f0-9]{64})  (.+)', line)
        need(m is not None, 'complete manifest row')
        digest,name = m.groups()
        need(name not in rows and '..' not in Path(name).parts, 'unique safe member')
        need(absolute or not Path(name).is_absolute(), 'directory-relative package base')
        p = (Path(name) if Path(name).is_absolute() else ROOT/name) if absolute else path.parent/name
        need(p != path and p.is_file() and (absolute or not p.is_symlink()), 'exact package versus runtime-input link policy')
        read(p, {'sha256':digest})
        key_name = str(p) if absolute else name
        need(key_name not in rows, 'no mixed-spelling input collision')
        rows[key_name] = KEYS[str(p)]
    need(len(rows) == count, 'all original manifest rows')
    if exact:
        actual = set()
        for p in path.parent.rglob('*'):
            need(not p.is_symlink() and (p.is_file() or p.is_dir()), 'ordinary package tree')
            if p.is_file():
                need(p.stat().st_nlink == 1, 'physical non-hardlinked package file')
                actual.add(p.relative_to(path.parent).as_posix())
        need(actual == set(rows)|{path.name}, 'complete exact package inventory')
    return rows


def native(value, exit_code=0):
    need(set(value) >= {'request','result'}, 'actual native envelope')
    parts = [value['result']]
    for p in value.get('polls',[]):
        need(p['request']['session_id'] == parts[-1]['session_id'], 'actual native session')
        parts.append(p['result'])
    need(parts[-1].get('exit_code') == exit_code and not parts[-1].get('session_id'), 'actual terminal exit')
    need(all('chunk_id' in p and 'output' in p for p in parts), 'complete actual returned records')
    raw = ''.join(p['output'] for p in parts).encode()
    need(not raw.startswith(b'Warning: truncated output'), 'no native truncation header; literal source-code text remains ordinary data')
    return raw


def state(path, content=True):
    p = Path(path)
    row = {'lexists':os.path.lexists(p), 'exists':p.exists(), 'is_file':p.is_file(),
           'is_dir':p.is_dir(), 'is_character_device':p.is_char_device(),
           'resolved':str(p.resolve()), 'symlink':os.readlink(p) if p.is_symlink() else None}
    if p.is_char_device():
        st = p.stat()
        row['character_device'] = {'major':os.major(st.st_rdev),'minor':os.minor(st.st_rdev),'mode':st.st_mode}
    if content and p.is_file():
        read(p)
        row.update({k:KEYS[str(p)][k] for k in ['bytes','sha256']})
    return row


need(Path.cwd() == ROOT and not (OUT/'RESULT.json').exists(), 'fixed new reception')
read(__file__)
read(B/'SHA256SUMS', {'bytes':3549,'sha256':'45b7c0337259da2fccb078cf4d7b84ec7228a16a6bf6089167c19a26c477ca46'})
final = manifest(B/'SHA256SUMS',39,True)
need(sum(k['bytes'] for k in final.values()) == 6076055, 'payload-only final byte sum')
read(B/'DELTA.md',{'bytes':8851,'sha256':'c4520571bd1774c499c9a91fafc430c94b3a02af189761d99235a9714ba31a2d'})
read(B/'DELTA_ACCEPTANCE.json',{'bytes':47212,'sha256':'7115031d29bb860325eab69498e042c57cfb33210a50e450f114ee4879eb69ad'})
decision = doc(B/'DELTA_ACCEPTANCE.json')
need(decision['decision'] == 'SAME_B_ACCEPTED_EXACT_NO_CHANGE' and decision['review_result'] == 'PASS'
     and decision['reviewer'] == '/root/round211_rational_scout/relation_primary_sources'
     and decision['response_type'] == 'NO_CHANGE' and decision['delta_received'] is True
     and decision['delta_accepted'] is True, 'actual same B accepted exact response')
for field in ['actual_response','actual_response_keys','root_report_reception','root_response_native']:
    row = decision[field]
    read(row['path'],row['key'])
census = decision['current_finding_census']
need(census['current_open_total'] == 0 and census['new_findings'] == []
     and all(census[s] == {'open':0} for s in ['Critical','Major','Minor'])
     and census['historical_report_pending_flags_preserved'] is True, 'current exact zero-open census')
need(all(decision[k] is False for k in ['round2_created_or_accepted_by_B','paper_complete','batch_complete']),
     'no later gate supplied')
delta_native = doc(B/'evidence/DELTA_DOCUMENTARY_NATIVE01.json')
need(delta_native['request'] == {'cmd':'/usr/bin/python3.10 -I -S -B docs/papers211_215_sequence/reviews/p211_b/receive_delta_documents.py',
     'workdir':str(ROOT),'max_output_tokens':300000,'yield_time_ms':1000}, 'exact original B delta request')
need(delta_native['result']['chunk_id'] == '07e5f1', 'actual B check identity')
delta = parse(native(delta_native))
need(delta['documentary_checks'] == 154857 and delta['read_paths'] == 1774
     and len(delta['read_inputs']) == 1774, 'full actual B delta key/census')
for p,k in delta['read_inputs'].items():
    need(set(k) == {'bytes','sha256','resolved','symlink'}, 'entire original four-field rich key')
    read(p,k)
pins = manifest(B/'DELTA_INPUT_PINS.sha256',1774,absolute=True)
need(pins == delta['read_inputs'], 'complete absolute pins match complete original rich keys')
same = decision['same_B_documentary_reception']
read(B/same['source'],same['source_key'])
need(same['actual_native'] == 'evidence/DELTA_DOCUMENTARY_NATIVE01.json'
     and same['actual_chunk'] == '07e5f1' and same['actual_exit_code'] == 0
     and same['documentary_checks'] == 154857 and same['full_rich_read_paths'] == 1774,
     'decision binds actual source/check evidence')
need(all(delta[k] == 0 for k in ['scientific_executions','submitted_imports','builds','page_views']),
     'actual documentary non-science scope')
prior = doc(RR/'INPUTS.json')
response_inputs = doc(RR/'RESPONSE_INPUTS.json')
response = doc(RR/'RESPONSE_KEYS.json')
need(len(prior)==1751 and len(response_inputs)==1757, 'two original root ledgers')
for ledger in [prior,response_inputs]:
    for p,k in ledger.items(): read(p,k)
need(set(response_inputs)-set(prior) == {str(RR/n) for n in ['response_keys.py','INPUTS.json','NATIVE07.json','RESULT.json','RECEPTION.md']}
     | {str(BASE/'P211_B_RESPONSE.md')}, 'exact six lifecycle additions')
report = manifest(B/'REPORT_SHA256SUMS',31)
prep = manifest(B/'PREPARATION_SHA256SUMS',19)
need(report == response['report_stage_payload_keys'] == decision['report_stage']['all_report_stage_payload_keys']
     and sum(k['bytes'] for k in report.values()) == 4711295, 'all unchanged report originals')
need(set(final)-set(report) == {'REPORT_SHA256SUMS','DELTA.md','DELTA_ACCEPTANCE.json','DELTA_INPUT_PINS.sha256',
     'receive_delta_documents.py','evidence/DELTA_DOCUMENTARY_NATIVE01.json','evidence/DELTA_ORIGINAL_READS01.json',
     'evidence/DELTA_CLOSING_METADATA_NATIVE01.json'}, 'exact final additions to old 31-payload stage')
r0 = manifest(PAPER/'frozen_round0/SHA256SUMS',32,True)
r1 = manifest(PAPER/'frozen_round1/SHA256SUMS',83,True)
need(KEYS[str(PAPER/'frozen_round1/SHA256SUMS')]['sha256'] == decision['reviewed_round1_manifest_sha256'], 'reviewed exact Round1')
author = decision['exact_author_delta']
need(author['before_after'] == response['author_before_after'] == delta['author_before_after']
     and set(author['before_after']) == set(r0), 'every complete before/after row')
need(all(author[k] == [] for k in ['additions','removals','modifications'])
     and author['payloads'] == 32 and author['all_live_Round0_Round1_raw_triples_equal'] is True, 'actual zero author delta')
for name,row in author['before_after'].items():
    need(row['before'] == row['after'] == prior[str(PAPER/name)], 'historical before/after identity')
    data = read(PAPER/name,row['after'])
    need(data == read(PAPER/'frozen_round1'/name,row['frozen']) == read(PAPER/'frozen_round0'/name), 'all actual author raw triples')
live = {p.relative_to(PAPER).as_posix() for p in PAPER.rglob('*') if p.is_file()
        and not p.relative_to(PAPER).parts[0].startswith('frozen_round')}
need(live == set(r0), 'complete live author membership unchanged')
binding = doc(BASE/'qa/p211_b_pair_binding/BINDING.json')
lock = doc(binding['runtime_lock']['path'])
need(len(lock['files']) == 122 and len(lock['configuration']['paths']) == 69
     and len(lock['configuration']['memberships']) == 5 and len(lock['loader_search_directory_states']) == 9,
     'complete runtime/settings dimensions')
for p,k in lock['files'].items(): read(p,k)
for p,k in lock['configuration']['paths'].items(): need(state(p)==k,('all configured path fields',p))
for p,k in lock['configuration']['memberships'].items():
    path=Path(p)
    now={'directory':state(path,False),'members':{}}
    if path.is_dir(): now['members']={x.name:state(x,False) for x in sorted(path.iterdir())}
    need(now==k,('complete directory membership',p))
for p,k in lock['loader_search_directory_states'].items(): need(state(p,False)==k,('loader state',p))

# Receive every actual new native read without executing an archived command.
reads = doc(B/'evidence/DELTA_ORIGINAL_READS01.json')['reads']
need(len(reads)==30,'all delta-stage original reads')
sed_count=0
diff_count=0
for i,record in enumerate(reads):
    argv=shlex.split(record['request']['cmd'])
    raw=native(record,1 if argv[0]=='diff' else 0)
    if argv[:2]==['sed','-n']:
        m=re.fullmatch(r'(\d+),(\d+)p',argv[2]);need(m is not None,'exact sed extent')
        path=Path(argv[3]);path=path if path.is_absolute() else ROOT/path
        if path in [ROOT/'SYMBOLIC_DYNAMICS_STATE.md',BASE/'PIPELINE_STATE.md']:
            path=BASE/'qa/control_before_four_desk_accepted/originals'/path.name
        lines=read(path).splitlines(keepends=True)
        need(raw==b''.join(lines[int(m[1])-1:int(m[2])]),('entire actual read slice',i))
        sed_count+=1
    elif argv[:2]==['diff','-u']:
        before,after=[read(ROOT/p).decode().splitlines(keepends=True) for p in argv[2:]]
        expected=list(difflib.unified_diff(before,after,fromfile=argv[2],tofile=argv[3]))
        actual=raw.decode().splitlines(keepends=True)
        need(actual[0].split('\t',1)[0]=='--- '+argv[2]
             and actual[1].split('\t',1)[0]=='+++ '+argv[3]
             and actual[2:]==expected[2:],('complete actual source diff hunks; original timestamp headers retained',i))
        diff_count+=1
    else:
        need(i in [7,10] and argv[0] in ['rg','wc'],'only two declared inventory/size reads')
closing=doc(B/'evidence/DELTA_CLOSING_METADATA_NATIVE01.json')
need(len(closing['closing_native_checks'])==5,'all actual closing checks')
for i,record in enumerate(closing['closing_native_checks']):
    raw=native(record)
    if i<2:
        p=B/('DELTA.md' if i==0 else 'DELTA_ACCEPTANCE.json')
        need(raw==read(p),'whole actually displayed final decision bytes')
    else:
        p=B/['DELTA_INPUT_PINS.sha256','REPORT_SHA256SUMS','PREPARATION_SHA256SUMS'][i-2]
        expected=''.join(line.split('  ',1)[1]+': OK\n' for line in read(p).decode().splitlines()).encode()
        need(raw==expected,'entire actual closing pin output, no selected subset')
link_native=closing['delta_local_link_native']
actual=native(link_native)
paths=link_native['unique_paths']
need(len(paths)==11 and len(link_native['links'])==11 and paths==sorted(set(paths)), 'complete original link key')
for row in link_native['links']:
    need(str((B/row['target']).resolve())==row['resolved'] and row['resolved'] in paths,'exact relative link')
expected=''.join(p+'|regular file|'+str(len(read(p)))+'\n' for p in paths).encode()
need(actual==expected,'entire original LF-delimited stat output')

# Complete existing build reuse is a documentary dependency check, not a build.
build_native=doc(RR/'BUILD_REUSE_NATIVE01.json')
build_raw=native(build_native)
need(build_raw==read(BASE/'qa/p211_b_root_reception/BUILD_REUSE_STDOUT01.raw'),'whole accepted build-reuse native output')
build=parse(build_raw)
buildkeys=doc(build['prior_read_key']['path'])
need(len(buildkeys)==1299 and build['checks']==5974 and build['configuration_entries_checked_twice']==843,'complete accepted build key')
for p,k in buildkeys.items(): read(build['exact_navigation_substitutions'].get(p,p),k)
read(build['prior_read_key']['path'],build['prior_read_key']['pin'])
read(build['historical_mapping']['path'],build['historical_mapping']['pin'])
for p,k in list(KEYS.items()): read(p,k)
result={'status':'PASS_ROOT_FINAL_B_AND_SAME_REVIEWER_EXACT_DELTA','checks':checks,'read_paths':len(KEYS),
        'final_payloads':39,'final_payload_bytes':6076055,'final_files':40,'final_total_bytes':6079604,
        'same_B_actual_documentary_checks':154857,'same_B_complete_original_keys':1774,
        'old_report_payloads_unchanged':31,'old_preparation_payloads_unchanged':19,
        'author_raw_triples_unchanged':32,'all_actual_new_read_records':30,'exact_native_sed_slices':sed_count,
        'exact_native_diff_hunks':diff_count,'closing_native_checks':5,'local_links':11,
        'runtime_file_keys':122,'runtime_configuration_paths':69,'runtime_memberships':5,'loader_states':9,
        'delta_accepted':True,'current_open_findings':0,'new_scientific_runs':0,'new_builds':0,'new_page_views':0,
        'final_manifest_sha256':KEYS[str(B/'SHA256SUMS')]['sha256'],
        'scope':'Original documentary reception, not a new scientific replay or build. Existing full-key replay/build evidence retains its original authorship. Round2 and terminal gates remain pending.',
        'external_status':'OWNER_AMBER / HOLD_EXTERNAL'}
for name,value in [('INPUTS.json',KEYS),('RESULT.json',result)]:
    with (OUT/name).open('xb') as f:f.write((json.dumps(value,sort_keys=True,indent=2)+'\n').encode())
print(json.dumps(result,sort_keys=True))





