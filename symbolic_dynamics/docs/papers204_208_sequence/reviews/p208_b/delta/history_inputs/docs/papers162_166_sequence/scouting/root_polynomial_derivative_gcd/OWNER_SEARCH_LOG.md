# Bounded owner and collision log — derivative--GCD dynamics

**Date:** 2026-09-03 UTC  
**Status:** `KILL_DIRECT_OWNER_AND_INTERNAL_PDG`  
**External state:** `HOLD_EXTERNAL`

## Searches

```text
iterate map f -> gcd(f,f') polynomial dynamics finite field
"gcd(f,f')" iteration polynomial
repeated gcd with derivative finite field polynomial
dynamical system gcd polynomial derivative
squarefree factorization finite fields repeated gcd derivative primary paper
formal derivative gcd multiplicities characteristic p squarefree decomposition
```

The local search found the decisive collision after the formulas were checked:
P152--P156 scouting already treats this exact capped monic-polynomial self-map
as `PDG`, and a second algebraic-replacement pass records it as `SFE`.  Thus
this is not a new literal system in the portfolio.

## Ownership that must be subtracted

1. D. R. Musser, *Algorithms for Polynomial Factorization*, PhD thesis,
   University of Wisconsin (1971), and D. Y. Y. Yun,
   *On square-free decomposition algorithms*, SYMSAC 1976, pp. 26--35,
   [ACM DOI record](https://doi.org/10.1145/800205.806320).  They own the
   square-free decomposition problem and derivative/GCD multiplicity peeling.
   The map definition and all algorithmic motivation receive zero credit.

2. P. Wang and B. Trager, *New algorithms for polynomial square-free
   decomposition over the integers*, SIAM J. Comput. 8 (1979), and the broad
   subsequent computational-algebra literature own gcd/derivative techniques,
   complexity concerns, and square-free output.  No algorithmic novelty is
   asserted here.

3. Standard finite-field square-free factorization handles the vanishing
   derivative by extracting a `p`th root; see the openly available
   [MIT 18.783 finite-field arithmetic notes](https://ocw.mit.edu/courses/18-783-elliptic-curves-spring-2021/b6d0aef71278ad8c1d8b5144c4138cb7_MIT18_783S21_notes3.pdf)
   and [MIT algebra/computation notes](https://people.csail.mit.edu/madhu/ST12/scribe/lect07.pdf).
   The characteristic-`p` factor rule is therefore background, not a new
   algebraic observation.

4. Counts of monic irreducibles and their Euler products are classical finite
   field theory and receive zero credit.

## Correct extension, but no surviving residual

The present scout correctly extends the old `char>N` formula to arbitrary
prime characteristic, where multiplicities stop at their residues modulo
`p`.  It thereby obtains:

- simultaneous residue clock and all depth layers on the capped phase;
- the global cap-sensitive time-image criterion;
- every-time/every-target degree-excess Euler fibre polynomial;
- fixed basin/zeta and narrowly stated parameter recovery.

These formulas are useful negative controls.  They remain one factor-
multiplicity engine plus Euler bookkeeping after direct owner subtraction,
and the literal map is already occupied in the local kill ledger.  This forces
a kill without consuming an independent paper-review slot.

## Internal firewall

P100/P107/P115/P157 and the earlier derivative scouts were inspected.  Their
carriers are residue-ring nilradicals, ideal lattices, coefficient spaces, or
scalar Hensel maps.  None is a restriction or quotient of this monic-
polynomial gcd map.  Generic valuation/residue arguments remain zero credit.

The exact local collisions are:

- `docs/papers152_156_sequence/scouting/algebraic/SCOUT.md`, handle `PDG`,
  verdict `RESERVE_OWNER_COMPRESSED`, explicitly never a quota filler;
- `docs/papers152_156_sequence/scouting/algebraic_replacement2/SCOUT.md`,
  handle `SFE`, verdict `KILL_ALGORITHM_ENGINE`.

```text
KILL_DIRECT_OWNER_AND_INTERNAL_PDG
HOLD_EXTERNAL
```
