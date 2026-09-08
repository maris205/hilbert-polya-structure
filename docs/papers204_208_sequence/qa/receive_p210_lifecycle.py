#!/usr/bin/env python3
"""Root's independent original reception; no old gate or producer is imported."""
from collections import Counter
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import shlex
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
PREP = QA / 'p210_terminal_lifecycle_preparation'
OUT = QA / 'p210_terminal_lifecycle_01'
HISTORY = QA / 'p210_precompletion_controls_01'
ENV = dict(PATH='/usr/bin:/bin', LANG='C.UTF-8', LC_ALL='C.UTF-8', TZ='UTC')
SEAL = '0745224b3f793ac4fe7a68ebc5c66a68e2649a7fb475b8deaf70ecd3bfdb4714'
READ, CHECKS, PACKAGES = {}, Counter(), {}

def ck(ok, label):
    CHECKS[label] += 1
    if not ok:
        raise AssertionError(label)

def key(path):
    p = Path(path)
    ck(p.is_file(), 'physical regular target')
    digest = sha256()
    with p.open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            digest.update(block)
    value = dict(real=str(p.resolve()), size=p.stat().st_size,
                 sha256=digest.hexdigest(), symlink=os.readlink(p) if p.is_symlink() else None)
    ck(str(p) not in READ or READ[str(p)] == value, 'entire current key stable')
    READ[str(p)] = value
    return value

def pin(path, expected=None):
    value = key(path)
    small = dict(sha256=value['sha256'], bytes=value['size'])
    if expected is not None:
        ck((value if set(expected) == set(value) else small) == expected, 'entire expected pin')
    return small

def raw(path):
    expected = pin(path)
    value = Path(path).read_bytes()
    ck(dict(bytes=len(value), sha256=sha256(value).hexdigest()) == expected, 'raw stability')
    return value

def obj(path):
    return json.loads(raw(path))

def rows(path):
    value = {}
    for line in raw(path).decode().splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        ck(m is not None, 'strict manifest syntax')
        digest, name = m.groups()
        p = Path(name)
        ck(not p.is_absolute() and p.as_posix() == name and
           not any(x in {'.', '..'} for x in p.parts) and name not in value, 'bounded unique member')
        value[name] = digest
    return value

def inventory(base):
    result = set()
    for p in base.rglob('*'):
        ck(not p.is_symlink(), 'no package symlink')
        if p.is_file():
            result.add(p.relative_to(base).as_posix())
    return result

def package(base, count, manifest='SHA256SUMS'):
    members = rows(base / manifest)
    ck(len(members) == count and manifest not in members and
       inventory(base) == set(members) | {manifest}, 'complete nonself package')
    PACKAGES[base] = set(members) | {manifest}
    for name, digest in members.items():
        ck(key(base / name)['sha256'] == digest, 'entire payload bytes')
    return members

def main():
    # Verify the actual original normal native closure BEFORE accepting the output seal.
    launch = obj(QA / 'P210_LIFECYCLE01_ROOT_LAUNCH.actual.json')
    completed = obj(QA / 'P210_LIFECYCLE01_ROOT_COMPLETION.actual.json')
    ck(launch['result']['output'] == '' and 'exit_code' not in launch['result'] and
       launch['result']['session_id'] == completed['session_id'] == 5316 and
       completed['launch_record'] == 'P210_LIFECYCLE01_ROOT_LAUNCH.actual.json' and
       completed['result']['exit_code'] == 0 and 'session_id' not in completed['result'] and
       launch['cwd'] == str(ROOT) and shlex.split(launch['command']) ==
       ['/usr/bin/python3.10', '-I', '-S', '-B', str(QA / 'record_p210_lifecycle_01.py'),
        '--expected-lifecycle-preparation-sha256', SEAL], 'actual normal-zero native closure')
    report = obj(OUT / 'LIFECYCLE_REPORT.json')
    result, attempt, spawn = (obj(OUT / n) for n in ('RESULT.json', 'ATTEMPT.json', 'SPAWN.json'))
    argv = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
            'pycache_prefix=' + str(OUT / 'never_created_reader_cache'),
            str(PREP / 'inspect_p210_lifecycle.py'), '--expected-preparation-sha256', SEAL]
    ck(result['argv'] == argv and result['cwd'] == str(ROOT) and result['environment'] == ENV and
       result['original_wait_exit_code'] == result['cleanup_wait_exit_code'] == 0 and
       result['timed_out'] is False and result['wait_error'] is None and result['cleanup_events'] == [] and
       result['child_reaped'] is result['process_group_absent'] is result['inputs_unchanged'] is
       result['paper_terminal_present_after'] is True and result['inputs_before'] == result['inputs_after'] and
       len(result['inputs_before']) == 11 and not os.path.lexists(OUT / 'never_created_reader_cache'),
       'original normal wait and settled capture')
    ck(attempt == dict(argv=argv, cwd=str(ROOT), environment=ENV, inputs_before=result['inputs_before'],
       timeout_seconds=600, start_new_session=True, started_epoch=attempt['started_epoch'],
       paper_terminal_present_before=True) and
       spawn == dict(pid=result['pid'], process_group_id=result['pid'], spawned_epoch=spawn['spawned_epoch']) and
       result['finished_epoch'] >= spawn['spawned_epoch'] >= attempt['started_epoch'] and
       type(result['pid']) is int and result['pid'] > 0, 'complete attempt and spawn')
    try:
        os.killpg(result['pid'], 0)
    except ProcessLookupError:
        pass
    else:
        raise AssertionError('owned process group still exists')
    pin(PREP / 'SHA256SUMS', dict(bytes=434, sha256=SEAL))
    package(PREP, 5)
    package(OUT, 6)
    for name, expected in result['inputs_before'].items():
        pin(name, expected)
    pin(OUT / 'LIFECYCLE_REPORT.json', result['stdout'])
    pin(OUT / 'stderr', result['stderr'])
    ck(raw(OUT / 'stderr') == b'' and
       raw(OUT / 'executed_source.py') == raw(QA / 'record_p210_lifecycle_01.py'), 'separate raw streams and source')
    summary = dict(status='PASS_ACTUAL_P210_LIFECYCLE_FOLLOWUP_CAPTURE', output=str(OUT),
        original_wait_exit_code=0, stdout=result['stdout'], stderr=result['stderr'],
        result=pin(OUT / 'RESULT.json'), seal=pin(OUT / 'SHA256SUMS'),
        checks=28659, current_path_keys=2319, lifecycle_acceptance=False)
    ck(completed['result']['output'] == json.dumps(summary, sort_keys=True) + '\n', 'entire native stdout')
    ck(report['schema'] == 'p210-document-only-lifecycle-followup-v1' and
       report['status'] == 'PASS_P210_DOCUMENT_ONLY_LIFECYCLE_FOLLOWUP_ROOT_ACCEPTANCE_PENDING' and
       report['checks'] == sum(report['checks_by_kind'].values()) == 28659 and
       report['paper'] == 'P210' and report['external'] == 'OWNER_AMBER / HOLD_EXTERNAL' and
       all(report[n] == 0 for n in ('new_scientific_runs', 'new_builds', 'new_views',
           'new_manuscript_reviews', 'reader_file_writes', 'old_programs_imported_or_executed', 'host_dependency_tree_walks')) and
       report['root_acceptance'] is report['paper_completion'] is report['five_paper_completion'] is False,
       'complete bounded actual PASS scope')
    runtime = report['current_documentary_runtime']
    ck(runtime == dict(argv=argv[6:], cache=str(OUT / 'never_created_reader_cache'), cache_absent=True,
       cwd=str(ROOT), environment=ENV, executable='/usr/bin/python3.10', isolated=1, no_site=1,
       no_bytecode=True, module_search_path=['/usr/lib/python310.zip', '/usr/lib/python3.10',
       '/usr/lib/python3.10/lib-dynload']), 'entire reported invocation')
    binding = obj(PREP / 'ACTUAL_BINDING.json')
    for name, expected in binding['named_current_input_pins'].items():
        pin(name, expected)
    ck(len(binding['named_current_input_pins']) == 62, 'all actual named pins')
    package(QA / 'p210_terminal_artifact_revision_03', 9)
    package(QA / 'p210_terminal_artifact_03', 6)
    package(HISTORY, 7)
    after = package(PAPER, 2244, 'PAPER_MANIFEST.sha256')
    before = rows(HISTORY / 'PAPER_MANIFEST.sha256')
    transition = report['document_only_transition']
    ck(len(before) == 2244 and set(before) == set(after) and
       [n for n in before if before[n] != after[n]] == ['ROOT_LIFECYCLE.md'] and
       transition['old_payloads'] == transition['current_payloads'] == 2244 and
       transition['physical_files'] == 2245 and transition['changed_payloads'] == ['ROOT_LIFECYCLE.md'],
       'sole changed lifecycle manifest row')
    for name, prefix in [('ROOT_LIFECYCLE.md', 'lifecycle'), ('PAPER_MANIFEST.sha256', 'whole_manifest')]:
        pin(HISTORY / name, transition['old_' + prefix])
        pin(PAPER / name, transition['current_' + prefix])
    ck(report['exact_two_historical_control_roles'] == [dict(original_path=str(PAPER / name),
       physical_path=str(HISTORY / name), **transition['old_' + prefix]) for name, prefix in
       [('PAPER_MANIFEST.sha256', 'whole_manifest'), ('ROOT_LIFECYCLE.md', 'lifecycle')]], 'two exact history roles')
    links = []
    for source in (PAPER / 'ROOT_LIFECYCLE.md', QA / 'P210_ARTIFACT_ROOT_INSPECTION.md'):
        body = raw(source).decode()
        ck('```' not in body and '~~~' not in body and
           re.search(r'(?m)^(?: {4}|\t)', body) is None, 'actual documents need no fenced or indented code removal')
        body = re.sub(r'(`+)(?:(?!\1)[\s\S])*?\1', ' ', body)
        for href in re.findall(r'\[[^\]]*\]\(([^)]+)\)', body):
            target = href.strip().strip('<>').split('#', 1)[0]
            if not target or re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', target):
                continue
            path = (source.parent / unquote(target)).resolve()
            ck(path.is_relative_to(ROOT), 'bounded documentary target')
            links.append(dict(document=str(source), href=href, path=str(path), pin=key(path)))
    ck(links == transition['genuine_documentary_links'] and len(links) == 22, 'all ordered full link rows')
    ledger = report['complete_current_read_keys']
    ck(len(ledger) == report['current_path_keys'] == 2319 and
       all(set(v) == {'real', 'size', 'sha256', 'symlink'} for v in ledger.values()), 'entire current map schema')
    for name, expected in ledger.items():
        ck(key(name) == expected, 'full ledger row all four fields')
    for base, members in PACKAGES.items():
        if base != OUT:
            ck({str(base / name) for name in members} <= set(ledger), 'source package present in full map')
    ck(set(binding['named_current_input_pins']) <= set(ledger), 'all named inputs present in map')
    fixed = dict(READ)
    for name, expected in fixed.items():
        ck(key(name) == expected, 'root second full content read')
    for base, members in PACKAGES.items():
        ck(inventory(base) == members, 'final exact package membership')
    encoded = json.dumps(ledger, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()
    print(json.dumps(dict(status='PASS_ROOT_P210_LIFECYCLE_ORIGINAL_RECEPTION',
        checks=sum(CHECKS.values()), current_documentary_keys=2319, direct_paths=len(READ),
        full_map=dict(bytes=len(encoded), sha256=sha256(encoded).hexdigest()),
        lifecycle_raw=result['stdout'], lifecycle_seal=pin(OUT / 'SHA256SUMS'),
        packages=len(PACKAGES), full_links=len(links), whole_payloads=2244,
        changed_payloads=['ROOT_LIFECYCLE.md'], original_native_session=5316, original_native_exit=0,
        additional_whole_host_passes=0, new_scientific_runs=0, new_builds=0, new_views=0,
        external='OWNER_AMBER / HOLD_EXTERNAL'), sort_keys=True))

if __name__ == '__main__':
    main()
