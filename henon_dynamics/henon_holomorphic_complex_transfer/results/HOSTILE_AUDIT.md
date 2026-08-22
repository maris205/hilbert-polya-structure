# Hostile audit

The mutation test edits the weighted trace, resultant, degree growth, verdict,
and Jacobian fields. Every edit changes the canonical evidence object; the
original evidence is restored before the test exits.
