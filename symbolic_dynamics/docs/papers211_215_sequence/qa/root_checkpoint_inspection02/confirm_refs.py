#!/usr/bin/env python3
"""Fresh root read-only ref/tree confirmation with the inspected native recorder."""
from pathlib import Path
import json
import runpy

HERE = Path(__file__).resolve().parent
RUN = Path('/root/symbolic-dynamics-closed-scout-checkpoint-4dtz40s2')
m = runpy.run_path(str(RUN / 'executed_source.py'), run_name='root_readonly_import')
d = HERE / 'postpush_readonly01'
d.mkdir(exist_ok=False)
c = m['Commands'](d, 'prepare')  # Its allowlist prohibits all Git mutations.
commit = '7d43cb323adf7d27326263b8ce4158d4eefff43a'
tree = '64feab3a9eff397179a6670aff5b1ff7d0595796'
plan = json.loads((RUN / 'PLAN.json').read_bytes())
m['frozen_guard'](RUN, plan)
assert c.git('rev-parse', 'refs/heads/main').decode().strip() == commit
assert c.git('rev-parse', commit + '^{tree}').decode().strip() == tree
assert c.git('rev-list', '--parents', '-n', '1', commit).decode().split() == [commit, plan['base']]
assert c.mirror('rev-parse', 'HEAD').decode().strip() == plan['mirror_base']
assert c.mirror('status', '--porcelain=v1', '-z', '--untracked-files=all') == b''
assert c.git('ls-remote', '--exit-code', plan['remote_url'], 'refs/heads/main') == (commit + '\trefs/heads/main\n').encode()
m['frozen_guard'](RUN, plan)
result = {'status': 'PASS_ROOT_FRESH_READONLY_REFS', 'commands': c.count,
          'commit': commit, 'tree': tree, 'remote_confirmed': True,
          'original_mirror_unchanged_clean': True, 'bare_worktree_status': 'N/A',
          'git_mutations': 0, 'new_science': 0}
seal = m['finish'](d, result)
print(json.dumps({**result, 'manifest_sha256': seal}))
