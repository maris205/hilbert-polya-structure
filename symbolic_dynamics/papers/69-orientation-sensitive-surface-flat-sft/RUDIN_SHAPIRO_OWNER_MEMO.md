# REJECTED CANDIDATE — NOT MANUSCRIPT CONTENT

## Owner-subtracted proof memo for the Rudin--Shapiro skew product

This file records the Stage-2 gate that rejected the original P69 candidate.
Nothing below is part of the replacement manuscript, and none of it is claimed
as a priority result.

### 1. Frozen system and exact edge-name count

Let `theta` be the constant-length substitution

```text
a -> ab,  b -> ac,  c -> db,  d -> dc,
```

let `(Y,S)` be its two-sided subshift, and put
`kappa(a)=kappa(b)=+1`, `kappa(c)=kappa(d)=-1`.  With `sigma` the shift on a
full `q`-shift, define

```text
F(y,x)=(Sy,sigma^(kappa(y_0))x).
```

For `w=w_0...w_(n-1)` put `s_0=0` and
`s_j=sum_(i<j)kappa(w_i)`.  Define

```text
r(w)=1+max_(0<=j<=n)s_j-min_(0<=j<=n)s_j.
```

Use the clopen edge partition which records `y_0` and the two fibre symbols at
coordinates `0` and `kappa(y_0)`.  At times `0,...,n-1` it reads precisely the
fibre coordinates `s_0,...,s_n`.  Since every increment is `+1` or `-1`, this
visited set is the full integer interval between its extrema.  Distinct base
words remain distinguished by their base names.  Hence the number of nonempty
length-`n` atoms is exactly

```text
C_q(n)=sum_(w in L_n(Y)) q^(r(w)).                         (RS-1)
```

Carrasco--Vargas already writes the corresponding exponential visited-range
sum as Equation (14) in the proof framework for generalized `[T,T^-1]`
systems; Proposition 4.8 supplies the spanning-number comparison.

### 2. Range equals a running maximum

Let `M(m)` be the largest signed sum of a length-`m` Rudin--Shapiro factor and
let `rho(m)=M(m)+1`.  Lü--Chen--Wen--Wu prove sign symmetry in Lemma 2 and
`rho=M+1` in Lemma 3; their Theorem 1 gives the maximal-sum recurrence and
Corollary 2 gives `Delta M in {-1,+1}`.

For a fixed `w`, the difference of two partial sums is the signed sum of the
contiguous factor between them.  Therefore `r(w)-1` is the largest absolute
sum of a contiguous subfactor of `w`.  Sign symmetry turns absolute maxima
into `M(m)`, and recurrence/minimality of the primitive substitution language
lets every factor of length `m<=n` extend to a factor of length `n`.  Thus

```text
R(n):=max_(w in L_n(Y)) r(w)
    =1+max_(1<=m<=n)M(m)
    =max_(1<=m<=n)rho(m).                                (RS-2)
```

Lü--Han define `s(k)=min{n:rho(n)=k}` in Definition 1 and prove in Lemma 4

```text
s(2k)=4s(k)-1,  s(2k+1)=4s(k),  k>=2.                  (RS-3)
```

Because the first differences do not skip an integer, (RS-2) becomes

```text
R(n)=max{k:s(k)<=n}.                                    (RS-4)
```

### 3. Exact dyadic law

For `t>=0`, repeated use of the odd branch of (RS-3) gives

```text
s(3*2^t-1)=4^t,
s(2^(t+2)-1)=2*4^t.
```

The adjacent first occurrences satisfy

```text
s(3*2^t)=(5*4^t+1)/3 > 4^t,
s(2^(t+2))=(8*4^t+1)/3 > 2*4^t.
```

Inverting by (RS-4) yields, for every `j>=0`,

```text
R(2^j)=3*2^(j/2)-1                 if j is even,
R(2^j)=2^((j+3)/2)-1              if j is odd.          (RS-5)
```

### 4. Envelopes and the complete accumulation interval

An elementary induction in (RS-3), with bases `k=2,3`, proves

```text
27s(k)<=5k^2+9,                                          (RS-6)
```

and equality is preserved by the even branch from `k=3`; hence equality holds
at `k=3*2^t`.  If `R(n)=m`, then `n<s(m+1)`, so (RS-6) gives

```text
liminf R(n)/sqrt(n) >= 3sqrt(3/5).
```

At

```text
n_t=s(3*2^t)-1=(5*4^t-2)/3
```

one has `R(n_t)=3*2^t-1`, proving equality.  Lü--Han's Theorem 1 gives the
pointwise upper bound `rho(n)<=3sqrt(n)`.  Therefore `R(n)<=3sqrt(n)`, while
the even cases of (RS-5) approach `3`; hence

```text
liminf R(n)/sqrt(n)=3sqrt(3/5),
limsup R(n)/sqrt(n)=3.                                  (RS-7)
```

Corollary 2 of Lü--Chen--Wen--Wu implies
`R(n+1)-R(n) in {0,1}`.  Together with `R(n)<=3sqrt(n)`, this shows that
successive differences of `R(n)/sqrt(n)` tend to zero.  Any sequence with
vanishing successive differences crosses every intermediate value between
its liminf and limsup arbitrarily late.  Consequently

```text
Acc{R(n)/sqrt(n)}=[3sqrt(3/5),3].                       (RS-8)
```

### 5. Relation to topological slow entropy

The primitive constant-length base has linear factor complexity.  From
(RS-1),

```text
R(n)log q <= log C_q(n) <= R(n)log q+O(log n).          (RS-9)
```

For a product cylinder of fixed radius `L`, an `n`-Bowen name reads a base
word with a fixed buffer and the fibre interval enlarged by at most `2L`.
Thus its logarithmic spanning/separated counts differ from the right side of
(RS-9) by `O_L(log n)`.  With the root-exponential scale
`a_n(t)=exp(t sqrt(n))` in the definition of topological slow entropy from
Carrasco--Vargas, Section 2.4, the threshold calculation gives

```text
upper ent_a(F)=3 log q,
lower ent_a(F)=3sqrt(3/5) log q,                        (RS-10)
```

and the accumulation set of normalized logarithmic name counts is the entire
interval between these values.  In the adapted scale of Carrasco--Vargas
Equation (14), the same exact sum is already built into the scale and their
Proposition 4.8 and Proposition 4.9/Theorem 1.3 own the general transfer to the
fibre entropy `log q`.

### 6. Exact owner ledger

1. X. Lü, J. Chen, Z. Wen and W. Wu, “On the abelian complexity of the
   Rudin--Shapiro sequence,” *Journal of Mathematical Analysis and
   Applications* **451** (2017), 379--390,
   DOI `10.1016/j.jmaa.2017.02.019`, arXiv:`1606.06935`.
   Relevant exact locations: Theorem 1, Corollary 2, Lemmas 2--3.
2. X. Lü and P. Han, “A Note on the Abelian Complexity of the Rudin--Shapiro
   Sequence,” *Mathematics* **10** (2022), article 221,
   DOI `10.3390/math10020221`.  Relevant exact locations: Definition 1,
   Lemma 4, Theorems 1--2, Corollary 1.
3. P. Carrasco-Vargas, “Topological slow entropy, sequence entropy, and
   generalized `[T,T^-1]` systems,” arXiv:`2506.17932` (2025).
   Relevant exact locations: Section 2.4 (definition of upper/lower
   topological slow entropy), Equation (14), Proposition 4.8, and Proposition
   4.9/Theorem 1.3.

### 7. Gate verdict

**REJECTED / REPLACED.**  After subtracting the owners' maximal-sum,
first-occurrence, density, and general range-sum/slow-entropy results, the
remaining Rudin--Shapiro specialization is a short inverse-envelope argument.
A genuinely independent measure/topological theorem would require uniform
local-time or Hamming-cover estimates that were not established.  The
candidate therefore did not have theorem-sized independent mass and is not
used in the replacement P69 manuscript.

