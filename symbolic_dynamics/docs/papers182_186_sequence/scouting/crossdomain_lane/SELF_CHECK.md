# Self-check protocol

The evidence is intentionally reproducible without third-party packages.

1. `verify_crossdomain.py` exhausts the declared small carriers and emits a
   deterministic transcript.  Its current transcript ends with
   `ASSERTIONS=221585` and `RESULT=PASS`.
2. `self_check.py` launches the verifier in **two new Python processes**.  It
   requires both stdout byte streams to equal each other and
   `CANONICAL.txt`; any stderr is a failure.
3. It then parses `SHA256SUMS`, requires exactly the documented lane files,
   requires the manifest to exclude itself, and recomputes every digest.

The verifier covers:

- every loopless digraph through `n=4` for RICS one-step fixed/conflict/fibre
  claims, and every conflict graph through `n=4` for all history lengths
  `0,...,n` in the absorption and first-order endpoint formulas;
- 25 CGT prime-power carriers (`2^1` through `2^9`, `3^1` through `3^7`,
  `5^1` through `5^5`, and `7^1` through `7^4`) for every state, target,
  orbit, tail, period, cycle, and fibre;
- every nonempty subset of binary `d`-words through `d=4` for the SSC depth,
  shell, image, and one-step fibre identities, plus all histories through
  `t=d+2` for `d<=3`.

These are finite theorem checks, not proofs of the unbounded statements and
not novelty evidence.

