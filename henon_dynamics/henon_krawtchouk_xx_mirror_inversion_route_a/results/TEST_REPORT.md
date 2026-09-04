# Test report — HCS-C366

Run from the package root:

```bash
python -B code/c366_krawtchouk_xx_producer.py
python -B code/c366_krawtchouk_xx_checker.py
python -B code/c366_krawtchouk_xx_sympy_crosscheck.py
python -B code/c366_krawtchouk_xx_replay.py
python -B code/c366_krawtchouk_xx_mutation.py
python -B code/c366_release_manifest.py
```

Expected status: all six commands print `PASS`.  The release gate additionally
checks `-O` and `-OO` refusal, strict evidence/YAML serialization, exact
payload membership, three deterministic PDF rounds, embedded/subset fonts,
text extraction, rasterization, and the forbidden-claim firewall.

Final lane ledger before manifest closure:

- producer: 65,534 subset states, 66 spectral rows, 231 endpoint cells, and
  136 Gaussian-polynomial rows;
- independent checker: 877,612 assertions;
- SymPy: 4,001 exact identities;
- replay: 14,106,891 byte-identical bytes in each of two temporary roots;
- hostile suite: 100/100 rejected, comprising 81 repaired-hash cases, one
  stale-hash control, duplicate/nonfinite JSON, and 16 strict-YAML cases;
- optimized-mode gate: every executable refuses both `-O` and `-OO`.
