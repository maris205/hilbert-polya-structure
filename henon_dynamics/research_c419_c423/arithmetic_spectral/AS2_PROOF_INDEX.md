# AS2 all-level proof and coordinator integration

2026-09-07 UTC. Status: COMPLETE PROOF; NONAUTHOR REVIEW PASS;
ADMITTED AS ONE CONTRACT. This is one all-level classification, not a
collection of prime-power papers. The original fixed width-one cusp
coordinate convention, trivial nebentypus and weight zero are unchanged.

## Complete statement

For every positive integer $N$, let $\Phi_N(s)$ be the full cusp scattering
matrix for $\Gamma_0(N)$. Its values commute pairwise at all regular
parameters if and only if all the following conditions hold:

1. $v_2(N)\le9$, $v_3(N)\le3$, $v_5(N)\le3$, and
   $v_p(N)\le1$ for every prime $p\ge7$.
2. If $v_5(N)\ge2$, every $p\ne5$ with odd $v_p(N)$ satisfies
   $p\equiv\pm1\pmod5$.
3. If $v_2(N)\ge8$, every odd prime $p$ with odd $v_p(N)$ satisfies
   $p\equiv\pm1\pmod8$.

Equivalently, every primitive character $\chi$ of conductor $q$ with
$q^2\mid N$ must have real square, and its value at an unramified divisor
prime must be real whenever that prime has odd exponent in $N$.
There is no second condition at even exponents or at a prime dividing $q$.
The empty conditions include $N=1$.

## Proof dependencies and actual coordinator reading

The coordinator has read each complete mathematical dependency below;
this integration check is not described as a wholly nonauthor review,
because the coordinator authored the arithmetic reformulation.

| Dependency | Exact obligation it supplies |
|---|---|
| [General analytic proof](independent_review/REPAIRED_CLASSIFICATION.md) | Full fixed cusp Fourier decomposition; Young local factors; determinant and outside-level Dirichlet coefficient necessity; tensor noncancellation; meromorphic assembly. |
| [Principal oldform proof](oldform_review/PROOF_PACKAGE.md) | All-exponent fixed basis, eigenvalues, width-one applicability, fixed multiplicity normalization, boundary exponents zero and one. |
| [Character phase-parity proof](oldform_review/TWIST_PARITY_LEMMA.md) | Constant phase transforms, odd central two-dimensional obstruction, even-exponent cancellation, all real-character sectors. |
| [Minimal-level scalar lemma](independent_review/PROOF_PACKAGE.md) | Primitive functional equation with all missing Euler factors of an imprimitive square retained. The same file also contains the distinct $N=50$ counterexample. |
| [Arithmetic equivalence](AS2_PARITY_CRITERION.md) and its [explicit group facts](AS2_REPAIRED_CRITERION.md) | Character separation, unit-group exponent bounds and the odd-exponent congruences displayed above. The first repaired analytic conjecture remains false. |

The analytic author also checked the principal and phase-parity dependencies.
The principal author independently derived the actual incoming coefficients
from the cusp geometry and from the second classical formula source.
These cross-checks are useful, but do not replace the separate
assembled-theorem reviewer, who has not coauthored any AS2 proof.
That [review](non_author_review/REVIEW.md) is now complete and PASS.

## Coordinator's mathematical checks

The full Fourier transform uses every character of each cusp residue group;
the unique primitive conductor and divisor labels exhaust that group.
Its entries contain no spectral powers. Incoming oldform matrices do depend
on $s$; they are used in a functional equation, never as a fixed similarity.
Comparing outgoing cusp coefficients identifies the resulting paired blocks
as blocks of the original matrix, not a newly defined scattering family.

Prime factorization of Young's inversion yields diagonal ramified matrices
and the unramified matrices
$$
C_{\chi,p}(s)_{b,k}=
\chi(p)^{|b-k|}p^{s(\max(k,e-k)-|b-k|)}.
$$
The coordinator checked the exponent, conductor factor and generic
invertibility. The principal proof handles both central parity cases and
proves a full fixed basis even when eigenvalues coincide.

For a nonreal square, commutativity forces a determinant quotient to be
constant. After all finite factors at primes dividing $N$ are retained,
its normalized coefficient at $\ell^{-2s}$ for $\ell\nmid N$ is
$$
d(\ell-1)\bigl(\xi(\ell)-\bar\xi(\ell)\bigr),
$$
where $d>0$ is the oldform dimension and $\xi$ induces the square.
The series converges absolutely in the stated half-plane. CRT produces
an integer prime to $N$ with nonreal character value; one of its prime
factors supplies a nonzero coefficient. This uses neither a prime-density
claim nor an assumed noncancellation of imprimitive Euler factors.

For real squares, all conjugate directions reduce by constant similarities
to local principal families times a fixed phase matrix. That matrix is the
identity in the even imaginary-phase case; in the odd case it exchanges
the two central channels. Their ratio
$$
\frac{(p+X)(X-1)}{(p-X)(X+1)}
$$
is nonconstant for $p>1$. The general tensor lemma uses generic
invertibility, partial traces and continuity of a finite set of scalar
roots of unity to exclude cancellation between prime factors.
Meromorphic identities extend to all regular values of the actual matrix,
including removable singularities in intermediate formulas.

The elementary reformulation keeps the conductor-coprimality restriction.
It asks $p^2\equiv1$ modulo the prime-to-$p$ part of the square-root level
only when $v_p(N)$ is odd; applying it at even exponents was exactly the
error in the first repaired analytic conjecture.

No mathematical blocker was found in this coordinator integration check.
The separate independent proof and substantive review has also passed.
The coordinator read both complete review files and adopted the
recommendation of one contract in the [admission decisions](../ADMISSION_DECISIONS.md).
The single source-location correction was actually reread and closed by
the original reviewer; no theorem or mathematical code changed.

## Failed conjectures and computational boundary

The [original conjecture](AS2_CONJECTURE.md) fails at $N=50$.
The [first repair](AS2_REPAIRED_CRITERION.md) fails at $N=100$.
Their exact objects were not changed to avoid these counterexamples.
The second condition above excludes $50$ but includes $100$.

The recorded [40-cell principal probe](AS2_CHECK_RECEIPT.md) and
[single exact counterexample check](independent_review/CHECK_RECEIPT.md)
were not rerun for the general proof. Neither a larger level table nor a
new numerical parameter grid is a premise of this classification.

## Source ownership and scientific gate

The [bounded primary-source audit](AS2_SOURCE_AUDIT.md) credits the
classical explicit scattering formulas, basis changes and squarefree
channels. Huxley's foundational full text was not obtained; Keil's
dissertation was only inspected in specified portions. These are retained
limitations, not concealed by a claim of worldwide novelty.

The proposed residual is the complete all-level fixed-coordinate
commutativity classification, with both necessity mechanisms and exact
parity boundaries. The explicit scattering machinery, principal lemma,
unit-group calculation and small counterexamples do not separately earn
paper slots. The [nonauthor source/substance audit](non_author_review/SOURCE_SUBSTANCE_AUDIT.md)
finds that this full residual meets the substantial-contract gate.
Admission remains conditional on the accurately bounded ownership claims,
not a claim that every possible predecessor was read or excluded.

The spectral parameter is not a native chronological clock. No target
Euler-factor dictionary, root number, zero correspondence or Hilbert–Pólya
realization is established. No paper number or formal evaluation is assigned.
