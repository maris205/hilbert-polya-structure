# MIP hostile gate — internal P1--P166 collision audit

**Date:** 2026-09-03 UTC  
**Result:** no literal duplicate or proof-complete transfer found;
`GREEN_OWNER_THIN / HOLD_EXTERNAL`

## 1. Audit method and inventory boundary

The comparison coordinates were carrier, literal update, first invariant
image, component/clock mechanism, recurrent classification, inverse/fibre
mechanism, and exact restriction or conjugacy.  Shared nouns such as
"height", "fibre", "Bell", "involution", "functional graph", or "zeta"
were assigned zero separation value and zero contribution value.

The on-disk scan found 161 numbered directories with 160 distinct numerical
identifiers through P166: P96 has two historical directories and P51--P56
have no numbered directory.  The latter six were checked through the
historical occupancy records: countable finite-memory shadowing,
one-forbidden-word SFTs, synchronized spoke codes, uniform word morphisms,
probabilistic finite automata, and irreducible-SFT finite covers.  Batch
Stage-2 reports were read across P57--P166, followed by direct inspection of
the closest paper READMEs/main sources.  The current directory-list digest
used by this audit was
`890e9025e3f0aba32a69447b0f0fa7507e1af74c9f092cc662c6b7a2d6707570`.

The candidate signature used throughout was:

```text
carrier:       all endofunction words [n]^[n]
update:        value i -> least source position carrying i, else i
first image:   off-diagonal-injective functional digraphs, with a stricter
               target-product support test
dynamics:      cycle inversion plus endpoint-tested path reversal/splitting
clock:         2n-2 on the carrier, 2n-3 on the first image
recurrence:    sets of cycles and endpoint-descent paths; periods 1 or 2
inverse:       optional fixed symbols + opened-first-position product
maximum fibre: Bell B_n, via kernel partitions over the identity
```

## 2. Exhaustive range comparison

| occupied range | mechanisms checked | collision decision |
|---|---|---|
| P1--P43 | incidence/Fredholm, tensor, holonomy, affine-semigroup, arithmetic and verifier obstruction systems | no finite endofunction least-section self-map |
| P44--P50 | q-adic finite boundaries, lattice/operator spectra, carry-free Schatten, transient tree shifts, affine-divisibility Toeplitz systems | no kernel-transversal or first-position iteration |
| P51--P56 | historical shift shadowing, forbidden words, spoke codes, morphisms, probabilistic automata, finite covers | different infinite/symbolic carriers and proof engines; no literal restriction |
| P57--P76 | CA minorization, SFT periodic realization, entropy and language systems, substitutions, group/matroid and higher-rank shift constraints | no endofunction carrier; periodic data alone is generic |
| P77--P96 | automatic towers, sandpile translations, random contexts/stacks, majority and traffic CA, algebraic shifts, subset expansion | no least-preimage selector; P80/P90 zeta and period-two silhouettes transfer no proof |
| P97--P106 | sumset squaring, torsion and lattice actions, digit erasure, random clamps, group-algebra norms, adjugates, random cocycles, cycle-minimum pruning, graph polarity | P105 is the only close minimum/involution silhouette and is separated below |
| P107--P116 | annihilator powers, capped Fibonacci, nilpotent-image subspaces, cyclic partition joins, word area, tournament updates, hooks, rooted peeling, Cartier chains, max-plus products | P110/P114/P115 are close generic Bell/path/component neighbors only |
| P117--P126 | run and fringe reversal, mex, commutators, stochastic coalescence, record blocks, graph component complementation, ideals, quadratic shear, composition splitting | reversals and period two occur on incompatible carriers; no kernel-section inverse |
| P127--P136 | parity transpose, polynomial GCD erosion, pile coalescence, crossing components, Euclidean queues, prefix majority, Pratt divisors, KMP borders, centralizers, random covers | P134 recomputes word border arrays, not symbol first positions; its factorial fibre and `2n-4` clock do not transfer |
| P137--P146 | rank feedback, palindromic XOR, Lyndon starts, stochastic majority/MIS, Boolean row inclusion, Dyck merging, orientation push, triangulation deletion | P143 is the nearest relation/retraction neighbor and is separated below |
| P147--P156 | run consolidation, tree contraction, peak extraction, Lyness, first passage, triangular books, finite-plane maps, normalizers, permutation extraction | P154--P156 share graph signatures or block extrema only; no literal/conjugate map |
| P157--P166 | Hensel lifting, cut intersection, odd-vertex pruning, Ferrers stripping, orthocentre windows, random translation intersection, shadows, equality feedback, code shortening, Hamming-weight translation | P166 has the same set-sized word carrier but incompatible graph invariants; see below |

## 3. Focused hostile comparisons

### P105 — cycle-minimum pruning

P105 acts on permutations and removes the least label from each nontrivial
cycle, making it fixed.  Its height is longest-cycle minus one, recurrence is
identity only, and its one-step fibres use threshold matchings.  MIP instead
acts on all endofunctions.  On the permutation slice it is simply
`f -> f^(-1)`, so it neither prunes nor changes rank and has tail zero.

The involution number occurs in both packages but in different places:
P105 obtains it as the identity indegree, whereas MIP obtains it as the number
of fixed *states*.  This standard sequence gives no separation credit and no
proof transfer.  P105 cannot yield MIP's path split, `2n-2` clock, recurrent
path species, or Bell identity fibre.

### P110 — cyclic shift--join partitions

P110 evolves a set partition by joining it with a cyclic translate.  MIP's
Bell bound also indexes sources by their kernel partitions, and its identity
fibre labels each block by its minimum.  That is a real shared static
mechanism and must be subtracted.  It is not a dynamic factor: two maps with
the same kernel partition but different block labels can have different MIP
images, while P110 sees only the partition.  P110's monotone lattice join,
coset endpoints, `n-2` clock, and Möbius--Bell basins cannot produce MIP's
component reversals or target product.

### P114 and P115 — rooted peeling and generic functional components

P114 deletes leaves in rooted forests; P115 decomposes bounded Cartier
operators into finite nilpotent chains attached to periodic cores.  They own
generic rooted-path clocks, component products, attached-tree language, and
fibre bookkeeping in the internal portfolio.  MIP's image components are
paths because off-diagonal values are injective, but they reverse and split
according to endpoint *label inequalities* rather than peel by graph depth
or shift along coefficient chains.  Neither pointwise update nor inverse
grammar transfers.

### P143 — Boolean row-inclusion residual

P143 replaces a Boolean relation by inclusion among row supports and retracts
to preorder-transpose dynamics.  If an endofunction is embedded as a Boolean
matrix with one `1` per row, P143 records equality/inclusion of singleton row
supports; it discards the least positions inside kernel blocks.  MIP instead
chooses those ordered representatives and retains block labels through the
codomain coordinate.  P143's quotient-poset induced-embedding fibres do not
specialize to the optional-present/first-open product, and MIP is not a
restriction, quotient, transpose, or relabelling of P143.

### P154--P156 — graph signatures and permutation extraction

P154 classifies unlabelled functional graphs arising from dihedral subgroup
normalizers, but its states are subgroups and its binary inverse forests are
arithmetic.  P155 orders permutation-cycle supports by their minima, reads
their maxima, and standardizes; P156 retains weak-excedance letters.  MIP's
least elements belong to *kernel fibres* of an arbitrary endofunction, not to
permutation cycles, and it keeps ambient rank `n`.  On permutations MIP is
inversion, while P155/P156 generally shorten and standardize.  Thus the
block-minimum vocabulary is shared but no dynamic transfer exists.

### P166 — Hamming-weight translation on the same ambient word set

After identifying `[n]` with `Z/nZ`, P166 and MIP both have `n^n` states.
P166 applies one common modular translation determined by Hamming weight;
MIP replaces coordinates by ordered first-preimage positions.  Their
conjugacy invariants already disagree at `n=3`: MIP has eight recurrent
states and carrier height four, whereas P166's phase system has a different
recurrent census and sharp height `n-2=1`.  P166's occupancy-phase/Stirling
inverse grammar cannot yield MIP's path inequalities or Bell kernel
partition injection.

### DFJ negative control — same carrier, already killed

The unnumbered degree-feedback-jump scout also acts on endofunctions.  Its
closed slices are ordinary power maps: the permutation slice is squaring and
uniform-leaf lifts realize fixed powers, with arbitrary periods.  MIP's
permutation slice is inversion and the complete recurrent system has period
at most two.  DFJ has no stable every-target inverse formula, while MIP's
product is exact.  DFJ remains a permanent kill and supplies no MIP theorem;
conversely, carrier reuse alone does not clear MIP's external owner risk.

## 4. KRR relation attack

For `e_f(j)=M(f)(f(j))`, direct algebra gives

```text
e_f(j)=the least member of the ker(f) block containing j,
e_f^2=e_f,                 ker(e_f)=ker(f).
```

This kernel-representative retraction is classical transversal structure.
It is not the iterated map `f -> M(f)`: it changes the coordinate domain from
symbols to positions through composition with the *old* `f`, and it is
idempotent immediately.  Treating KRR as a second dynamics would therefore
collapse the result to a definition-level retraction.  The paper-worthy
residual, if retained, must stay on literal iteration of `M`.

## 5. Collision verdict

No numbered P1--P166 system is the literal MIP map, a restriction that still
contains its nonbijective theorem core, or a conjugate/factor that transfers
both its temporal and inverse axes.  The closest overlaps—least labels,
kernel/set partitions, path components, involutions, Bell numbers, and
finite-map zeta—are explicitly zero-credit ingredients.

This is an internal noncollision result only.  Because canonical kernel
transversals and first-occurrence partition encodings are externally owned,
the correct gate is `GREEN_OWNER_THIN`, not an unqualified green light.
