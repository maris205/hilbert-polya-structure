# P122 paper plan — residual theorem lock

Status: **PROVED / OWNER-BOUNDED / EXTERNAL HOLD**.

## One-sentence contribution

For simultaneous reversal of even record blocks, determine the sharp global
clock, every one-step fibre, and the all-size image/Garden-of-Eden census.

## Frozen theorem contract

1. If a state changes then it decreases in lexicographic order; hence there
   are no nontrivial cycles.
2. The maximum depth on `S_n` is `n-1`, attained uniformly by
   `(2,3,...,n,1)`.
3. Fixed states are exactly permutations with odd record-block lengths.  The
   transfer to odd cycles and its EGF are classical controls and receive zero
   credit.
4. For each target, preimages are bijective with admissible cut sequences;
   last-cut decomposition gives the exact quadratic-arithmetic fibre DP.
5. Fibre nonemptiness depends only on record positions.  Five Boolean state
   bits, weighted by the classical record-position multiplicities, give the
   image count `I_n` and Garden count `n!-I_n` for every `n`.

## Owner subtraction

- Remmel--Wachs, p. 40: the exact maximum-first cycle-to-record-block
  transformation; Foata--Han supplies related fundamental-transformation
  background.
- Lugo: weighted cycle enumeration and odd-cycle controls.
- Bouvel--Cioni--Ferrari: neighboring pointwise-preimage and functional-tree
  methods for bubblesort.
- Cioni--Ferrari: recursive queuesort preimages and the special
  left-to-right-maximum target class.
- Huang: current record/fibre neighbor in an order-polynomial setting.
- Classical relative-rank encoding: the weight product for a prescribed
  record set.

No contribution is claimed for those interfaces, for finite enumeration, or
for the generic finite-state/segmentation paradigms.  The bounded non-hit for
the literal map is not external clearance.

## Collision firewall

The paper does not market the generic silhouette "permutation dynamics plus
depth plus fibres."  P105 already occupies that silhouette on the same
carrier; P117 and P120 are the closest parity/reversal mechanisms.  The
residual mechanism here is the endpoint-parity admissibility bijection and
its aggregation into a five-bit record automaton.  Literal difference alone
is not counted as value.

## Claim ceiling

No maximum-indegree formula, all-depth-layer formula, iterated-fibre theorem,
minimal-state assertion, asymptotic, novelty, priority, or external-release
claim is permitted.
