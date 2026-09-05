# P201 author response: confirmed exact historical OCL conjugacy

Date: 2026-09-05 UTC. Author response only; no independent-review or
acceptance claim. All P201 frozen manuscript/source/bibliography/code/PDF
artifacts are preserved unchanged. External status: HOLD_EXTERNAL.

## Read exact historical implementation

The old file
docs/papers162_166_sequence/scouting/replacement_adaptive_maps/verify_scout.py,
lines 427–438, defines orbit_cycle_length by direct orbit tracing and then

```python
def orbit_length_map(f):
    n = len(f)
    return tuple(orbit_cycle_length(f, i) % n for i in range(n))
```

This is exactly OCL(f)(i)=ell_f(i) modulo n, on the same full zero-based
endofunction carrier. The old SCOUT.md ledger explicitly assigns it
KILL_FUNCTIONAL_GRAPH_SUMMARY_THIN. Its retained canonical row at n=5
has image 60, sole fixed point, maximum tail three and maximum fibre 1296.

## Full conjugacy, all n

Let sigma(i)=i+1 modulo n and let H(f)=sigma composed with f composed
with sigma inverse. This is a bijection on the entire endofunction carrier.
Relabelling preserves cycle lengths and their basins, so for every i,

```text
OCL(H(f))(i)
  = ell_f(sigma^(-1)(i)) modulo n
  = sigma(ell_f(sigma^(-1)(i))−1)
  = H(P(f))(i).
```

Thus OCL composed with H equals H composed with P. The identity includes
ell=n, since sigma(n−1)=0, and n=1, where all maps are the sole state.
It is a complete literal-system conjugacy, not merely a histogram factor,
similar numerical signature, partial restriction, or a shared proof method.

## Binding consequence

The author confirms the review objection without qualification. P201 is
a conjugate of an explicitly killed historical candidate, hence falls
below the central anchor's fresh-system admission threshold. The new sharp
rank hierarchy, critical equality/count and inverse/extremal proofs may be
useful mathematical progress on that old system, but do not make it a new
eligible dynamical subclass under the current batch contract. They must
not be used to bypass the exact-history exclusion.

The earlier author message calling OCL only a close neighbor was incomplete:
it had not recognized simultaneous pointer/domain relabelling. This response
supersedes that interpretation, not the preserved source or manuscript
snapshots. The author requests no promotion on the basis of stronger
theorems, changed labels, amount of work, or the previous five-seat freeze.
The root and independent reviewer should record the actual kill and reopen
the seat. The frozen P201 package remains a truthful record of correct
research on an old conjugate, not a completed accepted fifth paper.
