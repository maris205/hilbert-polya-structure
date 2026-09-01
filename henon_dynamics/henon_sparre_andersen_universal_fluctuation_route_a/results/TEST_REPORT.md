# Test report

| Gate | Command | Result |
|---|---|---|
| producer | `python3 -B code/c273_sparre_andersen_producer.py` | PASS, 41 rows / 561 cells / 695,482 histories |
| independent checker | `python3 -B code/c273_sparre_andersen_checker.py` | PASS, 528 assertions |
| SymPy | `python3 -B code/c273_sparre_andersen_sympy_crosscheck.py` | PASS, 411 checks |
| byte replay | `python3 -B code/c273_sparre_andersen_replay.py` | PASS, 48,872 bytes |
| hostile mutation | `python3 -B code/c273_sparre_andersen_mutation.py` | PASS, 24/24 rejected |

Every command was run with `PYTHONDONTWRITEBYTECODE=1`.  The checker has no
producer import.  The mutation suite recomputes `payload_sha256` after each
change before it asks the checker to reject the evidence.
