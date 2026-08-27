# C202 results

## Theorem-level result

For every `D,r>0`, the profile equation

`D U'' + c U' + r U(1-U) = 0`

has a positive decreasing `1 -> 0` front, unique modulo translation, exactly
when `c>=2sqrt(Dr)`.  Reflection gives the unique increasing `0 -> 1` front
for `c<=-2sqrt(Dr)`.  Nonzero subcritical speeds have oscillatory zero-state
tails and therefore no `[0,1]` front.  At `c=0`, Hamiltonian endpoint energies
exclude the requested heteroclinic although periodic ovals exist.

The package also derives the back exponent and the supercritical, critical
and subcritical leading-edge laws, proves absence of nonconstant periodic
profiles for `c!=0`, and checks the exact Ablowitz--Zeppetella profile at
`c=5sqrt(Dr/6)`.

## Finite regression result

- 17 dimensionless speed classes;
- 340 exact vector-field rows;
- 25 invariant-triangle boundary rows;
- 6 Hamiltonian-oval rows;
- 9 exact-profile samples;
- 6 physical scalings.

The canonical payload SHA-256 is
`f02781c209fe741b81985cde6999aa0b1af727793461b4ee0082693226218b5e`.
The evidence-file SHA-256 is
`605176e6653d796b6f86b1df8493a64d07ef8bca0fa308b256bf970d27110243`
for 110,686 bytes.

## Route result

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, overall
`ROUTE_A_REJECTED`, Route B false, under
`NO_BAD_EULER_OR_ROOT_NUMBER`.

Finite rows are implementation sentinels.  The written trapping/phase-plane
proof and classical sources carry the continuum quantifiers.
