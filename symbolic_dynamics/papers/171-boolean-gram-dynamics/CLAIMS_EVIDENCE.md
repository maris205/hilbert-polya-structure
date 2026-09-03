# Claims and evidence ledger — P171

**Decision:** `AUTHOR_ROUND0_PASS`  
**Owner status:** `GREEN_OWNER_THIN`  
**External status:** `HOLD_EXTERNAL`

Finite computation below is counterexample pressure only.  Uniform claims
are credited to the proofs in `main.tex`.

| ID | Claim | Uniform support | Exact computational control | Boundary pressure |
|---|---|---|---|---|
| T1 | For `G=AA^T` and `t>=1`, `Gamma^t(A)=G^(2^(t-1))`. | Symmetry after the first step and induction in Theorem 1. | Every source for `n<=4`, times 1--4, literal iterate versus independently exponentiated Boolean power. | Includes zero, nonsymmetric sources, and already-fixed sources. |
| T2 | Endpoint is the fully looped clique completion of each active component. | Walk/distance interpretation with loop padding in Theorem 1. | Every source for `n<=4`; endpoint checked partial-equivalent and fixed. | Inactive zero rows remain unlooped isolates; active singleton components retained. |
| T3 | Exact clock is zero on fixed states and otherwise `1+ceil(log2 D(G))`, with logarithmic term zero for `D<=1`. | Distance threshold at time `t` is `2^(t-1)`. | Every source for `n<=4`, direct first-stable time versus graph diameter. | Explicit `D=0` and `D=1` sources; `n=1`. |
| T4 | Sharp carrier height is zero at `n=1` and `1+ceil(log2(n-1))` for `n>=2`. | Universal diameter bound plus path-incidence source. | Full carriers `n<=4`; path family through `n=64`. | `n=2` witness has depth one; unused final column is allowed. |
| T5 | Recurrent states are precisely partial equivalence relations and all are fixed. | Fixed equation gives symmetry, active reflexivity, and transitivity; converse by symmetric idempotence. | Full carrier/codomain `n<=4`. | Zero relation and arbitrary inactive set. |
| T6 | Fixed count is `sum_k binom(n,k)B_k=B_(n+1)` and zeta is `(1-z)^(-B_(n+1))`. | Choose active set then partition; distinguished-element Bell bijection; all periodic points fixed. | Exact fixed census `2,5,15,52` for `n=1,2,3,4`; Bell identity checked through `n=15`. | Empty active set included. |
| F1 | Invalid nonsymmetric targets or edges without endpoint loops have empty fibre. | Every Gram output is a loop-compatible symmetric relation. | Every one of all `2^(n^2)` targets for `n<=4`. | Explicit unlooped two-way edge target. |
| F2 | Compatible target fibre is `sum_S (-1)^|S| c_H(S)^n`. | Ordered column supports and inclusion--exclusion in Theorem 2. | Formula versus literal predecessor histogram for every compatible target `n<=4`. | Empty and repeated columns, isolated loops, zero target. |
| F3 | Image iff loop/edge atoms have an allowed clique cover of size at most `n`. | Column-square union and empty padding. | Independent bounded cover reachability versus positive fibre for every target `n<=4`. | Looped `K_(2,3)` at `n=5` gives a compatible zero fibre obstruction. |

## Frozen census

| `n` | sources | image | fixed | depth histogram | max fibre |
|---:|---:|---:|---:|---|---:|
| 1 | 2 | 2 | 2 | `0:2` | 1 |
| 2 | 16 | 5 | 5 | `0:5, 1:11` | 7 |
| 3 | 512 | 18 | 15 | `0:15, 1:407, 2:90` | 175 |
| 4 | 65,536 | 113 | 52 | `0:52, 1:34272, 2:29340, 3:1872` | 17,887 |

## Reproduction contract

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 verify_p171.py
assertions: 594,955
terminal decision: AUTHOR_ROUND0_PASS
external marker: HOLD_EXTERNAL_OWNER_THIN
```

The verifier imports no scouting file, old verifier, generated data, or paper
module.  Two fresh-process replays must match `verification_output.txt` byte
for byte before the Round-0 freeze.
