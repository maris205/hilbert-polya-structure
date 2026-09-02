# Executable evidence plan

## Frozen inputs

- baseline `7fbe9db30cc460a82883533d7cfb2edd988c5b65`
- date `2026-09-02`, epoch `1788307200`
- evaluator v0.2.0, SHA-256
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
- scope `NO_BAD_EULER_OR_ROOT_NUMBER`

The producer records rational Fourier–Hermite cells for fluxes `1/3`, `1/2`,
and `2/5`; finite-cutoff high-precision heat receipts; zero-flux
nonresonant multiplicities and counts; source-zeta values; and symmetry
boundaries.  The analytic manuscript proves the infinite formulas.

The checker imports no producer code.  It reconstructs heat values by summing
individual oscillator eigenvalues rather than using the producer's
`1/(2sinh)` formula, independently enumerates odd divisors and level counts,
and checks the separated double-index zeta sum.  Exact nested schemas reject
duplicate keys, nonfinite constants, bool/int confusion, noncanonical
fractions, incomplete/duplicate grids, and altered theorem/proof/spectral
contracts.  A dedicated repaired-hash attack changes the free-line a.c.
multiplicity from two back to one and must fail.

The evaluation YAML is loaded with a duplicate-rejecting safe loader that
keeps the date scalar as a string.  Its complete recursive key/type/value
tree and canonical semantic SHA-256
`e3ff56c62d1830a03a8a0b2a7d33acf73d6d997de4d9c872e6f6ff278d98adae`
are mandatory.  Twenty-one YAML attacks exercise duplicate and unknown or
missing keys, tuple/verdict/Route-B changes, scope and axis drift, exact-type
confusion, and a non-object root.

Release requires three substantive rounds and six fresh deterministic
two-pass LuaLaTeX builds, settled warning freedom, all-font embedding and
subsetting, pages/text/hash gates, and exact 27-payload/28-physical closure.
