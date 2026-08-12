# Methodology Blueprint

## Research paradigm

**Selected:** exact deductive mathematics with falsification-oriented
computer algebra.

The research question concerns algebraic identities, function fields,
singularity type, and square classes.  Numerical continuation can be a
sanity check, but every promoted claim must be proved by exact arithmetic.

## Method

**Type:** theoretical/computational algebraic dynamics.  
**Specific method:** chronological recurrence reduction, resultants and
subresultants, quotient-field arithmetic, local plane-curve analysis, number
field norms, and independent finite-field replay.

This method answers the question because the equal-action locus is an
elimination image of an exact periodic-orbit cover, while the local
Morse-isometry gate is precisely a determinant square-class question.

## Frozen mathematical objects

For

\[
H_A(q,p)=(1-Aq^2-p,q),
\]

the cyclic action is

\[
\Phi_{5,A}(x_0,\ldots,x_4)
=\sum_{i\bmod5}
\left(x_ix_{i+1}-x_i+\frac A3x_i^3\right).
\]

On the reversor line \(p=q\), remove the fixed-point factor from
\(\operatorname{Fix}(H_A^5)\).  The resulting exact period-five marker is

\[
\begin{aligned}
G_A(q)={}&A^6q^6+2A^5q^5+(-3A^5+2A^4)q^4
 +(-4A^4+2A^3)q^3\\
&+(3A^4-4A^3+A^2)q^2+(2A^3-2A^2)q
 -A^3+2A^2-A-1.
\end{aligned}
\]

Let

\[
R_A(q)\equiv 3A^2\Phi_{5,A}\pmod{G_A(q)},
\]

and define the primitive action polynomial

\[
W_5(A,c)=A^{-30}\operatorname{Res}_q
\bigl(G_A(q),3A^2c-R_A(q)\bigr).
\]

The Hill polynomial is computed independently from the chronological
derivative product, or equivalently checked against the cyclic Hessian via
Hill's identity.

## Data strategy

### Primary mathematical data

- exact coefficients derived from the recurrence and generating action;
- the C12A generic period-five marker as a byte-locked regression source;
- the C32 \(p=61,n=5\) collision as a post-discovery regression control;
- symbolic quotient-field data over
  \(K_9=\mathbb Q[A]/(P_9(A))\).

### Sampling

There is no statistical sample.  The characteristic-zero calculation is the
primary proof.  The split primes

\[
61,\ 157,\ 3203,\ 21943
\]

are the complete prime factorization of \(P_9(6)\) and therefore form a
structurally selected specialization ledger rather than a fitted prime list.

## Analytical workflow

1. **Source/equivalence lock.** Re-derive \(G_A\) from the Paper-5 recurrence
   and verify the exact scaling to the Hamiltonian Hénon convention.
2. **Exact-period firewall.** Divide out the period-one factor before any
   action elimination; verify generic degree six.
3. **Action reduction.** Generate the five chronological coordinates and
   reduce \(3A^2\Phi_{5,A}\) modulo \(G_A\).
4. **Plane image.** Compute \(W_5\), prove it is primitive and irreducible,
   and prove \(\mathbb Q(A,c)=\mathbb Q(A,q)\).  This records that the
   normalization is old while the plane embedding may be new.
5. **Discriminant split.** Independently compute
   \(\operatorname{Disc}_qG_A\) and \(\operatorname{Disc}_cW_5\).  Separate
   orbit-cover ramification from equal-action collision factors.  Certify
   \(\operatorname{Gal}(P_9/\mathbb Q)=S_9\) from irreducibility and exact
   unramified modular cycle types, rather than a numerical Galois routine.
6. **Node theorem.** Over \(K_9\), use subresultants to recover the unique
   double action value \(c_0\) and the quadratic branch-pair polynomial
   \(g_2(q)\).  Verify
   \(W=W_A=W_c=0\), \(W_{cc}\ne0\), and nonzero tangent-cone discriminant.
7. **Nonparabolic gate.** Compute the Hill polynomial \(h_A(q)\) and prove
   \(\operatorname{Res}_q(G_A,h_A)\) is coprime to \(P_9\).
8. **Kummer invariant.** Reduce \(h_A\) modulo \(g_2\), compute
   \(N_H=h_A(q_1)h_A(q_2)\), and prove \(N_H\notin K_9^{\times2}\) using an
   exact rational field norm with an odd valuation.
9. **Gauge audit.** Prove that equal-action collisions survive addition of a
   parameter-dependent constant, cyclic coboundaries, and a common nonzero
   rescaling.  Prove that branch exchange and a common Hill normalization
   change \(N_H\) only by a square.
10. **Finite-prime controls.** Replay all four primes dividing \(P_9(6)\),
    recovering the two branches, their action, Hill values, and the quadratic
    character of \(N_H\).
11. **Independent checker.** Recompute resultants with Sylvester determinants
    or modular interpolation, use a separately written quotient-ring engine,
    and reject all verdict fields unless reconstructed.
12. **Route-A evaluation.** Treat the Kummer cover as arithmetic structure,
    not as a cross-period determinant or a Riemann-divisor bridge.

## Falsification gates

| Gate | STOP/redirect condition |
|---|---|
| Novel divisor | \(P_9\) divides the old marker discriminant or is reducible into known lower-period factors. |
| Node geometry | The generic point is a cusp, higher collision, or nonreduced artifact rather than two transverse branches. |
| Morse scope | Either branch is generically parabolic on \(P_9\). |
| Kummer content | \(N_H\) is a square in \(K_9\), or its class depends on branch labeling or action gauge. |
| Arithmetic control | The four primes fail exact specialization or do not include both square and nonsquare cases. |
| Novelty | A primary source already contains the same degree-nine action-node divisor together with its Hill Kummer cover. |
| Route A | Any claim silently promotes a fixed-period algebraic cover into a Hilbert--Pólya operator or global dynamical determinant. |

## Validity criteria

| Criterion | Strategy |
|---|---|
| Algebraic correctness | Two implementations; exact rational/integer arithmetic; canonical serialization and SHA-256 locks. |
| Exact-period validity | Explicit factor removal and independent least-period controls at specializations. |
| Chronology | Generate coordinates by the recurrence in chronological order; use only cyclically invariant action/Hill quantities. |
| Singularity validity | Verify derivatives and tangent cone in the residue field, not just a squared discriminant exponent. |
| Square-class validity | Prove descent by \([h_1/h_2]=[h_1h_2]\); certify nonsquareness by exact field norm. |
| Good-prime scope | Exclude denominator, leading-coefficient, orbit-discriminant, characteristic-two, and characteristic-three primes as appropriate. |
| Novelty discipline | Phase-2 primary-source audit; label any priority conclusion search-bounded. |
| Reproducibility | Producer/checker separation, mutation tests, deterministic manifest, no hidden CAS session state. |

## Limitations by design

- Period five is a proof-of-mechanism, not a cross-period tower.  A positive
  result authorizes, but does not prove, an all-period construction.
- A nontrivial Kummer cover is arithmetic monodromy, not yet a transfer
  operator or self-adjoint spectrum.
- The pilot does not prove the full combined group \(C_2\wr S_9\).  That
  would require independence of the nine conjugate Kummer classes, not just
  nonsquareness of one class in \(K_9\).
- The normalization is birational to the already known marker cover.  The
  only candidate novelty is the singular action embedding and Hill coupling.
- The prime \(61\) witness was discovered in C32 before this protocol.  It is
  a regression control, never a preregistered prediction.
- The general existence of self-intersections under projection is not
  Hénon-specific; the contribution must be stated as an exact Hénon
  specialization with a dynamical Hill decoration.

## Ethics, reporting, and preregistration

- **Human subjects / IRB:** not applicable.
- **Ethics:** disclose AI assistance, exact source provenance, and the
  post-pilot status of \(p=61\).
- **Reporting standard:** theorem--proof--certificate format; no EQUATOR
  human-study guideline applies.
- **Preregistration:** the Phase-1 files serve as a repository design freeze.
  Phase-2 search and Phase-3 implementation must preserve these falsifiers.

## Design-freeze checkpoint audit

`ARS_CROSS_MODEL` is unset, so no external-model content transfer or blind
checkpoint was performed.  The primary design decision is **sound**, with
high confidence, because the question, exact objects, falsifiers, and
independent verification strategy align.  The mandatory in-family Devil's
Advocate review is recorded separately.
