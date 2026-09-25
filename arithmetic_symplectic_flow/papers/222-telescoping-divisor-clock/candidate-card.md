# Classical candidate card — ASFS-20260918-TDC01

**Version:** 1, 2026-09-18; frozen before the mathematical audit.  
**Initial status:** P0 HYPOTHESIS — endogenous telescoping clock, geometry,
and full periodic ledger OPEN.

## Frozen object

For each integer \(n\ge 2\), let

\[
 D_2=\{1\},\qquad D_n=\{2,3,\ldots,n-1\}\quad(n\ge3),
\]

with cyclic successor \(d^+=d+1\) for \(d<n-1\), \(d^+=2\) for
\(n\ge3,d=n-1\), and \(1^+=1\) in the empty-scan sentinel fibre \(n=2\).
The sentinel \(d=1\) performs no divisor test; it makes the empty scan for
2 a well-defined one-state carrier without inserting a prime-dependent
parameter.  Define

\[
 h(n,d)=\mathbf 1_{\{2\le d<n,\ d\mid n\}},
 \qquad
 \tau(n,d,q,p)=\log\!\frac{d+1}{d}.
\]

Freeze the full disconnected carrier and one map:

\[
 M=\coprod_{n\ge2,\ d\in D_n}\mathbb R^2_{n,d},
 \qquad \omega|_{\mathbb R^2_{n,d}}=dq\wedge dp,
\]
\[
 F(n,d,q,p)=
 \bigl(n,d^+,p,\;2p-q+(p-1)^2+h(n,d)\bigr).
\]

The candidate is the variable-roof suspension of this exact \(F\), with
endpoint gluing by \(F\) and roof \(\tau\).  No prime table, \(\log p\), von
Mangoldt weight, fitted parameter, or zero data is supplied.  The only
arithmetic operation is the local divisibility test in \(h\); the only clock
operation is the universal adjacent-integer ratio.

| P0 field | Frozen definition / obligation |
| --- | --- |
| Source lineage | Prime/composite divisor exclusion -> sequential symbolic scan -> positive-dimensional Hénon-form symplectic lift |
| Phase space | Full countable disjoint union of real planes above every \(n\ge2\) and every phase \(d\in D_n\) |
| Symplectic map | The displayed polynomial Hénon-form map; coefficient 2 is fixed before audit |
| Arithmetic action | One proper-divisor witness test per phase; no precomputed primality flag |
| Roof / flow | Positive universal \(\tau(n,d)=\log((d+1)/d)\); endpoint-glued variable-roof suspension of this same \(F\) |
| Clock hypothesis to audit | For \(p\ge3\), the complete scan has the frozen sum \(\sum_{d=2}^{p-1}\log((d+1)/d)=\log(p/2)\); the initially hoped-for \(\log p\) target is a falsifiable obligation, not an input. The sentinel has \(\tau(2,1)=\log2\) |
| Primitive convention | All intrinsic least-period full states modulo cyclic phase, all transverse coordinates and all integer fibres retained before classification; oriented flow orbits |
| Repetition law | \(r\)-fold traversal of one primitive flow orbit has time \(rT\); no prime powers are identified with map repeats |
| Non-Zeno obligation | Prove accumulated roof diverges in both directions on every full orbit; for fixed \(n\), use the finite positive minimum over \(D_n\) |
| Analytic owner | NOT SUPPLIED before the full ledger; any zeta/operator must use this map, roof, multiplicity and normalization |
| Controls | Unit-roof 145-style comparator; replace \(h\) by zero or block-cardinality force; compare the \(d=1\) empty-scan convention; check all noncentral states |
| PROVES_TOO_MUCH | Exact telescoping is a universal phase identity, but source selectivity and Hénon coefficients remain design choices; natural A0 and a trace owner are not automatic |
| Stop/fork | Stop if global inverse, completeness, or full periodic ledger fails; after the clock audit, retain only the actual offset-clock ledger and audit A0 naturalness separately |
| Later owner / Route | Hamiltonian/contact/quantum DEFERRED; formal Route coordinates UNASSIGNED; Route B NOT INVOKED |

This is a new candidate, not a repair of 145: its phase set has one phase for
each individual divisor test rather than a dyadic batch, and its roof is part
of the frozen object rather than the unit roof.  Any change to the sentinel,
force, phase set, or roof creates a new candidate ID.

## Appended audit outcome — version-1 object unchanged

**Status:** STOP — TELESCOPING ROOF HAS THE OFFSET \(\log 2\); NO PRIME-LOG CLOCK.

The frozen scan begins at \(d=2\), so for every prime \(p\ge3\)
\[
\sum_{d=2}^{p-1}\log\frac{d+1}{d}=\log\frac p2,
\]
not \(\log p\).  The map is still a global symplectomorphism, the full
periodic ledger is prime-only, and the variable roof is complete, but the
candidate fails the exact prime-log clock obligation.  The \(p=2\) sentinel
has length \(\log2\) and does not remove the offset for larger primes.
The candidate is retained as a precise positive control and stopped for the
Riemann-target clock.  Adding a \(d=1\) phase would be a new candidate, not a
repair of this object.
