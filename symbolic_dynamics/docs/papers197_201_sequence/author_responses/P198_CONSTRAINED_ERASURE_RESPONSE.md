# P198 author response: complete constrained-erasure reduction

Date: 2026-09-05 UTC. This is a bounded author response to the independent
Review A concern, not an independent review or an acceptance decision.
The Round0 manuscript, source, bibliography, verifier and frozen PDF are
unchanged. External status remains HOLD_EXTERNAL.

## 1. The stronger representation is correct

Let n=2m+1 and let S be the monomer set of a cycle matching. S is nonempty
and has odd cardinality. Every clockwise gap between successive monomers
has odd length, because its internal vertices are tiled by dimers. Conversely,
any nonempty subset S with all clockwise gaps odd determines one and only
one matching: tile the even interior of each gap. The singleton case has
one gap of length n and the same unique reconstruction. Thus this is a
bijection on the entire state space, not only a quotient or a core factor.

Write D(S)=S without its least element, with D(empty)=empty. In monomer
coordinates the literal CMM update is

```text
F(S)=D^2(S)                if |S|>=3,
F({a})={a+2 mod n}         if |S|=1.
```

Deleting the first two monomers preserves admissibility: the new cyclic
gap is a sum of three odd gaps. The recurrent splice on singletons is an
ordinary n-cycle. Hence the full transient dynamics is two least-element
erasures restricted to the odd-gap carrier, followed by a singleton rotor.

## 2. The proposed inverse engine becomes filtered insertion

Let U be an admissible target with least label u and greatest label v.
Because U has odd cardinality and successive ordinary gaps are odd,
u and v have the same parity. Any transient source must have the form
U union {a,b} with a<b<u: these are the two erased least elements.

The unchanged target gaps are already admissible. The three replaced gaps
are v to a across the cut, a to b, and b to u. Since n is odd, all three
are odd precisely when

```text
a ≡ u (mod 2),       b not≡ u (mod 2),       a<b<u.
```

This is the ordinary two-step deletion source set, intersected with the
admissible parity-gap carrier. For u=2r, choose a among 0,2,...,2r−2 and
b among the larger odd labels below u. There are r+(r−1)+...+1=T_r
choices. For u=2r+1, choose a among 1,3,...,2r−1 and b among the larger
even labels below u, giving the same T_r. The target singleton receives
one additional rotor predecessor, disjoint by cardinality. These are
exactly all Round0 fibre formulas, source sets, support conditions and
maximal-fibre consequences.

The target-prefix dimer intervals are therefore another encoding of this
parity-filtered insertion count. Their correctness does not demonstrate
a materially independent inverse engine.

## 3. Bounded historical evidence and author position

The author reread P100's main.tex, Sections 1–3: binary least-valuation
erasure is exactly least-element deletion and is explicitly credited to
Wegner. The author also reread
docs/papers132_136_sequence/replacement_scout/combinatorial/SCOUT.md,
Section 5.1 and Section 6. HF1 states the full delete-maximum element
source sets and binomial all-time counts; order reversal gives D. At
time two, a nonempty target's sources are exactly arbitrary two-element
insertions below its least label. The parity conditions above only filter
that known source set. HF1's separate powerset lift is not being falsely
identified with CMM.

No exact literal assertion that the unrestricted P100 system is globally
conjugate to CMM is justified: the carrier restriction and recurrent
splice are real. Nor did this bounded rereading locate an earlier paper
stating the identical odd-gap rule. Those distinctions are not sufficient
to retain the note under the central mechanism threshold. The author
currently has no nontransferring theorem or materially different inverse
mechanism after the complete reduction.

Accordingly the objection is likely fatal for independent-paper admission,
despite correct formulas and successful exact checks. The author does not
request a pass based on rotor period, larger enumeration, different
terminology or the previously issued five-seat freeze. The independent
reviewer and root should record the actual decision; a Critical finding
can reopen the slot. No frozen artifact is silently edited or erased.
