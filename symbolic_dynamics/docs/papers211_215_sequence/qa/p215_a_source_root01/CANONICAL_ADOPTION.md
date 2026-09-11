# P215 Review A canonical adoption

2026-09-11 UTC. After complete initial DATA reception, root checked that
`reviews/p215_a/CANONICAL.txt` was absent, materialized only the actual
initial01 stdout, and compared the complete raw bytes. The adopted canonical
is 2,060 bytes with SHA256
`58f40d2d90505ccf3be39453c213bb99d82aa4b268f88a2c8d6b1e968209d695`.

The initial producer did not read a canonical. Strict runs additionally bind
this exact canonical in their PRE/POST input sets. This adoption is not a
strict replay, final Review A verdict, manuscript change, build or Round1
freeze.
