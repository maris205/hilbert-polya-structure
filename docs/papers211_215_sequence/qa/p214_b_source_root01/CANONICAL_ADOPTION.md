# P214 Review B canonical adoption

2026-09-11 UTC. After complete initial DATA reception, root verified the B
canonical path was absent, copied only the actual initial01 stdout without
clobbering, and compared the complete raw bytes. `CANONICAL.txt` is 641,682
bytes, SHA256 `7834b38f93b9dfe5e5a57f230ef8d8bac3082a7f7870e9cb384c0dfb9b9ec8f9`.

The initial producer did not read a canonical. Each strict run additionally
binds this exact file in its PRE/POST set. This adoption is not a strict
replay, final B verdict, manuscript edit, build or Round2 freeze.
