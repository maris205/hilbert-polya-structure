# Preserved pre-producer launch failure

The first top-level attempt guessed `/usr/local/bin/python3`; that executable
does not exist here. Actual shell exit was 127 and the complete stderr was:

```
/usr/bin/env: ‘/usr/local/bin/python3’: No such file or directory
```

Command body, from the actual call:

```sh
task_cache_dir=$(mktemp -d /tmp/fth-gate-parent-XXXXXX)
/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/local/bin/python3 -I -S -B -X "pycache_prefix=$task_cache_dir/never_created_cache" /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/scouting/FTH_GATE/record_pair.py
```

No recorder, ldd inventory, mathematical kernel or replay capsule started in
this failed launch. No input, code or hypothesis changed. The next launch
resolves the real interpreter first. This is neither a failed theorem test
nor one of the two successful science replays.
