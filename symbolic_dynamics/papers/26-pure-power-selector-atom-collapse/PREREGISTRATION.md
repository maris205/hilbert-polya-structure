# Preregistration — SD-C28

**Freeze date:** 2026-08-14  
**Candidate:** SD-C28  
**Primary family:** Symbolic Dynamics  
**Zero-data firewall:** active  
**Review loop:** excluded by instruction  
**Experiment status at freeze:** theorem and exact-prototype protocol frozen;
no unexecuted count is reported as evidence

## 1. Research question

Can a source-derived cyclic branch-incidence or homological construction on a
shared logarithmic-code renewal assign coefficient one to every nonempty
monochromatic return word and zero to every mixed word, at every repetition,
without compiling into one observable recurrent block per supplied color?

The primary object is the wordwise cyclic series `chi_m`, not its commutative
abelianization.  Finite recognizable, ordinary trace, graded trace,
support-exterior, bar/Hochschild, and countable holomorphic-tensor realizations
are tested separately.

## 2. Primary hypotheses

**H1 — exact positive selectors.**  The reduced-support exterior Euler
coefficient and the rank-`m` coordinate-projector character both realize the
pure/mixed rule for every positive word and every repetition.

**H2 — Hankel lower bound.**  Under `chi_m(1)=m`, the Hankel rank is exactly
`m`; under `chi_m(1)=0`, it is exactly `m+1`.  Consequently any recognizable
implementation needs memory proportional to the supplied color count.

**H3 — syntactic atom algebra.**  The observable syntactic algebra is `C^m`
under the character convention and `C^(m+1)` under the language convention.
The extra summand is dormant and determinant-invisible.

**H4 — semisimple character collapse.**  Wordwise equality of a finite
ordinary or even `Z/2`-graded trace character with `chi_m` forces one net
one-dimensional color character per label after semisimplification.  Common
even/odd sectors, dormant sectors, and radicals are the only invisible
freedom.

**H5 — determinant collapse.**  H4 forces

\[
 \operatorname{Ber}\!\left(I-z\sum_i x_iA_i\right)
 =\prod_i(1-zx_i)
\]

as a formal identity.  Tensoring the character with the Paper25 de Rham
sector preserves this atom/color product.

**H6 — literal-block overclaim is false.**  Strictly triangular radical
extensions can connect color sectors without changing any word trace.
Therefore only semisimplification, virtual character, syntactic algebra, and
determinant are classified.

**H7 — aggregate pencil traces are insufficient.**  Even equality of all
power traces of a commuting variable pencil can hide cancellation between
oriented necklaces.  The frozen three-color matrix-unit adversary separates
the words `012` and `210`.

**H8 — canonical homology collapses.**  Free or polynomial bar complexes
retain mixed cyclic information.  The separable algebra `C^m` removes it, but
has only its `m` atom classes in degree zero and no positive Hochschild
homology.

**H9 — countable analytic ceiling.**  Coordinate projectors on `ell^2(I)`,
tensored with the holomorphic de Rham sector, give an honest trace-class
graded determinant exactly on the `ell^1` weight domain.  This is a countable
direct atom-block architecture, not a finite-source selector.

**H10 — Route closure.**  H1–H9 give a genuine A2 determinant but fail A1;
without same-object continuation or a self-adjoint spectral realization, A3
and A4 fail and Route B stays locked.

## 3. Exact audit protocol

### E1 — projector word census

For finite colors `m=1,...,7` and all positive words through the frozen length
cutoff, compare exact projector-product traces with the support oracle.  Check
cyclic rotation and repetition invariance.

### E2 — Hankel and empty-word census

Construct finite Hankel witness matrices under both empty-word conventions.
Verify ranks `m` and `m+1` exactly, and verify that the added language
character is killed by every letter.

### E3 — radical invisibility

Add deterministic strictly triangular extensions to projector realizations.
Check every frozen word trace while also certifying that the matrices need not
be simultaneously diagonal or an orthogonal direct sum.

### E4 — graded virtual-character census

Add identical even/odd semisimple sectors and dormant zero-action sectors.
Verify exact wordwise supertraces, all power coefficients, and the surviving
one-net-color virtual character.

### E5 — aggregate adversary

Use `R_0=E_12`, `R_1=E_23`, `R_2=E_31` in an even sector and transposes in an
odd sector.  Verify the aggregate commuting-pencil power identities, then
certify the oriented word discrepancy

\[
 \operatorname{Str}(012)=1,\qquad \operatorname{Str}(210)=-1.
\]

This test must fail any evaluator that abelianizes before the wordwise gate.

### E6 — support exterior and Hochschild controls

For supports of sizes one through nine, compute the alternating exterior
dimension `(1-1)^(k-1)` exactly.  Record that its fiber depends on the
completed support.  Separately verify the finite separable algebra has only
the supplied primitive idempotents as degree-zero atom classes.

### E7 — determinant identities

For symbolic finite inventories, compare the trace-log coefficients of the
projector and graded realizations with `product_i(1-z x_i)`.  Keep ordinary
determinants and graded ratios in separate ledgers.

### E8 — countable trace-class control

Use exact positive summable prefixes, including `n^{-2}`, to verify nonzero
power traces and the finite product identities.  The infinite statement is
decided analytically by `sum_n |b_n|<infinity`, not by a numerical cutoff.

### E9 — arbitrary-inventory and marker controls

Run the same selector on prime, composite, square, Fibonacci, and deterministic
hash inventories.  All must pass, producing the classification
`SELECTOR_TAUTOLOGICAL | PROVES_TOO_MUCH`.  Retain `u^ell(n)` at digit scale
and use `z` only for completed returns.

### E10 — integrity

Run exact self-tests and generate two clean snapshots.  Require byte identity
for independently integrated code/results artifacts and record SHA-256
digests.  That certificate does not cover manuscript or documentation files.
No network input, stochastic fitting, floating inference, or zero data are
admissible.

## 4. Decision rule

`GO_NONATOMIC_SELECTOR` requires an exact wordwise selector whose observable
memory does not grow with the supplied colors and whose analytic tensor is not
unitarily/determinant-equivalent to disjoint color blocks.

- `EXACT_SELECTOR_ATOM_COLLAPSE`: exact coefficients, syntactic algebra
  proportional to colors, and atom-product determinant;
- `AGGREGATE_ONLY_REJECTED`: commuting-power sums pass but a necklace-resolved
  word fails;
- `SUPPORT_RULE_NONSTATIONARY`: exact exterior coefficient with the fiber
  chosen from the completed word;
- `HOMOLOGY_ALREADY_ATOMIC`: the successful canonical algebra is `C^m` with
  only degree-zero atom classes;
- `SELECTOR_TAUTOLOGICAL | PROVES_TOO_MUCH`: arbitrary inventories pass
  unchanged.

The frozen expected verdict is `EXACT_SELECTOR_ATOM_COLLAPSE`, yielding

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

No universal impossibility is preregistered for infinite nonrecognizable
memory, unbounded derived categories, odd-letter theories, or nonlocal
completed-orbit weights.
