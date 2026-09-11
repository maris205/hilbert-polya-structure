# Owner-search log — replacement adaptive maps

**Search date:** 2026-09-02 UTC  
**External state:** `HOLD_EXTERNAL`  
**Purpose:** bounded owner subtraction and collision control, not a novelty
claim

## Search protocol

The historical P1--P161 occupancy and kill ledgers were read before external
search.  The active P162--P166 scout ledgers in the root,
`arithmetic_algebra`, `geometry_group`, `graph_set`, `stochastic_spatial`, and
`word_combinatorial` lanes were then checked for the literal carrier, update,
state statistic, and proof engine.  External queries were made early for the
three strongest mechanism families rather than after ranking:

```text
"state-dependent rotation" finite words Hamming weight dynamics
cyclic word rotate by number of transitions normalize first symbol dynamics
finite field words quotient global translation rotation functional graph
"adaptive rotation" binary words dynamical system
"rotate by its Hamming weight" binary word
"rotation by the Hamming weight" word
functional graph cyclic words number of runs rotation
necklace rotation step depends on weight cyclic word
q-ary cyclic words fixed content
zero-sum finite-field words fixed rotation
single parity-check code weight enumerators
"cyclic derivative" word finite field rotation
"difference sequence" necklaces finite field cyclic words
q-ary necklaces modulo alphabet translation
cyclic words quotient by global additive constant finite field
inventory loops counting sequences iteration
Černý automaton greedy synchronizing subset rank reduction
"nonlinear feedback shift register" cycle structure exact periods
```

Exact-phrase searches for the `AQN` update and its conjunction of cyclic
difference, state-dependent rotation, and first-symbol normalization produced
no matching mathematical dynamics in this bounded search.  That is only a
non-hit, not evidence of novelty or owner absence.

## Candidate `AQN`: source subtraction

The following results are inputs and receive zero credit.

| known neighbourhood | source | subtraction from any future claim |
|---|---|---|
| rotation controlled by Hamming weight | P. Hoyer and R. Spalek, *Quantum Fan-out is Powerful*, Theory of Computing 1 (2005), especially its rotation-by-Hamming-weight circuit ([article](https://doi.org/10.4086/toc.2005.v001a005)) | the idea that a state statistic can choose a rotation is not new |
| data-dependent rotations in cryptography | A. Biryukov, *Case studies in symmetric key cryptography*, discussion of RC5/RC6/MARS rotations whose amount depends on data ([repository copy](https://research.tue.nl/files/1987507/200512844.pdf)) | “adaptive” or data-dependent rotation alone is not a contribution |
| necklaces and cyclic orbits | classical Moreau/Burnside necklace enumeration; F. J. MacWilliams, “A theorem on the distribution of weights in a systematic code,” Bell System Technical Journal 44 (1965), 79--94 ([DOI](https://doi.org/10.1002/j.1538-7305.1965.tb01664.x)) | ordinary orbit, fixed-point, and Möbius inversion machinery is zero credit |
| zero-sum/single-parity-check words | standard single-parity-check code and its elementary weight enumerator; the general dual-weight identity is covered by MacWilliams above | formula for the number of zero-sum words with a prescribed support is zero credit |
| functional graphs | standard finite-map terminology and cycle/tree decomposition | calling the graph a decorated collection of cycles is not itself a theorem |

The residual package is narrower: for

```text
T_c(w)=R^(c k(w))w-w_0 1,
k(w)=|supp Delta(w)|,
```

it is the simultaneous derivation of the state-selected image hyperplane,
depth-one decorated cycles, all-time target fibres and their target-dependent
zero-count polynomial, exact fixed/cycle census across change strata, and
marked recovery of `c`.  No exact external owner for that literal conjunction
was found.  A specialist owner gate is still mandatory because the proof
reduces the recurrent part to a disjoint union of classical necklace actions.

## Internal collision audit for `AQN`

| occupied system | closest shared feature | decisive separation |
|---|---|---|
| P96 circle-subset expansion | finite cyclic carrier | P96 changes a subset by geometric expansion; it has neither word differences nor state-frozen rotations |
| P98 equal-block-sum map | finite-field words and a noninvertible image | P98 is a fixed linear operator analyzed by repeated-root algebra; `AQN` is state-dependent and quotients global translations |
| P99 unipotent sublattice action | exact cycle census for a finite action | P99 is bijective and has neither depth-one leaves nor target fibres |
| P139 Lyndon selector | words and rotations | P139 selects factor starts and standardizes; `AQN` selects no coordinate or subword |
| current `RFW/CNG/USP/BQC` | exact finite dynamics | their engines are respectively rational-window singularities, gcd erosion, Schur complementation, and quotient/coalescence |

No internal proof-engine transfer was detected.  The risk is instead
external/classical reducibility: a referee may regard the residual as an
elementary quotient wrapper around necklaces.  This is why the gate is amber.

## Owner and collision decisions for the 25 controls

| IDs | nearest owner or occupied engine | consequence |
|---|---|---|
| `HWR` | Hoyer--Spalek Hamming-weight rotation and cryptographic data-dependent rotations | direct mechanism owner; singleton fibres |
| `DCR` | exactly the recurrent difference action inside `AQN` | dominated action-only subproblem |
| `DAR,CCR,SVT,BRT,EGR,PFC,EIC,PDR,PCR,ISR,WCR,MRR,CLT` | dihedral/cyclic relabelling, Burnside, group conjugation, inverse-semigroup action, coordinate involution, or rank-frozen permutation | invertible action only; no target-dependent inverse axis; `SVT` also approaches P96 and `PFC` approaches P154 |
| `IDH` | O. M. Cain and S. T. Enin, *Inventory Loops (i.e. Counting Sequences) have Pre-period 2 max S1 + 60* ([arXiv:2004.00209](https://arxiv.org/abs/2004.00209)) | direct counting/inventory iteration neighbourhood and no uniform spine |
| `PIS,OCL,BAS` | functional-digraph statistics and P135 component/partition summaries | finite signatures only; no all-parameter temporal theorem |
| `RAC` | finite transformation semigroups and rank decomposition | engineered one-drop scheduler, thin residual |
| `CNY,PAS` | synchronizing automata, subset synchronization, and reset thresholds; see M. V. Volkov, *Synchronization of finite automata*, Russian Math. Surveys 77 (2022), 819--891 ([DOI](https://doi.org/10.4213/rm10005e)), and D. Ananichev et al., *Approximation of Reset Thresholds with Greedy Algorithms* ([DOI](https://doi.org/10.3233/FI-2016-1357)) | direct mature owner for reset/greedy subset dynamics; the parity scheduler is artificial |
| `MFS` | global-majority dynamics and occupied P132 majority mechanism | internal owner collision |
| `NFS` | J. Mykkeltveit, M. Siu, and P. Tong, *On the cycle structure of some nonlinear shift register sequences*, Information and Control 43 (1979), 202--215 ([DOI](https://doi.org/10.1016/S0019-9958(79)90708-3)); H. Hu and G. Gong, time-varying NFSR periods ([DOI](https://doi.org/10.1142/S0129054111008738)) | literal nonlinear feedback-shift-register territory; small pattern is not a residual theorem |
| `ACA` | state-switched cellular automata, plus occupied P82/P90 cellular/Boolean mechanisms | internal owner proximity and unstable signatures |

## Search conclusion

```text
AQN  NO_EXACT_OWNER_HIT_IN_BOUNDED_SEARCH
AQN  CLASSICAL_ACTION_COMPONENTS_FULLY_SUBTRACTED
AQN  SELECT_AMBER_SPECIALIST_OWNER_GATE
all 25 controls  KILL
HOLD_EXTERNAL
```

The negative exact search must not be quoted as novelty.  Before any paper is
allocated, an independent specialist should search combinatorics on words,
necklace actions on additive quotients, finite dynamical systems over fields,
and coding-theoretic orbit enumerators using the exact displayed update.
