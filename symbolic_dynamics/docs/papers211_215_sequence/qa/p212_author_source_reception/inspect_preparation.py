"""Receive P212 source preparation as documents; never load scientific code.

This new scoped receiver checks the original 22-file source-only inventory,
its 28 immutable provenance pins, the actual preseal diagnostics, and lexical
interfaces. It preserves all 22 files by native cp followed by native diff
and complete raw comparisons. It is neither a scientific run nor a build.
"""
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
PAPER = ROOT/'papers/212-closed-pointer-orbits'
OUT = Path(__file__).resolve().parent
SNAPSHOT = OUT/'source_preparation_original'
SEAL = 'SOURCE_PREP_MANIFEST.sha256'
SEAL_HASH = 'cec04ab58f92d8b4e1dc91e0e9be6fab8b04335d65ab685fb707e64ef0d365dc'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
checks = []
before = {}


def encode(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True, allow_nan=False)


def check(name, actual, expected):
    ok = encode(actual) == encode(expected)
    checks.append({'name': name, 'observed': actual, 'expected': expected, 'passed': ok})
    if not ok:
        raise AssertionError(name)


def unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('duplicate JSON key: '+key)
        result[key] = value
    return result


def js(body):
    return json.loads(body, object_pairs_hook=unique)


def digest(body):
    return {'bytes': len(body), 'sha256': sha256(body).hexdigest()}


def read(path):
    check('regular_nonsymlink:'+str(path), path.is_file() and not path.is_symlink(), True)
    prior = path.stat()
    body = path.read_bytes()
    after = path.stat()
    key = {**digest(body), 'mode': prior.st_mode, 'mtime_ns': prior.st_mtime_ns}
    check('stable_read_stat:'+str(path), [after.st_mode, after.st_mtime_ns, after.st_size],
          [prior.st_mode, prior.st_mtime_ns, len(body)])
    if str(path) in before:
        check('unchanged_repeated_read:'+str(path), key, before[str(path)])
    before[str(path)] = key
    return body


def put(name, value):
    body = value if isinstance(value, bytes) else (json.dumps(value, sort_keys=True, indent=2)+'\n').encode()
    with (OUT/name).open('xb') as stream:
        stream.write(body)


def manifest(path, base):
    result = {}
    for line in read(path).decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        check('manifest_format:'+line, match is not None, True)
        expected, name = match.groups()
        target = Path(name)
        check('relative_safe_manifest:'+name,
              not target.is_absolute() and all(part not in ('', '.', '..') for part in name.split('/')), True)
        check('unique_manifest:'+name, name in result, False)
        body = read(base/target)
        check('manifest_digest:'+name, sha256(body).hexdigest(), expected)
        result[name] = body
    return result


def native(label, argv):
    request = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV,
               'stdin': 'DEVNULL', 'timeout_seconds': 30, 'started_epoch': time.time()}
    put(label+'.ATTEMPT.json', request)
    result = subprocess.run(argv, cwd=ROOT, env=ENV, stdin=subprocess.DEVNULL,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
    put(label+'.stdout.raw', result.stdout)
    put(label+'.stderr.raw', result.stderr)
    receipt = {**request, 'ended_epoch': time.time(), 'exit_code': result.returncode,
               'stdout': digest(result.stdout), 'stderr': digest(result.stderr)}
    put(label+'.RECEIPT.json', receipt)
    check('native_zero:'+label, result.returncode, 0)
    check('native_empty_streams:'+label, [len(result.stdout), len(result.stderr)], [0, 0])
    return receipt


check('receiver_exact_location', str(OUT), str(ROOT/'docs/papers211_215_sequence/qa/p212_author_source_reception'))
read(Path(__file__).resolve())
check('snapshot_absent', os.path.lexists(SNAPSHOT), False)
seal_bytes = read(PAPER/SEAL)
check('original_source_seal', sha256(seal_bytes).hexdigest(), SEAL_HASH)
payload = manifest(PAPER/SEAL, PAPER)
check('complete_nonself_payload_count', len(payload), 21)
check('exact_paper_files', sorted(str(p.relative_to(PAPER)) for p in PAPER.rglob('*') if p.is_file()),
      sorted([*payload, SEAL]))
check('no_symlinks_anywhere', [str(p) for p in PAPER.rglob('*') if p.is_symlink()], [])
check('only_source_directory', sorted(str(p.relative_to(PAPER)) for p in PAPER.rglob('*') if p.is_dir()), ['sections'])
check('all_payloads_nonempty_lf', all(body and body.endswith(b'\n') for body in payload.values()), True)
pins = manifest(PAPER/'ORIGINAL_INPUT_PINS.sha256', ROOT)
check('immutable_provenance_count', len(pins), 28)
check('no_mutable_control_provenance', [name for name in pins if name.endswith(('PIPELINE_STATE.md', 'SYMBOLIC_DYNAMICS_STATE.md'))], [])

archive = js(payload['SOURCE_PREP_CHECKS.json'])
check('source_diagnostics_not_full_session', archive['full_session_log'], False)
check('two_actual_diagnostic_records', len(archive['records']), 2)
first, second = archive['records']
for record in archive['records']:
    check('recorded_zero:'+record['native_return']['chunk_id'], record['native_return']['exit_code'], 0)
    check('recorded_workdir:'+record['native_return']['chunk_id'], record['request']['workdir'], str(ROOT))
check('actual_inline_documentary_request', first['request']['cmd'].startswith("python3 -B - <<'P212_DOCUMENTARY'\n"), True)
old = js(first['native_return']['output'])
check('old47_diagnostics', old['check_count'], 47)
check('old47_complete', len(old['checks']), 47)
for record in old['checks']:
    check('archived_check_consistency:'+record['name'], [record['passed'], encode(record['observed']) == encode(record['expected'])], [True, True])
check('old_success', [old['failed_checks'], old['passed']], [[], True])
preseal_names = sorted(set(payload)-{'SOURCE_PREP_CHECKS.json'})
check('archived_preseal_inventory', [item['path'] for item in old['files']], preseal_names)
for item in old['files']:
    body = payload[item['path']]
    check('all20_actual_preseal_keys:'+item['path'],
          [len(body), len(body.decode().splitlines()), sha256(body).hexdigest()],
          [item['bytes'], item['lines'], item['sha256']])
check('actual_original_pin_command', second['request']['cmd'],
      'sha256sum --check --strict papers/212-closed-pointer-orbits/ORIGINAL_INPUT_PINS.sha256')
check('whole_actual_pin_stdout', second['native_return']['output'], ''.join(name+': OK\n' for name in pins))

texts = {name: body.decode('utf-8') for name, body in payload.items()}
params = js(payload['PARAMETERS.json'])
source = texts['verify.py']
# Only textual lexical extraction: neither ast, compile, exec nor import of verify.py.
param_block = source.split('PARAMETERS = ', 1)[1].split('\nFAMILIES = ', 1)[0].strip()
param_json = re.sub(r',\s*}', '}', param_block)
check('entire_literal_parameter_object', js(param_json), params)
check('fixed_all_four_sizes', params['carrier_sizes'], [1, 2, 3, 4])
check('fixed_scalar_limits', [params['series_max_core_size'], params['expected_total_states'], params['unobserved_core_first_sizes']], [4, 4356, [5, 6, 5]])
check('exact_declared_imports', re.findall(r'^(?:import .+|from .+ import .+)$', source, re.M),
      ['import itertools', 'import json', 'import math', 'import sys', 'from fractions import Fraction'])
check('only_one_scientific_file_open_site', re.findall(r'with open\(([^\n]+)', source), ['path, "r", encoding="utf-8") as stream:'])
check('guarded_main_literal', source.count('if __name__ == "__main__":'), 1)
check('explicit_application_interface', 'if len(sys.argv) != 3 or sys.argv[1] != "--parameters":' in source, True)
check('absolute_parameter_interface', 'if not sys.argv[2].startswith("/"):' in source, True)
check('canonical_path_override_permitted', 'Root may fix a\ndifferent exact path in a later documented interface decision before any\nadoption' in texts['OUTPUT_PLAN.md'], True)
for name in ('CANONICAL.json', 'canonical.stdout.json', 'main.pdf', 'frozen_round0', '__pycache__'):
    check('not_yet_produced:'+name, os.path.lexists(PAPER/name), False)
tex_names = sorted(name for name in payload if name.endswith('.tex'))
tex = '\n'.join(texts[name] for name in tex_names)
check('source_tex_count', len(tex_names), 7)
check('anonymous_source', re.findall(r'\\author\{([^}]+)\}', texts['main.tex']), ['Anonymous'])
labels = re.findall(r'\\label\{([^}]+)\}', tex)
refs = re.findall(r'\\(?:ref|eqref)\{([^}]+)\}', tex)
bibkeys = re.findall(r'@\w+\{([^,]+),', texts['references.bib'])
cites = [key.strip() for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}', tex) for key in group.split(',')]
check('unique_tex_labels', len(labels), len(set(labels)))
check('all_refs_resolve', sorted(set(refs)-set(labels)), [])
check('five_exact_citations', sorted(set(cites)), sorted(bibkeys))
check('five_bibliography_entries', len(bibkeys), 5)
check('seven_table_rows', len(re.findall(r'^(?:Figure-eight|Barbell|Theta|Any other theta).* & ', texts['sections/02_returns.tex'], re.M)), 7)
predicates = re.findall(r'"([a-z_]+)"', re.search(r'^PREDICATES = \((.*?)^\)', source, re.M|re.S).group(1))
check('46_unique_named_predicates', [len(predicates), len(set(predicates))], [46, 46])
check('complete_named_predicate_schema', [name for name in predicates if '`'+name+'`' not in texts['OUTPUT_SCHEMA.md']], [])

native_records = [native('copy_complete_source', ['/usr/bin/cp', '-R', '--', str(PAPER), str(SNAPSHOT)]),
                  native('compare_complete_source', ['/usr/bin/diff', '-r', '--', str(PAPER), str(SNAPSHOT)])]
check('complete_snapshot_set', sorted(str(p.relative_to(SNAPSHOT)) for p in SNAPSHOT.rglob('*') if p.is_file()), sorted([*payload, SEAL]))
for name, body in [*payload.items(), (SEAL, seal_bytes)]:
    check('complete_physical_raw_copy:'+name, read(SNAPSHOT/name) == body, True)
after = {}
for path, expected in sorted(before.items()):
    p = Path(path)
    body = p.read_bytes()
    stat = p.stat()
    key = {**digest(body), 'mode': stat.st_mode, 'mtime_ns': stat.st_mtime_ns}
    check('full_final_rich_key:'+path, key, expected)
    after[path] = key
result = {'status': 'ROOT_SOURCE_PREPARATION_ONLY_PASS', 'scientific_executions': 0,
          'scientific_imports_compiles_ast': 0, 'builds': 0, 'page_views': 0,
          'payload_count': len(payload), 'payload_bytes': sum(map(len, payload.values())),
          'total_files_with_seal': len(payload)+1, 'total_bytes_with_seal': sum(map(len, payload.values()))+len(seal_bytes),
          'original_provenance_pins': len(pins), 'source_seal': digest(seal_bytes),
          'snapshot': str(SNAPSHOT), 'native_copy_compare': native_records,
          'rich_input_count': len(before), 'check_count': len(checks), 'checks': checks,
          'before': before, 'after': after}
put('RESULT.json', result)
print(json.dumps(result, sort_keys=True))
