# CSF bounded owner and collision audit

**Audit date:** 2026-09-03 UTC  
**Candidate:** cyclic successor-feedback `T_q(w)_i=1{w_(i+1)=w_i+1}`  
**Decision:** `FAIL_VALUE_AFTER_SUBTRACTION`  
**External status:** `HOLD_EXTERNAL`  
**Novelty/priority claim:** none

## 1. Subtraction rule

The owner gate separates four ingredients:

1. the q-ary successor-edge mask and its exact cyclic difference count;
2. the binary map `U(b)_i=(1-b_i)b_(i+1)`;
3. the cyclic independent-set/rotation core;
4. the weighted pullback through all binary preimages of a target.

Any direct owner of an ingredient removes contribution credit for that
ingredient and all formal corollaries.  A search non-hit for the exact
four-part conjunction does not restore credit and does not establish novelty.

## 2. Direct owner of the binary temporal core

### Braga--Cattaneo--Flocchini--Mauri (1993)

G. Braga, G. Cattaneo, P. Flocchini, and G. Mauri,
[*Complex Chaotic Behavior of a Class of Subshift Cellular
Automata*](https://www.complex-systems.com/abstracts/v07_i04_a02/),
**Complex Systems 7** (1993), 269--296.
[Primary full text](https://content.wolfram.com/sites/13/2018/02/07-4-2.pdf)

This is a direct temporal owner, not merely general CA background.  Its Rule
34 transition table is the Boolean function that is one on neighborhoods
`001` and `101`, hence

```text
f(l,c,r)=(1-c)r.
```

That is exactly CSF's binary tail (the left input is unused).  Proposition 3
states that every Rule-34 configuration enters after one step the subshift
forbidding `011` and `111`; together those two forbidden length-three blocks
are exactly the condition that `11` never occurs.  On that subshift the rule
is the shift.  The paper also explicitly develops the transition-matrix
description of the Rule-34 subshift.

Its setting is bi-infinite, but the local statement restricts immediately to
periodic words of any circumference.  Therefore CSF receives zero credit for:

- `U({0,1}^n)=I_n`;
- `U|I_n=sigma`;
- entry into the recurrent core in one binary step;
- the absence of transient cycles and every later rotation consequence.

### Meunier (2016)

Pierre-Étienne Meunier,
[*Unraveling simplicity in elementary cellular automata*](https://doi.org/10.1016/j.tcs.2016.01.004),
**Theoretical Computer Science 641** (2016), 2--10.
[Primary manuscript](https://arxiv.org/html/1406.5306)

Proposition 3 independently classifies Rules 2 and 34 among elementary rules
with constant dependency and again explains their eventual shift behavior.
The article's short Rule-34 description uses a different forbidden-symbol
presentation from the 1993 transition-table treatment; the explicit Boolean
lookup above fixes the convention relevant to CSF.  This source reinforces
that “elementary rule becomes a shift on its reachable subshift” is an
established CA analysis pattern.

### Fukś (2003)

Henryk Fukś,
[*Sequences of Preimages in Elementary Cellular Automata*](https://doi.org/10.25088/ComplexSystems.14.1.29),
**Complex Systems 14** (2003), 29--43.
[Primary full text](https://content.wolfram.com/uploads/sites/13/2023/02/14-1-2.pdf)

Fukś studies exact preimage sequences for elementary cellular automata and
includes Rule 34 in the explicit preimage tables.  The paper does not state
CSF's finite-ring gap polynomial, and the table concerns finite blocks rather
than the precise periodic all-target fibres here.  It nevertheless makes
generic Rule-34 preimage enumeration an occupied subject, so a new scout must
earn value from its q-ary pullback rather than from the fact that Rule-34
preimages can be counted.

**Owner disposition for the temporal axis:** `DIRECT_OWNER`.

## 3. Hard-core cycles, transfer matrices, and necklaces

### Independent sets and Lucas numbers

Helmut Prodinger and Robert F. Tichy,
[*Fibonacci Numbers of Graphs*](https://doi.org/10.1080/00150517.1982.12430021),
**The Fibonacci Quarterly 20** (1982), 16--21.
[Primary issue record](https://www.fq.math.ca/20-1.html)

This line treats graph independent sets as Fibonacci numbers of graphs; the
cycle count `|I_n|=L_n` is a standard result subsequently cited under this
source.  In CSF the refined coefficient

```text
n/(n-r) binom(n-r,r)
```

is also the elementary labelled-cycle independent-set count.  Both it and the
two-state transfer recurrence for `A_n(x)` receive zero contribution credit.

### Cyclic construction and forbidden words

P. Flajolet and M. Soria,
[*The Cycle Construction*](https://doi.org/10.1137/0404006),
**SIAM Journal on Discrete Mathematics 4** (1991), 58--60, gives the standard
cycle generating-function construction.

Anne E. Edlin and Doron Zeilberger,
[*The Goulden--Jackson Cluster Method for Cyclic Words*](https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/cgj.html),
**Advances in Applied Mathematics 25** (2000), 228--232, adapts forbidden-word
enumeration explicitly to cyclic words.

Richard P. Stanley,
[*Ordered Structures and Partitions*](https://doi.org/10.1090/MEMO/0119),
**Memoirs of the American Mathematical Society 119** (1972), develops the
foundational generating-function theory of order-reversing maps from finite
posets to chains.  CSF's gap choice `1<=j<=ell-1` is only a product of bounded
chains (a degenerate P-partition-type enumerator), not a new poset theorem.

These sources are broader than the single no-`11` language, but they own the
cycle/necklace and forbidden-pattern toolkits.  Once CSF's recurrent set is
known to be `I_n`, the following are zero-credit corollaries:

- cyclic hard-core words and their Lucas census;
- rotation orbits and constrained necklaces;
- Möbius extraction of exact periods;
- the finite-map zeta product;
- transfer-matrix evaluation of `A_n(x)` and `A_n(-1)`.

No direct primary source was located in the bounded search for the particular
finite-ring polynomial

```text
P_c(x)=product_j(x+...+x^(ell_j-1))
```

as a labelled Rule-34 target fibre.  That non-hit is not a novelty finding.
The product itself follows from the standard run decomposition between
isolated target ones and is methodologically very thin.

## 4. The q-ary successor-mask front

The exact first fibre

```text
(q-1)^(n-r)+epsilon_(n,q)(-1)^(n-r)
```

is the trace/character count for closed walks in the complete directed
alphabet graph in which the single transition `a -> a+1` is marked.  The
proof is a one-line additive-character diagonalization of a circulant
transition matrix.  Searches were made for primary work using combinations
of:

```text
cyclic q-ary word directed succession statistic
modular successor adjacencies in words
cyclic words prescribed transitions transfer matrix
successor edge mask finite cellular automaton
q-ary neighbour successor indicator feedback
```

The closest opened items concerned successions in permutations, general
cyclic forbidden-word methods, staircase words, or unrestricted transition
statistics.  None of the inspected primary records stated the literal map or
the exact mask-resolved formula used here.

This bounded non-hit has limited value.  Character orthogonality, trace of a
weighted adjacency matrix, and cyclic edge-statistic enumeration are
classical techniques; they receive no novelty credit.  The only residual is
their particularly compact evaluation for this literal successor relation and
its composition with the Rule-34 target gaps.

## 5. Internal P1--P161 collision audit

The paper-directory roster, sequence anchor, prior collision reports, and the
nearest manuscripts were searched by carrier and proof engine.

| internal item | occupied surface | CSF subtraction |
|---|---|---|
| P57, uniform-cylinder minorization CA | cellular-automaton lane | Broad only, but confirms CA is an established portfolio class. |
| P63, rank-one XOR inverse radius | local binary CA inverse questions | Different additive map, yet generic CA inverse packaging is occupied. |
| P66, hard-core sofic entropy dependence | hard-core/no-adjacency symbolic system | CSF gets no credit from presenting `I_n` as a hard-core subshift. |
| P77, digit-weight automatic towers | nilpotent CA/automatic tower | Different literal system; temporal-CA mechanisms are already screened tightly. |
| P90, Rule-184 particle periodic zeta | finite-ring ECA, no-`11`/no-`00` cores, Lucas counts, Möbius periods, zeta | Strong architecture collision. P90 explicitly subtracts those same hard-core/necklace consequences and earns value only from its particle-resolved clock. CSF has no analogous residual clock. |
| P117, odd-run reversal cyclic words | finite binary cyclic recurrence and zeta | Different local rule, but cyclic-word functional-graph packaging is occupied. |
| P131, Euclidean quotient queues | recurrent rotation, compositions, necklaces, exact fibres | Different carrier, yet rotation/necklace orbit extraction is explicitly zero-credit there too. |
| P138, palindromic-prefix XOR feedback | nonlinear indicator feedback followed by binary dynamics and exact inverse | Not conjugate, but it occupies the closest indicator-feedback narrative. |

No P1--P161 note was found with exactly the q-ary successor relation (1).
That internal non-hit does not overcome the direct external ownership of the
tail or the current-batch collision below.

## 6. Same-batch CEF collision

Current P164/CEF studies

```text
T_q(w)_i=1{w_i=w_(i+1)}
```

at dyadic lengths.  Its architecture is nearly identical:

```text
q-ary local adjacency comparison
    -> binary mask after one step
    -> named elementary/additive CA tail
    -> exact mask multiplicity
    -> weighted all-target inverse formula.
```

CEF's binary tail is classically owned Rule 102/153, and its repeated-root
code theory is explicitly subtracted.  It nevertheless survived a hostile
re-entry gate because the remaining literal interface gives a sharp `n+1`
depth clock, full depth CDF, a nontrivial image staircase, a sharp last shell,
and two evaluated target-class spectra at different times.

CSF is weaker at precisely the portfolio discriminant:

- its post-front height is the direct one-step Rule-34 collapse;
- its stable dynamics is only rotation;
- its “all-time” fibre is time-independent after time two;
- its periods and zeta are hard-core necklace data;
- both residual fibre formulas arise by weighting the same binary mask/run
  decomposition.

Promoting CSF beside CEF would repeat the same q-ary-comparison-to-binary-CA
story with a shorter, directly owned temporal law.

**Same-batch disposition:** `FATAL_PORTFOLIO_COLLISION_WITH_CEF`.

## 7. Search boundary and final owner/value decision

The audit used only primary articles or official journal/author records to
assign ownership.  Secondary search snippets were used only for routing and
not as evidence.  Search families covered:

- Rule 34 / Rule 2 shift, subshift, forbidden blocks, and preimages;
- cyclic ECA state graphs and finite periodic boundaries;
- hard-core cycle independent sets and Lucas counts;
- constrained necklaces, cyclic forbidden words, and transfer matrices;
- P-partitions and products of bounded chain choices;
- modular successor adjacencies and q-ary cyclic word statistics;
- the P1--P161 title/keyword roster and current CEF source/review record.

The search does **not** establish that nobody has written the exact q-ary map,
nor does it authorize novelty or priority language.

```text
BINARY TAIL OWNER      DIRECT HIT (Braga et al.; reinforced by Meunier/Fuks)
HARD-CORE/NECKLACE     CLASSICAL ZERO CREDIT
Q-ARY FRONT            NO DIRECT HIT FOUND IN BOUNDED SEARCH
GAP-WEIGHTED FIBRE     NO DIRECT HIT FOUND IN BOUNDED SEARCH
INTERNAL P1--P161      NO EXACT LITERAL HIT; MULTIPLE ENGINE COLLISIONS
SAME-BATCH CEF         FATAL ARCHITECTURE/VALUE COLLISION
OVERALL                FAIL_VALUE_AFTER_SUBTRACTION
EXTERNAL               HOLD_EXTERNAL
```

The safe claim ceiling is purely documentary: “the CSF scout derives an exact
finite-ring q-ary pullback over the already known Rule-34 shift core.”  It is
not paper-sized under the batch threshold and must not be circulated as a new
CA or necklace theorem.
