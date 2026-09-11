#!/usr/bin/env python3
"""Documentary preview copies only; not the checkpoint capture phase."""
import runpy
import sys
from pathlib import Path

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
OLD = ROOT / 'docs/papers211_215_sequence/qa/private_checkpoint_preparation/checkpoint.py'
OUT = ROOT / 'docs/papers211_215_sequence/qa/private_checkpoint_preparation02'
old = runpy.run_path(str(OLD), run_name='inspected_previous_checkpoint_library')
need, key, save = old['need'], old['key'], old['save']
need(sys.flags.isolated == 1 and sys.flags.no_site == 1 and sys.dont_write_bytecode,
     'Require python3 -I -S -B')
directory = OUT / 'controls_preview34'
directory.mkdir(exist_ok=False)
command = old['Commands'](directory, 'prepare')
roles = {
    'SYMBOLIC_DYNAMICS_STATE.md': directory / 'SYMBOLIC_DYNAMICS_STATE.md',
    'docs/papers211_215_sequence/PIPELINE_STATE.md': directory / 'PIPELINE_STATE.md',
}
try:
    before = {name: key(ROOT / name) for name in roles}
    native_before = command.run(['/usr/bin/sha256sum', *[str(ROOT / n) for n in roles]])
    for name, target in roles.items():
        command.run(['/usr/bin/cp', '--no-clobber', '--preserve=mode', str(ROOT / name), str(target)])
        command.run(['/usr/bin/cmp', str(ROOT / name), str(target)])
        need(key(target) == before[name] == key(ROOT / name), 'Control changed during preview copy')
    native_after = command.run(['/usr/bin/sha256sum', *[str(ROOT / n) for n in roles]])
    need(native_before == native_after, 'Native before/after source list differs')
    pipeline = roles['docs/papers211_215_sequence/PIPELINE_STATE.md'].read_text()
    need('total **34**, zero reserves.' in pipeline,
         'Expected exact 34-closed boundary is no longer the current pipeline')
    save(directory / 'SOURCE_ROLES.json', {
        'kind': 'documentary preparation preview; NOT execution capture phase',
        'closed_literal_boundary': 34,
        'source_mapping': {name: str(target.relative_to(ROOT)) for name, target in roles.items()},
        'inventory': before,
        'wrapper': {'path': str(Path(__file__).resolve()), **key(Path(__file__).resolve())},
        'imported_previous_executor': {'path': str(OLD), **key(OLD)},
        'native_tools': {name: key(Path(name)) for name in ['/usr/bin/cp', '/usr/bin/cmp', '/usr/bin/sha256sum']},
        'interpreter': {'path': str(Path(sys.executable).resolve()), **key(Path(sys.executable).resolve())},
        'future_live_equality_required': False,
    })
    seal = old['finish'](directory, {
        'status': 'DOCUMENTARY_PREVIEW_34_COPIES_BYTE_EQUAL',
        'commands': command.count, 'git_commands': 0, 'scientific_runs': 0,
        'source_role_count': len(roles), 'future_live_controls_not_dependencies': True,
    })
    print(seal)
except BaseException:
    old['failure'](directory, 'documentary-control-preview34')
    raise
