# Final frozen theorem contracts — P137–P141

These contracts are internal ceilings after classical inputs and direct-owner
background have been subtracted.  A manuscript may narrow a statement after
review, but it may not silently broaden one.  Exact enumeration is used only
as counterexample pressure.  Every paper remains `HOLD_EXTERNAL`.

## P137 — rank-feedback splitting of finite abelian p-groups

Let

```text
G_lambda = direct_sum_i Z/p^(a_i)Z,
lambda=(a_1>=...>=a_r),  r=d(G_lambda),
F(G)=p^rG direct-sum G[p^r].
```

1. Prove the literal type rule

   ```text
   a<=r  -> (a),          a>r -> (r,a-r),
   ```

   with the rank recomputed after every update.
2. A nonfixed step strictly increases rank.  Hence every recurrent state is
   fixed, and `lambda` is fixed exactly when `lambda_1<=ell(lambda)`.  The
   fixed-state ordinary generating function is

   ```text
   sum_(r>=1) x^r [2r-1 choose r]_x.
   ```

3. With `T_j=j(j+1)/2`, the maximum depth on partitions of `n` is

   ```text
   D(n)=ceil((sqrt(8n+1)-3)/2),
   ```

   and `(n)` is the unique maximizer.  The upper bound must use the permanent
   marker parts created at successive ranks; sharpness must use

   ```text
   F^t((n))=sort(n-T_t,t,t-1,...,1).
   ```

4. For a target `mu` of length `L`, sum over
   `ceil(L/2)<=r<=L`.  Put `c=L-r`, require at least `c` copies of `r`, remove
   them, and write the remaining multiplicities as `q_j`.  With
   `Q_>=sum_(j>r)q_j`, the rank-`r` contribution is zero for `Q_> > c` and is

   ```text
   [u^(c-Q_>)] product_(1<=j<=r)(1+u+...+u^(q_j))
   ```

   otherwise.  The sum is exactly the one-step fibre; its positivity is the
   complete image criterion.
5. Classification of finite abelian p-groups and the cyclic-factor identities
   for `p^rG` and `G[p^r]` are zero-credit inputs.  The admissible residual is
   the recomputed-rank iteration, sharp triangular clock, recurrent census,
   and every-target inverse theorem.

## P138 — palindromic-prefix XOR feedback

For `x in {0,1}^n`, let

```text
P_n(x)_i = x_i xor 1{x_1...x_i is a palindrome}.
```

1. Prove complement equivariance.  On the normalized quotient
   `y_i=x_i xor x_1`, `y_1=0`, prove the exact rule

   ```text
   Q_n(y)_i=y_i xor 1 xor 1{y_1...y_i is a palindrome}.
   ```

2. One update zeros the first `min(3,n)` normalized coordinates.  If the
   first `k` normalized bits are zero, the next state has at least `k+1`
   leading zeros.  It follows that the original system has one recurrent
   class, the strict two-cycle `0^n <-> 1^n`.
3. The maximum transient depth is `0` for `n=1`, `1` for `n=2`, and `n-2`
   for `n>=3`.  Sharpness must use the normalized word

   ```text
   y_i=1 exactly when i=3 mod 4,
   ```

   and prove that its alternating-tail image grows the leading-zero prefix by
   exactly one coordinate per further step.
4. Give the complete target decoder.  For normalized target `z`, construct a
   source prefix from left to right.  At position `i>=2`, if the current middle
   word `y_2...y_(i-1)` is nonpalindromic then `y_i=1-z_i` is forced; if it is
   palindromic then `z_i=0` is necessary and both choices of `y_i` are allowed.
   Prove that this recursion counts every one-step fibre and is an exact image
   criterion.  Recover the original phase without an extra multiplicity.
5. Classical palindrome recognition, border algorithms, and generic XOR
   network language are zero credit.  The residual is the repeated full
   palindrome-prefix indicator vector, its quotient amplifier, sharp clock,
   and every-target decoder.

## P139 — Lyndon-factor-start feedback on binary words

Fix `0<1`.  Write the unique nonincreasing Chen–Fox–Lyndon factorization
`w=u_1...u_k` and let `L_n(w)` be the binary mask whose ones are precisely the
factor starts.

1. Prove that the starts are the left-to-right strict new minima among the
   suffixes.  This equivalence may import the classical factorization theorem,
   but the repeated mask dynamics must be derived explicitly.
2. For `w=1^r0s`, prove

   ```text
   L_n(w)=1^r L_(n-r)(0s).
   ```

   Hence every nonfixed update increases the leading-one prefix, and the
   unique recurrent state is the fixed word `1^n`.
3. Every orbit reaches `1^n` within `n` steps.  The sharp and unique deepest
   source is the alternating word `a_n=0101...`, for which

   ```text
   L_n(a_n)=1 a_(n-1).
   ```

   The uniqueness proof must reverse equality at every prefix-growth step and
   force the successive `01` Lyndon blocks, including the final boundary.
4. If a target mask starts with one and its one-positions determine a
   composition `(ell_1,...,ell_k)`, prove

   ```text
   |L_n^(-1)(y)|
     = #{(u_1,...,u_k): |u_i|=ell_i, each u_i binary Lyndon,
                         u_1>=...>=u_k lexicographically}.
   ```

   Express the count as a product of rectangular zero-one lex-comparison
   matrices and give positivity as the complete image criterion.  Deduce the
   special fibres

   ```text
   |L_n^(-1)(10^(n-1))|=(1/n) sum_(d|n) mu(d)2^(n/d),
   |L_n^(-1)(1^n)|=n+1.
   ```

5. Chen–Fox–Lyndon factorization, Duval's algorithm, the classical binary
   Lyndon census, and matrix multiplication are zero-credit tools.  The
   residual is the iterated factor-start mask, its sharp unique clock witness,
   and the complete ordered-Lyndon inverse atlas.

## P140 — random majority-of-three contraction

Let an odd-length binary word shrink by choosing a current length-three
window uniformly and replacing the window by its majority bit.  The discrete
number of contractions is the deterministic `(n-1)/2`.

1. On a two-run word `0^a1^b`, `a,b>=1`, prove the reduced kernel

   ```text
   (a,b)->(a-2,b) with multiplicity (a-2)_+,
   (a,b)->(a,b-2) with multiplicity (b-2)_+,
   (a,b)->(a-1,b-1) with multiplicity 1_{a>=2}+1_{b>=2}.
   ```

   Deduce

   ```text
   Pr(final=1)=(b-1)/(n-2),
   Pr(final=0)=(a-1)/(n-2).
   ```

2. Every complete window-position history has probability `1/(n-2)!!`.
   Prove the exact endpoint counts

   ```text
   #(final 1)=(b-1)(n-4)!!,
   #(final 0)=(a-1)(n-4)!!.
   ```

3. If `C` counts cross-boundary contractions, prove the full endpoint-marked
   recurrence

   ```text
   H^1_(a,b)(u)
    =(a-2)_+ H^1_(a-2,b)(u)
     +(b-2)_+ H^1_(a,b-2)(u)
     +(1_{a>=2}+1_{b>=2})u H^1_(a-1,b-1)(u),
   ```

   with the correct one-run boundaries and the symmetric formula for final
   zero.  Prove the exact support

   ```text
   {c:1<=c<=min(a,b-1), c congruent a mod 2}
   ```

   for final one when `b>=2`, and the extreme law
   `Pr(final=1,C=1)=1/a` for odd `a` and zero otherwise (plus its symmetric
   counterpart).
4. Under independent unit-rate clocks on current windows, prove independence
   of elapsed time from the complete embedded contraction history and

   ```text
   tau_n =_d sum_(k=1,3,...,n-2) Exp(rate=k).
   ```

   For `n=2m+1`, derive

   ```text
   E[e^(-s tau_n)]
    =Gamma(m+1/2)Gamma((1+s)/2)
      /(Gamma(1/2)Gamma(m+(1+s)/2)),
   e^(-2 tau_n)~Beta(1/2,m),
   m e^(-2 tau_n) => Gamma(shape=1/2,rate=1).
   ```

   State the equivalent centered limit and the exact mean and variance.
5. Generic majority dynamics and continuous-time exponential-race facts are
   zero credit.  The residual is the shrinking-window process on two runs,
   its marked history polynomial, and the exact clock law and limit.

## P141 — weighted random-greedy independent sets on threshold graphs

Represent a threshold graph by a creation word `b_1...b_n`, where a zero
vertex is isolated from all earlier vertices and a one vertex is dominating
to all earlier vertices.  Give vertex `i` positive weight `w_i`; independent
exponential priorities drive the usual accept-and-delete greedy algorithm.
Write `W_j=sum_(i<=j)w_i` and `h_j=w_j/W_j` for dominating vertices.

1. The endpoint support consists of `Z`, the set of all zero vertices, and
   `S_d={d}` together with all zero vertices later than a dominating vertex
   `d`.  Prove the weighted masses

   ```text
   p_d=h_d product_(e>d, e dominating)(1-h_e),
   p_Z=product_(e dominating)(1-h_e).
   ```

2. Prove the reverse-hazard inverse

   ```text
   h_d=p_d/(p_Z+sum_(e<=d, e dominating)p_e).
   ```

   Thus endpoint laws are in bijection with the open reverse-hazard simplex;
   explain precisely why individual zero-vertex weights are not identifiable
   beyond the dominant prefix hazards.
3. Derive the accepted-update/independent-set-size PGF

   ```text
   G(z)=p_Z z^|Z|+sum_d p_d z^(1+#later zero vertices),
   ```

   dominant inclusion probabilities `p_d`, zero-vertex inclusion
   probabilities `product_(j>i, j dominating)(1-h_j)`, and the nested joint
   law for pairs of zero vertices.
4. Separate three clocks: a full priority scan has `n` inspected vertices;
   the number of accepted active updates is `|I|`; and continuous-time
   completion has, on a residual active set `A`, the exact Laplace recursion

   ```text
   L_empty(s)=1,
   L_A(s)=sum_(v in A) w_v L_(A\N[v])(s)/(s+sum_(u in A)w_u).
   ```

   No sum-of-independent-holding-times claim is allowed for arbitrary
   residual threshold states.
5. Threshold-graph structure, its maximal-independent-set support, and the
   general random-greedy/RSA process are directly owned and receive zero
   contribution credit.  Only the weighted reverse stick-breaking law,
   inverse-hazard theorem, marginals, and clock recursion are admissible.

## Common Stage 2 obligations

Each package must contain an anonymous manuscript, a verified bibliography,
a deterministic paper-local verifier and frozen transcript, a claims/evidence
ledger, two independent hostile-review rounds with all critical and major
issues closed, immutable round PDFs, isolated LaTeX/BibTeX reproduction,
visual inspection of every page, font/text/metadata checks, and final SHA-256
hashes.  None of these operations authorizes public release.
