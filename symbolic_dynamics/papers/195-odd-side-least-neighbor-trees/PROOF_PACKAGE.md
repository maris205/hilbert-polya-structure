# Proof package — P195

## Frozen assumptions

- The underlying object is a simple labelled tree on `[n]`.
- The distinguished root is the only changing state.
- A neighbour is eligible iff its component after deleting the incident edge
  has odd order; the least label is chosen.

## Proof dependencies

1. For odd `n`, the two edge sides have opposite parity, producing a one-way
   orientation and fixed sinks.
2. For even `n`, eligibility is symmetric. The parity of the sum of branch
   sizes proves every degree in the odd-cut subforest is odd; forest cycles
   force functional periods two.
3. Odd tails follow nested odd side sizes decreasing by at least two. Even
   tails use one distinct off-path witness for every internal orbit vertex.
4. Odd fixed roots are `Z * SET(T_even)`. Even recurrent orientations split
   into two odd rooted sides weighted by inverse numbers of odd root branches.
5. A predecessor is either the fixed target itself or a neighbouring root
   for which the target is the least eligible neighbour.
6. Branch-size budgets give sharp fibre maxima; stars and two-edge bouquets
   attain them.

## Boundary and repair audit

- `n=1`: one fixed state, depth zero, fibre one.
- `n=2`: one edge gives one 2-cycle; maximum tail zero and fibre one.
- A connected component of `H(T)` can contain multiple mutual-minimum edges.
  No theorem uses component-level uniqueness.
- The even recurrent EGF counts ordered oriented cut sides, hence rooted
  recurrent states, not components of `H`.
- The two label-comparison sets after cutting a mutual edge are disjoint;
  relative orders on disjoint label subsets are independent.

## Exact falsifier

The verifier enumerates every Prüfer code through `n=8`, computes all
oriented side sizes, constructs the literal root map, and independently
checks direct fibres, depths, periods, maxima, EGF coefficients, and depth
histograms. Computation is not proof or novelty evidence.
