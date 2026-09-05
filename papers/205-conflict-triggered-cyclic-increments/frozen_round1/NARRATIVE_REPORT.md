# P205 — research narrative

The map changes a colour only in response to an equal-colour neighbor. An
initial conflict cannot be repaired by synchronous equal increments: its
edge stays conflicted. This makes activation irreversible, but not an
unweighted Boolean flood. Two sources can have the same active set and
different next active sets because the colour wait differs.

An activated vertex advances at every future step; a not-yet activated one
still has its initial colour. Their first meeting has the directed residue
delay of those initial colours. Competing seeds are handled by the two
shortest-path inequalities, not by assuming a unique front. The last finite
arrival is the actual entrance into the recurrent core, with sharp path
sources for every n≥3 and q≥3.

The inverse instead starts with a target and asks which vertices advanced.
Three independent edge constraints identify exactly the valid active masks:
covering target equalities, an internal equal-colour neighbor for each active
vertex, and closure under target predecessor colours. These constraints
lead to a total-cover upper bound; constant targets attain it. An elementary
static proof plus connected monochromatic equality transfer identifies stars
and the exceptional triangle. The static objects and extremal tools are
not themselves claimed as new.

The proof is deductive and all-parameter. The original standalone verifier's
actual canonical contains 1,029,769 finite assertions; the independent
candidate checker contains 7,530,194. Neither check count proves an all-size
claim or replaces the still-required manuscript reviews. No all-time inverse,
general cover-counting efficiency or global novelty is asserted.
