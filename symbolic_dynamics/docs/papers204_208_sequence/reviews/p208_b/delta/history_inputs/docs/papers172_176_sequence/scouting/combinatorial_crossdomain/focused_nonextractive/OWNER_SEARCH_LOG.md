# Primary-owner search log — focused non-extractive lane

**Search date:** 2026-09-03 UTC  
**Lifecycle:** `HOLD_EXTERNAL`  
**Rule:** every search is bounded and terminology-dependent.  A non-hit is
not novelty, priority, clearance, or permission to circulate.

## 1. Search protocol

The repository inventory and collision materials through P171 were searched
before external queries.  Exact phrases and structural paraphrases included:

```text
permutation map rank of pi_i plus i iteration
"pi(i)+i" permutation sorting map
permutation points sort by diagonal x+y rank
"rotate" word "frequency" first letter dynamical system
"number of occurrences" "rotate" word combinatorics
word rotation frequency dynamical system first symbol
"rotate by" "frequency of the first" word
"number of occurrences of the first" rotate string
"multiplicity of its first" cyclic word rotation
"frequency-dependent rotation" binary word
"i+c_i" functional graph composition cyclic map
"x+a_x" functional graph cyclic group
map i to i plus c_i modulo n composition dynamics
pointed necklace dynamical system rotation binary word
deterministic walk on cycle vertex-dependent step binary coloring
"Hamming weight rotation" binary strings cyclic shift
```

No result located in this bounded pass states the FCR literal

```text
w -> rotate w by the multiplicity of w_0
```

or its conjunction of the sharp clock, complete period inventory, labelled
fibres, and fixed census.  That sentence records only the search outcome; it
is not evidence of novelty.

## 2. Primary sources and exact subtraction

| source | what it owns | consequence here |
|---|---|---|
| P. Høyer and R. Špalek, *Quantum Fan-out is Powerful*, [arXiv:quant-ph/0208043](https://arxiv.org/abs/quant-ph/0208043), *Theory of Computing* 1 (2005), 81--103, [DOI 10.4086/toc.2005.v001a005](https://doi.org/10.4086/toc.2005.v001a005) | Section 3.2 constructs the one-qubit phase rotation `R_z(phi |x|)`, whose angle is controlled by Hamming weight; it is not a cyclic coordinate shift. | The general phrase “Hamming-weight-controlled rotation” receives zero credit, but this source is not a literal owner of either coordinate branch of FCR. |
| O. Grošek and V. Hromada, *Rotation-Equivalence Classes of Binary Vectors*, *Tatra Mountains Mathematical Publications* 67 (2016), 93--98, [DOI 10.1515/tmmp-2016-0033](https://doi.org/10.1515/tmmp-2016-0033) | coordinate-rotation classes at fixed Hamming weight, feasible class sizes, and their enumeration | fixed-weight rotation-class structure and enumeration receive zero credit; the source does not define the adaptive first-symbol gluing or its functional graph |
| A. Gupta et al., *Rotating Binaries*, *AppliedMath* 2 (2022), 104--117, [DOI 10.3390/appliedmath2010005](https://doi.org/10.3390/appliedmath2010005) | literal circular coordinate shifts, rotation distance/equivalence, Hamming weight, and complement symmetry | these ordinary coordinate-rotation ingredients receive zero credit; the source does not define the adaptive first-symbol gluing or its functional graph |
| I. Heckenberger and J. Sawada, *A Pascal-like Bound for the Number of Necklaces with Fixed Density*, [arXiv:1801.09516](https://arxiv.org/abs/1801.09516) | binary and `q`-ary necklaces/Lyndon words with fixed density/content | fixed-content necklace language and enumeration are zero credit; the source does not state the adaptive pointed update located in the bounded check |
| R. Meštrović, *Different classes of binary necklaces and a combinatorial method for their enumerations*, [arXiv:1804.00992](https://arxiv.org/abs/1804.00992) | Moreau's aperiodic-necklace count and the binary MacMahon/Witt formula | ordinary primitive-word and Möbius necklace counts, including the ingredient in the FCR fixed census, are zero credit |

Generic functional-graph decomposition, orientations of an undirected cycle,
binomial conditioning at two labelled positions, and Möbius inversion are
also zero-credit tools whether or not a paper is cited for them.

## 3. Internal primary owners

### P117 — odd-run reversal

P117 uses the same literal carrier of labelled cyclic binary words, but flips
all bits in odd maximal adjacent runs.  It changes content, evolves boundary
parities, and has only fixed/two-periodic recurrence.  FCR preserves content
and moves only the pointer; its runs occur on the `+k` generator components,
which are generally not adjacent runs of the displayed word.  No P117 proof
transfers beyond generic cyclic-word/run vocabulary.  That vocabulary is
nevertheless zero credit.

### P166 — Hamming-weight diagonal translation

This is the decisive near collision.  P166 acts on `(Z/nZ)^n` by

```text
x -> x + wt(x) 1.
```

On a diagonal-translation orbit with symbol histogram `c`, its phase map is
`j -> j+c_j`.  FCR, on a coordinate-rotation orbit, also produces a phase
map of this form: `j -> j+a_j`, where `a_j` is the global multiplicity of the
binary letter at the pointer.  The shared phase-map reduction, generic finite
graph language, sharp value `n-2`, and indicator-style inverse presentation
are all zero contribution.

The exact difference is not cosmetic.  P166 has `sum_j c_j=n`; mass
exhaustion implies at most one nontrivial recurrent cycle and permits every
period `1,...,n`.  FCR's profile takes only the two values `k,n-k` and need
not sum to `n`; its proof instead orients `gcd(k,d)` disjoint `+/-k` Cayley
cycles.  It may have several recurrent components, and its possible periods
are only `1`, `2`, and proper divisors of `n`.  P166's target sources are
diagonal alphabet translates selected by histogram equations and can have
growing fibre size; FCR has exactly two labelled inverse rotations and fibre
sizes only `0/1/2`.  Therefore P166 does not directly imply the retained
residual, but it caps FCR at amber.

### P162--P166 adaptive-rotation scouts

The killed `HWR` control rotates a binary word by its frozen Hamming weight;
it is exactly the invertible branch owner already identified above.  `DCR`
rotates by transition count, and the stochastic `MCR` samples a site and
rotates by its colour multiplicity.  These establish that data-dependent
rotation is a heavily occupied mechanism.  FCR survives only because the
deterministic moving pointer makes the map noninvertible and supplies the
component clock and target fibres; none of the generic rotation idea is a
contribution.

## 4. Other focused candidates

The value-index stable reranker received exact-phrase searches for
`rank(pi_i+i)` and diagonal sorting.  No exact hit was located, but it was
killed because its sharp clock and target atlas remain open, not because of
the non-hit.  The minimum-ordered matching cross was not sent to an external
novelty gate: its restricted-growth encoding proves an internal collision
with P169, which is already fatal.

## 5. Owner verdict and kill switches

```text
FCR  NO_EXACT_EXTERNAL_OWNER_HIT_IN_BOUNDED_SEARCH
FCR  AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL
VIS  KILL_UNCLOSED_CLOCK_SCORE_RERANK
MOC  KILL_INTERNAL_P169_PAIR_SLICE
```

FCR changes immediately to `KILL` if a source is found for the exact adaptive
first-symbol map, if it is literally conjugate to a P166 subsystem, or if the
`+/-k` component theorem is shown to be a formal specialization of P166's
mass-exhaustion theorem.  No external action was taken or authorized.
