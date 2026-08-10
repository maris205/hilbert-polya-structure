# Narrative report — COPRIME-0001 countable trace stage

The breadth pivot sought a countable, genuinely recurrent object that avoids
the finite-state `O(T)` and modular Selberg `Omega(T^2)` subclasses without
reading target data. The selected object is the bi-infinite shift on labels
`n>=2` with the local rule `gcd(n_k,n_{k+1})=1`, suspended by `log(n_0)`.

Splitting the roof symmetrically across an edge gives the kernel
`K_s(m,n)=1_{gcd(m,n)=1}(mn)^(-s/2)`. Around a closed word the half-roof
factors telescope exactly to `prod_i n_i^(-s)`, fixing one clock and one trace
ledger.

The standard Mobius identity decomposes the kernel into rank-one terms. For
`sigma=Re(s)>1`, their trace norms sum to
`zeta(sigma)^2/zeta(2 sigma)-1`, so the family is trace class and holomorphic
in trace norm. The determinant `D_cop(s)=det_F(I-L_s)` is therefore defined on
that half-plane.

The domain is sharp for this Hilbert-space realization. Applied to `e_2`, the
kernel produces the odd-label sequence `(2m)^(-s/2)`. Its squared norm diverges
for `sigma<=1`. Any scalar continuation across the line would be a separate
analytic theorem, not a continuation of the same bounded operator.

Finite projections and absolute cycle summability yield the exact trace-power
identity. There are no self-loops. Period-two cycles are coprime unordered
pairs with a factor of two from the cyclic starting point. Period-three cycles
are pairwise-coprime triples; each unordered triple has two directed
orientations and six ordered representatives.

The exact certificate uses Fraction weights at `s=2`. The validation block
`2..10` has cyclic counts `0,44,120` for periods one through three, while the
sealed block `11..18` has `0,40,132`. A repetition control on labels `2..8`
passes through power six, including 1,183 primitive six-cycles and 7,192
cyclic words at the final power.

Route-A status is
`(A1_WEAK,A2_ANALYTIC_DETERMINANT,A3_PARTIAL_ANALYTIC_STRUCTURE,A4_FAIL)`.
The strongest missing ingredient is an arithmetic primitive-orbit law. The
next task is only a scalar continuation or barrier audit across `Re(s)=1`;
root matching and Route B remain closed.
