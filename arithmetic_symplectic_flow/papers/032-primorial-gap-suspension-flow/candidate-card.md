# Broadened candidate card — `AFC-20260914-PGS01`, version 1

| Field | Frozen definition / owner | State |
| --- | --- | --- |
| Base packets | `W_k=(Z/P_k Z)^times`, cyclically ordered, `P_k=p_k#` | frozen |
| Base return | `R_k(a)=next_k(a)` | frozen |
| Roof | `tau_k(a)=next_k(a)-a` cyclically, the corresponding gap in `G(P_k)` | frozen positive |
| Suspension | `Y_k=(W_k x [0,tau_k(a)]) / ((a,tau_k(a))~(R_k(a),0))`; `Y=disjoint_union_k Y_k` | frozen |
| Flow | translation in suspension coordinate on each `Y_k` | frozen |
| Arithmetic relation | directed exact sieve updates `E_k:G(P_k)->G(P_(k+1))`, next prime read as `g_1+1` | source-backed |
| Primitive packet | one oriented circle `C_k=Y_k`; basepoints are cyclic parametrizations, not distinct packets | frozen |
| Clock / repetition | `T(C_k)=sum_a tau_k(a)=P_k`; `T(C_k^r)=rP_k` | T1/T2 established |
| Zeta | `Z_P(s)=product_k(1-e^(-sP_k))^(-1)`, `Re(s)>0` | T3 established locally |
| Classical ASFS / Route | no symplectic base | NOT APPLICABLE / NOT INVOKED |
