# Verification plan: HCS-C363

1. Freeze and hash the Route-A YAML in raw and canonical semantic forms.
2. Enumerate 21 exact mass/moment virial receipts across the subcritical,
   critical, and supercritical regimes.
3. Enumerate 21 exact free-energy scaling-sign receipts.
4. Check nine rational samples of the critical profile, Poisson equation,
   enclosed mass, and zero stationary flux.
5. Check nine samples of the normalized radial cumulative equation.
6. Reconstruct every cell in an independent checker that imports no producer.
7. Use SymPy to derive the Poisson, stationary-flux, mass, infinite-moment,
   radial, virial, scaling, and pair-symmetrization identities independently.
8. Require two isolated producer/checker copies to be byte identical.
9. Repair payload hashes after hostile semantic mutations and require all to
   fail; also attack strict JSON/YAML behavior.
10. Require every executable to refuse `python -O` and `python -OO`.
11. Compile three substantive revisions twice at epoch `1788480000`; require
    byte determinism, settled logs, embedded/subset fonts, clean extracted
    text, and successful page rasterization.
12. Enforce exactly 27 payloads plus one self-excluded manifest.

No finite grid is used to infer a continuum PDE theorem.
