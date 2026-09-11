#!/usr/bin/python3.10
"""Independent saved-build auditor; never imports or executes submitted code.

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
HERE = QA / 'p211_initial_build_independent_reception'
BUILD = QA / 'p211_initial_build_01'
INNER = BUILD / 'inner'
OUTER = BUILD / 'outer'
COLD = INNER / 'source_only'
BINDDIR = QA / 'p211_initial_build_binding01'
PREP = QA / 'p211_build_revision01'
PAPER = ROOT / 'papers/211-kernel-image-projection-feedback'
BINDPATH = BINDDIR / 'BINDING.json'
LOCKPATH = BINDDIR / 'ROOT_DERIVED_SOURCE_LOCK.json'
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
EXPECTED_MANIFEST = {'bytes': 39346, 'sha256': '7904f81845aa802f8ba2ebf15698655cae97471e94bfe5f49fa510d66833bbec'}
EXPECTED_BINDING = {'bytes': 4596, 'sha256': '2ee260311f7cb686d1dbddb9d96697e74b88f5373f8c53cbd4cff2350d43e4c0'}
EXPECTED_LOCK = {'bytes': 570037, 'sha256': '1a879caa4d7bb68fd841e381f37d5ec3e31236ccd6c7b677dbd95492a92bbf87'}
EXPECTED_PDF = {'bytes': 301007, 'sha256': '532b8c462e907878c3d75829b2c4ff86de7d59c137efa91b61ebc80717a077dc'}
DENIED = {PAPER / n for n in ('CANONICAL.json', 'verify.py', 'PROOF_PACKAGE.md')}
READS, COUNTS, DETAILS = {}, collections.Counter(), {}
OUTPUT = None


def demand(test, group, detail):
    COUNTS[group] += 1
    if not test:
        raise AssertionError(group + ': ' + str(detail))


def raw_pin(raw):
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def read(path):
    p = Path(path)
    demand(p.is_absolute() and p not in DENIED and p.resolve() not in DENIED,
           'read_scope', str(p))
    raw = p.read_bytes()
    value = raw_pin(raw)
    demand(str(p) not in READS or READS[str(p)] == value, 'read_consistency', str(p))
    READS[str(p)] = value
    return raw


def pin(path):
    return raw_pin(read(path))


def obj(path):
    return json.loads(read(path))


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
    p = Path(path)
    result = {'path': str(p), 'present': os.path.lexists(p),
              'symlink': p.is_symlink(), 'resolved': str(p.resolve())}
    if p.is_symlink():
        result['link'] = os.readlink(p)
    if result['present']:
        mode = p.stat().st_mode
        if stat.S_ISREG(mode):
            result.update(kind='file', **pin(p))
        elif stat.S_ISDIR(mode):
            result['kind'] = 'directory'
            if members:
                result['members'] = sorted(child.name for child in p.iterdir())
        elif stat.S_ISCHR(mode):
            dev = p.stat().st_rdev
            result.update(kind='character_device', major=os.major(dev), minor=os.minor(dev))
        else:
            result.update(kind='other', mode=stat.S_IFMT(mode))
    return result


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
    demand(pin(BINDPATH) == EXPECTED_BINDING, 'binding', 'root-supplied identity')
    demand(pin(LOCKPATH) == EXPECTED_LOCK, 'binding', 'root-derived lock identity')
    binding, lock = obj(BINDPATH), obj(LOCKPATH)
    demand(binding['schema'] == 'p211-initial-source-only-root-binding-v1' and
           binding['status'] == 'ROOT_AUTHORIZED_INITIAL_SOURCE_ONLY_BUILD' and
           binding['scope'] == 'ONE_INITIAL_BUILD_ONLY' and binding['output'] == str(BUILD),
           'binding', 'literal schema/status/scope/output')
    demand(binding['environment'] == lock['environment'] == ENV8, 'binding', 'ENV8')
    demand(all(binding[k] is False for k in ('scientific_execution', 'manuscript_review', 'terminal_acceptance')),
           'binding', 'separate gates')
    demand(binding['dependency_lock'] == {'path': str(LOCKPATH), 'pin': EXPECTED_LOCK},
           'binding', 'exact dependency association')
    receipt = binding['root_read_receipt']
    demand(receipt['path'] == str(QA / 'p211_build_root_reception/RECEPTION.md') and
           pin(receipt['path']) == receipt['pin'], 'binding', 'exact root-read receipt')
    demand(set(binding['adapter_pins']) == set(CODE_NAMES) and
           binding['adapter_pins'] == lock['code_observations'], 'binding', 'five-code lock')
    for name in CODE_NAMES:
        demand(pin(PREP / name) == pin(OUTER / 'executed_adapter' / name) == binding['adapter_pins'][name],
               'code_snapshot', name)
    sources = binding['source_pins']
    demand(set(sources) == set(SOURCE_NAMES) and sources == lock['source_observations'],
           'source', 'exact nine roles')
    for name in SOURCE_NAMES:
        for base in (PAPER, COLD):
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
    baseline_path = PREP / 'discovery01/DEPENDENCY_LOCK.candidate.json'
    baseline = obj(baseline_path)
    demand(pin(baseline_path) == {'bytes':570037,'sha256':'bb89d966250b0552a47784a5c4aa0d2aaf5b36bc9057fc177a5e552b9bf042ec'},
           'source_delta', 'accepted original candidate')
    demand(set(baseline) == set(lock) and all(baseline[k] == lock[k] for k in lock if k != 'source_observations'),
           'source_delta', 'all nonsource lock fields unchanged')
    changed = [n for n in SOURCE_NAMES if baseline['source_observations'][n] != sources[n]]
    demand(changed == ['sections/5_scope.tex'], 'source_delta', changed)
    delta = obj(BINDDIR / 'SOURCE_LOCK_DELTA.json')
    demand(delta['baseline_candidate'] == {'path': str(baseline_path), 'pin': pin(baseline_path)} and
           delta['derived_lock'] == binding['dependency_lock'] and delta['before'] == baseline['source_observations'][changed[0]] and
           delta['after'] == sources[changed[0]], 'source_delta', 'exact delta associations')
    oldpath = QA / 'p211_author_execution_documentation01/originals/sections/5_scope.tex'
    old, new = read(oldpath).decode(), read(PAPER / changed[0]).decode()
    demand(pin(oldpath) == delta['before'], 'source_delta', 'physical original')
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
    demand(old.count(old_paragraph) == old.count('is designed to enumerate') == 1 and
           old.replace('is designed to enumerate','enumerates').replace(old_paragraph,new_paragraph) == new,
           'source_delta', 'only two exact execution-prose replacements')
    demand(re.findall(r'\\[A-Za-z]+',old) == re.findall(r'\\[A-Za-z]+',new), 'source_delta', 'macro sequence unchanged')
    native_diff = obj(BINDDIR / 'SOURCE_DIFF_NATIVE.json')
    raw_diff, stderr = read(BINDDIR / 'SOURCE_DIFF_STDOUT.raw'), read(BINDDIR / 'SOURCE_DIFF_STDERR.raw')
    demand(native_diff['argv'] == ['/usr/bin/diff','-u',str(oldpath),str(PAPER / changed[0])] and
           native_diff['native_exit_code'] == 1 and native_diff['stdout'] == raw_pin(raw_diff) and
           native_diff['stderr'] == raw_pin(stderr) and stderr == b'', 'source_delta', 'saved real diff association')
    diff_lines = raw_diff.decode().splitlines(keepends=True)
    expected_diff = list(difflib.unified_diff(old.splitlines(keepends=True),new.splitlines(keepends=True)))
    demand(diff_lines[2:] == expected_diff[2:] and diff_lines[0].startswith('--- '+str(oldpath)+'\t') and
           diff_lines[1].startswith('+++ '+str(PAPER / changed[0])+'\t'), 'source_delta', 'entire raw diff body')
    binding_result = obj(BINDDIR / 'RESULT.json')
    native_binding = obj(BINDDIR / 'BINDING_NATIVE01.json')
    demand(native_binding['exit_code'] == 0 and json.loads(native_binding['output']) == binding_result,
           'binding', 'actual binding creation return')
    demand(binding_result['binding'] == {'path':str(BINDPATH),'pin':EXPECTED_BINDING} and
           binding_result['source_lock_pin'] == EXPECTED_LOCK and binding_result['output_absent'] is True,
           'binding', 'binding creation result')
    # This metadata contains a root canonical/verify hash. Do not follow those bodies.
    binding_inputs = obj(BINDDIR / 'INPUTS_AT_BINDING.json')
    demand(str(PAPER/'CANONICAL.json') in binding_inputs, 'scope_metadata', 'root canonical pin is metadata only')
    for name in CODE_NAMES:
        demand(binding_inputs[str(PREP/name)] == binding['adapter_pins'][name], 'binding', 'creation code pin '+name)
    for name in SOURCE_NAMES:
        demand(binding_inputs[str(PAPER/name)] == sources[name], 'binding', 'creation source pin '+name)
    DETAILS['source_delta'] = {'changed_names':changed,'literal_replacements':2,'new_dependency_discovery':False,
                               'canonical_body_read':False,'science_review':False}
    return binding, lock


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
    actual = {p:current_entry(p,v['members']) for p,v in sorted(specs.items())}
    demand(actual == expected and len(actual) == 843, 'configuration', 'fresh complete recapture')
    put('CONFIGURATION_CURRENT_BEFORE.json', actual)
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
                 binding['root_read_receipt']['path']:binding['root_read_receipt']['pin']}
    originals.update({str(PREP/n):binding['adapter_pins'][n] for n in CODE_NAMES})
    originals.update({str(PAPER/n):binding['source_pins'][n] for n in SOURCE_NAMES})
    for base in (INNER,OUTER):
        demand(obj(base/'ORIGINALS_BEFORE.json') == obj(base/'ORIGINALS_AFTER.json') == originals,
               'original_closure', str(base))
    for p,v in originals.items():
        demand(pin(p) == v, 'original_closure', p)
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
                mapped.add(str(Path(cols[5]).resolve()))
        demand(mapped==set(sample['mapped_files']), 'runtime', label+' complete raw-map parse')
        for p,v in sample['mapped_files'].items():
            demand(known.get(p)==v and pin(p)==v, 'runtime', label+' mapped '+p)
        for name,row in sample['modules'].items():
            p=row['path']; v={k:row[k] for k in ('bytes','sha256')}
            demand(Path(p).suffix not in ('.pyc','.pyo') and known.get(p)==v and pin(p)==v,
                   'runtime', label+' module '+name)
        runtime_rows.append({'sample':label,'modules':len(sample['modules']),'mapped_files':len(mapped),
                             'maps_pin':sample['maps_pin']})
    DETAILS['parent_runtime'] = runtime_rows
    DETAILS['configuration'] = {'spellings':843,'base_spellings':840,'future_absence':3,
                                 'file_entries':sum(v.get('kind')=='file' for v in actual.values()),
                                 'membership_entries':sum('members' in v for v in actual.values())}
    return specs,expected,originals,coverage


def check_native(base,label,expected_argv,expected_cwd,extra_inputs,timeout,expected_exits,lock):
    directory=base/'commands'/label
    demand(set(p.name for p in directory.iterdir())=={'ATTEMPT.json','SPAWNED.json','RECEIPT.json',
           'INPUTS_BEFORE.json','INPUTS_AFTER.json','stdout.raw','stderr.raw'}, 'native_complete', label)
    attempt,spawn,receipt=(obj(directory/name) for name in ('ATTEMPT.json','SPAWNED.json','RECEIPT.json'))
    demand(all(receipt.get(k)==v for k,v in attempt.items()), 'native_fields', label+' exact attempt')
    demand(attempt['argv']==expected_argv and attempt['cwd']==str(expected_cwd) and attempt['environment']==ENV8,
           'native_fields', label+' literal argv/cwd/ENV8')
    demand(attempt['schema']=='p211-native-attempt-v1' and attempt['label']==label and
           attempt['timeout_seconds']==timeout and attempt['expected_exit_codes']==expected_exits and
           attempt['requested_new_session'] is True and attempt['stdin']=={'path':'/dev/null','policy':'DEVNULL'},
           'native_fields', label+' complete request')
    demand(spawn['pid']==spawn['session'] and type(spawn['pid']) is int and spawn['pid']>0 and
           attempt['attempted_epoch']<=spawn['spawned_epoch']<=receipt['ended_epoch'], 'native_identity', label)
    demand(receipt['native_handle_received'] is True and receipt['launch_outcome']=='KNOWN_NATIVE_HANDLE' and
           receipt['native_exit_code'] in expected_exits and receipt['wrapper_reason']=='NATIVE_EXIT' and
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
            demand(current_entry(p)==v, 'native_inputs', label+' current '+p)
        if p in lock['entries']:
            demand(v==lock['entries'][p], 'native_inputs', label+' prelocked '+p)
    raw={name:read(directory/name) for name in ('stdout.raw','stderr.raw')}
    demand(set(receipt['streams'])==set(raw) and
           all(receipt['streams'][n]==raw_pin(v) for n,v in raw.items()), 'native_raw', label)
    return receipt,spawn,raw


def commands_and_envelopes(binding,lock,originals,coverage):
    result=obj(INNER/'RESULT.json'); outer_result=obj(OUTER/'RESULT.json')
    demand(result['status']=='INITIAL_BUILD_RECORDED_NOT_VIEWED_NOT_ACCEPTED' and result['failures']==[] and
           outer_result['status']=='INITIAL_BUILD_CAPTURED_PENDING_ROOT_INSPECTION' and outer_result['failures']==[],
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
        observed={str(Path(n).resolve()):pin(Path(n).resolve()) for n in names}
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
    tool=obj(BINDDIR/'BUILD_TOOL_INVOCATION.json')
    expected_cmd='/usr/bin/env -i '+' '.join(k+'='+v for k,v in ENV8.items())+' '+' '.join(expected_python('outer'))
    demand(tool['request']=={'cmd':expected_cmd,'workdir':str(ROOT),'yield_time_ms':1000,'max_output_tokens':12000},
           'product_tool', 'exact literal outer launch')
    demand(tool['launch']['session_id']==31539 and tool['launch']['output']=='' and
           'exit_code' not in tool['launch'] and tool['completion']['exit_code']==0,
           'product_tool', 'yielded launch and real completion')
    outer_expected={**outer_result,'seal':{'payloads':362,'manifest':EXPECTED_MANIFEST}}
    demand(tool['completion']['output']==json.dumps(outer_expected,sort_keys=True)+'\n',
           'product_tool', 'exact full final product output')
    demand(set(p.name for p in (OUTER/'commands').iterdir())=={'inner_builder'}, 'native_complete', 'single outer child')
    demand(not list(BUILD.rglob('UNCLOSED.json')) and
           len(list(BUILD.rglob('ATTEMPT.json')))==len(plan)+1==len(list(BUILD.rglob('RECEIPT.json'))),
           'native_complete', 'all attempts accounted, no unclosed state')
    DETAILS['native']={'inner_count':len(plan),'outer_count':1,'records':summaries,
                       'outer_pid':outer_spawn['pid'],'product_session':31539,
                       'new_native_children_launched_by_auditor':0}
    return result,receipts,raws


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
                                {'path':style_path,'role':'EXTERNAL_PRELOCKED','pin':pin(style_path)}],
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
                    resolved=path.resolve()
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
                        demand(str(resolved)==external['resolved'] and pin(path)=={k:external[k] for k in ('bytes','sha256')},
                               'fls_event', name+' current external '+str(path))
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
            warning_census[name]={key:len(re.findall(pattern,log,re.M)) for key,pattern in {
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
           'measurement', 'full independent final diagnostic derivation')
    demand(diagnostics['underfull']==['Underfull \\hbox (badness 1325) in paragraph at lines 65--65',
                                     'Underfull \\hbox (badness 10000) in paragraph at lines 16--19'] and
           all(not value for key,value in diagnostics.items() if key!='underfull'),
           'measurement', 'only two disclosed final underfull diagnostics')
    demand(measured['visual_review']=='NOT_VIEWED' and measured['venue_page_limit'] is None and
           measured['size_threshold_100KB']=='NOT_AN_ACCEPTANCE_RULE', 'measurement_scope', 'no invented acceptance threshold/view')
    expected_images={'page-%04d.png'%n for n in range(1,6)}
    demand(set(p.name for p in (INNER/'pages').iterdir())==expected_images and len(measured['renders'])==5,
           'render_census', 'exact five files/rows')
    rows=[]
    visual=read(QA/'p211_initial_build_root_reception/VISUAL_RECEPTION.md').decode()
    demand(EXPECTED_PDF['sha256'] in visual, 'root_visual_attribution', 'receipt names same PDF only')
    for number,row in enumerate(measured['renders'],1):
        image=INNER/'pages'/('page-%04d.png'%number); raw=read(image)
        demand(row=={'page':number,'image':str(image),'pin':raw_pin(raw),'visual_review':'NOT_VIEWED'},
               'render_census', 'exact measured row '+str(number))
        demand(raw[:8]==b'\x89PNG\r\n\x1a\n' and raw[12:16]==b'IHDR', 'render_census', 'PNG signature '+str(number))
        width,height=struct.unpack('>II',raw[16:24])
        demand(width>0 and height>0 and row['pin']['sha256'] in visual, 'render_census', 'dimensions/root receipt pin '+str(number))
        rows.append({'page':number,'pin':raw_pin(raw),'pixel_dimensions':[width,height],'auditor_visual_review':False})
    DETAILS['measurements']={'pdf':EXPECTED_PDF,'pages':5,'embedded_fonts':21,'diagnostics':diagnostics,
                             'text_markers':markers,'bibtex_findings':blg,'reference_heading_pages':references,
                             'render_census':rows,'auditor_visual_review':False,'root_visual_receipt_pinned_only':True}


def main():
    global OUTPUT
    demand(Path(__file__).resolve()==HERE/'inspect_build.py' and Path.cwd()==ROOT, 'auditor_scope', 'physical checker/cwd')
    demand(len(sys.argv)==2 and re.fullmatch(r'run[0-9]+',sys.argv[1]) is not None, 'auditor_scope', 'new run label')
    OUTPUT=HERE/sys.argv[1]
    demand(not os.path.lexists(OUTPUT), 'auditor_scope', 'never resume or overwrite run')
    OUTPUT.mkdir(mode=0o700)
    started=time.time()
    source=read(HERE/'inspect_build.py')
    put('executed_checker.py',source)
    put('ENTRY.json',{'argv':sys.orig_argv,'cwd':str(Path.cwd()),'environment':dict(os.environ),
                      'flags':str(sys.flags),'source':raw_pin(source),'started_epoch':started,
                      'submitted_code_executions':0,'scientific_executions':0,'new_builds':0,'own_visual_review':False})
    specs=expected=None; failure=None
    try:
        for path in (HERE/'SCOPE.md',ROOT/'.agents/skills/symbolic-dynamics-research/SKILL.md',
                     Path('/root/autodl-tmp/.codex/skills/paper-compile/SKILL.md'),ROOT/'docs/research_state/WORKFLOW.md',
                     ROOT/'SYMBOLIC_DYNAMICS_STATE.md',ROOT/'docs/papers211_215_sequence/PIPELINE_STATE.md',
                     ROOT/'docs/papers211_215_sequence/PROBLEM_ANCHOR.md',ROOT/'docs/papers204_208_sequence/ARTIFACT_CONTRACT.md',
                     QA/'p211_build_preparation/README.md',PREP/'README.md',QA/'p211_build_independent_audit/REPORT.md',
                     QA/'p211_build_independent_delta01/REPORT.md',QA/'p211_build_root_reception/RECEPTION.md',
                     BINDDIR/'prepare_binding.py'):
            read(path)
        DETAILS['manifests']=[manifest(BUILD,EXPECTED_MANIFEST,362),manifest(INNER),
                               manifest(QA/'p211_build_independent_delta01',count=49),
                               manifest(QA/'p211_build_independent_audit',count=50)]
        binding,lock=source_and_binding()
        specs,expected,originals,coverage=configuration(binding,lock)
        result,receipts,raws=commands_and_envelopes(binding,lock,originals,coverage)
        pass_archives(result,receipts,raws,binding['source_pins'],expected)
        measurements(result,raws)
        after={p:current_entry(p,v['members']) for p,v in sorted(specs.items())}
        put('CONFIGURATION_CURRENT_AFTER.json',after)
        demand(after==expected, 'configuration', 'fresh final recapture unchanged')
    except BaseException:
        failure=traceback.format_exc()
    # Close every actually read file, including whole raw streams. No external
    # metadata-only reference (notably canonical) is silently followed here.
    before=dict(READS)
    after_reads={}
    for path,value in before.items():
        try:
            current=raw_pin(Path(path).read_bytes())
            after_reads[path]=current
            demand(current==value, 'final_input_closure', path)
        except BaseException:
            failure=(failure or '')+traceback.format_exc()
    put('READ_INPUTS_BEFORE.json',before)
    put('READ_INPUTS_AFTER.json',after_reads)
    put('DETAILS.json',DETAILS)
    result={'status':'FAIL_PRESERVED' if failure else 'INDEPENDENT_INITIAL_BUILD_EVIDENCE_PASS_PENDING_ROOT_RECEPTION',
            'failure':failure,'checks':sum(COUNTS.values()),'check_groups':dict(COUNTS),
            'read_paths':len(before),'read_bytes':sum(v['bytes'] for v in before.values()),
            'inputs_equal':before==after_reads,'auditor_source':raw_pin(source),'elapsed_seconds':time.time()-started,
            'submitted_code_executions':0,'new_builds':0,'new_renderings':0,'scientific_executions':0,
            'canonical_body_read':False,'manuscript_reviews':0,'auditor_visual_review':False,
            'terminal_acceptance':False,'external':'OWNER_AMBER / HOLD_EXTERNAL'}
    put('RESULT.json',result)
    payloads=regular_members(OUTPUT)
    put('SHA256SUMS',''.join(raw_pin(p.read_bytes())['sha256']+'  '+name+'\n' for name,p in payloads.items()).encode())
    print(json.dumps({**result,'run':str(OUTPUT),'seal':{'payloads':len(payloads),'manifest':raw_pin((OUTPUT/'SHA256SUMS').read_bytes())}},sort_keys=True))
    return 1 if failure else 0


if __name__=='__main__':
    raise SystemExit(main())

