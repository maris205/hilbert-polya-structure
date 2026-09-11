# P167--P171 cross-domain scout: final disposition

## Outcome first

This lane tested **30 genuinely different literal systems/support kernels**
across permutations, set partitions, words, endofunctions, graphs,
hypergraphs, finite-field geometry, and random supports.  The disposition is:

- **29 KILL**;
- **one provisional survivor:** C06, successor transfer on canonical set
  partitions (STF);
- **zero reserve candidates**.

STF cleared the internal mathematical gate in this scout:

1. on the `k`-block stratum its exact maximum preperiod is
   `min(n-2,2k-2)` for `1<k<n`, hence the global clock is sharply `n-2`;
2. every recurrent state and exact period is classified, with recurrent count
   `k! S(n-k,k)` in the dense regime and `(k)_(n-k)` in the sparse regime;
3. independently, every target fibre is counted by the trace of an explicit
   product of five-state local matrices, and image membership is positivity of
   that trace.

The closest external owners materially narrow the claim: restricted-growth
word whirling already owns this carrier, and directed-cycle parallel chip
firing owns STF's load projection.  No literal owner of the simultaneous
maximum-transfer lift was found in the bounded search.  Accordingly the
correct status is **provisional short-paper candidate**, not “novel theorem”
without a conventional citation-chain search and expert proof check.

## Why this is not a carrier repaint

The temporal proof deliberately uses the occupied load factor, but the fibre
theorem cannot be recovered from that factor.  Targets with the same ordered
block sizes, minima, and maxima can have different fibres (`025|134` has fibre
two while `035|124` has fibre one).  The five-state matrices retain labelled
interlacing discarded by the queue factor.  This is also why the other
set-partition candidates were killed: their entire signals reduced to prior
split/merge/sorting machinery.

## Verification record

Two deterministic, dependency-free programs are supplied.

```bash
python docs/papers167_171_sequence/scouting/combinatorial_crossdomain/breadth_pilots.py
python docs/papers167_171_sequence/scouting/combinatorial_crossdomain/verify_stf.py
```

The breadth program reports 76,363 assertions.  The focused program reports
1,217,023 assertions and checks:

- all set partitions through `n=10` for the clock, recurrent forms, periods,
  and counts;
- 532,467 bounded max-plus queue cone cases;
- all 26,442 targets through `n=9` against literal predecessor enumeration;
- the sharp witness in every nontrivial stratum through `n=50`.

Both programs were run twice and their outputs were byte-identical.  The exact
transcripts are `BREADTH_CANONICAL.txt` and `STF_CANONICAL.txt`.

## File map

- `IDEA_LEDGER.md`: complete 30-candidate ledger and every kill reason;
- `STF_DERIVATION.md`: theorem statements and proofs, including the
  five-state fibre matrices;
- `OWNER_SEARCH_LOG.md`: query record, primary sources, external owner
  subtraction, and P1--P166 collision audit;
- `breadth_pilots.py`, `BREADTH_CANONICAL.txt`: breadth falsification code and
  exact output;
- `verify_stf.py`, `STF_CANONICAL.txt`: focused exact verifier and exact output.

No paper directory, shared top-level file, or Git state was modified by this
lane.

## Promotion recommendation

Promote only STF to the parent review pool.  Its defensible paper-shaped core
is the conjunction of the labelled sharp clock/recurrent classification and
the full-target five-state fibre trace theorem.  Do not promote the load
factor alone, do not call the map whirling or promotion, and do not use any of
the 29 killed systems as a fallback.  If the parent standard regards a fixed
five-state trace product as merely an algorithmic inverse rather than an exact
structural fibre formula, demote STF and record this lane as **KILL ALL**.
