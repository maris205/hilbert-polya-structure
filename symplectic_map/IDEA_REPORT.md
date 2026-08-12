# Stage-1 Idea Report

## Decision

The first paper will not pursue a generic "symplectic map for the Riemann zeros."
The selected question is narrower:

> For the frozen quadratic parameter
> \(u_c=1.5436890126920763\), can the parent's weak mod-2 symbolic shadow be
> transported through the matched Hénon family
> \(H_{a,\rho}(x,y)=(1-a x^2-\rho y,x)\) to a regular conservative system, or is
> that inheritance destroyed by the singular endpoint, branch ambiguity, escape, or
> the symplectic dynamics itself?

This is a high-risk diagnostic question. A controlled failure is an acceptable and
potentially publishable outcome. No Riemann-zero table may be used, and no
prime/multiplier correspondence is assumed.

## Problem anchor

The original project chain was

```text
Logistic arithmetic seed -> Hénon bridge -> symplectic geometry -> orbit zeta -> quantization
```

The audit found that its first arrow is not established strongly enough to support the
later arrows. Prior work appears to show at most a mod-2/parity shadow. In particular,
the inherited gap law is broadly geometric and does not establish the mod-3/mod-6
structure expected of rational primes. Some legacy numerical comparisons also used
target-dependent normalizations or were not reproduced by the code audit.

The research program must therefore test inheritance before constructing an
arithmetic zeta function. The Hénon family is useful because

\[
DH_{a,\rho}(x,y)=
\begin{pmatrix}-2ax&-\rho\\1&0\end{pmatrix},
\qquad \det DH_{a,\rho}=\rho.
\]

Thus \(0<\rho<1\) supplies conformally symplectic matched controls and \(\rho=1\)
is area preserving. The endpoint \(\rho=0\) is singular, not an ordinary smooth
member of the same diffeomorphism family.

## Ranked ideas

| Rank | Idea | Novelty | Feasibility | Arithmetic risk | Decision |
|---:|---|---:|---:|---:|---|
| 1 | Regular-lift obstruction plus frozen-\(u_c\) symbolic-shadow survival/failure across \(\rho\) | Medium | High | High | **SELECTED** |
| 2 | Anti-integrable/high-\(a\) Hénon orbit census as completeness and branch-tracking calibration | Low | High | None by itself | **REQUIRED CONTROL** |
| 3 | Unstable-multiplier Euler product and prime-enrichment test | Potentially high | Medium | Extreme | **DEFERRED UNTIL A0 PASSES** |
| 4 | Generic area-preserving Hénon zeta/Fredholm determinant | Low | Medium | High | **REJECTED AS MAIN CLAIM** |
| 5 | Direct quantum-map/Riemann-zero comparison | Unclear | Low | Fatal at present | **STOP-SCOPED** |
| 6 | Higher-dimensional coupled symplectic Hénon map | Low for present question | Low | Adds rather than resolves ambiguity | **ROUND2_CLUE** |

The independent external review ranked the packages in the same order:

```text
obstruction + rho-survival experiment
    > anti-integrable positive control
    >> multiplier-to-prime Euler product
```

## Idea 1: Critical-lift boundary and arithmetic-shadow survival

### Core construction

Use the matched family

\[
H_{a,\rho}(x,y)=(1-a x^2-\rho y,x),\qquad 0\leq\rho\leq1,
\]

with the primary parameter frozen at \(a=u_c\) before orbit multipliers or prime
labels are inspected. Use neighboring \(a\)-values as robustness controls. Treat the
legacy \(a=1.02\) choice only as a tainted historical negative control because it was
associated with earlier zero-oriented heuristics.

### Exact theoretical component

If a \(C^1\) submersion \(\pi\) and a local diffeomorphism \(F\) obey
\(\pi\circ F=f\circ\pi\), then

\[
D\pi_{F(z)}DF_z=Df_{\pi(z)}D\pi_z.
\]

At a critical point of the one-dimensional \(f\), the two sides have incompatible
ranks. Hence the critical quadratic map cannot be a smooth-submersion factor of a
planar symplectomorphism across its critical fiber. This is an elementary and known
boundary, not the novelty claim.

The Hénon memory coordinate avoids the contradiction because its first component is
not \(f(x)\) alone. It consequently gives up exact semiconjugacy. Whether any
arithmetic shadow survives is therefore an empirical question.

### Primary falsifiable observable

The only currently justified parent feature is parity. Before confirmatory data are
opened, freeze a symbol partition and use the left-return parity polarity

\[
P(\rho)=
\frac{N_{\mathrm{even}}(\rho)-N_{\mathrm{odd}}(\rho)}
     {N_{\mathrm{even}}(\rho)+N_{\mathrm{odd}}(\rho)}.
\]

This statistic is defined without primes, composites, or target zeros. Trajectory
exposure/survival is an eligibility condition rather than a second success metric, so
an apparently small violation rate among a tiny survivor set cannot count as
transport.

### Why it might work

- The parameter is frozen independently of the symplectic multiplier data.
- The family separates a singular one-dimensional parent from regular
  conformally-symplectic and symplectic maps with one parameter.
- A predeclared parity statistic tests exactly the limited structure the parent is
  believed to possess; it does not silently upgrade that evidence to "prime coding."
- A negative result can identify whether loss occurs through branch failure, escape,
  or symbolic-grammar change.

### Why it may fail

- \(\rho=0\) is singular, so "the same orbit" may have no unique continuation.
- The frozen parameter lies outside a simple uniformly hyperbolic regime; orbit
  completeness may not be certifiable.
- Survivor conditioning can mimic symbolic persistence unless exposure is gated.
- The upstream parity claim itself may be a weak finite-sample artifact.
- Neighboring parameters or shuffled/Markov controls may reproduce the same signal.

### Falsification outcomes

- `A0_FAIL`: the parity statistic does not survive at regular \(\rho>0\) or at
  \(\rho=1\).
- `NOT_TESTABLE_AS_TRANSPORT`: exposure collapses or branch identity is not defined.
- `PROVES_TOO_MUCH`: matched controls show the same response.
- `A0_WEAK_ARITHMETIC_RELATION`: parity survives robustly, but no structure beyond
  mod 2 is established.

Even the most favorable listed outcome is not yet a rational-prime correspondence.

## Idea 2: Anti-integrable orbit census as a positive control

At a high-\(a\) value in the full-horseshoe/anti-integrable regime, binary symbolic
words provide controlled initial guesses and exact primitive-necklace counts provide
a completeness benchmark. The control should check:

- one representative per cyclic class;
- minimal period versus repeated words;
- residual and high-precision validation;
- determinant identity \(\det M_\gamma=\rho^n\);
- expected primitive binary-necklace counts through the declared cutoff;
- branch-tracking and deduplication failure modes.

Passing this control validates the software and missed-orbit accounting. It does not
imply that the mixed frozen-\(u_c\) regime is complete, and it gives no arithmetic
evidence.

The implemented control now passes through period 10: the exact primitive-necklace
counts \(2,1,2,3,6,9,18,30,56,99\) were recovered with maximum float cyclic
residual \(1.42\times10^{-13}\). This is numerical certification of the declared
calibration regime only. The \(u_c\) ledgers remain explicitly incomplete.

## Idea 3: Unstable multipliers as an arithmetic clock

For a frozen primitive hyperbolic ledger, define

\[
\ell_\gamma=\log|\Lambda_{u,\gamma}|,
\qquad
Z_u(s)=\prod_\gamma(1-|\Lambda_{u,\gamma}|^{-s})^{-1}.
\]

Where termwise differentiation is justified,

\[
-\frac{Z_u'(s)}{Z_u(s)}
=\sum_\gamma\sum_{r\geq1}
\ell_\gamma|\Lambda_{u,\gamma}|^{-rs}.
\]

This resembles the rational-prime logarithmic derivative only if the primitive
multipliers arise intrinsically as primes, with correct multiplicity. Symplecticity
does not imply that condition. A single low-period multiplier near an integer or prime
is post-hoc evidence and must be rejected.

Indeed, an exact parameter-tuned coincidence is available algebraically. For a
symplectic fixed point, set \(t=\lambda+\lambda^{-1}\). Combining its fixed-point and
trace equations gives

\[
a=\frac{t^2}{4}-t.
\]

Choosing \(\lambda=5\) gives \(t=26/5\) and exactly \(a=1.56\), one of the neighbor
controls. This is a useful demonstration that an exact prime multiplier obtained by
parameter selection carries no intrinsic arithmetic evidence.

This idea is deferred because:

- the orbit ledger at \(u_c\) may be incomplete;
- generic Hénon zeta machinery is prior art;
- an orbit-to-prime assignment has not been defined without labels;
- the external review judged this package to require rethinking;
- any result based on reordering, fitting, phase adjustment, or target normalization
  would fail the Route-A gate.

The provisional Euler product must also remain distinct from the semiclassical
stability factor

\[
|\det(M_\gamma^r-I)|^{-1/2}
=\frac{|\Lambda|^{-r/2}}{|1-\Lambda^{-r}|},
\]

which is not exactly \(|\Lambda|^{-r/2}\).

## Eliminated directions

### Generic Hénon ledger/zeta

Existing work already supplies sophisticated symbolic orbit ledgers, monodromy data,
cycle expansions, and spectral determinants for area-preserving Hénon maps. Repeating
that machinery can calibrate the implementation but cannot be the paper's novelty.

### Cat-map rescue

Cat maps are useful exact symplectic and quantum controls. They do not supply the
desired prime multipliers: for \(A\in SL(2,\mathbb Z)\), a prime unstable eigenvalue
\(p\) would force the integer trace to equal \(p+p^{-1}\), a contradiction.

### Riemann-zero or GUE comparison

No zero table is permitted during construction. GUE-like statistics, generic spectral
repulsion, or a natural unitary quantization would still not establish arithmetic
origin. These analyses are stop-scoped until A0 and A1 pass independently.

### Higher-dimensional coupling

Dimension, coupling, and additional phase variables cannot repair an undefined
one-dimensional inheritance mechanism. They are postponed until the two-dimensional
test yields a specific structural clue.

## Selected-paper claim in one sentence

The Stage-1 paper will determine, under a frozen parameter, explicit censoring rules,
and validated orbit-finding controls, whether a weak parity-coded quadratic shadow can
survive the singular passage into a regular symplectic Hénon map; it will not claim a
prime correspondence unless a later, independently gated experiment supplies one.

## Immediate deliverables

1. Exact geometry and proof packages with corrected scope.
2. A high-\(a\) orbit-finder calibration through a certifiable low-period cutoff.
3. A development/validation/confirmatory symbolic-transport experiment.
4. A branch-identity and completeness uncertainty report at \(u_c\).
5. A Route-A decision that stops before zeta construction when A0 fails or is not
   testable.
