# HCS-C266 executable certificate

Run, in order:

```bash
python3 -B c266_skew_brownian_producer.py
python3 -B c266_skew_brownian_checker.py
python3 -B c266_skew_brownian_sympy_crosscheck.py
python3 -B c266_skew_brownian_replay.py
python3 -B c266_skew_brownian_mutation.py
python3 -B c266_release_manifest.py
```

The checker and symbolic reconstruction import no producer module.  The replay
uses a fresh output path, and all semantic hostile mutations repair the outer
payload hash before they are presented to the checker.  The literal scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
