# Frozen theorem contracts — P187–P191

Status: `5/5 SELECTED / OWNER_AMBER / HOLD_EXTERNAL`.

Finite enumeration is counterexample pressure. Every item below requires an
all-parameter written proof in its paper, and no bounded owner-search non-hit
may be reported as novelty.

## P187 — cyclic divisor-quotient dynamics

For divisor words of `N`, set
`Q(x)_i=x_i/gcd(x_i,x_(i+1))` cyclically. The paper must prove:

1. the exact primewise conjugacy to `D(e)_i=(e_i-e_(i+1))_+`;
2. eventual fixedness and sharp global height: zero for `N=1`, one for
   `m=1,2` when `N>1`, and `max_p a_p` for `m>=3`;
3. fixed count `prod_p I_m(a_p)`, with the cyclic-support polynomial and its
   `m=1,2` conventions explicit;
4. every labelled one-step target fibre as a product of traces of the local
   matrices `L_b(u,v)=1[(u-v)_+=b]`, including zero fibres and mass;
5. the all-one fibre, common-prime image obstruction, short-length fibre
   laws, and all boundary parameters.

## P188 — self-cardinality truncation

For `A subseteq [n]`, set `T(A)=A intersect [|A|]`. The paper must prove:

1. `T^t(A)=A intersect [k_(t-1)]` for the scalar rank recursion
   `k_0=|A|`, `k_(t+1)=|A intersect [k_t]|`;
2. endpoint `[rho(A)]`, fixed/recurrent initial segments, and terminal basin
   sizes `2^(n-r-1)` for `r<n` and one for `r=n`;
3. sharp height `n-1` for `n>=2`, uniquely at `{2,...,n}`;
4. an every-time every-target nested-rank-chain binomial formula, with time
   zero, stabilized time, and mass explicit;
5. the one-step fibre sum, iff image inequality, Fibonacci image and empty
   fibre counts, cardinality layers, and unique largest fibre for `n>=2`.

## P189 — transpose after row compression

For binary `n x n` matrices, set
`F(A)_(ij)=1[i<=sum_k A_(jk)]`. The paper must prove:

1. `F^2(A)=D(lambda(A)^*)`, `F^3(A)=D(lambda(A))`, and `F^4=F^2`;
2. the complete recurrent Ferrers locus, conjugation two-cycles, and
   self-conjugate fixed locus;
3. exact depth-zero/one/two criteria and populations, including `n=1`;
4. recurrent/fixed/strict-two-cycle counts
   `C(2n,n)`, `2^n`, and `(C(2n,n)-2^n)/2`;
5. every-target time-one and time-two fibres and image counts `(n+1)^n` and
   `C(2n,n)`.

## P190 — Brandt sandwich erosion

On cyclic words over `B_n={0} union {(a,b)}`, set
`T(x)_i=x_i x_(i+1) x_i`. The paper must prove:

1. the all-time good-edge run normal form;
2. fixed counts `1+n` for odd length and `1+n^2` for even length;
3. exact pointwise tails and sharp parity-dependent heights, including
   `n=1` and `m=1,2`;
4. every-target trace and nonzero-anchor gap products with matrix orientation
   unambiguous;
5. the all-zero fibre recurrence/spectrum, labelled image gap criterion, and
   total fibre mass.

## P191 — prefix-divisibility cut filter

For a composition with cuts `s_i` and incoming parts `a_i`, retain an old
internal cut exactly when `a_i` divides `s_i`. The paper must prove:

1. monotone cut loss, fixedness criterion, and the fixed-state path recurrence;
2. sharp height zero for `N<=3` and `N-3` for `N>=4`;
3. uniqueness of the deepest state `(1,2,1^(N-3))` and its full orbit;
4. every-target one-step fibres via the admissible source-path DP, including
   the no-skipped-target and retained-iff-divisible conditions;
5. exact image recognition by DP positivity and mass `2^(N-1)`, including
   `N=1` and the unconstrained final endpoint.

## Common delivery contract

Each package must contain anonymous LaTeX, a normalized proof package,
claims/evidence and source ledgers, a deterministic paper-local verifier and
canonical transcript, immutable Round-0/1/2 PDFs, two process-separated
hostile reviews with accepted deltas, two source-only cold builds, visual and
mechanical QA, non-self manifests, and a visible `HOLD_EXTERNAL` boundary.
