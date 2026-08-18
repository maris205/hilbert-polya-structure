# Theorem Falsifiers — Paper 47

## Required negative controls

Consumer keys are frozen as follows: `D` is the direct ordered-pair
evaluator, `P` is the coprime-scale/analytic evaluator, `X` is their
independent cross-check, `A` is the typed read-only proof/result auditor, `L`
is the literature-ownership auditor, and `R` denotes both strict Route
validators. The consumer set in each row is exact, not a minimum.

| ID | Mutation | Exact consumers | Exact rejection |
|---|---|---|---|
| F01 | Replace \(m+n\mid mn\) by \(m+n\le mn\) | D,P,X | SOURCE_RELATION_CHANGED |
| F02 | Delete even loops | D,P,X | LOOP_CONVENTION_CHANGED |
| F03 | Omit the coprimality condition on \(a,b\) | P,X | EDGE_PARAMETERIZATION_NONUNIQUE |
| F04 | Replace \(g=t(a+b)\) by \(g=tab\) | P,X | EDGE_PARAMETERIZATION_FALSE |
| F05 | Assert boundedness at \(\sigma=0\) | P,A | UNBOUNDED_DEGREE_ENDPOINT |
| F06 | Assert \(S_2\) at \(\sigma=1/2\) | P,A | LOOP_SCALE_HS_DIVERGENCE |
| F07 | Assert \(S_1\) at \(\sigma=1\) | P,A | EVEN_DIAGONAL_TRACE_DIVERGENCE |
| F08 | Drop the scale factor \(\zeta(2s)\) from \(\operatorname{Tr}E_s^2\) | D,P,X | SECOND_TRACE_SCALE_FAILURE |
| F09 | Drop the coprime divisor \(\zeta(4s)\) | P,X,A | PRIMITIVE_MT_FACTOR_FAILURE |
| F10 | Insert an extra factor \(2\) for ordered edges | D,P,X | ORDERED_EDGE_MULTIPLICITY_FAILURE |
| F11 | Call \((a,b)=1\) a primitive temporal orbit | A | PRIMITIVE_TYPE_FAILURE |
| F12 | Call \(E_s\) positive semidefinite for real \(s\) | D,A | NEGATIVE_PRINCIPAL_MINOR |
| F13 | Use ordinary determinant for \(1/2<\sigma\le1\) | A | DETERMINANT_DOMAIN_FAILURE |
| F14 | Claim MT-series novelty | L | LITERATURE_OWNERSHIP_FAILURE |
| F15 | Remove the mixed triangle while retaining the same support | D,P,X | SUPPORT_WITNESS_FAILURE |

## Positive controls

| ID | Control | Expected result |
|---|---|---|
| P01 | direct divisibility on all pairs up to the cutoff | agrees with divisor-row enumeration |
| P02 | coprime-scale triples generating endpoints up to the cutoff | agrees with the same edge set |
| P03 | row \(m=6\) | neighbors exactly \(3,6,12,30\) |
| P04 | loops up to the cutoff | exactly the even vertices |
| P05 | triangle \(15,30,60\) | all three ordered edge pairs legal |
| P06 | exact \(s=2\) second trace truncations | direct matrix and primitive-MT lanes agree |
| P07 | complex phase control | singular values depend only on \(\Re s\) |

## Quantifier and ownership guards

- ordered edges are not unordered graph edges in the trace sum;
- coprime primitive and temporal primitive are distinct types;
- all endpoint inequalities are strict;
- the classical MT series is prior art;
- finite truncations test implementations but do not prove endpoints;
- no result is allowed to rely on Paper 46's generated files.
- for every negative row, every and only the exact listed consumer keys must
  occur, and each must return the row's exact rejection code.
