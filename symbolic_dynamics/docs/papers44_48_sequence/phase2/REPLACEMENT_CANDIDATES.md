# Replacement-Candidate Ledger — P44–P48 Phase 2

## Status

`PHASE2 CLOSED / REPLACEMENTS B AND C ADMITTED / NO AUTHORITY WRITE`

The original finite-prime-square census and all-`k` perfect-power operator
are mathematically correct but do not survive nearest-owner subtraction as
standalone papers.

## Withdrawn standalone candidates

### Finite-prime-square census

Manada--Kashyap already own general PFT zeta machinery, while the finite
`B`-free literature owns the sofic/hereditary approximation.  After that
subtraction, the explicit CRT fixed-point formula, `rad(P0)` least-period
criterion, standard Moebius inversion, and coefficientwise limit occupy only
a compact specialization.  Decision: `STOP_STANDALONE / MERGE_CONTROL`.

### Perfect-power product operator

Hilberdink already owns the prime tensor product, Hilbert--Schmidt Euler
criterion, norm product, compact spectral product, and multiplicative-Hankel
framework.  The residue-complement diagonalization is correct, but its
`S_q` thresholds, trace powers, and `det_2` factors then follow mechanically.
Decision: `STOP_SALAMI / MERGE_WORKED_EXAMPLE`.

## Replacement A — admissible-tower zeta pole wall

The replacement is not the withdrawn finite-stage CRT example.  It must be a
general theorem about nested periodic hereditary masks (with pairwise-coprime
prime-power towers as a fully audited arithmetic class):

- entropy converges to a prescribed positive limit while periodic entropy
  drops to zero at the limit;
- the first nontrivial period tends to infinity and yields local uniform
  convergence of zeta functions on the maximal subcritical disk;
- the radii of the approximating rational zeta functions converge to a
  strict value below the radius of the formal coefficientwise limit;
- dominant Perron poles form a quantitatively controlled dense wall on the
  critical circle;
- an abstract `first-period / exponential-envelope / presentation-period`
  criterion separates the general mechanism from the prime-square example.

Current decision: `HOLD_GENERAL_THEOREM_AND_POLE_PROOF_REQUIRED`.

## Replacement B — isospectral arithmetic fiber retractions

A single radical operator is too close to generic weighted-composition theory.
The only admissible version is the all-`h` comparison of two source-canonical
retractions onto the `h`-free integers.  For `h>=2`, put

```text
tau_h(n) = product_p p^min(v_p(n),h-1),
omega_h(n) = product_p p^(v_p(n) mod h),
S_{h,s} e_n = n^(-s/2) e_{tau_h(n)},
M_{h,s} e_n = n^(-s/2) e_{omega_h(n)}.
```

Both operators fix the same `h`-free basis and therefore have the same
nonzero eigenvalues, power traces, and regularized determinant ledger.  Their
fiber geometry is nevertheless different.  With `sigma=Re(s)>0` and
`m` `h`-free,

```text
rho_S(m)^2 = m^(-sigma)
             product_{p:v_p(m)=h-1}(1-p^(-sigma))^(-1),
rho_M(m)^2 = m^(-sigma) zeta(h sigma).
```

The proposed indivisible theorem package is:

- exact polar and singular-value decompositions for both fiber systems;
- `S_{h,s}` is bounded and compact for every `sigma>0`, whereas `M_{h,s}`
  is bounded and compact exactly for `sigma>1/h`;
- `S_{h,s} in S_q iff sigma>2/q`, while
  `M_{h,s} in S_q iff sigma>max(1/h,2/q)`; the corresponding power criterion
  replaces `sigma` by `k sigma` in the ideal wall while retaining the
  `1/h` existence wall for `M`;
- their common legal trace ledger
  `Tr(T^k)=zeta(k s/2)/zeta(h k s/2)` and hence identical ordinary
  regularized determinants wherever defined;
- exact Riesz-projection norms: the saturated system has
  `product_{p:v_p(m)=h-1}(1-p^(-sigma))^(-1/2)`, while the modulo system has
  the constant `sqrt(zeta(h sigma))`;
- consequently `S_{h,s}` is boundedly similar to a normal compact diagonal
  operator exactly for `sigma>1`, but `M_{h,s}` is so similar throughout its
  bounded domain `sigma>1/h`; primorial saturated fibers prove the negative
  endpoint;
- a second, adjoint-sensitive ideal wall:
  `[S^*,S] in S_q iff sigma>1/q` and
  `[M^*,M] in S_q iff sigma>max(1/h,1/q)`;
- for `h=2`, if
  `lambda_m=product_{p|m}(p^sigma-1)^(-1)` and
  `delta_m=product_{p|m}(1-p^(-sigma))`, each nontrivial commutator block has
  two equal singular values
  `lambda_m sqrt(1-delta_m)`; for `sigma>1/2` its Hilbert--Schmidt norm is the
  exact difference of two separately convergent Euler products;
- a free-UFD clone proving that neither retraction is a hidden
  rational-prime selector.

Paper 27 already owns the warning that ordinary cyclic invariants cannot see
oblique incidence geometry and proves a different zeta/Moebius similarity for
`eta>1`; Paper 28 then carries out the project's adjoint/Gram/Schatten route.
The replacement cannot be described as merely fulfilling an open adjoint
obligation.  It is admissible only as a new pairwise arithmetic-retraction
classification whose maximal-order projection law, singular Weyl constants,
and exact three-wall phase diagram remain after subtracting both papers.
Generic weighted-composition theory owns the abstract operator framework.
The independent Tauberian/source audit reproduced the full theorem after the
mandatory P27--P30/P43 and generic weighted-composition subtraction.  Current
decision: `GO_WITH_FIREWALL`; the `h=2` singleton remains `STOP`.

## Replacement C — q-adic finite-size boundary spectrum

For a primitive zero-one matrix `A` and `q>=2`, let

```text
X_A^(q)={x:A[x_n,x_(qn)]=1 for every n>=1}
```

and let `Z(N)` count admissible prefixes on `[1,N]`.  The known multiplicative
chain product and entropy are prior-owned and receive no novelty credit.  The
new indivisible package begins with the exact increment

```text
log Z(N)-log Z(N-1)=c_(nu_q(N)),
c_v=log(W_(v+1)/W_v),
W_l=1^T A^(l-1)1.
```

After subtracting the Perron eigenvalue, exact summation extends the bounded
remainder `log Z(N)-hN` to a continuous function on `Z_q`.  Its image is the
complete accumulation set of the finite-size correction.  In the
multiplicative golden-mean control, Binet's formula yields a strongly
separated digit series with Cantor dimension

```text
log 2/(2 log phi),
```

and a lacunary Lambert generating function with dense dyadic pole-type
boundary singularities and a unit-circle natural boundary.
Fan--Liao--Ma, Kenyon--Peres--Solomyak, and Ban--Hu--Lai own the object,
leading entropy/dimension, and boundary-complexity setting, but not this
exact `q`-adic order-one spectrum.  Two independent audits returned `GO`.
The frozen theorem and ownership details are in
`REPLACEMENT_C_THEOREM_AUDIT.md`.

Current decision: `GO_WITH_FIREWALL`.

## Rejected emergency replacements

- Babylonian/Pythagorean graph: Benito--Varona (2002) already own the same
  `c N log N` leg-bound asymptotic and constant; `STOP_EXACT_PRIMARY_SOURCE`.
- `mn+1`-square Diophantine graph: its clique/cycle core belongs to classical
  Diophantine-tuple theory and the residual weighted ideal staircase is too
  thin; `STOP_SALAMI`.
- Pythagorean-leg and square-sum weighted kernels: either exact primary
  ownership, an unresolved endpoint, or same-batch salami risk.

Replacements B and C received two independent source/proof signatures.  The
five-way Devil's Advocate gate assigns them P45 and P44, respectively;
Replacement A remains an unnumbered `HOLD_BACKUP`.
