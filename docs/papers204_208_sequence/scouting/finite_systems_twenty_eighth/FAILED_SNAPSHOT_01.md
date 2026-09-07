# Actual failed documentary snapshot

This is a post-command transcription of the actual terminal result, not an
at-launch recorder or a successful snapshot. No scientific code ran.

Command, cwd `/root/autodl-tmp/symbolic_dynamics`:

```text
python docs/papers204_208_sequence/scouting/finite_systems_twenty_eighth/capture.py snapshot nearby_originals docs/papers127_131_sequence/scouting/algebraic/SCOUT.md docs/papers204_208_sequence/scouting/algebra_third/INTAKE.md docs/papers204_208_sequence/scouting/algebra_third/SOURCE_AND_COLLISION_NOTES.md
```

Actual exit code: `1`. The terminal returned the following complete merged
output. Its API did not separate stdout and stderr in this original call:

```text
Traceback (most recent call last):
  File "/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/scouting/finite_systems_twenty_eighth/capture.py", line 58, in <module>
    if args.mode == 'snapshot': snapshot(args.name, args.paths)
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/scouting/finite_systems_twenty_eighth/capture.py", line 34, in snapshot
    shutil.copy2(p, target)
  File "/root/miniconda3/lib/python3.12/shutil.py", line 475, in copy2
    copyfile(src, dst, follow_symlinks=follow_symlinks)
  File "/root/miniconda3/lib/python3.12/shutil.py", line 260, in copyfile
    with open(src, 'rb') as fsrc:
         ^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/scouting/algebra_third/INTAKE.md'
```

The first `SCOUT.md` had already been physically copied into
`history/nearby_originals/`; no `PIN_MANIFEST.json` was emitted because the
second target did not exist. That incomplete directory is preserved as
failure evidence. Remaining targets are resolved by filename-only discovery
and copied into a distinct v2 directory. The v2 snapshot is not a repair
pretending that the initial operation succeeded. No missing file is invented.
