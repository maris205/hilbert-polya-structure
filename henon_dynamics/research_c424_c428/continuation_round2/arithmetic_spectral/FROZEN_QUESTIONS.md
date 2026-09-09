# Second-round arithmetic return/spectral questions

2026-09-08 UTC. Two AI-generated full questions, frozen before mathematical
implementation. Neither is an admitted contract. This lane is the only
writer of this directory; old files, shared state, Git, TeX and evaluations
are outside its write scope. No mathematical program is planned merely to
produce a finite table.

## AS2-G: maximal-order closed-geodesic trace, with the physical length clock

**Object and full family.** For every integer $N\geq1$, let
$\Gamma_N=\Gamma_0(N)/\{\pm I\}$ and
$X_N=\Gamma_N\backslash\mathrm{PSL}_2(\mathbb R)$. The native flow is
right multiplication by
$a_t=\operatorname{diag}(e^{t/2},e^{-t/2})$ on all of $X_N$; $t$ is
unit-speed hyperbolic length, not symbolic word length or $\log p$.
Cusps and all geodesics belong to the source; only hyperbolic primitive
closed flow orbits contribute to the following locally finite observable.
The two orientations are not identified by hand.

For a primitive hyperbolic conjugacy class represented by
$A=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$ in
$\Gamma_0(N)$, set
$$
K_A=\mathbb Q[A],\qquad
\mathcal O_A=K_A\cap M_2(\mathbb Z),\qquad
f_A=[\mathcal O_{K_A}:\mathcal O_A],
$$
where $\mathcal O_{K_A}$ is the maximal order in the real quadratic
field. The intrinsic selected condition is **$f_A=1$**. It is not the
stronger condition that $\operatorname{tr}(A)^2-4$ be fundamental.
The latter is the discriminant of $\mathbb Z[A]$, which may be strictly
smaller than the multiplier order. The positive length is
$\ell_A=2\operatorname{arcosh}(|\operatorname{tr}A|/2)$.

**Observable and trace ownership.** Use the exact primitive-orbit product
and its distributional logarithmic derivative:
$$
\zeta^{\rm max}_N(s)=
\prod_{[A]\ {\rm primitive},\ f_A=1}(1-e^{-s\ell_A})^{-1},
\qquad
\Theta^{\rm max}_N=\sum_{[A]\ {\rm primitive},\ f_A=1}
\ell_A\sum_{m\geq1}\delta_{m\ell_A}.
$$
Initially the product is in $\Re s>1$, by domination by the full
geodesic product. The distribution acts on $C_c^\infty((0,\infty))$.
Every repeat uses the same primitive owner and its unchanged physical
length. No ordinary Hilbert-space trace or Fredholm operator is supplied
by this definition; obtaining a source-defined operator realization is
a proof obligation, not an inference from the scalar product.

**Complete question.** Determine the meromorphic-continuation domain and
singularity/branch behavior of this entire $N$-family, in particular
whether it has single-valued meromorphic continuation to $\mathbb C$.
An operator solution must construct its domain and trace from this flow
and the multiplier-order condition, and prove its trace is exactly
$\Theta_N^{\rm max}$ with all repetitions. A negative solution must
prove an actual analytic boundary, not merely failure of one proposed
operator. A finite congruence approximation, asymptotic density, or
unfiltered Selberg determinant does not close the question.

**Arithmetic carrier and closest sources.** Multiplier rings, quadratic
field discriminants and conductor valuations arise from the actual
return matrices. Maucourant, *Size of discriminants of periodic geodesics
on the modular surface*, JTNB 37 (2025), 795–835,
[DOI/source](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1343.pdf),
owns the multiplier-order formulation and its matrix-norm distribution
theory. Bourgain–Kontorovich, *Beyond expansion II: low-lying fundamental
geodesics*, JEMS 19 (2017), 1331–1359,
[source](https://ems.press/content/serial-article-files/32202), owns the
fundamental-geodesic sieve existence mechanism. Their complete relevant
statements and possible closer sources must be checked before any
increment claim. C420 concerns cusp scattering, not this periodic trace;
O29, O33 and O119 remain relevant boundaries but do not answer this
infinite arithmetic selector question.

**Cheap decisive tests, before a census.** Check that the maximal-order
condition is conjugacy- and repetition-invariant. Test whether any fixed
finite congruence quotient can detect it already at $N=1$. Distinguish
matrix-norm sampling from primitive-orbit length sampling. Try the full
conductor sieve on the logarithmic derivative and identify exactly the
uniform estimate needed to pass from finite local data to continuation.
If only a finite-quotient obstruction survives, retain it as auxiliary;
do not shrink the original question or award a paper slot.

## AS2-B: all-input native quadratic return problem for Browkin I

**Object and parameters.** For every odd rational prime $p$, use the
unique balanced $p$-adic digits
$\mathcal D_p=\{-(p-1)/2,\ldots,(p-1)/2\}$. For
$x=\sum_{j=k}^{\infty}c_jp^j\in\mathbb Q_p$, put
$$
s_p(x)=\sum_{j=k}^{0}c_jp^j
\quad\text{(empty sum $0$)},\qquad
T_p(x)=\frac1{x-s_p(x)}.
$$
The input family is every embedded quadratic irrational
$x\in\mathbb Q_p$ with $[\mathbb Q(x):\mathbb Q]=2$, including both
real and imaginary quadratic fields whenever they embed. Every complete
quotient remains quadratic irrational, so no termination denominator
vanishes. The domain is this whole forward-invariant set, without
passing to a conjugate, a different prime, or an altered floor rule.
For rational inputs the known terminating algorithm is only a boundary
control, not a proposed new classification.

**Native clock and observable.** One application of $T_p$ is one tick;
$a_n=s_p(T_p^n x)$ is the actual partial quotient. For each input, the
observable is eventual periodicity of the actual complete-quotient
orbit, with its exact least preperiod and least period when finite.
No height truncation or equality of approximate digits counts as a
return. An ordinary all-input fixed-point trace/zeta is not assumed;
its finiteness is a separate cheap check. No alternate length/valuation
clock is used to repair a failed trace.

**Complete question.** Give a terminating necessary-and-sufficient
criterion for eventual periodicity for all of these inputs and primes,
recovering the actual least preperiod and period. In particular, settle
whether every quadratic input is eventually periodic; if not, a proposed
classification must specify and prove its negative cases, not mark a
long unrepeated prefix as nonperiodic. The full signed algorithm and
both kinds of quadratic fields remain in the quantifiers.

**Arithmetic carrier and sources.** The quadratic field, its chosen
$p$-adic embedding, balanced floor and complete-quotient arithmetic are
intrinsic. The mechanism is different from rational genus-one torsion
and from a finite-state trace. Browkin introduced the algorithm.
Capuano–Murru–Terracini,
[*On periodicity of p-adic Browkin continued fractions*](https://arxiv.org/abs/2010.07364),
provides quadratic recurrences and partial criteria. Romeo,
[*Real convergence and periodicity of p-adic continued fractions*](https://link.springer.com/article/10.1007/s11139-025-01264-7),
Ramanujan J. 68, 112 (2025), supplies necessary real-convergence results
and explicitly conditional probabilistic arguments. Ruban's effective
criterion is a different algorithm and cannot be transplanted across
the sign change. The 2026 periodic-variety paper must also be checked:
formal $\mathbb Z[1/p]$ periodic representations need not follow the
frozen Browkin digits.

**Cheap decisive tests.** Derive the exact complete-quotient recurrence
with all denominators and valuations retained. Test proposed real-height
descent against signed partial quotients and imaginary quadratic input.
Check the source's bounded-subsequence criterion rather than assuming
every orbit reaches its hypotheses. Check whether any probabilistic
claim for Haar-almost-every $p$-adic point applies to the countable
quadratic locus. No pilot is necessary for a missing uniform argument.

**Replacement boundary.** If only the known boundedness criterion,
prescribed-period constructions, or necessary real convergence survives,
report the exact missing exhaustion argument. Do not rename a different
continued-fraction algorithm as the solution or split one periodic family
into a separate paper.

## Batch and target boundary

The preceding first-pass U-correspondence/support inclusion-exclusion,
ordinary rational-Witt packet and Bost–Connes diagonal calculations are
retired and unchanged. The already admitted AM1 remains the only admitted
contract. These two questions supply neither target Euler factors nor
root numbers, automorphy, a zero/divisor identification or a
Hilbert–Pólya realization. `NO_BAD_EULER_OR_ROOT_NUMBER` is unconditional.
