# C190 proof package: recurrent Bulgarian solitaire

## Main theorem

Let `N>=1`, write uniquely

\[
N=\binom{k}{2}+r,\qquad k\ge2,\quad 0\le r<k,
\]

let `P(N)` be the integer partitions of `N`, and let `T_N` be the ordinary
Bulgarian-solitaire map.  For a length-`k` word `w` of Hamming weight `r`, put

\[
\phi(w)=\text{positive parts of }(k-1,k-2,\ldots,0)+w,
\]

and let `rho` be right rotation.  Then:

1. Brandt's attributed recurrent theorem gives a bijection from the
   weight-`r` binary words to the recurrent partitions, and
   `T_N phi=phi rho`.
2. For every integer `t>=1`, with `g=gcd(k,t)`,
   \[
   F_t:=\#\operatorname{Fix}(T_N^t)=
   \begin{cases}
   \binom{g}{rg/k},&(k/g)\mid r,\\
   0,&\text{otherwise}.
   \end{cases}
   \]
3. For each `d|k`, the least-period population and cycle count are
   \[
   P_d=\sum_{e\mid d}\mu(d/e)F_e,\qquad C_d=P_d/d.
   \]
4. The Artin--Mazur zeta of the full noninvertible finite system is
   \[
   \zeta_{T_N}(z)=\prod_{d\mid k}(1-z^d)^{-C_d}.
   \]
5. For the Koopman pullback `(U_N f)(lambda)=f(T_N lambda)` on all functions
   on `P(N)`,
   \[
   \det(\xi I-U_N)=
   \xi^{p(N)-\binom{k}{r}}\prod_{d\mid k}(\xi^d-1)^{C_d},
   \]
   \[
   \det(I-zU_N)=\prod_{d\mid k}(1-z^d)^{C_d}
   =\zeta_{T_N}(z)^{-1},\qquad \operatorname{Tr}(U_N^t)=F_t.
   \]
   Zero has algebraic multiplicity `p(N)-binom(k,r)`.  If
   `omega_k=exp(2 pi i/k)`, then
   \[
   \operatorname{mult}(\omega_k^j)=
   \sum_{\substack{d\mid k\\k\mid jd}}C_d.
   \]
6. On the recurrent word layer, `Q(w)_i=w_(-i mod k)` obeys
   `Q^2=1` and `Q rho Q=rho^(-1)`.  Every `rho^a Q` is another
   phase-labelled involutory reversor.  These `k` formulas need not define
   `k` distinct maps when the weight layer is nonfaithful.
7. If `r=0`, the recurrent core is the singleton staircase
   `(k-1,k-2,...,1)`.  Its zeta is `(1-z)^(-1)` and its recurrent Koopman
   eigenvalue is one; the full zero multiplicity is `p(N)-1`.

## Status

`PROVABLE AS STATED` as a source-derived theorem package.  Item 1 is an
explicitly attributed classical input.  Items 2--7 are proved consequences.
No new-theorem priority is claimed for the Brandt/Akin--Davis inputs.

## Proof

### Step 1: recurrent coordinates and rotation

The vector `(k-1,...,0)+w` is weakly decreasing, because adjacent staircase
entries differ by one and adjacent bits differ by at most one.  Its sum is
`binom(k,2)+r=N`; deleting a final zero gives a partition.  Brandt's theorem
says precisely that these are all recurrent partitions.  If the final bit is
zero, the partition has `k-1` positive parts; if it is one, it has `k`.
Subtracting one from every positive part and inserting the new pile therefore
moves the final bit to the first position in both cases.  Hence
`T_N phi=phi rho`.

### Step 2: all positive-iterate fixed counts

The index permutation `rho^t` has `g=gcd(k,t)` cycles, each of length `k/g`.
A fixed word is constant on each index cycle.  Its weight must therefore be a
multiple of `k/g`.  When `(k/g)|r`, choose the `rg/k` index cycles carrying a
one; this gives `binom(g,rg/k)`.  Otherwise no fixed word exists.

If `T_N^t(lambda)=lambda` with `t>=1`, then `lambda` is periodic and hence
recurrent.  Thus transient partitions never add to the fixed count.  The word
formula is the full-map formula.

### Step 3: least periods, cycles, and zeta

For every `d|k`, a recurrent point fixed by `T_N^d` has least period dividing
`d`, so

\[
F_d=\sum_{e\mid d}P_e.
\]

Divisor Möbius inversion gives the displayed formula for `P_d`.  Each
least-period-`d` orbit contains `d` points, so `C_d=P_d/d`.  Finally,
`F_t=sum_(d|t) d C_d`; substituting this into the exponential zeta definition
and using `sum_(m>=1) z^(dm)/m=-log(1-z^d)` proves the cycle product.

### Step 4: full Koopman algebraic spectrum

Every component of a finite functional graph is a directed cycle with finite
trees feeding it.  Order the basis from transient vertices toward the cycle.
The transient diagonal block is nilpotent and contributes one zero
characteristic root per transient vertex.  A `d`-cycle contributes the cyclic
permutation factor `xi^d-1`.  There are `p(N)-binom(k,r)` transient vertices,
which proves the characteristic polynomial and the zero multiplicity.

Substituting `xi=1/z` gives the determinant in `I-zU_N`; zero eigenvalues add
no `z` factor, so it is the reciprocal zeta.  Each `d`-cycle contributes every
`d`th root once.  The root `omega_k^j` is a `d`th root exactly when `k|jd`,
which proves the multiplicity formula.  The trace of a finite-map pullback
counts fixed basis coordinates, giving `Tr(U_N^t)=F_t`.

This argument determines algebraic eigenvalue multiplicities, not the sizes
of nilpotent Jordan blocks.  Those sizes depend on transient-tree geometry.

### Step 5: reflection and noninvertibility boundary

For indices modulo `k`,

`(Q rho Q w)_i=(rho Q w)_(-i)=(Qw)_(-i-1)=w_(i+1)`,

which equals `(rho^(-1)w)_i`; also `Q^2=1`.  Replacing `Q` by `rho^a Q`
preserves both identities.  Transport through `phi` gives recurrent-core
partition reversors.  Since the full Bulgarian map is generally noninjective,
no inverse and hence no global reversal identity is asserted on all `P(N)`.

### Step 6: triangular boundary

When `r=0`, only `0^k` occurs.  Its image is the staircase and rotation fixes
it.  All fixed counts equal one, only `C_1=1` is nonzero, and all displayed
specializations follow.  This says nothing about the shape or depth of the
transient basin.

## N=8 sentinel

For `N=8=binom(4,2)+2`, the six words split into one 2-cycle and one 4-cycle.
Thus

- positive-residue fixed ledger: `(F_1,F_2,F_3,F_4)=(0,2,0,6)`;
- cycle ledger: `C_2=C_4=1`;
- zeta: `((1-z^2)(1-z^4))^(-1)`;
- full zero multiplicity: `p(8)-6=22-6=16`;
- fourth-root multiplicities: `(2,1,2,1)`.

## Route-A stopping theorem

The recurrent cycles, finite zeta, and recurrent permutation are natural
source structures, so A1 is weakly positive.  Nevertheless, deck size,
partitions, and binary necklaces have no intrinsic rational-prime carrier,
prime-power repetition weight, or logarithmic prime clock.  The finite
determinant has no established target divisor or analytic structure.  The
full Koopman map is nonunitary, and the recurrent unitary is only a formal
operator hint.  Therefore

`(A0,A1,A2,A3,A4)=(FAIL,WEAK,FAIL,FAIL,FORMAL_HINT)`, overall
`ROUTE_A_REJECTED`, and Route B is false.

## Open risks and nonclaims

- The package imports rather than reproves Brandt's all-`N` classification.
- It does not classify transient trees, hitting-time distributions, or
  nilpotent Jordan block sizes.
- It does not claim a global reversor for a noninvertible map.
- Finite regression cannot establish theorem priority or literature-wide
  novelty.
- No target divisor, functional equation, continuation, Weil compression, or
  Hilbert--Polya operator is asserted.
