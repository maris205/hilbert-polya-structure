# Independent nonauthor review of the complete AS2 classification

2026-09-07 UTC. Review type: current-team AI-assisted internal proof,
source-ownership and substantive-contract review. The reviewer did not
derive or write any AS2 author proof. Reviewing a completed argument does
not make this an external or human peer review.

## Verdict

**PROOF PASS; RECOMMEND ADMISSION AS ONE COMPLETE CONTRACT.**
No unresolved mathematical blocker was found in the assembled all-level
criterion. After deducting the classical scattering machinery and the
local C18 predecessor, the complete necessity-and-sufficiency result is
substantial enough for one source-system classification contract. The
coordinator retains the actual admission decision.

This is not certification of worldwide priority, journal suitability, a
finished manuscript, an evaluator grade, or target arithmetic. A minor
source-location correction identified below has been applied and checked
closed. It does not affect the proof. The source-access limits are retained in the
[source and substance audit](SOURCE_SUBSTANCE_AUDIT.md).

No conference or journal rubric was supplied: `criteria_binding_unavailable`;
venue calibration is `NOT_CALIBRATED`. No numerical acceptance score or
formal editorial decision is assigned. The applicable internal standard
is the repository's complete-question, classical-deduction and nonauthor
review gate, not a fabricated venue threshold.

## Exact claim reviewed

The object is the full width-one cusp scattering matrix of
$\Gamma_0(N)$, with weight zero and trivial nebentypus, for every positive
integer $N$. The cusp coordinates are fixed independently of $s$.
Commutativity means $[\Phi_N(s),\Phi_N(t)]=0$ for every pair at which
the actual meromorphic matrix is regular.

The reviewed equivalence is that every primitive character $\chi$ of
conductor $q$ with $q^2\mid N$ satisfies both:

1. $\chi^2=\bar\chi^2$;
2. $\chi(p)\in\mathbb R$ for every $p\mid N$ with $p\nmid q$ and
   **odd** $v_p(N)$.

The second requirement is absent at even exponents and at primes of the
primitive conductor. The principal character of conductor one is
included. The equivalent elementary conditions are exactly those in the
[current proof index](../AS2_PROOF_INDEX.md), including $v_2(N)\le9$,
$v_3(N),v_5(N)\le3$, and the conditional congruences modulo $5$ and $8$.

This is not either earlier conjecture. The original criterion is
refuted by $N=50$; the first repair is refuted by $N=100$. Their failure
records remain part of the evidence, not retrospectively successful tests.

## Actual reading and checking

Read the complete mathematical contents of:

- [General all-level proof](../independent_review/REPAIRED_CLASSIFICATION.md),
  all eight proof steps and its correction/status sections.
- [Principal oldform proof](../oldform_review/PROOF_PACKAGE.md), including
  cusp normalization, both central parity cases and the complete fixed basis.
- [Character phase-parity proof](../oldform_review/TWIST_PARITY_LEMMA.md),
  including its tensor and actual-scattering applicability arguments.
- [Minimal-level and counterexample proof](../independent_review/PROOF_PACKAGE.md),
  including all Euler factors of an imprimitive square.
- [Parity-sensitive arithmetic equivalence](../AS2_PARITY_CRITERION.md) and
  the explicit finite-group facts in the
  [first-repair record](../AS2_REPAIRED_CRITERION.md).
- The [original conjecture](../AS2_CONJECTURE.md), current proof index,
  coordinator component review, both AS2 source audits, and the full local
  [C18 source audit](../../../modular_open_trace_obstruction/SOURCE_AUDIT.md).

The source audit records the separate primary-source readings. The
mathematical checks were proof checks, not a fresh numerical experiment.
No forty-cell probe, exact counterexample program, larger census or new
parameter grid was run. The conclusion does not depend on having rerun
those diagnostics.

## Mathematical findings and evidence anchors

### R1. Full fixed-coordinate identification — checked, no open issue

Anchor: general proof, Steps 1–3, equations (1)–(6).

At each denominator, ordinary character orthogonality exhausts the cusp
residue group. Unique primitive conductors and the relation
$q\mid\gcd(f,N/f)$ give precisely the stated oldform labels. Thus the
Fourier transform is square, invertible and independent of $s$; it does
not omit nonprincipal or repeated-denominator cusps.

The valuations in the divisor sum produce the claimed unramified
Toeplitz factor and the ramified diagonal factor. In particular the
ramified diagonal has its conductor power, and the unramified factor has
the absolute-distance character phase. Their determinants are not
identically zero. Comparing outgoing constant terms identifies the
paired functional-equation blocks as blocks of the original scattering
matrix under this fixed transform. The parameter-dependent incoming
matrix is never used as an alleged fixed similarity. A real character
contributes one block, not a duplicated conjugate pair.

### R2. Nonreal-square necessity at arbitrary level — checked, no open issue

Anchor: general proof, Step 4, equations (7)–(11), and the minimal-level
auxiliary lemma in its linked dependency.

The determinant quotient forced by commutativity was checked with the
order of all four incoming determinants retained. The primitive
functional equation is applied to the character inducing the square;
primitivity of the original character is not incorrectly transferred to
its square. The missing Euler factors and the additional oldform factors
are all retained. The latter are supported at primes dividing $N$.

Consequently, after normalization at real $s\to+\infty$, the coefficient
at a prime $\ell\nmid N$ is
$d(\ell-1)(\xi(\ell)-\bar\xi(\ell))$. The asserted Dirichlet
expansions converge absolutely in the stated half-plane. A finite factor
at level primes cannot contribute to this coefficient. The CRT argument
really supplies an integer prime to $N$ with nonreal character value;
one of its prime factors has nonreal value. It therefore avoids any
unstated theorem about primes in progressions. This closes necessity at
nonminimal levels, rather than extrapolating the minimal-level example.

### R3. Principal, real and quartic sectors — checked, no open issue

Anchors: principal proof, Steps 1–7; phase-parity proof, Steps 1–5;
general proof, Steps 6–7.

The width-one incoming coefficient was independently checked against the
cusp-height calculation. Class multiplicities lead only to a fixed
diagonal normalization. The principal difference vectors and the central
vectors satisfy the stated generalized eigenvector identities; the
geometric-sum and reciprocal-polynomial arguments cover both parities.
The support and coordinate-sum arguments establish a full fixed basis,
including exponents zero and one and coincident eigenvalues.

For real-square characters, the constant Gauss and phase changes remove
only constant conjugacies and a common scalar. With an imaginary local
phase and even exponent, the remaining phase matrix is the identity.
With odd exponent it interchanges the two central channels; their
eigenvalue ratio is the displayed nonconstant rational function of
$X$. This gives a genuine local noncommutator. It also explains why the
first repair incorrectly excluded $N=100$. No numerical observation is
being substituted for either assertion.

### R4. Assembly and exceptional parameters — checked, no open issue

Anchors: general proof, Steps 5 and 8; parity-sensitive arithmetic proof,
Steps 1–3.

The tensor lemma is strong enough for several bad primes: on a generic
open set, tensor commutativity forces each multiplicative commutator to
be scalar. Determinant one and continuity near the diagonal force that
scalar to be one. Meromorphic continuation then gives local
commutativity identically. Scalar anticommutation or cancellation across
different primes is therefore not a loophole.

The arithmetic proof applies character separation to the prime-to-$p$
part of the square-root level only when $v_p(N)$ is odd. The finite unit
groups give exactly the listed exponent bounds and congruences. No
constraint is accidentally imposed on an even exponent or on a ramified
character value. The empty cases and $N=1$ are covered.

All divisions in the matrix arguments are made generically and then
continued as meromorphic identities. Artificial poles of an intermediate
factor do not exclude a regular point of the original matrix. Both
necessity and sufficiency therefore have the claimed full parameter
scope.

### R5. Source location — minor, corrected and closed

Anchor: [coordinator source audit](../AS2_SOURCE_AUDIT.md), item 2.

In the verified arXiv v2 of Booker–Lee–Strömbergsson, the matrix
functional equation, Lemma 2.26 and reconstruction of the scattering
matrix occur in **§2.7**, not §2.8. The latter starts the explicit
continuous-spectrum contribution. The coordinator corrected the section
pointer, and this reviewer actually reread the corrected item 2 after
that change. It now states the correct §2.7 location and preserves the
correction history. This is a closed bibliographic-location issue; the
actual formulas agree with the proof's use. No mathematical rerun was
needed or performed. No required correction remains open in this review.

## Substantive-contract judgment and boundaries

The proposed increment is one complete answer to when the original
all-level scattering family has parameter-independent commuting
channels. Neither the imported cusp/oldform formulas nor the already
known squarefree tensor structure answers that question by itself.
The proof needs both the nonreal-square obstruction and the exact
quartic parity mechanism, and must rule out hiding either obstruction
inside the full oldform space. Those obligations are now discharged.

I therefore recommend one admission, subject to the accurately bounded
source claims recorded in the companion audit. The principal lemma,
unit-group calculation, $N=50$ counterexample and $N=100$ repair are
components of that contract, not separate papers or admissions. No
second contract is created by reformulating the answer arithmetically.

The spectral parameter remains a spectral parameter, not native
chronological time. Nothing reviewed establishes target Euler factors,
root numbers, a target divisor or zero correspondence, automorphy, or a
Hilbert–Pólya realization. `NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.
No manuscript, C-number, formal evaluator output, registry entry or Git
change is made by this reviewer.
