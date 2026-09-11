#!/usr/bin/python3.10
"""SOURCE ONLY: two disabled terminal drafts, never a build or root decision.

Fresh documentary assembly source, explicitly adapting accepted initial/
terminal binding field conventions. It has not been imported, AST-parsed,
compiled or executed. Even a future invocation emits only disabled drafts.
No host referent, ambient environment, submitted program or TeX is accessed
as executable code. Every inherited lock field survives except the exact four.
"""
from hashlib import sha256
import copy
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
HERE = QA/'p211_terminal_binding_preparation01'
OUT = QA/'p211_terminal_binding_root01/disabled_assembly01'
PAPER = ROOT/'papers/211-kernel-image-projection-feedback'
ROUND2 = PAPER/'frozen_round2'
NEW_CODE = QA/'p211_round2_preparation01/terminal_build'
OLD_CODE = QA/'p211_initial_build_01/outer/executed_adapter'
OLD_BINDING = QA/'p211_initial_build_binding01/BINDING.json'
OLD_LOCK = QA/'p211_initial_build_binding01/ROOT_DERIVED_SOURCE_LOCK.json'
OLD_LOCK_PIN = {'bytes':570037, 'sha256':'1a879caa4d7bb68fd841e381f37d5ec3e31236ccd6c7b677dbd95492a92bbf87'}
CODE_NAMES = ('build_core.py', 'build_p211.py', 'launch_build.py',
              'prepare_build.py', 'static_checks.py')
SOURCES = ('main.tex', 'math_commands.tex', 'references.bib',
           'sections/0_abstract.tex', 'sections/1_introduction.tex',
           'sections/2_image.tex', 'sections/3_clock.tex',
           'sections/4_inverse.tex', 'sections/5_scope.tex')
CHANGED_FIELDS = ('schema', 'status', 'code_observations', 'terminal_derivation')
OLD_FIELDS = frozenset((
    'code_observations', 'cwd_relative_absence_roles', 'entries', 'environment',
    'historical_inputs', 'ldd_elf_inputs', 'queries', 'query_commands',
    'residual_review', 'schema', 'scope', 'selection_reasons', 'selector_specs',
    'source_observations', 'status'))
PENDING_RECEIPTS = (
    'whole_round2_root_reception', 'fresh_terminal_source_and_binding_reception',
    'complete_inherited_build_key_and_settings_recheck')
ENV8 = {'PATH':'/usr/bin:/bin', 'LANG':'C.UTF-8', 'LC_ALL':'C.UTF-8', 'TZ':'UTC',
        'SOURCE_DATE_EPOCH':'1788825600', 'FORCE_SOURCE_DATE':'1',
        'openin_any':'p', 'openout_any':'p'}
READS = {}


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def relative(name):
    need(isinstance(name, str) and name and '\\' not in name
         and not any(c in name for c in '\x00\r\n\t')
         and not PurePosixPath(name).is_absolute()
         and str(PurePosixPath(name)) == name
         and all(p not in ('', '.', '..') for p in name.split('/')),
         'Nonliteral workspace input: '+repr(name))
    return name


def byte_pin(raw):
    return {'bytes':len(raw), 'sha256':sha256(raw).hexdigest()}


def valid_pin(value):
    need(isinstance(value, dict) and set(value) == {'bytes', 'sha256'}
         and type(value['bytes']) is int and value['bytes'] >= 0
         and isinstance(value['sha256'], str)
         and re.fullmatch('[0-9a-f]{64}', value['sha256']) is not None,
         'Expected an exact byte pin')
    return value


def read(path, expected=None):
    path = Path(path)
    need(path.is_absolute() and path.is_relative_to(ROOT),
         'Only explicitly selected workspace bytes may be read')
    relative(str(path.relative_to(ROOT)))
    need(path.is_file() and not path.is_symlink() and path.resolve() == path,
         'Ordinary physical workspace original required: '+str(path))
    before = path.stat()
    raw = path.read_bytes()
    after = path.stat()
    need(before == after and len(raw) == after.st_size, 'Read drift: '+str(path))
    value = byte_pin(raw)
    need(str(path) not in READS or READS[str(path)] == value, 'Changed original: '+str(path))
    if expected is not None:
        need(value == valid_pin(expected), 'Exact original pin changed: '+str(path))
    READS[str(path)] = value
    return raw


def pairs(items):
    result = {}
    for key, value in items:
        need(key not in result, 'Duplicate JSON object key')
        result[key] = value
    return result


def obj(path, expected=None):
    return json.loads(read(path, expected), object_pairs_hook=pairs,
                      parse_constant=lambda value: (_ for _ in ()).throw(
                          ValueError('Nonfinite JSON constant: '+value)))


def serialized(value):
    return (json.dumps(value, sort_keys=True, indent=2, allow_nan=False)+'\n').encode()


def complete_round2(expected):
    need(set(expected) >= {'SHA256SUMS', 'review_a/SHA256SUMS', 'review_b/SHA256SUMS'}
         and len(expected) == 124, 'Complete 124-file physical Round2 key')
    need(ROUND2.is_dir() and ROUND2.resolve() == ROUND2 and not ROUND2.is_symlink(),
         'Ordinary literal Round2 tree')
    names, directories, wanted = set(), {'.'}, {'.'}
    for name, value in expected.items():
        relative(name)
        read(ROUND2/name, value)
        wanted.update(str(p) for p in PurePosixPath(name).parents)
    # The only enumerated input tree is the explicit complete physical Round2.
    for path in ROUND2.rglob('*'):
        need(path.resolve() == path and not path.is_symlink(), 'No Round2 alias')
        if path.is_file():
            names.add(str(path.relative_to(ROUND2)))
        else:
            need(path.is_dir(), 'No special Round2 entry')
            directories.add(str(path.relative_to(ROUND2)))
    need(names == set(expected) and directories == wanted, 'Exact Round2 membership')
    manifest = ''.join(expected[n]['sha256']+'  '+n+'\n'
                       for n in sorted(expected) if n != 'SHA256SUMS').encode()
    need(read(ROUND2/'SHA256SUMS') == manifest, 'Exact original nonself outer manifest')
    need(sum(v['bytes'] for n,v in expected.items() if n != 'SHA256SUMS') == 10518152,
         'Exact frozen payload bytes')
    return directories


def derive_candidate(prior, adapters):
    """Pure object derivation; no host probes and no authority creation."""
    need(set(prior) == OLD_FIELDS, 'Whole exact original lock field set')
    candidate = copy.deepcopy(prior)
    candidate.update(
        schema='p211-terminal-bounded-dependency-lock-v1',
        status='ROOT_BOUND_EXACT_INHERITED_HOST_KEY_NEW_ADAPTER_ONLY',
        code_observations=copy.deepcopy(adapters),
        terminal_derivation={
            'original_lock':{'path':str(OLD_LOCK), 'pin':OLD_LOCK_PIN},
            'allowed_changes':list(CHANGED_FIELDS), 'host_candidate_extension':False})
    need(set(candidate) == OLD_FIELDS | {'terminal_derivation'}, 'No removed or extra lock field')
    actual_changes = {k for k in set(prior) | set(candidate)
                      if k not in prior or k not in candidate or prior[k] != candidate[k]}
    need(actual_changes == set(CHANGED_FIELDS), 'Exactly four changed/added fields')
    need(all(candidate[k] == prior[k] for k in OLD_FIELDS-set(CHANGED_FIELDS)),
         'Every unchanged nested field retained without pruning or extension')
    return candidate


def main():
    need(Path.cwd() == ROOT and Path(__file__).absolute() == HERE/'assemble_disabled.py',
         'Literal source-only placement/cwd')
    need(sys.argv[1:] == ['--write-disabled-candidates'],
         'Separate explicit documentary-only invocation required')
    need(OUT.parent.is_dir() and OUT.parent.resolve() == OUT.parent
         and not os.path.lexists(OUT), 'Root creates parent separately; exclusive fresh draft output')
    plan = obj(HERE/'INPUT_PLAN.json')
    recipe = obj(HERE/'LOCK_DERIVATION_PLAN.json')
    expected_round2 = obj(HERE/'ROUND2_ALL_FILE_PINS.json')
    need(plan['status'] == 'SOURCE_ONLY_NOT_ASSEMBLED_NOT_DERIVED_NOT_AUTHORIZED'
         and plan['future_assembly_output'] == str(OUT.relative_to(ROOT)),
         'Only the pinned source-only plan')
    for name, value in plan['input_pins'].items():
        read(ROOT/relative(name), value)
    need(plan['original_lock'] == {'path':str(OLD_LOCK), 'pin':OLD_LOCK_PIN},
         'One exact accepted original lock')
    prior = obj(OLD_LOCK, OLD_LOCK_PIN)
    initial = obj(OLD_BINDING)
    adapters = {n:byte_pin(read(NEW_CODE/n, plan['new_adapter_pins'][n])) for n in CODE_NAMES}
    originals = {n:byte_pin(read(OLD_CODE/n, plan['original_adapter_pins'][n])) for n in CODE_NAMES}
    need(set(plan['new_adapter_pins']) == set(plan['original_adapter_pins']) == set(CODE_NAMES),
         'Exactly five fresh and five actual original sources')
    need(initial['adapter_pins'] == originals == prior['code_observations'],
         'Complete original adapter lineage')
    need(initial['dependency_lock'] == {'path':str(OLD_LOCK), 'pin':OLD_LOCK_PIN},
         'Initial binding points to the actual full lock')
    need(prior['environment'] == plan['fixed_environment'] == ENV8,
         'Only the inherited literal ENV8; ambient environment is never collected')
    sources = {n:byte_pin(read(PAPER/n, plan['source_pins'][n])) for n in SOURCES}
    need(set(plan['source_pins']) == set(SOURCES)
         and sources == initial['source_pins'] == prior['source_observations'],
         'Exactly nine unchanged live/initial/inherited sources')
    directories = complete_round2(expected_round2)
    need(all(expected_round2[n] == sources[n] for n in SOURCES), 'All nine frozen sources agree')
    need(set(prior['cwd_relative_absence_roles']) == {'TEXMFHOME', 'TEXMFCONFIG', 'TEXMFVAR'}
         and {r['relative'] for r in prior['cwd_relative_absence_roles'].values()} ==
             {'texmf', '.texlive2021/texmf-config', '.texlive2021/texmf-var'},
         'Exactly three unchanged relative search roles, not current absence observations')
    need(recipe['changed_fields'] == list(CHANGED_FIELDS)
         and recipe['original_lock'] == plan['original_lock'], 'Exact disclosed derivation recipe')
    artifacts = {}
    for number in (1, 2):
        template = obj(HERE/('BINDING_%d.disabled.json'%number))
        original_template = obj(ROOT/relative(plan['disabled_original_templates'][str(number)]))
        need(set(template) == set(original_template), 'No added or omitted binding field')
        prepared_changes = {'status', 'adapter_pins', 'round2_package', '_note'}
        need(all(template[k] == original_template[k]
                 for k in set(original_template)-prepared_changes),
             'All unchanged original disabled-template fields retained')
        package = copy.deepcopy(original_template['round2_package'])
        package['all_file_pins'] = expected_round2
        need(template['round2_package'] == package and template['status'] ==
             'SOURCE_ONLY_PHYSICAL_ROUND2_PINNED_PENDING_ACCEPTANCE_AND_SEPARATE_ROOT_BINDING',
             'Only full physical pins added, never an accepted-round status')
        need(template['build_number'] == number and type(template['build_number']) is int
             and template['enabled'] is False, 'Independent literal disabled build role')
        cold = PAPER/'qa_final'/('cold_build_'+str(number))
        need(template['output'] == str(cold) and not os.path.lexists(cold),
             'No existing, partial or shared cold-build output')
        need(template['environment'] == ENV8 and template['source_pins'] == sources
             and template['adapter_pins'] == adapters
             and template['original_adapter_pins'] == originals, 'Whole template source/code keys')
        need(template['round2_package']['all_file_pins'] == expected_round2
             and template['round2_package']['root'] == str(ROUND2), 'Whole physical Round2 template')
        need(template['dependency_lock'] is None and template['cwd_relative_configuration'] is None,
             'No invented derived lock or future cwd observation')
        need(all(template['receipt_references'][r] is None for r in PENDING_RECEIPTS)
             and template['root_authorization'] ==
                 {'issuer':None, 'decision':None, 'build_number':number, 'record':None},
             'Missing actual root receipts/authority remain blocking, even if newer files exist')
        for name, ref in template['receipt_references'].items():
            if ref is not None:
                read(ref['path'], ref['pin'])
        candidate = derive_candidate(prior, adapters)
        need(candidate == {**copy.deepcopy(prior), **recipe['new_field_values']},
             'Whole candidate equals exact separately documented four-field recipe')
        prefix = 'build_%d/'%number
        lock_raw = serialized(candidate)
        artifacts[prefix+'DEPENDENCY_LOCK.candidate.json'] = lock_raw
        disabled = copy.deepcopy(template)
        disabled['dependency_lock'] = {
            'path':str(OUT/(prefix+'DEPENDENCY_LOCK.candidate.json')), 'pin':byte_pin(lock_raw)}
        # Required lock status strings are schema content, not self-issued authority.
        # Binding enabled/status/receipts/cwd/root decision stay disabled and null.
        artifacts[prefix+'BINDING.disabled.json'] = serialized(disabled)
    need(artifacts['build_1/DEPENDENCY_LOCK.candidate.json'] ==
         artifacts['build_2/DEPENDENCY_LOCK.candidate.json'], 'Identical exact keys, separate physical candidates')
    for path, expected in dict(READS).items():
        read(path, expected)
    result = {'status':'DISABLED_TERMINAL_CANDIDATES_ONLY_NOT_ROOT_ACCEPTANCE',
        'read_paths':len(READS), 'round2_files':124, 'round2_directories':sorted(directories),
        'build_roles':[1,2], 'new_adapter_files':5, 'original_adapter_files':5,
        'source_files':9, 'lock_field_changes':list(CHANGED_FIELDS),
        'all_original_host_fields_retained':True, 'host_paths_dereferenced':0,
        'ambient_environment_collected':False, 'science_or_submitted_adapter_executions':0,
        'builds':0, 'root_authority_issued':False, 'cwd_absence_observations':None,
        'whole_round2_accepted':False, 'terminal_accepted':False}
    OUT.mkdir()
    for number in (1, 2):
        (OUT/('build_'+str(number))).mkdir()
    artifacts['INPUTS.json'] = serialized(READS)
    artifacts['RESULT.json'] = serialized(result)
    for name, raw in artifacts.items():
        with (OUT/name).open('xb') as stream:
            stream.write(raw)
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
