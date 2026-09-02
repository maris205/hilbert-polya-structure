# Paper plan

## Claim--evidence matrix

| paper claim | proof owner | executable owner |
|---|---|---|
| legal firing is a quotient weak-order ascent | root-sign and parabolic-coset lemma | checker reconstructs roots, Weyl group and `W^J` |
| every play reaches one terminal element | unique maximum `w_0w_J` of `W^J` | checker constructs the complete quotient path DAG |
| common length is `|Phi^+|-|Phi_J^+|` | inversion lengths of `w_0` and `w_J` | positive-root and longest-element reconstruction |
| strict, wall and zero faces | specialize `J=empty`, proper `J`, and `J=I` | exact A/B/C/D/G2 strict, wall and zero cases |
| reducible and rank-one faces | direct-product factorization | `A2+A1`, positive `A1`, and zero `A1` cases |
| implementation convention | coordinate reflection formula | producer/checker/SymPy/replay/mutation gates |

No figure is needed: the decisive structure is an exact theorem and a compact
claim--evidence table, not a spatial or statistical relationship.

## Round 0 -- finite owner and strict chamber

Freeze the Cartan/coordinate/product conventions, prove the reflection-sign
lemma, and close the strictly dominant case: every play is a reduced word for
`w_0` and has `|Phi^+|` moves.

## Round 1 -- parabolic walls and every degenerate face

Add the quotient `W^J`, prove that legal edges stay in it, identify its unique
maximum `w_0w_J`, and derive the exact parabolic length loss.  Add zero,
disconnected, rank-one, and strict-positive-rule boundaries, plus the explicit
finite-type stopping firewall.

## Round 2 -- independent reconstruction and release audit

Add the 23-case/3332-branch executable certificate, producer-independent
root/Weyl reconstruction, symbolic controls, dual fresh-path replay, repaired-
hash mutations, classical-owner source audit, internal collision scan, and the
strict all-fail Route-A disposition.

The paper remains a finite Coxeter combinatorial-dynamics theorem in every
round.  Reduced terminating words are never relabelled as periodic orbits or
arithmetic primes.
