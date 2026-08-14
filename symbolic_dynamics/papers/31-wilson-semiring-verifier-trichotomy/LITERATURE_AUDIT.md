# Literature audit — Paper 31 / SD-C33

## 1. Search scope and claim discipline

Searches were completed on 2026-08-14.  The bounded query families were:

- `Wilson congruence countable Markov shift Fredholm determinant prime cycles`;
- `factorial modulo n symbolic dynamics transfer operator`;
- `full shift semiring alphabet sum product prime`;
- `commutative semiring natural numbers UFD transported addition`;
- `weighted cyclic block direct sum compact operator`;
- `state expansion first return marker zeta`;
- `primality verifier symbolic dynamics transient pruning`;
- 2024--2026 freshness variants of those queries.

Primary papers, publisher records, author/institution repositories, and arXiv
records were preferred.  A source entered the core matrix only if it directly
addressed symbolic zeta/determinant identities, countable Markov dynamics,
computation in symbolic systems, prime recognition, semirings of dynamical
objects, state expansion/return time, or Hilbert-space determinant ownership.
Works using “prime” only to mean a primitive graph walk were excluded from
supporting the arithmetic claim.

The search cannot prove that no equivalent construction exists.  Accordingly,
the manuscript uses a search-bounded statement: within these searches, no
external source was found that combines the specific Paper-30 bare-clone
separation, matched-semiring transport, Wilson graph-step product, and
whole-operator compactness trichotomy.  The nearest collisions are Papers 19
and 20 of this project, and the manuscript names them explicitly instead of
claiming a literature vacuum.

## 2. Verified primary-source matrix

| Source | Primary contribution used | Boundary imposed on Paper 31 |
|---|---|---|
| Bowen and Lanford, “Zeta Functions of Restrictions of the Shift Transformation” (1970), DOI `10.1090/pspum/014/9985` | finite shift cycle/zeta/determinant identity | converting a finite cycle census to a determinant is classical; the countable non-trace-class limit needs a separate proof |
| Hartmanis and Shank, “On the Recognition of Primes by Automata” (1968), DOI `10.1145/321466.321470` | classical automata-theoretic prime-recognition boundary | “an automaton recognizes primes” is not a novelty claim |
| Shepherdson and Sturgis, “Computability of Recursive Functions” (1963), DOI `10.1145/321160.321170` | register-style realization of recursive computation | compiling a total decider into a graph is computation, not arithmetic selectivity |
| Parry and Sullivan, “A Topological Invariant of Flows on 1-Dimensional Spaces” (1975), DOI `10.1016/0040-9383(75)90012-9` | state expansion and flow-equivalence lineage | graph subdivision and first-return time cannot be silently identified |
| Kůrka, “On Topological Dynamics of Turing Machines” (1997), DOI `10.1016/S0304-3975(96)00025-4` | computation embedded in topological dynamics | computational symbolic dynamics is established machinery |
| Salo and Törmä, “Category Theory of Symbolic Dynamics” (2015), DOI `10.1016/j.tcs.2014.10.023` | categorical framework for subshifts and block maps | `boxplus` is called alphabet-sum, not a categorical coproduct |
| Kopra, “Direct Prime Subshifts and Canonical Covers” (2023), DOI `10.1017/etds.2022.33` | direct-product primeness in symbolic dynamics | prime-cardinality full shifts and product indecomposability are not new here |
| Naquin and Gadouleau, “Factorisation in the Semiring of Finite Dynamical Systems” (2024), DOI `10.1016/j.tcs.2024.114509` | addition/product semirings of finite dynamics | semiring language for dynamical systems is established; Paper 31's claim is the scoped obstruction chain |
| Gadouleau and Johnson, “Semirings of Formal Sums and Injective Partial Transformations” (2026 preprint), arXiv:`2603.26508` | current formal-sum/partial-transformation semiring work | freshness collision only; it does not supply the Wilson/Fredholm trichotomy |
| Schlage-Puchta, “Alternating State Complexity of the Set of Primes and Squarefree Integers” (2025), DOI `10.1007/s00013-024-02075-w` | state-complexity lower bounds for prime and squarefree languages | reinforces the nontrivial state cost of prime recognition; it does not prove the operator obstruction |
| Gurevich and Savchenko, “Thermodynamic Formalism for Countable Symbolic Markov Chains” (1998), DOI `10.1070/RM1998v053n02ABEH000017` | thermodynamic formalism for countable symbolic chains | Paper 31 names a specific vertex adjacency and does not invoke an unrestricted Ruelle theorem |
| Sarig, “Thermodynamic Formalism for Countable Markov Shifts” (1999), DOI `10.1017/S0143385799146820` | countable-state thermodynamic formalism | recurrence formalism does not by itself confer trace-class determinant ownership |
| Hong, “The Zeta Functions of Renewal Systems” (2011), DOI `10.1017/S0143385710000015` | zeta behavior of renewal/code systems | flexible formal code products are weaker than Hilbert-space Fredholm determinants |
| Simon, “Notes on Infinite Determinants of Hilbert Space Operators” (1977), DOI `10.1016/0001-8708(77)90057-3` | infinite determinants for trace-class perturbations | fixes the ordinary determinant ownership boundary used in the paper |

All DOI-bearing bibliography entries retain their DOI.  The Gadouleau--Johnson
item is cited only as a 2026 preprint and only to bound the freshness claim; no
theorem in Paper 31 depends on it.

## 3. The closest collisions are internal

### Paper 19: transient semiring verifier

Paper 19 already constructs a source-local semiring verifier that can be made
trace class and have the exact prime Euler determinant.  It also proves that
the verifier DAG lies outside every closed walk and prunes to the accepted
prime-loop diagonal.  Paper 31 therefore cannot claim transient pruning as a
new phenomenon.

### Paper 20: recurrent verifier clock dilution

Paper 20 already proves:

1. the compactness criterion for direct sums of weighted cycles;
2. the entropy-clock dilution obstruction;
3. failure of all finite Schatten classes in the long-cycle regime;
4. first-return marker change;
5. the universal padded-total-decider control.

Paper 31 uses these results only after deriving a new concrete bridge from
Paper 30.  Its Wilson specialization is included to make the inference
self-contained, not to reclaim the abstract theorems.

## 4. Defensible novelty boundary

The elementary components have low novelty in isolation:

- full-shift alphabet sum/product realizes \(\mathbb N_0\);
- ordinary polynomial addition does not preserve the prime-exponent monomial
  encoding;
- Wilson's congruence recognizes primes;
- state-expanded computation can be encoded symbolically;
- disjoint long cycles dilute a fixed roof budget.

The defensible contribution is the exact project-specific bridge:

1. the nonmultiplicative source enrichment requested by Paper 30 really does
   invalidate that paper's bare UFD clone;
2. additive rigidity identifies the separating axiom;
3. the matched semiring clone gives the remaining naturality firewall;
4. Wilson supplies a table-free exact primitive ledger;
5. the first such terminal congruence witness immediately collapses into the
   Paper 19/20 pruning-or-dilution alternatives.

| Component claim | Novelty assessment | Safe positioning |
|---|---|---|
| full-shift semiring skeleton | low | setup, not contribution |
| bare polynomial-UFD addition failure | elementary algebra; medium relevance inside this series | exact closure of Paper 30's stated loophole |
| matched semiring transport | low as functoriality | mandatory no-go firewall |
| Wilson stationary prime-cycle grammar | low-to-medium, model-specific | exact witness, not a new primality test |
| noncompactness, return, and pruning | low externally and already internal | inherited machinery, specialized transparently |
| combined Paper-30-to-Paper-20 trichotomy | medium and defensible | main contribution of the negative closure paper |

Overall novelty assessment: **5/10**.  The recommendation is to publish or
archive Paper 31 only as a compact negative closure paper.  It should not be
positioned as a new primality algorithm, a new general compactness theorem, or
progress on the critical-line spectral problem.

## 5. Citation and integrity notes

- The manuscript proves Wilson's congruence implication directly, so it does
  not rely on an unverifiable historical attribution.
- Classical sources older than ten years remain because they are the original
  works defining the relevant boundaries.
- No target-zero paper is cited because no zero data or critical-line fitting
  enters the research question.
- No citation is asked to support an absence claim.  The novelty sentence is
  explicitly bounded by the recorded search date and query families.
- No external cross-model novelty review was run.  The user explicitly waived
  review loops, and the callable cross-model interface was unavailable during
  the research stage.
