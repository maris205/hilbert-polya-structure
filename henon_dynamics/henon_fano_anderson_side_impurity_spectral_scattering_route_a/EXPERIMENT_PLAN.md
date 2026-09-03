# Exact evidence plan

## Claim-to-receipt map

| Claim | Analytic owner | Finite executable receipt |
|---|---|---|
| Schur resolvent and secular equation | block inversion | symbolic determinant and series identities |
| exactly two physical bound states | endpoint limits and strict monotonicity on the two physical branches | exact rational Sturm counts on 126 parameter rows |
| quartic roots need filtering | branch sign conditions | total-real versus physical-root ledger, including rows with two rejected roots |
| pure-ac band and no singular continuous part | parity/cyclicity; local-uniform Stone inversion; off-band meromorphy; zero edge atom tests | anti-Herglotz sign, density positivity, Schur edge rewrite, and exact boundary-value factors |
| residue normalization | Cauchy-transform representation and `G_dd(z)=1/z+O(z^-2)` | first four exact resolvent moments on 21 rows |
| scattering and Fano zero | stationary matching at the origin | 315 rational `T`, `R`, density-factor rows and 63 Fano-location rows |
| release integrity | fixed schema and file ledger | strict JSON/YAML, replay, mutation, PDF and manifest gates |

## Parameter receipt

- `J in {1/2,1,2}`.
- `epsilon in {-3,-2,-1,0,1,2,3}`.
- nonzero signed `g in {-2,-1,-1/2,1/2,1,2}` for the spectral ledger.
- `cos(k) in {-3/4,-1/2,0,1/2,3/4}` and positive
  `|g| in {1/2,1,2}` for scattering.

All stored numbers are integers or reduced rational strings.  The parameter
grid is an implementation receipt, not a sampling proof.  No finite-volume
eigenvalue computation is allowed to upgrade an infinite-volume claim.

## Independent lanes

1. The producer writes canonical JSON with a self-excluding payload hash.
2. The checker imports no producer and independently rebuilds all rows,
   including a rational Sturm implementation.
3. SymPy independently checks the Schur/density/scattering/moment identities
   and all parameter-row root counts, including the anti-Herglotz boundary
   sign and the vanishing edge-resolvent limits.
4. Replay invokes the producer in two isolated temporary directories and
   requires byte identity with the checked-in evidence.
5. Mutation repairs outer hashes after semantic attacks, attacks every
   evaluator leaf, and separately covers duplicate/nonfinite JSON, YAML
   aliases/anchors/merge keys, authority/status deletion, stale hashes, and
   every field of the six-step spectral-measure proof lock.
6. Every Python lane must explicitly refuse optimized `-O` and `-OO` runs.

## PDF/release gate

Round 0 proves the branch-safe Schur and two-pole theorem.  Round 1 adds the
spectral-measure and scattering atlas.  Round 2 adds every degeneration,
source/collision boundaries, evidence discipline, and Route-A rejection.  Each
round is built twice in fresh directories with the fixed epoch; fonts, text,
rasterization, warnings, revision tokens, and byte identity are checked.
