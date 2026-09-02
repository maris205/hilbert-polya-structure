# CEF V2 re-entry owner audit

**Audit date:** 2026-09-03 UTC  
**Scope:** bounded primary-source and P1--P161 collision audit  
**External status:** `HOLD_EXTERNAL`  
**Novelty/priority claim:** none

## Object and subtraction rule

CEF is the finite-ring map

```text
T_q(w)_i = 1{w_i=w_(i+1)},  q>=3, n=2^m>=4.
```

Writing `c_i=1{w_i!=w_(i+1)}` and `D=I+S` on the binary cyclic ring gives
`T_q^t(w)=1+D^(t-1)c(w)` for `t>=1`.  The following receive zero contribution
credit before the V2 repair is evaluated:

- the Rule-102 cyclic difference map `D`, its Rule-153 affine complement,
  their powers, and power-of-two nilpotence;
- the ideal flag `ker D^j=<(x+1)^(n-j)>`, all homogeneous code weight
  distributions, and repetition/direct-sum decompositions of these codes;
- the cycle chromatic polynomial giving fixed-change-mask colourings;
- character orthogonality/Fourier inversion for arbitrary affine-code weight
  enumerators.

## Closest primary owners

### 1. Rule 102 on periodic rings: direct owner of the binary tail

Jae-Gyeom Kim, *Cycles of characteristic matrices of cellular automata with
periodic boundary condition*, **Korean Journal of Mathematics 19** (2011),
291--300, studies powers of the characteristic matrix for uniform Rule 102
with periodic boundary conditions.  In particular its Theorem 3.5 gives
vanishing at power-of-two length.  [Primary PDF](https://kkms.org/index.php/kjm/article/viewFile/107/80)

The more recent discussion by Sfairopoulos et al. explicitly identifies the
cyclic mod-2 Ducci matrix with Rule 102, writes `D=I+S`, and derives
`D^(2^k)=0` at circumference `2^k`.  [Primary journal PDF](https://journals.aps.org/prb/pdf/10.1103/PhysRevB.108.174107)

Martin, Odlyzko and Wolfram's earlier finite additive-CA paper owns the broad
algebraic functional-graph framework.  [Primary author-hosted PDF](https://content.wolfram.com/sw-publications/2020/07/algebraic-properties-cellular-automata.pdf)

**Subtraction consequence.**  CEF gets no credit for the binary iterate,
nilpotence, kernel dimensions, image flag, or absorption of Rule 102/153 in
isolation.  These sources do not count q-ary sources of a binary state and do
not state the CEF target-fibre spectra.

### 2. Zhao--Li--Yang--Fu--Shum: direct owner of repeated-root code weights

Zhao et al., *Weight Distribution of Repeated-Root Cyclic Codes with Prime
Power Lengths*, arXiv:2304.00762v3 (2025), explicitly treats every ideal
`<(x-1)^i>` in the prime-power-length cyclic ring, gives homogeneous weight
distributions, and supplies monomial repetition/direct-sum decompositions
(notably Theorem 6).  [Primary article](https://arxiv.org/html/2304.00762v3)

For CEF over `F_2`, `ker D^j=<(x+1)^(n-j)>`.  Therefore the complete
homogeneous enumerators, the dyadic repeated-block checkpoints, and the
even-weight penultimate kernel are zero-credit code theory.  At the midpoint,
Zhao's structure also owns the fact that the kernel is monomially equivalent
to a direct sum of binary length-two repetition codes.

**Residual not supplied by Zhao.**  The V2 quantities are not homogeneous
code enumerators.  They sum the q-dependent nonlinear multiplicity

```text
chi_q(c)=(q-1)^wt(c)+(-1)^wt(c)(q-1)
```

over every affine syndrome class `D^j c=d`, and then count target syndromes by
an integrated-radius or half-word statistic.  The inspected Zhao text contains
no affine-coset target classification and no q-ary equality-feedback front.

### 3. Equality-based cellular automata: close vocabulary, different carrier

Bolognesi and Ciancia, *Exploring nominal cellular automata*, **Journal of
Logical and Algebraic Methods in Programming 93** (2017), 23--41,
DOI `10.1016/j.jlamp.2017.08.001`, builds cellular automata whose rules depend
on equality patterns of names.  [Primary publisher page](https://www.sciencedirect.com/science/article/pii/S2352220816301730)

Its alphabet is a nominal set and its output copies or creates names.  It does
not apply the binary adjacent-equality indicator, does not enter Rule 153
after one step, and does not provide any CEF clock or fibre spectrum.  This is
a conceptual neighbour, not a direct owner.

## What remains after external subtraction

The residual conjunction is owner-thin but nonempty:

1. a genuinely q-ary, equality-invariant first step with exact source
   multiplicity `chi_q(c)` and exactly the unit-mask support holes;
2. the q-weighted depth census and sharp last shell for this literal front;
3. all-target q-weighted affine fibres, with two evaluated classifications:
   time two by integrated radius and time `n/2+1` by half-word weight;
4. exact target-class multiplicities, q-dependent fibre values, and recovery
   of `(q,n)` from the functional graph.

The two V2 spectra use classical code structures, but neither Zhao nor the
Rule-102 sources perform the nonlinear `chi_q` pullback or target-syndrome
census.  That distinction closes the old owner-reduction objection only for
the stated special times; it does not support a claim of a new general code
or cellular-automaton theorem.

## Internal P1--P161 collision attack

| nearest occupied paper | shared surface | decisive separation |
|---|---|---|
| P63, rank-one XOR inverse radius | the same nearest-neighbour binary derivative `D` | P63 restricts `D` to infinite rank-one subshifts and studies exact inverse window radius.  It has no q-ary equality front, finite nilpotent ring, absorption census, or weighted target spectrum. |
| P90, Rule-184 particle dynamics | finite elementary CA, clocks, and zeta-style census | different local rule and conserved particle carrier; no conjugacy or proof transfer. |
| P98, equal-block-sum torsion shifts | finite-field cyclic modules and repeated-root algebra | P98 is a reversible constrained shift and owns the repeated-root proof engine.  CEF's residual is the nonlinear source pullback and q-weighted affine syndromes; all module-only claims are subtracted. |
| P109/P115, nilpotent image/Cartier dynamics | nilpotent flags, images, fibres, and depth shells | their carriers are subspace lattices and bounded polynomials.  Rank-nullity/chain products do not produce CEF's colour-mask multiplicity or radius/half-weight spectra. |
| P117, cyclic odd-run reversal | finite cyclic binary words and exact recurrence | the update is parallel odd-run flipping; no equality indicator or linear tail. |
| P138, palindromic-prefix XOR feedback | nonlinear indicator feedback followed by XOR language | its indicator is global prefix-palindromicity and its inverse is a sequential decoder.  Neither the map nor the fibre engine transfers. |

No exact literal or theorem-conjunction collision was found in P1--P161.
This is an internal bounded non-hit, not evidence of global novelty.

## Search record and ceiling

Queries covered exact/local variants of: `q-ary adjacent equality cellular
automaton`, `equality indicator feedback`, `Rule 102 periodic boundary power
of two`, `Rule 153 periodic boundary`, `Ducci map mod 2`, `repeated-root cyclic
code weight distribution`, `coset weight enumerator repetition code`, and
`nominal equality cellular automata`.  Primary texts were opened for the
strongest matches above.  Generic preimage algorithms and secondary CA pages
were not used to support a non-ownership claim.

**Owner decision:** `PASS_OWNER_THIN`.  The permissible claim ceiling is the
literal CEF conjunction and the two stated special-time spectra.  Claiming
novel Rule-102 dynamics, repeated-root code weights, a general affine-coset
theory, or absolute novelty would cross the owner firewall.

`HOLD_EXTERNAL` remains mandatory.
