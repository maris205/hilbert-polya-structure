# Hostile audit — C107

Six mutations were applied to the frozen hole, matrix, determinant, trace, and
primitive-count fields.  All six structural edits changed the canonical
evidence object and were detected by the mutation gate (`6/6`).  This script
does not itself invoke the checker or replay command; those are run separately
in the package test sequence.  The audit does not test claims outside the
finite symbolic object.
