# Narrative report

## Outcome

The rational map at \(\mu=-2\) supplies a different Route-A dynamical subtype:
it is nonlinear, reversible, rational rather than polynomial, and exactly
area-preserving on its domain.  Its coordinate-swap reversor and quartic first
integral are verified as rational identities.

## Main finite result

The fixed equation has three valid complex solutions, of which only the origin
is real.  Clearing denominators in the second-iterate equations introduces the
factor \((x^2+1)^2\).  Those roots are not dynamics: they are precisely forward
poles.  Removing them leaves the fixed solutions and the real primitive cycle
\((1,-1)\leftrightarrow(-1,1)\).

At the two cycle points the derivative is the same quarter-turn matrix, so the
ordered two-step product is \(-I_2\).  This yields the exact local polynomial
\((1+z)^2\).  The fixed-origin control instead gives
\(z^2+4z+1\), demonstrating that one-step and two-step linearizations have not
been conflated.

## Evidence strength

The producer is independently checked with 66 assertions; a second SymPy path
uses Groebner elimination and 23 checks; replay is byte-identical; twelve
hostile mutations are rejected.  These facts support low-period algebra only.

## Route assessment

- `A1_PARTIAL_CERTIFIED`: exact birational identities and validated low-period
  rational witnesses only.
- `A2_FAIL`: no transfer operator or finite transfer owner.
- `A3_NOT_ADDRESSED`.
- `A4_FAIL`.
- Overall: `ROUTE_A_EXPLORATORY`.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
