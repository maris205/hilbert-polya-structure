# Object, marker, operator, and determinant contract

## Typed objects

| Name | Type | Owner | Equality permissions |
|---|---|---|---|
| \(x\) | `SquarefreeAdmissiblePoint` | \(X_{\rm sf}\) | coordinate equality only |
| \(\sigma\) | `TwoSidedShiftHomeomorphism` | \(X_{\rm sf}\) | source time evolution |
| \(y\) | `TopologicalFactorState` | \(Y\) | target-state equality only |
| \(S\) | `FactorHomeomorphism` | \(Y\) | target time evolution |
| \(\pi\) | `ContinuousOntoZFactorMap` | source-to-target morphism | equivariant for all integer times |
| \(\mathcal O_0\) | `PeriodicOrbit(Y,S)` | factor ledger | sole least-period-one orbit |
| \(p\) | `RationalPrimeAtom` | external comparator | never equal by type to \(\mathcal O_0\) |
| \(K_{\rm per}\) | `FiniteRankLedgerOperator` | singleton periodic core | not a full-state transfer operator |

## Source admissibility field

For each rational prime \(p\) and point \(x\), define the nonempty set of
missing residues

\[
M_p(x)=\left(\mathbb Z/p^2\mathbb Z\right)
\setminus\left(\operatorname{supp}(x)\bmod p^2\right).
\]

The CRT proof may choose one \(a_p(x)\in M_p(x)\) for each of finitely many
pairwise distinct primes. The choice is a proof witness, not a tuned model
parameter.

## Factor contract

The following diagram commutes for all \(n\in\mathbb Z\):

\[
\begin{array}{ccc}
X_{\rm sf} & \xrightarrow{\sigma^n} & X_{\rm sf}\\
\pi\downarrow && \downarrow\pi\\
Y & \xrightarrow{S^n} & Y.
\end{array}
\]

Surjectivity supplies lifts of arbitrary target pairs. Compactness supplies
uniform continuity. Both are used in the factor-proximality proof.

## Marker contract

The marker \(z\) has exactly one meaning: one application of the original
unit-time factor dynamics. Therefore

\[
\mathcal O_0\mapsto z,
\qquad
\mathcal O_0^r\mapsto z^r.
\]

The superscript \(r\) means temporal traversal, not a new primitive object.
The optional rational-prime comparison uses an independent marker \(u\). No
specialization \(u=z\) can repair the mismatch in primitive support.

## Periodic ledger

The theorem fixes

\[
\operatorname{Prim}(Y,S)=\{\mathcal O_0\},
\qquad
\operatorname{Per}(Y,S)=\mathcal O_0,
\qquad
\#\operatorname{Fix}(S^m)=1.
\]

The Euler and logarithmic forms agree:

\[
\zeta_{\rm AM,Y}(z)
=\prod_{\mathcal O\in\operatorname{Prim}(Y,S)}
(1-z^{|\mathcal O|})^{-1}
=(1-z)^{-1},
\]

\[
\log\zeta_{\rm AM,Y}(z)=\sum_{r\ge1}\frac{z^r}{r}.
\]

There is one primitive factor and infinitely many traversals. These are not
infinitely many primitive factors.

## Operator ownership

Let \(\mathcal H_{\rm per}=\mathbb C e_0\) and
\(K_{\rm per}e_0=e_0\). Then

\[
\operatorname{tr}(K_{\rm per}^m)=1,
\qquad
\det(I-zK_{\rm per})=1-z.
\]

This operator packages the already proved singleton ledger. It does not
generate the full source language, encode aperiodic points, define an
analytic continuation of a transfer family, or provide a self-adjoint
spectral realization of a completed arithmetic divisor.

The external rational-prime diagonal family, if introduced on a separate
space, remains externally owned and cannot be credited to \(X_{\rm sf}\) or
any factor \(Y\).

## Determinant convention

The ordinary one-dimensional determinant and the inverse Artin--Mazur
determinant coincide:

\[
D_{\rm AM,Y}(z)=\det(I-zK_{\rm per})=1-z.
\]

This equality is exact as a formal power series near zero and as a polynomial
identity for the inverse determinant. It contains no hidden regularization,
prime weighting, gamma factor, or completed functional equation.

## Firewall verdicts

| Proposed identification | Verdict | Reason |
|---|---|---|
| \(\mathcal O_0=p\) for every prime \(p\) | `TYPE_ERROR` | one object cannot biject to infinitely many primitive atoms |
| \(z^r\) is a new prime primitive | `REPETITION_ERROR` | it is an \(r\)-fold traversal |
| \(K_{\rm per}\) is the source transfer operator | `OWNERSHIP_ERROR` | it acts only on the proved periodic core |
| finite-square approximant repairs the factor ledger | `SOURCE_CHANGE` | it deletes infinitely many exclusions |
| product with a periodic system is a factor repair | `DIRECTION_ERROR` | it changes the source by extension |
| another zeta based on aperiodic statistics is the same determinant | `OBSERVABLE_CHANGE` | fixed-point counts no longer own it |

