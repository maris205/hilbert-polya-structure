# Actual root precheck invocation failure

Before any new Git write, root invoked:

`python3 -I -S -B docs/papers211_215_sequence/qa/private_checkpoint_preparation02/inspect_preparation.py`

The actual tool return (chunk ca89c1) exited 1 at line 14,
`assert plan['protected_roles'] == m['protected_roles']()`, raising
`AssertionError`. This was the author read-only inspector, not a Git phase.

The follow-up actual read-only role diff (8adfcb, exit 0) showed exactly
one changed executable role: shell `python3` resolves to
`/root/miniconda3/bin/python3.12`, while the approved preparation uses
`/usr/bin/python3.10` via explicit `/usr/bin/python3`. The former 30,626,264
bytes/SHA256 9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101
is not the latter 5,937,704 bytes/SHA256
d6bca2b84e73c7775a0dd5e6a76899cfe4ee62863d7c8f88513811d1fda23f49.
No other protected-role difference was returned.

The exact intended invocation with `/usr/bin/python3 -I -S -B` passed
unchanged author inspection (66874d, exit 0): 714 selected files,
182 inherited rows and 14 protected roles. No plan, interpreter, guard or
source was changed to make it pass. This success is not independent root
inspection or capture. All later phases must use the explicit interpreter.

The actual failed-versus-final executor diff (e07c7e, expected diff exit 1)
shows three NUL/TAB literal fixes in dependency_tree plus removal of a
trailing blank line. The preparer's failed original remains physically
preserved. No claim of byte-identical failed/final source is made.

The first broad root executor display was truncated; root then read the
missing inherited-input/prior-QA block at lines 360–450 in full. No approval
rests on the truncated portion or an unread summary. No Git mutation,
scientific run, deletion or external release occurred in these checks.
