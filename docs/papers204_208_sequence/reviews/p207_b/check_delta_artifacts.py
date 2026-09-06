#!/usr/bin/env python3
"""Read-only exact-no-change B delta audit; never runs mathematical code.

Historical package paths FINDINGS.json, BUILD_REPORT.md and SHA256SUMS
resolve to preserved initial aliases. REPORT.md stays unchanged and also
has an exact alias. The sole build-report warning correction is explicit.
All subprocess output below is from actual read-only hash/byte checks.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys


BASE = Path(__file__).resolve().parents[4]
B = BASE / 'docs/papers204_208_sequence/reviews/p207_b'
PAPER = BASE / 'papers/207-upper-neighbor-rank-dynamics'
FREEZE = PAPER / 'frozen_round1'
REPLAY = BASE / 'docs/papers204_208_sequence/qa/root_replays/p207_b_controlled'
RESPONSE = BASE / 'docs/papers204_208_sequence/P207_B_RESPONSE.md'
SUPPLEMENT = BASE / 'docs/papers204_208_sequence/P207_B_RESPONSE_SUPPLEMENT.md'
UTILITY = BASE / 'docs/papers204_208_sequence/qa/replay_p207_review.py'
UTILITY_AUDIT = BASE / 'docs/papers204_208_sequence/qa/P207_B_INITIAL_ARTIFACT_AUDIT.md'
UTILITY_EVIDENCE = BASE / 'docs/papers204_208_sequence/qa/p207_b_artifact_audit'
INITIAL_MANIFEST = '6f103d933c8135563b00734d8850ce36bf2fc47aa504d669e01cf6c99ef29074'
RESPONSE_HASH = 'd1e3f7b0ede25f375269ebedaa84c12558f7055322dfe905379974e05dbd3244'
SUPPLEMENT_HASH = 'a3e3c2a36388291240f12055d44a2a4c281b3ee94800b76fa20e87124c874294'
FREEZE_HASH = '8d134689f8c07f9bcac65b4576a5bfca2e073ece6281f9d893148f12adb43f5d'
CANONICAL_HASH = 'b7206f01180dcbe5eca24dbaec67cc96ae5dc80f86004455d382e7723c786fda'
CHECKS = 0
CONSUMED = {}
COMMANDS = []


def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def info(raw):
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}


def read(path):
    path = path.resolve()
    raw = path.read_bytes()
    key = str(path.relative_to(BASE)) if BASE in path.parents else str(path)
    entry = info(raw)
    if key in CONSUMED:
        check(CONSUMED[key] == entry, 'changed during consumption: ' + key)
    CONSUMED[key] = entry
    return raw


def pins(path):
    rows = []
    for line in read(path).decode().splitlines():
        digest, name = line.split('  ', 1)
        rel = Path(name)
        check(len(digest) == 64 and all(c in '0123456789abcdef' for c in digest), 'bad digest')
        check(not rel.is_absolute() and '..' not in rel.parts, 'bad relative path')
        rows.append((name, digest))
    check(len(rows) == len(dict(rows)), 'duplicate pin path')
    return rows


def verify_rows(rows, base, aliases=None):
    aliases = aliases or {}
    for name, digest in rows:
        path = base / aliases.get(name, name)
        check(info(read(path))['sha256'] == digest, 'pin mismatch: ' + str(path))


def execute(command, cwd, expected_exit=0):
    child = subprocess.run(command, cwd=cwd, capture_output=True)
    COMMANDS.append({'command': command, 'cwd': str(cwd), 'exit': child.returncode,
                     'stdout': child.stdout.decode(), 'stderr': child.stderr.decode(),
                     'expected_exit': expected_exit})
    check(child.returncode == expected_exit and not child.stderr, 'actual command failed: ' + str(command))
    return child.stdout


def main():
    check(sys.flags.optimize == 0 and __debug__, 'assertions disabled')
    check(info(read(RESPONSE))['sha256'] == RESPONSE_HASH, 'wrong actual response')
    check(info(read(SUPPLEMENT))['sha256'] == SUPPLEMENT_HASH, 'wrong actual response supplement')
    initial = pins(B / 'SHA256SUMS.initial')
    check(len(initial) == 118, 'wrong initial payload census')
    check(info(read(B / 'SHA256SUMS.initial'))['sha256'] == INITIAL_MANIFEST, 'initial seal changed')
    aliases = {'FINDINGS.json': 'FINDINGS.initial.json', 'BUILD_REPORT.md':'BUILD_REPORT.initial.md'}
    verify_rows(initial, B, aliases)
    check(read(B / 'REPORT.md') == read(B / 'REPORT.initial.md'), 'initial report changed')
    initial_findings = json.loads(read(B / 'FINDINGS.initial.json'))
    check(initial_findings['accepted_delta'] is False and not initial_findings['findings'], 'not initial finding record')
    freeze_rows = pins(FREEZE / 'SHA256SUMS')
    check(len(freeze_rows) == 105, 'wrong freeze payload census')
    check(info(read(FREEZE / 'SHA256SUMS'))['sha256'] == FREEZE_HASH, 'wrong frozen manifest')
    actual_freeze = {str(p.relative_to(FREEZE)) for p in FREEZE.rglob('*') if p.is_file()}
    check(actual_freeze == set(dict(freeze_rows)) | {'SHA256SUMS'}, 'freeze has missing/extra files')
    verify_rows(freeze_rows, FREEZE)
    verify_rows(freeze_rows, PAPER)
    freeze_pins = pins(B / 'INPUT_PINS.sha256')
    check(len(freeze_pins) == 106, 'wrong initial freeze pins')
    check(set(dict(freeze_pins)) == {str((FREEZE / n).relative_to(BASE)) for n in actual_freeze}, 'freeze pin paths incomplete')
    verify_rows(freeze_pins, BASE)
    check(pins(B/'INPUT_PINS.after.sha256') == freeze_pins, 'after freeze pins differ')
    live_rows = pins(B/'LIVE_SCIENTIFIC_PINS.after.sha256')
    check(live_rows == [(str((PAPER/n).relative_to(BASE)), digest) for n,digest in freeze_rows], 'live after pins differ')
    verify_rows(live_rows, BASE)
    groups = {}
    for name, count in [('CONTEXT_PINS.sha256', 144), ('SUPPLEMENTAL_READ_PINS.sha256', 7), ('PAGE_VIEW_PINS.sha256', 7)]:
        rows = pins(B / name)
        check(len(rows) == count, 'wrong context count: ' + name)
        verify_rows(rows, BASE)
        groups[name] = rows
    check(pins(B/'CONTEXT_PINS.after.sha256') == groups['CONTEXT_PINS.sha256'], 'after context pins differ')
    check(pins(B/'SUPPLEMENTAL_READ_PINS.after.sha256') == groups['SUPPLEMENTAL_READ_PINS.sha256'], 'after supplementary pins differ')
    verify_rows(pins(B / 'cold_build_01/SOURCE_INPUTS.sha256'), B / 'cold_build_01')
    receipt = json.loads(read(REPLAY / 'RECEIPT.json'))
    check(receipt['pass'] is True and receipt['failure'] is None and receipt['package_unchanged'] is True, 'root receipt failed')
    check(receipt['review'] == str(B), 'wrong review path')
    check(receipt['structural_checks'] == {'complete_nonself_package_entries': 118, 'exact_freeze_inputs': 106}, 'wrong root structural census')
    snapshot = receipt['before_package_files']
    check(snapshot == receipt['after_package_files'] and len(snapshot) == 119, 'root snapshots unequal')
    check(set(snapshot) == set(dict(initial)) | {'SHA256SUMS'}, 'root original inventory mismatch')
    historical_aliases = {'FINDINGS.json': 'FINDINGS.initial.json', 'SHA256SUMS': 'SHA256SUMS.initial',
                          'BUILD_REPORT.md': 'BUILD_REPORT.initial.md'}
    for name, expected in snapshot.items():
        check(info(read(B / historical_aliases.get(name, name))) == expected, 'root snapshot differs: ' + name)
    check(info(read(REPLAY / 'harness_input.py')) == receipt['harness'], 'root harness pin differs')
    check(read(UTILITY) == read(REPLAY / 'harness_input.py'), 'live/copied root utility differs')
    check(info(read(Path(receipt['python']['executable']))) == receipt['python']['file'], 'runtime binary differs')
    check(receipt['python_flags'] == ['-I', '-B'], 'wrong recorded flags')
    check(receipt['environment_overrides'] == {'LC_ALL':'C', 'PYTHONDONTWRITEBYTECODE':'1', 'PYTHONHASHSEED':'0', 'PYTHONSAFEPATH':'1', 'TZ':'UTC'}, 'wrong overrides')
    check(read(REPLAY / 'verify.py') == read(B / 'verify.py'), 'root verifier differs')
    canonical = read(B / 'CANONICAL.json')
    check(info(canonical) == {'sha256': CANONICAL_HASH, 'bytes': 1558382}, 'wrong canonical')
    check(read(REPLAY / 'CANONICAL.json') == canonical, 'root canonical differs')
    stems = ['SHA256SUMS.before', 'INPUT_PINS.sha256.before', 'CONTEXT_PINS.sha256.before',
             'python_version', 'python_runtime_flags', 'python_link_dependencies', 'run1',
             'run1.cmp', 'run2', 'run2.cmp', 'pair.cmp', 'INPUT_PINS.sha256.after',
             'CONTEXT_PINS.sha256.after', 'SHA256SUMS.after']
    check(len(receipt['commands']) == len(stems) == 14, 'wrong root command census')
    expected_pins = {'SHA256SUMS': initial, 'INPUT_PINS.sha256': freeze_pins,
                     'CONTEXT_PINS.sha256': groups['CONTEXT_PINS.sha256']}
    for row, stem in zip(receipt['commands'], stems):
        stdout = read(REPLAY / (stem + '.stdout'))
        stderr = read(REPLAY / (stem + '.stderr'))
        check(row['exit'] == 0 and not stderr, 'root command failed: ' + stem)
        check(row['stdout'] == info(stdout) and row['stderr'] == info(stderr), 'root raw stream mismatch')
        if stem.endswith(('.before', '.after')):
            name = stem.rsplit('.', 1)[0]
            expected_stdout = ''.join(n + ': OK\n' for n, _ in expected_pins[name]).encode()
            check(stdout == expected_stdout, 'root pin output incomplete')
            check(row['command'] == ['sha256sum', '-c', str(B / name)], 'wrong root pin command')
            check(row['cwd'] == str(B if name == 'SHA256SUMS' else BASE), 'wrong root pin cwd')
        else:
            check(row['cwd'] == str(REPLAY), 'wrong root command cwd')
        if stem in ('run1', 'run2'):
            check(row['command'] == [receipt['python']['executable'], '-I', '-B', str(REPLAY / 'verify.py')], 'wrong actual producer command')
            parsed = json.loads(stdout)
            check(parsed['assertions'] == 2158999 and parsed['status'] == 'PASS', 'wrong root math result')
            check(stdout == canonical, 'root output not raw canonical')
        if stem.endswith('.cmp'):
            left, right = ((REPLAY / 'run1.stdout', REPLAY / 'run2.stdout') if stem == 'pair.cmp'
                           else (REPLAY / 'CANONICAL.json', REPLAY / (stem.split('.')[0] + '.stdout')))
            check(row['command'] == ['cmp', str(left), str(right)] and not stdout, 'wrong root byte comparison')
    flags = json.loads(read(REPLAY / 'python_runtime_flags.stdout'))
    check(flags == {'debug':True, 'ignore_environment':1, 'isolated':1, 'no_user_site':1, 'optimize':0}, 'root actual flags fail')
    check(receipt['commands'][3]['command'] == [receipt['python']['executable'], '-I', '-B', '--version'], 'version command differs')
    check(receipt['commands'][4]['command'][:4] == [receipt['python']['executable'], '-I', '-B', '-c'], 'probe command differs')
    check(receipt['commands'][5]['command'] == ['ldd', receipt['python']['executable']], 'ldd command differs')
    check(receipt['runs'] == [{'assertions':2158999, 'empty_stderr':True, 'label':label, 'producer_status':'PASS'} for label in ('run1','run2')], 'root run fields differ')
    for p in REPLAY.rglob('*'):
        if p.is_file():
            read(p)
    audit_present = UTILITY_AUDIT.is_file()
    check(audit_present, 'actual artifact assessor report not yet available')
    check(info(read(UTILITY_AUDIT))['sha256'] == 'a3c526e52635877a2de042bd40e1e0ce9e299588204af4495b35d5f00a13bef2', 'wrong closed assessor report')
    utility_rows = pins(UTILITY_EVIDENCE/'SHA256SUMS')
    check(len(utility_rows) == 7, 'wrong utility evidence census')
    verify_rows(utility_rows, UTILITY_EVIDENCE)
    supplement_rows = pins(UTILITY_EVIDENCE/'SUPPLEMENT_PINS.sha256')
    check(len(supplement_rows) == 3, 'wrong packaging supplement census')
    verify_rows(supplement_rows, UTILITY_EVIDENCE)
    check(set(dict(utility_rows)) | set(dict(supplement_rows)) | {'SHA256SUMS','SUPPLEMENT_PINS.sha256'} ==
          {p.name for p in UTILITY_EVIDENCE.iterdir() if p.is_file()}, 'initial plus supplemental utility seals incomplete')
    utility_raw = read(UTILITY_EVIDENCE/'attempt_03.stdout.json')
    check(info(utility_raw)['sha256'] == '457e3da885163d5888a95aa165f34e53580a687c63ada34d43f2568cb4ec46aa', 'wrong complete utility output')
    utility_result = json.loads(utility_raw)
    check(utility_result['status'] == 'INITIAL_ARTIFACT_MINOR_FINDING_REQUIRES_DOCUMENTARY_DELTA', 'initial artifact finding was erased')
    check(utility_result['checks'] == sum(utility_result['checks_by_section'].values()) == 39623, 'utility check census differs')
    check(len(utility_result['artifact_findings']) == 1 and utility_result['artifact_findings'][0]['id'] == 'P207-B-ART1'
          and utility_result['artifact_findings'][0]['status'] == 'OPEN_ON_EXACT_INITIAL_PACKAGE', 'wrong actual initial finding')
    utility_consumed = utility_result['all_consumed_inputs_before_after']
    check(len(utility_consumed) == utility_result['consumed_objects'] == 599, 'utility referent census differs')
    utility_aliases = {str((B/name).relative_to(BASE)):str((B/alias).relative_to(BASE)) for name,alias in historical_aliases.items()}
    utility_aliases[str((B/'check_delta_artifacts.py').relative_to(BASE))] = str((B/'check_delta_artifacts.initial.py').relative_to(BASE))
    check(info(read(B/'check_delta_artifacts.initial.py')) == {'bytes':11515,'sha256':'7c53fb7e1f857bf4fc599a67cbce7c206eea1f905b42edb7f3a261592381a1a7'}, 'provisional utility-consumed checker alias differs')
    for name, expected in utility_consumed.items():
        resolved = utility_aliases.get(name,name)
        path = Path(resolved) if Path(resolved).is_absolute() else BASE/resolved
        check(info(read(path)) == expected, 'utility historical consumed referent differs: ' + name)
    actual_utility = json.loads(read(UTILITY_EVIDENCE/'attempt_03.actual.json'))
    exact_utility_raw = read(UTILITY_EVIDENCE/'attempt_03.stdout.exact.json')
    check(info(exact_utility_raw) == {'bytes':147133,'sha256':'5f5487bad8a7c11c73b6a6adb251f90bfa365be42ec91d4b6152ed965b334afd'}, 'wrong recovered exact tool output')
    check(exact_utility_raw.isascii() and utility_raw == exact_utility_raw + b'\n', 'not the documented one-LF archival difference')
    check(json.loads(exact_utility_raw) == utility_result, 'packaging altered parsed content')
    packaging = json.loads(read(UTILITY_EVIDENCE/'PACKAGING_CORRECTION.actual.json'))
    check(packaging['status'] == 'EXACT_STDOUT_PACKAGING_CORRECTION_VERIFIED' and
          packaging['roundtrip_exit_code'] == 0 and packaging['recovered_stdout_equals_retained_actual_tool_output'] is True,
          'missing actual recovered-output comparison')
    check(packaging['original_captured_output_chars'] == packaging['recovered_exact_bytes'] == len(exact_utility_raw) and
          packaging['closed_original_bytes'] == len(utility_raw) and packaging['closed_original_equals_exact_plus_one_LF'] is True,
          'packaging size/identity fields differ')
    check(packaging['closed_original_sha256'] == info(utility_raw)['sha256'] and
          packaging['recovered_exact_sha256'] == info(exact_utility_raw)['sha256'], 'packaging digest fields differ')
    check(actual_utility['exit_code'] == 0 and actual_utility['output_chars'] == len(exact_utility_raw.decode())
          and actual_utility['new_mathematical_executions'] == actual_utility['new_builds'] == actual_utility['new_page_views'] == 0, 'utility completion role differs')
    for number, reason in [('01','manifest_coverage'),('02','full log diagnostic surface')]:
        stopped = json.loads(read(UTILITY_EVIDENCE/('attempt_'+number+'.actual.json')))
        check(stopped['exit_code'] == 1 and reason in stopped['output'], 'actual stopped utility attempt missing')
    response_rows = pins(B/'RESPONSE_AND_ROOT_REPLAY_PINS.after.sha256')
    expected_response = {str(p.relative_to(BASE)) for folder in (REPLAY,UTILITY_EVIDENCE) for p in folder.rglob('*') if p.is_file()}
    expected_response |= {str(p.relative_to(BASE)) for p in (RESPONSE,SUPPLEMENT,UTILITY,UTILITY_AUDIT)}
    check(len(response_rows) == 49 and set(dict(response_rows)) == expected_response, 'response/rootpair/utility pins incomplete')
    verify_rows(response_rows, BASE)
    before_packaging = pins(B/'RESPONSE_AND_ROOT_REPLAY_PINS.before_packaging.sha256')
    check(len(before_packaging) == 45 and set(before_packaging) < set(response_rows), 'original response pins not preserved')
    verify_rows(before_packaging, BASE)
    initial_build = read(B/'BUILD_REPORT.initial.md').decode()
    corrected_build = read(B/'BUILD_REPORT.md').decode()
    build_log = read(B/'cold_build_01/main.log').decode()
    pass3 = read(B/'cold_build_01/pass3.stdout').decode()
    check('undefined reference, overfull or underfull box diagnostic remains' in initial_build, 'original finding evidence missing')
    check('That scan does not include `Underfull`.' in corrected_build, 'scanner correction missing')
    check('Underfull \\vbox (badness 1038)' in corrected_build, 'actual warning missing in corrected report')
    check('underfull box diagnostic remains' not in corrected_build, 'false claim retained')
    check(build_log.count('Underfull') == 1 and pass3.count('Underfull') == 1, 'warning census differs')
    check('Underfull \\vbox (badness 1038)' in build_log.splitlines()[637], 'original log line differs')
    check('Underfull \\vbox (badness 1038)' in pass3.splitlines()[87], 'original pass3 line differs')
    check(all(marker not in build_log for marker in ('Overfull', 'undefined', 'Warning')), 'additional final diagnostics')
    open_finding = json.loads(read(B/'FINDINGS.delta_open.json'))
    check(open_finding['census']['open'] == {'critical':0,'major':0,'minor':1}, 'later finding census absent')
    check(open_finding['findings'][0]['id'] == 'P207-B-ART1', 'finding identity differs')
    read(Path(__file__))
    for name in ['INPUT_PINS.sha256', 'CONTEXT_PINS.sha256', 'SUPPLEMENTAL_READ_PINS.sha256', 'PAGE_VIEW_PINS.sha256',
                 'INPUT_PINS.after.sha256', 'LIVE_SCIENTIFIC_PINS.after.sha256', 'CONTEXT_PINS.after.sha256',
                 'SUPPLEMENTAL_READ_PINS.after.sha256', 'RESPONSE_AND_ROOT_REPLAY_PINS.after.sha256']:
        execute(['sha256sum', '-c', str(B / name)], BASE)
    execute(['sha256sum', '-c', str(FREEZE / 'SHA256SUMS')], FREEZE)
    execute(['sha256sum', '-c', str(FREEZE / 'SHA256SUMS')], PAPER)
    execute(['sha256sum','-c',str(UTILITY_EVIDENCE/'SHA256SUMS')], UTILITY_EVIDENCE)
    execute(['sha256sum','-c',str(UTILITY_EVIDENCE/'SUPPLEMENT_PINS.sha256')], UTILITY_EVIDENCE)
    for left, right in [(REPLAY/'run1.stdout', B/'CANONICAL.json'), (REPLAY/'run2.stdout', B/'CANONICAL.json'),
                        (REPLAY/'run1.stdout', REPLAY/'run2.stdout'), (B/'INPUT_PINS.sha256', B/'INPUT_PINS.after.sha256'),
                        (B/'CONTEXT_PINS.sha256', B/'CONTEXT_PINS.after.sha256'),
                        (B/'SUPPLEMENTAL_READ_PINS.sha256', B/'SUPPLEMENTAL_READ_PINS.after.sha256'),
                        (B/'REPORT.md', B/'REPORT.initial.md'), (B/'cold_build_01/main.pdf', FREEZE/'main.pdf')]:
        execute(['cmp', str(left), str(right)], BASE)
    execute(['diff','-u',str(B/'BUILD_REPORT.initial.md'),str(B/'BUILD_REPORT.md')], BASE, expected_exit=1)
    execute(['rg','-n','Underfull|Overfull|undefined|Warning',str(B/'cold_build_01/main.log'),str(B/'cold_build_01/pass3.stdout')], BASE)
    before = dict(CONSUMED)
    after = {}
    for key in before:
        path = Path(key) if Path(key).is_absolute() else BASE / key
        after[key] = info(path.read_bytes())
        check(after[key] == before[key], 'dependency changed during delta audit: ' + key)
    print(json.dumps({'kind':'ACTUAL_READ_ONLY_B_DELTA_INTEGRITY_AUDIT_NOT_NEW_MATHEMATICS_OR_VIEWS',
                      'utc':datetime.now(timezone.utc).isoformat(), 'pass':True, 'checks':CHECKS,
                      'counts':{'initial_payload':118,'root_initial_physical_package':119,'freeze_physical':106,
                                'live_scientific':105,'context':144,'supplement':7,'page_pins':7,
                                'response_root_and_utility_pins':49,'utility_historical_consumed_objects':599,
                                'root_commands':14,'root_new_runs':2,'assertions_per_root_run':2158999},
                      'historical_aliases':historical_aliases,'utility_audit_present':audit_present,
                      'utility_historical_aliases':utility_aliases,
                      'later_artifact_finding':'P207-B-ART1; exact correction checked, reviewer acceptance recorded separately',
                      'packaging_scope':'old utility JSON = exact captured stdout + one LF; failed-source snapshots preserve content/version, not unrecorded exact historical digests',
                      'consumed_inputs_before':before,'consumed_inputs_after':after,
                      'actual_delta_commands':COMMANDS}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
