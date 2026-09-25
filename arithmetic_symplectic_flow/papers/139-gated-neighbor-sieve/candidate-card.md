# Broadened carrier card — ANG-20260914-GNS01

**Version:** 1, 2026-09-14; frozen before mathematical audit or computation.  
**Initial status:** BROADENED HYPOTHESIS — T0--T3 OPEN.

Let X={0,1}^{N_{>=2}} with product topology and arithmetic over F_2.
Use the exact same divisor source expression

\[
G(y)_n=\prod_{\substack{2\leq d\leq\lfloor\sqrt n\rfloor\\d\mid n}}(1-y_d).
\]

Empty products are one. For the reflected ghost coordinate set y_1=y_2.
Freeze the nonlinear spatial feedback and full map

\[
L(y)_n=(y_{n-1}+y_n)(y_{n+1}+y_n)\quad(n\geq2),
\qquad R(x,y)=(y,x+G(y)+L(y)).
\]

In particular L(y)_2=0. No parameter sweep, cutoff, or later boundary
change is permitted for this card.

| Field | Frozen specification |
| --- | --- |
| Lineage | Prime/composite divisor exclusion -> reversible two-register deformation -> state-gated bidirectional spatial feedback |
| New architecture assumption | Unlike 138's additive neighbor term, dependence on the higher neighbor is gated by the current left difference; audit whether removing unconditional right-permutativity changes the packet obstruction |
| Carrier / proposed groupoid | Full X squared, exactly R, transformation groupoid by Z if invertibility is proved |
| Arithmetic data | Integer divisibility and coordinate-neighbor relation only; no selected primes or mask input |
| Diagnostic seed / observable | (0,0); both integer-labelled registers; no carrier restriction to this orbit |
| Roof / flow | Unit roof, ((x,y),1) identified with (R(x,y),0) |
| Packet convention | All least positive full R-periods modulo cyclic phase; retain complete multiplicity and r-fold same-clock repetitions |
| Arithmetic target | Source-derived prime-side readout belonging to an intrinsic packet; arbitrary cycles elsewhere are insufficient |
| Analytic owner | Ordinary unweighted orbit product only if packet audit warrants it; operators, spaces and trace OPEN |
| Controls | G removed, G constant, and 138's additive feedback, each a distinct comparison object |
| Planned first checks | Full inverse/continuity; source first outputs; exact period-4 constraints, followed only if informative by period-8 constraints or a finite contradiction certificate |
| Computational scope | At most coordinates 2 through 16 for finite temporal constraints; higher boundary variables left free, not set to zero. Satisfiability never proves a full infinite periodic point |
| Stop budget | One bounded audit, not a Boolean-rule search. If arithmetic packet remains non-testable after these checks, record OPEN/scoped stop and move to a different architecture |
| Classical / later lift | Finite-dimensional symplectic fields NOT APPLICABLE; Hamiltonian/contact/quantum owner NOT SUPPLIED |
| Route | Broadened T0--T3 only; formal Route coordinates UNASSIGNED; Route B NOT INVOKED |

This is one deliberately bounded nonlinear-feedback fork, not a continuation
of 138's identity or claims. A different Boolean rule, selected periodic
subsystem, or changed roof would require a fresh card.

## Audit append — version 1 unchanged, 2026-09-14

**Current status:** STOP / FORK — PRIME READOUT AND REVERSIBILITY PROVED; PERIOD 4 EXCLUDED; PERIOD 8 OPEN AT THE SEARCH CAP.

The exact full R is a homeomorphism; the full transformation groupoid and
unit-roof suspension retain that owner. Two steps from the uniform zero seed
give the complete prime indicator as the second register. The coordinate-2
recurrence forces every full period to be divisible by four. Exhaustive
period-four constraints become inconsistent at coordinate eight independently
of the higher boundary. The planned period-eight check reaches its predeclared
100000-prefix cap during equation nine, so its full satisfiability remains
OPEN. No variant sweep or period-higher-than-eight search was performed.

T0 is ESTABLISHED; T1 and T2 are PARTIAL / OPEN; T3 is OPEN / NOT CONSTRUCTED.
No arithmetic-carrying closed packet is established. Classical Route
coordinates remain UNASSIGNED and Route B NOT INVOKED. The decision is a
bounded research stop, not a theorem of global nonperiodicity. See the
[paper](paper.md), [claim ledger](claim-ledger.md), and
[exact evidence](evidence/computation.md).
