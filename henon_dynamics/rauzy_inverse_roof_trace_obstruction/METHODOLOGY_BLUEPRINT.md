# HCS-C30 methodology blueprint

## Research design

This is a deductive computer-assisted obstruction study. The computational
part uses exact integer and rational arithmetic; the functional-analytic part
is proved symbolically under explicit hypotheses.

## Frozen objects

- C25 raw fourteen-edge Rauzy graph and matrices;
- C26 raw return matrices (A,B,C);
- C29 words (C_1,C_2,W_{24}) and chronology conventions;
- the positive cone
  (mathbb R_{>0}^{4});
- projective maps
  \(h_M(x)=Mx/\ell(Mx)\), with
  \(\ell(x)=x_1+\cdots+x_4\);
- logarithmic normalizer
  \(r_M(x)=\log\ell(Mx)\).

Every upstream artifact is SHA-256 source-locked. No observed spectrum is an
input.

## Exact positive-cone experiment

For every cyclic phase of a raw identity relation, compute two prefix systems
exactly:

1. the genuine AGY length recurrence
   \(P_k=B(t_k)^{-\mathsf T}P_{k-1}\) in raw path order;
2. the transfer recurrence
   \(Q_k=B(u_k)^{\mathsf T}Q_{k-1}\) after reversing that path phase.

A genuine positive-domain orbit would require every coordinate form of every
prefix to be strictly positive on one common \(x>0\).  The raw covariant
recurrence \(H_k=B(t_k)H_{k-1}\) is checked separately as a convention
control; its positivity is not an AGY length result.

Infeasibility is accepted only with a rational Farkas-type certificate:

\[
 a_1L_1+\cdots+a_kL_k=0,
 \qquad a_j>0,
\]

where each \(L_j(x)\) is a coordinate form required to be positive. Such a
certificate gives the contradiction \(0>0\) without a numerical tolerance or
linear-programming solver.

A single nonzero row with all coefficients nonpositive is also a complete
certificate.  Descriptors are selected canonically by `(step, coordinate)` so
the independent checker can reconstruct them without trusting producer
labels.

## Theoretical gates

1. Derive the general groupoid inverse-sign law and the projective normalizer
   law directly, while separating identity arrows from identity holonomy.
2. Prove the same-space compactness obstruction by block compression and the
   operator-ideal property.
3. For each raw identity word, compute (h_W), (Dh_W), the fixed set, and
   the fixed-point denominator used by standard holomorphic trace formulas.
4. Separate the finite-dimensional Hashimoto/von-Neumann trace-log model from
   an ordinary infinite-dimensional Fredholm determinant.

## Reproducibility design

- `c30_producer.py` reconstructs the certificate from source files.
- `c30_independent_check.py` does not import the producer and replays all
  decisive arithmetic.
- JSON equality is recursive and type-strict; unknown keys fail.
- Mutation tests recompute payload hashes before challenging semantic gates.
- Source paths and hashes, chronology, conclusions, and pivot scope are all
  checked.

## Validity threats

| Threat | Control |
|---|---|
| Confusing symplectic identity with raw dynamical identity | Replay every word using the raw C25/C26 matrices. |
| Reversing chronology | Store raw path, \(B^{-\mathsf T}\) length, and contravariant \(B^{\mathsf T}\) transfer orders separately and verify every final product. |
| Treating one failed starting point as cone infeasibility | Test every cyclic phase with global integer certificates valid for every \(x>0\). |
| Calling raw homology positivity an AGY orbit | Freeze C1/C2 positive covariant controls and label them `raw_homology_zigzag` only. |
| Treating matrix-kernel words as unit arrows | Record signed abelianization and state precisely which cocycles factor through matrix holonomy. |
| Overstating flat-trace failure | Restrict the theorem to ordinary nuclear and standard isolated-fixed-point formulas. |
| Rebranding a graph clock as AGY time | Prove and record the inverse antisymmetry of the true normalizer cocycle. |
| Duplicating prior Hénon pinning work | Source the existing mixed-domain pinning infrastructure and target only its unfinished quantitative tail gate. |

## Preregistration and reporting

The source locks, forbidden data, stop/go rule, and theorem surfaces are
frozen in the code and this document. This is theoretical/computational work;
human-subject IRB review is not applicable.
