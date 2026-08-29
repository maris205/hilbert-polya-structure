# C238 results

The receipt contains 8 exact rest/capture rows, 8 arbitrary signed-velocity
phase rows, 5 static-threshold/release rows, 4 conservative harmonic rows,
and 5 first-arc work rows.  The producer and checker agree on the positive and
negative shifted centers, the `atan2` phases, the partial first arc, the
remaining integer half-cycles, and the finite stopping turn/time.

The independent symbolic audit verifies the two slip energy laws, threshold
selection, turning map, radius/center identities, and harmonic solution.  Byte
replay is identical in two fresh trees; the hostile suite rejects 28/28
mutations, including the exterior-rest center-sign and partial-arc fields.

This is a source-local nonsmooth-mechanics theorem.  It is not an arithmetic
primitive-orbit construction, target determinant, or Hilbert–Pólya operator;
Route-A is `ROUTE_A_REJECTED` and Route B is disabled.
