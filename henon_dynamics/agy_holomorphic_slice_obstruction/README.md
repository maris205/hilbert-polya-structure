# HCS-C26: scalar AGY determinants survive, oscillator twists do not

HCS-C26 closes the holomorphic/no-localizer escape left open by HCS-C25 and,
at the same time, extracts a positive scalar dynamical zeta structure.

The result uses the same source-faithful countable AGY return system and the
same chronological symplectic cocycle as C25.  No transition matrices are
averaged, no oscillator modes are truncated, and no heat factor is inserted.

## Main result

Every AGY return matrix factors as

\[
B_\gamma^T=P C_\gamma,
\qquad
P=B_{\gamma_*}^T>0,
\qquad C_\gamma\ge0.
\]

The nonnegative factor preserves a canonical complex positive cone, while
the fixed strictly positive factor sends its closure into the interior.
This gives one bounded domain `Omega` in `C^3` with

\[
h_\gamma(\Omega)\Subset\Omega
\quad\text{uniformly for every return branch.}
\]

For every `Re(s)>-sigma_0`, the scalar weights

\[
w_{s,\gamma}(z)
=\bigl(\mathbf1^TB_\gamma^Tz\bigr)^{-(s+4)}
\]

use one principal logarithm and have summable sup norms on `Omega`.
Consequently the scalar operator on `A^2(Omega)` belongs to an exponential
singular-value class and is trace class.

For a chronological word with raw integer matrix

\[
A_w=A_{\gamma_n}\cdots A_{\gamma_1}\in SL(4,\mathbb Z),
\]

Perron root `lambda_w`, and characteristic polynomial `chi_w`, its scalar
fixed-point trace atom is exactly

\[
\boxed{
\operatorname{tr}T_w
=\frac{\lambda_w^{-(s+1)}}{\chi_w'(\lambda_w)}.
}
\]

The dimension cancellation is exact: the weight exponent `s+4` combines
with the three-dimensional projective fixed-point denominator to leave
`s+1`.  Since `A_w` is integral with determinant one, `lambda_w` is an
algebraic unit.  This is genuine chronological arithmetic structure, but it
is not a prime law or an RH match.

## Same-domain obstruction

Let `F=L^2(R^2)` and let `U_gamma` be the pathwise metaplectic unitary.
The vector-valued Bergman series

\[
(\mathcal L_s^{\rm Mp}F)(z)
=\sum_\gamma
w_{s,\gamma}(z)U_\gamma F(h_\gamma z)
\]

converges absolutely in operator norm on `A^2(Omega;F)`.  Constants and
evaluation at a real interior point give the exact slice

\[
E_{x_0}\mathcal L_s^{\rm Mp}J
=\sum_\gamma w_{s,\gamma}(x_0)U_\gamma.
\]

C25 proves that the projected symplectic atoms are pairwise distinct, and
C24 proves that such an `ell^1` metaplectic atom sum has essential norm at
least its coefficient `ell^2` norm.  Therefore

\[
\boxed{
\|\mathcal L_s^{\rm Mp}\|_{\rm ess}
\ge
\frac{
\left(\sum_\gamma|w_{s,\gamma}(x_0)|^2\right)^{1/2}}
{\|E_{x_0}\|\,\|J\|}>0.
}
\]

Thus, on the same complex domain,

| Fibre | Operator status | Ordinary determinant |
|---|---|---|
| scalar | exponential class, trace class | exists |
| unsmoothed infinite oscillator | bounded, noncompact | not available in trace/nuclear Fredholm theory |

The proof needs no branch-supported holomorphic localizer.  More generally,
it closes every bounded literal realization on a point-evaluative
holomorphic function space that contains constants.  It does not claim to
close a non-tensor anisotropic distribution space with no bounded point or
fibre slice, nor a separately defined flat/distributional trace.

## Exact witness

The source branch is

```text
state:   (1342)/(4321)
gamma*:  t^64 (tbttbtbb)^8
length:  128
```

Its exact chronological matrix is

\[
B_{\gamma_*}=
\begin{pmatrix}
18540&1210580&11430&27373\\
24020&1568410&14783&35450\\
50233&3279928&31130&74253\\
38803&2533625&24020&57343
\end{pmatrix}.
\]

At the independently reconstructed point

\[
x_0=
\frac{(131596,8592543,81363,194419)}{8999921},
\]

the projective normalizer is

\[
S_*(x_0)=\frac{15076979616018}{8999921}.
\]

One branch alone gives

\[
\|\mathcal L_s^{\rm Mp}\|_{\rm ess}
\ge
\frac{S_*(x_0)^{-(\operatorname{Re}s+4)}}
{\|E_{x_0}\|\,\|J\|}.
\]

The released certificate also records the positive-prefix coordinate margin,
a Birkhoff contraction sentinel, three Perron-trace identities, and a
three-return noncyclic reversal with different reciprocal characteristic
polynomial.  Its two-return AB/BA pair verifies inverse-order bookkeeping at
matrix level only, since cyclic invariance forces the same characteristic
polynomial.  These finite computations verify conventions; the
complex-domain, trace, decoder, and essential-norm conclusions are theorems.

## Route-A verdict and pivot

The target oscillator candidate remains

\[
(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}),
\qquad
\mathrm{ROUTE\_A\_REJECTED}.
\]

The next large door changes the fibre:

\[
g_\gamma\bmod p\in\operatorname{Sp}(4,\mathbb F_p),
\qquad
\rho_p(g_\gamma)\in U(p^2),
\]

for odd primes `p`.  Finite Weil fibres preserve the true chronology, have
ordinary finite characters and arithmetic Gauss sums, and do not inherit the
infinite-multiplicity obstruction.  They are a new model, not a limit claim
for the nonexistent ordinary oscillator trace.

## Reproduce

```bash
cd henon_dynamics/agy_holomorphic_slice_obstruction
./code/run_c26.sh
```

The runner rebuilds the exact certificate, runs an implementation-independent
checker, executes mutation tests, and refreshes the artifact hash manifest.

## Project map

- [`RESEARCH_QUESTION.md`](RESEARCH_QUESTION.md) -- frozen question and scope;
- [`METHODOLOGY_BLUEPRINT.md`](METHODOLOGY_BLUEPRINT.md) -- proof and
  experiment design;
- [`THEOREM_PACKAGE.md`](THEOREM_PACKAGE.md) -- complete statements and
  proofs;
- [`SOURCE_AUDIT.md`](SOURCE_AUDIT.md) -- primary-source and duplication
  audit;
- [`PAPER_PLAN.md`](PAPER_PLAN.md) -- claims-first article plan;
- [`REPOSITORY_UPDATE.md`](REPOSITORY_UPDATE.md) -- release summary and next
  large gate;
- [`paper/main.pdf`](paper/main.pdf) -- compiled research note;
- [`code/`](code/) -- independent exact implementations and runner;
- [`results/`](results/) -- certificates, tests, validation, and hashes;
- [`route_a_evaluation.yaml`](route_a_evaluation.yaml) -- formal Route-A
  decision;
- [`evaluations/route_a/HCS-C26/20260810T044618Z.yaml`](evaluations/route_a/HCS-C26/20260810T044618Z.yaml)
  -- immutable Route-A evaluation record tied to implementation commit
  `6d8c40eed90fc6bd0cf5349069756c0045fb11bd`.
