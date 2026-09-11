# Cyclic sliding-AND — bounded owner and collision search

**Search date:** 2026-09-03  
**Status:** `HOLD_EXTERNAL`  
**Ruling:** `KILL_DIRECT_RULE136_AND_PREIMAGE_OWNER`

This ledger distinguishes a direct owner, a framework owner, an ingredient
owner, and a bounded non-hit.  It makes no novelty or priority claim.

## 1. Search object and orientation correction

The literal query object was

```text
E(x)_i=x_i*x_{i+1},  x in {0,1}^{Z/nZ}.
```

Queries included `Rule 192 AND cellular automaton`, `Rule 136 explicit
solution`, `elementary cellular automaton 136 preimages`, `arbitrary sequence
preimage Rule 136`, `binary erosion interval iteration`, `morphological
erosion composition`, `cyclic binary words avoiding consecutive ones trace`,
and `weighted preimage cellular automata`.

The first audit result is a nomenclature repair.  In the conventional Wolfram
ordering the literal rule is Rule 136.  Rule 192 is its left-right reflection.
The equivalence is exact on a cyclic ring, but the displayed orientation must
not be mislabeled.

## 2. Direct forward owner

### Henryk Fukś — exact Rule-136 iterate

Fukś's author-maintained table of deterministic ECA solutions explicitly
lists

```text
[F_136^n(x)]_j = product_{i=0}^n x_{i+j}.
```

- [Author's explicit-solution table](https://lie.ac.brocku.ca/~hfuks/solvableca.html)
- Henryk Fukś, *Solvable Cellular Automata: Methods and Applications*,
  Springer, 2023, DOI
  [10.1007/978-3-031-38700-5](https://doi.org/10.1007/978-3-031-38700-5).

The publisher describes the book's objective as explicit arbitrary-time cell
states and says its appendix tabulates solutions for more than sixty ECA.

**Subtraction:** the sliding product formula receives zero credit.  The
longest-run erosion, fixed-point classification, and `n-1` sharp height are
immediate finite-ring consequences and cannot serve as an independent new
temporal axis.

## 3. Direct preimage-family owner

### Erica Jen — arbitrary spatial preimages, including Rule 136

Erica Jen, “Enumeration of Preimages in Cellular Automata,” *Complex Systems*
**3** (1989), 421--456, derives exact preimage formulae for arbitrary spatial
sequences under arbitrary one-dimensional nearest-neighbour CA rules.

- [Official abstract](https://www.complex-systems.com/abstracts/v03_i05_a02/)
- [Primary full text](https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf)

The paper decomposes arbitrary targets into alternating zero/one blocks,
derives preimage recurrences through de Bruijn graphs, and classifies Rule 136
in its type C: products of Fibonacci-like terms indexed by run lengths.  Its
stated uses include Garden-of-Eden tests, all-word probability calculations,
and run statistics.

**What it directly consumes:** arbitrary-target preimage enumeration as a
research direction, run/gap factorization, transfer/de-Bruijn methodology,
and unweighted one-step Rule-136 preimages.

**What was not located verbatim:** the exact periodic-boundary,
arbitrary-`t`, source-weight-refined polynomial in `SCOUT.md` equation (3.5).
Jen's displayed paper studies finite spatial sequences on the infinite CA and
does not visibly state that exact cyclic formula.  This narrow non-match does
not reverse the ownership decision: (3.5) is a straightforward specialization
of the owned arbitrary-target/run-factorized lane after replacing one-step
memory by the `t+1` forbidden-run automaton.

### Henryk Fukś — preimage sequences

Henryk Fukś, “Sequences of Preimages in Elementary Cellular Automata,”
*Complex Systems* **14** (2003), 29--43, DOI
[10.25088/ComplexSystems.14.1.29](https://doi.org/10.25088/ComplexSystems.14.1.29),
develops systematic exact preimage-sequence methods for ECA blocks.
[Primary journal PDF](https://content.wolfram.com/uploads/sites/13/2023/02/14-1-2.pdf)

It is a framework owner rather than an exact owner of the cyclic weighted
formula.  It reinforces the zero-credit boundary for generic preimage-tree and
transfer-matrix machinery.

## 4. Mathematical-morphology owner

H.J.A.M. Heijmans and C. Ronse, “The algebraic basis of mathematical
morphology I: Dilations and erosions,” *Computer Vision, Graphics, and Image
Processing* **50** (1990), 245--295, DOI
[10.1016/0734-189X(90)90148-O](https://doi.org/10.1016/0734-189X(90)90148-O),
places translation-invariant erosions in the complete-lattice/adjunction
framework and characterizes their intersection-preserving behavior.

- [CWI primary record](https://ir.cwi.nl/pub/5977)
- [CWI primary scan](https://ir.cwi.nl/pub/5977/5977D.pdf)

The closest iteration-specific source located was H.J.A.M. Heijmans,
“Iterations of morphological transformations,” *CWI Quarterly* **2** (1989),
19--36. [CWI primary record](https://ir.cwi.nl/pub/18153)

Identifying the one-set of `E(x)` with erosion by `{0,1}` makes the growing
window in the iterate the Minkowski sum of the structuring element with
itself.  Hence the erosion terminology and composition mechanism are classical
and receive zero credit.

## 5. Forbidden-run ingredient owner

L.J. Guibas and A.M. Odlyzko, “String overlaps, pattern matching, and
nontransitive games,” *Journal of Combinatorial Theory, Series A* **30**
(1981), 183--208, DOI
[10.1016/0097-3165(81)90005-4](https://doi.org/10.1016/0097-3165(81)90005-4),
gives generating functions for words avoiding prescribed finite pattern sets.

This source is broader than the specific cyclic trace `tr(Q_t(z)^n)`; it is
recorded as an ingredient owner, not a claim that the trace identity is copied
there.  Transfer matrices for avoiding `1^{t+1}`, including their weighted
version, are standard finite-automaton technology.  The depth CDF therefore
cannot supply independent residual value after the Rule-136 solution is
subtracted.

## 6. Internal P1--P161 collision audit

| paper | overlap | ruling |
|---|---|---|
| P63 | sliding binary local rule and inverse-window language | Different XOR/rank-one infinite carrier; no literal formula transfer, but inverse-radius vocabulary is occupied. |
| P90 | elementary CA on a finite binary ring, exact transients and weighted enumeration | Strong category collision despite a different local rule (Rule 184). |
| P105 | sharp `n-1` finite pruning clock plus every-target fibres | Packaging collision only; literal carrier differs. |
| P117 | cyclic binary words, run-local evolution, exact recurrence/preperiod | Strong carrier and proof-statistic collision. |
| P147 | local run dynamics, sharp clock, every-target gap-factorized product fibre | Decisive theorem-architecture collision. |
| P149 | ranked images/sections under endpoint extraction | No literal collision; only image-atlas packaging. |
| P155 | ranked images, target thresholds, every-target fibres | No literal collision; only extraction/atlas packaging. |

The audit used the corresponding local paper abstracts/contracts and the
P1--P161 occupancy material.  It is an internal non-equivalence check, not an
external novelty search.

## 7. Same-batch collision audit

- **RTI:** random translation intersections in `F_2^d` use a stochastic
  history-span statistic and stabilizer-weighted fibres.  Sliding AND can be
  written as intersection with a translate of a subset of the cycle, but the
  translation is fixed rather than random and the theorem engine collapses to
  interval erosion.  No literal or proof-equivalence collision was found.
- **CEF:** q-ary cyclic equality feedback has a nonlinear equality front and
  an additive Rule-102/153 tail, plus q-weighted target spectra.  It is not
  conjugate to Rule 136.  It nevertheless creates material portfolio crowding
  in the exact cyclic finite-word CA category.

Thus neither same-batch system directly owns the map, but neither supplies the
missing second residual theorem axis.

## 8. Search ceiling and ruling

The bounded primary-source audit did not locate a text stating the full
cyclic weighted formula

```text
z^{sum(a_i+t)} product_i (Q_t(z)^{b_i-t-1})_{0,0}
```

for every nonconstant target.  Search coverage was finite, terminology varies,
and old CA tables may contain stronger specializations.  Therefore this
non-hit must never be phrased as novelty, first discovery, or exhaustive
absence.

Even under the generous assumption that this exact refinement is unowned, it
is only one theorem axis after subtracting:

1. Fukś's exact temporal solution;
2. mathematical erosion and composition;
3. Jen's arbitrary-target Rule-136 preimage/run-product framework; and
4. classical forbidden-pattern automata.

**Owner/value decision: `KILL`.**  The residual is mathematically valid but
not paper-scale for this batch.  Retain the record under `HOLD_EXTERNAL`; do
not promote it or infer novelty from the bounded non-hit.
