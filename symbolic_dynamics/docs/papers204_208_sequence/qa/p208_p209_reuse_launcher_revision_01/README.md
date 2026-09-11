# Native launcher revision 01 — fixed fresh reuse_02

Preparation only. This launcher and the revised checker have not been run.
Both original preparations, the actual failed `p208_p209_reuse_01/`, and the
root launch/completion records remain unchanged.

The sole checker correction is the exact original P208 canonical-first
operand order. See the companion `qa/p208_p209_reuse_revision_01/README.md`,
its complete source delta, 34 original preservation pins, and the actual
bounded 52-argv diagnostic. Neither package grants a current-reuse PASS.

This launcher differs from the original by seven exact substitutions only:
its own preparation path, revised checker preparation path, checker seal,
checker source hash, fixed output `reuse_02`, and the two preparation payload
counts. Native execution, timeout, signal handling, process-group settling,
raw streams, runtime/configuration keys and map sampling are unchanged.
`SOURCE_DELTA.diff` is the complete minimal two-hunk native unified diff;
`STATIC_CHECK.json` checks exact byte substitutions and unchanged AST portions.

## Root's future actual command

From cwd `/root/autodl-tmp/symbolic_dynamics`, replace only the final placeholder
with the independently verified SHA-256 of this preparation's `SHA256SUMS`:

```text
/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/p208_p209_reuse_02/unused_launcher_cache /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/p208_p209_reuse_launcher_revision_01/launcher.py launch-current-p208-p209 LAUNCHER_REVISION_SHA256SUMS_DIGEST
```

The child command is the exact separate native system-Python invocation of
the revised checker, with the same ENV4/cwd and the distinct absent
`reuse_02/unused_checker_cache`. It is bound to:

```text
Checker source SHA256
8b38768261afe5bd6db8d769a8209b4aa3daec40119189c953e69c9b20e60ea0

Checker revision SHA256SUMS
ac8fe8834360fdb35e70860416a3c7bb2283b8e32f738251ffc5a1acdfc52a46
```

Output `qa/p208_p209_reuse_02/` must be absent; existing output is refused.
The old `reuse_01` is never reused, renamed or overwritten. Root must read
both complete revised sources and deltas and verify both exact nonself seals
before actual execution. This launcher preparation has five payloads/six
physical files; the checker revision has seven payloads/eight physical files.
The original 128 fixed checker inputs and six alias declarations are unchanged.

All original launcher boundaries remain: direct native checker only, timeout
600 seconds, owned-group TERM/grace/KILL/reap and recorded absence before
settled stream hashes; uncertainty yields no final seal. Actual raw stdout
and stderr, full checker JSON, source copies, complete before/after keys and
retained parent/child samples are recorded by a future run. No imported
checker, bootstrap, new mathematical execution, build or view is authorized.

Success remains `PASS_NATIVE_READ_ONLY_REUSE_LAUNCH_NOT_BATCH_ACCEPTANCE`.
It requires the actual checker exit/status and all original closure checks;
failed or unsettled attempts remain preserved. The final wrapper stdout does
not replace root's actual outer native exit record. `HOLD_EXTERNAL` remains.
