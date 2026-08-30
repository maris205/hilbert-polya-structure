# C241 test report

The validation suite is producer-independent at the schema and arithmetic
layers.  The recursive checker verifies exact branch fractions, the `(0,1]`
image convention, all 780 word itineraries/fixed points/multipliers, necklace
Möbius counts, 88 weighted rows, the corrected `1/M` tail, the `s=1/2`
divergence label, finite formal products, citations, scope flags, and the
`A4_FORMAL_HINT` route tuple.  SymPy supplies independent rational identities;
replay compares fresh producer bytes; hostile mutations include repaired
payload hashes.

Expected current outputs (regenerated at release) are:

* checker: `PASS` with an assertion count reported by the executable;
* SymPy: `PASS` with 1,585 symbolic identities;
* byte replay: `PASS`;
* hostile mutations: `PASS 56/56` (including repaired-digest semantic cases);
* LuaLaTeX: two settled passes per round in two fresh directories, embedded
  fonts, no retained build sidecars, and deterministic round-2 bytes.

The scope firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`; no target prime/zero,
Euler-factor, root-number, automorphy, target-divisor, functional-equation,
Hilbert–Pólya, or Route-B claim is tested or made.
