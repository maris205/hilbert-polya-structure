# Obstruction registry

## O1 — Critical-factor rank obstruction (PROVED, standard)

If a \(C^1\) submersion \(\pi:M\to N\), a \(C^1\) local diffeomorphism \(F\),
and a \(C^1\) map \(f\) satisfy \(\pi\circ F=f\circ\pi\), no point in the
image of \(\pi\) can be critical for \(f\). This follows immediately by
differentiating and comparing ranks. Hence the critical quadratic map cannot
be a globally smooth submersion factor of a planar symplectomorphism over its
critical fiber. This is a boundary lemma, not a novelty claim.

Artifact: [proof package](../papers/1-symp-vs-diss/notes/PROOF_PACKAGE.md).

## O2 — Smooth lift versus exact projection (PROVED consequence)

The singular cotangent/weak-noise lift preserves the quadratic-map projection
away from \(f'=0\), but becomes singular at the critical fiber. The polynomial
Hénon lift is globally smooth at \(\rho=1\), but its first-coordinate
projection is not semiconjugate to the parent map. Exact projection and a
regular finite-dimensional symplectic lift cannot both be assumed here.

## O3 — Noncompact escape (NUMERICAL_OBSERVATION, frozen ensemble)

In the sealed test at \(a=u_c,\rho=1\), exposure was 0.011724, no trajectory
survived the full horizon, and only 9,988 return gaps were available. These
values fail the preregistered exposure and gap-count gates. A separate
post-validation diagnostic also had 256/256 trajectories escape. The result
is scoped to the frozen parent-derived ensembles; it does not assert that the
entire noncompact phase space has no bounded invariant set. Survivor-conditioned
symbolic statistics would be selection-biased, so the formal decision is
carrier unavailability.

## O4 — Upstream arithmetic specificity (STOP_SCOPED / unsupported)

Repository evidence shows parity rigidity but missing mod-3/mod-6 structure,
kneading defects, and a previously calibrated twin-prime scale. Consequently,
the inherited object is an attributed mod-2 shadow, not a proved rational-prime
mechanism. In validation and sealed test, all four clean neighboring parameters
reproduced polarity above 0.997 at \(\rho=0.1\) and \(0.2\), while all exhibited
approximately one-percent endpoint exposure and zero endpoint survivors. Thus
the tested weak shadow is not specific to \(u_c\); the rational-prime branch
was never opened.

## O5 — Integral cat-map prime multiplier (PROVED negative control)

For a hyperbolic \(A\in SL(2,\mathbb Z)\), an unstable eigenvalue cannot equal
a rational prime \(p\): the reciprocal eigenvalue is \(1/p\), forcing the
integer trace to equal \(p+1/p\notin\mathbb Z\). Cat maps remain useful
geometry/quantization controls but are exact negative controls for direct
rational-prime multipliers.

## O6 — Tunable Hénon fixed-point prime (PROVED proves-too-much control)

For \(H_{a,1}\), the negative fixed point has
\(\operatorname{tr}DH=2+2\sqrt{1+a}\). Requiring its unstable multiplier to
equal any selected \(m>1\) gives

\[
a=\frac{(m-1)^4}{4m^2}-1.
\]

Thus \(a=1.56\) gives multiplier \(5\) exactly, while frozen \(u_c\) gives
\(4.98936\ldots\). A single near-prime multiplier is therefore an explicit
one-parameter coincidence, not an arithmetic signal; only a frozen,
multi-orbit, held-out correspondence could survive this control.

## O7 — Frozen-ledger completeness (NOT_TESTABLE at \(u_c\))

The same implementation exactly recovered primitive binary-necklace counts
through period 10 at the strongly hyperbolic \((a,\rho)=(6,1)\) positive
control, and all found cycles passed an independent 80-digit residual audit.
At \((u_c,1)\), however, the period-1--8 counts
\(2,0,2,2,2,3,4,5\) are explicitly incomplete. The high-\(a\) control
validates the implementation in its declared regime but cannot certify
completeness at \(u_c\). Cycle expansions and dynamical determinants are
therefore stop-scoped for the frozen candidate.

## O8 — Finite-memory locally constant prime-clock obstruction (PROVED)

For a fixed finite directed graph and a finite-memory locally constant scalar
multiplicative cocycle, every periodic instability length lies in the
finite-dimensional rational span of the finitely many local log-multipliers.
Distinct rational-prime logarithms are rationally linearly independent by
unique factorization.  Hence the periodic clock can contain at most the rank
of that span many exact prime logarithms and cannot contain all of them.

For `pcf_markov_baker_v1`, every closed walk has period \(2k\) and
\(|\Lambda_u|=2^k\), so the exact multiplier ledger meets the rational primes
only at \(2\).  This is a termwise exact obstruction for the frozen scalar
clock, not a no-go theorem for point-dependent roofs, countable-state systems,
matrix spectral radii, approximate matching, or growing families.

Artifacts: [proof package](../papers/2-branch-baker/PROOF_PACKAGE.md),
[verified results](../papers/2-branch-baker/results/EXPERIMENT_RESULTS.md).

## O9 — Base-two exponent boundary for the frozen PCF quadratic (PROVED / OPEN tail)

For the frozen PCF quadratic

\[
g(z)=z^2-u,\qquad u^3-2u^2+2u-2=0,
\]

the exact local argument makes every period-\(n\ge2\) point a 2-adic unit.
Consequently a rational period-\(n\) multiplier is \(2^n\) times an odd
integer.  The equality \(\Lambda=\pm2^n\) is proved impossible at periods 2
and 3.  The exact periods 2--7 ledger also contains no target hit, but those
periods were development-seen before the source lock and do not prove the
all-period statement.  The equality question remains open for arbitrary
\(n\ge4\).

Artifacts: [proof package](../papers/7-base2-exponent-clock/notes/PROOF_PACKAGE.md),
[registered ledger](../papers/7-base2-exponent-clock/results/EXPERIMENT_RESULTS.json).

## O10 — Prime-torsion capacity is not a prime clock (PROVED)

Every hyperbolic matrix in \(SL_2(\mathbb Z)\) has a nonzero prime-order
torsion point of every exact period \(n>12\).  For the standard trace-three
cat map such a carrier exists exactly for
\(n\notin\{1,6,12\}\), including the non-semisimple modulo-five repair at
period 10.  This is capacity rather than specificity: periodic points are
exactly torus torsion, every additive order occurs, and
\(x\mapsto\log\operatorname{ord}(x)\) is unbounded and discontinuous in every
neighborhood.  Native linear monodromy depends on the period, not the torsion
order.  Thus the construction proves too much and does not provide a local or
Hölder prime-labelled potential.

Artifacts: [proof package](../papers/8-cat-torsion-capacity/notes/PROOF_PACKAGE.md),
[exact audit](../papers/8-cat-torsion-capacity/results/EXPERIMENT_RESULTS.json).

## O11 — Prime-shell orbit multiplicity (PROVED, scalar scope)

For the standard cat map the nonzero \(p\)-torsion shell has one primitive
orbit only at \(p=2\).  Every odd prime has at least \(p-1\) primitive orbits.
Accordingly an unweighted one-time orbit-label product has local factor
\((1-p^{-s})^{-m_p}\), while a raw-return product retains the orbit periods as
well.  A pure product of nonzero scalar denominator factors cannot reduce its
degree from \(m_p>1\) to one.  Fractional shell weights can force unit total
mass, but that normalization is global, partition-tautological, and works for
composite exact-order shells too.  The theorem does not exclude numerators,
matrix-valued or alternating Fredholm determinants, or a separately justified
equivariant mechanism.

Artifacts: [proof package](../papers/9-cat-prime-shell-multiplicity/notes/PROOF_PACKAGE.md),
[five-shell audit](../papers/9-cat-prime-shell-multiplicity/results/EXPERIMENT_RESULTS.json).

## O12 — Full-centralizer compression kills the native period (PROVED)

Over \(\mathbb Z/q\mathbb Z\), the cyclic-vector locus of the standard cat
matrix is a torsor for the full local centralizer
\(C_q=(\mathbb Z/q\mathbb Z[A])^\times\).  Its coarse \(C_q\)-quotient is one
class, but \(A\in C_q\), so the induced dynamics is the identity and has native
period one.  Restricting to the determinant-one/symplectic centralizer retains
the norm-image strata.  Obtaining a single class therefore uses a
modulus-dependent nonsymplectic pseudo-symmetry family, and the label
\(q^{-s}\) still has to be supplied externally.  The same compression works
for composite moduli, so it is not prime-specific.

Artifacts: [proof package](../papers/10-cat-centralizer-quotient/notes/PROOF_PACKAGE.md),
[nine-modulus audit](../papers/10-cat-centralizer-quotient/results/EXPERIMENT_RESULTS.json).

## O13 — Equivariant retention versus compression (PROVED, family-uniform scope)

For a finite abelian \(C\)-set
\(X=\bigsqcup_K n_K C/K\) with distinguished \(A\in C\), the source period on
\(C/K\) is
\([\langle A\rangle:\langle A\rangle\cap K]\).  Coarse and orbit-counting
reductions collapse the translation; fixed-point Burnside data retain the
subgroup \(\langle A\rangle\), while a labelled effective \(C\times\mathbb Z\)
invariant can recover \(A\) only modulo the action kernel.  Static
inertia/stabilizer data do not restore the clock.  At the locked modulus
\(q=2\), point-cardinality happens to give source support with unit exponent,
but this is the unique row/type exception, is not family-uniform, and its
support collides with \(q=4\).  Hence no single audited reduction supplies an
intrinsic modulus clock across the family.

Artifacts: [proof package](../papers/11-cat-equivariant-clock/notes/PROOF_PACKAGE.md),
[independent scope correction](../papers/11-cat-equivariant-clock/notes/INDEPENDENT_POSTRUN_SCOPE_AUDIT.md),
[exact audit](../papers/11-cat-equivariant-clock/results/EXPERIMENT_RESULTS.json).
