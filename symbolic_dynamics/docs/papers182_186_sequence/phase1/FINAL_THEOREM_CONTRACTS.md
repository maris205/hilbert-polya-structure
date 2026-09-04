# Frozen theorem contracts — P182–P186

These contracts are the minimum scientific payloads for the five papers.
Finite verification is counterexample pressure; every displayed identity
requires a written all-parameter proof.

## P182 — cyclic subspace-lattice comparator dynamics

Let `L(V)` be the subspace lattice of `V=F_q^d` and set
`F(A,B,C)=(C,A∩B,A+B)`.

The paper must prove:

1. `F^2(A,B,C)=(A+B,C∩A∩B,C+(A∩B))` and `F^4=F^2`;
2. a state is recurrent iff `B<=A` and `B<=C`; on that locus `F` swaps the
   outer coordinates, so fixed points have `A=C` and every other recurrent
   state lies in a strict two-cycle;
3. depth is zero on the recurrent locus, one iff `A∩B<=C` off that locus,
   and two otherwise, with sharp height two;
4. the image is exactly the triples `(C,X,Y)` with `X<=Y`;
5. for such a target, the fibre size is the number of ordered complementary
   pairs in `Y/X`, namely
   `c_r(q)=sum_i [r choose i]_q q^{i(r-i)}`, where `r=dim(Y/X)`;
6. exact Gaussian-sum formulas for the image, fixed, recurrent, and strict
   two-cycle populations.

## P183 — random incoming-copy symmetrization

The paper must prove:

1. selecting `v` deletes exactly the `v`-star of the current conflict graph;
2. symmetric digraphs are exactly the recurrent states and are absorbing;
3. the number of length-`t` absorbing vertex words is
   `sum_{M independent in H(A)} (n-|M|)! S(t,n-|M|)`;
4. the endpoint kernel refines support by first-occurrence order, with exactly
   `S(t,|S|)` histories per prescribed order;
5. if `k(B)` is the isolated-vertex count of the target conflict graph, the
   labelled one-step fibre is `k(B)2^(n-1)` and the distinct-source fibre is
   zero for `k=0`, otherwise `1+k(B)(2^(n-1)-1)`.

## P184 — co-gcd translation on prime powers

For `N=p^a`, set `T(x)=x+N/gcd(x,N) mod N`.  The paper must prove:

1. low valuation `2v<a` is recurrent with exact period `p^v`;
2. high valuation `2v>a` has tail one and lands at valuation `a-v`;
3. when `a=2h`, the equality layer has the explicit unit-increment conveyor,
   tail `p-(u mod p)+1`, and the stated landing period (written without
   ambiguity in the manuscript);
4. the complete cycle and tail censuses, including `p=2` and `x=0`;
5. image defect `p^floor((a-1)/2)`, fibres only of sizes `0,1,2`, equal empty
   and double counts, and the exact double-target criterion.

The manuscript must normalize the middle-layer notation carefully: if
`r=p-(u mod p)`, the tail is `r+1`.

## P185 — prefix-diversity delay

For `P(w)_i=|{w_0,...,w_{i-1}}|` on `[n]^n`, the paper must prove:

1. the exact pointwise formula for every `P^t(w)`;
2. `im(P^t)` and `|im(P^t)|=2^(n-t-1)` for `1<=t<=n-1`;
3. the identity word is the unique recurrent state and `P^(n-1)` is constant;
4. the pointwise clock from the longest all-distinct prefix, sharp height
   `n-1`, and depth CDF `(n)_(n-t)n^t`;
5. a zero-or-product formula for every target fibre at every time, including
   `t=0`, `t=n-1`, `n=1`, and mass conservation.

## P186 — rank-compression support

For `R({a_0<...<a_{k-1}})=supp{a_j-j}`, the paper must prove:

1. at time `t`, every positive source gap `g` becomes `g-t` when positive
   and disappears otherwise, with order preserved;
2. the exact pointwise clock, fixed set, basins, sharp height `n-1`, and unique
   deepest state `{0,n-1}`;
3. a nonempty target `B` occurs at time `t` iff
   `max(B)+t(|B|-1)<n`;
4. the complete time-`t` fibre coefficient formula using
   `(1-(z+...+z^t))^(-|B|)`, with the empty and time-zero boundaries explicit;
5. the one-step binomial fibre and Fibonacci first-image corollaries.

## Common contract

Each package must include an exact deterministic verifier, frozen canonical
stdout, explicit claim/evidence and source ledgers, anonymous LaTeX, immutable
Round-0/1/2 PDFs, two process-separated hostile reviews, two source-only cold
builds, visual/mechanical QA, manifests, and `HOLD_EXTERNAL`.  No manuscript
may infer novelty from the bounded owner search.
