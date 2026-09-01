# Narrative report — Boolean row-inclusion residual dynamics

## Problem

On all (n\times n) Boolean matrices, compare each ordered pair of row supports by inclusion and use the resulting comparison matrix as the next state.  The operation is the familiar relational self-residual, so its one-step preorder property is not itself a contribution.  The question is what happens when this standard construction is iterated as a literal finite self-map and whether every one-step fibre can be described exactly.

## Main result

Every first image is a labelled preorder, every labelled preorder occurs, and on a preorder the map is transpose/order reversal.  Hence (T^3=T).  Nonpreorders have tail one, equivalence relations are precisely the fixed states, and all other preorders form strict transpose two-cycles.  This yields all temporal fixed-set counts and the dynamical zeta function.

For the inverse problem, quotient a target preorder by mutual comparability.  Rows in one quotient class must coincide, and the distinct quotient rows form an induced order embedding into the Boolean lattice (B_n).  Encoding each Boolean coordinate as an upper set gives an inclusion--exclusion formula over all missing ordered pairs.  It counts the fibre over every preorder target; nonpreorder targets have empty fibre.

## Evidence

An exact verifier exhausts every Boolean matrix through (n=4).  It checks image/preorder equality, transpose action, (T^3=T), the Bell fixed census, mass conservation, and the quotient-poset inclusion--exclusion formula for every image target.  The discovery control recorded 264,673 assertions; the paper-local verifier independently replays the same theorem interfaces.

## Ownership boundary

Relational residuation, the self-residual preorder, principal upper sets, finite-preorder enumeration, equivalence-relation/Bell enumeration, induced poset embeddings into Boolean lattices, and generic inclusion--exclusion are credited background.  A bounded search found no direct owner of the full iterated-plus-inverse conjunction, but that non-hit does not establish novelty.  The manuscript is anonymous and `HOLD_EXTERNAL`.
