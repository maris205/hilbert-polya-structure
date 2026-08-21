# C97 theorem package

Let `G_eff` be the faithful order-1920 permutation group on the sixteen C88
labels.  Its induced target action sends `H_i` to `gH_i`; on ordered pairs it
acts diagonally by `g(i,j)=(gi,gj)`.

## Theorem

1. The diagonal action partitions all 400 ordered target pairs into 272
   orbits, with orbit-size spectrum `144 x 1 + 128 x 2` and stabilizer-order
   spectrum `144 x 1920 + 128 x 960`.
2. Each orbit has one fixed C88 relation type.  The orbit spectrum is 16
   diagonal, 62 forward-comparable, 62 reverse-comparable, and 132
   incomparable orbits.
3. The complete C90 payload for `(T_i,T_j)` is constant on every ordered-pair
   orbit.  This includes all 289 joint-survival cells, all mixed raw moments
   through bidegree `(6,6)`, and covariance.
4. Pair transposition induces an involution on the 272 orbits, with 20
   self-transpose orbits.
5. Burnside's finite orbit count is exact:

   ```text
   sum_{g in G_eff} Fix_targets(g)^2 = 522240 = 1920 * 272.
   ```

6. Projection to either coordinate recovers exactly the sixteen C93
   single-target orbits.

## Proof certificate

The producer selects the unique maximal-order hit target as each support's
exact closure.  The independent checker instead identifies the support hit
vector with a column of the C88 inclusion matrix.  Both decoders induce the
same target permutations from the five named label generators.  Generator
equivariance gives the full generated action.  Direct orbit enumeration then
proves the partition, while byte-canonical digests of C90 joint payloads prove
law transport.  Orbit--stabilizer, the fixed-point sum, and the transpose
lookup give the remaining statements.

All statements concern the frozen finite model.  No arithmetic/local data,
Euler factors, root numbers, automorphy, full Burnside ring/table of marks, or
Hilbert--Polya operator is claimed.
