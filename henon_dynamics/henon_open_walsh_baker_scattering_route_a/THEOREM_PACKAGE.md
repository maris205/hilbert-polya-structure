# C148 proof package

## Claim and status

**Status: PROVABLE AFTER CORRECTING THE ONE-STEP RANK.**  The frozen Walsh gate
has the exact contraction, tensor-power, gcd-trace, secular-determinant,
complex primitive-path, and defect statements below.  The proposed equality
`rank(B_k)=2^k` is false for one step.  The exact repair is
`rank(B_k)=2*3^(k-1)` and `rank(B_k^k)=2^k`.

## Assumptions and notation

Let `omega=(-1+i*sqrt(3))/2`.  On `C^3`, indexed by `0,1,2`, set

```text
F3[j,l]=omega^(j*l)/sqrt(3),  P=diag(1,0,1),  A=F3^* P.
```

On `H_k=(C^3)^(tensor k)`, define

```text
B_k(v0 tensor ... tensor v_(k-1))
 =v1 tensor ... tensor v_(k-1) tensor A*v0.       (1)
```

One application of `B_k` is one clock tick.  Put
`D_k(z)=det(I_(3^k)-z B_k)`.  For field receipts, `[a,b,c,d]` means
`a+b*sqrt(3)+c*i+d*sqrt(3)*i`.

## Dependency map

1. The one-qutrit matrix gives its Gram projections, rank, norm, and quadratic
   recurrence.
2. The shift is unitary, so one-step ranks and defects follow by conjugating a
   one-factor gate.
3. Tracking a pure tensor for `k` steps proves `B_k^k=A^(tensor k)`.
4. The cycles of the factor permutation induced by `shift^n` prove the gcd
   trace formula at every period.
5. Finite-dimensional log determinants and unique primitive roots give the
   secular and complex-amplitude path expansions.
6. Spectral mapping fixes the zero multiplicity and hence the exact polynomial
   degree.
7. Unitary similarity and a changed-hole trace separate two controls.

## Theorem 1: one-qutrit and escape structure

In the frozen basis,

```text
A=(1/sqrt(3))*[[1,0,1],[1,0,omega],[1,0,omega^2]],
```

so `A^*A=P`, `AA^*=F3^* P F3`, `||A||=1`, and `rank(A)=2`.  Consequently,
for every `k>=1`,

```text
||B_k||=1,                  rank(B_k)=2*3^(k-1),
B_k^k=A^(tensor k),         rank(B_k^k)=2^k.       (2)
```

Moreover,

```text
I-B_k^*B_k=(I-P) tensor I_(3^(k-1)),
I-B_k B_k^*=I_(3^(k-1)) tensor F3^*(I-P)F3.        (3)
```

Both matrices in (3) are orthogonal projections of rank `3^(k-1)`.

**Proof.**  Write `S(v0,...,v_(k-1))=(v1,...,v_(k-1),v0)` and
`C=I^(tensor(k-1)) tensor A`; then `B_k=C S`.  The shift is unitary, so
`||B_k||=||C||=1` and
`rank(B_k)=rank(C)=3^(k-1)rank(A)`.  Successive applications of (1) send
each original factor through `A` exactly once before restoring its position;
multilinearity gives `B_k^k=A^(tensor k)`.  Tensor rank multiplicativity gives
the second rank.  Finally,

```text
B_k^*B_k=S^*(I tensor ... tensor A^*A)S
         =P tensor I_(3^(k-1)),
B_kB_k^*=I_(3^(k-1)) tensor AA^*.
```

Since `P` and `F3^*PF3` are rank-two orthogonal projections, their complements
and tensor extensions have the asserted projection and rank properties.  This
also proves that the false one-step `2^k` rank confuses one opening with the
full opening accumulated over `k` ticks.  ∎

## Theorem 2: all-period trace formula

For every `k,n>=1`, let `d=gcd(n,k)`.  Then

```text
Tr(B_k^n)=Tr(A^(n/d))^d.                            (4)
```

**Proof.**  The basis matrix element of one step is

```text
<y|B_k|x>=(product_(r=0)^(k-2) 1_[y_r=x_(r+1)]) A_[y_(k-1),x_0].
```

In the diagonal sum for `B_k^n`, the Kronecker constraints identify tensor
positions along the cycles of addition by `n` modulo `k`.  This permutation
has exactly `d` cycles, each of length `k/d`.  Across all `n` steps there are
`n` ordered `A` factors, and cyclic translation distributes exactly `n/d`
factors to each permutation cycle.  Summing the qutrit index along one cycle
is `Tr(A^(n/d))`; distinct cycles have independent indices.  Their product is
(4).  This index contraction proves the exponent and does not use any finite
period replay.  ∎

## Corollary 3: exact secular and characteristic polynomials

Direct computation gives

```text
chi_A(lambda)=lambda*(lambda^2-tau*lambda+q),
tau=sqrt(3)/6-i/2,  q=-1/2-sqrt(3)*i/6.
```

Set `t_0=2`, `t_1=tau`, and
`t_m=tau*t_(m-1)-q*t_(m-2)` for `m>=2`.  Thus `t_m=Tr(A^m)`.  Define

```text
c_(k,0)=1,
c_(k,m)=-(1/m) sum_(j=1)^m c_(k,m-j)
         *t_(j/gcd(j,k))^gcd(j,k).                 (5)
```

Then

```text
D_k(z)=sum_(j=0)^(2^k)c_(k,j)z^j,
chi_(B_k)(lambda)=lambda^(3^k-2^k)
                  *sum_(j=0)^(2^k)c_(k,j)lambda^(2^k-j).  (6)
```

**Proof.**  In the formal power-series ring,

```text
-log D_k(z)=sum_(n>=1)Tr(B_k^n)z^n/n.
```

Substituting (4) and comparing coefficients gives Newton recursion (5).  To
fix the endpoint rather than infer it from a finite replay, triangularize
`A`.  Exactly two of its three diagonal eigenvalues are nonzero, so
`A^(tensor k)` has `2^k` nonzero and `3^k-2^k` zero eigenvalues, counted with
algebraic multiplicity.  Spectral mapping from `B_k` to `B_k^k` preserves the
total algebraic multiplicity at zero, because zero is the only eigenvalue
whose `k`th power is zero.  Hence `D_k` has exact degree `2^k`, and (6)
follows.  ∎

### Exact `k=1,...,5` coefficient ledger

Only nonzero `j:[a,b,c,d]` entries are shown; omitted degrees are exactly zero.
Together with (6), each line is the complete characteristic polynomial.

```text
k=1: 0:[1,0,0,0]; 1:[0,-1/6,1/2,0];
     2:[-1/2,0,0,-1/6]
k=2: 0:[1,0,0,0]; 1:[0,-1/6,1/2,0];
     3:[0,-1/6,1/6,0]; 4:[-1/6,0,0,-1/6]
k=3: 0:[1,0,0,0]; 1:[0,-1/6,1/2,0];
     2:[-1/2,0,0,-1/6]; 3:[0,1/6,-1/6,0];
     4:[0,0,0,1/9]; 5:[0,-1/9,0,0];
     6:[0,0,0,-1/9]; 7:[0,1/18,1/18,0];
     8:[-1/18,0,0,1/18]
k=4: 0:[1,0,0,0]; 1:[0,-1/6,1/2,0];
     3:[0,-1/6,1/6,0]; 4:[0,0,0,-1/9];
     5:[0,-1/18,1/18,0]; 7:[0,-1/27,0,0];
     8:[0,0,0,-2/27]; 9:[0,1/54,1/54,0];
     11:[0,1/162,1/54,0]; 12:[1/54,0,0,1/162];
     13:[0,-1/162,1/54,0]; 15:[0,-1/162,1/162,0];
     16:[-1/162,0,0,-1/162]
k=5: 0:[1,0,0,0]; 1:[0,-1/6,1/2,0];
     2:[-1/2,0,0,-1/6]; 5:[0,1/18,-1/18,0];
     6:[0,0,0,1/27]; 7:[0,-1/27,0,0];
     10:[1/54,0,0,-7/162]; 11:[0,1/54,5/162,0];
     12:[-5/162,0,0,1/54]; 15:[0,7/486,-7/486,0];
     16:[0,0,0,7/729]; 17:[0,-7/729,0,0];
     20:[-1/729,0,0,-2/729]; 21:[0,7/4374,1/1458,0];
     22:[-1/1458,0,0,7/4374]; 25:[0,0,-1/2187,0];
     26:[1/4374,0,0,1/13122];
     27:[0,-1/13122,1/4374,0]; 30:[0,0,0,-1/6561];
     31:[0,1/13122,1/13122,0];
     32:[-1/13122,0,0,1/13122]
```

## Proposition 4: complex closed walks and primitive paths

In the fixed qutrit basis, let a nonzero directed edge carry its matrix entry
from `B_k`.  Then

```text
Tr(B_k^n)=sum_(rooted length-n closed walks w) amplitude(w),
D_k(z)=product_[gamma primitive]
       (1-z^|gamma| amplitude(gamma)).              (7)
```

The first equality is matrix multiplication.  Every rooted closed walk has a
unique primitive cyclic root; grouping the formal logarithm by that root gives
the second equality.  The maximum absolute column sum of `B_k` is `sqrt(3)`.
Therefore the absolute closed-path logarithm is dominated for
`|z|<1/sqrt(3)`, where the raw product may be regrouped absolutely.  The
finite determinant itself is a polynomial on the whole plane; this does not
extend the raw path product beyond its proved local domain.

## Proposition 5: controls

1. **Closed control.**  If `P=I_3`, then `A_closed=F3^*` and `B_k,closed` is
   unitary of rank `3^k`; both defect projections vanish.
2. **Projector-order control.**  For `A_right=P F3^*`,
   `A_right=F3 A F3^*`.  Hence all power traces of `A_right` equal those of
   `A`; formula (4) proves that every `D_k` is unchanged.  Matrix entries and
   the placements of the left/right Gram projections do change, so this is an
   isospectral geometry control, not evidence of spectral order sensitivity.
3. **Hole-location control.**  For `P0=diag(0,1,1)` and `A0=F3^*P0`,
   `Tr(A0)=-sqrt(3)/3-i`, whereas `Tr(A)=sqrt(3)/6-i/2`.  Because the linear
   coefficient of every `D_k` is `-Tr(A)`, it changes from
   `-sqrt(3)/6+i/2` to `sqrt(3)/3+i`, although the opening rank is unchanged.

## Verification and boundary

The exact prefix checks 60 direct traces.  The `k=2`, period-eight path ledger
contains 510 rooted nonzero closed paths and 71 primitive cycles when totals
are summed over periods one through eight.  The independent checker passes
748 assertions, SymPy passes 141 checks, byte replay passes, and all 41 hostile
cases (40 repaired-hash and one stale-hash) are rejected.  These finite totals
test implementations; they do not prove the all-period statements.

The strict tuple is `(A1_WEAK,A2_FAIL,A3_FAIL,
A4_UNITARY_OR_SCATTERING_CANDIDATE)`, overall `ROUTE_A_EXPLORATORY`.
This is a finite-`k` subunitary scattering gate with a natural closed unitary
parent.  It is not a self-adjoint quantization and supplies no semiclassical
target matching.  We assert no antiunitary symmetry, target divisor,
functional equation, counting law, prime-like map, arithmetic local data,
Euler factors, root numbers, automorphy, Hilbert--Polya operator, or Route-B
authorization.  Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
