# Literature Audit — SD-C25

**Search closed:** 2026-08-14  
**Primary field:** Symbolic Dynamics  
**Adjacent fields used for collision control:** unary automata, weighted
automata, linear recurrence sequences  
**Technical-source rule:** primary papers or official publisher/
institutional records only  
**Global priority claim:** not made

## 1. Research question searched

The search tested whether prior work already proves, in substantially the
same form, that the canonical successor–divisor word

\[
        1^{k-1}2
\]

cannot support a fixed finite group/semigroup/automaton or
finite-dimensional weighted response whose exact nonzero support is the
rational primes, and whether this obstruction has already been connected to
the same graph's Fredholm determinant and factorial roof.

Queries covered:

- finite automata over a unary alphabet and arithmetic progressions;
- recognition of primes by finite, pushdown, and bounded-memory automata;
- multiplicity and weighted automata;
- unary weighted automata and linear recurrence sequences;
- Skolem–Mahler–Lech zero sets and corrigenda;
- rational Artin–Mazur zeta functions and periodic-orbit length sets;
- finitely presented symbolic systems;
- growing finite-state realizations and finite-prefix memorization;
- countable computational symbolic systems, pruning, inducing, and
  long-cycle/short-roof noncompactness.

## 2. Verified primary source ledger

### 2.1 Unary automata

**Chrobak 1986.** Marek Chrobak, “Finite automata and unary languages,”
*Theoretical Computer Science* 47, 149–158.

- DOI:
  [10.1016/0304-3975(86)90142-8](https://doi.org/10.1016/0304-3975(86)90142-8)
- Official page:
  [ScienceDirect](https://www.sciencedirect.com/science/article/pii/0304397586901428)
- Use: quantitative unary NFA/DFA normal-form and state-complexity context.
- Boundary: the Paper23 finite-DFA proof is elementary and does not depend
  on the quantitative normal form.

**Chrobak 2003 erratum.** “Errata to: ‘Finite Automata and Unary
Languages’,” *Theoretical Computer Science* 302, 497–498.

- DOI:
  [10.1016/S0304-3975(03)00136-1](https://doi.org/10.1016/S0304-3975(03)00136-1)
- Official page:
  [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0304397503001361)
- Use: mandatory correction record when the quantitative 1986 normal form
  is cited.

**To 2009.** Anthony Widjaja To, “Unary finite automata vs. arithmetic
progressions,” *Information Processing Letters* 109(17), 1010–1014.

- DOI:
  [10.1016/j.ipl.2009.06.005](https://doi.org/10.1016/j.ipl.2009.06.005)
- Official page:
  [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0020019009001896)
- Use: identifies and repairs a subtle error in the arithmetic-progression
  proof associated with Chrobak's normal form.

**Hartmanis–Shank 1968.** Juris Hartmanis and H. Shank, “On the Recognition
of Primes by Automata,” *Journal of the ACM* 15(3), 382–389.

- DOI:
  [10.1145/321466.321470](https://doi.org/10.1145/321466.321470)
- Official institutional record:
  [Cornell eCommons](https://ecommons.cornell.edu/items/a065595f-9181-4c54-833f-dd743aff69e3)
- Use: closest classical prime-recognition collision.  The official abstract
  states that neither the primes nor an infinite subset of primes is
  accepted by a finite or pushdown automaton, while linearly bounded
  automata can accept primes.
- Boundary: Paper23 states its narrower result on the source-derived
  canonical word.

### 2.2 Weighted automata and rational series

**Schützenberger 1961.** Marcel-Paul Schützenberger, “On the definition of a
family of automata,” *Information and Control* 4(2–3), 245–270.

- DOI:
  [10.1016/S0019-9958(61)80020-X](https://doi.org/10.1016/S0019-9958(61)80020-X)
- Official page:
  [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S001999586180020X)
- Use: foundational multiplicity-automata and rational-series context.
- Boundary: Paper23 derives the displayed recurrence directly by
  Cayley–Hamilton.

**Barloy–Fijalkow–Lhote–Mazowiecki 2020.** “A Robust Class of Linear
Recurrence Sequences,” CSL 2020.

- DOI:
  [10.4230/LIPIcs.CSL.2020.9](https://doi.org/10.4230/LIPIcs.CSL.2020.9)
- Official page:
  [Dagstuhl DROPS](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CSL.2020.9)
- Use: modern primary context linking structured weighted automata, rational
  formal series, and LRS.

**Mazowiecki–Puch–Smertnig 2026.** “Pumping-Like Results for Copyless Cost
Register Automata and Polynomially Ambiguous Weighted Automata,” STACS
2026.

- DOI:
  [10.4230/LIPIcs.STACS.2026.67](https://doi.org/10.4230/LIPIcs.STACS.2026.67)
- Official page:
  [Dagstuhl DROPS](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.67)
- Use: current evidence that unary behavior and recurrence methods remain
  active in quantitative automata.
- Boundary: its pumping results are not invoked as Paper23 proofs.

### 2.3 Skolem–Mahler–Lech

**Lech 1953.** Christer Lech, “A note on recurring series,”
*Arkiv för Matematik* 2, 417–421.

- DOI:
  [10.1007/BF02590997](https://doi.org/10.1007/BF02590997)
- Use: primary classical source for the zero-set theorem.

**Bell 2006.** Jason P. Bell, “A generalised Skolem–Mahler–Lech theorem for
affine varieties,” *Journal of the London Mathematical Society* 73(2),
367–379.

- DOI:
  [10.1112/S002461070602268X](https://doi.org/10.1112/S002461070602268X)
- Official page:
  [Cambridge Core](https://www.cambridge.org/core/journals/journal-of-the-london-mathematical-society/article/abs/a-generalised-skolemmahlerlech-theorem-for-affine-varieties/CFB1881CDB67C479CA15E0950C2D37FE)
- Use: its official abstract states the classical characteristic-zero LRS
  zero-set theorem used here.

**Bell 2008 corrigendum.**

- DOI:
  [10.1112/jlms/jdn012](https://doi.org/10.1112/jlms/jdn012)
- Citation: *Journal of the London Mathematical Society* 78, 267–272.
- Use: records the repair to the generalized \(p\)-adic analytic-arc
  argument.
- Boundary: Paper23 uses the classical SML statement, not the corrected
  generalized proof as a candidate-specific theorem.

### 2.4 Direct Symbolic-Dynamics collision

**De Jong 2026.** Huub de Jong, “On sets of periodic orbit lengths in
finitely presented dynamical systems,” *Ergodic Theory and Dynamical
Systems*, First View, 1–33.

- DOI:
  [10.1017/etds.2026.10313](https://doi.org/10.1017/etds.2026.10313)
- Official page:
  [Cambridge Core](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/on-sets-of-periodic-orbit-lengths-in-finitely-presented-dynamical-systems/A4984CCDB44619E0F7894EFF03314324)
- Published online: 15 June 2026.
- Verified claim range: for systems whose logarithmic derivative of the
  Artin–Mazur zeta function is rational, the paper uses SML to classify
  periods; it also classifies least-period sets for finitely presented
  systems.
- Collision consequence: Paper23 cannot claim the first SML obstruction to
  prime period support in Symbolic Dynamics.
- Noncollision boundary: de Jong does not study the particular
  successor–divisor cofactor family, its canonical word
  \(1^{k-1}2\), the finite/growing/countable memory control chain, or the
  Paper21 factorial roof.
- Applicability boundary: the present countable Markov shift is not asserted
  to be compact or finitely presented, and its trace logarithmic derivative
  is not asserted to be rational.  We therefore use de Jong as a direct
  novelty collision for broad period-set language, not as a theorem applied
  to SD-C25.

### 2.5 Fredholm determinant

**Simon 1977.** Barry Simon, “Notes on infinite determinants of Hilbert space
operators,” *Advances in Mathematics* 24(3), 244–273.

- DOI:
  [10.1016/0001-8708(77)90057-3](https://doi.org/10.1016/0001-8708(77)90057-3)
- Use: classical trace-class Fredholm determinant context.
- Boundary: the exact \(\Re s>1/2\) threshold is proved from this graph's
  edge families, not imported from Simon.

## 3. Closest-collision ranking

| Rank | Source | Existing result | Remaining SD-C25 delta |
|---:|---|---|---|
| 1 | de Jong 2026 | SML applied directly to dynamical period sets; least-period classification for finitely presented systems | exact successor–divisor word and full same-object closure chain |
| 2 | Hartmanis–Shank 1968 | finite/pushdown automata cannot accept primes or an infinite prime subset | graph-derived marked cycle, weighted response, Fredholm and roof consequences |
| 3 | Chrobak 1986/2003 and To 2009 | unary automata and arithmetic-progression normal forms | cofactor origin and factorial-roof ledger |
| 4 | Schützenberger and modern weighted automata | fixed linear representations/rational-series/LRS machinery | exact \(A^{k-1}B\) reduction on \(C_k\) |
| 5 | Lech/Bell | LRS zero-set classification | prime-support corollary integrated with the same symbolic determinant |

## 4. Novelty boundary

### Not novel

- unary regular languages being ultimately periodic;
- unary NFA arithmetic-progression normal forms;
- finite-automaton nonrecognition of primes;
- multiplicity automata and rational series;
- Cayley–Hamilton recurrences for matrix coefficients;
- the Skolem–Mahler–Lech theorem;
- SML restrictions on dynamical period sets;
- growing-state realization of arbitrary finite data.

### Defensible contribution

The model-specific contribution is the exact reduction

\[
 C_k
 \longmapsto
 W(C_k)=1^{k-1}2
\]

inside the successor–divisor countable Markov shift, followed by one
same-object closure theorem:

\[
\begin{aligned}
&\text{fixed finite fiber periodicity}\\
&\quad\Longrightarrow
\text{fixed-dimensional SML support rigidity}\\
&\quad\Longrightarrow
\text{growing finite-memory universality}\\
&\quad\Longrightarrow
\text{countable-wrapper pruning/clock dilution}\\
&\quad\Longrightarrow
\text{unchanged factorial roof and graph marker}.
\end{aligned}
\]

This is a synthesis and route-closure result, not a new automata or number
theory theorem.

## 5. Dangerous citation formulations

| Do not write | Safe formulation |
|---|---|
| “Chrobak proved the final unary normal form” | cite Chrobak 1986, the 2003 erratum, and To 2009 together for the corrected quantitative context |
| “Bell 2006 is uncorrected” | record the 2008 corrigendum; invoke only classical SML |
| “SML makes every threshold response periodic” | SML controls exact zero sets and fixed-level sets |
| “Paper23 is the first dynamical SML prime obstruction” | de Jong 2026 is a direct collision |
| “Hartmanis–Shank proves this exact cofactor theorem” | it is a broader classical prime-automata collision; the cofactor reduction is model-specific |
| “Weighted automata cannot recognize primes by any semantics” | claim only exact zero/nonzero support for the displayed fixed linear responses |

## 6. Search limitations

The bounded search found no primary source containing the complete
SD-C25-specific closure chain.  This does not establish global priority.
The workflow's independent cross-model reviewer was unavailable in the
research session; the fallback was a primary-source collision search and a
hostile claim-language audit.  No unresolved citation enters
[references.bib](references.bib).

## 7. Literature verdict

The theorem package is publishable as a scoped negative result if its title,
abstract, introduction, and figure foreground the ordered cofactor family
rather than presenting the classical unary/SML ingredients as new.
De Jong 2026 must be cited prominently.  The novelty wording is
search-bounded and model-specific.
