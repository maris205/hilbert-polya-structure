#!/usr/bin/env python3
"""Root original reception: full map algebra, actual native/raw evidence.

The just-completed exact-five gate supplies both whole-host content passes.
This receiver recomposes every reported rich row from its three full bases,
rehashes all new extras and its direct inputs, and checks current path metadata.
It does not execute a scientific program, builder, viewer or old auditor.
"""
import ast
from collections import Counter
from hashlib import sha256
import gzip
import importlib.util
import json
import os
from pathlib import Path
import re
import shlex
import types

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PREP = QA / 'five_paper_terminal_exact_revision_02'
OUT = QA / 'five_paper_terminal_exact_run_02'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
HISTORY = QA / 'p210_precompletion_controls_01'
# Bound only after the actual revised preparation and native execution exist.
SEAL = 'ae2ad7e13909ad439e75329d26ff7bc95f0bc5d61fea0e224911584fef9799cc'
PREP_PAYLOADS = 10
FIXED_INPUTS = 71
NATIVE_SESSION = 20030
ENV = dict(PATH='/usr/bin:/bin', LANG='C.UTF-8', LC_ALL='C.UTF-8', TZ='UTC')
IDS = ['P205', 'P207', 'P208', 'P209', 'P210']
READS, COUNTS = {}, Counter()

def need(ok, label, detail=None):
    COUNTS[label] += 1
    if not ok:
        raise AssertionError((label, detail))

def bytes_key(data):
    return dict(bytes=len(data), sha256=sha256(data).hexdigest())

def canonical(value, lf=False):
    return bytes_key((json.dumps(value, sort_keys=True, separators=(',', ':')) + ('\n' if lf else '')).encode())

def rich_schema(v):
    need(set(v) == {'real', 'size', 'sha256', 'symlink'} and Path(v['real']).is_absolute() and
         type(v['size']) is int and v['size'] >= 0 and re.fullmatch('[0-9a-f]{64}', v['sha256']) and
         (v['symlink'] is None or type(v['symlink']) is str), 'full four-field file schema')

def pin(path, expected=None):
    p = Path(path)
    need(p.is_absolute() and p.is_file(), 'direct absolute file')
    h, size = sha256(), 0
    with p.open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block); size += len(block)
    row = dict(real=str(p.resolve()), size=size, sha256=h.hexdigest(),
               symlink=os.readlink(p) if p.is_symlink() else None)
    need(str(p) not in READS or READS[str(p)] == row, 'direct complete key stable', str(p))
    READS[str(p)] = row
    if expected is not None:
        if type(expected) is str:
            need(row['sha256'] == expected, 'direct exact hash')
        else:
            need((row if set(expected) == set(row) else dict(bytes=size, sha256=row['sha256'])) == expected,
                 'direct entire expected record', str(p))
    return row

def byte_pin(path):
    v = pin(path)
    return dict(bytes=v['size'], sha256=v['sha256'])

def raw(path):
    v = byte_pin(path); data = Path(path).read_bytes()
    need(bytes_key(data) == v, 'complete direct raw read stable', str(path))
    return data

def obj(path):
    data = raw(path)
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)

def package(base, count):
    rows = {}
    for line in raw(base / 'SHA256SUMS').decode().splitlines():
        h, n = line.split('  ', 1)
        need(re.fullmatch('[0-9a-f]{64}', h) and Path(n).name == n and n not in rows, 'strict shallow nonself row')
        rows[n] = h; pin(base / n, h)
    need(len(rows) == count and {p.name for p in base.iterdir()} == set(rows) | {'SHA256SUMS'} and
         all(p.is_file() and not p.is_symlink() for p in base.iterdir()), 'complete shallow physical package')
    return set(rows) | {'SHA256SUMS'}

def four_names():
    # Exactly the sealed metadata selector, not its incomplete rich/partial statistics.
    probe = QA / 'five_four_key_reconstruction_preparation/probe.py'
    source = raw(probe)
    need(bytes_key(source) == dict(bytes=9505, sha256='3665507daace69ce2b12a916316b31b4dd72a44cdc0123a5ff0adfc7c4599a42'),
         'exact original pure-metadata selection source')
    body = source.decode()
    replacements = {
        'def J(p):return json.loads(A(p).read_bytes())': 'def J(p):return json.loads(ROOT_RECEPTION_RAW(A(p)))',
        'physical.read_text()': 'ROOT_RECEPTION_RAW(physical).decode()',
        "(rv/'INPUT_PINS.sha256').read_text()": "ROOT_RECEPTION_RAW(rv/'INPUT_PINS.sha256').decode()",
        'z.read_bytes()': 'ROOT_RECEPTION_RAW(z)',
        'physical.read_bytes()': 'ROOT_RECEPTION_RAW(physical)',
    }
    for old, new in replacements.items():
        need(body.count(old) == 1, 'exact metadata-only measured-read instrumentation')
        body = body.replace(old, new)
    tree = ast.parse(body)
    need(isinstance(tree.body[-1], ast.Expr) and isinstance(tree.body[-1].value, ast.Call) and
         isinstance(tree.body[-1].value.func, ast.Name) and tree.body[-1].value.func.id == 'print' and
         tree.body[-1].lineno == 156, 'remove only old metadata summary print')
    tree.body.pop()
    namespace = {'__name__': 'root_four_name_metadata', 'ROOT_RECEPTION_RAW': raw}
    exec(compile(tree, str(probe), 'exec'), namespace)
    names = namespace['names']
    need(len(names) == 142784, 'complete original four lexical selection')
    return names

def merge(*groups):
    result = {}
    for group in groups:
        for name, row in group.items():
            rich_schema(row)
            need(name not in result or result[name] == row, 'entire overlapping rich row equality', name)
            result[name] = row
    return result

def main():
    need(type(SEAL) is str and re.fullmatch('[0-9a-f]{64}', SEAL) and
         all(type(v) is int and v > 0 for v in (PREP_PAYLOADS, FIXED_INPUTS, NATIVE_SESSION)),
         'actual revision and native constants bound before reception')
    launch = obj(QA / 'FIVE_EXACT02_ROOT_LAUNCH.actual.json')
    done = obj(QA / 'FIVE_EXACT02_ROOT_COMPLETION.actual.json')
    need(launch['cwd'] == str(ROOT) and launch['result']['output'] == '' and 'exit_code' not in launch['result'] and
         launch['result']['session_id'] == done['session_id'] == NATIVE_SESSION and
         done['result']['exit_code'] == 0 and 'session_id' not in done['result'] and
         done['launch_record'] == 'FIVE_EXACT02_ROOT_LAUNCH.actual.json' and
         shlex.split(launch['command']) == ['/usr/bin/python3.10', '-I', '-S', '-B',
             str(QA / 'record_five_terminal_exact_02.py'), '--expected-five-preparation-sha256', SEAL],
         'actual normal native closure before output seal')
    result, attempt, spawn = (obj(OUT / n) for n in ('RESULT.json', 'ATTEMPT.json', 'SPAWN.json'))
    argv = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(OUT / 'never_created_reader_cache'),
            str(PREP / 'inspect_five.py'), '--expected-preparation-sha256', SEAL]
    need(result['argv'] == argv and result['cwd'] == str(ROOT) and result['environment'] == ENV and
         result['original_wait_exit_code'] == result['cleanup_wait_exit_code'] == 0 and
         result['timed_out'] is False and result['wait_error'] is None and result['cleanup_events'] == [] and
         result['child_reaped'] is result['process_group_absent'] is result['inputs_unchanged'] is
         result['all_five_terminal_evidence_present_after'] is True and result['inputs_before'] == result['inputs_after'],
         'original normal wait and settled unchanged-input capture')
    need(attempt == dict(argv=argv, cwd=str(ROOT), environment=ENV, inputs_before=result['inputs_before'],
         timeout_seconds=1800, start_new_session=True, started_epoch=attempt['started_epoch'],
         all_five_terminal_evidence_present_before=True) and
         spawn == dict(pid=result['pid'], process_group_id=result['pid'], spawned_epoch=spawn['spawned_epoch']) and
         type(result['pid']) is int and result['pid'] > 0 and
         attempt['started_epoch'] <= spawn['spawned_epoch'] <= result['finished_epoch'] and
         not os.path.lexists(OUT / 'never_created_reader_cache'), 'entire attempt, spawn and chronology')
    try:
        os.killpg(result['pid'], 0)
    except ProcessLookupError:
        pass
    else:
        raise AssertionError('owned group currently present')
    prep_names, out_names = package(PREP, PREP_PAYLOADS), package(OUT, 6)
    pin(PREP / 'SHA256SUMS', SEAL)
    binding = obj(PREP / 'ACTUAL_BINDING.json')
    need(binding['schema'] == 'actual-exact-five-preparation-binding-v1' and
         len(binding['fixed_inputs']) == FIXED_INPUTS, 'all fixed actual preparation originals')
    for name, row in binding['fixed_inputs'].items():
        pin(name, row)
    for name, row in result['inputs_before'].items():
        pin(name, row)
    expected_recorder_inputs = {str(PREP / n) for n in prep_names} | {
        str(QA / 'record_five_terminal_exact_02.py'),
        str(QA / 'batch_terminal_builds_01/SHA256SUMS'),
        str(ROOT / 'papers/208-original-snapshot-triangulation-sweeps/qa_final/SHA256SUMS'),
        str(ROOT / 'papers/209-ordered-fibre-threading/qa_final/SHA256SUMS'),
        str(PAPER / 'qa_final/SHA256SUMS'), str(ROOT / 'SYMBOLIC_DYNAMICS_STATE.md'),
        str(QA.parent / 'PIPELINE_STATE.md'), str(QA.parent / 'FINAL_THEOREM_CONTRACTS.md'),
        str(QA / 'P210_LIFECYCLE_ROOT_ACCEPTANCE.actual.json'), '/usr/bin/python3.10'}
    need(len(result['inputs_before']) == PREP_PAYLOADS + 11 and
         set(result['inputs_before']) == expected_recorder_inputs, 'entire exact source-defined recorder input scope')
    need(raw(OUT / 'executed_source.py') == raw(QA / 'record_five_terminal_exact_02.py') and
         raw(OUT / 'stderr') == b'' and byte_pin(OUT / 'stderr') == result['stderr'], 'complete original recorder and empty separate stderr')
    data = raw(OUT / 'FIVE_REPORT.json'); report = json.loads(data)
    need(bytes_key(data) == result['stdout'] and len(data) < 100000000 and
         data == (json.dumps(report, sort_keys=True, separators=(',', ':')) + '\n').encode(), 'entire actual canonical stdout')
    need(report['schema'] == 'exact-five-current-rich-key-gate-v1' and report['status'] == 'PASS_EXACT_FIVE_GATE_ROOT_ACCEPTANCE_PENDING' and
         report['papers'] == IDS and report['retained_papers'] == report['individually_root_accepted_papers'] == 5 and
         report['current_open_findings'] == 0 and report['reused_strict_author_A_B_pairs'] == 15 and
         report['reused_terminal_source_only_builds'] == 10 and report['reused_actual_prior_root_page_views'] == 27 and
         report['complete_current_rich_file_reads'] == 2 and report['root_acceptance'] is report['five_paper_completion'] is False and
         report['external'] == 'OWNER_AMBER / HOLD_EXTERNAL' and all(report[n] == 0 for n in ('new_scientific_runs',
         'new_builds', 'new_views', 'new_manuscript_reviews', 'reader_file_writes', 'old_auditors_or_writers_imported_or_executed')) and
         report['checks'] == report['new_driver_checks'] + report['copied_four_checks'] and
         report['new_driver_checks'] == sum(report['new_driver_checks_by_kind'].values()), 'entire bounded five-paper scope')
    summary = dict(status='PASS_ACTUAL_EXACT_FIVE_CAPTURE', output=str(OUT), original_wait_exit_code=0,
        stdout=result['stdout'], stderr=result['stderr'], result=byte_pin(OUT / 'RESULT.json'), seal=byte_pin(OUT / 'SHA256SUMS'),
        checks=report['checks'], current_path_keys=report['complete_current_file_keys'], root_acceptance=False, five_paper_completion=False)
    need(done['result']['output'] == json.dumps(summary, sort_keys=True) + '\n', 'entire actual native stdout')
    full, recipe = report['complete_current_read_keys'], report['current_key_reconstruction']
    need(len(full) == report['complete_current_file_keys'] == recipe['complete_keys'] and
         canonical(full) == report['complete_current_file_map'] == recipe['complete_map'], 'every field in full reported current map')
    names = four_names(); four_aliases = recipe['original_four']['exact_post_digest_rebases']
    historical = {}
    expected_four_roles = [
        ('FINAL_THEOREM_CONTRACTS.md', 28714, '329cb32f4764dd59b1a500a8c21ef7dd4b2d83c87dd781d9934a413142f2a914'),
        ('PIPELINE_STATE.md', 94487, '592b60ef55cc39f1efdf8c81459beff8e55c9d86bce0e2eb0213aeafdb1d595d'),
    ]
    need(len(four_aliases) == 2, 'exactly two four historical documentary roles')
    for fa, (basename, size, digest) in zip(four_aliases, expected_four_roles):
        logical = str(QA.parent / basename); physical = str(QA / 'central_round2_p210' / basename)
        need(logical in names and physical not in names and fa['logical'] == logical and fa['physical'] == physical and
             fa['original'] == dict(real=logical, size=size, sha256=digest, symlink=None) and
             pin(physical) == fa['physical_record'] == full[physical] == {**fa['original'], 'real': physical},
             'exact historical four documentary original and physical bytes', basename)
        historical[logical] = fa['original']
    old_four = {name: dict(resolved=v['real'], bytes=v['size'], sha256=v['sha256'], symlink=v['symlink'])
                for name in names for v in [historical[name] if name in historical else full[name]]}
    need(canonical(old_four, True)['sha256'] == recipe['original_four']['original_compact_LF_sha256'] ==
         '087b90f42ad1a55fef4daa2acb29cee4fca614736c862aa9aed5e2a65d628dc0', 'entire original142784 four rich fields and original LF canonical')
    four_result = report['reconstructed_four_result']
    need(four_result['papers_checked'] == IDS[:4] and four_result['current_valid_author_A_B_pairs'] == 12 and
         four_result['current_valid_source_only_builds'] == 8 and four_result['actual_prior_page_attestations_bound'] == 21 and
         four_result['current_file_keys_reread'] == 142784 and
         four_result['current_file_key_sha256'] == canonical(old_four, True)['sha256'],
         'complete four reconstructed result retains original scope')
    current_four = {name: full[name] for name in names if name not in historical}
    for fa in four_aliases:
        current_four[fa['physical']] = full[fa['physical']]
    need(len(current_four) == recipe['original_four']['current_keys'] and
         canonical(current_four) == recipe['original_four']['current_map'], 'complete rebased four map')
    # Newly written, source-read pure metadata helper; import alone has no execution side effects.
    helper = PREP / 'p210_reconstruction.py'; pin(helper, 'e9987d48cbf7ac5fcab1b672ec1ebd08180617536cd4961aa5eba09d6f9e411b')
    spec = importlib.util.spec_from_file_location('root_p210_metadata', helper)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    callbacks = types.SimpleNamespace(need=need, obj=obj, pin=pin, byte_pin=byte_pin, canonical=canonical,
                                    rich_schema=rich_schema, bytes_key=bytes_key)
    initial, nonfiles, initial_report, ledger, p210_recipe = module.reconstruct(callbacks)
    need(p210_recipe == recipe['original_P210'], 'entire P210 original source recipe')
    current_p210 = dict(initial)
    for row in recipe['exact_post_initial_digest_P210_rebases']:
        name, target = row['logical'], row['physical']
        need(name in {str(PAPER / n) for n in ('ROOT_LIFECYCLE.md', 'PAPER_MANIFEST.sha256')} and
             target == str(HISTORY / Path(name).name) and current_p210.pop(name) == row['original'] and
             pin(target) == row['physical_record'] == {**row['original'], 'real': target},
             'exact post-initial P210 role and unchanged original physical bytes')
        need(target not in current_p210 or current_p210[target] == row['physical_record'], 'P210 rebase collision equality')
        current_p210[target] = row['physical_record']
    need(len(recipe['exact_post_initial_digest_P210_rebases']) == 2 and len(current_p210) == recipe['rebased_P210_keys'] and
         canonical(current_p210) == recipe['rebased_P210_map'], 'entire P210 map after two exact aliases')
    life_path = QA / 'p210_terminal_lifecycle_01/LIFECYCLE_REPORT.json'; life = obj(life_path)['complete_current_read_keys']
    need(recipe['actual_lifecycle'] == dict(source=str(life_path), source_pin=byte_pin(life_path),
         selector=['complete_current_read_keys'], keys=len(life), complete_map=canonical(life)) and len(life) == 2319,
         'entire lifecycle original rich map recipe')
    base = merge(current_four, current_p210, life); extra = recipe['extra_current_keys']
    need(len(base) == recipe['base_keys'] and canonical(base) == recipe['base_map'] and
         len(extra) == recipe['extra_count'] and not set(base) & set(extra) and merge(base, extra) == full,
         'complete three-base union plus disjoint extras equals every full current row')
    for name, row in full.items():
        rich_schema(row); p = Path(name)
        need(p.is_file() and p.stat().st_size == row['size'] and str(p.resolve()) == row['real'] and
             (os.readlink(p) if p.is_symlink() else None) == row['symlink'], 'all reported current pathname metadata, not a third content pass')
    for name, row in extra.items():
        pin(name, row)
    for phase in ('before', 'after'):
        runtime = report['current_runtime_' + phase]
        need(bytes_key(runtime['raw_maps'].encode()) == runtime['raw_maps_pin'], 'entire actual runtime maps text')
        for row in runtime['modules'].values():
            need(full[row['path']] == {k: v for k, v in row.items() if k != 'path'}, 'all sampled module full fields')
        for name, row in runtime['mapped_files'].items():
            need(full[name] == row, 'all sampled mapped-file full fields')
    need(report['current_runtime_before']['modules'] == report['current_runtime_after']['modules'] and
         report['current_runtime_before']['mapped_files'] == report['current_runtime_after']['mapped_files'], 'actual runtime interval equality')
    fixed = dict(READS)
    for name, row in fixed.items():
        pin(name, row)
    need(package(PREP, PREP_PAYLOADS) == prep_names and package(OUT, 6) == out_names, 'final complete capture/preparation membership')
    for name, row in READS.items():
        if name in full:
            need(full[name] == row, 'all directly rehashed overlapping inputs equal the reported entire rich row', name)
    print(json.dumps(dict(status='PASS_ROOT_EXACT_FIVE_ORIGINALS_AND_COMPLETE_CURRENT_MAP',
        native_session=NATIVE_SESSION, native_exit=0, checks=sum(COUNTS.values()), gate_checks=report['checks'],
        direct_paths=len(READS), complete_current_keys=len(full), complete_current_map=canonical(full),
        original_four_keys=len(old_four), original_four_LF_sha256=canonical(old_four, True)['sha256'],
        original_P210_keys=len(initial), current_lifecycle_keys=len(life), extras_rehashed=len(extra),
        full_raw=bytes_key(data), output_seal=byte_pin(OUT / 'SHA256SUMS'),
        additional_whole_host_content_passes=0, reused_pairs=15, reused_builds=10, reused_actual_views=27,
        new_science=0, new_builds=0, new_views=0, external='OWNER_AMBER / HOLD_EXTERNAL'), sort_keys=True))

if __name__ == '__main__':
    main()
