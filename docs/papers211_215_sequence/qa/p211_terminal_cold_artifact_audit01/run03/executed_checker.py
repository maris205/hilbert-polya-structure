#!/usr/bin/python3.10
"""Cold1-only documentary adaptation of the initial independent saved-build auditor.

Never imports or executes submitted code or dereferences inherited host paths.
Old 840/1299 keys and non-source Round2 pins are archived data, not fresh checks.

Only the explicitly assigned new QA directory is writable. The checker is
not a build, scientific verifier or visual review. Every run uses exclusive
output and preserves its exact executed checker before inspecting evidence.
"""
import collections
import difflib
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import struct
import sys
import time
import traceback

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers211_215_sequence/qa'
HERE = QA / 'p211_terminal_cold_artifact_audit01'
BUILD = ROOT / 'papers/211-kernel-image-projection-feedback/qa_final/cold_build_1'
INNER = BUILD / 'inner'
OUTER = BUILD / 'outer'
COLD = INNER / 'source_only'
CONTROL = QA / 'p211_terminal_enable_root01/build_1'
BINDDIR = CONTROL / 'enable01'
CAPTURE = CONTROL / 'capture01'
ENTRY = CONTROL / 'capture_entry01'
PREP = QA / 'p211_round2_preparation01/terminal_build'
OLDPREP = QA / 'p211_initial_build_01/outer/executed_adapter'
OLDLOCK = QA / 'p211_initial_build_binding01/ROOT_DERIVED_SOURCE_LOCK.json'
OLDBIND = QA / 'p211_initial_build_binding01/BINDING.json'
PAPER = ROOT / 'papers/211-kernel-image-projection-feedback'
BINDPATH = BINDDIR / 'BINDING.json'
LOCKPATH = BINDDIR / 'DEPENDENCY_LOCK.json'
ROUND2 = PAPER / 'frozen_round2'
ENV8 = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8',
        'TZ': 'UTC', 'SOURCE_DATE_EPOCH': '1788825600', 'FORCE_SOURCE_DATE': '1',
        'openin_any': 'p', 'openout_any': 'p'}
SOURCE_NAMES = ('main.tex', 'math_commands.tex', 'references.bib',
                'sections/0_abstract.tex', 'sections/1_introduction.tex',
                'sections/2_image.tex', 'sections/3_clock.tex',
                'sections/4_inverse.tex', 'sections/5_scope.tex')
CODE_NAMES = ('build_core.py', 'prepare_build.py', 'build_p211.py',
              'launch_build.py', 'static_checks.py')
GENERATED = {'main.' + ext for ext in ('aux', 'bbl', 'blg', 'fls', 'log', 'out', 'pdf', 'toc')}
TEX_ARGV = ['/usr/bin/pdflatex', '-no-shell-escape', '-interaction=nonstopmode',
            '-halt-on-error', '-file-line-error', '-recorder', 'main.tex']
PASS_NAMES = ('pass1', 'bibtex', 'pass2', 'pass3')
ROLES = ('SOURCE', 'EXTERNAL_PRELOCKED', 'GENERATED_BEFORE',
         'GENERATED_EARLIER_OUTPUT_SAME_PASS', 'GENERATED_OUTPUT')
EXPECTED_MANIFEST = {'bytes': 39346, 'sha256': '2fba3b0638d5ffc9596e68e7cf93ead2fd3fa5c0fcac6a403327dc5528c34226'}
EXPECTED_BINDING = {'bytes': 27981, 'sha256': 'e800309c7319eef06ee21acf04dc581c0534ca074a4adba2740cf860f9179767'}
OLD_LOCK_PIN = {'bytes': 570037, 'sha256': '1a879caa4d7bb68fd841e381f37d5ec3e31236ccd6c7b677dbd95492a92bbf87'}
EXPECTED_LOCK = {'bytes': 570551, 'sha256': 'e951219fdfa40ed1e6780f493089b059f4417bb5cfbab9b3cbdfbf87e20a346e'}
EXPECTED_PDF = {'bytes': 301007, 'sha256': '532b8c462e907878c3d75829b2c4ff86de7d59c137efa91b61ebc80717a077dc'}
DENIED = {PAPER / n for n in ('CANONICAL.json', 'verify.py', 'PROOF_PACKAGE.md')}
READS, COUNTS, DETAILS = {}, collections.Counter(), {}
OUTPUT = None
ARCHIVE = {}
ARCHIVED_ONLY_REFERENTS = set()
FINDINGS = []
EXPLICIT_LOCAL = {OLDLOCK, OLDBIND, HERE/'inspect_cold1.py', HERE/'original_inspect_build.py',
    QA/'p211_initial_build_independent_reception/run01/READ_INPUTS_BEFORE.json',
    QA/'p211_initial_build_01/inner/CONFIGURATION_BEFORE.json',
    QA/'p211_initial_build_adoption01/HISTORICAL_MAPPING.json',
    QA/'p211_b_final_root/BUILD_REUSE_NATIVE01.json',
    QA/'p211_terminal_enable_preparation01/INPUT_PLAN.json',
    QA/'p211_terminal_enable_preparation01/terminal_control.py',
    ROOT/'docs/papers211_215_sequence/reviews/p211_a/inspect_build_reuse.py'}
EXPLICIT_LOCAL.update(PAPER/n for n in SOURCE_NAMES)
EXPLICIT_LOCAL.update(ROUND2/n for n in SOURCE_NAMES)
EXPLICIT_LOCAL.update(PREP/n for n in CODE_NAMES)
EXPLICIT_LOCAL.update(OLDPREP/n for n in CODE_NAMES)
LOCAL_TREES = (BUILD, BINDDIR, CAPTURE, ENTRY)


def demand(test, group, detail):
    COUNTS[group] += 1
    if not test:
        raise AssertionError(group + ': ' + str(detail))


def raw_pin(raw):
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def authorized_local(path):
    p = Path(path)
    demand(p.is_absolute() and str(p) == os.path.normpath(str(p)) and
           p.is_relative_to(ROOT) and 'cold_build_2' not in p.parts and
           not (p.is_relative_to(QA/'p211_terminal_enable_root01') and 'build_2' in p.parts),
           'read_scope', 'workspace-only normalized build1 path: '+str(p))
    demand(p in EXPLICIT_LOCAL or any(p.is_relative_to(base) for base in LOCAL_TREES) or
           (OUTPUT is not None and p.is_relative_to(OUTPUT)),
           'read_scope', 'explicit artifact/read role: '+str(p))
    demand(p.resolve() == p and not p.is_symlink(), 'read_scope', 'no workspace symlink: '+str(p))
    return p


def read(path):
    p = authorized_local(path)
    raw = p.read_bytes()
    value = raw_pin(raw)
    demand(str(p) not in READS or READS[str(p)] == value, 'read_consistency', str(p))
    READS[str(p)] = value
    return raw

def pin(path):
    return raw_pin(read(path))


def reject_duplicate_pairs(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError('duplicate JSON key '+key)
        value[key] = item
    return value


def obj(path):
    # CPython parses arbitrary-sized integers exactly; never round-trips via JS.
    value = json.loads(read(path), object_pairs_hook=reject_duplicate_pairs,
                       parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))
    def typed(item, field=''):
        if isinstance(item, dict):
            if field in {'stat','lstat'} and {'ctime_ns','mtime_ns','inode','mode'} <= set(item):
                demand(all(type(v) is int for v in item.values()),
                       'precise_json_integers', 'every rich '+field+' metadata field')
            for key, child in item.items():
                typed(child, key)
        elif isinstance(item, list):
            for child in item:
                typed(child)
        elif field in {'bytes','ctime_ns','mtime_ns','device','gid','inode','nlink',
                       'size','uid','pid','session','native_exit_code','timeout_seconds',
                       'build_number','major','minor'}:
            demand(type(item) is int, 'precise_json_integers', field)
    typed(value)
    return value

def put(name, value):
    p = OUTPUT / name
    demand(p.parent == OUTPUT and p.resolve() == p, 'output_scope', str(p))
    raw = value if isinstance(value, bytes) else (json.dumps(value, sort_keys=True, indent=2) + '\n').encode()
    with p.open('xb') as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    return raw_pin(raw)


def current_entry(path, members=False):
    """Archived host/metadata consistency, physical reads only for scoped local files."""
    p = Path(path)
    if str(p) in ARCHIVE:
        row = ARCHIVE[str(p)]
        # For exact allowed workspace file roles also verify live artifact bytes.
        if p in EXPLICIT_LOCAL or any(p.is_relative_to(base) for base in LOCAL_TREES):
            if row.get('kind') == 'file':
                demand(pin(p) == {k:row[k] for k in ('bytes','sha256')},
                       'local_artifact_current', str(p))
        else:
            ARCHIVED_ONLY_REFERENTS.add(str(p))
        return row
    authorized_local(p)
    demand(p.is_file(), 'local_artifact_current', str(p))
    return {'path':str(p),'present':True,'symlink':False,'resolved':str(p),'kind':'file',**pin(p)}


def archived_resolve(path):
    """Lexical/archived resolution; never stat/resolve a host spelling."""
    p = Path(path)
    if p.is_relative_to(ROOT):
        return p
    demand(str(p) in ARCHIVE, 'archived_resolution', str(p))
    return Path(ARCHIVE[str(p)]['resolved'])

def regular_members(base):
    result = {}
    for p in sorted(base.rglob('*')):
        demand(not p.is_symlink(), 'physical_package', str(p))
        if p.is_file():
            result[p.relative_to(base).as_posix()] = p
    return result


def manifest(base, expected=None, count=None):
    path = base / 'SHA256SUMS'
    raw = read(path)
    if expected is not None:
        demand(raw_pin(raw) == expected, 'manifest_identity', str(path))
    rows = {}
    for line in raw.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        demand(match is not None, 'manifest_parse', line)
        digest, name = match.groups()
        relative = Path(name)
        demand(not relative.is_absolute() and '..' not in relative.parts and
               name != 'SHA256SUMS' and name not in rows, 'manifest_nonself', name)
        p = base / relative
        demand(p.resolve() == p and p.is_file(), 'manifest_physical', name)
        value = pin(p)
        demand(value['sha256'] == digest, 'manifest_payload', name)
        rows[name] = value
    actual = regular_members(base)
    demand(set(rows) == set(actual) - {'SHA256SUMS'}, 'manifest_complete', str(base))
    demand(list(rows) == sorted(rows), 'manifest_order', str(base))
    if count is not None:
        demand(len(rows) == count, 'manifest_count', str(base))
    return {'root': str(base), 'payloads': len(rows), 'manifest': raw_pin(raw),
            'payload_bytes': sum(v['bytes'] for v in rows.values())}


def expected_python(role):
    name = 'launch_build.py' if role == 'outer' else 'build_p211.py'
    return ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
            'pycache_prefix=' + str(BUILD / ('unused_' + role + '_cache')),
            str(PREP / name), '--binding', str(BINDPATH),
            '--binding-sha256', EXPECTED_BINDING['sha256']]


def source_and_binding():
    demand(pin(BINDPATH) == EXPECTED_BINDING and pin(LOCKPATH) == EXPECTED_LOCK,
           'binding', 'exact enabled binding/derived lock')
    binding, lock = obj(BINDPATH), obj(LOCKPATH)
    demand(binding['schema'] == 'p211-terminal-source-only-root-binding-v1' and
           binding['status'] == 'ROOT_AUTHORIZED_ONE_P211_TERMINAL_COLD_BUILD' and
           binding['scope'] == 'ONE_OF_EXACTLY_TWO_PHYSICAL_TERMINAL_BUILDS' and
           binding['output'] == str(BUILD) and binding['build_number'] == 1 and
           binding['enabled'] is True and binding['source_root'] == str(PAPER) and
           binding['round2_source_root'] == str(ROUND2), 'binding', 'literal terminal roles')
    demand(binding['environment'] == lock['environment'] == ENV8 and
           all(binding[k] is False for k in ('scientific_execution','manuscript_review','terminal_acceptance')),
           'binding', 'scope/settings')
    demand(binding['dependency_lock'] == {'path':str(LOCKPATH),'pin':EXPECTED_LOCK},
           'binding', 'exact dependency association')
    for ref in [binding['accepted_initial_binding'],binding['root_authorization']['record'],
                *binding['receipt_references'].values()]:
        p=Path(ref['path']); EXPLICIT_LOCAL.add(p)
        demand(set(ref)=={'path','pin'} and pin(p)==ref['pin'], 'binding_receipts', str(p))
    demand(binding['accepted_initial_binding']['path']==str(OLDBIND) and
           set(binding['receipt_references']) == {
               'accepted_initial_build_reception','complete_inherited_build_key_and_settings_recheck',
               'fresh_terminal_source_and_binding_reception','whole_final_b_root_reception','whole_round2_root_reception'},
           'binding_receipts', 'complete five roles')
    authority=binding['root_authorization']
    demand(authority['issuer']=='/root' and authority['build_number']==1 and authority['decision']==
           'AUTHORIZE_ONE_P211_SOURCE_ONLY_TERMINAL_BUILD_AFTER_ACCEPTED_ROUND2',
           'binding_receipts', 'one exact authority')
    prior=obj(OLDBIND); original_lock=obj(OLDLOCK)
    demand(pin(OLDLOCK)==OLD_LOCK_PIN and prior['source_pins']==binding['source_pins'] and
           prior['adapter_pins']==binding['original_adapter_pins'], 'lineage', 'original objects')
    expected_lock=dict(original_lock)
    expected_lock.update(schema='p211-terminal-bounded-dependency-lock-v1',
        status='ROOT_BOUND_EXACT_INHERITED_HOST_KEY_NEW_ADAPTER_ONLY',
        code_observations=binding['adapter_pins'],
        terminal_derivation={'original_lock':{'path':str(OLDLOCK),'pin':OLD_LOCK_PIN},
            'allowed_changes':['schema','status','code_observations','terminal_derivation'],
            'host_candidate_extension':False})
    demand(lock==expected_lock, 'lineage', 'all inherited lock fields exact; 840 paths remain data')
    demand(set(binding['adapter_pins'])==set(CODE_NAMES) and
           binding['adapter_pins']==lock['code_observations'], 'code_snapshot', 'five source roles')
    for name in CODE_NAMES:
        demand(pin(PREP/name)==pin(OUTER/'executed_adapter'/name)==binding['adapter_pins'][name] and
               pin(OLDPREP/name)==binding['original_adapter_pins'][name], 'code_snapshot', name)
    sources = binding['source_pins']
    demand(set(sources) == set(SOURCE_NAMES) and sources == lock['source_observations'],
           'source', 'exact nine roles')
    for name in SOURCE_NAMES:
        for base in (PAPER, COLD, ROUND2):
            p = base / name
            demand(p.resolve() == p and not p.is_symlink() and pin(p) == sources[name], 'source', str(p))
    initial = obj(INNER / 'SOURCE_ONLY_INITIAL.json')
    demand(initial == sources, 'source', 'cold initial nine-source record')
    for base in (INNER, OUTER):
        demand(obj(base / 'SOURCES_BEFORE.json') == obj(base / 'SOURCES_AFTER.json') == sources,
               'source_closure', str(base))
    demand(obj(INNER / 'COPIED_SOURCES_AFTER.json') == sources, 'source_closure', 'copied sources after')
    demand(set(regular_members(COLD)) <= set(SOURCE_NAMES) | GENERATED, 'source_closure', 'only permitted local products')
    graph = read(PAPER / 'main.tex').decode()
    demand(re.findall(r'\\input\{([^}]+)\}', graph) == [n[:-4] for n in SOURCE_NAMES if n not in ('main.tex', 'references.bib')],
           'source_graph', 'ordered literal inputs')
    demand('\\documentclass[11pt,a4paper]{amsart}' in graph and
           '\\bibliographystyle{amsplain}' in graph and '\\bibliography{references}' in graph,
           'source_graph', 'class/style/database')
    packages = [p for group in re.findall(r'\\usepackage(?:\[[^\]]*\])?\{([^}]+)\}', graph) for p in group.split(',')]
    demand(packages == ['fontenc','lmodern','geometry','amsmath','amssymb','mathtools','booktabs','microtype','hyperref'],
           'source_graph', 'exact package set/order')
    for name in SOURCE_NAMES:
        body = read(PAPER / name).decode()
        demand(not re.search(r'\\(?:include|includegraphics|write18|openin|openout|read|catcode)\b', body),
               'source_graph', 'no extra declared I/O: ' + name)
        if name != 'main.tex':
            demand(not re.search(r'\\(?:input|usepackage|RequirePackage|documentclass)\b', body),
                   'source_graph', 'no nested graph: ' + name)

    package=binding['round2_package']; r2=package['all_file_pins']
    demand(package['root']==str(ROUND2) and package['payload_count']==123 and
           package['total_file_count']==len(r2)==124 and
           all(r2[n]==sources[n] for n in SOURCE_NAMES), 'round2_metadata', 'complete accepted package key')
    demand({'SHA256SUMS','review_a/SHA256SUMS','review_b/SHA256SUMS'}<=set(r2),
           'round2_metadata', 'all three seal roles')
    DETAILS['source_lineage']={'source_files':9,'source_bytes':sum(v['bytes'] for v in sources.values()),
        'current_cold_and_frozen_source_bytes_equal':True,'round2_other_115_paths':'SAVED_KEY_ONLY_NOT_REREAD',
        'old_840_host_referents':'ARCHIVED_DATA_NOT_FRESH_HOST_QUERY','new_science':False}
    return binding,lock

def configuration(binding, lock):
    demand(len(lock['selector_specs']) == len(lock['entries']) == 840 and
           set(lock['selector_specs']) == set(lock['entries']), 'configuration', '840 selected spellings')
    future = binding['cwd_relative_configuration']
    expected_future = {str(COLD / row['relative']) for row in lock['cwd_relative_absence_roles'].values()}
    demand(set(future) == expected_future and len(future) == 3, 'configuration', 'three future cwd roles')
    for path, row in future.items():
        demand(row == {'path':path,'present':False,'symlink':False,'resolved':path}, 'configuration', path)
    specs = dict(lock['selector_specs'])
    specs.update({p:{'members':False} for p in future})
    expected = dict(lock['entries'])
    expected.update(future)
    actual = expected
    ARCHIVE.update(expected)
    demand(len(actual)==843, 'configuration', 'complete archived configuration membership')
    put('CONFIGURATION_ARCHIVED_EXPECTED.json', actual)
    for base in (INNER,OUTER):
        demand(obj(base/'CONFIGURATION_BEFORE.json') == obj(base/'CONFIGURATION_AFTER.json') == expected,
               'configuration', 'saved closure '+str(base))
    for name in ('unused_outer_cache','unused_inner_cache'):
        demand(not os.path.lexists(BUILD/name), 'configuration', 'unused isolated cache '+name)
    coverage = {}
    for row in actual.values():
        if row.get('kind') == 'file':
            value = {k:row[k] for k in ('bytes','sha256')}
            demand(row['resolved'] not in coverage or coverage[row['resolved']] == value,
                   'configuration', 'resolved aliases agree')
            coverage[row['resolved']] = value
    originals = {str(BINDPATH):EXPECTED_BINDING,str(LOCKPATH):EXPECTED_LOCK,
                 str(OLDBIND):pin(OLDBIND),str(OLDLOCK):OLD_LOCK_PIN}
    for ref in [binding['root_authorization']['record'],*binding['receipt_references'].values()]:
        originals[ref['path']]=ref['pin']
    originals.update({str(PREP/n):binding['adapter_pins'][n] for n in CODE_NAMES})
    originals.update({str(OLDPREP/n):binding['original_adapter_pins'][n] for n in CODE_NAMES})
    originals.update({str(PAPER/n):binding['source_pins'][n] for n in SOURCE_NAMES})
    originals.update({str(ROUND2/n):v for n,v in binding['round2_package']['all_file_pins'].items()})
    for p,v in originals.items():
        ARCHIVE[p]={'path':p,'present':True,'symlink':False,'resolved':p,'kind':'file',**v}
    for base in (INNER,OUTER):
        demand(obj(base/'ORIGINALS_BEFORE.json') == obj(base/'ORIGINALS_AFTER.json') == originals,
               'original_closure', str(base))
    for p,v in originals.items():
        if Path(p) in EXPLICIT_LOCAL:
            demand(pin(p) == v, 'original_closure', p)
        else:
            ARCHIVED_ONLY_REFERENTS.add(p)
    for role in ('inner','outer'):
        entered = obj((INNER if role=='inner' else OUTER)/'ENTERED.json')
        demand(entered['binding'] == EXPECTED_BINDING and entered['argv'] == expected_python(role) and
               entered['environment'] == ENV8, 'parent_entry', role)
        if role == 'outer':
            demand(entered['inner_started'] is False and entered['cwd'] == str(ROOT), 'parent_entry', 'fresh outer')
    samples = [('outer_before',obj(OUTER/'PARENT_RUNTIME_BEFORE.json'),'outer'),
               ('outer_after',obj(OUTER/'PARENT_RUNTIME_AFTER.json'),'outer'),
               ('inner_before',obj(INNER/'ENTERED.json')['runtime'],'inner'),
               ('inner_after',obj(INNER/'PARENT_RUNTIME_AFTER.json'),'inner')]
    runtime_rows = []
    known = {**coverage,**originals}
    for label,sample,role in samples:
        demand(sample['environment']==ENV8 and sample['cwd']==str(ROOT) and
               sample['argv']==expected_python(role) and sample['locale_ctype']=='C.UTF-8', 'runtime', label+' settings')
        demand(sample['sys_path']==['/usr/lib/python310.zip','/usr/lib/python3.10','/usr/lib/python3.10/lib-dynload'] and
               sample['pycache_prefix']==str(BUILD/('unused_'+role+'_cache')), 'runtime', label+' isolated paths')
        for field,value in [('isolated','1'),('no_site','1'),('no_user_site','1'),('ignore_environment','1'),
                            ('dont_write_bytecode','1'),('optimize','0')]:
            demand(re.search(r'(?:\(|, )'+field+'='+value+r'(?:,|\))',sample['flags']) is not None,
                   'runtime', label+' '+field)
        raw = sample['maps_raw'].encode()
        demand(raw_pin(raw)==sample['maps_pin'], 'runtime', label+' raw map identity')
        mapped = set()
        for line in sample['maps_raw'].splitlines():
            cols=line.split(None,5)
            if len(cols)==6 and cols[5].startswith('/'):
                demand(not cols[5].endswith(' (deleted)'), 'runtime', label+' no deleted mapping')
                mapped.add(str(archived_resolve(cols[5])))
        demand(mapped==set(sample['mapped_files']), 'runtime', label+' complete raw-map parse')
        for p,v in sample['mapped_files'].items():
            demand(known.get(p)==v, 'runtime_archived', label+' mapped '+p)
        for name,row in sample['modules'].items():
            p=row['path']; v={k:row[k] for k in ('bytes','sha256')}
            demand(Path(p).suffix not in ('.pyc','.pyo') and known.get(p)==v,
                   'runtime_archived', label+' module '+name)
        runtime_rows.append({'sample':label,'modules':len(sample['modules']),'mapped_files':len(mapped),
                             'maps_pin':sample['maps_pin']})
    DETAILS['parent_runtime'] = runtime_rows
    DETAILS['configuration'] = {'spellings':843,'base_spellings':840,'future_absence':3,
                                 'file_entries':sum(v.get('kind')=='file' for v in actual.values()),
                                 'membership_entries':sum('members' in v for v in actual.values())}
    return specs,expected,originals,coverage

def check_native(base,label,expected_argv,expected_cwd,extra_inputs,timeout,expected_exits,lock,env=None,schema='p211-native-attempt-v1',direct=False):
    environment = ENV8 if env is None else env
    directory=(base/label) if direct else (base/'commands'/label)
    demand(set(p.name for p in directory.iterdir())=={'ATTEMPT.json','SPAWNED.json','RECEIPT.json',
           'INPUTS_BEFORE.json','INPUTS_AFTER.json','stdout.raw','stderr.raw'}, 'native_complete', label)
    attempt,spawn,receipt=(obj(directory/name) for name in ('ATTEMPT.json','SPAWNED.json','RECEIPT.json'))
    demand(all(receipt.get(k)==v for k,v in attempt.items()), 'native_fields', label+' exact attempt')
    demand(attempt['argv']==expected_argv and attempt['cwd']==str(expected_cwd) and attempt['environment']==environment,
           'native_fields', label+' literal argv/cwd/ENV8')
    demand(attempt['schema']==schema and attempt['label']==label and
           attempt['timeout_seconds']==timeout and attempt['expected_exit_codes']==expected_exits and
           attempt['requested_new_session'] is True and attempt['stdin']=={'path':'/dev/null','policy':'DEVNULL'},
           'native_fields', label+' complete request')
    demand(spawn['pid']==spawn['session'] and type(spawn['pid']) is int and type(spawn['session']) is int and spawn['pid']>0 and
           attempt['attempted_epoch']<=spawn['spawned_epoch']<=receipt['ended_epoch'], 'native_identity', label)
    demand(receipt['native_handle_received'] is True and receipt['launch_outcome']=='KNOWN_NATIVE_HANDLE' and
           type(receipt['native_exit_code']) is int and receipt['native_exit_code'] in expected_exits and receipt['wrapper_reason']=='NATIVE_EXIT' and
           receipt['error'] is None and receipt['successful'] is True and receipt['streams_settled'] is True,
           'native_outcome', label)
    demand(receipt['owned_session_interventions']==receipt['remaining_session_members']==
           receipt['session_members_at_settlement']==[], 'native_settlement', label)
    before,after=obj(directory/'INPUTS_BEFORE.json'),obj(directory/'INPUTS_AFTER.json')
    demand(before==after and receipt['direct_inputs_equal'] is True, 'native_inputs', label+' complete pair')
    keys={expected_argv[0],'/dev/null',*map(str,extra_inputs)}
    demand(set(before)==keys, 'native_inputs', label+' exact direct-input membership')
    for p,v in before.items():
        if label=='bibtex' and p==str(COLD/'main.aux'):
            # Later TeX passes may update this generated input. Its native
            # before/after key must bind the physical same-stage archives,
            # not an anachronistic final-file pin.
            archived=INNER/'pass_artifacts_bibtex'
            value=pin(archived/'before/main.aux')
            demand(pin(archived/'after/main.aux')==value and
                   v=={'path':p,'present':True,'symlink':False,'resolved':p,'kind':'file',**value},
                   'native_inputs', label+' exact archived generated auxiliary')
        else:
            demand(current_entry(p)==v, 'native_inputs', label+' archived-or-physical-local '+p)
        if p in lock['entries']:
            demand(v==lock['entries'][p], 'native_inputs', label+' prelocked '+p)
    raw={name:read(directory/name) for name in ('stdout.raw','stderr.raw')}
    demand(set(receipt['streams'])==set(raw) and
           all(receipt['streams'][n]==raw_pin(v) for n,v in raw.items()), 'native_raw', label)
    return receipt,spawn,raw

def commands_and_envelopes(binding,lock,originals,coverage):
    result=obj(INNER/'RESULT.json'); outer_result=obj(OUTER/'RESULT.json')
    demand(result['status']=='TERMINAL_BUILD_RECORDED_NOT_VIEWED_NOT_ACCEPTED' and result['failures']==[] and
           outer_result['status']=='TERMINAL_BUILD_CAPTURED_PENDING_ROOT_INSPECTION' and outer_result['failures']==[],
           'result_status', 'both saved products')
    demand(result['scientific_executions']==result['manuscript_reviews']==0 and
           result['visual_review']=='NOT_VIEWED' and not any(result[k] for k in
               ('build_acceptance','terminal_acceptance','paper_completion')), 'result_scope', 'inner')
    demand(outer_result['scientific_executions']==0 and outer_result['A_B_review_gates']=='SEPARATE_NOT_EXECUTED' and
           outer_result['visual_review']=='NOT_VIEWED' and outer_result['build_acceptance'] is False and
           outer_result['terminal_acceptance'] is False, 'result_scope', 'outer')
    elf=lock['ldd_elf_inputs']; demand(len(elf)==33, 'native_plan', '33 ELF inputs')
    plan=[('ldd_before',['/usr/bin/ldd',*elf],INNER,elf,120,[0])]
    for name in ('pdflatex','bibtex','kpsewhich'):
        plan.append(('version_'+name,['/usr/bin/'+name,'--version'],INNER,[],120,[0]))
    for name in ('pdfinfo','pdffonts','pdftotext','pdftoppm'):
        plan.append(('version_'+name,['/usr/bin/'+name,'-v'],INNER,[],120,[0]))
    config_keys=[k for k in sorted(lock['queries']) if k.startswith('var_') or k=='expanded_TEXMF']
    for key in config_keys:
        plan.append(('config_'+key,lock['query_commands'][key],COLD,[],120,[0,1]))
    cfg=['/usr/bin/kpsewhich','--progname=pdflatex','--engine=pdftex','--all','amsart.cfg']
    plan.append(('optional_amsart_cfg_before',cfg,COLD,[],120,[0,1]))
    style=lock['queries']['explicit_graph_seeds']['resolutions']['amsplain.bst']
    demand(len(style)==1, 'bibtex', 'unique bound amsplain style')
    source_paths=[COLD/n for n in SOURCE_NAMES]
    for name in PASS_NAMES:
        plan.append((name,['/usr/bin/bibtex','main'] if name=='bibtex' else TEX_ARGV,COLD,
                     source_paths+([COLD/'main.aux',Path(style[0])] if name=='bibtex' else []),600,[0]))
    for name in ('pdfinfo','pdffonts'):
        plan.append((name,['/usr/bin/'+name,'main.pdf'],COLD,[COLD/'main.pdf'],120,[0]))
    plan.append(('pdftotext',['/usr/bin/pdftotext','-layout','main.pdf',str(INNER/'main.txt')],COLD,[COLD/'main.pdf'],120,[0]))
    pages=result['measurements']['pages']
    demand(pages==5, 'measurement', 'root-reported page count')
    for number in range(1,pages+1):
        name='render_%04d'%number; prefix=INNER/'pages'/('page-%04d'%number)
        plan.append((name,['/usr/bin/pdftoppm','-f',str(number),'-l',str(number),'-singlefile','-png','-r','105',
                           'main.pdf',str(prefix)],COLD,[COLD/'main.pdf'],180,[0]))
    plan += [('optional_amsart_cfg_after',cfg,COLD,[],120,[0,1]),('ldd_after',['/usr/bin/ldd',*elf],INNER,elf,120,[0])]
    demand([r['label'] for r in result['native_commands']]==[p[0] for p in plan], 'native_order', 'complete planned order')
    demand(set(p.name for p in (INNER/'commands').iterdir())=={p[0] for p in plan}, 'native_order', 'no extra commands')
    receipts,raws,summaries={}, {}, []
    previous_end=None; pids=[]
    for label,argv,cwd,inputs,timeout,exits in plan:
        receipt,spawn,raw=check_native(INNER,label,argv,cwd,inputs,timeout,exits,lock)
        demand(receipt==result['native_commands'][len(summaries)], 'result_native', label+' embedded actual receipt')
        demand(previous_end is None or previous_end<=receipt['attempted_epoch'], 'native_order', label+' timestamps')
        previous_end=receipt['ended_epoch']; pids.append(spawn['pid'])
        receipts[label]=receipt; raws[label]=raw
        summaries.append({'label':label,'pid':spawn['pid'],'attempted':receipt['attempted_epoch'],
                          'spawned':spawn['spawned_epoch'],'ended':receipt['ended_epoch'],
                          'exit':receipt['native_exit_code'],'direct_inputs':len(obj(INNER/'commands'/label/'INPUTS_BEFORE.json')),
                          'streams':receipt['streams']})
    demand(len(pids)==len(set(pids)), 'native_identity', 'distinct saved child PIDs')
    for key in config_keys:
        raw=raws['config_'+key]['stdout.raw'].decode().strip()
        demand(raw.replace(str(COLD),'{COMMAND_CWD}')==lock['queries'][key], 'effective_configuration', key)
    demand(obj(INNER/'EFFECTIVE_CONFIGURATION.json')=={
           k:raws['config_'+k]['stdout.raw'].decode().strip() for k in config_keys},
           'effective_configuration', 'complete actual query result map')
    for side in ('before','after'):
        cfg_raw=raws['optional_amsart_cfg_'+side]['stdout.raw'].decode().splitlines()
        demand(cfg_raw==lock['queries']['explicit_graph_seeds']['resolutions']['amsart.cfg'],
               'effective_configuration', 'optional class config '+side)
        raw=raws['ldd_'+side]['stdout.raw'].decode()
        demand('not found' not in raw, 'linkage', side+' no unresolved library')
        names=sorted(set(re.findall(r'(/[^\s():]+)',raw)))
        observed={str(archived_resolve(n)):coverage[str(archived_resolve(n))] for n in names}
        demand(observed==obj(INNER/('LINKAGE_'+side.upper()+'.json')) and
               all(coverage.get(p)==v for p,v in observed.items()), 'linkage', side+' exact complete raw-derived key')
    demand(obj(INNER/'LINKAGE_BEFORE.json')==obj(INNER/'LINKAGE_AFTER.json'), 'linkage', 'before/after')
    outer_receipt,outer_spawn,outer_raw=check_native(OUTER,'inner_builder',expected_python('inner'),ROOT,
                                                   list(originals),3600,[0],lock)
    demand(outer_result['native_builder']==outer_receipt and outer_result['inner_result_pin']==pin(INNER/'RESULT.json'),
           'product_association', 'outer embeds exact inner receipt/result')
    demand(outer_receipt['attempted_epoch']<=min(r['attempted_epoch'] for r in receipts.values()) and
           max(r['ended_epoch'] for r in receipts.values())<=outer_receipt['ended_epoch'],
           'product_association', 'all child intervals contained in actual builder interval')
    inner_expected={**result,'seal':{'payloads':DETAILS['manifests'][1]['payloads'],
                                    'manifest':DETAILS['manifests'][1]['manifest']}}
    demand(outer_raw['stdout.raw']==(json.dumps(inner_expected,sort_keys=True)+'\n').encode() and outer_raw['stderr.raw']==b'',
           'product_association', 'exact inner stdout bytes and settled separate stderr')

    controller_capture(binding, lock, outer_result, outer_receipt)
    demand(set(p.name for p in (OUTER/'commands').iterdir())=={'inner_builder'}, 'native_complete', 'single outer child')
    demand(not list(BUILD.rglob('UNCLOSED.json')) and
           len(list(BUILD.rglob('ATTEMPT.json')))==len(plan)+1==len(list(BUILD.rglob('RECEIPT.json'))),
           'native_complete', 'all attempts accounted, no unclosed state')
    DETAILS['native']={'inner_count':len(plan),'outer_count':1,'records':summaries,
                       'outer_pid':outer_spawn['pid'],'product_session':95844,
                       'new_native_children_launched_by_auditor':0}
    return result,receipts,raws


def controller_capture(binding, lock, outer_result, outer_receipt):
    env4={k:ENV8[k] for k in ('PATH','LANG','LC_ALL','TZ')}
    controller=QA/'p211_terminal_enable_preparation01/terminal_control.py'
    planpath=QA/'p211_terminal_enable_preparation01/INPUT_PLAN.json'
    plan=obj(planpath)
    capture_result=obj(CAPTURE/'RESULT.json'); enabled=obj(BINDDIR/'RESULT.json')
    demand(enabled['enabled_binding']=={'path':str(BINDPATH),'pin':EXPECTED_BINDING} and
           enabled['enabled_binding_created'] is True and enabled['new_builds']==0,
           'controller_enable','no earlier build; exact binding creation')
    for phase,base,expected_count in [('enable',BINDDIR,1625),('capture',CAPTURE,1646)]:
        result=obj(base/'RESULT.json')
        demand(result['phase']==phase and result['build_number']==1 and
               result['source']==pin(controller)==pin(base/'EXECUTED_CONTROLLER_SOURCE.py') and
               result['input_plan']==pin(planpath) and result['scope_counts']==plan['scope_counts'] and
               result['scope_originals_before_after_equal'] is True and result['read_paths']==expected_count and
               result['new_science']==result['new_page_views']==0 and
               all(result[k] is False for k in ('independent_review','build_acceptance','terminal_acceptance','paper_complete')),
               'controller_product',phase)
        authority=CONTROL/(phase.upper()+'_AUTHORITY.md'); EXPLICIT_LOCAL.add(authority)
        demand(pin(authority)==result['authority']==pin(base/'AUTHORITY.snapshot.md'),
               'controller_authority',phase+' actual pinned snapshot')
        original=obj(base/'ORIGINAL_INPUTS_BEFORE.json')
        demand(original==obj(base/'ORIGINAL_INPUTS_AFTER.json') and len(original)==expected_count,
               'controller_rich_closure',phase+' exact arbitrary-precision metadata equality')
        for path,v in plan['workspace_input_pins'].items():
            demand(path in original and {k:original[path][k] for k in ('bytes','sha256')}==v,
                   'controller_planned_key',phase+' '+path)
        oldkey=obj(QA/'p211_initial_build_independent_reception/run01/READ_INPUTS_BEFORE.json')
        mapping=obj(QA/'p211_initial_build_adoption01/HISTORICAL_MAPPING.json')
        substitution={v['logical_path']:v for v in mapping if v['logical_path'] in oldkey}
        demand(len(oldkey)==1299 and len(substitution)==2, 'controller_historical_key',phase+' exact metadata cardinalities')
        for logical,v in oldkey.items():
            physical=substitution[logical]['physical_original'] if logical in substitution else logical
            demand(physical in original and {k:original[physical][k] for k in ('bytes','sha256')}==v,
                   'controller_historical_key',phase+' complete saved 1299 association')
        saved=obj(base/'CONFIGURATION_BEFORE.json')
        demand(saved==obj(base/'CONFIGURATION_AFTER.json') and
               set(saved)=={'inherited840','historical843','current843','cwd_relative'} and
               saved['inherited840']==lock['entries'] and
               saved['historical843']==obj(QA/'p211_initial_build_01/inner/CONFIGURATION_BEFORE.json') and
               saved['cwd_relative']==binding['cwd_relative_configuration'] and
               saved['current843']=={**lock['entries'],**binding['cwd_relative_configuration']},
               'controller_config_archived',phase+' complete 840/843/future saved keys')
        runtime_rows=[]
        argv=['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix='+str(base/'unused_controller_cache'),
              str(controller),phase,'1',str(authority),str(result['authority']['bytes']),result['authority']['sha256']]
        coverage={row['resolved']:{k:row[k] for k in ('bytes','sha256')}
                  for row in lock['entries'].values() if row.get('kind')=='file'}
        coverage[str(controller)]=pin(controller)
        for edge in ('BEFORE','AFTER'):
            sample=obj(base/('CONTROLLER_RUNTIME_'+edge+'.json'))
            demand(sample['environment']==env4 and sample['argv']==argv and sample['cwd']==str(ROOT) and
                   sample['locale_ctype']=='C.UTF-8' and
                   sample['sys_path']==['/usr/lib/python310.zip','/usr/lib/python3.10','/usr/lib/python3.10/lib-dynload'] and
                   sample['pycache_prefix']==str(base/'unused_controller_cache'),
                   'controller_runtime_archived',phase+' '+edge+' exact parent settings')
            for field,value in [('isolated','1'),('no_site','1'),('no_user_site','1'),('ignore_environment','1'),
                                ('dont_write_bytecode','1'),('optimize','0')]:
                demand(re.search(r'(?:\(|, )'+field+'='+value+r'(?:,|\))',sample['flags']) is not None,
                       'controller_runtime_archived',phase+' '+edge+' '+field)
            demand(raw_pin(sample['maps_raw'].encode())==sample['maps_pin'],
                   'controller_runtime_archived',phase+' '+edge+' map raw bytes')
            mapped=set()
            for line in sample['maps_raw'].splitlines():
                cols=line.split(None,5)
                if len(cols)==6 and cols[5].startswith('/'):
                    demand(not cols[5].endswith(' (deleted)'), 'controller_runtime_archived','no deleted mapped path')
                    mapped.add(cols[5])
            demand(mapped==set(sample['mapped_files']), 'controller_runtime_archived',phase+' '+edge+' full map parse')
            for path,v in sample['mapped_files'].items():
                demand(coverage.get(str(archived_resolve(path)))==v,
                       'controller_runtime_archived',phase+' mapped '+path)
            for name,row in sample['modules'].items():
                path=row['path']; v={k:row[k] for k in ('bytes','sha256')}
                demand(Path(path).suffix not in ('.pyc','.pyo') and
                       row['resolved']==str(archived_resolve(path)) and coverage.get(row['resolved'])==v,
                       'controller_runtime_archived',phase+' module '+name)
            runtime_rows.append({'edge':edge,'modules':len(sample['modules']),'mapped_files':len(mapped),'maps_pin':sample['maps_pin']})
        DETAILS['controller_'+phase]={'rich_keys':len(original),'old_key_associations':len(oldkey),
            'historical_substitutions':len(substitution),'runtime_samples':runtime_rows,
            'host_keys_as_data_only':True,'arbitrary_precision_integer_metadata':True}
    comparator=ROOT/'docs/papers211_215_sequence/reviews/p211_a/inspect_build_reuse.py'
    reused=[comparator,QA/'p211_initial_build_independent_reception/run01/READ_INPUTS_BEFORE.json',
            QA/'p211_initial_build_01/inner/CONFIGURATION_BEFORE.json',
            QA/'p211_initial_build_adoption01/HISTORICAL_MAPPING.json']
    oldnative=obj(QA/'p211_b_final_root/BUILD_REUSE_NATIVE01.json')
    expected_reuse=oldnative['result']['output'].encode()
    demand(oldnative['result']['exit_code']==0 and raw_pin(expected_reuse)==
           {'bytes':6223,'sha256':'2623e94bc9b182dcde81750e88488a0012b32824ceb5a42a680217d885cdd217'},
           'controller_comparator','saved old exact output reference, not a fresh replay')
    all_rows=[]
    for base,labels in [(BINDDIR,['reuse_before']),(CAPTURE,['reuse_before','terminal_outer','reuse_after'])]:
        rows=obj(base/'RESULT.json')['native_commands']
        demand([row['label'] for row in rows]==labels, 'controller_native','complete phase order')
        previous_end=None
        for index,label in enumerate(labels):
            if label=='terminal_outer':
                argv=expected_python('outer'); inputs=[BINDPATH,LOCKPATH,*[PREP/n for n in CODE_NAMES]]
                env=ENV8; timeout=4500
            else:
                argv=['/usr/bin/python3.10','-I','-S','-B',str(comparator)]
                inputs=reused; env=env4; timeout=180
            receipt,spawn,raw=check_native(base,label,argv,ROOT,inputs,timeout,[0],lock,env,
                                           'p211-terminal-controller-native-attempt-v1',True)
            demand(receipt==rows[index] and (previous_end is None or previous_end<=receipt['attempted_epoch']),
                   'controller_native','exact embedded receipt and serial order '+label)
            previous_end=receipt['ended_epoch']
            if label=='terminal_outer':
                expected={**outer_result,'seal':{'payloads':362,'manifest':EXPECTED_MANIFEST}}
                demand(raw['stdout.raw']==(json.dumps(expected,sort_keys=True)+'\n').encode() and
                       raw['stderr.raw']==b'' and receipt['attempted_epoch']<=outer_receipt['attempted_epoch'] and
                       outer_receipt['ended_epoch']<=receipt['ended_epoch'],
                       'controller_outer','entire raw outer product and interval nesting')
            else:
                demand(raw['stdout.raw']==expected_reuse and raw['stderr.raw']==b'',
                       'controller_comparator','actual full comparator raw bytes '+str(base)+' '+label)
            all_rows.append({'phase':base.name,'label':label,'pid':spawn['pid'],'receipt':pin(base/label/'RECEIPT.json'),
                             'streams':receipt['streams']})
    demand(capture_result['new_builds']==1 and capture_result['enabled_binding_created'] is False and
           capture_result['cold_output']==str(BUILD) and capture_result['cold_build']=={
               'acceptance':False,'files':363,'native_commands':36,'pages':5,'payloads':362,
               'pdf':EXPECTED_PDF,'seal':EXPECTED_MANIFEST,'visual_review':'NOT_VIEWED'},
           'controller_capture','complete product association')
    tool=obj(ENTRY/'CONTROLLER_TOOL_NATIVE.json')
    demand(tool['request']==obj(ENTRY/'CONTROLLER_REQUEST.json') and
           tool['request']['workdir']==str(ROOT) and tool['request']['shell']=='/usr/bin/bash' and
           tool['request']['login'] is False and tool['results'][0]['session_id']==95844 and
           'exit_code' not in tool['results'][0] and tool['results'][0]['output']=='' and
           tool['results'][1]['exit_code']==0 and tool['results'][1]['output']=='' and
           len(tool['results'])==2 and len(tool['poll_requests'])==1 and
           tool['poll_requests'][0]['session_id']==95844,
           'controller_tool','real yielded session and final product return')
    authority=CONTROL/'CAPTURE_AUTHORITY.md'
    argv=['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix='+str(CAPTURE/'unused_controller_cache'),
          str(controller),'capture','1',str(authority),'5677',
          '36bbc32b6b099892a69e8ec38f5a44666225f090ed6cdb4ddb85ecb50f5e7691']
    command="set -o noclobber\nexec /usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC "
    command+=' '.join("'"+v+"'" for v in argv)
    command+=" < /dev/null > '"+str(ENTRY/'controller.stdout.raw')+"' 2> '"+str(ENTRY/'controller.stderr.raw')+"'"
    demand(tool['request']=={'cmd':command,'workdir':str(ROOT),'shell':'/usr/bin/bash','login':False,
           'yield_time_ms':1000,'max_output_tokens':5000},'controller_tool','entire literal product request')
    expected_output={key:capture_result[key] for key in
        ('status','phase','build_number','checks','read_paths','new_builds','new_science','new_page_views','terminal_acceptance')}
    expected_output.update(result={'path':str(CAPTURE/'RESULT.json'),'pin':pin(CAPTURE/'RESULT.json')},
        seal={'files':31,'payloads':30,'pin':pin(CAPTURE/'SHA256SUMS')})
    demand(read(ENTRY/'controller.stdout.raw')==(json.dumps(expected_output,sort_keys=True)+'\n').encode() and
           read(ENTRY/'controller.stderr.raw')==b'','controller_tool','complete redirected output bytes')
    DETAILS['controller_native']={'records':all_rows,'capture_product_session':95844,'new_replays_by_auditor':0}


def pass_archives(result,receipts,raws,sources,expected_config):
    demand([row['label'] for row in result['passes']]==list(PASS_NAMES), 'pass_order', 'exact three TeX/one BibTeX')
    previous=None; full_roles={}; warning_census={}
    for index,name in enumerate(PASS_NAMES):
        base=INNER/('pass_artifacts_'+name)
        snapshots={}
        for phase in ('before','after'):
            directory=base/phase; snap=obj(directory/'GENERATED.json'); snapshots[phase]=snap
            demand(set(snap)==GENERATED, 'pass_archive', name+' '+phase+' all eight generated roles')
            expected_files={'GENERATED.json'}
            for generated,value in snap.items():
                demand(type(value['present']) is bool and (set(value)=={'present','bytes','sha256'} if value['present']
                       else value=={'present':False}), 'pass_archive', name+' '+phase+' '+generated)
                if value['present'] and generated!='main.pdf':
                    expected_files.add(generated)
                    demand(pin(directory/generated)=={k:value[k] for k in ('bytes','sha256')},
                           'pass_archive', name+' '+phase+' immutable '+generated)
            demand(set(p.name for p in directory.iterdir())==expected_files, 'pass_archive', name+' '+phase+' exact copies')
        before,after=snapshots['before'],snapshots['after']
        if previous is None:
            demand(all(v=={'present':False} for v in before.values()), 'pass_source_only', 'no initial generated input')
        else:
            demand(previous==before, 'pass_chain', name+' before equals previous after')
        previous=after
        recorded=obj(base/'INPUT_OUTPUT_ROLES.json')
        demand(result['passes'][index]=={'label':name,'native':receipts[name],'generated_after':after,
               'roles':pin(base/'INPUT_OUTPUT_ROLES.json')}, 'pass_association', name)
        if name=='bibtex':
            aux=read(base/'before/main.aux').decode(); blg=read(base/'after/main.blg').decode()
            demand(re.findall(r'\\bibstyle\{([^}]+)\}',aux)==['amsplain'] and
                   re.findall(r'\\bibdata\{([^}]+)\}',aux)==['references'] and '\\@input{' not in aux,
                   'bibtex', 'actual before auxiliary graph')
            demand(re.findall(r'^The top-level auxiliary file:\s*(.+)$',blg,re.M)==['main.aux'] and
                   re.findall(r'^The style file:\s*(.+)$',blg,re.M)==['amsplain.bst'] and
                   re.findall(r'^Database file #[0-9]+:\s*(.+)$',blg,re.M)==['references.bib'],
                   'bibtex', 'actual BLG inputs')
            style_path='/usr/share/texlive/texmf-dist/bibtex/bst/amscls/amsplain.bst'
            expected={'mode':'BibTeX has no FLS; explicit aux/style/database plus native/config lock',
                      'inputs':[{'path':'main.aux','role':'GENERATED_BEFORE','pin':before['main.aux']},
                                {'path':'references.bib','role':'SOURCE','pin':sources['references.bib']},
                                {'path':style_path,'role':'EXTERNAL_PRELOCKED','pin':{k:expected_config[style_path][k] for k in ('bytes','sha256')}}],
                      'outputs':{n:after[n] for n in ('main.bbl','main.blg')},
                      'blg_pin':pin(base/'after/main.blg'),'non_FLS_trace':False}
            demand(recorded==expected, 'bibtex', 'complete independent roles reconstruction')
            for generated in GENERATED-{'main.bbl','main.blg'}:
                demand(before[generated]==after[generated], 'bibtex', 'unchanged nontarget '+generated)
            full_roles[name]=expected
        else:
            events=[]; emitted=set()
            for number,line in enumerate(read(base/'after/main.fls').decode().splitlines(),1):
                if line.startswith('PWD '):
                    demand(line=='PWD '+str(COLD), 'fls_event', name+' PWD')
                    event={'line':number,'kind':'PWD','raw':line}
                else:
                    parts=line.split(' ',1)
                    demand(len(parts)==2 and parts[0] in ('INPUT','OUTPUT'), 'fls_event', name+' syntax '+str(number))
                    kind,spelling=parts
                    path=Path(os.path.abspath(str(COLD/spelling) if not Path(spelling).is_absolute() else spelling))
                    resolved=archived_resolve(path)
                    event={'line':number,'kind':kind,'spelling':spelling,'absolute':str(path),'resolved':str(resolved)}
                    if path.is_relative_to(COLD):
                        demand(path==resolved and not path.is_symlink(), 'fls_event', name+' physical local')
                        local=path.relative_to(COLD).as_posix(); event['relative']=local
                        if kind=='OUTPUT':
                            demand(local in GENERATED and local not in sources, 'fls_event', name+' permitted output')
                            emitted.add(local); event.update(role='GENERATED_OUTPUT',after=after[local])
                        elif local in sources:
                            event.update(role='SOURCE',pin=sources[local])
                        elif local in GENERATED and local in emitted:
                            event.update(role='GENERATED_EARLIER_OUTPUT_SAME_PASS',read_time_bytes='NOT_OBSERVED_BY_FLS',
                                         pass_start=before[local],pass_end=after[local])
                        else:
                            demand(local in GENERATED and before[local]['present'], 'fls_event', name+' generated input provenance')
                            event.update(role='GENERATED_BEFORE',input_pin=before[local],pass_end=after[local])
                    else:
                        demand(kind=='INPUT' and str(path) in expected_config and expected_config[str(path)].get('kind')=='file',
                               'fls_event', name+' exact prelocked external spelling '+str(path))
                        external=expected_config[str(path)]
                        demand(str(resolved)==external['resolved'],
                               'fls_event', name+' archived external '+str(path))
                        event.update(role='EXTERNAL_PRELOCKED',pin={k:external[k] for k in ('bytes','sha256')})
                events.append(event)
            reconstructed={'events':events,'count':len(events),
                           'roles':{role:sum(e.get('role')==role for e in events) for role in ROLES},
                           'limitation':'FLS records ordered declared I/O, not exact mid-pass content or non-FLS OS reads.'}
            demand(recorded==reconstructed, 'fls_full_reconstruction', name+' every ordered event/field/duplicate')
            outputs={e.get('relative') for e in events if e['kind']=='OUTPUT'}
            demand({'main.pdf','main.log','main.fls','main.aux','main.out'}-{'main.fls'}<=outputs,
                   'fls_output_census', name+' expected declared outputs')
            stdout=raws[name]['stdout.raw'].decode()
            produced=re.findall(r'Output written on main\.pdf \((\d+) pages?, (\d+) bytes\)',stdout)
            demand(len(produced)==1 and int(produced[0][1])==after['main.pdf']['bytes'],
                   'pass_pdf_record', name+' actual TeX output size')
            log=read(base/'after/main.log').decode(errors='replace')
            warning_census[name]={key:len(re.findall(pattern,log,re.M|re.I)) for key,pattern in {
                'undefined_lines':r'^.*undefined.*$','warning_lines':r'^.*Warning.*$',
                'underfull_lines':r'^.*Underfull.*$','overfull_lines':r'^.*Overfull.*$',
                'rerun_lines':r'^.*(?:Rerun to|Please .*rerun|Label\(s\) may have changed).*$'}.items()}
            full_roles[name]=reconstructed
    for name,value in previous.items():
        p=COLD/name
        demand(value==({'present':True,**pin(p)} if p.is_file() else {'present':False}),
               'pass_chain', 'last pass versus current '+name)
        if value['present'] and name!='main.pdf':
            demand(read(INNER/'pass_artifacts_pass3/after'/name)==read(p), 'pass_chain', 'last copy raw '+name)
    put('INDEPENDENT_ORDERED_IO_RECONSTRUCTION.json',full_roles)
    DETAILS['pass_roles']={name:({'events':r['count'],'roles':r['roles']} if name!='bibtex' else
                                {'input_roles':[x['role'] for x in r['inputs']],'outputs':list(r['outputs'])})
                           for name,r in full_roles.items()}
    DETAILS['per_pass_diagnostics']=warning_census
    DETAILS['pass_limit']='Intermediate PDF pins are recorded, not archived intermediate PDF bytes; same-pass input bytes are not observed.'

def measurements(result,raws):
    measured=obj(INNER/'MEASURED_NOT_VIEWED.json')
    demand(measured==result['measurements'], 'measurement', 'exact result/measured association')
    demand(pin(COLD/'main.pdf')==EXPECTED_PDF==measured['pdf'] and read(COLD/'main.pdf').startswith(b'%PDF-1.5'),
           'measurement', 'exact final PDF')
    info=raws['pdfinfo']['stdout.raw'].decode()
    pairs={k.strip():v.strip() for k,v in (line.split(':',1) for line in info.splitlines() if ':' in line)}
    demand(pairs['Pages']=='5' and pairs['File size']=='301007 bytes' and pairs['Author']=='' and
           pairs['Page size']=='595.276 x 841.89 pts (A4)' and pairs['Encrypted']=='no',
           'measurement', 'actual metadata')
    font_lines=raws['pdffonts']['stdout.raw'].decode().splitlines()
    demand(font_lines[0].split()[-5:]==['emb','sub','uni','object','ID'], 'measurement', 'font column meanings')
    fonts=[line.split() for line in font_lines[2:] if line.strip()]
    demand(len(fonts)==21==measured['embedded_fonts'] and all(len(v)>=8 and v[-5]=='yes' for v in fonts),
           'measurement', 'all 21 actual embedded fonts')
    text=read(INNER/'main.txt').decode(); pages=text.split('\f')
    if not pages[-1].strip(): pages.pop()
    demand(len(pages)==5==measured['pages'], 'measurement', 'text/PDF page census')
    markers=[s for s in ('[VERIFY]','??','[?]') if s in text]
    references=[i+1 for i,p in enumerate(pages) if re.search(r'^\s*(References|Bibliography)\s*$',p,re.M)]
    log=read(COLD/'main.log').decode(errors='replace')
    patterns={'undefined':r'^.*undefined.*$','overfull':r'^.*Overfull.*$','underfull':r'^.*Underfull.*$',
              'warnings':r'^.*Warning.*$','missing_characters':r'^.*Missing character.*$',
              'rerun':r'^.*(?:Rerun to|Please .*rerun|Label\(s\) may have changed).*$'}
    diagnostics={key:re.findall(pattern,log,re.M) for key,pattern in patterns.items()}
    blg=re.findall(r'(?im)^.*(?:Warning--|I couldn.t open|error message).*$',read(COLD/'main.blg').decode())
    demand(diagnostics==measured['diagnostics'] and markers==measured['text_markers']==[] and
           blg==measured['bibtex_findings']==[] and references==measured['reference_heading_pages']==[5],
           'measurement', 'exact reproduction of saved case-sensitive derivation; NOT full warning census')

    corrected={key:re.findall(pattern,log,re.M|re.I) for key,pattern in patterns.items()}
    demand(corrected['undefined']==corrected['overfull']==corrected['missing_characters']==corrected['rerun']==[],
           'diagnostic_reconstruction', 'actual final absence categories')
    demand(corrected['underfull']==diagnostics['underfull'] and len(corrected['underfull'])==2,
           'diagnostic_reconstruction', 'two underfull entries')
    missed=[line for line in corrected['warnings'] if line not in diagnostics['warnings']]
    demand(len(missed)==1 and missed[0].startswith('pdfTeX warning (font expansion):'),
           'diagnostic_reconstruction', 'exact current lower-case warning finding')
    FINDINGS.append({'id':'P211-COLD1-IO-D1','status':'OPEN_PENDING_ROOT_DIAGNOSTIC_DISPOSITION',
        'category':'incomplete_case_sensitive_diagnostic_census','severity':'Minor',
        'missed_final_warning_lines':missed,'warning_free_claim':False,
        'glyph_loss_or_benignness_inferred':False,
        'required_action':'Root supplemental diagnostic census and explicit disposition; no submitted edits authorized.'})
    DETAILS['corrected_final_diagnostics']=corrected
    demand(measured['visual_review']=='NOT_VIEWED' and measured['venue_page_limit'] is None and
           measured['size_threshold_100KB']=='NOT_AN_ACCEPTANCE_RULE', 'measurement_scope', 'no invented acceptance threshold/view')
    expected_images={'page-%04d.png'%n for n in range(1,6)}
    demand(set(p.name for p in (INNER/'pages').iterdir())==expected_images and len(measured['renders'])==5,
           'render_census', 'exact five files/rows')
    rows=[]
    for number,row in enumerate(measured['renders'],1):
        image=INNER/'pages'/('page-%04d.png'%number); raw=read(image)
        demand(row=={'page':number,'image':str(image),'pin':raw_pin(raw),'visual_review':'NOT_VIEWED'},
               'render_census', 'exact measured row '+str(number))
        demand(raw[:8]==b'\x89PNG\r\n\x1a\n' and raw[12:16]==b'IHDR', 'render_census', 'PNG signature '+str(number))
        width,height=struct.unpack('>II',raw[16:24])
        demand(width>0 and height>0, 'render_census', 'dimensions; no page view '+str(number))
        rows.append({'page':number,'pin':raw_pin(raw),'pixel_dimensions':[width,height],'auditor_visual_review':False})
    DETAILS['measurements']={'pdf':EXPECTED_PDF,'pages':5,'embedded_fonts':21,'diagnostics':diagnostics,
                             'text_markers':markers,'bibtex_findings':blg,'reference_heading_pages':references,
                             'render_census':rows,'auditor_visual_review':False,'root_visual_gate':'SEPARATE_PENDING_ROOT'}


def main():
    global OUTPUT
    demand(Path(__file__).resolve()==HERE/'inspect_cold1.py' and Path.cwd()==ROOT,
           'auditor_scope','physical checker and workspace cwd')
    demand(len(sys.argv)==2 and re.fullmatch(r'run[0-9]+',sys.argv[1]) is not None,
           'auditor_scope','new run label')
    OUTPUT=HERE/sys.argv[1]
    demand(not os.path.lexists(OUTPUT),'auditor_scope','never overwrite or resume a run')
    OUTPUT.mkdir(mode=0o700)
    started=time.time(); source=read(HERE/'inspect_cold1.py')
    put('executed_checker.py',source)
    put('ENTRY.json',{'argv':sys.orig_argv,'cwd':str(Path.cwd()),'environment':dict(os.environ),
        'flags':str(sys.flags),'source':raw_pin(source),'started_epoch':started,
        'original_independent_auditor':pin(HERE/'original_inspect_build.py'),
        'submitted_code_executions':0,'scientific_executions':0,'new_builds':0,
        'fresh_host_queries':0,'own_visual_review':False})
    failure=None
    try:
        DETAILS['manifests']=[manifest(BUILD,EXPECTED_MANIFEST,362),manifest(INNER),
            manifest(BINDDIR,{'bytes':1642,'sha256':'47d76e394e8948b4557397b1c1a2080c9d2762d7f61dea374a333ee1714d7e2d'},18),
            manifest(CAPTURE,{'bytes':2785,'sha256':'0c3d748b923cdae9c9e8b3b3762772f4d36f84cee0f01ea6b565eb5931732a29'},30),
            manifest(ENTRY,count=14)]
        binding,lock=source_and_binding()
        specs,expected,originals,coverage=configuration(binding,lock)
        result,receipts,raws=commands_and_envelopes(binding,lock,originals,coverage)
        pass_archives(result,receipts,raws,binding['source_pins'],expected)
        measurements(result,raws)
    except BaseException:
        failure=traceback.format_exc()
    before=dict(READS); after={}
    for path,value in before.items():
        try:
            current=raw_pin(read(path)); after[path]=current
            demand(current==value,'final_input_closure',path)
        except BaseException:
            failure=(failure or '')+traceback.format_exc()
    put('READ_INPUTS_BEFORE.json',before); put('READ_INPUTS_AFTER.json',after)
    put('ARCHIVED_ONLY_REFERENTS.json',{'paths':sorted(ARCHIVED_ONLY_REFERENTS),
        'no_host_files_opened':True,'no_host_metadata_dereference':True,
        'limitation':'Recorded old host/metadata keys checked for consistency, not freshly recaptured; no OS-hermetic claim.'})
    put('DETAILS.json',DETAILS); put('FINDINGS.json',FINDINGS)
    result={'status':'FAIL_PRESERVED' if failure else 'COLD1_DOCUMENTARY_CHECKS_COMPLETE_WITH_OPEN_DIAGNOSTIC_FINDING',
        'failure':failure,'checks':sum(COUNTS.values()),'check_groups':dict(COUNTS),
        'read_paths':len(before),'read_bytes':sum(v['bytes'] for v in before.values()),
        'inputs_equal':before==after,'auditor_source':raw_pin(source),'elapsed_seconds':time.time()-started,
        'submitted_code_executions':0,'new_builds':0,'new_renderings':0,'scientific_executions':0,
        'fresh_host_queries':0,'old_1299_referents_replayed':False,'canonical_body_read':False,
        'manuscript_reviews':0,'auditor_visual_review':False,'open_findings':len(FINDINGS),
        'warning_free_claim':False,'build_acceptance':False,'terminal_acceptance':False,
        'external':'OWNER_AMBER / HOLD_EXTERNAL'}
    put('RESULT.json',result)
    payloads=regular_members(OUTPUT)
    put('SHA256SUMS',''.join(raw_pin(p.read_bytes())['sha256']+'  '+name+'\n'
                           for name,p in payloads.items()).encode())
    print(json.dumps({**result,'run':str(OUTPUT),'seal':{'payloads':len(payloads),
          'manifest':raw_pin((OUTPUT/'SHA256SUMS').read_bytes())}},sort_keys=True))
    return 1 if failure else 0


if __name__=='__main__':
    raise SystemExit(main())
