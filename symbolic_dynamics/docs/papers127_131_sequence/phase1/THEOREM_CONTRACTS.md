# Frozen theorem contracts — P127–P131

All contracts are internal ceilings.  A manuscript may prove less only if a
hostile review requires deletion; it may not silently claim more.

## P127 — odd-outdegree transpose dynamics

For `n>=1`, on `M_n(F_2)` let `r=A1`, `c=A^T1`, `tau=1^T A1`, and
`Phi(A)=A^T+rr^T`.

1. `tau(Phi(A))=0`; on the even hyperplane margins swap, while an odd state
   maps to `(c+r,0)` in the margin quotient.
2. The even hyperplane is image and complete recurrent set; every odd state
   has exact depth one; `Phi^2(A)=A+rr^T+cc^T` there and periods are `1,2,4`.
3. Every codomain fibre has size `0`, `1`, or `2^(n-1)+1`, with the exact
   total/column-margin criterion.
4. Fixed, 2-cycle, 4-cycle, depth-one, and fixed-`n` zeta formulas are exact.
5. An independent transvection/projection factorisation controls the collapse.

## P128 — translation–GCD depth and terminal fibres

Let `q=p^a`, `sigma f(x)=f(x+1)`, `T(f)=gcd(f,sigma f)`, and
`Q=T^(p-1)` on monic `F_q[x]`.

1. On every nonfixed irreducible translation orbit, exponent vectors evolve
   by cyclic window minima; after the common minimum is removed, depth is the
   longest positive cyclic run.  This generic orbit-fold mechanism is old and
   zero credit.
2. With owner-supplied fixed-irreducible counts `b_d`, nonfixed orbit counts
   `a_d=(N_d(q)-b_d)/p`, and the run automaton polynomial
   `R_(p,t)(y)`, the formal all-depth series is

   ```text
   H_(q,p,t)(z)=1/(1-q z^p) product_(d>=1) R_(p,t)(z^d)^(a_d).
   ```

   Consecutive differences enumerate exact depth.
3. Every monic factors uniquely as `f=Q(f)g` with `Q(g)=1`.  This is a graded
   set bijection, not a monoid-kernel theorem.
4. The unit-fibre OGF is `(1-qz^p)/(1-qz)`; hence its degree-`n` coefficient
   is `q^n` for `n<p` and `q^n-q^(n-p+1)` for `n>=p`.
5. For every invariant terminal target `h` of degree `m`, the exact degree-`N`
   fibre is the unit-fibre coefficient at `N-m`; summation gives every capped
   fibre.

## P129 — rootward active-pile coalescence

For a rooted finite set `S={0=s_0<...<s_r}`, choose an occupied nonroot site
uniformly, move it left by one, and erase multiplicity on collision.

1. The strict potential gives absorption and the complete acyclic PGF
   recursion.
2. After Poissonization, ordered graphical interfaces and the jump-count
   compensator give

   ```text
   E[T_S] = sum_(i=1)^r h(s_(i-1),s_i),
   h(a,a)=0, h(0,b)=b,
   h(a,b)=1/2+(h(a-1,b)+h(a,b-1))/2.
   ```

3. A ballot/first-passage calculation gives the adjacent value
   `h(m-1,m)=(2m-1)!!/(2m-2)!!` and therefore the full-start exact mean and
   `4/(3 sqrt(pi)) n^(3/2)+O(n^(1/2))` asymptotic.
4. `supp(T_S)={max S,...,sum S}`; the full-start minimum mass is
   `1/(n-1)!`.
5. The observed maximum-endpoint mass is excluded unless independently
   proved during manuscript review.

## P130 — crossing-component fibre geometry

On a rooted/cut labelled chord matching, replace each crossing-graph
component by consecutive pairs on its sorted support.

1. The map is an idempotent retraction to noncrossing matchings; this and its
   Catalan count are background.
2. For target nesting forest `T`, if `d_T(v)` counts immediate children and
   `a_d` counts noncrossing partitions of a sibling list decorated by
   crossing-connected diagrams, prove the full mutual inverse

   ```text
   |Phi^(-1)(T)| = product_v a_(d_T(v)).
   ```

3. The proof must cover the virtual root, nested sibling blocks, component
   nonmerging, extraction, construction, and mutual inversion.
4. Strict supermultiplicativity of `a_d` implies that the consecutive matching
   is the unique maximum-fibre target.  The owned sequence values and OGF are
   zero credit.

## P131 — cyclic Euclidean-quotient queues

On canonical `q=[0;a_1,...,a_k] in (0,1)` of digit sum `N`, rotate the first
quotient to the end and normalize a terminal one.

1. Exact depth is the position of the last digit one, with sharp `N-2`.
2. Cyclic one-runs are absorbed into their preceding non-one digit; the cut
   after the last original one gives the terminal core, whose primitive
   rotation period is eventual period.
3. Exact-depth formal OGFs are

   ```text
   D_0=x^2/(1-x-x^2),
   D_t=x^(t+2)/((1-x)^(t-1)(1-x-x^2)), t>=1.
   ```

4. Two explicit inverse branches give every fibre (`0/1/2`), image, and
   Garden count, including `N=2,3`.
5. A subtractive Euclidean `L/R` block route independently proves the marker,
   core, and inverses.  Necklace and fixed counts are background corollaries.
