"""Scoped same-A no-change delta adapter; no scientific/build/view execution."""
import gzip, hashlib, json, os, pathlib, sys
R = pathlib.Path('/root/autodl-tmp/symbolic_dynamics')
D = pathlib.Path(__file__).resolve().parent
H = D / 'history/initial_before_delta'
P = R / 'papers/210-weakly-increasing-run-aggregation'
F = P / 'frozen_round0'
Q = R / 'docs/papers204_208_sequence/qa'
B = Q / 'root_replays/p210_a_strict_pair_01'
MODE = sys.argv[1]
assert MODE in ('before', 'after')
assert sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode and not sys.flags.optimize
SEALS = {'initial': 'e60d352a6520dd5f56b01035912ce753bb1a669c7368ce0a999ff56a72ff966d',
         'round0': 'e8446cd17b1a283c74f9a6b4ced413b9e30810396c3d30f936ac2986ce790e26',
         'author': 'b0c72e401acaf50acb611dc27f2ff1c45e3ad6e1b547218b48d13be8c82a0f6c',
         'paper': '9c092df8a673debea2697f6213e92002b8fb575b336a8821f5c18fdb0a79e727',
         'root_pair': '9b30c2a3fc93874e4eaafdec345d9894f95aa36b7e9d764bd54646cfe5c7d6fb'}
ALIASES = {str(D/'DELTA.md'): H/'DELTA.md', str(D/'SHA256SUMS'): H/'SHA256SUMS'}
CURRENT, CHECKS = {}, 0
def require(ok, why):
    global CHECKS
    CHECKS += 1
    if not ok: raise AssertionError(why)
def digest(data): return hashlib.sha256(data).hexdigest()
def raw(path): return pathlib.Path(path).read_bytes()
def pin(path):
    path = pathlib.Path(path)
    name = str(path)
    if name not in CURRENT:
        data = raw(path)
        CURRENT[name] = {'sha256': digest(data), 'bytes': len(data),
                         'resolved': str(path.resolve()),
                         'symlink': os.readlink(path) if path.is_symlink() else None}
    return CURRENT[name]
def read(path):
    pin(path)
    return raw(path)
def obj(path):
    data = read(path)
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)
def rows(path):
    found = {}
    for line in read(path).decode().splitlines():
        sha, rel = line.split('  ', 1)
        require(len(sha)==64 and not pathlib.Path(rel).is_absolute() and '..' not in pathlib.Path(rel).parts and rel not in found, 'strict manifest path')
        found[rel] = sha
    return found
def manifest(base, seal, expected, count, physical=False, historical=False):
    require(pin(seal)['sha256']==expected, 'exact seal '+str(seal))
    found = rows(seal)
    require(len(found)==count, 'exact manifest count')
    for rel, sha in found.items():
        path = base/rel
        if historical: path = ALIASES.get(str(path), path)
        require(pin(path)['sha256']==sha, 'full payload '+str(path))
    if physical:
        require(set(found)=={str(p.relative_to(base)) for p in base.rglob('*') if p.is_file() and p != seal}, 'full physical membership '+str(base))
    return found
def ledger(before, after, count):
    left, right = obj(before), obj(after)
    require(left==right and len(left)==count, 'complete archived runtime pair '+str(before))
    used_aliases=[]
    for name, old in left.items():
        path = ALIASES.get(name, pathlib.Path(name))
        now = pin(path)
        want = {'sha256':old['sha256'], 'bytes':old.get('bytes',old.get('size')),
                'resolved':old.get('resolved',old.get('real')), 'symlink':old['symlink']}
        if name in ALIASES:
            require(want['resolved']==name and want['symlink'] is None and now['symlink'] is None, 'exact regular historical documentary role')
            require(now['sha256']==want['sha256'] and now['bytes']==want['bytes'], 'historical bytes '+name)
            used_aliases.append({'original_path':name, 'physical_preserved_path':str(path), 'original_key':want})
        else: require(now==want, 'full current runtime key '+name)
    return {'before':str(before), 'after':str(after), 'count':count, 'exact_documentary_aliases':used_aliases}
def native_parent(name):
    base=D/'execution'/name
    result, attempt=obj(base/'RESULT.json'), obj(base/'ATTEMPT.json')
    require(result['native_returncode']==0, 'native success '+name)
    for channel in ('stdout','stderr'):
        require(pin(base/channel)['sha256']==result[channel+'_sha256'], 'complete native stream '+name)
    require(set(attempt['environment']) <= {'PATH','LANG','LC_ALL','LC_CTYPE','TZ'}, 'minimal safe-parent environment '+name)
    return result
def complete(name, checks=None, key='checks'):
    wrapped=obj(Q/name)
    require(wrapped['result']['exit_code']==0, 'actual complete native exit '+name)
    result=json.loads(wrapped['result']['output'])
    if checks is not None: require(result[key]==checks, 'exact native result '+name)
    return result
def put(path, value):
    require(not path.exists(), 'new-only output '+str(path))
    data=(json.dumps(value,sort_keys=True,indent=2)+'\n').encode()
    path.write_bytes(gzip.compress(data,mtime=0) if str(path).endswith('.gz') else data)

pin(__file__)
initial=manifest(D,H/'SHA256SUMS',SEALS['initial'],484,historical=True)
require(pin(H/'DELTA.md')['sha256']=='835047cc14c04de6057a93b993b6f21dd57e77f1ce8e83afba7dce0af8e2445e', 'initial delta before-state')
frozen=manifest(F,F/'SHA256SUMS',SEALS['round0'],493,physical=True)
author=manifest(P,P/'AUTHOR_MANIFEST.sha256',SEALS['author'],489)
manifest(P,P/'PAPER_MANIFEST.sha256',SEALS['paper'],987,physical=True)
manifest(B,B/'SHA256SUMS',SEALS['root_pair'],59,physical=True)
for rel, sha in author.items():
    require(frozen[rel]==sha and read(P/rel)==read(F/rel), 'all live/frozen author bytes '+rel)
require(read(P/'SHA256SUMS')==read(P/'AUTHOR_MANIFEST.sha256')==read(F/'AUTHOR_MANIFEST.sha256'), 'original author aliases')
inputs=rows(D/'INPUT_PINS.sha256')
require(len(inputs)==494,'all reviewed freeze inputs')
for rel,sha in inputs.items(): require(pin(R/rel)['sha256']==sha,'reviewed input '+rel)
for rel,sha in obj(D/'REPLAY_KEYS.json')['file_keys'].items(): require(pin(R/rel)['sha256']==sha,'exact A replay key '+rel)
for name in ('delta_preserve_delta01','delta_preserve_seal01','delta_cmp_initial_delta01','delta_cmp_initial_seal01'): native_parent(name)
for path,expected in [(Q.parent/'P210_A_RESPONSE.md','829acdc6048f1aa9b9dcbe0d1195bb935c3ea8ed84154dc2b2abc24ef2a17b66'),
                      (Q/'P210_A_ROOT_INITIAL_INSPECTION.md','1d60f6565ae6abff155ea9f65451ff7c62971d7fa1a07f9cdebc00a65246e737')]:
    require(pin(path)['sha256']==expected,'exact response/initial acceptance')
for name in ('P210_A_STRICT_ROOT_INSPECTION.md','P210_A_STRICT_LAUNCH.actual.json','P210_A_STRICT_ROOT_LAUNCH.actual.json',
             'P210_A_ORIGINALS_ROOT_LAUNCH.actual.json','P210_A_EXACT_NOCHANGE_LAUNCH.actual.json','check_p210_a_response.py',
             'inspect_p210_a_strict_pair.py'):
    read(Q/name)
strict=complete('P210_A_STRICT_COMPLETION.actual.json',[133978,133978],'checks_each')
complete('P210_A_STRICT_ROOT_COMPLETION.actual.json',26033)
originals=complete('P210_A_ORIGINALS_ROOT_COMPLETION.actual.json',2188885)
require(originals['current_paths_reread']==118767 and len(originals['complete_native_records'])==71,'root original full coverage')
require(originals['source_and_finding_scope']['current_open_findings']==0 and originals['source_and_finding_scope']['resolved_major_findings']==1,'original census')
complete('P210_A_EXACT_NOCHANGE_COMPLETION.actual.json',9840)
ledgers=[ledger(D/'pair02/INPUTS_BEFORE.json',D/'pair02/INPUTS_AFTER.json',2631),
         ledger(D/'build02/INPUTS_BEFORE.json.gz',D/'build02/INPUTS_AFTER.json.gz',117808),
         ledger(B/'INPUTS_BEFORE.json',B/'INPUTS_AFTER.json',3634)]
canonical=read(D/'CANONICAL.json')
for path in (D/'pair02/commands/run_1/stdout',D/'pair02/commands/run_2/stdout',B/'commands/03_verify_01/stdout.raw',B/'commands/03_verify_02/stdout.raw'):
    require(read(path)==canonical,'entire archived canonical bytes '+str(path))
require(read(D/'build02/source/main.pdf')==read(F/'main.pdf'),'selected viewed PDF remains exact')
findings=obj(D/'FINDINGS.json')
require(len(findings['findings'])==1 and findings['findings'][0]['id']=='P210-A-E1' and findings['findings'][0]['severity']=='Major' and findings['findings'][0]['status']=='resolved','retained resolved Major')
require(findings['census']['total_open']==0 and findings['census']['total_resolved']==1,'exact initial census')
if MODE=='before':
    require(read(D/'DELTA.md')==read(H/'DELTA.md'),'not yet changed initial delta')
    # Remove the mutable direct spelling; preserved historical bytes are the stable input.
    CURRENT.pop(str(D/'DELTA.md'))
    mapped={('history/initial_before_delta/DELTA.md' if rel=='DELTA.md' else rel):sha for rel,sha in initial.items()}
    mapped['history/initial_before_delta/SHA256SUMS']=SEALS['initial']
    path=D/'INITIAL_PRESERVED_PINS.sha256'
    require(not path.exists(),'new exact projected initial inventory')
    path.write_text(''.join(sha+'  '+rel+'\n' for rel,sha in sorted(mapped.items())))
else:
    before_keys=json.loads(gzip.decompress(raw(D/'DELTA_INPUTS_BEFORE.json.gz')))
    require(CURRENT==before_keys,'exact complete before/after key equality')
    current=json.loads(raw(D/'CURRENT_FINDINGS.json'))
    require(current['findings']==findings['findings'] and current['census']==findings['census'],'all finding details retained')
    require(current['verdict']=='ACCEPTED_EXACT_NO_CHANGE_DELTA' and current['response_sha256']=='829acdc6048f1aa9b9dcbe0d1195bb935c3ea8ed84154dc2b2abc24ef2a17b66','same-A exact current decision')
    require(b'ACCEPTED_EXACT_NO_CHANGE_DELTA' in raw(D/'DELTA.md'),'actual current delta written')
keys=dict(CURRENT)
for name,expected in keys.items():
    CURRENT.pop(name)
    require(pin(name)==expected,'uncached end-of-phase reread '+name)
out=D/('DELTA_INPUTS_'+MODE.upper()+'.json.gz')
put(out,CURRENT)
print(json.dumps({'status':'PASS_SAME_A_DELTA_'+MODE.upper(), 'reviewer':'/root/p210_a_reviewer', 'checks':CHECKS,
                  'input_paths_reread':len(CURRENT), 'complete_before_after_ledger':str(out),
                  'ledger_sha256':digest(raw(out)), 'preserved_initial_payloads':484,'unchanged_in_place_initial_payloads':483,
                  'physical_initial_seal_preserved':str(H/'SHA256SUMS'), 'exact_documentary_aliases':{k:str(v) for k,v in ALIASES.items()},
                  'runtime_reuse_ledgers':ledgers, 'paper_seal_unchanged':SEALS['paper'],
                  'current_census':findings['census'], 'science_executions':0,'tex_builds':0,'new_views':0,
                  'scope':'Changed-dependency/preservation check only; accepted original gates and prior actual views reused, not re-executed.'},sort_keys=True))
