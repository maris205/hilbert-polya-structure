# C167 test report

| gate | result |
|---|---|
| canonical producer | PASS |
| producer-independent checker | PASS, 1,362 assertions |
| separate SymPy reconstruction | PASS, 28,585 checks |
| canonical byte replay | PASS |
| repaired-hash semantic mutations | PASS, 30/30 rejected |
| stale payload-hash mutation | PASS, 1/1 rejected |
| all-α proof versus finite-sentinel boundary | PASS |
| scope firewall and Route-B prohibition | PASS |

Commands are listed in `paper/COMPILE_REPORT.md` and `code/README.md`.  The
final release audit reruns every executable on the checked-in bytes.
