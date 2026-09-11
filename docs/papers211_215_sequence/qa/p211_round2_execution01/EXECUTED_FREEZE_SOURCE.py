#!/usr/bin/python3.10
"""P211 physical Round2 preparation source. Requires a future separate root binding.

Disclosed adaptation of accepted Round1 recorder helpers, not a science
producer, manuscript review, build launcher or self-certifying infrastructure.
All original Round1 payload and complete final-B bytes are copied unchanged.
No execution, import, static test or physical freeze occurred in preparation.
"""
from hashlib import sha256
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
import time
import traceback
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
PAPER = ROOT/'papers/211-kernel-image-projection-feedback'
ROUND0, ROUND1, FROZEN = (PAPER/'frozen_round0', PAPER/'frozen_round1', PAPER/'frozen_round2')
B_ROOT = ROOT/'docs/papers211_215_sequence/reviews/p211_b'
PREPARATION = QA/'p211_round2_preparation01'
EXECUTION = QA/'p211_round2_execution01'
HERE = Path(__file__).absolute().parent
BASE_SOURCE = QA/'p211_round1_adapter02/freeze.py'
ENV = {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
TOOLS = ('/usr/bin/cp','/usr/bin/cmp','/usr/bin/sha256sum','/usr/bin/python3.10')
B_REVIEWER = '/root/round211_rational_scout/relation_primary_sources'
ACCEPTANCE_ROLES = frozenset((
    'round1_root_reception', 'round1_complete_execution_read_key',
    'root_whole_final_b_reception', 'b_final_report', 'b_final_findings',
    'same_b_accepted_delta', 'same_b_delta_acceptance', 'root_exact_b_response',
    'accepted_b_initial_canonical_adoption', 'accepted_b_strict_pair_native_comparisons',
    'accepted_build_full_key', 'accepted_all_page_views',
    'source_preparation_root_reception'))
INHERITED_KEY_ROLES = {
    'round1_all_reads': ('docs/papers211_215_sequence/qa/p211_round1_execution01/READ_INPUTS_AFTER.json',
                         'DIRECT_BYTE_PIN_WITH_CONTEXT'),
    'round1_all_external': ('docs/papers211_215_sequence/qa/p211_round1_execution01/EXTERNAL_REFERENCES.json',
                           'WRAPPED_EXTERNAL_PIN'),
    'whole_final_b_root_inputs': ('docs/papers211_215_sequence/qa/p211_b_final_root/INPUTS.json',
                                 'DIRECT_BYTE_PIN_WITH_CONTEXT'),
}
EXTERNAL_EMPTY_DIRECTORIES = {
    'docs/papers211_215_sequence/qa/root_replays/p211_a_initial_01': ('child01/commands',),
    'docs/papers211_215_sequence/qa/root_replays/p211_a_pair_01':
        ('child01/commands','child02/commands'),
    'docs/papers211_215_sequence/qa/p211_runtime_preparation': (
        'discovery01/empty_probe_capsule','discovery02/empty_probe_capsule',
        'tests01/existing_cache','tests02/existing_cache',
        'tests02/fixture_initial/child01/commands','tests02/fixture_pair/child01/commands',
        'tests02/fixture_pair/child02/commands'),
    'docs/papers211_215_sequence/qa/root_replays/p211_b_initial_01': ('child01/commands',),
    'docs/papers211_215_sequence/qa/root_replays/p211_b_pair_01':
        ('child01/commands','child02/commands'),
}
reads, external, commands = {}, {}, []
checks, record_failure = 0, False


def need(value, label):
    global checks
    checks += 1
    if not value:
        raise AssertionError(label)


def pin(raw):
    return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}


def metadata(s):
    return {'mode':s.st_mode,'device':s.st_dev,'inode':s.st_ino,
            'uid':s.st_uid,'gid':s.st_gid,'nlink':s.st_nlink,'size':s.st_size,
            'mtime_ns':s.st_mtime_ns,'ctime_ns':s.st_ctime_ns}


def ordinary(p, directory=False):
    p = Path(p)
    s = p.lstat()
    need(p.is_absolute() and p.resolve() == p and
         (stat.S_ISDIR(s.st_mode) if directory else stat.S_ISREG(s.st_mode)),
         ('ordinary physical path, including parents',str(p)))
    return s


def fresh_read(p):
    p = Path(p)
    before = metadata(ordinary(p))
    raw = p.read_bytes()
    after = metadata(ordinary(p))
    need(before == after and before['size'] == len(raw),('read metadata drift',str(p)))
    return raw, {**pin(raw),'stat':after}


def read(p):
    raw, value = fresh_read(p)
    key = str(p)
    need(key not in reads or reads[key] == value,('read drift',key))
    reads[key] = value
    return raw


def obj(p):
    return json.loads(read(p))


def put(name, value):
    p = HERE/name
    need(p.parent == HERE or p.is_relative_to(HERE/'commands'),('owned output',str(p)))
    raw = value if isinstance(value,bytes) else (json.dumps(value,sort_keys=True,indent=2)+'\n').encode()
    with p.open('xb') as stream:
        stream.write(raw)


def rel(name):
    need(isinstance(name,str) and name and '\\' not in name and
         not any(c in name for c in '\x00\r\n\t') and
         not PurePosixPath(name).is_absolute() and
         PurePosixPath(name).as_posix() == name and
         all(p not in ('','..','.') for p in name.split('/')),('normalized relative path',name))
    return name


def workspace(name):
    return ROOT/rel(name)


def valid_pin(value):
    need(isinstance(value,dict) and set(value) == {'bytes','sha256'} and
         type(value['bytes']) is int and value['bytes'] >= 0 and
         isinstance(value['sha256'],str) and re.fullmatch('[0-9a-f]{64}',value['sha256']),
         ('exact byte pin',value))
    return value


def pinned(path, value):
    raw = read(path)
    need(pin(raw) == valid_pin(value),('bound pin',str(path)))
    return raw


def parent_names(names):
    result = {'.'}
    for name in names:
        for p in PurePosixPath(rel(name)).parents:
            result.add(str(p))
    return result


def inventory(base, names, prune=(), *, empty_directories=()):
    """Complete ordinary tree; only literal prunes or bound external empties."""
    ordinary(base, directory=True)
    need(type(empty_directories) in (tuple,list),
         ('explicit empty-directory sequence',str(base)))
    empty_names = tuple(rel(name) for name in empty_directories)
    need(len(empty_names) == len(set(empty_names)),
         ('unique empty-directory names',str(base)))
    need(not empty_names or (not prune and base.is_relative_to(ROOT) and
         empty_names == EXTERNAL_EMPTY_DIRECTORIES.get(str(base.relative_to(ROOT)),())),
         ('only exact hardcoded external empty directories; never pruned',str(base)))
    need(not (set(empty_names) & (set(names) | parent_names(names) | parent_names(empty_names))),
         ('empty directories are not files, file ancestors or nested empty ancestors',str(base)))
    expected_dirs = parent_names(names) | parent_names(empty_names) | set(empty_names)
    rows = {'.':{'kind':'directory','stat':metadata(base.lstat())}}
    omitted = {}
    def walk(directory):
        for p in sorted(directory.iterdir()):
            s = p.lstat()
            name = str(p.relative_to(base))
            rel(name)
            if p in prune:
                ordinary(p,directory=True)
                omitted[name] = {'kind':'directory','stat':metadata(s)}
                continue
            need(p.resolve() == p and not stat.S_ISLNK(s.st_mode),('no tree symlink',str(p)))
            if stat.S_ISDIR(s.st_mode):
                rows[name] = {'kind':'directory','stat':metadata(s)}
                if name in empty_names:
                    ordinary(p,directory=True)
                    need(not any(p.iterdir()),('bound ordinary directory is truly empty',str(p)))
                walk(p)
            else:
                need(stat.S_ISREG(s.st_mode),('no special tree entry',str(p)))
                rows[name] = {'kind':'file','stat':metadata(s)}
    walk(base)
    need({n for n,v in rows.items() if v['kind'] == 'file'} == set(names),('exact file membership',str(base)))
    need({n for n,v in rows.items() if v['kind'] == 'directory'} == expected_dirs,
         ('exact directory membership including only declared empty directories',str(base)))
    need(all(rows.get(n,{}).get('kind') == 'directory' for n in empty_names),
         ('every declared empty directory is inventoried',str(base)))
    need(set(omitted) == {str(p.relative_to(base)) for p in prune},('exact literal pruning',str(base)))
    return {'entries':rows,'pruned_exact_subtrees':omitted,
            'declared_empty_directories':list(empty_names)}


def parse_sums(raw, nonself=True):
    need(raw.endswith(b'\n'), 'manifest final newline')
    rows = {}
    for line in raw.decode('utf-8').splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)',line)
        need(m is not None,('manifest syntax',line))
        digest,name = m.groups()
        rel(name)
        need(name not in rows and (not nonself or name != 'SHA256SUMS'),('unique/nonself manifest path',name))
        rows[name] = digest
    need(rows, 'nonempty exact manifest')
    return rows


def command(label, argv, cwd=ROOT, empty=True):
    need(re.fullmatch('[a-z0-9_]+',label),('native label',label))
    directory = HERE/'commands'/label
    directory.mkdir(parents=True,exist_ok=False)
    request = {'argv':argv,'cwd':str(cwd),'environment':ENV,
               'stdin':'subprocess.DEVNULL','timeout_seconds':60,
               'started_epoch':time.time(),'executable_key':reads[argv[0]]}
    put(directory/'ATTEMPT.json',request)
    native_exit, exception, stream_state = None, None, 'captured'
    try:
        actual = subprocess.run(argv,cwd=cwd,env=ENV,stdin=subprocess.DEVNULL,
                                capture_output=True,timeout=60)
        stdout,stderr,native_exit = actual.stdout,actual.stderr,actual.returncode
    except subprocess.TimeoutExpired as exc:
        stdout,stderr = exc.stdout or b'',exc.stderr or b''
        exception = {'type':type(exc).__name__,'message':str(exc)}
        stream_state = 'captured_partial_at_timeout; no exit code invented'
    except OSError as exc:
        stdout,stderr = b'',b''
        exception = {'type':type(exc).__name__,'message':str(exc)}
        stream_state = 'unknown_launch_outcome_without_native_handle; streams unavailable'
    put(directory/'stdout.raw',stdout)
    put(directory/'stderr.raw',stderr)
    receipt = {**request,'native_exit_code':native_exit,'exception':exception,
               'stream_capture_status':stream_state,'ended_epoch':time.time(),
               'stdout':pin(stdout),'stderr':pin(stderr),
               'record_directory':str(directory.relative_to(HERE))}
    put(directory/'NATIVE.json',receipt)
    commands.append(receipt)
    need(exception is None and native_exit == 0 and stderr == b'' and
         (not empty or stdout == b''),('native',label))
    return stdout


def evidence_ref(row):
    need(isinstance(row,dict) and set(row) == {'path','pin'}, 'exact reference fields')
    key = rel(row['path'])
    need(key in external and external[key]['pin'] == valid_pin(row['pin']),
         ('entire external evidence was consumed',key))
    return workspace(key)


def file_key(base, names):
    return {name:(read(base/name),reads[str(base/name)])[1] for name in sorted(names)}


def external_trees(specs):
    result = {}
    for spec in specs:
        need(set(spec) == {'root','files','empty_directories','manifest','accepted_scope_reference'},
             'complete external tree fields')
        base = workspace(spec['root'])
        need(str(base) not in result, 'unique complete external tree root')
        names = spec['files']
        need(isinstance(names,list) and len(names) == len(set(names)), 'exact external names')
        empties = spec['empty_directories']
        need(empties == list(EXTERNAL_EMPTY_DIRECTORIES.get(spec['root'],())),
             'only exact separately named historical external empty dirs')
        need(all(str((base/rel(n)).relative_to(ROOT)) in external for n in names),
             ('whole explicit external tree consumed',str(base)))
        result[str(base)] = inventory(base,names,empty_directories=empties)
        if spec['manifest'] is not None:
            name = rel(spec['manifest'])
            sums = parse_sums(read(base/name))
            need(set(sums) == set(names)-{name}, 'complete external nonself seal')
            need(all(external[str((base/n).relative_to(ROOT))]['pin']['sha256'] == h
                     for n,h in sums.items()), 'all external tree hashes')
        evidence_ref(spec['accepted_scope_reference'])
    return result


def original_path(spelling, base=''):
    """Explicit original workspace/absolute spelling, never a destination rebase."""
    need(isinstance(spelling,str) and spelling and '\\' not in spelling and
         not any(c in spelling for c in '\x00\r\n\t'), 'bounded original spelling')
    path = PurePosixPath(spelling)
    if path.is_absolute():
        need(path.as_posix() == spelling and all(p not in ('.','..','') for p in path.parts[1:]),
             'normalized absolute original spelling')
        return Path(spelling)
    return (ROOT if base == '' else workspace(base))/rel(spelling)


def resolve_original(row, logical, value, host):
    """Workspace bytes are read here; full host-entry/settings checks stay with root."""
    valid_pin(value)
    need(set(row) == {'kind','physical_path','accepted_resolution_reference'},
         'explicit original resolution fields')
    if row['kind'] == 'WORKSPACE_FILE':
        physical = rel(row['physical_path'])
        need(logical.is_relative_to(ROOT) and physical in external and
             external[physical]['pin'] == value, 'full workspace key row')
        if workspace(physical) != logical:
            need(row['accepted_resolution_reference'] is not None,
                 'historical substitution requires an actual accepted mapping')
        if row['accepted_resolution_reference'] is not None:
            evidence_ref(row['accepted_resolution_reference'])
    else:
        need(row['kind'] == 'HOST_SEPARATE_ROOT' and not logical.is_relative_to(ROOT) and
             row['physical_path'] == str(logical) and
             row['accepted_resolution_reference'] in host['precopy_recheck_references'],
             'host original spelling kept under a complete separate root recheck')
        evidence_ref(row['accepted_resolution_reference'])
    return {'logical_path':str(logical),'pin':value,**row}


def inherited_keys(binding, host):
    specs = binding['inherited_input_keys']
    need(set(specs) == set(INHERITED_KEY_ROLES), 'all three complete original inherited keys')
    records = {}
    for role,(path,layout) in INHERITED_KEY_ROLES.items():
        spec = specs[role]
        need(spec['reference']['path'] == path and spec['entry_layout'] == layout,
             ('literal accepted full-key schema',role))
        original = obj(evidence_ref(spec['reference']))
        need(isinstance(original,dict) and original and
             set(spec['resolutions']) == set(original), ('no inherited original omission',role))
        mapped = {}
        for logical,value in original.items():
            item = value['pin'] if layout == 'WRAPPED_EXTERNAL_PIN' else value
            expected = {k:item[k] for k in ('bytes','sha256')}
            resolved = resolve_original(spec['resolutions'][logical],original_path(logical),expected,host)
            mapped[logical] = {'original_entry':value,'resolution':resolved}
        records[role] = {'reference':spec['reference'],'entry_layout':layout,'rows':mapped}
    return records


def pin_list_bases(specs, source_map, host):
    needed = {n for n in source_map if n.endswith('.sha256')}
    need({s['document'] for s in specs} == needed and len(specs) == len(needed),
         'every copied SHA input list keeps a complete explicit base/resolution table')
    records = []
    for spec in specs:
        name = spec['document']
        need(spec['base'] == '', 'all current author/A/B SHA input lists are workspace-root relative or absolute')
        evidence_ref(spec['accepted_origin_reference'])
        raw = read(source_map[name]['source'])
        need(raw.endswith(b'\n'), 'original input list final newline')
        parsed = {}
        for line in raw.decode().splitlines():
            match = re.fullmatch(r'([0-9a-f]{64})  (.+)',line)
            need(match is not None, 'exact unchanged input-list syntax')
            digest,spelling = match.groups()
            need(spelling not in parsed, 'unique original input-list spelling')
            original_path(spelling,spec['base'])
            parsed[spelling] = digest
        need(set(parsed) == set(spec['resolutions']), 'whole original mixed-base list resolved')
        mapped = {}
        for spelling,digest in parsed.items():
            resolution = spec['resolutions'][spelling]
            need(set(resolution) == {'pin','resolution'} and resolution['pin']['sha256'] == digest,
                 'root supplies exact original bytes and unchanged SHA for every listed path')
            mapped[spelling] = resolve_original(
                resolution['resolution'],original_path(spelling,spec['base']),resolution['pin'],host)
        records.append({'document':name,'original_base':spec['base'],
                        'accepted_origin_reference':spec['accepted_origin_reference'],'rows':mapped})
    return records


def markdown_links(specs, source_map):
    need(set(specs) == {n for n in source_map if n.endswith('.md')},
         'complete original document map, including every unchanged Round1 Markdown')
    by_original = {str(v['original_document']):n for n,v in source_map.items()}
    need(len(by_original) == len(source_map), 'unambiguous original copied document roles')
    result = {}
    for name,spec in sorted(specs.items()):
        original = workspace(spec['original_document'])
        need(original == source_map[name]['original_document'], 'original document base unchanged')
        evidence_ref(spec['accepted_origin_reference'])
        body = read(source_map[name]['source']).decode()
        need(re.search(r'(?m)^\s{0,3}\[[^\]\n]+\]:',body) is None and
             re.search(r'\[[^\]\n]*\]\[[^\]\n]*\]',body) is None,
             'unsupported reference-link syntax requires a fresh scoped source')
        actual = []
        for match in re.finditer(r'!?\[[^\]\n]*\]\(([^)\n]+)\)',body):
            href = match.group(1).strip().strip('<>')
            if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:',href) or href.startswith('#'):
                continue
            target = unquote(href.split('#',1)[0])
            need(target and '\\' not in target and not any(c in target for c in '\x00\r\n\t'),
                 'bounded inline local target')
            logical = Path(os.path.abspath(original.parent/target))
            need(logical.is_relative_to(ROOT), 'current copied Markdown local links remain workspace scoped')
            actual.append((href,str(logical.relative_to(ROOT))))
        selected = spec['local_links']
        need(actual == [(r['href'],r['logical_target']) for r in selected],
             ('complete ordered unchanged local links',name))
        for row in selected:
            logical = workspace(row['logical_target'])
            destination = by_original.get(str(logical))
            if destination is not None:
                need(row['kind'] == 'copied' and row['target'] == destination,
                     'literal copied target mapping')
            elif row['kind'] == 'external_file':
                need(row['target'] in external, 'complete external file target consumed')
                evidence_ref(row['accepted_resolution_reference'])
            else:
                need(row['kind'] == 'external_directory', 'explicit external directory link')
                physical = workspace(row['target'])
                need(all(str((physical/rel(n)).relative_to(ROOT)) in external
                         for n in row['directory_files']), 'every directory link file consumed')
                inventory(physical,row['directory_files'])
                evidence_ref(row['accepted_resolution_reference'])
        result[name] = spec
    return result


def json_bases(specs, source_map):
    need(set(specs) == {n for n in source_map if n.endswith('.json')},
         'every copied JSON retains original field meanings, not generic schema relabelling')
    for name,spec in specs.items():
        need(spec['original_document'] == str(source_map[name]['original_document'].relative_to(ROOT)),
             'JSON original document unchanged')
        need(spec['base'] == '' or rel(spec['base']), 'explicit JSON original base')
        evidence_ref(spec['accepted_origin_and_schema_reference'])
        need(isinstance(spec['scope_note'],str) and spec['scope_note'], 'explicit accepted schema/read limit')
    return specs


def recorder_runtime(expected):
    """Actual loaded source/map subset; not a substitute for the entire reused host key."""
    need(isinstance(expected,dict) and expected, 'root-bound complete recorder runtime-file set')
    for path,value in expected.items():
        need(Path(path).is_absolute() and Path(path).resolve() == Path(path), 'resolved runtime file spelling')
        pinned(Path(path),value)
    modules = {}
    for name,module in sorted(sys.modules.items()):
        path = getattr(module,'__file__',None)
        if path and Path(path).is_file():
            physical = Path(path).resolve()
            need(physical.suffix not in ('.pyc','.pyo'), 'no bytecode runtime module')
            modules[name] = {'path':str(physical),'pin':pin(read(physical))}
    raw = Path('/proc/self/maps').read_bytes()
    mapped = {}
    for line in raw.decode().splitlines():
        columns = line.split(None,5)
        if len(columns) == 6 and columns[5].startswith('/'):
            physical = Path(columns[5]).resolve()
            mapped[str(physical)] = pin(read(physical))
    observed = dict(mapped)
    observed.update({r['path']:r['pin'] for r in modules.values()})
    need(all(expected.get(p) == value or
             (Path(p) == HERE/'freeze.py' and value == pin(read(HERE/'freeze.py')))
             for p,value in observed.items()), 'every actually imported/mapped runtime file prebound')
    return {'modules':modules,'mapped_files':mapped,'maps_raw':raw.decode(),
            'maps_pin':pin(raw),'environment':dict(os.environ),'argv':sys.orig_argv,
            'cwd':str(Path.cwd()),'flags':str(sys.flags),'sys_path':sys.path,
            'pycache_prefix':sys.pycache_prefix,
            'scope':'Actual parent observed maps/imports and all explicit runtime files; not transient/non-FLS OS tracing.'}


def main():
    global record_failure
    need(HERE == EXECUTION and Path.cwd() == ROOT and
         Path(__file__).absolute() == HERE/'freeze.py', 'literal fresh root-owned execution placement')
    need(sys.argv[1:] == ['--binding',str(HERE/'BINDING.json')], 'literal binding argv')
    need({p.name for p in HERE.iterdir()} ==
         {'freeze.py','BINDING.json','ROOT_INVOCATION_ATTEMPT.json'}, 'exact three initial files')
    for name in ('freeze.py','BINDING.json','ROOT_INVOCATION_ATTEMPT.json'):
        ordinary(HERE/name)
    binding = obj(HERE/'BINDING.json')
    need(binding.get('schema') == 'p211-round2-root-binding-v1' and binding.get('enabled') is True,
         'SOURCE_ONLY pending template cannot execute')
    need(binding['execution_directory'] == str(EXECUTION.relative_to(ROOT)) and
         binding['root_authorization']['issuer'] == '/root' and
         binding['root_authorization']['decision'] == 'AUTHORIZE_PHYSICAL_P211_ROUND2_FROM_ACCEPTED_FINAL_B',
         'literal separate root authority after actual whole final-B acceptance')
    record_failure = True
    need(dict(os.environ) == ENV and sys.executable == '/usr/bin/python3.10' and
         sys.flags.isolated == 1 and sys.flags.no_site == 1 and
         sys.flags.dont_write_bytecode == 1 and not sys.flags.optimize and
         sys.path == ['/usr/lib/python310.zip','/usr/lib/python3.10','/usr/lib/python3.10/lib-dynload'],
         'exact isolated recorder environment/runtime settings')
    need(not os.path.lexists(FROZEN) and not os.path.lexists(PAPER/'qa_final'),
         'wholly absent Round2 and terminal-build root before the freeze')
    for row in binding['external_inputs']:
        key = rel(row['physical_path'])
        need(key not in external and row['roles'] and
             all(isinstance(r,str) and r for r in row['roles']), 'unique declared external physical row')
        need(not workspace(key).is_relative_to(HERE) and not workspace(key).is_relative_to(FROZEN),
             'no output/self prerequisite')
        pinned(workspace(key),row['pin'])
        external[key] = row
    need(set(binding['acceptance_references']) == ACCEPTANCE_ROLES, 'all actual acceptance roles')
    for reference in binding['acceptance_references'].values():
        evidence_ref(reference)
    evidence_ref(binding['root_authorization']['record'])
    need(evidence_ref(binding['preparation_manifest']) == PREPARATION/'SHA256SUMS',
         'entire final preparation seal bound')
    need(evidence_ref(binding['base_source']) == BASE_SOURCE, 'actual declared Round1 recorder lineage')
    need(evidence_ref(binding['intended_inventory']) == PREPARATION/'INTENDED_INVENTORY.json',
         'exact fully enumerated preparation selection')
    need(pinned(HERE/'freeze.py',binding['execution_source_pin']) == read(PREPARATION/'freeze.py'),
         'actual prepared and executed fresh source equal')
    invocation = obj(HERE/'ROOT_INVOCATION_ATTEMPT.json')
    need(invocation == {'argv':['/usr/bin/python3.10','-I','-S','-B',str(HERE/'freeze.py'),'--binding',str(HERE/'BINDING.json')],
          'cwd':str(ROOT),'environment':ENV,'stdin':'subprocess.DEVNULL',
          'source_pin':binding['execution_source_pin'],'binding_pin':pin(read(HERE/'BINDING.json'))},
         'exact root pre-invocation request; actual native completion remains separate')
    host = binding['host_reuse_boundary']
    need(host['mode'] == 'ROOT_SEPARATE_COMPLETE_HOST_KEYS_AND_SETTINGS_RECHECK' and
         host['postcopy_root_recheck_required'] is True and
         host['recorder_rehashes_complete_reused_host_keys'] is False and
         host['complete_host_key_references'] and host['precopy_recheck_references'],
         'no claim to consume every reused host referent through workspace metadata')
    for field in ('complete_host_key_references','accepted_settings_references','precopy_recheck_references'):
        need(isinstance(host[field],list) and host[field], 'nonempty complete separate root references')
        for reference in host[field]:
            evidence_ref(reference)
    need(binding['b_acceptance'] == {
        'reviewer':B_REVIEWER,'same_reviewer_accepted_exact_delta':True,
        'root_received_whole_final_originals':True,'current_open_findings':0,
        'accepted_final_manifest_pin':{'bytes':3549,'sha256':'45b7c0337259da2fccb078cf4d7b84ec7228a16a6bf6089167c19a26c477ca46'}},
        'root binds actual final same-B acceptance, never an inferred preparatory verdict')
    selected = obj(PREPARATION/'INTENDED_INVENTORY.json')
    need(selected['schema'] == 'p211-round2-intended-inventory-v1' and
         selected['target'] == str(FROZEN.relative_to(ROOT)) and
         selected['payload_count'] == 123 and selected['payload_bytes'] == 10518152 and
         selected['total_file_count_with_future_outer_manifest'] == 124,
         'literal accepted complete intended scope')
    source_map = {}
    for row in selected['rows']:
        name = rel(row['destination'])
        need(name not in source_map and name != 'SHA256SUMS', 'distinct nonself destination')
        source,original = workspace(row['source']),workspace(row['original_document'])
        if row['role'] == 'UNCHANGED_ROUND1_PAYLOAD':
            need(source == ROUND1/name and not name.startswith('review_b/'), 'unchanged R1 role')
        else:
            need(row['role'] == 'COMPLETE_FINAL_B_PACKAGE' and name.startswith('review_b/') and
                 source == B_ROOT/name.removeprefix('review_b/') and original == source,
                 'complete exact B role under review_b')
        source_map[name] = {'source':source,'original_document':original,
                            'pin':valid_pin(row['pin']),'role':row['role']}
    r1 = {n:v['pin'] for n,v in source_map.items() if v['role'] == 'UNCHANGED_ROUND1_PAYLOAD'}
    b_all = {n.removeprefix('review_b/'):v['pin'] for n,v in source_map.items()
             if v['role'] == 'COMPLETE_FINAL_B_PACKAGE'}
    r1_seal = selected['source_seals']['round1']['pin']
    need(r1_seal == {'bytes':8048,'sha256':'582630470c6d1b423f818ed566ed4b699865c04b30543aa502d4556011dd6828'},
         'literal accepted Round1 outer seal is external, not a second copied outer seal')
    need(len(r1) == 83 and len(b_all) == 40 and len(source_map) == 123 and
         sum(v['pin']['bytes'] for v in source_map.values()) == 10518152, 'complete exact inventory arithmetic')
    need(parse_sums(pinned(ROUND1/'SHA256SUMS',r1_seal)) == {n:v['sha256'] for n,v in r1.items()},
         'all old83 rows match accepted physical Round1 manifest')
    b_sums = parse_sums(pinned(B_ROOT/'SHA256SUMS',b_all['SHA256SUMS']))
    need(b_sums == {n:v['sha256'] for n,v in b_all.items() if n != 'SHA256SUMS'},
         'entire B39 payload manifest plus original seal copied')
    for role,name in (('b_final_report','REPORT.md'),('b_final_findings','FINDINGS.json'),
                      ('same_b_accepted_delta','DELTA.md'),('same_b_delta_acceptance','DELTA_ACCEPTANCE.json')):
        need(binding['acceptance_references'][role] ==
             {'path':str((B_ROOT/name).relative_to(ROOT)),'pin':b_all[name]}, 'exact copied accepted B role')
    live_names = sorted(n for n in r1 if not n.startswith('review_a/'))
    need(len(live_names) == 32, 'literal unchanged author32')
    r1_all = {**r1,'SHA256SUMS':r1_seal}
    source_trees_before = {'round1':inventory(ROUND1,r1_all),'b':inventory(B_ROOT,b_all),
                           'live':inventory(PAPER,live_names,(ROUND0,ROUND1))}
    source_before = {'round1':file_key(ROUND1,r1_all),'b':file_key(B_ROOT,b_all),
                     'live':file_key(PAPER,live_names)}
    for role,expected in (('round1',r1_all),('b',b_all),('live',{n:r1[n] for n in live_names})):
        need({n:{k:v[k] for k in ('bytes','sha256')} for n,v in source_before[role].items()} == expected,
             'entire physical source key agrees with accepted bytes')
    need(set(binding['native_tool_pins']) == set(TOOLS), 'all four native tools bound')
    for path,value in binding['native_tool_pins'].items():
        pinned(Path(path),value)
    runtime_before = recorder_runtime(binding['recorder_runtime_file_pins'])
    tools_before = {p:reads[p] for p in TOOLS}
    external_before = {n:reads[str(workspace(n))] for n in sorted(external)}
    external_trees_before = external_trees(binding['external_trees'])
    need(str(PREPARATION) in external_trees_before and
         str(QA/'p211_round1_execution01') in external_trees_before,
         'complete preparation and accepted R1 execution inventories required')
    inherited = inherited_keys(binding,host)
    pin_bases = pin_list_bases(binding['pin_list_bases'],source_map,host)
    links = markdown_links(binding['document_origins'],source_map)
    json_origins = json_bases(binding['json_pin_bases'],source_map)
    for name,value in (
        ('PROCESS_CONTEXT.json',runtime_before),('EXECUTED_FREEZE_SOURCE.py',read(HERE/'freeze.py')),
        ('BINDING_PIN.json',pin(read(HERE/'BINDING.json'))),('HOST_REUSE_BOUNDARY.json',host),
        ('SOURCE_TREES_BEFORE.json',source_trees_before),('SOURCE_INPUTS_BEFORE.json',source_before),
        ('EXTERNAL_INPUTS_BEFORE.json',external_before),('EXTERNAL_TREES_BEFORE.json',external_trees_before),
        ('NATIVE_TOOLS_BEFORE.json',tools_before),('INHERITED_ORIGINAL_KEYS.json',inherited),
        ('DECLARED_PIN_LIST_BASES.json',pin_bases),('DECLARED_JSON_PIN_BASES.json',json_origins),
        ('MARKDOWN_LINK_MAP.json',links),
        ('SOURCE_SELECTION.json',{n:{**v,'source':str(v['source'].relative_to(ROOT)),
         'original_document':str(v['original_document'].relative_to(ROOT))} for n,v in sorted(source_map.items())})):
        put(name,value)
    for number,name in enumerate(live_names,1):
        command('live_round1_compare_%03d'%number,['/usr/bin/cmp','--',str(PAPER/name),str(ROUND1/name)])
    FROZEN.mkdir()
    (FROZEN/'review_b').mkdir()
    command('copy_unchanged_round1_payloads',['/usr/bin/cp','-p','--parents','--',*sorted(r1),str(FROZEN)],cwd=ROUND1)
    command('copy_complete_final_b',['/usr/bin/cp','-p','--parents','--',*sorted(b_all),str(FROZEN/'review_b')],cwd=B_ROOT)
    origins,destination_inodes = [],set()
    for number,(name,row) in enumerate(sorted(source_map.items()),1):
        source,destination = row['source'],FROZEN/name
        ss,ds = ordinary(source),ordinary(destination)
        inode = (ds.st_dev,ds.st_ino)
        need(inode != (ss.st_dev,ss.st_ino) and inode not in destination_inodes and ds.st_nlink == 1,
             'separate physical, non-hardlinked immutable payload')
        destination_inodes.add(inode)
        command('copy_compare_%05d'%number,['/usr/bin/cmp','--',str(source),str(destination)])
        need(read(source) == read(destination) and pin(read(destination)) == row['pin'], 'full copied bytes')
        origins.append({'relative_name':name,'role':row['role'],'original_path':str(source.relative_to(ROOT)),
                        'original_document':str(row['original_document'].relative_to(ROOT)),
                        'frozen_path':str(destination.relative_to(ROOT)),'pin':row['pin'],
                        'source_key':reads[str(source)],'frozen_key':reads[str(destination)]})
    manifest = ''.join(source_map[n]['pin']['sha256']+'  '+n+'\n' for n in sorted(source_map)).encode()
    with (FROZEN/'SHA256SUMS').open('xb') as stream:
        stream.write(manifest)
    need(read(FROZEN/'SHA256SUMS') == manifest, 'actual new exact nonself outer manifest')
    tree = inventory(FROZEN,set(source_map)|{'SHA256SUMS'})
    for label,base,names in (('outer',FROZEN,sorted(source_map)),
        ('inner_a',FROZEN/'review_a',list(parse_sums(read(ROUND1/'review_a/SHA256SUMS')))),
        ('inner_b',FROZEN/'review_b',list(b_sums))):
        raw = command('verify_'+label+'_manifest',['/usr/bin/sha256sum','-c','SHA256SUMS'],cwd=base,empty=False)
        need(raw == ''.join(n+': OK\n' for n in names).encode(), 'all actual native hash lines')
    source_after = {'round1':file_key(ROUND1,r1_all),'b':file_key(B_ROOT,b_all),'live':file_key(PAPER,live_names)}
    need(source_after == source_before, 'full rich original source before/after equality')
    source_trees_after = {'round1':inventory(ROUND1,r1_all),'b':inventory(B_ROOT,b_all),
                          'live':inventory(PAPER,live_names,(ROUND0,ROUND1,FROZEN))}
    for role in ('round1','b'):
        need(source_trees_after[role] == source_trees_before[role], 'unchanged complete original trees')
    live_before,live_after = source_trees_before['live']['entries'],source_trees_after['live']['entries']
    need({n:v for n,v in live_before.items() if n != '.'} ==
         {n:v for n,v in live_after.items() if n != '.'}, 'all live descendants unchanged')
    permitted = {'size','mtime_ns','ctime_ns','nlink'}
    need({k:v for k,v in live_before['.']['stat'].items() if k not in permitted} ==
         {k:v for k,v in live_after['.']['stat'].items() if k not in permitted},
         'only parent directory metadata from the one new Round2 may change')
    runtime_after = recorder_runtime(binding['recorder_runtime_file_pins'])
    external_after = {n:fresh_read(workspace(n))[1] for n in sorted(external)}
    external_trees_after = external_trees(binding['external_trees'])
    tools_after = {p:fresh_read(Path(p))[1] for p in TOOLS}
    need(external_after == external_before and external_trees_after == external_trees_before and
         tools_after == tools_before, 'complete external/tool tree and file rich closure')
    read_before = dict(reads)
    read_after = {p:fresh_read(Path(p))[1] for p in sorted(read_before)}
    need(read_after == read_before and inventory(FROZEN,set(source_map)|{'SHA256SUMS'}) == tree,
         'every actual read and the complete physical new tree close unchanged')
    for name,value in (('SOURCE_INPUTS_AFTER.json',source_after),('SOURCE_TREES_AFTER.json',source_trees_after),
        ('EXTERNAL_INPUTS_AFTER.json',external_after),('EXTERNAL_TREES_AFTER.json',external_trees_after),
        ('NATIVE_TOOLS_AFTER.json',tools_after),('PARENT_RUNTIME_AFTER.json',runtime_after),
        ('READ_INPUTS_BEFORE.json',read_before),('READ_INPUTS_AFTER.json',read_after),
        ('FROZEN_ORIGIN_MAP.json',origins),('FROZEN_TREE.json',tree),
        ('EXTERNAL_REFERENCES.json',external),('NATIVE_COMMANDS.json',commands)):
        put(name,value)
    result = {'status':'PHYSICAL_P211_ROUND2_CREATED_PENDING_ROOT_RECEPTION',
              'round1_unchanged_payloads':83,'complete_final_b_files':40,'payloads':123,
              'files_with_manifest':124,'payload_bytes':10518152,'manifest':pin(manifest),
              'checks':checks,'read_paths':len(reads),'native_commands':len(commands),
              'scientific_executions':0,'builds':0,'new_page_views':0,'reviews':0,
              'paper_complete':False,'execution_package_seal':'PENDING_ACTUAL_ROOT_INVOCATION_RETURN',
              'complete_reused_host_keys_rehashed_by_recorder':False,
              'postcopy_complete_host_keys_and_settings_recheck':'PENDING_SEPARATE_ROOT_RECEPTION',
              'external':'OWNER_AMBER / HOLD_EXTERNAL'}
    put('RESULT.json',result)
    print(json.dumps(result,sort_keys=True))


if __name__ == '__main__':
    try:
        main()
    except BaseException as exc:
        failure = {'status':'FAILED_PRESERVE_ATTEMPT_AND_ANY_PARTIAL_ROUND2',
                   'exception_type':type(exc).__name__,'message':str(exc),
                   'checks':checks,'native_commands':len(commands),'ended_epoch':time.time()}
        if record_failure:
            for name,value in (('FAILURE.json',failure),('READ_INPUTS_PARTIAL.json',reads),
                               ('EXTERNAL_REFERENCES_PARTIAL.json',external),('NATIVE_COMMANDS.json',commands)):
                if not os.path.lexists(HERE/name):
                    put(name,value)
        print(json.dumps(failure,sort_keys=True))
        traceback.print_exc()
        raise SystemExit(1)
