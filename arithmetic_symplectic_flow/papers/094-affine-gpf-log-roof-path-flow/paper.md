# An endogenous aggregate-log roof on the affine-GPF path-groupoid flow

**Paper ID:** 094-affine-gpf-log-roof-path-flow  
**Candidate ID:** ANG-20260914-AGPF02  
**Date / status:** 2026-09-14; BROADENED T0–T3 ESTABLISHED  
**Route state:** Broadened audit only; formal Route A unassigned; Route B NOT INVOKED.

## New frozen object

Use the affine-GPF two-sided path space and shift of 087, but do not reuse its unit roof. This candidate has the separate roof `tau(z)=log(gpf(z_0+1))`. It is one formula applied to the same edge output that defines every path; no prime list, per-prime parameter, or prescribed `log p` label is introduced.

| Item | Owner | Status |
| --- | --- | --- |
| Carrier/action | affine-GPF path space and shift | frozen |
| Arithmetic edge rule | `gpf(z_0+1)` | frozen |
| Roof | log of that output | frozen and distinct from 087 |
| Packet/repetitions | unique two-phase packet from 084 | exact |
| Zeta | same roof and packet | exact |

## Clock and zeta calculation

The primitive packet has edge outputs `gpf(2+1)=3` and `gpf(3+1)=2`. Therefore its time is `log 3 + log 2 = log 6`, while its r-fold traversal has time `r log 6`. As 087's complete ledger has only this oriented primitive packet, its roofed orbit zeta is

`log zeta(s) = sum_(r>=1) 6^(-r s)/r`, so `zeta(s)=(1-6^(-s))^(-1)` for `Re(s)>0`.

This is an aggregate clock. It neither assigns a separate orbit to every prime nor recovers an Euler product over primes.

## Broadened audit

| Audit | Result | Status |
| --- | --- | --- |
| T0 | path groupoid, shift, and roof frozen together | established |
| T1 | fixed factor rule plus aggregate map-output log roof | established |
| T2 | one primitive two-packet and r-fold convention | established |
| T3 | zeta uses that exact packet and roof | established |
| Classical P0/A0–A2 | no positive-dimensional symplectic base | NOT APPLICABLE |
| Route B | no Route-A readiness | NOT INVOKED |

## Decision

**Portfolio position: advance within broadened controls; fork for classical ASFS.** The discrete carrier, one finite packet, and absent Hénon/symplectic owner leave the original mission open.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [084 affine-GPF classification](../084-affine-gpf-two-cycle-control/paper.md)
- [087 distinct unit-roof path flow](../087-affine-gpf-path-groupoid-flow/paper.md)
- [081 GPF-Fibonacci log-roof control](../081-gpf-log-roof-path-flow/paper.md)
