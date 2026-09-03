# P169 claims--evidence ledger

**Freeze:** anonymous author Round 0  
**Gate:** `GREEN_OWNER_THIN`  
**Lifecycle:** `HOLD_EXTERNAL`

## Frozen claim ledger

| ID | Frozen claim | Analytic dependency | Exact-control dependency | Status |
|---|---|---|---|---|
| C1 | Successor transfer preserves canonical block order and is exactly simultaneous last-occurrence increment on restricted-growth words | retained minima and adjacent-block comparison; first-occurrence order | every partition through `n=10` maps to an RGF with the same `k` | proved and checked |
| C2 | The load projection reaches the binary regime by `m-1` for `m<=k` and the everywhere-positive regime by `k-1` for `m>=k` | periodic height lift, explicit max-plus solution, cone implications | 532,467 bounded queue-cone cases | proved and checked; load mechanism is zero-credit background |
| C3 | After smoothing, the labelled prefix/suffix window settles within `k-1` steps | dense final-window queue; sparse excess/hole prefix | every state through `n=10` | proved and checked |
| C4 | For `1<k<n`, the sharp stratum clock is `min(n-2,2k-2)`; `k=1` and `k=n` are fixed; the global clock is `n-2` for `n>=2` | C2--C3 and the explicit family `0^(n-k+1)12...(k-1)` | every stratum through `n=10`; family through `n=50` | proved and checked |
| C5 | Dense and sparse recurrent states have the stated prefix/suffix normal forms | forward-invariant smoothing and labelled-window conditions; converse last-occurrence action | recurrence equivalence for every state through `n=10` | proved and checked |
| C6 | Every nontrivial recurrent `k`-block state has exact period `k`, with counts `k!S(n-k,k)` and `(k)_(n-k)`; the descriptions agree at `n=2k` | cyclic increment on a nonempty terminal permutation/injection; direct counting | all recurrent states and periods through `n=10` | proved and checked |
| C7 | The five-state matrix product gives the fibre of every canonical target and trace positivity is the exact image test | cyclic selected maxima, retained extrema, donation test, linear minimum order, bijective reconstruction | every one of 26,442 targets through `n=9` | proved and checked |
| C8 | The inverse axis is not a function of ordered block size/minimum/maximum data | explicit matrices and predecessor reconstruction | `025|134` has fibre 2; `035|124` has fibre 1 | proved and checked |
| C9 | The formula handles `n=1`, `k=1`, `k=n`, `n=2k`, singleton deletion, and cyclic wrap exactly | explicit boundary clauses and the omission of a false wrap minimum comparison | exhaustive carrier/fibre checks in tested ranges | proved and checked |

## Exact theorem ceiling

The manuscript may state C1--C9 only for the literal simultaneous
maximum-to-successor rule.  It does not assign independent value to:

- the restricted-growth encoding or Stirling enumeration;
- whirling on restricted-growth functions;
- threshold-one directed-cycle parallel chip firing;
- Bulgarian-solitaire pile smoothing;
- promotion, jeu de taquin, rowmotion, or toggle mechanisms;
- box-ball carriers and soliton structure;
- deterministic set-partition stack sorting;
- generic finite-state transfer products or trace closure.

The load factor alone cannot establish C3, C5, or C7--C8.  The fibre trace is
not a size-only recurrence: its entries use comparisons between actual labels
in adjacent target blocks.  Conversely, the five-state inverse calculation is
not used in the clock proof.

## Boundary ledger

| Boundary | Frozen behavior |
|---|---|
| `n=1` | unique one-block/all-singleton state, fixed, fibre one |
| `k=1` | the unique one-block partition is fixed; fibre one |
| `k=n` | the all-singleton partition is fixed; the all-absent state path in the matrix product has weight one |
| `n=2k` | dense and sparse forms both read `01...(k-1)` followed by a permutation; both counts equal `k!` |
| target singleton block | selecting its sole element leaves an empty retained part and gives an all-zero next row, so it cannot be the whole image of a donated token |
| cyclic wrap | donations use indices modulo `k`; only `i<k-1` imposes a canonical-minimum comparison; the trace identifies outgoing state `k-1` with incoming state `0` |

## Reproducibility evidence

```text
verifier: verify_p169.py
frozen transcript: verification_output.txt
assertions: 1,217,025
carrier sweep: all set partitions through n=10
fibre sweep: all 26,442 targets through n=9
queue-cone cases: 532,467
sharp-family sweep: all nontrivial strata through n=50
decision: AUTHOR_ROUND0_PASS
external status: HOLD_EXTERNAL_OWNER_THIN
```
