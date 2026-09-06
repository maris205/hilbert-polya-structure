# A critical-coupling second Weyl coefficient on the harmonic chain

2026-09-06. Unnumbered candidate, authored by the coordinator. This is a
complete proposed proof, not an admission, priority claim, or release. Source
ownership and non-author mathematical review remain required. One question
is pursued: the second counting coefficient at and above critical impedance,
including stability under arbitrary asymptotically critical couplings.

## 1. Contract and theorem

Let `x_0=0`, `x_n=pi sum_{j=1}^n 1/j` and `I_n=(x_{n-1},x_n)`.
Let `(b_n)` be positive real numbers such that `n b_n -> infinity`. In
`L^2(0,infinity)` define the quadratic form

    q_b[f]= integral |f'|^2 + sum_{n>=1} b_n |f(x_n)|^2,
    D(q_b)={f in H^1_0(0,infinity): sum b_n |f(x_n)|^2 < infinity}.

Here `H^1_0` means zero trace at zero, not an additional condition at
infinity. The operator `H_b` is the nonnegative self-adjoint operator
represented by this form. The source clock is `exp(-it H_b)` and the
observable is the inclusive eigenvalue count `N_b(k^2)`. The spatial
couplings are fixed independently of the spectral frequency `k`.

For `kappa>0`, define a periodic **comparison** problem on a cell of length
`pi`. For each `theta in [0,2pi)`, its form is

    q_{kappa,theta}[u]= integral_0^pi |u'|^2 + kappa |u(0)|^2,
    D_theta={u in H^1(0,pi): u(pi)=exp(i theta) u(0)}.

Let `nu_kappa(z,theta)` count its eigenvalues at most `z^2`, and set

    J_kappa(z)=(1/(2pi)) integral_0^{2pi} nu_kappa(z,theta) dtheta,
    C(kappa)=gamma + integral_0^infinity
                     [J_kappa(z)-z 1_{z>=1}]/z^2 dz.            (1)

`J` is the integrated density of states **per cell**, not per unit length.
This convention fixes all factors of `pi`. The comparison lattice is not
asserted to be globally conjugate to the shrinking harmonic chain.

**Proposed theorem.** The form `q_b` is densely defined, closed and has
compact embedding into `L^2`; the operator has strictly positive discrete
spectrum. If `b_n/n -> kappa in (0,infinity)`, then

    N_b(k^2)=k log k + C(kappa) k + o(k).                       (2)

The integral (1) converges. The function `C` is continuous and strictly
decreasing on `(0,infinity)`, and maps that interval onto
`(2 gamma-1,infinity)`. In particular

    lim_{kappa->infinity} C(kappa)=2 gamma-1,
    lim_{kappa->0+} C(kappa)=infinity.                          (3)

If `b_n/n -> infinity`, then

    N_b(k^2)=k log k+(2 gamma-1)k+o(k).                        (4)

If `b_n/n ->0` (still with `n b_n ->infinity`), the precise conclusion is

    [N_b(k^2)-k log k]/k ->infinity.                          (5)

No leading-order formula is asserted for this last general class. In
particular, (5) does not incorrectly give compact resolvent to the free
half-line `b_n=0`. All limits in (2), (4), (5) are for real `k ->infinity`,
including eigenvalue thresholds.

The proposed increment is the local-periodic counting reduction at critical
coupling, its second coefficient and full asymptotic-coupling stability. The
Kronig--Penney dispersion, Dirichlet divisor law, form representation,
min--max principle and finite-codimension bracketing are classical inputs.
No target Euler factors or target zero correspondence are asserted.

## 2. Closedness, compactness, and cut comparison

Point evaluation on each fixed finite interval is continuous in `H^1`.
If `f_j` is Cauchy for `||f||^2+q_b[f]`, it converges in `H^1_0` to `f`
and its weighted sampled values converge in `ell^2`. Coordinatewise
continuity identifies the latter limit with `sqrt(b_n) f(x_n)`. Thus
`q_b` is closed. Compactly supported smooth functions belong to its domain,
so it is dense.

The fundamental theorem for Sobolev functions and Cauchy--Schwarz give

    integral_{I_n} |f|^2
       <= 2(pi/n)|f(x_n)|^2 + 2(pi/n)^2 integral_{I_n}|f'|^2.

Consequently, for every integer `M>=1`,

    integral_{x_M}^infinity |f|^2 <= a_M q_b[f],
    a_M=2pi sup_{n>M}(1/(n b_n)) + 2pi^2/(M+1)^2 ->0.          (6)

Local Rellich compactness and this uniform tail estimate prove compact
embedding of the form unit ball. Zero cannot be an eigenvalue: `q_b[f]=0`
forces `f'=0` and the zero trace forces `f=0`. The compact spectral theorem
then gives a positive first eigenvalue and discrete spectrum tending to
infinity.

Requiring a function to vanish at a fixed set of `r` internal vertices
restricts the form domain by codimension at most `r`. The min--max
principle therefore places the restricted eigenvalue count between the
original count minus `r` and the original count. This holds for inclusive
counts, with multiplicities. On the restricted domain the chain splits
into independent Dirichlet-ended blocks, and the coupling term at each
cut vanishes. We use this comparison, not a claim that removing every
coupling changes the infinite count by finite rank.

## 3. Periodic-cell facts and a finite-chain estimate

The cell forms have compact resolvent. The Dirichlet-cell domain is a
codimension-one subspace of every `D_theta`, and its count is `floor(z)`.
It follows that

    floor(z) <= nu_kappa(z,theta) <= floor(z)+1.                (7)

Increasing `kappa` increases each fiber eigenvalue. Comparison to zero
coupling, followed by integration over `theta`, gives

    floor(z) <= J_kappa(z) <= z.                              (8)

For completeness, the free eigenfrequencies are
`|2j+theta/pi|`, `j in Z`; integrating their indicator functions over
`theta in [0,2pi)` gives exactly `z`. Thus the upper bound in (8) uses the
per-cell normalization rather than a hidden factor of `pi`.

The same endpoint estimate as in (6), on a cell of length `pi`, gives a
strictly positive uniform lower bound for all fiber eigenvalues. A sharper
description of the band bottom is useful below. The modulus of a
quasiperiodic function is periodic, has the same sampled and Hilbert norms,
and no larger derivative norm. Thus the bottom over all fibers is the
periodic ground state. Its positive symmetric solution is a multiple of
`cos(z(x-pi/2))`, with endpoint matching

    z tan(pi z/2)=kappa/2.

There is a unique solution `r(kappa) in (0,1)`, and it is strictly increasing
and continuous. This solution is the ground state because it is strictly
positive. Hence

    J_kappa(z)=0 for 0<=z<r(kappa).                            (9)

For each `z>r(kappa)` sufficiently close to the bottom, `J_kappa(z)>0`:
the periodic ground eigenvalue is below `z^2`, and continuous dependence
of the fiber forms on `theta` gives an open set of such phases. In fact
this argument works for every `z>r(kappa)`.

We next prove the finite-chain approximation needed for the varying
geometry. The elementary free-propagation and delta-jump matrices on one
cell have determinant one and half-trace

    D_kappa(z)=cos(pi z)+(kappa/(2z))sin(pi z).                 (10)

At `z=0` use the continuous limit. The quasiperiodic eigenvalue equation
is `D_kappa(z)=cos(theta)`. This is derived by taking the eigenvalues of
the two-by-two transfer matrix. When `z` is a positive integer, the same
matrix formula remains valid: its off-diagonal sine entry vanishes but
the nonzero delta shear does not, so the possible eigenphase is still
only `theta=0` or `pi`, and its eigenspace has dimension one.

Fix `z`. Away from the at most two phases solving this equation, the
integer-valued fiber count is locally constant. To justify continuity
here, multiplication by `exp(i theta x/pi)` puts all fiber forms on a
fixed periodic domain with coefficients continuous in `theta`, so their
compact eigenvalues vary continuously. By (7), the count minus
`floor(z)` is either 0 or 1. It is therefore the indicator of an arc
(or its complement, the whole circle, the empty set), with at most two
endpoint exceptions. A uniform phase mesh of `M` points approximates
the integral of such a function with discrepancy at most 4 in the
unnormalized sum. This deliberately loose constant covers all endpoints.

A ring of `M` cells with delta strength `kappa` at every junction
decomposes by the finite Fourier transform of cell translation into the
fibers `theta=2pi j/M`. Its inclusive count therefore differs from
`M J_kappa(z)` by at most 4. Imposing zero trace at the ring junction
cuts it to a Dirichlet-ended `M`-cell chain and has codimension one.
The form restrictions agree, since the endpoint delta term vanishes.
Thus its count `N^D_{M,kappa}(z^2)` satisfies the uniform estimate

    |N^D_{M,kappa}(z^2)-M J_kappa(z)| <= 5                     (11)

for every `M>=1`, `kappa>0`, and real `z>=0`. This estimate and the
comparison-cell facts are proved here for clarity; they are not claimed
as new Floquet theory.

The same phase equation shows that `J_kappa` is continuous in `z`:
for a fixed positive energy only finitely many phases have an eigenvalue
exactly there, so dominated convergence of the fiber counts applies
locally, using (7). In particular all Riemann integrals below away from
zero have the needed regularity.

## 4. Critical local-periodic reduction

First let `b_n=kappa n` exactly, with `kappa` fixed. From (6),

    integral_{x_M}^infinity |f|^2
       <= [2pi/kappa+2pi^2]/(M+1)^2 q_b[f].                   (12)

Choose a fixed `R` so large that `R^2>2pi/kappa+2pi^2` and
`R>1/r(kappa)+1`. For `M=ceil(Rk)`, the Dirichlet tail after `x_M`
has no eigenvalues at most `k^2`. Cutting there changes the count by
at most one. This is a proved tail exclusion, not an arbitrary numerical
cutoff.

Set `m=floor(sqrt(k))` and `epsilon=(log k)^(-2)` for large `k`.
The head consisting of cells `1,...,m`, with Dirichlet endpoints,
has total length `pi H_m`. Removing its `m-1` internal positive delta
terms and imposing zeros at all its internal vertices gives, by
finite-codimension comparison with the free interval,

    N_head(k^2)=k H_m+O(m).                                   (13)

One may obtain (13) directly: both the free interval and the coupled
interval restrict to the same `m` Dirichlet cells, with at most `m-1`
trace constraints. The free interval count is `floor(k H_m)`.

Partition the remaining integer cell indices into blocks
`a<n<=b`, starting at `a=m`, with `b=min(M,floor((1+epsilon)a))`.
For large `k`, `epsilon m>2`, so every step is positive. Except possibly
for the last shortened block, the endpoints grow by a factor at least
`1+epsilon/2`; always

    0<b-a<=epsilon a,   rho=b/a<=1+epsilon.

The number `B` of blocks is `O_kappa(epsilon^(-1) log k)`.
Imposing Dirichlet conditions at their boundaries changes the count by
at most `B+1`, in addition to the far-tail cut already counted.

For a block `a<n<=b`, map each cell affinely to a reference interval of
length `pi/a`, preserving endpoint values. The original/reference length
ratio is `s_n=a/n in [rho^(-1),1]`. On this common space the original
Hilbert norm is between `rho^(-1)` and 1 times the reference squared norm;
its derivative energy is between 1 and `rho` times the reference one.
At every internal node its coupling `kappa n` is between `kappa a` and
`rho kappa a`. All endpoint couplings vanish. Thus every Rayleigh quotient
is between the reference quotient and `rho^2` times that quotient.
Scaling the reference coordinate by `a` gives a `(b-a)`-cell problem
of cell length `pi` and strength `kappa`. Equation (11) yields

    (b-a)J_kappa(k/b)-5 <= N_block(k^2)
                              <=(b-a)J_kappa(k/a)+5.          (14)

Because `J` is nondecreasing, the discrete sum
`sum_{a<n<=b} J_kappa(k/n)` lies between the same two main terms.
We explicitly control the accumulated upper/lower discrepancy, which
cannot be discarded as a fixed-parameter Riemann-sum error.

Write `a_0=m<a_1<...<a_B=M` and `j_i=J_kappa(k/a_i)`.
Then `j_i` is nonincreasing, and

    sum_i (a_{i+1}-a_i)(j_i-j_{i+1})
       <=epsilon sum_i a_i(j_i-j_{i+1})
       <=epsilon [m j_0+sum_{i=1}^{B-1}(a_i-a_{i-1})j_i]
       <=epsilon k [1+log(M/m)].                             (15)

The last bound uses (8) and
`(a_i-a_{i-1})/a_i <= log(a_i/a_{i-1})`; the discarded last
summation-by-parts term is nonpositive. Equations (13)--(15) and the
cut errors imply

    N_{kappa n}(k^2)
        =k H_m+sum_{m<n<=M}J_kappa(k/n)
           +O_kappa(m+B+epsilon k log k).

The error is `o(k)`: `m=O(sqrt(k))`, `B=O_kappa(log^3 k)`, and
`epsilon k log k=k/log k`. By (8), replacing the head `k H_m`
with `sum_{n<=m}J_kappa(k/n)` costs at most `m`. By (9) and the
choice of `R`, all terms after `M` vanish. Therefore

    N_{kappa n}(k^2)=sum_{n>=1}J_kappa(k/n)+o(k).               (16)

This local-periodic reduction is the main analytic step. It keeps the
microscopic delta transmission in the transition region `n` of order `k`;
averaging the deltas into a scalar step potential would not justify this
second coefficient at critical coupling.

## 5. Evaluation of the second coefficient

Define, for `x>0`,

    G_kappa(x)=J_kappa(1/x)-x^(-1) 1_{x<=1}.

This function is bounded near zero by (8), is zero outside a fixed
bounded interval by (9), and is continuous away from zero and the single
cut point 1. Its integral at zero exists as an improper integral. Its
Riemann sums satisfy

    (1/k)sum_{n>=1}G_kappa(n/k) -> integral_0^infinity G_kappa(x)dx.

To see that no regularity at zero is tacitly assumed, discard `0<x<delta`:
boundedness controls both that integral and its normalized mesh sum by
`O(delta+1/k)`. On the remaining compact interval ordinary Riemann
convergence applies. Then send `delta` to zero.

Consequently

    sum_{n>=1}J_kappa(k/n)
      =k H_{floor(k)}+k integral_0^infinity G_kappa(x)dx+o(k)
      =k log k+C(kappa)k+o(k).

Changing variables `z=1/x` gives exactly (1). Equations (16) and this
identity prove (2) for exact linear couplings. All bounds concern the
inclusive finite counts, so there is no exclusion of eigenvalue thresholds.

## 6. Continuity, strict monotonicity, and endpoint values

At fixed `z>0`, the fiber eigenvalues depend continuously on positive
`kappa` by the fixed-domain forms. For a given `kappa`, the exceptional
phases with eigenvalue `z^2` form a finite set by (10). It follows by
dominated convergence and (7) that `J_kappa(z)` is continuous in `kappa`.
On a compact positive range of `kappa`, (9) provides a uniform gap at zero
and (8) provides an integrable majorant `1/z^2` for the integrand at
infinity. Hence `C` is continuous.

Fiber monotonicity shows `J_{kappa_1}>=J_{kappa_2}` if `kappa_1<kappa_2`.
Moreover `r(kappa_1)<r(kappa_2)`. Between those band bottoms the second
IDS is zero and the first is positive, as shown after (9). Integrating
their difference against `z^(-2)` proves strict decrease of `C`.

As `kappa` increases to infinity, monotone convergence of the finite-cell
forms imposes `u(0)=0`, hence also `u(pi)=0`. Their limiting form domain
is the dense Dirichlet domain. The compact finite-interval variational
principle gives convergence of each eigenvalue to the Dirichlet ones
`j^2`. Thus, for noninteger `z`, `J_kappa(z)->floor(z)`. The same
uniform gap and tail bounds justify dominated convergence in (1).
The limiting integral is

    integral_1^infinity [floor(z)-z]/z^2 dz
      =sum_{j>=1}[1/(j+1)-log((j+1)/j)]=gamma-1.

This proves the first limit in (3).

As `kappa` decreases to zero, finite-cell form convergence gives the free
fiber spectrum. Except at a finite set of phases for a fixed `z`, the
counts converge, so `J_kappa(z)->z`. To prove divergence of `C`, note
that its contribution from `z>=1` is at least `-1` by (8), whereas for
any `0<delta<1` its contribution from `delta<z<1` tends to
`integral_delta^1 dz/z=log(1/delta)`. The contribution on `(0,delta)`
is nonnegative. Sending `delta` to zero proves the second limit in (3).
Continuity and strict decrease now give the asserted exact range of `C`.

## 7. Asymptotic-coupling stability and the hard/soft sides

Suppose first `b_n/n ->kappa in (0,infinity)`. For every
`0<eta<kappa`, all but finitely many couplings obey

    (kappa-eta)n <= b_n <= (kappa+eta)n.

Impose zero traces at the finitely many exceptional vertices. On that
common finite-codimension domain the three forms are ordered. Min--max
and the cut comparison in section 2 therefore give, for a fixed integer
`r_eta` independent of `k`,

    N_{(kappa+eta)n}(k^2)-r_eta <= N_b(k^2)
                          <=N_{(kappa-eta)n}(k^2)+r_eta.

Subtract `k log k`, divide by `k`, use the already proved exact-coupling
law, and then let `eta` decrease to zero. Continuity of `C` proves (2)
without any rate of convergence for `b_n/n`. This is why arbitrary
`o(n)` perturbations, including nonmonotone ones, are allowed.

If `b_n/n ->infinity`, comparison with `K n` for every fixed `K>0`
gives the same upper bound with coefficient `C(K)`. A lower bound is the
fully decoupled Dirichlet operator: its form domain of functions vanishing
at every node is a subdomain of `D(q_b)`, and its eigenvalues therefore
lie above the coupled ones. Its classical counting law is

    N_D(k^2)=sum_{n<=k}floor(k/n)
       =k log k+(2 gamma-1)k+O(sqrt(k)).                       (17)

One can verify the stated error directly from the hyperbola identity
`sum floor(k/n)=2 sum_{n<=floor(sqrt(k))} floor(k/n)-floor(sqrt(k))^2`
and `H_m=log m+gamma+1/(2m)+O(m^(-2))`. This is the classical divisor
calculation, not a new arithmetic correspondence. Letting `K` tend to
infinity and using (3) proves (4).

Finally, if `b_n/n ->0`, comparison from above with every fixed `K n`
gives

    liminf_{k->infinity} [N_b(k^2)-k log k]/k >= C(K).

Since `C(K)->infinity` as `K->0+`, this is precisely (5). Compactness
in this case still uses the separately stated hypothesis `n b_n ->infinity`.
The proof of all proposed claims is complete.

## 8. Admission and scope risks

The classical harmonic chain with constant coupling and its Dirichlet endpoint
must be fully credited. The prior C400 finite-constant-coupling law has a
different leading coefficient (`2k log k`), and it cannot be substituted
into (14) in the critical transition region. The proposed theorem concerns
the full critical second-coefficient mechanism and arbitrary asymptotic
couplings, not a table of new numerical constants.

The required independent reviewer must check the fiber phase-mesh estimate,
block-coordinate form comparison, cumulative error (15), endpoint limits,
and the finite-codimension stability argument. Closest-source ownership and
paper-level significance remain provisional until that review and the
primary literature audit finish. No numerical experiment has yet run for
this candidate; the proof is not described as computationally certified.

`NO_BAD_EULER_OR_ROOT_NUMBER`: the self-adjoint source model and a two-term
mean law do not establish target Euler factors, root numbers, automorphy,
individual zero matching, or a Hilbert--Pólya realization. No meromorphic
spectral-zeta continuation follows merely from an `o(k)` counting remainder.
