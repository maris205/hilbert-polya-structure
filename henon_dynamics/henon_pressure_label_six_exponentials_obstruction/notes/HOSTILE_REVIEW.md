# Hostile proof review

Status: **PROVABLE AS STATED**.

## Attacks performed

1. Checked that the period-three radical sequence satisfies all three cyclic
   recurrence equations and is primitive.
2. Printed the exact survivor intervals and adjacency transitions so that
   survivor membership is not inferred from a decimal catalog.
3. Recomputed the three minimal polynomials and both quartic discriminants
   from independent trace definitions.
4. Audited the ramification ladder separately at \(5,11,29\), including the
   odd valuation of the period-three relative discriminant over
   \(\mathbb Q(\sqrt5)\).
5. Checked that degree \(32\) is the full product degree, so the factorwise
   inversion maps genuinely extend to the compositum.
6. Checked the exact order of the Six Exponentials inputs: three independent
   logarithms and the independent pair \((1,h)\).
7. Split rational and irrational \(h\) before invoking transcendence; no
   algebraicity assumption on the pressure root is made.
8. Kept the conclusion at “at least one of three labels is nonprime”; the
   proof does not identify the exceptional orbit for transcendental \(h\).

## Independent exact sentinel

An independent SymPy construction from the three traces, without importing
the HCS-P48 implementation, returned one irreducible primitive-element factor of
degree \(32\). The quartic discriminant factorizations also matched.

## Remaining boundary

The review does not promote HCS-P48 to a collective arithmetic trace theorem.
Prime ideals, Galois packets, cyclic resultants and distributional traces
remain outside the no-go.
