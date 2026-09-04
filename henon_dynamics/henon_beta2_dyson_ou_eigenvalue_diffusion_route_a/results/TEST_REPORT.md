# Test report

All commands were run from the package directory under ordinary Python with
assertions enabled.

```text
python -B code/c378_dyson_ou_producer.py
C378 producer PASS: dimensions=16 levels=1040 partitions=16602 kernels=12

python -B code/c378_dyson_ou_checker.py
C378 checker PASS: dimensions=16 levels=1040 partitions=16602 kernels=12

python -B code/c378_dyson_ou_sympy_crosscheck.py
C378 SymPy PASS: exact_symbolic_checks=350 slater_partition_checks=39 heat_trace_coefficients=264

python -B code/c378_dyson_ou_replay.py
C378 replay PASS: bytes=8917819 isolated_runs=2

python -B code/c378_dyson_ou_mutation.py
C378 mutation PASS: killed=63/63 repaired_hash_attacks=39
```

The release lane additionally runs three unittests, `-O` and `-OO` refusal
for all six scripts, three twice-fresh wrapper PDF rebuilds, strictly
increasing page counts, Latin/CJK font embedding, bilingual and round-isolated
text extraction, exact round-specific title locking, source hygiene, firewall
validation, and the exact 38-file payload ledger.
