# Broadened candidate card — `AFC-20260914-PWF01`, version 1

| Field | Frozen definition / owner | State |
| --- | --- | --- |
| Carrier | discrete union `W=disjoint_union_(k>=1) W_k`, `W_k=(Z/P_k Z)^times`, `P_k=p_k#` | frozen |
| Packet action | `R(k,a)=(k,next_k(a))`, where `next_k` is cyclic successor in the ordered reduced residues mod `P_k` | frozen |
| Packet convention | one `R_k`-orbit is the full reduced-residue wheel; all `phi(P_k)` basepoints are retained as its cyclic parametrizations | frozen |
| Arithmetic relation | exact directed sieve update `E_k: G(P_k)->G(P_(k+1))`, with next prime read as `g_1+1` | source-backed |
| Symbolic lineage | prime/composite sieve -> gap cycles/admissibility -> sequential recursion -> fibre-cycle carrier | direct |
| Clock | `R` step count; a packet has period `phi(P_k)` | established, not prime-log clock |
| Repetition | `r` traversals take `r phi(P_k)` discrete steps | T2 established |
| Trace/operator | none frozen | T3 OPEN |
| Classical ASFS / Route A/B | no `(M,omega,F,tau)` | NOT APPLICABLE / NOT INVOKED |
