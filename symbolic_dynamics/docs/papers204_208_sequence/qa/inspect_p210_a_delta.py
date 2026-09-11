#!/usr/bin/python3.10
"""Root read-only final A closure: exact documentary delta, unchanged full keys.

Does not import/execute original science, build, review or audit programs.
Prior root originals/strict acceptance are reused only after exact input checks.
"""
from pathlib import Path
from hashlib import sha256
import gzip
import json
import os
import re
import sys
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
D = QA.parent / 'reviews/p210_a'
H = D / 'history/initial_before_delta'
P = ROOT / 'papers/210-weakly-increasing-run-aggregation'
F = P / 'frozen_round0'
B = QA / 'root_replays/p210_a_strict_pair_01'
FINAL = 'f6b92663cb2a7909f85a25a892ee4433ccd6177e84c07bf7ceccc9555b191f6d'
INITIAL = 'e60d352a6520dd5f56b01035912ce753bb1a669c7368ce0a999ff56a72ff966d'
OLD_DELTA = '835047cc14c04de6057a93b993b6f21dd57e77f1ce8e83afba7dce0af8e2445e'
ROUND0 = 'e8446cd17b1a283c74f9a6b4ced413b9e30810396c3d30f936ac2986ce790e26'
AUTHOR = 'b0c72e401acaf50acb611dc27f2ff1c45e3ad6e1b547218b48d13be8c82a0f6c'
WHOLE = '9c092df8a673debea2697f6213e92002b8fb575b336a8821f5c18fdb0a79e727'
RESPONSE = '829acdc6048f1aa9b9dcbe0d1195bb935c3ea8ed84154dc2b2abc24ef2a17b66'
PAIR = '9b30c2a3fc93874e4eaafdec345d9894f95aa36b7e9d764bd54646cfe5c7d6fb'
ALIASES = {str(D/'DELTA.md'): (H/'DELTA.md', OLD_DELTA), str(D/'SHA256SUMS'): (H/'SHA256SUMS', INITIAL)}
CENSUS = {'Critical': {'open': 0, 'resolved': 0}, 'Major': {'open': 0, 'resolved': 1},
          'Minor': {'open': 0, 'resolved': 0}, 'total_open': 0, 'total_resolved': 1}
CURRENT, CHECKS, USED = {}, 0, set()

def need(ok, message):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(message)

def measured(path):
    path = Path(path)
    need(path.is_absolute() and path.is_file(), 'absolute existing input: '+str(path))
    h = sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return {'sha256': h.hexdigest(), 'bytes': path.stat().st_size, 'resolved': str(path.resolve()),
            'symlink': os.readlink(path) if path.is_symlink() else None}

def pin(path, expected=None):
    name = str(path)
    if name not in CURRENT:
        CURRENT[name] = measured(path)
    value = CURRENT[name]
    if expected is not None:
        need(value['sha256'] == expected, 'exact bytes: '+name)
    return value

def raw(path):
    before = pin(path)
    data = Path(path).read_bytes()
    need(sha256(data).hexdigest() == before['sha256'] and len(data) == before['bytes'], 'stable read: '+str(path))
    return data

def obj(path):
    data = raw(path)
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)

def rows(path):
    result = {}
    for line in raw(path).decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None, 'strict manifest row')
        h, name = match.groups()
        need(not Path(name).is_absolute() and '..' not in Path(name).parts and name not in result, 'strict relative unique member')
        result[name] = h
    return result

def manifest(base, seal, expected, count, complete=True, historical=False):
    pin(seal, expected)
    result = rows(seal)
    need(len(result) == count, 'exact manifest census '+str(base))
    for name, h in result.items():
        path = base/name
        if historical and str(path) in ALIASES:
            path, old = ALIASES[str(path)]
            need(old == h, 'only exact historical manifest role')
        pin(path, h)
    if complete:
        entries = list(base.rglob('*'))
        need(not any(p.is_symlink() for p in entries), 'physical non-symlink package')
        need(set(result) == {str(p.relative_to(base)) for p in entries if p.is_file() and p != seal}, 'entire physical manifest membership')
    return result

def key(path, old, historical=False):
    wanted = {'sha256': old['sha256'], 'bytes': old.get('bytes', old.get('size')),
              'resolved': old.get('resolved', old.get('real')), 'symlink': old['symlink']}
    if historical and path in ALIASES:
        dest, h = ALIASES[path]
        need(wanted['sha256'] == h and wanted['resolved'] == path and wanted['symlink'] is None, 'exact original documentary alias key')
        now = pin(dest, h)
        need(now['bytes'] == wanted['bytes'] and now['resolved'] == str(dest) and now['symlink'] is None, 'physical historical documentary bytes')
        USED.add(path)
    else:
        need(pin(path) == wanted, 'full current dependency key '+path)

def resources():
    names = {'/usr/bin/python3.10', '/usr/bin/cmp', '/usr/bin/ldd', '/usr/bin/env', '/bin/bash', '/bin/sh'}
    for directory, folders, files in os.walk('/usr/lib/python3.10'):
        folders[:] = [n for n in folders if n not in {'site-packages', 'dist-packages', '__pycache__'}]
        names.update(str(Path(directory)/n) for n in files if not n.endswith(('.pyc', '.pyo')))
    for base in map(Path, ('/usr/lib/x86_64-linux-gnu', '/usr/lib64', '/usr/local/lib')):
        paths = base.glob('*') if base == Path('/usr/local/lib') else base.rglob('*')
        names.update(str(p) for p in paths if p.is_file() and (p.name.endswith('.so') or '.so.' in p.name))
    for base in map(Path, ('/usr/lib/locale/C.utf8', '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv', '/etc/ld.so.conf.d')):
        if base.is_dir():
            names.update(str(p) for p in base.rglob('*') if p.is_file())
    return sorted(names)

def tree(base):
    return {str(p) for p in Path(base).rglob('*') if p.is_file() and
            not {'__pycache__', 'site-packages', 'dist-packages'}.intersection(p.parts) and p.suffix not in {'.pyc', '.pyo'}}

def configuration():
    left = obj(B/'CONFIGURATION_BEFORE.json')
    need(left == obj(B/'CONFIGURATION_AFTER.json'), 'strict original configuration interval')
    for name, old in left.items():
        p = Path(name)
        now = {'lexists': os.path.lexists(p), 'exists': p.exists(), 'is_file': p.is_file(), 'is_dir': p.is_dir(),
               'resolved': str(p.resolve()), 'symlink': os.readlink(p) if p.is_symlink() else None}
        if p.is_file():
            now.update({k: pin(p)[k] for k in ('sha256', 'bytes')})
        need(now == old, 'all actual current strict configuration roles '+name)
    return left

def main():
    need(sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode and not sys.flags.optimize, 'read-only isolated source interpreter')
    final = manifest(D, D/'SHA256SUMS', FINAL, 552)
    initial = manifest(D, H/'SHA256SUMS', INITIAL, 484, False, True)
    frozen = manifest(F, F/'SHA256SUMS', ROUND0, 493)
    author = manifest(P, P/'AUTHOR_MANIFEST.sha256', AUTHOR, 489, False)
    manifest(P, P/'PAPER_MANIFEST.sha256', WHOLE, 987)
    manifest(B, B/'SHA256SUMS', PAIR, 59)
    need({n for n in initial if final[n] != initial[n]} == {'DELTA.md'}, 'only initial DELTA payload replaced')
    projected = {('history/initial_before_delta/DELTA.md' if n == 'DELTA.md' else n): h for n,h in initial.items()}
    projected['history/initial_before_delta/SHA256SUMS'] = INITIAL
    need(rows(D/'INITIAL_PRESERVED_PINS.sha256') == projected, 'complete485 exact initial preservation projection')
    need(rows(D/'INPUT_PINS.sha256') == {str((F/n).relative_to(ROOT)): h for n,h in frozen.items()} |
         {str((F/'SHA256SUMS').relative_to(ROOT)): ROUND0}, 'complete494 frozen review inputs')
    for n,h in author.items():
        need(frozen[n] == h and raw(P/n) == raw(F/n), 'all489 author/frozen byte pairs')
    pin(QA.parent/'P210_A_RESPONSE.md', RESPONSE)
    pin(D/'DELTA.md', 'fa03852f5366d6a0e4fd5a202dfb57e6d6887e8b858a14576ed82e810011d123')
    pin(D/'CURRENT_FINDINGS.json', 'f3d5a14b62b880f79fc5c98fa44f9ba98415ebf111e30f6e5eee64a8e4984e7b')
    findings, current, closure = obj(D/'FINDINGS.json'), obj(D/'CURRENT_FINDINGS.json'), obj(D/'DELTA_CLOSURE.json')
    need(current['reviewer'] == '/root/p210_a_reviewer' and current['verdict'] == 'ACCEPTED_EXACT_NO_CHANGE_DELTA' and current['response_sha256'] == RESPONSE, 'same actual A exact decision')
    need(current['findings'] == findings['findings'] and current['census'] == findings['census'] == CENSUS, 'entire E1 retained and zero current open')
    need(closure['status'] == 'PASS_EXACT_ACCEPTED_NO_CHANGE_DELTA_NATIVE_AND_INITIAL_PRESERVATION' and closure['reviewer'] == current['reviewer'] and closure['response_sha256'] == RESPONSE and closure['historical_losses_recovered'] is False, 'exact original delta scope')
    before, after = obj(D/'DELTA_INPUTS_BEFORE.json.gz'), obj(D/'DELTA_INPUTS_AFTER.json.gz')
    need(before == after and len(before) == closure['unchanged_complete_key_count'] == 119881, 'entire actual119881 before/after dictionaries')
    need(raw(D/'DELTA_INPUTS_BEFORE.json.gz') == raw(D/'DELTA_INPUTS_AFTER.json.gz'), 'entire lossless gz pair bytes')
    for name, value in before.items():
        key(name, value)
    audit = obj(D/'AUDIT_READS.json.gz')
    need(len(audit) == 118753, 'complete original audit read dictionary')
    special = str(D/'execution/audit01/stdout')
    empty = sha256(b'').hexdigest()
    for name, value in audit.items():
        if name == special:
            need(value == {'sha256': empty, 'size': 0, 'real': special, 'symlink': None}, 'sole exact historic own-output observation')
            pin(name, '5438c5abf2b66c97b472fa7be09c26f3717a0d6c2ce98efa5808f878d877c7d3')
        else:
            key(name, value, True)
    known = obj(B/'INPUTS_BEFORE.json')
    need(known == obj(B/'INPUTS_AFTER.json') and len(known) == 3634, 'strict full3634 original before/after')
    for name,value in known.items():
        key(name, value, True)
    need(USED == set(ALIASES), 'exactly both documentary aliases used, no broader waiver')
    runtime = obj(B/'RESOURCE_NAMES_BEFORE.json')
    need(runtime == obj(B/'RESOURCE_NAMES_AFTER.json') == resources(), 'full current strict resource membership')
    conf = configuration()
    build = obj(D/'build02/INPUTS_BEFORE.json.gz')
    build_roots = ('/usr/lib/python3.10', '/usr/lib/locale', '/usr/lib/x86_64-linux-gnu/gconv', '/etc/texmf',
                   '/var/lib/texmf', '/usr/share/texlive/texmf-dist', '/usr/share/texmf', '/etc/fonts',
                   '/usr/share/fontconfig', '/var/cache/fontconfig', '/usr/share/poppler', '/usr/share/fonts')
    memberships = {base: tree(base) for base in build_roots}
    for base, names in memberships.items():
        need(names == {n for n in build if Path(n).is_relative_to(base)}, 'entire current original A build root '+base)
    so = {str(p) for p in Path('/usr/lib/x86_64-linux-gnu').glob('*.so*') if p.is_file()}
    need(so <= set(build), 'original A optional shared-library membership')
    for name in so:
        key(name, build[name])
    natives = closure['actual_safe_parent_native_commands']
    need(len(natives) == 14 and {r['name'] for r in natives} == {p.name for p in (D/'execution').iterdir() if p.name.startswith('delta_')}, 'all14 added native commands')
    for row in natives:
        folder = D/'execution'/row['name']
        attempt, result = obj(folder/'ATTEMPT.json'), obj(folder/'RESULT.json')
        need(attempt['argv'] == row['argv'] and attempt['cwd'] == row['cwd'] and result['native_returncode'] == row['native_returncode'] == 0, 'full original native bindings '+row['name'])
        need(attempt['environment'] == {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC'} and attempt['omitted_launcher_environment_keys'] == [], 'exact cleared safe-parent environment')
        need(result['end_ns'] >= attempt['start_ns'], 'actual native chronology')
        for stream in ('stdout', 'stderr'):
            value = pin(folder/stream, result[stream+'_sha256'])
            need({k:value[k] for k in ('bytes','sha256')} == row['streams'][stream], 'entire saved native streams')
        need(raw(folder/'stderr') == b'', 'complete native empty stderr')
        argv, cwd = row['argv'], Path(row['cwd'])
        if argv[0] == '/usr/bin/sha256sum':
            expected = ''.join(n+': OK\n' for n in rows(cwd/argv[-1]))
            need(raw(folder/'stdout').decode() == expected, 'complete native checksum result')
        elif argv[0] in ('/usr/bin/cmp','/usr/bin/cp'):
            need(raw(folder/'stdout') == b'', 'complete copy/comparator stdout')
            left, right = [(cwd/v).resolve() for v in argv[-2:]]
            if str(left) in ALIASES:
                left = ALIASES[str(left)][0]
            need(raw(left) == raw(right), 'complete original raw comparison/copy operands under exact historical roles')
        else:
            mode = 'before' if row['name'] == 'delta_before01' else 'after'
            need(row['name'] in {'delta_before01','delta_after01'} and argv == ['/usr/bin/python3.10','-I','-S','-B','-X', 'pycache_prefix='+str(D/('unused_delta_'+mode+'01')), 'check_delta.py', mode], 'exact before/after native no-science command')
            need(not os.path.lexists(D/('unused_delta_'+mode+'01')), 'original new delta cache still absent')
            output = obj(folder/'stdout')
            need(output['status'] == 'PASS_SAME_A_DELTA_'+mode.upper() and output['checks'] == (250531 if mode == 'before' else 250533) and output['input_paths_reread'] == 119881 and output['current_census'] == CENSUS, 'complete actual delta return')
            need(output['ledger_sha256'] == pin(D/('DELTA_INPUTS_'+mode.upper()+'.json.gz'))['sha256'] and output['science_executions'] == output['tex_builds'] == output['new_views'] == 0, 'explicit reused-not-executed scope')
    for label, expected in [('P210_A_ORIGINALS_ROOT_COMPLETION.actual.json', 'PASS_DOCUMENTARY_INITIAL_A_ORIGINALS_ONLY'), ('P210_A_STRICT_ROOT_COMPLETION.actual.json', 'PASS_ROOT_P210_A_STRICT_PAIR_ORIGINAL_RECEPTION')]:
        r = obj(QA/label)['result']
        need(r['exit_code'] == 0 and json.loads(r['output'])['status'] == expected, 'actual prior accepted root native gate')
    links = []
    for name in ('DELTA.md', 'DELTA_ARTIFACT_ROLES.md'):
        for href in re.findall(r'\[[^\]]*\]\(([^)]+)\)', raw(D/name).decode()):
            if href.startswith(('https://','http://','#','mailto:')):
                continue
            target = (D/unquote(href.split('#',1)[0].strip('<>'))).resolve()
            pin(target)
            links.append({'document':name,'href':href,'target':str(target)})
    for base,names in memberships.items():
        need(tree(base) == names, 'A build membership unchanged during final inspection')
    need(resources() == runtime and configuration() == conf, 'strict current membership/config unchanged after inspection')
    reads = dict(CURRENT)
    for name, value in reads.items():
        need(measured(name) == value, 'final uncached current-path reread '+name)
    need(set(final) == {str(p.relative_to(D)) for p in D.rglob('*') if p.is_file() and p != D/'SHA256SUMS'}, 'final complete review membership unchanged')
    print(json.dumps({'status':'PASS_ROOT_P210_A_FINAL_DOCUMENTARY_DELTA_AND_CURRENT_KEYS', 'checks':CHECKS,
        'current_paths_reread':len(reads), 'current_key_digest':sha256(json.dumps(reads,sort_keys=True).encode()).hexdigest(),
        'final_payloads':552,'initial_payloads_preserved':484,'initial_unchanged_in_place':483,
        'original_audit_paths':118753,'delta_before_after_paths':119881,'strict_known_paths':3634,
        'original_delta_native_commands':14,'new_document_links':links,'initial_aliases':{k:str(v[0]) for k,v in ALIASES.items()},
        'current_open_findings':0,'resolved_major_findings':1,'science_runs':0,'builds':0,'new_views':0,
        'reviewer_delta_actually_accepted':True,'root_acceptance_attestation_written':False,
        'boundary':'Prior full original/native/science/build/view gates reused only after exact full current keys; original audit own-output role and two documentary aliases explicit. No history recovered, no new independent review, no paper/batch completion.'},sort_keys=True))

if __name__ == '__main__':
    main()
