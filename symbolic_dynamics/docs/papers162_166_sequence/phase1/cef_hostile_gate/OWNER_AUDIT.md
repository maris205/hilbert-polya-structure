# CEF independent owner audit

Status: **bounded audit; HOLD_EXTERNAL; no novelty or priority claim**  
Audit date: 2026-09-03

## Object being subtracted

For `q>=3` and `n=2^m>=4`, CEF maps a cyclic word to its adjacent-equality
indicator.  After the first step the state is binary and the map is affine:
with `D=I+S` over `F_2`, `T(b)=1+Db`.   Thus three classical owner lanes must
be removed before evaluating the residual package:

1. finite linear/affine cellular-automaton dynamics;
2. cyclic differences and repeated-root cyclic codes;
3. cycle-colouring multiplicities and character/Fourier inversion.

## External owner subtraction

### Linear and affine cellular automata

- Martin, Odlyzko and Wolfram, *Algebraic Properties of Cellular Automata*,
  Communications in Mathematical Physics 93 (1984), 219--258,
  [doi:10.1007/BF01223745](https://doi.org/10.1007/BF01223745), derives finite
  state-transition diagrams for algebraic cellular automata.  CEF receives no
  credit for applying the finite-linear functional-graph toolkit after time
  one.
- Ganguly, Sikdar and Pal Chaudhuri, *Exploring Cycle Structures of Additive
  Cellular Automata*, Fundamenta Informaticae 87 (2008), 137--154,
  [doi:10.3233/FUN-2008-87202](https://doi.org/10.3233/FUN-2008-87202),
  explicitly treats XOR/XNOR affine CA and their cyclic vector subspaces.
- Nomenclature matters: `Db_i=b_i+b_{i+1}` is the one-sided elementary
  **Rule 102** (up to reflection, Rule 60), and `1+Db` is its complement,
  **Rule 153**.  It is not literally Rule 90, whose local rule uses the two
  outer neighbours.  A Rule-90 comparison is permissible only after stating
  the relevant shift/shear convention; it is not the literal map.

Subtraction: nilpotence of `D` at power-of-two circumference, its kernel flag,
and the resulting binary absorption clock belong to this background lane.

### Cyclic differences and repeated-root cyclic codes

- Breuer, Lötter and van der Merwe, *Ducci-sequences and cyclotomic
  polynomials*, Finite Fields and Their Applications 13 (2007), 293--304,
  [doi:10.1016/j.ffa.2005.11.003](https://doi.org/10.1016/j.ffa.2005.11.003),
  studies cyclic difference dynamics through polynomials over `F_2`.
- Zhao, Li, Yang, Fu and Shum, *Weight Distribution of Repeated-Root Cyclic
  Codes with Prime Power Lengths*, arXiv:2304.00762v3 (2025),
  [primary text](https://arxiv.org/html/2304.00762v3), states and develops
  weight distributions for all repeated-root cyclic codes of prime-power
  lengths.
- Here
  `F_2^n = F_2[x]/((x+1)^n)` and
  `ker D^j = <(x+1)^(n-j)>`.  Thus every homogeneous polynomial
  `W_{n,j}(a)=sum_{c in ker D^j} a^wt(c)` is exactly a weight enumerator of a
  repeated-root binary cyclic code.  The dyadic repeated-block specialization
  and last even-weight layer are therefore owner-dense, not an independent
  novelty axis.

### Colouring and Fourier ingredients

- The multiplicity
  `chi_q(c)=(q-1)^r+(-1)^r(q-1)`, with `r=wt(c)`, is the standard chromatic
  polynomial of a cycle after contracting equality edges.  This ingredient
  receives zero independent credit.
- The displayed formula for
  `W_{n,j,d}(a)=sum_{D^j c=d}a^wt(c)` is ordinary character orthogonality for an
  affine binary code/coset.  It is exact, but merely writing the full character
  sum does not classify targets or their fibre spectrum.

## Internal subtraction

- **P98:** the literal map differs: P98 uses a reversible equal-block-sum
  finite-field shift and studies companion modules/cycles/zeta data.  There is
  no literal-system duplicate.  However P98 already occupies the repeated-root
  finite-linear/polynomial dynamics proof engine.  CEF can survive internally
  only on the nonlinear q-ary front and results that genuinely exploit its
  nonuniform change-mask multiplicities.
- No exact P1--P161 match was located for “cyclic adjacent equality indicator
  followed by one-sided binary difference.”  This is a bounded non-hit, not a
  novelty statement.

## Residual after subtraction

The real residual is narrow but nonempty:

- the nonlinear q-ary first-step map has all binary change masks except the
  `n` unit masks, with q-dependent multiplicity `chi_q`;
- the exact time-one support holes are consequently q-ary-front phenomena;
- weighting affine `D^j`-cosets by `chi_q` gives correct target-dependent
  fibres, and the all-one time-one fibre recovers `q`.

What is **not** yet residual enough is a second theorem axis.  The absorption
CDF is the zero-coset instance of the same weighted-coset calculation used for
all target fibres.  The current Fourier display is a universal transform, not
an evaluated target classification, extremal theorem, or fibre-spectrum
theorem.  Hence “q-ary front + every-target fibre formula” is mathematically
valid but, at present, not logically independent of the clock engine after
owner subtraction.

## Owner verdict

No exact direct owner of the full nonlinear CEF composition was found in the
bounded search.  Nevertheless, the binary tail and homogeneous kernel
enumerators are strongly owned, and the proposed second axis is presently too
generic.  Owner status: **AMBER-LOW / DO NOT ALLOCATE A PAPER YET**.

Re-entry requires an evaluated, target-sensitive theorem beyond the defining
coset/Fourier sum: for example a classification of fibre values and their
multiplicities, a sharp extremal-target theorem with equality cases, or a
deformation/recovery result whose proof does not reduce to the same kernel
filtration.

