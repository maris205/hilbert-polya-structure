# W01 author-side owner subtraction: oriented ternary fusion

## Decision

**Recommendation:** `KILL_RECOMMEND`.

**External status:** `HOLD_EXTERNAL`.

The proof dossier is mathematically correct, but its periodic-start system is
an injectively labelled presentation of random greedy maximal matching on a
path.  The static support recurrence, bivariate generating function,
cardinality strata, binomial closed form, and parking interpretation are
directly owned in the primary maximal-matching literature.  The stochastic
engine is directly owned by randomized greedy matching and one-dimensional
dimer random sequential adsorption (RSA).  The remaining terminal label code
and the factor \(m!\) for occurrence-distinguished histories are elementary
mechanical consequences of that reduction, not a paper-scale residual.

No paper number should be assigned from the present package.  The proof report
and verifier should be archived as a successful kill-gate exercise.

## Scope and source standard

This is an **author-side subtraction**, not an independent hostile review.  I
read the W01 proof dossier and verifier, the earlier stochastic scouting
records, and primary papers or official publisher records for:

1. enumeration of maximal matchings on paths;
2. randomized greedy matching on fixed graphs;
3. lattice dimer RSA and parking;
4. general graph deposition/RSA; and
5. order/history interpretations of greedy matching.

Search-result non-hits for the exact three rewrite strings are not treated as
novelty evidence.  A literal-symbol non-hit is especially weak here because the
proof gives an exact state/output encoding of an owned graph process.

## 1. Exact reduction of W01 to a path process

Let the periodic input have \(N=3k\) letters.  Give its original positions the
path \(P_N^{\mathrm{vert}}\) with \(N\) vertices and \(N-1\) edges.  The proof
dossier establishes that no periodic interval of length at least \(3\) can
collapse to one symbol.  Consequently:

| W01 object | path-matching object |
|---|---|
| two adjacent singleton letters | an available path edge |
| one fusion | accept that edge and cover/delete its endpoints |
| previously fused letter | an accepted dimer; it never participates again |
| active redex after some steps | edge joining two still-unmatched adjacent vertices |
| terminal state | maximal matching |
| monomer/dimer composition | unmatched vertices/accepted matching edges |
| terminal with \(m\) dimers | maximal matching of size \(m\) |
| terminal length \(\ell\) | \(N-m\) |
| redex history | ordering of the accepted matching edges |

The terminal word is not extra state beyond the matching.  Starting at the
leftmost original position, the next output symbol uniquely says whether the
next block is a monomer or a dimer.  Thus the ternary label map is injective and
has an explicit inverse.  W01 terminal support is therefore in bijection with,
not merely equinumerous to, maximal matchings of the path.

Under the specified stochastic rule, choosing uniformly among current redexes
is exactly choosing uniformly among current available edges, accepting the
chosen edge, and deleting its endpoints.  The labels do not alter any
transition probability.

## 2. Direct owner for the support, strata, recurrence, and GF

### Došlić--Zubac

Tomislav Došlić and Ivana Zubac, *Counting maximal matchings in linear
polymers*, Ars Mathematica Contemporanea 11 (2016), 255--276,
[DOI 10.26493/1855-3974.851.167](https://doi.org/10.26493/1855-3974.851.167).
This is a peer-reviewed primary paper and is the decisive static owner.

Section 3 treats paths explicitly.  In the authors' convention \(P_q\) has
vertices \(v_0,\ldots,v_q\), hence \(q\) edges and \(q+1\) vertices.  They
prove:

- Proposition 3.1: the total number \(\psi_q\) of maximal matchings satisfies
  \(\psi_q=\psi_{q-2}+\psi_{q-3}\);
- Proposition 3.2: the size-refined numbers satisfy
  \(\psi_{q,m}=\psi_{q-2,m-1}+\psi_{q-3,m-1}\);
- Proposition 3.3: the bivariate generating function is

  \[
  \sum_{q,m\geq0}\psi_{q,m}x^q y^m
  =\frac{1+xy+x^2y}{1-x^2y-x^3y};
  \]

- Proposition 3.6: the exact size stratum is

  \[
  \psi_{q,m}=\binom{m+1}{3m-q};
  \]

- Corollaries 3.7--3.8: the maximal-matching polynomial and total binomial
  sum; and
- Propositions 3.4--3.5: asymptotic total growth and the asymptotic mean size
  under the uniform distribution on maximal matchings.

The paper explicitly frames these path matchings as dimers/cars saturating a
linear parking substrate.  It therefore owns both the path enumeration and its
parking interpretation, not just a generic graph definition.

### Exact translation to every W01 static formula

W01 has \(N\) original vertices, so its matchings are those of the paper's
\(P_{N-1}\).  Therefore

\[
b_N=\psi_{N-1}\qquad(N\geq1),
\]

with the empty \(N=0\) boundary adjoined.  The W01 bivariate composition
series

\[
C(x,u)=\frac{1+x}{1-ux^2-ux^3}
\]

is just

\[
C(x,u)=1+x\,
\frac{1+xu+x^2u}{1-x^2u-x^3u},
\]

the vertex-indexed shift of Došlić--Zubac Proposition 3.3.

For a W01 terminal with \(m\) dimers and final length
\(\ell=N-m\), their Proposition 3.6 gives

\[
\psi_{N-1,m}
=\binom{m+1}{3m-N+1}
=\binom{m+1}{N-2m},
\]

where the last equality is binomial symmetry.  Substituting
\(m=N-\ell\) gives exactly

\[
\binom{N-\ell+1}{2\ell-N},
\]

the W01 terminal-length stratum.

Finally, \(a_k=b_{3k}=\psi_{3k-1}\).  The claimed recurrence

\[
a_k=3a_{k-1}-2a_{k-2}+a_{k-3}
\]

and

\[
\sum_{k\geq0}a_kz^k
=\frac{1-z}{1-3z+2z^2-z^3}
\]

are the routine \(3\)-section of the owned Padovan/path-matching sequence.
Taking a residue-class subsequence does not create a new enumerative
contribution.

### Static subtraction verdict

The following receive **zero contribution credit**:

- the no-adjacent-monomer/maximal-matching grammar;
- the recurrence for \(b_N\);
- the recurrence and rational GF for \(a_k=b_{3k}\);
- the bivariate terminal-size GF;
- the binomial terminal-length strata;
- the Padovan/plastic-constant interpretation and asymptotics; and
- any “linear parking” narrative based only on these enumerations.

These are directly stated by Došlić--Zubac or obtained by an index shift,
binomial symmetry, and a \(3\)-section.

## 3. Direct owner for the stochastic engine

### Randomized greedy matching

Martin Dyer and Alan Frieze, *Randomized greedy matching*, Random Structures
& Algorithms 2 (1991), 29--45,
[DOI 10.1002/rsa.3240020104](https://doi.org/10.1002/rsa.3240020104).
The publisher's primary record defines the randomized greedy algorithm on a
fixed input graph by repeatedly choosing the next available edge at random.
It analyzes sparse graph classes and forests.  After the W01 reduction, this
is the literal transition rule on the fixed path.

Martin Dyer, Alan Frieze, and Boris Pittel, *The average performance of the
greedy matching algorithm*, Annals of Applied Probability 3 (1993), 526--552,
[DOI 10.1214/aoap/1177005436](https://doi.org/10.1214/aoap/1177005436),
develops mean, variance, and limit-law analysis for greedy matching on sparse
random graphs and random trees.  It is not needed to own the fixed-path
definition, but it confirms that greedy-matching performance and distributional
questions form an established line.

### Dimer RSA / parking

The exact physical process is older than the graph-algorithm terminology.
The following primary sources establish the relevant ownership chain:

- Paul J. Flory, *Intramolecular Reaction between Neighboring Substituents of
  Vinyl Polymers*, Journal of the American Chemical Society 61 (1939),
  1518--1521,
  [DOI 10.1021/ja01875a053](https://doi.org/10.1021/ja01875a053), studies the
  nearest-neighbour irreversible one-dimensional reaction that became the
  classical lattice-dimer RSA model.
- R. B. McQuistan and D. Lichtman, *Exact Occupation Kinetics for
  One-Dimensional Arrays of Dumbbells*, Journal of Mathematical Physics 9
  (1968), 1680--1684,
  [DOI 10.1063/1.1664497](https://doi.org/10.1063/1.1664497), gives exact
  kinetics for finite one-dimensional arrays and the infinite-array limit.
- Nicholas Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal
  on Discrete Mathematics 2 (1989), 393--401,
  [DOI 10.1137/0402034](https://doi.org/10.1137/0402034), treats graph RSA and
  explicitly includes the edge-occupation version in which occupying an edge
  blocks all incident edges, with dynamic and jamming observables.
- Mathew D. Penrose and Aidan Sudbury, *Exact and approximate results for
  deposition and annihilation processes on graphs*, Annals of Applied
  Probability 15 (2005), 853--889,
  [DOI 10.1214/105051604000000765](https://doi.org/10.1214/105051604000000765),
  develops dimer RSA on graphs, exact forward equations and probability
  controls; the author preprint is
  [arXiv:math/0503519](https://arxiv.org/abs/math/0503519).

Rényi's continuous car-parking problem is important background but is not the
literal owner: W01 is a finite lattice/path dimer process, not continuous
interval parking.  The direct lineage is Flory--McQuistan--Pippenger and the
randomized greedy matching papers.

### Stochastic subtraction verdict

The following receive **zero contribution credit**:

- termination at a maximal matching;
- equivalence between random available-edge choice, random greedy matching,
  and lattice dimer RSA on a path;
- generic jamming, coverage, matching-size, moment, and limit-law questions;
- exponential-priority/random-order formulations of greedy matching; and
- any claim that probabilistic rewriting supplies a new stochastic engine.

W01 has not proved a new uniform-redex probability formula.  Its exact
rational law computed by finite DAG recursion is the pushforward of the
standard finite-path random greedy matching law through a deterministic
terminal labelling.

## 4. Matching-history subtraction

Fix a terminal whose matching has \(m\) edges.  Those edges are pairwise
disjoint.  Every permutation of them is a legal accepted-edge order, and the
inverse terminal decoder forces every history ending at that terminal to use
exactly those edges.  Hence the fibre size \(m!\).

No inspected primary source was located that advertises this exact
occurrence-history sentence for the ternary code.  It nevertheless does not
survive the value subtraction:

1. it is a one-line ordering consequence of disjointness, with no new
   stochastic weights;
2. it does not give the uniform-redex terminal probability, because different
   histories generally have different products of reciprocal active-edge
   counts; and
3. the total

   \[
   H_N=\sum_m m!\,\psi_{N-1,m}
   \]

   is the factorial transform of the directly owned maximal-matching
   polynomial.

Thus the formula

\[
H_{3k}=\sum_{m=k}^{\lfloor3k/2\rfloor}
\binom{m+1}{3k-2m}m!
\]

is not directly quoted from the located papers, but it is a **mechanical
zero-credit corollary** of Došlić--Zubac Proposition 3.6.  Calling it a second
paper-scale engine would overstate the residual.

## 5. Internal collision

This exact mechanism was already considered and killed in the P117--P121
round.  The Phase-2B stochastic scout contains:

> B11. Random greedy dimers on a path — KILL.

It describes uniform selection of a surviving path edge, endpoint deletion,
and recursive path splitting, then identifies the model as one-dimensional
dimer RSA/random greedy matching with Pippenger as direct owner
(`docs/papers117_121_sequence/scouting/STOCHASTIC_PHASE2B_SCOUT.md`, lines
531--554).

W01's ternary symbols do not clear that internal kill.  The proof dossier
shows that they encode B11 exactly and do not influence its dynamics.

## 6. Owned/zero-credit versus residual ledger

| W01 claim | ownership result | credit |
|---|---|---|
| reachable terminals are no-\(11\) monomer/dimer compositions | exact maximal matchings of a path | **owned / zero** |
| \(b_N=b_{N-2}+b_{N-3}\) | Došlić--Zubac Proposition 3.1 after index shift | **directly owned / zero** |
| bivariate GF \((1+x)/(1-ux^2-ux^3)\) | Došlić--Zubac Proposition 3.3 after vertex shift | **directly owned / zero** |
| exact terminal-length binomial coefficient | Došlić--Zubac Proposition 3.6 under \(m=N-\ell\) | **directly owned / zero** |
| \(a_k\) cubic recurrence and GF | \(3\)-section of the owned path sequence | **mechanical / zero** |
| uniform-redex dynamics | randomized greedy matching / edge RSA | **directly owned mechanism / zero** |
| XOR invariant | elementary label check | **zero** |
| no periodic block of length \(\geq3\) collapses | exact coding lemma for these symbols | **literal residual, theorem-thin** |
| injective terminal labelling/inverse decoder | deterministic code of a maximal matching | **literal residual, theorem-thin** |
| terminal history fibre \(m!\) | permutations of the matching edges | **bounded non-hit but mechanical / zero** |
| total history sum | factorial transform of the owned size polynomial | **mechanical / zero** |
| complete uniform-redex terminal probability formula | not proved in the dossier; standard process underneath | **no current residual claim** |

## 7. Allowed claim ceiling

The only defensible archival statement is:

> For the periodic word \((012)^k\), the oriented ternary fusion rule gives an
> explicit injective labelling of maximal matchings of the \(3k\)-vertex path;
> the no-large-block lemma supplies the elementary conjugacy.

It may not claim as contributions:

- the support recurrence or rational GF;
- maximal-matching enumeration or its size refinement;
- the terminal-length closed form;
- the random greedy/RSA process;
- generic parking or jamming interpretations;
- the \(m!\) edge-ordering observation; or
- the factorially weighted total history sum.

A literal exact-string non-hit for
`01->2, 12->0, 20->1` does not raise this ceiling.

## 8. Final recommendation

**`KILL_RECOMMEND / ARCHIVE PROOF / HOLD_EXTERNAL`.**

The owner subtraction removes both proposed paper-scale outputs:

1. the grammar/recurrence/GF/strata package is directly owned path maximal
   matching enumeration; and
2. the history package is a trivial ordering/factorial transform of the owned
   size polynomial.

The stochastic process is additionally a direct instance of random greedy
matching and one-dimensional dimer RSA, and it repeats the internally killed
B11 lane.  The ternary endpoint labels are a mechanical code, not a new
dynamics.

Reconsideration would require changing the mathematical content, not adding
more exposition or bounded computation.  In particular, it would need a
label-sensitive theorem that is not determined by the underlying maximal
matching or its accepted-edge order, together with a fresh collision and
primary-owner audit.  No such theorem is present for the current periodic
start family.
