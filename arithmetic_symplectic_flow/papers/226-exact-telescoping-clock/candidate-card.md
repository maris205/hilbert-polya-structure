# Classical candidate card — ASFS-20260918-ETC01

**Version:** 1, 2026-09-18; frozen before the mathematical audit.  
**Initial status:** P0 FROZEN — exact telescoping clock, full symplectic
ledger, and analytic boundary OPEN.

## Frozen object

For every integer $n\ge 2$, use the full phase set

\[
D_n=\{1,2,\ldots,n-1\}.
\]

The cyclic successor is $d^+=d+1$ when $d<n-1$, and $d^+=1$ at
$d=n-1$.  In particular $D_2=\{1\}$ and $1^+=1$.  Define the local
divisor witness

\[
h(n,1)=0,\qquad h(n,d)=\mathbf 1_{\{d\mid n\}}\quad(2\le d<n),
\]

and the positive phase roof

\[
\tau(n,d,q,p)=\log\!\frac{d+1}{d}.
\]

Freeze the full disconnected carrier and one map:

\[
M=\coprod_{n\ge2,\,d\in D_n}\mathbb R^2_{n,d},
\qquad \omega|_{\mathbb R^2_{n,d}}=dq\wedge dp,
\]
\[
F(n,d,q,p)=
\bigl(n,d^+,p,\;2p-q+(p-1)^2+h(n,d)\bigr).
\]

The candidate is the endpoint-glued variable-roof suspension of this same
$F$:

\[
M_\tau=\{(z,t):z\in M,\ 0\le t\le\tau(z)\}/
((z,\tau(z))\sim(Fz,0)),
\]

with translation flow.  No prime table, manually assigned $\log p$, von
Mangoldt weight, Riemann-zero data, or fitted per-prime parameter is allowed.

## P0 ownership ledger

| P0 field | Frozen definition / obligation |
| --- | --- |
| Candidate relation | New phase carrier relative to 222; no theorem, credit, or status is inherited silently |
| Source lineage | Prime/composite divisor exclusion -> sequential symbolic scan -> positive-dimensional Hénon-form symplectic lift |
| Phase space | Full countable disjoint union of real planes above every $n\ge2$ and every phase $1\le d<n$ |
| Symplectic map | The displayed polynomial Hénon-form map; coefficient 2 is fixed before audit |
| Arithmetic action | One local divisibility test at every phase $d\ge2$; phase $d=1$ is a neutral initialization interval |
| Roof / flow | Universal adjacent-integer ratio on every integer/phase state; endpoint-glued suspension above the same $F$ |
| Clock hypothesis | For prime $p$, all witnesses vanish and the complete phase sum is $\sum_{d=1}^{p-1}\log((d+1)/d)=\log p$ |
| Periodic convention | All intrinsic least-period full states modulo cyclic phase, retaining every integer fibre and all $q,p\in\mathbb R$ before classification |
| Repetition law | An $r$-fold traversal of one primitive oriented flow orbit has time $rT$; no new orbit is created by relabelling a repeat |
| Non-Zeno obligation | Prove an orbit-wise positive floor from the finite phase set at fixed conserved $n$, in both time directions |
| Analytic owner | Not supplied at freeze; any later object must use this $F$, this roof, this ledger and its normalization |
| Controls | 222/160 adjacent-ratio engineered-clock comparator; unit-roof comparator; zero-witness and altered-force controls; all-state and sentinel checks; unipotent-monodromy trace warning |
| Source naturalness | OPEN: exact telescoping is endogenous once the phase scan is frozen, but the phase convention and quadratic force are design choices |
| Future lift owner | Hamiltonian/contact/quantum DEFERRED |
| Route state | A0/A1/A2 to be audited for this ID; formal Route coordinates UNASSIGNED; Route B NOT INVOKED |

## Immediate boundaries and stop rules

This candidate is not 222 with a repaired sentence.  Its phase set is changed
from the earlier divisor-test-only convention to all $d=1,\ldots,n-1$, so it
has its own ID, card, proof, controls and evidence record.  The adjacent-ratio
roof mechanism is also present in the earlier source-geometric-return-clock
control [160](../160-source-geometric-return-clock/README.md); 226 must therefore
record it as a duplicated engineered timing mechanism, not as a new natural
clock discovery.

Stop or fork if any of the following occurs: the displayed map is not globally
invertible; the full periodic ledger contains non-prime packets or omitted
continuous families; the roof is not complete; a determinant or trace requires
a different owner; or the claimed clock relies on a prime-selected domain.

The candidate card does not assert A0, A1, A2, a transfer operator, a Fredholm
determinant, a trace formula, a Route result, a quantum object, or a Riemann-zero
statement.  Unknown fields remain OPEN until the paper audit below supplies
candidate-specific evidence.
