#!/usr/bin/env python3
"""Root documentary intake only; never imports submitted runtime/science code."""
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import stat
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
OUT = Path(__file__).resolve().parent
PREP = ROOT / 'docs/papers211_215_sequence/qa/p212_runtime_preparation01'
OLD = PREP.parent / 'p211_runtime_preparation'
PAPER = ROOT / 'papers/212-closed-pointer-orbits'
checks, before, native = [], {}, []


def need(ok, label):
    if not ok:
        raise AssertionError(label)
    checks.append(label)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def rich(path):
    p = Path(path)
    a, b = p.lstat(), p.stat()
    data = p.read_bytes()
    return {'path': str(p), 'resolved': str(p.resolve(strict=True)),
            'symlink': os.readlink(p) if p.is_symlink() else None,
            'lmode': a.st_mode, 'mode': b.st_mode, 'nlink': b.st_nlink,
            'size': len(data), 'sha256': digest(data), 'mtime_ns': b.st_mtime_ns,
            'uid': b.st_uid, 'gid': b.st_gid}


def read(path):
    p = Path(path)
    if not p.is_absolute():
        p = ROOT / p
    key = rich(p)
    need(stat.S_ISREG(key['mode']), 'regular:' + str(p))
    if str(p) in before:
        need(before[str(p)] == key, 'repeat_same:' + str(p))
    before[str(p)] = key
    return p.read_bytes()


def obj(path):
    return json.loads(read(path))


def save(name, value):
    with (OUT / name).open('x', encoding='utf8') as f:
        json.dump(value, f, ensure_ascii=True, sort_keys=True, indent=2)
        f.write('\n')


def pin(path, key):
    data = read(path)
    need(digest(data) == (key if isinstance(key, str) else key['sha256']), 'sha256:' + str(path))
    if isinstance(key, dict):
        need(len(data) == key['bytes'], 'bytes:' + str(path))


def manifest(path, base, count, membership=False):
    result = {}
    for line in read(path).decode().splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(m is not None, 'manifest_line:' + str(path))
        h, name = m.groups()
        need(name not in result and '..' not in Path(name).parts, 'unique_safe_manifest:' + name)
        result[name] = h
        pin(Path(name) if Path(name).is_absolute() else base / name, h)
    need(len(result) == count, 'manifest_count:' + str(path))
    if membership:
        entries = list(base.rglob('*'))
        need(all(p.is_file() and not p.is_symlink() and p.stat().st_nlink == 1 for p in entries), 'exact_regular_singlelink_tree')
        need({p.relative_to(base).as_posix() for p in entries} == set(result) | {Path(path).name}, 'exact_complete_nonself_membership')
    return result


def command(argv, cwd, expected):
    i = len(native)
    request = {'argv': argv, 'cwd': str(cwd), 'timeout_seconds': 60,
               'stdin': 'DEVNULL', 'shell': False, 'environment': dict(os.environ)}
    save('COMMAND_%02d_ATTEMPT.json' % i, request)
    done = subprocess.run(argv, cwd=cwd, stdin=subprocess.DEVNULL, capture_output=True, timeout=60)
    for tag, data in [('stdout', done.stdout), ('stderr', done.stderr)]:
        with (OUT / ('COMMAND_%02d_%s.bin' % (i, tag))).open('xb') as f:
            f.write(data)
    result = {'request': request, 'exit_code': done.returncode,
              'stdout': {'bytes': len(done.stdout), 'sha256': digest(done.stdout)},
              'stderr': {'bytes': len(done.stderr), 'sha256': digest(done.stderr)}}
    save('COMMAND_%02d_NATIVE.json' % i, result)
    native.append(result)
    need(done.returncode == expected and done.stderr == b'', 'native_complete_expected:%02d' % i)
    return done.stdout


need(not (OUT / 'PREPARATION_RESULT.json').exists(), 'fresh_documentary_output')
read(__file__)
seal = manifest(PREP / 'SHA256SUMS', PREP, 15, True)
need(digest(read(PREP / 'SHA256SUMS')) == 'c78360b5be2c6f82bf7e8429700d381d800e95c693a6d98e2eac99f698c2ba78', 'exact_delivered_seal')
need(sum(len(read(PREP / n)) for n in seal) == 638040, 'exact_payload_bytes')
pins = manifest(PREP / 'INPUT_PINS.sha256', ROOT, 19)
need(sum(Path(n).is_absolute() for n in pins) == 2, 'two_host_source_metadata_pins_only')
manifest(PAPER / 'SOURCE_PREP_MANIFEST.sha256', PAPER, 21)
original = obj(PREP / 'ORIGINAL_NATIVE_READS.json')['records']
closing_obj = obj(PREP / 'CLOSING_NATIVE.json')
closing = closing_obj['records']
root_reads = obj(OUT / 'ROOT_SELECTED_READS.json')['records']
need((len(original), len(closing), len(root_reads)) == (54, 18, 6), 'actual_native_record_censuses')
for label, records, nonzero in [('original', original, {11:1, 24:2, 34:2, 49:1, 50:1, 51:1}), ('closing', closing, {11:1}), ('root', root_reads, {})]:
    for i, row in enumerate(records):
        req, res = row['request'], row['result']
        need(isinstance(req['cmd'], str) and isinstance(res['output'], str) and isinstance(res['chunk_id'], str), 'actual_envelope:' + label + ':' + str(i))
        need(res['exit_code'] == nonzero.get(i, 0) and 'session_id' not in res, 'actual_completed_exit:' + label + ':' + str(i))
        # Central navigation output can be presentation-limited; never bind it as current history.
        if not (label == 'original' and i in (2, 3, 9)):
            need(not res['output'].startswith('Warning: truncated output'), 'complete_selected_tool_output:' + label + ':' + str(i))

bindings = []
def bind(records, ids, path):
    raw = b''.join(records[i]['result']['output'].encode() for i in ids)
    need(raw == read(path), 'whole_actual_read_bytes:' + str(path) + ':' + str(ids))
    bindings.append({'indices': ids, 'path': str(path), 'bytes': len(raw), 'sha256': digest(raw)})

for ids, path in [([16], OLD/'runtime_core.py'), ([17,18], OLD/'p211_runtime.py'), ([19], OLD/'prepare_runtime.py'),
                  ([20,21,22], PAPER/'verify.py'), ([27,28], PAPER/'OUTPUT_SCHEMA.md'),
                  ([44], PREP/'runtime_core.py'), ([45,46], PREP/'p212_runtime.py'),
                  ([47], PREP/'prepare_runtime.py'), ([48], PREP/'prepare_runtime.py'),
                  ([39], Path('/usr/lib/python3.10/decimal.py'))]:
    bind(original, ids, path)
for i, name in [(0,'PLAN.md'), (1,'INFRASTRUCTURE_LINEAGE.md'), (2,'BINDING_CONTRACT.md'), (3,'READ_SCOPE.md'),
                (4,'DISCOVERY.pending.json'), (5,'INITIAL.pending.json'), (6,'PAIR.pending.json'), (8,'INTERFACE.json'), (13,'HANDOFF.md')]:
    bind(closing, [i], PREP/name)
for ids, path in [([1],PREP/'runtime_core.py'),([2,3],PREP/'p212_runtime.py'),([4],PREP/'prepare_runtime.py')]:
    bind(root_reads, ids, path)
need(root_reads[0]['result']['output'].encode() == b''.join(read(PREP/n) for n in ['PLAN.md','BINDING_CONTRACT.md','INFRASTRUCTURE_LINEAGE.md','READ_SCOPE.md']), 'whole_root_four_document_read')
need(root_reads[5]['result']['output'].encode() == read(PREP/'INITIAL.pending.json') + read(PREP/'PAIR.pending.json'), 'whole_root_pair_template_read')
need(original[52]['result']['output'].encode() == read(PREP/'INPUT_PINS.sha256'), 'whole_original_pin_listing_bytes')
earlier = json.loads(closing[7]['result']['output'])
current = obj(PREP/'INTERFACE.json')
changed = [k for k in current if current[k] != earlier[k]]
need(changed == ['roles'] and set(earlier) == set(current), 'disclosed_unsealed_interface_wording_scope')
need(all(current['roles'][k] == earlier['roles'][k] for k in current['roles'] if k != 'initial'), 'only_initial_role_prose_changed')
for group in ['source_files','original_infrastructure_inputs']:
    for path, key in current[group].items():
        pin(path,key)
for row in current['scientific_input_interface']:
    pin(row['path'],row)
discovery = obj(PREP/'DISCOVERY.pending.json')
need(discovery['approved'] is False and discovery['reviewed_all_preparation_sources'] is False and discovery['native_timeout_seconds'] is None and discovery['provenance_inputs'] == [], 'disabled_discovery')
need(discovery['source_inputs'] == current['source_files'] and discovery['lineage_inputs'] == current['original_infrastructure_inputs'], 'exact_disabled_discovery_keys')
for mode in ('initial','pair'):
    role = obj(PREP/(mode.upper()+'.pending.json'))
    need(role['approved'] is False and role['attempt'] is None and role['mode'] == mode and role['role'] == 'author', 'disabled_exact_scientific_role:' + mode)
    need(role['capsule_files'] == current['scientific_input_interface'] and role['declared_imports'] == current['declared_imports'], 'exact_two_source_role:' + mode)
    need(all(v is None for v in role['timeouts'].values()) and role['provenance_inputs'] == [], 'unbound_deadlines_authority:' + mode)
    need(role['schema']['top_keys'] == current['required_top_keys'], 'full_top_key_contract:' + mode)

for name in ['CANONICAL.json', 'canonical.stdout.json']:
    need(not os.path.lexists(PAPER/name), 'still_absent:' + name)
need(not os.path.lexists(discovery['output']) and not os.path.lexists(PREP/'RUNTIME_LOCK.json'), 'no_discovery_or_lock')
for link in closing_obj['local_markdown_links']:
    resolved = (PREP/link['document']).parent.joinpath(link['literal']).resolve(strict=True)
    need(str(resolved) == link['resolved'] and resolved.is_file(), 'physical_declared_link:' + link['literal'])

command(['/usr/bin/sha256sum','-c','SHA256SUMS'], PREP, 0)
command(['/usr/bin/sha256sum','-c',str(PREP/'INPUT_PINS.sha256')], ROOT, 0)
for i in (49,50,51):
    old = original[i]
    raw = command(shlex.split(old['request']['cmd']), ROOT, 1)
    # File/time headers are preserved separately. Equality here is explicitly complete hunk bytes.
    need(raw.split(b'\n',2)[2] == old['result']['output'].encode().split(b'\n',2)[2], 'whole_native_lineage_hunk_bytes:' + str(i))
for path, value in list(before.items()):
    need(rich(path) == value, 'entire_before_after_rich_key:' + path)
result = {'status':'PASS_SOURCE_ARTIFACT_INTAKE_ONLY_PENDING_INDEPENDENT_AUDIT',
          'checks':len(checks), 'labels':checks, 'input_key':before, 'input_count':len(before),
          'payload_count':15, 'payload_bytes':638040, 'pin_count':19,
          'actual_source_bindings':bindings, 'native':native,
          'scientific_executions':0, 'submitted_program_imports_or_execution':0,
          'limits':'No host-runtime closure, discovery approval, runtime lock, science, canonical, build, view or manuscript verdict. Archived complete hunk equality is not whole raw diff equality; actual headers are retained.'}
save('PREPARATION_RESULT.json', result)
print(json.dumps({'status':result['status'],'checks':len(checks),'input_count':len(before),'actual_read_bindings':len(bindings),'native_commands':len(native),'result_sha256':digest((OUT/'PREPARATION_RESULT.json').read_bytes())}, sort_keys=True))
