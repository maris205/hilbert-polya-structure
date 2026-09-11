"""Root documentary rerun/reception only; no scientific or build execution."""
from pathlib import Path
import base64
import gzip
import hashlib
import importlib.util
import json
import os
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PREP = QA / 'p210_round1_central_update_check'
OUT = QA / 'p210_round1_central_update_root'
SUPPORT = QA / 'p210_checkpoint_stage_revision_01/process_support.py'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write(path, value):
    with path.open('x') as stream:
        json.dump(value, stream, sort_keys=True, indent=2)
        stream.write('\n')

assert Path.cwd() == ROOT and dict(os.environ) == ENV
assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
assert not OUT.exists() and not Path(sys.pycache_prefix).exists()
assert sha(SUPPORT) == '8ce99e3b7684123c5a04d99d8fa5cee98bd4e8e8b9bca7f7a4dd5dc93b5dde7c'
assert sha(PREP / 'SHA256SUMS') == '697d10eb671f293fa85a3540951551af1e472644eff372578600ec65cbd8d152'
pins = {}
for line in (PREP / 'SHA256SUMS').read_text().splitlines():
    digest, name = line.split('  ', 1)
    assert name != 'SHA256SUMS' and name not in pins and not Path(name).is_absolute() and '..' not in Path(name).parts
    assert sha(PREP / name) == digest
    pins[name] = digest
assert len(pins) == 15 and set(pins) == {p.relative_to(PREP).as_posix() for p in PREP.rglob('*') if p.is_file()} - {'SHA256SUMS'}
prior_raw = gzip.decompress(base64.b64decode((PREP / 'DOCUMENTARY_RESULT.json.gz.b64').read_bytes()))
assert hashlib.sha256(prior_raw).hexdigest() == '1f7b761b05f55f94462e341f837a1a7fcf008b581b2644fa4478d3f6b379e5be'
prior = json.loads(prior_raw)
OUT.mkdir()
spec = importlib.util.spec_from_file_location('central_owned_native', SUPPORT)
support = importlib.util.module_from_spec(spec)
spec.loader.exec_module(support)
argv = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(OUT / 'never_created_child_cache'), str(PREP / 'check_central_update.py'), 'documentary-only']
(OUT / 'stdin.raw').open('xb').close()
native = support.run_files(argv, OUT / 'stdin.raw', OUT / 'stdout.raw', OUT / 'stderr.raw', ENV, timeout=300)
write(OUT / 'NATIVE.actual.json', {'argv': argv, 'cwd': str(ROOT), 'environment': ENV, **native,
    'stdout_sha256': sha(OUT / 'stdout.raw'), 'stderr_sha256': sha(OUT / 'stderr.raw'), 'root_source_sha256': sha(Path(__file__))})
assert native['exit'] == 0 and native['process_group_settlement']['quiescent'] and not native['process_group_settlement']['signals']
assert not (OUT / 'stderr.raw').read_bytes()
current = json.loads((OUT / 'stdout.raw').read_bytes())
assert current['status'] == prior['status'] == 'DOCUMENTARY_SCOPE_CLOSED_NOT_TERMINAL_PASS'
assert current['checks'] == 34632 and current['unique_file_inputs_reread'] == 1752 and not current['failures']
ignored = {'started_utc', 'ended_utc'}
assert {k: v for k, v in current.items() if k not in ignored} == {k: v for k, v in prior.items() if k not in ignored}
assert all(sha(PREP / name) == digest for name, digest in pins.items())
result = {'status': 'ROOT_DOCUMENTARY_RERUN_AND_FULL_ORIGINAL_COMPARISON_PASS', 'checks': current['checks'],
    'input_paths_reread': 1752, 'complete_prior_stdout_sha256': hashlib.sha256(prior_raw).hexdigest(),
    'root_stdout_sha256': sha(OUT / 'stdout.raw'), 'only_ignored_comparison_fields': sorted(ignored),
    'science_build_view_review_git_or_terminal_acceptance': False, 'external': 'HOLD_EXTERNAL'}
write(OUT / 'RESULT.actual.json', result)
with (OUT / 'SHA256SUMS').open('x') as stream:
    for path in sorted(p for p in OUT.iterdir() if p.is_file() and p.name != 'SHA256SUMS'):
        stream.write(sha(path) + '  ' + path.name + '\n')
print(json.dumps(result, sort_keys=True))
