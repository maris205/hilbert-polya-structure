# CEF bounded owner and collision log

**Date:** 2026-09-03  
**Status:** direct binary engine found and fully subtracted; no literal
`q`-ary conjunction located in the bounded pass; `HOLD_EXTERNAL`.

## Direct background owners

1. O. Martin, A. M. Odlyzko, and S. Wolfram, “Algebraic properties of
   cellular automata,” *Communications in Mathematical Physics* **93**
   (1984), 219--258, DOI `10.1007/BF01223745`.  This directly owns algebraic
   treatment of finite additive cellular automata, including cyclic XOR
   difference rules.
2. M. Misiurewicz, J. G. Stevens, and D. M. Thomas, “Iterations of linear
   maps over finite fields,” *Linear Algebra and its Applications* **413**
   (2006), 218--234, DOI `10.1016/j.laa.2005.09.002`.  This owns the
   linear-functional-graph and Rule-90/Ducci context.
3. N. Ganguly, B. K. Sikdar, and P. Pal Chaudhuri, “Exploring Cycle
   Structures of Additive Cellular Automata,” *Fundamenta Informaticae*
   **87** (2008), 137--154, DOI `10.3233/FUN-2008-87202`.  This explicitly
   treats XOR/XNOR additive CA structure.  CEF claims no binary-CA priority.
4. Jae-Gyeom Kim, “Cycles of characteristic matrices of cellular automata
   with periodic boundary condition,” *Korean Journal of Mathematics* **19**
   (2011), 291--300.  Its periodic Rule-102 matrix powers directly own the
   power-of-two vanishing theorem.  CEF assigns zero credit to every
   periodic-ring power, kernel, image, and nilpotence statement for `D=I+S`.
5. J. Lee and H. Shin, “The chromatic polynomial for cycle graphs,” arXiv
   `1907.04320` (2019), records the classical cycle formula
   `(q-1)^r+(-1)^r(q-1)`.  The formula and all generic chromatic-polynomial
   language receive zero credit.

Generic finite Fourier inversion, cyclic-code weight enumerators, and the
factorization `x^(2^m)-1=(x+1)^(2^m)` over `F_2` are also background.

6. Zhao, Li, Yang, Fu, and Shum,
   [*On the Weight Distribution of Repeated-Root Cyclic Codes*](https://arxiv.org/abs/2304.00762v3)
   (version current in 2025), treats weight distributions of repeated-root
   cyclic codes of prime-power lengths.  Accordingly, homogeneous kernel
   enumerators and the repeated-root ideal description receive zero credit.

Terminology is corrected as well: the one-sided binary tail is Rule 102 and
its affine complement is Rule 153; it is not literally Rule 90.

## Literal search

Queries combined: cyclic word equality indicator iteration; q-ary adjacent
equality cellular automaton; XNOR neighbour feedback; cyclic difference at
power-of-two length; equality-mask preimages; and affine-code fibres.  The
bounded pass did not locate a source for the literal map

```text
w -> (1{w_i=w_(i+1)})_i
```

on a `q>=3` alphabet together with its full finite functional graph or
target-resolved fibres.  This is a bounded non-hit only.

## P1--P161 subtraction

- **P98:** directly owns repeated-root finite-linear dynamics and zeta/cycle
  machinery.  CEF makes no claim to those.  Its residual begins at the
  nonlinear colour-change mask, uses a nilpotent rather than reversible
  tail, and retains exact q-dependent fibres over affine binary cosets.
- **P117/P138:** word dynamics, parity and sharp clocks are architectural
  overlap only; neither has this local equality map or affine-code fibre.
- **P147:** its “equality” is consolidation of equal adjacent positive parts,
  not equality-indicator feedback.
- **Killed AQN:** cyclic derivative data controls a rotation after quotienting
  alphabet translations.  CEF instead maps immediately to the binary change
  mask and repeatedly differentiates it.
- **Generic linear-system permanent exclusion:** all results about `D` alone
  are excluded from the residual claim.  Hostile review must decide whether
  formulas (5), (9), (10), and (13) leave a sufficiently independent
  q-ary interface after this subtraction.

```text
NOVELTY CLAIM       NONE
BINARY DIRECT OWNER YES, SUBTRACTED
LITERAL Q-ARY HIT   NONE IN BOUNDED PASS
EXTERNAL            HOLD_EXTERNAL
```
