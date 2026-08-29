# Exact Control Results

Status: **fresh author run PASS**.

## Reproduction

From the paper directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python code/verify.py
```

The verifier uses only the Python standard library, integer arithmetic, and
`fractions.Fraction`. It performs no sampling, floating-point calculation,
network call, or external-package import.

## Stored result

```text
max-plus switching-induced-growth verifier: PASS
exact assertions: 1,183,356
literal words: 131,071 through n <= 16
biased law/PGF horizon: n <= 32
probabilities: 0, 1/7, 1/5, 1/2, 3/4, 6/7, 1
arithmetic: integers and fractions.Fraction only
orientation sentinel: A,A,B product differs from B,A,A
endpoint sentinel: H_n(A^n)=H_n(B^n)=n mod 2
reset sentinel: no reset through length 2; ABA/ABB/BAA/BAB only at length 3
support sentinel: every parity-compatible height is attained
rare-event sentinel: exactly two alternating maximizers for n >= 1
```

Exact stdout, including lane counts, is stored in `code/verify.out`.

## Coverage by lane

| Lane | Coverage | Assertion count |
|---|---|---:|
| literal products | matrix products versus literal vector actions and row maxima | 262,142 |
| five literal gaps | direct gaps/rewards and local formulas | 393,223 |
| strong reward lumping | state and accumulated reward agreement | 262,148 |
| word bounds | parity and exact interval for every exhausted word | 262,142 |
| exact word support | histogram equality, explicit `AA`-block/alternating-suffix witnesses, and interior biased supports | 344 |
| reset words | exhaustive lengths 1--3, four matrices, rank, column gaps, and constant finite-input images | 69 |
| finite PGF | independent DP transform versus powers of `Q_p(y)` | 1,155 |
| biased laws | exact masses, supports, and brute-law comparisons | 546 |
| rare words | alternating maxima and minimum block events | 343 |
| endpoints | empty word, deterministic laws, heights, and powers | 226 plus 3 empty-word checks |
| generators | cycle means, tropical rank, explicit powers | 132 |
| cubic and temperature | determinant, similarity, limiting polynomials | 441 |
| stationary/drift/Poisson/variance/Perron | exact rational identities | 126 |
| structural/DP sentinels | orientation, finite-law totals, and helper preconditions | 316 |

The detailed lane counts sum to 1,183,356 and are machine-printed by the
verifier; grouped rows above combine related lanes for readability.

## Independent implementations

The verifier does not test a formula only against itself.

- Literal max-plus matrix multiplication is compared with literal vector
  action, a manually encoded five-gap table, and a separate lumped table.
- Tropical-rank-one products are exhaustively classified through length
  three; the four reset matrices are checked against their two column gaps
  and constant output gaps on a wide exact finite-input sentinel set.
- Exhaustive word histograms are compared with a dynamic program.
- Every support value has an explicit `(AA)^k` plus alternating-suffix
  witness, independently checked against the reward recursion.
- Biased laws are compared with direct weighted word enumeration on a
  smaller independent horizon.
- Finite PGFs are compared with ordinary powers of the tilted 3-by-3 kernel.
- The CLT variance is checked both from a Poisson/martingale sum and from
  implicit derivatives of the characteristic cubic.
- Negative-temperature normalization is checked by exact diagonal
  similarity, not by numerical eigenvalues.

## Convention and boundary sentinels

- `M_n=X_n⊗...⊗X_1`; the word `A,A,B` and its reversal have different
  product matrices.
- `H_0=0`; the empty product is the max-plus identity.
- Both deterministic endpoints are present among the tested probabilities.
- `p=0,1` laws retain only their positive-mass atom; zero-mass DP states are
  excluded before equality checks.
- Exactly two alternating maximizers are asserted only for `n>=1`.
- No reset occurs through length two; exactly `ABA/ABB/BAA/BAB` reset at
  length three in the fixed chronological orientation.
- Every parity-compatible height is asserted and constructively witnessed.
- Both generator power cycles are checked through exponent 64.

## Evidence limits

The finite checks do not prove the SLLN, CLT, LDP, analytic pressure, or
temperature limits. They do not establish external ownership, novelty,
priority, or independence from undiscovered literature. Those boundaries
are explicit in the manuscript and `CLAIMS_EVIDENCE.md`.
