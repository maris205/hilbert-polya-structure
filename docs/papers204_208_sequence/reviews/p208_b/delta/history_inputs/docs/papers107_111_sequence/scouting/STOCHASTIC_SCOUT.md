# Stochastic / random / hybrid candidate scout for P107--P111

Status: **scouting only; external release HOLD**
Date of bounded inventory and source gate: 2026-08-29
Edit boundary: this report and the two `scouting/code/stochastic_*` probes
only.  No existing paper was edited and no paper number is assigned here.

## Executive decision

The branch produced one mathematically strong paper candidate, one exact but
collision-heavy reserve, two further reserves, and six kills.

1. **S1, Bernoulli positive-Heisenberg word-area cocycle — GO internally,
   external HOLD.**  It has an exact finite-word matrix normal form, a
   Gaussian-binomial conditional law, exact biased moments, an explicit
   `n^(3/2)` CLT, a sharp polynomial norm exponent, and a kinked `n^2`-scale
   annealed area pressure.  The two proof lanes close independently.  The
   main weakness is ownership: the inversion statistic and its conditional
   Gaussian-polynomial law are directly owned background, and random walks
   on Heisenberg/unitriangular groups are mature.  A paper would therefore
   have to sell only the owner-subtracted dynamical conjunction.
2. **S2, clipped left/right path automaton — RESERVE, not recommended for
   this batch.**  The image diameter is exactly the unvisited span of a
   simple random walk, and the synchronization-time PGF factors into
   Chebyshev gambler's-ruin factors.  However, random-walk span first-passage
   laws have a direct 1986 owner, while the proof engine is too close to P93
   reflection and P101 monotone synchronization.

The top-two exact probes passed **298,964** assertions in total.  S8 is the
best fallback if S1 fails a specialist owner search, but S1 and S8 must not
be selected together because S8 is the next unitriangular/scattered-subword
level of the same mechanism.

## Inventory and collision protocol

An exact `find papers -mindepth 1 -maxdepth 1` scan found 101 on-disk paper
directories.  The difference from the nominal P1--P106 range is explicit:
P51--P56 are absent from `papers/`, while two distinct P96 directories are
present.  Both P96 objects were included in the collision check.  Titles and
the random/cocycle/automaton vocabulary in `main.tex`, `README.md`, and
`CLAIMS_EVIDENCE.md` were searched before candidate construction.

The relevant occupied regions are:

| Existing work | Occupied object / proof engine | Consequence here |
|---|---|---|
| P35--P36 | affine-semigroup and Cayley-chain obstruction packages | elementary affine randomizations receive a high collision penalty |
| P62 | random substitutions and projective entropy | no random substitution or substitution-matrix repackaging |
| P70 | finite-Heisenberg-quotient shifts and weighted congruence nullities | the name “Heisenberg” alone is not a firewall; S1 must use a genuinely different phase space, observable, and proof |
| P79 | noisy de Bruijn process and delayed irreversibility | no hidden/noisy finite-memory process |
| P86 | finite-field adjacent-product hidden process | no hidden-output or finite-dependence repackaging |
| P89 | Bernoulli reset random SFT, renewal rewards, quenched/annealed gap | no reset, regeneration, or rank-one renewal product |
| P91 | generalized-dihedral finite shift | finite group-walk candidates need a non-dihedral invariant |
| P93 | push--pop cocycle, reflected maximum, ballot laws, two thresholds | reflected-length/free-word systems and span systems are collision-heavy |
| P96 finite-subset circle expansion | deterministic integer circle expansion and finite-subset temporal census | random degree cocycles on the same base circle are too thin |
| P98 | repeated-root finite-field torsion shift | random nilpotent filters are an internal repeated-root/rank-loss collision |
| P99 | deterministic unipotent shear on index-`N` sublattices | random powers of one unipotent shear are excluded |
| P101 | random cap--floor interval synchronization | any monotone chain synchronization needs a different normal form and temporal law |
| P104 | monomial-toggle random matrix cocycle, folded CLT, annealed/quenched gap | a new random-matrix candidate cannot reuse occupation parity or exponential singular-value pressure |
| P105--P106 | deterministic graph pruning/polarity maps | randomizing their update schedules would be an unearned variant |

Hard exclusions applied before ranking were reset/renewal products,
push--pop or free-reduction reflections, cap--floor/order-statistic systems,
projection/overwrite/coupon processes, generic random rank-one products,
and randomizations of P96/P98/P99/P105/P106.

## Candidate ledger

### S1. Bernoulli positive-Heisenberg word-area cocycle — **GO / HOLD**

**Phase space and update.**  Work in the positive integer unitriangular
semigroup `UT_3(Z)`.  Put

```text
X = I + E_12,       Y = I + E_23,
P(A_t=X)=p,         P(A_t=Y)=q=1-p,
M_n=A_n ... A_1.    (A_1 acts first.)
```

For a word `w`, let `J_n` be its number of `X` letters and let

```text
C_n = #{(i,j): 1 <= i < j <= n, A_i=Y, A_j=X}.
```

**Early exact signals.**

1. Literal multiplication gives the complete finite-time normal form

   ```text
   M_n = [[1, J_n, C_n], [0, 1, n-J_n], [0, 0, 1]].
   ```

   Thus the noncommutative central coordinate is exactly a binary-word area,
   not a hidden renewal count or occupation parity.
2. Conditional on `J_n=j`, every binary word has the same probability and

   ```text
   sum_c #{C_n=c, J_n=j} z^c = GaussianBinomial(n,j;z).
   ```

   Consequently the full biased finite-time PGF is

   ```text
   E[z^C_n] = sum_{j=0}^n p^j q^(n-j) GaussianBinomial(n,j;z).
   ```

**Proposed theorem package.**  The following statements are already reduced
to proof-sized claims.

1. **Normal form and finite law.**  The displayed matrix identity and
   Gaussian-binomial slice law hold for every word, including `p=0,1`.
2. **Exact biased moments.**  For all `n>=0`,

   ```text
   E C_n = n(n-1)pq/2,

   Var(C_n) = n(n-1)pq/6 *
     [6n p^2 - 6n p + 2n - 9p^2 + 9p - 1].
   ```

   At `p=1/2`, this becomes `n(n-1)(2n+5)/96`.
3. **Strong law and explicit CLT.**  For `0<p<1`,

   ```text
   C_n/n^2 -> pq/2                        almost surely,

   (C_n-E C_n)/n^(3/2) => Normal(0,sigma_p^2),
   sigma_p^2 = pq(3p^2-3p+1)/3.
   ```

   A direct decomposition with `eta_k=1_{A_k=X}-p` is

   ```text
   C_n-E C_n
     = sum_{k=1}^n [k-1-p(n-1)] eta_k
       - sum_{i<j} eta_i eta_j.
   ```

   The first term satisfies a triangular-array Lindeberg CLT; the second is
   `O_P(n)` and is negligible on the `n^(3/2)` scale.  No general
   nilpotent-group CLT is needed for this biased positive walk.
4. **Polynomial norm phase boundary.**  For any fixed matrix norm,

   ```text
   log ||M_n|| / log n -> 2     a.s. for 0<p<1,
   log ||M_n|| / log n -> 1     at p=0 or p=1.
   ```

   Positivity makes the central entry a lower bound and the sum of the four
   nontrivial entries an upper bound.
5. **Sharp area-pressure kink.**  With
   `Lambda_p(theta)=lim n^(-2) log E exp(theta C_n)`,

   ```text
   Lambda_p(theta) = theta/4  for theta>0 and 0<p<1,
                   = 0        for theta<=0 or p in {0,1}.
   ```

   The upper bound is `C_n<=floor(n^2/4)`.  A single ordered word with
   balanced letter counts gives the matching lower bound at exponential
   probability cost only; a zero-area monotone word gives the negative-`theta`
   lower bound.  This is the cleanest dynamical statement not already equal
   to the standard conditional inversion law.

**Two independent proof / control routes.**

- **Matrix route:** induct on chronological left multiplication.  An `X`
  update increments `(J,C)` by `(1,n-J)`, while a `Y` update increments the
  lower shear only.  Literal `3 x 3` products are the falsification oracle.
- **Word-statistic route:** use
  `G(n,j)=G(n-1,j)+z^(n-j)G(n-1,j-1)`, conditional moments of binary
  inversions, total variance, and the displayed centered decomposition.
  Extremal ordered words prove the pressure separately.

**Exact probe.**  `code/stochastic_heisenberg_area.py` exhausts every word
through `n=15`, compares literal matrices to the word statistic, reconstructs
all Gaussian-binomial slices independently, checks conditional and biased
moments at `p=1/5,1/2,3/4`, and checks the CLT decomposition word by word
through `n=10`.  Result: **72,361 exact assertions, PASS**.

**Owner and collision gate.**

- Canfield--Janson--Zeilberger directly own the Gaussian-polynomial inversion
  distribution and asymptotic normality on fixed-composition words
  ([DOI 10.1016/j.aam.2009.10.001](https://doi.org/10.1016/j.aam.2009.10.001));
  their corrigendum must also be read before drafting
  ([DOI 10.1016/j.aam.2012.04.002](https://doi.org/10.1016/j.aam.2012.04.002)).
- Işlak--Özdemir include inversion counts in iid possibly biased random words
  within their subsequence framework
  ([DOI 10.1016/j.dam.2018.05.043](https://doi.org/10.1016/j.dam.2018.05.043)).
- Diaconis--Hough directly occupy random walks on Heisenberg and
  unitriangular groups, including coordinate limit theory
  ([DOI 10.24033/asens.2466](https://doi.org/10.24033/asens.2466)).
- **P70 firewall:** P70 is a deterministic finite-quotient group shift with
  convolution/nullity/Fermat-curve observables.  S1 is a positive random
  matrix semigroup with a central word-area observable.  The common
  Heisenberg algebra is disclosed, not hidden.
- **P99 firewall:** P99 iterates one shear on sublattices and proves finite
  cycles/zeta/recovery.  S1 has two noncommuting generators, no sublattice
  phase space, and no finite temporal zeta.
- **P104 firewall:** P104 has exponentially contracting monomial matrices,
  a two-state occupation chain, singular values, and order-`n` pressure.  S1
  is unipotent, has polynomial norm growth, a nonlocal pair statistic, and
  order-`n^2` pressure.

**Kill condition.**  Kill S1 if a specialist search finds the exact package
for iid positive generators `I+E_12,I+E_23`, or if owner subtraction leaves
only the observation that a matrix entry is an inversion count.  Search
absence is not evidence.  Otherwise it is the branch's sole recommended
paper slot, with every novelty/priority claim suppressed and external status
HOLD.

### S2. Clipped nearest-neighbour path automaton — **RESERVE**

**Phase space and update.**  On `P_m={0,1,...,m}`, let

```text
L(x)=max(x-1,0),     R(x)=min(x+1,m),
Phi_n=omega_n o ... o omega_1,
P(omega_t=L)=P(omega_t=R)=1/2.
```

Let `S_k` be the `+1/-1` driving walk, `H_n=max_{k<=n}S_k`,
`h_n=min_{k<=n}S_k`, and `R_n=H_n-h_n`.

**Early exact signals.**

1. The image is always an integer interval and

   ```text
   diam Phi_n(P_m) = (m-R_n)_+.
   ```

   Before synchronization its endpoints are exactly
   `S_n-h_n` and `m+S_n-H_n`.  Hence
   `T_m=inf{n:R_n>=m}` is the synchronization time.
2. Put `tau_r=T_{r+1}-T_r`.  Reflection symmetry and the strong Markov
   property make `tau_0,...,tau_{m-1}` independent.  If `U_r` denotes the
   Chebyshev polynomial of the second kind, then

   ```text
   E[z^tau_r] = [1+U_r(1/z)]/U_{r+1}(1/z),

   E[z^T_m] = product_{r=0}^{m-1}
              [1+U_r(1/z)]/U_{r+1}(1/z).
   ```

**Proposed theorem package.**

1. The deterministic image/span identity for every direction word.
2. The factorized fair synchronization-time PGF above.
3. Exact moments

   ```text
   E T_m = m(m+1)/2,
   Var(T_m) = m(m-1)(m+1)(m+2)/12.
   ```

4. An optional biased extension should be stated only as a product of
   explicit `2 x 2` boundary-orientation gambler's-ruin kernels.  At the
   deterministic endpoints the time is `T_m=m`; no fair-symmetry
   independence claim may be silently extended to biased walks.

**Two independent proof / control routes.**

- **Cocycle route:** propagate the images of `0` and `m`; until they meet,
  they are the lower and upper one-sided Skorokhod reflections.  Once they
  meet, monotonicity keeps the image a singleton.
- **First-passage route:** decompose the range growth into exits from
  intervals of widths `0,...,m-1`; solve
  `f_i=(z/2)(f_{i-1}+f_{i+1})`, `f_0=f_{r+2}=1`, by Chebyshev polynomials.

**Exact probe.**  `code/stochastic_clipped_span.py` compares every literal
finite-map composition with the span formula for `1<=m<=8`, `n<=12`;
independently solves the Chebyshev difference equations through stage 11;
and matches the PGF coefficients to a first-hit DP for `1<=m<=7` through
time 28.  Result: **226,603 exact assertions, PASS**.

**Owner and collision gate.**

- Weiss--DiMarzio--Gaylord directly study first-passage densities for random
  walk spans ([DOI 10.1007/BF01127728](https://doi.org/10.1007/BF01127728)).
- Palleschi--Torquati explicitly revisit the mean first-passage time for a
  random-walk span ([DOI 10.1103/PhysRevA.40.4685](https://doi.org/10.1103/PhysRevA.40.4685)).
- P93 already owns a reflected-walk cocycle normal form, ballot/first-passage
  analysis, and synchronization language.  P101 already owns exact
  synchronization of monotone interval compositions.

**Kill condition.**  Do not select unless a direct reading establishes that
the clipped-composition normal form plus the finite product PGF is not
already explicit and the batch accepts a second reflection/synchronization
engine.  Current decision: high-quality **RESERVE**, external HOLD.

### S3. Random adjacent-comparator / 0-Hecke sorting walk — **KILL**

**Phase space and update.**  On `S_m`, choose `i` uniformly from
`{1,...,m-1}` and swap entries in positions `i,i+1` only when they are in
decreasing order.  The identity is absorbing.

**Two early exact signals.**

1. Every active update lowers the inversion number by exactly one, so the
   transition matrix is triangular in weak-order/inversion order.
2. Its diagonal entry at `pi` is
   `1-des(pi)/(m-1)`.  Therefore the characteristic polynomial is

   ```text
   product_{d=0}^{m-1}
     [lambda-(1-d/(m-1))]^(EulerianNumber(m,d)).
   ```

**Possible theorem package.**  Besides the exact characteristic polynomial,
the absorption PGF has the acyclic recursion

```text
G_id(z)=1,
G_pi(z)= z * sum_{i in Des(pi)} G_{c_i pi}(z)
          / [m-1-z(m-1-des(pi))].
```

The matching expectation recursion is
`E_pi=[m-1+sum_{i in Des(pi)}E_{c_i pi}]/des(pi)`.  The endpoint `m=1` is
absorbed at time zero.

**Independent routes.**  Build the rational transition matrix and read its
triangular diagonal; separately recurse on weak-order covers and compare
PGF coefficients with path enumeration.

**Owner/collision.**  Random walks on `R`-trivial/0-Hecke-related monoids
already have explicit spectral theory in Ayyer--Schilling--Steinberg--Thiery
([DOI 10.1142/S0218196715400081](https://doi.org/10.1142/S0218196715400081)).
The equivalent continuous-time oriented swap process is a direct mature
owner ([DOI 10.1214/09-AOP456](https://doi.org/10.1214/09-AOP456)).

**Kill condition and decision.**  The parameter-level absorption law did not
collapse beyond a state recursion, while both the semigroup spectrum and
sorting process are directly owned.  `KILL_DIRECT_OWNER_NO_SECOND_CLOSED_LAW`.

### S4. Symmetric endpoint-switching linear PDMP — **KILL / prior reserve**

**Phase space and update.**  On `[0,1] x {0,1}`, let the mode `sigma_t`
flip `0<->1` at rate `lambda>0`, and between flips solve

```text
dX_t/dt = sigma_t-X_t.
```

**Two early exact signals.**

1. The pathwise affine normal form is
   `X_t=e^{-t}X_0+integral_0^t e^{-(t-s)}sigma_s ds`.
2. The stationary marginal is `Beta(lambda,lambda)`, with joint densities
   `rho_0(x)=(1-x)rho(x)` and `rho_1(x)=x rho(x)`.  In stationarity,

   ```text
   Cov(X_t,X_0)
     = [e^(-2lambda t)-2lambda e^(-t)]
       / [4(2lambda+1)(1-2lambda)]       if lambda != 1/2,

     = (1+t)e^(-t)/8                    if lambda = 1/2.
   ```

**Possible theorem package.**  Pathwise normal form, invariant law,
all polynomial moments from a triangular generator, the displayed exact
temporal covariance, and the nonergodic `lambda=0` endpoint.

**Independent routes.**  Solve the two stationary transport equations and
zero-flux identity; separately close the generator on `(X-1/2,
sigma-1/2)` and solve its `2 x 2` moment semigroup.

**Owner/collision.**  Stationary laws for PDMPs are direct background
([DOI 10.1017/S0021900200038420](https://doi.org/10.1017/S0021900200038420));
exact dichotomous-Markov-noise dynamics are directly surveyed in
[DOI 10.1142/S0217979206034881](https://doi.org/10.1142/S0217979206034881).
The P102--P106 kill ledger had already retained this endpoint-switching PDMP
only as an owner-risk reserve.

**Kill condition and decision.**  It repeats a prior reserve and its two
best formulas lie squarely inside the direct owner family.
`KILL_REPEAT_LEDGER_DIRECT_OWNER`.

### S5. Random nilpotent/unit filter on a truncated polynomial ring — **KILL**

**Phase space and update.**  Let `R=F_Q[u]/(u^m)`.  At each time multiply by
`u` with probability `p`, or by the unit `1+u` with probability `1-p`.

**Two early exact signals.**

1. The maps commute and the product is
   `u^J_n(1+u)^(n-J_n)`.  Thus image dimension is `(m-J_n)_+` and kernel
   dimension is `min(m,J_n)`.
2. The zero-map time is the `m`th success time,

   ```text
   P(T_m=t)=binom(t-1,m-1)p^m(1-p)^(t-m),
   E[z^T_m]=(pz/[1-(1-p)z])^m,
   E T_m=m/p,  Var(T_m)=m(1-p)/p^2.
   ```

   At `p=0`, `T_m=infinity`; at `p=1`, `T_m=m`.

**Possible theorem package / routes.**  One can state the exact image and
fibre sizes for every word and the negative-binomial absorption law.  Literal
companion matrices give one check; ideal valuation plus binomial counting
gives the other.

**Owner/collision.**  P98 already occupies repeated-root finite-field
nilpotence and exact torsion depths.  Classical autonomous finite linear
networks are owned by Elspas
([DOI 10.1109/TCT.1959.1086506](https://doi.org/10.1109/TCT.1959.1086506)).

**Kill condition and decision.**  This is precisely the thin random
information-loss/rank lane excluded at intake, and the only temporal law is
negative binomial.  `KILL_THIN_P98_COLLISION`.

### S6. Random inverse powers of one finite-field unipotent block — **KILL**

**Phase space and update.**  On `F_p^d`, let `U=I+N` with `N` one regular
nilpotent block.  Choose `U` or `U^{-1}` with probabilities `alpha` and
`1-alpha`.

**Two early exact signals.**

1. Every word is `U^S_n`.  The order is
   `h=p^ceil(log_p d)`, so `S_n mod h` has an exact finite Fourier law with
   eigenvalues
   `alpha exp(2pi i ell/h)+(1-alpha)exp(-2pi i ell/h)`.
2. For `k` not divisible by `h`,

   ```text
   dim Fix(U^k) = min(d,p^v_p(k));
   ```

   divisibility by `h` gives the full `d`-dimensional fixed space.  This
   yields an exact annealed fixed-count sum over residues.

**Possible theorem package / routes.**  State the word normal form, fixed
dimension staircase, Fourier fixed-count law, periodicity at `alpha=1/2`
when relevant, and deterministic endpoints.  Compare literal Jordan powers
and ranks against Lucas/Frobenius valuation algebra plus cyclic Fourier
inversion.

**Owner/collision.**  This is a random walk on a cyclic subgroup generated by
one unipotent matrix, directly adjacent to Diaconis--Hough
([DOI 10.24033/asens.2466](https://doi.org/10.24033/asens.2466)) and an
obvious randomization of P99's unipotent-shear temporal staircase.

**Kill condition and decision.**  `KILL_P99_RANDOMIZATION`; the fixed-space
formula is not enough to overcome the single-generator random-walk reduction.

### S7. Random integer-degree circle cocycle — **KILL**

**Phase space and update.**  On `R/Z`, choose `f_a(x)=ax mod 1` or
`f_b(x)=bx mod 1`, for fixed integers `a,b>=2` and Bernoulli parameter `p`.

**Two early exact signals.**

1. `Phi_n=f_D_n` with `D_n=a^J_n b^(n-J_n)`, and
   `#Fix(Phi_n)=D_n-1`.
2. The quenched fixed-point exponent is
   `p log a+(1-p)log b`, while
   `E[#Fix(Phi_n)]=(pa+(1-p)b)^n-1`; Jensen gives the strict interior gap.
   The centered quenched exponent has the elementary binomial CLT.  The
   endpoints are the two deterministic degree maps.

**Possible theorem package / routes.**  Composition and fixed points can be
checked by lifts of circle maps; the independent route is binomial
enumeration of degrees and literal rational grids.

**Owner/collision.**  Random distance-expanding maps already have a full
thermodynamic framework
([Springer DOI 10.1007/978-3-642-23650-1](https://doi.org/10.1007/978-3-642-23650-1)).
Internally, P96 owns integer circle expansion and P104 already uses the same
binomial quenched/annealed mechanism.

**Kill condition and decision.**  `KILL_TEXTBOOK_NORMAL_FORM_P96_P104`.

### S8. Three-generator `UT_4` scattered-subword cocycle — **RESERVE behind S1**

**Phase space and update.**  In positive `UT_4(Z)`, choose
`X_i=I+E_{i,i+1}`, `i=1,2,3`, with positive probabilities `p_i`, and use
chronological left products.

**Two early exact signals.**

1. The first superdiagonal records letter counts; `E_13` and `E_24` record
   scattered subwords `21` and `32`; the `E_14` coordinate records the exact
   number `C_321` of scattered subwords `321`.
2. Almost surely

   ```text
   C_321/n^3 -> p_1 p_2 p_3/6,
   log ||M_n||/log n -> 3.
   ```

   Moreover `max C_321=max_{a+b+c=n}abc`, attained by the ordered word, so
   the positive `n^3`-scale pressure is `theta/27` and the nonpositive
   pressure is zero.

**Possible theorem package.**  Exact six-coordinate normal form; strong law;
an `n^(5/2)` CLT whose variance is the explicit first-projection integral

```text
integral_0^1 Var(
  1_{A=3} p_1p_2(1-x)^2/2
 +1_{A=2} p_1p_3 x(1-x)
 +1_{A=1} p_2p_3 x^2/2) dx;
```

polynomial norm exponent; and the sharp pressure kink.  Literal `4 x 4`
multiplication and an independent scattered-subword DP are the two routes.

**Owner/collision.**  General unitriangular random walks are occupied by
Diaconis--Hough, while iid word-pattern/subsequence limit theory is mature
(the Işlak--Özdemir DOI above is a nearby entry point).  More importantly,
S8 is the same algebraic/probabilistic ladder as S1.

**Kill condition and decision.**  Keep only as a fallback if S1 is killed by
owner search.  Never place S1 and S8 in the same five-paper batch.
`RESERVE_SAME_ENGINE`.

### S9. Random affine digit-collapse automaton — **KILL at intake**

**Phase space and update.**  On `Z/2^m Z`, choose
`f_b(x)=2x+b mod 2^m`, `b in {0,1}`.

**Two early exact signals.**

1. `Phi_n(x)=2^n x+B_n mod 2^m`; its image and fibre sizes are
   `2^(m-n)_+` and `2^min(m,n)`.
2. Synchronization occurs deterministically at time `m`; for fair bits the
   final constant is uniform on the phase space.

**Possible theorem package / routes.**  The congruence normal form and a
literal full-map enumeration agree immediately; Bernoulli digit counting is
the second route.  Biased-bit endpoints merely make the final digit word
deterministic.

**Owner/collision.**  General iterated random functions are classical
([Diaconis--Freedman DOI 10.1137/S0036144598338446](https://doi.org/10.1137/S0036144598338446)),
and the system is exactly the projection/overwrite lane excluded after P101.

**Kill condition and decision.**  `KILL_EXCLUDED_OVERWRITE`; deterministic
absorption time is not a paper-level anomaly.

### S10. Free-product cancellation-length cocycle — **KILL**

**Phase space and update.**  Let
`G=Z_2 * ... * Z_2` have `r>=2` factors.  Left-multiply a reduced word by a
uniformly chosen involutory generator and freely reduce.

**Two early exact signals.**

1. The entire reduced word is a canonical finite-time normal form.
2. Its length is a reflected birth--death chain: from positive length it
   decreases with probability `1/r` and increases with probability
   `(r-1)/r`; from zero it increases.  Ballot/reflection formulas give every
   finite-time length probability and speed `(r-2)/r` for `r>2`, with the
   `r=2` square-root boundary.

**Possible theorem package / routes.**  One could record the reduced-word
law, exact length transition kernel, return probabilities, speed, and the
critical folded limit.  Literal free reduction and the independent
birth--death transfer matrix are the two checks.

**Owner/collision.**  Random walks on free products are directly classical
([DOI 10.5802/aif.1261](https://doi.org/10.5802/aif.1261)).  Internally this
is P93's reflected push--pop proof engine with a group label substituted.

**Kill condition and decision.**  `KILL_P93_REFLECTION_REPACKAGE`.

## Ranked theorem contracts

### Rank 1: S1 — recommend one slot, subject to source gate

The non-negotiable short-paper contract is:

1. chronological-product convention and exact `UT_3` normal form;
2. conditional Gaussian-binomial law and full biased finite-time PGF;
3. exact mean and variance for general `p`;
4. strong law and explicit `n^(3/2)` CLT by the displayed decomposition;
5. polynomial norm exponent `2` in the interior versus `1` at endpoints;
6. sharp `n^2` area-pressure kink;
7. explicit P70/P99/P104 firewalls and full owner subtraction;
8. external release HOLD, with no absolute novelty or priority language.

The finite-time distribution and CLT cannot be presented as original; the
residual claim is the exact dynamical package tying them to the central
coordinate, polynomial norm growth, endpoint jump, and pressure kink.

### Rank 2: S2 — proof-complete reserve, not a current slot

The mathematical contract is already exact: image/span normal form,
factorized Chebyshev PGF, and closed first two moments.  It should move from
RESERVE to GO only if direct reading of Weiss--DiMarzio--Gaylord leaves the
factorization or cocycle normal form genuinely unowned and the batch is
willing to accept the P93/P101 proximity.  At present those conditions are
not met.

## Exact probes and reproduction

```bash
python docs/papers107_111_sequence/scouting/code/stochastic_heisenberg_area.py
python docs/papers107_111_sequence/scouting/code/stochastic_clipped_span.py
```

Observed clean outputs:

```text
stochastic Heisenberg-area spike: PASS
exact assertions: 72,361
exhaustive matrix/q-binomial horizon: n <= 15
moment lanes: p = 1/5, 1/2, 3/4
max-area pressure sentinel: max C_n=floor(n^2/4), zero-area paths=n+1

stochastic clipped-span spike: PASS
exact assertions: 226,603
literal cocycle lane: 1 <= m <= 8, n <= 12
PGF/first-hit lane: 1 <= m <= 7, coefficients through n=28
stage lane: Chebyshev difference equations for 0 <= r <= 11
```

Both programs are finite falsification controls.  They do not replace the
strong law, triangular-array CLT, strong-Markov independence argument, or
the specialist source audit.

## Final branch recommendation

- **Advance S1 only** to theorem-contract drafting if the batch needs a
  stochastic/random-matrix paper.  Keep external status HOLD.
- **Keep S2 and S8 in reserve**, in that order for mathematical closure but
  with S8 preferred only if diversity relative to P93/P101 dominates and S1
  is abandoned.
- **Kill S3--S7, S9, and S10** under the reasons recorded above.
- Do not infer novelty from the bounded search.  The next source step for S1
  is a direct full-text search for the exact positive-generator Heisenberg
  walk and its central-coordinate pressure, followed by owner subtraction
  against the three sources already identified.
