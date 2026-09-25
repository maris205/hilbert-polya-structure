# Frozen card — coprime exchange heap histories

Candidate `ANG-20260922-CEH01`; batch `FULL-TRANSPORT-20260922-G`, round2/5.
2026-09-22. Status `FROZEN; FULL TRANSPORT AND TARGET OPEN`.

## Source, arithmetic and law

A={2,3,...}; H=A*/~ under only uabv~ubav when gcd(a,b)=1. States are
actual finite-word equivalence classes, not chosen word representatives.
e is empty; L(h)={g:h=[a]g for some a}; R(h)={g:h=g[a] for some a}.
Both sets use actual distinct quotient states. Prove the needed cancellation,
finiteness and enumeration, not by invoking an unproved normal-form theorem.
rho(a)=1/[a(a-1)]. pi is the pushforward of word sampling: length n has
probability2^(-n-1), independent rho letters. All finite heaps retained.
At nonempty h, with probability1/2 right-multiply by rho-distributed [a],
and with probability1/2 choose uniformly a distinct element of L(h).
At e only right-multiply. Merge probabilities only if target states coincide;
P(h,g) is the resulting transition probability, not a hidden labelled edge.
X is ALL infinite legal state paths from ALL finite heaps; T deletes h_0.
mu([h_0,...,h_n])=pi(h_0)product_(i<n)P(h_i,h_(i+1)).
No infinite initial heaps, conull deletion or selected starting root.
Arithmetic lineage: common-divisor observable determines which symbols may
cross older symbols and become actual deletable left factors. This is not
377's stack-top deletion, but still a countable Markov lift, not an assumed
escape from closed-walk splicing. Strong naturalness OPEN.

## Entire inverse and physical ledger

All predecessors of a path with first state h must be enumerated; proposed
list R(h) union {[a]h:a>=2}, deduplicated by actual state. Verify exactly.
For any actual predecessor c, freeze j_c(y)=pi(c)P(c,h)/pi(h) on all X_h.
Prove full-support probability, atom status and every-Borel IMAGE, including
all null paths; no stationarity is presumed. kappa(z)=-log j_(z_0)(Tz)
may have either sign. G={(z,m-n,y):T^m z=T^n y}, c=A_m(z)-A_n(y),
with all integer lags retained; prove descent and finite-history identities.
For full X times R / G give source incoming/orbits, entire source isotropy,
clock/lag kernels and intersection, extension isotropy, full H, primitive
closed packets, all phases and repetitions. Finite closed state walks need
not visit e; no deletion of another communicating component is allowed.
First inspect e->[2]->e and then an actual commuting-letters closed walk.
Target each positive primitive log p, at most one packet per p; a wrong
primitive or multiplicity forces STOP, no probability/clock tuning.

## Three independent controls

FREE-WORD: no exchanges. COMMUTATIVE: all distinct letters exchange.
NONCOPRIME: distinct letters exchange iff gcd(a,b)>1.
For EACH define its own quotient H,L,R, word-pushforward pi, transitions P,
full path source, law, all-point j and whole groupoid/packet ledger by the
same recipe. Own state classes matter, not MAIN's pi or branching counts.
These test source interaction; identical short-loop failure is still a
negative control, not evidence of arithmetic naturalness.

## Release and limits

Definition scout read375summary and selected lineage paragraphs, not377card;
root knows the stack comparison. No external novelty/nonconjugacy claim.
ARS CP1 before mathematics; card-only raw freeze before manuscript unlock;
CP2/CP3 internal shared-history NOT_CALIBRATED, inherited session model.
Broadened Borel/groupoid only; classical A0/A1/A2 NOT APPLICABLE;
formal UNASSIGNED; B NOT INVOKED; T3 NOT AUDITED. Exact Markdown only.

## Appended outcome — original 61-line contract preserved

Candidate `ANG-20260922-CEH01`.
Outcome: `OWNED HEAP IMAGE CLOCK; COMPOSITE PRIMITIVE TIMES — STOP / FORK`

The [main proof](paper.md) directly proves dependence-poset representation,
cancellation, distinct minimal/maximal-node deletion counts and the exhaustive
predecessor list. The word-pushforward probability and each actual transition
give a full-support nonatomic path law and every-Borel IMAGE. The frozen branch
densities are the unique continuous versions on their whole actual domains.
The source law is nonstationary and the local clock is signed; no positive
roof or invariant physical-flow measure is inferred.

All finite-history IMAGE identities, full clock/lag kernels and intersection,
source/extension isotropy, H, incoming histories, phases and primitive
closed-state-walk packets are classified. Walks need not visit the empty heap;
different actual state necklaces and equal-time packets are not identified.

The first packet e->[2]->e has entire H=(log4)Z. The actual MAIN exchange
packet e->[2]->[23]=[32]->[2]->e has entire H=(log192)Z. More generally
every nonempty closed walk of these four frozen recipes has a composite integer
multiplier, since every actual positive P is an even integer's reciprocal.
This scoped all-walk conclusion is not a no-go for other Markov laws.

Each of FREE-WORD, COMMUTATIVE and NONCOPRIME owns its own quotient counts,
probability, transitions, IMAGE and full packet ledger. None rescues MAIN.
The same-object ledger is intact: no selected root, omitted closed walk,
probability adjustment, clock rescaling or borrowed operator.
Strong naturalness OPEN; countable Markov splicing is not claimed absent.
See the [claim ledger](claim-ledger.md). T3 NOT AUDITED; classical A0/A1/A2
NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED. Any fork requires a fresh card.
