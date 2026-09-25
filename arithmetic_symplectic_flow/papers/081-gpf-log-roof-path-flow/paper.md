<!-- PSR01 CORRECTION NOTICE START -->
> **2026-09-19 superseding correction — ANG-20260914-GPF02.**
> Current status: **CORRECTED FULL LEDGER — PRIME LOG CIRCLES PLUS MIXED PACKET; NATURAL CLOCK NOT ESTABLISHED**.
> The unchanged full path space and log-output roof give one primitive of time log p per prime AND one primitive of time log 210. The full ordinary product is zeta(s)/(1−210^(−s)) on Re s>1. The old only-one-packet, absent-per-prime and full-single-factor claims below are WITHDRAWN. The supplied log readout is not a proof of natural physical time; the extra packet cannot be deleted.
> See the [complete correction and proof](../266-prime-source-return-rescreen/paper.md).
> Full carrier, action, roof and same-object identity are preserved;
> formal coordinates UNASSIGNED, Route B NOT INVOKED.
>
> **Historical text retained below; superseded claims must not be used.**
<!-- PSR01 CORRECTION NOTICE END -->

# A map-internal logarithmic roof on the GPF path flow yields log(210), not a prime-by-prime clock

**Paper ID:** 081-gpf-log-roof-path-flow  
**Record ID:** ANG-20260914-GPF02  
**Date / status:** 2026-09-14; BROADENED T0–T3 ESTABLISHED  
**Classical Route state:** NOT APPLICABLE; Route B NOT INVOKED.

## New frozen object

079 used the two-sided path carrier X_G of the GPF map with unit roof. The roof
is part of the one-object identity, so the following is a fresh broadened
candidate:

\[
\tau(z)=\log\!\bigl(\operatorname{gpf}(x_0+y_0)\bigr),
\qquad z_0=(x_0,y_0)\in\mathbb N_{>0}^2.
\]

This is well-defined and positive because x_0+y_0 >= 2 and its greatest prime
factor is at least two. It is not a per-prime schedule: the single universal
formula reads the arithmetic output already used by the fixed GPF update at
every path edge.

The carrier, action, and path convention are otherwise exactly stated anew here:

\[
X_G=\{(z_j)_{j\in\mathbb Z}:z_{j+1}=G(z_j)\},
\qquad \sigma(z)_j=z_{j+1},
\]

with G(x,y)=(y,gpf(x+y)), and the roofed path suspension identifies
(z,tau(z)) with (sigma z,0).

## Exact packet clock

The unique primitive path packet follows the phase cycle

\[
(7,3)\to(3,5)\to(5,2)\to(2,7)\to(7,3).
\]

The successive GPF outputs, hence roof values, are 5,2,7,3. Therefore

\[
T_\gamma=\log5+\log2+\log7+\log3=\log210,
\qquad
T_{\gamma^r}=r\log210.
\]

All four phases are one oriented primitive packet, not four packets. The
clock has an endogenous logarithmic form but aggregates all four selected
primes into one period. It cannot be reinterpreted as a family p -> gamma_p
with T_(gamma_p)=log p.

## Same-object zeta

There is one primitive packet, so the roofed suspension product is

\[
\zeta_{\mathrm{GPF},\log}(s)
=\left(1-e^{-s\log210}\right)^{-1}
=\left(1-210^{-s}\right)^{-1},
\qquad \operatorname{Re}s>0.
\]

This product uses the same GPF carrier, shift, roof, primitive packet, and
repetition convention. It has no claimed relation to the Riemann zeta function,
its Euler factors, zero set, or explicit formula.

| Broadened audit | Result |
| --- | --- |
| T0 carrier/type and ownership | established |
| T1 endogenous arithmetic / clock | established gpf-derived aggregate log roof |
| T2 packet and repetition | established: one packet, r log 210 |
| T3 same-object zeta | established for Re(s)>0 |
| per-prime clock / prime powers | scoped FAIL / absent |
| classical ASFS P0--A2 | NOT APPLICABLE |
| Route B | NOT INVOKED |

## Controls and decision

- Replacing tau by one, log(x_0+y_0), or a manually supplied prime-time list
  would define another object. No conclusion is transferred from 079 or to it.
- The formula is endogenous but its finite packet is too small to encode the
  prime distribution. The positive result is only a same-object aggregate
  arithmetic clock.
- The carrier remains a type-labelled path/groupoid object; no finite-dimensional
  symplectic or Hénon owner has been constructed.

**Portfolio position: advance as a broadened clock control; fork for a
prime-resolved carrier.** A successor must retain endogenous roof ownership
while producing a non-preselected family of primitive packets rather than
collapsing its entire arithmetic rule into log 210.

## Evidence index

- [078 GPF-Fibonacci A0/A1 control](../078-gpf-fibonacci-a0-a1-control/paper.md)
- [079 unit-roof GPF path flow](../079-gpf-path-groupoid-flow/paper.md) — comparator only; distinct roof and candidate ID.
- [081 evidence boundary](evidence/README.md)
