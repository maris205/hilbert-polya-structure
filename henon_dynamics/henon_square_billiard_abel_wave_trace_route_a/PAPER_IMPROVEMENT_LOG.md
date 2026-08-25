# C157 paper improvement log

No external or cross-model reviewer was used or claimed.  Both rounds are
genuine internal theorem, scope, and presentation audits without numerical
scores.

## Pre-manuscript derivation audit

The Fourier constant and quadrant multiplicity were rederived before drafting.
With the fixed `exp(-2*pi*i*m dot x)` convention, the full radial transform is
`2s/[pi(s^2+4|m|^2)^(3/2)]`; division by four for the positive quadrant gives
the outer `s/(2pi)`.  Four nonaxis sign lifts then restore `2s/pi` for each
ordered positive primitive/repetition pair.  This prevented a factor-of-two
error from entering the paper.

## Round 0 to round 1

The baseline PDF described the interior branch points but did not inventory
all analytically distinct boundary contributions.  It also quoted numerical
agreement without exposing the deterministic error budget.

**Fix:** separate the Weyl zero mode, dual-axis branches, interior clean-family
branches, and boundary-subtraction simple poles.  State that axis branches and
poles may coincide but neither have the same singularity type nor are claimed
to cancel.  Add the primal geometric tail and the two-term Epstein-accelerated
dual tail bound.

## Round 1 to round 2

The second review requested a clearer source/target boundary and the mandatory
academic-paper front/back matter.

**Fix:** clarify that this is exactly the source Dirichlet Abel trace but not
an isolated-orbit determinant or target identity; add independently phrased
English and Chinese abstracts, six keywords in each language, and compact data,
ethics, contribution, conflict, funding, and AI-use declarations.  LuaLaTeX
manual CJK line breaks preserve a warning-free two-page layout.

## Final audit

Producer, independent checker, SymPy, byte replay, hostile mutations,
fixed-epoch double builds, embedded fonts, clean logs, extracted text, visual
inspection, Route-A schema, scope flags, and exact manifest closure all pass.
An independent internal release audit then corrected the second sentinel's
three-significant-digit display from `3.93e-12` to `3.92e-12`, closed every
claim-bearing nested key ledger, and distinguished rigorous analytic
truncation envelopes from deterministic 55-decimal centers with a `1e-34`
serialization/rounding comparison margin.
