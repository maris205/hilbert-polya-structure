# S01 theorem package — fresh-map self-image erosion

**Provisional gate:** `SPIKE_1_OWNER_THIN / HOLD_EXTERNAL`  
**Literal system:** for independent uniform maps `f_t:[n]->[n]`,

```text
A_(t+1) = A_t intersect f_t(A_t).
```

This file states the all-parameter package that would have to survive before
allocation.  The finite verifier checks the formulas, but the proofs below—not
the bounded boxes—are the intended theorem routes.

## 1. Exact one-step endpoint and image-size mark

Fix `A subseteq [n]`, `B subseteq A`, and put `a=abs A`, `b=abs B`.  Let
`K=abs f(A)`.  For `k=b+r`, the number of restrictions `f|A` with

```text
A intersect f(A)=B,       abs f(A)=k
```

is

```text
H_n(a,b;k)
 = binom(n-a,k-b) k! S(a,k),                              (1)
```

where `0<=k-b<=min(n-a,a-b)` and a term outside that range is zero.  Hence,
for one fixed target,

```text
P(A,B)
 = 1_(B subseteq A) n^(-a)
   sum_(r=0)^min(n-a,a-b) binom(n-a,r)(b+r)!S(a,b+r).     (2)
```

Formula (1) is also the complete endpoint-conditioned mark:

```text
Pr(K=k | A_(t+1)=B,A_t=A) = H_n(a,b;k) / sum_j H_n(a,b;j). (3)
```

**Proof route.**  Choose the `r=k-b` image points outside `A`; then `f|A`
must be onto the chosen `k`-set `B union R`, giving `k!S(a,k)` maps.  The
values of `f` outside `A` cancel from probabilities and contribute the fibre
factor `n^(n-a)` if full endomaps rather than restrictions are counted.

## 2. Cardinality quotient and every-time/every-target law

Let `Q=(Q_ab)_(0<=b<=a<=n)` be the size chain.  With

```text
N_ab = sum_r binom(n-a,r)(b+r)!S(a,b+r),
Q_ab = binom(a,b) N_ab / n^a.                             (4)
```

The row identity `sum_b Q_ab=1` follows by partitioning all maps `A->[n]`
according to `A intersect f(A)`.  Relabelling equivariance and nesting give,
for every `t>=0`,

```text
P^t(A,B)
 = 1_(B subseteq A) (Q^t)_(a,b) / binom(a,b).             (5)
```

At `t=0`, the quotient is interpreted in the evident way and (5) is the
identity kernel.  Formula (5) is stronger than a size marginal: it resolves
every labelled endpoint at every time.

For joint image-size marks at successive epochs, replace (4) by

```text
Q_ab(z)=binom(a,b)n^(-a) sum_r
        binom(n-a,r)(b+r)!S(a,b+r) z^(b+r).               (6)
```

Then a product `Q(z_1)...Q(z_t)` is the exact multitime marked size law; a
fixed labelled final target is obtained by dividing its `(a,b)` entry by
`binom(a,b)`.  No independence between the marks is asserted.

## 3. Complete algebraic spectrum and the forced Jordan anomaly

Order the `2^n` subset states by cardinality.  The full transition matrix is
lower triangular because the set can only shrink.  Its diagonal entry at any
`a`-set is

```text
lambda_a = a!/n^a.                                       (7)
```

Therefore its complete algebraic eigenvalue multiset is

```text
{lambda_a with multiplicity binom(n,a): 0<=a<=n}.         (8)
```

For `n>=3`,

```text
lambda_0 > lambda_1 > ... > lambda_(n-2) >
lambda_(n-1)=lambda_n=(n-1)!/n^(n-1).                    (9)
```

For `n=2`, the corresponding statement is simply
`lambda_0>lambda_1=lambda_2`.

In the size quotient, `Q_(n,n-1)>0`.  Since the repeated values in (9) are
adjacent diagonal entries, the restriction cannot have two independent
eigenvectors: the eigenvalue in (9) has one genuine `J_2` block.  Equivalently,

```text
nullity(Q-lambda I)=1,   nullity((Q-lambda I)^2)=2.        (10)
```

The verifier checks (10) exactly for every `2<=n<=7`.  The uniform proof uses
the strict ratios `lambda_(a+1)/lambda_a=(a+1)/n` until the final equality and
the positive `n -> n-1` transition.  Thus the Jordan signal is forced by the
literal update, not fitted from a numeric eigenvalue coincidence.  The claim
about the full matrix is deliberately limited to the algebraic spectrum and
the inherited non-diagonalizability; no unproved full Jordan form is asserted.

## 4. Absorption

For `n>=2`, the empty set is the unique recurrent state.  Every nonempty
proper set has a positive one-step probability of strict decrease, and the
full set has a positive probability of first entering a proper layer.  A
finite monotone chain therefore reaches zero almost surely.

For a start of size `a`, if `tau` is the first empty time,

```text
Pr_a(tau<=t) = (Q^t)_(a,0),                               (11)
E_a tau = sum_(t>=0) [1-(Q^t)_(a,0)]                     (12)
```

and the latter is equivalently the unique triangular solution

```text
E_0=0,   E_a=[1+sum_(b<a)Q_ab E_b]/(1-Q_aa).              (13)
```

The spectral expansion of (11) contains a polynomial-exponential term
`(c_0+c_1 t)lambda_n^t` because of (10).  For example, at `n=2`,

```text
Q = [[1,0,0],[1/2,1/2,0],[0,1/2,1/2]],   E_2 tau=4.      (14)
```

## 5. Boundary ledger

- `n=0`: if admitted, the only state is empty and is fixed; formulas use the
  usual `0^0=1` convention only after this case is separated.
- `n=1`: empty and full are both fixed.  The full-start absorption time to
  empty is infinite.  There is no transient Jordan claim.
- `n=2`: (14) is the first genuine Jordan case and must remain an explicit
  regression sentinel.
- Empty `A`: (1)--(6) have only `a=b=k=0` and mass one.

## 6. Owner subtraction and residual

Zero contribution credit is assigned to:

1. ordinary random-map occupancy and `k!S(a,k)`;
2. the image-size process `S_(t+1)=f_t(S_t)` and its asymptotics, including
   Zubkov--Serov;
3. generic triangular-chain absorption algebra and generic finite-matrix
   spectral bookkeeping; and
4. P158/P162/P170's already occupied random-intersection, history-signature,
   and marked-kernel proof vocabularies.

The proposed residual conjunction is only:

```text
literal self-image erosion
+ every-labelled-target all-time kernel
+ forced top-layer Jordan block
+ endpoint-conditioned total-image mark.
```

A direct owner of that conjunction, a transfer reducing (1)--(13) to an
occupied internal process, or a finding that the mark is merely decorative
kills the candidate.  The current bounded search did not locate the literal
chain, but that non-hit is not novelty, priority, or permission to circulate.
