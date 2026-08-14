# Reproduction code

Run the complete compact certificate and independent test suite with:

```bash
bash code/run_c51.sh
```

`c51_abel_germ.py` produces the theorem ledger and finite sentinels.
`independent_check.py` recomputes the symbolic census, constants, packet
sentinels, and adversarial mutations without importing the producer.
