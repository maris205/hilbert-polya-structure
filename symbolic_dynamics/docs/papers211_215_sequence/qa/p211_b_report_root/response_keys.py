"""Bind the exact issued root no-change response; not reviewer acceptance."""
from pathlib import Path
from hashlib import sha256
import json
import os

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT/'docs/papers211_215_sequence'
HERE = BASE/'qa/p211_b_report_root'
PAPER = ROOT/'papers/211-kernel-image-projection-feedback'
B = BASE/'reviews/p211_b'
checks = 0
reads = {}


def need(ok, label):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(label)


def pin(path, expected=None):
    path = Path(path)
    body = path.read_bytes()
    key = {'bytes': len(body), 'sha256': sha256(body).hexdigest(),
           'resolved': str(path.resolve(strict=True)),
           'symlink': os.readlink(path) if path.is_symlink() else None}
    need(str(path) not in reads or reads[str(path)] == key, 'same complete input bytes')
    reads[str(path)] = key
    if expected is not None:
        need(all(key[k] == v for k, v in expected.items()), ('all original key fields', str(path)))
    return key


def doc(path):
    pin(path)
    return json.loads(Path(path).read_bytes())


def state(path, with_bytes=True):
    path = Path(path)
    row = {'lexists': os.path.lexists(path), 'exists': path.exists(),
           'is_file': path.is_file(), 'is_dir': path.is_dir(),
           'is_character_device': path.is_char_device(), 'resolved': str(path.resolve()),
           'symlink': os.readlink(path) if path.is_symlink() else None}
    if path.is_char_device():
        st = path.stat()
        row['character_device'] = {'major': os.major(st.st_rdev), 'minor': os.minor(st.st_rdev), 'mode': st.st_mode}
    if with_bytes and path.is_file():
        key = pin(path)
        row.update({k: key[k] for k in ('bytes', 'sha256')})
    return row


need(Path.cwd() == ROOT and not os.path.lexists(B/'DELTA.md')
     and not os.path.lexists(B/'SHA256SUMS'), 'actual pre-delta response phase')
source = pin(__file__)
prior = doc(HERE/'INPUTS.json')
need(len(prior) == 1751, 'entire original root report key')
for path, expected in prior.items():
    need(pin(path, expected) == expected, ('whole prior rich key', path))
native = doc(HERE/'NATIVE07.json')
result = doc(HERE/'RESULT.json')
need(native['result']['exit_code'] == 0 and json.loads(native['result']['output']) == result
     and result['checks'] == 31473 and result['delta_accepted'] is False, 'actual successful report reception')
author = {}
for line in (PAPER/'frozen_round0/SHA256SUMS').read_text().splitlines():
    digest, name = line.split('  ', 1)
    before = prior[str(PAPER/name)]
    after = pin(PAPER/name, before)
    frozen = pin(PAPER/'frozen_round1'/name, {'sha256': digest})
    need(before == after and (PAPER/name).read_bytes() == (PAPER/'frozen_round1'/name).read_bytes(),
         'exact author before/after raw freeze equality')
    author[name] = {'before': before, 'after': after, 'frozen': frozen}
need(len(author) == 32, 'whole author target set')
report = {}
for line in (B/'REPORT_SHA256SUMS').read_text().splitlines():
    digest, name = line.split('  ', 1)
    report[name] = pin(B/name, {'sha256': digest})
need(len(report) == 31, 'whole immutable report target set')
binding = doc(BASE/'qa/p211_b_pair_binding/BINDING.json')
lock_path = binding['runtime_lock']['path']
pin(lock_path, {k: binding['runtime_lock'][k] for k in ('sha256', 'bytes', 'resolved', 'symlink')})
lock = doc(lock_path)
need(len(lock['files']) == 122, 'all runtime ordinary files')
for path, expected in lock['files'].items():
    pin(path, expected)
for path, expected in lock['configuration']['paths'].items():
    need(state(path) == expected, ('complete current runtime state', path))
for path, expected in lock['configuration']['memberships'].items():
    p = Path(path)
    current = {'directory': state(p, False), 'members': {}}
    if p.is_dir():
        current['members'] = {x.name: state(x, False) for x in sorted(p.iterdir())}
    need(current == expected, ('entire current runtime membership', path))
for path, expected in lock['loader_search_directory_states'].items():
    need(state(path, False) == expected, ('full loader directory state', path))
response = BASE/'P211_B_RESPONSE.md'
out = {'status': 'PASS_EXACT_NO_CHANGE_B_RESPONSE_KEYS', 'checks': checks,
       'source_key': source, 'prior_root_input_ledger_key': pin(HERE/'INPUTS.json'),
       'root_reception_key': pin(HERE/'RECEPTION.md'), 'response_path': str(response),
       'response_key': pin(response), 'complete_prior_keys_checked': len(prior),
       'report_stage_manifest_key': pin(B/'REPORT_SHA256SUMS'),
       'report_stage_payload_keys': report, 'author_before_after': author,
       'author_additions': [], 'author_removals': [], 'author_modifications': [],
       'full_runtime_ordinary_keys': 122, 'runtime_configuration_paths': len(lock['configuration']['paths']),
       'runtime_memberships': len(lock['configuration']['memberships']),
       'delta_accepted': False, 'new_scientific_runs': 0, 'new_builds': 0, 'new_page_views': 0}
out['checks'] = checks
for name, value in [('RESPONSE_INPUTS.json', reads), ('RESPONSE_KEYS.json', out)]:
    with (HERE/name).open('xb') as stream:
        stream.write((json.dumps(value, sort_keys=True, indent=2)+'\n').encode())
print(json.dumps({'status': out['status'], 'checks': out['checks'], 'response_key': out['response_key'],
                  'result_key': pin(HERE/'RESPONSE_KEYS.json'), 'read_paths': len(reads)}, sort_keys=True))
