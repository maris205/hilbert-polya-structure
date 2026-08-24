# Narrative report — C117

The central design choice is chronology.  A Markov transition from environment
`i` to `j` is followed by application of `F_j`; this turns the transition
matrix and local Jacobians into a unique block operator rather than an
ambiguous averaged map.  The same rule lifts exactly to symmetric quadratic
moments.

The finite operators are genuinely source-owned because their spaces, bases,
and actions arise directly from the frozen tangent cocycle.  Their limitation
is equally important: they live at one common fixed point and say nothing by
themselves about the global nonlinear random dynamics.  The stationary
rank-one gap provides a useful control, showing why a naive average-map
replacement loses switching variance even at degree two.
