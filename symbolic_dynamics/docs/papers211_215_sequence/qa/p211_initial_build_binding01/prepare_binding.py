#!/usr/bin/python3.10
"""Root binds unchanged reviewed builder and one explicit prose-only source delta."""
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import stat
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers211_215_sequence/qa'
HERE = Path(__file__).resolve().parent
PREP = QA / 'p211_build_revision01'
PAPER = ROOT / 'papers/211-kernel-image-projection-feedback'
OUTPUT = QA / 'p211_initial_build_01'
RECEPTION = QA / 'p211_build_root_reception'
OLD_SCOPE = QA / 'p211_author_execution_documentation01/originals/sections/5_scope.tex'
ENV4 = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
ENV8 = {**ENV4, 'SOURCE_DATE_EPOCH': '1788825600', 'FORCE_SOURCE_DATE': '1', 'openin_any': 'p', 'openout_any': 'p'}
reads = {}


def pin(raw):
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}


def read(path):
    p = Path(path)
    raw = p.read_bytes()
    value = pin(raw)
    assert str(p) not in reads or reads[str(p)] == value, ('binding read drift', str(p))
    reads[str(p)] = value
    return raw


def data(path):
    return json.loads(read(path))


def put(name, value):
    raw = value if isinstance(value, bytes) else (json.dumps(value, sort_keys=True, indent=2) + '\n').encode()
    p = HERE / name
    with p.open('xb') as f:
        f.write(raw)
    return pin(raw)


def entry(path, members=False):
    p = Path(path)
    value = {'path': str(p), 'present': os.path.lexists(p), 'symlink': p.is_symlink(), 'resolved': str(p.resolve())}
    if p.is_symlink():
        value['link'] = os.readlink(p)
    if value['present']:
        s = p.stat()
        if stat.S_ISREG(s.st_mode):
            value.update(kind='file', **pin(read(p)))
        elif stat.S_ISDIR(s.st_mode):
            value['kind'] = 'directory'
            if members:
                value['members'] = sorted(x.name for x in p.iterdir())
        elif stat.S_ISCHR(s.st_mode):
            value.update(kind='character_device', major=os.major(s.st_rdev), minor=os.minor(s.st_rdev))
        else:
            value.update(kind='other', mode=stat.S_IFMT(s.st_mode))
    return value


assert ROOT == Path.cwd() and OUTPUT.resolve() == OUTPUT and not os.path.lexists(OUTPUT)
for name in ('unused_outer_cache', 'unused_inner_cache'):
    assert not os.path.lexists(OUTPUT / name)
candidate_path = PREP / 'discovery01/DEPENDENCY_LOCK.candidate.json'
candidate_pin = pin(read(candidate_path))
assert candidate_pin == {'bytes': 570037, 'sha256': 'bb89d966250b0552a47784a5c4aa0d2aaf5b36bc9057fc177a5e552b9bf042ec'}
candidate = data(candidate_path)
assert candidate['environment'] == ENV8
assert data(RECEPTION / 'RESULT.json')['status'] == 'ROOT_BUILD_PREPARATION_ORIGINALS_CHECKED_PENDING_SAME_AUDITOR_DELTA'
assert data(RECEPTION / 'ENVELOPE_RESULT.json')['status'] == 'FULL_SAVED_ENVELOPES_AND_REVISED_RUNTIME_BINDINGS_PASS'
assert data(RECEPTION / 'INDEPENDENT_DELTA_RESULT.json')['status'] == 'ROOT_ACCEPTS_SAME_AUDITOR_BLD_I1_REVISION01_DELTA'
for name in ('NATIVE02.json', 'ENVELOPE_NATIVE01.json', 'INDEPENDENT_DELTA_NATIVE01.json', 'RECEPTION.md'):
    read(RECEPTION / name)
for name, expected in candidate['code_observations'].items():
    assert pin(read(PREP / name)) == expected
configuration = {p: entry(p, spec['members']) for p, spec in candidate['selector_specs'].items()}
assert configuration == candidate['entries'] and len(configuration) == 840
sources = {name: pin(read(PAPER / name)) for name in candidate['source_observations']}
for name in sources:
    assert (PAPER / name).resolve() == PAPER / name and not (PAPER / name).is_symlink()
changed = [name for name in sources if sources[name] != candidate['source_observations'][name]]
assert changed == ['sections/5_scope.tex']
assert pin(read(OLD_SCOPE)) == candidate['source_observations'][changed[0]] == {'bytes': 1737, 'sha256': '48ea12838dad19fe6849da3cf80cd2837240f392bd6433e73c56b92636a12c0c'}
assert sources[changed[0]] == {'bytes': 2087, 'sha256': '03d72522a90376e18a0a96e8e6dc707af9e182df7f7dc291bb0aacb70ee1b432'}
old, new = read(OLD_SCOPE).decode(), read(PAPER / changed[0]).decode()
old_paragraph = '''At this source-preparation stage, the new verifier has not been executed,
its canonical output has not been produced, and this manuscript has not
been built or independently reviewed. An earlier exploratory author
pilot is separate: its strict runtime-prelock audit failed and its
archived output is not reused as the canonical or as strict manuscript
verification. Fresh production and replay require their own recorded
source, parameter and runtime closure.'''
new_paragraph = '''The new verifier has completed one initial production and a separately
recorded strict author replay pair. Each invocation checked $14523$
predicates over the same $2353$ maps. The complete initial stdout was
adopted as the canonical; three native comparisons checked each replay
against that canonical and the two replays against one another. These
are supporting finite checks, not additional proofs or independent
manuscript reviews; the execution milestone supplies neither a manuscript
build nor review acceptance. An earlier exploratory author pilot remains
separate: its strict runtime-prelock audit failed and its archived output
is not reused as the canonical or as strict manuscript verification.
The new initial production and pair have separately recorded source,
parameter and bounded runtime-closure evidence.'''
assert old.count(old_paragraph) == 1
assert old.replace('is designed to enumerate', 'enumerates').replace(old_paragraph, new_paragraph) == new
main = read(PAPER / 'main.tex').decode()
inputs = re.findall(r'\\input\{([^}]+)\}', main)
expected_inputs = ['math_commands', 'sections/0_abstract', 'sections/1_introduction', 'sections/2_image',
                   'sections/3_clock', 'sections/4_inverse', 'sections/5_scope']
assert inputs == expected_inputs
assert not re.search(r'\\(?:include|input|includegraphics|write18|openin|openout|read|catcode|usepackage|RequirePackage)\b', new)
assert re.findall(r'\\[A-Za-z]+', old) == re.findall(r'\\[A-Za-z]+', new)
assert sorted(p.name for p in (PAPER / 'sections').iterdir()) == sorted(Path(n + '.tex').name for n in inputs if n.startswith('sections/'))
for name, expected in {'verify.py': {'bytes': 13009, 'sha256': '595fbf7c81f52a86192e82b663526ecb9f5abf222f6854859bfee108ff1355f8'},
                       'CANONICAL.json': {'bytes': 1327062, 'sha256': '2a9d1311a491805644efa7cd4884ae50ed9f9ffa48e347b822a7ff68e12ee6b4'}}.items():
    assert pin(read(PAPER / name)) == expected
argv = ['/usr/bin/diff', '-u', str(OLD_SCOPE), str(PAPER / changed[0])]
actual = subprocess.run(argv, cwd=ROOT, env=ENV4, stdin=subprocess.DEVNULL, capture_output=True, timeout=30)
put('SOURCE_DIFF_STDOUT.raw', actual.stdout)
put('SOURCE_DIFF_STDERR.raw', actual.stderr)
put('SOURCE_DIFF_NATIVE.json', {'argv': argv, 'cwd': str(ROOT), 'environment': ENV4, 'native_exit_code': actual.returncode,
                               'stdout': pin(actual.stdout), 'stderr': pin(actual.stderr)})
assert actual.returncode == 1 and actual.stderr == b''
derived = json.loads(json.dumps(candidate))
derived['source_observations'] = sources
assert all(derived[k] == candidate[k] for k in candidate if k != 'source_observations')
source_lock_pin = put('ROOT_DERIVED_SOURCE_LOCK.json', derived)
delta = {'status': 'ROOT_SOURCE_ONLY_DOCUMENTARY_LOCK_DELTA_NO_NEW_DISCOVERY',
         'baseline_candidate': {'path': str(candidate_path), 'pin': candidate_pin},
         'derived_lock': {'path': str(HERE / 'ROOT_DERIVED_SOURCE_LOCK.json'), 'pin': source_lock_pin},
         'changed_field': 'source_observations.sections/5_scope.tex', 'before': candidate['source_observations'][changed[0]],
         'after': sources[changed[0]], 'old_physical_source': str(OLD_SCOPE), 'other_eight_sources_identical': True,
         'all_other_candidate_fields_identical': True, 'TeX_macro_sequence_and_source_graph_identical': True,
         'new_dependency_discovery': False, 'new_science': False, 'builder_code_changed': False}
put('SOURCE_LOCK_DELTA.json', delta)
cold = OUTPUT / 'inner/source_only'
future = {str(cold / row['relative']): entry(cold / row['relative']) for row in derived['cwd_relative_absence_roles'].values()}
assert len(future) == 3 and all(v == {'path': p, 'present': False, 'symlink': False, 'resolved': p} for p,v in future.items())
binding = {'schema': 'p211-initial-source-only-root-binding-v1', 'status': 'ROOT_AUTHORIZED_INITIAL_SOURCE_ONLY_BUILD',
           'scope': 'ONE_INITIAL_BUILD_ONLY', 'environment': ENV8, 'output': str(OUTPUT),
           'adapter_pins': derived['code_observations'], 'source_pins': sources,
           'dependency_lock': {'path': str(HERE / 'ROOT_DERIVED_SOURCE_LOCK.json'), 'pin': source_lock_pin},
           'root_read_receipt': {'path': str(RECEPTION / 'RECEPTION.md'), 'pin': pin(read(RECEPTION / 'RECEPTION.md'))},
           'cwd_relative_configuration': future, 'scientific_execution': False,
           'manuscript_review': False, 'terminal_acceptance': False}
for path, expected in reads.items():
    assert pin(Path(path).read_bytes()) == expected
assert configuration == {p: entry(p, spec['members']) for p, spec in candidate['selector_specs'].items()}
put('INPUTS_AT_BINDING.json', reads)
binding_pin = put('BINDING.json', binding)
result = {'status': 'EXACT_ROOT_BINDING_CREATED_NO_BUILD', 'binding': {'path': str(HERE / 'BINDING.json'), 'pin': binding_pin},
          'source_lock_pin': source_lock_pin, 'configuration_entries': len(configuration), 'bound_future_absence_roles': len(future),
          'source_changes': changed, 'dependency_selector_changes': 0, 'new_scientific_executions': 0, 'TeX_commands': 0,
          'output_absent': not OUTPUT.exists()}
put('RESULT.json', result)
print(json.dumps(result, sort_keys=True))
