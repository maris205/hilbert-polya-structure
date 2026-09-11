# Focused scout: nullity-feedback Jordan powers

Verdict: **`KILL_INTERNAL_P137_PLUS_ROOT_OWNER`**  
External lifecycle: **`HOLD_EXTERNAL`**  
Paper allocation: **none**

## Outcome first

The literal system is mathematically exact and has a clean Sylvester-speed
absorption law.  Independent enumeration also found and proved the correct
boundary omitted by the initial guess: the cyclic partition is deepest for all
`n` but is not always uniquely deepest.  A fixed-exponent integer-flow atlas
counts every one-step target fibre, and the zero target is a provable maximum
fibre.

The candidate nevertheless fails the paper threshold.  Nilpotent fixed-power
inverse classification is directly owned by matrix-root literature, especially
Öztürk (2021).  More importantly, P137 already has the same partition carrier,
current-length feedback, absorption/clock spine, cyclic extremizer, and
every-target coefficient/image theorem.  The new all-time inverse attempt never
became more than conditional coefficient extraction.  The surviving feedback
clock alone is not enough for P166.

## Literal system

For a nilpotent similarity class `[A]` of size `n`, set

`F([A])=[A^(1+dim ker A)]`.

Nilpotent classes are indexed by partitions `lambda|-n`.  The system is
field-independent at type level.  No representative ambiguity is present.

## Exact theorem signal

The full derivation and proofs are in `DERIVATION_PACKAGE.md` and
`PROOF_PACKAGE.md`.  The strongest findings are:

- `F^t([A])=[A^K_t]` with
  `K_(t+1)=K_t(1+sum_i min(K_t,lambda_i))`;
- unique recurrent zero type `(1^n)` and exact point clock first
  `K_t>=lambda_1`;
- sharp global depth first `t` at which the Sylvester exponent
  `1,2,6,42,1806,...` reaches `n`;
- every deepest type classified by an explicit tail recursion;
- for global depth `D>=1`, the cyclic type is uniquely deepest iff
  `n<=2^(2^(D-1))`, with first extra witness `(n-1,1)`;
- a necessary-and-sufficient quotient/residue integer flow and exact multiset
  product for every fixed-length one-step fibre;
- zero-target fibre
  `[q^n] sum_(ell>=1) q^ell [2ell choose ell]_q`, and it is maximal.

## Exact signatures

The frozen verifier reports:

- literal matrices over `F_2,F_3`, `n<=8`, all partitions and powers through
  `n+1`: `964` power-type cells;
- temporal identities and deepest classification for all `376,325` partition
  states through `n=43`;
- every target through `n=24`: `151,355` target/exponent cells and `43,228`
  nontrivial flow evaluations;
- `7,124,325` assertions total.

Selected depth signatures:

| `n` | partition states | maximum depth | deepest count |
|---:|---:|---:|---:|
| 5 | 7 | 2 | 2 |
| 7 | 15 | 3 | 1 |
| 16 | 231 | 3 | 1 |
| 17 | 297 | 3 | 2 |
| 42 | 53,174 | 3 | 25 |
| 43 | 63,261 | 4 | 1 |

Selected image-size sequences, starting at time zero:

| `n` | image sizes | zero-target fibre |
|---:|---|---:|
| 5 | `7,3,1` | 5 |
| 7 | `15,5,2,1` | 10 |
| 10 | `42,9,2,1` | 28 |
| 17 | `297,32,3,1` | 184 |
| 24 | `1575,88,4,1` | 948 |

## Threshold decision

The requested two-axis threshold is not met after subtraction:

1. **Temporal axis:** survives mathematically, but is architecturally adjacent
   to P137.
2. **Inverse/structural axis:** fixed-power root classification is owned; the
   all-time refinement is only a computable coefficient.

Accordingly the honest decision is **KILL**, not an amber reserve.  The exact
work is retained solely as a negative discovery record and boundary reference.

