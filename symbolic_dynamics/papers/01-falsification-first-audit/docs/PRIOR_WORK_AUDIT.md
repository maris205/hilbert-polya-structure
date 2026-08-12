# Prior-Work Audit for Session 4

Date: 2026-08-12  
Scope: evidence imported into the symbolic-dynamics session only

This audit rechecks the six supplied prior-work items before any claim is used
as a premise.  A published formula, a numerical observation, and an
independently proved statement are kept separate.  None of the earlier systems
is promoted to a Session-4 candidate; non-symbolic implications are recorded
only in the ROUND2 clue ledger.

## Audit table

| Item | Rechecked claim | Session-4 grade | Consequence |
|---|---|---|---|
| Paper 1, prime/logistic construction | The sieve-word limit is a prime indicator and is conjugate to the positive-entropy logistic attractor | **REFUTED** | The pointwise limit is \(RLR^\infty\); its orbit closure has entropy zero |
| Paper 1, band-merging skeleton | The three-symbol factor retains the full arithmetic dynamics | **REFUTED as stated; PROVED as a parity skeleton** | Its zeta is \(1/(1-2z^2)\), so it retains only a mod-2 transition structure |
| Paper 1, twin-prime constant | \(C_2\) is predicted from the symbolic invariant | **REFUTED as an independent prediction** | The scale is calibrated from \(C_2\), then \(C_2\) is recovered |
| Paper 2, admissibility | The gap/parity argument proves every encoded prime-dynamics claim unconditionally | **CONDITIONAL_THEOREM / OPEN** | The stated gap condition and induced-map spectral claims remain obligations |
| Paper 3, sequential logistic theorem | Ordinary ergodic averages yield the claimed \(1/\log n\) arithmetic envelope | **OPEN; proof chain incomplete** | No Session-4 premise is imported |
| Paper 4, matrix product | The averaged propagator equals the chronological product and predicts Riemann zeros intrinsically | **REFUTED / FITTED_PARAMETER** | Averaging removes order; six zeros and a first-zero scale enter the fit |
| Paper 5, geometric carrier | A geometric realization is already supplied | **NOT_TESTABLE from supplied record** | Recorded only as a ROUND2 clue |
| Paper 6, Weil benchmark | The claimed constants have a complete Lean certificate | **source-record verified; independent replay not performed** | May be used only as a provenance-qualified benchmark, never as a Session-4 theorem proved here |

## Paper 1: sieve limit and logistic factor

At sieve level \(k\), let

\[
Q_k(n)=L\quad\Longleftrightarrow\quad \gcd(n,P_k)=1,
\]

where \(P_k\) is the product of the sieving primes used through level \(k\).
For every prime \(p\), the stage that introduces \(p\) marks the position \(p\)
as \(R\).  Every composite is marked at or before the stage of one of its prime
divisors.  Thus, with the conventional exceptional entries at \(1\) and \(2\),
the pointwise limit is

\[
Q_\infty=RLR^\infty,
\]

not the prime indicator word.  Its shift-orbit closure is finite, hence its
topological entropy is zero.  It therefore cannot be topologically conjugate,
in the standard sense, to a positive-entropy logistic attractor.

For the exact band-merging parameter \(u_c\), the audit gives

\[
u_c^3-2u_c^2+2u_c-2=0,\qquad 1<u_c<2,
\]

with \(u_c\approx1.543689012692\).  Put \(b=u_c-1\) and

\[
A=[-b,0],\qquad B=[0,b],\qquad C=[b,1].
\]

The corresponding adjacency matrix is

\[
\mathsf A=
\begin{pmatrix}
0&0&1\\
0&0&1\\
1&1&0
\end{pmatrix}.
\]

Consequently,

\[
h_{\rm top}=\log\sqrt2,\qquad
\zeta_{\mathsf A}(z)=\frac{1}{\det(I-z\mathsf A)}
=\frac{1}{1-2z^2}.
\]

**PROVED:** this is an exact finite symbolic factor.  
**REFUTED:** it is not a complete rational-prime or prime-power ledger.

The reported twin-prime comparison also uses

\[
k=\frac{2C_2}{\mu_{LRL}},
\]

and then recovers \(C_2\) from the same equality.  That is a calibration
identity, not a first-principles prediction.

Sources: [journal article](https://doi.org/10.1080/27684830.2026.2684334),
[archived version](https://doi.org/10.5281/zenodo.18439638), and
[associated code](https://github.com/maris205/prime_logistic).

## Paper 2: exact defects and conditional chain

The finite-word checks locate the reported first defects at:

- \(k=3\): shift \(22\), integer \(31\);
- \(k=5\): shift \(112\), integer \(125\).

The parity-gap lemma is one-way and does not by itself close the final
admissibility statement.  The latter remains conditional on the declared
prime-gap input.  A scan through \(k\le5000\) is a numerical observation, not
a proof of the unbounded claim.

The induced-map spectral gap, its geometric-tail estimate, and the limiting
measure identification are not established by the finite numerical measures
alone.  Session 4 therefore imports none of them as proved operator facts.

Sources: [archived manuscript](https://doi.org/10.5281/zenodo.20463341) and
[associated code](https://github.com/maris205/prime_dynamics).

## Papers 3–5: proof-chain and scope warnings

For Paper 3, sequential use of logistic-map results does not automatically
give a theorem for a nonautonomous composition.  In particular, an ordinary
Birkhoff average has no mechanism that by itself produces a \(1/\log n\)
envelope.  The claimed bridge is therefore **OPEN**.

For Paper 4, the chronological object is

\[
P_TP_{T-1}\cdots P_1,
\]

whereas replacing it by an average deletes noncommutative order information.
The reported comparison also trains a parameter on the first six Riemann
zeros and fixes a scale using the first zero.  It is consequently a
target-trained finite fit, not an intrinsic determinant calculation.

Source: [Paper 4 preprint](https://doi.org/10.21203/rs.3.rs-9024307/v1) and
[associated code](https://github.com/maris205/riemann_logistic).

Paper 5 is retained only as a provenance note for a possible external
geometric carrier.  It is not developed in this session.

## Paper 6: provenance-qualified Weil benchmark

The supplied local manuscript is dated 2026-08-10 and attributes the result to
“CLAUDE.”  The accompanying public repository states a sorry-free Lean
formalization of its named theorems and records the expected small axiom set.
The source tree and audit record were inspected, but the full multi-gigabyte
Lean build was not independently replayed in this session.  No DOI, arXiv
record, or peer-reviewed version was located as of the session date.

Accordingly, the constants reported there—including the \(2/3\) benchmark and
the stronger simple/distinct-zero variants—are labelled **source-record
verified**, not **independently certified here**.  They may serve as a
comparison target for the eventual Weil-form bookkeeping, but they supply no
symbolic candidate and no Route-B permission.

Source: [public Lean repository](https://github.com/anthropics/zeta-23-lean).

## Import policy

Only the following facts are imported into Session 4:

1. the exact finite Markov calculation above;
2. the distinction between chronological and averaged propagation;
3. the need to expose calibration and target data;
4. the provenance-qualified Weil benchmark;
5. the obligation to keep a symbolic arithmetic ledger, determinant, and any
   later geometric carrier on one frozen construction.

Everything else must be rederived or independently sourced inside this
package.
