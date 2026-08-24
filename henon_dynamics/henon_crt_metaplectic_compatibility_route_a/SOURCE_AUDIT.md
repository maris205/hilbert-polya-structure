# Source audit — HCS-C136

## Frozen local source

The only inherited mathematical object is HCS-C131, the odd-level
metaplectic family for

\[
A=\begin{pmatrix}3&-1\\1&0\end{pmatrix}.
\]

The precise local inputs inspected on 2026-08-24 were:

| artifact | SHA-256 | content used |
|---|---|---|
| `../henon_odd_level_metaplectic_family_route_a/results/c131_odd_metaplectic_evidence.json` | `676c4469cb52785efb46ed258b9d7207a8db3c0457d7ea8205e22bee382b3869` | frozen odd-level Weyl, Fourier, chirp, unitary, and one-step clock conventions |
| `../henon_odd_level_metaplectic_family_route_a/THEOREM_PACKAGE.md` | `74b317b5a31c4a476060531f4527785afba3e9dc7930167591a4c546d932f415` | exact per-level Egorov theorem and its stated cross-level nonclaim |

No claim is imported from a title, abstract, bibliographic database, or
unread external paper.  The CRT theorem in C136 is derived in the package and
checked by exact modular arithmetic.  The generalized antiunitary theorem is
also derived here from the frozen Fourier, chirp, Weyl, and residue-basis
conjugation formulas; no antiunitary conclusion is imported by citation.
C131's `c=1` antiunitary is a consistency baseline, but C136 rederives the
statement for every unit `c` and proves the new CRT compatibility directly.

## Source-owned data

Allowed inputs are:

- the integer matrix `A` above;
- odd levels and units in their residue rings;
- the canonical residue map for pairwise-coprime factors;
- exact integer inverses, congruences, and finite case ledgers.

Forbidden inputs are:

- prime or zero tables;
- arithmetic Euler factors, local factors, or root numbers;
- fitted phases or an externally selected target divisor;
- Route-B operators or spectral targets;
- floating-point phase comparisons.

## Integrity boundary

The active scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.  C136 proves compatibility
inside the generalized additive-character family.  It does not claim that the
standard `c=1` factors are directly compatible, nor does it construct a
coherent correction back to those standard factors.  Noncoprime and even
factor levels are outside the theorem.  Multifactor coherence is only for
fixed ordered leaves under changes of binary split schedule and
parenthesization; no permutation or braiding coherence is claimed.

## Citation status

The short paper is self-contained and contains no external citations.  Thus
there is no unverified bibliography entry or citation-to-claim alignment to
promote.  The local C131 dependency is byte-locked above.
