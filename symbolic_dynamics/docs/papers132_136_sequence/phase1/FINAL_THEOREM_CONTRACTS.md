# Final frozen theorem contracts — P132–P136

These are internal ceilings after direct-owner subtraction.  A manuscript may
narrow a contract when review exposes a flaw, but it may not silently broaden
one.  Bounded computation supports falsification only.  All five papers remain
`HOLD_EXTERNAL`.

## P132 — synchronous prefix-majority feedback

For `w in {0,1}^n`, define `P_n(w)_i=1` exactly when
`sum_(j<=i) w_j >= i/2`.

1. The fixed words are precisely
   `(01)^r 0^(n-2r)` and `(01)^r 1^(n-2r)`, over the admissible `r`; there are
   `n+1` of them and no other recurrent points.
2. Every orbit is fixed within `ceil(log_2 n)` steps, and this clock is sharp.
   The proof must use the fixed-prefix amplifier.  Sharpness must use
   `W_a=1^a0^(n-a)` and `P_n(W_a)=W_min(2a,n)`.
3. For every target, the exact one-step fibre is the product of the Dyck
   excursion factors forced by its sign changes and a terminal meander factor,
   with the stated run-parity compatibility conditions.
4. The image has size `F_(n+2)`.  The maximum fibre is
   `binom(n,floor(n/2))`, uniquely at `1^n` for `n>=2`; the strictness proof
   must be an explicit injection, not an asymptotic comparison.
5. Husfeldt–Rauhe's prefix-majority query, all classical walk counts, the
   Fibonacci enumeration, and generic majority-network facts are zero credit.
   The admissible residual is the repeated full-answer-vector feedback and its
   sharp temporal theorem.

## P133 — totient-complement dynamics on squarefree divisors

Let `n=product_(p in P)p` be squarefree and
`F_n(d)=gcd(n,(n/d)phi(d))`.  Direct the induced Pratt DAG by `q -> p` when
`p | q-1`.

1. Under divisor supports, prove the literal conjugacy
   `F(S)=(P\S) union N(S)`.  In complemented bits,
   `y_p(t+1)=(1-y_p(t)) product_(q in Par(p))y_q(t)`.
2. If `s` is the number of DAG sources, give the explicit topological
   source-phase decoder and prove exactly `2^s` recurrent states, hence
   `2^(s-1)` cycles of exact period two and no fixed point.
3. Prove `y_p(t+2)=product_(q in Par(p))y_q(t+1)` for every nonsource.  If
   `h` is the longest source-to-vertex path, every orbit enters its two-cycle
   by time at most `h+1`, including singleton and disconnected cases.  No
   sharpness claim is permitted.
4. For every target `B`, with `Z=P\B` and `Par(U)` the union of its parents,
   prove

   ```text
   |F_n^(-1)(B)| =
     sum_(T subseteq B, (Z union T) intersect Par(Z union T)=empty)
       (-1)^|T| 2^(|P|-|Z union T|-|Par(Z union T)|).
   ```

   The proof must expose the forced-one/forced-zero compatibility, so targets
   outside the image also evaluate correctly.
5. Prime chains, Pratt height, Euler products, signed Boolean networks, and
   inclusion–exclusion are zero-credit tools.  No bounded owner non-hit may be
   phrased as novelty or priority.

## P134 — repeated whole-border-array dynamics

Let `E_n={(e_0,...,e_(n-1)):0<=e_i<=i}`.  Regard `e` as an integer word and
let `Pi_n(e)` be its complete ordinary KMP border/prefix-function array.

1. For `1<=r<n`, define
   `A_r=(0,1,...,r,0,...,0)` and let `B_(r+1)` have `r+1` initial zeros and
   then ones.  Prove `A_r <-> B_(r+1)` and that these are all recurrent
   states: one fixed point at `n=1`, and `n-1` exact two-cycles for `n>=2`.
2. Prove the indexed mismatch automaton

   ```text
   A1 -> B2 -> extension,
   B0 -> A1 -> B2 -> extension,
   ```

   for valid arrays.  It must distinguish recomputing `Pi_n(Pi_n(w))` from
   following failure links inside one original word.
3. The maximum depth among valid border arrays is `2n-5` for `n>=4`; among
   all of `E_n` it is `2n-4`.  The latter complete boundary is
   `0,0,1,2n-4` for `n=1,2,3,n>=4`, with the explicit witnesses
   `p_n=(0,0,1,0^(n-3))` and `e_n=(0,1,0,2,1^(n-4))`.
4. Every one-step fibre has size at most `(n-1)!`.  For `n>=2`, equality is
   attained exactly by the two targets `0^n` and `A_1`; the proof must use the
   corrected proper-suffix argument at positions zero, one, and at least two.
5. KMP, border-array validation/realization, and the valid-array census are
   zero credit.  Only whole-table feedback, the recurrent/clock theorem, and
   the extremal inverse result are admissible.

## P135 — derived-centralizer orbit-partition dynamics

For a permutation of cycle type `lambda=product_j j^(m_j)`, replace `lambda`
by the orbit-size partition of the derived subgroup of its full centralizer.

1. From `C_(S_n)(sigma)=product_j(C_j wr S_(m_j))`, prove the local rule

   ```text
   j^1 -> 1^j,
   j^2 -> j^2,
   j^m -> (jm) for m>=3,
   ```

   and collect the outputs across `j`.  The centralizer and wreath-commutator
   structural inputs are owner-credited background.
2. For every target `mu=product_k k^(r_k)`, prove the exact coefficient fibre

   ```text
   #CT1^(-1)(mu) = [x_1^(r_1)...x_n^(r_n)] [z^n]
     product_(j=1)^n
       (1+z^j x_1^j+z^(2j)x_j^2+
          sum_(m=3)^floor(n/j) z^(jm)x_(jm)).
   ```

3. In the coloured tagged lift, tags coarsen on cross-tag mergers.  Prove the
   two-clean-step lemma and hence
   `tail(lambda)<=2 ell(lambda)<=2n` and eventual period in `{1,2}`.  This
   bound is explicitly nonsharp.
4. With `Delta_D=product_(j in D)j^2`, exhaust the recurrent classes:
   fixed `1^e Delta_D` (`e=0,1,2`); strict cycles
   `a Delta_D <-> 1^a Delta_D`; fixed points
   `a1^a Delta_D`; and strict antiphase cycles
   `a1^b Delta_D <-> b1^a Delta_D`, with `a,b>=3` and the stated exclusions
   from `D`.
5. Derive the formal OGFs for fixed points and strict two-cycles from that
   disjoint decoder.  Generic multiplicity dynamics, partition iteration,
   product extraction, and short-cycle rhetoric are zero credit.

## P136 — exact laws for random sunflower transversals

On a sunflower with core size `c`, petal sizes `p_i`, and positive edge rates
`lambda_i`, select an active edge rate-proportionally, then a uniform vertex
of that edge, record it, and delete all hit edges.  Put
`r_i=p_i/(c+p_i)` and `q_i=c/(c+p_i)`.

1. For a proper petal set `A`, prove the exact aggregate endpoint law

   ```text
   I(A)=sum_(B subset A)(-1)^|B| /
        (Lambda([m]\A)+Lambda(B)),
   pi(A)=product_(i in A)r_i
         [sum_(j notin A)q_j lambda_j] I(A),
   pi([m])=product_i r_i.
   ```

2. Resolve actual recorded vertices: a specified
   `{x_i:i in A} union {y}` has mass
   `pi(A)/(c product_(i in A)p_i)`, and a specified all-petal transversal has
   mass `product_i 1/(c+p_i)`.  The recorded endpoint need not be minimal.
3. At unit rates put
   `s_t=e_t(r_1,...,r_m)/binom(m,t)`.  Prove
   `Pr(T>t)=s_t`, `Pr(T=t)=s_(t-1)-s_t` for `t<m`, and
   `Pr(T=m)=s_(m-1)`.  The top atom must visibly include both the all-petal
   and last-edge-core mechanisms.  Derive the complete PGF, mean, second
   moment, and variance.
4. For vertex-disjoint sunflower components, prove the tensor product of
   endpoint laws and the sum/convolution/product law for discrete selection
   counts and their PGFs using an explicit independent marked-clock coupling.
   Continuous elapsed absorption time is outside the contract; the forest
   completion time would be the maximum, not the sum, of component times.
5. The sunflower carrier, Pitt/Bar-Yehuda random cover process,
   rate-proportional size-biased ordering, exponential races, dissociation,
   beta integrals, and symmetric-polynomial tools receive zero contribution
   credit.  The sole residual is the exact marked sunflower atlas above.

## Common Stage 2 obligations

Each paper needs a deterministic paper-local verifier and frozen transcript,
two independent hostile-review rounds, closure of every critical and major
issue, isolated four-pass LaTeX/BibTeX reproduction, visual inspection of all
pages, font/text/metadata checks, and final hashes.  None of these operations
authorizes external release.
