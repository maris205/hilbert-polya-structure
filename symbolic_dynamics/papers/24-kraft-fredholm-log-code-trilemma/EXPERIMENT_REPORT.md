# Experiment Report — SD-C26

## Outcome

The exact suite supports the strict closure verdict

`(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`

with `ROUTE_A_REJECTED` and Route B locked. No target-zero or target-root data
were used.

The result is a scoped Kraft--Fredholm trilemma: a finite local code can
visibly separate a literal positive prime-only ledger, but positivity and
unique factorization then force the prime cycles to be vertex-disjoint;
finite-code counting supplies logarithmically long cycles, and total roof
(log p) forces the whole counting-space adjacency to be noncompact.

## Exact result census

| Audit | Result |
|---|---:|
| finite-code rows | 112 |
| disjoint positive-roof rows | 672 |
| shared prime-pair firewalls | 28 |
| shared-trie rows | 28 |
| mixed primitive-necklace rows | 112 |
| exact symbolic trie determinants | 4 |
| marker rows | 20 |
| arbitrary architecture/inventory rows | 84 |
| diagonal escape rows | 28 |
| factorization-renewal rows | 4 |
| finite-prefix stationarization rows | 140 |
| finite-roof rank rows | 5 |
| tests | 35/35 PASS |

Every marked binary/Elias word has exactly one visible return marker over the
fixed alphabet `{0,1,#}`. All 112 finite-code rows have zero cyclic collision,
zero candidate target calls, and exact finite-word capacity certificates.
The payload prefix/Kraft fields are controls only; the theorem requires
finite visible orbit separation, not prefix freeness.

## Positive roof and whole-operator firewall

For a weighted cycle of length (ell), positive roofs totaling (log n)
give singular values (e^{-\sigma\tau_j}). Exact rows verify

\[
 \max_j e^{-\sigma\tau_j}\ge n^{-\sigma/\ell},
 \qquad
 \|L_{n,\sigma}\|_1\ge \ell n^{-\sigma/\ell}.
\]

At the prime witness (8191), the marked Elias-gamma cycle has length 26.
Equal roof at (sigma=1) gives maximum singular value
`0.70711010127182405` and block (S_1)-norm
`18.384862633067424`. Concentrated and deterministic hashed positive roofs
also satisfy the allocation-independent lower bounds. Finite rows audit the
formula; the proof combines it with finite-code counting and disjointness to
establish infinite noncompactness.

## Shared recurrence and renewal firewall

All 28 distinct-prime pair rows certify that a shared vertex would create a
legal mixed word whose norm (pq) is no prime power. At the trie cutoff 127,
the prime evaluator contains 31 returns. Elias gamma already produces 465,
9,920, 230,640, and 5,725,824 mixed primitive necklaces with two through five
returns. The finite symbolic determinants agree exactly with

\[
 \det(I-zA)=1-F(z),
\]

not a disconnected product of the individual first-return factors.

The concrete trie roof gives every bit edge roof (log2/8) and puts the
positive remainder on its return edge, preserving total (log n). Infinitely
many bit edges retain weight (2^{-\sigma/8}), so this whole trie is
noncompact as well.

The factorization renewal control reaches 496 mixed primitive two-return
necklaces at token cutoff 33, with 156 excess product collisions. The
finite-prefix S-adic controls explicitly separate compact finite matrices
from their noncompact single stationary union; shared level states add mixed
cycles, while acyclic levels have no primitive orbit.

## Marker and arbitrary-inventory controls

Every finite binary/Elias prime cycle has graph-step degree greater than one
and therefore contributes (z^{\ell(p)}p^{-s}), not (zp^{-s}). First return
changes this marker and is not a same-object repair.

The countable one-symbol-per-atom diagonal has the clean degree-one ledger
and is trace class for (Re s>1), but all 28 prime, composite, square,
Fibonacci, random, hash, and decidable diagonal controls pass equally. Across
all three closures, the 84 matched controls have zero selectivity credit and
are labeled `PROVES_TOO_MUCH`. The diagonal is exactly the Paper04/Paper19
selector-tautological boundary, not a new arithmetic mechanism.

## Reproducibility and scope

The canonical runner performs two complete generator, 35-test, and analysis
runs, requires byte-identical code/result snapshots, then checks Route-A
schema, scientific predicates, control characters, caches, and the SHA-256
inventory. Provenance initially uses `PENDING_FIRST_ARTIFACT_COMMIT` under the
documented two-stage freeze; a later metadata-only commit binds the three
commit fields to the immutable first-stage artifact hash.

The theorem excludes neither signed or matrix cancellations, infinite local
alphabets, nonlocal completed-orbit operators, anisotropic spaces, nor all
countable or S-adic systems. This candidate constructs no analytic
completion, critical-line mechanism, self-adjoint carrier, RH implication,
or Route-B object.

