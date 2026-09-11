#!/usr/bin/env python3
"""Root reception of actual initial artifact raw capture and complete map recipe.

The accepted reader just performed the full current double read and membership
checks. This separate reception reconstructs every original map field, checks
all ten exact historical roles, hashes all new extras/direct inputs and checks
nonfile states. It does not claim another whole-host content pass or new
science/builds/views. No old program is imported or executed.
"""
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import shlex

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
CAP = QA / 'p210_terminal_artifact_03'
PREP = QA / 'p210_terminal_artifact_revision_03'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
READS, CHECKS = {}, 0

def need(value, label):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(label)

def dp(data):
    return {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}

def raw(path):
    p = Path(path)
    data = p.read_bytes()
    value = dict(real=str(p.resolve()), sha256=hashlib.sha256(data).hexdigest(), size=len(data),
                 symlink=str(p.readlink()) if p.is_symlink() else None)
    need(str(p) not in READS or READS[str(p)] == value, 'current direct read stable')
    READS[str(p)] = value
    return data

def pin(path):
    return dp(raw(path))

def obj(path):
    data = raw(path)
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)

def canonical(value):
    return dp(json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode())

def package(base, digest, count):
    need(pin(base / 'SHA256SUMS')['sha256'] == digest, 'fixed nonself seal')
    rows = {}
    for line in raw(base / 'SHA256SUMS').decode().splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(m is not None, 'manifest syntax')
        h, name = m.groups()
        need(name not in rows and not Path(name).is_absolute() and '..' not in Path(name).parts and
             name != 'SHA256SUMS' and (base / name).resolve() == base / name, 'contained unique row')
        rows[name] = pin(base / name)
        need(rows[name]['sha256'] == h, 'complete sealed payload content')
    need(len(rows) == count and set(rows) == {p.relative_to(base).as_posix() for p in base.rglob('*')
         if p.is_file() and p != base / 'SHA256SUMS'}, 'complete physical package membership')
    return rows

def rich_schema(row):
    need(set(row) == {'real','sha256','size','symlink'} and Path(row['real']).is_absolute() and
         type(row['size']) is int and row['size'] >= 0 and re.fullmatch('[0-9a-f]{64}', row['sha256']) is not None and
         (row['symlink'] is None or type(row['symlink']) is str), 'entire rich file schema')
    return row

def main():
    launch = obj(QA / 'P210_ARTIFACT03_ROOT_LAUNCH.actual.json')
    completed = obj(QA / 'P210_ARTIFACT03_ROOT_COMPLETION.actual.json')
    need(launch['result']['session_id'] == completed['session_id'] == 16560 and
         launch['result']['chunk_id'] == '2d36d8' and launch['result']['output'] == '' and
         'exit_code' not in launch['result'] and completed['result']['chunk_id'] == 'c0c94a' and
         completed['result']['exit_code'] == 0 and 'session_id' not in completed['result'], 'actual normal root native closure before capture hashes')
    result, attempt, spawn = (obj(CAP / name) for name in ('RESULT.json','ATTEMPT.json','SPAWN.json'))
    need(result['original_wait_exit_code'] == result['cleanup_wait_exit_code'] == 0 and
         result['child_reaped'] is result['process_group_absent'] is True and result['cleanup_events'] == [] and
         result['timed_out'] is False and result['wait_error'] is None, 'original normal wait not cleanup success')
    try:
        os.killpg(result['pid'], 0)
    except ProcessLookupError:
        pass
    else:
        raise AssertionError('owned group still exists')
    seal = '8efef29aee07210eee9ec95a1d3df51d4539f33d3189991cd1b42a98a508d3dd'
    argv = ['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix=' + str(CAP / 'never_created_reader_cache'),
            str(PREP / 'inspect_p210_artifact.py'),'--expected-preparation-sha256',seal]
    source = QA / 'record_p210_artifact_03.py'
    need(shlex.split(launch['command']) == ['/usr/bin/python3.10','-I','-S','-B',str(source),
         '--expected-artifact-preparation-sha256',seal] and launch['cwd'] == str(ROOT) and
         completed['launch_record'] == 'P210_ARTIFACT03_ROOT_LAUNCH.actual.json', 'exact actual root command')
    need(result['argv'] == attempt['argv'] == argv and result['cwd'] == attempt['cwd'] == str(ROOT) and
         result['environment'] == attempt['environment'] == ENV and attempt['timeout_seconds'] == 1800 and
         attempt['start_new_session'] is True and attempt['inputs_before'] == result['inputs_before'] == result['inputs_after'] and
         result['inputs_unchanged'] is True and len(result['inputs_before']) == 11 and
         spawn['pid'] == spawn['process_group_id'] == result['pid'] and
         attempt['started_epoch'] <= spawn['spawned_epoch'] <= result['finished_epoch'] and
         not os.path.lexists(CAP / 'never_created_reader_cache'), 'complete actual recorder context and stable interval')
    for name, row in result['inputs_before'].items():
        need(pin(name) == row, 'all eleven direct recorder inputs')
    package(PREP, seal, 9)
    payloads = package(CAP, '0fc403270819cdb74c1d14a2aac39169af7ee7029e3c85a9f5f25aa082e11c7c', 6)
    need(raw(CAP / 'executed_source.py') == raw(source) and raw(CAP / 'stderr') == b'' and
         result['stdout'] == payloads['ARTIFACT_REPORT.json'] and result['stderr'] == payloads['stderr'], 'full source and raw dual stream pins')
    report = obj(CAP / 'ARTIFACT_REPORT.json')
    need(raw(CAP / 'ARTIFACT_REPORT.json') == json.dumps(report, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode() + b'\n', 'entire canonical original stdout')
    need(report['status'] == 'PASS_P210_TERMINAL_ARTIFACT_INITIAL_LIFECYCLE_FOLLOWUP_PENDING' and
         report['checks'] == sum(report['checks_by_kind'].values()) == 5838453 and report['paper'] == 'P210' and
         report['root_acceptance'] is report['paper_completion'] is report['five_paper_completion'] is False and
         all(report[k] == 0 for k in ('new_scientific_runs','new_builds','new_views','new_manuscript_reviews',
                                    'reader_file_writes','old_programs_imported_or_executed')), 'actual documentary-only gate scope')
    rec = report['complete_current_key_reconstruction']
    returned = dict(status='PASS_ACTUAL_P210_ARTIFACT_INITIAL_CAPTURE', output=str(CAP), original_wait_exit_code=0,
        stdout=result['stdout'], stderr=result['stderr'], result=pin(CAP / 'RESULT.json'), seal=pin(CAP / 'SHA256SUMS'),
        checks=report['checks'], current_path_keys=rec['complete_keys'], artifact_acceptance=False)
    need(completed['result']['output'] == json.dumps(returned, sort_keys=True) + '\n', 'whole actual native return')
    contract = obj(PREP / 'ACTUAL_BINDING.json')
    for name, expected in contract['named_input_pins'].items():
        need(pin(name) == expected, 'all190 bound original roles and failures')
    roles = obj(QA / 'p210_terminal_artifact_preparation/ACTUAL_ROLES.json')
    aliases = []
    def alias(logical, physical, expected, provenance):
        need(expected['real'] == logical and expected['symlink'] is None, 'original documentary metadata')
        need(pin(physical) == {'sha256':expected['sha256'],'bytes':expected['size']}, 'exact historical physical bytes')
        aliases.append(dict(logical=logical, original=expected, physical=physical,
                            physical_record=READS[physical], provenance=provenance))
    for row in roles['exact_available_historical_aliases']:
        alias(row['logical'], row['physical'], dict(real=row['logical'], sha256=row['original_sha256'],
              size=row['original_size'], symlink=None), row['provenance_role'])
    r2 = obj(PAPER / 'frozen_round2/ROUND2_PROVENANCE.json')
    for logical, row in roles['actual_b_final_map_recipe']['old_control_roles_requiring_actual_Round2_history'].items():
        anchor = r2['anchors']['PRE_ROUND2_' + Path(logical).name]
        need(anchor['original_path'] == logical and anchor['sha256'] == row['sha256'], 'actual R2 anchor source')
        alias(logical, str(PAPER / 'frozen_round2' / anchor['physical_path']), row, str(PAPER / 'frozen_round2/ROUND2_PROVENANCE.json'))
    preserved = QA / 'p210_preterminal_controls_01/PRESERVATION.actual.json'
    for logical, row in obj(preserved)['copies'].items():
        alias(logical, row['physical'], dict(real=logical, sha256=row['sha256'], size=row['bytes'], symlink=None), str(preserved))
    by_key = {(r['logical'],r['original']['sha256'],r['original']['size']):r for r in aliases}
    need(len(by_key) == 10 and [by_key[k] for k in sorted(by_key)] == rec['exact_historical_aliases'], 'all ten source-defined complete alias rows')
    def rebase(name, row):
        rich_schema(row)
        a = by_key.get((name,row['sha256'],row['size']))
        if a:
            need(a['original'] == row, 'entire original alias metadata retained')
            return a['physical'], a['physical_record']
        return name, row
    common = obj(roles['actual_b_final_map_recipe']['common_path'])
    need(common == obj(QA.parent / 'reviews/p210_b/DELTA_INPUTS_AFTER.json.gz') and len(common) == 121013, 'entire B common interval')
    b = {}
    for name, row in common.items():
        need(set(row) == {'resolved','sha256','bytes','symlink'}, 'actual B original rich schema')
        b[name] = dict(real=row['resolved'],sha256=row['sha256'],size=row['bytes'],symlink=row['symlink'])
    b_native = obj(roles['actual_b_final_map_recipe']['root_completion'])
    need(b_native['result']['exit_code'] == 0, 'actual B root normal native')
    b_original = json.loads(b_native['result']['output'])
    b_extra = b_original['current_read_keys_outside_B_common']
    need(len(b_extra) == 44 and not set(b) & set(b_extra), 'B original disjoint extras before union')
    b.update(b_extra)
    need(canonical(b) == {'sha256':rec['b_final_basis']['canonical_sha256'],'bytes':rec['b_final_basis']['canonical_bytes']} and
         len(b) == 121057 and rec['b_final_basis'] == roles['actual_b_final_map_recipe'], 'complete original B map canonical fields')
    terminal_path = QA / 'p210_terminal_root_reception_01/ROOT_RECEPTION.json'
    terminal = obj(terminal_path)
    basis = rec['terminal_receiver_basis']
    need(basis['path'] == str(terminal_path) and basis['pin'] == pin(terminal_path) and basis['selector'] == ['current_key_reconstruction'], 'exact original terminal basis role')
    recipe = terminal['current_key_reconstruction']
    ledger = obj(recipe['known_ledger'])
    need(ledger == obj(PAPER / 'qa_final/KNOWN_INPUTS_AFTER.json.gz') and set(ledger) == {'runtime','configuration','tex'}, 'entire original terminal grouped interval')
    known = {}
    for rows in ledger.values():
        for name, row in rows.items():
            need(name not in known or known[name] == row, 'complete original spelling duplicates agree')
            known[name] = row
    need(len(known) == 123595 and len(recipe['extra_entries']) == 1904 and not set(known) & set(recipe['extra_entries']), 'terminal original disjoint union before any files projection')
    term = known | recipe['extra_entries']
    need(len(term) == 125499 and canonical(term) == recipe['complete_map'] == basis['original_map'], 'entire terminal original presence-rich map')
    files, nonfiles = {}, {}
    for name, row in term.items():
        if row['is_file']:
            files[name] = dict(real=row['resolved'],sha256=row['sha256'],size=row['bytes'],symlink=row['link'] if row['symlink'] else None)
        else:
            nonfiles[name] = row
    need(nonfiles == rec['nonfile_presence_roles'] and len(nonfiles) == rec['nonfile_presence_count'] == 5271, 'all original nonfile roles retained separately')
    union = {}
    for group in (b,files):
        for name, value in group.items():
            target, row = rebase(name,value)
            need(target not in union or union[target] == row, 'full rebased physical duplicate equality')
            union[target] = row
    need(len(union) == rec['base_union_keys'] == 121899 and canonical(union) == rec['base_union_canonical'], 'complete independent two-basis current union')
    extra = rec['extra_current_keys']
    need(len(extra) == rec['extra_count'] == 250 and not set(union) & set(extra), 'exact current extras disjoint before union')
    full = union | extra
    need(len(full) == rec['complete_keys'] == 122149 and canonical(full) == rec['canonical_map'], 'entire current rich-map canonical bytes')
    for name, row in extra.items():
        raw(name)
        need(READS[name] == rich_schema(row), 'all250 current extra bytes and metadata')
    for name, row in nonfiles.items():
        p = Path(name)
        current = dict(exists=p.exists(),symlink=p.is_symlink(),link=str(p.readlink()) if p.is_symlink() else None,
                       resolved=str(p.resolve()),is_file=p.is_file(),is_dir=p.is_dir())
        need(current == row, 'all5271 current nonfile presence roles')
    runtime = report['current_reader_runtime']
    need(runtime['argv'] == argv and runtime['cwd'] == str(ROOT) and runtime['environment'] == ENV and
         dp(runtime['raw_maps'].encode()) == {'sha256':runtime['raw_maps_sha256'],'bytes':runtime['raw_maps_bytes']}, 'full actual sampled runtime context/raw maps')
    mapped = {str(Path(line.split(maxsplit=5)[5]).resolve()) for line in runtime['raw_maps'].splitlines()
              if len(line.split(maxsplit=5)) == 6 and line.split(maxsplit=5)[5].startswith('/')}
    need(mapped == set(runtime['mapped_files']), 'entire raw maps selected file names')
    for name, value in runtime['modules'].items():
        need(full[value['path']] == {k:v for k,v in value.items() if k != 'path'}, 'all actual module full fields bound')
    for name, row in runtime['mapped_files'].items():
        need(full[name] == row, 'all actual mapping full fields bound')
    need(report['physical_frozen_payloads'] == [493,508,524] and report['physical_frozen_link_roles'] == [57,71,86] and
         [(r['role'],r['checks_each']) for r in report['actual_strict_pairs_reused']] ==
         [('author',[197471,197471]),('a',[133978,133978]),('b',[51129,51129])] and
         all(r['current_open'] == 0 for r in report['accepted_reviews'].values()) and
         report['actual_terminal_reused']['reused_terminal_builds'] == 2 and
         report['actual_root_terminal_and_view_binding']['actual_six_root_views']['pages_actually_viewed_by_root'] == 6,
         'exact original review/pair/freeze/build/view scope')
    views = obj(QA / 'P210_TERMINAL_ROOT_VIEWS.actual.json')
    need(views['status'] == 'ROOT_ACTUALLY_VIEWED_ALL_SIX_FINAL_PAGES_PASS' and views['open_visual_findings'] == 0,
         'actual root views not a new view')
    before = dict(READS)
    for name, row in before.items():
        raw(name)
        need(READS[name] == row, 'all original-reception direct inputs stable')
    need(READS == before, 'no extra source read after final closure')
    print(json.dumps(dict(status='PASS_ROOT_P210_INITIAL_ARTIFACT_ORIGINALS_AND_COMPLETE_MAP',checks=CHECKS,
        initial_gate_checks=report['checks'],current_file_keys=len(full),base_union_keys=len(union),current_extras=len(extra),
        nonfile_presence_roles=len(nonfiles),complete_current_map=rec['canonical_map'],original_B_keys=len(b),
        original_terminal_presence_keys=len(term),exact_aliases=len(aliases),direct_original_reception_paths=len(READS),
        direct_current_map=canonical(READS),artifact_raw=pin(CAP / 'ARTIFACT_REPORT.json'),artifact_seal=pin(CAP / 'SHA256SUMS'),
        actual_native_session=16560,actual_native_exit=0,new_whole_host_content_passes=0,new_scientific_runs=0,new_builds=0,new_views=0,
        scope='Complete original metadata map reconstruction; actual just-completed reader supplies full122149 double content read and source-defined membership. Root independently rehashes all direct/extras and checks5271 nonfile roles.',
        paper_completion=False,five_paper_completion=False,external='OWNER_AMBER / HOLD_EXTERNAL'),sort_keys=True))

if __name__ == '__main__':
    main()
