# P189 claims-to-evidence ledger

| Claim | Proof location | Independent exact pressure |
|---|---|---|
| `F(A)=D(r)`, `F^2(A)=D(r*)`, `F^3(A)=D(r_down)`, `F^4(A)=F^2(A)` and post-height alternation | Lemma 1 and Theorem 2 | every matrix and every entry through `n=4`; two post-height phases checked |
| recurrent states are Ferrers matrices; recurrent action is conjugation | Theorem 3 | exact recurrent-set equality through `n=4`; conjugation involution through `n=9` |
| recurrent, fixed, and strict-two-cycle counts `binom(2n,n)`, `2^n`, and `(binom(2n,n)-2^n)/2` | Theorem 3 | complete functional graphs through `n=4`; partition/self-conjugate census through `n=9` |
| exact depth sets and populations `N_0,N_1,N_2`, with height two for `n>=2` and the `n=1` boundary | Theorem 3 | exact depth of every matrix through `n=4`; two independent formulas for `W_n` compared through `n=9`; coefficient transfer through `n=12` |
| time-one image criterion, every-target product fibre, and `(n+1)^n` image count | Theorem 4 | incoming counter for every one of `2^(n^2)` targets through `n=4`; zero/hole targets and mass checked |
| time-two Ferrers criterion, multiset-assignment fibre, and `binom(2n,n)` image count | Theorem 4 | incoming counter for every target through `n=4`; all Ferrers targets and total mass through `n=9` |
| tempting stronger collapses are false | Section 2 and author attack | explicit `n=2` witnesses for both `F^2 != F` and `F^3 != F` |

The verifier makes **5,336,613** exact assertions and is independent of the
scouting implementation.  These controls support internal correctness only;
they are not proofs of novelty, ownership, priority, or freedom to circulate.
