# Source audit and evidence boundary

## Inputs

The only mathematical input is the explicitly frozen rational map with
\(\mu=-2\).  Every displayed identity is derived inside the package with exact
SymPy arithmetic and then recomputed by an independent checker that does not
import the producer.

No external paper, table, database, numerical orbit list, or web source is
used.  Consequently the manuscript makes no historical priority or novelty
claim and carries no bibliography.

## Domain audit

- Forward map: undefined over \(\mathbb C\) on \(x^2+1=0\).
- Inverse: undefined over \(\mathbb C\) on \(y^2+1=0\).
- The three fixed points have forward denominators \(1,-2,-2\).
- The two real cycle points both have forward denominator \(2\).
- The eliminated roots \(x=\pm i\) have zero forward denominator and are
  rejected before orbit counting.

## Claim boundary

The evidence owns exact rational identities and validated low-period points
only.  The local polynomial \(\det(I-zP_2)\) is not a transfer determinant.
There is no function space, trace-class or nuclearity estimate, global symbolic
coding, or tail control.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
