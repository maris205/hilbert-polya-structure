# Exact control results — P108

Canonical command:

```bash
python3 code/verify_capped_fibonacci.py
```

The standard-library script enumerates every state for caps `a=1..220`.
It compares literal iteration with the closed Fibonacci formula at every
registered time, independently reconstructs the depth histogram and CDF,
and builds a reverse table for every one-step fibre.

The final assertion count and byte-identical stdout are frozen in
`code/verification_output.txt` after the final run.  The exhaustive finite
control checks conventions and endpoints; the quantified theorem rests on
the analytic proof in `main.tex`.
