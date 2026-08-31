# Paper plan — P127

## Claim spine

The paper studies one literal map on looped labelled digraphs, equivalently
on `M_n(F_2)`:

```text
Phi(A) = A^T + (A1)(A1)^T.
```

The theorem spine is deliberately narrow.

1. The row/column/total-parity quotient sends every state to the even-total
   hyperplane in one step and swaps the two margins thereafter.
2. The even hyperplane is exactly the recurrent set; odd-total states have
   exact depth one; recurrent periods are exactly among `1,2,4`.
3. Every codomain fibre has size `0`, `1`, or `2^(n-1)+1`, with an explicit
   margin criterion.
4. Fixed points, 2-cycles, 4-cycles, depth-one states, and the finite zeta
   function have closed formulas.

## Proof architecture

- Route I: direct parity-margin dynamics, followed by an explicit affine
  parametrisation of matrices with prescribed margins.
- Route II: the factorisation
  `(I + r 1^T) A^T`, where the left factor is the identity or an involutory
  transvection on the even coset and a rank-`n-1` projection on the odd
  coset.  The product `L_c A L_r^T` independently recovers the second and
  fourth iterates.
- The paper-local verifier reconstructs both routes and exhausts all matrices
  for `1 <= n <= 4`; finite checks are falsifiers, never proof.

## Mandatory subtraction

Transpose, rank-at-most-one updates, binary margin counting, static local or
subgraph complementation, transvections, and finite-map zeta bookkeeping are
zero-credit background.  The residual is only their exact conjunction for
the recomputed odd-outdegree update above.  P102/P103/P125 receive explicit
internal zero credit.  No novelty, priority, or external-release claim is
made.

## Boundary cases

All main theorems assume `n >= 1`; `n=0` is a separately fixed empty state.
The fibre theorem quantifies over the entire codomain, so odd-total targets
have zero preimages.  “Rank-at-most-one” is used throughout.
