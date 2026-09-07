"""B's bounded documentary audit. No mathematical producer/build/view is run.

Only runtime recording primitives are reused; every scientific input remains
the already sealed original. Historical path/hash pairs resolve explicitly.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import traceback

W = Path('/root/autodl-tmp/symbolic_dynamics')
B = W / 'docs/papers204_208_sequence/reviews/p209_b'
P = W / 'papers/209-ordered-fibre-threading'
F = P / 'frozen_round1'
A = W / 'docs/papers204_208_sequence/reviews/p209_a'
L = W / 'docs/papers204_208_sequence/qa/central_lifecycle_p209_round1'
ENV = {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
spec = importlib.util.spec_from_file_location('recording_only', B / 'record_review.py')
rec = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rec)
INPUTS = set()
ALIASES = {}
RESOLVED = {}
COUNTS = {}


def read(path):
    path = Path(path)
    INPUTS.add(str(path))
    return path.read_bytes()


def js(path):
    return json.loads(read(path))


def pin(path, digest):
    path = Path(path)
    INPUTS.add(str(path))
    assert rec.info(path)['sha256'] == digest, ('HASH', str(path), digest)


def alias(original, digest, physical):
    key = (str(original), digest)
    physical = str(physical)
    pin(physical, digest)
    if key not in ALIASES:
        ALIASES[key] = physical


def resolve(original, digest):
    key = (str(original), digest)
    physical = ALIASES.get(key, str(original))
    pin(physical, digest)
    if physical != str(original):
        RESOLVED[str(original) + ' @ ' + digest] = physical
    return physical


def manifest(path, base, complete=False):
    entries = {}
    for line in read(path).decode().splitlines():
        digest, name = line.split('  ', 1)
        rel = Path(name)
        assert len(digest) == 64 and set(digest) <= set('0123456789abcdef')
        assert not rel.is_absolute() and '..' not in rel.parts and name not in entries
        assert (Path(base) / rel) != Path(path)
        entries[name] = digest
        resolve(Path(base) / rel, digest)
    if complete:
        actual = {p.relative_to(base).as_posix() for p in Path(base).rglob('*')
                  if p.is_file() and p != Path(path)}
        assert actual == set(entries), ('COMPLETE_MANIFEST', str(path))
    return entries


def recorded_map(folder, before, after):
    x, y = js(folder / before), js(folder / after)
    assert x == y, ('RECORDED_BEFORE_AFTER', str(folder), before)
    for path, info in x.items():
        assert 'error' not in info
        physical = resolve(path, info['sha256'])
        current = rec.info(physical)
        assert current['bytes'] == info['bytes']
        if physical == path:
            assert current == info, ('RESOLUTION_METADATA', path)
    return len(x)


def commands(folder):
    rows = js(folder / 'ALL_COMMAND_RECORDS.json')
    for row in rows:
        c = row['command']
        assert c['exit'] == 0 and c['process_outcome'] == 'COMPLETED'
        assert c['spawn_error'] is None
        assert all(c['env'].get(k) == v for k,v in ENV.items())
        for stream in ('stdout', 'stderr'):
            path = Path(row['folder']) / c[stream]
            pin(path, c[stream + '_info']['sha256'])
            assert rec.info(path)['bytes'] == c[stream + '_info']['bytes']
        assert js(Path(row['folder']) / (row['tag'] + '.command.json')) == c
    return len(rows)


def configuration(folder, capture):
    old = js(folder / 'CONFIGURATION_BEFORE.json')
    assert old == js(folder / 'CONFIGURATION_AFTER.json')
    new = rec.presence([Path(p) for p in old['optional']],
                       [Path(p) for p in old['directories']])
    assert new == old, ('CURRENT_CONFIGURATION', str(folder))
    capture[folder.name] = new
    for p, item in old['optional'].items():
        if item['is_file']:
            pin(p, item['sha256'])
    for names in old['directories'].values():
        INPUTS.update(names or [])
    if folder.name == 'review_build_01':
        oldtex = js(folder / 'TEX_RESOURCES_BEFORE.json')
        assert oldtex == js(folder / 'TEX_RESOURCES_AFTER.json')
        now = rec.inventory([Path(p) for p in oldtex['roots']])
        assert now == oldtex, 'CURRENT_TEX_RESOURCES'
        INPUTS.update(oldtex['files'])
        # Existing complete maps are referenced, not copied a third time.
        capture['tex_resource_map_sha256'] = rec.info(folder / 'TEX_RESOURCES_BEFORE.json')['sha256']
        roots = js(folder / 'USER_ROOTS_BEFORE.json')
        assert roots == js(folder / 'USER_ROOTS_AFTER.json')
        assert all(not Path(x['path']).exists() and not x['exists'] for x in roots.values())
        capture['user_roots'] = roots


def main():
    out = Path(sys.argv[1])
    assert out == B / 'artifact_audit_01'
    assert sys.flags.isolated and sys.flags.no_site and sys.flags.optimize == 0 and sys.dont_write_bytecode
    assert dict(os.environ) == ENV
    assert not Path(sys.pycache_prefix).exists()
    INPUTS.update([str(B / 'audit_artifacts.py'), str(B / 'record_review.py')])
    r = js(F / 'ROUND1_PROVENANCE.json')
    for item in js(B / 'assignment_context/ROLES.json'):
        alias(item['original'], item['sha256'], item['preserved'])
    for item in js(L / 'CAPTURE.actual.json')['copies']:
        alias(item['original_path'], item['sha256'], item['physical_path'])
    for item in r['anchor_mapping'].values():
        alias(item['original_path'], item['sha256'], F / item['physical_path'])
    for item in r['historical_external_resolution'].values():
        alias(item['original_path'], item['sha256'], item['round1_physical_path'])
    manifest(L / 'SHA256SUMS', L, True)
    pin(F / 'SHA256SUMS', 'c93e16cf20d2eb87f3b454fbdb3576e52c6c79fb74c8712a277efeab7e60ce57')
    core = manifest(F / 'SHA256SUMS', F, True)
    assert len(core) == 2003
    frozen = manifest(B / 'INPUT_PINS.sha256', W)
    assert len(frozen) == 2004
    assert set(frozen) == {str((F / name).relative_to(W)) for name in core} | {str((F / 'SHA256SUMS').relative_to(W))}
    COUNTS.update(round1_payloads=len(core), frozen_inputs=len(frozen))
    r0 = manifest(F / 'ROUND1_ACCEPTANCE/ROUND0_CORE_MANIFEST.sha256', P / 'frozen_round0')
    assert set(r0) == {p.relative_to(P / 'frozen_round0').as_posix()
                       for p in (P / 'frozen_round0').rglob('*')
                       if p.is_file() and p != P / 'frozen_round0/SHA256SUMS'}
    assert r0 == r['core_payload_pins'] and len(r0) == 1989
    for name, digest in r0.items(): pin(F / name, digest)
    author = manifest(F / 'AUTHOR_MANIFEST.sha256', F)
    assert len(author) == 1985 and all(core[k] == v for k,v in author.items())
    COUNTS.update(core_preserved=len(r0), author_preserved=len(author))
    for key in ('all_source_inputs_before_and_rechecked_after',
                'accepted_review_and_root_manifest_referents'):
        for path, digest in r[key].items(): resolve(path, digest)
        COUNTS[key] = len(r[key])
    for key in ('round1_core_link_map', 'acceptance_and_historical_anchor_link_map'):
        for row in r[key]: resolve(row['physical_target'], row['sha256'])
        COUNTS[key] = len(r[key])
    oldpaper = r['prior_whole_paper_manifest']
    assert oldpaper['original_referent_base'] == str(P)
    assert not oldpaper['complete_current_paper_after_round1']
    old = manifest(oldpaper['physical_path'], P)
    assert {str(P/k):v for k,v in old.items()} == oldpaper['original_referent_pins']
    assert len(old) == 3978
    COUNTS['historical_paper_referents_original_base'] = len(old)
    for key in ('A_REVIEW_MANIFEST.sha256', 'ROOT_PAIR_MANIFEST.sha256', 'ROOT_LAUNCHER_MANIFEST.sha256'):
        item = r['anchor_mapping'][key]
        entries = manifest(F / item['physical_path'], Path(item['original_path']).parent)
        COUNTS[key] = len(entries)
    findings = js(F / 'ROUND1_ACCEPTANCE/A_CURRENT_FINDINGS.json')
    assert findings['delta_status'] == 'ACCEPTED_EXACT_NOCHANGE_DELTA'
    assert findings['current_open_counts'] == {'critical':0,'major':0,'minor':0}
    assert findings['findings'] == []
    assert js(F / 'ROUND1_ACCEPTANCE/A_INITIAL_FINDINGS.json')['delta_status'] != 'ACCEPTED_EXACT_NOCHANGE_DELTA'
    manifest(B / 'INDEPENDENCE_COMMITMENT.sha256', B)
    manifest(B / 'INFRASTRUCTURE_INPUT_PINS.sha256', W)
    selected = ['review_pair_01','review_pair_01/replay_01','review_pair_01/replay_02',
                'launcher_review_pair_01','review_build_01','launcher_review_build_01','auxiliary_01']
    for name in selected:
        folder = B / name
        COUNTS[name + '_payloads'] = len(manifest(folder / 'SHA256SUMS', folder, True))
    cfg_before = {}
    for name in ('review_pair_01','review_build_01'):
        folder = B / name
        receipt = js(folder / 'RECEIPT.json')
        assert receipt['status'] == 'PASS_REVIEW_B_' + ('PAIR' if name == 'review_pair_01' else 'BUILD')
        assert not receipt['failures']
        COUNTS[name + '_inputs'] = recorded_map(folder, 'ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json', 'ALL_INPUTS_AFTER.json')
        COUNTS[name + '_commands'] = commands(folder)
        configuration(folder, cfg_before)
    for name in ('launcher_review_pair_01','launcher_review_build_01','auxiliary_01'):
        COUNTS[name + '_inputs'] = recorded_map(B/name, 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json')
    COUNTS['auxiliary_commands'] = commands(B / 'auxiliary_01')
    pair = js(B / 'review_pair_01/RECEIPT.json')
    assert all(x['checks'] == 54794 and x['total_states'] == 3414 for x in pair['result']['replays'])
    assert all(x['exit'] == 0 for x in pair['result']['comparisons'])
    pin(B / 'CANONICAL.json', '612e1463162deba868cf7cf81d61c8f017713f9b28c4c38b81b00d376bac992c')
    for name in ('replay_01','replay_02'):
        assert read(B / 'review_pair_01' / name / 'producer.stdout') == read(B / 'CANONICAL.json')
    rr = js(B / 'auxiliary_01/reconcile.stdout')
    assert rr['status'] == 'PASS_FULL_MATHEMATICAL_PAYLOAD_RECONCILIATION'
    assert rr['row_count'] == 3414 and rr['checks'] == 78548
    for names in [('author_projection.json','B_to_author_projection.json'),('A_projection.json','B_to_A_projection.json')]:
        assert read(B / 'auxiliary_01' / names[0]) == read(B / 'auxiliary_01' / names[1])
    assert read(F / 'main.pdf') == read(B / 'review_build_01/cold_build/main.pdf')
    pin(B / 'review_build_01/cold_build/main.pdf', 'ca2e381904905939e121b7931641b050ba24657c16661df3bb5008c88c28884f')
    for name in ('BUILD_REPORT.md','REPLAY_LOG.md','SOURCE_AND_PROOF.md','INDEPENDENCE_DESIGN.md'):
        read(B / name)
    # Every known audit input is explicit. Discovery precedes this new
    # documentary before/after interval; old original timing is not relabelled.
    before = rec.pins(INPUTS)
    assert all('error' not in item for item in before.values())
    rec.save(out / 'DOCUMENTARY_INPUTS_BEFORE.json', before)
    rec.save(out / 'EXACT_HISTORICAL_RESOLUTION.json', RESOLVED)
    rec.save(out / 'CONFIGURATION_RECHECK_BEFORE.json', cfg_before)
    problem = None
    try:
        # Final remeasure: no math/build process is launched in this interval.
        cfg_after = {}
        for name in ('review_pair_01','review_build_01'):
            configuration(B / name, cfg_after)
        assert cfg_after == cfg_before
        rec.save(out / 'CONFIGURATION_RECHECK_AFTER.json', cfg_after)
    except BaseException:
        problem = traceback.format_exc()
    assert set(INPUTS) == set(before), 'LATE_UNINVENTORIED_INPUT'
    after = rec.pins(INPUTS)
    rec.save(out / 'DOCUMENTARY_INPUTS_AFTER.json', after)
    assert before == after, 'DOCUMENTARY_INPUTS_CHANGED'
    assert problem is None, problem
    result = {'status':'PASS_DOCUMENTARY_ROLE_AND_DEPENDENCY_AUDIT','counts':COUNTS,
              'documentary_inputs_before_and_after':len(before),
              'explicit_historical_resolutions':len(RESOLVED),
              'new_math_build_render_or_view':False,
              'limits':'Discovery and prior completed records are not new mathematical execution; no continuous trace, grandchild capture, or OS-hermetic claim. Current mutable whole-paper manifest is not substituted for the preserved historical 3978-referent seal.',
              'delta_status':'UNASSESSED','external':'OWNER_AMBER / HOLD_EXTERNAL'}
    rec.save(out / 'AUDIT_RESULT.json', result)
    print(json.dumps(result,sort_keys=True))


if __name__ == '__main__': main()
