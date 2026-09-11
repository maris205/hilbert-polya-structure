# Circular recency follow-up: genuine higher-alphabet recurrence

AUTHOR_DEDUCTIVE_FOLLOWUP / NO_PROMOTION. Proof author:
current_round_two_seats_scout. Only this file is new; DESK.md is unchanged.
No code, pilot, enumeration of a finite box, child, Git, central edit or
count change. The single explicit word below is a symbolic counterexample
certificate, checked by its defining formula rather than a scientific run.

## Main answer

Higher-alphabet recurrent orbits exist. In fact, for every k>=1 there is
a word using all k symbols whose recency transform is its cyclic shift.
For k=3, the word

    w = 3312331323221

has exact R-period 13. Thus no theorem saying that every orbit eventually
uses at most two symbols can be true. A full classification of arbitrary
recurrent words or transients is still not supplied by this follow-up.

Throughout, S is left rotation: (Sw)_i=w_{i+1}, with cyclic indices.
R is exactly the circular recency-rank map defined in DESK.md. The
definition immediately gives RS=SR and invariance under injective
renaming of input symbols. No renaming of OUTPUT ranks is performed.

## 1. Complete fixed-point statement

The only fixed word in [q]^n is 1^n. Indeed, DESK's maximum-rank argument
shows max R(w)=number of distinct symbols in w. If R(w)=w and that number
is h, then the support must be [h]. If h>1, the word contains a 1.
At any position i with w_i=1, equality R(w)_i=1 forces w_{i-1}=w_i=1:
zero distinct symbols between consecutive occurrences means adjacency.
Repeat this implication backwards round the circle; every symbol is 1,
contradicting h>1. Finally R(1^n)=1^n directly.

This proves fixed points only. It does not imply fixation of all orbits.

## 2. An auxiliary bijection constructs traveling recurrent words

Let B_k act on pairs (a,L), where a is in [k] and L is a permutation list
of [k]. If a has position r in L, set

    B_k(a,L) = (r, move-to-front(a,L)).

This is a bijection. For a target (b,G), let a be G's first entry and
obtain L by removing that entry and reinserting it in position b. Then
a has position b in L, and applying B_k returns (b,G). This supplies
the unique inverse. Thus every state lies on a cycle of length <= k*k!.

Take any cycle, write its states (a_i,L_i), with i modulo its least
period m, and let U be the symbols occurring among the a_i. Every used
symbol has been moved to the front during a full traversal; unused
symbols have not. Therefore at the end all used symbols precede all
unused symbols. Periodicity implies the same at the beginning. The used
prefix of each L_i is precisely the cyclic recency order immediately
before a_i: after a full period every used symbol has occurred, so its
last occurrence determines its rank, independently of older history.

Consequently the rank of a_i in L_i is R(a)_i. By the update rule it is
also a_{i+1}. Hence the cyclic word a_0...a_{m-1} satisfies R(a)=S(a).

Put h=|U|. Those ranks are at most h, so all a_i are in [h], by cyclic
indexing. Since there are h different a_i, U=[h]. In particular, a cycle
containing a state with a=k uses ALL k symbols. Such a cycle exists,
for example the one containing (k,(1,2,...,k)).

For this full-support cycle, the word has primitive cyclic length m.
If it had a smaller cyclic period d, its current letter and its complete
recency list would repeat after d; the pair state would then have period
d, contradicting minimality of m. Since R commutes with S,

    R^t(a)=S^t(a) for every t>=0.

Its exact R-period is therefore m. This proves: for each k>=1 there is
some k<=m<=k*k! and a full-support k-letter word of exact R-period m.
The proof does NOT assert a closed formula for m or a single cycle on
all full-support auxiliary states.

## 3. Explicit ternary obstruction, with a full local certificate

For w=3312331323221, the following table gives the previous occurrence
index and the SET of intervening symbols. Indices wrap modulo 13.

| i | w_i | Previous occurrence | Intervening distinct symbols | R(w)_i |
|---|---|---|---|---|
| 1 | 3 | 10 | {1,2} | 3 |
| 2 | 3 | 1 | empty | 1 |
| 3 | 1 | 13 | {3} | 2 |
| 4 | 2 | 12 | {1,3} | 3 |
| 5 | 3 | 2 | {1,2} | 3 |
| 6 | 3 | 5 | empty | 1 |
| 7 | 1 | 3 | {2,3} | 3 |
| 8 | 3 | 6 | {1} | 2 |
| 9 | 2 | 4 | {1,3} | 3 |
| 10 | 3 | 8 | {2} | 2 |
| 11 | 2 | 9 | {3} | 2 |
| 12 | 2 | 11 | empty | 1 |
| 13 | 1 | 7 | {2,3} | 3 |

Thus R(w)=3123313232213=Sw. As 13 is prime and w is nonconstant,
w has primitive cyclic length 13. The commutation identity proves its
exact dynamical period 13, with all three symbols present at every time.
Repeating w any positive number of times preserves all recency ranks,
so it gives exact period-13 examples at every length divisible by 13,
inside every ambient alphabet [q] with q>=3.

## 4. What the partition factor does and does not solve

Let Pi be the set of partitions of [n] into at most q nonempty blocks,
and let p(w) be the equality partition of a word. Let C(P) be the circular
recency-rank word obtained by giving the blocks of P distinct names.
Renaming invariance makes C well-defined. DESK's inverse argument proves
that C is injective. Define H=p composed with C on Pi. Then

    R=C composed with p,   H=p composed with C,
    R(C(P))=C(H(P)).

The restriction of R to its first image C(Pi) is therefore conjugate to
H. This is an exact factor/section reduction, not a solution of H's
orbits. In particular, H cannot be replaced by the mere block count;
the ternary example supplies a constant-three-block recurrent orbit.

For precision, if h_H(P) is the entrance time into the recurrent set of H,
then every NONRECURRENT word w satisfies

    h_R(w)=1+h_H(p(w)).

Indeed R^t(w)=C(H^{t-1}(p(w))) for t>=1, and C maps recurrent H-states
exactly to recurrent R-states. Recurrent words instead have h_R(w)=0.
This identity merely relocates the unsolved clock to the partition map;
it is not an evaluated general temporal theorem.

## Source/claim boundary and stop

The synchronized list/rank decoder is the classical primitive already
subtracted in DESK.md; the present auxiliary bijection and certificates
are explicit author deductions from it, not attributed to an unread source.
A bounded public search for the exact ternary word and the self-indexing
move-to-front description returned no exact-owner result; this is not
novelty clearance. General self-organizing-list/shuffle results returned
as neighboring search leads are NOT imported as dynamical classifications.

The binary restriction remains the old cyclic difference. The explicit
ternary orbit refutes eventual reduction to that binary restriction; it
does not rule out every conceivable linear encoding on a larger state
space. General periods, recurrent-set characterization and sharp entrance
times remain opaque. No all-state theorem contract or pilot is requested.
Native tool returns remain conversational evidence, not a new frozen raw
package. This follow-up answers the bounded recurrence question without
changing DESK.md, claiming independent review, or increasing any count.
