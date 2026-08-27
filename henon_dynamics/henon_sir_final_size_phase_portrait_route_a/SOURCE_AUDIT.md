# Source audit

## Locked sources

1. W. O. Kermack and A. G. McKendrick, “A contribution to the mathematical
   theory of epidemics,” *Proceedings of the Royal Society A* 115 (1927),
   700–721. DOI: `10.1098/rspa.1927.0118`.
2. A. G. Pakes, “Lambert's W meets Kermack–McKendrick epidemics,” *IMA Journal
   of Applied Mathematics* 80 (2015), 1368–1386. DOI:
   `10.1093/imamat/hxu057`.

The Royal Society source owns the classical epidemic-model, threshold and
final-size ancestry.  Pakes explicitly owns a detailed Lambert-W treatment of
the final-size equation and its branches.  C198 does not claim discovery or
priority for the equations, invariant, threshold, peak or Lambert formula.

## Package contribution

The contribution is a convention-locked, all-parameter dynamical synthesis:
physical-to-dimensionless conjugacy, phase portrait, boundary cases, peak,
branch-selected final state, time quadrature, sensitivity, equilibrium-line
linearization, monotonic no-recurrence theorem, two independent executable
branch oracles, and strict Route-A evaluation.

## Verification record

- The Royal Society publisher record fixes the 1927 authors, journal, volume,
  pages and DOI.
- The Oxford Academic record fixes the Pakes title, volume, pages, DOI and the
  article's explicit Lambert-W final-size purpose.
- All formulas used by C198 are independently differentiated or solved in the
  package; source citation never substitutes for a convention check.

## Safety and limitations

This audit is not an exhaustive systematic review.  The package does not use
or interpret real outbreak data, estimate parameters, compare interventions,
or give medical advice.  Vital dynamics, latency, heterogeneity, networks,
stochasticity and reinfection change the model and are outside the frozen
owner.  No global literature-priority or external-review claim is made.
