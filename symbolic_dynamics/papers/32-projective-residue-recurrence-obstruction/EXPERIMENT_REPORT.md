# Paper32 exact experiment report — projective residue recurrence obstruction

Candidate: **SD-C34**
Strongest GO: **nonterminal shared-state recurrence with an ordinary
same-object Fredholm determinant**
Strongest STOP: **universal modular-cycle and cusp-diamond composite flood**
Overall: **Route A rejected; Route B locked**

## Outcome

The projective-residue construction clears the two architectural barriers
left by Paper31. Every state participates in overlapping nonterminal
recurrence, and the original uninduced graph-step operator is trace class on
`Re(s)>2`, so it owns an ordinary Fredholm determinant with its free marker
unchanged. It nevertheless fails prime separation before weights: projective
`S^2=R^3=1` on every modulus, and bidirectional cusp sharing creates the
primitive nonbacktracking diamond `n -> 2n -> 6n -> 3n -> n` for every base
modulus.

The static equality `|P^1(Z/nZ)|=n+1` agrees exactly with primality, but using
it to delete composite blocks is a completed terminal selector. The frozen
Route-A tuple is

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_FAIL,
     A2_ANALYTIC_DETERMINANT,
     A3_FAIL,
     A4_FAIL).

## Canonical exact census

| Surface | Exact result |
|---|---:|
| moduli `2..192` | 191 |
| prime moduli | 43 |
| prime-power composites | 14 |
| mixed composites | 134 |
| composite recurrent blocks | 148/148 |
| static selector equivalence | 191/191 |
| matched finite-semiring transports | 191/191 |
| generic `C2*C3` actions with recurrence | 48/48 |
| cusp diamonds with composite top | 31/31 |
| trace orders | 1 through 8 |
| exact artifact tests | 13/13 PASS under direct pytest and isolated runner |
| source-separated evaluator | 4,819,026/4,819,026 PASS |

Every matched row represents independent reconstruction of all `n^2`
addition entries, all `n^2` multiplication entries, and both projective edges
at every state. Hashes make the serialized certificate compact; the evaluator
does not trust candidate booleans and imports neither candidate module.

## Analytic ownership

At `sigma=Re(s)>2`, the within-modulus trace norm is bounded by

    2 sum_{n>=2} psi(n)n^{-sigma}
    <= 2 zeta(sigma)zeta(sigma-1),

while the bidirectional rank-one cusp terms are bounded by

    2(2^{-sigma}+3^{-sigma}) sum_{n>=2} n^{-sigma}.

The canonical exact rational rows at `sigma=3,4` are finite implementation
witnesses for this independently proved estimate. Thus
`det(I-zB_s)` is the ordinary Fredholm determinant of the same uninduced
object, entire in `z` and holomorphic in `s` on `Re(s)>2`. It owns the
composite primitive ledger and therefore passes A2 without repairing A1.

## Controls and selector firewall

- The candidate census is prime-blind; arithmetic strata appear only in the
  physically separate evaluator.
- All 14 prime-power and 134 mixed-composite blocks retain universal `S/R`
  recurrence.
- All 48 generic finite actions satisfying the same presentation reproduce
  the overlap mechanism.
- The matched clone transports complete finite-semiring tables and the full
  projective graph for every modulus.
- All 191 static-selector rows prove equivalence to primality and separately
  certify `selector_used_by_candidate=0`.
- The inherited bare polynomial-UFD presentation still fails ordinary
  alphabet addition at `2=1+1`; this is not claimed as universal separation.

## Reproducibility

The evaluator independently checked 2,377,759 additions, 2,377,759
multiplications, and 56,318 projective edges. Six legacy prototype payloads
are byte-identical; the source-oracle certificate is semantically identical
apart from naming the physically separated authority evaluator.

Two isolated authority runs produced the same 16 fresh artifacts byte for
byte. Their aggregate SHA-256 is
`3cc4d3bddb5e771c5b2621110e9499b169359438d88608c36f8dc615ce73c727`.
The final code/result ledger contains 31 verified entries and has SHA-256
`689a73a593f1791e6b2f49836b50cc2a11e5ddb1b91c46053af7aaa495ae4b8f`.
Direct cache-disabled pytest and the isolated runner both pass `13/13`; the
complete frozen-tree audit is idempotent, exits zero, and reports `PASS`.
Every JSON/CSV parses, and LF/control-byte/cache/one-EOF checks pass.

No target-zero datum, modified determinant, first-return ownership transfer,
Route-B operator, or RH claim is used.

## Next obligation

Paper33 may continue only through a source-natural cycle quotient or twist of
this same recurrent object. It must annihilate `S^2`, `R^3`, and cusp-diamond
boundaries before arithmetic labels, prove the complete surviving primitive
ledger, retain the original marker and determinant ownership, and pass
matched-ring plus generic-action controls. A static projector, surviving
universal cycles, or cancellation equally effective on random actions closes
the semiring-residue branch.
