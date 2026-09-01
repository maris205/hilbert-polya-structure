# Test report

| Gate | Command | Result |
|---|---|---|
| producer | `python3 -B code/c276_random_mapping_producer.py` | PASS, 873,612 maps / 196 enumeration cells |
| independent checker | `python3 -B code/c276_random_mapping_checker.py` | PASS, 821 assertions |
| SymPy | `python3 -B code/c276_random_mapping_sympy_crosscheck.py` | PASS, 918 checks |
| byte replay | `python3 -B code/c276_random_mapping_replay.py` | PASS, 118,171 bytes |
| hostile mutation | `python3 -B code/c276_random_mapping_mutation.py` | PASS, 24/24 rejected |

Every command was run with `PYTHONDONTWRITEBYTECODE=1`.  The checker imports no
producer code and uses an independently designed every-orbit reconstruction.
The mutation suite recomputes `payload_sha256` after every change before asking
the checker to reject it.
