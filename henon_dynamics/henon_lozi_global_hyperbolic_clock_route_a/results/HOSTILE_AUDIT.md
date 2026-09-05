# Hostile audit

26 repaired-hash changes cover metadata, forbidden claims, route promotion,
word omission/duplication, rational coordinates, parameters, periods, signs,
monodromy, trace weights, necklaces, reversal, primitive counts, sign margins,
noncanonical fractions, boolean substitution and unknown fields. The final
two attacks replace a false scope flag and the false Route-B flag with the
integer zero after repairing the payload hash; both must fail strict typing.
Two JSON and eight YAML serialization attacks are rejected. YAML duplicate
keys, implicit dates, aliases, merge keys and unknown fields cannot change
the frozen evaluation. The last pass rejected 36 of 36 actual attacks.

Independent final review actually reproduced acceptance of those two integer
zeros before the repair: Python mapping equality conflated False and 0.
The final release source gate already rejected them, but the standalone
checker did not. Explicit boolean identity checks now close that checker
gap. This is a validation bug and correction, not a mathematical result.
