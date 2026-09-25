# Claim ledger — DRC01

Candidate ID: ANG-20260923-DRC01.
Outcome: `OWNED CLOCK; PRIME-2 FIXED PACKET — BOUNDED OPEN / FORK`

This ledger refers only to the [frozen owner](candidate-card.md), [full proof](paper.md) and [package entry](README.md).

| Claim | Status and exact boundary | Evidence |
|---|---|---|
| Proper-divisor interface | PROVED: the full seed $(n,d,d^2)$ outputs $(d,d^2,dr)$; nondivisors and all other real states are retained. | Paper §1 |
| Every inverse and all-point IMAGE | PROVED separately for MAIN/Q/L, every Borel branch restriction and assigned floor face. MAIN/Q $J=1/\lvert u\rvert$; L $J=1$. | §§2–3 |
| Full actual groupoid | PROVED: every legal depth and inverse label, integer lag, clock and joint kernels, isotropy, entire $H$, extension and phases; terminal next-step clock NOT DEFINED. | §4 |
| Global fixed states | PROVED: MAIN only $(2,2,2)$; Q only $(1,1,1)$; L exactly $(t,t,t)$ for $0\le t<1$. | §5 |
| Frozen two-step cells | PROVED EMPTY for MAIN and each control, including rotation and all half-open faces; no other period-two assertion. | §6 |
| MAIN fixed packet | PROVED: full orbit is $(-1/2,-2,1)\to(-2,1,2)\to(1,2,2)\to(2,2,2)$ and its fixed loop. One packet, $H=(\log2)\mathbb Z$, full kernels/incoming/phases retained. | §7 |
| Control fixed packets | PROVED: every listed core has singleton incoming source orbit, full lag $\mathbb Z$, zero $H$ and retained extension isotropy. | §8 |
| Q entire return clock | PROVED zero $H$ for every source by finite cycle-product cancellation, not by zero one-step clock or a cycle census. | §4 |
| L entire clock | PROVED zero on all legal steps and arrows; full source/lag structure remains. | §4 |
| Global prime target | OPEN: MAIN nonempty positive ledger established, but every-positive-prime, global uniqueness and all-prime coverage are not settled. | §9 |
| Naturalness and later gates | Strong naturalness OPEN; arithmetic T1 NOT PASSED; T3 NOT AUDITED; classical NOT APPLICABLE; formal Route UNASSIGNED; B NOT INVOKED. | §§1,9 |

The same-object ledger is intact; control conclusions are not MAIN failure certificates. The scoped decision is BOUNDED OPEN / FORK, without tuning or a larger census.
AI-assisted design, derivation, drafting and internal workflow review are disclosed. Shared history is NOT_CALIBRATED; no human/external verification or external peer review is certified.
