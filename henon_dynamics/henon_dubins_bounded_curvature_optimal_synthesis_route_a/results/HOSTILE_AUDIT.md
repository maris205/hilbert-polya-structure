# C310 hostile audit

Attacks alter the turning radius, target pose, winning word, feasibility
boolean, tangent discriminant, individual segment, total length, endpoint
residual, word coverage, candidate count, Route-A tuple, and scope flags.
Each semantic mutation receives a repaired payload hash before checking.

Parser attacks add duplicate keys, nonfinite JSON, wrong top-level types,
duplicate or anchored YAML, scope escalation, and Route-B activation.  All 30
must be rejected.  Special attention is given to the zero straight segment
and `CCC` cosine endpoints, where a plausible but inconsistent `atan2(0,0)`
choice otherwise changes the parameter triple.
