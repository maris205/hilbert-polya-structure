# Executable evidence plan

## Frozen contract

- Candidate: `HCS-C291`
- Source commit: `7fbe9db30cc460a82883533d7cfb2edd988c5b65`
- Date / epoch: `2026-09-02` / `1788307200`
- Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`
- Obstruction: `HEN-O275`
- Route tuple: `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`

## Evidence lanes

1. **Producer lane.**  Reconstruct path PGFs through `n=20` from the
   first-edge convolution, exact first two factorial moments through `n=200`,
   path order-count tables through `n=10`, cycle tables through `n=9`, and
   canonical decimal asymptotic cells at `n=20,50,100,200`.  Use `Fraction`
   arithmetic and canonical JSON hashing.
2. **Independent checker lane.**  Reject duplicate keys, nonstandard JSON
   constants, unknown/missing keys, bool-as-int confusion, incomplete/duplicate
   row families, and any contract drift.  Enumerate all labeled edge orders by
   a processed-edge/matched-vertex bitmask DP, without importing the producer.
   Separately reconstruct every stored factorial moment through the general
   conditional falling-factorial triangle.
3. **Symbolic lane.**  Use SymPy to verify the Riccati specialization, `H_1`
   and `H_2` ODEs, the Laurent-pole algebra giving `e^{-4}`, coefficient-level
   finite controls, and shifted cycle support identities.
4. **Replay lane.**  Copy the producer to two unrelated temporary package
   paths and require both fresh outputs to equal the release evidence byte for
   byte.
5. **Hostile lane.**  Repair the payload hash after semantic/schema attacks;
   require rejection of altered theorems, moments, support, collision and Route
   contracts, drops, duplicate replacements, stale hash, raw duplicate keys,
   and `NaN`.
6. **Paper lane.**  Compile rounds 0, 1, and 2 twice each in isolated
   directories under fixed epoch.  Require byte identity, embedded/subset
   fonts, clean settled logs, distinct round hashes, readable text contracts,
   and visual inspection.
7. **Release lane.**  Hash exactly 27 payload files, exclude the manifest from
   its own ledger, assert exactly 28 physical files, rerun every executable
   gate, and rewrite/verify the manifest idempotently.

## Epistemic boundary

The finite rows can falsify an implementation.  The all-`n` theorem rests on
the first-edge decomposition, formal OGF identities, analytic coefficient
extraction, and binary-gap support proof written in the paper.
