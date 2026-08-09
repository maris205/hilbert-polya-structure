# Next large step: graded projective Hénon Ruelle complex

**Date:** 2026-08-09
**Candidate ID:** HCS-C22G
**Parent/closed form:** HCS-C22 orbitwise geometric scalar T5
**Status:** source-locked changed form; geometric foundation certified; no
graded operator theorem yet

## Decision

The orbitwise geometric scalar T5 route is closed by the
primitive/double-repetition denominator obstruction.  This does not rule out
all aggregate scalar representations, but no scalar-kernel finite spectrum
will be computed for the frozen termwise claim.

The only authorized continuation of this dynamical form is a genuinely
different object: the projectivized unstable Hénon skew product equipped
with an exterior-degree Ruelle--Lefschetz complex.  Its output, if it exists,
is an alternating Fredholm product, not one scalar determinant.

## Frozen lifted dynamics

For the joint sign branch \(\varepsilon=\operatorname{sgn}q\), define

\[
\widetilde H_a(q,p,m)=
\left(
1-aq^2-p,
q,
\frac{112/123}{-2aq-(123/112)m}
\right),
\]

and

\[
j_{a,\varepsilon}(q,m)
=-\varepsilon\left(-2aq-\frac{123}{112}m\right),
\qquad
g_s=\exp(-s\operatorname{Log}j_{a,\varepsilon}).
\]

The parameter letters remain \(59/10\) and \(61/10\); later letters act on
the left.  The base is not averaged.  The common endpoint disks are the
certified \(X_\sigma,Y_\sigma\), and the projective disk is
\(M=\overline D(0,1/2)\).

Already certified:

- both Hénon letters share the strict two-coordinate complex pinning disks;
- the projective map sends \(M\) into \(|m|<125440/466211\);
- its slope derivative is at most \(11289600/129299641<1\);
- the oriented factor \(j\) stays in the right half-plane at distance at
  least \(11371/3360\) from zero;
- the principal logarithm is common to all chronological branches;
- each periodic base orbit has exactly one lifted periodic point in the
  slope domain, so the stable direction is not double-counted;
- the periodic weight is exactly \(g_s^{(n)}=|\Lambda_{u,n}|^{-s}\).

## Specific mathematical question

Can one construct four graph-directed holomorphic nuclear families
\(\mathcal L_{s,k}\), \(k=0,1,2,3\), for the lifted three-complex-dimensional
branches such that

\[
\operatorname{tr}\mathcal L_{s,k}^n
=\sum_{x\in\operatorname{Fix}\widetilde{\mathcal F}^n}
\frac{g_s^{(n)}(x)
\operatorname{tr}(\wedge^kD\widetilde{\mathcal F}^n_x)}
{\det(I-D\widetilde{\mathcal F}^n_x)}
\]

on one common complex domain, with every word product retaining its genuine
letter order?

If so, the Lefschetz identity would give

\[
\sum_{k=0}^3(-1)^k
\operatorname{tr}\mathcal L_{s,k}^n=B_n(s)
\]

and, initially in the T4 convergence domain,

\[
D_{\mathrm{inst}}(z,s)
=\prod_{k=0}^3
\det(I-z\mathcal L_{s,k})^{(-1)^k}.
\]

## One-round large gates

### G0 -- primary-source reconstruction

Reconstruct the actual analytic exterior kernels from Ruelle's expanding/
Anosov zeta construction, Rugh's pinning theory, Ruelle's differentiable
Fredholm extension, and Baladi--Pujals--Sambarino.  Freeze contour
orientations, mixed variables, form degree, whether tangent or cotangent
exterior powers are used, pullback versus inverse pullback, the exact
derivative/inverse/transpose convention, determinant exponent, and nuclear
ideal before coding.

**Kill:** if the desired Hénon statement is an immediate unmodified
specialization of an existing theorem, record the constants as infrastructure
but do not claim a new operator mechanism or paper.

### G1 -- full lifted pinning domains

Upgrade the separate base and slope inclusions to a single triangular lifted
pinning theorem on connected compact polydiscs with strict enlarged/nested
domains and specified contours.  Every half-map must send the relevant
closure compactly into an interior.  Prove that the relevant partial inverses
are holomorphic and injective and that the lifted Jacobian never vanishes.
Freeze the split \((u;s_1,s_2)=(u;\text{base stable},m)\), prove the stable
block Jacobian is invertible, and construct the unique multidimensional
stable half-inverse.  Prove that every periodic word has only the declared
nondegenerate lifted fixed points, none on a contour or Markov boundary and
none elsewhere in the chosen complex branch domains, with
\(\det(I-D\widetilde{\mathcal F}^n)\ne0\).

**Kill:** any extra lifted periodic branch, slope pole, loss of strict
nesting, or failure of a common two-letter space.

### G2 -- exterior branch operators

Write the four exact one-step branch kernels.  The sum over letters is
\(\mathcal L_{s,k}=\mathcal L_{0,s,k}+\mathcal L_{1,s,k}\), never an
average.  Expansion of its \(n\)-th power must contain every strictly ordered
word product exactly once with the correct state incidences.
The signed orientation local system and exterior-degree action must be
explicit rather than absorbed into an informal contour convention.  Prove
that branch signs form a coherent cocycle and that numerator and residue use
the same signed denominator.  If coherence fails on the graph, use an
explicit orientation double cover or sign line bundle.

**Kill:** a formula that changes the microstep clock, omits ordered words,
uses a finite-memory approximation in place of the exact kernel, averages
transitions, or leaves the trace formal.  An exact higher-block conjugacy is
allowed only if its intertwining and unchanged chronology/multiplicity are
proved.

### G3 -- nuclear factorization

Factor each branch as a bounded analytic composition/multiplication operator
followed by restriction between explicit nested holomorphic domains.  Prove
nuclearity of order zero and locally uniform nuclear bounds in \(s\), or
state a different precise ideal no weaker than the threshold needed for a
canonical trace/determinant.  Prove the approximation property for every
direct-sum Banach space used, so the nuclear trace is representation
independent.  Nuclear-topology holomorphy in \(s\) must be locally uniform.

**Kill:** compactness only, a Hölder-space quasi-compact theorem only,
single-branch singular-value decay, or a finite-section spectrum.

### G4 -- exact supertrace gate

First prove periods one and two by residues, including primitive/double
repetitions, all orientation factors, and the lifted projective derivative.
Then prove general \(n\) by chronological kernel composition.  An independent
checker must reject reversed word order, deleted exterior degree, stable-line
double counting, boundary or spurious complex fixed points, degeneracy, and
absolute/signed convention swaps.

The coding theorem must show that every joint fixed point is counted exactly
once.  If any Markov-boundary multiple coding remains, freeze and prove the
required inclusion--exclusion/Manning correction before taking a trace.

**Kill:** any mismatch at \(n=1,2\).  No larger-period numerical scan is
authorized before these identities pass.

### G5 -- determinant scope

Only after G0--G4 may the alternating determinant be defined.  State whether
the result is entire or meromorphic and give a rigorous upper bound for the
pole divisor, for example through the zeros of denominator Fredholm factors.
Do not claim a complete list of actual poles without a spectral/cancellation
theorem.  An
alternating quotient of entire Fredholm determinants is not called an entire
scalar determinant without a separate divisibility/cancellation theorem.

**Kill:** finite roots without a common-domain/nuclear theorem, or a claim of
entireness inferred only from the individual factors.

## Reproducibility contract

The implementation must contain:

- exact rational domain producer and nonimporting checker;
- symbolic low-period exterior-trace identities;
- explicit Banach spaces, contours, restrictions, and nuclear norms;
- source hashes and artifact hashes;
- chronology, orientation, multiplicity, and scope mutation tests;
- no target zeros, prime data, fitted clocks, Ulam matrices, or averaged
  kernels.

## Promotion and pivot rule

Promote only if G0--G4 pass and the result contains a genuinely Hénon-specific
uniform construction beyond routine theorem substitution.  Otherwise close
the entire C22 operator lineage and change dynamical form; do not return to
finite-memory matrices or longer cycle sections.

Even a full pass would not improve Route-A A1 or A2 by itself.  It would raise
only the internal A3 analytic infrastructure from failure toward partial
structure.  Arithmetic primitives, a completed functional equation, and a
self-adjoint Hilbert--Pólya lift remain separate unsolved problems.
