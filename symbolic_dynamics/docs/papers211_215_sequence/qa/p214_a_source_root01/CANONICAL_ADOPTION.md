# P214 Review A canonical adoption

2026-09-11 UTC. After complete initial DATA reception, root checked that
reviews/p214_a/CANONICAL.txt was absent, copied only the actual initial01
stdout without clobbering, and compared the complete raw bytes. The adopted
canonical is 644 bytes with SHA256
998a741598f8794b92a16730e9d4fd572d09ff366b1baa108eb19f1c54818d18.

The initial producer did not read a canonical. Strict runs use a revised
guard that additionally binds this exact canonical in their PRE/POST input
sets. This adoption is not a strict replay, final Review A verdict, manuscript
repair, build or Round1 freeze.
