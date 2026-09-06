# Preserved infrastructure launch failure

Actual command: `python -I -S -B docs/papers204_208_sequence/reviews/p208_b/search_history.py`.
Parent command exit 1. The initial recorder assumed `/usr/bin/rg`; no such
file exists. `subprocess.run` raised FileNotFoundError at the initial
inventory call, before any search child launched or outputs existed.
No history search or mathematical failure is inferred from this stop.
The initial source is retained here verbatim. The empty history_context
directory created before the launch is retained and reused only after
the corrected recorder explicitly checks it is empty.
