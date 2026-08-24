# C130 research question

## Frozen question

Can one mixing finite-type symbolic source support, with no period cutoff,

1. primitive closed suspension orbits;
2. an explicit two-state bivariate determinant;
3. a one-variable nonlattice exponential-polynomial determinant;
4. an exact primitive Euler/trace identity; and
5. a provable separation of suspension-time sectors,

while a roof-only rational control recovers lattice collisions and vertical
periodicity?

## Source lock

- Base: the two-sided full binary shift with
  `B=[[1,1],[1,1]]`.
- Roof: `tau(0)=1`, `tau(1)=sqrt(2)`.
- Suspension: `(Sigma_B x R)/((x,t+tau(x))~(sigma(x),t))`.
- Weight convention: destination-symbol weights, so
  `M(u,v)=B diag(u,v)`.
- Determinant: `Delta(u,v)=det(I-M(u,v))` and
  `d_tau(s)=Delta(exp(-s),exp(-sqrt(2)s))`.
- Precision: exact integer/formal-polynomial arithmetic and the algebraic
  basis `{1,sqrt(2)}`.
- Theorem cutoff: none.  Periods 1--10 form only a replay prefix.

## What would count as progress?

Progress is an all-period identity owned by the same frozen suspension,
together with an exact statement of what irrationality separates.  It must
not identify distinct orbits merely because their symbol populations agree.
The rational control must change only the roof pair and must exhibit both a
cross-sector collision and periodicity of the specialized determinant.

## What is out of scope?

No target zero/pole divisor is frozen.  No arithmetic Euler factors, prime or
zero tables, root number, functional equation, automorphy statement, natural
self-adjoint lift, or Route-B input may enter.  Therefore success on the
internal question cannot promote A2, A3, or A4.
