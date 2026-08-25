# C156 test report

The deterministic producer and byte replay pass with exact evidence SHA-256
`06791bf5734a48d0fe84d0e752e5d156172e637fe9a6a5e29792dfb3b2637b40`.

- Full producer-independent checker: **507,331 assertions**.
- Independent SymPy path: **1,842 checks**.
- Hostile suite: **54/54 rejected**, consisting of 53 repaired-hash semantic
  mutations and one stale-hash control.

The checker reconstructs all 314,151 local elements by direct numerator
cocycle iteration, verifies all local denominators and histograms, and checks
191,597 cross-primary polarization pairs.  SymPy derives the correct cocycle
and rotation polarizations, recomputes Smith/Hermite forms through `n=14`,
rebuilds all primary histograms through `n=10`, and closes the all-iterate
parity proof by recurrence-state analysis rather than a long finite prefix.
