# Final Sequence Gate — Papers 44–48

## Status

`PHASE2 CLEAN / FIVE GO / NO AUTHORITY WRITE`

This gate is evaluated against the accepted Papers 1–43 tree at Git commit
`6e5658649d2eab0fce077cbcdcc00070dd54095f`.  No position inherits A0
credit, novelty, priority, or a Route outcome.  The numbering is a dependency
order, not a ranking.  All Phase-2 work remains outside the authority tree;
this document authorizes no authority, Git, README, or mirror write.

The Phase-1 finite-prime-square and perfect-power-product proposals were
mathematically correct but failed nearest-owner subtraction.  They are not
silently renamed below: their STOP/MERGE chronology is preserved in the
rejected-candidate ledger.

## Proposed sequence

### Paper 44 — q-adic finite-size laws for multiplicative SFTs

Let `q>=2`, let `A` be a primitive zero-one matrix, and freeze

```text
X_A^(q)={x in alphabet^N : A[x_n,x_(qn)]=1 for every n>=1}.
```

If `Z(N)` counts admissible prefixes on `[1,N]`, define

```text
W_0=1,
W_l=1^T A^(l-1)1,
c_v=log(W_(v+1)/W_v).
```

The first exact theorem is the finite-size increment law

```text
log Z(N)-log Z(N-1)=c_(nu_q(N)).
```

Let `rho` be the Perron eigenvalue, `d_v=c_v-log rho`, and

```text
h=sum_{v>=0}(q-1)q^(-v-1)c_v.
```

Then

```text
log Z(N)=hN+E(N),
E(x)=-sum_{v>=1}(d_v-d_(v-1))(x mod q^v)/q^v,
x in Z_q.
```

The series defines a continuous function on the `q`-adic integers and

```text
Acc{log Z(N)-hN}=E(Z_q),
Acc{Z(N)exp(-hN)}=exp(E(Z_q)).
```

For `q=2` and the golden-mean adjacency, Binet's formula gives a strongly
separated digit series with

```text
dim_H E(Z_2)=dim_B E(Z_2)=log 2/(2 log phi).
```

The dyadic-scale content has this exact Cantor accumulation spectrum.  A
lacunary Lambert-series corollary has dense dyadic pole-type boundary
singularities with nonzero radial residues and a unit-circle natural
boundary, but that one-page corollary is not the novelty anchor.

Fan--Liao--Ma and Kenyon--Peres--Solomyak own the object, Fibonacci chain
product, leading entropy, and leading dimension.  Ban--Hu--Lai own the
boundary-complexity setting.  Paper 44 claims only the exact order-one
`q`-adic remainder, its full accumulation image, and the golden Cantor
geometry.  General multiplicative-SFT definitions and leading formulas must
be cited as inputs.

### Paper 45 — isospectral arithmetic fiber retractions

For every `h>=2`, let

```text
tau_h(n)=product_p p^min(v_p(n),h-1),
omega_h(n)=product_p p^(v_p(n) mod h),
S_(h,s)e_n=n^(-s/2)e_(tau_h(n)),
M_(h,s)e_n=n^(-s/2)e_(omega_h(n)).
```

Both retractions fix the same `h`-free basis and have identical nonzero
eigenvalues, legal power traces, and regularized determinants.  On their
common bounded domain `sigma>1/h`, the ordinary trace formula is legal only
when `k sigma>2`:

```text
Tr(T^k)=zeta(ks/2)/zeta(hks/2).
```

Their singular and nonnormal geometry differs.  With `sigma=Re(s)` and
`J_h(m)={p:v_p(m)=h-1}`,

```text
rho_S(m)^2=m^(-sigma) product_(p in J_h(m))(1-p^(-sigma))^(-1),
rho_M(m)^2=m^(-sigma) zeta(h sigma).
```

The full phase theorem is

```text
S bounded/compact iff sigma>0,
M bounded/compact iff sigma>1/h,
S in S_q iff sigma>2/q,
M in S_q iff sigma>max(1/h,2/q).
```

The Riesz projections satisfy

```text
||P_S(m)||=product_(p in J_h(m))(1-p^(-sigma))^(-1/2),
||P_M(m)||=sqrt(zeta(h sigma)).
```

Hence `S` is boundedly similar to a compact normal diagonal operator exactly
for `sigma>1`, while `M` is so similar throughout its bounded domain.  The
paper must prove the primorial maximal-order transition, including the
Mertens endpoint, rather than cite the threshold without its arithmetic
growth law.

The singular Weyl constants are explicit.  For

```text
w_(h,sigma)(m)=m product_(p in J_h(m))(1-p^(-sigma))^(1/sigma),
```

the Tauberian theorem gives

```text
s_n(S)~(C_(h,sigma)/n)^(sigma/2),
s_n(M)~(D_(h,sigma)/n)^(sigma/2),
```

with the explicit Euler products frozen in the theorem audit, whereas the
common eigenvalue constant is `1/zeta(h)`.  At `sigma=1`, however,
`C_(h,1)=D_(h,1)=1` for every `h`: the two singular leading terms coincide
exactly while only the modulo system is similar to normal.  Finally,

```text
[S*,S] in S_q iff sigma>1/q,
[M*,M] in S_q iff sigma>max(1/h,1/q).
```

Generic weighted-composition theory owns the fiber framework.  Papers
27--28 own the project's general obliqueness, similarity, adjoint, Gram, and
Schatten lessons; Paper 30 owns the free-UFD firewall, and Paper 43 owns an
`h`-free inventory in a different dynamical object.  No novelty credit is
assigned to those mechanisms.  The eligible unit is the all-`h` paired
classification, exact maximal order, two singular Weyl laws, and the
self-commutator wall.  The `h=2` radical operator alone is forbidden as a
standalone paper.  A free-UFD clone is mandatory and must reproduce the
theorem.

### Paper 46 — dyadic-sum Hankel operator

Freeze

```text
H_s(m,n)=1_(m+n is a power of two)(mn)^(-s/2).
```

The principal package is the exact bounded/compact, Hilbert--Schmidt, and
trace-class phase diagram; the `v_2`-preserving orthogonal direct sum over
odd vertices; the trace and `det_2` product; and the complete odd/even
linear-solver theorem for closed cycles with power-of-two edge labels.

The sharp safe thresholds are

```text
bounded/compact iff Re(s)>0,
Hilbert--Schmidt iff Re(s)>1/2,
trace class iff Re(s)>1.
```

Thus `1/2<Re(s)<=1` is a genuine `det_2` strip.  Generic Hankel--Besov
theory, finite unweighted Hankel determinants, and finite graph-label
solvers are prior art.  The paper does not claim an unproved all-`S_p`
criterion.

### Paper 47 — harmonic/Egyptian adjacency operator

Freeze the looped symmetric kernel

```text
E_s(m,n)=1_(m+n divides mn)(mn)^(-s/2).
```

Every edge has the unique coprime-scale form

```text
m=t a(a+b), n=t b(a+b), gcd(a,b)=1.
```

The phase diagram is

```text
Re(s)<=0       : unbounded,
0<Re(s)<=1/2   : compact, not Hilbert--Schmidt,
1/2<Re(s)<=1   : Hilbert--Schmidt, not trace class,
Re(s)>1        : trace class.
```

The principal package also includes the following domain-qualified traces:

```text
Tr E_s=2^(-s)zeta(s)                              (Re(s)>1),
Tr E_s^2=zeta(2s) zeta_MT(s,s;2s)/zeta(4s)       (Re(s)>1/2),
```

and a genuinely mixed closed-cycle ledger.  Egyptian-fraction
parametrization and Mordell--Tornheim series are classical.  Loops are part
of the frozen object; deleting them destroys the trace and endpoint proof
and is a required negative control.

### Paper 48 — radix carry-free Schatten transition

For every integer radix `b>=2`, freeze

```text
B_(b,s)(m,n)=1_(m+n has no carry in base b)(mn)^(-s/2),
m,n>=1.
```

Let

```text
C_b[a,c]=1_(a+c<b), 0<=a,c<b,
kappa_(b,q)=||C_b||_(S_q),
tau_b=kappa_(b,1),
alpha_b=log_b(tau_b).
```

For `1<=q<infinity`, the all-radix theorem is

```text
B_(b,s) in S_q iff Re(s)>max(1,log_b kappa_(b,q)).
```

The case `q=infinity` is the separate boundedness statement.  In particular,
boundedness, compactness, and Hilbert--Schmidt membership are equivalent to
`Re(s)>1`, while trace class is equivalent to
`Re(s)>max(1,alpha_b)`.  The explicit finite singular-value formula gives
`tau_b>b` for every `b>=2`, so this maximum equals `alpha_b`; equality is
excluded.  The paper owns the exact shell
Kronecker norms, equality pinching, weighted trace and `det_2` ledger, and
the corrected infinite least-period boundary: all positive integers for
`b>2`, and all integers at least two for `b=2`.

For prime `b=p`, Kummer identifies the edge predicate with
`p` not dividing `binom(m+n,m)`; this is a corollary, not the all-radix
definition.  Kummer, Lucas, finite Boolean/binomial/Pascal/disjointness
spectra, finite tensor norms, and the binary Lucas census are prior art.
Every finite zero-completed or positive-prefix census is a validation
control and contributes zero novelty.

## Required two-evaluator separation

| Paper | Evaluator A | Evaluator B |
|---|---|---|
| 44 | direct prefix enumeration and successive finite differences | independent `q`-free chain product, residue-series `Z_q` map, and pole residues |
| 45 | finite fiber matrices: SVD, powers, Riesz projections, commutators | independent Euler/Tauberian, primorial, and saturated-versus-modulo formulas |
| 46 | finite cutoff SVD/traces/regularized determinants | edge-label tuples, odd/even cycle solver, and `v_2` direct sum |
| 47 | cutoff matrix plus divisor-row enumeration | primitive `(t,a,b)` enumerator and Mordell--Tornheim truncation |
| 48 | finite cutoff SVD and base-`b` trace powers | shell Kronecker norms plus independent digit-DP/zero-deletion controls |

No pair may share production source, serialized intermediates, fixtures, or
expected-value tables.  Agreement is canonical-byte agreement only after
independently specified scientific projections.

## Stop and merge decisions

- finite-prime-square census: `STOP_STANDALONE / MERGE_CONTROL`; finite-B
  and PFT ownership leaves only a short CRT specialization;
- all-`k` perfect-power product kernel: `STOP_SALAMI / MERGE_WORKED_EXAMPLE`;
  Hilberdink's tensor theorem makes the residue specialization mechanical;
- admissible-tower pole wall: `HOLD_BACKUP`; the cross-tower phenomenon is
  plausible, but generic PFT pole ownership leaves a higher collision risk
  than the admitted q-adic boundary theorem;
- the `h=2` radical retraction alone: `STOP_GENERIC_SPECIALIZATION`;
- all-`h` power-free-gcd and coprimality kernels: `MERGE_CONTROL`;
- primorial odometer, finite holonomy, finite fiber/roof, and typed closure:
  `STOP_DUPLICATE_OR_SALAMI`;
- squarefree renewal, Ledrappier three-dot, beta `3/2`, Pythagorean/Babylonian
  graph, and Diophantine `mn+1` graph: `STOP_PRIMARY_OWNER_OR_SALAMI`;
- visible-lattice finite-prime census: `MERGE_FINITE_B_CONTROL`;
- square-sum and Pythagorean-leg weighted kernels: `STOP_ENDPOINT_OR_SALAMI`;
- cyclic multiplicative SFT: `STOP_CLASSICAL_COMPONENT_ASSEMBLY`.

## Final admission conditions

The sequence becomes frozen only if a fresh Devil's Advocate pass confirms:

1. all five packages are correct at every endpoint and quantifier;
2. P44 returns all leading multiplicative-SFT formulas to Fan--Liao--Ma,
   Kenyon--Peres--Solomyak, and Ban--Hu--Lai;
3. P45's Tauberian constant and bounded-similarity iff theorem have passed an
   independent proof replay, and Papers 27--30/P43 are explicitly
   subtracted;
4. deleting the shared operator-ideal lemmas still leaves distinct principal
   theorems in P45--P48;
5. P46 and P47 remain separate because their `v_2` cycle solver and primitive
   Mordell--Tornheim trace survive deletion of the shared `0,1/2,1` staircase;
6. P48 proves every all-radix endpoint including equality, while all finite
   Boolean/Lucas/Pascal material remains zero-credit control;
7. all five admit two independent exact evaluators and hostile source/type/
   endpoint mutations before any integration implementation.

All seven conditions passed the final five-way Devil's Advocate replay.  The
Phase-2 package freezes five research positions, but it is not an authority
materialization authorization: each paper still requires its own source
lock, proof, independent evaluators, mutation/audit package, and Route gate.
