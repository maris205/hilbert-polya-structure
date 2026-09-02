# Exact theorem package — HCS-C285

## 1. Frozen Gordon–Newell owner

Fix `m>=1`, a population `N>=0`, positive service rates `mu_i`, and an
irreducible row-stochastic routing matrix `P=(p_ij)`. Zero routing entries and
self-routing are allowed; detailed balance is not assumed. The state space is

`S_N={n in Z_+^m: sum_i n_i=N}`.

At an occupied station `i`, one exponential server completes work at total
rate `mu_i`; the customer is sent to `j` with probability `p_ij`. Thus the
row-generator acts by

`Lf(n)=sum_{i:n_i>0} mu_i sum_j p_ij[f(n-e_i+e_j)-f(n)]`.

The `j=i` term is a genuine service event but has zero generator increment.
Let `e` be the unique positive traffic vector normalized by

`e=eP`, `sum_i e_i=1`,

and put `w_i=e_i/mu_i`. This normalization is a gauge; replacing `e` by
`c e` multiplies every `w_i` by `c` without changing the stochastic law.

## 2. Canonical product form and complete moment calculus

Define the complete homogeneous polynomial

`Z_N=h_N(w)=[z^N] product_i (1-w_i z)^(-1)` and `Z_0=1`.

### Theorem 1 (finite canonical law)

For every frozen network above,

`pi_N(n)=Z_N^(-1) product_i w_i^(n_i)`, `n in S_N`,

is the unique stationary law. For the Euler derivative
`D_i=w_i partial/partial w_i`,

`E[n_i]=D_i log Z_N`,

`Cov(n_i,n_j)=D_i D_j log Z_N`.

More generally, for every multi-index `alpha in Z_+^m`,

`E[product_i (n_i)_(alpha_i)]
 = w^alpha partial_w^alpha Z_N / Z_N`,

where `(x)_r=x(x-1)...(x-r+1)`. Hence all ordinary joint occupancy moments
follow by Stirling conversion.

### Global-balance proof

Ignore self-events only while forming the state-change generator. For a state
`n`, outgoing nonself rate is

`sum_{j:n_j>0} mu_j(1-p_jj)`.

An incoming transition with destination `j` comes from `n-e_j+e_i`. Its
product weight relative to `n` is `w_i/w_j`. Therefore the incoming stationary
mass at a fixed occupied `j` is

`pi_N(n) sum_{i!=j} (w_i/w_j) mu_i p_ij
 =pi_N(n) (mu_j/e_j) sum_{i!=j} e_i p_ij
 =pi_N(n) mu_j(1-p_jj)`.

Summing over occupied `j` proves global balance without detailed balance.
Strong connectivity of `P` makes the composition chain irreducible when
`N>0`; at `N=0` it is a singleton. Differentiating the finite partition sum
gives the moment identities.

## 3. Throughput, edge flow, and exact reversal

Set `R_N=Z_(N-1)/Z_N` for `N>=1` and `R_0=0`. Decrementing an occupied
coordinate gives

`P(n_i>0)=w_i R_N`.

Consequently the station-completion throughput and directed service-event
flow (including self-routes) are

`T_i=mu_i P(n_i>0)=e_i R_N`,

`J_ij=e_i p_ij R_N`.

Traffic balance gives `sum_j J_ij=sum_j J_ji=T_i`; the stationary net current
is `C_ij=J_ij-J_ji=-C_ji`.

Define

`p*_ij=e_j p_ji/e_i`.

### Theorem 2 (time reversal and reversibility gate)

`P*` is irreducible and row-stochastic, has traffic vector `e`, and the exact
stationary time reversal of the occupancy process has the same service rates
and routing `P*`. Reversal is involutive. For `N>=1`, the state process is
reversible if and only if

`e_i p_ij=e_j p_ji` for every `i,j`,

equivalently `P*=P`. Reversed event flow is the transpose of forward event
flow. At `N=0` the singleton state process is trivially reversible for every
`P`; therefore it cannot identify a routing-level reversibility criterion.

### Proof

For `n_i>0`, put `n'=n-e_i+e_j`. Detailed time reversal gives

`q^rev(n',n)=pi(n) mu_i p_ij/pi(n')
 =mu_j e_i p_ij/e_j=mu_j p*_(j i)`.

The row sums and stationarity of `P*` follow from `e=eP`. Applying the same
formula twice returns `P`. Positive population supplies a transition along
every routing edge from some composition, so state detailed balance is
equivalent to the displayed traffic detailed balance.

## 4. Unique and tied bottleneck condensation

Let

`w*=max_i w_i`, `B={i:w_i=w*}`, `r=|B|`, `C=B^c`,

and `q_j=w_j/w*` for `j in C`. Define

`A(z)=product_{j in C}(1-q_j z)^(-1)`.

### Theorem 3 (normalizer and joint thermodynamic limit)

As `N->infinity` with `m,P,mu` fixed,

`Z_N ~ w*^N N^(r-1)/(r-1)! product_{j in C}(1-q_j)^(-1)`.

Moreover, in total variation on the discrete nonbottleneck coordinate and
weakly on the bottleneck simplex,

`(n_C,n_B/N) => (G,Y)`,

where the `G_j` are independent geometric variables on `Z_+` with
`P(G_j=k)=(1-q_j)q_j^k`, `Y~Dirichlet(1,...,1)`, and `G` and `Y` are
independent.

- If `r=1`, the unique bottleneck contains `N-O_P(1)` customers and
  `N-n_b=>sum_{j in C}G_j`.
- If `r>1`, the total nonbottleneck population remains tight but the
  bottleneck stations retain random macroscopic shares; no deterministic
  equal split is asserted.
- If every weight is equal, `C` is empty,
  `Z_N=binom(N+m-1,m-1)w*^N`, the finite law is exactly uniform on weak
  compositions, and the full normalized vector converges to
  `Dirichlet(1,...,1)`.
- If `m=1`, the Dirichlet law is the degenerate one-point law and the sole
  station contains all customers exactly.

### Exact finite decomposition and proof

After dividing by `w*^N`,

`H_N=[z^N](1-z)^(-r)A(z)
 =sum_(k=0)^N a_k binom(N-k+r-1,r-1)`,

where `a_k=[z^k]A(z)>=0` and `sum_k a_k=A(1)<infinity`. Dividing by
`binom(N+r-1,r-1)`, the summand ratio is at most one and tends to one for
each fixed `k`; dominated convergence proves the normalizer asymptotic.

For a fixed vector `k in Z_+^C`,

`P(n_C=k)=q^k binom(N-|k|+r-1,r-1)/H_N` when `|k|<=N`.

This converges to `product_j(1-q_j)q_j^(k_j)`. The limiting masses sum to
one, so pointwise convergence upgrades to total variation.

Conditional on `n_C=k`, put `M=N-|k|`. Every weak composition of `M` over
the `r` tied bottlenecks has the same weight, hence is exactly uniform. Its
conditional factorial moments are

`E[product_(i in B)(n_i)_(beta_i) | M]
 =(M)_(|beta|) product_i beta_i! (r-1)!/(r+|beta|-1)!`.

After division by `M^|beta|`, these are precisely the moments of the uniform
Dirichlet law in the limit. Compactness of the simplex makes the moment
limit determining. Total-variation tightness of `n_C` implies `M/N->1` and
also yields independence in the joint limit.

## 5. Boundary atlas

- `N=0`: one empty state, `Z_0=1`, zero occupancies, zero completion flows.
- `N=1`: `pi(customer at i)=w_i/sum_j w_j`; covariance is categorical.
- `m=1`: `P=[1]`, `Z_N=w_1^N`; service completions are self-events.
- `p_ij=0`: allowed, including periodic embedded routing, provided the
  routing digraph is strongly connected. Continuous time removes no need for
  irreducibility but imposes no aperiodicity assumption.
- `p_ii>0`: included in event flow and throughput, omitted from off-diagonal
  state changes.
- equal or tied weights: retained exactly; denominators such as
  `w_i-w_j` are never used in the owner theorem or checker.
- traffic gauge `e->c e`: `w->c w`, `Z_N->c^N Z_N`, while `pi`, `P*`,
  throughputs, and edge flows stay unchanged.
- `mu_i=0`: excluded singular face; the positive-service CTMC theorem does
  not evaluate infinite weights or trapped-customer classes.
- `w_i=0`: impossible under irreducible `P` and positive `mu`; it is not an
  interior boundary value to substitute into the theorem.
- reducible routing: excluded; a unique positive traffic vector and an
  irreducible composition owner need not exist.
- negative or nonintegral `N`: outside the state-space definition.

## 6. Executable evidence and proof boundary

The canonical evidence contains 9 exact network cases, all 177 states in
those cases, 165 joint factorial-moment cells through degree three, 9 flow
and 9 reversal rows, 28 finite condensation rows, and 12 boundary rows. The
producer-independent checker reconstructs the traffic vector, the complete
Fraction generator, its one-dimensional left nullspace, global balance,
three independent computations of `Z_N`, every stored moment and flow, and
all condensation cells. SymPy supplies a separate symbolic layer. Two fresh
paths reproduce the evidence byte for byte, and repaired-hash, drop/replace,
duplicate-key, and stale-hash attacks must fail closed.

These finite computations are regression oracles. The all-parameter and
thermodynamic statements are proved by the arguments above, not by
extrapolation from `N<=32`.

## 7. Ownership, collision, and Route-A result

Gordon and Newell (1967) own the classical closed exponential-server
product form and bottleneck asymptotic lineage. Kelly (1979) is the standard
reversibility reference, and Kelly–Yudovina (2014) is a modern queueing
network source. This package claims no literature originality; it supplies a
self-contained source-local synthesis and a hostile executable closure.

The nearest repository packages have different owners: C225 is a single
finite M/M/1/K birth–death spectrum; C263 is a reinforced Pólya urn; C220 is
open TASEP; C246 is an AIMD perpetuity; C282 is a killed risk process; C181 is
deterministic rotor routing. None contains this closed routed canonical
ensemble, traffic-equation reversal, and bottleneck-condensation theorem.

The strict Route-A tuple is

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.

There is no arithmetic origin, intrinsic deterministic primitive-orbit
owner, target dynamical determinant, target divisor, or natural same-clock
Hilbert–Pólya operator. The overall verdict is `ROUTE_A_REJECTED`; Route B is
false. Scope is exactly `NO_BAD_EULER_OR_ROOT_NUMBER`.
