# Frozen control receipt

Run date: 2026-08-26 UTC

Environment:

```text
Python 3.12.3
Linux x86_64
```

Command:

```sh
python3 code/verify_degree_pressure.py
```

Receipt:

```text
degree-weighted periodic identities: PASS (two profiles, n<=5, four weights)
pressure derivative/variance identities: PASS
fixed-point local-degree profile recovery: PASS
equal ordinary entropy / unequal degree pressure control: PASS
binary multifractal/Legendre identity and maximum: PASS
repeated-extremal endpoint/Legendre limits: PASS (profile (1,1,2,4,4), min mass 2, max mass 8)
ALL CHECKS PASS
```

- script SHA-256: `46f72e4559bf6f3465c5dc2674136fe26c31888ef727ca2c79a14308069509ca`
- periodic controls: profiles `(1,3)` and `(1,2,3)`, periods `1` through `5`, exponents `-1,0,1,2`, exact rational arithmetic
- profile controls: repeated and nonrepeated fibre sizes recovered from fixed-point degree histograms
- spectrum controls: five interior exponents for `(1,3)`, with direct entropy and Legendre values compared to `1e-12`; repeated-extremal profile `(1,1,2,4,4)`, with exact endpoint masses `1*2=2` and `4*2=8` and stable limiting Legendre values `log(2)` and `log(8)` compared to `1e-12`

The computations are regression evidence only. The manuscript proves the infinite pressure, equilibrium, periodic, profile-recovery, zeta, and Bowen-spectrum statements directly.
