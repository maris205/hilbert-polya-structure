# Primary-owner and adjacency search log

**Search date:** 2026-09-03 UTC  
**Policy:** bounded search; non-hit is not novelty, priority, or clearance.

## Search matrix

| candidate / queries | verified primary source | exact credit boundary and decision |
|---|---|---|
| `MCJ`: `permutation merge cycle containing 1 minimum outside swap successors`; `star transposition cycle minima`; `Foata cycles decreasing minima left-right minima` | Ira M. Gessel and Richard P. Stanley, *Algebraic Enumeration*, in *Handbook of Combinatorics*, vol. 2 (1995), 1021--1061, [author publication record](https://math.mit.edu/~rstan/pubs/) and [official manuscript](https://math.mit.edu/~rstan/pubs/pubfiles/79.pdf). | The source explicitly gives the minimum-first/decreasing-minima cycle flattening and the cycle/lower-record equivalence.  These static facts and unsigned Stirling counts receive zero credit. |
| `MCJ`: `minimal star factorization permutation`; `right multiplication star transposition` | John Irving and Amarpreet Rattan, *Factorizations of Permutations into Star Transpositions*, [arXiv:math/0610640](https://arxiv.org/abs/math/0610640); journal version *Minimal Factorizations of Permutations into Star Transpositions*, *Discrete Mathematics* 309 (2009), 1435--1442, DOI `10.1016/j.disc.2008.02.018`. | Star transpositions, their action on permutation cycles, and minimal-factorization word encodings receive zero credit.  The source does not need to state the same adaptive minimum schedule: after P122's internal record-cut subtraction, the residual is already too thin. |
| `MCJ`: `cycle cutting mapping tree minima`; `endofunction cycles ordered by minima` | Steven Heilman, *Tree/Endofunction Bijections and Concentration Inequalities*, *Electronic Journal of Combinatorics* 29(2) (2022), P2.33, [DOI 10.37236/10560](https://doi.org/10.37236/10560), [journal page](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v29i2p33). | Ordered cycle cutting/stringing in functional digraphs is explicit background.  It is not the same self-map, but it reinforces that the normal-form operation is owned. |
| `IAC`: `number mth roots permutations explicit formula`; `square roots uniform cycles` | Jesús Leaños, Rutilo Moreno, and Luis Manuel Rivera-Martínez, *On the Number of mth Roots of Permutations*, [arXiv:1005.1531](https://arxiv.org/abs/1005.1531), *Australasian Journal of Combinatorics* 52 (2012), 41--54. | Exact root existence/counting by cycle type is direct.  `IAC`'s odd fixed powers reduce to that problem; even powers reduce to centralizers.  Its cycle census is therefore a routine Möbius lift, not a new axis. |
| `TAN`: `nonsingular nonlinear feedback shift register x0 plus F tail`; `NLFSR cycle joining` | Tomasz Rachwalik, Janusz Szmidt, Robert Wicik, and Janusz Zabłocki, *Generation of Nonlinear Feedback Shift Registers*, [IACR ePrint 2012/314](https://eprint.iacr.org/2012/314.pdf).  Ming Li, Cees J. A. Jansen, Dongdai Lin, and Qiuyan Wang, *De Bruijn Sequences from Joining Cycles of Nonlinear Feedback Shift Registers*, [IACR ePrint 2015/667](https://eprint.iacr.org/2015/667.pdf). | The nonsingular form `x_0 xor F(x_1,...,x_{n-1})` and cycle-joining programme are explicit.  `TAN` is exactly such a register and differs from the pure circulating register only on the all-one/one-zero orbit. |
| `FDF`: `first adjacent out of order move smaller to beginning`; `First Sort permutation`; `move first descent follower to front` | Project Euler, [Problem 523: First Sort I](https://projecteuler.net/problem=523) and [Problem 524: First Sort II](https://projecteuler.net/problem=524). | **Direct literal owner.**  Both pages state: scan adjacent pairs from the beginning; at the first out-of-order pair, move the smaller element to the beginning; repeat.  They explicitly define and study the step count `F`.  Kill without residual novelty analysis. |
| `FDF` adjacency: `sorting cut longest increasing prefix`; `first descent shuffle sorting` | Lara Pudwell and Rebecca Smith, *Sorting via Shuffles with a Cut after the Longest Increasing Prefix*, preprint dated 3 June 2024, [author-hosted manuscript](https://faculty.valpo.edu/lpudwell/papers/shuffle_sorting.pdf). | Their `PRE` and `MIN` algorithms cut at the first descent but perform a full riffle, not the single move-to-front update.  This is an adjacent owner only; Project Euler supplies the decisive exact owner. |

## Candidate-specific owner notes without survival claims

- `CTC` is a conjugacy-orbit map; no literal search can make the elementary
  `n`-to-one conjugation fibre a novelty axis.
- `PMX` was killed internally before an external mex/transducer search could
  matter.
- `NOG` is a labelled encoding of equality partitions.  Bell and falling
  factorial counts are treated as owned background.
- `CRP` is standard stable least-significant-digit radix sorting under a cyclic
  relabelling of bit positions.  The algorithmic identification is itself the
  kill.
- `DCS` has no theorem spine to put through an owner gate.
- `CSS` is a deterministic canonical-support selection algorithm; it is killed
  internally as canonicalization, not retained on an external non-hit.

## Non-hit language

The bounded queries did not locate an article spelling out `MCJ` in precisely
the same adaptive notation.  That non-hit carries no positive evidentiary
weight.  The candidate is killed anyway because its entire inverse and
enumerative package transfers from owner-subtracted Foata/star-transposition
machinery and the P122 record-cut engine.

