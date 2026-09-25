# Exact gap roofs turn every primorial wheel into a same-object closed flow packet

**Paper ID:** `032-primorial-gap-suspension-flow`  
**Candidate ID:** `AFC-20260914-PGS01`  
**Date / status:** `2026-09-14; T0–T3 ESTABLISHED AS A BROADENED PACKET CARRIER`  
**Route state:** `Classical Route A not applicable; Route B NOT INVOKED`

## Construction and lineage

Let `P_k=p_k#` and order `W_k=(Z/P_k Z)^times` cyclically. For the successor
`R_k`, give `a` the positive roof equal to the cyclic gap from `a` to `R_k(a)`.
Suspend `R_k` by this roof. The resulting `Y_k` is one oriented circle, and
`Y=disjoint_union_k Y_k` carries the translation suspension flow. The exact
sieve relation `E_k` remains part of the frozen carrier and reads
`p_(k+1)=g_1+1` from the present gap cycle.

This realizes the full required early lineage without a detached clock:

```text
prime/composite sieve -> gap-cycle symbolic admissibility -> sequential update
-> cyclic packets -> roofed flow carrier.
```

## T0–T2

The roof is not selected after the fact. It is the cyclic gap word itself, and
the gaps make one full turn through the residue period. Consequently

```text
T(C_k)=sum_(a in W_k) tau_k(a)=P_k,
T(C_k^r)=rP_k.
```

There is one primitive oriented packet per `k`; its `phi(P_k)` basepoints are
kept as cyclic parametrizations. This avoids both a terminal-wheel choice and
the false multiplication of one packet into `phi(P_k)` prime orbits.

## Same-object zeta

With that primitive convention the natural packet zeta is

```text
Z_P(s)=product_(k>=1) (1-exp(-s P_k))^(-1).
```

For `Re(s)=sigma>0`, `P_k>=2^k`; therefore the associated log series
`sum_(k,r) exp(-sigma rP_k)/r` converges absolutely. This is a same-object T3
calculation for the frozen roofed packets, not a Fredholm determinant, a global
continuation claim, or a Riemann-zeta identification.

## Boundary and decision

The carrier is a discrete union of roofed circle packets, not a finite
dimensional symplectic base map. Its intrinsic actions are `P_k`, not `log p`.
Thus it is a broadened `advance` result only; it does not pass classical A0–A2
or invoke Route B. The next legitimate test is whether a non-arbitrary
geometric/conservative realization can retain *this exact roof, packet count,
and zeta*, rather than replacing them with a Hénon control.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence](evidence/README.md)
