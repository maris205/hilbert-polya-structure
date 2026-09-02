# P164 independent owner and collision audit

Status: **owner-thin pass under explicit subtraction; HOLD_EXTERNAL**  
Audit date: 2026-09-03

This is a bounded owner audit, not a novelty or priority opinion.

## External owner subtraction

### Periodic additive cellular automata

- Martin, Odlyzko, and Wolfram, *Algebraic Properties of Cellular Automata*,
  *Communications in Mathematical Physics* 93 (1984), 219--258,
  <https://doi.org/10.1007/BF01223745>, is a primary general source for the
  algebraic treatment of finite cellular automata.
- Jae-Gyeom Kim, *Cycles of Characteristic Matrices of Cellular Automata with
  Periodic Boundary Condition*, *Korean Journal of Mathematics* 19 (2011),
  291--300,
  <https://kkms.org/index.php/kjm/article/download/107/80/0>, directly studies
  powers of the periodic Rule-102 characteristic matrix.

Accordingly, the binary operator `D=I+S`, its dyadic nilpotence, ranks,
kernels, images, and matrix powers receive zero contribution credit.  The
manuscript states this firewall explicitly and uses the correct Rule-102
nomenclature.

### Repeated-root cyclic codes

Zhao, Li, Yang, Fu, and Shum, *Weight Distribution of Repeated-Root Cyclic
Codes with Prime Power Lengths*, arXiv:2304.00762v3 (revised 2025),
<https://arxiv.org/abs/2304.00762>, explicitly determines weight distributions
for repeated-root cyclic codes of prime-power lengths.  The homogeneous
kernel enumerators in P164 sit in this owner lane and receive zero credit.
The bibliography's year `2025` consistently identifies the cited v3, although
adding the version number would make that choice more transparent.

### Equality-pattern cellular automata and colouring

Bolognesi and Ciancia, *Exploring Nominal Cellular Automata*, *Journal of
Logical and Algebraic Methods in Programming* 93 (2017), 23--41,
<https://doi.org/10.1016/j.jlamp.2017.08.001>, studies cellular automata whose
local rules depend on equality patterns of names.  It is a relevant conceptual
owner, but the inspected source does not state the finite-q cyclic map in P164
or Theorem 1's clock and target-fibre atlas.

The change-mask multiplicity is the cycle chromatic polynomial after equality
edges are contracted, and the affine-code display is ordinary character
orthogonality.  The manuscript explicitly assigns both zero credit.  These
classical ingredients do not support a novelty claim.

## Residual theorem package

After subtraction, the residual is the conjunction of:

1. the literal finite-q equality front and its nonuniform source multiplicity;
2. the exceptional unit-mask holes at time one;
3. the pullback of every affine tail target with the q-dependent weight;
4. the fully evaluated time-two and midpoint target spectra, with exact
   parameter-class censuses and numerical-collision aggregation.

The evaluated slices are not supplied by a homogeneous repeated-root weight
distribution alone: they resolve affine cosets, pull them back through the
q-ary nonlinear front, and count the syndrome classes.  This is enough for an
owner-thin short-paper package, while remaining far below an absolute novelty
claim.

## Internal P1--P161 collision audit

- **P98** is the closest proof-engine collision.  It already occupies a
  repeated-root finite-linear shift and its periodic data.  P164 correctly
  subtracts that entire tail.  Its residual change-mask pullback and the two
  target-resolved spectra are not statements of P98.
- **P63** uses XOR differentiation only inside an infinite symbolic-conjugacy
  inverse-radius problem; it does not contain this finite equality map or its
  weighted affine fibres.
- **P117** is a run-reversal dynamics whose recurrent census is controlled by
  cyclic run parities; it is not a linearized adjacent-equality feedback map.
- **P138** is palindromic-prefix XOR feedback with a sequential fibre decoder;
  neither its literal system nor its proof engine matches the affine
  change-mask census here.

A bounded exact-phrase and mechanism search found no P1--P161 paper with the
same literal map.  This non-hit does not certify external novelty.

## Citation and source QA

- All four cited keys resolve in the final BibTeX pass; BibTeX reports four
  entries and zero warnings.
- Author names, titles, venues, years, volumes, pages, and DOI/URL fields agree
  with the inspected primary landing pages or texts.
- Kim is the direct periodic Rule-102 owner and Zhao is the strong current
  repeated-root-code owner; both are cited at the point of subtraction.
- The text does not overstate priority: it says `owner-thin`, disclaims
  absolute novelty, and retains `HOLD_EXTERNAL`.

## Owner verdict

**PASS_OWNER_THIN.**  No direct owner of the full nonlinear-front plus two
evaluated target spectra was located.  The linear, coding, colouring, and
Fourier components remain zero-credit background.  External posting,
circulation, or submission must remain `HOLD_EXTERNAL`.
