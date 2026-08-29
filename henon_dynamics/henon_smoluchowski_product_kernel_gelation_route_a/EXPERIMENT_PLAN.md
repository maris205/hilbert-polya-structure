# Evidence and experiment plan

## Frozen ledger

- Exact Cayley coefficients \(a_k=k^{k-2}/k!\) and their recurrence for
  \(1\le k\le40\).
- Pregel/critical rows at \(t=0,1/10,1/2,9/10,1\).
- Four postgel rows for each of the Smoluchowski/Stockmayer and Flory closures
  at \(t=6/5,2,5,10\).
- Critical-tail controls at \(k=20,50,100,200,500\).
- First 20 cluster equations checked directly per time row at 90 digits.

## Claim-driven gates

1. Verify the exact Cayley recurrence independently of decimal calculations.
2. Reconstruct every coefficient, moment and branch root without importing
   producer code.
3. Check both ODE loss conventions separately; reject any branch swap.
4. Reconstruct tree, moment and balance identities with SymPy.
5. Require clean-process canonical-byte replay.
6. Reject stale hashes, repaired semantic changes, nested unknown material,
   altered provenance/scope and truncated ledgers.
7. Build three content-distinct paper revisions twice at a fixed epoch; check
   logs, embedded subset fonts, extracted text and page images.
8. Close 27 payload files plus one self-excluded manifest.

Finite coefficient rows audit exact identities.  They cannot establish the
infinite critical tail by curve fitting and are never presented that way.
