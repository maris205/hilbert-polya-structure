# Narrative report

## Problem

Crossing components canonically partition the endpoint set of a rooted chord
matching into noncrossing even blocks.  Pairing consecutive endpoints inside
each block gives a natural cut-dependent retraction, but idempotence and its
Catalan image are mechanically weak.  The paper asks the harder inverse
question: how many sources map to each particular noncrossing target?

## Structural turn

The correct coordinate is not the crossing graph of the target (which is
edgeless), but its nesting forest.  A component-support block can contain
section chords only from one immediate-sibling list.  If two alleged parents
were different, the inner one would be a strict intermediate container
between a section chord and its alleged outer immediate parent.  Its selected
siblings form a noncrossing block in that list.  Conversely, for a child
selected by a parent block its descendant interval is an exact gap; for an
unselected child its entire support is a strict subinterval of one gap.
Leaf-to-root induction, repeated at the virtual root, then assembles the
independent groupings without crossings or accidental identification.  A
connected chord matching on each resulting endpoint block restores exactly
one crossing component.

This yields a genuine all-size inverse, not an aggregate recurrence.  The
fibre over `T` factors as a product indexed by the virtual-rooted nesting
forest.  The proof explicitly checks forward localization, converse global
assembly, connected decoration and mutual inversion.

## Second engine

The factor `a_d` is already-owned A111088 data, so its enumeration is not the
paper's value.  What remains useful is an elementary strict inequality:
juxtaposition injects `A_i×A_j` into `A_{i+j}`, while a one-block all-crossing
decoration is missing.  Since all child degrees sum to `n`, the product is
maximal only when the virtual root has all `n` children.  This forces the
consecutive target and proves unique maximality.

## Subtraction and firewall

All Catalan, connected-component, transform, full-wiring, parallel-part and
uncrossing facts receive zero contribution credit.  For the endpoint
partition into matching chords, every nonempty top-level or
immediate-sibling list is exactly an Igusa parallel set (Definition 1.7), and
Proposition 1.8 owns the compatible-merge criterion.  A degree-zero list is
only the singleton `A_0` bookkeeping factor; none of these static facts is
residual.  The paper
corrects the uncrossing attribution to Thomas Lam.  Alman--Lian--Tran's
Theorem 4.1.6, Remark 4.1.7, Theorem 4.1.8 and Theorem 4.2.1 own the all-size
full-wiring sequence neighborhood.  Internally, P110 is cyclic partition
shift--join dynamics and shares only a narrow chord witness, P120 uses a tree
coordinate, P123 is componentwise, and P117/P122/P126 have
run/composition fibre products; none has this literal map, but those generic
silhouettes are not claimed as value.

## Claim ceiling

The residual claims are only the target-wise sibling inverse/product and the
unique largest fibre for this fixed-cut section.  The OGF is formal; no
analytic or asymptotic statement is made.  No novelty, priority, canonical
unrooted map or external-release claim is made.  Status remains
`HOLD_EXTERNAL`.
