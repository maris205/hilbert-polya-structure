"""Pure audit-refusal test. No scientific module and no native grandchild."""
import json
from pathlib import Path
import sys
import types

source, out = map(Path, sys.argv[1:])
core = types.ModuleType('_core_audit_refusal_fixture')
core.__file__ = str(source)
exec(compile(source.read_bytes(), str(source), 'exec'), core.__dict__)
out.mkdir()
(out / 'commands').mkdir()
core.OUT = out
seen = []


def refuse(event, args):
    if event == 'subprocess.Popen':
        seen.append(event)
        raise RuntimeError('PURE_TEST_AUDIT_REFUSAL_BEFORE_POPEN_RETURN')


sys.addaudithook(refuse)
refused = False
try:
    core.command('refused_before_return', ['/usr/bin/true'], timeout=10,
                 cwd=core.ROOT, require_success=False)
except RuntimeError:
    refused = True
assert refused and seen == ['subprocess.Popen'] and core.UNFINALIZED_NATIVE
assert not (out / 'commands/refused_before_return/RECEIPT.json').exists()
assert (out / 'commands/refused_before_return/ATTEMPT.json').is_file()
assert (out / 'commands/refused_before_return/UNFINALIZED_NATIVE.json').is_file()
blocked_seal = False
try:
    core.seal()
except AssertionError:
    blocked_seal = True
assert blocked_seal and not (out / 'SHA256SUMS').exists()
print(json.dumps({'pure_infrastructure_test': True, 'audit_event': seen,
                  'unknown_pre_return_outcome_preserved': True,
                  'no_invented_native_exit_or_stream_seal': True}, sort_keys=True))
