# Prime indecomposables are not a full prime-orbit flow

**Paper ID:** 186-multiplicative-bar-clock  
**Candidate ID:** AFC-20260916-MBC01  
**Date:** 2026-09-16  
**Status:** STOP — PRIME H1 CLASSES, BUT COMPOSITE HIGHER HOMOLOGY AND WRONG POINT-ORBIT CLOCK.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

We construct a factorization chain complex using all ordered words of
integers greater than one and adjacent-factor multiplication. Its entire
first homology derives one basis class per prime without a prime table.
However, the complete homology retains a nonzero composite class already
at weight 6 in degree two. A uniform product-character action commutes
with the differential, but its actual point orbits in a nonzero weight
line have period 2pi/log N and continuously many amplitude packets,
not one orbit of length log p per prime. These exact early tests stop
the proposed full prime-orbit interpretation. The algebraic source result
is retained; no homological degree, amplitude or quotient is selected to
repair it. No global high-degree classification or trace is attempted.

## 1. Frozen object, question and lineage

The [version-1 card](candidate-card.md) preceded this proof. This is an
arithmetic factorization complex and algebraic real action, explicitly
type-labelled AFC. It is neither a classical symplectic suspension nor
a constructed Hilbert/quantum operator. The question is whether keeping
all factor words and all resulting homology produces the requested
prime-only packet and clock mechanism.

The [prior-work lineage](../../docs/prior_work/README.md) is proper-divisor
exclusion -> multiplicative factor-word admissibility -> homological
identification -> proposed arithmetic action. This is an explicit algebraic
replacement of the prime/composite symbolic encoding. It is not a
Logistic or Henon conjugacy, or a generic operator detached from arithmetic.

| Item | Exact owner | Boundary |
| --- | --- | --- |
| Arithmetic data | All integers n>=2 and ordinary multiplication | No prime predicate, table or fitted data defines the complex |
| Carrier | All finite complex-linear combinations of factor words in every positive degree | Algebraic direct sum, not a Hilbert completion |
| Evolution between degrees | Alternating adjacent-factor merging d | A chain differential, not a physical time step |
| Real action | U_t multiplies every weight-N vector by N^(it) | A declared uniform character; its actual point period must be computed |
| Full packet proposal | All nonzero homology sectors and their finite-dimensional point orbits | No H_1 projection or normalized-representative choice |
| Analytic/later owner | NOT SUPPLIED | No trace, determinant, self-adjointness or quantum assertion |
| Classical map, roof and suspension | NOT APPLICABLE | No formal A0--A2 or Route-B promotion |

The nearest inspected local cards, 158 and 166, concern localization
groupoids with respectively a basic de Rham differential and a zero-
differential unit-exterior model. Neither supplies this integer word
complex, its action or an analytic result for it. This is a bounded
local collision comparison, not a global novelty claim.

## 2. All factor words and the exact differential

For k>=1 let C_k have basis [n_1|...|n_k], each n_i>=2. Put
C_0=0 and d_1=0, and define

\[
d_k[n_1|\cdots|n_k]
=\sum_{i=1}^{k-1}(-1)^{i-1}
[n_1|\cdots|n_i n_{i+1}|\cdots|n_k].
\tag{1}
\]

The weight N is product n_i. It is preserved by d. For each fixed N
there are finitely many such words: each entry is a divisor of N and
the word length is at most floor(log_2 N). Thus every weight subcomplex
is finite-dimensional, but the full object includes all weights and
degrees with finite linear support.

**Lemma 1.** Equation (1) defines a chain complex, and its homology
decomposes algebraically as the direct sum of its weight homologies.

**Proof.** Write m_i for merging entries i and i+1. For i<j,
m_i m_j=m_(j-1)m_i, including the overlapping case by associativity.
Their coefficients in two consecutive differentials are respectively
(-1)^(i+j-2) and (-1)^(i+j-3), hence cancel. These pairs exhaust
the terms of d^2, which is zero. Since d preserves weight and every
vector has finite support, kernels and images are the corresponding
algebraic direct sums. In particular a missing boundary in one weight
cannot be supplied by another weight. QED.

For orientation within standard algebra, let A have basis e_n for all
positive integers, e_m e_n=e_(mn), and unit e_1. The map alpha(e_1)=1,
alpha(e_n)=0 for n>1 is an augmentation, because a product of two
integers greater than one is greater than one. Its ideal A+ has exactly
the positive factor basis above. Equation (1) is the positive-degree
reduced bar differential for this augmentation. It is not the different
augmentation sending every e_n to 1. Removing degree zero was fixed
before proof and does not remove any positive-degree homology.

The same differential and zero map at degree one are described in
[Positselski, Differential graded Koszul duality, Section 1.1](https://arxiv.org/pdf/2207.07063),
[DOI 10.1112/blms.12797](https://doi.org/10.1112/blms.12797).
Only that localized definition is used. No Tor computation, Koszul-duality
equivalence or all-degree theorem from the survey is imported; the
necessary elementary homology is calculated directly below.

## 3. Positive source result and the first decisive composite

**Proposition 2 (all first homology).** H_1 has basis the classes [p]
for primes p, each in its own weight p. All composite weight-N classes
vanish in H_1.

**Proof.** Since d_1=0, H_1=C_1/im d_2. Every d_2[a|b]=[ab]
is a composite basis vector. Conversely every composite n=ab, a,b>=2,
arises this way. Therefore im d_2 is exactly the span of the composite
basis vectors. The remaining independent basis vectors are precisely
the multiplicatively indecomposable integers greater than one. This
derives primes from the whole factorization rule, without an input list
or a choice of one factorization for each integer. QED.

That is an exact source construction, but not yet the full homology or
a closed-orbit statement. The frozen whole object contains every degree.

**Proposition 3 (complete weight-6 counterexample).** The full homology
has a one-dimensional degree-two sector at composite weight 6, represented
by [2|3]-[3|2]. In contrast the complete weight-4 subcomplex is acyclic.

**Proof.** At weight 6 the only nonzero chain groups are

\[
C_{1,6}=\mathbb C[6],\qquad
C_{2,6}=\mathbb C[2|3]\oplus\mathbb C[3|2],\qquad
d_2=(1\ \ 1).
\tag{2}
\]

There is no C_(3,6), since three factors >=2 have product at least 8.
Hence the kernel of d_2 is the displayed nonzero difference and has
no incoming boundary. Weight preservation excludes an incoming boundary
from any other integer. H_(1,6)=0 and H_(2,6)=C. At weight 4 the
only groups are C_(2,4)=C[2|2] and C_(1,4)=C[4], with d_2 an
isomorphism; higher groups are zero for the same minimum-product reason.
This gives all homology of those two exact weights. QED.

These are complete finite subcomplex calculations yielding an exact
counterexample to a global prime-only assertion, not finite sampling
offered as proof that every higher degree has been classified. The
weight-6 obstruction already ends that target; no all-degree Koszul
calculation is needed to keep the candidate alive.

## 4. A character frequency is not an orbit length

The fixed action on a weight-N word and its homology class is

\[
U_t v=N^{it}v=e^{it\log N}v,\qquad t\in\mathbb R.
\tag{3}
\]

The group law follows directly from exponential addition. Since d
preserves N, it commutes with U_t, which therefore acts on every
homology sector. It is well-defined algebraically on the full direct
sum. On each finite-dimensional weight sector this is an ordinary
smooth complete linear real action. No global infinite-dimensional
topology or Hilbert generator is asserted by those statements.

**Proposition 4 (actual point-orbit control).** In any nonzero weight-N
homology line, each nonzero point has least positive time

\[
P_N=\frac{2\pi}{\log N}.
\tag{4}
\]

That line contains continuously many distinct nonconstant time orbits,
as well as its fixed origin. Its positive repeats have time rP_N.

**Proof.** For v nonzero, U_t v=v is equivalent to exp(it log N)=1.
Since N>=2, the positive solutions are exactly integer multiples of
2pi/log N. Choose any nonzero vector in the line merely as a coordinate
for this calculation. The orbits of rho v for rho>0 are distinct:
the action has unit modulus, so no time maps rho v to rho' v when
rho differs from rho'. The chosen coordinate imposes no normalization
on the carrier. Zero is fixed by every U_t. QED.

This already applies to every prime line of H_1, and separately to the
composite weight-6 line of H_2. Even discarding H_2 would neither give
one point orbit per prime nor convert the reciprocal-logarithmic times
into logarithmic times. Calling log N a character frequency is correct;
calling it the period of (3) reverses the relation. No new roof is
inserted to change (4).

## 5. Controls and meaning of the stop

| Control | Exact result and boundary |
| --- | --- |
| Prime weight p | C_(1,p) alone survives, giving a genuine indecomposable class; its point action still has all amplitude circles |
| Composite weight 4 | Complete acyclicity, which alone would be a misleading positive screen |
| Composite weight 6 | Nonzero H_2 survives in the unchanged full complex and defeats the prime-only full-homology target |
| Keep only H_1 | Gives prime-indexed algebraic classes but is a different observable/carrier, not the frozen full homology; the time/multiplicity obstruction still applies to its point action |
| Identify factor-word permutations or use a shuffle quotient | Changes the complex and may change (2); no such quotient is performed or asserted to work |
| Choose one amplitude, vector or projective line | Deletes point orbits or changes their equivalence relation; not a full-orbit count for (3) |
| Replace integer multiplication by a free commutative monoid on arbitrary generators | The same H_1 argument retains those generators. This PROVES_TOO_MUCH control limits arithmetic naturalness, not the validity of the integer calculation |
| Treat d as physical evolution | d lowers degree and satisfies d^2=0; it is not an invertible real flow or a source of return times |

## 6. Owner-level decision

| Obligation | Exact outcome | Status |
| --- | --- | --- |
| T0-style category and ownership | A full algebraic complex, all weight sectors and its compatible algebraic action are defined | ESTABLISHED only in the declared algebraic category |
| T1-style arithmetic source | H_1 derives precisely the integer indecomposables | Positive source control; naturalness OPEN and no physical logarithmic clock |
| T2-style full packets / repetitions | Higher composite homology and continuous point-orbit multiplicity; actual time (4) | Scoped FAIL of the proposed prime-only log-period interpretation |
| T3 analytic owner | No completion, trace, determinant or full high-degree formula attempted after the decisive test | NOT ADVANCED |
| Classical A0--A2 | No classical phase space or symplectic suspension supplied | NOT APPLICABLE |
| Formal Route coordinates / Route B | No formal protocol evaluated | UNASSIGNED / NOT INVOKED |

Decision: STOP the frozen full-homology prime-orbit interpretation and
retain the exact H_1 source construction as a control. The decisive
first full-object counterexample is weight 6; the actual-time test is
an independent, predeclared control. Do not hide the higher sector,
normalize point orbits, or attach a different clock. A changed complex,
quotient, degree selection or action requires a fresh card. These results
do not rule out all derived or homological approaches.

## Evidence and reproducibility

All definitions, inputs and stops are fixed in the [card](candidate-card.md).
The [ledger](claim-ledger.md) separates the source result and failed
interpretation. The [evidence index](evidence/README.md) records source
access and actual separate review. Every calculation above is exact:
there is no orbit sample, fitted constant, precision parameter, script,
matrix experiment or arithmetic data table. The proof uses the complete
weight-4/6 complexes with a rigorous length bound and all first homology.
ARS contributes bounded claim/evidence/reasoning and counterargument
discipline only. This AI-authored note and its actual nonblind model
review are not human peer review or an independent-error certificate.
