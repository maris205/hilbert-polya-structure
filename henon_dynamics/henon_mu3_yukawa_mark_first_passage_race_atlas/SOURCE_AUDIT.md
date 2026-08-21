# Source audit

C91 reads only the canonical C75 closure-incidence receipt, the C83 stopping
time receipt, the C85 subgroup-poset receipt, and the C88 subgroup
first-passage atlas plus their prefreeze manifests.  All eight source bytes
are bound by SHA-256 in the producer and independent checker.  C75/C83/C85
are rebound through C88's authority chain, and the C88 hit bitsets are decoded
directly rather than copied from a C91 intermediate.

The source group is the finite additive model `Z/9 + Z/3 + Z/2`, with sixteen
named labels, twenty actual subgroup targets, and 65,536 prefix supports.
The only claim is the exact finite uniform-permutation race law.  Scope
firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
