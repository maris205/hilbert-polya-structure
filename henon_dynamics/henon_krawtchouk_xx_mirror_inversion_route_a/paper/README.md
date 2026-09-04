# Paper build — HCS-C366

`main.tex` is one conditional source.  The release script builds revision
rounds 0, 1, and 2 twice each in fresh directories using LuaLaTeX at frozen
epoch `1788480000`; byte equality is required. Round 0 owns the one-particle
propagator, Round 1 adds the exact Fock-space phase and Gaussian-polynomial
recurrence, and Round 2 adds the exact uniform-field revival conditions plus
all boundary and Route-A firewalls. `main.pdf` is byte-identical to Round 2.

No figure was generated because the proof is an exact representation and
exterior-power calculation; a decorative chain drawing would not carry a
claim that the formulas do not already state more precisely.
