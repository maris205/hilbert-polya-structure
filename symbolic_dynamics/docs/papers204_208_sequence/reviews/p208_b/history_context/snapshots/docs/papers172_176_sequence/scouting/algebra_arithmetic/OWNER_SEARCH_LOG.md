# Bounded owner search for A01, A03, and A16

Search date: 2026-09-03.  Status: `HOLD_EXTERNAL`.

This log is a preliminary owner subtraction, not a novelty certificate or a
freedom-to-operate review.  The internal P1--P171 corpus was searched first,
because a local literal or proof-engine collision kills a candidate even when
an external exact-title search is empty.  External conclusions below use
primary records: author arXiv pages, DOI/publisher metadata, and publisher
pages.

## Search protocol

Local queries combined literal update strings and mechanism terms, including

```text
gcd(f,f')
derivative gcd square-free Yun Musser
fixed commutator centralizer coset twisted coboundary Engel
subspace meet Frobenius semilattice orbit fold
translation gcd sliding intersection
```

Bounded external queries included variants of

```text
Frobenius intersection subspace lattice dynamics
iterate subspace intersection Frobenius finite field
commutator map fixed transposition functional graph symmetric group
fixed points conjugators transposition support overlap
fixed element commutator permutation fixed points
derivative gcd iteration finite field polynomial fibres
```

Crossref and arXiv exact-phrase/top-result probes were used as discovery
checks.  The exact A01 arXiv probes returned no records; exact A16 phrases
likewise returned no records.  Crossref top-five results for those phrases did
not state either literal finite map.  These are deliberately reported only as
bounded non-hits.

## A01: Frobenius-meet subspaces

### Primary background located

L. Brickman and P. A. Fillmore,
[*The Invariant Subspace Lattice of a Linear
Transformation*](https://doi.org/10.4153/CJM-1967-075-4), *Canadian Journal
of Mathematics* 19 (1967), 810--822.

This is relevant owner background for the invariant-subspace lattice of the
Frobenius linear transformation.  The present fixed-point count can also be
derived directly from the cyclic-module model
`F_q[X]/(X^m-1)`.  The source is not claimed to state the self-map
`U -> U cap F(U)` or its time-`t` fibres.

### Internal owners are decisive

- P110 iterates a lattice automorphism followed by join and uses orbit-fold
  stabilization plus Möbius basin inversion.
- P128 explicitly calls its translation--GCD sliding-window mechanism the
  order-dual semilattice orbit fold inherited from P110.
- A01's identity `M^t(U)=cap_{i=0}^t F^i(U)` and its full-subspace Möbius
  fibre formula are direct instances of those two tools.

**Assessment:** no literal external match was located in the bounded probes,
but the complete proposed conjunction is internally transferable.
`KILL_INTERNAL_P110_P128`.  The non-hit supplies no novelty evidence.

## A03: derivative--GCD erosion

### Direct primary owner

David Y. Y. Yun,
[*On square-free decomposition
algorithms*](https://doi.org/10.1145/800205.806320), SYMSAC 1976, 26--35;
the [IBM Research record](https://research.ibm.com/publications/on-square-free-decomposition-algorithms)
describes the square-free-decomposition setting and its relation to earlier
Horowitz/Musser algorithms.

Derivative--GCD repeated-factor extraction is therefore zero-credit
background even before the internal-repeat test.

### Exact internal repeats

- `docs/papers127_131_sequence/scouting/algebraic/SCOUT.md`, row `P03`, uses
  the literal update and already records characteristic-dependent tails
  `1,2,4`.
- `docs/papers152_156_sequence/scouting/algebraic/SCOUT.md`, row `PDG`, gives
  a multiplicity clock and every-target square-free inverse product.
- `docs/papers152_156_sequence/scouting/algebraic_replacement2/SCOUT.md`, row
  `SFE`, again uses the literal update.
- `docs/papers157_161_sequence/scouting/algebraic/SCOUT.md` gives the
  characteristic-`p` coordinate rule
  `e -> e-min(t,e mod p)` and target-fibre Euler products.
- `docs/papers162_166_sequence/phase1/CANDIDATE_POOL_AND_KILL_LEDGER.md`
  explicitly identifies `DGD` as the prior `PDG/SFE` map.

The current factor-degree generating functions are clean independent
checks, but they do not create a new system or theorem axis.

**Assessment:** `KILL_DIRECT_OWNER_REPEAT`.

## A16: fixed-transposition commutator

### Primary sources located

R. Brandl,
[*The commutator map*](https://doi.org/10.1017/CBO9780511600647.011), in
*Proceedings of Groups -- St Andrews 1985* (published 1987), 138--142.

This is broad direct background for commutator maps.  No assertion is made
here that Brandl states the fixed-transposition graph or the marked fibre
polynomial.

Jason Fulman,
[*Fixed points of non-uniform permutations and representation theory of the
symmetric group*](https://arxiv.org/abs/2406.12139), arXiv:2406.12139v2
(2024).

The author abstract explicitly includes the commutator of uniform `g` with
fixed `x` in `S_n` and studies the fixed-point distribution of the resulting
non-uniform permutation.  This is a close owner for output statistics.  The
current polynomial instead marks fixed points of `g` conditional on a
specified commutator target, so Fulman is not cited as a literal owner of that
formula.

### Internal owner

P119's literal system is a fixed-element commutator on a finite group.  It
writes the update as the twisted coboundary `g -> g^{-1}phi(g)` and proves
uniform fibres as centralizer cosets, then derives all iterated fibres and the
complete functional tree.  Replacing the regular unitriangular element by a
transposition changes the small image geometry but not the update type or the
fibre proof.

The proposed new mark factors as

```text
two-point endpoint polynomial × partial rencontres polynomial,
```

after the same centralizer-coset reduction.  It is an exact residual formula,
but not a second engine large enough to defeat the P119 transfer.

**Assessment:** `KILL_INTERNAL_P119_TRANSFER`.

## Claim-by-claim owner matrix

| Candidate claim | Closest owner/collision | Treatment |
|---|---|---|
| A01 sliding Frobenius intersection and invariant core | P110 semilattice orbit fold; P128 meet-dual sliding GCD | zero credit / internal kill |
| A01 invariant-subspace count | Brickman--Fillmore background; elementary cyclic-module divisor count | background, not novelty |
| A01 every-time fibre Möbius formula | generic subspace-lattice inversion; P110/P128 fibre/basin engine | exact but transferable |
| A03 exponent rule and repeated-factor stripping | Yun square-free decomposition; exact P127/P152/P157/P162 repeats | hard repeat kill |
| A03 factor-degree depth/fibre products | P152/P157 internal packages already contain the same programme | hard repeat kill |
| A16 fixed-element commutator and uniform fibres | P119; Brandl broad background | zero credit / internal kill |
| A16 fixed points of commutator output | Fulman 2024 close direct topic | must cite and subtract |
| A16 target-conditioned fixed points of conjugator | no literal formula found in bounded search | non-hit only; elementary residual does not clear P119 |

## Search ceiling

No database search here was citation-complete, and no full-text theorem-level
search of MathSciNet or zbMATH was available.  More searching cannot rescue
A03 or the internal P119 collision.  If a future policy reopens A01, it would
need a backward/forward citation chase from invariant-subspace lattices and a
literal search for meet-with-Frobenius operators before any external claim.
