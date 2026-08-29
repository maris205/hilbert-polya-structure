# Exact control results — P99

Command:

```text
python3 code/verify_shear_sublattices.py
```

Result on 2026-08-29 UTC:

```text
Exact verification: unipotent shear on fixed-index sublattices
HNF/action lane: N=1..120, 11973 canonical states checked
general dynamics lane: 120 cycle censuses, 14520 fixed-time cases, 7260 Mobius cases
prime-power lane: 40 pairs (p,r), 680 valuation/unit cases
regression lane: six inventories and the N=8 fixed sequence checked
PASS: 93,912 exact assertions
```

The 93,912 registered assertions cover:

- 11,973 canonical HNF states across `1<=N<=120`, including determinant,
  coordinate range, raw shear, canonicalization, and mutual lattice
  containment;
- complete literal permutation-cycle enumeration at all 120 indices;
- exact state accounting and uniqueness of the maximal `N`-cycle;
- 14,520 fixed-time cases through `2N`, each checked both by literal phase
  enumeration and by reconstruction from cycle data;
- 7,260 Möbius inversions, including divisibility and zero periods;
- 40 prime-power parameter pairs for four primes through exponent 10;
- 680 prime-power valuation/unit cases, which test that the staircase depends
  on `v_p(n)` rather than the coprime unit; and
- six frozen cycle-inventory examples plus the first eight fixed counts at
  `N=8`.

All evidence-bearing calculations use Python integers and the standard
library.  There is no random seed, floating-point tolerance, computer algebra
black box, or numerical eigenvalue used as proof.  The literal output is also
stored in `code/verification_output.txt`.
