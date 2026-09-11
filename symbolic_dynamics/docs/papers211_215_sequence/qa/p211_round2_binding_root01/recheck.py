"""Actual root whole accepted key/settings check, no science/build/freeze.

The four-field key and configuration conventions are disclosed reuse from
p211_round1_binding_root/recheck02.py, fully read by root. This forward
adapter receives all 1785 accepted B entries (including 801 host paths),
the four complete R1 host stat entries, full existing 122 runtime key and
69/5/9 settings. No host selector or runtime baseline is extended.
The separate unchanged accepted inspect_build_reuse.py execution is bound
by its entire actual native output, not merely a receipt PASS string.
No inherited ambient environment is recorded by this documentary script.
"""
from hashlib import sha256
import json
import os
from pathlib import Path
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
HERE = Path(__file__).resolve().parent
PAPER = ROOT/'papers/211-kernel-image-projection-feedback'
READS = {}
CHECKS = []


def need(ok, label):
    if not ok:
        raise AssertionError(label)
    CHECKS.append(label)


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    key = {'bytes': len(raw), 'sha256': sha256(raw).hexdigest(),
           'resolved': str(path.resolve(strict=True)),
           'symlink': os.readlink(path) if path.is_symlink() else None}
    need(str(path) not in READS or READS[str(path)] == key, 'same_full_read:' + str(path))
    READS[str(path)] = key
    return raw


def pin(path, expected):
    read(path)
    actual = READS[str(Path(path))]
    need(all(actual[k] == v for k, v in expected.items()), 'whole_original_key:' + str(path))


def obj(path):
    return json.loads(read(path))


def state(path, with_bytes=True):
    path = Path(path)
    row = {'lexists': os.path.lexists(path), 'exists': path.exists(),
           'is_file': path.is_file(), 'is_dir': path.is_dir(),
           'is_character_device': path.is_char_device(), 'resolved': str(path.resolve()),
           'symlink': os.readlink(path) if path.is_symlink() else None}
    if path.is_char_device():
        st = path.stat()
        row['character_device'] = {'major': os.major(st.st_rdev), 'minor': os.minor(st.st_rdev), 'mode': st.st_mode}
    if with_bytes and path.is_file():
        raw = read(path)
        row.update({'bytes': len(raw), 'sha256': sha256(raw).hexdigest()})
    return row


def all_settings(lock):
    for path, expected in lock['configuration']['paths'].items():
        need(state(path) == expected, 'whole_config:' + path)
    for directory, expected in lock['configuration']['memberships'].items():
        path = Path(directory)
        current = {'directory': state(path, False), 'members': {}}
        if path.is_dir():
            current['members'] = {p.name: state(p, False) for p in sorted(path.iterdir())}
        need(current == expected, 'entire_membership:' + directory)
    for path, expected in lock['loader_search_directory_states'].items():
        need(state(path, False) == expected, 'loader_directory:' + path)


def r1_host_stat(path):
    raw = read(path)
    p = Path(path)
    need(p.resolve(strict=True) == p and not p.is_symlink(), 'ordinary_R1_host_tool:' + str(path))
    st = p.stat()
    return {'bytes': len(raw), 'sha256': sha256(raw).hexdigest(), 'stat': {
        'ctime_ns': st.st_ctime_ns, 'device': st.st_dev, 'gid': st.st_gid,
        'inode': st.st_ino, 'mode': st.st_mode, 'mtime_ns': st.st_mtime_ns,
        'nlink': st.st_nlink, 'size': st.st_size, 'uid': st.st_uid}}


need(len(sys.argv) == 2 and sys.argv[1] in ('precopy','postcopy'), 'exact_phase')
phase = sys.argv[1]
need(Path.cwd() == ROOT, 'physical_workspace_cwd')
out = HERE/(phase+'01')
need(not os.path.lexists(out), 'exclusive_new_documentary_output')
if phase == 'precopy':
    need(not os.path.lexists(PAPER/'frozen_round2') and not os.path.lexists(PAPER/'qa_final'), 'physical_R2_terminal_not_started')
else:
    need((PAPER/'frozen_round2').is_dir() and not os.path.lexists(PAPER/'qa_final'), 'postcopy_before_terminal_build')
read(__file__)
key_path = QA/'p211_b_final_root/INPUTS.json'
pin(key_path, {'sha256':'c78f32fa33e73c428f3915a2f9b49cd5926289e93f9ca32fc28a86b5a4fc9509'})
accepted = obj(key_path)
need(len(accepted) == 1785 and sum(not Path(p).is_relative_to(ROOT) for p in accepted) == 801, 'all_1785_B_entries_801_host')
for path, expected in accepted.items():
    pin(path, expected)
r1_key = QA/'p211_round1_execution01/READ_INPUTS_AFTER.json'
pin(r1_key, {'sha256':'73dddc8f548fe275baa16ca515b4340ae69160256db78a0efaf4acca2433656c'})
r1 = obj(r1_key)
need(len(r1) == 2255, 'entire_R1_key_schema')
host = {p:v for p,v in r1.items() if not Path(p).is_relative_to(ROOT)}
need(len(host) == 4, 'exact_four_R1_host_rows')
for path, expected in host.items():
    need(r1_host_stat(path) == expected, 'whole_original_R1_host_stat:' + path)
binding_path = QA/'p211_b_pair_binding/BINDING.json'
need(str(binding_path) in accepted, 'accepted_B_pair_binding_is_original_key_input')
binding = obj(binding_path)
lock_path = Path(binding['runtime_lock']['path'])
pin(lock_path, {k:binding['runtime_lock'][k] for k in ('sha256','bytes','resolved','symlink')})
lock = obj(lock_path)
need((len(lock['files']),len(lock['configuration']['paths']),len(lock['configuration']['memberships']),len(lock['loader_search_directory_states'])) == (122,69,5,9), 'whole_unchanged_122_69_5_9_runtime_scope')
for path, expected in lock['files'].items():
    pin(path, expected)
all_settings(lock)
new_build = obj(HERE/('BUILD_'+phase.upper()+'_NATIVE01.json'))
old_build = obj(QA/'p211_b_final_root/BUILD_REUSE_NATIVE01.json')
need(new_build['result']['exit_code'] == 0 and 'session_id' not in new_build['result'], 'actual_complete_new_build_reuse_native')
need(all(new_build['request'][k] == old_build['request'][k] for k in ('cmd','workdir')) and new_build['result']['output'] == old_build['result']['output'], 'entire_original_and_new_build_output_bytes_equal')
reuse = json.loads(new_build['result']['output'])
need(reuse['checks'] == 5974 and reuse['prior_read_key_entries_checked_twice'] == 1299 and reuse['configuration_entries_checked_twice'] == 843 and reuse['fresh_build'] is False and reuse['scientific_execution'] is False, 'actual_full_build_dependency_recheck_not_build')
for path, expected in dict(READS).items():
    pin(path, expected)
for path, expected in host.items():
    need(r1_host_stat(path) == expected, 'post_whole_R1_host_stat:' + path)
all_settings(lock)
result = {'status':'PASS_COMPLETE_ACCEPTED_KEY_HOST_RUNTIME_AND_BUILD_SETTINGS_RECHECK',
          'phase':phase, 'checks':len(CHECKS), 'read_paths':len(READS),
          'accepted_full_key':{'path':str(key_path),'pin':READS[str(key_path)]},
          'accepted_key_entries':1785, 'outside_workspace_entries':801,
          'r1_full_schema_entries':2255, 'r1_host_rows_full_stat_checked_twice':4,
          'runtime_files':122, 'runtime_configuration_paths':69,
          'runtime_memberships':5, 'runtime_loader_directory_states':9,
          'configuration_passes':2, 'build_file_keys_checked_twice':1299,
          'build_configurations_checked_twice':843,
          'build_native_reference':str(HERE/('BUILD_'+phase.upper()+'_NATIVE01.json')),
          'new_scientific_runs':0, 'new_builds':0, 'new_page_views':0,
          'round2_received':False, 'binding_authorized_by_this_script':False,
          'limits':'Complete old key/settings recheck only. R1 workspace version resolutions and physical R2 require separate actual binding/reception. No baseline extension or ambient environment capture.'}
out.mkdir()
for name, data in [('RESULT.json',result),('READ_INPUTS.json',READS),('CHECK_LABELS.json',CHECKS)]:
    with (out/name).open('x') as f:
        json.dump(data,f,sort_keys=True,indent=2)
        f.write('\n')
print(json.dumps(result,sort_keys=True))
