# Code

`c58_tail_parity.py` builds the primary exact certificate.  It reconstructs
the three reflection closures, eliminates the coordinate variable, proves
total reality by Sturm counts, locks modular irreducibility, identifies four
physical embeddings in rational boxes, and certifies the signs of
`Delta_6` and `Delta_7` by integer products.

`independent_check.py` reconstructs the factor/resultant/root-count and
integer-product data without importing the primary checker.  `test_c58.py`
checks the emitted schema and claim firewall.

Run all checks with:

```bash
bash code/run_c58.sh
```
