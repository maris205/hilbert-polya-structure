"""Root receives the full new documentary package and actual same-source reuse.

No science, source download, archived script or subprocess is executed here.
The original 72 rich records include exact integer nanoseconds; Python parses
them without routing their values through JavaScript numeric serialization.
"""
from pathlib import Path
from hashlib import sha256
import json
import os
import re
import stat

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
A = QA/'four_desk_documentary_audit01'
HERE = Path(__file__).resolve().parent
KEYS = {}
checks = 0


def need(ok, label):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(label)


def read(path, expected=None):
    path = Path(path)
    body = path.read_bytes()
    s = path.lstat()
    key = {'bytes': len(body), 'sha256': sha256(body).hexdigest(),
           'resolved': str(path.resolve()), 'symlink': os.readlink(path) if path.is_symlink() else None,
           'mode': s.st_mode, 'device': s.st_dev, 'inode': s.st_ino,
           'mtime_ns': s.st_mtime_ns, 'ctime_ns': s.st_ctime_ns}
    need(stat.S_ISREG(s.st_mode) and not path.is_symlink(), 'ordinary full input')
    need(str(path) not in KEYS or KEYS[str(path)] == key, 'unchanged rich identity')
    if expected is not None:
        need(all(key[k] == v for k, v in expected.items()), ('every original field', str(path)))
    KEYS[str(path)] = key
    return body


def pairs(rows):
    out = {}
    for k, v in rows:
        need(k not in out, 'duplicate JSON key')
        out[k] = v
    return out


def parse(body):
    return json.loads(body, object_pairs_hook=pairs)


def doc(path):
    return parse(read(path))


need(Path.cwd() == ROOT, 'explicit working directory')
read(__file__)
read(HERE/'PRIMARY_READ_RECORDS.json')
read(HERE/'REUSE_SCOPE.md')
seal = A/'MANIFEST.sha256'
read(seal, {'bytes': 511, 'sha256': '9adc02c796e782c055e5798dbec8c3954137d36880282dc9c31cda6f10deb2dd'})
payloads = {}
for line in read(seal).decode().splitlines():
    m = re.fullmatch(r'([a-f0-9]{64})  ([^/]+)', line)
    need(m is not None and m[2] not in payloads and m[2] != seal.name, 'flat safe nonself manifest')
    read(A/m[2], {'sha256': m[1]})
    payloads[m[2]] = KEYS[str(A/m[2])]
need(len(payloads) == 6 and {p.name for p in A.iterdir()} == set(payloads)|{seal.name}, 'whole seven-file package')
original_raw = read(A/'RECEPTION_RESULT.json')
original = parse(original_raw)
native = doc(A/'NATIVE_EXECUTION.json')
root_native = doc(HERE/'DOCUMENTARY_REUSE_NATIVE01.json')
need(root_native['request'] == native['actual_execution']['request'], 'exact disclosed same-source request')
need(root_native['result']['chunk_id'] == '7a9123' and root_native['result']['exit_code'] == 0
     and root_native['result']['output'].encode() == original_raw, 'whole actual root output equals original bytes')
need(original['checks'] == 2985 and original['input_paths'] == 72
     and original['INPUTS_BEFORE'] == original['INPUTS_AFTER'], 'full original result/census')
for path, expected in original['INPUTS_BEFORE'].items():
    read(path, expected)
need(len(original['INPUTS_BEFORE']) == 72, 'all original input keys')
pin_rows = {}
for line in read(A/'INPUT_PINS.sha256').decode().splitlines():
    digest, path = line.split('  ', 1)
    need(path not in pin_rows and Path(path).is_absolute(), 'exact original pin spelling')
    pin_rows[path] = digest
need(pin_rows == {p:k['sha256'] for p,k in original['INPUTS_BEFORE'].items()}, 'complete seal/rich correspondence')
for label, chunk in [('actual_execution', '3b9f14'), ('exact_saved_output_roundtrip', '9e426a')]:
    item = native[label]
    meta = item['result_without_output']
    binding = item['result_output_verbatim']
    need(meta['exit_code'] == 0 and meta['chunk_id'] == chunk, 'actual original native completion')
    need(binding['file'] == 'RECEPTION_RESULT.json' and binding['utf8_bytes'] == len(original_raw)
         and binding['sha256'] == sha256(original_raw).hexdigest()
         and binding['separate_raw_stdout_stderr'] is False, 'lossless split original output')
need(native['exact_saved_output_roundtrip']['exact_string_match'] is True, 'actual saved string roundtrip')
old_pin = native['actual_saved_result_pin_check']
need(old_pin['result']['exit_code'] == 0, 'actual old pin completion')
need(parse(old_pin['result']['output']) == {'before_after_equal': True, 'bytes': len(original_raw),
     'checks': 2985, 'desk_bytes': 597622, 'input_paths': 72, 'sha256': sha256(original_raw).hexdigest()},
     'entire actual old result pin response')
validation = native['final_package_validation']
need(validation['result']['exit_code'] == 0 and validation['result']['chunk_id'] == 'c779db',
     'actual final documentary validation')
validation_result = parse(validation['result']['output'])
need(validation_result['checks'] == 3217 and validation_result['unchanged_full_rich_inputs'] == 72,
     'whole final validation census')
for name, expected in validation_result['stable_five_payload_pins'].items():
    read(A/name, expected)
need(set(validation_result['stable_five_payload_pins']) == set(payloads)-{'NATIVE_EXECUTION.json'},
     'exact five pre-insertion stable originals')
need(len(original['complete_archived_native_entries']) == 62
     and len(original['actual_native_source_byte_bindings']) == 34
     and len(original['desks']['finite_permutation_gap_desk01']['indexed_returned_rows']) == 4,
     'complete native and byte-slice censuses')
need(original['reported_closed_attempt_deltas'] == [0,0,1,1]
     and original['count_or_admission_adoption'] is False, 'original documentary nonadoption')
need(all(original[k] == 0 for k in ['scientific_imports_or_executions', 'archived_commands_evaluated',
                                  'new_web_requests', 'new_literal_orbit_calculations']), 'non-scientific scope')
for p, k in list(KEYS.items()):
    read(p, k)
result = {'status': 'PASS_ROOT_FOUR_DESK_ORIGINAL_DOCUMENTARY_RECEPTION', 'checks': checks,
          'read_paths': len(KEYS), 'auditor_payloads': 6, 'auditor_files': 7,
          'auditor_payload_bytes': sum(k['bytes'] for k in payloads.values()),
          'auditor_total_bytes': sum(k['bytes'] for k in payloads.values())+511,
          'complete_unchanged_original_rich_keys': 72, 'original_desk_files': 34,
          'original_desk_bytes': 597622, 'historical_pins': 36,
          'explicit_same_source_reuse_checks': 2985, 'entire_original_output_equal': True,
          'actual_selected_native_entries': 62, 'native_sed_byte_slices': 34, 'indexed_byte_rows': 4,
          'new_scientific_runs': 0, 'new_builds': 0, 'new_page_views': 0,
          'count_increment_not_yet_adopted': 2, 'external_status': 'HOLD_EXTERNAL',
          'scope': 'Documentary original reception and disclosed same-source reuse. Root proof/source disposition and index update remain separately recorded.'}
for name, value in [('INPUTS.json', KEYS), ('RESULT.json', result)]:
    with (HERE/name).open('xb') as stream:
        stream.write((json.dumps(value, sort_keys=True, indent=2)+'\n').encode())
print(json.dumps(result, sort_keys=True))
