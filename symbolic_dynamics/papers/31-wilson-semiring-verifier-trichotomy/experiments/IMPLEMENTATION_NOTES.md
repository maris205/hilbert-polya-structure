# SD-C33 implementation notes

## Provenance

- Research package SHA-256:
  `d531e13e2c94972b4c38b7df0a9b070da7f04eb80d1f533b433edf16b0937a68`.
- Prototype source SHA-256:
  `01005ee0f7d10a97de9978f6f512596f6146d21abe0302bab61d459892fe86a5`.
- Prototype 14-artifact ledger SHA-256:
  `100490afb62c6302329db814a856782d20cf986c608a365b9a72fb848fc5a0cd`.
- Prototype aggregate payload:
  `100490afb62c6302329db814a856782d20cf986c608a365b9a72fb848fc5a0cd`.

## Physical source separation

`code/wilson_core.py` contains only the source remainder scan and Wilson
residue/acceptance recurrence. `code/independent_evaluator.py` imports neither
that module nor the generator; it implements trial division and independent
residue reconstruction from serialized ledgers. The generator may compute
reference columns for prototype parity, but the integrity gate trusts only
the separately recomputed evaluator output.

Candidate-source AST inspection forbids prime/factorization/target-zero and
file/network identifiers. The three audited candidate functions contain only
integer literals `0,1,2`.

## Run order

Each isolated fresh run executes generation, independent evaluation, exact
tests, and bounded analysis. The seven legacy JSON artifacts remain
byte-identical to the cutoff-4096 prototype. The seven CSV artifacts retain
identical parsed rows after the sole canonical bridge normalization from the
prototype writer's CRLF to authority LF. `evaluation.json` and `analysis.json`
are new authority layers. Only after all 16 outputs match between fresh runs
are they published to `results/`.

The runner then writes environment, parameter, research, prototype-equivalence,
and inventory metadata; validates Route-A v0.2 and source separation; and
freezes exactly 31 code/result hashes.

`code/test_wilson.py` defaults to the authority `results/` directory, so it
also passes when invoked directly by pytest. `code/run_tests.py --results`
overrides that default for each isolated fresh directory and emits the frozen
18-test JSON report.

The inventory gate removes `integrity_audit.json` and `SHA256SUMS.txt` from
both actual and expected inventories. Consequently the same audit command is
valid before those self-generated files exist and after the complete tree has
been frozen. The direct-pytest regression runs the complete-tree command and
requires exit status zero plus a serialized `PASS` verdict.

## Ownership firewall

The recurrent Wilson adjacency is the primary object and is noncompact for
every nonnegative exact-clock allocation. Its marked product is formal
periodic-orbit data, not an ordinary determinant. The first-return diagonal is
trace class only for `Re(s)>1` and changes `z^(p-1)` to `z`. The transient
verifier prunes to accept loops for any total support predicate. Neither
comparison object repairs the primary operator.
