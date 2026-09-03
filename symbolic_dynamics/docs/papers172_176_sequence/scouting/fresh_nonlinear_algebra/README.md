# Fresh nonlinear algebra breadth lane

This lane tests eighteen genuinely different deterministic finite algebra,
group, vector, and matrix dynamics.  Sixteen satisfy the intake exclusion of
valuation/multiplicity erosion, pure power maps, incidence-linear maps, and
closure systems; two retractions remain only as labelled negative controls
and do not count toward that breadth.

## Outcome

- **Sole recommendation:** `M01`, the diagonal-feedback additive commutator
  (A\mapsto[D(A),A]).
- **Correct theorem but killed internally:** `V02`, the cyclic Gram gate,
  because its formed-space quotient/fibre/component engine substantially
  transfers from P125 and the killed `NL03` scout.
- **Other candidates:** sixteen explicit kills; none is held as a disguised
  parameter variant or reserve.
- **External status:** `HOLD_EXTERNAL` throughout.
- **Paper allocation:** none in this directory.

M01's retained two-axis signal is especially crisp: the full forward graph
has universal height two, while a target is reachable exactly when its
undirected nonzero support is (q)-colourable and its fibre is an
occupation-weighted proper-colouring sum.  P119's commutator shell and all
generic Potts/chromatic machinery are zero credit.

## Files

| file | role |
|---|---|
| `verify_scout.py` | standard-library exact exhaustive verifier for all eighteen maps |
| `CANONICAL.txt` | frozen deterministic transcript |
| `M01_THEOREM_PACKAGE.md` | all-(n,q) theorem, proof, all-time fibres, controls, and recommendation |
| `V02_THEOREM_PACKAGE.md` | all-(m) theorem and proof, followed by the decisive P125/`NL03` kill |
| `SCOUT_AND_KILL_LEDGER.md` | literal carrier/update, early signal, and decision for every candidate |
| `COLLISION_FIREWALL.md` | strict P1--P171 proof-engine comparison |
| `OWNER_SEARCH_LOG.md` | dated primary-source search and zero-credit boundary |
| `CONTROL_RESULTS.md` | verifier coverage and canonical signatures |
| `MANIFEST.sha256` | SHA-256 integrity manifest |

## Reproduction

From the workspace root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers172_176_sequence/scouting/fresh_nonlinear_algebra/verify_scout.py
```

The final lines must be

```text
EDGE_DIGEST=ba346c933983b076b55a3560b603017a1f43cdc1f510aea12392eea624dd2098
ASSERTIONS=517353
RESULT=PASS
```

Exact enumeration is a deterministic falsifier, not a proof or an ownership
certificate.  The theorem packages contain the symbolic arguments; the
owner log records only bounded search outcomes.
