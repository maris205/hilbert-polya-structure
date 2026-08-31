# Exact control — P131

The paper-local verifier has three explicit engines: canonical digit words,
exact rational `Fraction` values followed by literal subtractive Euclid, and
the normalized raw-`L/R`-string self-map `Psi`.  The last engine updates full
strings without first replacing them by run-length tuples.  It imports no
proof-spike code and uses no randomness.

Every state of every level `2<=N<=18` is exhausted.  The verifier checks the
continued-fraction/path run identity, the full-string conjugacy
`E(Phi(q))=Psi(E(q))`, raw-string terminal cores and both raw inverse
branches, exact tails and periods, every depth bin, every target's digit
inverse branches, Garden/image counts, recurrent rotation orbits, and fixed
counts.  It passed **6,101,926 exact assertions**.

Canonical hashes after Hostile Review A repair:

```text
94939887128cf0d487e6b054d5113c3fcd6f0921c880c07de5351a5b5eb9d07a  code/verify.py
caa4df1e70fd2bdb86aa5aeb1308c2baa74b5d5e560d73980f1f6886c91bc8c6  code/verification_output.txt
```

A fresh stdout must byte-match `code/verification_output.txt`.  The finite
range is counterexample pressure, not an all-level proof or novelty result.
