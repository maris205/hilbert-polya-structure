# Independent h-adic verification of the period-12 counterexample

2026-09-06. This verifies a finite exact counterexample. It is not an
ordinary all-period count, a new paper, or a novelty certificate.

For f(x)=x+x^4 over F_3 and

    h=x^4+2x^3+2,       Q=x^3+2x^2+x+1,

the root coordinator independently implemented polynomial arithmetic over
F_3 in the Python standard library. It does not use the author's F_81
implementation, translated Taylor jets, output file, or FLINT dependency.
The degree-4^12 iterate is never constructed: every step is reduced modulo
h^13, a polynomial of degree 52.

The executed check establishes:

1. h is squarefree and irreducible: gcd(h,h')=1,
   x^81=x mod h, and gcd(h,x^9−x)=1.
2. f^12(x)=x mod h, while f^d(x)−x is nonzero mod h for every proper
   divisor d=1,2,3,4,6 of 12. The orbit therefore has least period 12.
3. f^12(x)−x=h^12 Q mod h^13 and Q is nonzero mod h.

Since h is squarefree, each of its roots consequently has first-return
local multiplicity 12, not 3. Its first-return weight divided by the
characteristic is 4, not 1. The equality of this certificate with the
author's separately computed local jet is an actual independent agreement;
it does not establish a universal pattern beyond the certified example.

Reproduction, from the repository root:

```sh
python henon_dynamics/continuation_c407_c408_round3/ROOT_WILD_CHECK.py
```

Actual execution on 2026-09-06: exit status 0; all assertions passed;
`minimal_period=12`, `h_adic_valuation_f12_minus_x=12`, and
`h_adic_first_coefficient_ascending=[1,1,2,1]`.
The script prints the complete 12-point orbit and all proper-divisor
remainders so the certificate is auditable without a large census.

This new check reads or writes none of the 179 sealed round-2 files.
