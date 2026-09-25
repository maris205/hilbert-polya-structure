# P0 candidate card — `ASFS-20260913-SHL01` v1.0

**State:** `STOPPED AT A0 AFTER STRICT AUDIT`

Let \(Q=\mathbb R^3\), with coordinates \((q,x,y)\), choose fixed constants
\(u_c=1.543689\ldots\), \(c>0\), and define
\[
a(q)=u_c-\frac{c}{\log^2(e+q^2)},\qquad
g(q,x,y)=(q+1,\;1-a(q)x^2-y,\;x).
\]
The Hénon part is invertible, so \(g\) is a diffeomorphism of \(Q\). Set
\(M=T^*Q\), \(\omega=dq\wedge dp_q+dx\wedge dp_x+dy\wedge dp_y\), and
let \(F=T^*g\) be the cotangent lift. Thus \(F\) is a specified symplectomorphism. Set \(\tau\equiv1\), define the usual mapping torus and translation suspension, and use the canonical Liouville volume normalization only where finite-volume statements are actually needed (`OPEN` here). The roof is positive and non-Zeno.

| Field | Owner / state |
| --- | --- |
| Lineage | Prior-work Papers 1–5: prime-symbolic sieve proposal → non-autonomous quadratic schedule → area-preserving Hénon bridge → symplectic lift. |
| Arithmetic proposal | The schedule was intended to retain the prior-work prime-density/symbolic deformation; strict audit found no map-internal arithmetic observable or derivation. |
| Allowed data | \(u_c,c\), formula for \(a(q)\), and the displayed map only; no primes, \(\log p\), von Mangoldt weights, or target zeros. |
| Orbit convention | Since \(q\mapsto q+1\), this frozen map has no periodic points on \(Q\); no A1 credit is possible unless a new candidate changes the object. |
| Operator / determinant | `OPEN; NOT CONSTRUCTED`. |
| Route state | A0 `SCOPED FAIL`; A1 `SCOPED FAIL AT PRECHECK`; A2 `NOT EVALUATED`; Route B `NOT INVOKED`. |

Changing the schedule, compactifying the clock, quotienting the clock, or importing a periodic-orbit carrier requires a new ID.
