# Hostile theorem, evidence, and scope audit

## Analytic attack surface

**Mean obstruction.** A periodic logarithmic derivative has zero mean, so a naive
\(u=-2\nu(\log w)_x\) cannot cover \(m\ne0\). Closed: the map is
\(u=m-2\nu(\log w)_x\), and the inverse uses the periodic primitive of \(u-m\).

**False autonomous heat claim.** A Galilean transformation depends on time. Closed:
the autonomous fixed-\(x\) conjugate is drift--heat
\(e^{t(\nu\partial_x^2-m\partial_x)}\); pure heat is stated only in \(y=x-mt\).

**Projective gauge.** Cole--Hopf lifts are not unique. Closed: the state is quotiented
by exactly \(\mathbb R_{>0}\), and the inverse fixes a zero-mean primitive only to
construct a representative.

**Positivity and regularity.** Logarithms require a positive continuous lift. Closed:
the cone assumes \(\min w>0\) in \(H^{s+1}\), \(s>3/2\); periodic heat preserves
strict positivity and smooths instantly.

**Overstated recurrence.** Convergence alone must be connected to a definition.
Closed: recurrence is explicitly a sequence \(t_j\to\infty\) returning in \(H^s\);
the full orbit tends to \(m\), so the returning state must be \(m\).

**Wrong sharp remainder.** The next error can come from either the next Fourier mode
or the quadratic logarithmic term. Closed: the remainder exponent is the minimum of
\(\nu\kappa_{r_2}^2\) and \(2\nu\kappa_r^2\), which is strictly above the leading
exponent.

**Incomplete spectrum.** A list of Fourier values is not a full operator statement.
Closed: the complexified generator, domain \(H^{s+2}\), compact resolvent, fixed-mean
removal of \(k=0\), and real conjugate blocks are all stated.

**Fake physical-time snapshots.** Independent rational heat-decay and translation
phases generally do not lie on the same one-parameter physical curve. Closed: the
certificate calls them evaluations of the universal two-parameter commuting
multiplier. The analytic physical curve
\(\rho=e^{-\nu t},\zeta=e^{-imt}\) is a subcurve; no rational row is labelled as an
actual time sample.

## Executable attack surface

- Producer and checker share no imported implementation.
- Every coefficient list is required to be sorted and mode-unique.
- Evidence binds commit, evaluator SHA, scope literal, source identifiers, theorem
  conventions, route tuple, and summary counts into the semantic hash.
- Repaired-hash mutations test semantics after the attacker recomputes the hash;
  the stale mutation separately tests the hash itself.
- SymPy re-expands selected residuals instead of trusting stored zeros.
- Replay compares canonical bytes, not merely parsed JSON equality.
- Conservative L1 positivity bounds are sufficient regression sentinels, not claimed
  to characterize every positive trigonometric polynomial.

## Ownership and scope attack

Hopf and Cole own the classical transformation line. This package makes no novelty
or priority claim for it. It also does not infer arithmetic meaning from linearity.
Absent claims include any target zero/prime use, arithmetic local data, Euler product
or factor, root number, automorphy, target divisor/functional equation, quantization,
Hilbert--Pólya operator, external review, or acceptance score.

## Verdict

No theorem blocker or executable blocker remains under the frozen phase space,
physical clock, regularity, and scope. Route A still fails at A0--A3; A4 remains only
a formal source-linearization hint. Route B invocation is false. Finite evidence is
regression only and no bug is promoted as mathematical insight.
