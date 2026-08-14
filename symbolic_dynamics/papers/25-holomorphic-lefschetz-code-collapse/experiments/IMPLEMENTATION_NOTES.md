# Implementation Notes — SD-C27

## Source/evaluator firewall

`code/sdc27_holomorphic_lefschetz.py` contains only gamma coding, affine digit
composition, exact polynomial pullbacks, de Rham algebra, determinant
identities, and necklace combinatorics. Inventory predicates live only in
`code/sdc27_evaluator.py` and are applied after the compiler is frozen.

## Affine ordering

Starting with the identity map, each code digit applies its frozen map after
the current affine map. If the current map is (a+qz), the next state is
(a/2+t_b+(q/2)z), with (t_0=-1/4), (t_1=1/4). Hence every word has
derivative (2^{-\ell}), and the translations retain ordered digit data.

## Exact polynomial convention

On the zero-form monomial basis (1,z,ldots,z^N), column (k) is the
expansion of ((a+qz)^k). On one-forms the coefficient degree is at most
(N-1) and the pullback has the additional factor (q). The differential
matrix has entry (D_{k-1,k}=k). Every matrix and characteristic polynomial
uses exact SymPy rationals.

The all-order certificate is

`det(I-zL0) = (1-z*sum(weights))*det(I-zL1)`.

Power supertraces through eight are readable independent checksums, not a
replacement for the characteristic-polynomial identity.

## Ownership firewalls

- Graded object: `det(I-zL0) / det(I-zL1)`.
- Ordinary ungraded block: `det(I-zL0) * det(I-zL1)`.
- Return marker: one `z` per completed codeword.
- Digit marker: `u^ell(n)` for the original binary history.

All four expressions are materialized separately.

## Reproducibility

The runner disables bytecode and pytest caches, fixes `PYTHONHASHSEED=0`,
performs two complete generator/test/analysis passes, and compares every code
and result byte except self-referential audit files. JSON keys and CSV order
are fixed; runtime and timestamp metadata are forbidden. Provenance remains
pending until the external two-stage Git freeze.

