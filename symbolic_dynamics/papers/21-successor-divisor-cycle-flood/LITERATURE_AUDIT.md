# Literature Audit — SD-C23

**Search date:** 2026-08-14
**Scope:** symbolic zeta functions, countable Markov shifts, infinite weighted
graph determinants, and arithmetic divisor graphs
**Priority status:** search-bounded; no absolute priority claim

## 1. Search protocol

Queries covered:

- successor-divisor graph;
- directed graph \(d\mid n+1\);
- shifted divisor directed graph;
- divisor graph plus successor edge;
- countable Markov shift arithmetic divisor graph;
- weighted infinite graph Fredholm determinant;
- trace-class arithmetic adjacency;
- divisor graph and divisor-successor work dated 2024–2026.

Sources were checked through publisher pages, DOI metadata, MathNet, arXiv,
AMS, SIAM, and Cambridge.  The search found no paper using the exact edge rule

\[
 n\to d\iff d\mid n+1,\quad d\ge2
\]

as a countable Markov shift with the \(2r-1\) confinement theorem or the sharp
\(\mathcal S_1\) threshold proved here.  This is evidence from a bounded
search, not a proof of priority.

## 2. Symbolic zeta foundations

Artin and Mazur introduced the periodic-point zeta framework for dynamical
systems.  Bowen and Lanford established the rational zeta/determinant
paradigm for restrictions of finite shifts.  These works supply the
primitive/repetition language but concern compact or finite-type settings.

Gurevich and Savchenko developed generating functions and dynamic zeta
factorizations for countable symbolic Markov chains.  Sarig established a
thermodynamic formalism for countable Markov shifts, including pressure and
recurrence conditions for Ruelle–Perron–Frobenius theory.  SD-C23 belongs to
the countable Markov-shift setting, but its \(\ell^2\) weighted vertex
adjacency is not presented as Sarig's function-space Ruelle operator.

## 3. Infinite determinants

Simon supplies the trace-ideal and Fredholm determinant facts used after
trace class has been proved.  The candidate-specific work is the sharp
row-nuclear decomposition and superdiagonal necessity argument.

Deitmar extends Ihara zeta functions to infinite weighted graphs of finite
total weight and obtains Fredholm determinant formulas.  That setting is
nearby in analytic technology but different in object: Ihara zeta functions
use nonbacktracking graph data, while SD-C23 freezes a directed
vertex-adjacency determinant on a countable Markov grammar.

## 4. Arithmetic graph collisions

Phunphayap, Pongsriiam, and Noppakaew define directed integer graphs using
values of arithmetic functions on multiples.  Their arrows are not shifted
factorization arrows and they do not study the present determinant.

McNew studies finite ordinary divisor graphs on \([1,n]\), with edges when
one vertex divides the other, in connection with permutation cycle covers.
That graph is finite, undirected before the cycle-cover orientation, and
includes self-loops for fixed points.

Perucca, Seuré, and Wolff study finite residue graphs with additive edges
\(a\to a+1\) and multiplicative edges \(a\to ab\bmod n\).  The additive and
multiplicative vocabulary is superficially close, but the vertex set,
transition rule, and cycle problem differ.

Two 2026 preprints were checked as hostile collisions.  Davis studies
forbidden subgraphs in ordinary divisor graphs.  Li uses the phrase
“divisor-successor graph” for coalescence under \(n\mapsto n+\tau(n)\).
Neither uses \(d\mid n+1\) as the edge relation of a countable Markov shift.

## 5. Positioning table

| Source family | Shared ingredient | Difference from SD-C23 |
|---|---|---|
| Artin–Mazur / Bowen–Lanford | periodic orbit zeta and repetitions | finite/compact framework; no successor-divisor graph |
| Gurevich–Savchenko / Sarig | countable symbolic Markov chains | general theory; no candidate-specific confinement or nuclear threshold |
| Simon | trace-class determinants | standard functional analysis; no arithmetic graph |
| Deitmar | Fredholm determinants of infinite weighted graph zeta functions | Ihara/nonbacktracking object |
| ordinary divisor graphs | divisibility on integer vertices | no successor shift and usually finite |
| modular divisibility graphs | additive and multiplicative edges | residue dynamics, not successor factorization |
| \(n+\tau(n)\) coalescence graph | phrase “divisor-successor” | different arithmetic iteration and question |

## 6. Safe novelty sentence

The manuscript uses:

> To our knowledge, based on searches of arXiv, publisher/DOI indexes,
> MathNet, AMS, SIAM, and Cambridge through 2026-08-14, we found no directly
> comparable analysis of the successor–divisor countable Markov shift with
> the \(2r-1\) confinement and sharp trace-class theorem proved here.

It does not use “first,” “only,” or “no prior work” without the search bound.

## 7. Verified reference ledger

1. M. Artin and B. Mazur, “On Periodic Points,” *Annals of Mathematics* 81
   (1965), 82–99. DOI:
   [10.2307/1970384](https://doi.org/10.2307/1970384).
2. R. Bowen and O. E. Lanford III, “Zeta Functions of Restrictions of the
   Shift Transformation,” *Proceedings of Symposia in Pure Mathematics* 14
   (1970), 43–49. DOI:
   [10.1090/pspum/014/9985](https://doi.org/10.1090/pspum/014/9985).
3. B. M. Gurevich and S. V. Savchenko, “Thermodynamic Formalism for
   Countable Symbolic Markov Chains,” *Russian Mathematical Surveys* 53
   (1998), 245–344. DOI:
   [10.1070/RM1998v053n02ABEH000017](https://doi.org/10.1070/RM1998v053n02ABEH000017).
4. O. M. Sarig, “Thermodynamic Formalism for Countable Markov Shifts,”
   *Ergodic Theory and Dynamical Systems* 19 (1999), 1565–1593. DOI:
   [10.1017/S0143385799146820](https://doi.org/10.1017/S0143385799146820).
5. B. Simon, “Notes on Infinite Determinants of Hilbert Space Operators,”
   *Advances in Mathematics* 24 (1977), 244–273. DOI:
   [10.1016/0001-8708(77)90057-3](https://doi.org/10.1016/0001-8708(77)90057-3).
6. A. Deitmar, “Ihara Zeta Functions of Infinite Weighted Graphs,”
   *SIAM Journal on Discrete Mathematics* 29 (2015), 2100–2116. DOI:
   [10.1137/140957925](https://doi.org/10.1137/140957925).
7. P. N. Phunphayap, P. Pongsriiam, and P. Noppakaew, “Directed Graphs of
   Integers with Arcs Determined by an Arithmetic Function,” *Utilitas
   Mathematica* 124 (2025), 101–114. DOI:
   [10.61091/um124-06](https://doi.org/10.61091/um124-06).
8. N. McNew, “Permutations and the Divisor Graph of \([1,n]\),”
   [arXiv:2207.09652](https://arxiv.org/abs/2207.09652).
9. A. Perucca, T. Seuré, and V. Wolff, “Divisibility Graphs and Modular
   Multiplication Tables,” *American Mathematical Monthly* 131 (2024),
   319–334. DOI:
   [10.1080/00029890.2023.2298181](https://doi.org/10.1080/00029890.2023.2298181).
10. D. Davis, “Forbidden Subgraphs in Divisor Graphs and an Erdős
    Divisibility Problem,”
    [arXiv:2604.17613](https://arxiv.org/abs/2604.17613).
11. E. Li, “Square-Annular Dynamics and Coalescence Frontiers for
    \(n+\tau(n)\),”
    [arXiv:2606.17926](https://arxiv.org/abs/2606.17926).

## 8. Citation boundary

Foundational sources justify terminology and standard theorems.  None is
cited as evidence for an SD-C23-specific graph identity.  Candidate-specific
claims are proved in the manuscript.  No reference is used to infer Riemann
analytic continuation for \(D_{\rm SD}\).
