# Theorem falsifiers and literal mutation ledger

## Purpose

This file lists observations that would refute the scoped theorem, invalidate
one of its proof dependencies, or show that a test is no longer testing the
frozen source. A mutation is not evidence merely because it is listed here;
its expected outcome remains a prediction until the corresponding evaluator
run is recorded in `EXPERIMENT_TRACKER.md`.

## Decisive theorem falsifiers

| ID | Scoped statement | Decisive falsifier | Required response |
|---|---|---|---|
| F1 | exact increment | one frozen primitive pair $(q,A)$ and one $N$ for which direct enumeration gives $Z(N)W_v\ne Z(N-1)W_{v+1}$, $v=\nu_q(N)$ | `THEOREM_STOP`; inspect cutoff and chain proof |
| F2 | exact remainder | one exact mismatch in the coefficientwise valuation identity, or disjoint certified enclosures after both infinite Perron tails are bounded independently | `THEOREM_STOP` |
| F3 | uniform extension | a frozen primitive $A$ for which $\sum_v|d_v-d_{v-1}|=\infty$ | `THEOREM_STOP`; PF-decay lemma is false or misapplied |
| F4 | complete image | an $x\in\mathbb Z_q$ for which the explicit $N_j=(x\bmod q^j)+q^j$ fails either $N_j\to\infty$ or $N_j\to x$ $q$-adically | `THEOREM_STOP` |
| F5 | golden sign | an exact or certified value with $(-1)^k\gamma_k\le0$ | `GOLDEN_STOP` |
| F6 | strong separation | one $k$ with $|\gamma_k|\le\sum_{j>k}|\gamma_j|$ | `GOLDEN_STOP`; topology and dimension proof cannot be used |
| F7 | exact dimension | failure of either uniform diameter $O(t^n)$ or uniform sibling gap $\Omega(t^n)$ | `GOLDEN_STOP` |
| F8 | radial coefficient | a primitive $2^v$-th root $\xi$ for which the certified radial coefficient differs from $-\gamma_{v-1}/(2^{v-1}(1-\xi))$ | `RADIAL_STOP` |
| F9 | natural boundary | analytic continuation across an open unit-circle arc compatible with the nonzero radial limits | `THEOREM_STOP` |
| F10 | ownership | a primary source states the same $\mathbb Z_q$ extension and complete accumulation theorem, or the same golden boundary theorem | `STOP_DUPLICATE` for a standalone Paper 44 |

Finite floating-point disagreement is not by itself a falsifier. It must be
converted to exact arithmetic or disjoint certified intervals, with the
object, indexing, and tail bound recorded.

## Literal mutation families

Consumer keys are exact: `A` is the direct finite-prefix evaluator, `B` is
the independent chain/Perron/Binet/cyclotomic evaluator, `X` is the
non-scientific exact comparator, `T` is the typed contract auditor, `P` is
the proof-certificate auditor, `L` is the literature-ownership auditor, and
`I` is the evaluator-independence auditor. Every and only the listed keys
must return the listed nonzero code; an exception is not a rejection.

Every implementation must expose these mutations as named alternatives, not
as prose-only warnings. Source-changing mutations are expected to be rejected
by the contract checker; formula mutations are expected to disagree with a
positive control.

| Mutation ID | Literal mutation | Exact consumers | Exact nonzero rejection code |
|---|---|---|---|
| `MUT-Q1` | set `q = 1` | T,A,B | INVALID_RADIX |
| `MUT-A0` | replace $A$ by the all-zero matrix | T,A,B | NONPRIMITIVE_ZERO_ADJACENCY |
| `MUT-APR` | use a reducible or irreducible-periodic $A$ while retaining the primitive theorem label | T,A,B | STOP_SCOPED |
| `MUT-EDGE` | replace each edge $n\to qn$ by $n\to n+q$ | A,B,X | SOURCE_EDGE_CHANGED |
| `MUT-PREFIX` | enumerate $\{0,\ldots,N-1\}$ but apply the $\{1,\ldots,N\}$ formula | A,B,X | PREFIX_CONVENTION_CHANGED |
| `MUT-NOSUB` | set $d_v=c_v$ instead of $c_v-\log\rho$ | B,P | PERRON_SUBTRACTION_MISSING |
| `MUT-MODFLOOR` | replace $N\bmod q^v$ by $\lfloor N/q^v\rfloor$ | A,B,X | RESIDUE_FORMULA_MISMATCH |
| `MUT-MODFRAC` | replace the canonical residue by a real fractional part without its $q^v$ normalization | T,A,B | RESIDUE_TYPE_ERROR |
| `MUT-REP` | use $N_j=x\bmod q^j$ with no $+q^j$ | A,B,P | REPRESENTATIVE_NOT_DIVERGENT |
| `MUT-RSIGN` | use $r=+\varphi^{-2}$ in Binet's formula | A,B,X | BINET_SIGN_MISMATCH |
| `MUT-LOGSIGN` | replace $\log(1-u)=-\sum u^m/m$ by the positive-sign series | A,B,X | LOG_SERIES_SIGN_MISMATCH |
| `MUT-TAIL` | certify separation from finitely many $\gamma_k$ without the infinite remainder bound | A,B,P | INFINITE_TAIL_UNCERTIFIED |
| `MUT-DIM` | label $\dim_HE(\mathbb Z_2)$ as the dimension of the original multiplicative shift | T,P | BOUNDARY_DIMENSION_OWNER_ERROR |
| `MUT-POLELEVEL` | retain only the level $w=v$ term at a primitive $2^v$-th root | A,B,X | RADIAL_LEVEL_TAIL_OMITTED |
| `MUT-RADIALXI` | replace the exact bracket coefficient $-1/(1-\xi)$ by the superseded proportional expression $\xi/(1-\xi)$ | A,B,X | RADIAL_COEFFICIENT_NORMALIZATION_ERROR |
| `MUT-MERO` | call the dense boundary points isolated meromorphic poles of the full function | T,P | ANALYTIC_TYPE_ERROR |
| `MUT-CONTENT` | append ordinary Minkowski-content nonexistence to Theorem B | T,P | NOT_CURRENTLY_JUSTIFIED |
| `MUT-OWNER` | mark the chain product, entropy, or leading dimensions as new | L | PRIOR_OWNERSHIP_TRANSFER |
| `MUT-EVAL` | let Evaluator B import fixtures, code, or expected values from Evaluator A | I | EVALUATOR_INDEPENDENCE_FAILURE |

## Proof-dependency kill tests

1. Removing Lemma 2 removes the only exact bridge from prefix counts to the
   valuation sequence; the rest of Theorem A cannot substitute for it.
2. Removing Perron subtraction removes absolute summability and invalidates
   both uniform convergence and the interchange used for $G$.
3. Removing the reverse inclusion in Lemma 6 proves only an upper bound on
   the accumulation set.
4. Removing the exact inequality in Lemma 9 leaves numerical evidence for
   separation but no all-level theorem.
5. Removing the cylinder lower-gap estimate leaves the Hausdorff upper bound
   but not the Frostman/lower-box conclusions.
6. Removing the $w>v$ radial tail changes the coefficient and can make a
   false noncancellation argument.
7. Removing source subtraction makes a mathematically correct derivation an
   invalid standalone novelty package.

## False positives to reject

- Agreement through a finite cutoff does not prove uniform convergence,
  complete accumulation, or an all-level separation inequality.
- A plot resembling a Cantor set does not prove injectivity or dimension.
- Growth of $G(r\xi)$ at finitely many radii does not identify its Abelian
  coefficient.
- Failure to find a paper is not a novelty theorem.
- A mutation rejected only because both evaluators share the same assertion
  or fixture does not count as independent detection.
