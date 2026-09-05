# Root's actual CCI admission replays

2026-09-05 UTC. Root executed the independent CCI_GATE/verify_gate.py twice
in separate Python 3.12.3 processes, with -B, standard library only. Full
stdout was first saved to /tmp/cci_gate_root_run1.stdout and run2.stdout;
each producer exited zero, and each raw cmp against CCI_GATE/CANONICAL.json
exited zero. The two stdout files here are exact copies of those completed
runs, subsequently compared again with the canonical at exit zero; copying
and rechecking are not represented as new executions.

Both runs contain 7,530,194 assertions. The canonical and both stdout
streams have SHA256
`da851425b43c4ef7d27b56f29d9fb5a6d5091435f26aed795da463dd7f876783`.
All eleven workspace-root source pins and seven gate nonself manifest
entries passed before admission. Root read the entire author/gate/source
audits and actual author response. These are admission checks, not A/B
manuscript reviews or a five-paper terminal audit.
