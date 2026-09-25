# Clock-fork card — ASFS-20260915-DRC01

Version 1, 2026-09-15. Frozen before the non-Zeno audit.
Initial P0 clock/completeness OPEN.

For every n>=2 define K_n=max(1,floor(log_2(n-1))), cyclic k, and
b(n,k)=sum_{2^k<=d<2^{k+1}, d<n}1_{d|n}. On all real planes set

\[
f_{n,k}(q)=q+\tfrac12\tanh q+K_n b(n,k),\quad
F(n,k,q,p)=(n,k^+,f_{n,k}(q),p/f'_{n,k}(q)),
\quad\omega=dq\wedge dp.
\]

The new roof, fixed before testing, is

\[
\tau(n,k,q,p)=\log f'_{n,k}(q)
=\log\bigl(1+\tfrac12\operatorname{sech}^2q\bigr).
\]

This is not the unit roof of 147. It is proposed as a derivative-generated
time and must receive a fresh full-state completeness audit.

| Field | Frozen scope |
| --- | --- |
| Source lineage | Same displayed local divisor-witness action, now paired with its intrinsic configuration derivative observable |
| Allowed data | All n and all real coordinates; no prime-selected domain or inserted prime-log formula |
| Mapping torus proposal | Endpoint gluing with the displayed positive smooth tau, only a complete flow if accumulated times are proved divergent in both directions |
| Early test | Follow a noncentral n=2 configuration q>0 with any momentum; bound its growth and the sum of derivative roofs |
| Primitive ledger | Full base cycles and all other states retained; existence of closed prime packets cannot excuse finite-time escape elsewhere |
| Analytic owner | NOT EVALUATED before clock gate; no old unit-roof determinant or trace transfers |
| Controls | Unit roof as a separate complete comparator; central prime cycle versus escaping full states; pointwise positivity versus uniform lower bound |
| Stop | A single full-state finite accumulated return time disproves claimed global completeness; no roof floor, cutoff or selected trapped set repair |
| Route | Owner-level completeness screen only; formal coordinates UNASSIGNED and Route B NOT INVOKED |

Adding a constant to tau, restricting to periodic centres or otherwise
changing the owner would require a new card; none is authorized by this card.

## Appended result — version-1 object unchanged

**Status:** STOP — POSITIVE DERIVATIVE ROOF HAS FINITE-TIME ESCAPE.

The [paper](paper.md) proves that for n=2 and every q_0>0,
q_j>=q_0+cj with c=(1/2)tanh q_0>0, while the roof sum is bounded by
2 exp(-2q_0)/(1-exp(-2c)). A continuous observable on the actual
endpoint-glued space diverges along this finite-time trajectory, so there
is no endpoint or complete continuation within the frozen carrier.

The roof is smooth and strictly positive, but not uniformly bounded below.
Central prime cycles retain sums r K_p log(3/2) as a partial control only.
The candidate stops at P0 clock/completeness: no A0--A2 advancement,
operator result or unit-roof credit is transferred. Formal coordinates
remain UNASSIGNED and Route B NOT INVOKED. No floor, carrier restriction
or compactification was introduced.
