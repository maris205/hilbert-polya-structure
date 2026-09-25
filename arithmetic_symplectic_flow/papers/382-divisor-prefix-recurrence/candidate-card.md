# Frozen card — divisor-prefix recurrence histories

Candidate `ANG-20260922-DPR01`; batch `FULL-TRANSPORT-20260922-G`, round3/5.
2026-09-22. Status `FROZEN; SOURCE CLOSURE / TRANSPORT / TARGET OPEN`.

## Full recurrence and own measure

S={(a,b) positive integers:gcd(a,b)=1}; D(a,b)={d>=1:d divides a+b}.
Each actual labelled edge d sends (a,b) to (b,(a+b)/d). Check closure.
X consists of ALL infinite legal state-and-edge paths from EVERY s in S,
with discrete-product Borel structure; T deletes the first edge/state.
No terminal paths, truncation, chosen recurrent core or state quotient.
eta(a,b)=2^(-a-b)/C, C=sum_S2^(-a-b), P_s(d)=1/|D(s)|.
mu is the resulting probability on FULL X with initial eta and these edge
transitions. State positive support, atoms and stationarity honestly.
Lineage: exact divisibility/compositeness -> prefix-dependent legal divisor
choices -> sequential integer-pair evolution and possible arithmetic return.
The pair is the whole history state: this remains countable Markov, not
proved non-free-block or an infinite-memory escape. Naturalness OPEN.

## Actual inverses, full-point version and decisive tests

For target state(b,c), proposed incoming edges have source(dc-b,b),
d>=1, dc>b, gcd(d,b)=1. Check sufficiency, necessity and ALL branches.
For each edge f:s->t prescribe j_f(y)=eta(s)/(|D(s)|eta(t)) on ALL X_t.
Prove every-Borel IMAGE, finite-history identity, positivity and full support.
If admitted kappa=-log j, retained-lag G={(z,m-n,y):T^m z=T^n y},
c=A_m(z)-A_n(y). Local kappa may be signed; do not claim a positive roof.
Prove descent/composition, full orbit/incoming ledger, source isotropy,
clock/lag kernels/intersection, full-height extension isotropy and H,
all primitive closed state-edge necklaces, phases and repeated traversals.
Do not count only cycles based at(1,1), or replace H by an arbitrary period.
First test the d=2 self-edge at(1,1), and the exact closed walk
(1,1)--1-->(1,2)--3-->(2,1)--3-->(1,1).
Target each positive primitive log p, at most one packet per p. A wrong
primitive/multiplicity stops; no rescaling or removal of a bad incoming path.

## Three own controls

NO-DIVISION: same coprime S, only d=1.
END-DIVISORS: same S, allowed d in {1,a+b}.
ALL-PAIRS: all positive integer pairs, all d dividing a+b, no coprime test.
Each uses its OWN normalized eta=2^(-a-b)/C, uniform legal-edge rule,
FULL path carrier, inverse domains, all-point j and physical ledger.
For ALL-PAIRS rederive inverse conditions without importing gcd(d,b)=1.
No control supplies missing MAIN fields. Full source nonreturn, if found,
is distinct from an undefined clock or a positive primitive target failure.

## Integrity and release

Definition scout knows previous stack results through shared history; no
blindness, cross-model or external-review claim. ARS CP1 first, separate
card-only raw before paper unlock, CP2/CP3; NOT_CALIBRATED.
Broadened measured path groupoid; classical A0/A1/A2 NOT APPLICABLE;
formal UNASSIGNED; B NOT INVOKED; T3 NOT AUDITED. Exact Markdown only.

## Outcome — 2026-09-22

Candidate ANG-20260922-DPR01.
Outcome: `OWNED DIVISOR CLOCK; COMPOSITE PRIMITIVE PACKET — STOP / FORK`
The preceding 55 lines are the unchanged pre-audit freeze.
The [main proof](paper.md) establishes closure, the exhaustive inverse list,
the full-support atomless probability and its nonstationarity. Every actual
inverse chart has the prescribed positive finite every-point/every-Borel
IMAGE; the resulting local clock is signed, not a positive classical roof.
The entire retained-lag groupoid, all three kernels, source/extension
isotropy, closed-necklace packets, incoming histories and height phases
remain. Closed words have L=log product_i |D(s_i)|.

The self-edge at (1,1) has q=1 and H=(log2)Z. The precommitted three-step
word has least source period 3 and ENTIRE H=(log8)Z: it is a separate
primitive packet, not a repeat of the self-edge packet. Thus the fixed
prime-time target stops; no rescaling or packet deletion is used.
NO-DIVISION independently owns an atomic measure and clock but no nonzero
returns. END-DIVISORS owns its log2/log8 packets; ALL-PAIRS retains every
positive pair, removes the inverse gcd test, and also has primitive log4.
Each control uses its own law and complete incoming/phase ledger.

Strong naturalness OPEN; T3 NOT AUDITED; classical A0/A1/A2 NOT APPLICABLE;
formal UNASSIGNED; B NOT INVOKED. This is still countable Markov, not an
infinite-memory escape or universal history no-go. Method: exact cylinder,
integer-product and full-orbit proofs; no scientific numerics or finite census.
See [overview](README.md) and [claim ledger](claim-ledger.md).
